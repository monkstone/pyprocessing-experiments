"""
csplant2.py pythonic exploration of context sensitive lsystems grammar
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
frameCount = 0
THETA = (5 * pi)/36 # 25 degrees in radians
production = None   # needs exposure at module level
    
def drawRod(distance):
    sides = 16
    radius = distance/7
    angle = 0
    angleIncrement = TWO_PI / sides
    
    beginShape(QUAD_STRIP)
    for i in range(sides+1):
        normal(cos(angle), 0, sin(angle))
        vertex(radius*cos(angle), 0, radius*sin(angle))
        vertex(radius*cos(angle), -distance, radius*sin(angle))
        angle += angleIncrement
    endShape()        
    # draw the spherical top cap
    translate(0, -distance, 0)
    sphereDetail(16)
    sphere(radius)

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
            drawRod(distance)
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
    fill(0, 200, 0)
    noStroke()
    

def draw():
    """
    Animate a 3D context free plant in processing/pyglet draw loop
    """
    background(20, 20, 180)
    global frameCount
    frameCount += 1
    lights()  
    camera(250, 250, 800, 0, -300, 0, 0, 1, 0)     
    rotateY(radians((frameCount * 2)%720) )
    pushMatrix()
    render(production)
    popMatrix()
run()        
