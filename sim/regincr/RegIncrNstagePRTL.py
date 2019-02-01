#=========================================================================
# RegIncrNstagePRTL
#=========================================================================
# Registered incrementer that is parameterized by the number of stages.

from pymtl      import *
from RegIncrRTL import RegIncrRTL

class RegIncrNstagePRTL( Model ):

  # Constructor

  def __init__( s, nstages=2 ):

    # Verilog module name

    s.explicit_modulename = "RegIncrNstageRTL_{}stage".format(nstages)

    # Port-based interface

    s.in_ = InPort  (8)
    s.out = OutPort (8)

    # Instantiate the registered incrementers

    s.reg_incrs = [ RegIncrRTL() for x in xrange(nstages) ]

    # Connect input port to first reg_incr in chain

    s.connect( s.in_, s.reg_incrs[0].in_ )

    # ''' SECTION TASK '''''''''''''''''''''''''''''''''''''''''''''''''''
    # This model is incomplete. As part of the tutorial you will insert
    # code here to connect the stages together.
    # ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    # Connect last reg_incr in chain to output port

    s.connect( s.reg_incrs[-1].out, s.out )

  # Line tracing

  def line_trace( s ):
    return "{} ({}) {}".format(
      s.in_,
      '|'.join([ str(reg_incr.out) for reg_incr in s.reg_incrs ]),
      s.out
    )

