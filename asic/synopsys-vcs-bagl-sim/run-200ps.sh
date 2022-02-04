vcs -full64 -sverilog +lint=all -xprop=tmerge -override_timescale=1ns/1ps \
  +define+CYCLE_TIME=0.2 \
  +define+VTB_INPUT_DELAY=0.1 \
  +define+VTB_OUTPUT_ASSERT_DELAY=0.19 \
  +neg_tchk +sdfverbose \
  -sdf max:RegIncr4stageRTL_tb.DUT:../cadence-innovus-pnr/post-pnr.sdf \
  +incdir+../../sim/build \
  +vcs+dumpvars+vcs-bagl-sim.vcd \
  -top RegIncr4stageRTL_tb \
  ../cadence-innovus-pnr/post-pnr.v \
  $ECE5745_STDCELLS/stdcells.v \
  ../../sim/build/RegIncr4stageRTL_test_4stage_random_tb.v
