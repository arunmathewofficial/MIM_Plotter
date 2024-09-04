# Author: Arun Mathew
# Created: 10-11-2022
# Plotting luminosity vs time

from tools import *
import numpy as np
import matplotlib.pyplot as plt
import argparse

plt.rc('font', family='serif', serif=['Times New Roman'])
plt.legend(prop={'family': 'Times New Roman'})

parser = argparse.ArgumentParser()
parser.add_argument("luminosity_set1_file", type=str, help="line luminosity txt file")
parser.add_argument("luminosity_set2_file", type=str, help="line luminosity txt file")
parser.add_argument("output_dir", type=str, help="output dir path")
args = parser.parse_args()
output_dir = args.output_dir

output_dir = make_directory(output_dir)
line_luminosity_set1 = args.luminosity_set1_file
line_luminosity_set2 = args.luminosity_set2_file

# Species vs Walltime for Nthreads = 10 ##############################
line_luminosity_set1 = np.loadtxt(line_luminosity_set1, comments='#')
# Extract data from each column into separate arrays
time = line_luminosity_set1[:, 0]
luminosity_OIII4960 = line_luminosity_set1[:, 1]
luminosity_OIII5008 = line_luminosity_set1[:, 2]
luminosity_OIV258933 = line_luminosity_set1[:, 3]
luminosity_OVI1032 = line_luminosity_set1[:, 4]
luminosity_OVI1038 = line_luminosity_set1[:, 5]

line_luminosity_set2 = np.loadtxt(line_luminosity_set2, comments='#')
# Extract data from each column into separate arrays
luminosity_NIV3479 = line_luminosity_set2[:, 1]
luminosity_NIV3485 = line_luminosity_set2[:, 2]
luminosity_OIV3404 = line_luminosity_set2[:, 3]
luminosity_OIV3414 = line_luminosity_set2[:, 4]
luminosity_OVI3812 = line_luminosity_set2[:, 5]
luminosity_OVI3835 = line_luminosity_set2[:, 6]



fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 8), sharex=False, sharey=False)

print('Plotting line luminosity as fucntion of time')
ax.plot(time, luminosity_OIII4960, label=r'OIII $\lambda$4959', color='crimson',
        linestyle='--', linewidth=2.5)
ax.plot(time, luminosity_OIII5008, label=r'OIII $\lambda$5007', color='blue',
        linestyle='--', linewidth=2.5)
ax.plot(time, luminosity_OIV258933, label=r'OIV $\lambda$258933', color='gray',
        linestyle='--', linewidth=2.5)
ax.plot(time, luminosity_OVI1032, label=r'OVI $\lambda$1032', color='black',
        linestyle='--', linewidth=2.5)
ax.plot(time, luminosity_OVI1038, label=r'OVI $\lambda$1038', color='magenta',
        linestyle='--', linewidth=2.5)

ax.plot(time, luminosity_NIV3479, label=r'NIV $\lambda$3478', color='darkgreen',
        linestyle='-', linewidth=2.5)
ax.plot(time, luminosity_NIV3485, label=r'NIV $\lambda$3485', color='blue',
        linestyle='-', linewidth=2.5)
ax.plot(time, luminosity_OIV3404, label=r'OIV $\lambda$3403', color='crimson',
        linestyle='-', linewidth=2.5)
ax.plot(time, luminosity_OIV3414, label=r'OIV $\lambda$3413', color='black',
        linestyle='-', linewidth=2.5)
ax.plot(time, luminosity_OVI3812, label=r'OVI $\lambda$3811', color='magenta',
        linestyle='-', linewidth=2.5)
ax.plot(time, luminosity_OVI3835, label=r'OVI $\lambda$3834', color='gray',
        linestyle='-', linewidth=2.5)



ax.legend(fontsize=17, loc="upper right", ncol=3, frameon=False, columnspacing=2.3, bbox_to_anchor=(1, 1.27))
ax.set_ylabel('Luminosity (erg s$^{-1}$)', fontsize=20)
ax.set_xlabel('time (kyr)', fontsize=18)
ax.set_xlim(0.0, 65)
ax.set_ylim(1.e+26, 1.e+36)
ax.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4,
               labelsize=20)
ax.set_yscale('log')




fig.tight_layout()
imagefile = output_dir + 'lines_luminosity.png'
print("Saving image " + imagefile)
plt.subplots_adjust(left=0.13, right=0.98, top=0.82, bottom=0.1, hspace=0.0)
plt.savefig(imagefile)
plt.close()


'''
####################################################################################
fig, ax = plt.subplots(nrows=4, ncols=1, figsize=(8, 14), sharex=True, sharey=False)

print('Plotting line luminosity as fucntion of time')

ax[0].plot(time, luminosity, color='crimson', linestyle='-', linewidth=2, marker='o')
ax[0].set_ylabel(r'$\rm Luminosity \, (erg \, s^{-1})$', fontsize=16)
ax[0].set_xlabel(r'$\rm time (kyr)$', fontsize=16)
ax[0].set_xlim(0.0, 35)
ax[0].tick_params(which='minor', direction='in', length=2)
ax[0].tick_params(which='major', direction='in', length=3)
ax[0].tick_params(axis='both', labelsize=20)
ax[0].set_yscale('log')
ax[0].legend(frameon=False)

ax[1].plot(time, temperature, color='blue', linestyle='-', linewidth=2)
ax[1].set_ylabel(r'$\rm T \, (K})$', fontsize=16)
ax[1].set_xlabel(r'$\rm time (kyr)$', fontsize=16)
#ax[1].set_xlim(0.0, 63)
ax[1].tick_params(which='minor', direction='in', length=2)
ax[1].tick_params(which='major', direction='in', length=3)
ax[1].tick_params(axis='both', labelsize=20)
ax[1].set_yscale('log')


ax[2].plot(time, ne, color='green', linestyle='-', linewidth=2)
ax[2].set_ylabel(r'$\rm n_e \, (cm^{-3})$', fontsize=16)
ax[2].set_xlabel(r'$\rm time (kyr)$', fontsize=16)
#ax[2].set_xlim(0.0, 63)
ax[2].tick_params(which='minor', direction='in', length=2)
ax[2].tick_params(which='major', direction='in', length=3)
ax[2].tick_params(axis='both', labelsize=20)
ax[2].set_yscale('log')

ax[3].plot(time, ns, color='gray', linestyle='-', linewidth=2)
ax[3].set_ylabel(r'$\rm n_s \, (cm^{-3})$', fontsize=16)
ax[3].set_xlabel(r'$\rm time (kyr)$', fontsize=16)
#ax[2].set_xlim(0.0, 63)
ax[3].tick_params(which='minor', direction='in', length=2)
ax[3].tick_params(which='major', direction='in', length=3)
ax[3].tick_params(axis='both', labelsize=20)
ax[3].set_yscale('log')

fig.tight_layout()
imagefile = output_dir + 'OIV_luminosity_analysis.png'
print("Saving image " + imagefile)
plt.savefig(imagefile)
plt.close()
'''


