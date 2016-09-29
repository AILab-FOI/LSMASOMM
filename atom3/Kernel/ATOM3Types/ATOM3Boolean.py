# __ File: ATOM3Boolean.py __________________________________________________________________________________________________
#  Implements  : class ATOM3Boolean
#  Author      : Juan de Lara
#  Description : This is the class for boolean types. It inherits from ATOM3Type
#  Modified    : 31 Dec 2001
#  Changes :
#      - 31 Dec 2001: Fixed bug in the setValue() and show() methods. In config mode, the widget did not show the display
#        text properly after a setValue()
# _____________________________________________________________________________________________________________________________
"""
if( booleanObject.getValue()[1] == 1 ): print 'True'
"""

from Tkinter import *

from ATOM3String     import *
from ATOM3Type       import *
from ATOM3Exceptions import *
from types import *

class ATOM3Boolean(ATOM3Type):

    def __init__(self, displayText = None, valInitial=None, config = 0 ):
       "The constructor still does nothing"
       ATOM3Type.__init__(self )			# call the ancestor constructor
       self.variable = IntVar()				# create an associate variable
       self.config   = config				# flag that tells us if we are configuring the item
       self.configText = None
       if self.config:					# if we are configuring the widget...
          self.configText = ATOM3String()		# create an ATOM3String to set some text...
       if valInitial: self.variable.set(valInitial)
       self.chkEntry = None				# widget to be created when show is called
       self.dspText  = displayText			# Store the display text
       self.containerFrame   = None			# frame with all the widgets
       self._isNone = 0

    def toString(self, maxWide = None, maxLines = None ):
       "returns a string with the widget value"
       if self.variable.get() == 0: return "False"
       else: return "True"

    def clone(self):
       "Makes an exact copy of itself"
       cloneObject = ATOM3Boolean(self.dspText, self.variable.get(), self.config)
       cloneObject.chkEntry = self.chkEntry
       cloneObject._isNone  = self._isNone
       return cloneObject

    def setNone(self):
       "Sets the widget to None"
       self._isNone = 1

    def isNone(self):
       "Returns if the widget is None"
       return self._isNone

    def unSetNone(self):
       "Sets the widget to None"
       self._isNone = 0

    def setValue(self, value):
       "Sets the actual attribute value. value is a tuple (displayText, value)"
       if type(value) == NoneType :
          self.setNone()
          return
       if type(value) == IntType :
          mvalue = ( None, value )
       elif(type(value) == type(True)):
         mvalue = (None, int(value))
       else: 
         mvalue = value
       if type(mvalue) != TupleType :
          raise ATOM3BadAssignmentValue, "in setValue(), tuple expected"
       elif len(mvalue) != 2:
          raise ATOM3BadAssignmentValue, "in setValue(), 2-element tuple expected"
       else:          
          if mvalue[0]:
             if type(mvalue[0]) != StringType:
                raise ATOM3BadAssignmentValue, "in setValue(), 1st tuple element should be a string"                
             else:
                self.dspText = mvalue[0]
                if self.chkEntry: chkEntry.config(text=self.dspText)
                if self.configText: self.configText.setValue(self.dspText)      # modified 31/12/2001
          if mvalue[1] != None:
             if type(mvalue[1]) != IntType:
                raise ATOM3BadAssignmentValue, "in setValue(), 2nd tuple element should be an integer"
             if mvalue[1] < 0 or mvalue[1] > 1:
                raise ATOM3BadAssignmentValue, "in setValue(), 2nd tuple element out of range"
             self.variable.set(mvalue[1])
             

    def getValue(self):
       "Gets the actual attribute value"
       return (self.dspText, self.variable.get())
       
    def getValueBoolean(self):
      """ Return the value as either a Python True or False """
      return self.variable.get() == 1

    def show(self, parent, parentWindow = None):
       "Creates an entry to show the value"

       ATOM3Type.show(self, parent)
       # check if we are configuring the item...
       if self.config:
          if not self.configText: self.configText = ATOM3String()
          if self.dspText: self.configText.setValue(self.dspText)       # modified 31/12/2001
          self.containerFrame = Frame(parent) 				# A frame to put the configuration widget (if it is the case)
          widget = self.configText.show(self.containerFrame)		# show the configuration widget
          widget.grid(row=0, column=0, sticky=W)
          self.chkEntry = Checkbutton(self.containerFrame, variable = self.variable)
          self.chkEntry.grid(row=0, column=1, sticky=W)
          return self.containerFrame
       else:
          if self.dspText: self.chkEntry = Checkbutton(parent, text = self.dspText, variable = self.variable)
          else: self.chkEntry = Checkbutton(parent, variable = self.variable )
          return self.chkEntry

    def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.variable.set(other.variable.get())
       self.chkEntry = other.chkEntry
       self.dspText  = other.dspText
       self.config   = other.config

    def destroy(self):
       "copies information to class attributes"
       if self.config:
          self.configText.destroy()
          self.dspText = self.configText.toString()	# get the configuration text

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+"=ATOM3Boolean()\n")
       if self.isNone():
          file.write(indent+objName+".setNone()\n")
       else:
          file.write(indent+objName+".setValue("+str(self.getValue())+")\n")
       if generatingCode:
          file.write(indent+objName+".config = 0\n" )
       else:
          file.write(indent+objName+".config = "+str(self.config)+"\n" )

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"

       if(self.isNone()):
          file.write(indent+objName+".setNone()\n")
       else:
          file.write(indent+objName+".setValue("+str(self.getValue())+")\n")
       
       if(generatingCode):
          file.write(indent+objName+".config = 0\n" )
       else:
          file.write(indent+objName+".config = "+str(self.config)+"\n" )
        
