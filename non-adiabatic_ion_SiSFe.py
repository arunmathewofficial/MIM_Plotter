# Author: Arun Mathew
# Created: 11-03-2023
# Multi-ion-module-publication: This script generates plots comparing
# the non-adiabatic ionization fraction of silicon (Si), sulfur (S),
# and iron (Fe) behind the plane shock for inflow velocities of 1000 km/s and 3000 km/s.


# Import required libraries: ##########################################
import warnings
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nonadia_v1000_silofile", type=str, help="Silo file for non-adiabatic shock with inflow velocity of 1000 km/s")
parser.add_argument("nonadia_v3000_silofile", type=str, help="Silo file for non-adiabatic shock with inflow velocity of 3000 km/s")
parser.add_argument("output_dir", type=str, help="Output image dir path")
args = parser.parse_args()
print("*** Multi-ion-module-publication: non-adiabatic ionisation fraction v1000 vs v3000 ***")

output_dir = args.output_dir
output_dir = make_directory(output_dir)
v1000_file = args.nonadia_v1000_silofile
v3000_file = args.nonadia_v3000_silofile

np.set_printoptions(threshold=np.inf)  # Print the entire array


# x data for v=1000 km/s
x_v1000 = get_basic_data(v1000_file)['x']
# x data for v=3000 km/s
x_v3000 = get_basic_data(v3000_file)['x']

'''

# SILICON ###################################################################
print(' 1 -- Plotting Silicon ion-fraction for v=1000 km/s and v=3000 km/s ...')
plot_data = []
# y data - Silicon species - 1000 km/s velocity =============================
tracer_list = SILICON_NON_ADIABATIC
tracer_labels = SILICON_SHOCK_LABELS
label_position = [[2.5625e16, 0.92], [2.558e16, 0.7], [2.550e16, 0.62], [2.546e16, 0.4], [2.547e16, 0.04],
                  [], [], [], [], [], [], [], [], [], []]
line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
              'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
              'magenta', 'magenta', 'magenta', 'magenta']
line_style = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
tracer_data_list = get_tracers(v1000_file, tracer_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
# loop over silicon ions
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracer_labels[i]
    single_species_data['x'] = x_v1000
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    # single_species_data['line-color'] = line_color[i]
    # single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add neon species to final plot data
plot_data.append(species_data)
del species_data
# y data - Silicon species - 3000 km/s velocity ============================
tracer_list = SILICON_NON_ADIABATIC
tracer_labels = SILICON_SHOCK_LABELS
label_position = [[2.5625e13, 0.92], [2.558e13, 0.7], [2.550e13, 0.62], [2.546e13, 0.4], [2.547e13, 0.04],
                  [], [], [], [], [], [], [], [], [], []]
line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
              'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
              'magenta', 'magenta', 'magenta', 'magenta']
line_style = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
tracer_data_list = get_tracers(v3000_file, tracer_list)

normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
# loop over silicon ions
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracer_labels[i]
    single_species_data['x'] = x_v3000
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    # single_species_data['line-color'] = line_color[i]
    # single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add neon species to final plot data
plot_data.append(species_data)
del species_data
# plot style ===============================================================
plot_style = {}
plot_style['figsize'] = (12, 8)
plot_style['label-font-size'] = 12
plot_style['matrix'] = [2, 1]
plot_style['legend'] = False  # options: True/False
plot_style['sharex'] = False  # options: True/False, 'col', 'all'
plot_style['sharey'] = True  # options: True/False, 'col', 'all'
# insert text in the figure (add several number of text)
# plot_style['insert-txt'] = [['text', 0, 2, 45],['hi-text', -2, 2, 90]]
# plot_style['insert-txt'] = []
plot_style['axis-label'] = [[None, r'\Large{Ioniastion fraction}'],
                            [r'\Large{x (cm)}', r'\Large{Ioniastion fraction}']]
# plot_style['axis-label'] = []
#plot_style['xlimit'] = [[0.0e+14, 1e+14], [0.0e+14, 1e+14],[0.0e+14, 1e+14], [0.0e+14, 1e+14]]
plot_style['insert-txt'] = [[r"${\rm \huge v_0 = 1000 \, km/s}$", 6.2E+15, 2.2, 0],
                            [r"${\rm v_0 = 3000 \, km/s}$", 6.2E+15, 0.9, 0]]
# plot_style['ylimit'] = []
# plot margin adjustments
plot_style['left'] = 0.05  # the left side of the subplots of the figure
plot_style['right'] = 0.9  # the right side of the subplots of the figure
plot_style['bottom'] = 0.1  # the bottom of the subplots of the figure
plot_style['top'] = 0.95  # the top of the subplots of the figure
# plot_style['wspace'] = 0.05  # the amount of width reserved for blank space between subplots
# plot_style['hspace'] = 0.05  # the amount of height reserved for white space between subplots

# this option will force the plot into any subplots
# syntax: [plot-index, plot-location] first enter plot-index and then row and col location of
# plot to be placed into an 1-D array. Place this array in plot_style['force-plotting']
# default setting: plot_style['force-plotting'] = [] or no mention of plot_style['force-plotting']
# example: [2,1,1] this will place second plot at (row=1, col=1)
# plot_style['force-plotting'] = []
# plot_style['force-plotting_1d'] = [[2, 1], [4, 2]]
onedim_master_plotter(plot_data, plot_style)
imagename = output_dir + 'nonadia_v3000_vs_v1000_Si.png'
print(' Saving image ' + imagename)
plt.savefig(imagename)
plt.close()
#############################################################################



# SULFUR ####################################################################
print(' 2 -- Plotting Sulfur ion-fraction for v=1000 km/s and v=3000 km/s ...')
plot_data = []
# y data - Sulfur species 1000 km/s =========================================
tracer_list = SULFUR_NON_ADIABATIC
tracer_labels = SULFUR_SHOCK_LABELS
label_position = [[2.5625e16, 0.92], [2.558e16, 0.7], [2.550e16, 0.62], [2.546e16, 0.4], [2.547e16, 0.04],
                  [], [], [], [], [], [], [], [], [], [], [], []]
line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
              'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
              'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta']
line_style = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--',
              '--', '--', '--', '--', '--', '--']
tracer_data_list = get_tracers(v1000_file, tracer_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
# loop over sulfur ions
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracer_labels[i]
    single_species_data['x'] = x_v1000
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    # single_species_data['line-color'] = line_color[i]
    # single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add neon species to final plot data
plot_data.append(species_data)
del species_data
# y data - Sulfur species 3000 km/s =========================================
tracer_list = SULFUR_NON_ADIABATIC
tracer_labels = SULFUR_SHOCK_LABELS
label_position = [[2.5625e16, 0.92], [2.558e16, 0.7], [2.550e16, 0.62], [2.546e16, 0.4], [2.547e16, 0.04],
                  [], [], [], [], [], [], [], [], [], [], [], []]
line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
              'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
              'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta']
line_style = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--',
              '--', '--', '--', '--', '--', '--']
tracer_data_list = get_tracers(v3000_file, tracer_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
# loop over sulfur ions
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracer_labels[i]
    single_species_data['x'] = x_v3000
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    # single_species_data['line-color'] = line_color[i]
    # single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add neon species to final plot data
plot_data.append(species_data)
del species_data

# plot style ===============================================================
plot_style = {}
plot_style['figsize'] = (12, 8)
plot_style['label-font-size'] = 12
plot_style['matrix'] = [2, 1]
plot_style['legend'] = False  # options: True/False
plot_style['sharex'] = False  # options: True/False, 'col', 'all'
plot_style['sharey'] = True  # options: True/False, 'col', 'all'
# insert text in the figure (add several number of text)
# plot_style['insert-txt'] = [['text', 0, 2, 45],['hi-text', -2, 2, 90]]
# plot_style['insert-txt'] = []
plot_style['axis-label'] = [[None, r'\Large{\rm Ioniastion fraction}'],
                            [r'\Large{\rm x (cm)}', r'\Large{\rm Ioniastion fraction}']]
# plot_style['axis-label'] = []
#plot_style['xlimit'] = [[2e+15, 8e+15], [6e+15, 8.7e+15], [6e+15, 8.7e+15], [6e+15, 8.7e+15]]
plot_style['insert-txt'] = [[r"${\rm \huge v_0 = 1000 \, km/s}$", 6.2E+15, 2.2, 0],
                            [r"${\rm v_0 = 3000 \, km/s}$", 6.2E+15, 0.9, 0]]
# plot_style['ylimit'] = []
# plot margin adjustments
plot_style['left'] = 0.05  # the left side of the subplots of the figure
plot_style['right'] = 0.980  # the right side of the subplots of the figure
plot_style['bottom'] = 0.09  # the bottom of the subplots of the figure
plot_style['top'] = 0.88  # the top of the subplots of the figure
# plot_style['wspace'] = 0.05  # the amount of width reserved for blank space between subplots
plot_style['hspace'] = 0.23  # the amount of height reserved for white space between subplots

# this option will force the plot into any subplots
# syntax: [plot-index, plot-location] first enter plot-index and then row and col location of
# plot to be placed into an 1-D array. Place this array in plot_style['force-plotting']
# default setting: plot_style['force-plotting'] = [] or no mention of plot_style['force-plotting']
# example: [2,1,1] this will place second plot at (row=1, col=1)
# plot_style['force-plotting'] = []
# plot_style['force-plotting_1d'] = [[2, 1], [4, 2]]
onedim_master_plotter(plot_data, plot_style)
imagename = output_dir + 'nonadia_v3000_vs_v1000_S.png'
print(' Saving image ' + imagename)
plt.savefig(imagename)
plt.close()
#############################################################################



'''


# IRON ######################################################################
print(' 3 -- Plotting Iron ion-fraction for v=1000 km/s and v=3000 km/s ...')
plot_data = []
# defining plot frame
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(14, 5), sharex=False, sharey=True)

line_style = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
              '--', '--', '--', '--', '--', '--', '--', '--', '--', '--',
              ':', ':', ':', ':', ':', ':', ':']
tracer_labels = IRON_NON_ADIABATIC_LABELS
discard_last_species = 8
# 1000 km/s velocity %%%%%%%%%%%
tracer_list = IRON_NON_ADIABATIC
tracer_list = OLD_IRON_SHOCK_RAY79E
tracer_data_list = get_tracers(v1000_file, tracer_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
for i in range(len(pro_tracer_data_list) - discard_last_species):
    ax[0].plot(x_v1000, pro_tracer_data_list[i], linestyle=line_style[i])

ax[0].text(5.1E+15, 0.8, r"${\rm V_0 = 1000 \, km/s}$", fontsize=16)
ax[0].set_ylabel(r"\rm Ionisation fraction", fontsize=16)
ax[0].set_xlabel(None, fontsize=18)
ax[0].set_xlim(5e+15, 8.0e+15)
ax[0].tick_params(axis="both", direction="in", which="both",
                  bottom=True, top=True, left=True, right=True,
                  length=3, width=1, labelsize=16)
# 3000 km/s velocity %%%%%%%%%%%%
tracer_list = IRON_NON_ADIABATIC
tracer_list = OLD_IRON_SHOCK_RAY79E
tracer_data_list = get_tracers(v3000_file, tracer_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
for i in range(len(pro_tracer_data_list)- discard_last_species):
    ax[1].plot(x_v3000, pro_tracer_data_list[i], label=tracer_labels[i], linestyle=line_style[i])

ax[1].text(7.1E+15, 0.8, r"${\rm V_0 = 3000 \, km/s}$", fontsize=16)
ax[1].set_ylabel(r"\rm Ionisation fraction", fontsize=16)
ax[1].set_xlabel(r"\rm x (cm)", fontsize=18)
ax[1].set_xlim(7e+15, 8.7e+15)
ax[1].tick_params(axis="both", direction="in", which="both",
                  bottom=True, top=True, left=True, right=True,
                  length=3, width=1, labelsize=16)
ax[1].legend(fontsize=10, bbox_to_anchor=(1.01, 0.09), loc='best',  frameon=True)

# Margin adjustments
left = 0.06  # the left side of the subplots of the figure
right = 0.9  # the right side of the subplots of the figure
bottom = 0.12  # the bottom of the subplots of the figure
top = 0.98  # the top of the subplots of the figure
wspace= 0.1  # the amount of width reserved for blank space between subplots
hspace = 0.23  # the amount of height reserved for white space between subplots
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

# Saving to file
imagename = output_dir + 'nonadia_v3000_vs_v1000_Fe.png'
print(' Saving image ' + imagename)
plt.savefig(imagename)
plt.close()
#############################################################################





