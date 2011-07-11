from pyprocessing import *
from random import randint

def setup():
    size(800,  600)
    n = randint(50, 100) # of cells
    nx = []
    ny = []
    nr = []
    ng = []
    nb = []
    for i in xrange(n):
        nx.append(randint(0, width - 1))
        ny.append(randint(0, height - 1))
        nr.append(randint(0, 255))
        ng.append(randint(0, 255))
        nb.append(randint(0, 255))
    
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
            setScreen(x, y, color(nr[j], ng[j], nb[j]))  
            
run()
