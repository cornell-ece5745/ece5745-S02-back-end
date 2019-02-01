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

class RegIncrVRTL( VerilogModel ):

  # Constructor

  def __init__( s ):

    # Port-based interface

    s.in_ = InPort  ( Bits(8) )
    s.out = OutPort ( Bits(8) )

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
  from RegIncrPRTL import RegIncrPRTL as RegIncrRTL
elif rtl_language == 'verilog':
  RegIncrRTL = RegIncrVRTL
else:
  raise Exception("Invalid RTL language!")

