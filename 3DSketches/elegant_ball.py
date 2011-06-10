"""
elegant_ball.py
Another opengl sketch from lazydog translated to pyprocessing by monkstone.
Suggestions for avoiding the PVector class method mult by Claudio Esperanca 
http://lazydog-bookfragments.blogspot.com/2009/05/final-version-of-ball-of
-confusion-for.html
"""


from pyprocessing import *
from math import sin, sqrt, pi
import time

# define PHI as the Golden Ratio constant
PHI = (1 + sqrt(5))/2

def setup():
    """
    processing setup
    """
    size(800, 800)
    colorMode(RGB, 1)
    
    
def draw():
    """
    processing draw loop
    """
    background(0)
    # Move the origin so that the scene is centered on the screen.
    translate(width/2, height/2, 0.0)
    # Set up the lighting.
    setupLights()
    # Rotate the local coordinate system.
    smoothRotation(5.0, 6.7, 7.3)
    # Draw the inner object.
    noStroke()
    fill(smoothColour(10.0, 12.0, 7.0))
    drawIcosahedron(5, 60.0, False)
    # Rotate the local coordinate system again.
    smoothRotation(4.5, 3.7, 7.3)
    # Draw the outer object.
    stroke(0.2)
    fill(smoothColour(6.0, 9.2, 0.7))
    drawIcosahedron(5, 200.0, True)
    
    
def setupLights():
    """
    Setup lights
    """
    ambientLight(0.2, 0.2, 0.2)
    directionalLight(0.2, 0.2, 0.2, -1, -1, -1)
    spotLight(1.0, 1.0, 1.0, -200, 0, 300, 1, 0, -1, pi/4, 20)
    
    

def smoothVector(s1, s2, s3):
    """
    Generate a vector whose components change smoothly over time in the range 
    [ 0, 1 ]. Each component uses a sin() function to map the current time
    in milliseconds somewhere in the range [ 0, 1 ].A 'speed' factor is 
    specified for each component.
    """
    mills = time.time() * 0.03 
    x = 0.5 * sin(mills * s1) + 0.5
    y = 0.5 * sin(mills * s2) + 0.5
    z = 0.5 * sin(mills * s3) + 0.5
    return PVector(x, y, z)
    

def smoothColour(s1, s2, s3):
    """
    Generate a colour which smoothly changes over time.
    The speed of each component is controlled by the parameters s1, s2 and s3.
    """
    v = smoothVector(s1, s2, s3)
    return color(v.x, v.y, v.z)    
    

def smoothRotation(s1, s2, s3):
    """
    Rotate the current coordinate system.
    Uses smoothVector() to smoothly animate the rotation.
    """
    r1 = smoothVector(s1, s2, s3) 
    rotateX(2.0 * pi * r1.x)
    rotateY(2.0 * pi * r1.y)
    rotateX(2.0 * pi * r1.z)   
    

def drawIcosahedron(depth, r, spherical):
    """
    Draw an icosahedron defined by a radius r and recursive depth d.
    Geometry data will be saved into dst. If spherical is true then the 
    icosahedron is projected onto the sphere with radius r.
    """

    # Calculate the vertex data for an icosahedron inscribed by a sphere radius
    # 'r'.  Use 4 Golden Ratio rectangles as the basis.
    h = r / sqrt(1.0 + PHI * PHI)
    v = [
        PVector(0, -h, h * PHI), PVector(0, -h, -h * PHI), PVector(0, h, -h * PHI), PVector(0, h, h * PHI),
        PVector(h, -h * PHI, 0), PVector(h, h * PHI, 0), PVector(-h, h * PHI, 0), PVector(-h, -h * PHI, 0),
        PVector(-h * PHI, 0, h), PVector(-h * PHI, 0, -h), PVector(h * PHI, 0, -h), PVector(h * PHI, 0, h)
    ]    
    
    # Draw the 20 triangular faces of the icosahedron.
    if (not spherical):
        r = 0.0          
          
    beginShape(TRIANGLES)
    
    drawTriangle(depth, r, v[0], v[7], v[4])
    drawTriangle(depth, r, v[0], v[4], v[11])
    drawTriangle(depth, r, v[0], v[11], v[3])
    drawTriangle(depth, r, v[0], v[3], v[8])
    drawTriangle(depth, r, v[0], v[8], v[7])
    
    drawTriangle(depth, r, v[1], v[4], v[7])
    drawTriangle(depth, r, v[1], v[10], v[4])
    drawTriangle(depth, r, v[10], v[11], v[4])
    drawTriangle(depth, r, v[11], v[5], v[10])
    drawTriangle(depth, r, v[5], v[3], v[11])
    drawTriangle(depth, r, v[3], v[6], v[5])
    drawTriangle(depth, r, v[6], v[8], v[3])
    drawTriangle(depth, r, v[8], v[9], v[6])
    drawTriangle(depth, r, v[9], v[7], v[8])
    drawTriangle(depth, r, v[7], v[1], v[9])
    
    drawTriangle(depth, r, v[2], v[1], v[9])
    drawTriangle(depth, r, v[2], v[10], v[1])
    drawTriangle(depth, r, v[2], v[5], v[10])
    drawTriangle(depth, r, v[2], v[6], v[5])
    drawTriangle(depth, r, v[2], v[9], v[6])
    
    endShape()  
  

def drawTriangle(depth, r, p1, p2, p3):
    """
    Draw a triangle either immediately or subdivide it first.
    If depth is 1 then draw the triangle otherwise subdivide first.
    """
    if (depth == 1):
        vertex(p1.x, p1.y, p1.z)
        vertex(p2.x, p2.y, p2.z)
        vertex(p3.x, p3.y, p3.z)
        
    else:
        # Calculate the mid points of this triangle.
        v1 = (p1 + p2) * 0.5  # was PVector.mult(PVector.add(p1, p2), 0.5)
        v2 = (p2 + p3) * 0.5  # was PVector.mult(PVector.add(p2, p3), 0.5)
        v3 = (p3 + p1) * 0.5  # was PVector.mult(PVector.add(p3, p1), 0.5)
        if (r != 0.0):
            # Project the verticies out onto the sphere with radius r.
            v1.normalize()
            v1.mult(r)
            v2.normalize()
            v2.mult(r)
            v3.normalize()
            v3.mult(r)
        ## Generate the next level of detail
        depth -= 1
        drawTriangle(depth, r, p1, v1, v3)
        drawTriangle(depth, r, v1, p2, v2)
        drawTriangle(depth, r, v2, p3, v3)
        # Uncomment out the next line to include the central part of the triangle.
        #drawTriangle(depth, r, v1, v2, v3)  

run()


