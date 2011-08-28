"""
Copyright (c) 2011 Martin Prout
 
This example is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
http://creativecommons.org/licenses/LGPL/2.1/

voronoi.py example
"""
from pyprocessing import *
from random import randint

def setup():
    size(800,  600)
    n = randint(50, 100) # of cells
    nx = [None] * n
    ny = [None] * n
    nr = [None] * n
    ng = [None] * n
    nb = [None] * n
    for i in xrange(n):
        nx[i] = randint(0, width - 1)
        ny[i] = randint(0, height - 1)
        nr[i] = randint(0, 255)
        ng[i] = randint(0, 255)
        nb[i] = randint(0, 255)
    
    for y in xrange(height):
        for x in xrange(width):
            # find the closest cell center
            # dmin = hypot_squared(width - 1, height - 1) # more intelligible version
            dmin = ((width - 1) * (width - 1)) + ((height - 1) * (height - 1)) # inline version
            j = -1
            for i in xrange(n):
                # d = hypot_squared((nx[i] - x),  (ny[i] - y)) # more intelligible version
                d = ((nx[i] - x) * (nx[i] - x)) + ((ny[i] - y) * (ny[i] - y)) # inline version
                if d < dmin:
                    dmin = d
                    j = i
            setScreen(x, y, color(nr[j], ng[j], nb[j]))  

#def hypot_squared(a, b):
#    """
#    Must be cheaper to calculate than hypot
#    """
#    return (a * a ) + (b *b)

run()
