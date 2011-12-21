"""
povwriter_test.py
"""
from povwriter.povwriter import *

def create_scene():
    scene = POVFile("basic_scene.pov",  (800, 800), "colors.inc",  "skies.inc")
    cam = Camera(location = (0, 2, -3), look_at = (0, 1, 2),  right = (1,  0,  0))
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
                                    ), 
                                    rotate = (0,  10, 0)
                                )
    triangle = Triangle((0, 1, 2), (1, 0, 1),  (0,  0, 0), 
                        Texture(
                            Pigment(
                                    color = "Red")
                                    )
                                )
                           
    light = LightSource( (2, 4, -3), color = "White")
    
    scene.write(cam,  sky,  light,  ground,  triangle,  sphere)
    
def main():
    import subprocess
    create_scene()
    subprocess.check_output(['povray','+W800',  '+H800',  '+Q11',  '+Ibasic_scene.pov'])
    
    
if __name__ == "__main__":
    main()    


