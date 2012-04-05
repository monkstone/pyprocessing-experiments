from pyprocessing import *
from util.cube import Cube

FOV = PI/3.0
angle = 0.0
ANGLE_STEP = PI / 180.0
menger = []

             

def setup():
    size(800,600)
    cameraZ = (height/2.0) / tan(FOV/ 2.0)
    perspective(FOV, float(width)/float(height), cameraZ/10.0, cameraZ*10.0)
    create_menger(0, 0, 0, height/2.0)
    
def draw():
    background(0,  0,  200)
    lights()
    defineLights()
    translate(width/2.0, height/2.0, 0)
    global angle,  menger
    angle = (angle + ANGLE_STEP) % TWO_PI
    rotateZ(angle)
    rotateY(angle)
    export_menger()
    #for cub in menger:
    #    draw_cube(cub)
    

def draw_cube(cube):
    """
    Draw a cube with centre xx, yy, zz and size sz
    """
    noStroke()
    beginShape(TRIANGLES)
    for vec in cube.mesh_array():
        vertex(vec.x, vec.y, vec.z)
    endShape()
    
def export_menger():
    f = open("menger.inc", 'w')
    global menger
    f.write("#declare mesh_objects = union{\n")
    for cub in menger: 
        f.write(cub.mesh2())
    f.write("}\n")        
    f.close()
    exit(0)
    

def create_menger(xx, yy, zz, sz):
    """
    Create a recursive menger sponge using my_cube
    """	
    u = sz / 3.0
    if (sz < 10):
        menger.append(Cube(xx, yy, zz, sz))
    else:
        for i in xrange(-1, 2, 1):
            for j in xrange(-1, 2, 1):
                for k in xrange(-1, 2, 1):
                    if ((abs(i) + abs(j) + abs(k)) > 1):
                        create_menger(xx + (i * u), yy + (j * u), zz + (k * u), u)
                        
def defineLights():
    """
    Without lights you wouldn't see the menger
    """
    ambientLight(50, 50, 50)
    pointLight(150, 100, 0, 200, -150, 0)
    directionalLight(0, 102, 255, 1, 0, 0)
    spotLight(255, 255, 109, 0, 40, 200, 0, -0.5, -0.5, PI / 2, 2)     
 

run()
    




