#=========================================================================
# RegIncrPRTL
#=========================================================================
# This is a simple model for a registered incrementer. An eight-bit value
# is read from the input port, registered, incremented by one, and
# finally written to the output port.

from pymtl import *

class RegIncrPRTL( Model ):

  # Constructor

  def __init__( s ):

    # Port-based interface

    s.in_ = InPort  ( Bits(8) )
    s.out = OutPort ( Bits(8) )

    # Sequential logic

    s.reg_out = Wire( Bits(8) )

    @s.tick_rtl
    def block1():
      if s.reset:
        s.reg_out.next = 0
      else:
        s.reg_out.next = s.in_

    # ''' SECTION TASK '''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the section you will insert a
    # combinational concurrent block here to model the incrementer logic.
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

  def line_trace( s ):
    return "{} ({}) {}".format( s.in_, s.reg_out, s.out )

