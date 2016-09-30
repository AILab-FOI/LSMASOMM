# __ ATOM3String _________________________________________________________________________________
#  This is the class for String types. It inherites from ATOM3Type
#  Last Modified: 27/July/2002
#  Changes:
#   - 27/July/2002: Changed methods "writeConstructor2File" and "writeValue2File" in order to allow
#     saving strings with '\n' characters inside.
# ________________________________________________________________________________________________

from Tkinter import *

from ATOM3Type       import *
from ATOM3Exceptions import *
from types           import *
from string          import replace

class ATOM3String(ATOM3Type):

    def __init__(self, valInitial="", width=20):
       "The constructor still does nothing"
       ATOM3Type.__init__(self )
       self.strValue = str(valInitial)			# Attribute to store the value
       self.strEntry = None				# widget to be create when show is called       
       self.width = width # Number of chars that can be seen at once

    def isNone (self):
       "check if the type value is none"
       if self.strValue == '' or self.strValue == None: return 1
       return 0

    def setNone (self):
       "sets to None the attribute value"
       self.strValue = ''

    def setValue(self, value):
       "Sets the actual attribute value"
       # check that we have the correct type (a string)
       if type(value) != StringType and type(value) != NoneType:
          raise ATOM3BadAssignmentValue, "in setValue(), a string was expected"
       self.strValue = value
       if self.strEntry:
         self.strEntry.delete(0, END)			# delete from graphical field
         if value:
            self.strEntry.insert(0, value)		# insert into graphical field

    def getValue(self):
       "Gets the actual attribute value"
       if self.strEntry:
          self.strValue = self.strEntry.get()
       return self.strValue

    def toString(self, maxWide = None, maxLines = None ):
       "Returns the string representation of this type"
       if self.strEntry:
          self.strValue = self.strEntry.get()
       if self.strValue:
          if type(self.strValue) == StringType:
             if maxWide: return self.strValue[0:maxWide]
             elif self.strValue: return str(self.strValue)
          else: return str(self.strValue)
       else: return ""

    def show(self, parent, parentTopWindow = None ):
       "Creates an entry to show the value"
       ATOM3Type.show(self, parent, parentTopWindow )

       self.strEntry = Entry(parent, exportselection=0, width=self.width)
       self.strEntry.insert(0, self.strValue)
       return self.strEntry

    def destroy(self):
       "Stores the widget value into the variable"
       if self.strEntry:
          self.strValue = self.strEntry.get()
          self.strEntry = None

    def clone(self):
       "Makes an exact copy of this object"
       cloneObject = ATOM3String()
       cloneObject.parent   = self.parent
       cloneObject.mode     = self.mode
       cloneObject.strValue = self.strValue
       cloneObject.strEntry = self.strEntry
       cloneObject.width = self.width
       return cloneObject

    def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.strValue = other.strValue
       self.strEntry = other.strEntry
       self.width = other.width

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       replacedStr = self.toString()                                
       replacedStr = replace( replacedStr, '\\', '\\'+'\\')         
       replacedStr = replace( replacedStr, "'", "\\'")              
       replacedStr = replace( replacedStr, '\n', '\\n')             
       file.write(indent+objName+"=ATOM3String('"+replacedStr+"', "
                  +str(self.width)+")\n")       

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       replacedStr = self.toString()                               
       replacedStr = replace( replacedStr, '\\', '\\'+'\\')        
       replacedStr = replace( replacedStr, "'", "\\'")              
       replacedStr = replace( replacedStr, '\n', '\\n')             
       file.write(indent+objName+".setValue('"+replacedStr+"')\n")  
       if self.isNone():
         file.write(indent+objName+".setNone()\n")
         
                                 