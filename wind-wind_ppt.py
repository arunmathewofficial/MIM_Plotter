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
from matplotlib.ticker import MaxNLocator

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

LINEWIDTH = 1.5

# find files and put them in order of levels:
files = []
lev = 0

for i in range(0, 20):
  seek = path + "/" + sim + "_level" + str(i).zfill(2) + "_0000.*.silo"
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

  xSi = dataio.get_1Darray("Tr006_X_Si")['data']
  xSi0 = dataio.get_1Darray("Tr043_Si")['data']
  xSi1 = dataio.get_1Darray("Tr044_Si1p")['data']
  xSi2 = dataio.get_1Darray("Tr045_Si2p")['data']
  xSi3 = dataio.get_1Darray("Tr046_Si3p")['data']
  xSi4 = dataio.get_1Darray("Tr047_Si4p")['data']
  xSi5 = dataio.get_1Darray("Tr048_Si5p")['data']
  xSi6 = dataio.get_1Darray("Tr049_Si6p")['data']
  xSi7 = dataio.get_1Darray("Tr050_Si7p")['data']
  xSi8 = dataio.get_1Darray("Tr051_Si8p")['data']
  xSi9 = dataio.get_1Darray("Tr052_Si9p")['data']
  xSi10 = dataio.get_1Darray("Tr053_Si10p")['data']
  xSi11 = dataio.get_1Darray("Tr054_Si11p")['data']
  xSi12 = dataio.get_1Darray("Tr055_Si12p")['data']
  xSi13 = dataio.get_1Darray("Tr056_Si13p")['data']




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

  XSi= get_single_array(n, np.array(xSi), np.array(vM))
  Si0 = get_single_array(n, np.array(xSi0), np.array(vM))
  Si1p = get_single_array(n, np.array(xSi1), np.array(vM))
  Si2p = get_single_array(n, np.array(xSi2), np.array(vM))
  Si3p = get_single_array(n, np.array(xSi3), np.array(vM))
  Si4p = get_single_array(n, np.array(xSi4), np.array(vM))
  Si5p = get_single_array(n, np.array(xSi5), np.array(vM))
  Si6p = get_single_array(n, np.array(xSi6), np.array(vM))
  Si7p = get_single_array(n, np.array(xSi7), np.array(vM))
  Si8p = get_single_array(n, np.array(xSi8), np.array(vM))
  Si9p = get_single_array(n, np.array(xSi9), np.array(vM))
  Si10p = get_single_array(n, np.array(xSi10), np.array(vM))
  Si11p = get_single_array(n, np.array(xSi11), np.array(vM))
  Si12p = get_single_array(n, np.array(xSi12), np.array(vM))
  Si13p = get_single_array(n, np.array(xSi13), np.array(vM))
  Si14p = XSi - Si0 - Si1p - Si2p - Si3p - Si4p - Si5p - Si6p - Si7p - Si8p - Si9p - Si10p - Si11p - Si12p - Si13p




  fig, ax = plt.subplots(3, 2, figsize=(13.33, 7.5), sharex=True)
  fig.suptitle(f'time: {time:.2e}', fontsize=16, x=0.05, ha='left')

  vr = vx * 1.0e-5  # convert to km/s
  nH = ro * XH / (apc.m_p.cgs.value)  # convert density to n(H)

  #################################################################################################
  ax[0][0].plot(pos, np.log10(ro * 1e26), label="$\\rho\, \left(10^{-26}\,\mathrm{g\,cm}^{-3}\\right)$",
                linewidth=LINEWIDTH, color='green', linestyle='--')
  ax[0][0].plot(pos, np.log10(np.fabs(vr)), label="$\left|v_r\\right|\, \left(\mathrm{km\,s}^{-1}\\right)$",
                linewidth=LINEWIDTH, color='blue', linestyle='--')
  ax[0][0].plot(pos, np.log10(tt * 1e-5), label="$T\, (10^5\,\mathrm{K})$", linewidth=LINEWIDTH,
                color='crimson', linestyle='--')
  ax[0][0].plot(pos, np.log10(nH*10000), label="$n_H \, \left(10^{-4}\,\mathrm{cm}^{-3}\\right)$",
                linewidth=LINEWIDTH, color='gray', linestyle='-')

  ax[0][0].set_xlim(0.0, 12)
  ax[0][0].set_yticks([-5, 0, 5])
  #ax[0][0].set_ylim(-3, 3.5)
  ax[0][0].legend(fontsize=16,
                  loc="upper right", ncol=4, columnspacing=0.4, bbox_to_anchor=(1.9, 1.3),
                  frameon=False)
  ax[0][0].tick_params(axis="both", direction="in", which="both", bottom=True,
                top=True, left=True, right=True, length=4, labelsize=14)

  #################################################################################################
  #ax[0][1].plot(pos, H0 / XH, label="$H^{0}$", linestyle='-', linewidth=LINEWIDTH)
  ax[0][1].plot(pos, H1p / XH, label="$H^{+}$", linestyle='-', linewidth=LINEWIDTH)
  #ax[0][1].plot(pos, He0/XHe, label="$He^{0}$", linestyle='-', linewidth=LINEWIDTH)
  ax[0][1].plot(pos, He1p/XHe, label="$He^{+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[0][1].plot(pos, He2p/XHe, label="$He^{2+}$", linestyle='-', linewidth=LINEWIDTH)

  ax[0][1].set_yticks([0, 0.5, 1.0])
  ax[0][1].tick_params(axis="both", direction="in", which="both", bottom=True,
                    top=True, left=True, right=True, length=2, labelsize=14)
  ax[0][1].legend(fontsize=14, loc="lower left", ncol=3, columnspacing=0.4,
                  frameon=False)

  #################################################################################################
  #ax[1][0].plot(pos, C0/XC, label="$C^{0}$", linestyle='-', linewidth=LINEWIDTH)
  #ax[1][0].plot(pos, C1p/XC, label="$C^{+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[1][0].plot(pos, C2p/XC, label="$C^{2+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[1][0].plot(pos, C3p/XC, label="$C^{3+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[1][0].plot(pos, C4p/XC, label="$C^{4+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[1][0].plot(pos, C5p/XC, label="$C^{5+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[1][0].plot(pos, C6p / XC, label="$C^{6+}$", color='black', linestyle='--', linewidth=LINEWIDTH)
  ax[1][0].set_yticks([0, 0.5, 1.0])
  ax[1][0].tick_params(axis="both", direction="in", which="both", bottom=True,
                       top=True, left=True, right=True, length=2, labelsize=14)
  ax[1][0].legend(fontsize=14, loc="lower left", ncol=3, columnspacing=0.4,
                  frameon=False)


  #################################################################################################
  #ax[1][1].plot(pos, N0/XN, label="$N^{0}$", linestyle='-', linewidth=LINEWIDTH)
  #ax[1][1].plot(pos, N1p/XN, label="$N^{+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[1][1].plot(pos, N2p/XN, label="$N^{2+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[1][1].plot(pos, N3p/XN, label="$N^{3+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[1][1].plot(pos, N4p/XN, label="$N^{4+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[1][1].plot(pos, N5p/XN, label="$N^{5+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[1][1].plot(pos, N6p/XN, label="$N^{6+}$", color='black', linestyle='--', linewidth=LINEWIDTH)
  ax[1][1].plot(pos, N7p / XN, label="$N^{7+}$",color='magenta', linestyle='-', linewidth=LINEWIDTH)

  ax[1][1].set_yticks([0, 0.5, 1.0])
  ax[1][1].tick_params(axis="both", direction="in", which="both", bottom=True,
                       top=True, left=True, right=True, length=2, labelsize=14)
  ax[1][1].legend(fontsize=14, loc="lower left", ncol=3, columnspacing=0.4,
                  frameon=False)

  #################################################################################################
  #oxygen
  #ax[2][0].plot(pos, O0/XO, label="$O^{0}$", linestyle='--', linewidth=LINEWIDTH)
  #ax[2][0].plot(pos, O1p/XO, label="$O^{+}$", linestyle='--', linewidth=LINEWIDTH)
  ax[2][0].plot(pos, O2p/XO, label="$O^{2+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[2][0].plot(pos, O3p/XO, label="$O^{3+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[2][0].plot(pos, O4p/XO, label="$O^{4+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[2][0].plot(pos, O5p/XO, label="$O^{5+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[2][0].plot(pos, O6p/XO, label="$O^{6+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[2][0].plot(pos, O7p/XO, label="$O^{7+}$", linestyle='-', linewidth=LINEWIDTH)
  ax[2][0].plot(pos, O8p/XO, label="$O^{8+}$", color='black', linestyle='--', linewidth=LINEWIDTH)

  ax[2][0].set_yticks([0, 0.5, 1.0])
  ax[2][0].tick_params(axis="both", direction="in", which="both", bottom=True,
                       top=True, left=True, right=True, length=2, labelsize=14)
  ax[2][0].legend(fontsize=14, loc="lower left", ncol=3, columnspacing=0.4, frameon=False)

  #################################################################################################
  #ax[2][1].plot(pos, Si0/XSi, label="$Si^{0}$", color='yellow')
  #ax[2][1].plot(pos, Si1p/XSi, label="$Si^{+}$", color='orange')
  #ax[2][1].plot(pos, Si2p/XSi, label="$Si^{2+}$", color='blue', linestyle='--', linewidth=LINEWIDTH)
  ax[2][1].plot(pos, Si3p/XSi, label="$Si^{3+}$", color='magenta', linestyle='-.', linewidth=LINEWIDTH)
  ax[2][1].plot(pos, Si4p/XSi, label="$Si^{4+}$", color='crimson', linestyle='-', linewidth=LINEWIDTH)
  ax[2][1].plot(pos, Si5p/XSi, label="$Si^{5+}$", color='green', linestyle='--', linewidth=LINEWIDTH)
  ax[2][1].plot(pos, Si6p/XSi, label="$Si^{6+}$", color='black', linestyle='--', linewidth=LINEWIDTH)
  ax[2][1].plot(pos, Si7p/XSi, label="$Si^{7+}$", color='blue')
  ax[2][1].plot(pos, Si8p/XSi, label="$Si^{8+}$", color='black')
  ax[2][1].plot(pos, Si9p/XSi, label="$Si^{9+}$")
  ax[2][1].plot(pos, Si10p/XSi, label="$Si^{10+}$")
  ax[2][1].plot(pos, Si11p/XSi, label="$Si^{11+}$")
  ax[2][1].plot(pos, Si12p/XSi, label="$Si^{12+}$", linestyle='--')
  ax[2][1].plot(pos, Si13p/XSi, label="$Si^{13+}$")
  ax[2][1].plot(pos, Si14p/XSi, label="$Si^{14+}$")

  ax[2][1].set_yticks([0, 0.5, 1.0])
  ax[2][1].tick_params(axis="both", direction="in", which="both", bottom=True,
                    top=True, left=True, right=True, length=4, labelsize=14)
  ax[2][1].legend(fontsize=14, loc="lower left", ncol=3, columnspacing=0.4, frameon=False)


  ax[0][0].set_ylabel(r'$\rm log_{10} \ Quantities$', fontsize=16)
  ax[0][1].set_ylabel(r'$Y_{\kappa, i}$', fontsize=16)
  ax[1][0].set_ylabel(r'$Y_{\kappa, i}$', fontsize=16)
  ax[1][1].set_ylabel(r'$Y_{\kappa, i}$', fontsize=16)
  ax[2][0].set_ylabel(r'$Y_{\kappa, i}$', fontsize=16)
  ax[2][1].set_ylabel(r'$Y_{\kappa, i}$', fontsize=16)
  ax[2][0].set_xlabel(r'$\rm radius (pc)$', fontsize=16)
  ax[2][1].set_xlabel(r'$\rm radius (pc)$', fontsize=16)




  dataio.close()
  del dataio
  plt.subplots_adjust(left=0.06, right=0.98, top=0.93, bottom=0.08, hspace=0.0, wspace=0.15)
  iy = str(i).zfill(5)
  opf = img_path + "/" + sim + "." + iy + ".png"


  plt.savefig(opf)
  plt.close()


