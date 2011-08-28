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
    size(800,  600)
    n = randint(200, 300) # number of cells
    nx = np.random.randint(width, size=(n))      # numpy does randint(low, high) but high is excluded
    ny = np.random.randint(height, size= (n))    # if high = None, like here low defaults to randint(0, low)
    nh = np.random.randint(256, size=(3,  n))

    for y in xrange(height):
        for x in xrange(width):
            # find the closest cell center
            dmin = hypot_squared(width - 1, height - 1)                       # more intelligible version
            #dmin = ((width - 1) * (width - 1)) + ((height - 1) * (height - 1))  # optimized version?
            j = -1
            for i in xrange(n):
                d = hypot_squared((nx[i] - x),  (ny[i] - y))                  # more intelligible version
                #d = ((nx[i] - x) * (nx[i] - x)) + ((ny[i] - y) * (ny[i] - y))  # optimized version?
                if d < dmin:
                    dmin = d
                    j = i
            setScreen(x, y, color(nh[0][j], nh[1][j], nh[2][j])) 

def hypot_squared(a, b):
    """
    Must be cheaper to calculate than hypot
    """
    return (a * a) + (b * b)            

run()
