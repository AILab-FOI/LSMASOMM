# __ ATOM3File ___________________________________________________________________________________
#  This is the class for Files. It has a similar functionality than tkFileDialog, but wrapped
# as an ATOM3 basic type.
# ________________________________________________________________________________________________

from Tkinter         import *
from ATOM3Type       import *
from ATOM3TypeDialog import *
from ATOM3Exceptions import *
from types           import *
from ATOM3String import *

from FilePaths       import USER_MODEL_PATH
import os


import tkFileDialog

import copy

class ATOM3File(ATOM3Type):

    # modes in which this type can be used

    OPENFILE = 0
    SAVEFILE = 1
    
    USER_AREA = os.path.split(USER_MODEL_PATH)[0]

    def __init__(self, fileTypes=[("Python files", "*.py")], mode = OPENFILE ):
       "The constructor for ATOM3Files"
       ATOM3Type.__init__(self )
       self.fileName=ATOM3String('')
       self.Directory=ATOM3String('')
       self.fileTypes    = fileTypes				# store the file types
       self.modeOpen     = mode					# store the mode
       self._isNone      = 1					# by default it is none

    def isNone (self):
       "check if the type value is none"
       return self._isNone

    def setNone (self):
       "sets to None the attribute value"
       self._isNone = 1

    def unSetNone (self):
       "sets to None the attribute value"
       self._isNone = 0

    def setValue(self, value):
       "Sets the actual attribute value"
       # check that we have the correct type (a string)
       if type(value) != TupleType and type(value) != NoneType:
          raise ATOM3BadAssignmentValue, "in setValue(), a 2-element tuple was expected"
       self.fileName.setValue (value[0])
       self.Directory.setValue(value[1])

    def getValue(self):
       "Gets the actual attribute value"
       return (self.fileName.getValue(), self.Directory.getValue())

    def toString(self, maxWide = None, maxLines = None ):
       "Returns the string representation of this type"
       if maxWide: return self.fileName.toString()[0:maxWide]
       else: return self.fileName.toString()

    def show(self, parent, parentWindowInfo = None ):
       "Creates an entry to show the value"
       ATOM3Type.show(self, parent, parentWindowInfo )

       self.containerFrame = Frame(parent)
       Label(self.containerFrame, text='fileName').grid(row=0,column=0,sticky=W)
       self.fileName.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
       Label(self.containerFrame, text='Directory').grid(row=1,column=0,sticky=W)
       self.Directory.show(self.containerFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
       Button(self.containerFrame, text = "Browse", command = self.browseFile ).grid(row=2,column=1,sticky=W)
       return self.containerFrame

    def browseFile(self):
       "Opens a dialog window to browse a file"
       if self.mode == self.OPENFILE:
          fileName = tkFileDialog.askopenfilename(filetypes=self.fileTypes
                              ,initialdir=ATOM3File.USER_AREA)	  # ask for the file name
       else:
          fileName = tkFileDialog.asksaveasfilename(filetypes=self.fileTypes
                              ,initialdir=ATOM3File.USER_AREA)# ask for the file name
       if fileName:									  # if the user pressed ok...
          dir, file   = os.path.split(fileName)                                           # split path and file name
          self.Directory.setValue(dir)
          self.fileName.setValue(file)
          ATOM3File.USER_AREA = dir

    def destroy(self):
       "Stores the widget value into the variable"
       self.fileName.destroy()
       self.Directory.destroy()

    def clone(self):
       "Makes an exact copy of this object"
       cloneObject = ATOM3File(self.fileTypes, self.mode)
       cloneObject.parent       = self.parent
       cloneObject.modeOpen     = self.modeOpen     		# store the mode
       cloneObject.fileName	= self.fileName.clone() 	# file that's been selected
       cloneObject.Directory    = self.Directory.clone()	# directory

       return cloneObject

    def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.fileTypes    = other.fileTypes    		# store the file types
       self.modeOpen     = other.modeOpen     		# store the mode
       self.fileName     = other.fileName		# file that's been selected
       self.Directory    = other.Directory  		# directory

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+"=ATOM3File("+str(self.fileTypes)+","+str(self.mode)+")\n")

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+".setValue("+str(self.getValue())+")\n")
       if self.isNone():
         file.write(indent+objName+".setNone()\n")  
         

