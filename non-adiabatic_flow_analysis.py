# Author: Arun Mathew
# Created: 16-03-2023
# Multi-ion-module-publication: This script plots flow quantities and
# ionization profiles for the non-adiabatic shock test case. The plots
# are generated to compare the effects of the cooling function on
# density and the cooling timescale.

# Import required libraries: ##########################################
import warnings
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("low_density_subtime", type=str, help="Silo file for sub-cooling-time and low-density case.")
parser.add_argument("low_density_overtime", type=str, help="Silo file for high-time over cooling timescale and low-density case")
parser.add_argument("high_density_overtime", type=str, help="Silo file for high-density cases exceeding cooling timescales.")
parser.add_argument("output_dir", type=str, help="give the output image dir path")
args = parser.parse_args()
output_dir = args.output_dir
output_dir = make_directory(output_dir)

low_den_subtime_file = args.low_density_subtime
low_den_overtime_file = args.low_density_overtime
high_den_overtime_file = args.high_density_overtime


#plt.rc('font', **{'family': 'sans-serif', 'sans-serif': ['Helvetica']})
#plt.rc('text', usetex=True)
#plt.rc('font', **{'size': 12})
#plt.rc('lines', linewidth=1.5)


parsec = 3.086e+18 # cm
# x data in parsec
x_ldst = get_basic_data(low_den_subtime_file)['x']/parsec
x_ldot = get_basic_data(low_den_overtime_file)['x']/parsec
x_hdot = get_basic_data(high_den_overtime_file)['x']/parsec

time_ldst = r'\rm t = ' + str(get_basic_data(low_den_subtime_file)['time'].round(3))
time_ldot = r'\rm t = ' + str(get_basic_data(low_den_overtime_file)['time'].round(3))
time_hdot = r'\rm t = ' + str(get_basic_data(high_den_overtime_file)['time'].round(3))

# generate 5 panel figure
fig, ax = plt.subplots(5, 1, figsize=(5, 8))

### Panel - 1 Temperature profile
#ax[0].set_xlabel(r'$\rm x \, (cm)$', fontsize=18)
ax[0].set_ylabel(r'$\rm log \, T \, (K)$', fontsize=14, labelpad=16)
ax[0].plot(x_ldst, np.log10(get_temperature(low_den_subtime_file)), label=time_ldst,
           color='saddlebrown', linewidth=1)
ax[0].plot(x_ldot, np.log10(get_temperature(low_den_overtime_file)), label=time_ldot,
           color='darkgoldenrod', linestyle='--', linewidth=1)
ax[0].legend(frameon=False, fontsize=12, loc=(0.5, 0.3))
ax[0].set_xlim(0, 28)
#ax[0].xaxis.set_minor_locator(AutoMinorLocator())
#ax[0].yaxis.set_minor_locator(AutoMinorLocator())
ax[0].tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True, right=True, length=2)

### Panel - 2 density profile
#ax[1].set_xlabel(r'$\rm x \, (cm)$', fontsize=18)
ax[1].set_ylabel(r'$\rm log \, \rho \, (g/cm^3)$', fontsize=14, labelpad=2)
ax[1].plot(x_ldst, get_density(low_den_subtime_file),
           label=time_ldst, color='saddlebrown', linewidth=1)
ax[1].plot(x_ldot, get_density(low_den_overtime_file),
           label=time_ldot, color='darkgoldenrod', linestyle='--', linewidth=1)
ax[1].set_yscale('log')
ax[1].set_xlim(-0.4, 28)
ax[1].legend(frameon=False, fontsize=12, loc=(0.5, 0.3))
#ax[1].xaxis.set_minor_locator(AutoMinorLocator())
#ax[1].yaxis.set_minor_locator(AutoMinorLocator())
ax[1].tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True, right=True, length=2)

# save data to file the temperature profile with low density gas.
import pandas as pd
T_profile_data = {'x(pc)': x_ldot, 'T (K)':get_temperature(low_den_overtime_file)}
df = pd.DataFrame(T_profile_data)
print('Printing temperature profile data to file ...')
df.to_csv(output_dir + 'non-adiabatic_temp_profile.txt', sep='\t', index=False, float_format='%e')



### Panel - 3 H, He, ionisation profile
X_H = get_tracer(low_den_overtime_file, 'Tr000_X_H')
H0 = get_tracer(low_den_overtime_file, 'Tr009_H')
H1p = X_H - H0
X_He = get_tracer(low_den_overtime_file, "Tr001_X_He")
He0 = get_tracer(low_den_overtime_file, "Tr010_He")
He1p = get_tracer(low_den_overtime_file, "Tr011_He1p")
He2p = X_He - He0 - He1p

#ax[2].set_xlabel(r'$\rm x \, (cm)$', fontsize=18)
ax[2].set_ylabel(r'\rm Ionisation fraction', fontsize=12,  labelpad=12)
ax[2].plot(x_ldot, H0 / X_H, label="$\mathrm{H}$", linewidth=1, color='red')
ax[2].plot(x_ldot, H1p / X_H, label="$\mathrm{H}^{+}$", linewidth=1, color='black')
ax[2].plot(x_ldot, He0 / X_He, label="$\mathrm{He}$", linewidth=1, linestyle='--', color='turquoise')
ax[2].plot(x_ldot, He1p / X_He, label="$\mathrm{He}^{+}$", linewidth=1, linestyle='--', color='darkgoldenrod')
ax[2].plot(x_ldot, He2p / X_He, label="$\mathrm{He}^{2+}$", linewidth=1, linestyle='--', color='magenta')
ax[2].set_xlim(0, 3)
ax[2].set_ylim()
ax[2].legend(frameon=False, fontsize=10, ncol=2)
#ax[2].xaxis.set_minor_locator(AutoMinorLocator())
#ax[2].yaxis.set_minor_locator(AutoMinorLocator())
ax[2].tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True, right=True, length=2)

### Panel - 4, Carbon ionisation profile

X_C = get_tracer(low_den_overtime_file, "Tr002_X_C")
C0 = get_tracer(low_den_overtime_file, "Tr012_C")
C1p = get_tracer(low_den_overtime_file, "Tr013_C1p")
C2p = get_tracer(low_den_overtime_file, "Tr014_C2p")
C3p = get_tracer(low_den_overtime_file, "Tr015_C3p")
C4p = get_tracer(low_den_overtime_file, "Tr016_C4p")
C5p = get_tracer(low_den_overtime_file, "Tr017_C5p")
C6p = X_C - C0 - C1p - C2p - C3p - C4p - C5p

#ax[3].set_xlabel(r'$\rm x \, (cm)$', fontsize=18)
ax[3].set_ylabel(r'\rm Ionisation fraction', fontsize=12, labelpad=12)
ax[3].plot(x_ldot, C0 / X_C, label="$\mathrm{C}$", linewidth=1, color='red')
ax[3].plot(x_ldot, C1p / X_C, label="$\mathrm{C}^{+}$", linewidth=1, linestyle='--', color='black')
ax[3].plot(x_ldot, C2p / X_C, label="$\mathrm{C}^{2+}$", linewidth=1, color='magenta')
ax[3].plot(x_ldot, C3p / X_C, label="$\mathrm{C}^{3+}$", linewidth=1, linestyle='--', color='turquoise')
ax[3].plot(x_ldot, C4p / X_C, label="$\mathrm{C}^{4+}$", linewidth=1, color='saddlebrown', linestyle='--')
ax[3].plot(x_ldot, C5p / X_C, label="$\mathrm{C}^{5+}$", linewidth=1, color='orange')
ax[3].plot(x_ldot, C6p / X_C, label="$\mathrm{C}^{6+}$", linewidth=1, color='olivedrab', linestyle='--')
ax[3].set_ylim()
ax[3].set_xlim(0, 3)
ax[3].legend(frameon=False, fontsize=10, ncol=2)
#ax[3].xaxis.set_minor_locator(AutoMinorLocator())
#ax[3].yaxis.set_minor_locator(AutoMinorLocator())
ax[3].tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True, right=True, length=2)

### Panel - 5
ax[4].set_xlabel(r'$\rm x \, (pc)$', fontsize=14)
ax[4].set_ylabel(r'$\rm log \, T \, (K)$', fontsize=14, labelpad=16)
ax[4].plot(x_ldst, np.log10(get_temperature(low_den_overtime_file)), color='turquoise',
           linestyle='--', linewidth=1, label=r'$\rm \rho_1 $')
ax[4].plot(x_hdot, np.log10(get_temperature(high_den_overtime_file)), color='saddlebrown',
           linewidth=1, label=r'$\rm \rho_2$')
ax[4].set_xlim(0, 28)
ax[4].set_ylim()
ax[4].legend(frameon=False, fontsize=12, loc=(0.6, 0.4))
#ax[4].xaxis.set_minor_locator(AutoMinorLocator())
#ax[4].yaxis.set_minor_locator(AutoMinorLocator())
ax[4].tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True, right=True, length=2)


#fig.subplots_adjust(wspace=0.0)
plt.subplots_adjust(hspace=0.05)
plt.tight_layout()
plt.savefig(output_dir + 'non-adiabatic_analysis.png')
