# __ File: ATOM3Enum.py __________________________________________________________________________________________________
#  Implements  : class ATOM3Enum
#  Author      : Juan de Lara
#  Description : A class for the ATOM3 Enum type.
#  Modified    : 23 Oct 2001
#  Changes :
#   - 19 DEc 2001 : Modified the setValue(). If the second part of the tuple is < 0, then it is interpreted as setNone().
# ________________________________________________________________________________________________________________________

from Tkinter         import *
from ATOM3Type       import *
from ATOM3List       import *
from ATOM3Exceptions import *
from types           import *

import copy

class ATOM3Enum (ATOM3Type):

   def __init__(self, values = None, sel = None, config = 0 ):
       """ - values: is a tuple of strings
           - sel   : Initially selected item
           - config: 1 = if we will configure the item, 0 = if we will use the item """
       if values:         						# if a list of values is given...
          self.enumValues = values       				# store enumerate values and selected value
          self.selected = IntVar()					# create an IntVar with the selected value

          if sel:							# is a selected element is given...
             if (sel < 0) or (sel > len(values)-1):
                raise ATOM3BadAssignmentValue, "ATOM3Enum: selection out of range"
             self.selected.set(sel+1)                                     # do select it
          else:
             self.selected.set(1)                                       # else select the first
       else:								# No enumerated values yet...
          self.enumValues       = []					# attribute to store the possible values
          self.selected         = None					# selected item
       self.config = config                                             # Store the flag that indicates if we are configuring...
       if self.config:                                                  # If we are configuring...
          self.configItems = ATOM3List([1,1,1,0], ATOM3String, None )   # create the list to configure the items
          # add each element to the list...
          if values:							# If we have some values yet...
             vl = []							# create an empty, auxiliary list
             for item in values: vl.append(ATOM3String( item ))		# populate the list with the items (wrapped in an ATOM3String object)
             self.configItems.setValue( vl )				# set the widget with the elements
             self.enumValues = []					# set enumValues to void, we won't use it when configuring the widget
       else:
          self.configItems = None					# set config flag properly
       self.enumValuesWidget = []					# list of radiobuttons to select one
       self.containerFrame   = None					# frame with all the widgets
       self.enumFrame        = None
       ATOM3Type.__init__(self)

   def clone(self):
       "makes an exact copy of the self object"
       cloneObject = ATOM3Enum(self.enumValues )
       cloneObject.parent = self.parent
       cloneObject.config = self.config
       cloneObject.mode   = self.mode

       if self.selected:
           cloneObject.selected         = IntVar()
           cloneObject.selected.set(self.selected.get())
       else: cloneObject.selected = None

       if self.enumValuesWidget: 
           cloneObject.enumValuesWidget = copy.copy(self.enumValuesWidget)
       else: cloneObject.enumValuesWidget = []
       cloneObject.containerFrame   = self.containerFrame
       return cloneObject

   def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.enumValues = other.enumValues
       self.config = other.config
       if other.selected:
          self.selected   = IntVar()
          self.selected.set(other.selected.get())
       else: self.selected = None
       if other.enumValuesWidget:
          self.enumValuesWidget = copy.copy(other.enumValuesWidget)
       else: self.enumValuesWidget = []
       self.containerFrame = other.containerFrame

   def isNone(self):
       "checks if the value is none"
       if not self.selected or self.selected.get() < 0: return 1
       return 0

   def setNone(self):
       "sets the value to None"
       if self.selected: self.selected.set(-1)

   def unSetNone (self):
       "sets to selected attribute value to 0"
       if self.selected and self.selected.get() == -1: self.selected.set(0)
       
   def setValue(self, value):
       "value is a tuple ([values...], selected). [values...] can be none, and the only the selection is changed."
       if value and type(value) == TupleType:       						# if we have a tuple as argument...
          if value[0]:
             if type(value[0]) != ListType and type(value[0]) != TupleType:			# we expect a list or tuple of elements
                raise ATOM3BadAssignmentValue, "ATOM3Constraint: Bad type in setValue(), "+str(value)
             self.enumValues = value[0]          						# store enumerate values and selected value, if present
          if value[1] != None:                                  				# if we have a second value...
             if type(value[1]) != IntType:							# we expect the index of the selected element
                raise ATOM3BadAssignmentValue, "ATOM3Constraint: Bad type in setValue(), "+str(value)
             # check that values are inside the limits...
             if (value[1] > len(self.enumValues)-1):                              # outside the limits! : raise exception
                raise ATOM3BadAssignmentValue, "ATOM3Constraint: Bad type in setValue(), "+str(value)
             elif (value[1] < 0):								# if the value is negative then set it to None
                self.setNone()
                return
             selected = value[1]								# obtain index of selected element
             self.selected = IntVar()                      					# create an IntVar with the selected value
             self.selected.set(selected+1)
          if self.enumValuesWidget:                        					# if we are visible...
             for rb in self.enumValuesWidget:              					# delete each radiobutton
                rb.grid_forget()                    
          self.createRadioButtons(self.enumFrame)   						# create buttons with the new values
       elif type(value) == NoneType:								# call setNone
          self.setNone()
       else:
          raise ATOM3BadAssignmentValue, "ATOM3Constraint: Bad type in setValue(), "+str(value)

   def getValue(self):
       "returns a tuple ([values...], selected->integer)"
       if self.config:
          self.enumValues = []					# update the value of the enumerate items
          for item in self.configItems.getValue(): self.enumValues.append(item.toString())
       if self.selected:
          return (self.enumValues, self.selected.get()-1 )
       else:
          return (self.enumValues, None)

   def createRadioButtons(self, frame):
       "creates a radiobutton with each value"
       if self.containerFrame and self.enumValues and self.selected:
          counter = 1
          for item in self.enumValues:			# create a radioButton with each value
             rb = Radiobutton ( frame, text = item, variable = self.selected, value = counter)
             rb.grid(row = counter-1, sticky = W)
             self.enumValuesWidget.append(rb)		# add widget to list
             counter = counter + 1

   def show(self, parent, topWindowParent = None ):
       "Method that presents a widget to edit the selected value"
       ATOM3Type.show(self, parent)
       self.containerFrame = Frame(parent)				# create the container frame
       self.enumFrame      = Frame(self.containerFrame) 		# A frame to put the enumerate widget
       if self.config:							# if we are configuring the object
          self.configFrame    = Frame(self.containerFrame) 		# A frame to put the configuration widget (if it is the case)
          widget = self.configItems.show(self.configFrame)		# obtain the widget    
          widget.pack()
          self.configFrame.pack(side=TOP)

       self.createRadioButtons(self.enumFrame)
       self.enumFrame.pack(side=TOP)
       return self.containerFrame

   def invalid(self):
       "decides if we have a valid enumerate type"
       if not self.selected and not self.config:
          return "A value must be selected"
       return None

   def destroy(self):
       "updates attributes and destroys graphical widgets"
       if self.containerFrame:
          self.enumValuesWidget = []
          self.containerFrame   = None
          if self.config:						# if it is a configurable enumerate list...
             self.enumValues = []					# update the value of the enumerate items
             for item in self.configItems.getValue(): self.enumValues.append(item.toString())

   def toString(self, maxWide = None, maxLines = None ):
       "Shows the widget as a string"
       if self.config: retValue = str(self.enumValues)					# if it is configurable, show the item values
       elif self.selected: retValue = str(self.enumValues[self.selected.get()-1])   	# if not and there is a selected item, return its value
       else: retValue = str(self.enumValues)						# else return the items
       if maxWide: return retValue[0:maxWide]
       else: return retValue

   def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       """Method that writes into a file the constructor and the value of the object. Must be overriden in children
          if generatingCode == 1, that means that we are generating code, otherwise, it means that we are saving"""
       if self.selected: selec = str(self.selected.get()-1)
       else: selec = 'None'
       if generatingCode:
          if self.configItems:
             self.enumValues = []								# update the value of the enumerate items
             for item in self.configItems.getValue(): self.enumValues.append(item.toString())
          # before writing, check if we have a None value!
          if not self.selected or self.selected.get() < 0:			# None value!
             file.write(indent+objName+"=ATOM3Enum("+str(self.enumValues)+", None, 0)\n")
             file.write(indent+objName+".setNone()\n")
          else:                                       				# Value is not None
             file.write(indent+objName+"=ATOM3Enum("+str(self.enumValues)+", "+selec+", 0)\n")
       else:
          file.write(indent+objName+"=ATOM3Enum("+str(self.enumValues)+","+selec+","+str(self.config)+")\n")
          if self.configItems:
             self.configItems.writeValue2File(file, indent, objName+".configItems", depth, generatingCode )

   def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       if not self.selected or self.selected.get() < 0:							# We have a None value!
          file.write(indent+objName+".setNone()\n")
       else: 										# Value is NOT None
          if self.selected: selec = str(self.selected.get()-1)
          else: selec = 'None'
          file.write(indent+objName+".setValue( "+str(self.getValue())+" )\n")
       if generatingCode:
          file.write(indent+objName+".config = 0\n")
       else:
          file.write(indent+objName+".config = "+str(self.config)+"\n")
       if self.isNone():
         file.write(indent+objName+".setNone()\n")  
         
