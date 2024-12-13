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
from astropy import constants as apc
import glob

parsec = apc.pc.cgs.value

# MAIN ##################################################################################
#test_dir= '/mnt/data/jm/code/pion/test/problems/mpv10_tests/photoionisation_test/'
#test_dir= '/home/jmackey/code/mipion/test/problems/mpv10_tests/photoionisation_test/'
test_dir='/mnt/local/jm/code/mi-pion/test/problems/mpv10_tests/photoionisation_test/'
data_dir='/mnt/massive-stars/data/nemo/methods/photoionisation/'
plot_dir = make_directory(test_dir+'MIM2023_Images')

dens = ['n1','n2','n3']
for d in dens:

  cloudyfile1_T  = data_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ovr'
  cloudyfile1_H  = data_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_H'
  cloudyfile1_He = data_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_He'
  cloudyfile1_C  = data_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_C'
  cloudyfile1_N  = data_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_N'
  cloudyfile1_O  = data_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_O'
  cloudyfile1_Ne = data_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_Ne'
  cloudyfile1_S  = data_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_S'

  cloudyfile2_T  = data_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ovr'
  cloudyfile2_H  = data_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_H'
  cloudyfile2_He = data_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_He'
  cloudyfile2_C  = data_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_C'
  cloudyfile2_N  = data_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_N'
  cloudyfile2_O  = data_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_O'
  cloudyfile2_Ne = data_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_Ne'
  cloudyfile2_S  = data_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_S'

  #seek04 = data_dir+"lores/"+d+"_lexington_e9_ots_0000.*.silo"
  #seek08 = data_dir+"lores/"+d+"_lexington_e9_nots_0000.*.silo"
  seek04 = data_dir+"silo_nbins/"+d+"nb04_lexington_e9_ots_0000.*.silo"
  seek08 = data_dir+"silo_nbins/"+d+"nb08_lexington_e9_ots_0000.*.silo"
  seek15 = data_dir+"silo/"+d+"_lexington_e9_ots_0000.*.silo"
  seek16 = data_dir+"silo_nbins/"+d+"nb16_lexington_e9_ots_0000.*.silo"
  seek28 = data_dir+"silo_nbins/"+d+"nb28_lexington_e9_ots_0000.*.silo"
  seek64 = data_dir+"silo_nbins/"+d+"nb64_lexington_e9_ots_0000.*.silo"
  #print(seek04)
  #print(seek08)
  #print(seek16)
  #print(seek28)

  f1 = sorted(glob.glob(seek04))
  pionfile04 = f1[-1]
  f2 = sorted(glob.glob(seek08))
  pionfile08 = f2[-1]
  f3 = sorted(glob.glob(seek16))
  pionfile16 = f3[-1]
  f4 = sorted(glob.glob(seek28))
  pionfile28 = f4[-1]
  f5 = sorted(glob.glob(seek64))
  pionfile64 = f5[-1]
  f6 = sorted(glob.glob(seek15))
  pionfile15 = f6[-1]

  torus_haworth = data_dir+'torus_photoionradial.dat'

# common variables #################################################################
  table_T1 = ReadTable_Advance(cloudyfile1_T)
  print("Table Size: ( row =", table_T1['N_row'], ", columns = ", table_T1['N_col'], ")")
  dataset_T1 = table_T1['columns']
  cloudy_radius1 = (np.array(dataset_T1[0]) + 1.0e17) / parsec

  table_T2 = ReadTable_Advance(cloudyfile2_T)
  print("Table Size: ( row =", table_T2['N_row'], ", columns = ", table_T2['N_col'], ")")
  dataset_T2 = table_T2['columns']
  cloudy_radius2 = (np.array(dataset_T2[0]) + 1.0e17) / parsec

  pion_obj1 = GetSiloData([pionfile04])
  pion1_radius = pion_obj1.get_radial_coordinate() / parsec
  pion_obj2 = GetSiloData([pionfile08])
  pion2_radius = pion_obj2.get_radial_coordinate() / parsec
  pion_obj6 = GetSiloData([pionfile15])
  pion6_radius = pion_obj6.get_radial_coordinate() / parsec
  #pion_obj3 = GetSiloData([pionfile16])
  #pion3_radius = pion_obj3.get_radial_coordinate() / parsec
  pion_obj4 = GetSiloData([pionfile28])
  pion4_radius = pion_obj4.get_radial_coordinate() / parsec
  pion_obj5 = GetSiloData([pionfile64])
  pion5_radius = pion_obj5.get_radial_coordinate() / parsec

  #pion_data    = [pion_obj1,pion_obj2,pion_obj6,pion_obj3,pion_obj4,pion_obj5]
  #pion_radius  = [pion1_radius,pion2_radius,pion6_radius,pion3_radius,pion4_radius,pion5_radius]
  pion_data    = [pion_obj1,pion_obj2,pion_obj6,pion_obj4,pion_obj5]
  pion_radius  = [pion1_radius,pion2_radius,pion6_radius,pion4_radius,pion5_radius]

  torus_data = np.loadtxt(torus_haworth)
  torus_radius = torus_data[:,0] / 3.08e8

  xmax = 5.2
  xmin = 0.0
  lab = xmin + 0.94*(xmax-xmin)

  #fig, (ax0, ax1, ax2) = plt.subplots(3, 1, figsize=(5, 13))
  fig, (ax0, ax2) = plt.subplots(2, 1, figsize=(5, 9))
  pion_markers = ['o','^','*','D','s','x']
  #pion_bins = ['$N_b=4$','$N_b=8$','$N_b=15$','$N_b=16$','$N_b=28$','$N_b=64$']
  pion_bins = ['$N_\mathrm{b}=4$','$N_\mathrm{b}=8$','$N_\mathrm{b}=15$','$N_\mathrm{b}=28$','$N_\mathrm{b}=64$']

# Temperature profile ##############################################################
  print("Plotting temperature profile:")
  print("Reading silo file:", pionfile04)
  pion_temp = []
  for i in range(len(pion_data)):
    pion_temp.append(pion_data[i].get_parameter('Temperature'))

  cloudy_temp1 = np.array(dataset_T1[1])
  cloudy_temp2 = np.array(dataset_T2[1])
  torus_temp = torus_data[:,2]
  #if (d == 'n2'):
  #  ax0.plot(torus_radius, torus_temp*1e-3, label='\\textrm{\\textsc{Torus}}', linestyle=':', color='black')
  for i in range(len(pion_radius)):
    ax0.plot(pion_radius[i], pion_temp[i]*1e-3, label='\\textrm{\\textsc{Pion} '+pion_bins[i], linestyle='-.', color='blue', marker=pion_markers[i], markevery=50+3*i)
  #ax0.plot(cloudy_radius1, cloudy_temp1*1e-3, label='\\textrm{\\textsc{Cloudy}}', linestyle='--', color='red')
  ax0.plot(cloudy_radius2, cloudy_temp2*1e-3, label='\\textrm{\\textsc{Cloudy} CaseB}', linestyle='-', color='red')
  ax0.xaxis.set_minor_locator(AutoMinorLocator())
  ax0.yaxis.set_minor_locator(AutoMinorLocator())
  ax0.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4, labelsize=12)
  ax0.tick_params(axis="both", direction="in", which="minor", bottom=True, top=True, left=True, right=True, length=2, labelsize=12)

  ax0.set_xlim([xmin,xmax])
  ax0.set_ylim([4.5, 11.0])
  #ax0.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
  ax0.set_ylabel("$T\,$ ($10^3\,$K)", fontsize=12)
  ax0.text(lab,10.3,"\\textrm{(a)}", fontsize=12)

  ax0.legend(frameon=False, loc='lower center', fontsize='11',ncol=2)
  #image_file = plot_dir + d + '_HII_temperature.png'
  #print("Saving image to", image_file)
  #plt.savefig(image_file, dpi=300, bbox_inches='tight')
  #plt.close()


# Oxygen profile ##############################################################
  print("Plotting Oxygen profile:")
  table1_O = ReadTable_Advance(cloudyfile1_O)
  dataset1_O = table1_O['columns']
  table2_O = ReadTable_Advance(cloudyfile2_O)
  dataset2_O = table2_O['columns']

  pion_O0 = []
  pion_O1 = []
  pion_O2 = []
  pion_O3 = []
  pion_O4 = []
  for i in range(len(pion_data)):
    print("Reading silo file:", pion_bins[i])
    pion_O0.append( pion_data[i].get_parameter('Tr025_O'  ) / pion_data[i].get_parameter('Tr004_X_O'))
    pion_O1.append( pion_data[i].get_parameter('Tr026_O1p') / pion_data[i].get_parameter('Tr004_X_O'))
    pion_O2.append( pion_data[i].get_parameter('Tr027_O2p') / pion_data[i].get_parameter('Tr004_X_O'))
    pion_O3.append( pion_data[i].get_parameter('Tr028_O3p') / pion_data[i].get_parameter('Tr004_X_O'))
    pion_O4.append( pion_data[i].get_parameter('Tr029_O4p') / pion_data[i].get_parameter('Tr004_X_O'))

  #ax2.plot(cloudy_radius1, dataset1_O[1], label=r'$\rm O$', linestyle='--', color='C0')
  #ax2.plot(cloudy_radius1, dataset1_O[2], label=r'$\rm O^{1+}$', linestyle='--', color='C1')
  #ax2.plot(cloudy_radius1, dataset1_O[3], label=r'$\rm O^{2+}$', linestyle='--', color='C2')
  #ax2.plot(cloudy_radius1, dataset1_O[4], label=r'$\rm O^{3+}$', linestyle='--', color='C3')
  ##ax2.plot(cloudy_radius1, dataset1_O[5], label=r'$\rm O^{4+}$', linestyle='--', color='C4')

  ax2.plot(cloudy_radius2, dataset2_O[1], label=r'$\rm O$', linestyle='-', color='C0')
  ax2.plot(cloudy_radius2, dataset2_O[2], label=r'$\rm O^{1+}$', linestyle='-', color='C1')
  ax2.plot(cloudy_radius2, dataset2_O[3], label=r'$\rm O^{2+}$', linestyle='-', color='C2')
  ax2.plot(cloudy_radius2, dataset2_O[4], label=r'$\rm O^{3+}$', linestyle='-', color='C3')
  #ax2.plot(cloudy_radius2, dataset2_O[5], label='', linestyle='-', color='C4')

  for i in range(len(pion_data)):
    ax2.plot(pion_radius[i], pion_O0[i], label='', linestyle='-.', color='C0', marker=pion_markers[i], markevery=50+3*i)
    ax2.plot(pion_radius[i], pion_O1[i], label='', linestyle='-.', color='C1', marker=pion_markers[i], markevery=50+3*i)
    ax2.plot(pion_radius[i], pion_O2[i], label='', linestyle='-.', color='C2', marker=pion_markers[i], markevery=50+3*i)
    ax2.plot(pion_radius[i], pion_O3[i], label='', linestyle='-.', color='C3', marker=pion_markers[i], markevery=50+3*i)
    #ax2.plot(pion1_radius[i], pion_O4[i], label='', linestyle='-.', color='C4', marker=pion_markers[i], markevery=50)

  ax2.xaxis.set_minor_locator(AutoMinorLocator())
  ax2.yaxis.set_minor_locator(AutoMinorLocator())
  ax2.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4, labelsize=12)
  ax2.tick_params(axis="both", direction="in", which="minor", bottom=True, top=True, left=True, right=True, length=2, labelsize=12)
  ax2.text(lab,0.5,"\\textrm{(c)}", fontsize=12)

  ax2.set_xlim([xmin,xmax])
  #ax2.grid()
  ax2.set_yscale("log")
  ax2.set_ylim([1e-4,1.5])
  ax2.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
  ax2.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=12)
  ax2.legend(loc='lower left', bbox_to_anchor=(0.05, 0.98), ncol=4, fontsize=11)


  plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.2)
  image_file = plot_dir + d + '_HHeO.png'
  print("Saving image to", image_file)
  plt.savefig(image_file, dpi=300, bbox_inches='tight')
  plt.close()
  del fig, ax0,ax2
# Oxygen profile ##############################################################

