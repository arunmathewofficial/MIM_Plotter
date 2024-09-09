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
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 4), sharex=True)

# Panel - 1 Temperature profile
ax1.set_ylabel(r'$\rm log_{10} \ Quantities$', fontsize=14, labelpad=8)
ax1.plot(x_ldst, np.log10(get_temperature(low_den_subtime_file)), label=r'$\rm T (K)$',
           color='crimson', linewidth=1.5)
ax1.plot(x_ldst, np.log10(get_density(low_den_subtime_file) * 1.e+27),
         label=r'$\rho\, \left(10^{-27} \, \mathrm{g\,cm}^{-3} \right)$',
           color='darkblue', linestyle='--', linewidth=1.5)
ax1.text(1.5, 6.8, r'$\rm t_1 = 1.2945\times10^4 \, yr$', fontsize=14)
ax1.legend(frameon=False, fontsize=12, loc=(0.55, 0.4))
ax1.set_xlim(0.1, 9)
#ax1.set_ylim(3.2, 7.6)
ax1.tick_params(axis="both", direction="in", which="both", bottom=True,
                top=True, left=True, right=True, length=3, labelsize=12)
ax1.set_yticks([3.2, 4, 5, 6, 7])


# Panel - 1 Temperature profile
ax2.set_ylabel(r'$\rm log_{10} \ Quantities$', fontsize=14, labelpad=8)
ax2.plot(x_ldst, np.log10(get_temperature(low_den_cooltime_file)),
           color='crimson', linewidth=1.5)
ax2.plot(x_ldst, np.log10(get_density(low_den_cooltime_file) * 1.e+27),
           color='darkblue', linestyle='--', linewidth=1.5)
ax2.text(0.5, 7.0, r'$\rm t_2 = 1.2799\times10^5 \, yr$', fontsize=14)
ax2.legend(frameon=False, fontsize=12, loc=(0.5, 0.3))
ax2.set_xlim(0.1, 9)
ax2.set_ylim(3.2, 7.6)
ax2.set_xlabel(r'$\rm x \, (10^{19} \, cm)$', fontsize=14)
ax2.tick_params(axis="both", direction="in", which="both", bottom=True,
                top=True, left=True, right=True, length=3, labelsize=12)
ax2.set_yticks([3.2, 4, 5, 6, 7])

# Save data to file the temperature profile with low density gas
T_profile_data = {'x(pc)': x_ldot, 'T (K)': get_temperature(low_den_cooltime_file)}
df = pd.DataFrame(T_profile_data)

print('Printing temperature profile data to file ...')
df.to_csv(output_dir + 'non-adiabatic_temp_profile.txt', sep='\t', index=False, float_format='%e')


# Adjust the position of each subplot manually
plt.subplots_adjust(left=0.13, right=0.98, top=0.98, bottom=0.13, wspace=0.0, hspace=0.0)
#plt.tight_layout()
plt.savefig(output_dir + 'non-adiabatic_analysis_flowquan.png')
plt.close(fig)



# Ionisation profile
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 4.5))
# Panel - 2 H, He, ionisation profile
X_H = get_tracer(low_den_cooltime_file, 'Tr000_X_H')
H0 = get_tracer(low_den_cooltime_file, 'Tr009_H')
H1p = X_H - H0
X_He = get_tracer(low_den_cooltime_file, "Tr001_X_He")
He0 = get_tracer(low_den_cooltime_file, "Tr010_He")
He1p = get_tracer(low_den_cooltime_file, "Tr011_He1p")
He2p = X_He - He0 - He1p

ax1.set_ylabel(r'$\rm Ionisation \ fraction$', fontsize=14, labelpad=8)
ax1.plot(x_ldot, H0 / X_H, label=r'$\rm H$', linewidth=1.3, color='crimson', linestyle='--')
ax1.plot(x_ldot, H1p / X_H, label=r'$\rm H^{+}$', linewidth=1.3, color='darkblue', linestyle='--')
ax1.plot(x_ldot, He0 / X_He, label=r'$\rm He$', linewidth=1.3, linestyle='-', color='crimson')
ax1.plot(x_ldot, He1p / X_He, label=r'$\rm He^{+}$', linewidth=1.3, linestyle='-', color='darkgreen')
ax1.plot(x_ldot, He2p / X_He, label=r'$\rm He^{2+}$', linewidth=1.3, linestyle='-', color='darkblue')
ax1.set_xlim(0.01, 1.8)
#ax2.set_xlabel(r'\rm x (10$^{19}$ cm)', fontsize=16)
ax1.legend(frameon=False, fontsize=12, ncol=2)
ax1.tick_params(axis="both", direction="in", which="both", bottom=True,
                top=True, left=True, right=True, length=3, labelsize=12)
plt.setp(ax1.get_xticklabels(), visible=True)

# Panel - 3 Carbon ionisation profile
X_C = get_tracer(low_den_cooltime_file, "Tr002_X_C")
C0 = get_tracer(low_den_cooltime_file, "Tr012_C")
C1p = get_tracer(low_den_cooltime_file, "Tr013_C1p")
C2p = get_tracer(low_den_cooltime_file, "Tr014_C2p")
C3p = get_tracer(low_den_cooltime_file, "Tr015_C3p")
C4p = get_tracer(low_den_cooltime_file, "Tr016_C4p")
C5p = get_tracer(low_den_cooltime_file, "Tr017_C5p")
C6p = X_C - C0 - C1p - C2p - C3p - C4p - C5p

ax2.set_ylabel(r'$\rm Ionisation \ fraction$', fontsize=14, labelpad=8)
ax2.plot(x_ldot, C0 / X_C, label=r'$\rm C$', linewidth=1.3, color='red')
ax2.plot(x_ldot, C1p / X_C, label=r'$\rm C^{+}$', linewidth=1.3, linestyle='--', color='darkblue')
# Use UnivariateSpline to smooth the data
spline = UnivariateSpline(x_ldot, C4p / X_C, s=0.2)
norm_C4p_smooth = spline(x_ldot)
norm_C4p_smooth[norm_C4p_smooth < 0] = 0
ax2.plot(x_ldot, norm_C4p_smooth, label=r'$\rm C^{4+}$', linewidth=1.3, color='darkgreen', linestyle='-')
ax2.plot(x_ldot, C5p / X_C, label=r'$\rm C^{5+}$', linewidth=1.3, color='crimson', linestyle='--')
ax2.plot(x_ldot, C6p / X_C, label=r'$\rm C^{6+}$', linewidth=1.3, color='darkblue', linestyle='-')
ax2.set_xlim(0.8, 2.2)
ax2.legend(frameon=False, fontsize=12, ncol=2, columnspacing=0.5)
ax2.tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True,
                right=True, length=3, labelsize=12)

ax2.set_xlabel(r'\rm x (10$^{19}$ cm)', fontsize=14, labelpad=16)


# Adjust the position of each subplot manually
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1, wspace=0.4, hspace=0.3)
plt.tight_layout()
plt.savefig(output_dir + 'non-adiabatic_analysis_ionisation.png')
plt.close(fig)

#######################################################################
# Plot 2 - two distinct density
#######################################################################
fig, ax = plt.subplots(1, 1, figsize=(5, 4))
### Panel - 4 for distict densities
ax.set_xlabel(r'$\rm x \, (10^{19} cm)$', fontsize=14)
ax.set_ylabel(r'$\rm log \, T \, (K)$', fontsize=14)
ax.plot(x_ldst, get_temperature(low_den_cooltime_file), color='darkblue',
           linestyle='--', linewidth=1.5, label=r'$\rm \rho_1 $')
ax.plot(x_hdot, get_temperature(high_den_cooltime_file), color='crimson',
           linewidth=1.5, label=r'$\rm \rho_2$')
ax.set_yscale('log')
ax.set_xlim(0.05, 9)
ax.set_ylim(10**3.2, 10**7.3)
ax.legend(frameon=False, fontsize=16, bbox_to_anchor=(0.9, 0.8))
ax.tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True,
                right=True, length=3, labelsize=12)

plt.tight_layout()
plt.savefig(output_dir + 'non-adiabatic_analysis_densities.png')
plt.close()