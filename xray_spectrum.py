# Author: Arun Mathew
# Created: 10-11-2022
# Plotting xray spectrum
import constant
from tools import *
import numpy as np
import matplotlib.pyplot as plt
import argparse

plt.rc('font', family='serif', serif=['Times New Roman'])
plt.legend(prop={'family': 'Times New Roman'})

parser = argparse.ArgumentParser()
parser.add_argument("xray_spectrum_neq", type=str, help="line luminosity txt file")
parser.add_argument("xray_spectrum_eq", type=str, help="line luminosity txt file")
parser.add_argument("output_dir", type=str, help="output dir path")
args = parser.parse_args()
output_dir = args.output_dir

output_dir = make_directory(output_dir)
xray_spectrum_neq = args.xray_spectrum_neq
xray_spectrum_eq = args.xray_spectrum_eq

xray_spectrum_neq_data = np.loadtxt(xray_spectrum_neq, comments='#')
# Extract data from each column into separate arrays
wavelength_neq = xray_spectrum_neq_data[:, 0]
spectrum_neq = xray_spectrum_neq_data[:, 1]

xray_spectrum_eq_data = np.loadtxt(xray_spectrum_eq, comments='#')
# Extract data from each column into separate arrays
wavelength_eq = xray_spectrum_eq_data[:, 0]
spectrum_eq = xray_spectrum_eq_data[:, 1]


lflam_neq = wavelength_neq * spectrum_neq
energy_neq = 10**-3 * constant.ev2Ang / wavelength_neq

lflam_eq = wavelength_eq * spectrum_eq
energy_eq = 10**-3 * constant.ev2Ang / wavelength_eq

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6), sharex=False, sharey=False)
ax.plot(np.log10(energy_neq), np.log10(lflam_neq), label='NEQ', color='crimson', linestyle='-', linewidth=1)
ax.plot(np.log10(energy_eq), np.log10(lflam_eq), label='IEQ', color='blue', linestyle='-', linewidth=1)
#ax.set_yscale('log')
#ax.set_xscale("log")
#ax.set_xlim(0.5, 4)
ax.set_ylabel(r'log (E F$_E$) (erg cm$^{-2}$  s$^{-1}$)', fontsize=20)
ax.set_xlabel('log E (keV)', fontsize=18)
ax.tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True, right=True, length=4,
               labelsize=20)
ax.legend(fontsize=17, frameon=False)
imagefile = output_dir + 'xray_spectrum.png'
print("Saving image " + imagefile)
plt.subplots_adjust(left=0.13, right=0.98, top=0.98, bottom=0.13, hspace=0.0)
plt.savefig(imagefile)
plt.close()