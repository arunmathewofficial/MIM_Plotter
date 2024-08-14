# Author: Arun Mathew
# Created: 10-11-2022
# Plotting Performance_plots


from tools import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("performance_wt_ns_np10", type=str, help="Nspecies vs Walltime for Nthreads=10")
parser.add_argument("performance_wt_ns_np15", type=str, help="Nspecies vs Walltime for Nthreads=15")
parser.add_argument("performance_wt_np_ns99", type=str, help="Nthreads vs Walltime for Nspecies=99")
parser.add_argument("output_dir", type=str, help="give the output image dir path")
args = parser.parse_args()
output_dir = args.output_dir


output_dir = make_directory(output_dir)
wt_ns_np10 = args.performance_wt_ns_np10
wt_ns_np15 = args.performance_wt_ns_np15
wt_np_ns99 = args.performance_wt_np_ns99

# Species vs Walltime for Nthreads = 10 ##############################
wt_ns_np10 = np.loadtxt(wt_ns_np10, comments='#')
# Extract data from each column into separate arrays
wt_ns_np10_ntracers = wt_ns_np10[:, 0]
wt_ns_np10_walltime = wt_ns_np10[:, 3]
wt_ns_np10_nsteps = wt_ns_np10[:, 4]
wt_ns_np10_Ngrids = wt_ns_np10[:, 1]
wt_ns_np10_Nthreads = wt_ns_np10[:, 2]

# Species vs Walltime for Nthreads = 15 ##############################
wt_ns_np15 = np.loadtxt(wt_ns_np15, comments='#')
# Extract data from each column into separate arrays
wt_ns_np15_ntracers = wt_ns_np15[:, 0]
wt_ns_np15_walltime = wt_ns_np15[:, 3]
wt_ns_np15_nsteps = wt_ns_np15[:, 4]
wt_ns_np15_Ngrids = wt_ns_np15[:, 1]
wt_ns_np15_Nthreads = wt_ns_np15[:, 2]

# No of Species vs Walltime for Nthreads = 10, 15
fig, ax = plt.subplots(nrows=2, ncols=1, figsize=(6, 8), sharex=False, sharey=False)

print('Plotting NSpecies vs Walltime for Nthreads = 10, 15')
ax[0].plot(wt_ns_np10_ntracers, wt_ns_np10_walltime, label='No. of threads = 10', color='crimson', linestyle='-',
        marker='o', linewidth=2, markersize=10, markerfacecolor='crimson', markeredgecolor='none')
ax[0].plot(wt_ns_np15_ntracers, wt_ns_np15_walltime, label='No. of threads = 15', color='darkblue', linestyle='-',
        marker='o', linewidth=2, markersize=10, markerfacecolor='darkblue', markeredgecolor='none')
#ax[0].set_xlabel('N-Tracers')
ax[0].legend(frameon=False)
ax[0].set_ylabel(r'\rm walltime (s)', fontsize=16)
ax[0].set_xlabel(r'\rm $N_{\mathrm{tracer}}$', fontsize=16)
ax[0].tick_params(which='minor', direction='in', length=2)
ax[0].tick_params(which='major', direction='in', length=3)
ax[0].tick_params(axis='both', labelsize=20)
ax[0].xaxis.set_minor_locator(AutoMinorLocator())
ax[0].yaxis.set_minor_locator(AutoMinorLocator())


#ax[1].plot(ntracers, walltime, label='', color='black', linestyle='-',
#        marker='o', linewidth=0.7, markersize=10, markerfacecolor='red', markeredgecolor='none')

cell_update_speed_np10 = wt_ns_np10_Ngrids * wt_ns_np10_nsteps / ( wt_ns_np10_walltime * wt_ns_np10_Nthreads)
cell_update_speed_np15 = wt_ns_np15_Ngrids * wt_ns_np15_nsteps / ( wt_ns_np15_walltime * wt_ns_np15_Nthreads)

y2 = 1e5 / wt_ns_np15_ntracers
y3 = 3e6 / wt_ns_np15_ntracers**2
ax[1].plot(wt_ns_np15_ntracers, cell_update_speed_np10, label='No. of threads = 10', color='crimson', linestyle='-',
        marker='o', linewidth=2, markersize=10, markerfacecolor='crimson', markeredgecolor='none')
ax[1].plot(wt_ns_np15_ntracers, cell_update_speed_np15, label='No. of threads = 15', color='darkblue', linestyle='-',
        marker='o', linewidth=2, markersize=10, markerfacecolor='darkblue', markeredgecolor='none')
ax[1].plot(wt_ns_np15_ntracers, y2, label='$10^5/N_{\mathrm{tracer}}$')
ax[1].plot(wt_ns_np15_ntracers, y3, label='$3\\times10^6/N_{\mathrm{tracer}}^2$')
ax[1].set_xlabel(r'\rm $N_{\mathrm{tracer}}$', fontsize=16)
ax[1].set_ylabel(r'\rm cells / core / s', fontsize=16)
ax[1].legend(frameon=False)
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_ylim(3e2,1e5)
ax[1].tick_params(which='minor', direction='in', length=4)
ax[1].tick_params(which='major', direction='in', length=6)
ax[1].tick_params(axis='both', labelsize=20)
#ax[1].xaxis.set_minor_locator(AutoMinorLocator())
#ax[1].yaxis.set_minor_locator(AutoMinorLocator())

#fig.subplots_adjust(left=0.12, right=0.98, top=0.98, bottom=0.08)
fig.tight_layout()
imagefile = output_dir + 'performance_Wt_Ns.png'
print("Saving image "+ imagefile)
plt.savefig(imagefile)
plt.close()



# Nthreads vs Walltime for Nspecies set to 99 ##############################

wt_np_ns99 = np.loadtxt(wt_np_ns99, comments='#')
# Extract data from each column into separate arrays
wt_np_ns99_ntracers = wt_np_ns99[:, 2]
wt_np_ns99_walltime = wt_np_ns99[:, 3]
wt_np_ns99_nsteps = wt_np_ns99[:, 4]
wt_np_ns99_Ngrids = wt_np_ns99[:, 1]
wt_np_ns99_Nthreads = wt_np_ns99[:, 0]

y = 1e4 / wt_np_ns99_Nthreads
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(6, 4))

print('Plotting Nthreads vs Walltime for Nspecies set to 99')
ax.plot(wt_np_ns99_Nthreads, wt_np_ns99_walltime, label='', color='crimson', linestyle='-',
        marker='o', linewidth=2, markersize=10, markerfacecolor='k', markeredgecolor='none')
ax.plot(wt_np_ns99_Nthreads, y, label='', color='k', linestyle='--')
#ax[0].set_xlabel('N-Tracers')
ax.set_ylabel(r'\rm walltime (s)', fontsize=16)
ax.set_xlabel(r'\rm $N_\mathrm{thread}$', fontsize=16)
ax.tick_params(which='minor', direction='in', length=4)
ax.tick_params(which='major', direction='in', length=6)
ax.tick_params(axis='both', labelsize=20)
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.set_xscale('log')
ax.set_yscale('log')
#fig.subplots_adjust(left=0.1, right=0.98, top=0.98, bottom=0.13)
fig.tight_layout()
imagefile = output_dir + 'performance_Wt_Nth.png'
print("Saving image "+ imagefile)
plt.savefig(imagefile)
plt.close()
