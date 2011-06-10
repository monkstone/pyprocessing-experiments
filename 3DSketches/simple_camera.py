"""
simple_camera.py a simple camera experiment in pyprocessing
"""


from pyprocessing import *
from math import pi

def setup():
    """
    processing setup
    """
    size(200, 200)
    fill(220, 0, 0)

def draw():
    """
    processing draw loop
    """
    background(220)
    lights()
    camera(100, 50, 200, 50, 50, 0, 0, 1, 0)
    rotateX(-pi/6)
    translate(50, 50, 0)
    rotateY(mouse.x/30.0)
    rotateZ(mouse.y/30.0)
    box(100, 100, 100)

run()
