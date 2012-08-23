from pyprocessing import *
from math import pi, sin
from lsystems import csgrammar
from lsystems.arcball import ArcBall

myball = None          # needs exposure at module level
THETA = (6.5* pi)/36  #  32.5 degrees in radians
production = None   # needs exposure at module level
distance = 90
repeat = 1
count = 0
scale_factor = [0.55, 0.65, 0.72, 0.75, 0.8,  0.85]
AXIOM = 'F'
IGNORE = '[]+-^&3'
RULES = {
  'F': 'F[-EF[3&A]]E[+F[3^A]]',   # context free rule
  'F<E': 'F[&F[3+A]][^F[3-A]]'    # context sensitive rule 
}
    
def setup():
    """
    processing setup
    """
    size(800, 600)
    global production,  myball
    myball = ArcBall(width/2.0, height/2.0, (width - 20) * 0.5)
    myball.selectAxis(1)
    production = csgrammar.repeat(6, AXIOM, RULES, IGNORE)
    fill(0, 200, 0)
    noStroke()    

def draw():
    """
    Animate a 3D context free plant in processing/pyglet draw loop
    """
    background(20, 20, 180)
    lights()      
    translate(width/2.0, height * 0.8) 
    lightSpecular(204, 204, 204) 
    specular(255, 255, 255) 
    shininess(1.0)  
    update()  
    for val in production:
        evaluate(val)    
    
def __noop():
    pass

def __yawRight():
    global repeat
    rotateX(-THETA * repeat)
    repeat = 1
    
def __yawLeft():
    global repeat
    rotateX(THETA * repeat)
    repeat = 1
    
def __rollRight():
    global repeat
    rotateZ(-THETA * repeat)
    repeat = 1
    
def __rollLeft():
    global repeat
    rotateZ(THETA * repeat)
    repeat = 1
     
def __thriceRepeat():
    global repeat
    repeat = 3

def __pushStack():
    pushMatrix()
    
def __popStack():
    popMatrix()
    
def __drawRod():
    global distance,  count
    sides = 16
    radius1 = distance/6
    radius2 = distance/(6 *  scale_factor[count])
    angle = 0
    angleIncrement = TWO_PI / sides    
    beginShape(QUAD_STRIP)
    for i in range(sides+1):
        normal(cos(angle), 0, sin(angle))        
        vertex(radius2*cos(angle), 0, radius2*sin(angle))
        vertex(radius1*cos(angle), -distance, radius1*sin(angle))
        angle += angleIncrement
    endShape()        
    # draw the spherical top cap
    translate(0, -distance, 0)
    sphereDetail(16)
    sphere(radius1)
    if (count> 0):
        scale(scale_factor[count]);
    if (count< len(scale_factor) - 1):              
        count += 1
    
####
# A dictionary of lsystem operations 
####

lsysOp = {
    '+' : __yawRight,
    '-' : __yawLeft,
    '^' : __rollLeft,
    '&' : __rollRight,
    '3' : __thriceRepeat,
    'F' : __drawRod,
    '[' : __pushStack,
    ']' : __popStack,    
    'A' : __noop,   
    'E' : __noop  
}

def update():
    """
    wrap arcball update and rotation as a local function
    """
    theta,  x,  y,  z = myball.update()
    rotate(theta,  x,  y,  z)    
    
def mousePressed():
    myball.mousePressed(mouse.x, mouse.y)
  
def mouseDragged():
    myball.mouseDragged(mouse.x, mouse.y) 
    
def evaluate(key):
    """
    Is a wrapper controlling access to the dict of functions
    """
    if lsysOp.has_key(key):
        lsysOp[key]()
    else:
        if not RULES.has_key(key):        # useful debugging check you could
            print("Unknown rule {0}".format(key)) # comment out these lines        
run()        
