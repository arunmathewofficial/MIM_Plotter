# Author: Arun Mathew
# Created: 10-11-2022
# Ionization Flow Mapper: It plots the temperature, density, and hydrogen
# ionization profiles for all planar shock tests and wind-wind interactions.
# This tool serves as a debugging aid for the mpv10 module.

import matplotlib.pyplot as plt
from pypion.argparse_command import InputValues
from tools import *
import numpy as np
import astropy.units as u
import astropy.constants as const

Inputs = InputValues()
timeline = Inputs.time_dicts
dimension = Inputs.dimen
OutputDir = Inputs.img_path
imgbase = Inputs.img_file

OneParsec = 3.086e+18
# convert the x-axis into parsec scale
cm2pc = False

# minimum and maximum value of x-axis in cm


for i, frame in enumerate(timeline):
    silo_file = timeline[frame][0]

    time = get_basic_data(silo_file)['time']
    print(time)
    Temperature = get_temperature(silo_file)
    Density = get_density(silo_file)
    xaxis = get_basic_data(silo_file)['x']
    x_label = "cm"

    '''
    if cm2pc == True:
        if xaxis[-1].value < OneParsec:
            pass
        else:
            xaxis = xaxis * (unit.cm).to(unit.pc)
            x_label = "pc"
    '''

    norm = get_tracer(silo_file, 'Tr000_X_H')
    H0 = get_tracer(silo_file, 'Tr009_H')
    H1p = get_tracer(silo_file, 'Tr000_X_H') - get_tracer(silo_file, 'Tr009_H')

    fig, axs = plt.subplots(3, 1, figsize=(8, 8))
    axs[0].plot(xaxis, np.log10(Temperature))
    axs[0].set_xlabel(x_label)
    axs[0].set_ylabel("$\log T (K)$")
    #axs[0].tick_params(labelsize=16)
    #axs[0].grid()
    #axs[0].legend(fontsize=12, loc="lower right")
    #axs[0].set_xlim(x_min, x_max)

    axs[1].plot(xaxis, np.log10(Density))  # Corrected label
    axs[1].set_xlabel(x_label)
    axs[1].set_ylabel("$\log(\\rho)$")
    #axs[1].tick_params(labelsize=16)
    #axs[1].grid()
    #axs[1].legend(fontsize=12, loc="lower right")
    #axs[1].set_xlim(x_min, x_max)

    axs[2].plot(xaxis, H0/norm , label='H0')
    axs[2].plot(xaxis, H1p/norm, label='H1+')
    axs[2].set_xlabel(x_label)
    axs[2].set_ylabel("Ionisation fraction")
    #axs[2].set_xlim(x_min, x_max)
    #axs[2].tick_params(labelsize=16)
    #axs[2].grid()
    #axs[2].legend(fontsize=12, loc="lower right")

    # Margin adjustments
    left = 0.06  # the left side of the subplots of the figure
    right = 0.9  # the right side of the subplots of the figure
    bottom = 0.12  # the bottom of the subplots of the figure
    top = 0.98  # the top of the subplots of the figure
    wspace = 0.1  # the amount of width reserved for blank space between subplots
    hspace = 0.23  # the amount of height reserved for white space between subplots
    plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

    s = "$t=$" + f"{time:0.04e}"
    plt.text(0.2, 0.5, s, color="black", fontsize=14)
    iy = str(i).zfill(5)
    outfile = OutputDir + imgbase + "_" + iy + ".png"
    print("saving " + outfile)
    plt.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    del fig
    del outfile
