"""
sierpinski.py is a python script for use in pyprocessing.
A very simple lsystem example
uses a lystems module to generate grammar
"""
from pyprocessing import * 
from math import pi, cos, sin
from lsystems import grammar

# some lsystem constants
XPOS = 0
YPOS = 1
ANGLE = 2
DELTA = pi * 2/3

#####
# The lsystem string substition rules as a dict
#####

RULES = {
    'F': 'FF',
    'X' : '-FXF+FXF+FXF-'
}

AXIOM = 'FX'

##
# defining the actions as functions with a common signature
##

def __turnRight(turtle, length = None):
    """
    private right turn function
    """
    turtle[ANGLE] += DELTA
    return turtle
    
def __turnLeft(turtle, length = None):
    """
    private left turn function
    """
    turtle[ANGLE] -= DELTA
    return turtle 
  
def __drawLine(turtle, length):
    """
    private draw line function
    returns a turtle at the new position
    """
    new_xpos = turtle[XPOS] + length * cos(turtle[ANGLE])
    new_ypos = turtle[YPOS] + length * sin(turtle[ANGLE])
    line(turtle[XPOS], turtle[YPOS], new_xpos, new_ypos)
    return [new_xpos, new_ypos, turtle[ANGLE]]
  
  
lsys_op = {   # A dictionary of functions
   'F' : __drawLine,
   '-' : __turnLeft,
   '+' : __turnRight,
}

def evaluate(key, turtle, length = None):
    """
    Is a safe? wrapper controlling access to the dict of functions
    """
    if lsys_op.has_key(key):
        turtle = lsys_op[key](turtle, length)
    else:
        if not RULES.has_key(key):        # useful for debugging you could
            print "Unknown rule %s" % key # comment out these lines 
    return turtle   
          
          
def render(production):        
    """
    Render evaluates the production string and calls evaluate which
    draws the lines etc
    """
    distance = 1.7
    turtle = [width/12, height/12, -DELTA]
    for rule in production:
        turtle = evaluate(rule, turtle, distance)
      
      
def setup():
    """
    Is the processing setup function
    """
    size(500, 500)
    background(0)
    stroke(255)
    production = grammar.repeat(7, AXIOM, RULES)
    translate(width*0.9, height*0.8) 
    render(production)
  
run() 
