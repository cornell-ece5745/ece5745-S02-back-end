#=========================================================================
# RegIncr_test
#=========================================================================

from pymtl3                   import *
from pymtl3.stdlib.test_utils import run_test_vector_sim
from .RegIncrRTL              import RegIncrRTL

#-------------------------------------------------------------------------
# test_small
#-------------------------------------------------------------------------

def test_small( cmdline_opts ):
  run_test_vector_sim( RegIncrRTL(), [
    ('in_   out*'),
    [ 0x00, '?'  ],
    [ 0x03, 0x01 ],
    [ 0x06, 0x04 ],
    [ 0x00, 0x07 ],
  ], cmdline_opts )

#-------------------------------------------------------------------------
# test_large
#-------------------------------------------------------------------------

def test_large( cmdline_opts ):
  run_test_vector_sim( RegIncrRTL(), [
    ('in_   out*'),
    [ 0xa0, '?'  ],
    [ 0xb3, 0xa1 ],
    [ 0xc6, 0xb4 ],
    [ 0x00, 0xc7 ],
  ], cmdline_opts )

