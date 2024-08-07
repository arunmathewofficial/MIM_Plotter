# Author: Arun Mathew
# Created:
# Multi-ion-module-test: Plot the comparison between the photoionization
# cross-section generated by PION and the original fit formula.


from cross_section_fit_equation import photo_xsection
import numpy as np
import matplotlib.pyplot as plt
from tools import *
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("pion_lookup_table_dir", type=str, help="The directory path to the lookup table data generated by PION")
parser.add_argument("output_dir", type=str, help="Output image dir path")

args = parser.parse_args()
output_dir = args.output_dir
output_dir = make_directory(output_dir)
pion_lookuptab_dir = args.pion_lookup_table_dir
if not pion_lookuptab_dir.endswith('/'):
    pion_lookuptab_dir+= "/"
pion_mean_photo_xsection_file = pion_lookuptab_dir + 'photo-tables/mean-photo-xsection.txt'
pion_bin_weight_file = pion_lookuptab_dir + 'photo-tables/bin-weights.txt'

# read the xsection data and return label, species name and data dictionary
pion_xsection_data = read_xsection_data(pion_mean_photo_xsection_file)
species = np.array(pion_xsection_data['species'])
# read the weight data and return label, species name and data dictionary
pion_weight_data = read_xsection_data(pion_mean_photo_xsection_file)

# Customize the formatting options
np.set_printoptions(threshold=np.inf)
formatted_species_list = np.array2string(species, separator=', ', max_line_width=90)
# Display the formatted string array
print("Found the following species: \n", formatted_species_list)
# obtain minimum and maximum energy from the pion photo-ionisation bin
min_energy = pion_xsection_data["dict"]["Bin_Min"][0]
max_energy = pion_xsection_data["dict"]["Bin_Max"][-1]
# make energy array of 100 points within this limits
energy_array = np.linspace(min_energy, max_energy, 100)
# make histogram energy bins
energy_bins = []
for i in range(len(pion_xsection_data["dict"]["Bin_Min"])):
    bin = []
    bin.append(pion_xsection_data["dict"]["Bin_Min"][i])
    bin.append(pion_xsection_data["dict"]["Bin_Max"][i])
    energy_bins.append(bin)
    del bin

# Calculate bin centers from edge values
bin_centers = [(edge[0] + edge[1]) / 2 for edge in energy_bins]
# Calculate bar widths
bar_widths = [edge[1] - edge[0] for edge in energy_bins]

print('Plotting photo-cross-sections...')
for species in pion_xsection_data["species"]:

    #calculating species cross-section from fit formula
    species_xsection_array = photo_xsection.get_species_xsection(species, energy_array)
    # multiplying thw weight

    species_xsection_bin = [pion_xsection_data["dict"][species][i] * pion_weight_data['dict'][species][i]
              for i in range(len(pion_xsection_data["dict"][species]))]
    species_xsection_bin = pion_xsection_data["dict"][species]
    species_xsection_bin_Mb = [x * 1.0E+18 for x in species_xsection_bin]
    nbins = len(species_xsection_bin_Mb)
    y_min = min(species_xsection_array)
    y_max = max(species_xsection_array)

    # Create a figure with subplots
    fig, ax1 = plt.subplots()

    # Plot the curve
    ax1.plot(energy_array, species_xsection_array, label="Verner-fit", color='black',
             linestyle='-', linewidth=2)
    ax1.set_xlabel("Energy, eV")
    ax1.set_ylabel("Verner Cross section, Mb")
    ax1.set_title('Cross-section for ' + species)
    ax1.xaxis.set_minor_locator(AutoMinorLocator())
    ax1.yaxis.set_minor_locator(AutoMinorLocator())
    ax1.tick_params(axis="both", direction="in", which="both", bottom=True, top=True,
                   left=True, right=True, length=3)
    ax1.legend(loc='upper left')
    ax1.set_ylim(y_min, y_max)

    # Creating a twin axis sharing the x-axis
    ax2 = ax1.twinx()

    # Plot the bar
    ax2.bar(bin_centers, species_xsection_bin_Mb, width=bar_widths, align='center', color='orange',
            alpha=0.5, label="MPv10-PION")

    ax2.set_xlabel("Energy, eV")
    ax2.set_ylabel("MPV10 Cross section, Mb")
    ax2.xaxis.set_minor_locator(AutoMinorLocator())
    ax2.yaxis.set_minor_locator(AutoMinorLocator())
    ax2.legend(loc='upper right')
    #ax2.set_ylim(y_min, y_max)
    ax2.set_ylim(ax1.get_ylim())


    plt.tight_layout()  # To prevent overlapping of subplots
    # Show the combined plot
    image =  output_dir + "xsection_" + species + ".png"
    print("saving " + image)
    plt.savefig(image, dpi=200)
    plt.close(fig)

