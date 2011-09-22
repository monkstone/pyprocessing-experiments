"""
elegant_ball.py
Another opengl sketch from lazydog translated to pyprocessing by monkstone.
http://lazydog-bookfragments.blogspot.com/2009/05/final-version-of-ball-of
-confusion-for.html
"""
from pyprocessing import *
from povwriter.povwriter import *
from math import sqrt

# define PHI as the Golden Ratio constant
PHI = (1 + sqrt(5))/2

def main():
    scene = POVFile("basic_scene.pov",  "colors.inc",  "skies.inc")
    cam = Camera(location = (0, 2, -3), look_at = (0, 1, 2))
    sky = SkySphere("S_Cloud3")
    ground = Plane((0.0, 1.0, 0.0), 0.0,
                    Texture(
                            Pigment(color = "NeonBlue"),  
                            Finish(reflection = 0.15)
                            )
                        )
    sphere = Box( (0, 1, 2), (1, 0, 1), 
                    Texture(
                            Pigment(
                                    color = "Yellow")
                                    )
                                )
    triangle = Triangle((0, 1, 2), (1, 0, 1),  (0,  0, 0), 
                        Texture(
                            Pigment(
                                    color = "Red")
                                    )
                                )
                           
    light = LightSource( (2, 4, -3), color = "White")
    scene.write(cam,  sky,  light,  ground,  triangle,  sphere)
    
if __name__ == "__main__":
    main()    


