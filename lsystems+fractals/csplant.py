"""
cplant.py pythonic exploration of context sensitive lsystems grammar
context sensitive plant (includes cs grammar generator)
code looks super messy 'twas easier in ruby
"""
from pyprocessing import *
from math import pi, sin
from time import time
from lsystems import csgrammar

AXIOM = 'F'
IGNORE = '[]+-^&3'
RULES = {
  'F': 'F[-EF[3&A]]E[+F[3^A]]',
  'F<E': 'F[&F[3+A]][^F[3-A]]'
}

# string walk constants
LEFT = -1
RIGHT = 1

THETA = (5 * pi)/36 # 25 degrees in radians
production = None   # needs exposure at module level

def speedVector(speed):
    """
    Adapted from lazydogs 3D Sierpinski sketch.
    """
    mills = time() * 0.03 
    y = 0.5 * sin(mills * speed) + 0.5
    return y           
        
def speedRotation(speed):
    """
    Adapted from lazydogs 3D Sierpinski sketch. Rotate the current coordinate system.
    Uses speedVector() to speedly animate the trre rotation.
    """
    r1 = speedVector(speed) 
    rotateY(2.0 * pi * r1)

def render(production):       
    """
    Render evaluates the production string and calls box primitive
    uses processing affine transforms (translate/rotate)
    """
    lightSpecular(204, 204, 204) 
    specular(255, 255, 255) 
    shininess(1.0) 
    distance = 80
    repeat = 1
    for val in production:
        if val == "F":
            translate(0, distance/-2, 0)
            box(distance/9, distance, distance/9)
            translate(0, distance/-2, 0)
        elif val == '[': 
            pushMatrix() 
        elif val == ']': 
            popMatrix()              
        elif val == '+': 
            rotateX(-THETA * repeat)
            repeat = 1
        elif val == '-': 
            rotateX(THETA * repeat)
            repeat = 1
        elif val == '^': 
            rotateZ(THETA * repeat)            
            repeat = 1
        elif val == '&': 
            rotateZ(-THETA * repeat)
            repeat = 1
        elif (val == '3') :
            repeat = 3      
        elif (val == 'A' or val == 'E'):            
            pass  # assert as valid grammar and do nothing
        else: 
            print("Unknown grammar %s" % val)

    
def setup():
    """
    processing setup
    """
    size(800, 600)
    global production
    production = csgrammar.repeat(5, AXIOM, RULES, IGNORE)
    rotateY(pi/2)
    fill(0, 200, 0)
    noStroke()
    

def draw():
    """
    Animate a 3D context free plant in processing/pyglet draw loop
    """
    background(20, 20, 180)
    lights()  
    camera(250, 250, 800, 0, -300, 0, 0, 1, 0)     
    speedRotation(4.5)
    pushMatrix()
    render(production)
    popMatrix()
run()        
