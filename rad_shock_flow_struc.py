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
v100_file_1 = '/home/tony/Desktop/MIM_Pub_Datafiles/Rad_Shock/RSH_n2048_v100/RSH1D_n2048_v100_Ray79E_0000.00020480.silo'
v100_file_2 = '/home/tony/Desktop/MIM_Pub_Datafiles/Rad_Shock/RSH_n2048_v100/RSH1D_n2048_v100_Ray79E_0000.01071104.silo'

OPTION = 1


# OPTION: 1 ****************************************************************************
if OPTION == 1:

    # x data
    x_v100_1 = get_basic_data(v100_file_1)['x']
    x_v100_2 = get_basic_data(v100_file_2)['x']

    plt.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
    plt.rc('text', usetex=True)
    plt.rc('font', **{'size': 12})
    plt.rc('lines', linewidth=1.5)

    fig, ax = plt.subplots(figsize=(8,6))

    # first time instant ++++++++++++++++++++++++++++++++++++++++++++++++++++
    color = 'tab:green'
    ax.set_xlabel(r'$\rm x \, (cm)$', fontsize=18)
    ax.set_ylabel(r'$\rm \rho \, (g/cm^3)$', fontsize=18)
    ax.plot(x_v100_1, get_density(v100_file_1), color=color, label = r'$\rm \rho$', linestyle='--')
    ax.plot(x_v100_2, get_density(v100_file_2), color='black', linestyle='--')
    ax.tick_params(axis='y')
    ax.set_xlim(0, 2e+15)
    #ax.set_ylim(0, 5e-21)
    ax.legend( loc=(0.85, 0.9), frameon=False)

    ax_2 = ax.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:green'
    ax_2.set_ylabel(r'$\rm log \, T \, (K)$', fontsize=18)  # we already handled the x-label with ax1
    ax_2.plot(x_v100_1, np.log10(get_temperature(v100_file_1)), color=color, linestyle='-', label = r'$\rm T$')
    ax_2.plot(x_v100_2, np.log10(get_temperature(v100_file_2)), color='black', linestyle='-')
    ax_2.tick_params(axis='y')
    #ax_2.set_xlim(2.4e+16, 2.7e+16)
    #ax_2.set_ylim(3, 7)
    ax_2.legend(loc=(0.85, 0.84), frameon=False)

    ax.xaxis.set_minor_locator(AutoMinorLocator())
    ax.yaxis.set_minor_locator(AutoMinorLocator())
    ax.tick_params(axis="both", direction="in", which="both",
                   bottom=True, top=True, left=True, right=True, length=2)


    time_1 = get_basic_data(v100_file_1)['time']
    print(time_1)
    time_2 = get_basic_data(v100_file_2)['time']
    print(time_2)

    plt.savefig('RadShock_v100_FQ.png')


