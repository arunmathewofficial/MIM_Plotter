# Author: Arun Mathew
# Created:
# Multi-ion-module-test: Plot the charge exchange reaction rate as a
# function of temperature for all reactions in the pion lookup table.
# This data is generated by pion from the original fit formula in
# debug mode in the MPv10.cpp file.



import numpy as np
import matplotlib.pyplot as plt
from tools import *
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import argparse
from collections import namedtuple
from math import pow, exp
from typing import Dict, Tuple

eV2erg = 1.60218E-12
kB = 1.380649E-16

parser = argparse.ArgumentParser()
parser.add_argument("pion_debug_lookup_table_dir", type=str,
                    help="The directory path to the lookup table data generated by PION")
parser.add_argument("output_dir", type=str, help="Output image dir path")

args = parser.parse_args()
output_dir = args.output_dir
output_dir = make_directory(output_dir)
pion_lookuptab_dir = args.pion_debug_lookup_table_dir
if not pion_lookuptab_dir.endswith('/'):
    pion_lookuptab_dir+= "/"
cx_ionise_reaction_rate_file = pion_lookuptab_dir + 'charge-exchange-tables/cx-ionise-reactions.txt'
cx_recomb_reaction_rate_file = pion_lookuptab_dir + 'charge-exchange-tables/cx-recomb-reactions.txt'

# set xmin and xmax limits
xmin_limit = 1.0E+1
xmax_limit = 5.0E+5

#Section: Reading database to plot the actual data ***************************
# AR parameter are located in the file: data/charge_exchange_rates.dat
# Define a namedtuple for AR_parameters
AR_parameters = namedtuple(
    'AR_parameters', ['reaction_id','type', 'a', 'b',
                      'c', 'd', 'T_min', 'T_max', 'dE'])
# Initialize the AR_reaction dictionary
AR_reaction: Dict[Tuple[str, str], AR_parameters] = {}

# open database file
with open('data/charge_exchange_rates.dat', 'r') as file:
    for line in file:
        elements = line.split()
        key = (elements[0], elements[1])
        params = AR_parameters(elements[2], int(elements[3]), float(elements[4]), float(elements[5]),
                               float(elements[6]), float(elements[7]), float(elements[8]), float(elements[9]),
                               float(elements[10]))
        AR_reaction[key] = params

# calculating the reaction rate
def get_cx_rate(reaction_key: Tuple[str, str], T: float) -> Tuple[float, bool]:
    reaction = AR_reaction.get(reaction_key)
    if reaction is None:
        return 0.0, False

    # recombination reaction with H and He
    if not reaction.type:
        rate = reaction.a * pow(T * 1.00E-04, reaction.b)\
               * (1.00 + reaction.c * exp(reaction.d * T * 1.00E-04))
        constant = reaction.b == 0.0 and reaction.c == 0.0
        return rate, constant

    # ionisation reaction with H+
    if reaction_key[1] == "H1+" and reaction.type:
        rate = reaction.a * pow(T * 1.00E-04, reaction.b)\
               * (1.00 + reaction.c * exp(reaction.d * T * 1.00E-04))\
               * exp(-abs(reaction.dE) * eV2erg / (kB*T))

        constant = reaction.b == 0.0 and reaction.c == 0.0 and reaction.dE
        return rate, constant

    # ionisation reaction with He+
    if reaction_key[1] == "He1+" and reaction.type:
        rate = reaction.a * pow(T * 1.00E-04, reaction.b) \
               * exp(-reaction.c * T * 1.00E-04) \
               * exp(-abs(reaction.dE) * eV2erg / (kB * T))

        constant = reaction.b == 0.0 and reaction.c == 0.0 and reaction.dE
        return rate, constant


#get the reaction keys from the reaction ID
def get_reaction_keys(reaction_ID: str) -> Tuple[str, str]:
    for key, value in AR_reaction.items():
        if value.reaction_id == reaction_ID:
            return key
    return None, None
#End of Section **************************************************************



# Generate array of temperature values between xmin_limit and xmax_limit with
# logarithmic spacing
T_fit = np.logspace(np.log10(xmin_limit), np.log10(xmax_limit), 25)


# Section: Potting ************************************************************
# 1. plotting ionisation reaction rates from LUT table and from actual fit formula
print("----- plotting cx-ionisation reaction rates -----")
ReadData = Read_CX_Table(cx_ionise_reaction_rate_file)

N_Reactions = ReadData['N_Reactions']
Reaction_IDs = ReadData['Reaction_IDs']
Energy_Defect = ReadData['Energy_Defect']
Temperature = ReadData['Temperature']
Rate_Table = ReadData['Rate_Table']


# Generate rate tables from the fit formula
Rate_Table_fit = []
for i, id in enumerate(Reaction_IDs):
    key = get_reaction_keys(id)
    Rate_Table_fit.append([])
    for T in T_fit:
        Rate_Table_fit[i].append(get_cx_rate(key, T)[0])


for i, data in enumerate(Rate_Table):
    fig, ax = plt.subplots(figsize=(8, 6))
    # Convert data to a numpy array if it's not already
    data = np.array(data, dtype=float)
    temperature = np.array(Temperature, dtype=float)
    # Plot the data
    ax.plot(temperature, data, label='LUT Mpv10 PIONv3.0')
    ax.plot(T_fit, Rate_Table_fit[i], marker='o', linestyle='None', label='Fit Formula')
    ax.text(0.1, 0.9, 'Ionisation Reaction: ' + Reaction_IDs[i], transform=ax.transAxes, fontsize=10, color='black')
    ax.text(0.1, 0.8, r'$\Delta E = $' + Energy_Defect[i] + ' eV', transform=ax.transAxes, fontsize=10, color='black')
    ax.set_xlabel('T (K)')
    ax.set_ylabel(r'CX Reaction rate (cm$^3$/s)')
    ax.set_xscale('log')
    # setting x limits
    ax.set_xlim([xmin_limit, xmax_limit])
    # setting y-limits in the plot
    ax.set_ylim([Rate_Table_fit[i][0], Rate_Table_fit[i][-1]])
    ax.legend(loc='upper right')

    # saving images
    plt.tight_layout()
    image_name = output_dir + 'ionise_' + Reaction_IDs[i] + '.png'
    print("Saving " + image_name)
    fig.savefig(image_name)
    plt.close(fig)

# Clear the dictionary
ReadData.clear()
# Clear the fir data array
Rate_Table_fit.clear()


# plotting recombination reaction rates from LUT table and from actual fit formula
print("----- plotting cx-recombination reaction rates -----")
ReadData = Read_CX_Table(cx_recomb_reaction_rate_file)

N_Reactions = ReadData['N_Reactions']
Reaction_IDs = ReadData['Reaction_IDs']
Energy_Defect = ReadData['Energy_Defect']
Temperature = ReadData['Temperature']
Rate_Table = ReadData['Rate_Table']

# Generate rate tables from the fit formula
Rate_Table_fit = []
for i, id in enumerate(Reaction_IDs):
    key = get_reaction_keys(id)
    Rate_Table_fit.append([])
    for T in T_fit:
        Rate_Table_fit[i].append(get_cx_rate(key, T)[0])

for i, data in enumerate(Rate_Table):
    fig, ax = plt.subplots(figsize=(8, 6))
    temperature = np.array(Temperature, dtype=float)
    data = np.array(data, dtype=float)
    ax.plot(temperature, data, label='LUT Mpv10 PIONv3.0')
    ax.plot(T_fit, Rate_Table_fit[i], marker='o', linestyle='None', label='Fit Formula')
    ax.text(0.1, 0.9, 'CX Recombination Reaction: ' + Reaction_IDs[i], transform=ax.transAxes, fontsize=10, color='black')
    ax.text(0.1, 0.8, r'$\Delta E = $' + Energy_Defect[i] + ' eV', transform=ax.transAxes, fontsize=10, color='black')
    ax.set_xlabel('T (K)')
    ax.set_ylabel(r'Reaction rate (cm$^3$/s)')
    ax.set_xscale('log')
    ax.set_xlim([xmin_limit, xmax_limit])
    # setting y-limits in the plot
    ax.set_ylim([Rate_Table_fit[i][0], Rate_Table_fit[i][-1]])
    ax.legend(loc='upper right')

    #saving images
    plt.tight_layout()
    image_name = output_dir + 'recomb_' + Reaction_IDs[i] + '.png'
    print("Saving " + image_name)
    fig.savefig(image_name)
    plt.close(fig)

# Clear the dictionary
ReadData.clear()
# Clear the fir data array
Rate_Table_fit.clear()
