"""
penrose.py is a python script for use in pyprocessing 
It avoids switch, because python does not include it in the language, 
in my view this is big mistake switch is very easy on the eye, I dislike 
chains of if/elif, however the alternatives in python are either dodgy 
or equally ugly
"""

from pyprocessing import *
from math import pi, sin, cos

# some globals
XPOS = 0
YPOS = 1
ANGLE = 2
DELTA = pi/5

RULES = {
'F' : '',
'W' : 'YBF2+ZRF4-XBF[-YBF4-WRF]2+',
'X' : '+YBF2-ZRF[3-WRF2-XBF]+',
'Y' : '-WRF2+XBF[3+YBF2+ZRF]-',
'Z' : '2-YBF4+WRF[+ZRF4+XBF]2-XBF' 
}

AXIOM = '[X]2+[X]2+[X]2+[X]2+[X]'


def produce(axiom, rules):
    """
    single rule substitution utility
    """
    output = ""
    for i in axiom:
        output += rules.get(i, i)  # second i is returned when no dict key found
    return output
    
 
def repeat(rpx, axiom, rules):
    """
    Repeat rule substitution in a recursive fashion rpx times
    """ 
    production = axiom
    for i in range(0, rpx):
        production = produce(production, rules)
    return production
    

def render(production):        # avoiding switch and globals
    """
    Render evaluates the production string and calls draw_line
    """
    turtle = [0, 0, -DELTA]
    stack = []
    repeat = 1
    for val in production:
        if val == "F": 
            turtle = draw_line(turtle, 20)
        elif val == "+": 
            turtle[ANGLE] += DELTA * repeat
            repeat = 1
        elif val == "-": 
            turtle[ANGLE] -= DELTA * repeat
            repeat = 1
        elif val == "[": 
          temp = [turtle[XPOS], turtle[YPOS], turtle[ANGLE]]
          stack.append(temp)
        elif val == "]": 
            turtle = stack.pop() 
        elif (val == '2'):
            repeat = 2
        elif (val == '3'):
            repeat = 3    
        elif (val == '4'):
            repeat = 4     
        else: 
            pass


def draw_line(turtle, length):
    """
    Draw line utility uses processing 'line' function to draw lines
    """
    new_xpos = turtle[XPOS] + length * cos(turtle[ANGLE])
    new_ypos = turtle[YPOS] - length * sin(turtle[ANGLE])
    line(turtle[XPOS], turtle[YPOS], new_xpos, new_ypos)
    return [new_xpos, new_ypos, turtle[ANGLE]]     


def setup():
    """
    The processing setup statement
    """
    size(500, 500)
    production = repeat(5, AXIOM, RULES)
    translate(width/2, height/2) 
    render(production)    

run()
