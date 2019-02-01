#=========================================================================
# Choose PyMTL or Verilog version
#=========================================================================
# Set this variable to 'pymtl' if you are using PyMTL for your RTL design
# (i.e., your design is in RegIncrPRTL) or set this variable to
# 'verilog' if you are using Verilog for your RTL design (i.e., your
# design is in RegIncrVRTL).

rtl_language = 'verilog'

#-------------------------------------------------------------------------
# Do not edit below this line
#-------------------------------------------------------------------------

# This is the PyMTL wrapper for the corresponding Verilog RTL model.

from pymtl import *

class RegIncrNstageVRTL( VerilogModel ):

  # Constructor

  def __init__( s, nstages=2 ):

    # Verilog module name

    s.explicit_modulename = "RegIncrNstageRTL_{}stage".format(nstages)

    # Port-based interface

    s.in_ = InPort  ( Bits(8) )
    s.out = OutPort ( Bits(8) )

    # Verilog parameters

    s.set_params({
      'p_nstages' : nstages,
    })

    # Verilog ports

    s.set_ports({
      'clk'   : s.clk,
      'reset' : s.reset,
      'in'    : s.in_,
      'out'   : s.out,
    })

  # Line tracing

  def line_trace( s ):
    return "{} () {}".format( s.in_, s.out )

# Import the appropriate version based on the rtl_language variable

if rtl_language == 'pymtl':
  from RegIncrNstagePRTL import RegIncrNstagePRTL as RegIncrNstageRTL
elif rtl_language == 'verilog':
  RegIncrNstageRTL = RegIncrNstageVRTL
else:
  raise Exception("Invalid RTL language!")

