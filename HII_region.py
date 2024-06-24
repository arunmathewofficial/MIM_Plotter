# Author: Arun Mathew
# Created: 23-06-2024
# Multi-ion-module-publication: The script plot the
# HII-region temperature and ionisation profile for the
# HII40 Lexington Benchmark

# Import required libraries: ##########################################
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
from matplotlib.lines import Line2D

import pandas as pd
from matplotlib.ticker import MaxNLocator
from SiloReader import GetSiloData
import numpy as np
from matplotlib import colors as mcolors
import argparse
import constant as const


# MAIN ##################################################################################
parser = argparse.ArgumentParser()
parser.add_argument("cloudy_dir", type=str, help="Cloudy output directory")
parser.add_argument("silo_file", type=str, help="HII-region pion silo file path")
parser.add_argument("image_output_dir", type=str, help="Output image dir path")
parser.add_argument("numden", type=str, help="Which density")


args = parser.parse_args()
output_dir = args.image_output_dir
output_dir = make_directory(output_dir)
silo_file = args.silo_file
d = args.numden

# from the database
torus_haworth = 'data/HII_region_photoionradial_tom.dat'
# cloudy directory path
cloudy_dir = args.cloudy_dir
if not cloudy_dir.endswith('/'):
    cloudy_dir+= "/"

cloudyfile_ovr  = cloudy_dir + 'HII_region_' + d + '.ovr'
cloudyfile_H  = cloudy_dir + 'HII_region_' + d + '.ele_H'
cloudyfile_He = cloudy_dir + 'HII_region_' + d + '.ele_He'
cloudyfile_C  = cloudy_dir + 'HII_region_' + d + '.ele_C'
cloudyfile_N  = cloudy_dir + 'HII_region_' + d + '.ele_N'
cloudyfile_O  = cloudy_dir + 'HII_region_' + d + '.ele_O'
cloudyfile_Ne = cloudy_dir + 'HII_region_' + d + '.ele_Ne'
cloudyfile_S  = cloudy_dir + 'HII_region_' + d + '.ele_S'
# **************************************************************************************

# Reading data #######################################################################
# reading cloudy data
ovr_data = read_cloudy(cloudyfile_ovr)
cloudy_radius = (np.array(ovr_data[0]) + 1.0e17) / const.parsec
cloudy_temp = np.array(ovr_data[1])
# reading pion data
print("Reading silo file:", silo_file)
object = GetSiloData([silo_file])
pion_radius = object.get_radial_coordinate() / const.parsec
# reading torus data
print("Reading torus file:", torus_haworth)
torus_data = np.loadtxt(torus_haworth)
torus_radius = torus_data[:,0] / 3.08e8


# Temperature profile ##############################################################
print("Plotting temperature profile ...")
pion_temp = object.get_parameter('Temperature')
torus_temp = torus_data[:,2]
fig, ax = plt.subplots(figsize=(5, 3))
ax.plot(cloudy_radius, cloudy_temp * 1.0e-3, label='\\textrm{\\textsc{Cloudy}}', linestyle='--', color='red')
if (d == 'n2'):
    ax.plot(torus_radius, torus_temp * 1.0e-3, label='\\textrm{\\textsc{Torus}}', linestyle=':', color='black')
ax.plot(pion_radius, pion_temp * 1.0e-3, label='\\textrm{\\textsc{Pion}}', linestyle='-.', color='blue')

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4,
               labelsize=12)
ax.tick_params(axis="both", direction="in", which="minor", bottom=True, top=True, left=True, right=True, length=2,
               labelsize=12)
ax.set_xlim([0.0, 6])
ax.set_ylim([5.0, 12.2])
ax.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
ax.set_ylabel("$T\,$ ($10^3\,$K)", fontsize=12)
ax.text(0.1, 11, "\\textrm{(a)}", fontsize=12)
ax.legend(frameon=False, loc='upper center', fontsize='12')
image_file = output_dir + d + '_HII_temperature.png'
print("Saving image to", image_file)
plt.savefig(image_file, dpi=300, bbox_inches='tight')
plt.close()


print("Plotting Hydrogen, Helium and Oxygen ionisation profile ...")
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 14))
# Hydrogen and Helium profile ##############################################################
H_data = read_cloudy(cloudyfile_H)
He_data = read_cloudy(cloudyfile_He)

print("Reading silo file:", silo_file)
H0 = object.get_parameter('Tr009_H') / object.get_parameter('Tr000_X_H')
H1p = np.ones_like(H0) - H0
He0 = object.get_parameter('Tr010_He') / object.get_parameter('Tr001_X_He')
He1p = object.get_parameter('Tr011_He1p') / object.get_parameter('Tr001_X_He')
He2p = np.ones_like(He0) - He0 - He1p

ax1.plot(cloudy_radius, H_data[1], label='', linestyle=':', color='C0')
ax1.plot(cloudy_radius, H_data[2], label='', linestyle=':', color='C1')
ax1.plot(cloudy_radius, He_data[1], label='', linestyle=':', color='C2')
ax1.plot(cloudy_radius, He_data[2], label='', linestyle=':', color='C3')
ax1.plot(cloudy_radius, He_data[3], label='', linestyle=':', color='C4')

ax1.plot(pion_radius, H0, label=r'$\rm H$', linestyle='-', color='C0')
ax1.plot(pion_radius, H1p, label=r'$\rm H^{1+}$', linestyle='-', color='C1')
ax1.plot(pion_radius, He0, label=r'$\rm He$', linestyle='-', color='C2')
ax1.plot(pion_radius, He1p, label=r'$\rm He^{1+}$', linestyle='-', color='C3')
ax1.plot(pion_radius, He2p, label=r'$\rm He^{2+}$', linestyle='-', color='C4')

ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax1.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4, labelsize=12)
ax1.tick_params(axis="both", direction="in", which="minor", bottom=True, top=True, left=True, right=True, length=2, labelsize=12)
ax1.text(0.4,0.9,"\\textrm{(b)}", fontsize=12)

ax1.set_xlim([0.0, 6])
ax1.grid()
ax1.set_yscale("log")
ax1.set_ylim([1e-6,1.5])
#ax.set_ylim([-25.5, -19.5])
#ax1.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
ax1.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=12)
ax1.legend(loc='upper left', bbox_to_anchor=(-0.12, 1.15), ncol=5, fontsize=11)



# Carbon profile ##############################################################
O_data = read_cloudy(cloudyfile_O)
print("Reading silo file:", silo_file)

O0 = object.get_parameter('Tr025_O') / object.get_parameter('Tr004_X_O')
O1p = object.get_parameter('Tr026_O1p') / object.get_parameter('Tr004_X_O')
O2p = object.get_parameter('Tr027_O2p') / object.get_parameter('Tr004_X_O')
O3p = object.get_parameter('Tr028_O3p') / object.get_parameter('Tr004_X_O')
O4p = object.get_parameter('Tr029_O4p') / object.get_parameter('Tr004_X_O')
O5p = object.get_parameter('Tr030_O5p') / object.get_parameter('Tr004_X_O')
O6p = object.get_parameter('Tr031_O6p') / object.get_parameter('Tr004_X_O')
O7p = object.get_parameter('Tr032_O7p') / object.get_parameter('Tr004_X_O')
O8p = np.ones_like(O0) - O0 - O1p - O2p - O3p - O4p - O5p - O6p - O7p

ax2.plot(cloudy_radius, O_data[1], label='', linestyle=':', color='C0')
ax2.plot(cloudy_radius, O_data[2], label='', linestyle=':', color='C1')
ax2.plot(cloudy_radius, O_data[3], label='', linestyle=':', color='C2')
ax2.plot(cloudy_radius, O_data[4], label='', linestyle=':', color='C3')
ax2.plot(cloudy_radius, O_data[5], label='', linestyle=':', color='C4')
ax2.plot(cloudy_radius, O_data[6], label='', linestyle=':', color='C5')
ax2.plot(cloudy_radius, O_data[7], label='', linestyle=':', color='C6')
ax2.plot(cloudy_radius, O_data[8], label='', linestyle=':', color='C7')
ax2.plot(cloudy_radius, O_data[9], label='', linestyle=':', color='C8')

ax2.plot(pion_radius, O0, label=r'$\rm O$', linestyle='-', color='C0')
ax2.plot(pion_radius, O1p, label=r'$\rm O^{1+}$', linestyle='-', color='C1')
ax2.plot(pion_radius, O2p, label=r'$\rm O^{2+}$', linestyle='-', color='C2')
ax2.plot(pion_radius, O3p, label=r'$\rm O^{3+}$', linestyle='-', color='C3')
ax2.plot(pion_radius, O4p, label=r'$\rm O^{4+}$', linestyle='-', color='C4')
ax2.plot(pion_radius, O5p, label=r'$\rm O^{5+}$', linestyle='-', color='C5')
ax2.plot(pion_radius, O6p, label=r'$\rm O^{6+}$', linestyle='-', color='C6')
ax2.plot(pion_radius, O7p, label=r'$\rm O^{7+}$', linestyle='-', color='C7')
ax2.plot(pion_radius, O8p, label=r'$\rm O^{8+}$', linestyle='-', color='C8')


ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax2.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4, labelsize=12)
ax2.tick_params(axis="both", direction="in", which="minor", bottom=True, top=True, left=True, right=True, length=2, labelsize=12)
ax2.text(0.4,0.9,"\\textrm{(b)}", fontsize=12)

ax2.set_xlim([0.0, 6])
ax2.grid()
ax2.set_yscale("log")
ax2.set_ylim([1e-6,1.5])
#ax.set_ylim([-25.5, -19.5])
#ax2.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
ax2.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=12)
ax2.legend(loc='upper left', bbox_to_anchor=(-0.12, 1.15), ncol=5, fontsize=11)

plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.2)
image_file = output_dir + d + '_HHeO.png'
print("Saving image to", image_file)
plt.savefig(image_file, dpi=300, bbox_inches='tight')
plt.close()


'''
# Carbon profile ##############################################################
O_data = read_cloudy(cloudyfile_O)
print("Reading silo file:", silo_file)
C0 = object.get_parameter('Tr012_C'  ) / object.get_parameter('Tr002_X_C')
C1p = object.get_parameter('Tr013_C1p') / object.get_parameter('Tr002_X_C')
C2p = object.get_parameter('Tr014_C2p') / object.get_parameter('Tr002_X_C')
C3p = object.get_parameter('Tr015_C3p') / object.get_parameter('Tr002_X_C')
C4p = object.get_parameter('Tr016_C4p') / object.get_parameter('Tr002_X_C')
C5p = object.get_parameter('Tr017_C5p') / object.get_parameter('Tr002_X_C')
C6p = np.ones_like(C0) - C0 - C1p - C2p - C3p - C4p - C5p

ax2.plot(cloudy_radius, C_data[1], label='', linestyle=':', color='C0')
ax2.plot(cloudy_radius, C_data[2], label='', linestyle=':', color='C1')
ax2.plot(cloudy_radius, C_data[3], label='', linestyle=':', color='C2')
ax2.plot(cloudy_radius, C_data[4], label='', linestyle=':', color='C3')
#ax2.plot(cloudy_radius, C_data[5], label='', linestyle=':', color='C4')
#ax2.plot(cloudy_radius, C_data[6], label='', linestyle=':', color='C5')
#ax2.plot(cloudy_radius, C_data[7], label='', linestyle=':', color='C6')

ax2.plot(pion_radius, C0, label=r'$\rm C$', linestyle='-', color='C0')
ax2.plot(pion_radius, C1p, label=r'$\rm C^{1+}$', linestyle='-', color='C1')
ax2.plot(pion_radius, C2p, label=r'$\rm C^{2+}$', linestyle='-', color='C2')
ax2.plot(pion_radius, C3p, label=r'$\rm C^{3+}$', linestyle='-', color='C3')
#ax2.plot(pion_radius, C4p, label=r'$\rm C^{4+}$', linestyle='-', color='C4')
#ax2.plot(pion_radius, C5p, label=r'$\rm C^{5+}$', linestyle='-', color='C5')
#ax2.plot(pion_radius, C6p, label=r'$\rm C^{6+}$', linestyle='-', color='C6')

ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax2.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4, labelsize=12)
ax2.tick_params(axis="both", direction="in", which="minor", bottom=True, top=True, left=True, right=True, length=2, labelsize=12)
ax2.text(0.4,0.9,"\\textrm{(b)}", fontsize=12)

ax2.set_xlim([0.0, 6])
ax2.grid()
ax2.set_yscale("log")
ax2.set_ylim([1e-6,1.5])
#ax.set_ylim([-25.5, -19.5])
#ax2.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
ax2.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=12)
ax2.legend(loc='upper left', bbox_to_anchor=(-0.12, 1.15), ncol=5, fontsize=11)

plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.2)
image_file = output_dir + d + '_HHeO.png'
print("Saving image to", image_file)
plt.savefig(image_file, dpi=300, bbox_inches='tight')
plt.close()

'''