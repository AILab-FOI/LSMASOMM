# __ ATOM3Integer _________________________________________________________________________________
#  This is the class for Integer types. It inherits from ATOM3Type
#  Changes:
#   - 17 July 2002: Line 92: Corrected typo: "except ATOM3BasAssignmentValue:" by "except ATOM3BadAssignmentValue:"
#                                           
# ________________________________________________________________________________________________

from Tkinter         import *
from ATOM3Exceptions import *
from ATOM3Type       import *

class ATOM3Integer(ATOM3Type):
    def __init__(self, valInitial = 0 ):
       "The constructor still does nothing"
       ATOM3Type.__init__(self )
       self.intValue = valInitial			# Attribute to store the value
       self.intEntry = None				# widget to be create when show is called
       self._isNone = 0					# for the moment it is not none

    def isNone (self):
       "check if the type value is none"
       return self._isNone

    def setNone (self):
       "sets to None the attribute value"
       self._isNone  = 1
       self.intValue = 0

    def unSetNone (self):
       "sets to None the attribute value to 0"
       self._isNone = 0

    def setValue(self, value):
       "Sets the actual attribute value"
       # check that we have the correct type (an integer or None)
       if type(value) == NoneType:
          self.setNone()
          return
       if not type(value) in [IntType,NoneType] :
          raise ATOM3BadAssignmentValue, "in setValue(), an integer was expected"
       if value == None:
          self._isNone = 1
          self.intValue = 0
       else:
          self.intValue = value
          if self.intEntry:
            self.intEntry.delete(0, END)			# delete from graphical field
            if value:
               self.intEntry.insert(0, str(value))		# insert into graphical field

    def getValue(self):
       "Gets the actual attribute value"
       if self.intEntry:
          try:
             self.intValue = int(self.intEntry.get())
          except ValueError:
             raise ATOM3BadAssignmentValue, "in getValue(), wrong value!"
       if type(self.intValue) != IntType:
          raise ATOM3BadAssignmentValue, "in getValue(), wrong value!"
       return self.intValue

    def invalid(self):
        "Decides if the value is a valid integer (returns 1) or not (return 0)"
        try:
           int(self.getValue())
        except ATOM3BadAssignmentValue:
           return "wrong integer value!"
	return None
	
    def toString(self, maxWide = None, maxLines = None ):
       "Returns the string representation of this type"
       if self.intEntry:
          try:
             self.intValue = self.getValue()
          except ATOM3BasAssignmentValue:
             raise ATOM3BadAssignmentValue, "in toString(), wrong value!"
       if self.intValue != None:
          if maxWide: return str(self.intValue)[0:maxWide]
          elif self.intValue != None: return str(self.intValue)
       else: return ""

    def show(self, parent, parentTopWindow = None ):
       "Creates an entry to show the value"
       ATOM3Type.show(self, parent, parentTopWindow )

       self.intEntry = Entry(parent)
       self.intEntry.insert(0, str(self.intValue))
       return self.intEntry

    def destroy(self):
       "Stores the widget value into the variable"
       if self.intEntry:
          try:
             self.intValue = self.getValue()
          except ATOM3BadAssignmentValue:
             return "wrong integer value!"
          self.intEntry = None

    def clone(self):
       "Makes an exact copy of this object"
       cloneObject = ATOM3Integer()
       cloneObject.parent   = self.parent
       cloneObject.mode     = self.mode
       cloneObject.intValue = self.intValue
       cloneObject.intEntry = self.intEntry
       cloneObject._isNone  = self._isNone
       return cloneObject

    def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.intValue = other.intValue
       self.intEntry = other.intEntry
       self._isNone  = other._isNone

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+"=ATOM3Integer("+self.toString()+")\n")
       if self.isNone():
          file.write(indent+objName+".setNone()\n")

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       if self.isNone():
          file.write(indent+objName+".setNone()\n")
       else:
          file.write(indent+objName+".setValue("+self.toString()+")\n")

