from matplotlib import pyplot as pp
import numpy as np
import txtreader
#wavelength, flux = 
#print(txtreader.readtxt('stelib_spec_txt_HD102212_moy.txt'))

wavelength, flux = txtreader.readtxt('stelib_spec_txt_HD95735_moy.txt') 
txtreader.save_to_csv(wavelength, flux, 'HD95735.csv')
