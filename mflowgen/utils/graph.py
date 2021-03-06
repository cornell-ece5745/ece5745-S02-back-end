#! /usr/bin/env python
#=========================================================================
# graph.py
#=========================================================================
# Takes a ninja DOT graph and outputs a new graph with per-tag subgraphs
#
#  -h --help     Display this message
#  -v --verbose  Verbose mode
#  -g --graph    Input DOT graph file
#  -o --output   Output DOT graph file
#  -t --tags     Comma-separated list of tags (each tag is a subgraph)
#
# Author : Christopher Torng
# Date   : June 3, 2019
#

from __future__ import print_function
import argparse
import re
import sys

#-------------------------------------------------------------------------
# Command line processing
#-------------------------------------------------------------------------

class ArgumentParserWithCustomError(argparse.ArgumentParser):
  def error( self, msg = "" ):
    if ( msg ): print("\n ERROR: %s" % msg)
    print("")
    file = open( sys.argv[0] )
    for ( lineno, line ) in enumerate( file ):
      if ( line[0] != '#' ): sys.exit(msg != "")
      if ( (lineno == 2) or (lineno >= 4) ): print( line[1:].rstrip("\n") )

def parse_cmdline():
  p = ArgumentParserWithCustomError( add_help=False )
  p.add_argument( "-v", "--verbose", action="store_true"            )
  p.add_argument( "-h", "--help",    action="store_true"            )
  p.add_argument( "-g", "--graph",   default=".graph.dot"           )
  p.add_argument( "-o", "--output",  default=".graph.subgraphs.dot" )
  p.add_argument( "-t", "--tags",    required=True                  )
  opts = p.parse_args()
  if opts.help: p.error()
  return opts

#-------------------------------------------------------------------------
# Helper functions
#-------------------------------------------------------------------------

# The subgraphs will be:
#
# - light gray background
# - labeled with the tag name (in blue, in big font)
#

subgraph_template_str = \
'''subgraph cluster_{num} {{
color="#cccccc"
fontsize=50
fontcolor=blue
style=filled
label="{label}"
{data}
}}
'''

def subgraph( num, label, data ):

  text = subgraph_template_str.format(
    num   = num,
    label = label,
    data  = data,
  )

  return text

#-------------------------------------------------------------------------
# Main
#-------------------------------------------------------------------------

def main():

  opts = parse_cmdline()
  tags = opts.tags.split(',')

  #-----------------------------------------------------------------------
  # Read the DOT graph
  #-----------------------------------------------------------------------

  with open( opts.graph, 'r' ) as fd:
    lines = fd.readlines()

  #-----------------------------------------------------------------------
  # Collect lines for subgraphs
  #-----------------------------------------------------------------------

  # For each tag, filter the dot file for related lines to form a subgraph

  subgraphs = {}

  for t in tags:

    # Filter for the tag ( with '-' and '_' as wildcards '.' )

    t_regex = t.replace( '-', '.' ).replace( '_', '.' )
    t_lines = [ l for l in lines if re.search( t_regex, l ) ]

    # Grab the dot IDs of these graph elements (first string in the line)

    t_dot_ids = [ l.split()[0] for l in t_lines ]

    # Do a second filter to find all graph elements that originate from
    # these dot IDs or edges that point to them

    t_lines = []

    for l in lines:
      tokens = l.split()
      # originates from this tag
      if tokens[0] in t_dot_ids:
        t_lines.append( l )
      # ends within this tag
      if len( tokens ) >= 3:
        if tokens[1] == '->' and tokens[2] in t_dot_ids:
          t_lines.append( l )

    # Aesthetics... make "execute" command labels pop out more

    for i, l in enumerate( t_lines ):
      execute_regex = t_regex + '.*commands_rule'
      if re.search( execute_regex, l ):
        l_new      = l.rstrip()[:-1] # chop off the ']' char
        l_new      = l_new + ', fontsize=25, penwidth=10, color=blue]\n'
        t_lines[i] = l_new

    # Save these lines for this subgraph

    subgraphs[t] = t_lines

  #-----------------------------------------------------------------------
  # Aesthetics
  #-----------------------------------------------------------------------
  # Make any arrows that connect two subgraphs together pop out more

  # Gather dot IDs that originate from (src) or end in (dst) a subgraph

  src_dot_ids = {}
  dst_dot_ids = {}

  for t in tags:
    src_dot_ids[t] = []
    dst_dot_ids[t] = []
    for l in subgraphs[t]:
      tokens = l.split()
      if len( tokens ) >= 3 and tokens[1] == '->':
        src = tokens[0]
        dst = tokens[2]
        src_dot_ids[t].append( src )
        dst_dot_ids[t].append( dst )

  # Go through each subgraph and search for a dst dot ID that is in
  # another subgraph

  for t in tags:
    other_tags = [ _ for _ in tags if _ is not t ]
    for ot in other_tags:
      # We have a pair of subgraphs now (t, ot)
      for idx, l in enumerate( subgraphs[t] ):
        tokens = l.split()
        if len( tokens ) >= 3 and tokens[1] == '->':
          dst = tokens[2]
          if dst in src_dot_ids[ot]:
            # Found an edge that crosses subgraphs..
            l_new = l.rstrip() + \
              ' [arrowhead=normal, penwidth=4, arrowsize=4, color=red]\n'
            subgraphs[t][idx] = l_new

  #-----------------------------------------------------------------------
  # Dump graph
  #-----------------------------------------------------------------------

  # Filter for all remaining non-tag lines to put at the end

  all_subgraph_lines = sum( subgraphs.values(), list() )

  other_lines = [ l for l in lines if l not in all_subgraph_lines ]

  # Dump the output graph dot file
  #
  # - all subgraphs are dumped after the first line where the graph opens
  #

  with open( opts.output, 'w' ) as fd:

    fd.write( other_lines[0] )

    for i, t in enumerate( tags ):
      data = ''.join( subgraphs[t] ).strip()
      fd.write( subgraph( i, t, data ) )

    for l in other_lines[1:]:
      fd.write( l )

main()

