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
