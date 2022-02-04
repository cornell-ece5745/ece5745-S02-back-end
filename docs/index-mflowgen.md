
ECE 5745 Section 2: ASIC Flow Back-End
==========================================================================

Automating the ASIC Flow
--------------------------------------------------------------------------

Our approach so far has enabled us to see the key tools used for the ASIC
flow front- and back-end, but we have been entering commands manually for
each tool. This is obviously very tedious and error prone. An agile
hardware design flow demands automation to simplify rapidly exploring the
area, energy, timing design space of one or more designs. Luckily,
Synopsys and Cadence tools can be easily scripted using TCL, and even
better, the ECE 5745 staff have already created these TCL scripts along
with a set of Makefiles to run the TCL scripts using a framework called
mflowgen.

Let's start by removing the directories we used for the manual flow.

    % cd $TOPDIR/asic/synopsys-vcs-bagl-sim
    % rm -rf cadence-innovus-pnr
    % rm -rf synopsys-dc-synth
    % rm -rf synopsys-vcs-bagl-sim

Each design that you want to push through the flow should have a
dedicated subdirectory in the `asic` directory with a `flow.py` script
that specifies all of the steps you want to use to push that design
through the flow.

The automated flow is located in the `mflowgen` subdirectory of this repo.
Take a look at the `designs` subdirectory. In the subdirectory, you should
see a directory already created for `RegIncr`, which holds all the
configuration required to derive the flow. Take the time to inspect the
file `construct.py`, which describes the desired flow to be ran.
As an input, the flow expects the file `design.v` to be placed inside
`rtl/outputs`. You can execute the following commands to inspect the
structure of the directory:

    % cd mflowgen/designs/RegIncr
    % tree ./

Inside the `construct.py` file, there are a lot of information, but the
important configuration is placed at the top of the file:

    #-----------------------------------------------------------------------
    # Parameters
    #-----------------------------------------------------------------------

    adk_name = 'freepdk-45nm'
    adk_view = 'view-standard'

    parameters = {
      'construct_path' : __file__,
      'design_name'    : 'RegIncr4stageRTL',
      'clock_period'   : 2.0,
      'adk'            : adk_name,
      'adk_view'       : adk_view,
      'topographical'  : True,
    }

The `adk_name` specifies the targeted technology node and fabrication
process. The `design_name` is the name of the corresponding top-level
module. The `clock_period` is the target clock period we want to use for
synthesis and place-and-route.

To get started create a build directory and run the configure script. You
need to explicitly specify which design you want to push through the flow
when you run the configure script.

    % cd $TOPDIR/mflowgen
    % mkdir build
    % cd build
    % ../configure --design ../designs/RegIncr
    % make list

The `list` Makefile target will display the various targets that you can
use to manage the flow. The following two commands will perform synthesis
and then place-and-route.

    % cd $TOPDIR/asic/build
    % make synopsys-dc-synthesis
    % make cadence-innovus-place-route

It will take 4-5 minutes to push the design through the flow. The
automated flow takes longer than the manual steps we used above because
the automated flow is using a much more sophisticated approach with many
more optimization steps. Be aware that for larger designs it can take
quite a while to push a design through the entire flow. Consider using
just the ASIC flow front-end to ensure your design is synthesizable and
to gain some rough early intuition on area and timing. Then you can
iterate quickly and eventually focus on the ASIC flow back-end.

You can use the `debug-` targets to view the final design in Cadence
Innovus.

    % make debug-cadence-innovus-place-route

*To Do On Your Own:* Modify the `construct.py` file to target a much
more aggressive clock period of only 300ps. Use the automated ASIC flow
to push the four-stage registered incrementer through the flow again.
Then use `debug-cadence-innovus-place-route` to bring the final deisgn
up in Cadence Innovus. Explore the design to see how the tool has placed
and routed the more complex incrementers. Use the `report_timing` and
`report_area` commands to look at the critical path and area.
