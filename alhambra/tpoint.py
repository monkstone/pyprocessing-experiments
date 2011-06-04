"""
tpoint.py contains my lighweight TPoint class avoids accessors 
by having public attributes (as do python default)
"""

class TPoint(object):
    """
    A lightweight convenience class to store triangle point data
    With a function to return new instance a the mid point between 
    two TPoint objects
    """
    
    def __init__(self, x = 0, y = 0):
        """
        Initialise the new TPoint object
        """
        self.x = x
        self.y = y 
        
        
    def mid_point(self, tvector):
        """ 
        Directly define mid point, sinc lerp is not automatically available to us.
        """
        return TPoint((self.x + tvector.x)/2, (self.y + tvector.y)/2)
        
        
    def add(self, tvector):
        """
        Adds tvector TPoints to self
        """
        self.x += tvector.x
        self.y += tvector.y  
  
