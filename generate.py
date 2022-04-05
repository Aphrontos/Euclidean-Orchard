# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 23:48:35 2022

@author: USER
"""

import png #pip install pypng
import numpy
from primesieve import nth_prime #pip install primesieve

def generate_primes(size):
    primes = numpy.full(size, 0, dtype = int)
    for i in range(size):
        primes[i] = nth_prime(i+1)
    
    return primes

# Generate the data

def generate_data(primes, height = None, width = None):
    data = numpy.full((height, width), 0, dtype = int)
    marked = numpy.full(width, False, dtype = bool)
        
    for j in range(height):
        p = primes[j]
        for i in range(width):
            if   i % p != 0 or  marked[i]:
                data[j, i] = 0
            elif i % p == 0 and i > p:
                data[j, i] = 1
                marked[i] = True
                
    for j in range(height):
        data[j, primes[j]] = 2
            
    return data

# Gashler M. (2019, April 16) Creating a PNG file in Python
#	Retrieved March 20 2022, from https://stackoverflow.com/a/55715162/15043016
# Generate the png

def generate_png(data):
    height = data.shape[0] # number of rows
    width  = data.shape[1] # number of columns
    
    img = []
    palette = [(0x18, 0x46, 0x46),
               (0x47, 0xEF, 0x91),
               (0xFF, 0x00, 0x00)]
    
    for y in range(height):
        row = ()
        for x in range(width):
            row += palette[data[y, x]]
        img.append(row)
    
    with open('sieve.png', 'wb') as f:
        w = png.Writer(width, height, greyscale=False)
        w.write(f, img)
        
def main():
    height = 100
    
    primes = generate_primes(height+1)
    print("Generated the primes")
    
    width = primes[height] ** 2
    
    data = generate_data(primes, height, width)
    print("Generated the data")
    
    # This takes a long time because of the width needed
    # to show the trend
    generate_png(data)
    print("Generated the PNG")
    
if __name__ == "__main__":
    main()
