# Author: Arun Mathew, Jonathan Mackey

#############################################################
# Import required libraries:
import matplotlib.pyplot as plt
import os
import numpy
#from pypion.argparse_command import InputValues
#from ReadTable import ReadTable
#from Analysis import Analysis
from astropy import units as unit
from argparse_pypionplotter import ArgparseInputs
from pypion_plotter import Plot_Functions


#############################################################
print('*************** Plot 2D wind-wind simulation *****************')
#############################################################
# Making Output directory
# If already exist, the pass.
inputs = ArgparseInputs()
OutputDir = inputs.img_dir
try:
    # Create target Directory
    os.mkdir(OutputDir)
    print("Output directory:", OutputDir,  "created.")
except FileExistsError:
    print("Output directory", OutputDir, "already exists.")
    pass
# ***********************************************************


##############################################################
# Plotting Density and Temperature
plot = Plot_Functions(path=inputs.path, 
                      basename=inputs.basename, 
                      image_dir=inputs.img_dir)


#*************************************************************
variable_1 = ["Density", -22, -27.5, "viridis", 'originalform','y', 127]
variable_2 = ["Temperature", 8.3, 3.75, "inferno", 'originalform', 'y', 127]
plot.TwoDPlotter_Double(["z", "R"], variable_1, variable_2)
#*************************************************************
