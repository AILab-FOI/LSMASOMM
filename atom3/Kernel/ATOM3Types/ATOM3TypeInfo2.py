# __ATOM3TypeInfo2.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
class ATOM3TypeInfo2(ASGNode, ATOM3Type):

   def __init__(self, parent):
      ASGNode.__init__(self)
      self.parent = parent
      self.asdsad= ATOM3String()
      self.asdsad.setValue('asad')
      self.generatedAttributes = {'asdsad': ('ATOM3String', )      }
   def show(self, parent):
      ATOM3Type.show(self, parent)
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text='asdsad').grid(row=0,column=0,sticky=W)
      self.asdsad.show(self.containerFrame).grid(row=0,column=1,sticky=W)
      return self.containerFrame

   def toString(self):
      return       self.asdsad.toString()

   def getValue(self):
      return (self.asdsad.getValue(),)

   def setValue(self, value):
      self.asdsad.setValue(value[0])

   def clone(self):
      cloneObject = ATOM3TypeInfo2( self.parent )
      cloneObject.asdsad = self.asdsad.clone()
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.asdsad = other.asdsad
      ASGNode.copy(self, other)

   def destroy(self):
      self.asdsad.destroy()
      self.containerFrame = None
   def cardinalityCheck(self):
      return None
   def checkConnectedObjectType(self):
      last=self.connections_[len(self.connections_)-1]
      return None
   def preCondition (self, actionID):
      return None
   def postCondition (self, actionID):
      if actionID == self.CONNECT:
         res = self.checkConnectedObjectType()
         if res: return res
      return None


