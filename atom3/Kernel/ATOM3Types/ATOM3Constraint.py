# __ File: ATOM3Constraint.py __________________________________________________________________________________________________
#  Implements  : class ATOM3Constraint
#  Author      : Juan de Lara
#  Description : A class for the ATOM3 Constraint type.
#  Modified    : 23 Oct 2001
#  Changes :
#
#   - 19 Dec 2001 : A constraint is invalid if it has no name, but is valid if it has been set to None. Constraints
#		    that have been set to None may not have a Name. This is corrected in the invalid() function.
#   - 19 Dec 2001 : attribute _isNone has been added to decide if the object is None. Modified: __init__, clone,
#   - 19 Dec 2001 : some methods modified to handle special cases qhen the object is None: writeConstructor2File, writeValue2File.
#   - 14 Jan 2002 : toString did not receive 3 arguments so it failed when tried to print in an icon.
# ____________________________________________________________________________________________________________________
from Tkinter         import *
from ATOM3Type       import *
from ATOM3Enum       import *
from ATOM3MSEnum     import *
from ATOM3String     import *
from ATOM3Exceptions import *
from code 	     import *

from ATOM3Integer import ATOM3Integer
from types import *
from string import *

from textUtilities import setTabs,createTabPanel, addFiltersFromIDLE
from textUtilities import processBackspace, processDelete
from textUtilities import processTab, processReturn

class ATOM3Constraint(ATOM3Type):

   def __init__(self, attribs = None, constrName = None, prefix="self.", kind = ['PREcondition', 'POSTcondition'],
                actions=['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE']):
      self.classAttribs    = attribs	    					# class attributes (list of ATOM3Attribute)
      self.prefix          = prefix						# prefix to be added to attributes (optional)
      self.constName	   = ATOM3String()					# constraint name
      if constrName: self.constName.setValue(constrName)        		# set the value if any
      self.constCodeWidget = None						# constraint widget to edit the code
      self.constCode       = None						# constraint code
      self.language        = ATOM3Enum(['Python', 'OCL'], 1)    		# constraint language
      if kind and len(kind)>0: self.kind   = ATOM3Enum(kind, 1)			# kind (PRE or POST)
      else: self.kind      = None
      self.containerFrame  = None						# container frame
      if actions and len(actions)>0:
        selected = []
        for counter in range(len(actions)):
           selected.append(0)
        self.actions = ATOM3MSEnum(actions, selected, 0, ATOM3MSEnum.LISTBOX)				# action when the constraint must be evaluated
      else: self.actions   = None
      self._isNone = 0
      
      self.heightATOM3Integer = ATOM3Integer(15)
      ATOM3Type.__init__(self)

   def clone (self):
      "makes an exact copy of the object"
      kinds, acts = None, None
      if self.kind: kinds = self.kind.enumValues
      if self.actions: acts = self.actions.enumValues
      cloneObject = ATOM3Constraint(self.classAttribs, None, self.prefix, kinds, acts)			# call constructor for clone object

      if self.constName: cloneObject.constName	  = self.constName.clone()				# clone constName
      else: cloneObject.constName = None

      cloneObject.constCodeWidget = self.constCodeWidget
      cloneObject.constCode       = self.constCode

      if self.language: cloneObject.language = self.language.clone()					# clone language
      else: cloneObject.language = None

      if self.kind: cloneObject.kind = self.kind.clone()						# clone kind
      else: cloneObject.kind = None

      cloneObject.actions         = self.actions.clone()						# clone actions

      cloneObject.containerFrame  = self.containerFrame
      cloneObject.mode            = self.mode
      cloneObject._isNone  	  = self._isNone
      return cloneObject

   def copy(self, other):
      "copies each field of the other object into its own state"
      ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
      self.prefix = other.prefix

      self.classAttribs = other.classAttribs

      self.constName       = other.constName
      self.constCodeWidget = other.constCodeWidget
      self.constCode       = other.constCode
      self.language        = other.language
      self.kind            = other.kind
      self.actions         = other.actions
      self.containerFrame  = other.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      "converts the values into a string..."
      if self.constCodeWidget:					# if the code widget is visible, update the attribute value
         self.constCode = self.constCodeWidget.get(1.0, END)
      if self.constCode: 					# show some portion of the code
         maxLen = min( len(self.constCode)-1, 10)
         result = self.constName.toString()+" : "+self.constCode[0:maxLen]
      else: result = self.constName.toString()
      if maxWide: return result[:maxWide]
      return result

   def isNone(self):
      "checks if the value is equivalent to None"
      return self._isNone == 1

   def setNone (self):
      "sets the type value equivalent to None"
      self._isNone = 1
      return 1

   def unSetNone (self):
      "calls unSetNone on all its attributes"
      self._isNone = 0
      return 1


   def setValue(self, value):
      """sets the value, value can be a tuple (name, language->integer, kind->(none or enum), actions->none or ([s1, s2, ...], number) code)
         or a string or None"""

      if type(value) == NoneType:                                       # INPUT = None. Valid (to set to None the object)
         self.setNone()
         return
      elif type(value) == StringType:					# INPUT = String. Valid (constraint name)
         if not self.constName:
            self.constName    = ATOM3String(value)			# constraint name
         else: self.constName.setValue(value)
         return
      elif type(value) == TupleType and len(value) == 5:                # Tuple Type of size 5
         name, language, kind, actions, code = value
      else:
         raise ATOM3BadAssignmentValue, "ATOM3Constraint: Bad type in setValue()"

      if not self.constName:
         self.constName    = ATOM3String(name)				# constraint name
      else: self.constName.setValue(name)

      if type(language) == TupleType:					# May be is a tuple ([languages...], selected)
         self.language.setValue(language)				# the pass it to self.language
      elif type(language) == IntType:                                  	# otherwise it is the selected language
         self.language.setValue((None, language))		
      else:
         raise ATOM3BadAssignmentValue, "ATOM3Constraint: Bad type in setValue() (2nd argument in tuple)"

      if kind:								# if it is present is a tuple ([types...], selectedType)
        if type(kind) == TupleType and len(kind) == 2:
           if not self.kind: self.kind = ATOM3Enum(kind[0], kind[1])
           else:
              try:
                 self.kind.setValue((None,kind[1]))                   # set kind of constraint if specified
              except ATOM3BadAssignmentValue:
                 raise ATOM3BadAssignmentValue, "ATOM3Constraint: Bad type in setValue(), "+ str(kind)
        elif type(kind) != NoneType:
           raise ATOM3BadAssignmentValue, "ATOM3Constraint: Bad type in setValue() (3rd argument in tuple)"
	
      if actions:
        if type(actions) == TupleType and len(actions) == 2:
           if not self.actions: self.actions = ATOM3MSEnum(actions[0], actions[1], 0, ATOM3MSEnum.LISTBOX)
           else: self.actions.setValue((None,actions[1]))		# set action where it must be evaluated, if specified
        else:
           raise ATOM3BadAssignmentValue, "ATOM3Constraint: Bad type in setValue() (4th argument in tuple)"

      if type(code) == StringType or type(code) == NoneType:
         self.constCode = code
         if self.constCode and self.constCodeWidget:
            self.constCodeWidget.insert(1.0, self.constCode)
      else:
         raise ATOM3BadAssignmentValue, "ATOM3Constraint: Bad type in setValue() (5th argument in tuple)"

   def setHeight(self, height=None):
       """
       Sets the height of the text box (as it appears visually)
       Parameter:
         height, integer value, represents # of lines of text
         If height == None, then uses self.heightATOM3Integer instead, this is 
         changed via the createTabPanel() and in the __init__ routine of course.
       """
       if(height):
         self.heightATOM3Integer.setValue(height)
       else:
         height = self.heightATOM3Integer.getValue()
       if(self.constCodeWidget != None):
         self.constCodeWidget.config(height=height)


   def getValue(self):
      "returns the constraint value in a tuple (name, language->integer, kind->(none or integer), actions->(none or integer), code)"
      if self.constCodeWidget:					# if the code widget is visible, update the attribute value
         self.constCode = self.constCodeWidget.get(1.0, END)

      theKind    = None
      theActions = None
      if self.kind: theKind = self.kind.getValue()
      if self.actions: theActions = self.actions.getValue()
      return (self.constName.getValue(), self.language.getValue(), theKind, theActions, self.constCode )

   def show (self, master, topWindowParent = None):
      "method that returns a widget to edit the constraint"
      ATOM3Type.show(self, master, topWindowParent)

      self.containerFrame = Frame(master) 			# container frame
      topFrame = Frame(self.containerFrame)			# frame to contain contraint name widget
      
      nameFrame = Frame( topFrame )
      Label(nameFrame, text="Constraint name: ", bg='light blue',
             relief='groove', padx=20).pack(side=TOP) # constraint name label
      if not self.constName:
         self.constName    = ATOM3String()			# constraint name
      constNameWidget = self.constName.show(nameFrame)
      constNameWidget.pack(side=TOP)
      nameFrame.pack(side=LEFT)
      #topFrame.pack(side=TOP)					# pack the frame in the containerFrame

      #aFrame = Frame(self.containerFrame)
         
      # DON'T show language widget since OCL is not implemented in AToM3 - Denis
      #languageWidget  = self.language.show(topFrame)
      #languageWidget.pack(side=LEFT)

      if self.kind:
         kindWidget = self.kind.show(topFrame)
         kindWidget.pack(side=LEFT)

      if self.actions:
         actionsWidget = self.actions.show(topFrame)
         actionsWidget.pack(side=LEFT)
      
      createTabPanel( self, topFrame)
      
      #aFrame.pack(side=TOP)
      topFrame.pack(side=TOP, fill=X)

      yscrollbar = Scrollbar(self.containerFrame, orient=VERTICAL)
      xscrollbar = Scrollbar(self.containerFrame, orient=HORIZONTAL)
     
      self.constCodeWidget = Text(self.containerFrame, bg='white',
                                  wrap='word', width = 80, padx=4,
                                  xscrollcommand = xscrollbar.set, 
                                  yscrollcommand = yscrollbar.set, 
                                  font = ('courier', 10), exportselection=False,
                                  height=self.heightATOM3Integer.getValue())
                                  #font = "{System} 10")
                                  
#      self.constCodeWidget = Text(self.containerFrame, bg='white',
#                                  wrap=CHAR, width = 80, padx=4,
#                                  xscrollcommand = xscrollbar.set, 
#                                  yscrollcommand = yscrollbar.set, 
#                                  font = ('courier', 10))
#                                  #font = "{System} 10")

      yscrollbar.pack(side=RIGHT, fill = Y)
      self.constCodeWidget.pack(side=TOP)
      xscrollbar.pack(side=BOTTOM, fill = X)

      yscrollbar.config(command = self.constCodeWidget.yview)
      xscrollbar.config(command = self.constCodeWidget.xview)

      if self.constCode:
         self.constCodeWidget.insert(1.0, self.constCode)

      self.constCodeWidget.bind("<Button-3>", self.showPopup)	# create a pop-up menu with the UML class attributes...
      #self.constCodeWidget.bind("<Return>", self.processReturn )# catch the <return> event...

      self.textWidget = self.constCodeWidget
      self.textWidget.bind("<Delete>", lambda e=None,s=self: processDelete(s) )  
      self.textWidget.bind("<BackSpace>", lambda e=None,s=self: processBackspace(s) )  
      self.textWidget.bind("<Tab>", lambda e=None,s=self: processTab(s) )  
      self.textWidget.bind("<Return>",  lambda e=None,s=self: processReturn(s) )  
      setTabs(self)
      addFiltersFromIDLE(self)
      
      return self.containerFrame
   '''
   def processReturn(self, event):
      "Adds a return to the text..."
      self.constCodeWidget.insert( INSERT, "\n")
      return "break"
    '''

   def showPopup(self, event):
      "Shows a pop-up menu with the class' attributes"
      self.popupMenu = Menu(self.constCodeWidget)
      if self.classAttribs and len(self.classAttribs)>0:			# check wether we have a list of attributes, or "pasteable things"
           for attrib in self.classAttribs:
              if type(attrib) == StringType:
                 self.attr = attrib
              else:
                 self.attr = attrib.getValue()[0]
              self.popupMenu.add_command(label=self.prefix+self.attr, command=lambda x=(self, self.attr): x[0].pasteAttribute(x[1]) )              
           self.popupMenu.post(event.x_root, event.y_root)

   def pasteAttribute(self, attrib):
      "gets the selected menu item and pastes it in self.constText"
      self.constCodeWidget.insert(CURRENT, self.prefix+attrib)

   def invalid(self):
      "decides if the widget values are valid"     
      if not self.isNone():
         val = self.constName.getValue() 					# obtain constraint name
         if not val or val == "":						# check that it has some value
            return "Contraint must have a name"            		        # raise the error
      # check if the constraint's been associated with an event

      #if not self.isNone():
      #   evtSel = self.actions.getValue()[1]                                    # Get the list selected events
      #   if not 1 in evtSel:                                                    # Did not found a selected event
      #      return "Constraint must be associated with some event"
      
      # compile the code in the constraint, in case of Python
      # lngs, sel = self.language.getValue()                              # check if the language is Python
      # print "lngs = ", lngs, " sel = ", sel
      #if lngs[sel] == 'Python':                                         # It is Python
      #   if self.constCodeWidget:                                       # if the widget is visible, update value
      #      self.constCode = self.constCodeWidget.get(1.0, END)
      #   try:
      #      a = compile_command(self.constCode)                             # Try the compiler on the written code
      #   except SyntaxError, errorText:
      #      msg, arg = errorText
      #      fileno, lineno, offset, text = arg
      #      ptext = text[:offset-1]+">>>"+text[offset-1]+"<<<"+text[offset:]
      #      return errorText[0]+" in : "+ptext
      #   except OverflowError, args:
      #      text = "Overflow Error: "+args[0]+" !"
      #      return text
      #   if not a:
      #      return "Syntax Error!"
      return None

   def destroy(self):
      "destroys graphical widgets and actualizes attributes value"
      if self.constCodeWidget:					# if the widget is visible, update value and destroy
         self.constCode       = self.constCodeWidget.get(1.0, END)
         self.constCodeWidget = None
      if self.constName: self.constName.destroy()                                  # destroy name
      if self.language: self.language.destroy()                 # destroy language type enumeration
      if self.containerFrame: self.containerFrame = None        # destroy container frame
      if self.kind: self.kind.destroy()                         # destroy kind, if it exisits
      if self.actions: self.actions.destroy()			# destroy actions, if it exists

   def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
      if self.constCodeWidget:					# if the code widget is visible, update the attribute value
         self.constCode = self.constCodeWidget.get(1.0, END)
      file.write(indent+objName+"=ATOM3Constraint()\n")
      if self.isNone():
         file.write(indent+objName+".setNone()\n")
      else:
         if self.constCode:
            constraintCode = replace( self.constCode, '\\', '\\'+'\\')
            constraintCode = replace( constraintCode, "'", "\\'")                        
            constraintCode = replace( constraintCode, '\n', '\\n')
            file.write(indent+objName+".setValue(('"+ self.constName.toString()+"', "+
       						   str(self.language.getValue())+", "+
      						   str(self.kind.getValue())+", "+
      						   str(self.actions.getValue())+", '"+
      						   constraintCode+"'))\n")
         else:
            file.write(indent+objName+".setValue(('"+ self.constName.toString()+"', "+
       						   str(self.language.getValue())+", "+
      						   str(self.kind.getValue())+", "+
      						   str(self.actions.getValue())+", None))\n")

   def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
      if self.constCodeWidget:					# if the code widget is visible, update the attribute value
         self.constCode = self.constCodeWidget.get(1.0, END)
      if self.isNone():
         file.write(indent+objName+".setNone()\n")
      else:
         if(self.constCode):
            # Check if code is empty
            tempCode = self.constCode
            tempCode = tempCode.replace( '\n', '')
            tempCode = tempCode.replace( ' ', '')
            tempCode = tempCode.replace( '\t', '')
            tempCode = tempCode.replace( '\r', '')
            if(len(tempCode) == 0):
              self.constCode = None
              return self.writeValue2File(file, indent, objName, depth, 
                                          generatingCode)
            # Fix up code for printing to file
            constraintCode = replace( self.constCode, '\\', '\\'+'\\')
            constraintCode = replace( constraintCode, "'", "\\'")            
            constraintCode = replace( constraintCode, '\n', '\\n')
            file.write(indent+objName+".setValue(('"+ self.constName.toString()+"', "+
       						str(self.language.getValue())+", "+
      						str(self.kind.getValue())+", "+
      						str(self.actions.getValue())+", '"+
      						constraintCode+"'))\n")
         else:
            file.write(indent+objName+".setValue(('"+ self.constName.toString()+"', "+
       						str(self.language.getValue())+", "+
      						str(self.kind.getValue())+", "+
      						str(self.actions.getValue())+", None))\n")


   def getNameCode( self ):
      """ Returns the name & the code in the constraint """
      constTuple = self.getValue()
      if( constTuple[4] == None ): return [ constTuple[0], None ]
      return [ constTuple[0], strip( constTuple[4] ) ]
