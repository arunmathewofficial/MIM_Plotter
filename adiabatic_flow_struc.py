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

fig, ax = plt.subplots(figsize=(8, 6))

color = 'tab:red'
ax.set_xlabel(r'$\rm x \, (cm)$', fontsize=18)
ax.set_ylabel(r'$\rm \rho \, (g/cm^3)$', fontsize=18)
ax.plot(x_high, get_density(high_resolution_file), color=color, label=r'$\rm \rho$')
ax.tick_params(axis='y')
ax.set_xlim(2e+16, 3e+16)
ax.set_ylim(7e-24, 10e-23)
ax.legend(loc=(0.85, 0.9), frameon=False)

ax_2 = ax.twinx()  # instantiate a second axes that shares the same x-axis

color = 'blue'
ax_2.set_ylabel(r'$\rm log \, T \, (K)$', fontsize=18)  # we already handled the x-label with ax1
ax_2.plot(x_high, np.log10(get_temperature(high_resolution_file)), color=color, linestyle='-', label=r'$\rm T$')
ax_2.tick_params(axis='y')
ax_2.set_xlim(2.4e+16, 2.7e+16)
ax_2.set_ylim(3, 7)
ax_2.legend(loc=(0.85, 0.84), frameon=False)

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis="both", direction="in", which="both",
               bottom=True, top=True, left=True, right=True, length=2)

image_file = output_dir + 'Adiabatic_flowstruc.png'
# get time
time = get_basic_data(high_resolution_file)['time']

print('snapshot time: ', time)
print('Saving image to', image_file)
plt.savefig(image_file, dpi=300)









