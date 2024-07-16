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
x_high = get_basic_data(high_resolution_file)['x']/1.0E+16

plt.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
plt.rc('text', usetex=True)
plt.rc('font', **{'size': 12})
plt.rc('lines', linewidth=1.5)

# Create figure and axes
fig, ax = plt.subplots(5, 1, figsize=(8, 12), sharex=True, gridspec_kw={'hspace': 0})  # Adjust figure size as needed

# Plot density
ax[0].plot(x_high, get_density(high_resolution_file)/1.0E-22, color='crimson', label=r'$\rho$', linewidth=2)
ax[0].set_ylabel(r'$\rm \rho \, (10^{-22} g \, cm^{-3})$', fontsize=22)  # Adjust fontsize as needed
ax[0].tick_params(axis='both', labelsize=18)  # Adjust tick label size as needed
ax[0].set_xlim(2.4, 2.7)
ax[0].set_ylim(0.1, 0.9)
ax[0].tick_params(axis="both", direction="in", which="both", bottom=True, left=True, length=3)


# Plot temperature
ax[1].plot(x_high, np.log10(get_temperature(high_resolution_file)), color="black", linestyle='-', label=r'$T$', linewidth=2)
# Set label and ticks for secondary y-axis
ax[1].set_ylabel(r'$\rm log \, T \, (K)$', fontsize=22)  # Adjust fontsize as needed
ax[1].tick_params(axis='y', labelsize=18, direction="in")
ax[1].set_xlim(2.4, 2.7)
ax[1].set_ylim(3.8, 5.8)
# Adjust minor ticks
#ax[1].xaxis.set_minor_locator(AutoMinorLocator())
#ax[1].yaxis.set_minor_locator(AutoMinorLocator())
ax[1].tick_params(axis="both", direction="in", which="both", bottom=True, left=True, length=3)


# Plot pressure
ax[2].plot(x_high, get_pressure(high_resolution_file)/1.0E-9, color="darkblue", linestyle='-', linewidth=2)
# Set label and ticks for secondary y-axis
ax[2].set_ylabel(r'$\rm P \, (10^{-9} \, dyne \, cm^{-2})$', fontsize=22, labelpad=18)  # Adjust fontsize as needed
ax[2].tick_params(axis='y', labelsize=18, direction="in")
ax[2].set_xlim(2.4, 2.7)
ax[2].set_ylim(None, 3.2)
# Adjust minor ticks
#ax[1].xaxis.set_minor_locator(AutoMinorLocator())
#ax[1].yaxis.set_minor_locator(AutoMinorLocator())
ax[2].tick_params(axis="both", direction="in", which="both", bottom=True, left=True, length=3)


# Plot velocity
ax[3].plot(x_high, abs(get_velocityX(high_resolution_file))/1.0E+07, color="darkgreen", linestyle='-', label=r'$T$', linewidth=2)
# Set label and ticks for secondary y-axis
ax[3].set_ylabel(r'$\rm v_x \, (10^2 \, km\, s^{-1})$', fontsize=22)  # Adjust fontsize as needed
ax[3].tick_params(axis='y', labelsize=18, direction="in")
ax[3].set_xlim(2.4, 2.7)
ax[3].set_ylim(None, 1.2)
ax[3].tick_params(axis="both", direction="in", which="both", bottom=True, left=True, length=3)




# Plot magnetic field
ax[4].plot(x_high, abs(get_MagneticFieldY(high_resolution_file))/1.0E-6, color="gray", linestyle='-', label=r'$T$', linewidth=2)
# Set label and ticks for secondary y-axis
ax[4].set_ylabel(r'$\rm B_y \, (10^{-6}\, G)$', fontsize=22, labelpad=12)  # Adjust fontsize as needed
ax[4].set_xlabel(r'$\rm x \, (10^{16} cm)$', fontsize=22)  # Adjust fontsize as needed
ax[4].set_xlim(2.4, 2.7)
ax[4].set_ylim(0.5, 4.5)
# Adjust minor ticks
ax[4].xaxis.set_minor_locator(AutoMinorLocator())
ax[4].tick_params(axis="both", direction="in", which="both", bottom=True, left=True, length=3, labelsize=18)











plt.subplots_adjust(wspace=0)

# Adjust layout to prevent label cutoff
plt.tight_layout()
image_file = output_dir + 'Adiabatic_flowstruc.png'
# get time
time = get_basic_data(high_resolution_file)['time']
print('snapshot time: ', time)
print('Saving image to', image_file)
plt.savefig(image_file)









