# __ File: ATOM3Attribute.py __________________________________________________________________________________________________
#  Implements  : class ATOM3Attribute
#  Author      : Juan de Lara
#  Description : This is the class for Attribute  (generative) types. It inherits from ATOM3Type
#  Modified    : 23 Oct 2001
#  Changes :
#      - 14 Nov 2001: Added attribute seltype to store the name of the selected type. (copied form old vesrion of ATOM3)
#      - 14 Nov 2001: Added methods updateType() and doSelect(). (copied form old vesrion of ATOM3)
#      - 23 Nov 2001: Fixed bug in the invalid() method. Copied from the old version of ATOM3
#      - 15 Jan 2002: Fixed bug in the writeConstructor2File() method. This method did not pass the generatingCode flag to writeValue2File()
#      - 15 Jan 2002: Fixed bug in the writeValue2File() method. This method did not pass the generatingCode flag to the initialValue
#      - 23 Sep 2002: Fixed some bugs (in setValue, getValue, toString and destroy) which did not updated the seltype attribute.
# _____________________________________________________________________________________________________________________________

from Tkinter import *

from ATOM3Type       import *
from ATOM3Boolean    import *
from ATOM3Exceptions import *
from types           import *
import string

class ATOM3Attribute(ATOM3Type):

    def __init__(self, AllowedTypes ):
        "It receives a dictionary with the allowed types for the attributes"
        ATOM3Type.__init__(self)
        self.allowedTypes       = AllowedTypes                          # dictionary of tuples: (type, parameters)
        self.name_entry         = None
        self.containerFrame     = None
        self.initialValue       = None
        self.initialValueWidget = None
        self.attrName           = None                              # an attribute to store the attribute name
        self.selected           = None                              # attribute type
        self.isKey              = ATOM3Boolean("Key", 0)            # to state if the attribute is the key
        self.directEditing      = ATOM3Boolean("Direct Editing", 1) # if when generated, it will be edited directly or thrugh a button
        self.typeList           = None                              # a future listbox widget
        self.seltype            = None				    # Name of the selected type
        
        # The following added by Denis Dube, Feb 2006
        # Indicates if this is a normal user-created attribute or if it was
        # derived using class diagram inheritance. 
        # Affected methods: clone(), copy(), writeValue2File(), 
        # setDerivedAttributeMarker(), and getDerivedAttributeMarker()
        self.isDerivedAttribute = False
        
        
        
    def clone(self):
        "makes an exact copy of itself"
        cloneObject = ATOM3Attribute(self.allowedTypes)
        cloneObject.containerFrame = self.containerFrame
        cloneObject.initialValue   = self.initialValue
        cloneObject.initialValueWidget = self.initialValueWidget
        cloneObject.attrName	       = self.attrName		
        cloneObject.selected	       = self.selected		
        cloneObject.name_entry         = self.name_entry
        cloneObject.isKey              = self.isKey.clone()
        cloneObject.directEditing      = self.directEditing.clone()
        cloneObject.typeList           = self.typeList
        cloneObject.mode               = self.mode
        cloneObject.seltype            = self.seltype
        cloneObject.isDerivedAttribute = self.isDerivedAttribute 
        return cloneObject

    def copy(self, other):
        "copies each field of the other object into its own state"
        ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
        self.containerFrame     = other.containerFrame
        self.initialValue       = other.initialValue
        self.initialValueWidget = other.initialValueWidget
        self.attrName	        = other.attrName		
        self.selected	        = other.selected		
        self.name_entry         = other.name_entry
        self.isKey              = other.isKey
        self.directEditing      = other.directEditing
        self.typeList           = other.typeList
        self.seltype            = other.seltype
        self.isDerivedAttribute = other.isDerivedAttribute

    def show(self, parent, topWindowParent=None):
        "Presents a frame to edit the item"
        ATOM3Type.show(self, parent, topWindowParent)

        self.containerFrame = Frame(parent)      
        
        Label(self.containerFrame, text = "Attribute name:").grid(row = 0, padx = 5, sticky = E)
        Label(self.containerFrame, text = "Attribute type:").grid(row = 1, padx = 5, sticky = E)
        Label(self.containerFrame, text = "Initial value:").grid(row = 2, padx = 5, sticky = E)

        self.name_entry = Entry(self.containerFrame, exportselection=0)
        self.name_entry.grid(row = 0, column = 1, columnspan = 2)
        if self.attrName:						        # show the name if any
           self.name_entry.insert(END, self.attrName)
        frame      = Frame(self.containerFrame)
        scrollbar  = Scrollbar(frame, orient=VERTICAL)
        self.typeList = Listbox(frame, yscrollcommand=scrollbar.set)		# Create a ListBox
        scrollbar.config(command=self.typeList.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.typeList.pack(side=LEFT, fill=BOTH, expand=1)
        frame.grid(row = 1, column = 1)
        # insert the allowed types in the listbox...        
        for typ in self.allowedTypes.keys():
           self.typeList.insert(END, typ)

        # bind the click button in the ListBox
        self.typeList.bind("<Double-Button-1>", self.selType)
        # show the widget with the initial value, if any
        if self.initialValue:
            self.initialValueWidget = self.initialValue.show(self.containerFrame)# obtain a widget to edit it
	    self.initialValueWidget.grid(row=2, column=1, padx=5, sticky=E)	 # place it in the appropriate place
	
	self.doSelect()
        self.isKey.show(self.containerFrame).grid(row=3, column=1, sticky = W)
        self.directEditing.show(self.containerFrame).grid(row=4, column=1, sticky = W)
        return self.containerFrame

    def updateType(self):
        "stores in self.seltype the type of the current initValue"
        if self.initialValue:
           newSelType = self.initialValue.getTypeName()
	   for typ in self.allowedTypes.keys():
	      if self.allowedTypes[typ][0].__name__ == newSelType:
	         self.seltype = typ

    def doSelect(self):
        "Selects in the listbox the type in attribte self.seltype"
        self.updateType()
        allTypes = self.typeList.get(0, self.typeList.size()-1)
	counter  = 0
   	for typ in allTypes:
	   if typ == self.seltype:
	      self.typeList.select_set(counter)	
	      self.selected = (counter, )
              self.typeList.select_set(self.selected[0])
              break
	   counter = counter + 1
	   
    def selType(self, event):
        "called when the user has selected a type from the list"
        self.selected = self.typeList.curselection()				 # find the selected items...
        try:
           self.selected = map(int, self.selected)
        except ValueError: pass        
	
	if self.initialValueWidget:
	   self.initialValueWidget.grid_forget()
		
	typeClass, typeParams = self.allowedTypes[self.typeList.get(self.selected[0])]		# obtain type and parameters
	self.initialValue = apply ( typeClass, typeParams )                                     # create the class
        self.initialValueWidget = self.initialValue.show(self.containerFrame)			# obtain a widget to edit it
	self.initialValueWidget.grid(row=2, column=1, padx=5, sticky=E)				# place it in the appropriate place
	
    def isNone(self):
        "returns 0 if the stored value can be considered None"
        name, typ, initialValue, isKey, directEditing = self.getValue()
        # 1st. element is the name
        if name != '' and name != None: return 0              # name is not None
        # 2nd. element is the type
        if typ != None: return 0                             # type is not None
        # 3rd. element is the initial value...
        if initialValue != None: return 0                     # initial value is not None
        return 1                                              # we don't evaluate if its key or not...

    def setNone(self):
        "Sets to None the Type value"
        if self.name_entry:
           self.name_entry.delete(0, END)        						# set the attribute name
        self.attrName = ""
        self.selected = None									# set the selected type to None
        self.initialValue = None
	
    def setValue(self, value, ignore=False):
        "sets the name, type and initial value (parameter value is a tuple)"
        if not value: return									# being None does nothing, but is not an error
        if (type(value) != TupleType) or (len(value) != 5):					# otherwise, make sure we have a 5-element tuple
           raise ATOM3BadAssignmentValue, " 5-element tuple expected "				# if we don't have it, raise an exception
        name, ttype, ivalue, isKey, directEditing = value					# unpack list

        self.seltype = ttype                                                                    # ADDED 23 Sept 2002
        
        if type(name) != StringType:	                                                        # Make sure we have a correct name
           raise ATOM3BadAssignmentValue, " 5-element tuple expected "				# if we don't have it, raise an exception
	if self.name_entry:
           self.name_entry.delete(0, END)        						# set the attribute name
           self.name_entry.insert(END, name)
        self.attrName = name

	if self.typeList:
           allTypes = self.typeList.get(0, self.typeList.size()-1)
	   counter  = 0
   	   for typ in allTypes:
	      if typ == ttype:
	         self.typeList.select_set(counter)	
                 break
	      counter = counter + 1
	
	   self.selected = (counter, )
        else:
           allTypes = self.allowedTypes.keys()
           counter  = 0
   	   for typ in allTypes:
	      if typ == ttype:
	         self.selected = (counter, )
                 break
	      counter = counter + 1		
		
	if self.initialValueWidget:
	   self.initialValueWidget.grid_remove()

      
	if not ttype in self.allowedTypes.keys():						# make sure we have the type...
	   raise ATOM3BadAssignmentValue, " type not known: "+ttype	+'\nAllowed Types:'+ str(self.allowedTypes)			# if we don't have it, raise an exception
	
	typeClass, typeParams = self.allowedTypes[ttype]						# If we DO have it, obtain type and parameters
	   	
	self.initialValue = apply ( typeClass, typeParams )					# Create an object of the requested type
	
	self.initialValue.setValue(ivalue)							# Set the initial value
        if isKey != None:
           try:
              self.isKey.setValue(isKey)
           except ATOM3BadAssignmentValue:
              raise ATOM3BadAssignmentValue, "Bad key value"

        if directEditing != None :
           try:
              self.directEditing.setValue(directEditing)
           except ATOM3BadAssignmentValue:
              raise ATOM3BadAssignmentValue, "Bad direct editing value"

    def getValue(self):
        "returns a tuple (name, type, value, key, directEditing)"

        if self.name_entry:				# update attributes with widget info
            self.attrName = self.name_entry.get()

        if self.initialValue:
           if self.seltype:                             # Modified 23 Sept 2002
                return tuple([ self.attrName, self.seltype, self.initialValue.getValue(), self.isKey.getValue(), self.directEditing.getValue() ] )               
           if self.selected:
                return tuple([ self.attrName, self.allowedTypes.keys()[self.selected[0]], self.initialValue.getValue(), self.isKey.getValue(), self.directEditing.getValue() ] )
	   else:
                return tuple([ self.attrName, None, self.initialValue.getValue(), self.isKey.getValue(), self.directEditing.getValue() ] )
	else:
  	   if self.selected:
                return tuple([ self.attrName, self.allowedTypes.keys()[self.selected[0]], None, self.isKey.getValue(), self.directEditing.getValue() ] )
	   else:
                return tuple([ self.attrName, None, None, self.isKey.getValue(), self.directEditing.getValue() ] )
	
    def toString(self, maxWide = None, maxLines = None ):
       "Returns the string representation of this type"
       if self.name_entry:				# update attributes with widget info
            self.attrName = self.name_entry.get()
       retString = ""
       if self.attrName:
          retString = retString + self.attrName
       else:
          retString = retString + "<None>"

       if self.seltype:                                             # Modified 23 Sept 2002
          retString = retString+" type="+self.seltype               # Modified 23 Sept 2002
       elif self.selected:
          retString = retString+" type="+self.allowedTypes.keys()[self.selected[0]]
       else:
          retString = retString+" type=<None>"

       if self.initialValue:
          retString = retString+" init.value="+self.initialValue.toString()
       else:
          retString = retString+" init.value=<None>"

       if maxWide: return retString[0:maxWide]
       return retString

    def invalid(self):
       "Decides if the attribute is valid, that is, if the initial value (if any) is valid"
       if self.name_entry: vname = self.name_entry.get()
       else: vname = self.attrName
       if (not vname) or (vname == ""):                 # the name is mandatory
          return "Attribute name must be specified"
       # now check that the name is valid (a variable name)
       if string.count(vname, " ") > 0:
          return "Invalid variable name, no white spaces allowed"
       # check first character
       if (vname[0] >= '0') and (vname[0] <= '9'):              # a number
          return "Invalid variable name, first character must be a letter or '_'"
       if vname[0] != '_' and (vname[0]<'A' or vname[0]>'z'):
          return "Invalid variable name, first character must be a letter or '_'"
       # now check for the rest of not allowed characters...
       for c in range(len(vname)-1):
          if vname[c+1] < 'A' or vname[c+1] > 'z':              # not a letter
             if vname[c+1] < '0' or vname[c+1] > '9':           # not a number
                if vname[c+1] != '_':                                # not underscore
                   return "Invalid variable name, character '"+vname[c+1]+"' is not allowed"
       if not self.selected:								# also the attribute type
          return "Attribute type must be specified"
       if self.initialValue:								# if initial value specified, do check it
          return self.initialValue.invalid()



    def destroy(self):
       "stores widget values into variables"
       if self.name_entry:
          self.attrName = self.name_entry.get()
          self.name_entry = None
       # send destroy to all ATOM3Type widgets
       if self.initialValue:
       	  self.initialValue.destroy()
       self.initialValueWidget = None
       self.containerFrame     = None
       self.isKey.destroy()
       self.directEditing.destroy()
       if self.selected:                                                                 # Modified t 2002
          self.seltype = self.typeList.get(self.selected[0])                            # Modified 23 Sept 2002

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       if generatingCode:								# if we are generating code, then it is
          file.write(indent+objName+"=ATOM3Attribute(parent.types)\n")			# the father who has information about allowed types
       else:
          file.write(indent+objName+"=ATOM3Attribute(self.types)\n")
       self.writeValue2File(file, indent, objName, depth, generatingCode)

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       """ Method that writes into a file the constructor and the value of the 
       object. Must be overriden in children """
       # getValue() returns a tuple (name, type, value, key, directEditing)
       name, type, value, key, directEditing = self.getValue()
       value2 = (name, type, None, key, directEditing)
       file.write(indent+objName+".setValue("+str(value2)+")\n")
       self.initialValue.writeConstructor2File( file, indent, 
          objName+".initialValue", depth, generatingCode)	# modified 15 Jan 2002
       if self.isNone():
         file.write(indent+objName+".setNone()\n")  

       file.write(indent+objName+".isDerivedAttribute = " 
                   + str(self.isDerivedAttribute)  + "\n") # See __init__

        
    def setDerivedAttributeMarker(self, flagBoolean):
       """ Marks this attribute as being derived by inheritance or not """
       self.isDerivedAttribute = flagBoolean
     
    def getDerivedAttributeMarker(self):
       """ 
       Return:
         True, this attribute was derived by inheritance (ie: in a class diagram)
         False, this is a user created attribute, not derived.
       """
       return self.isDerivedAttribute
