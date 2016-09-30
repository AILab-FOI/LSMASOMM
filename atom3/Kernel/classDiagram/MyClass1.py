# __MyClass1.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Integer import *
from ATOM3Boolean import *
from graph_MyClass1 import *
class MyClass1(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_MyClass1
      self.parent = parent
      self.c=ATOM3String('')
      self.a=ATOM3Integer(0)
      self.b=ATOM3Boolean()
      self.b.setValue((None, 0))
      self.b.config = 0
      self.generatedAttributes = {'c': ('ATOM3String', ),
                                  'a': ('ATOM3Integer', ),
                                  'b': ('ATOM3Boolean', )      }
      self.realOrder = ['c','a','b']
      self.directEditing = [1,1,1]
   def clone(self):
      cloneObject = MyClass1( self.parent )
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


