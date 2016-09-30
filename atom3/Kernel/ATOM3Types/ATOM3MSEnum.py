# __ File: ATOM3MSEnum.py __________________________________________________________________________________________________
#  Implements  : class ATOM3MSEnum
#  Author      : Juan de Lara
#  Description : A class for the ATOM3 Multiple Selection Enum type.
#  Modified    : 23 Oct 2001
#  Changes :
#   - 19 DEc 2001 : Modified the setValue(). If the second part of the tuple is None, then it is interpreted as setNone().
# ________________________________________________________________________________________________________________________

from Tkinter         import *
from ATOM3Type       import *
from ATOM3List       import *
from types           import *
from ATOM3Exceptions import *
from ATOM3Enum       import ATOM3Enum

import copy

class ATOM3MSEnum (ATOM3Type):

   # Some useful constants...

   CHECKBOX = 0
   LISTBOX  = 1

   def __init__(self, values = None, sel = None, config = 0, type = LISTBOX ):
       """ - values: is a LIST of strings
           - sel   : Initially selected items
           - config: 1 = if we will configure the item, 0 = if we will use the item """
       self.type = type					# copy item's type (CHECKBOX or LISTBOX)
       if values:
          self.enumValues = values       		# store enumerate values and selected value
          self.selected = []				# create an empty list with the selected items
          if sel:
             for itemSel in sel:			# iterate on the items (1 means selected, 0 means not selected)
                iv = IntVar()				# create an IntVar
                iv.set(itemSel)				# set its value
                self.selected.append(iv)		# append to the list...
          else:
             for itemSel in values:			# iterate on the items (1 means selected, 0 means not selected)
                iv = IntVar()				# create an IntVar
                iv.set(1)				# set its value
                self.selected.append(iv)		# append to the list...
       else:
          self.enumValues       = []			# attribute to store the possible values
          self.selected         = []			# empty list of selected items...
            
       self.config = config
       self.chooseType = None
       self._isNone = 0
       if self.config:
          self.configItems = ATOM3List([1,1,1,0], ATOM3String, None )     # create the list to configure the items
          # add each element to the list...
          if values:
             self.assignStringList(values)
             self.enumValues = []  
          self.chooseType = ATOM3Enum(["CheckBox", "ListBox"], self.type)  # create an enumerate type to select the appearance
       else:
          self.configItems = None
       if type == self.CHECKBOX:
          self.enumValuesWidget = []			# list of checkboxes to select one
       else:
          self.enumValuesWidget = None
       self.containerFrame   = None			# frame with all the widgets
       self.enumFrame        = None
       ATOM3Type.__init__(self)

   def assignStringList(self, strList):
       """method that assign the string list in 'strList' to self.configItems. For this purpose, each element of the list must be
          converted into an ATOM3String"""
       vl = []                                            	# initialize list
       for item in strList: vl.append(ATOM3String( item ))	# append ATOM3String created with the items in the list
       self.configItems.setValue( vl )

   def clone(self):
       "makes an exact copy of the self object"
       cloneObject = ATOM3MSEnum(self.enumValues, None, 0, self.type )
       cloneObject.parent = self.parent
       cloneObject.config = self.config
       cloneObject.mode   = self.mode

       if self.selected:					# clone the 'selected' list
           cloneObject.selected         = []
           for itemSel in self.selected:			# iterate over each element
              isel = IntVar()                  			# create a new IntVar
              isel.set(itemSel.get())				# set value
              cloneObject.selected.append(isel)			# add it to cloned object
       else: cloneObject.selected = None

       if self.chooseType:                                      # if the widget to configure the type is present...
          cloneObject.chooseType = self.chooseType.clone()      # clone it!

       if self.enumValuesWidget: 
           cloneObject.enumValuesWidget = copy.copy(self.enumValuesWidget)
       elif self.type == self.CHECKBOX:
           cloneObject.enumValuesWidget = []
       else:
           cloneObject.enumValuesWidget = None
       cloneObject.containerFrame   = self.containerFrame
       return cloneObject

   def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.enumValues = other.enumValues
       self.config = other.config
       if other.selected != []:
          for counter in range(len(self.selected)):
              itemsel = self.selected[counter]
              othersel= other.selected[counter]
              itemsel.set(othersel.get())
       else: self.selected = []
       if other.enumValuesWidget:
          self.enumValuesWidget = copy.copy(other.enumValuesWidget)
       elif self.type == self.CHECKBOX:
          self.enumValuesWidget = []
       else:
          self.enumValuesWidget = None
       if other.chooseType:                           # if the widget to edit the type is present
          self.chooseType = other.chooseType
       self.containerFrame = other.containerFrame

   def isNone(self):
       "checks if the value is none"
       #if self.selected != []: return 0
       return self._isNone
       #return 1

   def setNone(self):
       "sets the value to None"
       self._isNone = 1
       # self.selected = []

   def unSetNone(self):
       "sets the _isNone flag to 0"
       self._isNone = 0
       # pass      
       
   def setValue(self, value):
       "value is a tuple ([values...], [s1,...]). [values...] can be none, and then only the selection is changed."
       if type(value) == NoneType:
          self.setNone()
          return
       if type(value) != TupleType or len(value) != 2:			# Make sure we receive a 2-element tuple
          raise ATOM3BadAssignmentValue, "a 2-element tuple was expected"
       tv0 = type(value[0])
       tv1 = type(value[1])
       if (not type(value[0]) in [ListType,NoneType]) or (not type(value[1]) in [ListType, NoneType]):	# MODIFIED 19-DEC-2001
          raise ATOM3BadAssignmentValue, " wrong element types in tuple"
       if tv0 == ListType and len(value[0]) != len (value[1]) :		# Make sure we have two list of equal length
          raise ATOM3BadAssignmentValue, " wrong element types in tuple"
       if value:
          if value[0]:
             for item in value[0]:					# Make sure all elements are strings
                if type(item) != StringType:
                   raise ATOM3BadAssignmentValue, " wrong element types in list"
             if not self.config:					# if we are not configuring the item...
                self.enumValues = value[0]          			# store enumerate values and selected value, if present
             else:             						# if we are configuring the item, then modify also self.configItems
                self.assignStringList(value[0])
          if value[1]:
             self.selected = []
             for itemsel in value[1]:			   		# iterate on each selected item
                isel = IntVar()                      			# create an IntVar with the selected value
                isel.set(itemsel)					# set the value
                self.selected.append(isel)
          else:                                                         # MODIFIED 19/DEC/2001
             self.setNone()
             return
          if self.type == self.CHECKBOX:
             if self.enumValuesWidget:                        		# a list with the checkbuttons
                for cb in self.enumValuesWidget:              		# delete each value
                   cb.grid_forget()
             self.createCheckButtons(self.enumFrame)
          else:
             if self.enumValuesWidget:                        		# a list with the checkbuttons
                self.enumValuesWidget.delete(0,END)			# delete all elements in list
             self.createList(self.enumFrame)

   def getValue(self):
       "returns a tuple ([values...], [s1, s2,...])"
       # self.destroy()
      
       if self.config:
          self.enumValues = []					# update the value of the enumerate items
          for item in self.configItems.getValue(): self.enumValues.append(item.toString())

       if self.type == self.LISTBOX:					# store the selections
          if self.enumValuesWidget:
            now = self.enumValuesWidget.curselection()
            try:
               now = map(int, now)
            except ValueError: pass
            for index in range(len(self.selected)):
               if index in now: self.selected[index].set(1)
               else: self.selected[index].set(0)
       else:
           self.enumValuesWidget = []
       self.containerFrame   = None
       if self.config:						# if it is a configurable enumerate list...
          self.enumValues = []					# update the value of the enumerate items
          for item in self.configItems.getValue(): self.enumValues.append(item.toString())      
            
       if self.selected:
          selected = []
          for isel in self.selected:
             selected.append(isel.get())
          return (self.enumValues, selected)
       else:
          return (self.enumValues, None)

   def createList(self, frame):
       "creates a multiple selection list with each value"
       if frame == None : return
       scrollbar = Scrollbar(frame, orient=VERTICAL)
       height = min( len(self.enumValues), 4 )
       self.enumValuesWidget = Listbox(frame, exportselection=0, 
                        selectmode = MULTIPLE, yscrollcommand=scrollbar.set, 
                        height = height)
       scrollbar.config(command=self.enumValuesWidget.yview)
       scrollbar.pack(side=RIGHT, fill=Y)
       self.enumValuesWidget.pack(side=LEFT, fill=BOTH, expand=1)
       if self.containerFrame and self.enumValues and self.selected:
          counter = 0
          for item in self.enumValues:			# create a radioButton with each value
             sv = self.selected[counter]
             self.enumValuesWidget.insert(END, item)
             if sv.get() == 1:
             	self.enumValuesWidget.select_set(counter)
             counter = counter + 1

   def createCheckButtons(self, frame):
       "creates a checkbutton with each value"
       if self.containerFrame and self.enumValues and self.selected:
          counter = 0
          for item in self.enumValues:			# create a radioButton with each value
             sv = self.selected[counter]
             rb = Checkbutton ( frame, text = item, variable = sv)
             rb.grid(row = counter, sticky = W)
             if sv.get() == 1: rb.select()
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
          widget.grid(row=0, column=0, sticky=W)
          self.chooseType.show(self.configFrame).grid(row=1, column=0, sticky=W)
          self.configFrame.pack(side=TOP)
       else:
          if self.type == self.CHECKBOX:
             self.createCheckButtons(self.enumFrame)
          else:
             self.createList(self.enumFrame)
       self.enumFrame.pack(side=TOP)
       return self.containerFrame

   def invalid(self):
       "decides if we have a valid enumerate type"
       if self.selected == [] and not self.config and not self.isNone():
          return "A value must be selected"
       return None

   def destroy(self):
       "updates attributes and destroys graphical widgets"
       if self.containerFrame:
          if self.type == self.LISTBOX:					# store the selections
              if self.enumValuesWidget:
                now = self.enumValuesWidget.curselection()
                try:
                   now = map(int, now)
                except ValueError: pass
                for index in range(len(self.selected)):
                   if index in now: self.selected[index].set(1)
                   else: self.selected[index].set(0)
                self.enumValuesWidget = None
          else:
              self.enumValuesWidget = []
          self.containerFrame   = None
          if self.config:						# if it is a configurable enumerate list...
             self.enumValues = []					# update the value of the enumerate items
             for item in self.configItems.getValue(): self.enumValues.append(item.toString())
       elif self.enumValuesWidget: self.enumValuesWidget = None

   def toString(self, maxWide = None, maxLines = None ):
       "Shows the widget as a string"
       if self.config: retValue = str(self.enumValues)					# if it is configurable, show the item values
       elif self.selected != []:
          retValue = ""
          counter = 0
          for sel in self.selected:
             if sel.get() == 1:
               retValue = retValue + str(self.enumValues[counter])+" "   		# if not and there is a selected item, return its value
             counter = counter + 1
       else: retValue = str(self.enumValues)						# else return the items
       if maxWide: return retValue[0:maxWide]
       else: return retValue

   def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       """Method that writes into a file the constructor and the value of the object. Must be overriden in children
          if generatingCode == 1, that means that we are generating code, otherwise, it means that we are saving"""
       if self.selected:
          selec = "["
          for elem in self.selected:
             selec = selec + str(elem.get())
             if not elem == self.selected[-1]: selec = selec + ","
          selec = selec+ "]"   
       else: selec = 'None'
       if self.chooseType:
          chooseType = self.chooseType.getValue()[1]
       else: chooseType = self.type
       if generatingCode:
          self.enumValues = []					# update the value of the enumerate items
          for item in self.configItems.getValue(): self.enumValues.append(item.toString())
          file.write(indent+objName+"=ATOM3MSEnum("+str(self.enumValues)+", "+selec+", 0, "+str(chooseType)+")\n")
       else:
          file.write(indent+objName+"=ATOM3MSEnum("+str(self.enumValues)+","+selec+","+str(self.config)+","+str(chooseType)+")\n")
          #self.configItems.writeValue2File(file, indent, objName+".configItems", depth, generatingCode )

   def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       if self.selected != []:
           selist = []
           for s in self.selected:
              selist.append(s.get())
      	   selec = str(selist)
       else:
           selec = '[]'
       file.write(indent+objName+".setValue( "+str(self.getValue())+" )\n")
       if generatingCode:
          file.write(indent+objName+".config = 0\n")
       else:
          file.write(indent+objName+".config = "+str(self.config)+"\n")
       if self.isNone():
         file.write(indent+objName+".setNone()\n")
      
      
   def getValueAsDict( self ):
      """ Return a dictionary from the enumeration information """
      name, value = self.getValue()
      nameDict = dict()
      if( value == None ): 
        for i in range( 0, len( name ) ): nameDict[ name[i] ] = False
      else:      
        for i in range( 0, len( name ) ): nameDict[ name[i] ] = value[i]
      return nameDict
      
