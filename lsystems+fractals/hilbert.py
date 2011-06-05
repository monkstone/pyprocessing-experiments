"""
hilbert.py by Martin Prout based on a Hilbert curve from "Algorithmic Beauty
of Plants" by Przemyslaw Prusinkiewicz & Aristid Lindenmayer
and a python lsystem module to provide grammar module.
Features processing affine transforms.
"""
from pyprocessing import *
import math
import time
from lsystems import grammar

# some lsystem constants
XPOS = 0
YPOS = 1
ANGLE = 2
BEN = math.pi/720   # use BEN to create a bent Hilbert
THETA = math.pi/2 # + BEN
PHI = math.pi/2 # - BEN

RULES = {
    'A': "B>F<CFC<F>D+F-D>F<1+CFC<F<B1^",
    'B': "A+F-CFB-F-D1->F>D-1>F-B1>FC-F-A1^",
    'C': "1>D-1>F-B>F<C-F-A1+FA+F-C<F<B-F-D1^",
    'D': "1>CFB>F<B1>FA+F-A1+FB>F<B1>FC1^"
}

AXIOM = 'A'

production = None   # need exposure at module level

def render(production):       
    """
    Render evaluates the production string and calls box primitive
    uses processing affine transforms (translate/rotate)
    """
    lightSpecular(204, 204, 204) 
    specular(255, 255, 255) 
    shininess(1.0) 
    distance = 20
    repeat = 1
    for val in production:
        if val == "F":
            translate(0, 0, -distance / 2.0)
            box(5, 5, -distance + 2.5)
            translate(0, 0, -distance / 2.0)
            box(5, 5, 5)
        elif val == '+': 
            rotateX(THETA * repeat)
            repeat = 1
        elif val == '-': 
            rotateX(-THETA * repeat)
            repeat = 1
        elif val == '>': 
            rotateY(THETA * repeat)
            repeat = 1
        elif val == '<': 
            rotateY(-THETA * repeat)
        elif val == '^': 
            rotateZ(PHI * repeat)
            repeat = 1
        elif (val == '1') :
            repeat = 2         
        elif (val == 'A' or val == 'B' or val == 'C' or val == 'D'):            
            pass  # assert as valid grammar and do nothing
        else: 
            print("Unknown grammar %s" % val)
            
def smoothVector(s1, s2, s3):
    """
    Stolen from lazydogs 3D Sierpinski sketch.
    Generate a vector whose components change smoothly over time in the range [ 0, 1 ].
    Each component uses a math.sin() function to map the current time in milliseconds 
    somewhere in the range [ 0, 1 ].A 'speed' factor is specified for each component.
    """
    mills = time.time() * 0.03 
    x = 0.5 * math.sin(mills * s1) + 0.5
    y = 0.5 * math.sin(mills * s2) + 0.5
    z = 0.5 * math.sin(mills * s3) + 0.5
    return [x, y, z]           
        
def smoothRotation(s1, s2, s3):
    """
    Stolen from lazydogs 3D Sierpinski sketch. Rotate the current coordinate system.
    Uses smoothVector() to smoothly animate the rotation.
    """
    r1 = smoothVector(s1, s2, s3) 
    rotateX(2.0 * math.pi * r1[0])
    rotateY(2.0 * math.pi * r1[1])
    rotateX(2.0 * math.pi * r1[2])   


    
def setup():
    """
    The processing setup statement
    """
    size(500, 500)
    global production
    production = grammar.repeat(4, AXIOM, RULES)    
    noStroke()            
    fill(200, 0, 180)   
   
    
def draw():
    """
    Render a 3D Hilbert/Ben Tilbert, somewhat centered
    """
    background(255)
    lights()  
    camera(250, 250, 800, 0, 0, 0, 0, 1, 0)     
    smoothRotation(4.5, 3.7, 7.3)
    pushMatrix()
    translate(53, 33, 25)
    render(production)
    popMatrix()
run()
