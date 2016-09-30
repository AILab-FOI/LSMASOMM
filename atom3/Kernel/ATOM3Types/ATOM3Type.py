# __ ATOM3Type ____________________________________________________________________________________________
#  This is the base class for all types. It defines an API to access type values:
#    - setValue(value)
#    - getValue()
#    - isValid()
#    - show()
#    - getTypeName()
#  Changes:
#    - 6 August 2002: Added the subTypes and recursiveTypes static attributes, as well as isSubTypeOf method
# __________________________________________________________________________________________________________

from Tkinter import *
import string
from ATOM3TypeDialog import *
from types           import *
from ATOM3Exceptions import *

class ATOM3Type:

    subTypes = { "ATOM3String"     : ["ATOM3String"],
                   "ATOM3Integer"    : ["ATOM3Integer"],
                   "ATOM3Float"      : ["ATOM3Float", "ATOM3Integer"],
                   "ATOM3Attribute"  : ["ATOM3Attribute"],
                   "ATOM3Boolean"    : ["ATOM3Boolean"],
                   "ATOM3BottomType" : ["ATOM3Type"],
                   "ATOM3Connection" : ["ATOM3Connection"],
                   "ATOM3Constraint" : ["ATOM3Constraint"],
                   "ATOM3Action"     : ["ATOM3Action"],
                   "ATOM3Enum"       : ["ATOM3Enum"],
                   "ATOM3File"       : ["ATOM3File"],
                   "ATOM3Link"       : ["ATOM3Link"],
                   "ATOM3List"       : ["ATOM3List"],
                   "ATOM3MSEnum"     : ["ATOM3MSEnum"],
                   "ATOM3Port"       : ["ATOM3Port"] }
    recursiveTypes = ["ATOM3List"]
      
    def __init__(self):
       "The constructor just creates an attribute to store a reference to the parent"
       self.parent = None
       self.mode   = ATOM3TypeDialog.SHOW			# SHOW mode by default (valid modes are SHOW or OPEN)
       
    def getMode(self):
       "Returns the mode of the object"
       return self.mode

    def setMode(self, mode):
       "Sets the mode of the object, valid modes are SHOW or OPEN"
       self.mode = mode

    def hasEqualValue(self, obj):
       "checks if both objects have the same value"
       myValue  = self.getValue()			# get my value
       hisValue = obj.getValue()			# get his value
       type1    = type(myValue)				# my value type
       type2    = type(hisValue)			# his value type
       if type1 != type2: return 0			# cannot be equal
       if type1==TupleType:                     	# the 1st is a tuple!
          return myValue[0] == hisValue[0]		# if tuples, compare the first value
       else:
          return myValue == hisValue		

    def isNone(self):
       "Returns 0 if the value stored in the type is considered None, another Value otherwise. Must be overriden"
       pass

    def setNone(self):
       "Sets to None the value of the Type"
       pass

    def unSetNone(self):
       "sets the _isNone flag to 0"
       pass

    def getValue(self):
       "This is an abstract method, must be overriden to return the actual attribute value"
       pass

    def setValue(self, value):
       "This is an abstract method, must be overriden to set the actual attribute value"
       pass

    def invalid(self):
       "This is an abstract method, must be overriden to decide if the value is valid (returns 1) or invalid (return 0)"
       return None					# valid by default

    def show(self, parent, parentWindow = None):
       "This method is used to create some editable widget, must be extended"
       if not self.parent:
          self.parent = parent
       return None

    def open(self, parent, parentWindow = None):
       "This method is exactly the same as show()"
       return self.show(parent, parentWindow)

    def destroy(self):
       "Nothing to do by default, must be overriden"
       pass

    def clone(self):
       "creates an exact copy of itself"
       cloneObject        = ATOM3Type()
       cloneObject.parent = self.parent
       cloneObject.mode   = self.mode
       return cloneObject

    def copy(self, other):
       "copies each field of the other object into its own state"
       self.parent = other.parent
       self.mode   = other.mode

    def getTypeName(self):
       "Method that returns a string with the type name"
       return self.__class__.__name__

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+"=ATOM3Type()\n")

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       pass
      
    def toString(self, maxWide = None, maxLines = None ):
       pass

    def isSubTypeOf(type1, type2): # <--- blatantly illegal construct! -Denis
       """
          Static method which sees if type1 (a string) is a subtype of type2
          Returns 1: if type1 is a subtype of type2
       """
       if self.subTypes.has_key(type1):
           if not ( type2 in self.subTypes[type1]):
              return 0
       elif type1 != type2:
          return 0
       return 1
     
     
def isSubTypeOfByDenis(type1String, type2String):
  """
  Another version of isSubTypeOf that follows legal Python syntax...
  Returns 1 if type1 (a string) is a subtype of type2
  Returns 0 otherwise
  """
  if(ATOM3Type.subTypes.has_key(type1String)):
    if(not (type2String in ATOM3Type.subTypes[type1String])):
      return 0
  elif(type1String != type2String):
    return 0
  return 1
