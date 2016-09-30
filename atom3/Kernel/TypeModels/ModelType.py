# __ModelType.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from graph_ModelType import *
class ModelType(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_ModelType
      self.parent = parent
      self.Name=ATOM3String('')
      self.keyword_= self.Name
      self.MetaModelName=ATOM3String('')
      self.generatedAttributes = {'Name': ('ATOM3String', ),
                                  'MetaModelName': ('ATOM3String', )      }
      self.realOrder = ['Name','MetaModelName']
      self.directEditing = [1,1]
   def clone(self):
      cloneObject = ModelType( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      cloneObject.keyword_ = cloneObject.Name
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.Name
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


