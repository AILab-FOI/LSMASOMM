# __ ATOM3BottomType _________________________________________________________________________________
#  This is the class for the ATOM3BottomType type. It inherites from ATOM3Type
# ____________________________________________________________________________________________________

from Tkinter import *

from ATOM3Type import *
from types import *

class ATOM3BottomType(ATOM3Type):

    def __init__(self):
       "The constructor still does nothing"
       ATOM3Type.__init__(self )

    def isNone (self):
       "check if the type value is none (which is always the case)"
       return 1

    def setNone (self):
       "sets to None the attribute value"
       pass

    def setValue(self, value = None):
       "Sets the actual attribute value, any value is ignored, because variables of this type are always None"
       pass

    def getValue(self):
       "Gets the actual attribute value"
       return None

    def toString(self, maxWide = None, maxLines = None ):
       "Returns the string representation of this type"
       return ""

    def show(self, parent, parentTopWindow = None ):
       "Creates an entry to show the value"
       ATOM3Type.show(self, parent, parentTopWindow )
       return Label(parent,text="None")					# creates just an empty frame with None

    def destroy(self):
       "Stores the widget value into the variable"
       pass

    def clone(self):
       "Makes an exact copy of this object"
       cloneObject = ATOM3BottomType()
       return cloneObject						# nothing to clone

    def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)					# call the ancestor (copies the parent field)

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+"=ATOM3BottomType()\n")

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       pass


