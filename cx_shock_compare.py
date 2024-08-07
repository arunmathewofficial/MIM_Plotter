# Author: Arun Mathew
# Created: 11-03-2023
# Multi-ion-module-publication: Generate a comparison plot for
# ionisation profile of Oxygen and Silicon behind the planar shock.

# Import required libraries: ##########################################
import warnings
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("charge_exchange_on", type=str, help="silo file with charge exchange turned on")
parser.add_argument("charge_exchange_off", type=str, help="silo file with charge exchange turned off")
parser.add_argument("output_dir", type=str, help="Output image dir path")

args = parser.parse_args()
output_dir = args.output_dir
output_dir = make_directory(output_dir)
charge_exchange_on_file = args.charge_exchange_on
charge_exchange_off_file = args.charge_exchange_off


# Plot ionisation profile of Oxygen behind the shock for the non-adiabatic flow.

# check for match in time
if not abs(get_basic_data(charge_exchange_on_file)['time'].value
           - get_basic_data(charge_exchange_off_file)['time'].value) <= 1.0E-02:
    warnings.warn(message='Time in two silo file do not match, exiting ...', stacklevel=2)
    exit(0)

SCALE = 1.0E15 #CM
# x data
x_cx_on = get_basic_data(charge_exchange_on_file)['x']/SCALE
x_cx_off = get_basic_data(charge_exchange_off_file)['x']/SCALE


fig, ax = plt.subplots(2, 1, figsize=(6, 8), gridspec_kw={'height_ratios': [1, 2]})

# plot 1 ===================================================
temperature_cx_on = get_temperature(charge_exchange_on_file)
temperature_cx_off = get_temperature(charge_exchange_off_file)
# shock detection
cutoff_index_cx_on = detect_shock(temperature_cx_on)
cutoff_index_cx_off = detect_shock(temperature_cx_off)
# striping data
x_cx_on = x_cx_on[:cutoff_index_cx_on]
temperature_cx_on = temperature_cx_on[:cutoff_index_cx_on]
x_cx_off = x_cx_off[:cutoff_index_cx_off]
temperature_cx_off = temperature_cx_off[:cutoff_index_cx_off]

# ploting temperature profile
print('Plotting temperature profile ...')
ax[0].plot(x_cx_on, temperature_cx_on, color='crimson', label=r'\rm Charge Exchange Enabled', linewidth=2.0, alpha=0.6)
ax[0].plot(x_cx_off, temperature_cx_off, color='darkblue', linestyle='--',
           label=r'\rm Charge Exchange Disabled', linewidth=2.0)
ax[0].set_xlim(0.0, 2.2)
ax[0].set_yscale('log')
ax[0].legend(fontsize=12, loc="lower right")
ax[0].set_ylabel(r"\rm T(K)", fontsize=16)
ax[0].set_xlabel(r"\rm x ($10^{15}$ cm)", fontsize=16)
ax[0].tick_params(axis="both", direction="in", which="both",
                        bottom=True, top=True, left=True, right=True,
                        length=3, width=1, labelsize=16)
ax[0].tick_params(axis='both', which='major', length=5)  # Major ticks
ax[0].tick_params(axis='both', which='minor', length=5)   # Minor ticks
ax[0].legend(fontsize=14, bbox_to_anchor=(0.4, 0.48),  frameon=False)

'''
# plot 2 ================================================================
X_H = get_tracer(charge_exchange_on_file, 'Tr000_X_H')[:cutoff_index_cx_on]
H0 = get_tracer(charge_exchange_on_file, 'Tr001_H')[:cutoff_index_cx_on]
H1p = X_H - H0
print('Plotting hydrogen ionisation profile ...')
ax[1].plot(temperature_cx_on, H0/X_H , color='red', label=r"$H$")
ax[1].plot(temperature_cx_on, H1p/X_H , color='blue', label=r"$H+$")
ax[1].set_xscale('log')
ax[1].set_yscale('log')
ax[1].set_xlim(4000, 5.0e4)
ax[1].set_ylim(1.0e-3, 1.5)

X_H = get_tracer(charge_exchange_off_file, 'Tr000_X_H')[:cutoff_index_cx_off]
H0 = get_tracer(charge_exchange_off_file, 'Tr001_H')[:cutoff_index_cx_off]
H1p = X_H - H0

ax[1].plot(temperature_cx_off, H0/X_H , color='black', linestyle='--')
ax[1].plot(temperature_cx_off, H1p/X_H , color='black', linestyle='--')
ax[1].set_xscale('log')
ax[1].invert_xaxis()
ax[1].legend(fontsize=12, loc="lower right")
ax[1].set_yscale('log')
ax[1].set_ylabel(r"Ionisation fraction", fontsize=16)
ax[1].set_xlabel(r"T (K)", fontsize=16)
'''

# Plot 2 OXYGEN ####################################################
# y data - oxygen species - charge exchange on
tracer_list = CX_OXYGEN_SHOCK_RAY79E
tracer_labels = [r"\Large$\rm O$", r"\Large$\rm O^{1+}$", r"\Large$\rm O^{2+}$", r"\Large$\rm O^{3+}$",
                 r"\Large$4+$", r"\Large$5+$", r"\Large$6+$"]

label_position = [(4.2e3, 0.8), (1.3e4, 0.8), (6e4, 0.7),
                  (1e5, 0.3), (2.546e16, 0.1), (0.1, 0.1), (0.3, 0.4),
                  (0.1, 0.4), (0.1, 0.3)]
line_color = ['darkblue', 'crimson', 'darkgreen', 'gray', 'purple', 'brown', 'blue', 'red', 'black', 'green']
tracer_data_list = get_tracers(charge_exchange_on_file, tracer_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
print('Plotting Oxygen ionisation profile ...')
for i in range(len(pro_tracer_data_list)-4):
    pro_tracer_data_list[i] = pro_tracer_data_list[i][:cutoff_index_cx_on]
    x_filtered = temperature_cx_on[pro_tracer_data_list[i] >= 0.0001]
    y_filtered = pro_tracer_data_list[i][pro_tracer_data_list[i] >= 0.0001]
    ax[1].plot(x_filtered, y_filtered, label=tracer_labels[i], color=line_color[i], linewidth=2.0, alpha=0.6)
    ax[1].text(label_position[i][0], label_position[i][1], tracer_labels[i], fontsize=8)
    del x_filtered, y_filtered

# y data - oxygen species - charge exchange off
tracer_list = CX_OXYGEN_SHOCK_RAY79E
tracer_labels = OXYGEN_SHOCK_LABELS
label_position = [[2.5625e16, 0.92], [2.559e16, 0.68], [2.555e16, 0.7], [2.546e16, 0.72],
                      [2.546e16, 0.1], [], [], [], []]
line_color = ['darkblue', 'crimson', 'darkgreen', 'gray', 'brown', 'blue', 'red', 'black', 'green']
line_style = ['--', '--', '--', '--', '--', '--', '--']
tracer_data_list = get_tracers(charge_exchange_off_file, tracer_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)

for i in range(len(pro_tracer_data_list)-4):
    pro_tracer_data_list[i] = pro_tracer_data_list[i][:cutoff_index_cx_off]
    x_filtered = temperature_cx_off[pro_tracer_data_list[i] >= 0.001]
    y_filtered = pro_tracer_data_list[i][pro_tracer_data_list[i] >= 0.001]
    ax[1].plot(x_filtered, y_filtered, label=tracer_labels[i], linestyle=line_style[i],
               color=line_color[i], linewidth=2.0)
    del x_filtered, y_filtered

ax[1].tick_params(labelsize=16)
ax[1].tick_params(axis="both", direction="in", which="both", bottom=True, top=True,
                  left=True, right=True, length=3, width=1, labelsize=16)
ax[1].set_ylabel(r"\rm Ionisation fraction", fontsize=16)
ax[1].set_xlabel(r"\rm T (K)", fontsize=16)
ax[1].set_xlim(3.5e+3, 1.5e+5)
ax[1].set_ylim(0.0, 1.0)
ax[1].set_xscale('log')
ax[1].tick_params(axis='both', which='major', length=5)  # Major ticks
ax[1].tick_params(axis='both', which='minor', length=5)   # Minor ticks

'''
# Plot 3  ####################################################
# y data - SILICON species - charge exchange on
tracer_list = CX_SILICON_SHOCK_RAY79E
tracer_labels = [r"\Large$0$", r"\Large$1+$", r"\Large$2+$", r"\Large$3+$",
                 r"\Large$4+$", r"\Large$5+$", r"\Large$6+$"]

label_position = [(7e3, 0.4), (1.3e4, 0.8), (5e4, 0.65),
                  (9e4, 0.35), (2.546e16, 0.1), (0.1, 0.1), (0.3, 0.4),
                  (0.1, 0.4), (0.1, 0.3)]
line_color = ['crimson', 'darkblue', 'darkgreen', 'purple', 'brown', 'blue', 'red', 'black', 'green']
tracer_data_list = get_tracers(charge_exchange_on_file, tracer_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)
print('Plotting Oxygen ionisation profile ...')
for i in range(len(pro_tracer_data_list)-10):
    pro_tracer_data_list[i] = pro_tracer_data_list[i][:cutoff_index_cx_on]
    ax[2].plot(temperature_cx_on, pro_tracer_data_list[i], label=tracer_labels[i], color=line_color[i])
    ax[2].text(label_position[i][0], label_position[i][1], tracer_labels[i], fontsize=8)

# y data - oxygen species - charge exchange off
tracer_list = CX_SILICON_SHOCK_RAY79E
tracer_labels = SILICON_SHOCK_LABELS
label_position = [[2.5625e16, 0.92], [2.559e16, 0.68], [2.555e16, 0.7], [2.546e16, 0.72],
                      [2.546e16, 0.1], [], [], [], []]
line_color = ['crimson', 'darkblue', 'darkgreen', 'purple', 'brown', 'blue', 'red', 'black', 'green']
line_style = ['--', '--', '--', '--', '--', '--', '--']
tracer_data_list = get_tracers(charge_exchange_off_file, tracer_list)
normalisation_factor = tracer_data_list[0]
pro_tracer_data_list = process_tracer_data(tracer_data_list, normalisation_factor)

for i in range(len(pro_tracer_data_list)-10):
    pro_tracer_data_list[i] = pro_tracer_data_list[i][:cutoff_index_cx_off]
    ax[2].plot(temperature_cx_off, pro_tracer_data_list[i], label=tracer_labels[i], linestyle=line_style[i], color=line_color[i])

ax[2].tick_params(labelsize=16)
ax[2].tick_params(axis="both", direction="in", which="both", bottom=True, top=True,
                  left=True, right=True, length=3, width=1, labelsize=16)
ax[2].set_ylabel(r"\rm Ionisation fraction", fontsize=16)
ax[2].set_xlabel(r"\rm T (K)", fontsize=16)
ax[2].set_xlim(3.5e+3, 1.5e+5)
ax[2].set_xscale('log')
ax[2].invert_xaxis()
'''
plt.subplots_adjust(left=0.12, bottom=0.1, right=0.95, top=0.95, wspace=0.1, hspace=0.2)
plt.savefig(output_dir + 'cx_sh_T&O.png')
plt.close()
