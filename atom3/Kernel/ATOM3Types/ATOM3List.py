# __ File: ATOM3List.py __________________________________________________________________________________________________
#  Implements  : class ATOM3List
#  Author      : Juan de Lara
#  Description : This is the class for list types. It inherits from ATOM3Type
#  Modified    : 31 Dec 2001
#  Changes :
#    - 31 Dec 2001: bug fixed in the writeConstructor2File, the method did not write properly if one of the
#       arguments of the items' type was None, such as in the case of ATOM3Booleans.
#    - 1  Jan 2002 : bug fixed in the writeConstructor2File, the method does not write properly List of Lists.
#    - 15 Jan 2002 : AT3Type is made optional in the constructor. The default type for lists is ATOM3Attribute
#    - 16 Jan 2002 : in writeConstructor2File, if one of the parameters of the type of the list was a string, it did not print the quotes.
# _____________________________________________________________________________________________________________________________

from Tkinter         import *
from types           import *
from ATOM3Type       import *
from ATOM3TypeDialog import *
from ATOM3String     import *
from ATOM3Attribute  import *
from ATOM3Exceptions import *

import string

import copy

class ATOM3List(ATOM3Type):

    def __init__(self, actionFlags, AT3Type = None, * AT3TypeArgums ):
       """action Flags is a list of length 4 that indicates whether we can create, edit or delete elements. The fourth
          is a meta flag allows editing the rest of the flags. If it is different from None, it will contain a dictionary
          with the allowed types.
       """
       ATOM3Type.__init__(self)
       self.actionFlags= actionFlags				# Copy the actionFlags...
       self.itemList   = None					# For the moment, the list is empty
       self.objectList = []					# Create a List with the real objects
       if AT3Type == None:					# The default type for lists is ATOM3Attribute... (modified 15-Jan-2002)
          self.itemType = ATOM3Attribute
       else:
          self.itemType = AT3Type 				# Store the items type
       self.containerFrame = None				# will store a frame
       self.itemTypeArguments = AT3TypeArgums			# tuple with the arguments
       self._isNone = 0						# flag that indicates that the widget is NULL
       self.lastSelection = None				# Variable to store the last selected element of the list
       self.isRecursive = True
       
       self.listHeight = 5 # Default height of a listbox
       
    def setHeight(self, height):
      """ Set the height (number of items shown) of the listbox """
      self.listHeight = min(height, 1) # New height must be > 1

    def setNone(self):
       "sets the _isNone flag to 1"
       self._isNone = 1

    def isNone(self):
       "returns the _isNone flag"
       return self._isNone

    def unSetNone(self):
       "sets the _isNone flag to 0"
       self._isNone = 0

    def clone(self):
       "makes an exact copy of itself"
       objectClone                   = ATOM3List ( self.actionFlags, self.itemType )
       objectClone.actionFlags       = self.actionFlags
       objectClone.mode              = self.mode
       objectClone.itemTypeArguments = self.itemTypeArguments
       objectClone.containerFrame    = self.containerFrame
       objectClone.itemList          = self.itemList
       objectClone._isNone           = self._isNone
       objectClone.objectList        = []
       # clone each object in the list
       for obj in self.objectList: 
           objectClone.objectList.append(obj.clone())
       return objectClone

    def destroy(self):
       "copies actual value into the attributes and destroys widgets"
       if self.actionFlags[3]:                               # the meta-flag is active...
          # select the type of the new object from the list self.allowedTypes
          items = self.allowedTypes.itemList.curselection()
          try:
            items = map(int, items)
          except ValueError: pass
          if items:
             self.itemType, self.itemTypeArguments = self.actionFlags[3][self.actionFlags[3].keys()[items[0]]]
       if self.itemList:
          lastSelected = self.itemList.curselection()		# store the element last selected
          try:
            self.lastSelection = map(int, lastSelected)
          except ValueError: pass
          if len(self.lastSelection) > 0: self.lastSelection = self.lastSelection[0]
       self.itemList = None
       self.containerFrame = None

    def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.itemTypeArguments = other.itemTypeArguments
       self.containerFrame    = other.containerFrame
       self.itemList          = other.itemList
       self.objectList        = other.objectList
       self.actionFlags       = other.actionFlags

    def select (self, which):
      "Selects the given item. The first one is the zero"
      self.itemList.select_set(which)

    def show(self, parent, Unused = None ):
       "shows thre buttons (new, edit and delete) as well as a listbox"
       
       ATOM3Type.show(self, parent)
        
       # a container Frame for all the widgets
       self.containerFrame = Frame (parent, relief='raised',borderwidth=4)       					
       self.topFrame   	   = Frame (self.containerFrame) # a Frame for the buttons, to be placed on top
       metaFrame	   = Frame (self.containerFrame)			 # a Frame to edit the buttons that must be placed

       # a scrollbar for the listbox
       scrollbar      = Scrollbar(self.containerFrame, orient=VERTICAL)			
       
       # Create a ListBox
       height = min(len(self.objectList), self.listHeight)
       self.itemList  = Listbox(self.containerFrame, height=height,
                           exportselection=0, yscrollcommand=scrollbar.set)	
                           
       # This makes editing lists much more fun :)
       def handler(event=None):
          self.editItem()
       self.itemList.bind("<Double-ButtonPress-1>", handler)
       
       scrollbar.config(command=self.itemList.yview)
       scrollbar.pack(side=RIGHT, fill=Y)

       # show the items in the list, if any
       if self.objectList:
          for item in self.objectList:
             self.itemList.insert(END, item.toString() )

       # present the buttons, depending on the action flags
       self.buttonFrame = Frame(self.containerFrame)

       if self.actionFlags[0]:
          self.newItemButton = self.makeButton( 'New', self.newItem)
       else:
          self.newItemButton = None

       if self.actionFlags[1]:
          self.editItemButton = self.makeButton( 'Edit', self.editItem )
       else:
       	  self.editItemButton = None

       if self.actionFlags[2]:   											
          self.delItemButton = self.makeButton( 'Delete', self.deleteItem )
       else:
          self.delItemButton = None
          self.actionFlag = None

       if self.actionFlags[3]:									# meta-flag
          sel1 = IntVar()									# checkBox for "New items"
          sel1.set(self.actionFlags[0])
          cb1 = Checkbutton ( metaFrame, text = "New", variable = sel1, command = lambda x=(self, 0): x[0].hide(x[1]) )
          cb1.pack(side=LEFT, padx=2, pady=2)

          sel2 = IntVar()									# checkBox for "Edit items"
          sel2.set(self.actionFlags[1])
          cb2 = Checkbutton ( metaFrame, text = "Edit", variable = sel2, command = lambda x=(self, 1): x[0].hide(x[1]) )
          cb2.pack(side=LEFT, padx=2, pady=2)

          sel3 = IntVar()									# checkBox for "Delete items"
          sel3.set(self.actionFlags[2])
          cb3 = Checkbutton ( metaFrame, text = "Delete", variable = sel3, command = lambda x=(self, 2): x[0].hide(x[1]) )
          cb3.pack(side=LEFT, padx=2, pady=2)

          self.allowedTypes = ATOM3List ([0,0,0,None], ATOM3String)				# create a list with the possible types for the list
          strObjects = map(ATOM3String, self.actionFlags[3].keys())				# create the ATOM3STring objects
          self.allowedTypes.setValue(strObjects)						# set the value
          widget = self.allowedTypes.show(metaFrame)						# get the widget to browse the type list
          # now highlight the selected type...
          counter = 0
          itname  = self.itemType.__name__
          for type2consider in self.actionFlags[3].keys():
             if itname == self.actionFlags[3][type2consider][0].__name__:                
                self.allowedTypes.select( counter )
                break
             counter = counter + 1
             
          widget.pack(side=BOTTOM)

          self.sels = [sel1, sel2, sel3]

          metaFrame.pack(side=TOP)

       self.buttonFrame.pack(side=LEFT)
       self.topFrame.pack(side=TOP, padx=120)
       self.itemList.pack(side=BOTTOM, fill=BOTH, expand=1)
       return self.containerFrame								# returns the Frame with all the widgets


    def makeButton( self, text, command ):
      """ The quicker faster way to make nice buttons :D """
      if( text == 'New' ): order, color = [0,'#E8E8E8']
      elif( text == 'Edit' ): order, color = [1,'#C4C4C4']
      elif( text == 'Delete' ): order, color = [2,'#9C9C9C']
      button = Button( self.buttonFrame, text=text, width=4, bg=color, 
                       command=command)
      button.grid(row=order, column=0)
      return button

    def hide(self, which):
       "One of the buttons must be hidden/showed, actionFlags must be conveniently updated"
       if which == 0:
          if self.sels[which].get():
              self.newItemButton = self.makeButton( 'New', self.newItem)
              self.actionFlags[0] = 1
          else:
              self.newItemButton.grid_forget()
              del self.newItemButton
              self.actionFlags[0] = 0
       elif which == 1:
          if self.sels[which].get():
              self.editItemButton = self.makeButton( 'Edit', self.editItem )
              self.actionFlags[1] = 1
          else:
              self.editItemButton.grid_forget()
              del self.editItemButton
              self.actionFlags[1] = 0
       elif which == 2:
          if self.sels[which].get():
              self.delItemButton = self.makeButton( 'Delete', self.deleteItem )
              self.actionFlags[2] = 1
          else:
              self.delItemButton.grid_forget()
              del self.delItemButton
              self.actionFlags[2] = 0

    def deleteItem (self, itemToDelete = None ):
       "deletes current item"
       if itemToDelete == None:
          items =self.itemList.curselection()
          try:
              items = map(int, items)
          except ValueError: pass
          if items: itemToDelete = items[0]
          else: return

       elif (itemToDelete < 0) or (itemToDelete > len(self.objectList)-1):
          raise ATOM3ElementOutOfRange, " when deleting"
       del self.objectList[itemToDelete]
       if self.itemList: self.itemList.delete(ANCHOR)

    def newItem (self, item = None):
       "Opens a dialog to create a new item, if item is null, otherwise inserts item directly"
       if not item:						# then open a dialog to edit the item values...
          if self.actionFlags[3]:				# the meta-flag is active...
             # select the type of the new object from the list self.allowedTypes
             items = self.allowedTypes.itemList.curselection()
             try:
               items = map(int, items)
             except ValueError: pass
             if items:
                self.itemType, self.itemTypeArguments = self.actionFlags[3][self.actionFlags[3].keys()[items[0]]]
          params = []
          for arg in self.itemTypeArguments:
             params.append ( arg )
          obj = apply (self.itemType, params)			# create the appropriate object...
          dg = ATOM3TypeDialog ( self.containerFrame, obj, self.mode )
          if dg.result_ok:
             if self.itemList: self.itemList.insert(END, dg.result)
             self.objectList.append(dg.widget)
          else:
             del obj
       else:
          # see if the item is repeated...
          for obj in self.objectList:
             if item.hasEqualValue(obj): return

          if self.itemList: self.itemList.insert(END, item.toString())
          self.objectList.append(item)

    def editItem (self):
       "Opens a dialog to edit the selected item"
       from ATOM3TypeDialog import *
       items =self.itemList.curselection()
       try:
           items = map(int, items)
       except ValueError: pass
       if items:
          dg = ATOM3TypeDialog ( self.containerFrame, self.objectList[items[0]], self.mode )
          if dg.result_ok:
              self.itemList.insert(items[0], dg.widget.toString() )
              self.itemList.delete(items[0]+1, items[0]+1 )
              self.objectList[items[0]] = dg.widget

    def setValue(self, value):
       """
       Sets the actual attribute value (value is a list of objects of type 
       ATOM3Type)
       """
       if(type(value) != ListType and type(value) != NoneType 
         and type(value) != TupleType):
          raise ATOM3BadAssignmentValue, " list expected"
       # Shouldn't we check if each element is a subclass of ATOM3Type ??? 
       # (perhpas too costly...)
       if self.itemList: 
         self.itemList.delete(0, END)		# remove elements from ListBox
       # remove each element, but let the reference in the same place
       while self.objectList: 
         self.objectList.remove(self.objectList[0])
       if(value != None):
          for v in value:   
             if self.itemList: 
               self.itemList.insert(END, v.toString() )
             self.objectList.append( v )
             

    def getValue(self):
       "Gets the actual attribute value"
       return self.objectList

    def getActionFlags(self):
       "Returns the action flags"
       return self.actionFlags

    def setActionFlags(self, actFlags):
       "Returns the action flags"
       self.actionFlags = actFlags

    def toString(self, maxWide = None, maxLines = None):
       "Returns the string representation of this type"
       repr = ""
       counter = 0
       for item in self.objectList:
          if not maxWide: repr = repr+item.toString()+"\n"          
          else: repr = repr+item.toString()[0:maxWide]+"\n"
          counter = counter + 1
          if maxLines and counter == maxLines: break  
       return repr


    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       """
          Method that writes into a file the constructor and the value of the object. Must be overriden in children.
       """
       actFlags = "[ "
       counter = 0
       while counter < 3:
         actFlags = actFlags+str(self.actionFlags[counter])
         actFlags = actFlags + ", "
         counter = counter + 1
       if self.actionFlags[3] and not generatingCode:
         actFlags = actFlags + "self.types]"
       else:
         actFlags = actFlags + "0]"
       aux = str(self.itemType)						# obtain the class name
       clName = aux[string.rfind(aux,".")+1:]
       if str(self.itemTypeArguments) != '()':
          file.write(indent+objName+"=ATOM3List("+actFlags+","+clName+",")
          if clName == 'ATOM3Attribute':				# beware! self.itemTypeArguments can be a dictionary! (if clName is ATOM3Attribute)
             if generatingCode:
                file.write('parent.types )\n')                          # if generating code, we are inside an entity
             else:
                file.write('self.types )\n')                     # if we are not generating code, we are in an ATOM3 method (MODIFIED 19 SEP 2002)
          elif clName == 'ATOM3List':                                   # modified 1/1/2002
             if generatingCode:
                file.write('[1,1,1,parent.types])\n')
             else:
                file.write('[1,1,1,self.types])\n')                 
          elif clName == 'GGruleEdit':					# the 2nd. argument of the tuple is an ATOM3 instance...
             file.write('None, self)\n')
          else:								# it is not a dictionary, write the arguments, but unwrap them from a tuple...
             counter = 0
             for el in self.itemTypeArguments:
                if counter > 0: file.write(",")
                if type(el) == StringType:				# if it is a String, we have to wrap it in quotes modified 16/1/2002
                   file.write('"'+el+'"')
                else:
                   file.write(str(el))                                  # modified 31/12/01
                counter = counter + 1
             file.write(")\n")
       else:
          file.write(indent+objName+"=ATOM3List("+actFlags+","+clName+")\n")
       theName = "cobj"+str(depth)
       file.write(indent+"l"+theName+"=[]\n")
       for item in self.objectList:					# add the elements
          item.writeConstructor2File( file, indent, theName, depth+1, generatingCode )  # modified 1/1/2002
          file.write(indent+"l"+theName+".append("+theName+")\n")
       file.write(indent+objName+".setValue(l"+theName+")\n")
       if self.isNone():
          file.write(indent+objName+".setNone()\n")
           

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0 ):
       """
          Method that writes into a file the constructor and the value of the object. Must be overriden in children.
       """
       actFlags = "[ "
       counter = 0
       while counter < 3:
         actFlags = actFlags+str(self.actionFlags[counter])
         actFlags = actFlags + ", "
         counter = counter + 1
       if self.actionFlags[3] and not generatingCode:
         actFlags = actFlags + "self.types]"                   # MODIFIED 19 SEP 2002
       else:
         actFlags = actFlags + "0]"
       file.write(indent+objName+".setActionFlags("+actFlags+")\n")
       theName = "cobj"+str(depth)
       file.write(indent+"l"+theName+" =[]\n")
       for item in self.objectList:					# add the elements
          item.writeConstructor2File( file, indent, theName, depth + 1 )
          file.write(indent+"l"+theName+".append("+theName+")\n")
       file.write(indent+objName+".setValue(l"+theName+")\n")
       if self.isNone():
          file.write(indent+objName+".setNone()\n")
      

