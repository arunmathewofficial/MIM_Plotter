# Author: Arun Mathew
# Created: 16-03-2023
# Multi-ion-module-publication plots: flow quantities


# Import required libraries: ##########################################
import warnings
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *

# MAIN **********************************************************************
output_dir = make_directory('INAM_2023')

'''
Compare flow quanties of for radiavive flow at two different time
 - 2024 grid
'''
time1_file = '/home/mathew/Desktop/MIM_Pub_Datafiles/Planar_RadShock_v100/RadShock_n2048_v100_Ray78ModelE/RSH1D_n2048_v100_Ray79E_0000.00020480.silo'
time2_file = '/home/mathew/Desktop/MIM_Pub_Datafiles/Planar_RadShock_v100/RadShock_n2048_v100_Ray78ModelE/RSH1D_n2048_v100_Ray79E_0000.01071104.silo'

OPTION = 1

# OPTION: 1 ****************************************************************************
if OPTION == 1:
    '''

    # check for match
    if not abs(get_basic_data(high_resolution_file)['time'].value - get_basic_data(low_resolution_file)[
        'time'].value) <= 1.0E-04:
        warnings.warn(message='Time in two silo file do not match, exiting ...', stacklevel=2)
        exit(0)

    '''

    # make plotting data and append to plot_data array
    plot_data = []

    # x data
    x_time1 = get_basic_data(time1_file)['x']
    x_time2 = get_basic_data(time2_file)['x']

    # modify x_low data by shifting to left
    #x_low = x_low - 2.7e13 * np.ones_like(x_low)

    '''
    # density ###########################################################
    # y data - density - low resolution
    data_1 = []
    flow_data = {}

    flow_data['labels'] = 'density'
    flow_data['x'] = x_low
    flow_data['y'] = get_density(low_resolution_file)
    flow_data['label-position'] = []
    flow_data['line-color'] = 'magenta'
    flow_data['line-style'] = '-'
    data_1.append(flow_data.copy())
    plot_data.append(data_1)
    del data_1


    # temperature ###########################################################
    # y data - temperature - low resolution
    data_2 = []
    flow_data = {}

    flow_data['labels'] = 'temperature'
    flow_data['x'] = x_low
    flow_data['y'] = get_temperature(high_resolution_file)
    flow_data['label-position'] = []
    flow_data['line-color'] = 'magenta'
    flow_data['line-style'] = '-'
    data_2.append(flow_data.copy())
    plot_data.append(data_2)
    del data_2

    '''

    plt.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
    plt.rc('text', usetex=True)
    plt.rc('font', **{'size': 12})
    plt.rc('lines', linewidth=1.5)

    fig, ax = plt.subplots(figsize=(8, 6))

    color = 'tab:orange'
    ax.set_xlabel(r'$\rm x \, (cm)$', fontsize=18)
    ax.set_ylabel(r'$\rm log \, T \, (K)$', fontsize=18)
    ax.plot(x_time1, np.log10(get_temperature(time1_file)), color=color)
    ax.tick_params(axis='y')
    ax.set_xlim(1e+14, 1.8e+15)
    ax.set_ylim(2.0, 6.0)
    #ax.legend(loc=(0.75, 0.85), frameon=False, fontsize=24)

    text = "time = 5.62 yr"
    plt.text(3.5e+14, 5.7, text, fontsize=12, color='red', ha='center')



    color = 'darkgreen'
    #ax.set_ylabel(r'$\rm log \, T \, (K)$', fontsize=18)  # we already handled the x-label with ax1
    ax.plot(x_time2, np.log10(get_temperature(time2_file)), color=color, linestyle='-')
    ax.tick_params(axis='y')
    ax.set_xlim(1.0e+14, 1.8e+15)   # ax_2.set_ylim(3, 7)
    #ax.legend(loc=(0.75, 0.75), frameon=False, fontsize=24)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(axis="both", direction="in", which="both",
                   bottom=True, top=True, left=True, right=True, length=2)

    text = "time = 294.97 yr"
    plt.text(1.5e+15, 5.6, text, fontsize=12, color='red', ha='center')

    #time = get_basic_data(high_resolution_file)['time']

    #print(time)

    plt.savefig(output_dir + 'RS_logT.png', dpi=300)


