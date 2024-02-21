# Author: Arun Mathew
# Created: 16-03-2023
# Multi-ion-module-publication: Adiabatic flow structure plotter
# For the planar shock at an inflow velocity of 100 km/s.


# Import required libraries: ##########################################
import warnings
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("high_resolution", type=str, help="High-resolution silo file")
parser.add_argument("output_dir", type=str, help="give the output image dir path")
args = parser.parse_args()
output_dir = args.output_dir
output_dir = make_directory(output_dir)
high_resolution_file = args.high_resolution


# make plotting data and append to plot_data array
plot_data = []
# x data
x_high = get_basic_data(high_resolution_file)['x']

plt.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
plt.rc('text', usetex=True)
plt.rc('font', **{'size': 12})
plt.rc('lines', linewidth=1.5)

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))  # Adjust figure size as needed

# Define colors
color1 = 'tab:red'
color2 = 'tab:blue'

# Plot first data on primary y-axis
ax.plot(x_high, get_density(high_resolution_file), color=color1, label=r'$\rho$')

# Set labels and ticks for primary y-axis
ax.set_xlabel(r'$\rm x \, (cm)$', fontsize=20)  # Adjust fontsize as needed
ax.set_ylabel(r'$\rm \rho \, (g/cm^3)$', fontsize=20)  # Adjust fontsize as needed
ax.tick_params(axis='both', labelsize=16)  # Adjust tick label size as needed
ax.set_xlim(2e+16, 3e+16)
ax.set_ylim(7e-24, 10e-23)
ax.legend(loc=(0.7, 0.82), frameon=False, fontsize='xx-large')

# Create a secondary y-axis sharing the same x-axis
ax_2 = ax.twinx()

# Plot second data on secondary y-axis
ax_2.plot(x_high, np.log10(get_temperature(high_resolution_file)), color=color2, linestyle='-', label=r'$T$')

# Set label and ticks for secondary y-axis
ax_2.set_ylabel(r'$\rm log \, T \, (K)$', fontsize=20)  # Adjust fontsize as needed
ax_2.tick_params(axis='y', labelsize=16, direction="in")
ax_2.set_xlim(2.4e+16, 2.7e+16)
ax_2.set_ylim(3, 7)
ax_2.legend(loc=(0.7, 0.74), frameon=False, fontsize='xx-large')

# Adjust minor ticks
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis="both", direction="in", which="both",
               bottom=True, top=True, left=True, right=False, length=2)

# Adjust layout to prevent label cutoff
plt.tight_layout()

image_file = output_dir + 'Adiabatic_flowstruc.png'
# get time
time = get_basic_data(high_resolution_file)['time']

print('snapshot time: ', time)
print('Saving image to', image_file)
plt.savefig(image_file)









