"""
vec3d.py contains my lighweight Vec3D class avoids accessors 
by having public attributes (as does python default)
"""

class Vec3D(object):
    """
    A lightweight convenience class to store triangle point data
    """
    
    def __init__(self, x = 0, y = 0, z = 0):
        """
        Initialise the new Vec3D object
        """
        self.x = x
        self.y = y 
        self.z = z
     

        

  
