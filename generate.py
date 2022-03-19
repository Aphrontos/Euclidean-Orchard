# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 23:48:35 2022

@author: USER
"""

import png
import numpy
from primesieve import nth_prime
from math import log

# Generate the data

def generate_data(height = None, width = None):
    p = 0
    data = numpy.full((height, width), 0, dtype = int)
    isMarked = numpy.full(width, False, dtype = bool)
    for j in range(height):
        p = nth_prime(j + 1)
        for i in range(width):
            if i % p != 0 or isMarked[i] :
                data[j, i] = 0
            elif i % p == 0  and i > 0:
                data[j, i] = 1
                isMarked[i] = True
            
    return data

# Gashler M. (2019, April 16) 
#	Retrieved March 20 2022, from https://stackoverflow.com/a/55715162/15043016
# Generate the png

def generate_png(data):
    height = data.shape[0] # number of rows
    width = data.shape[1] # number of columns
    
    img = []
    for y in range(height):
        row = ()
        for x in range(width):
            if data[y, x] == 0 :
                row = row + (0x18, 0x46, 0x46)
            elif data[y, x] == 1 :
                row = row + (0x47, 0xEF, 0x91)
        img.append(row)
    with open('gradient.png', 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)
    
if __name__ == "__main__":
    height = 10 # make sure this is small
    width = round(height ** 2 * log(height))
	
    data = generate_data(height, width)
    generate_png(data)
