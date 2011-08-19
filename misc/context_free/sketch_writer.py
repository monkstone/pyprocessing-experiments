filename = "test.py"
 
BEGIN = """
from pyprocessing import *
\"\"\"
pyprocessing sketch from a set of rules
\"\"\"
SQRT3=sqrt(3)

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

INDENT="    "
EOL = '\n'
class SketchWriter(object):
    def __init__(self, filename):
        self.file = open(filename, 'w')
    def begin(self):
        self.file.write(BEGIN)
    def append(self, line):
        self.file.write(INDENT)
        self.file.write(line)
        self.file.write(EOL)
    def end(self):
        self.file.write(END)  
        self.file.close()

def test():
    fred = SketchWriter(filename)
    fred.begin()
    fred.append("gut")
    fred.end()

if __name__ == "__main__":
    test()
