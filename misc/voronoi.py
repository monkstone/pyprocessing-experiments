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
# cross platform address, depends working directory being where script is located
# and that directory containing the data folder

data_path = path.join(getcwd(), 'data')  

X = 0   # intelligible array indicies
Y = 1
R = 0
G = 1
B = 2
display_center = False

def setup():
    """
    pyprocessing setup
    """
    size(800, 600)
    global original,  image_array,  npos,  ncol,  n,  voronoi
    voronoi = None
    original = loadImage(path.join(data_path, 'voronoi.png') ) 
    n = randint(50, 100)                   # randomly determine number of cells
    nc= [[None] * n for i in range(3)]     # initialize empty multi arrays     
    ncol = [None] * n
    np =[[None] * 2 for j in range(n)]     # avoid  copy by reference trap (python bites)
    for i in xrange(n):
        np[i][X], np[i][Y]  = randint(0, width - 1),  randint(0, height - 1)
        nc[R][i] = randint(0, 255)                             # random red
        nc[G][i] = randint(0, 255)                             # random green
        nc[B][i] = randint(0, 255)                             # random blue
        ncol[i] = nc[R][i]<<16|nc[G][i]<<8|nc[B][i]  # bit shifting to a RGB color
    npos = sorted(np, compare_pixel_index)
    
def draw():
    """
    Loads an existing voronoi image from file to keep the impatient happy, creates 
    (it takes a while) a new voronoi image by brute force, and draws it screen. This
    is the draw loop so we can change things here using key/mouse etc
    """    
    global original, voronoi, npos,  ncol,  n
    if (frame.count < 5):
        background(original)      
    elif (voronoi == None):
        voronoi = new_voronoi(npos, ncol,  n)   # this is a candidate for a new thread!
    else:
        background(voronoi)
    if (display_center):
        fill(0)
        for vc in npos:
            ellipse(vc[X], vc[Y], 5, 5)
       
def  compare_pixel_index(a,  b):
    """
    Used to sort voronoi centers by their pixel index 
    """
    return cmp(a[1]*a[0] +a[0],  b[1]*b[0] +b[0])
        
def new_voronoi(npos, ncol,  n):
    """
    Creates a voronoi image by brute force
    @param npos = x, y position array voronoi cell centers
    @param ncol = RGB color int
    @param  n = no of voronoi cells
    @return new voronoi Pimage
    There is a possible speed up if we don't check every voronoi center
    see commented out code, the cut off maxima/minima were empirically 
    determined, if more than one center or no center is seen in a cell adjust 
    the appropriate cut off below code lines 85 to 88.
    """
    voronoi = PImage(width, height,  RGB)
    # minima = 0            # to get a slight speed up we don't check every cell center
    # maxima = int(0.6 * n) # minima and maxima determine which values are checked 
    for y in xrange(height):
        #if (y > 0.1 * height):  
        #    maxima = int(n * 0.8) if (y < 0.15 * height) else n       
        #    if (y > 0.8 * height):
        #        minima = int(n * 0.1) if (y < 0.9 * height) else int(n * 0.15)  
        for x in xrange(width):
            dmin = ((width - 1) * (width - 1)) + ((height - 1) * (height - 1)) 
            j = -1                
            for i in xrange(n):
            #for i in xrange(minima, maxima):  
                d = ((npos[i][X]- x) * (npos[i][X]- x)) + ((npos[i][Y]- y) * (npos[i][Y]- y)) 
                if d < dmin:
                    dmin = d
                    j = i
            voronoi.pixels[y*width+x] = ncol[j] 
    voronoi.updatePixels()
    return voronoi
    
def keyPressed():
    """
    Press 'c' to toggle the display of voronoi cell "centers" 
    Press 's' to save the current file to disk
    """
    global display_center
    if key.char in 'cC':
        display_center = not display_center
    if key.char in 'sS':
        global voronoi
        voronoi.save(path.join(data_path, "new_voronoi.png"))
    if key.char in 'eE':
        exit(0)
run()

