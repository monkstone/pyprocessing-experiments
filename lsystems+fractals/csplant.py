"""
cplant.py pythonic exploration of context sensitive lsystems grammar
context sensitive plant (includes cs grammar generator)
code looks super messy 'twas easier in ruby
"""
from pyprocessing import *
from math import pi, sin
from time import time

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

def __context(a):
    """
    Private helper function returns a tuple of value, index and context from key 'a'
    Valid direction setters are '>' or '<' else no direction is set
    """
    index = 0
    before =  a[1] == '<' if len(a) == 3 else False # python ternary operator
    after =  a[1] == '>' if len(a) == 3 else False # python ternary operator
    cont = a[0] if (before or after) else None
    if (before): 
        index += LEFT
    if (after): 
        index += RIGHT
    value = a[2] if len(a) == 3 else a[0]    
    return (value, index, cont)

def __getContext(path, index, direction, ignore):
    """
    Private helper returns context character from path[index + direction], 
    skipping and ignore characters
    """
    skip = 0
    while path[direction + index + skip] in ignore:
        skip += direction
    return path[direction + index + skip] 
    
        
def hasContext(a, b, index):
    """
    from a given key, axiom/production string and index returns
    has context boolean (ignoring characters in IGNORED)
    """
    cont = False
    if __context(a)[0] == b[index] and __context(a)[1] != 0:
        if __context(a)[1] == LEFT and index > 0:     # guard negative index
            cont = __context(a)[2] == __getContext(b, index, LEFT, IGNORE)
        elif __context(a)[1] == RIGHT and index < len(b) - 1: # guard out of range index
            cont = __context(a)[2] == __getContext(b, index, RIGHT, IGNORE)  
    return cont

def produce(ax, rules):
    """
    generate production from axiom and rules
    """
    str_buf = []   # initialize string buffer
    csrule = {}    # initialize context sensitive dict
    for key in rules.keys():
        if len(key) == 3:
            csrule[key[2]] = key
    for i, a in enumerate(ax):
        r = csrule.get(a, a)
        if (r == a):  # handle as a cf rule
            str_buf.append(rules.get(a, a))
        else:         # handle as a cs rule
            if hasContext(r, ax, i):
                str_buf.append(rules.get(r))
            else:
                str_buf.append(r[2])
    return ''.join(str_buf) # join str_buf list as a single string

def repeat(rpx, axiom, rules):
    """
    Repeat rule substitution in a recursive fashion rpx times
    """ 
    production = axiom
    from itertools import repeat
    for _ in repeat(None, rpx):
        production = produce(production, rules)
    return production
    
def setup():
    """
    processing setup
    """
    size(800, 600)
    global production
    production = repeat(5, AXIOM, RULES)
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
