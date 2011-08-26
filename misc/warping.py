"""
Copyright (c) 2011 Martin Prout
 
This module is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
http://creativecommons.org/licenses/LGPL/2.1/

warping.py example
"""

from pyprocessing import *
from os import getcwd,  path

# this sketch uses the vanilla processing convention of a local 'data' folder
# where images etc should be stored, and python path.join to create a 
# cross platform address, works for me!!!

data_path = path.join(getcwd(), 'data')  
source = None


def setup():
    size(301, 417)
    global source,  image_array
    source = loadImage(path.join(data_path,  'warp.jpg') ) 
    frameRate(3)

def draw():
    global source
    if (frame.count < 5):
        background(source)
    elif (frame.count > 200):
        exit(0)
    else:        
        destination = warp(source, frame.count)
        background(destination)



# implement a simple vertical wave warp.
def warp(sce, count):
    waveAmplitude = count/5.0# pixels
    numWaves = count % 5  # how many full wave cycles to run down the image
    w, h = sce.width, sce.height
    destination = PImage(w,h,  RGB)
    sce.loadPixels()
    sce.updatePixels()
    destination.loadPixels()
    

    yToPhase = 2.0*math.pi*numWaves / h # conversion factor from y values to radians.

    for x in xrange(w):
        for y in xrange(h):
            newX = int(x + waveAmplitude*sin(y * yToPhase))
            newY = y
            if ((newX < 0) or (newX > w)):
                c = 0
            else:
                c = sce.pixels[newY*w + newX]
            destination.pixels[y*w+x] = c
    destination.updatePixels() 
    return destination

run()


