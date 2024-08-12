# -*- coding: iso-8859-15 -*-

import sys

# sys.path.insert(0,"/home/jm/code/pypion/silo/lib")
sys.path.insert(0,"/home/tony/.local/silo/lib/")
from pypion.ReadData import ReadData
import numpy as np
import matplotlib.pyplot as plt
import argparse
import glob
import astropy.units as u
from astropy import constants as apc
import matplotlib as mpl
import pandas as pd
from scipy.interpolate import UnivariateSpline


mpl.rcParams['font.family'] = 'serif'
mpl.rcParams['font.serif'] = ['Computer Modern Roman']
mpl.rcParams['text.usetex'] = True

############################################################################
# flatten 1D PION nested-grid data into a single array
def get_single_array(nlevel, arr, mask):
  if (nlevel == 1):
    return arr[0] * mask[0]

  # start at finest level and add coarser data, removing masked elements
  # first
  b = arr[nlevel - 1]
  for i in range(nlevel - 2, -1, -1):
    c = np.delete(arr[i], np.where(mask[i] == 0))
    b = np.append(b, c)
  return np.array(b)


############################################################################


#plt.rcParams["font.weight"] = "normal"
# ignore divide-by-zero warnings :)
np.seterr(divide='ignore')

parser = argparse.ArgumentParser()
parser.add_argument("path", type=str)
parser.add_argument("fbase", type=str)
parser.add_argument("img_path", type=str)
args = parser.parse_args()
path = args.path
sim = args.fbase
img_path = args.img_path

LINEWIDTH = 2

# find files and put them in order of levels:
files = []
lev = 0

for i in range(0, 20):
  seek = path + "/" + sim + "_level" + str(i).zfill(2) + "_0000.003*.silo"
  # print(seek)
  f = sorted(glob.glob(seek))
  if (len(f) < 1):
    print("didn't find any files", f)
    break;
  else:
    files.append(f)
    lev = lev + 1

if (len(files) < 1):
  quit()

for i in range(len(files[0])):
  datafile = []
  for v in range(0, lev):
    datafile.append(files[v][i])
  print(i, datafile[0])
  dataio = ReadData(datafile)

  n = dataio.nlevels()
  c = dataio.cycle()
  # print(n,c)
  D = dataio.get_1Darray("Density")
  vP = dataio.get_1Darray("Pressure")['data']
  vV = dataio.get_1Darray("VelocityX")['data']
  vE = dataio.get_1Darray("Temperature")['data']
  tr0 = dataio.get_1Darray("Tr007_Trace")['data']

  xH = dataio.get_1Darray("Tr000_X_H")['data']
  xH0 = dataio.get_1Darray("Tr009_H")['data']

  xHe = dataio.get_1Darray("Tr001_X_He")['data']
  xHe0 = dataio.get_1Darray("Tr010_He")['data']
  xHe1 = dataio.get_1Darray("Tr011_He1p")['data']

  xC = dataio.get_1Darray("Tr002_X_C")['data']
  xC0 = dataio.get_1Darray("Tr012_C")['data']
  xC1 = dataio.get_1Darray("Tr013_C1p")['data']
  xC2 = dataio.get_1Darray("Tr014_C2p")['data']
  xC3 = dataio.get_1Darray("Tr015_C3p")['data']
  xC4 = dataio.get_1Darray("Tr016_C4p")['data']
  xC5 = dataio.get_1Darray("Tr017_C5p")['data']

  xN = dataio.get_1Darray("Tr003_X_N")['data']
  xN0 = dataio.get_1Darray("Tr018_N")['data']
  xN1 = dataio.get_1Darray("Tr019_N1p")['data']
  xN2 = dataio.get_1Darray("Tr020_N2p")['data']
  xN3 = dataio.get_1Darray("Tr021_N3p")['data']
  xN4 = dataio.get_1Darray("Tr022_N4p")['data']
  xN5 = dataio.get_1Darray("Tr023_N5p")['data']
  xN6 = dataio.get_1Darray("Tr024_N6p")['data']

  xO = dataio.get_1Darray("Tr004_X_O")['data']
  xO0 = dataio.get_1Darray("Tr025_O")['data']
  xO1 = dataio.get_1Darray("Tr026_O1p")['data']
  xO2 = dataio.get_1Darray("Tr027_O2p")['data']
  xO3 = dataio.get_1Darray("Tr028_O3p")['data']
  xO4 = dataio.get_1Darray("Tr029_O4p")['data']
  xO5 = dataio.get_1Darray("Tr030_O5p")['data']
  xO6 = dataio.get_1Darray("Tr031_O6p")['data']
  xO7 = dataio.get_1Darray("Tr032_O7p")['data']



  if lev > 1:
    vM = dataio.get_1Darray("NG_Mask")['data']
  vD = D['data']  # this is an array of arrays, one for each grid level

  time = (D['sim_time'] * u.s).to(u.kyr)

  print("time=", time)
  xmax = (D['max_extents'] * u.cm).to(u.pc)
  xmin = (D['min_extents'] * u.cm).to(u.pc)
  ng = dataio.ngrid()

  # get position arrays
  vpos = []
  for ilev in range(n):
    lmin = xmin[ilev].value
    lmax = xmax[ilev].value
    dx = (lmax[0] - lmin[0]) / ng[0]
    x0 = lmin[0] + 0.5 * dx
    xn = lmax[0] - 0.5 * dx
    x = np.linspace(x0, xn, ng[0])
    vpos.append(x)
  vpos = np.array(vpos)

  pos = get_single_array(n, np.array(vpos), np.array(vM))
  ro = get_single_array(n, np.array(vD), np.array(vM))
  pg = get_single_array(n, np.array(vP), np.array(vM))
  vx = get_single_array(n, np.array(vV), np.array(vM))
  tt = get_single_array(n, np.array(vE), np.array(vM))
  tr = get_single_array(n, np.array(tr0), np.array(vM))

  XH = get_single_array(n, np.array(xH), np.array(vM))
  H0 = get_single_array(n, np.array(xH0), np.array(vM))
  H1p = XH - H0

  XHe = get_single_array(n, np.array(xHe), np.array(vM))
  He0 = get_single_array(n, np.array(xHe0), np.array(vM))
  He1p = get_single_array(n, np.array(xHe1), np.array(vM))
  He2p = XHe - He0 - He1p

  XC = get_single_array(n, np.array(xC), np.array(vM))
  C0 = get_single_array(n, np.array(xC0), np.array(vM))
  C1p = get_single_array(n, np.array(xC1), np.array(vM))
  C2p = get_single_array(n, np.array(xC2), np.array(vM))
  C3p = get_single_array(n, np.array(xC3), np.array(vM))
  C4p = get_single_array(n, np.array(xC4), np.array(vM))
  C5p = get_single_array(n, np.array(xC5), np.array(vM))
  C6p = XC - C0 - C1p - C2p - C3p - C4p - C5p

  XN = get_single_array(n, np.array(xN), np.array(vM))
  N0 = get_single_array(n, np.array(xN0), np.array(vM))
  N1p = get_single_array(n, np.array(xN1), np.array(vM))
  N2p = get_single_array(n, np.array(xN2), np.array(vM))
  N3p = get_single_array(n, np.array(xN3), np.array(vM))
  N4p = get_single_array(n, np.array(xN4), np.array(vM))
  N5p = get_single_array(n, np.array(xN5), np.array(vM))
  N6p = get_single_array(n, np.array(xN6), np.array(vM))
  N7p = XN - N0 - N1p - N2p - N3p - N4p - N5p - N6p

  XO= get_single_array(n, np.array(xO), np.array(vM))
  O0 = get_single_array(n, np.array(xO0), np.array(vM))
  O1p = get_single_array(n, np.array(xO1), np.array(vM))
  O2p = get_single_array(n, np.array(xO2), np.array(vM))
  O3p = get_single_array(n, np.array(xO3), np.array(vM))
  O4p = get_single_array(n, np.array(xO4), np.array(vM))
  O5p = get_single_array(n, np.array(xO5), np.array(vM))
  O6p = get_single_array(n, np.array(xO6), np.array(vM))
  O7p = get_single_array(n, np.array(xO7), np.array(vM))
  O8p = XO - O0 - O1p - O2p - O3p - O4p - O5p - O6p - O7p

  fig, ax = plt.subplots(5, 1, figsize=(8, 15), sharex=True)

  vr = vx * 1.0e-5  # convert to km/s
  nH = ro * XH / (apc.m_p.cgs.value)  # convert density to n(H)


  ax[0].plot(pos, np.log10(ro * 1e24), "m-",
             label="$\\rho\, \left(10^{-24}\,\mathrm{g\,cm}^{-3}\\right)$", linewidth=LINEWIDTH)
  ax[0].plot(pos, np.log10(np.fabs(vr)), "b--",
             label="$\left|v_r\\right|\, \left(\mathrm{km\,s}^{-1}\\right)$", linewidth=LINEWIDTH)
  ax[0].plot(pos, np.log10(tt * 1e-5), "r-.",
             label="$T\, (10^5\,\mathrm{K})$", linewidth=LINEWIDTH)
  ax[0].plot(pos, np.log10(nH), "g--", label="$n_H$", linewidth=LINEWIDTH)

  ax[1].plot(pos, H0 / XH, color='crimson', linestyle='-', linewidth=LINEWIDTH)
  ax[1].plot(pos, H1p / XH, label="$H^{+}$", color='blue', linestyle='-', linewidth=LINEWIDTH)
  ax[1].text(4, 0.05, r'$\rm H^{0}$', fontsize=16)
  ax[1].text(4, 0.9, r'$\rm H^{+}$', fontsize=16)

  #ax[1].plot(pos, He0/XHe, label="$He^{0}$", color='green', linestyle='-', linewidth=LINEWIDTH)
  ax[1].plot(pos, He1p/XHe, label="$He^{+}$", color='magenta', linestyle='--', linewidth=LINEWIDTH)
  ax[1].plot(pos, He2p/XHe, label="$He^{2+}$", color='green', linestyle='--', linewidth=LINEWIDTH)
  ax[1].text(4, 0.55, r'$\rm He^{+}$', fontsize=16)
  ax[1].text(4, 0.4, r'$\rm He^{2+}$', fontsize=16)

  print2file = {'R(pc)': np.round(pos, 4), 'Den(g cm^-3)': np.array([f"{rho:.4e}" for rho in ro]),
                'vr(km s^-1)': np.round(np.fabs(vr), 4), 'T(K)': np.round(tt, 4),
                'nH(cm^-3)': np.array([f"{n:.4e}" for n in nH]), 'H': np.round(H0/XH, 4), 'H1+': np.round(H1p/XH, 4),
                'He': np.round(He0/XHe, 4), 'He1+': np.round(He1p/XHe, 4), 'He2+': np.round(He2p/XHe, 4)}

  #ax[2].plot(pos, C0/XC, label="$C^{0}$")
  #ax[2].plot(pos, C1p/XC, label="$C^{+}$", color='blue', linestyle='--', linewidth=LINEWIDTH)
  ax[2].plot(pos, C2p/XC, label="$C^{2+}$", color='magenta', linestyle='-', linewidth=LINEWIDTH)
  ax[2].plot(pos, C3p/XC, label="$C^{3+}$", color='green', linestyle='-', linewidth=LINEWIDTH)
  ax[2].plot(pos, C4p/XC, label="$C^{4+}$", color='blue', linestyle='--', linewidth=LINEWIDTH)
  ax[2].plot(pos, C5p/XC, label="$C^{5+}$", color='crimson', linestyle='--', linewidth=LINEWIDTH)
  #ax[2].plot(pos, C6p/XC, label="$C^{6+}$")

  ax[2].text(11, 0.23, r'$\rm C^{2+}$', fontsize=16)
  ax[2].text(4, 0.85, r'$\rm C^{3+}$', fontsize=16)
  ax[2].text(8.3, 0.7, r'$\rm C^{4+}$', fontsize=16)
  ax[2].text(8.1, 0.32, r'$\rm C^{5+}$', fontsize=16)

  print2file['C'] = np.round(C0/XC, 4)
  print2file['C1+'] = np.round(C1p/XC, 4)
  print2file['C2+'] = np.round(C2p/XC, 4)
  print2file['C3+'] = np.round(C3p/XC, 4)
  print2file['C4+'] = np.round(C4p/XC, 4)
  print2file['C5+'] = np.round(C5p/XC, 4)
  print2file['C6+'] = np.round(C6p/XC, 4)

  #ax[3].plot(pos, N0/XN, label="$N^{0}$")
  #ax[3].plot(pos, N1p/XN, label="$N^{+}$")
  ax[3].plot(pos, N2p/XN, label="$N^{2+}$", color='magenta', linestyle='-', linewidth=LINEWIDTH)
  ax[3].plot(pos, N3p/XN, label="$N^{3+}$", color='blue', linestyle='-.', linewidth=LINEWIDTH)
  ax[3].plot(pos, N4p/XN, label="$N^{4+}$", color='crimson', linestyle='-', linewidth=LINEWIDTH)
  spline = UnivariateSpline(pos, N5p/XN, s=0.1)
  norm_N5p_smooth = spline(pos)
  #norm_C4p_smooth[norm_C4p_smooth < 0] = 0
  ax[3].plot(pos, norm_N5p_smooth, label="$N^{5+}$", color='green', linestyle='--', linewidth=LINEWIDTH)
  ax[3].plot(pos, N6p/XN, label="$N^{6+}$", color='black', linestyle='--', linewidth=LINEWIDTH)
  #ax[3].plot(pos, N7p/XN, label="$N^{7+}$")

  ax[3].text(10.5, 0.1, r'$\rm N^{2+}$', fontsize=16)
  ax[3].text(4, 0.85, r'$\rm N^{3+}$', fontsize=16)
  ax[3].text(6.5, 0.3, r'$\rm N^{4+}$', fontsize=16)
  ax[3].text(8.6, 0.83, r'$\rm N^{5+}$', fontsize=16)
  ax[3].text(8.3, 0.32, r'$\rm N^{6+}$', fontsize=16)


  print2file['N'] = np.round(N0/XN, 4)
  print2file['N1+'] = np.round(N1p/XN, 4)
  print2file['N2+'] = np.round(N2p/XN, 4)
  print2file['N3+'] = np.round(N3p/XN, 4)
  print2file['N4+'] = np.round(N4p/XN, 4)
  print2file['N5+'] = np.round(N5p/XN, 4)
  print2file['N6+'] = np.round(N6p/XN, 4)
  print2file['N7+'] = np.round(N7p/XN, 4)


  #oxygen ################################################################################
  #ax[4].plot(pos, O0/XO, label="$O^{0}$", color='yellow')
  #ax[4].plot(pos, O1p/XO, label="$O^{+}$", color='orange')
  ax[4].plot(pos, O2p/XO, label="$O^{2+}$", color='blue', linestyle='--', linewidth=LINEWIDTH)
  ax[4].plot(pos, O3p/XO, label="$O^{3+}$", color='magenta', linestyle='-.', linewidth=LINEWIDTH)
  ax[4].plot(pos, O4p/XO, label="$O^{4+}$", color='crimson', linestyle='-', linewidth=LINEWIDTH)
  #spline = UnivariateSpline(pos, O5p/XO, s=0.1)
  #norm_O5p_smooth = spline(pos)
  #norm_C4p_smooth[norm_C4p_smooth < 0] = 0
  ax[4].plot(pos, O5p/XO, label="$O^{5+}$", color='green', linestyle='--', linewidth=LINEWIDTH)
  ax[4].plot(pos, O6p/XO, label="$O^{6+}$", color='black', linestyle='--', linewidth=LINEWIDTH)
  #ax[4].plot(pos, O7p/XO, label="$O^{7+}$", color = 'blue')
  #ax[4].plot(pos, O8p/XO, label="$O^{8+}$", color='black')

  ax[4].text(4, 0.85, r'$\rm O^{2+}$', fontsize=16)
  ax[4].text(6.0, 0.2, r'$\rm O^{3+}$', fontsize=16)
  ax[4].text(7.4, 0.51, r'$\rm O^{4+}$', fontsize=16)
  ax[4].text(8.2, 0.55, r'$\rm O^{5+}$', fontsize=16)
  ax[4].text(8.6, 0.85, r'$\rm O^{6+}$', fontsize=16)


  print2file['O'] = np.round(O0/XO, 4)
  print2file['O1+'] = np.round(O1p/XO, 4)
  print2file['O2+'] = np.round(O2p/XO, 4)
  print2file['O3+'] = np.round(O3p/XO, 4)
  print2file['O4+'] = np.round(O4p/XO, 4)
  print2file['O5+'] = np.round(O5p/XO, 4)
  print2file['O6+'] = np.round(O6p/XO, 4)
  print2file['O7+'] = np.round(O7p/XO, 4)
  print2file['O8+'] = np.round(O8p/XO, 4)


  # legends ###############################################################################
  ax[0].legend(fontsize=14, loc="upper right", ncol=4, frameon=True,
               columnspacing=0.5, bbox_to_anchor=(1.005, 1.3))


  ax[0].set_ylabel(r'\rm log$_{10}$ Quantities', fontsize=18)
  ax[1].set_ylabel(r'$\rm Ionisation \ fraction$', fontsize=18)
  ax[2].set_ylabel(r'$\rm Ionisation \ fraction$', fontsize=18)
  ax[3].set_ylabel(r'$\rm Ionisation \ fraction$', fontsize=18)
  ax[4].set_ylabel(r'$\rm Ionisation \ fraction$', fontsize=18)
  ax[4].set_xlabel(r'$\rm Radius (pc)$', fontsize=18)

  ax[0].set_xlim(0.0, 12)
  ax[0].set_ylim(-3, 3.5)

  ax[0].tick_params(axis="both", direction="in", which="both", bottom=True,
                top=True, left=True, right=True, length=4, labelsize=14)
  ax[1].tick_params(axis="both", direction="in", which="both", bottom=True,
                    top=True, left=True, right=True, length=4, labelsize=14)
  ax[2].tick_params(axis="both", direction="in", which="both", bottom=True,
                    top=True, left=True, right=True, length=4, labelsize=14)
  ax[3].tick_params(axis="both", direction="in", which="both", bottom=True,
                    top=True, left=True, right=True, length=4, labelsize=14)
  ax[4].tick_params(axis="both", direction="in", which="both", bottom=True,
                    top=True, left=True, right=True, length=4, labelsize=14)

  plt.subplots_adjust(hspace=0.0)
  iy = str(i).zfill(5)
  opf = img_path + "/" + sim + "." + iy + ".png"
  # plt.show()

  df = pd.DataFrame(print2file)
  file_path = img_path + "/" + sim + "." + iy + ".txt"
  df.to_csv(file_path, index=False, sep='\t')
  plt.savefig(opf, bbox_inches="tight")
  del print2file
  del df
  plt.close(fig)
  del fig
  dataio.close()
  del dataio

quit()