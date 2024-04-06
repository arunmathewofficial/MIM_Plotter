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

for i, frame in enumerate(timeline):
    silo_file = timeline[frame][0]

    time = get_basic_data(silo_file)['time']
    Temperature = get_temperature(silo_file)
    Density = get_density(silo_file)
    xaxis = get_basic_data(silo_file)['x']

    norm = get_tracer(silo_file, 'Tr000_X_H')
    H0 = get_tracer(silo_file, 'Tr009_H')
    H1p = get_tracer(silo_file, 'Tr000_X_H') - get_tracer(silo_file, 'Tr009_H')

    fig, axs = plt.subplots(3, 1, figsize=(8, 8))
    axs[0].plot(xaxis, np.log10(Temperature), label="$\log(T)$")
    #axs[0].tick_params(labelsize=16)
    #axs[0].grid()
    #axs[0].legend(fontsize=12, loc="lower right")
    #axs[0].set_xlim(0.0, 1.0E+14)

    axs[1].plot(xaxis, np.log10(Density), label="$\log(\\rho)$")  # Corrected label
    #axs[1].tick_params(labelsize=16)
    #axs[1].grid()
    #axs[1].legend(fontsize=12, loc="lower right")
    #axs[1].set_xlim(0.0, 1.0E+14)


    axs[2].plot(xaxis, H0/norm , label='H0')
    axs[2].plot(xaxis, H1p/norm, label='H1+' )
    #axs[2].tick_params(labelsize=16)
    #axs[2].grid()
    #axs[2].legend(fontsize=12, loc="lower right")

    s = "$t=$" + f"{time:0.04f}"
    plt.text(0.2, 0.5, s, color="black", fontsize=14)
    iy = str(i).zfill(5)
    outfile = OutputDir + imgbase + "_" + iy + ".png"
    print("saving " + outfile)
    plt.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    del fig
    del outfile
