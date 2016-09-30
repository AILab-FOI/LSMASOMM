# __ ATOM3Port _________________________________________________________________________________
#  This is the class for Ports. It inherits from ATOM3String
#  Created 24 July 2002.
#  Changes:
#                                          
# ________________________________________________________________________________________________

from Tkinter         import *
from ATOM3Exceptions import ATOM3BadAssignmentValue
from ATOM3Type       import ATOM3Type
from ATOM3String     import ATOM3String
import string

class ATOM3Port(ATOM3Type):
    def __init__(self):
        """
           A Port has no attributes.
        """
        ATOM3Type.__init__(self )
        self._isNone = 0					# for the moment it is not none

    def isNone (self):
        """
           check if the type value is none
        """
        return self._isNone

    def setNone (self):
        """
           sets to None the attribute value
        """
        self._isNone  = 1

    def unSetNone (self):
        """
           sets to None the attribute value to 0
        """
        self._isNone = 0

    def setValue(self, value):
        """
           Sets the actual attribute value
        """
        if value == None: self.setNone()

    def getValue(self):
        """
           Returns the actual attribute value
        """
        if self.isNone(): return None
        else: return ()

    def toString(self, maxWide = None, maxLines = None ):
        """
           Returns the string representation of this type
        """
        if self.isNone(): return ""
        else: return "Port"

    def show(self, parent, parentTopWindow = None ):
        """
           Creates a widget to show the value
        """
        ATOM3Type.show(self, parent, parentTopWindow )
        return Label(parent,text="Port")					# creates just an empty frame with "Port"


    def destroy(self):
        """
           Stores the widget value into the variable
        """
        pass

    def clone(self):
        """
           Makes an exact copy of this object
        """
        cloneObject = ATOM3Port()
        cloneObject.parent   = self.parent
        cloneObject.mode     = self.mode
        cloneObject._isNone  = self.isNone
        return cloneObject

    def copy(self, other):
        """
           copies each field of the other object into its own state
        """
        ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
        self._isNone = other._isNone

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       """
          Method that writes into a file the constructor and the value of the object.
       """
       file.write(indent+objName+"=ATOM3Port()\n")

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       """
          Method that writes into a file the constructor and the value of the object.
       """
       pass
       
    def invalid(self):
        """
           This must be a valid variable name
        """
        return None

	
