"""
Copyright (c) 2011 Martin Prout
 
This module is free software; you can redistribute it and/or
modify it under the terms of the GNU Lesser General Public
License as published by the Free Software Foundation; either
version 2.1 of the License, or (at your option) any later version.
http://creativecommons.org/licenses/LGPL/2.1/

context_rule.py module
"""
__all__ = ['ContextRule']

from random import random

class ContextRule(object):
    def __init__(self,  rule):
        object.__init__(self)
        self.weighting = {}
        self.rule = rule
    
    def add_expansion(self,  expansion,  weight = 1):
        self.weighting[expansion] = weight 
    
    def get_random_expansion(self):
        rand = random() 
        prob = 0
        tot = sum(self.weighting.values())
        for rule in self.weighting.keys():       # iterate over rule choices
            prob += self.weighting.get(rule)   # add assigned probalities
            if ((rand * tot) < prob):      # compare running total with scaled random value
                return rule
    
    def dump(self):        
        print(self.rule + " ->\n");
        for rle in self.weighting.keys():
            print('\t' + rle)
