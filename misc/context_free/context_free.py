import re
from context_rule import ContextRule

RECURSION_LIMIT = 100

class ContextFree(object):
    """
    You could inherit from this class to create your own generator, override render_expansion
    """
    def __init__(self):
        """
        Initialise an instance of ContextFree
        """
        object.__init__(self)
        self.limit = RECURSION_LIMIT
        self.count = 0
        self.rules ={}

    def add_rule(self,  rule,  expansion,  weight = 1):
        """
        Add a weighted rule (default of 1) actual weighting depends on total, sensible to
        use either decimal or % weighting (don't use % symbol that would be silly)
        """
        if (self.rules.has_key(rule)):
            cr = self.rules[rule]
            cr.add_expansion(expansion,  weight)
        else:
            cr = ContextRule(rule)
            cr.add_expansion(expansion,  weight)
            self.rules[rule] = cr

    def expand(self, current):
        """
        Expand current rule, unless no more expansions, or at recursion limit
        """
        self.count += 1
        if (not self.rules.has_key(current)):
            self.render_expansion(current)
        else:
            if (self.count <= self.limit):
                cr = self.rules[current]
                pattern = re.compile(' ')
                to_expand = pattern.split(cr.get_random_expansion())
                for rule in to_expand:
                    self.expand(rule)
            else:
                print "reached recursion limit!"
    
    def render_expansion(self, s):
        """
        Override this method to do something more edifying like render shape in pyprocessing
        """
        print(s)
    
    def dump(self):
        """
        Handy method for debugging / presentation
        """
        for rule in self.rules.keys():
            cr = self.rules[rule]
            cr.dump()


def main():
    """
    Hommage to the Adam Parrish original, also saves my imagination for something more
    edifying (Note the context is set by first rule NP precedes VP)
    """
    cf = ContextFree()
    cf.add_rule("S", "NP VP")
    cf.add_rule("NP", "the N")
    cf.add_rule("N", "cat")
    cf.add_rule("N", "dog")
    cf.add_rule("N", "weinermobile")
    cf.add_rule("N", "duchess")
    cf.add_rule("VP", "V the N")
    cf.add_rule("V", "sees")
    cf.add_rule("V", "chases")
    cf.add_rule("V", "lusts after")
    cf.add_rule("V", "blames")
    cf.expand("S")
    
if __name__ == "__main__":
    main()
