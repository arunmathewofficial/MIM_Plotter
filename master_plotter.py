# Python Script for General Plotter
# *********************************

# Author: Arun Mathew
# Created: 2023-03-07
# General Plotter: A master one dimensional plotter for publications

# New comments:
# 2023-03-07 Arun Mathew: Input the data and tell the plotter
# where and how to plot it.
# 2023-03-07 Arun Mathew:


# Required libraries:
from pypion.ReadData import ReadData
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import astropy.units as unit
#from labellines import labelLines
from matplotlib.ticker import (MultipleLocator, AutoMinorLocator)
import warnings
from cycler import cycler

plt.rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
plt.rc('text', usetex=True)
plt.rc('font',**{'size': 12})
plt.rc('lines', linewidth=1.25)

plt.rcParams["font.weight"] = "normal"
from matplotlib.font_manager import FontProperties

'''
font = FontProperties()
font.set_family('sans-serif')
font.set_name('stixsans')
font.set_style('italic')
font.set_weight('light')
font.set_size(8)
'''

# plot indexing function =========================================================================
# plot indexing 2D function
def plot_indexing_2Dfunc(plot_index, row_index, col_index, fig_index, nrows, ncols, force_plotting):
    # forced plotting
    if not force_plotting == None:
        Found = False
        # Since this function set table index for next plot. We shall look
        # for the plot_index in the force_plotting array.
        for i in range(len(force_plotting)):
            if plot_index + 1 == force_plotting[i][0] - 1:
                row_index = force_plotting[i][1] - 1
                col_index = force_plotting[i][2] - 1
                Found = True
                print('Master Plotter :: forcing plot -', plot_index + 2,
                      'at (', row_index + 1, ',', col_index + 1,')')
                break

        if Found == False:
            fig_index += 1
            if col_index == ncols - 1:
                row_index += 1
                col_index = 0  # increment row index if column index hit ncols-1
            else:
                col_index += 1  # if not increment the column index

    # if force_plotting = None, follow the default setting #########################
    if force_plotting == None:
        fig_index += 1
        if col_index == ncols - 1:
            row_index += 1
            col_index = 0  # increment row index if column index hit ncols-1
        else:
            col_index += 1  # if not increment the column index

    return row_index, col_index, fig_index


# plot indexing 1D function
def plot_indexing_1Dfunc(plot_index, total_fig, fig_index, force_plotting_1d):
    # forced plotting
    if not force_plotting_1d == None:
        Found = False
        # Since this function set table index for next plot. We shall look
        # for the plot_index in the force_plotting array.
        for i in range(len(force_plotting_1d)):
            if plot_index + 1 == force_plotting_1d[i][0] - 1:
                fig_index = force_plotting_1d[i][1] - 1
                Found = True
                print('Master Plotter :: forcing plot 1D -', plot_index + 2,
                      'at', fig_index + 1)
                break

        if Found == False:
            if fig_index < total_fig - 1:
                fig_index += 1  # increment fig_index only up to m

    elif fig_index < total_fig - 1:
        fig_index += 1  # increment fig_index only up to m

    #print(total_fig)
    return fig_index
# end of plot indexing function ===================================================================



def onedim_master_plotter(plot_data, plot_style):

    nrows = plot_style['matrix'][0]
    ncols = plot_style['matrix'][1]
    nplots = nrows*ncols

    # Default setting for fig-size, legend, label_font_size, sharex, sharey, insert-txt
    if not 'figsize' in plot_style.keys(): figsize = (6.4, 4.8)
    else: figsize = plot_style['figsize']
    if not 'legend' in plot_style.keys(): plot_style['legend'] = True
    if not 'label_font_size' in plot_style.keys(): label_font_size = 10
    else: label_font_size = plot_style['label_font_size']
    if not 'sharex' in plot_style.keys(): sharex = False
    else: sharex = plot_style['sharex']
    if not 'sharey' in plot_style.keys(): sharey = False
    else: sharey = plot_style['sharey']
    if not 'insert-txt' in plot_style.keys(): plot_style['insert-txt'] = []

    # Default setting for axis-labels
    if not 'axis-label' in plot_style.keys() or len(plot_style['axis-label']) == 0:
        plot_style['axis-label'] = []
        for i in range(nplots):
            plot_style['axis-label'].append([None, None])

    # Default setting for margins
    if not 'left' in plot_style.keys(): left = None
    else: left = plot_style['left']
    if not 'right' in plot_style.keys(): right = None
    else: right = plot_style['right']
    if not 'top' in plot_style.keys(): top = None
    else: top = plot_style['top']
    if not 'bottom' in plot_style.keys(): bottom = None
    else: bottom = plot_style['bottom']
    if not 'wspace' in plot_style.keys(): wspace = None
    else: wspace = plot_style['wspace']
    if not 'hspace' in plot_style.keys(): hspace = None
    else: hspace = plot_style['hspace']

    # Default setting for x-limits
    if not 'xlimit' in plot_style.keys() or len(plot_style['xlimit']) == 0:
        plot_style['xlimit'] = []
        for i in range(nplots):
            plot_style['xlimit'].append([None, None])

    # Default setting for y-limits
    if not 'ylimit' in plot_style.keys() or len(plot_style['ylimit']) == 0:
        plot_style['ylimit'] = []
        for i in range(nplots):
            plot_style['ylimit'].append([None, None])

    # Default setting for force-plotting
    if not 'force-plotting' in plot_style.keys() or len(plot_style['force-plotting']) == 0:
        force_plotting = None
    else: force_plotting = plot_style['force-plotting']

    # Default setting for force-plotting
    if not 'force-plotting_1d' in plot_style.keys() or len(plot_style['force-plotting_1d']) == 0:
        force_plotting_1d = None
    else: force_plotting_1d = plot_style['force-plotting_1d']


    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize, sharex=sharex, sharey=sharey)

    # one dimensional array ==================================================================
    if nrows==1 or ncols == 1:
        total_fig = max(nrows, ncols)

        # 1. single plot ======================================================================
        if total_fig == 1:
            # loop over plot_data
            for m in range(len(plot_data)):
                # loop over species
                for n in range(len(plot_data[m])):

                    ax.plot(plot_data[m][n]['x'], plot_data[m][n]['y'], label=plot_data[m][n]['labels'])

                    if len(plot_data[m][n]['label-position']) == 2:
                        x_position = plot_data[m][n]['label-position'][0]
                        y_position = plot_data[m][n]['label-position'][1]
                        ax.text(x_position, y_position, plot_data[m][n]['labels'], fontsize=label_font_size)

                ax.xaxis.set_minor_locator(AutoMinorLocator())
                ax.yaxis.set_minor_locator(AutoMinorLocator())
                ax.tick_params(axis="both", direction="in", which="both",
                               bottom=True, top=True, left=True, right=True, length=2)

                if plot_style['legend'] == True: ax.legend(frameon=False)

        # 2. one dimensional multiple plots ===================================================
        else:
            # onedim_index (no of separate figures)
            fig_index = 0 # index of the figure whereas plot_index represents plot index
            # loop over plot_data
            for plot_index in range(len(plot_data)):
                # loop over species
                for n in range(len(plot_data[plot_index])):

                    try:
                        linestyle = plot_data[plot_index][n]['line-style']
                        color = plot_data[plot_index][n]['line-color']
                    except:
                        linestyle = None
                        color = None

                    ax[fig_index].plot(plot_data[plot_index][n]['x'], plot_data[plot_index][n]['y'],
                               label=plot_data[plot_index][n]['labels'],
                               linestyle=linestyle, color=color)

                    if len(plot_data[plot_index][n]['label-position']) == 2:
                        x_position = plot_data[plot_index][n]['label-position'][0]
                        y_position = plot_data[plot_index][n]['label-position'][1]
                        ax[fig_index].text(x_position, y_position, plot_data[plot_index][n]['labels'],
                                   fontsize=label_font_size)

                ax[fig_index].xaxis.set_minor_locator(AutoMinorLocator())
                ax[fig_index].yaxis.set_minor_locator(AutoMinorLocator())
                ax[fig_index].tick_params(axis="both", direction="in", which="both",
                                  bottom=True, top=True, left=True, right=True, length=3)

                ax[fig_index].set_xlim(plot_style['xlimit'][fig_index])
                ax[fig_index].set_ylim(plot_style['ylimit'][fig_index])

                ax[fig_index].set_xlabel(plot_style['axis-label'][fig_index][0], fontsize=14)
                ax[fig_index].set_ylabel(plot_style['axis-label'][fig_index][1], fontsize=14)

                if plot_style['legend'] == True: ax[fig_index].legend(frameon=False)

                #ax[fig_index].legend(['First List', '', 'Second List'], loc='upper left')

                fig_index = plot_indexing_1Dfunc(plot_index, total_fig, fig_index, force_plotting_1d)


    # 3. two dimensional array =================================================================
    else:
         r = 0 # initial position of row
         c = 0 # initial position of col
         fig_index = 0 # initial figure
         # loop over plot_data
         for plot_index in range(len(plot_data)):

             # loop over species
             for n in range(len(plot_data[plot_index])):

                 try: linestyle = plot_data[plot_index][n]['line-style']
                 except: linestyle = None
                 try: color = plot_data[plot_index][n]['line-color']
                 except: color = None
                 try: marker = plot_data[plot_index][n]['line-marker']
                 except: marker = None

                 ax[r, c].plot(plot_data[plot_index][n]['x'], plot_data[plot_index][n]['y'],
                               label=plot_data[plot_index][n]['labels'],
                               linestyle=linestyle, linewidth=2,
                               color=color,
                               marker=marker, markersize=10
                               )

                 if len(plot_data[plot_index][n]['label-position']) == 2:
                     x_position = plot_data[plot_index][n]['label-position'][0]
                     y_position = plot_data[plot_index][n]['label-position'][1]
                     ax[r, c].text(x_position, y_position, plot_data[plot_index][n]['labels'],
                                   fontsize=label_font_size)

             #ax[r, c].xaxis.set_minor_locator(AutoMinorLocator())
             #ax[r, c].yaxis.set_minor_locator(AutoMinorLocator())
             ax[r, c].tick_params(axis="both", direction="in", which="both",
                                  bottom=True, top=True, left=True, right=True,
                                  length=5, width=3, labelsize=15)

             ax[r, c].set_xlabel(plot_style['axis-label'][fig_index][0], fontsize=10)
             ax[r, c].set_ylabel(plot_style['axis-label'][fig_index][1], fontsize=10)

             ax[r, c].set_xlim(plot_style['xlimit'][fig_index])
             ax[r, c].set_ylim(plot_style['ylimit'][fig_index])

             for location in ['left', 'right', 'top', 'bottom']:
                 ax[r, c].spines[location].set_linewidth(2)

             if plot_style['legend'] == True: ax[r, c].legend(frameon=False)

             r, c, fig_index = plot_indexing_2Dfunc(plot_index, r, c, fig_index, nrows, ncols, force_plotting)

    # Insert txt in the figure
    if not len(plot_style['insert-txt']) == None:
        for j in range(len(plot_style['insert-txt'])):
            plt.text(plot_style['insert-txt'][j][1], plot_style['insert-txt'][j][2],
                     plot_style['insert-txt'][j][0], rotation=plot_style['insert-txt'][j][3])

    plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)



    return fig