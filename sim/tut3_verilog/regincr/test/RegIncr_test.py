#=========================================================================
# RegIncr_test
#=========================================================================

from pymtl3 import *
from pymtl3.stdlib.test_utils import run_test_vector_sim
from tut3_verilog.regincr.RegIncr import RegIncr

#-------------------------------------------------------------------------
# test_small
#-------------------------------------------------------------------------

def test_small( cmdline_opts ):
  run_test_vector_sim( RegIncr(), [
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
  run_test_vector_sim( RegIncr(), [
    ('in_   out*'),
    [ 0xa0, '?'  ],
    [ 0xb3, 0xa1 ],
    [ 0xc6, 0xb4 ],
    [ 0x00, 0xc7 ],
  ], cmdline_opts )

# ''' TUTORIAL TASK ''''''''''''''''''''''''''''''''''''''''''''''''''''''
# This test script is incomplete. As part of the tutorial you will add
# another test case to test for overflow. Later you will add a test case
# for random testing.
# ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''\/

#-------------------------------------------------------------------------
# test_overflow
#-------------------------------------------------------------------------

def test_overflow( cmdline_opts ):
  run_test_vector_sim( RegIncr(), [
    ('in_   out*'),
    [ 0x00, '?'  ],
    [ 0xfe, 0x01 ],
    [ 0xff, 0xff ],
    [ 0x00, 0x00 ],
  ], cmdline_opts )

#-------------------------------------------------------------------------
# test_random
#-------------------------------------------------------------------------

import random

def test_random( cmdline_opts ):

  test_vector_table = [( 'in_', 'out*' )]
  last_result = '?'
  for i in range(20):
    rand_value = Bits8( random.randint(0,0xff) )
    test_vector_table.append( [ rand_value, last_result ] )
    last_result = Bits8( rand_value + 1, trunc_int=True )

  run_test_vector_sim( RegIncr(), test_vector_table, cmdline_opts )
