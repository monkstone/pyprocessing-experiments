"""
sierpinski.py in pyprocessing by Martin Prout, a recursive solution
"""
from pyprocessing import *
import math

SQRT3 = math.sqrt(3)
T_HEIGHT = SQRT3/2 
TOP_Y = 1/SQRT3
BOT_Y = SQRT3/6
triangleSize = 800

def setup():
    """
    processing setup
    """
    size(math.ceil(triangleSize), math.ceil(T_HEIGHT*triangleSize))
    smooth()  
    fill(255)
    background(0)
    noStroke()
    drawSierpinski(width/2, height * (TOP_Y/T_HEIGHT), triangleSize)
    
    
def drawSierpinski(cx, cy, sz):
    """
    Limit no of recursions on size, Only draw terminals    
    """
    if (sz < 5):  
        drawTriangle(cx, cy, sz) 
        noLoop()
        
    else:
        cx0 = cx
        cy0 = cy - BOT_Y * sz
        cx1 = cx - sz/4
        cy1 = cy + (BOT_Y/2) * sz
        cx2 = cx + sz/4
        cy2 = cy + (BOT_Y/2) * sz
        drawSierpinski(cx0, cy0, sz/2)
        drawSierpinski(cx1, cy1, sz/2)
        drawSierpinski(cx2, cy2, sz/2)
      
def drawTriangle(cx, cy, sz):
    """
    draw a terminal triangle (actually any shape would do)
    """
    cx0 = cx
    cy0 = cy - TOP_Y * sz
    cx1 = cx - sz/2
    cy1 = cy + BOT_Y * sz
    cx2 = cx + sz/2
    cy2 = cy + BOT_Y * sz
    triangle(cx0, cy0, cx1, cy1, cx2, cy2)

run()
