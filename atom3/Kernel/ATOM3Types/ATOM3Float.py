# __ ATOM3Float _________________________________________________________________________________
#  This is the class for Float types. It inherits from ATOM3Type
# ________________________________________________________________________________________________

from Tkinter         import *
from ATOM3Exceptions import *
from ATOM3Type       import *

class ATOM3Float(ATOM3Type):
    def __init__(self, valInitial = 0.0 ):
       "The constructor still does nothing"
       ATOM3Type.__init__(self )
       self.fltValue = valInitial			# Attribute to store the value
       self.fltEntry = None				# widget to be create when show is called
       self._isNone = 0					# for the moment it is not none

    def isNone (self):
       "check if the type value is none"
       return self._isNone

    def setNone (self):
       "sets to None the attribute value to 1"
       self._isNone  = 1
       self.fltValue = 0.0

    def unSetNone (self):
       "sets to None the attribute value to 0"
       self._isNone = 0

    def setValue(self, value):
       "Sets the actual attribute value"
       # check that we have the correct type (a float)
       if type(value) == NoneType:
          self.setNone()
          return
       if type(value) != FloatType and type(value) != IntType:
          raise ATOM3BadAssignmentValue, "in setValue(), a float was expected"
       self.fltValue = value
       if self.fltEntry:
         self.fltEntry.delete(0, END)			# delete from graphical field
         if value:
            self.fltEntry.insert(0, str(value))		# insert into graphical field

    def getValue(self):
       "Gets the actual attribute value"
       if self.fltEntry:
          try:
             self.fltValue = float(self.fltEntry.get())
          except ValueError:
             raise ATOM3BadAssignmentValue, "in getValue(), wrong value!"
       if type(self.fltValue) != FloatType and type(self.fltValue) != IntType:
          raise ATOM3BadAssignmentValue, "in getValue(), wrong value!"
       return self.fltValue

    def invalid(self):
        "Decides if the value is a valid float (returns 1) or not (return 0)"
        try:
           float(self.getValue())
        except ATOM3BadAssignmentValue:
           return "wrong float value!"
	return None
	
    def toString(self, maxWide = None, maxLines = None ):
       "Returns the string representation of this type"
       if self.fltEntry:
          try:
             self.fltValue = self.getValue()
          except ATOM3BasAssignmentValue:
             raise ATOM3BadAssignmentValue, "in toString(), wrong value!"
       if self.fltValue != None:
          if maxWide: return str(self.fltValue)[0:maxWide]
          elif self.fltValue != None: return str(self.fltValue)
       else: return ""

    def show(self, parent, parentTopWindow = None ):
       "Creates an entry to show the value"
       ATOM3Type.show(self, parent, parentTopWindow )

       self.fltEntry = Entry(parent)
       self.fltEntry.insert(0, str(self.fltValue))
       return self.fltEntry

    def destroy(self):
       "Stores the widget value into the variable"
       if self.fltEntry:
          try:
             self.fltValue = self.getValue()
          except ATOM3BasAssignmentValue:
             return "wrong float value!"
          self.fltEntry = None

    def clone(self):
       "Makes an exact copy of this object"
       cloneObject = ATOM3Float()
       cloneObject.parent   = self.parent
       cloneObject.mode     = self.mode
       cloneObject.fltValue = self.fltValue
       cloneObject.fltEntry = self.fltEntry
       cloneObject._isNone  = self._isNone
       return cloneObject

    def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.fltValue = other.fltValue
       self.fltEntry = other.fltEntry
       self._isNone  = other._isNone

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+"=ATOM3Float("+self.toString()+")\n")
       if self.isNone():
          file.write(indent+objName+".setNone()\n")

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       if self.isNone():
          file.write(indent+objName+".setNone()\n")
       else:
          file.write(indent+objName+".setValue("+self.toString()+")\n")
          
