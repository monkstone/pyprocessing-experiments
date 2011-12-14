"""
basic_scene.py
Author: Martin Prout September 2011
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
        self.light = LightSource( (2, 4, -3), color = "White")
        
    def foreground(self):
        for i in xrange(4):
            self.scene.write(Sphere( ((i * 0.5), 0.25 + (i * 0.5), 2), 0.25, 
                Texture(
                        Pigment(
                                color = "Yellow")
                                )
                            )
                        )
            
        
        
    def background(self):    
        self.scene.write(self.cam,  self.sky,  self.light,  self.ground)
        
def main():   
    scene = BasicScene("basic_scene.pov",  (800, 600))    
    scene.background()
    scene.foreground()
    
if __name__ == "__main__":
    main()
