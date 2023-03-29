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

Asplund_coolfn = '/home/mathew/Desktop/MIM_Pub_Datafiles/CIE_Cooling_Func/CoolFunc_Asplund2009/CIE_n128_Asplund2009_CoolFunc.txt'
Eatson_coolfn = '/home/mathew/Desktop/MIM_Pub_Datafiles/CIE_Cooling_Func/CoolFunc_Eatson2022/CIE_n128_Eatson2022_CoolFunc.txt'

plot_data = []

# 1. Cooling function for Asplund 2002 abuandance ############################################

table = ReadTable_Advance(Asplund_coolfn)
print("Table Size: ( row =", table['N_row'], ", columns = ", table['N_col'], ")")
data = table['columns']

# x-data
log_temperature = np.log10(data[0])
N_Temp = table['N_row']

# y-data for Asplund 2002 abuandance
Asplund_H  = [[np.log10(data[1]), 'H'], [np.log10(data[2]), 'H1+']]

Asplund_He = [[np.log10(data[3]), 'He'], [np.log10(data[4]), 'He1+'],
      [np.log10(data[5]), 'He2+']]

Asplund_C = [[np.log10(data[6]), 'C'], [np.log10(data[7]), 'C1+'],
     [np.log10(data[8]), 'C2+'], [np.log10(data[9]), 'C3+'],
     [np.log10(data[10]), 'C4+'], [np.log10(data[11]), 'C5+'],
     [np.log10(data[12]), 'C6+']]

Asplund_N = [[np.log10(data[13]), 'N'], [np.log10(data[14]), 'N1+'],
     [np.log10(data[15]), 'N2+'], [np.log10(data[16]), 'N3+'],
     [np.log10(data[17]), 'N4+'], [np.log10(data[18]), 'N5+'],
     [np.log10(data[19]), 'N6+'], [np.log10(data[20]), 'N7+']]

Asplund_O = [[np.log10(data[21]), 'O'], [np.log10(data[22]), 'O1+'],
     [np.log10(data[23]), 'O2+'], [np.log10(data[24]), 'O3+'],
     [np.log10(data[25]), 'O4+'], [np.log10(data[26]), 'O5+'],
     [np.log10(data[27]), 'O6+'], [np.log10(data[28]), 'O7+'],
     [np.log10(data[29]), 'O8+']]

Asplund_Ne = [[np.log10(data[30]), 'Ne'], [np.log10(data[31]), 'Ne1+'],
     [np.log10(data[32]), 'Ne2+'], [np.log10(data[33]), 'Ne3+'],
     [np.log10(data[34]), 'Ne4+'], [np.log10(data[35]), 'Ne5+'],
     [np.log10(data[36]), 'Ne6+'], [np.log10(data[37]), 'Ne7+'],
     [np.log10(data[38]), 'Ne8+'], [np.log10(data[39]), 'Ne9+'],
     [np.log10(data[40]), 'Ne10+']]

Asplund_Si = [[np.log10(data[41]), 'Si'], [np.log10(data[42]), 'Si1+'],
     [np.log10(data[43]), 'Si2+'], [np.log10(data[44]), 'Si3+'],
     [np.log10(data[45]), 'Si4+'], [np.log10(data[46]), 'Si5+'],
     [np.log10(data[47]), 'Si6+'], [np.log10(data[48]), 'Si7+'],
     [np.log10(data[49]), 'Si8+'], [np.log10(data[50]), 'Si9+'],
     [np.log10(data[51]), 'Si10+'], [np.log10(data[52]), 'Si11+'],
     [np.log10(data[53]), 'Si12+'], [np.log10(data[54]), 'Si13+'],
     [np.log10(data[55]), 'Si14+']]

Asplund_S = [[np.log10(data[56]), 'S'], [np.log10(data[57]), 'S1+'],
     [np.log10(data[58]), 'S2+'], [np.log10(data[59]), 'S3+'],
     [np.log10(data[60]), 'S4+'], [np.log10(data[61]), 'S5+'],
     [np.log10(data[62]), 'S6+'], [np.log10(data[63]), 'S7+'],
     [np.log10(data[64]), 'S8+'], [np.log10(data[65]), 'S9+'],
     [np.log10(data[66]), 'S10+'], [np.log10(data[67]), 'S11+'],
     [np.log10(data[68]), 'S12+'], [np.log10(data[69]), 'S13+'],
     [np.log10(data[70]), 'S14+'], [np.log10(data[71]), 'S15+'],
     [np.log10(data[72]), 'S16+']]

Asplund_Fe = [[np.log10(data[73]), 'Fe'], [np.log10(data[74]), 'Fe1+'],
     [np.log10(data[75]), 'Fe2+'], [np.log10(data[76]), 'Fe3+'],
     [np.log10(data[77]), 'Fe4+'], [np.log10(data[78]), 'Fe5+'],
     [np.log10(data[79]), 'Fe6+'], [np.log10(data[80]), 'Fe7+'],
     [np.log10(data[81]), 'Fe8+'], [np.log10(data[82]), 'Fe9+'],
     [np.log10(data[83]), 'Fe10+'], [np.log10(data[84]), 'Fe11+'],
     [np.log10(data[85]), 'Fe12+'], [np.log10(data[86]), 'Fe13+'],
     [np.log10(data[87]), 'Fe14+'], [np.log10(data[88]), 'Fe15+'],
     [np.log10(data[89]), 'Fe16+'], [np.log10(data[90]), 'Fe17+'],
     [np.log10(data[91]), 'Fe18+'], [np.log10(data[92]), 'Fe19+'],
     [np.log10(data[93]), 'Fe20+'], [np.log10(data[94]), 'Fe21+'],
     [np.log10(data[95]), 'Fe22+'], [np.log10(data[96]), 'Fe23+'],
     [np.log10(data[97]), 'Fe24+'], [np.log10(data[98]), 'Fe25+'],
     [np.log10(data[99]), 'Fe26+']]


asplund_element_list = [Asplund_H, Asplund_He, Asplund_C, Asplund_N, Asplund_O,
                        Asplund_Ne, Asplund_Si, Asplund_S, Asplund_Fe]
asplund_element_list_name = ['H', 'He', 'C', 'N', 'O', 'Ne', 'Si', 'S', 'Fe']
label_position = [[], [], [], [], [], [], [], [], []]
line_color = ['green', 'green', 'green', 'green', 'green', 'green', 'green', 'green', 'green']
line_style = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

net_asplund_coolfn = [0.0] * N_Temp

elements_data = []
for element in range(len(asplund_element_list)):
    element_net = [0.0] * N_Temp

    print('element--', element)

    single_element_data = {}
    for species in range(len(asplund_element_list[element])):
        element_net = element_net + np.power(10, asplund_element_list[element][species][0])
        print('species--', species)


    single_element_data['x'] = log_temperature
    single_element_data['y'] = np.log10(element_net)
    single_element_data['labels'] = asplund_element_list_name[element]
    single_element_data['label-position'] = label_position[element]
    #single_element_data['line-color'] = line_color[element]
    #single_element_data['line-style'] = line_style[element]
    elements_data.append(single_element_data.copy())

    net_asplund_coolfn = net_asplund_coolfn + element_net

plot_data.append(elements_data)
del elements_data




# 2. Cooling function for Eatson 2022 abuandance ############################################

table = ReadTable_Advance(Eatson_coolfn)
print("Table Size: ( row =", table['N_row'], ", columns = ", table['N_col'], ")")
data = table['columns']

# x-data
log_temperature = np.log10(data[0])
N_Temp = table['N_row']

# y-data for Asplund 2002 abuandance
Eatson_He = [[np.log10(data[1]), 'He'], [np.log10(data[2]), 'He1+'],
             [np.log10(data[3]), 'He2+']]

Eatson_C = [[np.log10(data[4]), 'C'], [np.log10(data[5]), 'C1+'],
            [np.log10(data[6]), 'C2+'], [np.log10(data[7]), 'C3+'],
            [np.log10(data[8]), 'C4+'], [np.log10(data[9]), 'C5+'],
            [np.log10(data[10]), 'C6+']]


Eatson_O = [[np.log10(data[11]), 'O'], [np.log10(data[12]), 'O1+'],
            [np.log10(data[13]), 'O2+'], [np.log10(data[14]), 'O3+'],
            [np.log10(data[15]), 'O4+'], [np.log10(data[16]), 'O5+'],
            [np.log10(data[17]), 'O6+'], [np.log10(data[18]), 'O7+'],
            [np.log10(data[19]), 'O8+']]

Eatson_Ne = [[np.log10(data[20]), 'Ne'], [np.log10(data[21]), 'Ne1+'],
             [np.log10(data[22]), 'Ne2+'], [np.log10(data[23]), 'Ne3+'],
             [np.log10(data[24]), 'Ne4+'], [np.log10(data[25]), 'Ne5+'],
             [np.log10(data[26]), 'Ne6+'], [np.log10(data[27]), 'Ne7+'],
             [np.log10(data[28]), 'Ne8+'], [np.log10(data[29]), 'Ne9+'],
             [np.log10(data[30]), 'Ne10+']]

Eatson_Si = [[np.log10(data[31]), 'Si'], [np.log10(data[32]), 'Si1+'],
             [np.log10(data[33]), 'Si2+'], [np.log10(data[34]), 'Si3+'],
             [np.log10(data[35]), 'Si4+'], [np.log10(data[36]), 'Si5+'],
             [np.log10(data[37]), 'Si6+'], [np.log10(data[38]), 'Si7+'],
             [np.log10(data[39]), 'Si8+'], [np.log10(data[40]), 'Si9+'],
             [np.log10(data[41]), 'Si10+'], [np.log10(data[42]), 'Si11+'],
             [np.log10(data[43]), 'Si12+'], [np.log10(data[44]), 'Si13+'],
             [np.log10(data[45]), 'Si14+']]

Eatson_S = [[np.log10(data[46]), 'S'], [np.log10(data[47]), 'S1+'],
            [np.log10(data[48]), 'S2+'], [np.log10(data[49]), 'S3+'],
            [np.log10(data[50]), 'S4+'], [np.log10(data[51]), 'S5+'],
            [np.log10(data[52]), 'S6+'], [np.log10(data[53]), 'S7+'],
            [np.log10(data[54]), 'S8+'], [np.log10(data[55]), 'S9+'],
            [np.log10(data[56]), 'S10+'], [np.log10(data[57]), 'S11+'],
            [np.log10(data[58]), 'S12+'], [np.log10(data[59]), 'S13+'],
            [np.log10(data[60]), 'S14+'], [np.log10(data[61]), 'S15+'],
            [np.log10(data[62]), 'S16+']]

Eatson_Fe = [[np.log10(data[63]), 'Fe'], [np.log10(data[64]), 'Fe1+'],
             [np.log10(data[65]), 'Fe2+'], [np.log10(data[66]), 'Fe3+'],
             [np.log10(data[67]), 'Fe4+'], [np.log10(data[68]), 'Fe5+'],
             [np.log10(data[69]), 'Fe6+'], [np.log10(data[70]), 'Fe7+'],
             [np.log10(data[71]), 'Fe8+'], [np.log10(data[72]), 'Fe9+'],
             [np.log10(data[73]), 'Fe10+'], [np.log10(data[74]), 'Fe11+'],
             [np.log10(data[75]), 'Fe12+'], [np.log10(data[76]), 'Fe13+'],
             [np.log10(data[77]), 'Fe14+'], [np.log10(data[78]), 'Fe15+'],
             [np.log10(data[79]), 'Fe16+'], [np.log10(data[80]), 'Fe17+'],
             [np.log10(data[81]), 'Fe18+'], [np.log10(data[82]), 'Fe19+'],
             [np.log10(data[83]), 'Fe20+'], [np.log10(data[84]), 'Fe21+'],
             [np.log10(data[85]), 'Fe22+'], [np.log10(data[86]), 'Fe23+'],
             [np.log10(data[87]), 'Fe24+'], [np.log10(data[88]), 'Fe25+'],
             [np.log10(data[89]), 'Fe26+']]


eatson_element_list = [Eatson_He, Eatson_C, Eatson_O,
                       Eatson_Ne, Eatson_Si, Eatson_S, Eatson_Fe]
eatson_element_list_name = ['He', 'C', 'O', 'Ne', 'Si', 'S', 'Fe']
label_position = [[], [], [], [], [], [], []]
line_color = ['green', 'green', 'green', 'green', 'green', 'green', 'green']
line_style = ['-', '-', '-', '-', '-', '-', '-']

net_eatson_coolfn = [0.0] * N_Temp

elements_data = []
for element in range(len(eatson_element_list)):
    element_net = [0.0] * N_Temp

    single_element_data = {}
    for species in range(len(eatson_element_list[element])):
        element_net = element_net + np.power(10, eatson_element_list[element][species][0])

    single_element_data['x'] = log_temperature
    single_element_data['y'] = np.log10(element_net)
    single_element_data['labels'] = asplund_element_list_name[element]
    single_element_data['label-position'] = label_position[element]
    #single_element_data['line-color'] = line_color[element]
    #single_element_data['line-style'] = line_style[element]
    elements_data.append(single_element_data.copy())

    net_eatson_coolfn = net_eatson_coolfn + element_net

plot_data.append(elements_data)
del elements_data


# 3. Net cooling for Asplund 2002 abundance #####################################
asplund_net_data = []
net_cooling_data = {}
asplund_element_list_name = ['net']
label_position = [[]]
line_color = ['green']
line_style = ['--']
net_cooling_data['x'] = log_temperature
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
eatson_element_list_name = ['net']
label_position = [[]]
line_color = ['orange']
line_style = [':']
net_cooling_data['x'] = log_temperature
net_cooling_data['y'] = np.log10(net_asplund_coolfn)
net_cooling_data['labels'] = asplund_element_list_name[0]
net_cooling_data['label-position'] = label_position[0]
net_cooling_data['line-color'] = line_color[0]
net_cooling_data['line-style'] = line_style[0]
eatson_net_data.append(net_cooling_data.copy())
plot_data.append(eatson_net_data)


# 5, 6 appending asplund_net_data qnd eatson_net_data once again ###################
plot_data.append(asplund_net_data)
plot_data.append(eatson_net_data)
del asplund_net_data
del eatson_net_data



# plot style #################################################################
plot_style = {}
plot_style['figsize'] = (9, 20)
plot_style['label-font-size'] = 12
plot_style['matrix'] = [3, 1]
plot_style['legend'] = True  # options: True/False
plot_style['sharex'] = False  # options: True/False, 'col', 'all'
plot_style['sharey'] = False  # options: True/False, 'col', 'all'

plot_style['xlimit'] = [[3.8, 8.5], [3.8, 8.5], [3.8, 8.5]]
plot_style['ylimit'] = [[-26, -20], [-26, -20], [-26, -20]]

plot_style['force-plotting_1d'] = [[3,1], [4, 2]]

plot_style['axis-label'] = [[None, r"${ \rm log(\Lambda) \,  erg \, cm^3 \, s^{-1}}$"],
                            [None, r"${ \rm log(\Lambda) \,  erg \, cm^3 \, s^{-1}}$"],
                            [r"${\rm log(T) \, K}$", r"${ \rm log(\Lambda) \,  erg \, cm^3 \, s^{-1}}$"]]

plot_style['insert-txt'] = []

# plot margin adjustments
plot_style['left'] = 0.1  # the left side of the subplots of the figure
plot_style['right'] = 0.9  # the right side of the subplots of the figure
plot_style['bottom'] = 0.1  # the bottom of the subplots of the figure
plot_style['top'] = 0.95  # the top of the subplots of the figure
plot_style['wspace'] = 0.0  # the amount of width reserved for blank space between subplots
plot_style['hspace'] = 0.1  # the amount of height reserved for white space between subplots

onedim_master_plotter(plot_data, plot_style)
plt.savefig('cooling_function.png')

