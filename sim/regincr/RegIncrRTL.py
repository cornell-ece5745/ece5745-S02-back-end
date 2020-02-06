#=========================================================================
# Choose PyMTL or Verilog version
#=========================================================================
# Set this variable to 'pymtl' if you are using PyMTL for your RTL design
# (i.e., your design is in RegIncrPRTL) or set this variable to
# 'verilog' if you are using Verilog for your RTL design (i.e., your
# design is in RegIncrVRTL).

rtl_language = 'pymtl'

#-------------------------------------------------------------------------
# Do not edit below this line
#-------------------------------------------------------------------------

# This is the PyMTL wrapper for the corresponding Verilog RTL model.

from pymtl3 import *
from pymtl3.passes.backends.verilog import VerilogPlaceholderConfigs, TranslationConfigs

class RegIncrVRTL( Component, Placeholder ):

  # Constructor
  def construct( s ):

    # Port-based interface
    s.in_ = InPort  ( Bits8 )
    s.out = OutPort ( Bits8 )

    from os import path
    s.config_placeholder = VerilogPlaceholderConfigs(
      # The absolute path of the SVerilog file to be imported
      src_file = path.dirname(__file__) + '/RegIncrVRTL.v',
    )
    s.config_verilog_translate = TranslationConfigs(
      explicit_module_name = 'RegIncrRTL',
    )

# Import the appropriate version based on the rtl_language variable

if rtl_language == 'pymtl':
  from .RegIncrPRTL import RegIncrPRTL as RegIncrRTL
elif rtl_language == 'verilog':
  RegIncrRTL = RegIncrVRTL
else:
  raise Exception("Invalid RTL language!")
