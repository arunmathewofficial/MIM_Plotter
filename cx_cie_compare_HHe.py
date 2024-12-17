# Author: Arun Mathew
# Created: 07-03-2023
# Script to compare cie ionisation profile of Ne, Si,
# and Fe with and without charge-exchange reactions.

# Import required libraries: ##########################################
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("cx_off_cie_silo", type=str, help="give the input silo input_silo path")
parser.add_argument("cx_on_cie_silo", type=str, help="give the input silo input_silo path")
parser.add_argument("output_dir", type=str, help="give the output image dir path")

args = parser.parse_args()
cx_off_cie_silo = args.cx_off_cie_silo
cx_on_cie_silo = args.cx_on_cie_silo
output_dir = args.output_dir
output_dir = make_directory(output_dir)
abundance  = "asplund09"

# make plotting data and append to plot_data array
plot_data = []

# X-DATA ###############################################################
# x data cx off ##########################
temperature_cx_off = get_temperature(cx_off_cie_silo)
temperature_cx_off = np.log10(temperature_cx_off)
# x data cx on ##########################
temperature_cx_on = get_temperature(cx_on_cie_silo)
temperature_cx_on = np.log10(temperature_cx_on)

fig, axs = plt.subplots(2, 2, figsize=(14, 8))

# Hydrogen ##############################################################
# y data - hydrogen species cx off ###########
X_H = get_tracer(cx_off_cie_silo, "Tr000_X_H")
H0 = get_tracer(cx_off_cie_silo, "Tr009_H")
H1p = X_H - H0

axs[0, 0].plot(temperature_cx_off, H0 / X_H, color='darkblue', linestyle='--', linewidth=2.0)
axs[0, 0].plot(temperature_cx_off, H1p / X_H, color='darkblue', linestyle='--', linewidth=2.0)

# y data - neon species cx on ###########
X_H = get_tracer(cx_on_cie_silo, "Tr000_X_H")
H0 = get_tracer(cx_on_cie_silo, "Tr009_H")
H1p = X_H - H0

axs[0, 0].plot(temperature_cx_on, H0 / X_H, color='crimson', alpha=0.6, linewidth=2.0)
axs[0, 0].plot(temperature_cx_on, H1p / X_H, color='crimson', alpha=0.6, linewidth=2.0)


axs[0, 0].text(4.05, 0.7, '$\mathrm{H}$', fontsize=12, color='black')
axs[0, 0].text(4.4, 0.6, "$\mathrm{H}^{+}$", fontsize=12, color='black')

#axs[0, 0].text(4.97, 0.09, '$\mathbf{CX-ON}$', fontsize=12, color='crimson', alpha=0.6)
#axs[0, 0].text(4.97, 0.06, '$\mathbf{CX-OFF}$', fontsize=12, color='darkblue')

axs[0, 0].tick_params(labelsize=16)
axs[0, 0].set_ylabel(r"\rm Ionisation fraction", fontsize=16)
axs[0, 0].set_xlabel(r"\rm T (K)", fontsize=16)
axs[0, 0].set_yscale('log')
axs[0, 0].set_ylim(10**-2, 1.1)
axs[0, 0].set_xlim(4.0, 5.2)
axs[0, 0].tick_params(axis='both', which='major', length=5, direction='in')  # Major ticks
axs[0, 0].tick_params(axis='both', which='minor', length=5, direction='in')   # Minor ticks

# Helium ##############################################################
# y data - helium species cx off ###########
X_He = get_tracer(cx_off_cie_silo, "Tr001_X_He")
He0 = get_tracer(cx_off_cie_silo, "Tr010_He")
He1p = get_tracer(cx_off_cie_silo, "Tr011_He1p")
He2p = X_He - He0 - He1p

axs[0, 1].plot(temperature_cx_off, He0 / X_He, color='darkblue', linestyle='--', linewidth=2.0)
axs[0, 1].plot(temperature_cx_off, He1p / X_He, color='darkblue', linestyle='--', linewidth=2.0)
axs[0, 1].plot(temperature_cx_off, He2p / X_He, color='darkblue', linestyle='--', linewidth=2.0)

# y data - helium species cx on ###########
X_He = get_tracer(cx_on_cie_silo, "Tr001_X_He")
He0 = get_tracer(cx_on_cie_silo, "Tr010_He")
He1p = get_tracer(cx_on_cie_silo, "Tr011_He1p")
He2p = X_He - He0 - He1p

axs[0, 1].plot(temperature_cx_on, He0 / X_He, color='crimson', alpha=0.6, linewidth=2.0, label='$\mathbf{CX enabled}$')
axs[0, 1].plot(temperature_cx_on, He1p / X_He, color='crimson', alpha=0.6, linewidth=2.0)
axs[0, 1].plot(temperature_cx_on, He2p / X_He, color='crimson', alpha=0.6, linewidth=2.0)

axs[0, 1].text(4.05, 0.7, '$\mathrm{He}$', fontsize=12, color='black')
axs[0, 1].text(4.65, 0.6, "$\mathrm{He}^{+}$", fontsize=12, color='black')
axs[0, 1].text(5.0, 0.5, '$\mathrm{He}^{2+}$', fontsize=12, color='black')


#axs[0, 1].text(4.97, 0.09, '$\mathbf{CX-ON}$', fontsize=12, color='crimson', alpha=0.6)
#axs[0, 1].text(4.97, 0.06, '$\mathbf{CX-OFF}$', fontsize=12, color='darkblue')

axs[0, 1].tick_params(labelsize=16)
axs[0, 1].set_ylabel(r"\rm Ionisation fraction", fontsize=16)
axs[0, 1].set_xlabel(r"\rm T (K)", fontsize=16)
axs[0, 1].set_yscale('log')
axs[0, 1].set_ylim(10**-2, 1.1)
axs[0, 1].set_xlim(4.0, 5.2)
axs[0, 1].tick_params(axis='both', which='major', length=5, direction='in')  # Major ticks
axs[0, 1].tick_params(axis='both', which='minor', length=5, direction='in')   # Minor ticks

# NEON ###################################################################
# y data - neon species cx off ###########
X_Ne = get_tracer(cx_off_cie_silo, "Tr005_X_Ne")
Ne0 = get_tracer(cx_off_cie_silo, "Tr033_Ne")
Ne1p = get_tracer(cx_off_cie_silo, "Tr034_Ne1p")
Ne2p = get_tracer(cx_off_cie_silo, "Tr035_Ne2p")
Ne3p = get_tracer(cx_off_cie_silo, "Tr036_Ne3p")
Ne4p = get_tracer(cx_off_cie_silo, "Tr037_Ne4p")
Ne5p = get_tracer(cx_off_cie_silo, "Tr038_Ne5p")
Ne6p = get_tracer(cx_off_cie_silo, "Tr039_Ne6p")
Ne7p = get_tracer(cx_off_cie_silo, "Tr040_Ne7p")
Ne8p = get_tracer(cx_off_cie_silo, "Tr041_Ne8p")
Ne9p = get_tracer(cx_off_cie_silo, "Tr042_Ne9p")
Ne10p = X_Ne - (Ne0 + Ne1p + Ne2p + Ne3p + Ne4p + Ne5p + Ne6p + Ne7p + Ne8p + Ne9p)

axs[1, 0].plot(temperature_cx_off, Ne0 / X_Ne, color='darkblue', linestyle='--', linewidth=2.0, label='$\mathrm{CX \ Disabled}$')
axs[1, 0].plot(temperature_cx_off, Ne1p / X_Ne, color='darkblue', linestyle='--', linewidth=2.0)
axs[1, 0].plot(temperature_cx_off, Ne2p / X_Ne, color='darkblue', linestyle="--", linewidth=2.0)
#axs[0].plot(temperature_cx_off, Ne3p / X_Ne, label="$\mathrm{Ne}^{3+}$", color='black')
#axs[0].plot(temperature_cx_off, Ne4p / X_Ne, label="$\mathrm{Ne}^{4+}$", color='black')
#axs[0].plot(temperature_cx_off, Ne5p / X_Ne, label="$\mathrm{Ne}^{5+}$", color='black')
#axs[0].plot(temperature_cx_off, Ne6p / X_Ne, label="$\mathrm{Ne}^{6+}$", color='black')
#axs[0].plot(temperature_cx_off, Ne7p / X_Ne, label="$\mathrm{Ne}^{7+}$", color='black')
#axs[0].plot(temperature_cx_off, Ne8p / X_Ne, label="$\mathrm{Ne}^{8+}$", color='black')
#axs[0].plot(temperature_cx_off, Ne9p / X_Ne, label="$\mathrm{Ne}^{9+}$", color='black')
#axs[0].plot(temperature_cx_off, Ne10p / X_Ne, label="$\mathrm{Ne}^{10+}$", color='black')

# y data - neon species cx on ###########
X_Ne = get_tracer(cx_on_cie_silo, "Tr005_X_Ne")
Ne0 = get_tracer(cx_on_cie_silo, "Tr033_Ne")
Ne1p = get_tracer(cx_on_cie_silo, "Tr034_Ne1p")
Ne2p = get_tracer(cx_on_cie_silo, "Tr035_Ne2p")
Ne3p = get_tracer(cx_on_cie_silo, "Tr036_Ne3p")
Ne4p = get_tracer(cx_on_cie_silo, "Tr037_Ne4p")
Ne5p = get_tracer(cx_on_cie_silo, "Tr038_Ne5p")
Ne6p = get_tracer(cx_on_cie_silo, "Tr039_Ne6p")
Ne7p = get_tracer(cx_on_cie_silo, "Tr040_Ne7p")
Ne8p = get_tracer(cx_on_cie_silo, "Tr041_Ne8p")
Ne9p = get_tracer(cx_on_cie_silo, "Tr042_Ne9p")
Ne10p = X_Ne - (Ne0 + Ne1p + Ne2p + Ne3p + Ne4p + Ne5p + Ne6p + Ne7p + Ne8p + Ne9p)

axs[1, 0].plot(temperature_cx_on, Ne0 / X_Ne, color='crimson', alpha=0.6, linewidth=2.0, label='$\mathrm{CX \ Enabled}$')
axs[1, 0].plot(temperature_cx_on, Ne1p / X_Ne, color='crimson', alpha=0.6, linewidth=2.0)
axs[1, 0].plot(temperature_cx_on, Ne2p / X_Ne, color='crimson', alpha=0.6, linewidth=2.0)
#axs[0].plot(temperature_cx_on, Ne3p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne4p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne5p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne6p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne7p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne8p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne9p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne10p / X_Ne, linestyle='--', color='black')

axs[1, 0].text(4.1, 0.7, '$\mathrm{Ne}$', fontsize=12, color='black')
axs[1, 0].text(4.5, 0.6, "$\mathrm{Ne}^{+}$", fontsize=12, color='black')
axs[1, 0].text(4.9, 0.5, '$\mathrm{Ne}^{2+}$', fontsize=12, color='black')

#axs[1, 0].text(4.75, 0.03, '$\mathbf{CX-ON}$', fontsize=12, color='crimson', alpha=0.6)
#axs[1, 0].text(4.75, 0.02, '$\mathbf{CX-OFF}$', fontsize=12, color='darkblue')

axs[1, 0].legend(frameon=False, bbox_to_anchor=(0.7, 0.2), loc="center", fontsize=12)

axs[1, 0].tick_params(labelsize=16)
axs[1, 0].set_ylabel(r"\rm Ionisation fraction", fontsize=16)
axs[1, 0].set_xlabel(r"\rm T (K)", fontsize=16)
axs[1, 0].set_yscale('log')
axs[1, 0].set_ylim(10**-2, 1.1)
axs[1, 0].set_xlim(4.0, 5.2)
axs[1, 0].tick_params(axis='both', which='major', length=5, direction='in')  # Major ticks
axs[1, 0].tick_params(axis='both', which='minor', length=5, direction='in')   # Minor ticks

# Silicon ###################################################################
# y data - Silicon species cx off ###########
X_Si = get_tracer(cx_off_cie_silo, "Tr006_X_Si")
Si0 = get_tracer(cx_off_cie_silo, "Tr043_Si")
Si1p = get_tracer(cx_off_cie_silo, "Tr044_Si1p")
Si2p = get_tracer(cx_off_cie_silo, "Tr045_Si2p")
Si3p = get_tracer(cx_off_cie_silo, "Tr046_Si3p")
Si4p = get_tracer(cx_off_cie_silo, "Tr047_Si4p")
Si5p = get_tracer(cx_off_cie_silo, "Tr048_Si5p")
Si6p = get_tracer(cx_off_cie_silo, "Tr049_Si6p")
Si7p = get_tracer(cx_off_cie_silo, "Tr050_Si7p")
Si8p = get_tracer(cx_off_cie_silo, "Tr051_Si8p")
Si9p = get_tracer(cx_off_cie_silo, "Tr052_Si9p")
Si10p = get_tracer(cx_off_cie_silo, "Tr053_Si10p")
Si11p = get_tracer(cx_off_cie_silo, "Tr054_Si11p")
Si12p = get_tracer(cx_off_cie_silo, "Tr055_Si12p")
Si13p = get_tracer(cx_off_cie_silo, "Tr056_Si13p")
Si14p = X_Si - (Si0 + Si1p + Si2p + Si3p + Si4p + Si5p + Si6p
                + Si7p + Si8p + Si9p + Si10p + Si11p + Si12p + Si13p)

#axs[1].plot(temperature_cx_off, Si0 / X_Si, label="$\mathrm{Si}^{0}$", color='black')
axs[1, 1].plot(temperature_cx_off, Si1p / X_Si, color='darkblue', linestyle='--', linewidth=2.0)
axs[1, 1].plot(temperature_cx_off, Si2p / X_Si, color='darkblue', linestyle='--', linewidth=2.0)
axs[1, 1].plot(temperature_cx_off, Si3p / X_Si, color='darkblue', linestyle='--', linewidth=2.0)
#axs[1].plot(temperature_cx_off, Si4p / X_Si, label="$\mathrm{Si}^{4+}$", color='black')
#axs[1].plot(temperature_cx_off, Si5p / X_Si, label="$\mathrm{Si}^{5+}$", color='black')
#axs[1].plot(temperature_cx_off, Si6p / X_Si, label="$\mathrm{Si}^{6+}$", color='black')
#axs[1].plot(temperature_cx_off, Si7p / X_Si, label="$\mathrm{Si}^{7+}$", color='black')
#axs[1].plot(temperature_cx_off, Si8p / X_Si, label="$\mathrm{Si}^{8+}$", color='black')
#axs[1].plot(temperature_cx_off, Si9p / X_Si, label="$\mathrm{Si}^{9+}$", color='black')
#axs[1].plot(temperature_cx_off, Si10p / X_Si, label="$\mathrm{Si}^{10+}$", color='black')
#axs[1].plot(temperature_cx_off, Si11p / X_Si, label="$\mathrm{Si}^{11+}$", color='black')
#axs[1].plot(temperature_cx_off, Si12p / X_Si, label="$\mathrm{Si}^{12+}$", color='black')
#axs[1].plot(temperature_cx_off, Si13p / X_Si, label="$\mathrm{Si}^{13+}$", color='black')
#axs[1].plot(temperature_cx_off, Si14p / X_Si, label="$\mathrm{Si}^{14+}$", color='black')

# y data - neon species cx on ###########
X_Si = get_tracer(cx_on_cie_silo, "Tr006_X_Si")
Si0 = get_tracer(cx_on_cie_silo, "Tr043_Si")
Si1p = get_tracer(cx_on_cie_silo, "Tr044_Si1p")
Si2p = get_tracer(cx_on_cie_silo, "Tr045_Si2p")
Si3p = get_tracer(cx_on_cie_silo, "Tr046_Si3p")
Si4p = get_tracer(cx_on_cie_silo, "Tr047_Si4p")
Si5p = get_tracer(cx_on_cie_silo, "Tr048_Si5p")
Si6p = get_tracer(cx_on_cie_silo, "Tr049_Si6p")
Si7p = get_tracer(cx_on_cie_silo, "Tr050_Si7p")
Si8p = get_tracer(cx_on_cie_silo, "Tr051_Si8p")
Si9p = get_tracer(cx_on_cie_silo, "Tr052_Si9p")
Si10p = get_tracer(cx_on_cie_silo, "Tr053_Si10p")
Si11p = get_tracer(cx_on_cie_silo, "Tr054_Si11p")
Si12p = get_tracer(cx_on_cie_silo, "Tr055_Si12p")
Si13p = get_tracer(cx_on_cie_silo, "Tr056_Si13p")
Si14p = X_Si - (Si0 + Si1p + Si2p + Si3p + Si4p + Si5p + Si6p
                + Si7p + Si8p + Si9p + Si10p + Si11p + Si12p + Si13p)

#axs[1].plot(temperature_cx_on, Si0 / X_Si, color='black', linestyle='--')
axs[1, 1].plot(temperature_cx_on, Si1p / X_Si, color='crimson', alpha=0.6, linewidth=2.0)
axs[1, 1].plot(temperature_cx_on, Si2p / X_Si, color='crimson', alpha=0.6, linewidth=2.0)
axs[1, 1].plot(temperature_cx_on, Si3p / X_Si, color='crimson', alpha=0.6, linewidth=2.0)
#axs[1].plot(temperature_cx_on, Si4p / X_Si, color='black', linestyle='--')
#axs[1].plot(temperature_cx_on, Si5p / X_Si, color='black', linestyle='--')
#axs[1].plot(temperature_cx_on, Si6p / X_Si, color='black', linestyle='--')
#axs[1].plot(temperature_cx_on, Si7p / X_Si, color='black', linestyle='--')
#axs[1].plot(temperature_cx_on, Si8p / X_Si, color='black', linestyle='--')
#axs[1].plot(temperature_cx_on, Si9p / X_Si, color='black', linestyle='--')
#axs[1].plot(temperature_cx_on, Si10p / X_Si, color='black', linestyle='--')
#axs[1].plot(temperature_cx_on, Si11p / X_Si, color='black', linestyle='--')
#axs[1].plot(temperature_cx_on, Si12p / X_Si, color='black', linestyle='--')
#axs[1].plot(temperature_cx_on, Si13p / X_Si, color='black', linestyle='--')
#axs[1].plot(temperature_cx_on, Si14p / X_Si, color='black', linestyle='--')


axs[1, 1].text(4.1, 0.7, '$\mathrm{Si}$', fontsize=14, color='black')
axs[1, 1].text(4.6, 0.5, "$\mathrm{Si}^{+}$", fontsize=14, color='black')
axs[1, 1].text(4.8, 0.1, '$\mathrm{Si}^{2+}$', fontsize=14, color='black')

#axs[1, 1].text(4.27, 0.03, '$\mathbf{CX-ON}$', fontsize=12, color='crimson', alpha=0.6)
#axs[1, 1].text(4.27, 0.02, '$\mathbf{CX-OFF}$', fontsize=12, color='darkblue')

axs[1, 1].tick_params(labelsize=16)
axs[1, 1].set_ylabel(r"\rm Ionisation fraction", fontsize=16)
axs[1, 1].set_xlabel(r"\rm T (K)", fontsize=16)
axs[1, 1].set_yscale('log')
axs[1, 1].set_ylim(10**-2, 1.1)
axs[1, 1].set_xlim(4.0, 5.0)

axs[1, 1].tick_params(axis='both', which='major', length=5, direction='in')  # Major ticks
axs[1, 1].tick_params(axis='both', which='minor', length=5, direction='in')   # Minor ticks

plt.subplots_adjust(hspace=0.3)  # Increase horizontal space between plots
outfile = output_dir + "CX_CIE_Aspulnd09_Compare_HHe.png"
print("saving " + outfile)
plt.savefig(outfile, bbox_inches="tight")
plt.close(fig)
del fig
