#  Implements  : class ATOM3Constraint
#  Author      : Juan de Lara
#  Description : A class for the ATOM3 Constraint type.
#  Modified    : 17 Oct 2002
#  Changes     :
# ____________________________________________________________________________________________________________________
from Tkinter         import *
from ATOM3Type       import ATOM3Type
from ATOM3Exceptions import *
from code 	         import *
from string          import replace, rstrip

from ATOM3Integer import ATOM3Integer
from textUtilities import setTabs,createTabPanel, addFiltersFromIDLE
from textUtilities import processBackspace, processDelete
from textUtilities import processTab, processReturn

class ATOM3Text(ATOM3Type):
    def __init__(self, initialValue = "", width = 80, height = 15):
       """
          Initialize textBody to initialValue and textWidget to None
       """
       ATOM3Type.__init__(self )
       self.textBody = initialValue			# widget to be create when show is called
       self.textWidget = None
       self._isNone = 0					# for the moment it is not none
       self.myWidth  = width
       self.myHeight = height
       self.heightATOM3Integer = ATOM3Integer(height)

    def isNone (self):
       """
          check if the type value is none
       """
       return self._isNone

    def setNone (self):
       """
          sets to None the attribute value
       """
       self._isNone = 1

    def setValue(self, value):
       """
          Sets the actual attribute value
       """       
       # check that we have the correct type (a string)
       if type(value) != StringType and type(value) != NoneType:
          raise ATOM3BadAssignmentValue, "in setValue(), a string was expected"
       self.textBody = value                            # Assign the value to the attribute
       if self.textWidget:                              # if the widget's been shown
         self.textWidget.delete(1.0, END)       	# delete from graphical field
         if value:
            self.textBody = value 
            self.textWidget.insert(1.0, value)		# insert into graphical field
         else:                                          # this means we want to set it to None
            self.setNone() 

    def getValue(self):
       """
          Gets the actual attribute value
       """
       if self.textWidget:                              # if the widget exists, the get its value...
          self.textBody = self.textWidget.get(1.0, END) # synchronize textBody and textWidget
       return self.textBody                             # return textBody

    def toString(self, maxWide = None, maxLines = None ):
       """
          Returns the string representation of this type, having at most "maxLines" lines
          and "maxWide" width.
       """
       if self.textWidget:                              # if the widget exists, then get its value...
          self.textBody = self.textWidget.get(1.0, END) # synchronize textBody and textWidget
       if self.textBody:
          self.textBody = rstrip( self.textBody, '\n' ) # Added by Denis Dube, Summer 2004, to remove excess \n
          self.textBody += '\n'                         # Put one \n back, rstrip is a bit agressive...
          result   = ""                                 # Auxiliary variable with the result
          current, numLines, currWidth = 0, 0, 0
          max      = len(self.textBody)
          if maxWide == None: maxWide = max
          if maxLines == None: maxLines = 50
          while (1):
             if current >= max: return result           # if we've gone over the textBody's with, return result
             
             cchar = self.textBody[current]             # get the current character
             if cchar == '\n':
                 numLines = numLines + 1                # increment the number of lines so far...
                 currWidth = -1
             if numLines > maxLines: return result      # ... if bigger than the maximum, return result
             currWidth = currWidth + 1                  # increment the width so far...
             
             result= result+self.textBody[current]
             if currWidth > maxWide:                    # if we're over the max width, find next '\n'
                 while (current < max and self.textBody[current] != '\n'):
                     current = current + 1
                 if current >= max: return result
                 result = result + '\n'                 # add a new line...
                 currWidth = 0
             current = current + 1    
       else: return ""
       
    def setHeight(self, height=None):
       """
       Sets the height of the text box (as it appears visually)
       Parameter:
         height, integer value, represents # of lines of text
         If height == None, then uses self.heightATOM3Integer instead, this is 
         changed via the createTabPanel() and in the __init__ routine of course.
       """
       if(height):
         self.myHeight = height
       else:
         self.myHeight = self.heightATOM3Integer.getValue()
       if(self.textWidget != None):
         self.textWidget.config(height=self.myHeight)
         

    def show(self, parent, parentTopWindow = None ):
       """
          Creates an entry to show the value
       """
       ATOM3Type.show(self, parent, parentTopWindow )

       self.containerFrame = Frame(parent) 			# container frame
       yscrollbar = Scrollbar(self.containerFrame, orient=VERTICAL)
       xscrollbar = Scrollbar(self.containerFrame, orient=HORIZONTAL)
       
       self.textWidget = Text(self.containerFrame, bg='white',
                              xscrollcommand = xscrollbar.set, 
                              yscrollcommand = yscrollbar.set, 
                              width = self.myWidth, height=self.myHeight,
                              padx=4, wrap='word', exportselection=False,                                
                              font = ('courier', 10))
                                  #font = "{System} 10")
     
       createTabPanel(self, self.containerFrame,frameSide='top' )

       yscrollbar.pack(side=RIGHT, fill = Y)
       self.textWidget.pack(side=TOP)
       xscrollbar.pack(side=BOTTOM, fill = X)

       yscrollbar.config(command = self.textWidget.yview)
       xscrollbar.config(command = self.textWidget.xview)

       if self.textBody:
          self.textWidget.insert(1.0, self.textBody)

       #self.textWidget.bind("<Return>", self.processReturn )# catch the <return> event...

       self.textWidget.bind("<Delete>", lambda e=None,s=self: processDelete(s) )  
       self.textWidget.bind("<BackSpace>", lambda e=None,s=self: processBackspace(s) )  
       self.textWidget.bind("<Tab>", lambda e=None,s=self: processTab(s) )  
       self.textWidget.bind("<Return>",  lambda e=None,s=self: processReturn(s) )  
       setTabs(self)
       addFiltersFromIDLE(self)
      
       return self.containerFrame

    def processReturn(self, event):
       """
          Bind method for <return>. Adds a return to the text.
       """
       self.textWidget.insert( INSERT, "\n")
       return "break"

    def destroy(self):
       """
          Stores the widget value into the variable
       """
       if self.textWidget:      
          self.textBody = self.textWidget.get(1.0, END)
          self.myHeight = self.heightATOM3Integer.getValue()
          self.textWidget = None     # destroy graphical widget

    def clone(self):
       """
          Makes an exact copy of this object
       """
       cloneObject = ATOM3Text("", self.myWidth, self.myHeight)
       cloneObject.parent     = self.parent
       cloneObject.mode       = self.mode
       cloneObject.textBody   = self.textBody
       cloneObject.textWidget = self.textWidget
       return cloneObject

    def copy(self, other):
       """
          copies each field of the other object into its own state
       """
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.textBody   = other.textBody
       self.textWidget = other.textWidget

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       """
          Method that writes into a file the constructor and the value of the object. Must be overriden in children
       """
       replacedStr = self.toString()                                        
       replacedStr = replace( replacedStr, '\\', '\\'+'\\')                 
       replacedStr = replace( replacedStr, "'", "\\'")                      
       replacedStr = replace( replacedStr, '\n', '\\n')                     
       file.write(indent+objName+"=ATOM3Text('"+replacedStr+"', "+str(self.myWidth)+","+str(self.myHeight)+" )\n")

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       """
          Method that writes into a file the constructor and the value of the object. Must be overriden in children
       """
       replacedStr = self.toString()                                        
       replacedStr = replace( replacedStr, '\\', '\\'+'\\')                 
       replacedStr = replace( replacedStr, "'", "\\'")                      
       replacedStr = replace( replacedStr, '\n', '\\n')                     
       file.write(indent+objName+".setValue('"+replacedStr+"')\n")     
       file.write(indent+objName+".setHeight("+str(self.myHeight)+")\n")     
       if self.isNone():
         file.write(indent+objName+".setNone()\n")     

