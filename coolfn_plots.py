# Author: Arun Mathew
# Created: 10-11-2022
# Plotting Cooling functions with Asplund2002 and Eatson2022 Abundances

# Import required libraries: ##########################################
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from species import *

# MAIN ##################################################################################
make_directory('MIM_Publi_Plots')

Asplund_coolfn = '/home/tony/Desktop/MIM_Pub_Datafiles/CIE_Cooling_Func/CoolFunc_Asplund2009/CIE_n128_Asplund2009_CoolFunc.txt'
Eatson_coolfn = '/home/tony/Desktop/MIM_Pub_Datafiles/CIE_Cooling_Func/CoolFunc_Eatson2022/CIE_n128_Eatson2022_CoolFunc.txt'

Eatson_coolfn_original = '/home/tony/Desktop/MIM_Pub_Datafiles/CIE_Cooling_Func/Eatson2022_original/Eatson_cooling_curve_WC_logT4-9.txt'

plot_data = []

# 1. Cooling function for Asplund 2002 abuandance ############################################

table_1 = ReadTable_Advance(Asplund_coolfn)
print("Table Size: ( row =", table_1['N_row'], ", columns = ", table_1['N_col'], ")")
dataset_1 = table_1['columns']

# x-data
asplund_log_temperature = np.log10(dataset_1[0])
N_Temp = table_1['N_row']

# y-dataset_1 for Asplund 2002 abuandance
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
label_position = [[4.25, -22.5], [4.9, -22.5], [4.9, -22], [5.2, -22.2], [5.3, -21.6],
                  [5.7, -22.1], [6.1, -22.6], [6.4, -23.0], [7, -22.9]]
line_color = ['black', 'black', 'darkblue', 'darkblue', 'crimson', 'crimson', 'darkblue', 'darkgreen', 'darkgreen']
line_style = ['-.', '--', '--', '-', '-', '--', 'dotted', '--', '-']

net_asplund_coolfn = [0.0] * N_Temp

asplund_elements_data = []

for element in range(len(asplund_element_list)):
    element_net = [0.0] * N_Temp

    single_element_data = {}
    for species in range(len(asplund_element_list[element])):
        element_net = element_net + np.power(10, asplund_element_list[element][species][0])

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
eatson_label_position = [[4.95, -22.2], [4.95, -20.2], [5.33, -21.0], [5.4, -22.5], [5.0, -22.9], [6.25, -23.0], [6.0, -22.3]]
line_color = ['black', 'black', 'crimson', 'darkgreen', 'darkblue', 'crimson', 'darkgreen']
line_style = ['--', '--', '-', '--', '-', '--', '-']

net_eatson_coolfn = [0.0] * N_Temp

eatson_elements_data = []

for element in range(len(eatson_element_list)):
    element_net = [0.0] * N_Temp

    single_element_data = {}
    for species in range(len(eatson_element_list[element])):
        element_net = element_net + np.power(10, eatson_element_list[element][species][0])

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
print("Table Size: ( row =", table_3['N_row'], ", columns = ", table_3['N_col'], ")")

dataset_3 = table_3['columns']

# x-dataset_3, temperature is given in log
eatson_orig_log_T = dataset_3[0]

eatson_orig_net_data = []
net_cooling_data = {}
eatson_orig_element_list_name = ['Eatson 2022 original']
label_position = [[]]
line_color = ['crimson']
line_style = ['--']
net_cooling_data['x'] = eatson_orig_log_T
# y data (rates) are not in log, so we convert them to log
net_cooling_data['y'] = np.log10(dataset_3[1])
print(net_cooling_data['y'])
net_cooling_data['labels'] = eatson_orig_element_list_name[0]
net_cooling_data['label-position'] = label_position[0]
net_cooling_data['line-color'] = line_color[0]
net_cooling_data['line-style'] = line_style[0]
eatson_orig_net_data.append(net_cooling_data.copy())
plot_data.append(eatson_orig_net_data)




# plot style #################################################################
plot_style = {}
plot_style['figsize'] = (6, 12)
plot_style['label-font-size'] = 12
plot_style['matrix'] = [3, 1]
plot_style['legend'] = True  # options: True/False
plot_style['sharex'] = False  # options: True/False, 'col', 'all'
plot_style['sharey'] = False  # options: True/False, 'col', 'all'

plot_style['xlimit'] = [[4, 8.5], [4, 8.3], [4, 8.5]]
plot_style['ylimit'] = [[-25.5, -21], [-25, -19.5], [-25, -19.5]]

plot_style['force-plotting_1d'] = [[3,1], [4, 2], [6, 3], [7, 3]]

plot_style['axis-label'] = [[None, r"${\Large \rm log(\Lambda) \,  erg \, cm^3 \, s^{-1}}$"],
                            [None, r"${ \rm log(\Lambda) \,  erg \, cm^3 \, s^{-1}}$"],
                            [r"${\rm log(T) \, K}$", r"${ \rm log(\Lambda) \,  erg \, cm^3 \, s^{-1}}$"]]

plot_style['insert-txt'] = []

# plot margin adjustments
plot_style['left'] = 0.125  # the left side of the subplots of the figure
plot_style['right'] = 0.95  # the right side of the subplots of the figure
plot_style['bottom'] = 0.05  # the bottom of the subplots of the figure
plot_style['top'] = 0.95  # the top of the subplots of the figure
plot_style['wspace'] = 0.0  # the amount of width reserved for blank space between subplots
plot_style['hspace'] = 0.1  # the amount of height reserved for white space between subplots

onedim_master_plotter(plot_data, plot_style)
plt.savefig('cooling_function.png', dpi=300)

