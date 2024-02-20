# Code to data fit an defined functions with arbitrary parameters.
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from tools import *
import math

plot_dir =make_directory('INAM_2023')

# Define the exponential decay function
def exponential_decay(x, a, b, c):
    return a * pow(x, b)




# Data
x_data = np.array([4.948453608247423, 6.804123711340207, 9.81958762886598, 16.469072164948454, 24.27835051546392, 33.09278350515464, 43.608247422680414, 57.98969072164949, 74.30412371134021, 100.43814432989691])
y_data = np.array([1.5790953412784399, 0.5782854821235103, 0.4099918743228602, 0.2524404117009751, 0.17903575297941496, 0.14322860238353197, 0.11816359696641388, 0.09667930660888407, 0.08772751895991333, 0.07698537378114843])

# Fit the data using curve_fit
initial_guess = [1.0, 0.01, 0.0]  # Initial guess for the parameters
fit_params, _ = curve_fit(exponential_decay, x_data, y_data, p0=initial_guess)

# Extract the fitted parameters
a_fit, b_fit, c_fit = fit_params

# Generate the fitted curve using the fitted parameters
y_fit = exponential_decay(x_data, a_fit, b_fit, c_fit)

# Plot the original data and the fitted curve
plt.scatter(x_data, y_data, label='Original Data')
plt.plot(x_data, y_fit, label='Fitted Curve', color='red')
plt.xlabel('ntracers')
plt.ylabel('normalize cell update speed')
plt.legend()


plt.savefig(plot_dir + 'curve_fitting.png', dpi=300)

print("Fitted Parameters:")
print("a =", a_fit)
print("b =", b_fit)
print("c =", c_fit)
