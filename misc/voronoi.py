"""
Copyright (c) 2011 Martin Prout
 
This module is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
http://creativecommons.org/licenses/LGPL/2.1/

voronoi.py example
"""

from pyprocessing import *
from random import randint
import numpy as npll

def setup():
    size(800,  600)
    n = randint(50, 100) # of cells
    npx = np.random.random((1, n)*height - 1)
    npy = np.random.random((1, n)*width - 1)
    npc = np.random.random((3, n)*255)
    
    for y in xrange(height):
        for x in xrange(width):
            # find the closest cell center
            dmin = hypot(width - 1, height - 1)
            j = -1
            for i in xrange(n):
                d = hypot(npx[i] - x, npy[i] - y)
                if d < dmin:
                    dmin = d
                    j = i
            setScreen(x, y, color(int([0][j]), int(npc[1][j]), int(npc[2][j])))  
            
run()
