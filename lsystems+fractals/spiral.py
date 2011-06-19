"""
  spiral.py a pyprocessing sketch
  features fairly extreme recursion for
  python hence need to increase limit
"""

from pyprocessing import *
import sys

sys.setrecursionlimit(3500)
REDUCE = 0.999  
MIN_SIZE = 0.8 # about right for processing

def shell(rot, disp, sz):
    """
    recursive shell shape limited by sz
    """
    if (sz < MIN_SIZE):
        return        
    else:
        sz *= REDUCE 
        disp *= REDUCE
        translate(disp, 0)
        rotate(rot)
        ellipse(disp, 0, sz, sz)
    return shell(rot, disp, sz)# recursive call

def setup():
    """
    processing setup
    """
    size(400, 400) 
    translate(100, 330) 
    rotate(0.3)
    fill(255, 0, 0, 0)
    background(0)
    noStroke()   
    smooth()
    fill(255, 0, 0, 20)# transparency makes for almost '3d' look
    shell(-0.008, 1.5, 25)

run()
