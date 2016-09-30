"""
__CD_Inheritance3.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: Denis Dube
Modified: Sat Feb 04 17:56:37 2006
_________________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from graph_CD_Inheritance3 import *
class CD_Inheritance3(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_CD_Inheritance3
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(False)
      self.parent = parent
      self.generatedAttributes = {      }
      self.realOrder = []
      self.directEditing = []
   def clone(self):
      cloneObject = CD_Inheritance3( self.parent )
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
   def preAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if actionID == self.CONNECT or actionID == self.MOVE:
         self.rotateMoveArrowEnd(params)
      if actionID == self.CONNECT or actionID == self.DISCONNECT:
         self.connectDisconnect(params)
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None
   def rotateMoveArrowEnd(self, params):
      # rotateMoveArrowEnd
      self.graphObject_.rotateMoveArrowEnd()
      
      

   def connectDisconnect(self, params):
      from inheritanceCodeBase import inheritanceCodeBase
      inheritanceCodeBase(self)
      
      
      



