"""
Copyright (c) 2011 Martin Prout

This demo is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
http://creativecommons.org/licenses/LGPL/2.1/

mpeano.py a script for use with pyprocessing
"""

from pyprocessing import *

# some globals
XPOS = 0
YPOS = 1
ANGLE = 2
DELTA = math.pi/4

RULES = {
'F' : '',
'Y': 'FFY',
'X' : '+!X!FF-BQFI-!X!FF+',
'A' : 'BQFI',
'B' : 'AFF' 
}

AXIOM = 'XFF2-AFF2-XFF2-AFF'


def produce(axiom, rules):
    """
    single rule substitution utility
    """
    output = ""
    for i in axiom:
        output += rules.get(i, i)    # second i is returned when no dict key found
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
    global DELTA
    distance = 15
    turtle = [width/10, height/10, -DELTA]
    repeat = 1
    for val in production:
        if val == "F": 
            turtle = draw_line(turtle, distance)
        elif val == "+": 
            turtle[ANGLE] += DELTA * repeat
            repeat = 1
        elif val == "-": 
            turtle[ANGLE] -= DELTA * repeat
            repeat = 1
        elif val == "I": 
          distance *= 1/math.sqrt(2)
        elif val == "Q": 
            distance *= math.sqrt(2)
        elif val == "!":             
            DELTA = -DELTA        
        elif (val == '2'):
            repeat = 2   
        else: 
            pass


def draw_line(turtle, length):
    """
    Draw line utility uses processing 'line' function to draw lines
    """
    new_xpos = turtle[XPOS] + length * math.cos(turtle[ANGLE])
    new_ypos = turtle[YPOS] - length * math.sin(turtle[ANGLE])
    line(turtle[XPOS], turtle[YPOS], new_xpos, new_ypos)
    return [new_xpos, new_ypos, turtle[ANGLE]]     


def setup():
    """
    The processing setup statement
    """
    size(600, 600)
    production = repeat(6, AXIOM, RULES)
    background(0, 0, 255)
    smooth()
    stroke(255, 255, 0)
    strokeWeight(3)
    render(production)    

if __name__ == "__main__":
    """
    guido would prefer this to naked run()?
    """
    run()
