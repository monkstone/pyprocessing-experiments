"""
alhambra.py by Martin Prout (created 3 June 2011)
Alhambra tiling in pyprocessing (version 0.1.2.7)
Colors chosen to be a bit nearer the original (also corrected orientation),
and added stars to the non drawn triangles.
Utilizes a custom lightweight TPoint (to replace the more fattening PVector)
"""

from tpoint import TPoint
from pyprocessing import *

from math import sqrt, sin, cos


xValues = [100, 300, 500, 700, 900, 1100, 1300, 1500]
yValues = [50 * sqrt(3), 150 * sqrt(3), 250 * sqrt(3), 350 * sqrt(3), 450 * sqrt(3), 550 * sqrt(3)]

GOLD = 0
BLACK = 1
GREEN = 2
BLUE = 3
RED = 4
WHITE = 5

colors = [
   color(151, 84, 5),
   color(33, 3, 3),
   color(21, 69, 43),
   color(27, 51, 121),
   color(59, 17, 1),
   color(211, 200, 200)
]

def setup():
    """
    processing setup
    """
    size(1280, 906)
    background(colors[WHITE])
    smooth()
    render()

def draw_star(xpos, ypos, sz, col):
    """
    draw star shape function
    """
    noStroke()
    fill(col)
    triangle(xpos + sz/sqrt(3), ypos, xpos - (sqrt(3)*sz)/6, ypos - 0.5 * sz, xpos - (sqrt(3)*sz)/6, ypos + 0.5 * sz)
    triangle(xpos - sz/sqrt(3), ypos, xpos + (sqrt(3)*sz)/6, ypos - 0.5 * sz, xpos + (sqrt(3)*sz)/6, ypos + 0.5 * sz)
    
def draw_hexagon(xpos, ypos, sz, theta):
    """
    hexagon draw function
    """
    fill(colors[WHITE])
    beginShape()
    for i in range(0, 6):
        vertex(xpos + sz*cos((pi/3 * i) + theta), ypos + sz*sin((pi/3 * i) +theta))
    endShape(CLOSE)
        
        
def draw_triangle(x0, y0, sz, coluer, disp):
    """
    Wavy triangle draw function
    """
    # Set the three initial triangle points, thereafter calculate mid points, and  
    # quarter points. Then adjust the bezier curve control points.
    pts = []
    pts.append(TPoint(x0, y0 + sz/sqrt(3)))               # A (A, B and C are the triangle points)
    pts.append(TPoint(x0 - 0.5 * sz, y0 - (sqrt(3)*sz)/6))# B
    pts.append(TPoint(x0 + 0.5 * sz, y0 - (sqrt(3)*sz)/6))# C
    pts.append(pts[0].mid_point(pts[1]))                        # Ab (Ab, Bc and Ca are the triangle mid points)
    pts.append(pts[1].mid_point(pts[2]))                        # Bc
    pts.append(pts[0].mid_point(pts[2]))                        # Ca
    pts.append(pts[0].mid_point(pts[3]))                        # Aba (Aba ... are the triangle quarter points)
    adjust_bezier(pts[6], -pi/3, -disp*sz)                      # Aba
    pts.append(pts[3].mid_point(pts[1]))                        # Abb
    adjust_bezier(pts[7], -pi/3, disp*sz)                       # Abb
    pts.append(pts[1].mid_point(pts[4]))
    adjust_bezier(pts[8], -pi/2, disp*sz)
    pts.append(pts[4].mid_point(pts[2]))
    adjust_bezier(pts[9], -pi/2, -disp*sz)
    pts.append(pts[2].mid_point(pts[5]))
    adjust_bezier(pts[10], pi/3, disp*sz)
    pts.append(pts[5].mid_point(pts[0]))
    adjust_bezier(pts[11], pi/3, -disp*sz)
    # render triangle
    fill(coluer)
    beginShape()
    vertex(pts[0].x, pts[0].y)
    bezierVertex(pts[0].x, pts[0].y, pts[6].x, pts[6].y, pts[3].x, pts[3].y)
    bezierVertex(pts[3].x, pts[3].y, pts[7].x, pts[7].y, pts[1].x, pts[1].y)
    bezierVertex(pts[1].x, pts[1].y, pts[8].x, pts[8].y, pts[4].x, pts[4].y)
    bezierVertex(pts[4].x, pts[4].y, pts[9].x, pts[9].y, pts[2].x, pts[2].y)
    bezierVertex(pts[2].x, pts[2].y, pts[10].x, pts[10].y, pts[5].x, pts[5].y)
    bezierVertex(pts[5].x, pts[5].y, pts[11].x, pts[11].y, pts[0].x, pts[0].y)
    endShape(CLOSE)   
    draw_hexagon(x0 - 4, y0, sz * 0.22, 0) 
    
    
def adjust_bezier(bzpoint, theta, disp):
    """
    Adjust the Bezier control point
    """
    bzpoint.add(TPoint(cos(theta)*disp, sin(theta)*disp))    

    
def render():
    """
    Tesselate the wavy triangles, add some star in the spaces
    """
    for column in range(0,len(xValues)):
        for row in range(0,len(yValues)):
            if (row % 2 == 0):
                draw_triangle(xValues[column], yValues[row], 200, colors[(1 + column)%5], 0.32)
                draw_star(xValues[column] - 95, yValues[row] + 60, 70, colors[(2 + column)%5])
            else:
                draw_triangle(xValues[column] - 100, yValues[row], 200, colors[column%5], 0.32)
                draw_star(xValues[column] + 5, yValues[row] + 60, 70, colors[(2 + column)%5])

run()
