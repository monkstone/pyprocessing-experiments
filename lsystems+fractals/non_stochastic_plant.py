"""
non-stochastic_plant.py is a python script for use in pyprocessing. 
Uses a lsystem module, that can parse both stochastic and
non-stochastic rules, or a mixture thereof
"""
from pyprocessing import *
from math import cos, sin, pi
from lsystems import grammar

# some constants
XPOS = 0
YPOS = 1
ANGLE = 2
WEIGHT = 3
DELTA = (22.5/180) * pi
# A simple stochastic rule as a dict, with a dict of values (only one key)
# and 3 weighted alternative substitutions.
RULES = {
    'X' : 'F-[[X]+X]+F[+FX]-X',
    'F' : 'FF',
}

AXIOM = 'X'


def render(production):       
    """
    Render evaluates the production string and calls draw_line
    """
    pen = [width/2, height*0.95, pi/2, 3]
    stack = []
    repeat = 1
    for val in production:
        if val == "F": 
            pen = draw_line(pen, 9)
        elif val == "+": 
            pen[ANGLE] += DELTA * repeat
        elif val == "-": 
            pen[ANGLE] -= DELTA * repeat
        elif val == "[": 
            temp = [pen[XPOS], pen[YPOS], pen[ANGLE],pen[WEIGHT] * 0.6]
            stack.append(temp)
        elif val == "]": 
            pen = stack.pop() 
            pen[WEIGHT] *= 1/0.6
        else: 
            pass
        
        
def draw_line(pen, length):
    """
    Draw line utility uses processing 'line' function to draw lines
    """
    new_xpos = pen[XPOS] + length * cos(pen[ANGLE])
    new_ypos = pen[YPOS] - length * sin(pen[ANGLE])
    strokeWeight(pen[WEIGHT])
    line(pen[XPOS], pen[YPOS], new_xpos, new_ypos)
    return [new_xpos, new_ypos, pen[ANGLE],pen[WEIGHT]]     
    
    
def setup():
    """
    The processing setup statement
    """
    size(500, 800)
    background(200, 200, 0)
    smooth()
    fill(190, 10, 10)
    noStroke()
    ellipse(300, 250, 180, 180)
    stroke(0, 100, 0)
    plant0 = grammar.repeat(4, AXIOM, RULES)
    plant1 = grammar.repeat(5, AXIOM, RULES)    
    plant2 = grammar.repeat(4, AXIOM, RULES)
    render(plant1)
    translate(-100, -5)
    stroke(200, 100, 100)
    render(plant0)
    translate(200, 0)    
    render(plant2)  
    print grammar.toRuleString(AXIOM, RULES)
    
    
run() 
