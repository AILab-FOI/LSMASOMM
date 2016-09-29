from CustomCode import *
import inspect

def dube(self):
    if(self.name.getValue() == 'Dube'):
        print "$$$$$ wrong $$$$$"
        return ("No Dube's allowed", self.graphObject_)

test = inspect.getsource(NameTesting)

print test