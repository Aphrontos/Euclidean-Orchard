import zlib
import struct
import numpy
from math import gcd

# Generate the data

def generateData(data, height = None, width = None):
    if height is None:
        height = data.shape[0] # number of rows
    if width is None:
        width = data.shape[1] # number of columns
				
    for j in range(height):
        for i in range(width):
            if gcd(j, i) == 1:
                data[j, i] = 0

# Draheim, G. U. (2014, September 14). Creating a PNG file in Python. 
#	Retrieved July 27, 2020, from https://stackoverflow.com/a/25835368
# Generate the PNG

def generatePNG(data, name, height = None, width = None):
    def I1(value):
        return struct.pack("!B", value & (2**8-1))
    def I4(value):
        return struct.pack("!I", value & (2**32-1))
    # compute width & height from data if not explicit
    if height is None:
        height = data.shape[0] # number of rows
    if width is None:
        width = data.shape[1] # number of columns
    # generate these chunks depending on image type
    makeIHDR = True
    makeIDAT = True
    makeIEND = True
    png = b"\x89" + "PNG\r\n\x1A\n".encode('ascii')
    if makeIHDR:
        colortype = 0 # true gray image (no palette)
        bitdepth = 8 # with one byte per pixel (0 to 255)
        compression = 0 # zlib (no choice here)
        filtertype = 0 # adaptive (each scanline seperately)
        
        interlaced = 0 # no
        IHDR = I4(width) + I4(height) + I1(bitdepth)
        IHDR += I1(colortype) + I1(compression)
        IHDR += I1(filtertype) + I1(interlaced)
        block = "IHDR".encode('ascii') + IHDR
        png += I4(len(IHDR)) + block + I4(zlib.crc32(block))
    if makeIDAT:
        raw = b""
        for y in range(height):
            raw += b"\0" # no filter for this scanline
            for x in range(width):
                c = b"\0" # default black pixel
                if y < len(data) and x < len(data[y]):
                    c = I1(data[y][x])
                raw += c
        compressor = zlib.compressobj()
        compressed = compressor.compress(raw)
        compressed += compressor.flush() #!!
        block = "IDAT".encode('ascii') + compressed
        png += I4(len(compressed)) + block + I4(zlib.crc32(block))
    if makeIEND:
        block = "IEND".encode('ascii')
        png += I4(0) + block + I4(zlib.crc32(block))
    open(name + ".png","wb").write(png)
    
height = input("height: ")
width = input("width: ")
name = input("name: ")

data = numpy.full((height, width), 255, dtype = int)

generateData(data, height, width)
generatePNG(data, name, height, width)
