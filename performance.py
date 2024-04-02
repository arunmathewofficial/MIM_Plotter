# Author: Arun Mathew
# Created: 10-11-2022
# Plotting Performance_plots

# Import required libraries: ##########################################
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
from matplotlib.lines import Line2D
from matplotlib.ticker import AutoMinorLocator
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("performance_datafile", type=str, help="The text file contains data for performance testing")
parser.add_argument("output_dir", type=str, help="give the output image dir path")
args = parser.parse_args()
output_dir = args.output_dir

################################################################
output_dir = make_directory(output_dir)
datafile = args.performance_datafile
# Load the text file, ignoring lines starting with #
data = np.loadtxt(datafile, comments='#')
# Extract data from each column into separate arrays
ntracers = data[:, 0]
walltime = data[:, 1]
nsteps = data[:, 2]
Ngrids = data[:, 3]
Nthreads = data[:, 4]

# Calculating Cell-Update Speed



fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(8, 12), sharex=False, sharey=False)

print('Plotting performance ...')
ax[0].plot(ntracers, walltime, label='', color='black', linestyle='-',
        marker='o', linewidth=0.7, markersize=10, markerfacecolor='red', markeredgecolor='none')
ax[0].set_xlabel('N-Tracers')
ax[0].set_ylabel('Walltime')
ax[0].xaxis.set_minor_locator(AutoMinorLocator())
ax[0].yaxis.set_minor_locator(AutoMinorLocator())


ax[1].plot(ntracers, walltime, label='', color='black', linestyle='-',
        marker='o', linewidth=0.7, markersize=10, markerfacecolor='red', markeredgecolor='none')
ax[1].set_xlabel('N-Tracers')
ax[1].set_ylabel('cell-update speed')
ax[1].xaxis.set_minor_locator(AutoMinorLocator())
ax[1].yaxis.set_minor_locator(AutoMinorLocator())


imagefile = output_dir + 'performance.png'
print("Saving image "+ imagefile)
plt.savefig(imagefile, dpi=200)


'''
plot_data = []

# This original data already is normalised  with norm_factor
print("Table Size: ( row =", table_1['N_row'], ", columns = ", table_1['N_col'], ")")


print(table_1)

tabledata_1 = table_1['columns']
# x-data, numner of tracers
NTracers = tabledata_1[0]
Walltime = tabledata_1[1]

normalized_walltime = Walltime/Walltime[0]

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(4, 3), sharex=False, sharey=False)
ax.plot(NTracers, normalized_walltime, label='', color='red', linestyle='-',
        marker='o', linewidth=0.7, markersize=4, markerfacecolor='black', markeredgecolor='none')

#ax.xaxis.set_minor_locator(AutoMinorLocator())
#ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis="both", direction="in", which="both",
               bottom=True, top=True, left=True, right=True, length=2)
# Add minor ticks to both x and y axes
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())

ax.set_xlabel(r'\rm No of species', fontsize=8)
ax.set_ylabel(r'\rm Normalized walltime', fontsize=8)
#ax.ticklabel_format(axis='y', style='sci', scilimits=(4,4))
left = 0.15  # the left side of the subplots of the figure
right = 0.95  # the right side of the subplots of the figure
bottom = 0.15  # the bottom of the subplots of the figure
top = 0.92  # the top of the subplots of the figure
wspace = 0.0  # the amount of width reserved for blank space between subplots
hspace = 0.0  # the amount of height reserved for white space between subplots
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)


# Save the plot
plt.savefig(plot_dir + 'performance_test_1.png', dpi=200)

'''

