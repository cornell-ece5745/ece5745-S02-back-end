
set_app_var target_library "$env(ECE5745_STDCELLS)/stdcells.db"
set_app_var link_library   "* $env(ECE5745_STDCELLS)/stdcells.db"
analyze -format sverilog ../../sim/build/RegIncrNstage__p_nstages_4__pickled.v
elaborate RegIncrNstage__p_nstages_4
check_design
create_clock clk -name ideal_clock1 -period 1
compile
write -format verilog -hierarchy -output post-synth.v
write -format ddc     -hierarchy -output post-synth.ddc
exit
