# -*- coding: iso-8859-15 -*-

from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
import astropy.units as unit
import argparse

mH = 1.6735575e-24 # in gms
parser = argparse.ArgumentParser()
parser.add_argument("input_silo_file", type=str, help="give the input silo file path")
parser.add_argument("output_dir", type=str, help="give the output image dir path")
parser.add_argument("whatplot", type=str, help="mention what to plot? options: flow_quantities, chemical_tracers")

args = parser.parse_args()
input_silo = args.input_silo_file
output_dir = args.output_dir
output_dir = make_directory(output_dir)
what2plot = args.whatplot
if what2plot != 'flow_quantities' and what2plot != 'chemical_tracers':
    print('\033[93mPlease specify what to plot!\033[0m')
    print('\033[93mOptions: flow_quantities, chemical_tracers\033[0m')

# switch to plot in pc
cm2pc = True

basic_info = get_basic_data(input_silo)
# time
time = basic_info['time']
# radial grid points
radial_grid_points = basic_info['x']




# plot flow quantities ############################################
if what2plot == 'flow_quantities':
    print("plotting flow quantities ...")
    # get temperature
    temperature = get_temperature(input_silo)
    # get density
    density = get_density(input_silo)
    # get radial velocity
    vx = get_velocityX(input_silo)
    # hydrogen number density
    X_H = get_tracer(input_silo, 'Tr000_X_H')
    nH = X_H * density / mH
    # Create a plot
    plt.plot(radius, temperature/(1.5*10**4), label=r'$T\, (1.5\times 10^{7} K)$', linestyle='-')
    #plt.plot(radius, density/(5*10**-23), label=r'$\rho \, (5.0\times 10^{22})$', linestyle='--')
    #plt.plot(radius, vx/10**8, label=r'$v_r \, (1.0\times 10^{8})$', linestyle='-.')
    #plt.plot(radius, nH/30, label=r'$n_H (3.0\times 10^1)$', linestyle=':')
    # Add labels and title
    plt.xlabel('radius (pc)')
    plt.ylabel('various quantities')
    plt.xlim(0, 2)
    # Show the plot
    plt.grid(True)
    plt.legend()
    imagefile = output_dir + 'flow_quantities.png';
    print('saving image to ' + imagefile)
    plt.savefig(output_dir + 'flow_quantities.png')
    plt.close()


if what2plot == 'chemical_tracers':
    print("plotting chemical tracers ...")

    X_H = get_tracer(input_silo, 'Tr000_X_H')
    H0 = get_tracer(input_silo, 'Tr001_H')
    H1p = X_H - H0

    X_He = get_tracer(input_silo, "Tr002_X_He")
    He0  = get_tracer(input_silo, "Tr003_He")
    He1p = get_tracer(input_silo, "Tr004_He1p")
    He2p = X_He - He0 - He1p

    # Carbon
    X_C = get_tracer(input_silo, "Tr005_X_C")
    C0 = get_tracer(input_silo, "Tr006_C")
    C1p = get_tracer(input_silo, "Tr007_C1p")
    C2p = get_tracer(input_silo, "Tr008_C2p")
    C3p = get_tracer(input_silo, "Tr009_C3p")
    C4p = get_tracer(input_silo, "Tr010_C4p")
    C5p = get_tracer(input_silo, "Tr011_C5p")
    C6p = X_C - C0 - C1p - C2p - C3p - C4p - C5p

    # Nitrogen
    X_N = get_tracer(input_silo, "Tr012_X_N")
    N0 = get_tracer(input_silo, "Tr013_N")
    N1p = get_tracer(input_silo, "Tr014_N1p")
    N2p = get_tracer(input_silo, "Tr015_N2p")
    N3p = get_tracer(input_silo, "Tr016_N3p")
    N4p = get_tracer(input_silo, "Tr017_N4p")
    N5p = get_tracer(input_silo, "Tr018_N5p")
    N6p = get_tracer(input_silo, "Tr019_N6p")
    N7p = X_N - (N0 + N1p + N2p + N3p + N4p + N5p + N6p)

    # Oxygen
    X_O = get_tracer(input_silo, "Tr020_X_O")
    O0 = get_tracer(input_silo, "Tr021_O")
    O1p = get_tracer(input_silo, "Tr022_O1p")
    O2p = get_tracer(input_silo, "Tr023_O2p")
    O3p = get_tracer(input_silo, "Tr024_O3p")
    O4p = get_tracer(input_silo, "Tr025_O4p")
    O5p = get_tracer(input_silo, "Tr026_O5p")
    O6p = get_tracer(input_silo, "Tr027_O6p")
    O7p = get_tracer(input_silo, "Tr028_O7p")
    O8p = X_O - (O0 + O1p + O2p + O3p + O4p + O5p + O6p + O7p)

    # Neon
    X_Ne = get_tracer(input_silo, "Tr029_X_Ne")
    Ne0 = get_tracer(input_silo, "Tr030_Ne")
    Ne1p = get_tracer(input_silo, "Tr031_Ne1p")
    Ne2p = get_tracer(input_silo, "Tr032_Ne2p")
    Ne3p = get_tracer(input_silo, "Tr033_Ne3p")
    Ne4p = get_tracer(input_silo, "Tr034_Ne4p")
    Ne5p = get_tracer(input_silo, "Tr035_Ne5p")
    Ne6p = get_tracer(input_silo, "Tr036_Ne6p")
    Ne7p = get_tracer(input_silo, "Tr037_Ne7p")
    Ne8p = get_tracer(input_silo, "Tr038_Ne8p")
    Ne9p = get_tracer(input_silo, "Tr039_Ne9p")
    Ne10p = X_Ne - (Ne0 + Ne1p + Ne2p + Ne3p + Ne4p + Ne5p + Ne6p + Ne7p + Ne8p + Ne9p)

    # Silicon
    X_Si = get_tracer(input_silo, "Tr040_X_Si")
    Si0 = get_tracer(input_silo, "Tr041_Si")
    Si1p = get_tracer(input_silo, "Tr042_Si1p")
    Si2p = get_tracer(input_silo, "Tr043_Si2p")
    Si3p = get_tracer(input_silo, "Tr044_Si3p")
    Si4p = get_tracer(input_silo, "Tr045_Si4p")
    Si5p = get_tracer(input_silo, "Tr046_Si5p")
    Si6p = get_tracer(input_silo, "Tr047_Si6p")
    Si7p = get_tracer(input_silo, "Tr048_Si7p")
    Si8p = get_tracer(input_silo, "Tr049_Si8p")
    Si9p = get_tracer(input_silo, "Tr050_Si9p")
    Si10p = get_tracer(input_silo, "Tr051_Si10p")
    Si11p = get_tracer(input_silo, "Tr052_Si11p")
    Si12p = get_tracer(input_silo, "Tr053_Si12p")
    Si13p = get_tracer(input_silo, "Tr054_Si13p")
    Si14p = X_Si - (Si0 + Si1p + Si2p + Si3p + Si4p + Si5p + Si6p
                    + Si7p + Si8p + Si9p + Si10p + Si11p + Si12p + Si13p)
    # Sulfur
    X_S = get_tracer(input_silo, "Tr055_X_S")
    S0 = get_tracer(input_silo, "Tr056_S")
    S1p = get_tracer(input_silo, "Tr057_S1p")
    S2p = get_tracer(input_silo, "Tr058_S2p")
    S3p = get_tracer(input_silo, "Tr059_S3p")
    S4p = get_tracer(input_silo, "Tr060_S4p")
    S5p = get_tracer(input_silo, "Tr061_S5p")
    S6p = get_tracer(input_silo, "Tr062_S6p")
    S7p = get_tracer(input_silo, "Tr063_S7p")
    S8p = get_tracer(input_silo, "Tr064_S8p")
    S9p = get_tracer(input_silo, "Tr065_S9p")
    S10p = get_tracer(input_silo, "Tr066_S10p")
    S11p = get_tracer(input_silo, "Tr067_S11p")
    S12p = get_tracer(input_silo, "Tr068_S12p")
    S13p = get_tracer(input_silo, "Tr069_S13p")
    S14p = get_tracer(input_silo, "Tr070_S14p")
    S15p = get_tracer(input_silo, "Tr071_S15p")
    S16p = X_S - (S0 + S1p + S2p + S3p + S4p + S5p + S6p
                  + S7p + S8p + S9p + S10p + S11p + S12p
                  + S13p + S14p + S15p)

    # Iron
    X_Fe = get_tracer(input_silo, "Tr072_X_Fe")
    Fe0 = get_tracer(input_silo, "Tr073_Fe")
    Fe1p = get_tracer(input_silo, "Tr074_Fe1p")
    Fe2p = get_tracer(input_silo, "Tr075_Fe2p")
    Fe3p = get_tracer(input_silo, "Tr076_Fe3p")
    Fe4p = get_tracer(input_silo, "Tr077_Fe4p")
    Fe5p = get_tracer(input_silo, "Tr078_Fe5p")
    Fe6p = get_tracer(input_silo, "Tr079_Fe6p")
    Fe7p = get_tracer(input_silo, "Tr080_Fe7p")
    Fe8p = get_tracer(input_silo, "Tr081_Fe8p")
    Fe9p = get_tracer(input_silo, "Tr082_Fe9p")
    Fe10p = get_tracer(input_silo, "Tr083_Fe10p")
    Fe11p = get_tracer(input_silo, "Tr084_Fe11p")
    Fe12p = get_tracer(input_silo, "Tr085_Fe12p")
    Fe13p = get_tracer(input_silo, "Tr086_Fe13p")
    Fe14p = get_tracer(input_silo, "Tr087_Fe14p")
    Fe15p = get_tracer(input_silo, "Tr088_Fe15p")
    Fe16p = get_tracer(input_silo, "Tr089_Fe16p")
    Fe17p = get_tracer(input_silo, "Tr090_Fe17p")
    Fe18p = get_tracer(input_silo, "Tr091_Fe18p")
    Fe19p = get_tracer(input_silo, "Tr092_Fe19p")
    Fe20p = get_tracer(input_silo, "Tr093_Fe20p")
    Fe21p = get_tracer(input_silo, "Tr094_Fe21p")
    Fe22p = get_tracer(input_silo, "Tr095_Fe22p")
    Fe23p = get_tracer(input_silo, "Tr096_Fe23p")
    Fe24p = get_tracer(input_silo, "Tr097_Fe24p")
    Fe25p = get_tracer(input_silo, "Tr098_Fe25p")
    Fe26p = X_Fe - (Fe0 + Fe1p + Fe2p + Fe3p + Fe4p + Fe5p + Fe6p + Fe7p + Fe8p + Fe9p
                    + Fe10p + Fe11p + Fe12p + Fe13p + Fe14p + Fe15p + Fe16p + Fe17p + Fe18p + Fe19p
                    + Fe20p + Fe21p + Fe22p + Fe23p + Fe24p + Fe25p)

    # Hydrogen, Helium, Carbon
    fig, axs = plt.subplots(3, 1, figsize=(14, 14))
    axs[0].plot(radius, H0 / X_H, label="$\mathrm{H}^{0}$")
    axs[0].plot(radius, H1p / X_H, label="$\mathrm{H}^{+}$")
    axs[0].plot(radius, He0 / X_He, label="$\mathrm{He}^{0}$")
    axs[0].plot(radius, He1p / X_He, label="$\mathrm{He}^{+}$")
    axs[0].plot(radius, He2p / X_He, label="$\mathrm{He}^{2+}$")
    axs[0].plot(radius, C0 / X_C, label="$\mathrm{C}^{0}$")
    axs[0].plot(radius, C1p / X_C, label="$\mathrm{C}^{+}$")
    axs[0].plot(radius, C2p / X_C, label="$\mathrm{C}^{2+}$")
    axs[0].plot(radius, C3p / X_C, label="$\mathrm{C}^{3+}$")
    axs[0].plot(radius, C4p / X_C, label="$\mathrm{C}^{4+}$")
    axs[0].plot(radius, C5p / X_C, label="$\mathrm{C}^{5+}$")
    axs[0].plot(radius, C6p / X_C, label="$\mathrm{C}^{6+}$")
    axs[0].tick_params(labelsize=16)
    axs[0].grid()
    axs[0].legend(fontsize=12, loc="lower right")
    axs[0].set_ylabel("Ion Fraction", fontsize=16)
    axs[0].set_xlabel("radius (pc)", fontsize=16)
    axs[0].set_xlim(0, 10)

    # Nitrogen, Oxygen, Neon
    axs[1].plot(radius, N0 / X_N, label="$\mathrm{N}^{0}$")
    axs[1].plot(radius, N1p / X_N, label="$\mathrm{N}^{+}$")
    axs[1].plot(radius, N2p / X_N, label="$\mathrm{N}^{2+}$")
    axs[1].plot(radius, N3p / X_N, label="$\mathrm{N}^{3+}$")
    axs[1].plot(radius, N4p / X_N, label="$\mathrm{N}^{4+}$")
    axs[1].plot(radius, N5p / X_N, label="$\mathrm{N}^{5+}$")
    axs[1].plot(radius, N6p / X_N, label="$\mathrm{N}^{6+}$")
    axs[1].plot(radius, N7p / X_N, label="$\mathrm{N}^{7+}$")
    axs[1].plot(radius, O0 / X_O, label="$\mathrm{O}^{0}$")
    axs[1].plot(radius, O1p / X_O, label="$\mathrm{O}^{+}$")
    axs[1].plot(radius, O2p / X_O, label="$\mathrm{O}^{2+}$")
    axs[1].plot(radius, O3p / X_O, label="$\mathrm{O}^{3+}$")
    axs[1].plot(radius, O4p / X_O, label="$\mathrm{O}^{4+}$")
    axs[1].plot(radius, O5p / X_O, label="$\mathrm{O}^{5+}$")
    axs[1].plot(radius, O6p / X_O, label="$\mathrm{O}^{6+}$")
    axs[1].plot(radius, O7p / X_O, label="$\mathrm{O}^{7+}$")
    axs[1].plot(radius, O8p / X_O, label="$\mathrm{O}^{8+}$")
    axs[1].tick_params(labelsize=16)
    axs[1].grid()
    axs[1].legend(fontsize=12, loc="lower right")
    axs[1].set_ylabel("Ion Fraction", fontsize=16)
    axs[1].set_xlabel("radius (pc)", fontsize=16)
    axs[1].set_xlim(0, 10.0)  # Set the x-axis limits from 4.0 to 9.0

    axs[2].plot(radius, Ne0 / X_Ne, label="$\mathrm{Ne}^{0}$")
    axs[2].plot(radius, Ne1p / X_Ne, label="$\mathrm{Ne}^{+}$")
    axs[2].plot(radius, Ne2p / X_Ne, label="$\mathrm{Ne}^{2+}$")
    axs[2].plot(radius, Ne3p / X_Ne, label="$\mathrm{Ne}^{3+}$")
    axs[2].plot(radius, Ne4p / X_Ne, label="$\mathrm{Ne}^{4+}$")
    axs[2].plot(radius, Ne5p / X_Ne, label="$\mathrm{Ne}^{5+}$")
    axs[2].plot(radius, Ne6p / X_Ne, label="$\mathrm{Ne}^{6+}$")
    axs[2].plot(radius, Ne7p / X_Ne, label="$\mathrm{Ne}^{7+}$")
    axs[2].plot(radius, Ne8p / X_Ne, label="$\mathrm{Ne}^{8+}$")
    axs[2].plot(radius, Ne9p / X_Ne, label="$\mathrm{Ne}^{9+}$")
    axs[2].plot(radius, Ne10p / X_Ne, label="$\mathrm{Ne}^{10+}$")
    axs[2].tick_params(labelsize=16)
    axs[2].grid()
    axs[2].legend(fontsize=12, loc="lower right")
    axs[2].set_ylabel("Ion Fraction", fontsize=16)
    axs[2].set_xlabel("radius (pc)", fontsize=16)
    axs[2].set_xlim(0, 10.0)  # Set the x-axis limits from 4.0 to 9.0

    outfile = output_dir + "HHeCNONe_ionfrac.png"
    print("saving " + outfile)
    plt.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    del fig


    # Figure 2 Si, S, Fe
    fig, axs = plt.subplots(3, 1, figsize=(14, 14))
    axs[0].plot(radius, Si0 / X_Si, label="$\mathrm{Si}^{0}$")
    axs[0].plot(radius, Si1p / X_Si, label="$\mathrm{Si}^{+}$")
    axs[0].plot(radius, Si2p / X_Si, label="$\mathrm{Si}^{2+}$")
    axs[0].plot(radius, Si3p / X_Si, label="$\mathrm{Si}^{3+}$")
    axs[0].plot(radius, Si4p / X_Si, label="$\mathrm{Si}^{4+}$")
    axs[0].plot(radius, Si5p / X_Si, label="$\mathrm{Si}^{5+}$")
    axs[0].plot(radius, Si6p / X_Si, label="$\mathrm{Si}^{6+}$")
    axs[0].plot(radius, Si7p / X_Si, label="$\mathrm{Si}^{7+}$")
    axs[0].plot(radius, Si8p / X_Si, label="$\mathrm{Si}^{8+}$")
    axs[0].plot(radius, Si9p / X_Si, label="$\mathrm{Si}^{9+}$")
    axs[0].plot(radius, Si10p / X_Si, label="$\mathrm{Si}^{10+}$")
    axs[0].plot(radius, Si11p / X_Si, label="$\mathrm{Si}^{11+}$")
    axs[0].plot(radius, Si12p / X_Si, label="$\mathrm{Si}^{12+}$")
    axs[0].plot(radius, Si13p / X_Si, label="$\mathrm{Si}^{13+}$")
    axs[0].plot(radius, Si14p / X_Si, label="$\mathrm{Si}^{14+}$")
    axs[0].tick_params(labelsize=16)
    axs[0].grid()
    axs[0].legend(fontsize=12, loc="lower right")
    axs[0].set_ylabel("Ion Fraction", fontsize=16)
    axs[0].set_xlabel("radius (pc)", fontsize=16)
    axs[0].set_xlim(0, 4)  # Set the x-axis limits from 4.0 to 9.0

    axs[1].plot(radius, S0 / X_S, label="$\mathrm{S}^{0}$")
    axs[1].plot(radius, S1p / X_S, label="$\mathrm{S}^{+}$")
    axs[1].plot(radius, S2p / X_S, label="$\mathrm{S}^{2+}$")
    axs[1].plot(radius, S3p / X_S, label="$\mathrm{S}^{3+}$")
    axs[1].plot(radius, S4p / X_S, label="$\mathrm{S}^{4+}$")
    axs[1].plot(radius, S5p / X_S, label="$\mathrm{S}^{5+}$")
    axs[1].plot(radius, S6p / X_S, label="$\mathrm{S}^{6+}$")
    axs[1].plot(radius, S7p / X_S, label="$\mathrm{S}^{7+}$")
    axs[1].plot(radius, S8p / X_S, label="$\mathrm{S}^{8+}$")
    axs[1].plot(radius, S9p / X_S, label="$\mathrm{S}^{9+}$")
    axs[1].plot(radius, S10p / X_S, label="$\mathrm{S}^{10+}$")
    axs[1].plot(radius, S11p / X_S, label="$\mathrm{S}^{11+}$")
    axs[1].plot(radius, S12p / X_S, label="$\mathrm{S}^{12+}$")
    axs[1].plot(radius, S13p / X_S, label="$\mathrm{S}^{13+}$")
    axs[1].plot(radius, S14p / X_S, label="$\mathrm{S}^{14+}$")
    axs[1].plot(radius, S15p / X_S, label="$\mathrm{S}^{15+}$")
    axs[1].plot(radius, S16p / X_S, label="$\mathrm{S}^{16+}$")
    axs[1].tick_params(labelsize=16)
    axs[1].grid()
    axs[1].legend(fontsize=12, loc="lower right")
    axs[1].set_ylabel("Ion Fraction", fontsize=16)
    axs[1].set_xlabel("radius (pc)", fontsize=16)
    axs[1].set_xlim(0, 4)  # Set the x-axis limits from 4.0 to 9.0

    axs[2].plot(radius, Fe0 / X_Fe, label="$\mathrm{Fe}^{0}$")
    axs[2].plot(radius, Fe1p / X_Fe, label="$\mathrm{Fe}^{+}$")
    axs[2].plot(radius, Fe2p / X_Fe, label="$\mathrm{Fe}^{2+}$")
    axs[2].plot(radius, Fe3p / X_Fe, label="$\mathrm{Fe}^{3+}$")
    axs[2].plot(radius, Fe4p / X_Fe, label="$\mathrm{Fe}^{4+}$")
    axs[2].plot(radius, Fe5p / X_Fe, label="$\mathrm{Fe}^{5+}$")
    axs[2].plot(radius, Fe6p / X_Fe, label="$\mathrm{Fe}^{6+}$")
    axs[2].plot(radius, Fe7p / X_Fe, label="$\mathrm{Fe}^{7+}$")
    axs[2].plot(radius, Fe8p / X_Fe, label="$\mathrm{Fe}^{8+}$")
    axs[2].plot(radius, Fe9p / X_Fe, label="$\mathrm{Fe}^{9+}$")
    axs[2].plot(radius, Fe10p / X_Fe, label="$\mathrm{Fe}^{10+}$")
    axs[2].plot(radius, Fe11p / X_Fe, label="$\mathrm{Fe}^{11+}$")
    axs[2].plot(radius, Fe12p / X_Fe, label="$\mathrm{Fe}^{12+}$")
    axs[2].plot(radius, Fe13p / X_Fe, label="$\mathrm{Fe}^{13+}$")
    axs[2].plot(radius, Fe14p / X_Fe, label="$\mathrm{Fe}^{14+}$")
    axs[2].plot(radius, Fe15p / X_Fe, label="$\mathrm{Fe}^{15+}$")
    axs[2].plot(radius, Fe16p / X_Fe, label="$\mathrm{Fe}^{16+}$")
    axs[2].plot(radius, Fe17p / X_Fe, label="$\mathrm{Fe}^{17+}$")
    axs[2].plot(radius, Fe18p / X_Fe, label="$\mathrm{Fe}^{18+}$")
    axs[2].plot(radius, Fe19p / X_Fe, label="$\mathrm{Fe}^{19+}$")
    axs[2].plot(radius, Fe20p / X_Fe, label="$\mathrm{Fe}^{20+}$")
    axs[2].plot(radius, Fe21p / X_Fe, label="$\mathrm{Fe}^{21+}$")
    axs[2].plot(radius, Fe22p / X_Fe, label="$\mathrm{Fe}^{22+}$")
    axs[2].plot(radius, Fe23p / X_Fe, label="$\mathrm{Fe}^{23+}$")
    axs[2].plot(radius, Fe24p / X_Fe, label="$\mathrm{Fe}^{24+}$")
    axs[2].plot(radius, Fe25p / X_Fe, label="$\mathrm{Fe}^{25+}$")
    axs[2].plot(radius, Fe26p / X_Fe, label="$\mathrm{Fe}^{26+}$")
    axs[2].tick_params(labelsize=16)
    axs[2].grid()
    axs[2].legend(fontsize=12, loc="lower right")
    axs[2].set_ylabel("Ion Fraction", fontsize=16)
    axs[2].set_xlabel("radius (pc)", fontsize=16)
    axs[2].set_xlim(0, 4)  # Set the x-axis limits from 4.0 to 9.0

    outfile = output_dir + "SiSFe_ionfrac.png"
    print("saving " + outfile)
    plt.savefig(outfile, bbox_inches="tight")
    plt.close(fig)
    del fig

