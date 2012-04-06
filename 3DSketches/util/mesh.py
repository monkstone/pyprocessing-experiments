"""
mesh.py contains use lighweight Vec3D class to store unique vector points
and correspondindg mesh indices 
"""

class Mesh(object):
    """
    A lightweight convenience class to store mesh point data
    With a function to return indexed vector points 
    """
      
    def __init__(self, name = "mesh0"):
        """
        Initialise the new Mesh object
        """
        self.name = name  
        self.vertex_index = []
        self.vertices = []
        
    def setVertices(self,  vertices):
       self.vertices = vertices
       
    def setVertexIndex(self,  idx):
       self.vertex_index = idx   
        
    def mesh_array(self):
        """
        Returns array of Vec3D for use in pyprocessing
        """
        temp = []
        for i in self.vertex_index:
            temp.append(self.vertices[i])
        return temp        
        
    def vert_string(self,  pt):
        """
        helper function that returns PovRAY vector string from a Vec3D
        """
        return "\t<{0}, {1}, {2}>,\n".format(pt.x,  pt.y,  pt.z)
        
    def vect_string(self,  x,  y,  z):
        return "\t<{0}, {1}, {2}>,\n".format(x,  y,  z)    
        
    def index_string(self,  idx):
        """
        PovRAY formatted face indices as string
        """
        temp = []
        temp.append("\tface_indices {\n")
        temp.append("\t{0:d},\n".format(int(len(idx)/3)))   # need to coerce int?       
        for i in xrange(0, len(idx),  3):
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
        temp.append("\t{0},\n".format(len(self.vertices)))
        for pt in self.points():
            temp.append(self.vert_string(pt))
        temp.append("\t}\n") 
        temp.append(self.index_string(self.vertex_index))
        temp.append("}\n") 
        return "".join(temp)
                    
    @classmethod         
    def meshFromVertices(clas, vertices, vertex_index):
        """
        Alternative constructor creates an instance of from vertex array and vertex indices
        """
        temp = Mesh()
        temp.setVertexIndex(vertex_index)
        temp.setVertices(vertices)
        return temp
        

