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
make_directory('MIM_Publi_Plots')


'''
1. Compare flow quanties of low and high resolution shock test.
low resolution - 1024 grid
high resolution - 10240 grid
'''
low_resolution_file = '/home/tony/Desktop/MIM_Pub_Datafiles/Compare_HL_NRShock/SH1D_n1024_v100_Ray79E_0000.00017408.silo'
high_resolution_file = '/home/tony/Desktop/Simulations/High_Resolution_SH_Test/SH1D_n10240_v100_Ray79E/SH1D_n10240_v100_Ray79E_0000.00174080.silo'

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
    x_low = get_basic_data(low_resolution_file)['x']
    x_high = get_basic_data(high_resolution_file)['x']

    #modify x_low data by shifting to left
    x_low = x_low - 2.7e13*np.ones_like(x_low)

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

    fig, ax = plt.subplots(figsize=(8,6))

    color = 'tab:red'
    ax.set_xlabel(r'$\rm x \, (cm)$', fontsize=18)
    ax.set_ylabel(r'$\rm \rho \, (g/cm^3)$', fontsize=18)
    ax.plot(x_high, get_density(high_resolution_file), color=color, label = r'$\rm \rho$')
    ax.tick_params(axis='y')
    ax.set_xlim(2e+16, 3e+16)
    ax.set_ylim(7e-24, 10e-23)
    ax.legend( loc=(0.85, 0.9), frameon=False)

    ax_2 = ax.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'blue'
    ax_2.set_ylabel(r'$\rm log \, T \, (K)$', fontsize=18)  # we already handled the x-label with ax1
    ax_2.plot(x_high, np.log10(get_temperature(high_resolution_file)), color=color, linestyle='-', label = r'$\rm T$')
    ax_2.tick_params(axis='y')
    ax_2.set_xlim(2.4e+16, 2.7e+16)
    ax_2.set_ylim(3, 7)
    ax_2.legend(loc=(0.85, 0.84), frameon=False)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(axis="both", direction="in", which="both",
                   bottom=True, top=True, left=True, right=True, length=2)

    time = get_basic_data(high_resolution_file)['time']

    print(time)

    plt.savefig('Shock_LH_FQ.png')


