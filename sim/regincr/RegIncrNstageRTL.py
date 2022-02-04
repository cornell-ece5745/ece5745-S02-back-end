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
from pymtl3.passes.backends.verilog import *

class RegIncrNstageVRTL( VerilogPlaceholder, Component ):

  # Constructor
  def construct( s, nstages=2 ):

    # Port-based interface
    s.in_ = InPort  ( Bits8 )
    s.out = OutPort ( Bits8 )

    # If translated into Verilog, we use the explicit name

    s.set_metadata( VerilogTranslationPass.explicit_module_name,
                    f"RegIncr{nstages}stageRTL" )

# Import the appropriate version based on the rtl_language variable

if rtl_language == 'pymtl':
  from .RegIncrNstagePRTL import RegIncrNstagePRTL as RegIncrNstageRTL
elif rtl_language == 'verilog':
  RegIncrNstageRTL = RegIncrNstageVRTL
else:
  raise Exception("Invalid RTL language!")
