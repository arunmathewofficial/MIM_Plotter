# Author: Arun Mathew
# Created: 16-03-2023
# Multi-ion-module-publication: This script plots flow quantities and
# ionization profiles for the non-adiabatic shock test case. The plots
# are generated to compare the effects of the cooling function on
# density and the cooling timescale.

# Import required libraries: ##########################################
import warnings
from tools import *
import numpy as np
import matplotlib.pyplot as plt
import argparse
from scipy.interpolate import UnivariateSpline
import pandas as pd
import matplotlib as mpl

parser = argparse.ArgumentParser()
parser.add_argument("low_density_subtime", type=str, help="Silo file for sub-cooling-time and low-density case.")
parser.add_argument("low_density_cooltime", type=str, help="Silo file for high-time over cooling timescale and low-density case")
parser.add_argument("high_density_cooltime", type=str, help="Silo file for high-density cases exceeding cooling timescales.")
parser.add_argument("output_dir", type=str, help="give the output image dir path")
args = parser.parse_args()
output_dir = args.output_dir
output_dir = make_directory(output_dir)

low_den_subtime_file = args.low_density_subtime
low_den_cooltime_file = args.low_density_cooltime
high_den_cooltime_file = args.high_density_cooltime

scale = 1.0e+19 # cm
# x data in parsec
x_ldst = get_basic_data(low_den_subtime_file)['x']/scale
x_ldot = get_basic_data(low_den_cooltime_file)['x']/scale
x_hdot = get_basic_data(high_den_cooltime_file)['x']/scale

time_ldst = r'\rm t = ' + str(get_basic_data(low_den_subtime_file)['time'].round(3))
time_ldot = r'\rm t = ' + str(get_basic_data(low_den_cooltime_file)['time'].round(3))
time_hdot = r'\rm t = ' + str(get_basic_data(high_den_cooltime_file)['time'].round(3))

mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = ['Computer Modern Roman']
mpl.rcParams['text.usetex'] = True

#######################################################################
# Plot 1 - two distinct time (sub and cooling)
#######################################################################

# Create a figure with 3 subplots
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(5, 6))

# Panel - 1 Temperature profile
ax1.set_ylabel(r'$\rm log \, T (K)$', fontsize=14, labelpad=16)
ax1.plot(x_ldst, np.log10(get_temperature(low_den_subtime_file)), label=r'$\rm Time \, t_1$',
           color='darkblue', linewidth=1.5)
ax1.plot(x_ldot, np.log10(get_temperature(low_den_cooltime_file)), label=r'$\rm Time \, t_2$',
           color='crimson', linestyle='--', linewidth=1.5)
ax1.legend(frameon=False, fontsize=12, loc=(0.5, 0.3))
ax1.set_xlim(0.1, 9)
ax1.set_ylim(3.2, 7.6)
#ax1.set_xlabel(r'$\rm x \, (10^{19} \, cm)$', fontsize=16)
ax1.tick_params(axis="both", direction="in", which="both", bottom=True,
                top=True, left=True, right=True, length=3, labelsize=14)
ax1.set_yticks([3.2, 4, 5, 6, 7])
# Save data to file the temperature profile with low density gas
T_profile_data = {'x(pc)': x_ldot, 'T (K)': get_temperature(low_den_cooltime_file)}
df = pd.DataFrame(T_profile_data)

print('Printing temperature profile data to file ...')
df.to_csv(output_dir + 'non-adiabatic_temp_profile.txt', sep='\t', index=False, float_format='%e')

# Panel - 2 H, He, ionisation profile
X_H = get_tracer(low_den_cooltime_file, 'Tr000_X_H')
H0 = get_tracer(low_den_cooltime_file, 'Tr009_H')
H1p = X_H - H0
X_He = get_tracer(low_den_cooltime_file, "Tr001_X_He")
He0 = get_tracer(low_den_cooltime_file, "Tr010_He")
He1p = get_tracer(low_den_cooltime_file, "Tr011_He1p")
He2p = X_He - He0 - He1p

ax2.set_ylabel(r'$\rm Ionisation \ fraction$', fontsize=14, labelpad=8)
ax2.plot(x_ldot, H0 / X_H, label=r'$\rm H$', linewidth=1.5, color='crimson', linestyle='--')
ax2.plot(x_ldot, H1p / X_H, label=r'$\rm H^{+}$', linewidth=1.5, color='darkblue', linestyle='--')
ax2.plot(x_ldot, He0 / X_He, label=r'$\rm He$', linewidth=1.5, linestyle='-', color='crimson')
ax2.plot(x_ldot, He1p / X_He, label=r'$\rm He^{+}$', linewidth=1.5, linestyle='-', color='darkgreen')
ax2.plot(x_ldot, He2p / X_He, label=r'$\rm He^{2+}$', linewidth=1.5, linestyle='-', color='darkblue')
ax2.set_xlim(0.01, 1.8)
#ax2.set_xlabel(r'\rm x (10$^{19}$ cm)', fontsize=16)
ax2.legend(frameon=False, fontsize=12, ncol=2)
ax2.tick_params(axis="both", direction="in", which="both", bottom=True,
                top=True, left=True, right=True, length=3, labelsize=14)
plt.setp(ax2.get_xticklabels(), visible=True)

# Panel - 3 Carbon ionisation profile
X_C = get_tracer(low_den_cooltime_file, "Tr002_X_C")
C0 = get_tracer(low_den_cooltime_file, "Tr012_C")
C1p = get_tracer(low_den_cooltime_file, "Tr013_C1p")
C2p = get_tracer(low_den_cooltime_file, "Tr014_C2p")
C3p = get_tracer(low_den_cooltime_file, "Tr015_C3p")
C4p = get_tracer(low_den_cooltime_file, "Tr016_C4p")
C5p = get_tracer(low_den_cooltime_file, "Tr017_C5p")
C6p = X_C - C0 - C1p - C2p - C3p - C4p - C5p

ax3.set_ylabel(r'$\rm Ionisation \ fraction$', fontsize=14, labelpad=8)
ax3.plot(x_ldot, C0 / X_C, label=r'$\rm C$', linewidth=1.5, color='red')
ax3.plot(x_ldot, C1p / X_C, label=r'$\rm C^{+}$', linewidth=1.5, linestyle='-', color='black')
# Use UnivariateSpline to smooth the data
spline = UnivariateSpline(x_ldot, C4p / X_C, s=0.2)
norm_C4p_smooth = spline(x_ldot)
norm_C4p_smooth[norm_C4p_smooth < 0] = 0
ax3.plot(x_ldot, norm_C4p_smooth, label=r'$\rm C^{4+}$', linewidth=1.5, color='darkgreen', linestyle='-')
ax3.plot(x_ldot, C5p / X_C, label=r'$\rm C^{5+}$', linewidth=1.5, color='orange')
ax3.plot(x_ldot, C6p / X_C, label=r'$\rm C^{6+}$', linewidth=1.5, color='darkblue', linestyle='-')
ax3.set_xlim(0.8, 2.2)
ax3.legend(frameon=False, fontsize=12, ncol=2, columnspacing=0.5)
ax3.tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True,
                right=True, length=3, labelsize=14)

ax3.set_xlabel(r'\rm x (10$^{19}$ cm)', fontsize=14, labelpad=16)


# Adjust the position of each subplot manually
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.3)
plt.tight_layout()
plt.savefig(output_dir + 'non-adiabatic_analysis_cooltime.png')
plt.close(fig)

#######################################################################
# Plot 2 - two distinct density
#######################################################################
fig, ax = plt.subplots(1, 1, figsize=(5, 4))
### Panel - 4 for distict densities
ax.set_xlabel(r'$\rm x \, (10^{19} cm)$', fontsize=14)
ax.set_ylabel(r'$\rm log \, T \, (K)$', fontsize=14)
ax.plot(x_ldst, np.log10(get_temperature(low_den_cooltime_file)), color='darkblue',
           linestyle='--', linewidth=1.5, label=r'$\rm \rho_1 $')
ax.plot(x_hdot, np.log10(get_temperature(high_den_cooltime_file)), color='crimson',
           linewidth=1.5, label=r'$\rm \rho_2$')
ax.set_xlim(0.05, 9)
ax.set_ylim(3.2, 7.25)
ax.legend(frameon=False, fontsize=16, bbox_to_anchor=(0.9, 0.8))
ax.tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True,
                right=True, length=3, labelsize=14)

plt.tight_layout()
plt.savefig(output_dir + 'non-adiabatic_analysis_densities.png')
plt.close()