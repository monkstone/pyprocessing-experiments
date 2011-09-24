"""
cornell_box.py
Author: Martin Prout September 2011, based on an original cornell.pov by Kari Kivisalo
This O0 Cornell Box, uses 'raw' writing for more complicated PovRAY elements
such as the non point light source, with a SubPatch.
The povwriter module, a modified recipe (http://code.activestate.com/recipes/205451/ (r1)) 
is the normal interface between python and PovRAY.
"""

from povwriter import *

LC ='LightColor=<1,0.67,0.21>;' 
N = 'N=3; //Divisions per side'
DX = 'DX=13/N;   //Dimensions of sub patches'
DZ = 'DZ=10.5/N;'

SP = """SubPatch=
  light_source{
    <27.8,54.88,27.95>
    color LightColor*7
    area_light DX*x, DZ*z, 4, 4 jitter adaptive 0
    spotlight radius -90 falloff 90 tightness 1 point_at <27.8,0,27.95> //for cosine falloff
    fade_power 2 fade_distance  (DX+DZ)/2
  }"""
  
I0 = 'i=0;#while (i<N)'
J0 = '  j=0;#while (j<N)'
UF = '    light_source{SubPatch translate<i*DX-(13-DX)/2,0,j*DZ-(10.5-DZ)/2>}'
JE = '  j=j+1;#end'
IE = 'i=i+1;#end'

class CornellBox(object):
    """
    Cornell box mainly as an object, except for the lights which are bit complicated
    """
    def __init__(self):
        self.scene = POVFile("cornell_box.pov",  (300, 300), "colors.inc",  "skies.inc")
        
        self.cam = Camera(
                          location = (27.8, 27.3, -80), 
                          direction = (0, 0, 1), 
                          up = (0,  1,  0), 
                          right = (-1,  0,  0), 
                          angle = 39.5
                          )
        # light patch                
        self.skylight = Box ((21.3, 54.87, 33.2),  (34.3, 54.88, 22.7),  'no_shadow', 
                             Pigment(rgb = (1, 1, 1)), Finish(emission = 0.78,  diffuse = 0))
        # Floor, Ceiling, Backwall                             
        self.cornell_box = Union(
            # Floor
            Triangle((55.28, 0.0, 0.0), (0.0, 0.0, 0.0), (0.0, 0.0, 55.92)),
            Triangle((55.28, 0.0, 0.0), (0.0, 0.0, 55.92), (54.96, 0.0, 55.92)), 
            # Ceiling
            Triangle((55.60, 54.88, 0.0), (55.60, 54.88, 55.92), (0.0, 54.88, 55.92)), 
            Triangle((55.60, 54.88, 0.0), (0.0, 54.88, 55.92), (0.0, 54.88, 0.0)), 
            # Backwall
            Triangle((0.0, 54.88, 55.92), (55.60, 54.88, 55.92), (54.96, 0.0, 55.92)), 
            Triangle((0.0, 54.88, 55.92), (54.96, 0.0, 55.92), (0.0, 0.0, 55.92)), 
            Texture(Pigment(rgb = (1,  1,  1)),  Finish(diffuse=0.75,  ambient = 0))
                       )
             
        # Right wall
        self.right_wall = Union (
            Triangle((0.0, 54.88, 0.0), (0.0, 54.88, 55.92), (0.0, 0.0, 55.92)), 
            Triangle((0.0, 54.88, 0.0), (0.0, 0.0, 55.92), (0.0, 0.0, 0.0)), 
            Texture(Pigment(rgb = (0.025, 0.236, 0.025)),  Finish(diffuse=0.75,  ambient = 0))
            )
            
        # Left wall
        self.left_wall = Union (
            Triangle((55.28, 0.0, 0.0), (54.96, 0.0, 55.92), (55.60, 54.88, 55.92)), 
            Triangle((55.28, 0.0, 0.0), (55.60, 54.88, 55.92), (55.60, 54.88, 0.0)), 
            Texture(Pigment(rgb = (0.57, 0.025, 0.025)),  Finish(diffuse=0.75,  ambient = 0))
            )
            
     
        self.short_box = Union (
        #Short block
        Triangle((13.00, 16.50, 6.50), (8.20, 16.50, 22.50), (24.00, 16.50, 27.20)), 
        Triangle((13.00, 16.50, 6.50), (24.00, 16.50, 27.20), (29.00, 16.50, 11.40)), 
        Triangle((29.00, 0.0, 11.40), (29.00, 16.50, 11.40), (24.00, 16.50, 27.20)), 
        Triangle((29.00, 0.0, 11.40), (24.00, 16.50, 27.20), (24.00, 0.0, 27.20)), 
        Triangle((13.00, 0.0, 6.50), (13.00, 16.50, 6.50), (29.00, 16.50, 11.40)), 
        Triangle((13.00, 0.0, 6.50), (29.00, 16.50, 11.40), (29.00, 0.0, 11.40)), 
        Triangle((8.20, 0.0, 22.50), (8.20, 16.50, 22.50), (13.00, 16.50, 6.50)), 
        Triangle((8.20, 0.0, 22.50), (13.00, 16.50, 6.50), (13.00, 0.0, 6.50)), 
        Triangle((24.00, 0.0, 27.20), (24.00, 16.50, 27.20), (8.20, 16.50, 22.50)), 
        Triangle((24.00, 0.0, 27.20), (8.20, 16.50, 22.50), (8.20, 0.0, 22.50)), 
        Texture(Pigment(rgb = (1,  1,  1)),  Finish(diffuse=0.75,  ambient = 0))
   
        )  

        self.tall_box = Union (
          #Tall block
          Triangle((42.30, 33.00, 24.70), (26.50, 33.00, 29.60), (31.40, 33.00, 45.60)), 
          Triangle((42.30, 33.00, 24.70), (31.40, 33.00, 45.60), (47.20, 33.00, 40.60)), 
          Triangle((42.30, 0.0, 24.70), (42.30, 33.00, 24.70), (47.20, 33.00, 40.60)), 
          Triangle((42.30, 0.0, 24.70), (47.20, 33.00, 40.60), (47.20, 0.0, 40.60)), 
          Triangle((47.20, 0.0, 40.60), (47.20, 33.00, 40.60), (31.40, 33.00, 45.60)), 
          Triangle((47.20, 0.0, 40.60), (31.40, 33.00, 45.60), (31.40, 0.0, 45.60)), 
          Triangle((31.40, 0.0, 45.60), (31.40, 33.00, 45.60), (26.50, 33.00, 29.60)), 
          Triangle((31.40, 0.0, 45.60), (26.50, 33.00, 29.60), (26.50, 0.0, 29.60)), 
          Triangle((26.50, 0.0, 29.60), (26.50, 33.00, 29.60), (42.30, 33.00, 24.70)), 
          Triangle((26.50, 0.0, 29.60), (42.30, 33.00, 24.70), (42.30, 0.0, 24.70)), 
          Texture(Pigment(rgb = (1,  1,  1)),  Finish(diffuse=0.75,  ambient = 0))
        )
                           
        
    def writePovray(self):
        self.scene.declare(LC)
        self.scene.declare(N)
        self.scene.declare(DX)
        self.scene.declare(DZ)
        self.scene.declare(SP)
        self.scene.declare(I0)
        self.scene.declare(J0)
        self.scene.raw(UF)
        self.scene.declare(JE)
        self.scene.declare(IE)
        self.scene.write(self.cam, self.skylight,  self.cornell_box,  self.right_wall, self.left_wall,  
                        self.short_box,  self.tall_box)
            

def main():
    myScene = CornellBox()
    myScene.writePovray()
    
if __name__ == "__main__":
    main()    
