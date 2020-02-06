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

class RegIncrNstageVRTL( Component, Placeholder ):

  # Constructor
  def construct( s, nstages=2 ):

    # Port-based interface
    s.in_ = InPort  ( Bits8 )
    s.out = OutPort ( Bits8 )

    from os import path
    s.config_placeholder = VerilogPlaceholderConfigs(
      # The absolute path of the SVerilog file to be imported
      src_file = path.dirname(__file__) + '/RegIncrNstageVRTL.v',
      # What is the name of the top module to be imported?
      top_module = 'RegIncrNstageVRTL',
    )
    s.config_verilog_translate = TranslationConfigs(
      explicit_module_name = f'RegIncr{nstages}stageRTL',
    )

# Import the appropriate version based on the rtl_language variable

if rtl_language == 'pymtl':
  from .RegIncrNstagePRTL import RegIncrNstagePRTL as RegIncrNstageRTL
elif rtl_language == 'verilog':
  RegIncrNstageRTL = RegIncrNstageVRTL
else:
  raise Exception("Invalid RTL language!")
