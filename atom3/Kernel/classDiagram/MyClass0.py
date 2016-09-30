# __MyClass0.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3Integer import *
from ATOM3Boolean import *
from graph_MyClass0 import *
class MyClass0(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_MyClass0
      self.parent = parent
      self.a=ATOM3Integer(0)
      self.b=ATOM3Boolean()
      self.b.setValue((None, 0))
      self.b.config = 0
      self.generatedAttributes = {'a': ('ATOM3Integer', ),
                                  'b': ('ATOM3Boolean', )      }
      self.realOrder = ['a','b']
      self.directEditing = [1,1]
   def clone(self):
      cloneObject = MyClass0( self.parent )
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


