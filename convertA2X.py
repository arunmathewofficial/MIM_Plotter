# Author: Arun Mathew
# Created: 15-06-2023
# Multi-ion-module-tools: This script converts the abundance of
# chemical species into the corresponding mass fractions and
# presents mass fractions from its database.

import numpy as np
import pandas as pd
import argparse
import warnings

# Create a dictionary of Abundances Name
abundance = {'Abundances':
            ['Raymond1978',
             'Asplund2009'
             ]}
mass = {
    "H": 1.6738E-24,
    "He": 6.6464768E-24,
    "C": 1.994374E-23,
    "N": 2.325892E-23,
    "O": 2.6567628E-23,
    "Ne": 3.3509177E-23,
    "Si": 4.6637066E-23,
    "S": 5.3245181E-23,
    "Fe": 9.2732796E-23}

# Create a DataFrame from the dictionary
abundances_df = pd.DataFrame(abundance)
# Convert DataFrame to string
abundance_string = abundances_df.to_string()
print('*** Convert Abundance into Mass-fraction ***')
print(abundance_string)
print('********************************************')
parser = argparse.ArgumentParser()
parser.add_argument('abundance', type=str,
                    help='Specify the abundance name')

args = parser.parse_args()
abundance_name = args.abundance
database_abundances = ['Raymond1978', 'Asplund2009']

if abundance_name not in database_abundances:
    print("\033[33mInvalid Abundances Name!\033[0m")



##################################################
def read_abundance_txt_file(file_path):
    data = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#'):
                continue
            # Assuming each line contains comma-separated values
            # Adjust this split method based on your data's actual delimiter
            line_data = line.strip().split()
            data.append(line_data)
    dict = {element[0]: [float(element[1]), float(element[2])] for element in data}
    return dict

##################################################
def calculate_massfraction(abundance_dict):
    dataframe = pd.DataFrame.from_dict(abundance_dict, orient='index', columns=['Abundaces', 'Error'])
    epsilon_X = []
    mass_value = []
    for key, value in abundance_dict.items():
        epsilon_X.append(sum(value) - 12)
        mass_value.append(mass[key])
    dataframe['mass'] = mass_value
    dataframe['epsilon_X'] = epsilon_X
    epsilon_X = np.array(epsilon_X)
    nfracH = 10.0 ** (epsilon_X)
    dataframe['nfrac/H'] = nfracH
    nfrac = nfracH / np.sum(nfracH)
    dataframe['nfrac'] = nfrac
    rhotot = np.sum(nfrac * mass_value)
    massfrac = nfrac * mass_value / rhotot
    total_massfrac = sum(massfrac)
    if total_massfrac != 1.0:
        print("The total mass fraction is not equal to 1.0, sum = {}".format(total_massfrac))
    massfrac_scientific = ['{:.5e}'.format(x) for x in massfrac]
    dataframe['X_E'] = massfrac_scientific
    return dataframe


##########################################################
if abundance_name == 'Raymond1978':
    print('Name: Raymond (1978) abundances')
    raymond_dict = read_abundance_txt_file('data/abundance_Raymond1978_ModelE.txt')
    raymond_dataframe = calculate_massfraction(raymond_dict)
    print(raymond_dataframe)


##########################################################
if abundance_name == 'Asplund2009':
    print('Name: Asplund (2009) proto-solar abundances')
    raymond_dict = read_abundance_txt_file('data/abundance_Asplund2009.txt')
    raymond_dataframe = calculate_massfraction(raymond_dict)
    print(raymond_dataframe)














'''
print("This script can be a part of pymicropion")
m_H = 1.6738e-24
m_He = 6.6464768e-24
m_C = 1.994374e-23
m_N = 2.325892e-23
m_O = 2.6567628e-23
m_Ne = 3.3509177e-23
m_Si = 4.6637066e-23
m_S = 5.3245181e-23
m_Fe = 9.2732796e-23

#########################################################
# given data
print("Given hydrogen number density and relative abundance, calculating mass fractions")
# number denisty of hydrogen
n_H = 100.0       #in units of 1/cm^3
# fraction of elements with respect to hydrogen
frac_He = 0.1
frac_C  = 2.2E-4
frac_N  = 4.0E-5
frac_O  = 3.3E-4
frac_Ne = 5.0E-5
frac_S  = 0.0 #9.0E-6

input = {'n_H': [n_H], 'a_He': [np.log10(frac_He)], 'a_C': [np.log10(frac_C)], 'a_N': [np.log10(frac_N)], 'a_O': [np.log10(frac_O)],
          'a_Ne': [np.log10(frac_Ne)], 'a_S': [np.log10(frac_S)]}
input_dataframe = pd.DataFrame(input, index=None)
input_dataframe.index = ["" for _ in range(len(input_dataframe))]  # Set empty string labels for the index
print(input_dataframe)

print("Hydrogen number density (in log): ", np.log10(n_H))
n_He = frac_He * n_H
n_C  = frac_C  * n_H
n_N  = frac_N  * n_H
n_O  = frac_O  * n_H
n_Ne = frac_Ne * n_H
n_S  = frac_S  * n_H

# calculating mass density
rho = m_H*n_H + m_He*n_He + m_C*n_C + m_N*n_N + m_O*n_O + m_Ne*n_Ne + m_S*n_S
print("Mass density (in g/cm^3): ", "{:.5e}".format(rho))

print("Calculated Mass-fraction: ")

def massfraction(species_number_density, species_mass, density):
    return species_number_density * species_mass / density

X_H = massfraction(n_H, m_H, rho)
X_He = massfraction(n_He, m_He, rho)
X_C = massfraction(n_C, m_C, rho)
X_N = massfraction(n_N, m_N, rho)
X_O = massfraction(n_O, m_O, rho)
X_Ne = massfraction(n_Ne, m_Ne, rho)
X_S = massfraction(n_S, m_S, rho)

print("mass-fraction H  :" + f"{X_H:.5E}")
print("mass-fraction He :" + f"{X_He:.5E}")
print("mass-fraction C  :" + f"{X_C:.5E}")
print("mass-fraction N  :" + f"{X_N:.5E}")
print("mass-fraction O  :" + f"{X_O:.5E}")
print("mass-fraction Ne :" + f"{X_Ne:.5E}")
print("mass-fraction S  :" + f"{X_S:.5E}")

Sum = X_H + X_He + X_C + X_N + X_O + X_Ne + X_S
print("Sum of Mass fraction:", Sum)

if Sum < 1.0:
    print("Scaling ...")
    X_H = X_H/Sum
    X_He = X_He / Sum
    X_C = X_C / Sum
    X_N = X_N / Sum
    X_O = X_O / Sum
    X_Ne = X_Ne / Sum
    X_S = X_S / Sum

    print("scaled mass-fraction H  :" + f"{X_H:.5E}")
    print("scaled mass-fraction He :" + f"{X_He:.5E}")
    print("scaled mass-fraction C  :" + f"{X_C:.5E}")
    print("scaled mass-fraction N  :" + f"{X_N:.5E}")
    print("scaled mass-fraction O  :" + f"{X_O:.5E}")
    print("scaled mass-fraction Ne :" + f"{X_Ne:.5E}")
    print("scaled mass-fraction S  :" + f"{X_S:.5E}")


if Sum > 1.0:
    print("Mass fraction exceed 1.0, X :", Sum)

'''



