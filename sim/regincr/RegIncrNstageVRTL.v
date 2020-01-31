//========================================================================
// RegIncrNstageVRTL
//========================================================================
// Registered incrementer that is parameterized by the number of stages.

`ifndef REG_INCR_NSTAGE_V
`define REG_INCR_NSTAGE_V

`include "regincr/RegIncrVRTL.v"

module RegIncrNstageVRTL
#(
  parameter nstages = 2
)(
  input  logic       clk,
  input  logic       reset,
  input  logic [7:0] in_,
  output logic [7:0] out
);

  // This defines an _array_ of signals. There are p_nstages+1 signals
  // and each signal is 8 bits wide. We will use this array of signals to
  // hold the output of each registered incrementer stage.

  logic [7:0] reg_incr_out [nstages+1];

  // Connect the input port of the module to the first signal in the
  // reg_incr_out signal array.

  assign reg_incr_out[0] = in_;

  // ''' SECTION TASK ''''''''''''''''''''''''''''''''''''''''''''''''''''
  // This model is incomplete. As part of the tutorial you will insert
  // code here to instantiate and connect the stages together.
  // '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

  // Connect the last signal in the reg_incr_out signal array to the
  // output port of the module.

  assign out = reg_incr_out[nstages];

endmodule

`endif /* REG_INCR_NSTAGE_V */

