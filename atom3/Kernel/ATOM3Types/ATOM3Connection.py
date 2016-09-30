# __ File: ATOM3Connection.py __________________________________________________________________________________________________
#  Implements  : class ATOM3Connection
#  Author      : Juan de Lara
#  Description : This is the class to regulate connections between entities.
#  Modified    : 23 Oct 2001
#  Changes :
# ______________________________________________________________________________________________________________________________

from Tkinter import *
from types           import *
from ATOM3Type       import *
from ATOM3String     import *
from ATOM3Enum       import *
from ATOM3Exceptions import *

class ATOM3Connection(ATOM3Type):

    def __init__(self, ASGclass = None, minValue = 0, maxValue = 'N' ):
        "It receives a class, to obtain the name from"
        ATOM3Type.__init__(self)
        self.containerFrame = None 
        if( ASGclass and ASGclass.keyword_ ): 
          self.className = ATOM3String ( ASGclass.keyword_.toString() )
        else: self.className = ATOM3String()
        self.minValue     = ATOM3String( minValue )
        self.maxValue     = ATOM3String( maxValue )

        self.direction       = ATOM3Enum(("Source", "Destination"), 1)

    def clone(self):
        "makes an exact copy of itself"
        cloneObject = ATOM3Connection( )
        cloneObject.className = self.className.clone()
        cloneObject.minValue  = self.minValue.clone()
        cloneObject.maxValue  = self.maxValue.clone()
        cloneObject.direction = self.direction.clone()
        cloneObject.containerFrame = self.containerFrame
        return cloneObject

    def copy(self, other):
        "copies each field of the other object into its own state"
        ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
        self.className      = other.className
        self.minValue       = other.minValue
        self.maxValue       = other.maxValue
        self.direction      = other.direction
        self.containerFrame = other.containerFrame
        self.mode           = other.mode

    def show (self, parent, parentTopWindow = None ):
        "Shows the widgets to edit the values"
        ATOM3Type.show(self, parent, parentTopWindow )
        self.containerFrame = Frame(parent)  
        
        i = 0
        self.className.show(self.containerFrame).grid(row=i, column=0, sticky=W)
        i += 1
        
        text = '\nWARNING: Do not change the SOURCE/DESTINATION'
        helpLabel = Label(self.containerFrame, text=text, font=("Helvetica", 10))
        helpLabel.grid(row=i, column=0, columnspan=2, sticky=W)
        i += 1
        
        self.direction.show (self.containerFrame).grid(row=i, column=0, sticky=W)
        i += 1
        
        isDestination = self.direction.getValue()[1]
        if(isDestination):
          text = 'Arrow starting at ' +  self.className.getValue() \
                  + ' and going to self'
        else:
          #text = 'Arrow going TO ' +  self.className.getValue() + ' from self'
          text = 'Arrow starting at self and going to ' \
                  + self.className.getValue() 
        helpLabel = Label(self.containerFrame, text=text, font=("Helvetica", 10))
        helpLabel.grid(row=i, column=0, columnspan=2,sticky=W)
        i += 1
        
        self.minValue.show (self.containerFrame).grid(row=i, column=0, sticky=W)
        text = 'Minimum cardinality'
        helpLabel = Label(self.containerFrame, text=text, font=("Helvetica", 10))
        helpLabel.grid(row=i, column=1, sticky=W)
        i += 1
        self.maxValue.show (self.containerFrame).grid(row=i, column=0, sticky=W)
        text = 'Maximum cardinality (N = Infinity)'
        helpLabel = Label(self.containerFrame, text=text, font=("Helvetica", 10))
        helpLabel.grid(row=i, column=1, sticky=W)
        i += 1
        
        return self.containerFrame
                
    def setValue(self, value):
        "sets the name, type and initial value (parameter value is a tuple)"
        ASGobject, direction, minValue, maxValue = value
        if ASGobject:
           # see if it is already a String
           if type(ASGobject) == StringType:            # A string type
              self.className.setValue(ASGobject)
           elif type(ASGobject) == InstanceType:        # A user defined class
              bases = [str(ASGobject.__class__)]        # see if the class or base classes derive from ASGNode
              for b in ASGobject.__class__.__bases__: bases.append(str(b))
              if not "ASGNode.ASGNode" in bases:
                 raise ATOM3BadAssignmentValue, "ATOM3Connection: Bad type in setValue(), "+str(ASGobject)
              # check if object has a keyword...
              if ASGobject.keyword_:
                 self.className.setValue(ASGobject.keyword_.toString())
              else:
                 self.className.setValue(str(ASGobject))
           else:
              raise ATOM3BadAssignmentValue, "ATOM3Connection: Bad type in setValue(), "+str(ASGobject)              
        if direction:
           # see if it is a tuple...
           if type(direction) == TupleType:
              try:
                 self.direction.setValue(direction)
              except ATOM3BadAssignmentValue:
                 raise ATOM3BadAssignmentValue, "ATOM3Connection: Out of range, "+str(direction)
           else:
              try:
                 self.direction.setValue((None, direction))
              except ATOM3BadAssignmentValue:
                 raise ATOM3BadAssignmentValue, "ATOM3Connection: Out of range, "+str(direction)
        if minValue:
           if type(minValue) == StringType:  self.minValue.setValue(str(minValue))
           else: raise ATOM3BadAssignmentValue, "ATOM3Connection: bad type, "+str(minValue)
        if maxValue:
           if type(maxValue) == StringType: self.maxValue.setValue(str(maxValue))
           else: raise ATOM3BadAssignmentValue, "ATOM3Connection: bad type, "+str(maxValue)

    def toString(self):
        "converts the values into a string"
        stRet = self.className.toString()+" dir= "+ self.direction.toString()+", min= "+self.minValue.toString()+", max="+self.maxValue.toString()
        return stRet

    def getValue(self):
        "returns a tuple with (className, direction, minValue, maxValue)"
        return ( self.className.getValue(), self.direction.getValue(), self.minValue.getValue(), self.maxValue.getValue() )

    def destroy(self):
        "destroys graphical widgets and updates internal attribute values"
        self.className.destroy()
        self.direction.destroy()
        self.minValue.destroy()
        self.maxValue.destroy()

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+"=ATOM3Connection()\n")
       self.writeValue2File(file, indent, objName, depth)
       pass

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+".setValue("+str(self.getValue())+")\n")
       if self.isNone():
         file.write(indent+objName+".setNone()\n")  
                                 
    def hasEqualValue(self, obj):
       """Two objects of this type are the same if have same name and same direction,
          PRECONDITION : obj has type ATOM3Connection """
       if obj.getTypeName() != self.getTypeName(): return 0		# objects don't have not the same type!
       myValue = self.getValue()					# obtain my value, tuple (className, direction, minValue, maxValue)
       hisValue= obj.getValue()						# obtain his value
       return myValue[0] == hisValue[0] and myValue[1] == hisValue[1]	# same class and same direction

    def setNone(self):
       """ Sets object's value to None """
       self.className.setNone()
       self.minValue.setNone()
       self.maxValue.setNone()
       self.direction.setNone()

    def isNone(self):
       """ Returns 1 if object is None, 0 in other case"""
       if self.className.isNone() and self.minValue.isNone() and self.maxValue.isNone() and self.direction.isNone():
          return 1
       else: return 0




