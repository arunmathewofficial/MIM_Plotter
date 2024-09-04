from tools import *
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("compare_luminosity_file", type=str, help="line luminosity txt file")
parser.add_argument("output_dir", type=str, help="output dir path")
args = parser.parse_args()
output_dir = args.output_dir

output_dir = make_directory(output_dir)
compare_luminosity = args.compare_luminosity_file

line_luminosity_file = np.loadtxt(compare_luminosity, comments='#')
# Extract data from each column into separate arrays
Lambda = line_luminosity_file[0, :]
luminosity_OIII4960 = line_luminosity_file[1:, 1]
luminosity_OIII5008  = line_luminosity_file[1:, 2]
luminosity_OIV258933 = line_luminosity_file[1:, 3]
luminosity_OVI1032 = line_luminosity_file[1:, 4]
luminosity_OVI1038 = line_luminosity_file[1:, 4]

'''
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6), sharex=False, sharey=False)

print('Plotting line luminosity as fucntion of time')
ax.plot([Lambda[1], Lambda[1]], luminosity_OIII4960, label=r'[OIII] $\lambda$ 4960', linestyle='-', linewidth=2)
ax.plot([Lambda[2], Lambda[2]], luminosity_OIII5008, label=r'[OIII] $\lambda$ 5008', linestyle='-', linewidth=2)
#ax.plot([Lambda[3], Lambda[3]], luminosity_OIV258933, label=r'[OIV] $\lambda$ 258933', linestyle='-', linewidth=2)
ax.plot([Lambda[4], Lambda[4]], luminosity_OVI1032, label=r'[OVI] $\lambda$ 1032', linestyle='-', linewidth=2)
ax.plot([Lambda[5], Lambda[5]], luminosity_OVI1038, label=r'[OVI] $\lambda$ 1038', linestyle='-', linewidth=2)


ax.legend(frameon=False)
ax.set_ylabel(r'$\rm Luminosity \, \, (erg \, \,  s^{-1})$', fontsize=16)
ax.set_xlabel(r'$\rm time\,  (kyr)$', fontsize=16)
#ax.set_xlim(0.0, 63)
#ax.set_ylim(1.e+32, 1.e+36)
ax.tick_params(which='minor', direction='in', length=2)
ax.tick_params(which='major', direction='in', length=3)
ax.tick_params(axis='both', labelsize=20)
ax.set_yscale('log')

fig.tight_layout()
imagefile = output_dir + 'compare_luminosity.png'
print("Saving image " + imagefile)
plt.savefig(imagefile)
plt.close()
'''

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, gridspec_kw={'width_ratios': [1, 1, 1], 'wspace': 0.05})


ax1.plot(Lambda[4], luminosity_OVI1032[0], label=r'[OVI] $\lambda$ 1032', linestyle='None',
         marker='d', markersize=8, markerfacecolor='crimson', markeredgecolor='crimson')
ax1.plot(Lambda[4], luminosity_OVI1032[1], label=r'[OVI] $\lambda$ 1032', linestyle='None',
         marker='*', markersize=8, markerfacecolor='blue', markeredgecolor='blue')


ax1.plot(Lambda[5], luminosity_OVI1038[0], label=r'[OVI] $\lambda$ 1038', linestyle='None',
         marker='d', markersize=8, markerfacecolor='crimson', markeredgecolor='crimson')
ax1.plot(Lambda[5], luminosity_OVI1038[1], label=r'[OVI] $\lambda$ 1038', linestyle='None',
         marker='*', markersize=8, markerfacecolor='blue', markeredgecolor='blue')
ax1.set_xlim([1030, 1040])

ax1.set_ylabel('Luminosity (erg s$^{-1}$)', fontsize=16)
ax1.set_yscale('log')

# Plotting the first part of the data
ax2.plot(Lambda[1], luminosity_OIII4960[0], label=r'[OIII] $\lambda$ 4960',
         marker='d', markersize=8, markerfacecolor='crimson', markeredgecolor='crimson')
ax2.plot(Lambda[1], luminosity_OIII4960[1], label=r'[OIII] $\lambda$ 4960',
         marker='*', markersize=8, markerfacecolor='blue', markeredgecolor='blue')

ax2.plot(Lambda[2], luminosity_OIII5008[0], label=r'[OIII] $\lambda$ 5008',
         marker='d', markersize=8, markerfacecolor='crimson', markeredgecolor='crimson')
ax2.plot(Lambda[2], luminosity_OIII5008[1], label=r'[OIII] $\lambda$ 5008',
         marker='*', markersize=8, markerfacecolor='blue', markeredgecolor='blue')
ax2.set_yscale('log')
ax2.set_xlim([4940, 5020])

ax3.plot(Lambda[3], luminosity_OIV258933[0], label=r'[OIV] $\lambda$ 258933',
         marker='d', markersize=8, markerfacecolor='crimson', markeredgecolor='crimson')
ax3.plot(Lambda[3], luminosity_OIV258933[1], label=r'[OIV] $\lambda$ 258933',
         marker='*', markersize=8, markerfacecolor='blue', markeredgecolor='blue')
ax3.set_yscale('log')



# Adding labels and title
fig.text(0.5, 0.04, r'$\lambda$', ha='center', fontsize=18)


plt.subplots_adjust(left=0.2, right=0.98, top=0.98, bottom=0.15, hspace=0.0)

imagefile = output_dir + 'compare_luminosity.png'
print("Saving image " + imagefile)
plt.savefig(imagefile)
plt.close()
