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

fig, axs = plt.subplots(3, 1, figsize=(14, 14))
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
axs[0].plot(temperature_cx_off, Ne3p / X_Ne, label="$\mathrm{Ne}^{3+}$", color='black')
axs[0].plot(temperature_cx_off, Ne4p / X_Ne, label="$\mathrm{Ne}^{4+}$", color='black')
axs[0].plot(temperature_cx_off, Ne5p / X_Ne, label="$\mathrm{Ne}^{5+}$", color='black')
axs[0].plot(temperature_cx_off, Ne6p / X_Ne, label="$\mathrm{Ne}^{6+}$", color='black')
axs[0].plot(temperature_cx_off, Ne7p / X_Ne, label="$\mathrm{Ne}^{7+}$", color='black')
axs[0].plot(temperature_cx_off, Ne8p / X_Ne, label="$\mathrm{Ne}^{8+}$", color='black')
axs[0].plot(temperature_cx_off, Ne9p / X_Ne, label="$\mathrm{Ne}^{9+}$", color='black')
axs[0].plot(temperature_cx_off, Ne10p / X_Ne, label="$\mathrm{Ne}^{10+}$", color='black')

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

axs[0].plot(temperature_cx_off, Ne0 / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_off, Ne1p / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_off, Ne2p / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_off, Ne3p / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_off, Ne4p / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_off, Ne5p / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_off, Ne6p / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_off, Ne7p / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_off, Ne8p / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_off, Ne9p / X_Ne, linestyle='--', color='black')
axs[0].plot(temperature_cx_off, Ne10p / X_Ne, linestyle='--', color='black')


axs[0].tick_params(labelsize=16)
axs[0].legend(fontsize=12, loc="lower right")
axs[0].set_ylabel("Ionisation Fraction", fontsize=16)
axs[0].set_xlabel(r"T (K)", fontsize=16)
axs[0].set_yscale('log')
axs[0].set_ylim(1, 10**-2)
axs[0].set_xlim(4.0, 5.2)  # Set the x-axis limits from 4.0 to 9.0

outfile = output_dir + "cx_cie_aspulnd09.png"
print("saving " + outfile)
plt.savefig(outfile, bbox_inches="tight")
plt.close(fig)
del fig
