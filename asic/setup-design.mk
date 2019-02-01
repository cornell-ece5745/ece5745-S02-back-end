#=========================================================================
# setup-design.mk
#=========================================================================
# Here we select the design to push as well as its top-level Verilog
# module name, the clock target, and the Verilog source file.
#
# Author : Christopher Torng
# Date   : March 26, 2018

#-------------------------------------------------------------------------
# PyMTL GcdUnit
#-------------------------------------------------------------------------

ifeq ($(design),pymtl-gcd)
  design_name  = GcdUnit
  clock_period = 2.0
  design_v     = ../designs/GcdUnit-demo.v
endif

#-------------------------------------------------------------------------
# ECE 5745 Multi-Stage Registered Incrementer
#-------------------------------------------------------------------------

ifeq ($(design),regincr)
  design_name  = RegIncrNstageRTL_4stage
  clock_period = 1.0
  design_v     = ../../sim/build/RegIncrNstageRTL_4stage.v
endif

#-------------------------------------------------------------------------
# Export
#-------------------------------------------------------------------------

export design_name


