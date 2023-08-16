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
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)


# MAIN **********************************************************************
output_dir = make_directory('INAM_2023')


'''
1. Compare flow quanties of low and high resolution shock test.
low resolution - 1024 grid
high resolution - 10240 grid
'''
v1000_file = '/home/mathew/Desktop/MIM_Pub_Datafiles/RadShock_v3000_vs_v1000/RSH1D_n10240_v1000_Ray79E_0000.00122880.silo'
v3000_file = '/home/mathew/Desktop/MIM_Pub_Datafiles/RadShock_v3000_vs_v1000/RSH1D_n10240_v3000_Ray79E_0000.00512000.silo'

OPTION = 1


# OPTION: 1 ****************************************************************************
if OPTION == 1:

    # x data
    x_v1000 = get_basic_data(v1000_file)['x']
    x_v3000 = get_basic_data(v3000_file)['x']

    plt.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
    plt.rc('text', usetex=True)
    plt.rc('font', **{'size': 12})
    plt.rc('lines', linewidth=1.5)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6, 4), sharex=True)

    # first time instant ++++++++++++++++++++++++++++++++++++++++++++++++++++
    color = 'tab:green'
    #ax1.set_xlabel(r'$\rm x \, (cm)$', fontsize=18)
    ax1.set_ylabel(r'$\rm \rho \, (g/cm^3)$', fontsize=18)
    ax1.plot(x_v1000, get_density(v1000_file), color=color, linestyle='-', label = r'$\rm v_0 = 1000 $')
    ax1.plot(x_v3000, get_density(v3000_file), color='black', linestyle='-', label = r'$\rm v_0 = 3000 $')
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    ax1.tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True, right=True, length=2)
    ax1.set_xlim(0, 1.7e+16)
    #ax.set_ylim(0, 5e-21)
    ax1.legend(frameon=False)

    #ax_2 = ax.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:green'
    ax2.set_xlabel(r'$\rm x \, (cm)$', fontsize=18)
    ax2.set_ylabel(r'$\rm log \, T \, (K)$', fontsize=18)  # we already handled the x-label with ax1
    ax2.plot(x_v1000, np.log10(get_temperature(v1000_file)), color=color, linestyle='-', label = r'$\rm v_0 = 1000 $')
    ax2.plot(x_v3000, np.log10(get_temperature(v3000_file)), color='black', label = r'$\rm v_0 = 3000 $')
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    ax2.tick_params(axis="both", direction="in", which="both", bottom=True, top=False, left=True, right=True, length=2)
    ax2.set_ylim(2, 9)
    ax2.set_xlim(0, 1.7e+16)
    ax2.legend(frameon=False)

    #ax.xaxis.set_minor_locator(AutoMinorLocator())
    #ax.yaxis.set_minor_locator(AutoMinorLocator())
    #ax.tick_params(axis="both", direction="in", which="both",
                 #  bottom=True, top=True, left=True, right=True, length=2)

    plt.subplots_adjust(left=0.1, bottom=0.15, right=0.97, top=0.92, wspace=0.0, hspace=0.0)

    time_1 = get_basic_data(v1000_file)['time']
    print(time_1)
    time_2 = get_basic_data(v3000_file)['time']
    print(time_2)

    plt.savefig(output_dir + 'RS_FlowStruc_v1000_vs_v3000.png', dpi=300)


