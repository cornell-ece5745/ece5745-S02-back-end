#=========================================================================
# RegIncrPRTL
#=========================================================================
# This is a simple model for a registered incrementer. An eight-bit value
# is read from the input port, registered, incremented by one, and
# finally written to the output port.

from pymtl3 import *
from pymtl3.passes.backends.sverilog import TranslationConfigs

class RegIncrPRTL( Component ):

  # Constructor

  def construct( s ):

    # Port-based interface

    s.in_ = InPort  ( Bits8 )
    s.out = OutPort ( Bits8 )

    # Sequential logic

    s.reg_out = Wire( Bits8 )

    @s.update_ff
    def block1():
      if s.reset:
        s.reg_out <<= b8(0)
      else:
        s.reg_out <<= s.in_

    # Combinational logic

    @s.update
    def block2():
      s.out = s.reg_out + b8(1)

    # Configuration

    s.config_sverilog_translate = TranslationConfigs(
      # Let --test-verilog option control whether we will translate PRTL
      translate = False,
      # What is the module name of the top level in the translated Verilog?
      explicit_module_name = 'RegIncrRTL',
    )

  def line_trace( s ):
    return f"{s.in_} ({s.reg_out}) {s.out}"

