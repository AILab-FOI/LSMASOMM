# __ASG_GGEditMetaModel.py_____________________________________________________
from ASG import *
from ATOM3Type       import *
from ATOM3           import *
class ASG_GGEditMetaModel(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, ASGroot, ['ASG_GGEditMetaModel' ,'GGruleEdit'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.generatedAttributes = {      }
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      rs = 
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs


   def getValue(self):
      return ()

   def setValue(self, value):
      pass

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"

   def clone(self):
      cloneObject = GGEditMetaModel( self.parent )
      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      ASGNode.copy(self, other)

   def destroy(self):
      self.containerFrame = None
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None


