#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
This module contains the Plot_Functions class which is used to plot the simulation data.

The Plot_Functions class contains methods for plotting the simulation data in different ways.

The class is initialized with the path to the simulation data, the desired fluid quantity, the
tolerance for the colorbar, the coordinate plane, and the image directory. 

The class then finds the dimensions of the simulation and creates a directory for the images. 

The class can also be used to make movies of the simulation
data. The class can also be used to plot the orbital phase of the simulation data. 

2024 - JM modified to limit to only 2D simulations, and added Arun Mathew's 2D plot
       functions
"""

__author__ = "Thomas Jones"

# Import the relevant standard packages ###############################
import os
import re
import numpy as np
from astropy import units as unit
import matplotlib.pyplot as plt
from matplotlib import ticker
import glob
import moviepy.video.io.ImageSequenceClip
from pypion.ReadData import ReadData
#plt.style.use("science")
import matplotlib
matplotlib.use('Agg')
from matplotlib.colorbar import Colorbar
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib.ticker import MultipleLocator
import matplotlib.cm as cm


###########################################################################
# Plot functions for different dimensions.
class Plot_Functions:
    quantity_dict = {'Density':r'$\rho$', 'Temperature':"T", 'Velocity': "v", 'Tr000_WIND': "Wind Tracer"}
    unit_dict = {'Density': "$g \, cm^{-3}$", 'Temperature': "K", 'Velocity': "$cm \, s^{-1}$", "Tr000_WIND": ""}

    def __init__(self, path, basename, image_dir):
        ########### Defining path to SILO files #######################
        self.data_path = path
        if os.path.exists(path):
            print(f"Chosen datapath: {path}")
        else:
            print(f"Directory does not exist: {path}")
            exit()
            
        ########### Base name of SILO files ############################
        # _ = os.listdir(path)
        # _= sorted([f for f in _ if f.endswith('.silo')])
        # self.filename=(_[0]).replace('_level00_0000.00000000.silo','')
        # # self.filename=sorted(os.listdir(self.data_path))[4].replace('_level00_0000.00000000.silo','')
        self.filename = basename
        print(self.filename)

        ########### Make snapshots of the simulation ###################
        self.evolution = self.make_snapshots(self.data_path, self.filename)

        ########### Find the dimensions of the simulation ##############
        self.find_dimensions()
        
        ########### Create image directory #############################
        self.ImageDir = self.create_image_dir(image_dir, self.filename, "Oxygen", "ZR")

        ######### Defining default fps for mp4 ##########
        self.fps=10

    @staticmethod
    def make_snapshots(data_path, filename):
        ########## Cataloging silo files ###############################
        # os.chdir(data_path)
        file_list = glob.glob(os.path.join(data_path, f'{filename}*.silo'), recursive=True)
        level_list = []
        files = []

        for file in file_list:
            level = re.search('_level(.*)_', file)
            if level == None:
                pass
            else:
                level = level.group(1)
                if not level in level_list:
                    level_list.append(level)
        level_list.sort()

        ########## Categorizing data files into levels #################
        if len(level_list) == 1: 
            print('Simulation Info: Single level')
            catalog = []
            files = sorted(glob.glob(filename + '_0000.*.silo'))
            catalog.append(files)
        else:
            print(f'Simulation Info: {len(level_list)} levels')
            catalog = []
            len_level_list = []
            for i in range(len(level_list)):
                files = sorted(glob.glob(os.path.join(data_path, f"{filename}_level{level_list[i]}_0000.*.silo")))
                len_level_list.append(len(files))
                catalog.append(files)

        for i in range(len(catalog)):
            catalog[i] = catalog[i][0:min(len_level_list)]

        # for i in range(len(catalog)):
        #     print(f"Level {i}: {len(catalog[i])} files")

        # Bundle silo files of different levels of same time instant into a snapshot.
        evolution = np.array(catalog).T
        print(f"Shape of evolution array: {evolution.shape}")
        return evolution

    def find_dimensions(self):
        # Looking inside the simulation file for dimensions.
        info = ReadData(self.evolution[0])
        N_grids = info.ngrid()
        self.N_dims = 0
        for j in range(len(N_grids)):
            if N_grids[j] > 1: self.N_dims += 1
        print(f'Simulation Info: {self.N_dims}D System')

    @staticmethod
    def create_image_dir(img_dir, *args):
        ImageDir = os.path.join(img_dir, f'SimulationPlots/{args[0]}/{args[1]}/{args[2]}')

        if not os.path.exists(ImageDir):
            os.makedirs(ImageDir)
            print("Image directory", ImageDir,  "created.")
        else:
            print("Image directory", ImageDir, "already exists.")
        return ImageDir


    #########################################################################################
    # ----------- Two parameters 2D Plotter
    def TwoDPlotter_Double(self, axis_labels, variable_1, variable_2):

        # ------- Plotting parameter_1 on the upper panel
        parameter_1 = variable_1[0]
        x_axis_label = axis_labels[0]
        y_axis_label = axis_labels[1]
        max_colorbar_1 = variable_1[1]
        min_colorbar_1 = variable_1[2]
        colormap_1 = variable_1[3]
        ########### Define desired fluid quantity ######################
        self.Quantity1 = parameter_1
        print(f"Fluid quantity: {self.Quantity1}")
        self.limits1 = [min_colorbar_1,max_colorbar_1]
        print(f"vmin: {self.limits1[0]} \nvmax: {self.limits1[1]}")

        # -------- Plotting parameter_2 on the lower panel
        parameter_2 = variable_2[0]
        max_colorbar_2 = variable_2[1]
        min_colorbar_2 = variable_2[2]
        colormap_2 = variable_2[3]

        ########### Define desired fluid quantity ######################
        self.Quantity2 = parameter_2
        print(f"Fluid quantity: {self.Quantity2}")
        self.limits2 = [min_colorbar_2,max_colorbar_2]
        print(f"vmin: {self.limits2[0]} \nvmax: {self.limits2[1]}")


        # print(self.evolution)
        # Loop over snapshots
        for k in range(0, len(self.evolution), 1):

          data = ReadData(self.evolution[k])
          N_level = data.nlevels()
          N_grids = data.ngrid()
          D1 = data.get_2Darray(self.Quantity1)
          data_1 = D1['data']
          dims_max_1 = (D1['max_extents'] * unit.cm).to(unit.pc)
          dims_min_1 = (D1['min_extents'] * unit.cm).to(unit.pc)
          time =(D1['sim_time']* unit.s).to(unit.kyr)


          # 2 rows, 4 columns
          fig1, axs1 = plt.subplots(2, 1, figsize=(8, 6))

          


          D2 = data.get_2Darray(parameter_2)
          data_2 = D2['data']
          dims_max_2 = (D2['max_extents'] * unit.cm).to(unit.pc)
          dims_min_2 = (D2['min_extents'] * unit.cm).to(unit.pc)

          ax_1 = axs1[0]
          ax_1.text(0.05, 0.9,'time = %5.2f kyr' % time.value, transform=ax_1.transAxes, fontsize=14)
          ax_1.set_xlim(dims_min_1[0][0].value, dims_max_1[0][0].value)
          ax_1.set_ylim(dims_min_1[0][1].value, dims_max_1[0][1].value)

          for l in range(len(data_1)):
            plot_data = np.log10(data_1[l])
            extents = [dims_min_1[l][0].value, dims_max_1[l][0].value,
                       dims_min_1[l][1].value, dims_max_1[l][1].value]
            image_1 = ax_1.imshow(plot_data, interpolation='nearest',
                              cmap=colormap_1, extent=extents, origin='lower', 
                              vmax=max_colorbar_1, vmin=min_colorbar_1)

          divider1 = make_axes_locatable(ax_1)  # Create divider for existing axes instance.
          cax_1 = divider1.append_axes("right", size="5%", pad=0.05)  # Append axes to the right of ax1.
          plt.colorbar(image_1, cax=cax_1, ticks=MultipleLocator(1),
                             format="%.1f")  # Create colorbar in the appended axes.
          ax_1.text(0.65, 0.9, r'$\log(\rho / \mathrm{g\,cm}^{-3})$', transform=ax_1.transAxes, fontsize=14)
          ax_1.tick_params(axis='both', which='major', labelsize=13)
          ax_1.axes.get_xaxis().set_visible(False)  # Remove the x-axis.


          # -------- Plotting parameter_2 on the lower panel
          ax_2 = axs1[1]
          ax_2.set_xlim(dims_min_2[0][0].value, dims_max_2[0][0].value)
          ax_2.set_ylim(-dims_max_2[0][1].value, -dims_min_2[0][1].value)

          for l in range(len(data_2)):
            plot_data = np.log10(data_2[l])
            extents = [dims_min_2[l][0].value, dims_max_2[l][0].value,
                      -dims_max_2[l][1].value, -dims_min_2[l][1].value]

            image_2 = ax_2.imshow(plot_data, interpolation='nearest', cmap=colormap_2,
                              extent=extents, vmax=max_colorbar_2, vmin=min_colorbar_2)

          divider2 = make_axes_locatable(ax_2)
          cax_2 = divider2.append_axes("right", size="5%", pad=0.05)
          plt.colorbar(image_2, cax=cax_2, ticks=MultipleLocator(1), format="%.1f")
          ax_2.text(0.65, 0.05, r'$\log(T / \mathrm{K})$', transform=ax_2.transAxes, color='white', fontsize=14)
          ax_2.set_xlabel('     '+x_axis_label+' (pc)', fontsize=16)
          ax_2.tick_params(axis='both', which='major', labelsize=13)
          ax_2.set_ylabel('                                              '+y_axis_label+' (pc)', fontsize=16)

          fig1.subplots_adjust(wspace=0, hspace=0)  # Remove the whitespace between the images
          plt.savefig(f"{self.ImageDir}/{self.filename}_{str(k).zfill(3)}_rhoT.png", bbox_inches="tight", dpi=500)
          plt.close(fig1)
          print(f'Time: {time:.2e}.',
                f'Saving snap-{str(k)} to {self.filename}_{str(k).zfill(3)}_rhoT.png ...')
        
          '''

          fig2, axs2 = plt.subplots(2, 3, figsize=(16, 5))


          EL = np.array(data.get_2Darray("Tr004_X_O")['data'])
          D3 = data.get_2Darray("Tr026_O1p")
          data3 = np.array(D3['data'])
          O1p = data3 / EL
          D4 = data.get_2Darray("Tr027_O2p")
          data4 = np.array(D4['data'])
          O2p = data4/EL
          D5 = data.get_2Darray("Tr028_O3p")
          data5 = np.array(D5['data'])
          O3p = data5 / EL
          D6 = data.get_2Darray("Tr029_O4p")
          data6 = np.array(D6['data'])
          O4p = data6/EL
          D7 = data.get_2Darray("Tr030_O5p")
          data7 = np.array(D7['data'])
          O5p = data7 / EL
          D8 = data.get_2Darray("Tr031_O6p")
          data8 = np.array(D8['data'])
          O6p = data8/EL
          D9 = data.get_2Darray("Tr032_O7p")
          data9 = np.array(D9['data'])
          O7p = data9/EL

          ax1 = axs2[0, 0]
          ax1.text(0.55, 0.9, r'O$^{2+}$ ion fraction', transform=ax1.transAxes, fontsize=14)
          ax1.text(0.05, 0.9,'time = %5.2f kyr' % time.value, transform=ax1.transAxes, fontsize=14)
          ax1.set_xlim(dims_min_1[0][0].value, dims_max_1[0][0].value)
          ax1.set_ylim(dims_min_1[0][1].value, dims_max_1[0][1].value)
          ax1.tick_params(axis='both', which='major', labelsize=13)
          ax1.axes.get_xaxis().set_visible(False)  # Remove the x-axis.

          ax2 = axs2[1, 0]
          ax2.text(0.55, 0.05, r'O$^{3+}$ ion fraction', color='white', transform=ax2.transAxes, fontsize=14)
          ax2.set_xlim(dims_min_1[0][0].value, dims_max_1[0][0].value)
          ax2.set_ylim(-dims_max_1[0][1].value, -dims_min_1[0][1].value)
          ax2.set_xlabel('   '+x_axis_label+' (pc)', fontsize=16)
          ax2.tick_params(axis='both', which='major', labelsize=13)
          ax2.set_ylabel('                                    '+y_axis_label+' (pc)', fontsize=16)


          ax3 = axs2[0, 1]
          ax3.text(0.55, 0.9,r'O$^{4+}$ ion fraction', color='white', transform=ax3.transAxes, fontsize=14)
          ax3.set_xlim(dims_min_1[0][0].value, dims_max_1[0][0].value)
          ax3.set_ylim(dims_min_1[0][1].value, dims_max_1[0][1].value)
          ax3.tick_params(axis='both', which='major', labelsize=13)
          ax3.axes.get_xaxis().set_visible(False)  # Remove the x-axis.

          ax4 = axs2[1, 1]
          ax4.text(0.55, 0.05,r'O$^{5+}$ ion fraction', color='white', transform=ax4.transAxes, fontsize=14)
          ax4.set_xlim(dims_min_1[0][0].value, dims_max_1[0][0].value)
          ax4.set_ylim(-dims_max_1[0][1].value, -dims_min_1[0][1].value)
          ax4.tick_params(axis='both', which='major', labelsize=13)
          ax4.set_xlabel('   '+x_axis_label+' (pc)', fontsize=16)

          ax5 = axs2[0, 2]
          ax5.text(0.55, 0.9, r'O$^{6+}$ ion fraction', color='white', transform=ax5.transAxes, fontsize=14)
          ax5.set_xlim(dims_min_1[0][0].value, dims_max_1[0][0].value)
          ax5.set_ylim(dims_min_1[0][1].value, dims_max_1[0][1].value)
          ax5.tick_params(axis='both', which='major', labelsize=13)
          ax5.axes.get_xaxis().set_visible(False)  # Remove the x-axis.

          ax6 = axs2[1, 2]
          ax6.text(0.55, 0.05, r'O$^{7+}$ ion fractions', color='white', transform=ax6.transAxes, fontsize=14)
          ax6.set_xlim(dims_min_1[0][0].value, dims_max_1[0][0].value)
          ax6.set_ylim(-dims_max_1[0][1].value, -dims_min_1[0][1].value)
          ax6.tick_params(axis='both', which='major', labelsize=13)
          ax6.set_xlabel('   '+x_axis_label+' (pc)', fontsize=16)

          for l in range(len(O1p)):
            extents = [dims_min_1[l][0].value, dims_max_1[l][0].value,
                       dims_min_1[l][1].value, dims_max_1[l][1].value]
            image_1 = ax1.imshow(O2p[l], interpolation='nearest',
                              cmap="magma", extent=extents, origin='lower',
                              vmax=1, vmin=0)
            #divider_1 = make_axes_locatable(ax1)  # Create divider for existing axes instance.
            #cax_1 = divider_1.append_axes("right", size="5%", pad=0.05)  # Append axes to the right of ax1.
            #plt.colorbar(image_1, cax=cax_1, ticks=MultipleLocator(1), format="%.1f")

            image_3 = ax3.imshow(O4p[l], interpolation='nearest',
                              cmap="magma", extent=extents, origin='lower',
                              vmax=1, vmin=0)
            #divider_3 = make_axes_locatable(ax3)  # Create divider for existing axes instance.
            #cax_3 = divider_3.append_axes("right", size="5%", pad=0.05)  # Append axes to the right of ax1.
            #plt.colorbar(image_3, cax=cax_3, ticks=MultipleLocator(1), format="%.1f")

            image_5 = ax5.imshow(O6p[l], interpolation='nearest',
                              cmap="magma", extent=extents, origin='lower',
                              vmax=1, vmin=0)
            #divider_5 = make_axes_locatable(ax5)  # Create divider for existing axes instance.
            #cax_5 = divider_5.append_axes("right", size="5%", pad=0.05)  # Append axes to the right of ax1.
            #plt.colorbar(image_5, cax=cax_5, ticks=MultipleLocator(1), format="%.1f")

            extents = [dims_min_1[l][0].value, dims_max_1[l][0].value,
                      -dims_max_1[l][1].value, -dims_min_1[l][1].value]

            image_2 = ax2.imshow(O3p[l], interpolation='nearest', cmap="magma",
                              extent=extents, vmax=1, vmin=0)
            #divider_2 = make_axes_locatable(ax2)  # Create divider for existing axes instance.
            #cax_2 = divider_2.append_axes("right", size="5%", pad=0.05)  # Append axes to the right of ax1.
            #plt.colorbar(image_2, cax=cax_2, ticks=MultipleLocator(1), format="%.1f")

            # Plot the first image
            image_4 = ax4.imshow(O5p[l], interpolation='nearest', cmap="magma",
                                 extent=extents, vmax=1, vmin=0)

            # Plot the second image
            image_6 = ax6.imshow(O7p[l], interpolation='nearest', cmap="magma",
                                 extent=extents, vmax=1, vmin=0)

            # Create a common color bar
            #divider = make_axes_locatable(ax6)  # Use one axis (e.g., ax6) to append the color bar
            #cax = divider.append_axes("right", size="5%", pad=0.05)  # Append axes to the right

            # Set a common color bar for both images
            #plt.colorbar(image_6, cax=cax, ticks=MultipleLocator(1), format="%.1f")



          fig2.subplots_adjust(wspace=0, hspace=0, right=.99)  # Remove the whitespace between the images
          # Create a common color bar
          divider = make_axes_locatable(ax6)  # Using ax6 to append the color bar
          #divider.append_axes("right", size="5%", pad=0.05)
          cax = fig2.add_axes([0.99, 0.11, 0.015, 0.77])  # Add the colorbar axes to fig2
          plt.colorbar(image_6, cax=cax, ticks=[0, 0.25, 0.5, 0.75, 1], format="%.2f")




          plt.savefig(f"{self.ImageDir}/{self.filename}_{str(k).zfill(3)}_ionfrac.png",
                      bbox_inches="tight", dpi=500)
          plt.close(fig2)
          print(f'Time: {time:.2e}.',
                f'Saving snap-{str(k)} to {self.filename}_{str(k).zfill(3)}_ionfrac.png ...')

          '''
