"""
fern.py is a python script for use in processing.py.
After a fern by Gareth Spor
by monkstone features a pen as a dictionary
"""
from pyprocessing import *
from math import pi, cos, sin

# some globals

DELTA = 5.4 * pi/180

STARTCOLOR = color(0, 255, 0) # bright green

# bitwise color decrement for efficiency
DECREMENT = (6<<8)

RULES = {
'B' : '[6+#FD][7-#FD]', 
'C' : 'B',
'D' : 'C+@FD'
}

AXIOM = 'FD'
production = ""

def __produce(axiom, rules):
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
        production = __produce(production, rules)
    return production
    

def render(production):        # avoiding switch and globals
    """
    Render evaluates the production string and calls draw_line
    """
    global DELTA
    pen = { 'xpos' : 10, 
            'ypos' : 150, 
            'theta' : 0, 
            'distance' : 100, 
            'col' : STARTCOLOR
           }
    stack = []
    repeat = 1
    for val in production:
        if val == "F": 
            pen = __drawLine(pen)
        elif val == "+": 
            pen['theta'] += DELTA * repeat
            repeat = 1
        elif val == "-": 
            pen['theta'] -= DELTA * repeat
            repeat = 1
        elif val == "#": 
            pen['distance'] *= 0.33
            pen['col'] -= DECREMENT
        elif val == "@": 
            pen['distance'] *= 0.9 
            pen['col'] -= (DECREMENT << 1) # continue with bit shift * 2
        elif ((val == '6') or (val == '7')):
            repeat += int(val)  
        elif (val == '['):
            stack.append(dict(pen))
        elif (val == ']'):
            pen = stack.pop()            
        else: 
            pass


def __drawLine(pen):
    """
    Draw line utility uses processing 'line' function to draw lines
    takes pen dictionary input returns a pen with new position
    """
    new_xpos = pen['xpos'] + pen['distance'] * cos(pen['theta'])
    new_ypos = pen['ypos'] + pen['distance'] * sin(pen['theta'])
    stroke(pen['col'])
    strokeWeight(2)
    line(pen['xpos'], pen['ypos'], new_xpos, new_ypos)
    new_pen = dict(pen)
    new_pen['xpos'] = new_xpos
    new_pen['ypos'] = new_ypos
    return new_pen


def setup():
    """
    The processing setup statement
    """
    size(800, 600)
    global production
    production = repeat(17, AXIOM, RULES)
    

def draw():
    """
    Render the fern on a black background
    """
    background(0)
    smooth()
    render(production) 


run()
