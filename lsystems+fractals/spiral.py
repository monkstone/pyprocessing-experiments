from pyprocessing import *
import sys

sys.setrecursionlimit(3500)

REDUCE = 0.999  
MIN_SIZE = 0.8 # about right for processing


def shell(rot, disp, sz):
    if (sz < MIN_SIZE):
        pass
    else:
        translate(disp * REDUCE, 0)
        rotate(rot)
        ellipse(disp, 0, sz, sz)
        shell(rot, disp * REDUCE, sz * REDUCE)# recursive call
    
def setup():
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
