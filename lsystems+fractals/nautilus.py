from pyprocessing import *
  
A = 0.8
B = 1.4
pvect = []

def getX(theta):
    return A * cos(theta)*exp(theta/tan(B))

def getY(theta):
    return A * sin(theta)*exp(theta/tan(B))  

def setup():
    size(400, 400)
    background(255)
    translate(width/2, height/3)
    rotate(0.75 * pi)
    for i in xrange(41):
        x = getX(i*A)
        y = getY(i*A)
        pvect.append(PVector(x, y))
    for z in xrange(8, len(pvect)):
        tmp0 = pvect[z]
        tmp1 = pvect[z - 1]
        tmp2 = pvect[z - 8]
        tmp3 = pvect[z - 7]
        x0 = tmp0.x
        y0 = tmp0.y
        x1 = tmp1.x # we would have negative increments otherwise
        y1 = tmp1.y   
        x2= tmp2.x
        y2 = tmp2.y
        x3= tmp3.x # we would have negative increments otherwise
        y3 = tmp3.y 
        curveTightness(-0.8)    
        curve( x0, y0, x1, y1, x2, y2, x3, y3) # draw the radial lines

    strokeWeight(4)
    stroke(255, 0, 0)
    noFill()
    curveTightness(0.0)   
    beginShape() # begin spiral 'shell' shape
    for v in range(0, len(pvect)):
        tmp = pvect[v]
        curveVertex(tmp.x, tmp.y) # successive calls to curveVertex a variation on curve?  
    endShape()        
        
run()        
