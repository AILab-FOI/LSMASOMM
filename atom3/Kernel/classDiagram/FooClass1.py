# __FooClass1.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from graph_FooClass1 import *
class FooClass1(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_FooClass1
      self.parent = parent
      self.name=ATOM3String('')
      self.generatedAttributes = {'name': ('ATOM3String', )      }
      self.realOrder = ['name']
      self.directEditing = [1]
   def clone(self):
      cloneObject = FooClass1( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


