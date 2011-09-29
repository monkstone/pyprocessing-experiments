"""
cornell_box.py
Author: Martin Prout September 2011, based on an original cornell.pov by Kari Kivisalo
This O0 Cornell Box, uses 'raw' writing for more complicated PovRAY elements
such as the non point light source, with a SubPatch.
The povwriter module, a modified recipe (http://code.activestate.com/recipes/205451/ (r1)) 
is the normal interface between python and PovRAY.
"""

from povwriter import *



class BasicScene(object):
    """
    Basic external scene
    Note the use of tuples to group scalar values for vector type
    """
    def __init__(self,  name,  size):
        self.scene = POVFile(name,  size, "colors.inc",  "skies.inc")
        self.cam = Camera(location = (0, 2, -3), look_at = (0, 1, 2))
        self.sky = SkySphere("S_Cloud3")
        self.ground = Plane((0.0, 1.0, 0.0), 0.0,
                        Texture(
                                Pigment(color = "NeonBlue"),  
                                Finish(reflection = 0.15)
                                )
                            )
        self.sphere = Sphere( (0, 1, 2), 1, 
                        Texture(
                                Pigment(
                                        color = "Yellow")
                                        )
                                    )
        self.light = LightSource( (2, 4, -3), color = "White")
        
    def add_spheres(self):
        self.spheres = [10]
        for i in xrange(10):
            self.spheres[i] = Sphere( (0, i, 2), 1, 
                Texture(
                        Pigment(
                                color = "Yellow")
                                )
                            )
            
        
        
    def write_file(self):    
        self.scene.write(self.cam,  self.sky,  self.light,  self.ground,  self.spheres)
        
def main():   
    scene = BasicScene("basic_scene.pov",  (800, 600))
    scene.write()
