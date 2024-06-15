import numpy as np
import matplotlib.pyplot as plt 
def readtxt(file):
#Load data from txt; numpy should handle white space automatically 
    data=np.loadtxt(file,delimiter=None)
#two arrays; stack to get a 2D array "data"
    wavelength=data[:,0]
    flux=data[:,1]
    return(wavelength,flux)

def save_to_csv(wavelength, flux, filename):
    # Combine wavelength and flux into a single 2D array
    data_to_save = np.column_stack((wavelength, flux))
    
    # Save the combined array to a CSV file
    # fmt specifies the format: '%.18e' for scientific notation
    # delimiter ',' is for CSV files
    np.savetxt(filename, data_to_save, delimiter=',', header='Wavelength,Flux', comments='', fmt='%.18e')



