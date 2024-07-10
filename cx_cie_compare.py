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

fig, axs = plt.subplots(1, 2, figsize=(5, 8))

# NITROGEN ##############################################################
# y data - neon species cx off ###########
X_N = get_tracer(cx_off_cie_silo, "Tr005_X_N")
N0 = get_tracer(cx_off_cie_silo, "Tr033_N")
N1p = get_tracer(cx_off_cie_silo, "Tr034_N1p")
N2p = get_tracer(cx_off_cie_silo, "Tr035_N2p")
N3p = get_tracer(cx_off_cie_silo, "Tr036_N3p")
N4p = get_tracer(cx_off_cie_silo, "Tr037_N4p")

axs[0].plot(temperature_cx_off, N0 / X_N, label="$\mathrm{Ne}^{0}$", color='black')
axs[0].plot(temperature_cx_off, N1p / X_N, label="$\mathrm{Ne}^{+}$", color='black')
axs[0].plot(temperature_cx_off, N2p / X_N, label="$\mathrm{Ne}^{2+}$", color='black')
axs[0].plot(temperature_cx_off, N3p / X_N, label="$\mathrm{Ne}^{3+}$", color='black')
axs[0].plot(temperature_cx_off, N4p / X_N, label="$\mathrm{Ne}^{4+}$", color='black')

# y data - neon species cx on ###########
X_N = get_tracer(cx_on_cie_silo, "Tr005_X_N")
N0 = get_tracer(cx_on_cie_silo, "Tr033_N")
N1p = get_tracer(cx_on_cie_silo, "Tr034_N1p")
N2p = get_tracer(cx_on_cie_silo, "Tr035_N2p")
N3p = get_tracer(cx_on_cie_silo, "Tr036_N3p")
N4p = get_tracer(cx_on_cie_silo, "Tr037_N4p")

axs[0].plot(temperature_cx_on, N0 / X_N, linestyle='--', color='black')
axs[0].plot(temperature_cx_on, N1p / X_N, linestyle='--', color='black')
axs[0].plot(temperature_cx_on, N2p / X_N, linestyle='--', color='black')
axs[0].plot(temperature_cx_on, N3p / X_N, linestyle='--', color='black')
axs[0].plot(temperature_cx_on, N4p / X_N, linestyle='--', color='black')

axs[0].tick_params(labelsize=16)
axs[0].legend(fontsize=12, loc="lower right")
axs[0].set_ylabel(r"\rm Ionisation Fraction", fontsize=16)
axs[0].set_xlabel(r"\rm T (K)", fontsize=16)
axs[0].set_yscale('log')
axs[0].set_ylim(10**-2, 1.0)
axs[0].set_xlim(4.0, 5.2)


# OXYGEN ################################################################
# NITROGEN ##############################################################
# y data - neon species cx off ###########
X_O = get_tracer(cx_off_cie_silo, "Tr005_X_O")
O0 = get_tracer(cx_off_cie_silo, "Tr033_O")
O1p = get_tracer(cx_off_cie_silo, "Tr034_O1p")
O2p = get_tracer(cx_off_cie_silo, "Tr035_O2p")
O3p = get_tracer(cx_off_cie_silo, "Tr036_O3p")
O4p = get_tracer(cx_off_cie_silo, "Tr037_O4p")

axs[0].plot(temperature_cx_off, O0 / X_O, label="$\mathrm{Ne}^{0}$", color='black')
axs[0].plot(temperature_cx_off, O1p / X_O, label="$\mathrm{Ne}^{+}$", color='black')
axs[0].plot(temperature_cx_off, O2p / X_O, label="$\mathrm{Ne}^{2+}$", color='black')
axs[0].plot(temperature_cx_off, O3p / X_O, label="$\mathrm{Ne}^{3+}$", color='black')
axs[0].plot(temperature_cx_off, O4p / X_O, label="$\mathrm{Ne}^{4+}$", color='black')

# y data - neon species cx on ###########
X_O = get_tracer(cx_on_cie_silo, "Tr005_X_O")
O0 = get_tracer(cx_on_cie_silo, "Tr033_O")
O1p = get_tracer(cx_on_cie_silo, "Tr034_O1p")
O2p = get_tracer(cx_on_cie_silo, "Tr035_O2p")
O3p = get_tracer(cx_on_cie_silo, "Tr036_O3p")
O4p = get_tracer(cx_on_cie_silo, "Tr037_O4p")

axs[0].plot(temperature_cx_on, O0 / X_O, linestyle='--', color='black')
axs[0].plot(temperature_cx_on, O1p / X_O, linestyle='--', color='black')
axs[0].plot(temperature_cx_on, O2p / X_O, linestyle='--', color='black')
axs[0].plot(temperature_cx_on, O3p / X_O, linestyle='--', color='black')
axs[0].plot(temperature_cx_on, O4p / X_O, linestyle='--', color='black')

axs[0].tick_params(labelsize=16)
axs[0].legend(fontsize=12, loc="lower right")
axs[0].set_ylabel(r"\rm Ionisation Fraction", fontsize=16)
axs[0].set_xlabel(r"\rm T (K)", fontsize=16)
axs[0].set_yscale('log')
axs[0].set_ylim(10**-2, 1.0)
axs[0].set_xlim(4.0, 5.2)

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

axs[0].plot(temperature_cx_off, Ne0 / X_Ne, label="$\mathrm{Ne}^{0}$", color='black')
axs[0].plot(temperature_cx_off, Ne1p / X_Ne, label="$\mathrm{Ne}^{+}$", color='black')
axs[0].plot(temperature_cx_off, Ne2p / X_Ne, label="$\mathrm{Ne}^{2+}$", color='black')
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

axs[0].plot(temperature_cx_on, Ne0 / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_on, Ne1p / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_on, Ne2p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne3p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne4p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne5p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne6p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne7p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne8p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne9p / X_Ne, linestyle='--', color='black')
#axs[0].plot(temperature_cx_on, Ne10p / X_Ne, linestyle='--', color='black')

axs[0].tick_params(labelsize=16)
axs[0].legend(fontsize=12, loc="lower right")
axs[0].set_ylabel(r"\rm Ionisation Fraction", fontsize=16)
axs[0].set_xlabel(r"\rm T (K)", fontsize=16)
axs[0].set_yscale('log')
axs[0].set_ylim(10**-2, 1.0)
axs[0].set_xlim(4.0, 5.2)

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
axs[1].plot(temperature_cx_off, Si1p / X_Si, label="$\mathrm{Si}^{+}$", color='black')
axs[1].plot(temperature_cx_off, Si2p / X_Si, label="$\mathrm{Si}^{2+}$", color='black')
axs[1].plot(temperature_cx_off, Si3p / X_Si, label="$\mathrm{Si}^{3+}$", color='black')
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
axs[1].plot(temperature_cx_on, Si1p / X_Si, color='black', linestyle='--')
axs[1].plot(temperature_cx_on, Si2p / X_Si, color='black', linestyle='--')
axs[1].plot(temperature_cx_on, Si3p / X_Si, color='black', linestyle='--')
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

axs[1].tick_params(labelsize=16)
axs[1].legend(fontsize=12, loc="lower right")
axs[1].set_ylabel(r"\rm Ionisation Fraction", fontsize=16)
axs[1].set_xlabel(r"\rm T (K)", fontsize=16)
axs[1].set_yscale('log')
axs[1].set_ylim(10**-2, 1.0)
axs[1].set_xlim(4.0, 5.0)

outfile = output_dir + "cx_cie_aspulnd09.png"
print("saving " + outfile)
plt.savefig(outfile, bbox_inches="tight")
plt.close(fig)
del fig
