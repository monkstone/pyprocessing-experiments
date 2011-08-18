from context_free.context_free import ContextFree

BEGIN = """
from pyprocessing import *
\"\"\"
pyprocessing sketch from a set of rules
\"\"\"


def setup():
    \"\"\"
    Processing setup
    \"\"\"
    size(600, 600)
    translate(width/2, height/2)
    background(255)
    fill(100, 0, 0, 20)
"""

END = """
run()
"""

class PyGenerate(ContextFree):
    def __init__(self):
        ContextFree.__init__(self)

    def render_expansion(self, s):
        """
        Override this method to do something more edifying like render shape in pyprocessing
        """
        if (s == "push"):
            print("\tpushMatrix()")
        elif (s == "pop"):
            print("\tpopMatrix()")
        elif (s == "left"):
            print("\ttranslate(-125, 0)")
        elif (s == "right"):
            print("\ttranslate(125, 0)")
            print("\tscale(0.45)")
        elif (s == "square"):
            print("\trect(0, 0, 500, 500)")
        elif (s == "scale"):
            print("\tscale(0.75)")
        elif (s == "circle"):
            print("\tellipse(0, 0, 500, 500)")
        elif (s == "triangle"):
            print("\ttriangle(-250, 250/sqrt(3), 0, -500/sqrt(3), 250, 250/sqrt(3))")
        elif (s == "rotate"):
            print("\trotate(radians(45))")
        else:
            print("unexpected syntax")
            
      

def main():
    """
    Hommage to Adam Parrish original, test also saves my imagination for something more
    edifying
    """
    pdeg = PyGenerate()
    pdeg.add_rule("Drawing", "Square")
    pdeg.add_rule("Square", "square")
    pdeg.add_rule("Triangle", "triangle")
    pdeg.add_rule("Square", "Triangle")
    pdeg.add_rule("Triangle", "Square Triangle")
    pdeg.add_rule("Square", "square scale circle rotate Square square")
    pdeg.add_rule("Triangle", "square scale circle rotate triangle triangle")
    pdeg.add_rule("Triangle", "square scale triangle scale triangle")
    pdeg.add_rule("Square", "square scale Square")
    pdeg.add_rule("Square", "square push left Square pop push right Square pop")
    pdeg.add_rule("Square", "square scale circle rotate square")
    pdeg.add_rule("Triangle", "square scale Triangle scale triangle")
    pdeg.add_rule("Square", "square scale Square")
    pdeg.add_rule("Square", "square push left Square pop push right Square pop")
    print(BEGIN)
    pdeg.expand("Drawing")
    print(END)
    
if __name__ == "__main__":
    main()
