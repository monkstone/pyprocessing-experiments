"""
box.py contains use lighweight Vec3D class to store indexed vector points 
by having public attributes (as does python default)
"""
from vec3d import Vec3D
from mesh import Mesh

class Box(object):
    """
    A lightweight convenience class to store box point data
    With a function to return indexed vector points 
    """
    
    def __init__(self, x = 0, y = 0,  z = 0,  xd = 1,  yd = 1,  zd = 1):
        """
        Initialise the new Box object
        """
        self.xx= x
        self.yy = y 
        self.zz = z 
        self.xd = xd
        self.yd = yd
        self.zd = zd
        self.idx_array  = [1,  0,  2,  3,  1,  2,  5,  4,  6,  7,  5,  6,  4,  5,  0,  1,  4,  0,  7,  6,  2,  2,  6,  3,  0,  5,  7,  2,  0,  7,  4,  1, 6,  6,  1,  3]
        self.normal_array = [0, 0, 1, 0, 0, -1, 1, 0, 0, -1, 0, 0, 0, 1, 0, 0, -1, 0]
    def points(self):
        """
        The unique corner points of box (front + back order)
        """
        cpoints = [] 
        cpoints.append( Vec3D(-self.xd * 0.5 + self.xx, -self.yd * 0.5 + self.yy, -self.zd * 0.5 + self.zz) )  
        cpoints.append( Vec3D(+self.xd * 0.5 + self.xx, -self.yd * 0.5 + self.yy, -self.zd * 0.5 + self.zz) )
        cpoints.append( Vec3D(-self.xd * 0.5 + self.xx, +self.yd * 0.5 + self.yy, -self.zd * 0.5 + self.zz) )
        cpoints.append( Vec3D(+self.xd * 0.5 + self.xx, +self.yd * 0.5 + self.yy, -self.zd * 0.5 + self.zz) )
        cpoints.append( Vec3D(+self.xd * 0.5 + self.xx, -self.yd * 0.5 + self.yy, +self.zd * 0.5 + self.zz) )
        cpoints.append( Vec3D(-self.xd * 0.5 + self.xx, -self.yd * 0.5 + self.yy, +self.zd * 0.5 + self.zz) )
        cpoints.append( Vec3D(+self.xd * 0.5 + self.xx, +self.yd * 0.5 + self.yy, +self.zd * 0.5 + self.zz) )
        cpoints.append( Vec3D(-self.xd * 0.5 + self.xx, +self.yd * 0.5 + self.yy, +self.zd * 0.5 + self.zz) )
        return cpoints   
        
        
    def toMesh(self):
        return Mesh.meshFromVertices(self.points(), self.idx_array)
 
                    
    @classmethod         
    def boxFromMaxMin(clas, bmin, bmax):
        """
        Alternative constructor creates an instance of from min and max Vec3D
        """
        return Box((bmin.x + bmax.x/2.0),  (bmin.y +bmax.y/2.0),  (bmin.z + bmax.z/2.0),  abs(bmin.x - bmax.x),  abs(bmin.y - bmax.y),  abs(bmin.z - bmax.z))
        
    @classmethod         
    def createAcube(clas,  x,  y,  z,  sz):
        """
        Alternative constructor creates a special box, where side have equal length
        """
        return Box(x,  y,  z,  sz,  sz,  sz)    
