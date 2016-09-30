# __ASG_ATOM3GraphicalObjects.py_____________________________________________________
from ASG import *
from ATOM3Type       import *
class ASG_ATOM3GraphicalObjects(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'ATOM3GraphicalObjects', ASGroot, ['ASG_ATOM3GraphicalObjects' ,'line' ,'oval' ,'polygon' ,'rectangle' ,'text'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.generatedAttributes = {      }
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      #from ATOM3 import *
      #a = ATOM3 (parentWindowInfo , 'ATOM3GraphicalObjects')
      #a.grid(row=0,column=0, columnspan = 2, sticky=W)
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      rs = ''

      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs


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
      return 

   def clone(self):
      return self
      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
   def destroy(self):
      ASGNode.GGcheckSetNone(self)
      self.destroyNodes()
      self.containerFrame = None
   def open(self, parent, topWindowParent):
       from ATOM3 import *
       a = ATOM3(topWindowParent, 'ATOM3GraphicalObjects', 0, 1, self)
       #self.writeContents(a)
       return a
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


