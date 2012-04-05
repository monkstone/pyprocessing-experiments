"""
cube.py contains use lighweight Vec3D class to store indexed vector points 
by having public attributes (as does python default)
"""
from vec3d import Vec3D

class Cube(object):
    """
    A lightweight convenience class to store cube point data
    With a function to return indexed vector points 
    """
    
    def __init__(self, x = 0, y = 0,  z = 0,  sz = 1):
        """
        Initialise the new Vec3D object
        """
        self.xx= x
        self.yy = y 
        self.zz = z 
        self.sz = sz
        self.idx_array  = [1,  0,  2,  3,  1,  2,  5,  4,  6,  7,  5,  6,  4,  5,  0,  1,  4,  0,  7,  6,  2,  2,  6,  3,  0,  5,  7,  2,  0,  7,  4,  1, 6,  6,  1,  3]
    
    def points(self):
        """
        The unique corner points of cube (front + back order)
        """
        cpoints = [] 
        cpoints.append( Vec3D(-self.sz / 2.0 + self.xx, -self.sz / 2.0 + self.yy, -self.sz / 2.0 + self.zz) )  
        cpoints.append( Vec3D(+self.sz / 2.0 + self.xx, -self.sz / 2.0 + self.yy, -self.sz / 2.0 + self.zz) )
        cpoints.append( Vec3D(-self.sz / 2.0 + self.xx, +self.sz / 2.0 + self.yy, -self.sz / 2.0 + self.zz) )
        cpoints.append( Vec3D(+self.sz / 2.0 + self.xx, +self.sz / 2.0 + self.yy, -self.sz / 2.0 + self.zz) )
        cpoints.append( Vec3D(+self.sz / 2.0 + self.xx, -self.sz / 2.0 + self.yy, +self.sz / 2.0 + self.zz) )
        cpoints.append( Vec3D(-self.sz / 2.0 + self.xx, -self.sz / 2.0 + self.yy, +self.sz / 2.0 + self.zz) )
        cpoints.append( Vec3D(+self.sz / 2.0 + self.xx, +self.sz / 2.0 + self.yy, +self.sz / 2.0 + self.zz) )
        cpoints.append( Vec3D(-self.sz / 2.0 + self.xx, +self.sz / 2.0 + self.yy, +self.sz / 2.0 + self.zz) )
        return cpoints
        
    def mesh_array(self):
        """
        Returns array of Vec3D for use in pyprocessing
        """
        temp = []
        for i in self.idx_array:
            temp.append(self.points()[i])
        return temp
        
  
    def vert_index(self):
        return self.idx_array
        
    def vert_string(self,  pt):
        return "\t<{0}, {1}, {2}>,\n".format(pt.x,  pt.y,  pt.z)
        
    def vect_string(self,  x,  y,  z):
        return "\t<{0}, {1}, {2}>,\n".format(x,  y,  z)    
        
    def index_string(self,  idx):
        temp = []
        temp.append("\tface_indices {\n")
        temp.append("\t{0:d},\n".format(int(len(idx)/3)))   # need to coerce int?       
        for i in range(0, len(idx),  3):
            temp.append(self.vect_string(idx[i],  idx[i +1],  idx[i +2]))
        temp.append("\t}\n")    
        return "".join(temp)   
        
        
    def mesh2(self):
        """
        Returns a string of type mesh2 array for use in PovRAY
        """
        temp = []
        temp.append("mesh2{\n")
        temp.append("\tvertex_vectors {\n")
        temp.append("\t{0},\n".format(len(self.points())))
        for pt in self.points():
            temp.append(self.vert_string(pt))
        temp.append("\t}\n") 
        temp.append(self.index_string(self.idx_array))
        temp.append("}\n") 
        return "".join(temp)
                    
             

