# Author: Arun Mathew
# Created: 11-03-2023
# Multi-ion-module-publication plots: shock test plots


# Import required libraries: ##########################################
import warnings
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *


# MAIN **********************************************************************
output_dir = make_directory('MIM2023_Images')

v1000_file = '/home/mathew/Desktop/MIM_Pub_Datafiles/RadShock_v3000_vs_v1000/RSH1D_n10240_v1000_Ray79E_0000.00122880.silo'
v3000_file = '/home/mathew/Desktop/MIM_Pub_Datafiles/RadShock_v3000_vs_v1000/RSH1D_n10240_v3000_Ray79E_0000.00512000.silo'

#OPTION = 1
'''
1. Comparing the ionisation profile behind the shock for v=1000 km/s flow
Resolution - 10240 grid
# for hydrogen, helium, carbon, nitrogen, oxygen and neon
'''
#OPTION = 2
'''
2. Comparing the ionisation profile behind the shock for 3000 km/s flow.
Resolution - 10240 grid
# for hydrogen, helium, carbon, nitrogen, oxygen and neon
'''
OPTION = 3
'''
3. Comparing the ionisation profile behind the shock for 1000 km/s and 3000 km/s flow.
Resolution - 10240 grid
# for silicon
'''

OPTION = 4
'''
4. Comparing the ionisation profile behind the shock for 1000 km/s and 3000 km/s flow.
Resolution - 10240 grid
# for sulfur
'''

OPTION = 5
'''
5. Comparing the ionisation profile behind the shock for 1000 km/s and 3000 km/s flow.
Resolution - 10240 grid
# for iron
'''

OPTION = 4

# OPTION: 1 ****************************************************************************
if OPTION == 1:

    # make plotting data and append to plot_data array
    plot_data = []

    # x data
    x_v1000 = get_basic_data(v1000_file)['x']

    # Hydrogen ###########################################################
    # y data - Hydrogen species - low velocity
    tracer_list = HYDROGEN_SHOCK_RAY79E
    tracer_labels = HYDROGEN_SHOCK_LABELS
    label_position = [[2.57e16, 0.9], [2.545e16, 0.9]]
    line_color = ['magenta', 'magenta']
    line_style = ['-', '-']
    tracer_data_list = get_tracers(v1000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over hydrogen ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v1000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        # single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add hydrogen species to final plot data
    plot_data.append(species_data)
    del species_data

    # Helium ##############################################################
    # y data - Helium species - low velocity
    tracer_list = HELIUM_SHOCK_RAY79E
    tracer_labels = HELIUM_SHOCK_LABELS
    label_position = [[2.57e16, 0.9], [2.55e16, 0.75], [2.545e16, 0.35]]
    line_color = ['magenta', 'magenta', 'magenta']
    line_style = ['-', '-', '-']
    tracer_data_list = get_tracers(v1000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over helium ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v1000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        # single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add helium species to final plot data
    plot_data.append(species_data)
    del species_data

    # Carbon ####################################################
    # y data - Carbon species - low velocity
    tracer_list = CARBON_SHOCK_RAY79E
    tracer_labels = CARBON_SHOCK_LABELS
    label_position = [[2.5625e16, 0.92], [2.559e16, 0.68], [2.555e16, 0.8], [2.546e16, 0.7], [2.546e16, 0.1], [], []]
    line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta']
    line_style = ['-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(v1000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over Carbon ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v1000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        # single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data

    # NITROGEN ####################################################
    # y data - nitrogen species - low velocity
    tracer_list = NITROGEN_SHOCK_RAY79E
    tracer_labels = NITROGEN_SHOCK_LABELS
    label_position = [[2.5625e16, 0.92], [2.559e16, 0.68], [2.555e16, 0.7], [2.546e16, 0.72], [2.546e16, 0.1], [], [],
                      []]
    line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta']
    line_style = ['-', '-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(v1000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over Carbon ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v1000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        # single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data

    # OXYGEN ####################################################
    # y data - oxygen species - 1000km/s  velocity
    tracer_list = OXYGEN_SHOCK_RAY79E
    tracer_labels = OXYGEN_SHOCK_LABELS
    label_position = [[2.5625e16, 0.92], [2.559e16, 0.68], [2.555e16, 0.7], [2.546e16, 0.72], [2.546e16, 0.1], [], [],
                      [], []]
    line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta']
    line_style = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(v1000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over oxygen ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v1000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        # single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add oxygen species to final plot data
    plot_data.append(species_data)
    del species_data

    # Neon ####################################################
    # y data - Neon species - low resolution
    tracer_list = NEON_SHOCK_RAY79E
    tracer_labels = NEON_SHOCK_LABELS
    label_position = [[2.5625e16, 0.92], [2.558e16, 0.7], [2.550e16, 0.62], [2.546e16, 0.4], [2.547e16, 0.04], [], [],
                      [], [], [], []]
    line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta',
                  'magenta', 'magenta']
    line_style = ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(v1000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over neon ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v1000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        # single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data

    # plot style ================================================================
    plot_style = {}
    plot_style['figsize'] = (12, 14)
    plot_style['label-font-size'] = 12
    plot_style['matrix'] = [3, 2]
    plot_style['legend'] = True  # options: True/False
    plot_style['sharex'] = False  # options: True/False, 'col', 'all'
    plot_style['sharey'] = True  # options: True/False, 'col', 'all'

    # insert text in the figure (add several number of text)
    plot_style['insert-txt'] = [[r'{\Large Hydrogen}', -2.3E+15, 3.5, 0],
                                [r'{\Large Helium}', 3.2E+15, 3.5, 0],
                                [r'{\Large Carbon}', -2.3E+15, 2.25, 0],
                                [r'{\Large Nitrogen}', 3.2E+15, 2.25, 0],
                                [r'{\Large Oxygen}', -2.3E+15, 0.95, 0],
                                [r'{\Large Neon}', 3.2E+15, 0.95, 0]]

    # plot_style['insert-txt'] = []
    plot_style['axis-label'] = [[None, r'\huge{Ioniastion fraction}'], [None, None],
                                [None, r'\huge{Ioniastion fraction}'], [None, None],
                                [r'\huge{x (cm)}', r'\huge{Ioniastion fraction}'], [r'\huge{x (cm)}', None]]
    # plot_style['axis-label'] = []

    plot_style['xlimit'] = [[6e+15, 8.5e+15], [6e+15, 8.5e+15], [3e+15, 9e+15], [3e+15, 9e+15], [3e+15, 9e+15],
                            [3e+15, 9e+15]]

    #plot_style['xlimit'] = []

    # plot_style['ylimit'] = []

    # plot margin adjustments
    plot_style['left'] = 0.1  # the left side of the subplots of the figure
    plot_style['right'] = 0.9  # the right side of the subplots of the figure
    plot_style['bottom'] = 0.1  # the bottom of the subplots of the figure
    plot_style['top'] = 0.95  # the top of the subplots of the figure
    plot_style['wspace'] = 0.1  # the amount of width reserved for blank space between subplots
    plot_style['hspace'] = 0.2  # the amount of height reserved for white space between subplots

    # this option will force the plot into any subplots
    # syntax: [plot-index, plot-location] first enter plot-index and then row and col location of
    # plot to be placed into an 1-D array. Place this array in plot_style['force-plotting']
    # default setting: plot_style['force-plotting'] = [] or no mention of plot_style['force-plotting']
    # example: [2,1,1] this will place second plot at (row=1, col=1)
    # plot_style['force-plotting'] = []
    # plot_style['force-plotting'] = [[2, 1, 1], [4, 1, 2], [6, 2, 1], [8, 2, 2], [10, 3, 1], [12, 3, 2]]

    figure = onedim_master_plotter(plot_data, plot_style)
    plt.savefig(output_dir + 'RadShock_v1000_HHeCN0Ne.png')



# OPTION: 2 ****************************************************************************
if OPTION == 2:

    # make plotting data and append to plot_data array
    plot_data = []

    # x data
    x_v3000 = get_basic_data(v3000_file)['x']

    # Hydrogen ###########################################################
    # y data - Hydrogen species - low velocity
    tracer_list = HYDROGEN_SHOCK_RAY79E
    tracer_labels = HYDROGEN_SHOCK_LABELS
    label_position = [[2.57e16,0.9], [2.545e16,0.9]]
    line_color = ['magenta', 'magenta']
    line_style = ['-', '-']
    tracer_data_list = get_tracers(v3000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over hydrogen ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v3000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        #single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add hydrogen species to final plot data
    plot_data.append(species_data)
    del species_data
    

    # Helium ##############################################################
    # y data - Helium species - low velocity
    tracer_list = HELIUM_SHOCK_RAY79E
    tracer_labels = HELIUM_SHOCK_LABELS
    label_position = [[2.57e16,0.9], [2.55e16,0.75], [2.545e16,0.35]]
    line_color = ['magenta', 'magenta', 'magenta']
    line_style = ['-', '-', '-']
    tracer_data_list = get_tracers(v3000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over helium ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v3000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        #single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add helium species to final plot data
    plot_data.append(species_data)
    del species_data

    # Carbon ####################################################
    # y data - Carbon species - low velocity
    tracer_list = CARBON_SHOCK_RAY79E
    tracer_labels = CARBON_SHOCK_LABELS
    label_position = [[2.5625e16,0.92], [2.559e16,0.68], [2.555e16,0.8], [2.546e16,0.7], [2.546e16,0.1], [], []]
    line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta']
    line_style = ['-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(v3000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over Carbon ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v3000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        #single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data


    # NITROGEN ####################################################
    # y data - nitrogen species - low velocity
    tracer_list = NITROGEN_SHOCK_RAY79E
    tracer_labels = NITROGEN_SHOCK_LABELS
    label_position = [[2.5625e16,0.92], [2.559e16,0.68], [2.555e16,0.7], [2.546e16,0.72], [2.546e16,0.1], [], [], []]
    line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta']
    line_style = ['-', '-', '-', '-', '-', '-', '-', '-']
    tracer_data_list = get_tracers(v3000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over Carbon ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v3000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        #single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data

    # OXYGEN ####################################################
    # y data - oxygen species - low velocity
    tracer_list = OXYGEN_SHOCK_RAY79E
    tracer_labels = OXYGEN_SHOCK_LABELS
    label_position = [[2.5625e16,0.92], [2.559e16,0.68], [2.555e16,0.7], [2.546e16,0.72], [2.546e16,0.1], [], [], [], []]
    line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta']
    line_style = ['-', '-', '-', '-', '-', '-', '-',  '-', '-']
    tracer_data_list = get_tracers(v3000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over oxygen ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v3000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        #single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add oxygen species to final plot data
    plot_data.append(species_data)
    del species_data

    # Neon ####################################################
    # y data - Neon species - low resolution
    tracer_list = NEON_SHOCK_RAY79E
    tracer_labels = NEON_SHOCK_LABELS
    label_position = [[2.5625e16,0.92], [2.558e16,0.7], [2.550e16,0.62], [2.546e16,0.4], [2.547e16,0.04], [], [], [], [], [], []]
    line_color = ['magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta', 'magenta']
    line_style = ['-', '-', '-', '-', '-', '-', '-',  '-', '-', '-', '-']
    tracer_data_list = get_tracers(v3000_file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over neon ions
    species_data = []
    single_species_data = {}
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracer_labels[i]
        single_species_data['x'] = x_v3000
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        #single_species_data['line-color'] = line_color[i]
        single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data

    # plot style ================================================================
    plot_style = {}
    plot_style['figsize'] = (12, 14)
    plot_style['label-font-size'] = 12
    plot_style['matrix'] = [3, 2]
    plot_style['legend'] = True       # options: True/False
    plot_style['sharex'] = False       # options: True/False, 'col', 'all'
    plot_style['sharey'] = True       # options: True/False, 'col', 'all'

    # insert text in the figure (add several number of text)
    plot_style['insert-txt'] = [[r'{\Large Hydrogen}', 7.3E+15, 3.5, 0],
                                [r'{\Large Helium}', 8.05E+15, 3.5, 0],
                                [r'{\Large Carbon}', 7.3E+15, 2.25, 0],
                                [r'{\Large Nitrogen}', 8.05E+15, 2.25,0],
                                [r'{\Large Oxygen}', 7.3E+15, 0.95, 0],
                                [r'{\Large Neon}', 8.05E+15, 0.95, 0]]

    #plot_style['insert-txt'] = []
    plot_style['axis-label'] = [[None, r'\huge{Ioniastion fraction}'], [None, None],
                                [None, r'\huge{Ioniastion fraction}'], [None, None],
                                [r'\huge{x (cm)}', r'\huge{Ioniastion fraction}'], [r'\huge{x (cm)}', None]]
    #plot_style['axis-label'] = []

    plot_style['xlimit'] = [[8e+15, 8.7e+15], [8e+15, 8.7e+15], [8e+15, 8.7e+15], [8e+15, 8.7e+15], [8e+15, 8.7e+15],
                            [8e+15, 8.7e+15]]

    #plot_style['ylimit'] = []

    # plot margin adjustments
    plot_style['left'] = 0.1  # the left side of the subplots of the figure
    plot_style['right'] = 0.9   # the right side of the subplots of the figure
    plot_style['bottom'] = 0.1  # the bottom of the subplots of the figure
    plot_style['top'] = 0.95    # the top of the subplots of the figure
    plot_style['wspace'] = 0.1  # the amount of width reserved for blank space between subplots
    plot_style['hspace'] = 0.2  # the amount of height reserved for white space between subplots

    # this option will force the plot into any subplots
    # syntax: [plot-index, plot-location] first enter plot-index and then row and col location of
    # plot to be placed into an 1-D array. Place this array in plot_style['force-plotting']
    # default setting: plot_style['force-plotting'] = [] or no mention of plot_style['force-plotting']
    # example: [2,1,1] this will place second plot at (row=1, col=1)
    #plot_style['force-plotting'] = []
    #plot_style['force-plotting'] = [[2, 1, 1], [4, 1, 2], [6, 2, 1], [8, 2, 2], [10, 3, 1], [12, 3, 2]]

    figure = onedim_master_plotter(plot_data, plot_style)
    plt.savefig(output_dir + 'RadShock_v3000_HHeCN0Ne.png')


# OPTION: 3 SILICON ****************************************************************
if OPTION == 3:

    # make plotting data and append to plot_data array
    plot_data = []
    # x data for v=1000 km/s
    x_v1000 = get_basic_data(v1000_file)['x']
    # x data for v=3000 km/s
    x_v3000 = get_basic_data(v3000_file)['x']

    # SILICON ####################################################
    # y data - Silicon species - 1000 km/s velocity
    tracer_list = SILICON_SHOCK_RAY79E
    tracer_labels = SILICON_SHOCK_LABELS
    label_position = [[2.5625e16,0.92], [2.558e16,0.7], [2.550e16,0.62], [2.546e16,0.4], [2.547e16,0.04],
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
        #single_species_data['line-color'] = line_color[i]
        #single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data


    # SILICON ####################################################
    # y data - Silicon species - 3000 km/s velocity
    tracer_list = SILICON_SHOCK_RAY79E
    tracer_labels = SILICON_SHOCK_LABELS
    label_position = [[2.5625e16,0.92], [2.558e16,0.7], [2.550e16,0.62], [2.546e16,0.4], [2.547e16,0.04],
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
        #single_species_data['line-color'] = line_color[i]
        #single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data

    # plot style ================================================================
    plot_style = {}
    plot_style['figsize'] = (12, 8)
    plot_style['label-font-size'] = 12
    plot_style['matrix'] = [2, 1]
    plot_style['legend'] = False       # options: True/False
    plot_style['sharex'] = False       # options: True/False, 'col', 'all'
    plot_style['sharey'] = True       # options: True/False, 'col', 'all'

    # insert text in the figure (add several number of text)
    #plot_style['insert-txt'] = [['text', 0, 2, 45],['hi-text', -2, 2, 90]]
    #plot_style['insert-txt'] = []
    plot_style['axis-label'] = [[None, r'\Large{Ioniastion fraction}'],
                                [r'\Large{x (cm)}', r'\Large{Ioniastion fraction}']]
    #plot_style['axis-label'] = []

    plot_style['xlimit'] = [[2e+15, 8e+15], [6e+15, 8.7e+15], [6e+15, 8.7e+15], [6e+15, 8.7e+15]]

    plot_style['insert-txt'] = [[r"${\rm \huge v_0 = 1000 \, km/s}$", 6.2E+15, 2.2, 0],
                                [r"${\rm v_0 = 3000 \, km/s}$", 6.2E+15, 0.9, 0]]


    #plot_style['ylimit'] = []

    # plot margin adjustments
    plot_style['left'] = 0.05  # the left side of the subplots of the figure
    plot_style['right'] = 0.9   # the right side of the subplots of the figure
    plot_style['bottom'] = 0.1  # the bottom of the subplots of the figure
    plot_style['top'] = 0.95    # the top of the subplots of the figure
    #plot_style['wspace'] = 0.05  # the amount of width reserved for blank space between subplots
    #plot_style['hspace'] = 0.05  # the amount of height reserved for white space between subplots

    # this option will force the plot into any subplots
    # syntax: [plot-index, plot-location] first enter plot-index and then row and col location of
    # plot to be placed into an 1-D array. Place this array in plot_style['force-plotting']
    # default setting: plot_style['force-plotting'] = [] or no mention of plot_style['force-plotting']
    # example: [2,1,1] this will place second plot at (row=1, col=1)
    #plot_style['force-plotting'] = []
    #plot_style['force-plotting_1d'] = [[2, 1], [4, 2]]

    figure = onedim_master_plotter(plot_data, plot_style)
    plt.savefig(output_dir + 'RadShock_v3000_vs_v1000_Si.png')



# OPTION: 4 ****************************************************************************
if OPTION == 4:

    # make plotting data and append to plot_data array
    plot_data = []
    # x data for v=1000 km/s
    x_v1000 = get_basic_data(v1000_file)['x']
    # x data for v=3000 km/s
    x_v3000 = get_basic_data(v3000_file)['x']

    # SULFUR ################################################
    # y data - Sulfur species 1000 km/s
    tracer_list = SULFUR_SHOCK_RAY79E
    tracer_labels = SULFUR_SHOCK_LABELS
    label_position = [[2.5625e16,0.92], [2.558e16,0.7], [2.550e16,0.62], [2.546e16,0.4], [2.547e16,0.04],
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
        #single_species_data['line-color'] = line_color[i]
        #single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data


    # SULFUR ################################################
    # y data - Sulfur species 3000 km/s
    tracer_list = SULFUR_SHOCK_RAY79E
    tracer_labels = SULFUR_SHOCK_LABELS
    label_position = [[2.5625e16,0.92], [2.558e16,0.7], [2.550e16,0.62], [2.546e16,0.4], [2.547e16,0.04],
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
        #single_species_data['line-color'] = line_color[i]
        #single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data

    # plot style ================================================================
    plot_style = {}
    plot_style['figsize'] = (12, 8)
    plot_style['label-font-size'] = 12
    plot_style['matrix'] = [2, 1]
    plot_style['legend'] = False       # options: True/False
    plot_style['sharex'] = False       # options: True/False, 'col', 'all'
    plot_style['sharey'] = True       # options: True/False, 'col', 'all'

    # insert text in the figure (add several number of text)
    #plot_style['insert-txt'] = [['text', 0, 2, 45],['hi-text', -2, 2, 90]]
    #plot_style['insert-txt'] = []
    plot_style['axis-label'] = [[None, r'\Large{\rm Ioniastion fraction}'],
                                [r'\Large{\rm x (cm)}', r'\Large{\rm Ioniastion fraction}']]
    #plot_style['axis-label'] = []

    plot_style['xlimit'] = [[2e+15, 8e+15], [6e+15, 8.7e+15], [6e+15, 8.7e+15], [6e+15, 8.7e+15]]

    plot_style['insert-txt'] = [[r"${\rm \huge v_0 = 1000 \, km/s}$", 6.2E+15, 2.2, 0],
                                [r"${\rm v_0 = 3000 \, km/s}$", 6.2E+15, 0.9, 0]]


    #plot_style['ylimit'] = []

    # plot margin adjustments
    plot_style['left'] = 0.05  # the left side of the subplots of the figure
    plot_style['right'] = 0.980   # the right side of the subplots of the figure
    plot_style['bottom'] = 0.09  # the bottom of the subplots of the figure
    plot_style['top'] = 0.88    # the top of the subplots of the figure
    #plot_style['wspace'] = 0.05  # the amount of width reserved for blank space between subplots
    plot_style['hspace'] = 0.23  # the amount of height reserved for white space between subplots

    # this option will force the plot into any subplots
    # syntax: [plot-index, plot-location] first enter plot-index and then row and col location of
    # plot to be placed into an 1-D array. Place this array in plot_style['force-plotting']
    # default setting: plot_style['force-plotting'] = [] or no mention of plot_style['force-plotting']
    # example: [2,1,1] this will place second plot at (row=1, col=1)
    #plot_style['force-plotting'] = []
    #plot_style['force-plotting_1d'] = [[2, 1], [4, 2]]

    figure = onedim_master_plotter(plot_data, plot_style)
    plt.savefig(output_dir + 'RadShock_v3000_vs_v1000_S.png')



# OPTION: 5 IRON ****************************************************************************
if OPTION == 5:

    # make plotting data and append to plot_data array
    plot_data = []
    # x data for v=1000 km/s
    x_v1000 = get_basic_data(v1000_file)['x']
    # x data for v=3000 km/s
    x_v3000 = get_basic_data(v3000_file)['x']

    # IFON ####################################################
    # y data - Iron species - 1000 km/s velocity
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
        #single_species_data['line-color'] = line_color[i]
        #single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data

    # IFON ####################################################
    # y data - Iron species - 3000 km/s velocity
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
        #single_species_data['line-color'] = line_color[i]
        #single_species_data['line-style'] = line_style[i]
        species_data.append(single_species_data.copy())
    # add neon species to final plot data
    plot_data.append(species_data)
    del species_data


    # plot style ================================================================
    plot_style = {}
    plot_style['figsize'] = (12, 8)
    plot_style['label-font-size'] = 12
    plot_style['matrix'] = [2, 1]
    plot_style['legend'] = True       # options: True/False
    plot_style['sharex'] = False       # options: True/False, 'col', 'all'
    plot_style['sharey'] = True       # options: True/False, 'col', 'all'

    # insert text in the figure (add several number of text)
    #plot_style['insert-txt'] = [['text', 0, 2, 45],['hi-text', -2, 2, 90]]
    #plot_style['insert-txt'] = []
    plot_style['axis-label'] = [[None, r'\Large{\rm Ioniastion fraction}'],
                                [r'\Large{\rm x (cm)}', r'\Large{\rm Ioniastion fraction}']]
    #plot_style['axis-label'] = []

    plot_style['xlimit'] = [[6e+15, 8.0e+15], [7e+15, 8.7e+15]]

    plot_style['insert-txt'] = [[r"${\rm \huge v_0 = 1000 \, km/s}$", 7.1E+15, 2.2, 0],
                                [r"${\rm v_0 = 3000 \, km/s}$", 7.1E+15, 0.9, 0]]

    #plot_style['ylimit'] = []

    # plot margin adjustments
    plot_style['left'] = 0.05  # the left side of the subplots of the figure
    plot_style['right'] = 0.97   # the right side of the subplots of the figure
    plot_style['bottom'] = 0.1  # the bottom of the subplots of the figure
    plot_style['top'] = 0.85    # the top of the subplots of the figure
    #plot_style['wspace'] = 0.1  # the amount of width reserved for blank space between subplots
    plot_style['hspace'] = 0.23  # the amount of height reserved for white space between subplots

    # this option will force the plot into any subplots
    # syntax: [plot-index, plot-location] first enter plot-index and then row and col location of
    # plot to be placed into an 1-D array. Place this array in plot_style['force-plotting']
    # default setting: plot_style['force-plotting'] = [] or no mention of plot_style['force-plotting']
    # example: [2,1,1] this will place second plot at (row=1, col=1)
    #plot_style['force-plotting'] = []
    #plot_style['force-plotting_1d'] = [[2, 1], [4, 2]]

    figure = onedim_master_plotter(plot_data, plot_style)
    plt.savefig(output_dir + 'RadShock_v3000_vs_v1000_Fe.png')
