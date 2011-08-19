"""
Copyright (c) 2011 Martin Prout
 
This module is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
http://creativecommons.org/licenses/LGPL/2.1/

pygenerate.py example
"""

from context_free.context_free import ContextFree
from context_free.sketch_writer import SketchWriter

class PyGenerate(ContextFree,  SketchWriter):
    def __init__(self,  filename):
        ContextFree.__init__(self)
        SketchWriter.__init__(self,  filename)
    def render_expansion(self, s):
        """
        Override this method to do something more edifying like render shape in pyprocessing
        """
        if (s == "push"):
            self.append("pushMatrix()")
        elif (s == "pop"):
            self.append("popMatrix()")
        elif (s == "left"):
            self.append("translate(-125, 0)")
        elif (s == "right"):
            self.append("translate(125, 0)")
            self.append("scale(0.45)")
        elif (s == "square"):
            self.append("rect(0, 0, 500, 500)")
        elif (s == "scale"):
            self.append("scale(0.75)")
        elif (s == "circle"):
            self.append("ellipse(0, 0, 500, 500)")
        elif (s == "triangle"):
            self.append("triangle(-250, 250/SQRT3, 0, -500/SQRT3, 250, 250/SQRT3)")
        elif (s == "rotate"):
            self.append("rotate(radians(45))")
        else:
            self.append("unexpected syntax")
            
      

def main():
    """
    Hommage to Adam Parrish original, test also saves my imagination for something more
    edifying
    """
    pdeg = PyGenerate("test.py")
    pdeg.add_rule("Drawing", "Square")
    pdeg.add_rule("Square", "square")
    pdeg.add_rule("Triangle", "triangle")
    pdeg.add_rule("Square", "Triangle")
    pdeg.add_rule("Triangle", "Square Triangle")
    pdeg.add_rule("Square", "square scale circle rotate Square square")
    pdeg.add_rule("Triangle", "square scale circle rotate triangle triangle")
    pdeg.add_rule("Triangle", "square scale triangle scale triangle")
    pdeg.add_rule("Square", "square scale Square")
    pdeg.add_rule("Square", "square push left Square pop push right Square pop")
    pdeg.add_rule("Square", "square scale circle rotate square")
    pdeg.add_rule("Triangle", "square scale Triangle scale triangle")
    pdeg.add_rule("Square", "square scale Square")
    pdeg.add_rule("Square", "square push left Square pop push right Square pop")
    pdeg.begin()
    pdeg.expand("Drawing")
    pdeg.end()
    
if __name__ == "__main__":
    main()
