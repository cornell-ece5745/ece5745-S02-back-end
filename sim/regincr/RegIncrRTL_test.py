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

def test_large( dump_vcd, test_verilog ):
  run_test_vector_sim( RegIncrRTL(), [
    ('in_   out*'),
    [ 0xa0, '?'  ],
    [ 0xb3, 0xa1 ],
    [ 0xc6, 0xb4 ],
    [ 0x00, 0xc7 ],
  ], dump_vcd, test_verilog )

