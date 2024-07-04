# Author: Arun Mathew
# Created: 07-03-2023
# Script to compare cie ionisation profile of Ne, Si,
# and Fe with and without charge-exchange reactions.

# Import required libraries: ##########################################
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("cx_off_cie_silo", type=str, help="give the input silo input_silo path")
parser.add_argument("cx_on_cie_silo", type=str, help="give the input silo input_silo path")
parser.add_argument("output_dir", type=str, help="give the output image dir path")

args = parser.parse_args()
cx_off_cie_silo = args.cx_off_cie_silo
cx_on_cie_silo = args.cx_on_cie_silo
output_dir = args.output_dir
output_dir = make_directory(output_dir)
abundance  = "asplund09"

# make plotting data and append to plot_data array
plot_data = []

# X-DATA ###############################################################
# x data cx off ##########################
temperature_cx_off = get_temperature(cx_off_cie_silo)
temperature_cx_off = np.log10(temperature_cx_off)
# x data cx on ##########################
temperature_cx_on = get_temperature(cx_on_cie_silo)
temperature_cx_on = np.log10(temperature_cx_on)


# NEON ###################################################################
# y data - neon species cx off ###########
tracers_list = NEON_CIE_ASPLUND2009
tracers_labels = NEON_CIE_LABELS
label_position = [[], [], [], [], [5.4, 0.7], [5.6, 0.6], [5.72, 0.42], [5.9, 0.18], [6.3, 1.0], [6.67, 0.45],
                  [6.8, 0.8]]
line_color = ['darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue',
              'darkblue', 'darkblue', 'darkblue']
line_style = ['-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-']
tracer_data_list = get_tracers(cx_off_cie_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
# loop over neon ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature_cx_off
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add neon species to final plot data
plot_data.append(species_data)
del species_data

# y data - neon species cx on ###########
tracers_list = NEON_CIE_ASPLUND2009
tracers_labels = NEON_CIE_LABELS
label_position = [[], [], [], [], [5.4, 0.7], [5.6, 0.6], [5.72, 0.42], [5.9, 0.18], [6.3, 1.0], [6.67, 0.45],
                  [6.8, 0.8]]
line_color = ['darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue',
              'darkblue', 'darkblue', 'darkblue']
line_style = ['-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-']
tracer_data_list = get_tracers(cx_on_cie_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
# loop over neon ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature_cx_on
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add neon species to final plot data
plot_data.append(species_data)
del species_data

# SILICON ###############################################################
# y data - silicon species cx off ###########
tracers_list = SILICON_CIE_ASPLUND2009
tracers_labels = SILICON_CIE_LABELS
label_position = [[3.9, 1.02], [4.2, 1.02], [4.65, 0.93], [], [5.2, 1.02],
                  [5.6, 0.58], [5.75, 0.58], [], [], [], [],
                  [], [6.6, 0.98], [6.9, 0.35], [7.5, 0.98]]
line_color = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
              'black', 'black', 'black', 'black', 'black', 'black', 'black']
line_style = ['-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-']
tracer_data_list = get_tracers(cx_off_cie_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
# loop over silicon ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature_cx_off
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add silicon species to final plot data
plot_data.append(species_data)
del species_data

# y data - silicon species cx on ###########
tracers_list = SILICON_CIE_ASPLUND2009
tracers_labels = SILICON_CIE_LABELS
label_position = [[3.9, 1.02], [4.2, 1.02], [4.65, 0.93], [], [5.2, 1.02],
                  [5.6, 0.58], [5.75, 0.58], [], [], [], [],
                  [], [6.6, 0.98], [6.9, 0.35], [7.5, 0.98]]
line_color = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
              'black', 'black', 'black', 'black', 'black', 'black', 'black']
line_style = ['-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-']
tracer_data_list = get_tracers(cx_on_cie_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
# loop over silicon ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature_cx_on
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add silicon species to final plot data
plot_data.append(species_data)
del species_data

# IRON #################################################################
# y data - iron species cx off ###########
tracers_list = IRON_CIE_ASPLUND2009
tracers_labels = IRON_CIE_LABELS
label_position = [[3.8, 1.02], [4.05, 1.02], [4.4, 1], [4.7, 0.92], [4.95, 0.78],
                  [5.08, 0.65], [5.2, 0.65], [5.45, 0.93], [5.5, 0.2], [5.55, 0.3], [5.67, 0.45],
                  [5.93, 0.88], [6.05, 0.36], [6.25, 0.32], [6.5, 0.2], [6.4, 0.42], [6.62, 0.53],
                  [6.85, 0.345], [6.9, 0.3], [], [7.07, 0.3], [], [7.4, 0.15], [7.35, 0.3],
                  [7.65, 0.79], [8.1, 0.47], [8.3, 0.6]]
line_color = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
              'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
              'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
              'black', 'black', 'black']
line_style = ['-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-',
              '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--']
tracer_data_list = get_tracers(cx_off_cie_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
# loop over sulfur ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature_cx_off
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add sulfur species to final plot data
plot_data.append(species_data)
del species_data

# y data - iron species cx on ###########
tracers_list = IRON_CIE_ASPLUND2009
tracers_labels = IRON_CIE_LABELS
label_position = [[3.8, 1.02], [4.05, 1.02], [4.4, 1], [4.7, 0.92], [4.95, 0.78],
                  [5.08, 0.65], [5.2, 0.65], [5.45, 0.93], [5.5, 0.2], [5.55, 0.3], [5.67, 0.45],
                  [5.93, 0.88], [6.05, 0.36], [6.25, 0.32], [6.5, 0.2], [6.4, 0.42], [6.62, 0.53],
                  [6.85, 0.345], [6.9, 0.3], [], [7.07, 0.3], [], [7.4, 0.15], [7.35, 0.3],
                  [7.65, 0.79], [8.1, 0.47], [8.3, 0.6]]
line_color = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
              'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
              'black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
              'black', 'black', 'black']
line_style = ['-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-',
              '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--']
tracer_data_list = get_tracers(cx_on_cie_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
# loop over sulfur ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature_cx_on
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add sulfur species to final plot data
plot_data.append(species_data)
del species_data

# plot style ================================================================
plot_style = {}
plot_style['figsize'] = (12, 16)
plot_style['label-font-size'] = 12
plot_style['matrix'] = [3 , 1]
plot_style['legend'] = False  # options: True/False
plot_style['sharex'] = False  # options: True/False, 'col', 'all'
plot_style['sharey'] = False  # options: True/False, 'col', 'all'

plot_style['xlimit'] = [[3.9, 6.6], [3.9, 7.1], [3.8, 8], [3.7, 8.5]]
plot_style['ylimit'] = [[0.0, 1.1], [0.0, 1.1], [0.0, 1.1], [0.0, 1.1]]

plot_style['force-plotting_1d'] = [[2, 1], [3, 1], [5, 2], [6, 2], [8, 3]]

plot_style['axis-label'] = [[None, r'$\rm Ioniastion \, fraction$'],
                            [None, r'$\rm Ioniastion \, fraction$'],
                            [None, r'$\rm Ioniastion \, fraction$'],
                            [r'$\rm log(T) \, K$', r'$\rm Ioniastion \, fraction$']]

plot_style['insert-txt'] = []

# plot margin adjustments
plot_style['left'] = 0.1  # the left side of the subplots of the figure
plot_style['right'] = 0.9  # the right side of the subplots of the figure
plot_style['bottom'] = 0.05  # the bottom of the subplots of the figure
plot_style['top'] = 0.95  # the top of the subplots of the figure
plot_style['wspace'] = 0.0  # the amount of width reserved for blank space between subplots
plot_style['hspace'] = 0.1  # the amount of height reserved for white space between subplots

onedim_master_plotter(plot_data, plot_style)
plot_input_silo = output_dir + 'CIE_' + abundance +'.png'
print('Saving image to input_silo', plot_input_silo)
plt.savefig(output_dir + 'CIE_' + abundance +'.png', dpi=300)
