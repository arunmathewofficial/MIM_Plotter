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

plot = 'Flam'

if plot == 'EFE':
    y_neq = np.log10(lflam_neq)
    x_neq = np.log10(energy_neq)
    y_eq = np.log10(lflam_eq)
    x_eq = np.log10(energy_eq)

if plot == 'Flam':
    x_neq = wavelength_neq
    y_neq = spectrum_neq
    x_eq = wavelength_eq
    y_eq = spectrum_eq


fig, ax = plt.subplots(nrows=3, ncols=1, figsize=(8, 12), sharex=False, sharey=False)
ax[0].plot(x_neq, y_neq, label='NEQ', color='crimson', linestyle='-', linewidth=1)
ax[1].plot(x_eq, y_eq, label='IEQ', color='blue', linestyle='-', linewidth=1)
ax[0].tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True, right=True, length=4,
               labelsize=20)
ax[0].legend(fontsize=17, frameon=False)

ax[1].tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True, right=True, length=4,
               labelsize=20)
ax[1].legend(fontsize=17, frameon=False)


ax[2].plot(x_neq, y_neq, label='NEQ', color='crimson', linestyle='-', linewidth=1)
ax[2].plot(x_eq, y_eq, label='IEQ', color='blue', linestyle='-', linewidth=1)

ax[2].tick_params(axis="both", direction="in", which="both", bottom=True, top=True, left=True, right=True, length=4,
               labelsize=20)
ax[2].legend(fontsize=17, frameon=False)


if plot == 'FEF':
    ax[0].set_ylabel(r'log (E F$_E$) (erg cm$^{-2}$  s$^{-1}$)', fontsize=20)
    ax[0].set_xlabel('log E (keV)', fontsize=18)
    ax[1].set_ylabel(r'log (E F$_E$) (erg cm$^{-2}$  s$^{-1}$)', fontsize=20)
    ax[1].set_xlabel('log E (keV)', fontsize=18)
    ax[2].set_ylabel(r'log (E F$_E$) (erg cm$^{-2}$  s$^{-1}$)', fontsize=20)
    ax[2].set_xlabel('log E (keV)', fontsize=18)

if plot == 'Flam':
    ax[0].set_ylabel(r'log (F$_\lambda$) (erg cm$^{-2}$  s$^{-1}$ $\AA^{-1}$)', fontsize=20)
    ax[0].set_xlabel(r'$\lambda$ ($\AA^{-1}$)', fontsize=18)
    ax[1].set_ylabel(r'log (F$_\lambda$) (erg cm$^{-2}$  s$^{-1}$ $\AA^{-1}$)', fontsize=20)
    ax[1].set_xlabel(r'$\lambda$ ($\AA^{-1}$)', fontsize=18)
    ax[2].set_ylabel(r'log (F$_\lambda$) (erg cm$^{-2}$  s$^{-1}$ $\AA^{-1}$)', fontsize=20)
    ax[2].set_xlabel(r'$\lambda$ ($\AA^{-1}$)', fontsize=18)


imagefile = output_dir + 'xray_spectrum_fb.png'
print("Saving image " + imagefile)
plt.subplots_adjust(left=0.13, right=0.98, top=0.98, bottom=0.13, hspace=0.0)
plt.savefig(imagefile)
plt.close()