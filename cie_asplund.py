# Author: Arun Mathew
# Created: 07-03-2023
# To plot CIE ASPLUND 2009

# Import required libraries: ##########################################
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_silo_file", type=str, help="give the input silo input_silo path")
parser.add_argument("output_dir", type=str, help="give the output image dir path")

args = parser.parse_args()
input_silo = args.input_silo_file
output_dir = args.output_dir
output_dir = make_directory(output_dir)
abundance  = "asplund09"

# make plotting data and append to plot_data array
plot_data = []

# make data to write to input_silo
data_dict = {}

# x data ##########################
temperature = get_temperature(input_silo)
temperature = np.log10(temperature)
# save data to dict
data_dict = add_data_to_dict(data_dict, temperature, '$log_T$')

# y data - Hydrogen species #########
tracer_list = HYDROGEN_CIE_ASPLUND2009
tracer_labels = HYDROGEN_CIE_LABELS
label_position = [[4.0, 1.02], [4.4, 1.02]]
line_color = ['black', 'black']
line_style = ['-', 'dashed']
tracer_data_list = get_tracers(input_silo, tracer_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
data_dict = add_data_to_dict(data_dict, pro_tracer_data_list, HYDROGEN_LABELS)
# loop over hydrogen ions
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracer_labels[i]
    single_species_data['x'] = temperature
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add hydrogen species to final plot data
plot_data.append(species_data)
del species_data

# y data - Helium species ###########
tracers_list = HELIUM_CIE_ASPLUND2009
tracers_labels = HELIUM_CIE_LABELS
label_position = [[], [4.65, 0.91], [4.96, 0.93]]
line_color = ['crimson', 'crimson', 'crimson']
line_style = ['-', 'dashed', '-']
tracer_data_list = get_tracers(input_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
data_dict = add_data_to_dict(data_dict, pro_tracer_data_list, HELIUM_LABELS)
# loop over helium ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add helium species to final plot data
plot_data.append(species_data)
del species_data

# y data - Carbon species ###########
tracers_list = CARBON_CIE_ASPLUND2009
tracers_labels = CARBON_CIE_LABELS
label_position = [[], [], [4.86, 0.9], [5.15, 0.2], [5.5, 0.9], [6, 0.55], [6.25, 0.9]]
line_color = ['darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue']
line_style = ['-', 'dashed', '-', 'dashed', '-', 'dashed', '-']
tracer_data_list = get_tracers(input_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
data_dict = add_data_to_dict(data_dict, pro_tracer_data_list, CARBON_LABELS)
# loop over carbon ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add carbon species to final plot data
plot_data.append(species_data)
del species_data

# y data - Nitrogen species ###########
tracers_list = NITROGEN_CIE_ASPLUND2009
tracers_labels = NITROGEN_CIE_LABELS
label_position = [[4.0, 1.02], [4.46, 1.02], [4.9, 0.83], [5.15, 0.75], [5.31, 0.25], [5.5, 1.0], [6.2, 0.52],
                  [6.6, 1.0]]
line_color = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black']
line_style = ['-', 'dashed', '-', 'dashed', '-', 'dashed', '-', 'dashed']
tracer_data_list = get_tracers(input_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
data_dict = add_data_to_dict(data_dict, pro_tracer_data_list, NITROGEN_LABELS)
# loop over oxygen ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add oxygen species to final plot data
plot_data.append(species_data)
del species_data

# y data - Oxygen species ###########
tracers_list = OXYGEN_CIE_ASPLUND2009
tracers_labels = OXYGEN_CIE_LABELS
label_position = [[], [], [], [], [5.4, 0.55], [5.54, 0.15], [6.0, 1.02], [6.35, 0.48], [6.56, 0.85]]
line_color = ['crimson', 'crimson', 'crimson', 'crimson', 'crimson', 'crimson', 'crimson', 'crimson', 'crimson']
line_style = ['-', '--', '-', '--', '-', '--', '-', '--', '-']
tracer_data_list = get_tracers(input_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
data_dict = add_data_to_dict(data_dict, pro_tracer_data_list, OXYGEN_LABELS)
# loop over oxygen ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add oxygen species to final plot data
plot_data.append(species_data)
del species_data

# y data - neon species ###########
tracers_list = NEON_CIE_ASPLUND2009
tracers_labels = NEON_CIE_LABELS
label_position = [[], [], [], [], [5.4, 0.7], [5.6, 0.6], [5.72, 0.42], [5.9, 0.18], [6.3, 1.0], [6.67, 0.45],
                  [6.8, 0.8]]
line_color = ['darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue', 'darkblue',
              'darkblue', 'darkblue', 'darkblue']
line_style = ['-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-']
tracer_data_list = get_tracers(input_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
data_dict = add_data_to_dict(data_dict, pro_tracer_data_list, NEON_LABELS)
# loop over neon ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add neon species to final plot data
plot_data.append(species_data)
del species_data

# y data - silicon species ###########
tracers_list = SILICON_CIE_ASPLUND2009
tracers_labels = SILICON_CIE_LABELS
label_position = [[3.9, 1.02], [4.2, 1.02], [4.65, 0.93], [], [5.2, 1.02],
                  [5.6, 0.58], [5.75, 0.58], [], [], [], [],
                  [], [6.6, 0.98], [6.9, 0.35], [7.5, 0.98]]
line_color = ['black', 'black', 'black', 'black', 'black', 'black', 'black', 'black',
              'black', 'black', 'black', 'black', 'black', 'black', 'black']
line_style = ['-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-']
tracer_data_list = get_tracers(input_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
data_dict = add_data_to_dict(data_dict, pro_tracer_data_list, SILICON_LABELS)
# loop over silicon ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add silicon species to final plot data
plot_data.append(species_data)
del species_data

# y data - sulfur species ###########
tracers_list = SULFUR_CIE_ASPLUND2009
tracers_labels = SULFUR_CIE_LABELS
label_position = [[], [], [], [4.95, 0.66], [5.15, 0.65], [], [5.52, 1.0], [5.95, 0.52],
                  [6.1, 0.51], [], [],
                  [], [6.52, 0.25], [6.7, 0.15], [6.9, 0.98], [7.6, 0.25], [7.5, 0.8]]
line_color = ['crimson', 'crimson', 'crimson', 'crimson', 'crimson', 'crimson', 'crimson', 'crimson',
              'crimson', 'crimson', 'crimson', 'crimson', 'crimson', 'crimson', 'crimson', 'crimson', 'crimson']
line_style = ['-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-', '--', '-']
tracer_data_list = get_tracers(input_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
data_dict = add_data_to_dict(data_dict, pro_tracer_data_list, SULFUR_LABELS)
# loop over sulfur ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature
    single_species_data['y'] = pro_tracer_data_list[i]
    single_species_data['label-position'] = label_position[i]
    single_species_data['line-color'] = line_color[i]
    single_species_data['line-style'] = line_style[i]
    species_data.append(single_species_data.copy())
# add sulfur species to final plot data
plot_data.append(species_data)
del species_data

# y data - iron species ###########
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
tracer_data_list = get_tracers(input_silo, tracers_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
data_dict = add_data_to_dict(data_dict, pro_tracer_data_list, IRON_LABELS)
# loop over sulfur ions and append the details in species data
species_data = []
single_species_data = {}
for i in range(len(pro_tracer_data_list)):
    single_species_data['labels'] = tracers_labels[i]
    single_species_data['x'] = temperature
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
plot_style['figsize'] = (3.6, 7.8)
plot_style['label-font-size'] = 12
plot_style['matrix'] = [4, 1]
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
plot_style['left'] = 0.16  # the left side of the subplots of the figure
plot_style['right'] = 0.98  # the right side of the subplots of the figure
plot_style['bottom'] = 0.06  # the bottom of the subplots of the figure
plot_style['top'] = 0.99  # the top of the subplots of the figure
plot_style['wspace'] = 0.0  # the amount of width reserved for blank space between subplots
plot_style['hspace'] = 0.1  # the amount of height reserved for white space between subplots

onedim_master_plotter(plot_data, plot_style)
plot_input_silo = output_dir + 'CIE_' + abundance +'.png'
print('Saving image to input_silo', plot_input_silo)
plt.savefig(output_dir + 'CIE_' + abundance +'.png', dpi=300)

df = pd.DataFrame(data_dict)
data_input_silo = output_dir + 'CIE_' + abundance + '.txt'
print('Writing data to input_silo', data_input_silo)
df.to_csv(data_input_silo, sep=' ', index=False, float_format='%.8e')
with open(data_input_silo, 'r+') as input_silo:
    contents = input_silo.read()
    input_silo.seek(0, 0)
    input_silo.write('# Collisional ionization equilibrium (CIE) ion-fractions\n' + contents)
    input_silo.write('# Abundances:' + abundance)
