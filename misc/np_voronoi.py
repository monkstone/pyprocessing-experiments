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
    size(800,  600)
    n = randint(200, 300) # of cells
    nx = np.floor(np.random.random((n))*(width-1))
    ny = np.floor(np.random.random((n))*(height-1))
    nh = np.floor(np.random.random((3, n))*255)

    for y in xrange(height):
        for x in xrange(width):
            # find the closest cell center
            dmin = hypot(width - 1, height - 1)
            j = -1
            for i in xrange(n):
                d = hypot(nx[i] - x, ny[i] - y)
                if d < dmin:
                    dmin = d
                    j = i
            setScreen(int(x),int(y), color(nh[0][j], nh[1][j], nh[2][j])) 
            
run()
