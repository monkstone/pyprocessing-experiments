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

from numpy import *

def setup():
    size(600,  600)
  # n = random.randint(50, 100) # of cells
    n = 20
    hue = floor(random.random((n, 3))*255)
    points = floor(random.random((n, 2))*600)
    
#    for i, j in points,  hue:
#        pass
#    for i in xrange(n):
#        nx.append(randint(0, width - 1))
#        ny.append(randint(0, height - 1))
#       # nr.append(randint(0, 255))
#       # ng.append(randint(0, 255))
#       # nb.append(randint(0, 255))
#    
#    for y in xrange(height):
#        for x in xrange(width):
#            # find the closest cell center
#            dmin = hypot(width - 1, height - 1)
#            j = -1
#            for i in xrange(n):
#                d = hypot(nx[i] - x, ny[i] - y)
#                if d < dmin:
#                    dmin = d
#                    j = i
     #       setScreen(x, y, color(200, 80, 10)  )
            
run()
