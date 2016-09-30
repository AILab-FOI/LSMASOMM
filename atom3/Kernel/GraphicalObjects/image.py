# __image.py_____________________________________________________
# This file was hand coded from rectangle.py
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Integer import *
from graph_image import *
class image(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_image
      self.parent = parent
      self.generatedAttributes = { }
      
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      return 'image'


   def getValue(self):
      return ()
    
   def setValue(self, value):
      pass

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
      pass
   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"
      pass
   def invalid(self):
      ASGNode.GGcheckSetNone(self)
      return False 

   def clone(self):
      cloneObject = image( self.parent )
      ASGNode.cloneActions(self, cloneObject)
      return cloneObject
    
   def copy(self, other):
      ATOM3Type.copy(self, other)
      ASGNode.copy(self, other)

   def destroy(self):
      ASGNode.GGcheckSetNone(self)
      self.containerFrame = None
      
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
      
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


