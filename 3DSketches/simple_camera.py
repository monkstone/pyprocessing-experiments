from pyprocessing import *
import math

def setup():
    size(200, 200)
    #hint(ENABLE_OPENGL_4X_SMOOTH)
    #hint(DISABLE_OPENGL_ERROR_REPORT)
    fill(220, 0, 0)
    #noStroke()  

def draw():
    background(220)
    lights()
    #beginCamera()
    camera(100, 50, 200, 50, 50, 0, 0, 1, 0)
    rotateX(-math.pi/6)
    #endCamera()
    translate(50, 50, 0)
    rotateY(mouse.x/30.0)
    rotateZ(mouse.y/30.0)
    box(100, 100, 100)

run()
