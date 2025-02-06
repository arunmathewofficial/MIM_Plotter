# Author: Arun Mathew
# Created: 11-03-2023
# Multi-ion-module-publication: This script generates plots comparing
# the non-adiabatic ionization fraction of silicon (Si), sulfur (S),
# and iron (Fe) behind the plane shock for inflow velocities of 1000 km/s and 3000 km/s.


# Import required libraries: ##########################################
import warnings
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nonadia_v1000_silofile", type=str, help="Silo file for non-adiabatic shock with inflow velocity of 1000 km/s")
parser.add_argument("nonadia_v3000_silofile", type=str, help="Silo file for non-adiabatic shock with inflow velocity of 3000 km/s")
parser.add_argument("output_dir", type=str, help="Output image dir path")
args = parser.parse_args()
print("*** Multi-ion-module-publication: non-adiabatic ionisation fraction v1000 vs v3000 ***")

output_dir = args.output_dir
output_dir = make_directory(output_dir)
v1000_file = args.nonadia_v1000_silofile
v3000_file = args.nonadia_v3000_silofile

np.set_printoptions(threshold=np.inf)  # Print the entire array


# x data for v=1000 km/s
x_v1000 = get_basic_data(v1000_file)['x']/1.0E+16
# x data for v=3000 km/s
x_v3000 = get_basic_data(v3000_file)['x']/1.0E+16

fig, axs = plt.subplots(2, 1, figsize=(7, 9))

# SILICON ###################################################################
print('Plotting Silicon ion-fraction for v=1000 km/s and v=3000 km/s ...')

# flow moving with v=1000 km/s
X_Si = get_tracer(v1000_file, "Tr040_X_Si")
Si0 = get_tracer(v1000_file, "Tr041_Si")
Si1p = get_tracer(v1000_file , "Tr042_Si1p")
Si2p = get_tracer(v1000_file , "Tr043_Si2p")
Si3p = get_tracer(v1000_file , "Tr044_Si3p")
Si4p = get_tracer(v1000_file , "Tr045_Si4p")
Si5p = get_tracer(v1000_file, "Tr046_Si5p")
Si6p = get_tracer(v1000_file, "Tr047_Si6p")
Si7p = get_tracer(v1000_file , "Tr048_Si7p")
Si8p = get_tracer(v1000_file, "Tr049_Si8p")
Si9p = get_tracer(v1000_file, "Tr050_Si9p")
Si10p = get_tracer(v1000_file, "Tr051_Si10p")
Si11p = get_tracer(v1000_file, "Tr052_Si11p")
Si12p = get_tracer(v1000_file, "Tr053_Si12p")
Si13p = get_tracer(v1000_file, "Tr054_Si13p")
Si14p = X_Si - (Si0 + Si1p + Si2p + Si3p + Si4p + Si5p + Si6p
                + Si7p + Si8p + Si9p + Si10p + Si11p + Si12p + Si13p)

axs[0].plot(x_v1000, Si0 / X_Si, linestyle='-', linewidth=2.0, label=r'$\rm Si$')
axs[0].plot(x_v1000, Si1p / X_Si, linestyle='-', linewidth=2.0, label=r'$\rm Si^{+}$')
axs[0].plot(x_v1000, Si2p / X_Si, linestyle='-', linewidth=2.0, label=r'$\rm Si^{2+}$')
axs[0].plot(x_v1000, Si3p / X_Si, linestyle='-', linewidth=2.0, label=r'$\rm Si^{3+}$')
axs[0].plot(x_v1000, Si4p / X_Si, linestyle='-', linewidth=2.0, label=r'$\rm Si^{4+}$')
axs[0].plot(x_v1000, Si5p / X_Si, linestyle='-', linewidth=2.0, label=r'$\rm Si^{5+}$')
axs[0].plot(x_v1000, Si6p / X_Si, linestyle='-', linewidth=2.0, label=r'$\rm Si^{6+}$')
axs[0].plot(x_v1000, Si8p / X_Si, linestyle='-', linewidth=2.0, label=r'$\rm Si^{7+}$')
axs[0].plot(x_v1000, Si9p / X_Si, linestyle='-', linewidth=2.0, label=r'$\rm Si^{8+}$')
axs[0].plot(x_v1000, Si10p / X_Si, linestyle='-', linewidth=2.0, label=r'$\rm Si^{9+}$')
axs[0].plot(x_v1000, Si11p / X_Si, linestyle='--', linewidth=2.0, label=r'$\rm Si^{10+}$')
axs[0].plot(x_v1000, Si12p / X_Si, linestyle='--', linewidth=2.0, label=r'$\rm Si^{11+}$')
axs[0].plot(x_v1000, Si13p / X_Si, linestyle='--', linewidth=2.0, label=r'$\rm Si^{12+}$')
axs[0].plot(x_v1000, Si14p / X_Si, linestyle='--', linewidth=2.0, label=r'$\rm Si^{13+}$')

axs[0].set_ylabel(r'\rm Ionisation fraction', fontsize=18)
#axs[0].set_xlabel(r'\rm x (10$^{16}$ \, cm)', fontsize=22)
axs[0].set_xlim(0.2, 0.58)
axs[0].text(0.25, 0.8, r'\rm $|v_x|$ = 1000 km s$^{-1}$', fontsize=18)
axs[0].legend(fontsize=14, loc='upper center', ncol=5, bbox_to_anchor=(0.47, 1.3),
              frameon=True, columnspacing=2.5, edgecolor='black')
axs[0].tick_params(axis='both', labelsize=16, direction='in')

# flow moving with v=3000 km/s
X_Si = get_tracer(v3000_file, "Tr040_X_Si")
Si0  = get_tracer(v3000_file, "Tr041_Si")
Si1p = get_tracer(v3000_file, "Tr042_Si1p")
Si2p = get_tracer(v3000_file, "Tr043_Si2p")
Si3p = get_tracer(v3000_file, "Tr044_Si3p")
Si4p = get_tracer(v3000_file, "Tr045_Si4p")
Si5p = get_tracer(v3000_file, "Tr046_Si5p")
Si6p = get_tracer(v3000_file, "Tr047_Si6p")
Si7p = get_tracer(v3000_file, "Tr048_Si7p")
Si8p = get_tracer(v3000_file, "Tr049_Si8p")
Si9p = get_tracer(v3000_file, "Tr050_Si9p")
Si10p = get_tracer(v3000_file, "Tr051_Si10p")
Si11p = get_tracer(v3000_file, "Tr052_Si11p")
Si12p = get_tracer(v3000_file, "Tr053_Si12p")
Si13p = get_tracer(v3000_file, "Tr054_Si13p")
Si14p = X_Si - (Si0 + Si1p + Si2p + Si3p + Si4p + Si5p + Si6p
                + Si7p + Si8p + Si9p + Si10p + Si11p + Si12p + Si13p)

axs[1].plot(x_v3000, Si0 / X_Si, linestyle='-', linewidth=2.0)
axs[1].plot(x_v3000, Si1p / X_Si, linestyle='-', linewidth=2.0)
axs[1].plot(x_v3000, Si2p / X_Si, linestyle='-', linewidth=2.0)
axs[1].plot(x_v3000, Si3p / X_Si, linestyle='-', linewidth=2.0)
axs[1].plot(x_v3000, Si4p / X_Si, linestyle='-', linewidth=2.0)
axs[1].plot(x_v3000, Si5p / X_Si, linestyle='-', linewidth=2.0)
axs[1].plot(x_v3000, Si6p / X_Si, linestyle='-', linewidth=2.0)
axs[1].plot(x_v3000, Si8p / X_Si, linestyle='-', linewidth=2.0)
axs[1].plot(x_v3000, Si9p / X_Si, linestyle='-', linewidth=2.0)
axs[1].plot(x_v3000, Si10p / X_Si, linestyle='-', linewidth=2.0)
axs[1].plot(x_v3000, Si11p / X_Si, linestyle='--', linewidth=2.0)
axs[1].plot(x_v3000, Si12p / X_Si, linestyle='--', linewidth=2.0)
axs[1].plot(x_v3000, Si13p / X_Si, linestyle='--', linewidth=2.0)
axs[1].plot(x_v3000, Si14p / X_Si, linestyle='--', linewidth=2.0)

axs[1].set_ylabel(r'\rm Ionisation fraction', fontsize=18)
axs[1].set_xlabel(r'\rm x (10$^{16}$ cm)', fontsize=18)
axs[1].set_xlim(0.58, 0.643)
axs[1].text(0.59, 0.8, r'\rm $|v_x|$ = 3000 km s$^{-1}$', fontsize=18)
axs[1].tick_params(axis='both', labelsize=16, direction='in')


plt.subplots_adjust(left=0.1, right=0.98, top=0.89, bottom=0.07, hspace=0.12)
imagename = output_dir + 'NonAdiaSh_v3000_vs_v1000_Si.png'
print('Saving image ' + imagename)
plt.savefig(imagename, dpi=300)
plt.close()
#############################################################################

