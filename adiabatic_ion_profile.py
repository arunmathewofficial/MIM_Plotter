# Author: Arun Mathew
# Created: 11-03-2023
# Multi-ion-module-publication: Generate a comparison plot for low
# and high-resolution chemical profiles in the vicinity of the shock.


# Import required libraries: ##########################################
import warnings
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("low_resolution", type=str, help="Low-resolution silo file")
parser.add_argument("high_resolution", type=str, help="High-resolution silo file")
parser.add_argument("output_dir", type=str, help="Output image dir path")
parser.add_argument("plot_option", type=int, help="Options: 1 for H, He, C, N, O, and Ne plot and 2 of Si, S, and Fe plot")

args = parser.parse_args()
output_dir = args.output_dir
output_dir = make_directory(output_dir)
low_resolution_file = args.low_resolution
high_resolution_file = args.high_resolution
option = args.plot_option
if option != 1 and option != 2:
    print('\033[93mSpecify the correct plot option\033[0m')
    print('\033[93mOptions: 1 for H, He, C, N, O, and Ne plot and 2 of Si, S, and Fe plot\033[0m')




##########################################################################
# OPTION: 1 ##############################################################
##########################################################################

if option == 1:

    '''
    Plot ionisation profile of H, He, C, N, O, and Ne behind the shock for
    the adiabatic flow.
    '''

    print('Plotting H, He, C, N, O, and Ne ionisation profile ...')

    # check for match
    if not abs(get_basic_data(high_resolution_file)['time'].value - get_basic_data(low_resolution_file)[
        'time'].value) <= 1.0E-04:
        warnings.warn(message='Time in two silo file do not match, exiting ...', stacklevel=2)
        exit(0)

    # make plotting data and append to plot_data array
    plot_data = []

    # x data
    x_low = get_basic_data(low_resolution_file)['x']/1.0E+16
    x_high = get_basic_data(high_resolution_file)['x']/1.0E+16

    #modify x_low data by shifting to left
    x_low = x_low - 0.0025*np.ones_like(x_low)

    # Hydrogen ###########################################################
    # y data - Hydrogen species - low resolution
    tracer_list = HYDROGEN_SHOCK_RAY79E
    tracer_labels = HYDROGEN_ADIA_SHOCK_LABELS
    label_position = [[2.563,0.75], [2.545,0.9]]
    line_color = ['crimson', 'darkblue']
    line_style = ['--', '--']
    line_marker = ['o', 'o']
    tracer_data_list = get_tracers(low_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over hydrogen ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_low
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        single_species_data['line-marker'] = line_marker[i]
        species_data.append(single_species_data.copy())
    # add hydrogen species to final plot data
    plot_data.append(species_data)
    del species_data

    # y data - Hydrogen species - high resolution
    tracer_list = HYDROGEN_SHOCK_RAY79E
    tracer_labels = HYDROGEN_LABELS
    label_position = [[], []]
    line_color = ['crimson', 'darkblue']
    line_style = ['-', '-']
    tracer_data_list = get_tracers(high_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over hydrogen ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_high
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add hydrogen species to final plot data
    plot_data.append(species_data)
    del species_data

    # Helium ##############################################################
    # y data - Helium species - low resolution
    tracer_list = HELIUM_SHOCK_RAY79E
    tracer_labels = HELIUM_ADIA_SHOCK_LABELS
    label_position = [[2.563,0.8], [2.55,0.7], [2.545,0.3]]
    line_color = ['crimson', 'darkblue', 'darkgreen']
    line_style = ['--', '--', '--']
    line_marker = ['o', 'o', 'o']
    tracer_data_list = get_tracers(low_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over helium ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_low
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        single_species_data['line-marker'] = line_marker[i]
        species_data.append(single_species_data.copy())
    # add helium species to final plot data
    plot_data.append(species_data)
    del species_data

    # y data - Helium species - high resolution
    tracer_list = HELIUM_SHOCK_RAY79E
    tracer_labels = HELIUM_LABELS
    label_position = [[], [], []]
    line_color = ['crimson', 'darkblue', 'darkgreen']
    line_style = ['-', '-', '-']
    tracer_data_list = get_tracers(high_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over helium ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_high
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add helium species to final plot data
    plot_data.append(species_data)
    del species_data

    # Carbon ####################################################
    # y data - Carbon species -     line_color = ['black', 'crimson', 'darkgreen', 'gold', 'royalblue', 'darkorange', 'magenta']low resolution
    tracer_list = OLD_CARBON_SHOCK_RAY79E
    tracer_labels = CARBON_ADIA_SHOCK_LABELS
    label_position = [[2.563,0.8], [2.559,0.68], [2.5565,0.83], [2.546,0.68], [2.543,0.1], [], []]
    line_color = ['crimson', 'darkblue', 'darkgreen', 'gray', 'darkorange']
    line_style = ['--', '--', '--', '--', '--', '--', '--']
    line_marker = ['o', 'o', 'o', 'o', 'o', 'o', 'o']
    tracer_data_list = get_tracers(low_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over Carbon ions
    species_data = []
    single_species_data = {}
    not_plot_last = 2
    for i in range(len(pro_tracer_data_list)-not_plot_last):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_low
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        single_species_data['line-marker'] = line_marker[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data

    # y data - Carbon species - high resolution
    tracer_list = CARBON_SHOCK_RAY79E
    tracer_labels = CARBON_LABELS
    label_position = [[], [], [], [], [], [], []]
    line_color = ['crimson', 'darkblue', 'darkgreen', 'gray', 'darkorange']
    line_style = ['-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(high_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over carbon ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)-not_plot_last):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_high
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data


    # NITROGEN ####################################################
    # y data - nitrogen species - low resolution
    tracer_list = NITROGEN_SHOCK_RAY79E
    tracer_labels = NITROGEN_ADIA_SHOCK_LABELS
    label_position = [[2.5635,0.85], [2.5585,0.68], [2.556,0.7], [2.542,0.8], [2.546,0.1], [], [], []]
    line_color = ['crimson', 'darkblue', 'darkgreen', 'gray', 'darkorange']
    line_style = ['--', '--', '--', '--', '--', '--', '--']
    line_marker = ['o', 'o', 'o', 'o', 'o', 'o', 'o']
    tracer_data_list = get_tracers(low_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over Carbon ions
    species_data = []
    single_species_data = {}
    not_plot_last = 3
    for i in range(len(pro_tracer_data_list)-not_plot_last):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_low
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        single_species_data['line-marker'] = line_marker[i]

        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data

    # y data - nitrogen species - high resolution
    tracer_list = NITROGEN_SHOCK_RAY79E
    tracer_labels = NITROGEN_LABELS
    label_position = [[], [], [], [], [], [], [], []]
    line_color = ['crimson', 'darkblue', 'darkgreen', 'gray', 'darkorange']
    line_style = ['-', '-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(high_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over nitrogen ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)-not_plot_last):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_high
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add nitrogen species to final plot data
    plot_data.append(species_data)
    del species_data

    # OXYGEN ####################################################
    # y data - oxygen species - low resolution
    tracer_list = OXYGEN_SHOCK_RAY79E
    tracer_labels = OXYGEN_ADIA_SHOCK_LABELS
    label_position = [[2.5635,0.85], [2.5585,0.68], [2.555,0.66], [2.542,0.72], [2.546,0.1], [], [], [], []]
    line_color = ['crimson', 'darkblue', 'darkgreen', 'gray', 'darkorange']
    line_style = ['--', '--', '--', '--', '--', '--', '--']
    line_marker = ['o', 'o', 'o', 'o', 'o', 'o', 'o']
    tracer_data_list = get_tracers(low_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over oxygen ions
    species_data = []
    single_species_data = {}
    dont_plot_last = 4
    for i in range(len(pro_tracer_data_list)-dont_plot_last):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_low
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        single_species_data['line-marker'] = line_marker[i]
        species_data.append(single_species_data.copy())
    # add oxygen species to final plot data
    plot_data.append(species_data)
    del species_data

    # y data - Oxygen species - high resolution
    tracer_list = OXYGEN_SHOCK_RAY79E
    tracer_labels = OXYGEN_LABELS
    label_position = [[], [], [], [], [], [], [], [], []]
    line_color = ['crimson', 'darkblue', 'darkgreen', 'gray', 'darkorange']
    line_style = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(high_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over oxygen ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)-dont_plot_last):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_high
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data


    # Neon ####################################################
    # y data - Neon species - low resolution
    tracer_list = NEON_SHOCK_RAY79E
    tracer_labels = NEON_ADIA_SHOCK_LABELS
    label_position = [[2.5625,0.75], [2.5575,0.72], [2.551,0.6], [2.5406,0.53], [2.547,0.03], [], [], [], [], [], []]
    line_color = ['crimson', 'darkblue', 'darkgreen', 'gray', 'darkorange']
    line_style = ['--', '--', '--', '--', '--', '--', '--']
    line_marker = ['o', 'o', 'o', 'o', 'o', 'o', 'o']
    tracer_data_list = get_tracers(low_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over neon ions
    species_data = []
    single_species_data = {}
    dont_plot_last = 6
    for i in range(len(pro_tracer_data_list)-dont_plot_last):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_low
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        single_species_data['line-marker'] = line_marker[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data

    # y data - neon species - high resolution
    tracer_list = NEON_SHOCK_RAY79E
    tracer_labels = NEON_LABELS
    label_position = [[], [], [], [], [], [], [], [], [], [], []]
    line_color = ['crimson', 'darkblue', 'darkgreen', 'gray', 'darkorange']
    line_style = ['-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(high_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = old_process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over neon ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)-dont_plot_last):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_high
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data

    # plot style ================================================================
    plot_style = {}
    plot_style['figsize'] = (16, 10)
    plot_style['label-font-size'] = 12
    plot_style['matrix'] = [3, 2]
    plot_style['legend'] = False       # options: True/False
    plot_style['sharex'] = True       # options: True/False, 'col', 'all'
    plot_style['sharey'] = False       # options: True/False, 'col', 'all'

    # insert text in the figure (add several number of text)
    #plot_style['insert-txt'] = [[r'\huge \rm Hydrogen', 2.514, 3.4, 0],
    #                            [r'\huge \rm Helium', 2.541, 3.5, 0],
    #                            [r'\huge \rm Carbon', 2.514, 2.2, 0],
    #                            [r'\huge \rm Nitrogen', 2.541, 2.2,0],
    #                            [r'\huge \rm Oxygen', 2.514, 0.9, 0],
    #                            [r'\huge \rm Neon', 2.541, 0.9, 0]]
    #plot_style['insert-txt'] = []
    plot_style['axis-label'] = [[None, r'\huge \rm Ioniastion fraction'], [None, r'\huge \rm Ioniastion fraction'],
                                [None, r'\huge \rm Ioniastion fraction'], [None, r'\huge \rm Ioniastion fraction'],
                                [r'\huge \rm x (10$^{16}$ cm)', r'\huge \rm Ioniastion fraction'], [r'\huge \rm x (10$^{16}$ cm)', r'\huge \rm Ioniastion fraction']]
    #plot_style['axis-label'] = []

    plot_style['xlimit'] = [[2.54, 2.57],
                            [2.54, 2.57],
                            [2.54, 2.57],
                            [2.54, 2.57],
                            [2.54, 2.565],
                            [2.54, 2.565]]

    #plot_style['ylimit'] = []

    # plot margin adjustments
    plot_style['left'] = 0.05  # the left side of the subplots of the figure
    plot_style['right'] = 0.97   # the right side of the subplots of the figure
    plot_style['bottom'] = 0.1  # the bottom of the subplots of the figure
    plot_style['top'] = 0.95    # the top of the subplots of the figure
    plot_style['wspace'] = 0.15  # the amount of width reserved for blank space between subplots
    plot_style['hspace'] = 0.0  # the amount of height reserved for white space between subplots

    # this option will force the plot into any subplots
    # syntax: [plot-index, plot-location] first enter plot-index and then row and col location of
    # plot to be placed into an 1-D array. Place this array in plot_style['force-plotting']
    # default setting: plot_style['force-plotting'] = [] or no mention of plot_style['force-plotting']
    # example: [2,1,1] this will place second plot at (row=1, col=1)
    #plot_style['force-plotting'] = []
    plot_style['force-plotting'] = [[2, 1, 1], [4, 1, 2], [6, 2, 1], [8, 2, 2], [10, 3, 1], [12, 3, 2]]

    figure = onedim_master_plotter(plot_data, plot_style)
    plt.savefig(output_dir + 'adiabatic_shock_HHeCN0Ne.png')



##########################################################################
# OPTION: 2 ##############################################################
##########################################################################

if option == 2:

    '''
    Plot ionisation profile of Si, S, and Fe behind the shock for
    the adiabatic flow.
    '''

    print('Plotting Si, S, and Fe ionisation profile ...')

    # check for match
    if not abs(get_basic_data(high_resolution_file)['time'].value - get_basic_data(low_resolution_file)[
        'time'].value) <= 1.0E-04:
        warnings.warn(message='Time in two silo file do not match, exiting ...', stacklevel=2)
        exit(0)


    # make plotting data and append to plot_data array
    plot_data = []

    # x data
    x_low = get_basic_data(low_resolution_file)['x']
    x_high = get_basic_data(high_resolution_file)['x']

    #modify x_low data by shifting to left
    x_low = x_low - 2.7e13*np.ones_like(x_low)

    # SILICON ####################################################
    # y data - Silicon species - low resolution
    tracer_list = SILICON_SHOCK_RAY79E
    tracer_labels = SILICON_SHOCK_LABELS
    label_position = [[2.5625e16,0.92], [2.558e16,0.7], [2.550e16,0.62], [2.546e16,0.4], [2.547e16,0.04],
                      [], [], [], [], [], [], [], [], [], []]
    line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
                  'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
                  'magenta', 'magenta', 'magenta', 'magenta']
    line_style = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
    tracer_data_list = get_tracers(low_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over silicon ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_low
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data

    # y data - SILICON species - high resolution
    tracer_list = SILICON_SHOCK_RAY79E
    tracer_labels = SILICON_LABELS
    label_position = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    line_color = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue',
                  'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
    line_style = ['-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(high_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over neon ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_high
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data

    # SULFUR################################################
    # y data - Sulfur species - low resolution
    tracer_list = SULFUR_SHOCK_RAY79E
    tracer_labels = SULFUR_SHOCK_LABELS
    label_position = [[2.5625e16,0.92], [2.558e16,0.7], [2.550e16,0.62], [2.546e16,0.4], [2.547e16,0.04],
                      [], [], [], [], [], [], [], [], [], [], [], []]
    line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
                  'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
                  'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta']
    line_style = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--',
                  '--', '--', '--', '--', '--', '--']
    tracer_data_list = get_tracers(low_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over sulfur ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_low
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data

    # y data - SULFUR species - high resolution
    tracer_list = SULFUR_SHOCK_RAY79E
    tracer_labels = SULFUR_LABELS
    label_position = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]
    line_color = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue',
                  'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
    line_style = ['-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(high_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over sulfur ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_high
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data

    # IFON ####################################################
    # y data - Iron species - low resolution
    tracer_list = IRON_SHOCK_RAY79E
    tracer_labels = IRON_SHOCK_LABELS
    label_position = [[2.5625e16,0.92], [2.558e16,0.7], [2.550e16,0.62], [2.546e16,0.4], [2.547e16,0.04],
                      [], [], [], [], [], [], [], [], [], [], [], [],
                      [], [], [], [], [], [], [], [], [], []]
    line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
                  'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
                  'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
                  'magenta', 'magenta', 'magenta', 'magenta',
                  'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta']
    line_style = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--',
                  '--', '--', '--', '--', '--', '--', '--', '--', '--', '--',
                  '--', '--', '--', '--', '--', '--']
    tracer_data_list = get_tracers(low_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over sulfur ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_low
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data

    # y data - SULFUR species - high resolution
    tracer_list = IRON_SHOCK_RAY79E
    tracer_labels = IRON_LABELS
    label_position = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
                      [], [], [], [], [], [], [], [], [], []]
    line_color = ['blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue',
                  'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue',
                  'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue', 'blue']
    line_style = ['-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-',
                  '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']

    tracer_data_list = get_tracers(high_resolution_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over sulfur ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_high
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data


    # plot style ================================================================
    plot_style = {}
    plot_style['figsize'] = (12, 10)
    plot_style['label-font-size'] = 12
    plot_style['matrix'] = [3, 1]
    plot_style['legend'] = False       # options: True/False
    plot_style['sharex'] = False       # options: True/False, 'col', 'all'
    plot_style['sharey'] = True       # options: True/False, 'col', 'all'

    # insert text in the figure (add several number of text)
    #plot_style['insert-txt'] = [['text', 0, 2, 45],['hi-text', -2, 2, 90]]
    #plot_style['insert-txt'] = []
    plot_style['axis-label'] = [[None, r'\Large{Ioniastion fraction}'],
                                [None, r'\Large{Ioniastion fraction}'],
                                [r'\Large{x (cm)}', r'\Large{Ioniastion fraction}']]
    #plot_style['axis-label'] = []

    plot_style['xlimit'] = [[2.52E+16, 2.58E+16], [2.52E+16, 2.58E+16], [2.52E+16, 2.58E+16],
                            [2.52E+16, 2.6E+16], [2.52E+16, 2.6E+16], [2.52E+16, 2.6E+16],
                            [2.52E+16, 2.6E+16], [2.52E+16, 2.6E+16],
                            [2.52E+16, 2.6E+16], [2.52E+16, 2.6E+16]]

    plot_style['insert-txt'] = [[r'\textbf{Silicon}', 2.522E+16, 3.4, 0],
                                [r'\textbf{Sulfur}', 2.522E+16, 2.2, 0],
                                [r'\textbf{Iron}', 2.522E+16, 0.8, 0]]

    #plot_style['ylimit'] = []

    # plot margin adjustments
    #plot_style['left'] = 0.1  # the left side of the subplots of the figure
    #plot_style['right'] = 0.9   # the right side of the subplots of the figure
    #plot_style['bottom'] = 0.1  # the bottom of the subplots of the figure
    #plot_style['top'] = 0.95    # the top of the subplots of the figure
    #plot_style['wspace'] = 0.05  # the amount of width reserved for blank space between subplots
    #plot_style['hspace'] = 0.05  # the amount of height reserved for white space between subplots

    # this option will force the plot into any subplots
    # syntax: [plot-index, plot-location] first enter plot-index and then row and col location of
    # plot to be placed into an 1-D array. Place this array in plot_style['force-plotting']
    # default setting: plot_style['force-plotting'] = [] or no mention of plot_style['force-plotting']
    # example: [2,1,1] this will place second plot at (row=1, col=1)
    #plot_style['force-plotting'] = []
    plot_style['force-plotting_1d'] = [[2, 1], [4, 2]]

    figure = onedim_master_plotter(plot_data, plot_style)
    plt.savefig(output_dir + 'adiabatic_shock_SiSFe.png')

