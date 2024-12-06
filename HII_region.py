# Author: Arun Mathew
# Created: 23-06-2024
# Multi-ion-module-publication: The script plot the
# HII-region temperature and ionisation profile for the
# HII40 Lexington Benchmark

# Import required libraries: ##########################################

import argparse
from tools import *
from master_plotter import *
import numpy as np
import matplotlib.pyplot as plt
from SiloReader import GetSiloData
from matplotlib import colors as mcolors
from astropy import constants as apc
import glob

parsec = apc.pc.cgs.value

# MAIN ##################################################################################
parser = argparse.ArgumentParser()
parser.add_argument("input_dir", type=str, help="cloudy and silo input directory")
parser.add_argument("image_output_dir", type=str, help="Output image dir path")


args = parser.parse_args()
output_dir = args.image_output_dir
output_dir = make_directory(output_dir)
test_dir = args.input_dir

dens = ['n1', 'n2', 'n3']
for d in dens:

  cloudyfile1_T  = test_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ovr'
  cloudyfile1_H  = test_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_H'
  cloudyfile1_He = test_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_He'
  cloudyfile1_C  = test_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_C'
  cloudyfile1_N  = test_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_N'
  cloudyfile1_O  = test_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_O'
  cloudyfile1_Ne = test_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_Ne'
  cloudyfile1_S  = test_dir+'cloudy/hii-region-'+d+'/'+'HII_region_'+d+'.ele_S'

  cloudyfile2_T  = test_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ovr'
  cloudyfile2_H  = test_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_H'
  cloudyfile2_He = test_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_He'
  cloudyfile2_C  = test_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_C'
  cloudyfile2_N  = test_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_N'
  cloudyfile2_O  = test_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_O'
  cloudyfile2_Ne = test_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_Ne'
  cloudyfile2_S  = test_dir+'cloudy/hii-region-'+d+'-caseB/'+'HII_region_'+d+'.ele_S'

  #seek1 = test_dir+"lores/"+d+"_lexington_e9_ots_0000.*.silo"
  #seek2 = test_dir+"lores/"+d+"_lexington_e9_nots_0000.*.silo"
  seek1 = test_dir+"silo/"+d+"_lexington_e9_ots_0000.*.silo"
  seek2 = test_dir+"silo/"+d+"_lexington_e9_nots_0000.*.silo"
  print(seek1)
  print(seek2)

  f1 = sorted(glob.glob(seek1))
  pionfile1 = f1[-1]
  f2 = sorted(glob.glob(seek2))
  pionfile2 = f2[-1]



  torus_haworth = os.path.join('data', 'HII_region_photoionradial_tom.dat')

# common variables #################################################################
  table_T1 = ReadTable_Advance(cloudyfile1_T)
  print("Table Size: ( row =", table_T1['N_row'], ", columns = ", table_T1['N_col'], ")")
  dataset_T1 = table_T1['columns']
  cloudy_radius1 = (np.array(dataset_T1[0]) + 1.0e17) / parsec

  table_T2 = ReadTable_Advance(cloudyfile2_T)
  print("Table Size: ( row =", table_T2['N_row'], ", columns = ", table_T2['N_col'], ")")
  dataset_T2 = table_T2['columns']
  cloudy_radius2 = (np.array(dataset_T2[0]) + 1.0e17) / parsec

  pion_obj1 = GetSiloData([pionfile1])
  pion1_radius = pion_obj1.get_radial_coordinate() / parsec
  pion_obj2 = GetSiloData([pionfile2])
  pion2_radius = pion_obj2.get_radial_coordinate() / parsec

  torus_data = np.loadtxt(torus_haworth)
  torus_radius = torus_data[:,0] / 3.08e8

  xmax = 5.2
  xmin = 0.0
  lab = xmin + 0.94*(xmax-xmin)

# Plotting Cloudy ##############################################################
# cloudy1 is regular execution, cloudy2 is CaseB
  cloudy_temp1 = np.array(dataset_T1[1])
  cloudy_temp2 = np.array(dataset_T2[1])
  table1_H = ReadTable_Advance(cloudyfile1_H)
  dataset1_H = table1_H['columns']
  table1_He = ReadTable_Advance(cloudyfile1_He)
  dataset1_He = table1_He['columns']
  fig, ax = plt.subplots(figsize=(5, 3))
  # This uses the OTS
  table2_H = ReadTable_Advance(cloudyfile2_H)
  dataset2_H = table2_H['columns']
  table2_He = ReadTable_Advance(cloudyfile2_He)
  dataset2_He = table2_He['columns']

  ax.plot(cloudy_radius1, cloudy_temp1*1e-4, label='$T$ ($10^4$ \\textrm{K})', linestyle='-', color='C1')
  ax.plot(cloudy_radius2, cloudy_temp2*1e-4, label='$T$ ($10^4$ \\textrm{K) CaseB}', linestyle='-.', color='C1')
  ax.plot(cloudy_radius1, dataset1_H[2], label='$y(\\textrm{H}^+)$', linestyle='-', color='C4')
  ax.plot(cloudy_radius2, dataset2_H[2], label='', linestyle='-.', color='C4')
  ax.plot(cloudy_radius1, dataset1_He[2], label='$y(\\textrm{He}^+)$', linestyle='-', color='C3')
  ax.plot(cloudy_radius2, dataset2_He[2], label='', linestyle='-.', color='C3')
  ax.set_xlim([xmin,xmax])
  ax.set_ylim([0.0, 1.1])
  ax.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
  ax.set_ylabel("$T\,$ ($10^4\,$\\textrm{K) / ion fraction}", fontsize=12)
  ax.text(lab,1.03,"\\textrm{(a)}", fontsize=12)

  ax.legend(frameon=False, loc='lower center', fontsize='10')
  image_file = output_dir + d + '_cloudy_comp.png'
  print("Saving image to", image_file)
  plt.savefig(image_file, dpi=300, bbox_inches='tight')
  plt.close()

# Temperature profile ##############################################################
  print("Plotting temperature profile:")
  print("Reading silo file:", pionfile1)
  pion1_temp = pion_obj1.get_parameter('Temperature')
  pion2_temp = pion_obj2.get_parameter('Temperature')
  cloudy_temp1 = np.array(dataset_T1[1])
  cloudy_temp2 = np.array(dataset_T2[1])
  torus_temp = torus_data[:,2]
  fig, (ax0, ax1, ax2) = plt.subplots(3, 1, figsize=(5, 13))
  ax0.plot(cloudy_radius1, cloudy_temp1*1e-3, label='\\textrm{\\textsc{Cloudy}}', linestyle='-', color='red')
  ax0.plot(cloudy_radius2, cloudy_temp2*1e-3, label='\\textrm{\\textsc{Cloudy} CaseB}', linestyle='--', color='red')
  if (d == 'n2'):
    ax0.plot(torus_radius, torus_temp*1e-3, label='\\textrm{\\textsc{Torus}}', linestyle=':', color='black')
  ax0.plot(pion1_radius, pion1_temp*1e-3, label='\\textrm{\\textsc{Pion} OTS}', linestyle='-.', color='blue')
  #ax.plot(pion2_radius, pion2_temp*1e-3, label='\\textrm{\\textsc{Pion} no OTS}', linestyle=':', color='blue')
  ax0.xaxis.set_minor_locator(AutoMinorLocator())
  ax0.yaxis.set_minor_locator(AutoMinorLocator())
  ax0.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4, labelsize=12)
  ax0.tick_params(axis="both", direction="in", which="minor", bottom=True, top=True, left=True, right=True, length=2, labelsize=12)

  ax0.set_xlim([xmin,xmax])
  ax0.set_ylim([5.0, 11.0])
  #ax0.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
  ax0.set_ylabel("$T\,$ ($10^3\,$K)", fontsize=12)
  ax0.text(lab,10.3,"\\textrm{(a)}", fontsize=12)

  ax0.legend(frameon=False, loc='upper left', fontsize='11')
  #image_file = plot_dir + d + '_HII_temperature.png'
  #print("Saving image to", image_file)
  #plt.savefig(image_file, dpi=300, bbox_inches='tight')
  #plt.close()


# H, He, O plot ##############################################################
  print("Plotting H, He, O profile:")
  table1_H = ReadTable_Advance(cloudyfile1_H)
  dataset1_H = table1_H['columns']
  table1_He = ReadTable_Advance(cloudyfile1_He)
  dataset1_He = table1_He['columns']

  # This uses the OTS
  table2_H = ReadTable_Advance(cloudyfile2_H)
  dataset2_H = table2_H['columns']
  table2_He = ReadTable_Advance(cloudyfile2_He)
  dataset2_He = table2_He['columns']

  print("Reading silo file:", pionfile1)
  H0  = pion_obj1.get_parameter('Tr009_H')  / pion_obj1.get_parameter('Tr000_X_H')
  H1p = np.ones_like(H0) - H0

  He0  = pion_obj1.get_parameter('Tr010_He') / pion_obj1.get_parameter('Tr001_X_He')
  He1p = pion_obj1.get_parameter('Tr011_He1p') / pion_obj1.get_parameter('Tr001_X_He')
  He2p = np.ones_like(He0) - He0 - He1p

  #fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 8))

  ax1.plot(cloudy_radius1, dataset1_H[1], label='', linestyle=':', color='C0')
  ax1.plot(cloudy_radius1, dataset1_H[2], label='', linestyle=':', color='C1')
  ax1.plot(cloudy_radius1, dataset1_He[1], label='', linestyle=':', color='C2')
  ax1.plot(cloudy_radius1, dataset1_He[2], label='', linestyle=':', color='C3')
  ax1.plot(cloudy_radius1, dataset1_He[3], label='', linestyle=':', color='C4')

  ax1.plot(cloudy_radius2, dataset2_H[1], label='', linestyle='--', color='C0')
  ax1.plot(cloudy_radius2, dataset2_H[2], label='', linestyle='--', color='C1')
  ax1.plot(cloudy_radius2, dataset2_He[1], label='', linestyle='--', color='C2')
  ax1.plot(cloudy_radius2, dataset2_He[2], label='', linestyle='--', color='C3')
  ax1.plot(cloudy_radius2, dataset2_He[3], label='', linestyle='--', color='C4')

  ax1.plot(pion1_radius, H0, label=r'$\rm H$', linestyle='-', color='C0')
  ax1.plot(pion1_radius, H1p, label=r'$\rm H^{1+}$', linestyle='-', color='C1')
  ax1.plot(pion1_radius, He0, label=r'$\rm He$', linestyle='-', color='C2')
  ax1.plot(pion1_radius, He1p, label=r'$\rm He^{1+}$', linestyle='-', color='C3')
  ax1.plot(pion1_radius, He2p, label=r'$\rm He^{2+}$', linestyle='-', color='C4')

  ax1.xaxis.set_minor_locator(AutoMinorLocator())
  ax1.yaxis.set_minor_locator(AutoMinorLocator())
  ax1.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4, labelsize=12)
  ax1.tick_params(axis="both", direction="in", which="minor", bottom=True, top=True, left=True, right=True, length=2, labelsize=12)
  ax1.text(lab,0.5,"\\textrm{(b)}", fontsize=12)
  ax1.text(1.1,1.1e-1, "\\textrm{dotted:\n \\textrm{dashed:}\n \\textrm{solid:}", fontsize=12)
  ax1.text(2.1,1.1e-1, "\\textrm{\\textsc{Cloudy}}\n \\textrm{\\textsc{Cloudy} CaseB}\n \\textrm{\\textsc{Pion}}", fontsize=12)

  ax1.set_xlim([xmin,xmax])
  #ax1.grid()
  ax1.set_yscale("log")
  ax1.set_ylim([1e-4,1.5])
#ax.set_ylim([-25.5, -19.5])
  #ax1.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
  ax1.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=12)
  ax1.legend(loc='upper left', bbox_to_anchor=(-0.12, 1.15), ncol=5, fontsize=11)

# Oxygen profile ##############################################################
  print("Plotting Oxygen profile:")
  table1_O = ReadTable_Advance(cloudyfile1_O)
  dataset1_O = table1_O['columns']
  table2_O = ReadTable_Advance(cloudyfile2_O)
  dataset2_O = table2_O['columns']

  print("Reading silo file:", pionfile1)
  O0 = pion_obj1.get_parameter('Tr025_O'  ) / pion_obj1.get_parameter('Tr004_X_O')
  O1p = pion_obj1.get_parameter('Tr026_O1p') / pion_obj1.get_parameter('Tr004_X_O')
  O2p = pion_obj1.get_parameter('Tr027_O2p') / pion_obj1.get_parameter('Tr004_X_O')
  O3p = pion_obj1.get_parameter('Tr028_O3p') / pion_obj1.get_parameter('Tr004_X_O')
  O4p = pion_obj1.get_parameter('Tr029_O4p') / pion_obj1.get_parameter('Tr004_X_O')

  ax2.plot(cloudy_radius1, dataset1_O[1], label='', linestyle=':', color='C0')
  ax2.plot(cloudy_radius1, dataset1_O[2], label='', linestyle=':', color='C1')
  ax2.plot(cloudy_radius1, dataset1_O[3], label='', linestyle=':', color='C2')
  ax2.plot(cloudy_radius1, dataset1_O[4], label='', linestyle=':', color='C3')
  #ax2.plot(cloudy_radius1, dataset1_O[5], label='', linestyle=':', color='C4')

  ax2.plot(cloudy_radius2, dataset2_O[1], label='', linestyle='--', color='C0')
  ax2.plot(cloudy_radius2, dataset2_O[2], label='', linestyle='--', color='C1')
  ax2.plot(cloudy_radius2, dataset2_O[3], label='', linestyle='--', color='C2')
  ax2.plot(cloudy_radius2, dataset2_O[4], label='', linestyle='--', color='C3')
  #ax2.plot(cloudy_radius2, dataset2_O[5], label='', linestyle='--', color='C4')

  ax2.plot(pion1_radius, O0, label=r'$\rm O$', linestyle='-', color='C0')
  ax2.plot(pion1_radius, O1p, label=r'$\rm O^{1+}$', linestyle='-', color='C1')
  ax2.plot(pion1_radius, O2p, label=r'$\rm O^{2+}$', linestyle='-', color='C2')
  ax2.plot(pion1_radius, O3p, label=r'$\rm O^{3+}$', linestyle='-', color='C3')
  #ax2.plot(pion1_radius, O4p, label=r'$\rm O^{4+}$', linestyle='-', color='C4')

  ax2.xaxis.set_minor_locator(AutoMinorLocator())
  ax2.yaxis.set_minor_locator(AutoMinorLocator())
  ax2.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4, labelsize=12)
  ax2.tick_params(axis="both", direction="in", which="minor", bottom=True, top=True, left=True, right=True, length=2, labelsize=12)
  ax2.text(lab,0.5,"\\textrm{(c)}", fontsize=12)

  ax2.set_xlim([xmin,xmax])
  #ax2.grid()
  ax2.set_yscale("log")
  ax2.set_ylim([1e-4,1.5])
#ax.set_ylim([-25.5, -19.5])
  ax2.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
  ax2.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=12)
  ax2.legend(loc='lower left', bbox_to_anchor=(-0.05, 0.98), ncol=5, fontsize=12)


  plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.2)
  image_file = output_dir + d + '_HHeO.png'
  print("Saving image to", image_file)
  plt.savefig(image_file, dpi=300, bbox_inches='tight')
  plt.close()
  del fig, ax1,ax2

# H, He, O plot ##############################################################
  print("Plotting H, He, O ZOOM profile:")

  fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(5, 8))

  ax1.plot(cloudy_radius1, dataset1_H[1], label='', linestyle=':', color='C0')
  ax1.plot(cloudy_radius1, dataset1_H[2], label='', linestyle=':', color='C1')
  ax1.plot(cloudy_radius1, dataset1_He[1], label='', linestyle=':', color='C2')
  ax1.plot(cloudy_radius1, dataset1_He[2], label='', linestyle=':', color='C3')
  #ax1.plot(cloudy_radius1, dataset1_He[3], label='', linestyle=':', color='C4')

  ax1.plot(cloudy_radius2, dataset2_H[1], label='', linestyle='--', color='C0')
  ax1.plot(cloudy_radius2, dataset2_H[2], label='', linestyle='--', color='C1')
  ax1.plot(cloudy_radius2, dataset2_He[1], label='', linestyle='--', color='C2')
  ax1.plot(cloudy_radius2, dataset2_He[2], label='', linestyle='--', color='C3')
  #ax1.plot(cloudy_radius2, dataset2_He[3], label='', linestyle='--', color='C4')

  ax1.plot(pion1_radius, H0, label=r'$\rm H$', linestyle='-', color='C0')
  ax1.plot(pion1_radius, H1p, label=r'$\rm H^{1+}$', linestyle='-', color='C1')
  ax1.plot(pion1_radius, He0, label=r'$\rm He$', linestyle='-', color='C2')
  ax1.plot(pion1_radius, He1p, label=r'$\rm He^{1+}$', linestyle='-', color='C3')
  #ax1.plot(pion1_radius, He2p, label=r'$\rm He^{2+}$', linestyle='-', color='C4')

  ax1.xaxis.set_minor_locator(AutoMinorLocator())
  ax1.yaxis.set_minor_locator(AutoMinorLocator())
  ax1.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4, labelsize=12)
  ax1.tick_params(axis="both", direction="in", which="minor", bottom=True, top=True, left=True, right=True, length=2, labelsize=12)
  ax1.text(4.93,0.5,"\\textrm{(x)}", fontsize=12)
  if (d=='n1'):
    locx = 4.025
    locy = 1.5e-4
    leg = 1
  elif (d=='n2'):
    locx = 4.025
    locy = 1.5e-4
    leg = 1
  elif (d=='n3'):
    locx = 4.025
    locy = 1.3e-2
    leg = 1
  if leg:
    ax1.text(locx,locy, "\\textrm{dotted:\n \\textrm{dashed:}\n \\textrm{solid:}", fontsize=12)
    ax1.text(locx+0.13,locy, "\\textrm{\\textsc{Cloudy}}\n \\textrm{\\textsc{Cloudy} CaseB}\n \\textrm{\\textsc{Pion}}", fontsize=12)

  ax1.set_xlim([4,5])
  #ax1.grid()
  ax1.set_yscale("log")
  ax1.set_ylim([1e-4,1.5])
#ax.set_ylim([-25.5, -19.5])
  #ax1.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
  ax1.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=12)
  ax1.legend(loc='upper left', bbox_to_anchor=(0.0, 1.15), ncol=4, fontsize=11)

# Oxygen profile ##############################################################
  print("Plotting Oxygen profile:")
  print("Reading silo file:", pionfile1)
  O0 = pion_obj1.get_parameter('Tr025_O'  ) / pion_obj1.get_parameter('Tr004_X_O')
  O1p = pion_obj1.get_parameter('Tr026_O1p') / pion_obj1.get_parameter('Tr004_X_O')
  O2p = pion_obj1.get_parameter('Tr027_O2p') / pion_obj1.get_parameter('Tr004_X_O')
  O3p = pion_obj1.get_parameter('Tr028_O3p') / pion_obj1.get_parameter('Tr004_X_O')
  O4p = pion_obj1.get_parameter('Tr029_O4p') / pion_obj1.get_parameter('Tr004_X_O')

  ax2.plot(cloudy_radius1, dataset1_O[1], label='', linestyle=':', color='C0')
  ax2.plot(cloudy_radius1, dataset1_O[2], label='', linestyle=':', color='C1')
  ax2.plot(cloudy_radius1, dataset1_O[3], label='', linestyle=':', color='C2')
  ax2.plot(cloudy_radius1, dataset1_O[4], label='', linestyle=':', color='C3')
  #ax2.plot(cloudy_radius1, dataset1_O[5], label='', linestyle=':', color='C4')

  ax2.plot(cloudy_radius2, dataset2_O[1], label='', linestyle='--', color='C0')
  ax2.plot(cloudy_radius2, dataset2_O[2], label='', linestyle='--', color='C1')
  ax2.plot(cloudy_radius2, dataset2_O[3], label='', linestyle='--', color='C2')
  ax2.plot(cloudy_radius2, dataset2_O[4], label='', linestyle='--', color='C3')
  #ax2.plot(cloudy_radius2, dataset2_O[5], label='', linestyle='--', color='C4')

  ax2.plot(pion1_radius, O0, label=r'$\rm O$', linestyle='-', color='C0')
  ax2.plot(pion1_radius, O1p, label=r'$\rm O^{1+}$', linestyle='-', color='C1')
  ax2.plot(pion1_radius, O2p, label=r'$\rm O^{2+}$', linestyle='-', color='C2')
  ax2.plot(pion1_radius, O3p, label=r'$\rm O^{3+}$', linestyle='-', color='C3')
  #ax2.plot(pion1_radius, O4p, label=r'$\rm O^{4+}$', linestyle='-', color='C4')

  ax2.xaxis.set_minor_locator(AutoMinorLocator())
  ax2.yaxis.set_minor_locator(AutoMinorLocator())
  ax2.tick_params(axis="both", direction="in", which="major", bottom=True, top=True, left=True, right=True, length=4, labelsize=12)
  ax2.tick_params(axis="both", direction="in", which="minor", bottom=True, top=True, left=True, right=True, length=2, labelsize=12)
  ax2.text(4.93,0.5,"\\textrm{(x)}", fontsize=12)

  ax2.set_xlim([4,5])
  #ax2.grid()
  ax2.set_yscale("log")
  ax2.set_ylim([1e-4,1.5])
#ax.set_ylim([-25.5, -19.5])
  ax2.set_xlabel(r"${\rm Radius \, (pc)}$", fontsize=12)
  ax2.set_ylabel(r"$\rm Ionisation \, \, Fraction $", fontsize=12)
  ax2.legend(loc='lower left', bbox_to_anchor=(0.0, 0.98), ncol=4, fontsize=12)


  plt.subplots_adjust(left=0.1, right=0.95, top=0.95, bottom=0.2)
  image_file = output_dir + d + '_HHeO_ZOOM.png'
  print("Saving image to", image_file)
  plt.savefig(image_file, dpi=300, bbox_inches='tight')
  plt.close()