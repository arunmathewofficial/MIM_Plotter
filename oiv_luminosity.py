# Author: Arun Mathew
# Created: 10-11-2022
# Plotting luminosity vs time

from tools import *
import numpy as np
import matplotlib.pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("luminosity_file", type=str, help="line luminosity txt file")
parser.add_argument("output_dir", type=str, help="output dir path")
args = parser.parse_args()
output_dir = args.output_dir

output_dir = make_directory(output_dir)
line_luminosity = args.luminosity_file


# Species vs Walltime for Nthreads = 10 ##############################
line_luminosity_file = np.loadtxt(line_luminosity, comments='#')
# Extract data from each column into separate arrays
time = line_luminosity_file[:, 0]
luminosity = line_luminosity_file[:, 1]


fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(8, 6), sharex=False, sharey=False)

print('Plotting line luminosity as fucntion of time')
ax.plot(time, luminosity, label='', color='crimson', linestyle='-', linewidth=2, marker='o')

ax.legend(frameon=False)
ax.set_ylabel(r'$\rm Luminosity \, (erg \, s^{-1})$', fontsize=16)
ax.set_xlabel(r'$\rm time (kyr)$', fontsize=16)
#ax.set_xlim(0.0, 63)
ax.tick_params(which='minor', direction='in', length=2)
ax.tick_params(which='major', direction='in', length=3)
ax.tick_params(axis='both', labelsize=20)
ax.set_yscale('log')


fig.tight_layout()
imagefile = output_dir + 'OIV_luminosity.png'
print("Saving image " + imagefile)
plt.savefig(imagefile)
plt.close()



