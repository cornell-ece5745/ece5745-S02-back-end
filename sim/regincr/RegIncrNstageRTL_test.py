#=========================================================================
# RegincrNstage_test
#=========================================================================

import collections
import pytest

from random import sample

from pymtl3                   import *
from pymtl3.stdlib.test_utils import run_test_vector_sim, mk_test_case_table
from .RegIncrNstageRTL        import RegIncrNstageRTL

#-------------------------------------------------------------------------
# mk_test_vector_table
#-------------------------------------------------------------------------

def mk_test_vector_table( nstages, inputs ):

  inputs.extend( [0]*nstages )

  test_vector_table = [ ('in_ out*') ]
  last_results = collections.deque( ['?']*nstages )
  for input_ in inputs:
    test_vector_table.append( [ input_, last_results.popleft() ] )
    last_results.append( b8(input_) + b8(nstages) )

  return test_vector_table

#-------------------------------------------------------------------------
# Parameterized Testing with Test Case Table
#-------------------------------------------------------------------------

test_case_table = mk_test_case_table([
  (                    "nstages inputs                "),
  [ "2stage_small",    2,       [ 0x00, 0x03, 0x06 ]   ],
  [ "2stage_large",    2,       [ 0xa0, 0xb3, 0xc6 ]   ],
  [ "2stage_overflow", 2,       [ 0x00, 0xfe, 0xff ]   ],
  [ "2stage_random",   2,       sample(range(0xff),20) ],
  [ "4stage_small",    4,       [ 0x00, 0x03, 0x06 ]   ],
  [ "4stage_large",    4,       [ 0xa0, 0xb3, 0xc6 ]   ],
  [ "4stage_overflow", 4,       [ 0x00, 0xfe, 0xff ]   ],
  [ "4stage_random",   4,       sample(range(0xff),20) ],
])

@pytest.mark.parametrize( **test_case_table )
def test( test_params, cmdline_opts ):
  nstages = test_params.nstages
  inputs  = test_params.inputs
  run_test_vector_sim( RegIncrNstageRTL( nstages ),
    mk_test_vector_table( nstages, inputs ),
    cmdline_opts )

#-------------------------------------------------------------------------
# Parameterized Testing of With nstages = [ 1, 2, 3, 4, 5, 6 ]
#-------------------------------------------------------------------------

@pytest.mark.parametrize( "n", [ 1, 2, 3, 4, 5, 6 ] )
def test_random( n, cmdline_opts ):
  run_test_vector_sim( RegIncrNstageRTL( nstages=n ),
    mk_test_vector_table( n, sample(range(0xff),20) ),
    cmdline_opts )

