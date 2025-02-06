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

from brokenaxes import brokenaxes
import matplotlib.gridspec as gridspec

plt.rc('font', family='serif', serif=['Times New Roman'])
plt.legend(prop={'family': 'Times New Roman'})

#plt.rcParams['font.family'] = 'serif'
#plt.rcParams['font.serif'] = ['Times New Roman']  # You can specify other fonts as well

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

########################################################################
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
########################################################################


i = 0
print(f' silo file: {i}')
datafile = []
for v in range(0, lev):
  datafile.append(files[v][i])
print(i, datafile[0])
dataio = ReadData(datafile)

n = dataio.nlevels()
c = dataio.cycle()
# print(n,c)
D = dataio.get_1Darray("Density")

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

XO_0= get_single_array(n, np.array(xO), np.array(vM))
O0_0 = get_single_array(n, np.array(xO0), np.array(vM))
O1p_0 = get_single_array(n, np.array(xO1), np.array(vM))
O2p_0 = get_single_array(n, np.array(xO2), np.array(vM))
O3p_0 = get_single_array(n, np.array(xO3), np.array(vM))
O4p_0 = get_single_array(n, np.array(xO4), np.array(vM))
O5p_0 = get_single_array(n, np.array(xO5), np.array(vM))
O6p_0 = get_single_array(n, np.array(xO6), np.array(vM))
O7p_0 = get_single_array(n, np.array(xO7), np.array(vM))
O8p_0 = XO_0 - O0_0 - O1p_0 - O2p_0 - O3p_0 - O4p_0 - O5p_0 - O6p_0 - O7p_0

dataio.close()
del dataio
########################################################################


########################################################################
i = 1
print(f' silo file: {i}')
datafile = []
for v in range(0, lev):
  datafile.append(files[v][i])
print(i, datafile[0])
dataio = ReadData(datafile)

n = dataio.nlevels()
c = dataio.cycle()
# print(n,c)
D = dataio.get_1Darray("Density")

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

XO_1 = get_single_array(n, np.array(xO), np.array(vM))
O0_1 = get_single_array(n, np.array(xO0), np.array(vM))
O1p_1 = get_single_array(n, np.array(xO1), np.array(vM))
O2p_1 = get_single_array(n, np.array(xO2), np.array(vM))
O3p_1 = get_single_array(n, np.array(xO3), np.array(vM))
O4p_1 = get_single_array(n, np.array(xO4), np.array(vM))
O5p_1 = get_single_array(n, np.array(xO5), np.array(vM))
O6p_1 = get_single_array(n, np.array(xO6), np.array(vM))
O7p_1 = get_single_array(n, np.array(xO7), np.array(vM))
O8p_1 = XO_1 - O0_1 - O1p_1 - O2p_1 - O3p_1 - O4p_1 - O5p_1 - O6p_1 - O7p_1

dataio.close()
del dataio
############################################################################


fig, ax = plt.subplots(2, 1, figsize=(8, 8), sharex=True)

# non-equilibirium oxygen ##################################################
#ax.plot(pos, O0_0 / XO_0, label="$O$", color='yellow', linewidth=LINEWIDTH)
#ax.plot(pos, O1p_0 / XO_0, label="$O^{+}$", color='orange', linewidth=LINEWIDTH)
ax[0].plot(pos, O2p_0 / XO_0, linestyle='--', color='blue',  linewidth=LINEWIDTH)
ax[0].plot(pos, O3p_0 / XO_0, linestyle='-', color='green',  linewidth=LINEWIDTH)
ax[0].plot(pos, O4p_0 / XO_0, linestyle='--', color='crimson',  linewidth=LINEWIDTH)
ax[0].plot(pos, O5p_0 / XO_0, linestyle='-', color='black',  linewidth=LINEWIDTH)
ax[0].plot(pos, O6p_0 / XO_0, color='gray', linestyle='--',  linewidth=LINEWIDTH)
ax[0].plot(pos, O7p_0 / XO_0, label="O$^{7+}$", color='orange', linewidth=LINEWIDTH)
ax[0].plot(pos, O8p_0 / XO_0, label="O$^{8+}$", color='magenta', linewidth=LINEWIDTH)

# equilibirium oxygen ##################################################
#ax.plot(pos, O0_1 / XO_1, color='yellow', linestyle='--',linewidth=LINEWIDTH)
#ax.plot(pos, O1p_1 / XO_1, color='orange', linestyle='--',linewidth=LINEWIDTH)
ax[1].plot(pos, O2p_1 / XO_1, linestyle='--', color='blue', linewidth=LINEWIDTH)
ax[1].plot(pos, O3p_1 / XO_1, label="O$^{3+}$", linestyle='-', color='green', linewidth=LINEWIDTH)
ax[1].plot(pos, O4p_1 / XO_1, label="O$^{4+}$", linestyle='--', color='crimson', linewidth=LINEWIDTH)
ax[1].plot(pos, O5p_1 / XO_1, label="O$^{5+}$", linestyle='-', color='black', linewidth=LINEWIDTH)
ax[1].plot(pos, O6p_1 / XO_1, color='gray', linestyle='--', linewidth=LINEWIDTH)
ax[1].plot(pos, O7p_1 / XO_1, color='orange', linewidth=LINEWIDTH)
ax[1].plot(pos, O8p_1 / XO_1, color='magenta', linewidth=LINEWIDTH)


# Set x-axis range
ax[0].set_xlim([0.5, 11])
ax[0].legend(fontsize=16, loc="upper right", ncol=1, frameon=False,
             columnspacing=0.15, bbox_to_anchor=(0.4, 0.6))
ax[0].set_ylabel('Ionisation  fraction', fontsize=20)
ax[0].tick_params(axis="both", direction="in", which="both", bottom=True,
                    top=True, left=True, right=True, length=4, labelsize=18)

ax[0].text(6, 0.83, r'O$^{2+}$', fontsize=18)
ax[0].text(6.4, 0.2, r'O$^{3+}$', fontsize=18)
ax[0].text(7.7, 0.53, r'O$^{4+}$', fontsize=18)
ax[0].text(8.4, 0.55, r'O$^{5+}$', fontsize=18)
ax[0].text(8.8, 0.87, r'O$^{6+}$', fontsize=18)

ax[1].set_xlim([4, 10])
ax[1].legend(fontsize=16, loc="upper right", ncol=1, frameon=False,
             columnspacing=0.15, bbox_to_anchor=(0.4, 0.6))
ax[1].set_ylabel('Ionisation  fraction', fontsize=20)
ax[1].set_xlabel('Radius (pc)', fontsize=18)
ax[1].tick_params(axis="both", direction="in", which="both", bottom=True,
                    top=True, left=True, right=True, length=4, labelsize=18)

ax[1].text(6, 0.85, r'O$^{2+}$', fontsize=18)
ax[1].text(7.7, 0.85, r'O$^{8+}$', fontsize=18)
ax[1].text(9.1, 0.85, r'O$^{6+}$', fontsize=18)
ax[1].text(8.6, 0.1, r'O$^{7+}$', fontsize=18)

ax[0].text(4.3, 0.7, 'time = 35 kyr', fontsize=18)
ax[1].text(4.3, 0.7, 'time = 1000 kyr', fontsize=18)

plt.subplots_adjust(left=0.11, right=0.98, top=0.98, bottom=0.1, hspace=0.0)
iy = str(i).zfill(5)
opf = img_path + "NEQ-EQ-Ofrac"+".png"

plt.savefig(opf, dpi=300)
plt.close()



