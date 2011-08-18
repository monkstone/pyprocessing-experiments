
from pyprocessing import *
"""
pyprocessing sketch from a set of rules
"""


def setup():
    """
    Processing setup
    """
    size(600, 600)
    translate(width/2, height/2)
    background(255)
    fill(100, 0, 0, 20)

    rect(0, 0, 500, 500)
    scale(0.75)
    ellipse(0, 0, 500, 500)
    rotate(radians(45))
    triangle(-250, 250/sqrt(3), 0, -500/sqrt(3), 250, 250/sqrt(3))
    triangle(-250, 250/sqrt(3), 0, -500/sqrt(3), 250, 250/sqrt(3))

run()

