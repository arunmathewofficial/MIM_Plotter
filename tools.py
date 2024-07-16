# Author: Arun Mathew
# Created: 08-03-2023
# Multi-ion-module-test scripts 

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

    read_data.close()
    open_data.close()

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
    read_data.close()
    return density
# **************************************************************************


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
    read_data.close()
    return temperature
# ***************************************************************************

def get_pressure(silo_file):
    '''
    read the silo file for temperature array

    :param silo_file:
    :return: temperature array
    '''
    read_data = ReadData([silo_file])
    pressure = read_data.get_1Darray("Pressure")['data'][0]
    read_data.close()
    return pressure
# ***************************************************************************

# get radial velocity #######################################################
def get_velocityX(silo_file):
    '''
    read the silo file for temperature array

    :param silo_file:
    :return: temperature array
    '''
    read_data = ReadData([silo_file])
    vx = read_data.get_1Darray("VelocityX")['data'][0]
    read_data.close()
    return vx

def get_MagneticFieldY(silo_file):
    '''
    read the silo file for temperature array

    :param silo_file:
    :return: temperature array
    '''
    read_data = ReadData([silo_file])
    By = read_data.get_1Darray('MagneticFieldY')['data'][0]
    read_data.close()
    return By

# get tracer data from the given silo file ##################################
def get_tracer(silo_file, tracer):
    '''
    read the silo file for tracer array

    :param silo_file:
    :return: tracer array
    '''
    read_data = ReadData([silo_file])
    tracer_data = read_data.get_1Darray(tracer)['data'][0]
    read_data.close()
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

    read_data.close()
    return tracer_data_list
# ***************************************************************************


# process tracer data (old) ################################################
def old_process_tracer_data(tracer_data_list, norm):

    '''
    process the tracer data list for plotting
    :param tracer_data_list:
    :param norm: this can be array or constant
    :return:
    '''

    processed_tracer_data = []

    # neutral calculation
    neutral_tracer = np.ones_like(tracer_data_list[0])
    zero_vector = np.zeros_like(neutral_tracer)
    for j in range(1, len(tracer_data_list)):
        neutral_tracer -= tracer_data_list[j] / norm

    # correct negative numbers in neutral fraction
    for i in range(np.size(neutral_tracer)):
        neutral_tracer[i] = max(neutral_tracer[i], zero_vector[i])

    tracer_data = neutral_tracer
    processed_tracer_data.append(tracer_data)

    # all other species
    for m in range(1, len(tracer_data_list)):
        tracer_data = tracer_data_list[m] / norm
        processed_tracer_data.append(tracer_data)

    return processed_tracer_data
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

    # all other species
    for m in range(1, len(tracer_data_list)):
        tracer_data = tracer_data_list[m] / norm
        processed_tracer_data.append(tracer_data)

    # top-ion calculation
    topion_tracer = np.ones_like(tracer_data_list[0])
    zero_vector = np.zeros_like(topion_tracer)
    for j in range(1, len(tracer_data_list)):
        topion_tracer -= tracer_data_list[j] / norm

    # correct negative numbers
    for i in range(np.size(topion_tracer)):
        topion_tracer[i] = max(topion_tracer[i], zero_vector[i])

    tracer_data = topion_tracer
    processed_tracer_data.append(tracer_data)

    return processed_tracer_data
# ***************************************************************************


# read table ################################################################
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
# ***************************************************************************

# read charge exchange Mpv10 PIONv3.0 table #################################
def Read_CX_Table(file):
    # Read a line of numbers out of a text file:
    print('Reading data from: ' + file)
    title = []
    info = []
    data = []
    with open(file) as table:
        for line in table:
            row = line.split()
            if row[0] == "------":
                continue
            if row[0] == "--":
                title.append(row)
            elif row[0] == "#":
                info.append(row)
            else:
                data.append(row)


    heading = ' '.join(title[0][index] for index in range(2, 8))
    print("Title: " + heading)
    # get number of reaction
    N_reactions = int(info[4][4].strip())
    print("No of charge exchange reactions:",  N_reactions)

    # get
    Reaction_IDs = info[0][3:3+N_reactions]
    Energy_Defect = info[1][3:3+N_reactions]

    # Extracting data
    temperature = [row[0] for row in data]
    reaction_rate_table = [[row[i] for row in data] for i in range(1, N_reactions+1)]

    return {'N_Reactions': N_reactions, 'Reaction_IDs': Reaction_IDs,
            'Energy_Defect': Energy_Defect, 'Temperature': temperature,
            'Rate_Table': reaction_rate_table}
# ***************************************************************************

# read cloudy file ##########################################################
def read_cloudy(file):
    print('Reading couldy data from:', file)
    data = []

    with open(file) as table:
        for line in table:
            row = line.split()
            if row[0].startswith("#"):
                continue
            else:
                data.append(row)

    columns = {}
    num_columns = len(data[0])

    for i in range(num_columns):
        columns[i] = []

    for row in data:
        for i in range(num_columns):
            try:
                columns[i].append(float(row[i]))
            except ValueError:
                print(f"Warning: Could not convert {row[i]} to float. Storing as string.")
                columns[i].append(row[i])

    return columns

# ***************************************************************************

# Add data to dict ##########################################################
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
# ***************************************************************************

# Read photo cross-section data  ###########################################
def read_xsection_data(filename):
    # Read the content of the text file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Initialize an empty dictionary to store data columns
    data_dict = {}

    # Extract labels from the comments
    for line in lines:
        if line.startswith('#ATTRIBUTE LABEL:'):
            line = line.replace('#ATTRIBUTE LABEL:', '', 1)
            labels = line.split()[1:]  # Splitting by whitespace and removing the '#NAME:' prefix
            labels = ["Bin_Min"] + labels  # Include "Bin_Min" as the first label
            break

    species = labels[2:]  # get all the species

    # Extract data from the lines after the '#DATA:' comment
    data_lines = [line for line in lines if not line.startswith('#')]
    for line in data_lines:
        values = line.split()
        for label, value in zip(labels, values):
            value = float(value)
            if label not in data_dict:
                data_dict[label] = []
            data_dict[label].append(value)

    return {"species": species, "names": labels, "dict" :data_dict}
# ***************************************************************************    



def detect_shock (temperature):

    for i in range(len(temperature)):
        if (temperature[i] - temperature[i+1]>1e+1):
            return i