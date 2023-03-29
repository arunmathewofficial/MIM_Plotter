# Author: Arun Mathew
# Created: 07-03-2023
# Multi-ion-module-publication plots:

# New comments:
# 2022-11-09 AM: scripted H and He OneDGrid_Plotter
# 2022-11-10 AM: scripted C, O, N OneDGrid_Plotter

# Import required libraries: ##########################################
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *


# MAIN **********************************************************************
make_directory('MIM_Publi_Plots')

'''
1. Ion fraction of Hydrogen, Helium and Carbon for CIE with Asplund 2009 abundances
'''
file = '/home/tony/Desktop/Simulations/CIE_Asplund2009/testCIE_mpv10_0000.06963200.silo'


'''
2. Compare the ion fraction of Helium, Carbon  and Nitrogen for Asplund2009 and Eatson2022 abundances 
'''
asplund_cie_silofile = '/home/tony/Desktop/MIM_Pub_Datafiles/CIE_Asplund2009/testCIE_mpv10_0000.06963200.silo'
eatson_cie_silofile = '/home/tony/Desktop/MIM_Pub_Datafiles/CIE_Eatson2022/CIE_Eatson2002_n128_0000.02284404.silo'


OPTION = 1


# OPTION: 1 ****************************************************************************
if OPTION == 1:
    '''
    1. Ion fraction of Hydrogen, Helium and Carbon for CIE with Asplund 2009 abundances
    '''
    # make plotting data and append to plot_data array
    plot_data = []

    # x data
    temperature = get_temperature(file)
    temperature = np.log10(temperature)

    # y data - Hydrogen species.
    tracer_list = HYDROGEN_CIE_ASPLUND2009
    tracer_labels = HYDROGEN_CIE_LABELS
    label_position = [[4.0, 0.88], [4.4, 0.88]]
    line_color = ['green', 'green']
    line_style = ['-', '-']
    tracer_data_list = get_tracers(file, tracer_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
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

    # y data - Helium species.
    tracers_list = HELIUM_CIE_ASPLUND2009
    tracers_labels = HELIUM_CIE_LABELS
    label_position = [[], [4.6, 0.8], [5.05, 0.8]]
    line_color = ['orange', 'orange', 'orange']
    line_style = ['--', '--', '--']
    tracer_data_list = get_tracers(file, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
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

    # y data - Carbon species.
    tracers_list = CARBON_CIE_ASPLUND2009
    tracers_labels = CARBON_CIE_LABELS
    label_position = [[4.05, 0.6], [4.75, 0.3], [4.86, 0.73], [5.15, 0.2], [5.5, 0.85], [6.01, 0.6], [6.5, 0.85]]
    line_color = ['black', 'black', 'black', 'black', 'black', 'black', 'black']
    line_style = [':', ':', ':', ':', ':', ':', ':']
    tracer_data_list = get_tracers(file, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
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

    # y data - Nitrogen species.
    tracers_list = NITROGEN_CIE_ASPLUND2009
    tracers_labels = NITROGEN_CIE_LABELS
    label_position = [[4.0, 0.9], [4.46, 0.85], [4.86, .68], [5.13, 0.62], [5.35, 0.2], [5.5, 1.0], [6.2, 0.36], [6.6, 1.0]]
    line_color = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
    line_style = ['--', '--', '--', '--', '--', '--', '--', '--']
    tracer_data_list = get_tracers(file, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
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


    # y data - Oxygen species.
    tracers_list = OXYGEN_CIE_ASPLUND2009
    tracers_labels = OXYGEN_CIE_LABELS
    label_position = [[], [], [], [], [5.4, 0.55], [5.6, 0.15], [6.1, 0.96], [6.35, 0.48], [6.7, 0.85]]
    line_color = ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange']
    line_style = [':', ':', ':', ':', ':', ':', ':', ':', ':']
    tracer_data_list = get_tracers(file, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
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


    # y data - neon species.
    tracers_list = NEON_CIE_ASPLUND2009
    tracers_labels = NEON_CIE_LABELS
    label_position = [[], [], [], [], [5.4, 0.55], [5.6, 0.15], [6.1, 0.96], [6.35, 0.48], [6.7, 0.85], [], []]
    line_color = ['orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange', 'orange' ]
    line_style = [':', ':', ':', ':', ':', ':', ':', ':', ':', ':', ':']
    tracer_data_list = get_tracers(file, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
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

    # y data - silicon species.
    tracers_list = SILICON_CIE_ASPLUND2009
    tracers_labels = SILICON_CIE_LABELS
    label_position = [[], [], [], [], [5.4, 0.55], [5.6, 0.15], [6.1, 0.96], [6.35, 0.48], [6.7, 0.85], [], [],
                      [], [], [], [], ]
    line_color = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green',
                  'green', 'green', 'green', 'green', 'green', 'green', 'green']
    line_style = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
    tracer_data_list = get_tracers(file, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
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


    # y data - sulfur species.
    tracers_list = SULFUR_CIE_ASPLUND2009
    tracers_labels = SULFUR_CIE_LABELS
    label_position = [[], [], [], [], [5.4, 0.55], [5.6, 0.15], [6.1, 0.96], [6.35, 0.48], [6.7, 0.85], [], [],
                      [], [], [], [], [], []]
    line_color = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green',
                  'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
    line_style = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
    tracer_data_list = get_tracers(file, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
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


    # y data - iron species.
    tracers_list = IRON_CIE_ASPLUND2009
    tracers_labels = IRON_CIE_LABELS
    label_position = [[], [], [], [], [5.4, 0.55], [5.6, 0.15], [6.1, 0.96], [6.35, 0.48], [6.7, 0.85], [], [],
                      [], [], [], [], [], [], [], [], [], [], [5.4, 0.55], [5.6, 0.15], [6.1, 0.96],
                      [6.35, 0.48], [6.7, 0.85], [], []]
    line_color = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green',
                  'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green',
                  'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green',
                  'green', 'green', 'green']
    line_style = ['--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--',
                  '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--', '--']
    tracer_data_list = get_tracers(file, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
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
    plot_style['figsize'] = (12, 16)
    plot_style['label-font-size'] = 12
    plot_style['matrix'] = [4, 1]
    plot_style['legend'] = False       # options: True/False
    plot_style['sharex'] = False       # options: True/False, 'col', 'all'
    plot_style['sharey'] = False       # options: True/False, 'col', 'all'

    plot_style['xlimit'] = [[3.7, 6.8], [3.7, 7], [3.7, 8], [3.7, 8.5]]

    plot_style['force-plotting_1d'] = [[2, 1], [3, 1], [5, 2], [6, 2], [8, 3]]

    plot_style['axis-label'] = [[None, 'ioniastion fraction'],
                                [None, 'ioniastion fraction'],
                                [None, 'ioniastion fraction'],
                                ['log(T) K', 'ioniastion fraction']]

    plot_style['insert-txt'] = []

    # plot margin adjustments
    plot_style['left'] = 0.1  # the left side of the subplots of the figure
    plot_style['right'] = 0.9   # the right side of the subplots of the figure
    plot_style['bottom'] = 0.1  # the bottom of the subplots of the figure
    plot_style['top'] = 0.95    # the top of the subplots of the figure
    plot_style['wspace'] = 0.0  # the amount of width reserved for blank space between subplots
    plot_style['hspace'] = 0.1  # the amount of height reserved for white space between subplots

    onedim_master_plotter(plot_data, plot_style)
    plt.savefig('CIE_Asplund2002.png')
# END OF OPTION 1 ***************************************************************




# OPTION: 2 ****************************************************************************
if OPTION == 2:
    '''
    Compare the ion fraction of Helium, Carbon  and Nitrogen for Asplund2009 and
    Eatson2022 abundances 
    '''
    # make plotting data and append to plot_data array
    plot_data = []

    # plot-1 Helium Asplund 2009 ==============================================
    # x data - Helium species for Asplund 2009
    temperature = get_temperature(asplund_cie_silofile)
    temperature = np.log10(temperature)

    # y data - Helium species for Asplund 2009
    tracers_list = HELIUM_CIE_ASPLUND2009
    tracers_labels = HELIUM_LABELS
    label_position = [[], [], []]
    tracer_data_list = get_tracers(asplund_cie_silofile, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over helium ions and append the details in species data
    species_data = []
    single_species_data = {}
    single_species_data['file'] = asplund_cie_silofile
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracers_labels[i]
        single_species_data['x'] = temperature
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        species_data.append(single_species_data.copy())
    # add helium species to final plot data
    plot_data.append(species_data)
    del species_data

    # plot-2 Helium Eatson 2022 ==============================================
    # x data - Helium species Eatson 2022
    temperature = get_temperature(eatson_cie_silofile)
    temperature = np.log10(temperature)

    # y data - Helium species Eatson 2022
    tracers_list = HELIUM_CIE_EATSON2022
    tracers_labels = HELIUM_LABELS
    label_position = [[], [], []]
    tracer_data_list = get_tracers(eatson_cie_silofile, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over helium ions and append the details in species data
    species_data = []
    single_species_data = {}
    single_species_data['file'] = eatson_cie_silofile
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracers_labels[i]
        single_species_data['x'] = temperature
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        species_data.append(single_species_data.copy())
    # add helium species to final plot data
    plot_data.append(species_data)
    del species_data

    # plot-3 Carbon Asplund 2009 ==============================================
    # x data - Carbon species for Asplund 2009
    temperature = get_temperature(asplund_cie_silofile)
    temperature = np.log10(temperature)

    # y data - Carbon species.
    tracers_list = CARBON_CIE_ASPLUND2009
    tracers_labels = CARBON_LABELS
    label_position = [[], [], [], [], [], [], []]
    tracer_data_list = get_tracers(asplund_cie_silofile, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over carbon ions and append the details in species data
    species_data = []
    single_species_data = {}
    single_species_data['file'] = asplund_cie_silofile
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracers_labels[i]
        single_species_data['x'] = temperature
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data

    # plot-4 Carbon Eatson 2022 ==============================================
    # x data - Carbon species Eatson 2022
    temperature = get_temperature(eatson_cie_silofile)
    temperature = np.log10(temperature)

    # y data - Carbon species.
    tracers_list = CARBON_CIE_EATSON2022
    tracers_labels = CARBON_LABELS
    label_position = [[], [], [], [], [], [], []]
    tracer_data_list = get_tracers(eatson_cie_silofile, tracers_list)
    normalisation_factor = tracer_data_list[0]
    pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
    # loop over carbon ions and append the details in species data
    species_data = []
    single_species_data = {}
    single_species_data['file'] = eatson_cie_silofile
    for i in range(len(pro_tracer_data_list)):
        single_species_data['labels'] = tracers_labels[i]
        single_species_data['x'] = temperature
        single_species_data['y'] = pro_tracer_data_list[i]
        single_species_data['label-position'] = label_position[i]
        species_data.append(single_species_data.copy())
    # add carbon species to final plot data
    plot_data.append(species_data)
    del species_data

    # plot style ================================================================
    plot_style = {}
    plot_style['figsize'] = (9, 16)
    plot_style['label_font_size'] = 12
    plot_style['matrix'] = [4, 1]
    plot_style['legend'] = True       # options: True/False
    plot_style['sharex'] = True       # options: True/False, 'col', 'all'
    plot_style['sharey'] = True       # options: True/False, 'col', 'all'

    # insert text in the figure (add several number of text)
    #plot_style['insert-txt'] = [['text', 0, 2, 45],['hi-text', -2, 2, 90]]
    plot_style['insert-txt'] = []
    plot_style['axis_label'] = [[None, 'ioniastion fraction'], [None, None],
                                ['log(T) K', 'ioniastion fraction'], ['log(T) K', None]]
    #plot_style['axis_label'] = []
    #plot_style['axis_limit'] = [[], [], [], [], ]

    plot_style['left'] = 0.125  # the left side of the subplots of the figure
    plot_style['right'] = 0.9   # the right side of the subplots of the figure
    plot_style['bottom'] = 0.1  # the bottom of the subplots of the figure
    plot_style['top'] = 0.9     # the top of the subplots of the figure
    plot_style['wspace'] = 0.05  # the amount of width reserved for blank space between subplots
    plot_style['hspace'] = 0.05  # the amount of height reserved for white space between subplots

    onedim_master_plotter(plot_data, plot_style)
    plt.show()
# END OF OPTION 2 ***************************************************************
















'''

#############################################################
print('*************** PYPION TOOLKIT : TRACER PLOT *****************')
# Exit if not 1D data
if dimension == "1D":
    print('Plotting 1D silo data ...')
else:
    print('Not 1D data, exiting ...')
    quit()



# Figure parameters ############################################################
fig_rows = 2 # number of rows in the figure
fig_cols = 1 # number of cols in the figure
#xlimit = [0e+15, 1.6e+15] # limit x range of the plot with this interval, empty = default
xlimit = [3.0,8.5] # limit x range of the plot with this interval, empty = default
ylimit = [] # limit y range of the plot with this interval, empty = default
resolution = 300 # control the resolution of the output image
figsize = (3,4) # set the size of the image, set to 'None' for default
axislabel = [r'log(T) K', 'ionisation fraction'] # axis labels
split = [14,13]
print2file = True
plot_info = [fig_rows, fig_cols, xlimit, ylimit, figsize, axislabel, split, print2file]


imagefile_count = 0
# Call OneDGrid_Advanced_Plotter for every time instant
for frame in timeline:
    data = timeline[frame]

    silo_tracer_plot = Silo_Plotter(data)
    output = silo_tracer_plot.OneDGrid_Advanced_Tracer_Plotter(x_info, tracer_list, tracer_namelist, plot_info)
    print('[Time {:.2e}]'.format(output['time']), 'Saving image:' + str(imagefile_count).zfill(4))
    imagefile = "%s%s%s_%s.png" % (OutputDir, Inputs.img_file, plot_name, str(imagefile_count).zfill(3))

    if print2file == True:
        textfile = "%s%s%s_%s.txt" % (OutputDir, Inputs.img_file, plot_name, str(imagefile_count).zfill(3))
        table = pd.DataFrame(output['data'])
        table.to_csv(textfile, float_format='%.5e')

    plt.savefig(imagefile, bbox_inches='tight', dpi=resolution)
    imagefile_count += 1
    plt.close()
    silo_tracer_plot.close()


print('*************** PYPION TOOLKIT : TRACER PLOT *****************')

'''