# Author: Arun Mathew
# Created: 08-03-2023
# Multi-ion-module-publication plots:

# New comments:
# 2022-11-09 AM: scripted H and He OneDGrid_Plotter
# 2022-11-10 AM: scripted C, O, N OneDGrid_Plotter

# Import required libraries: ##########################################
import warnings
import numpy as np
from pypion.ReadData import ReadData
from pypion.SiloHeader_data import OpenData
import astropy.units as unit
import os



# Making Output directory ################################################
def make_directory(dir_name):
    OutputDir = dir_name
    # Create target Directory
    try:
        os.mkdir(OutputDir)
        print("Output directory:", OutputDir, "created.")
    except FileExistsError:
        # If already exist, the pass.
        print("Output directory", OutputDir, "already exists.")
        pass

    if not OutputDir.endswith('/'):
        OutputDir += "/"

    return OutputDir
# *************************************************************************



# get basic data from the silo file ######################################
def get_basic_data(silo_file):
    '''
    read basic data from the silo file

    :param silo_file:
    :return: basic datas
    '''

    read_data = ReadData([silo_file])
    open_data = OpenData([silo_file])

    basic_data = read_data.get_1Darray("Density")
    xmax = (basic_data['max_extents'] * unit.cm)
    xmin = (basic_data['min_extents'] * unit.cm)
    sim_time = (basic_data['sim_time'] * unit.s).to(unit.kyr)

    n_grid = open_data.ngrid()
    n_dim = open_data.ndim()
    if not n_dim == 1:
        warnings.warn(
            message="Not 1D problem, use 1D silo file instead.", stacklevel=2)

    delta_x = (xmax - xmin) / n_grid
    xmin = xmin[0]
    xmax = xmax[0]
    ngrid_x = n_grid[0]
    dx = delta_x[0]
    x0 = xmin[0] + 0.5 * dx[0]
    xn = xmax[0] - 0.5 * dx[0]
    xdata = np.linspace(x0, xn, ngrid_x)

    return {'xmax': xmax, 'xmin': xmin, 'x': xdata, 'ngrid': n_grid, 'time': sim_time}
# **************************************************************************


# get density from the silo file ######################################
def get_density(silo_file):
    '''
    read basic data from the silo file

    :param silo_file:
    :return: basic datas
    '''

    read_data = ReadData([silo_file])
    density = read_data.get_1Darray("Density")['data'][0]
    return density
# **************************************************************************


    return {'xmax': xmax, 'xmin': xmin, 'x': xdata, 'ngrid': n_grid, 'time': sim_time}
# **************************************************************************



# get temperature data from the given silo file ###########################
def get_temperature(silo_file):
    '''
    read the silo file for temperature array

    :param silo_file:
    :return: temperature array
    '''
    read_data = ReadData([silo_file])
    temperature = read_data.get_1Darray("Temperature")['data'][0]
    return temperature
# ***************************************************************************

def get_velocityX(silo_file):
    '''
    read the silo file for temperature array

    :param silo_file:
    :return: temperature array
    '''
    read_data = ReadData([silo_file])
    vx = read_data.get_1Darray("VelocityX")['data'][0]
    return vx

# get tracer data from the given silo file ##################################
def get_tracer(silo_file, tracer):
    '''
    read the silo file for tracer array

    :param silo_file:
    :return: tracer array
    '''
    read_data = ReadData([silo_file])
    tracer_data = read_data.get_1Darray(tracer)['data'][0]
    return tracer_data
# ***************************************************************************


# get tracer data from the given silo file ##################################
def get_tracers(silo_file, tracer_list):
    '''
    read the silo file for tracer array

    :param silo_file:
    :return: tracer array
    '''
    read_data = ReadData([silo_file])

    tracer_data_list = []
    for i in range(len(tracer_list)):
        tracer_name = tracer_list[i]
        tracer_data = read_data.get_1Darray(tracer_name)['data'][0]
        tracer_data_list.append(tracer_data)

    return tracer_data_list
# ***************************************************************************


# process tracer data before pplotting ######################################
def process_tracer_data(tracer_data_list, norm):
    '''
    process the tracer data list for plotting
    :param tracer_data_list:
    :param norm: this can be array or constant
    :return:
    '''

    processed_tracer_data = []
    for m in range(len(tracer_data_list)):

        if m == 0:
            neutral_tracer = tracer_data_list[0] / norm
            for j in range(1, len(tracer_data_list)):
                neutral_tracer -= tracer_data_list[j] / norm

            zero_vector = np.zeros_like(neutral_tracer)
            # checking for negative number
            for i in range(np.size(neutral_tracer)):
                neutral_tracer[i] = max(neutral_tracer[i], zero_vector[i])

            tracer_data = neutral_tracer

        else:
            non_neutral_tracers = tracer_data_list[m] / norm
            tracer_data = non_neutral_tracers

        processed_tracer_data.append(tracer_data)

    return processed_tracer_data
# ***************************************************************************



def ReadTable_Advance(Table):
    # Read a line of numbers out of a text file:
    print('Reading tabulated data: ' + Table)
    # count number of rows and columns and
    # store entire table data in 2D vector.
    N_row = 0
    N_col = 0
    data = []
    with open(Table) as table:
        for line in table:
            row = line.split()
            if row[0] == "#":
                continue
            else:
                N_row += 1
                N_col  = len(row)
                row = np.asarray(row, dtype=float)
                data.append(row)

    #Create N_col arrays
    columns = [[] for _ in range(N_col)]
    #Append corresponding data into each columns
    for col in range(N_col):
        for row in range(N_row):
            columns[col].append(data[row][col])

    return {'N_row': N_row, 'N_col': N_col, 'columns': columns}



def add_data_to_dict(dict, column_data, column_name):

    '''
    This function will update dict with given data and
    return the dict
    :param dict:
    :param column_data: given data
    :param column_name: name of the data
    :return: dict
    '''

    # if column data is in perfect array format
    if isinstance(column_data, np.ndarray):
        if column_data.ndim == 1:
            dict[column_name] = column_data

        if column_data.ndim > 1 :
            for i in range(len(column_data)):
                dict[column_name[i]] = column_data[i]

    # If column data is not in array format
    if not isinstance(column_data, np.ndarray):
        if len(column_data) > 1:
            for i in range(len(column_data)):
                dict[column_name[i]] = column_data[i]

    return dict