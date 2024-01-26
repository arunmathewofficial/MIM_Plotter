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

import pandas as pd
from matplotlib.ticker import MaxNLocator
from SiloReader import GetSiloData
import numpy as np
from matplotlib import colors as mcolors

parsec = 3.086e+18

# MAIN ##################################################################################
plot_dir =make_directory('MIM2023_Images')

cloudyfile_T = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_BB/HII_region.ovr'
cloudyfile_H = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_BB/HII_region.ele_H'
cloudyfile_He = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_BB/HII_region.ele_He'
cloudyfile_C = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_BB/HII_region.ele_C'
cloudyfile_N = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_BB/HII_region.ele_N'
cloudyfile_O = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_BB/HII_region.ele_O'
cloudyfile_Ne = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_BB/HII_region.ele_Ne'
cloudyfile_S = '/home/mathew/Desktop/pion/photoionisation_test/cloudy_Haworth_BB/HII_region.ele_S'

pionfile_haworth = '/home/mathew/Desktop/pion/refactor-test/silo/mpv10_HIIregion_0000.00002487.silo'

torus_haworth = '/home/mathew/Desktop/pion/photoionisation_test/From_Tom/photoionradial.dat'


# common variables #################################################################
table_T = ReadTable_Advance(cloudyfile_T)
print("Table Size: ( row =", table_T['N_row'], ", columns = ", table_T['N_col'], ")")
dataset_T = table_T['columns']
cloudy_radius = (np.array(dataset_T[0]) + 3.e18) / parsec

object = GetSiloData([pionfile_haworth])
pion_radius = object.get_radial_coordinate() / parsec

torus_data = np.loadtxt(torus_haworth)
torus_radius = torus_data[:,0] / 3.08e8

# Temperature profile ##############################################################
print("Plotting temperature profile:")
print("Reading silo file:", pionfile_haworth)
pion_temp = object.get_parameter('Temperature')
cloudy_temp = dataset_T[1]
torus_temp = torus_data[:,2]
fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(cloudy_radius, cloudy_temp, label='Cloudy', linestyle='--', color='red')
ax.plot(pion_radius, pion_temp, label='PION', linestyle='-.', color='blue')
ax.plot(torus_radius, torus_temp, label='Torus', linestyle=':', color='black')
ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.tick_params(axis="both", direction="in", which="both",
               bottom=True, top=True, left=True, right=True, length=2, labelsize=10)

ax.set_xlim([1.0, 6])
#ax.set_ylim([0.0, 12000])
ax.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=10)
ax.set_ylabel(r"$\rm T \, (K)$", fontsize=10)

ax.legend(frameon=False, loc='upper right', fontsize='8')
image_file = plot_dir + 'HII_temperature.png'
print("Saving image to", image_file)
plt.savefig(image_file, dpi=300)


# Hydrogen and Helium profile ##############################################################
print("Plotting Hydrogen and Helium profile:")
table_H = ReadTable_Advance(cloudyfile_H)
print("Table Size: ( row =", table_H['N_row'], ", columns = ", table_H['N_col'], ")")
dataset_H = table_H['columns']
table_He = ReadTable_Advance(cloudyfile_He)
print("Table Size: ( row =", table_He['N_row'], ", columns = ", table_He['N_col'], ")")
dataset_He = table_He['columns']

print("Reading silo file:", pionfile_haworth)
H = object.get_parameter('Tr007_H1p')  / object.get_parameter('Tr000_X_H')
H0 = np.ones_like(H1p) - H1p

He2p = object.get_parameter('Tr009_He2p') / object.get_parameter('Tr001_X_He')
He1p = object.get_parameter('Tr008_He1p') / object.get_parameter('Tr001_X_He')
He0 = np.ones_like(He2p) - He2p - He1p

fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(6, 14))
ax1.plot(cloudy_radius, dataset_H[1], label=r'$\rm Cloudy - H$', linestyle=':', color='C0')
ax1.plot(cloudy_radius, dataset_H[2], label=r'$\rm Cloudy - H^{1+}$', linestyle=':', color='C1')
ax1.plot(cloudy_radius, dataset_He[1], label=r'$\rm Cloudy - He$', linestyle=':', color='C2')
ax1.plot(cloudy_radius, dataset_He[2], label=r'$\rm Cloudy - He^{1+}$', linestyle=':', color='C3')
ax1.plot(cloudy_radius, dataset_He[3], label=r'$\rm Cloudy - He^{2+}$', linestyle=':', color='C4')

ax1.plot(pion_radius, H0, label=r'$\rm PION - H$', linestyle='-', color='C0')
ax1.plot(pion_radius, H1p, label=r'$\rm PION - H^{1+}$', linestyle='-', color='C1')
ax1.plot(pion_radius, He0, label=r'$\rm PION - He$', linestyle='-', color='C2')
ax1.plot(pion_radius, He1p, label=r'$\rm PION - He^{1+}$', linestyle='-', color='C3')
ax1.plot(pion_radius, He2p, label=r'$\rm PION - He^{2+}$', linestyle='-', color='C4')

ax1.xaxis.set_minor_locator(AutoMinorLocator())
ax1.yaxis.set_minor_locator(AutoMinorLocator())
ax1.tick_params(axis="both", direction="in", which="both",
               bottom=True, top=True, left=True, right=True, length=2, labelsize=8)

ax1.set_xlim([0.0, 6])
ax1.grid()
#ax.set_ylim([-25.5, -19.5])
ax1.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=8)
ax1.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=8)
ax1.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.23), ncol=5, fontsize=8)


# Carbom profile ##############################################################

print("Plotting Carbon profile:")
table_C = ReadTable_Advance(cloudyfile_C)
print("Table Size: ( row =", table_C['N_row'], ", columns = ", table_C['N_col'], ")")
dataset_C = table_C['columns']

print("Reading silo file:", pionfile_haworth)
C1p = object.get_parameter('Tr010_C1p') / object.get_parameter('Tr002_X_C')
C2p = object.get_parameter('Tr011_C2p') / object.get_parameter('Tr002_X_C')
C3p = object.get_parameter('Tr012_C3p') / object.get_parameter('Tr002_X_C')
C4p = object.get_parameter('Tr013_C4p') / object.get_parameter('Tr002_X_C')
C5p = object.get_parameter('Tr014_C5p') / object.get_parameter('Tr002_X_C')
C6p = object.get_parameter('Tr015_C6p') / object.get_parameter('Tr002_X_C')
C0 = np.ones_like(C1p) - C1p - C2p - C3p - C4p - C5p - C6p

ax2.plot(cloudy_radius, dataset_C[1], label=r'$\rm Cloudy - C$', linestyle=':', color='C0')
ax2.plot(cloudy_radius, dataset_C[2], label=r'$\rm Cloudy - C^{1+}$', linestyle=':', color='C1')
ax2.plot(cloudy_radius, dataset_C[3], label=r'$\rm Cloudy - C^{2+}$', linestyle=':', color='C2')
ax2.plot(cloudy_radius, dataset_C[4], label=r'$\rm Cloudy - C^{3+}$', linestyle=':', color='C3')
ax2.plot(cloudy_radius, dataset_C[5], label=r'$\rm Cloudy - C^{4+}$', linestyle=':', color='C4')
ax2.plot(cloudy_radius, dataset_C[6], label=r'$\rm Cloudy - C^{5+}$', linestyle=':', color='C5')
ax2.plot(cloudy_radius, dataset_C[7], label=r'$\rm Cloudy - C^{6+}$', linestyle=':', color='C6')

ax2.plot(pion_radius, C0, label=r'$\rm PION - C$', linestyle='-', color='C0')
ax2.plot(pion_radius, C1p, label=r'$\rm PION - C^{1+}$', linestyle='-', color='C1')
ax2.plot(pion_radius, C2p, label=r'$\rm PION - C^{2+}$', linestyle='-', color='C2')
ax2.plot(pion_radius, C3p, label=r'$\rm PION - C^{3+}$', linestyle='-', color='C3')
ax2.plot(pion_radius, C4p, label=r'$\rm PION - C^{4+}$', linestyle='-', color='C4')
ax2.plot(pion_radius, C5p, label=r'$\rm PION - C^{5+}$', linestyle='-', color='C5')
ax2.plot(pion_radius, C6p, label=r'$\rm PION - C^{6+}$', linestyle='-', color='C6')

ax2.xaxis.set_minor_locator(AutoMinorLocator())
ax2.yaxis.set_minor_locator(AutoMinorLocator())
ax2.tick_params(axis="both", direction="in", which="both",
               bottom=True, top=True, left=True, right=True, length=2, labelsize=8)

ax2.set_xlim([0.0, 6])
ax2.grid()
#ax.set_ylim([-25.5, -19.5])
ax2.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=8)
ax2.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=8)
ax2.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.23), ncol=5, fontsize=8)


# Nitrogen profile ##############################################################
print("Plotting Nitrogen profile:")
table_N = ReadTable_Advance(cloudyfile_N)
print("Table Size: ( row =", table_N['N_row'], ", columns = ", table_N['N_col'], ")")
dataset_N = table_N['columns']

print("Reading silo file:", pionfile_haworth)
N1p = object.get_parameter('Tr016_N1p') / object.get_parameter('Tr003_X_N')
N2p = object.get_parameter('Tr017_N2p') / object.get_parameter('Tr003_X_N')
N3p = object.get_parameter('Tr018_N3p') / object.get_parameter('Tr003_X_N')
N4p = object.get_parameter('Tr019_N4p') / object.get_parameter('Tr003_X_N')
N5p = object.get_parameter('Tr020_N5p') / object.get_parameter('Tr003_X_N')
N6p = object.get_parameter('Tr021_N6p') / object.get_parameter('Tr003_X_N')
N7p = object.get_parameter('Tr022_N7p') / object.get_parameter('Tr003_X_N')
N0 = np.ones_like(N1p) - N1p - N2p - N3p - N4p - N5p - N6p - N7p

ax3.plot(cloudy_radius, dataset_N[1], label=r'$\rm Cloudy - N$', linestyle=':', color='C0')
ax3.plot(cloudy_radius, dataset_N[2], label=r'$\rm Cloudy - N^{1+}$', linestyle=':', color='C1')
ax3.plot(cloudy_radius, dataset_N[3], label=r'$\rm Cloudy - N^{2+}$', linestyle=':', color='C2')
ax3.plot(cloudy_radius, dataset_N[4], label=r'$\rm Cloudy - N^{3+}$', linestyle=':', color='C3')
ax3.plot(cloudy_radius, dataset_N[5], label=r'$\rm Cloudy - N^{4+}$', linestyle=':', color='C4')
ax3.plot(cloudy_radius, dataset_N[6], label=r'$\rm Cloudy - N^{5+}$', linestyle=':', color='C5')
ax3.plot(cloudy_radius, dataset_N[7], label=r'$\rm Cloudy - N^{6+}$', linestyle=':', color='C6')
ax3.plot(cloudy_radius, dataset_N[8], label=r'$\rm Cloudy - N^{7+}$', linestyle=':', color='C7')


ax3.plot(pion_radius, N0, label=r'$\rm PION - N$', linestyle='-', color='C0')
ax3.plot(pion_radius, N1p, label=r'$\rm PION - N^{1+}$', linestyle='-', color='C1')
ax3.plot(pion_radius, N2p, label=r'$\rm PION - N^{2+}$', linestyle='-', color='C2')
ax3.plot(pion_radius, N3p, label=r'$\rm PION - N^{3+}$', linestyle='-', color='C3')
ax3.plot(pion_radius, N4p, label=r'$\rm PION - N^{4+}$', linestyle='-', color='C4')
ax3.plot(pion_radius, N5p, label=r'$\rm PION - N^{5+}$', linestyle='-', color='C5')
ax3.plot(pion_radius, N6p, label=r'$\rm PION - N^{6+}$', linestyle='-', color='C6')
ax3.plot(pion_radius, N7p, label=r'$\rm PION - N^{7+}$', linestyle='-', color='C7')


ax3.xaxis.set_minor_locator(AutoMinorLocator())
ax3.yaxis.set_minor_locator(AutoMinorLocator())
ax3.tick_params(axis="both", direction="in", which="both",
               bottom=True, top=True, left=True, right=True, length=2, labelsize=8)

ax3.set_xlim([0.0, 6])
ax3.grid()
#ax.set_ylim([-25.5, -19.5])
ax3.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=8)
ax3.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=8)
ax3.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.23), ncol=5, fontsize=8)


# Oxygen profile ##############################################################
print("Plotting Oxygen profile:")
table_O = ReadTable_Advance(cloudyfile_O)
print("Table Size: ( row =", table_O['N_row'], ", columns = ", table_O['N_col'], ")")
dataset_O = table_O['columns']

print("Reading silo file:", pionfile_haworth)
O1p = object.get_parameter('Tr023_O1p') / object.get_parameter('Tr004_X_O')
O2p = object.get_parameter('Tr024_O2p') / object.get_parameter('Tr004_X_O')
O3p = object.get_parameter('Tr025_O3p') / object.get_parameter('Tr004_X_O')
O4p = object.get_parameter('Tr026_O4p') / object.get_parameter('Tr004_X_O')
O5p = object.get_parameter('Tr027_O5p') / object.get_parameter('Tr004_X_O')
O6p = object.get_parameter('Tr028_O6p') / object.get_parameter('Tr004_X_O')
O7p = object.get_parameter('Tr029_O7p') / object.get_parameter('Tr004_X_O')
O8p = object.get_parameter('Tr030_O8p') / object.get_parameter('Tr004_X_O')

O0 = np.ones_like(O1p) - O1p - O2p - O3p - O4p - O5p - O6p - O7p - O8p

ax4.plot(cloudy_radius, dataset_O[1], label=r'$\rm Cloudy - O$', linestyle=':', color='C0')
ax4.plot(cloudy_radius, dataset_O[2], label=r'$\rm Cloudy - O^{1+}$', linestyle=':', color='C1')
ax4.plot(cloudy_radius, dataset_O[3], label=r'$\rm Cloudy - O^{2+}$', linestyle=':', color='C2')
ax4.plot(cloudy_radius, dataset_O[4], label=r'$\rm Cloudy - O^{3+}$', linestyle=':', color='C3')
ax4.plot(cloudy_radius, dataset_O[5], label=r'$\rm Cloudy - O^{4+}$', linestyle=':', color='C4')
ax4.plot(cloudy_radius, dataset_O[6], label=r'$\rm Cloudy - O^{5+}$', linestyle=':', color='C5')
ax4.plot(cloudy_radius, dataset_O[7], label=r'$\rm Cloudy - O^{6+}$', linestyle=':', color='C6')
ax4.plot(cloudy_radius, dataset_O[8], label=r'$\rm Cloudy - O^{7+}$', linestyle=':', color='C7')
ax4.plot(cloudy_radius, dataset_O[9], label=r'$\rm Cloudy - O^{8+}$', linestyle=':', color='C8')


ax4.plot(pion_radius, O0, label=r'$\rm PION - O$', linestyle='-', color='C0')
ax4.plot(pion_radius, O1p, label=r'$\rm PION - O^{1+}$', linestyle='-', color='C1')
ax4.plot(pion_radius, O2p, label=r'$\rm PION - O^{2+}$', linestyle='-', color='C2')
ax4.plot(pion_radius, O3p, label=r'$\rm PION - O^{3+}$', linestyle='-', color='C3')
ax4.plot(pion_radius, O4p, label=r'$\rm PION - O^{4+}$', linestyle='-', color='C4')
ax4.plot(pion_radius, O5p, label=r'$\rm PION - O^{5+}$', linestyle='-', color='C5')
ax4.plot(pion_radius, O6p, label=r'$\rm PION - O^{6+}$', linestyle='-', color='C6')
ax4.plot(pion_radius, O7p, label=r'$\rm PION - O^{7+}$', linestyle='-', color='C7')
ax4.plot(pion_radius, O8p, label=r'$\rm PION - O^{8+}$', linestyle='-', color='C8')

ax4.xaxis.set_minor_locator(AutoMinorLocator())
ax4.yaxis.set_minor_locator(AutoMinorLocator())
ax4.tick_params(axis="both", direction="in", which="both",
               bottom=True, top=True, left=True, right=True, length=2, labelsize=8)

ax4.set_xlim([0.0, 6])
ax4.grid()
#ax.set_ylim([-25.5, -19.5])
ax4.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=8)
ax4.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=8)
ax4.legend(loc='lower left', bbox_to_anchor=(-0.1, -0.23), ncol=5, fontsize=8)




plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.2)
image_file = plot_dir + 'HII_Ionisa.png'
print("Saving image to", image_file)
plt.savefig(image_file, dpi=300)




'''

# Both the simulations use the following relevant parameters
rho = 2.26739E-24 # gas density in the units of g/cm^3
m_H = 1.67356E-24 # mass of Hydrogen atom in g
# Hence, the normalisation factor is
norm_factor = np.power(m_H/rho, 2.0)


Eatson_coolfn_original = '/home/mathew/Desktop/MIM_Pub_Datafiles/CIE_Cooling_Func/Eatson2022_original/Eatson_cooling_curve_WC_logT4-9.txt'

plot_data = []

# 1. Cooling function for Asplund 2002 abuandance ############################################

table_1 = ReadTable_Advance(Asplund_coolfn)
print("Table Size: ( row =", table_1['N_row'], ", columns = ", table_1['N_col'], ")")
dataset_1 = table_1['columns']

# x-data
asplund_log_temperature = np.log10(dataset_1[0])
N_Temp = table_1['N_row']

# y-dataset_1 for Asplund 2002 abuandance
# y dataset is the L function of individual ions.
Asplund_H  = [[np.log10(dataset_1[1]), 'H'], [np.log10(dataset_1[2]), 'H1+']]

Asplund_He = [[np.log10(dataset_1[3]), 'He'], [np.log10(dataset_1[4]), 'He1+'],
      [np.log10(dataset_1[5]), 'He2+']]

Asplund_C = [[np.log10(dataset_1[6]), 'C'], [np.log10(dataset_1[7]), 'C1+'],
     [np.log10(dataset_1[8]), 'C2+'], [np.log10(dataset_1[9]), 'C3+'],
     [np.log10(dataset_1[10]), 'C4+'], [np.log10(dataset_1[11]), 'C5+'],
     [np.log10(dataset_1[12]), 'C6+']]

Asplund_N = [[np.log10(dataset_1[13]), 'N'], [np.log10(dataset_1[14]), 'N1+'],
     [np.log10(dataset_1[15]), 'N2+'], [np.log10(dataset_1[16]), 'N3+'],
     [np.log10(dataset_1[17]), 'N4+'], [np.log10(dataset_1[18]), 'N5+'],
     [np.log10(dataset_1[19]), 'N6+'], [np.log10(dataset_1[20]), 'N7+']]

Asplund_O = [[np.log10(dataset_1[21]), 'O'], [np.log10(dataset_1[22]), 'O1+'],
     [np.log10(dataset_1[23]), 'O2+'], [np.log10(dataset_1[24]), 'O3+'],
     [np.log10(dataset_1[25]), 'O4+'], [np.log10(dataset_1[26]), 'O5+'],
     [np.log10(dataset_1[27]), 'O6+'], [np.log10(dataset_1[28]), 'O7+'],
     [np.log10(dataset_1[29]), 'O8+']]

Asplund_Ne = [[np.log10(dataset_1[30]), 'Ne'], [np.log10(dataset_1[31]), 'Ne1+'],
     [np.log10(dataset_1[32]), 'Ne2+'], [np.log10(dataset_1[33]), 'Ne3+'],
     [np.log10(dataset_1[34]), 'Ne4+'], [np.log10(dataset_1[35]), 'Ne5+'],
     [np.log10(dataset_1[36]), 'Ne6+'], [np.log10(dataset_1[37]), 'Ne7+'],
     [np.log10(dataset_1[38]), 'Ne8+'], [np.log10(dataset_1[39]), 'Ne9+'],
     [np.log10(dataset_1[40]), 'Ne10+']]

Asplund_Si = [[np.log10(dataset_1[41]), 'Si'], [np.log10(dataset_1[42]), 'Si1+'],
     [np.log10(dataset_1[43]), 'Si2+'], [np.log10(dataset_1[44]), 'Si3+'],
     [np.log10(dataset_1[45]), 'Si4+'], [np.log10(dataset_1[46]), 'Si5+'],
     [np.log10(dataset_1[47]), 'Si6+'], [np.log10(dataset_1[48]), 'Si7+'],
     [np.log10(dataset_1[49]), 'Si8+'], [np.log10(dataset_1[50]), 'Si9+'],
     [np.log10(dataset_1[51]), 'Si10+'], [np.log10(dataset_1[52]), 'Si11+'],
     [np.log10(dataset_1[53]), 'Si12+'], [np.log10(dataset_1[54]), 'Si13+'],
     [np.log10(dataset_1[55]), 'Si14+']]

Asplund_S = [[np.log10(dataset_1[56]), 'S'], [np.log10(dataset_1[57]), 'S1+'],
     [np.log10(dataset_1[58]), 'S2+'], [np.log10(dataset_1[59]), 'S3+'],
     [np.log10(dataset_1[60]), 'S4+'], [np.log10(dataset_1[61]), 'S5+'],
     [np.log10(dataset_1[62]), 'S6+'], [np.log10(dataset_1[63]), 'S7+'],
     [np.log10(dataset_1[64]), 'S8+'], [np.log10(dataset_1[65]), 'S9+'],
     [np.log10(dataset_1[66]), 'S10+'], [np.log10(dataset_1[67]), 'S11+'],
     [np.log10(dataset_1[68]), 'S12+'], [np.log10(dataset_1[69]), 'S13+'],
     [np.log10(dataset_1[70]), 'S14+'], [np.log10(dataset_1[71]), 'S15+'],
     [np.log10(dataset_1[72]), 'S16+']]

Asplund_Fe = [[np.log10(dataset_1[73]), 'Fe'], [np.log10(dataset_1[74]), 'Fe1+'],
     [np.log10(dataset_1[75]), 'Fe2+'], [np.log10(dataset_1[76]), 'Fe3+'],
     [np.log10(dataset_1[77]), 'Fe4+'], [np.log10(dataset_1[78]), 'Fe5+'],
     [np.log10(dataset_1[79]), 'Fe6+'], [np.log10(dataset_1[80]), 'Fe7+'],
     [np.log10(dataset_1[81]), 'Fe8+'], [np.log10(dataset_1[82]), 'Fe9+'],
     [np.log10(dataset_1[83]), 'Fe10+'], [np.log10(dataset_1[84]), 'Fe11+'],
     [np.log10(dataset_1[85]), 'Fe12+'], [np.log10(dataset_1[86]), 'Fe13+'],
     [np.log10(dataset_1[87]), 'Fe14+'], [np.log10(dataset_1[88]), 'Fe15+'],
     [np.log10(dataset_1[89]), 'Fe16+'], [np.log10(dataset_1[90]), 'Fe17+'],
     [np.log10(dataset_1[91]), 'Fe18+'], [np.log10(dataset_1[92]), 'Fe19+'],
     [np.log10(dataset_1[93]), 'Fe20+'], [np.log10(dataset_1[94]), 'Fe21+'],
     [np.log10(dataset_1[95]), 'Fe22+'], [np.log10(dataset_1[96]), 'Fe23+'],
     [np.log10(dataset_1[97]), 'Fe24+'], [np.log10(dataset_1[98]), 'Fe25+'],
     [np.log10(dataset_1[99]), 'Fe26+']]


asplund_element_list = [Asplund_H, Asplund_He, Asplund_C, Asplund_N, Asplund_O,
                        Asplund_Ne, Asplund_Si, Asplund_S, Asplund_Fe]
asplund_element_list_name = ['H', 'He', 'C', 'N', 'O', 'Ne', 'Si', 'S', 'Fe']
label_position = [[4.24, -22.6], [4.9, -22.8], [4.92, -22.3], [5.2, -22.4], [5.3, -21.9],
                  [5.63, -22.35], [6.1, -22.85], [6.37, -23.32], [7, -23.2]]
line_color = ['black', 'black', 'darkblue', 'darkblue', 'crimson', 'crimson', 'darkblue', 'darkgreen', 'darkgreen']
line_style = ['-.', '--', '--', '-', '-', '--', 'dotted', '--', '-']

# net Lambda
net_asplund_coolfn = [0.0] * N_Temp

asplund_elements_data = []

for element in range(len(asplund_element_list)):
    # elemental Lambda
    element_net = [0.0] * N_Temp

    single_element_data = {}
    for species in range(len(asplund_element_list[element])):
        element_net = element_net + norm_factor*np.power(10, asplund_element_list[element][species][0])

    single_element_data['x'] = asplund_log_temperature
    single_element_data['y'] = np.log10(element_net)
    single_element_data['labels'] = asplund_element_list_name[element]
    single_element_data['label-position'] = label_position[element]
    single_element_data['line-color'] = line_color[element]
    single_element_data['line-style'] = line_style[element]
    asplund_elements_data.append(single_element_data.copy())

    net_asplund_coolfn = net_asplund_coolfn + element_net

plot_data.append(asplund_elements_data)


# 2. Cooling function for Eatson 2022 abuandance ############################################

table_2 = ReadTable_Advance(Eatson_coolfn)
print("Table Size: ( row =", table_2['N_row'], ", columns = ", table_2['N_col'], ")")
dataset_2 = table_2['columns']

# x-dataset_2
eatson_log_temperature = np.log10(dataset_2[0])
N_Temp = table_2['N_row']

# y-dataset_2 for Eatson 2002 abuandance
Eatson_He = [[np.log10(dataset_2[1]), 'He'], [np.log10(dataset_2[2]), 'He1+'],
             [np.log10(dataset_2[3]), 'He2+']]

Eatson_C = [[np.log10(dataset_2[4]), 'C'], [np.log10(dataset_2[5]), 'C1+'],
            [np.log10(dataset_2[6]), 'C2+'], [np.log10(dataset_2[7]), 'C3+'],
            [np.log10(dataset_2[8]), 'C4+'], [np.log10(dataset_2[9]), 'C5+'],
            [np.log10(dataset_2[10]), 'C6+']]


Eatson_O = [[np.log10(dataset_2[11]), 'O'], [np.log10(dataset_2[12]), 'O1+'],
            [np.log10(dataset_2[13]), 'O2+'], [np.log10(dataset_2[14]), 'O3+'],
            [np.log10(dataset_2[15]), 'O4+'], [np.log10(dataset_2[16]), 'O5+'],
            [np.log10(dataset_2[17]), 'O6+'], [np.log10(dataset_2[18]), 'O7+'],
            [np.log10(dataset_2[19]), 'O8+']]

Eatson_Ne = [[np.log10(dataset_2[20]), 'Ne'], [np.log10(dataset_2[21]), 'Ne1+'],
             [np.log10(dataset_2[22]), 'Ne2+'], [np.log10(dataset_2[23]), 'Ne3+'],
             [np.log10(dataset_2[24]), 'Ne4+'], [np.log10(dataset_2[25]), 'Ne5+'],
             [np.log10(dataset_2[26]), 'Ne6+'], [np.log10(dataset_2[27]), 'Ne7+'],
             [np.log10(dataset_2[28]), 'Ne8+'], [np.log10(dataset_2[29]), 'Ne9+'],
             [np.log10(dataset_2[30]), 'Ne10+']]

Eatson_Si = [[np.log10(dataset_2[31]), 'Si'], [np.log10(dataset_2[32]), 'Si1+'],
             [np.log10(dataset_2[33]), 'Si2+'], [np.log10(dataset_2[34]), 'Si3+'],
             [np.log10(dataset_2[35]), 'Si4+'], [np.log10(dataset_2[36]), 'Si5+'],
             [np.log10(dataset_2[37]), 'Si6+'], [np.log10(dataset_2[38]), 'Si7+'],
             [np.log10(dataset_2[39]), 'Si8+'], [np.log10(dataset_2[40]), 'Si9+'],
             [np.log10(dataset_2[41]), 'Si10+'], [np.log10(dataset_2[42]), 'Si11+'],
             [np.log10(dataset_2[43]), 'Si12+'], [np.log10(dataset_2[44]), 'Si13+'],
             [np.log10(dataset_2[45]), 'Si14+']]

Eatson_S = [[np.log10(dataset_2[46]), 'S'], [np.log10(dataset_2[47]), 'S1+'],
            [np.log10(dataset_2[48]), 'S2+'], [np.log10(dataset_2[49]), 'S3+'],
            [np.log10(dataset_2[50]), 'S4+'], [np.log10(dataset_2[51]), 'S5+'],
            [np.log10(dataset_2[52]), 'S6+'], [np.log10(dataset_2[53]), 'S7+'],
            [np.log10(dataset_2[54]), 'S8+'], [np.log10(dataset_2[55]), 'S9+'],
            [np.log10(dataset_2[56]), 'S10+'], [np.log10(dataset_2[57]), 'S11+'],
            [np.log10(dataset_2[58]), 'S12+'], [np.log10(dataset_2[59]), 'S13+'],
            [np.log10(dataset_2[60]), 'S14+'], [np.log10(dataset_2[61]), 'S15+'],
            [np.log10(dataset_2[62]), 'S16+']]

Eatson_Fe = [[np.log10(dataset_2[63]), 'Fe'], [np.log10(dataset_2[64]), 'Fe1+'],
             [np.log10(dataset_2[65]), 'Fe2+'], [np.log10(dataset_2[66]), 'Fe3+'],
             [np.log10(dataset_2[67]), 'Fe4+'], [np.log10(dataset_2[68]), 'Fe5+'],
             [np.log10(dataset_2[69]), 'Fe6+'], [np.log10(dataset_2[70]), 'Fe7+'],
             [np.log10(dataset_2[71]), 'Fe8+'], [np.log10(dataset_2[72]), 'Fe9+'],
             [np.log10(dataset_2[73]), 'Fe10+'], [np.log10(dataset_2[74]), 'Fe11+'],
             [np.log10(dataset_2[75]), 'Fe12+'], [np.log10(dataset_2[76]), 'Fe13+'],
             [np.log10(dataset_2[77]), 'Fe14+'], [np.log10(dataset_2[78]), 'Fe15+'],
             [np.log10(dataset_2[79]), 'Fe16+'], [np.log10(dataset_2[80]), 'Fe17+'],
             [np.log10(dataset_2[81]), 'Fe18+'], [np.log10(dataset_2[82]), 'Fe19+'],
             [np.log10(dataset_2[83]), 'Fe20+'], [np.log10(dataset_2[84]), 'Fe21+'],
             [np.log10(dataset_2[85]), 'Fe22+'], [np.log10(dataset_2[86]), 'Fe23+'],
             [np.log10(dataset_2[87]), 'Fe24+'], [np.log10(dataset_2[88]), 'Fe25+'],
             [np.log10(dataset_2[89]), 'Fe26+']]


eatson_element_list = [Eatson_He, Eatson_C, Eatson_O,
                       Eatson_Ne, Eatson_Si, Eatson_S, Eatson_Fe]
eatson_element_list_name = ['He', 'C', 'O', 'Ne', 'Si', 'S', 'Fe']
eatson_label_position = [[4.9, -22.4], [4.96, -20.4], [5.34, -21.3], [5.4, -22.7], [5.0, -23.2], [6.25, -23.25], [6.0, -22.55]]
line_color = ['black', 'black', 'crimson', 'darkgreen', 'darkblue', 'crimson', 'darkgreen']
line_style = ['--', '--', '-', '--', '-', '--', '-']

net_eatson_coolfn = [0.0] * N_Temp

eatson_elements_data = []

for element in range(len(eatson_element_list)):
    element_net = [0.0] * N_Temp

    single_element_data = {}
    for species in range(len(eatson_element_list[element])):
        element_net = element_net + norm_factor*np.power(10, eatson_element_list[element][species][0])

    single_element_data['x'] = eatson_log_temperature
    single_element_data['y'] = np.log10(element_net)
    single_element_data['labels'] = eatson_element_list_name[element]
    single_element_data['label-position'] = eatson_label_position[element]
    single_element_data['line-color'] = line_color[element]
    single_element_data['line-style'] = line_style[element]
    eatson_elements_data.append(single_element_data.copy())

    net_eatson_coolfn = net_eatson_coolfn + element_net

plot_data.append(eatson_elements_data)

# 3. Net cooling for Asplund 2002 abundance #####################################
asplund_net_data = []
net_cooling_data = {}
asplund_element_list_name = ['Solar']
label_position = [[]]
line_color = ['black']
line_style = ['-']
net_cooling_data['x'] = asplund_log_temperature
net_cooling_data['y'] = np.log10(net_asplund_coolfn)
net_cooling_data['labels'] = asplund_element_list_name[0]
net_cooling_data['label-position'] = label_position[0]
net_cooling_data['line-color'] = line_color[0]
net_cooling_data['line-style'] = line_style[0]
asplund_net_data.append(net_cooling_data.copy())
plot_data.append(asplund_net_data)


# 4. Net cooling for Eatson 2022 abundance #####################################
eatson_net_data = []
net_cooling_data = {}
eatson_element_list_name = ['WC']
label_position = [[]]
line_color = ['darkblue']
line_style = ['-']
net_cooling_data['x'] = eatson_log_temperature
net_cooling_data['y'] = np.log10(net_eatson_coolfn)
net_cooling_data['labels'] = eatson_element_list_name[0]
net_cooling_data['label-position'] = label_position[0]
net_cooling_data['line-color'] = line_color[0]
net_cooling_data['line-style'] = line_style[0]
eatson_net_data.append(net_cooling_data.copy())
plot_data.append(eatson_net_data)


# 5, 6 appending asplund_net_dataset_1 qnd eatson_net_dataset_1 once again ###################
plot_data.append(asplund_net_data)
plot_data.append(eatson_net_data)
del asplund_net_data
del eatson_net_data

# table 3 original eatson 2022 data ###########################################
table_3 = ReadTable_Advance(Eatson_coolfn_original)
# This original data already is normalised  with norm_factor
print("Table Size: ( row =", table_3['N_row'], ", columns = ", table_3['N_col'], ")")

dataset_3 = table_3['columns']

# x-dataset_3, temperature is given in log
eatson_orig_log_T = dataset_3[0]
eatson_orig_net_data = []
net_cooling_data = {}
eatson_orig_element_list_name = ['Eatson et al. `22']
label_position = [[]]
line_color = ['crimson']
line_style = ['--']
net_cooling_data['x'] = eatson_orig_log_T
# y data (rates) are not in log, so we convert them to log
net_cooling_data['y'] = np.log10(dataset_3[1])
net_cooling_data['labels'] = eatson_orig_element_list_name[0]
net_cooling_data['label-position'] = label_position[0]
net_cooling_data['line-color'] = line_color[0]
net_cooling_data['line-style'] = line_style[0]
eatson_orig_net_data.append(net_cooling_data.copy())
#plot_data.append(eatson_orig_net_data)




# plot style #################################################################
plot_style = {}
plot_style['figsize'] = (6, 12)
plot_style['label-font-size'] = 12
plot_style['matrix'] = [3, 1]
plot_style['legend'] = True  # options: True/False
plot_style['sharex'] = False  # options: True/False, 'col', 'all'
plot_style['sharey'] = False # options: True/False, 'col', 'all'

plot_style['xlimit'] = [[4, 8.5], [4, 8.3], [4, 8.5]]
plot_style['ylimit'] = [[-25.5, -21.2], [-25.5, -19.6], [-25, -19.5]]

plot_style['force-plotting_1d'] = [[3,1], [4, 2], [6, 3], [7, 3]]

plot_style['axis-label'] = [[None, r"${\Large \rm log(\Lambda_N) \,  erg \, cm^3 \, s^{-1}}$"],
                            [None, r"${ \rm log(\Lambda_N) \,  erg \, cm^3 \, s^{-1}}$"],
                            [r"${\rm log(T) \, K}$", r"${ \rm log(\Lambda_N) \,  erg \, cm^3 \, s^{-1}}$"]]

plot_style['insert-txt'] = []


# plot margin adjustments
plot_style['left'] = 0.125  # the left side of the subplots of the figure
plot_style['right'] = 0.95  # the right side of the subplots of the figure
plot_style['bottom'] = 0.05  # the bottom of the subplots of the figure
plot_style['top'] = 0.95  # the top of the subplots of the figure
plot_style['wspace'] = 0.0  # the amount of width reserved for blank space between subplots
plot_style['hspace'] = 0.1  # the amount of height reserved for white space between subplots


plot_style['custom-legend'] = [
    [2, ['o', 'r', 'Line 1', '-', 6], ['s', 'b', 'Line 2', '--', 6]]
]

###################################################################
# Making INAM 2023 presentation plots
plot_dir = make_directory('INAM_2023')
plot_style['figsize'] = (14, 6)
plot_style['matrix'] = [1, 2]
plot_style['sharex'] = True  # options: True/False, 'col', 'all'
plot_style['sharey'] = True  # options: True/False, 'col', 'all'
plot_style['force-plotting_1d'] = [[3,1], [4, 2]]
plot_style['axis-label'] = [[r"${\rm log(T) \, K}$", r"${\Large \rm log(\Lambda_N) \,  erg \, cm^3 \, s^{-1}}$"],
                            [r"${\rm log(T) \, K}$", None],
                            [r"${\rm log(T) \, K}$", r"${ \rm log(\Lambda_N) \,  erg \, cm^3 \, s^{-1}}$"]]


plot_style['insert-txt'] = [[r'{With Solar Abundance}', -0.2, -20, 0], [r'{With WC Abundance}', 4.1, -20, 0],]

# plot margin adjustments
plot_style['left'] = 0.05  # the left side of the subplots of the figure
plot_style['right'] = 0.98  # the right side of the subplots of the figure
plot_style['bottom'] = 0.1  # the bottom of the subplots of the figure
plot_style['top'] = 0.95  # the top of the subplots of the figure
plot_style['wspace'] = 0.0  # the amount of width reserved for blank space between subplots
plot_style['hspace'] = 0.1  # the amount of height reserved for white space between subplots
###################################################################


# Plotting and saving the image to the file
onedim_master_plotter(plot_data, plot_style)
plt.savefig(plot_dir + 'cooling_function.png', dpi=300)

'''