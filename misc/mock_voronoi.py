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
from os import getcwd,  path
from random import randint
# this sketch uses the vanilla processing convention of a local 'data' folder
# where images etc should be stored, and python path.join to create a 
# cross platform address, works for me!!!

data_path = path.join(getcwd(), 'data')  

X = 0   # intelligible array indicies
Y = 1
R = 0
G = 1
B = 2

def setup():
    size(800, 600)
    global source,  image_array,  npos,  nc,  n,  voronoi
    voronoi = None
    source = loadImage(path.join(data_path,  'voronoi.png') ) 
    n = randint(50, 100)                              # randomly determine number of cells
    npos = [[None] * n for x in range(2)]   # initialize empty multi arrays 
    nc= [[None] * n for x in range(3)]        # avoid  copy by reference trap (python bites)

    for i in xrange(n):
        npos[X][i] = randint(0, width - 1)
        npos[Y][i] = randint(0, height - 1)
        nc[R][i] = randint(0, 255)
        nc[G][i] = randint(0, 255)
        nc[B][i] = randint(0, 255)


def draw():
    """
    loads a existing voronoi image from file to keep the impatient happy
    creates (takes a bit) a new voronoi image by brute force and draws it screen when ready
    """    
    global source,  voronoi, npos,  nc,  n
    if (frame.count < 5):
        background(source)      
    elif (voronoi == None):
        voronoi = new_voronoi(npos, nc,  n)
    else:
        background(voronoi)  
        
def new_voronoi(npos, nc,  n):
    """
    Creates a voronoi image by brute force
    @param npos = x, y position array voronoi centers
    @param nc = r, g, b color array
    @param  n = no of voronoi cells
    @return voronoi Pimage
    """
    voronoi = PImage(width,height,  RGB)
    for y in xrange(height):
        for x in xrange(width):
            # find the closest cell center
            # dmin = hypot_squared(width - 1, height - 1) # more intelligible version
            dmin = ((width - 1) * (width - 1)) + ((height - 1) * (height - 1)) # inline version
            j = -1
            for i in xrange(n):
                # d = hypot_squared((nx[i] - x),  (ny[i] - y)) # more intelligible version
                d = ((npos[X][i] - x) * (npos[X][i] - x)) + ((npos[Y][i] - y) * (npos[Y][i] - y)) # inline version
                if d < dmin:
                    dmin = d
                    j = i
            voronoi.pixels[y*width+x] = color(nc[R][j], nc[G][j], nc[B][j]) 
    voronoi.updatePixels()
    return voronoi
    

run()


