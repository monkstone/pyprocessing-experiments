"""
Copyright (c) 2011 Martin Prout
 
This example is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
http://creativecommons.org/licenses/LGPL/2.1/
NB: use of numpy does not seem to speed things up, however is probaby more sparing
of system resources (memory in particular)

np_voronoi.py example
"""

from pyprocessing import *
from random import randint
import numpy as np

def setup():
    """
    pyprocessing setup
    """
    size(400,  300)
    n = randint(40, 60) # number of cells
    nx = np.random.randint(width, size=(n))      # numpy does randint(low, high) but high is excluded
    ny = np.random.randint(height, size= (n))   # if high = None, like here low defaults to randint(0, low)
    nh = np.random.randint(256, size=(4,  n))
    #ncolor = np.zeros((n),  dtype=np.uint64)                       # on a 64 bit system it pays to specify 32 bits
    nimage = np.zeros((width * height,  3),  dtype=np.uint)
#    for i in xrange(n)32
#        ncolor[i] = 255<<24|nh[0][i]<<16|nh[1][i]<<8|nh[2][i]

    for y in xrange(height):
        min = 0 if (y < 0.5 * height) else int(n * 0.1)           # slight speedup if don't need to check  
        max = int(n * 0.5) if (y < 0.13 * height) else n        # every single particle center each time
        for x in xrange(width):
            # find the closest cell center
            dmin = hypot_squared(width - 1, height - 1)                       # more intelligible version
            #dmin = ((width - 1) * (width - 1)) + ((height - 1) * (height - 1))  # optimized version?
            j = -1
            for i in xrange(min,  max):
                d = hypot_squared((nx[i] - x),  (ny[i] - y))                  # more intelligible version
                #d = ((nx[i] - x) * (nx[i] - x)) + ((ny[i] - y) * (ny[i] - y))  # optimized version?
                if d < dmin:
                    dmin = d
                    j = i
                    nimage[width * y + x][0],  nimage[width * y + x][1],  nimage[width * y + x][2] = nh[0][j] << 16,  nh[1][j] << 8, nh[2][j] 
                    
    new = createImage(width,height, 'RGB')
    new.pixels = np.fromstring(nimage, dtype=ctypes.c_uint)
    new.updatePixels()
    image(new,  0,  0)
    
def hypot_squared(a, b):
    """
    Must be cheaper to calculate than hypot
    """
    return (a * a) + (b * b)            

run()
