#! /usr/bin/env python
#=========================================================================
# construct.py
#=========================================================================
# ECE5745 Session 02 with RegIncrs
#
# Author : Khalid Al-Hawaj
# Date   : January 31, 2020
#

import os
import sys

from mflowgen.components import Graph, Step

def construct():

  g = Graph()

  #-----------------------------------------------------------------------
  # Parameters
  #-----------------------------------------------------------------------

  adk_name = 'freepdk-45nm'
  adk_view = 'view-standard'

  parameters = {
    'construct_path' : __file__,
    'design_name'    : 'RegIncr4stageRTL',
    'clock_period'   : 2.0,
    'adk'            : adk_name,
    'adk_view'       : adk_view,
    'topographical'  : True,
  }

  #-----------------------------------------------------------------------
  # Create nodes
  #-----------------------------------------------------------------------

  this_dir = os.path.dirname( os.path.abspath( __file__ ) )

  # ADK step

  g.set_adk( adk_name )
  adk = g.get_adk_step()

  # Custom steps

  rtl = Step( this_dir + '/rtl' )

  # Default steps

  info         = Step( 'info',                          default=True )
  constraints  = Step( 'constraints',                   default=True )
  dc           = Step( 'synopsys-dc-synthesis',         default=True )
  iflow        = Step( 'cadence-innovus-flowsetup',     default=True )
  placeroute   = Step( 'cadence-innovus-place-route',   default=True )
  debugcalibre = Step( 'cadence-innovus-debug-calibre', default=True )

  #-----------------------------------------------------------------------
  # Graph -- Add nodes
  #-----------------------------------------------------------------------

  g.add_step( info         )
  g.add_step( rtl          )
  g.add_step( constraints  )
  g.add_step( dc           )
  g.add_step( iflow        )
  g.add_step( placeroute   )

  #-----------------------------------------------------------------------
  # Graph -- Add edges
  #-----------------------------------------------------------------------

  # Connect by name

  g.connect_by_name( rtl,         dc           )
  g.connect_by_name( adk,         dc           )
  g.connect_by_name( constraints, dc           )

  g.connect_by_name( adk,         iflow        )
  g.connect_by_name( dc,          iflow        )

  g.connect_by_name( adk,         placeroute   )
  g.connect_by_name( dc,          placeroute   )
  g.connect_by_name( iflow,       placeroute   )

  #-----------------------------------------------------------------------
  # Parameterize
  #-----------------------------------------------------------------------

  g.update_params( parameters )

  return g

if __name__ == '__main__':
  g = construct()
#  g.plot()

