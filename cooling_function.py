# Author: Arun Mathew
# Created: 10-11-2022
# Plotting Cooling functions with Asplund2002 and Eatson2022 Abundances
# Compare with original cooling data of Eatson 2022 for WC abundances

# Import required libraries: ##########################################
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *
from matplotlib.lines import Line2D

import argparse

parser = argparse.ArgumentParser()
parser.add_argument("Asplund_coolfn_data", type=str, help="Asplund 2009 cooling function data file")
parser.add_argument("Eatson_coolfn_data", type=str, help="Eatson 2022 cooling function data file")
parser.add_argument("Purpose", type=str, help="opt the purpose: journal or conference")
parser.add_argument("output_dir", type=str, help="give the output image dir path")
args = parser.parse_args()

Asplund_coolfn = args.Asplund_coolfn_data
Eatson_coolfn = args.Eatson_coolfn_data
purpose = args.Purpose
# Both the simulations use the following relevant parameters
rho = 2.26739E-24 # gas density in the units of g/cm^3
m_H = 1.67356E-24 # mass of Hydrogen atom in g
# Hence, the normalisation factor is
norm_factor = np.power(m_H/rho, 2.0)

# get original Eatson cooling function
Original_Eatson_coolfn_data_file = "data/Eatson_cooling_curve_WC_logT.txt"
Eatson_coolfn_original = Original_Eatson_coolfn_data_file

# Output directory
output_dir = args.output_dir
output_dir = make_directory(output_dir)

plot_data = []

# 1. Cooling function for Asplund 2002 abuandance ############################################

table_1 = ReadTable_Advance(Asplund_coolfn)
print("Table-1 Size: ( row =", table_1['N_row'], ", columns = ", table_1['N_col'], ")")
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

asplund_ne = dataset_1[100]
asplund_nH = dataset_1[101]

asplund_element_list = [Asplund_H, Asplund_He, Asplund_C, Asplund_N, Asplund_O,
                        Asplund_Ne, Asplund_Si, Asplund_S, Asplund_Fe]
asplund_element_list_name = ['H', 'He', 'C', 'N', 'O', 'Ne', 'Si', 'S', 'Fe']
label_position = [[4.22, -22.8], [4.9, -22.8], [4.92, -22.3], [5.2, -22.4], [5.3, -21.9],
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
print("Table-2 Size: ( row =", table_2['N_row'], ", columns = ", table_2['N_col'], ")")
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

eatson_ne = dataset_2[90]
eatson_ne = np.array(eatson_ne)
eatson_nH = np.full(eatson_ne.shape, asplund_nH[0])


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
del asplund_net_data

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
del eatson_net_data

# 5, 6, 7 appending asplund_net, Sutherland & Dopita, Wiersma 2009 ###################
# this is to plot the third figure in the cooling plot (comparison of net cooling)
asplund_net_data_refactor = []
net_cooling_data = {}
asplund_element_list_name_refactor = ['Solar']
label_position = [[]]
line_color = ['black']
line_style = ['-']
net_cooling_data['x'] = asplund_log_temperature
net_asplund_coolfn = net_asplund_coolfn / norm_factor / np.array(asplund_nH) / np.array(asplund_ne)
net_cooling_data['y'] = np.log10(net_asplund_coolfn)
net_cooling_data['labels'] = asplund_element_list_name_refactor[0]
net_cooling_data['label-position'] = label_position[0]
net_cooling_data['line-color'] = line_color[0]
net_cooling_data['line-style'] = line_style[0]
asplund_net_data_refactor.append(net_cooling_data.copy())
if(purpose == "journal"):
    plot_data.append(asplund_net_data_refactor)

# table 4 Sutherland & Dopita 1993 data ###########################################
Original_SD1993 = "data/SD93-m00-cie.txt"
table_4 = ReadTable_Advance(Original_SD1993)
# This original data already is normalised  with norm_factor
print("Table-4 Size: ( row =", table_4['N_row'], ", columns = ", table_4['N_col'], ")")
dataset_4 = table_4['columns']
# x-dataset_3, temperature is given in log
sd1993_orig_log_T = dataset_4[0]
sd1993_orig_lambda_norm = 10 ** np.array(dataset_4[5]) # we choose the normalised cooling fucntion
sd1993_orig_ne = np.array(dataset_4[1])
sd1993_orig_nH = np.array(dataset_4[2])
sd1993_orig_nt = np.array(dataset_4[3])
sd1993_orig_lambda = sd1993_orig_lambda_norm * sd1993_orig_nt
sd1993_orig_lambda_actual = sd1993_orig_lambda / sd1993_orig_nH
sd1993_orig_net_data = []
net_cooling_data = {}
sd1993_orig_element_list_name = ['Sutherland et al. `93']
label_position = [[]]
line_color = ['crimson']
line_style = ['--']
net_cooling_data['x'] = sd1993_orig_log_T
# y data (rates) are not in log, so we convert them to log
net_cooling_data['y'] = np.log10(sd1993_orig_lambda_actual)
net_cooling_data['labels'] = sd1993_orig_element_list_name[0]
net_cooling_data['label-position'] = label_position[0]
net_cooling_data['line-color'] = line_color[0]
net_cooling_data['line-style'] = line_style[0]
sd1993_orig_net_data.append(net_cooling_data.copy())
if (purpose == "journal"):
    plot_data.append(sd1993_orig_net_data)

# table 4 Wiersma 2009 original data ###########################################
Original_Wiersma09 = "data/Wiersma09-m00-cie.txt"
table_5 = ReadTable_Advance(Original_Wiersma09)
# This original data already is normalised  with norm_factor
print("Table Size: ( row =", table_5['N_row'], ", columns = ", table_5['N_col'], ")")
dataset_5 = table_5['columns']
# column 4 in txt file gives Lambda/n_H^2 [erg s-1 cm^3]

# x-dataset_5, temperature is given in K
wiersma09_orig_log_T = np.log10(dataset_5[0])
# H and He
wiersma09_orig_lambda_HHe = np.array(dataset_5[9]) # this is Lambda/n_H^2 [erg s-1 cm^3]
wiersma09_orig_nebynH = np.array(dataset_5[10]) # this is Lambda/n_H^2 [erg s-1 cm^3]
# Other elements
wiersma09_orig_lambda_C = np.array(dataset_5[16])
wiersma09_orig_lambda_N = np.array(dataset_5[17])
wiersma09_orig_lambda_O = np.array(dataset_5[18])
wiersma09_orig_lambda_Ne = np.array(dataset_5[19])
wiersma09_orig_lambda_Mg = np.array(dataset_5[20])
wiersma09_orig_lambda_Si = np.array(dataset_5[21])
wiersma09_orig_lambda_S = np.array(dataset_5[22])
wiersma09_orig_lambda_Ca = np.array(dataset_5[23])
wiersma09_orig_lambda_Fe = np.array(dataset_5[24])
wiersma09_orig_lambda_total = wiersma09_orig_lambda_HHe\
                              + wiersma09_orig_lambda_C + wiersma09_orig_lambda_N \
                              + wiersma09_orig_lambda_O + wiersma09_orig_lambda_Ne + wiersma09_orig_lambda_Mg \
                              + wiersma09_orig_lambda_Si + wiersma09_orig_lambda_Ca + wiersma09_orig_lambda_Fe

wiersma09_orig_lambda_net = wiersma09_orig_lambda_total / wiersma09_orig_nebynH
wiersma09_orig_net_data = []
net_cooling_data = {}
wiersma09_orig_element_list_name = ['Wiersma et al. `09']
label_position = [[]]
line_color = ['darkgreen']
line_style = ['--']
net_cooling_data['x'] = wiersma09_orig_log_T
# y data (rates) are not in log, so we convert them to log
net_cooling_data['y'] = np.log10(wiersma09_orig_lambda_net)
net_cooling_data['labels'] = wiersma09_orig_element_list_name[0]
net_cooling_data['label-position'] = label_position[0]
net_cooling_data['line-color'] = line_color[0]
net_cooling_data['line-style'] = line_style[0]
wiersma09_orig_net_data.append(net_cooling_data.copy())
if (purpose == "journal"):
    plot_data.append(wiersma09_orig_net_data)

# 8, 9 Eatson net obtained and Eatson original ###################
eatson_net_data_refactor = []
net_cooling_data = {}
eatson_element_list_name_refactor = ['WC']
label_position = [[]]
line_color = ['crimson']
line_style = ['-']
net_cooling_data['x'] = eatson_log_temperature
net_cooling_data['y'] = np.log10(net_eatson_coolfn)
net_cooling_data['labels'] = eatson_element_list_name_refactor[0]
net_cooling_data['label-position'] = label_position[0]
net_cooling_data['line-color'] = line_color[0]
net_cooling_data['line-style'] = line_style[0]
eatson_net_data_refactor.append(net_cooling_data.copy())
if(purpose == "journal"):
    plot_data.append(eatson_net_data_refactor)

# table 3 original eatson 2022 data ###########################################
table_3 = ReadTable_Advance(Eatson_coolfn_original)
# This original data already is normalised  with norm_factor
print("Table-3 Size: ( row =", table_3['N_row'], ", columns = ", table_3['N_col'], ")")
dataset_3 = table_3['columns']
# x-dataset_3, temperature is given in log
eatson_orig_log_T = dataset_3[0]
eatson_orig_net_data = []
net_cooling_data = {}
eatson_orig_element_list_name = ['Eatson et al. `22']
label_position = [[]]
line_color = ['darkblue']
line_style = ['--']
net_cooling_data['x'] = eatson_orig_log_T
# y data (rates) are not in log, so we convert them to log
net_cooling_data['y'] = np.log10(dataset_3[1])
net_cooling_data['labels'] = eatson_orig_element_list_name[0]
net_cooling_data['label-position'] = label_position[0]
net_cooling_data['line-color'] = line_color[0]
net_cooling_data['line-style'] = line_style[0]
eatson_orig_net_data.append(net_cooling_data.copy())
if(purpose == "journal"):
    plot_data.append(eatson_orig_net_data)




# plot style #################################################################
plot_style = {}

if(purpose == "journal"):
    plot_style['figsize'] = (6, 12)
    plot_style['label-font-size'] = 12
    plot_style['matrix'] = [4, 1]
    plot_style['legend'] = True  # options: True/False
    plot_style['sharex'] = False  # options: True/False, 'col', 'all'
    plot_style['sharey'] = False  # options: True/False, 'col', 'all'

    plot_style['xlimit'] = [[4, 8.5], [4, 8.3], [4, 8.5], [4, 8.5]]
    plot_style['ylimit'] = [[-25.5, -21.3], [-25.5, -19.8], [-24.5, -20], [-25, -19.5]]

    plot_style['force-plotting_1d'] = [[3, 1], [4, 2],
                                       [6, 3], [7, 3]
                                       ]

    plot_style['axis-label'] = [[None, r"${\rm log(\Lambda_N) \,  erg \, cm^3 \, s^{-1}}$"],
                                [None, r"${\rm log(\Lambda_N) \,  erg \, cm^3 \, s^{-1}}$"],
                                [None, r"${ \rm log(L_{cool}/(n_e \, n_H)) \,  erg \, cm^3 \, s^{-1}}$"],
                                [r"${\rm log(T) \, K}$", r"${ \rm log(\Lambda_N) \,  erg \, cm^3 \, s^{-1}}$"]]

    # plot_style['insert-txt'] = [[r'{Solar Abundance}', 2.2, 20, 0], [r'{With WC Abundance}', 4.1, -20, 0],]

    # plot margin adjustments
    plot_style['left'] = 0.14  # the left side of the subplots of the figure
    plot_style['right'] = 0.95  # the right side of the subplots of the figure
    plot_style['bottom'] = 0.04  # the bottom of the subplots of the figure
    plot_style['top'] = 0.98  # the top of the subplots of the figure
    plot_style['wspace'] = 0.0  # the amount of width reserved for blank space between subplots
    plot_style['hspace'] = 0.1  # the amount of height reserved for white space between subplots
    # plot_style['custom-legend'] = [
    #    [2, ['o', 'r', 'Line 1', '-', 6], ['s', 'b', 'Line 2', '--', 6]]
    # ]

if(purpose == "conference"):
    plot_style['figsize'] = (4, 5.4)
    plot_style['label-font-size'] = 4
    plot_style['matrix'] = [2, 1]
    plot_style['legend'] = True  # options: True/False
    plot_style['sharex'] = True  # options: True/False, 'col', 'all'
    plot_style['sharey'] = False  # options: True/False, 'col', 'all'

    plot_style['xlimit'] = [[4, 8.5], [4, 8.3], [4, 8.5]]
    plot_style['ylimit'] = [[-25.5, -21.2], [-25.5, -19.6], [-25, -19.5]]

    plot_style['force-plotting_1d'] = [[3, 1], [4, 2], [6, 3], [7, 3], [8, 3]]

    plot_style['axis-label'] = [[None, r"${\rm  log(\Lambda_N) \,  erg \, cm^3 \, s^{-1}}$"],
                                [r"${\rm \small log(T) \, K}$", r"${ \rm log(\Lambda_N) \,  erg \, cm^3 \, s^{-1}}$"]]

    # plot_style['insert-txt'] = [[r'{Solar Abundance}', 2.2, 20, 0], [r'{With WC Abundance}', 4.1, -20, 0],]

    # plot margin adjustments
    plot_style['left'] = 0.18  # the left side of the subplots of the figure
    plot_style['right'] = 0.98  # the right side of the subplots of the figure
    plot_style['bottom'] = 0.08  # the bottom of the subplots of the figure
    plot_style['top'] = 1.0  # the top of the subplots of the figure
    plot_style['wspace'] = 0.0  # the amount of width reserved for blank space between subplots
    plot_style['hspace'] = 0.0  # the amount of height reserved for white space between subplots
    # plot_style['custom-legend'] = [
    #    [2, ['o', 'r', 'Line 1', '-', 6], ['s', 'b', 'Line 2', '--', 6]]
    # ]


# Plotting and saving the image to the file
onedim_master_plotter(plot_data, plot_style)
plt.savefig(output_dir + 'cooling_function.png', dpi=300)

