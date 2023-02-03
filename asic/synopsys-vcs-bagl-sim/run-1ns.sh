
vcs -full64 -sverilog +lint=all -xprop=tmerge -override_timescale=1ns/1ps \
  +incdir+../../sim/build \
  +vcs+dumpvars+vcs-bagl-sim.vcd \
  -top RegIncrNstage__p_nstages_4_tb \
  +define+CYCLE_TIME=1.0 \
  +define+VTB_INPUT_DELAY=0.1 \
  +define+VTB_OUTPUT_ASSERT_DELAY=0.99 \
  +neg_tchk +sdfverbose \
  -sdf max:RegIncrNstage__p_nstages_4_tb.DUT:../cadence-innovus-pnr/post-pnr.sdf \
  ../cadence-innovus-pnr/post-pnr.v \
  $ECE5745_STDCELLS/stdcells.v \
  ../../sim/build/RegIncrNstage__p_nstages_4_test_random_4_tb.v

