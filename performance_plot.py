# Author: Arun Mathew
# Created: 10-11-2022
# Plotting Cooling functions with Asplund2002 and Eatson2022 Abundances

# Import required libraries: ##########################################
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
from matplotlib.lines import Line2D

# MAIN ##################################################################################
make_directory('MIM_Publication_1')

performance_test_file = '/home/tony/Desktop/MIM_Pub_Datafiles/Performance_Test/performance_test.txt'

plot_data = []

table_1 = ReadTable_Advance(performance_test_file)
# This original data already is normalised  with norm_factor
print("Table Size: ( row =", table_1['N_row'], ", columns = ", table_1['N_col'], ")")

tabledata_1 = table_1['columns']
# x-data, numner of tracers
NTracers = tabledata_1[0]
Walltime = tabledata_1[1]

normalized_walltime = Walltime/Walltime[0]

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(4, 3), sharex=False, sharey=False)
ax.plot(NTracers, normalized_walltime, label='', color='black', linestyle='-',
        marker='s', linewidth=0.7, markersize=4)

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis="both", direction="in", which="both",
               bottom=True, top=True, left=True, right=True, length=3)

ax.set_xlabel('Number of Tracers', fontsize=8)
ax.set_ylabel('', fontsize=8)
#ax.ticklabel_format(axis='y', style='sci', scilimits=(4,4))
left = 0.15  # the left side of the subplots of the figure
right = 0.95  # the right side of the subplots of the figure
bottom = 0.15  # the bottom of the subplots of the figure
top = 0.92  # the top of the subplots of the figure
wspace = 0.0  # the amount of width reserved for blank space between subplots
hspace = 0.0  # the amount of height reserved for white space between subplots
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)
plt.savefig('performance_test.png', dpi=300)



