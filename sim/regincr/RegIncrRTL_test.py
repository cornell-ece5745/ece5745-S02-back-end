#=========================================================================
# RegIncr_test
#=========================================================================

from pymtl      import *
from pclib.test import run_test_vector_sim
from RegIncrRTL import RegIncrRTL

#-------------------------------------------------------------------------
# test_small
#-------------------------------------------------------------------------

def test_small( dump_vcd, test_verilog ):
  run_test_vector_sim( RegIncrRTL(), [
    ('in_   out*'),
    [ 0x00, '?'  ],
    [ 0x03, 0x01 ],
    [ 0x06, 0x04 ],
    [ 0x00, 0x07 ],
  ], dump_vcd, test_verilog )

#-------------------------------------------------------------------------
# test_large
#-------------------------------------------------------------------------

# ''' SECTION TASK '''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This test script is incomplete. As part of the section you will
# insert add a new test case for larger inputs.
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

