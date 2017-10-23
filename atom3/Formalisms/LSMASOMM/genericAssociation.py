"""
__genericAssociation.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: bogdan
Modified: Sun Oct 22 23:29:30 2017
____________________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Text import *
from graph_genericAssociation import *
class genericAssociation(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_genericAssociation
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(False)
      self.parent = parent
      self.ID=ATOM3String('genR|', 20)
      self.keyword_= self.ID
      self.name=ATOM3String('', 20)
      self.Description=ATOM3Text('\n', 80,10 )
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'Description': ('ATOM3Text', ),
                                  'ID': ('ATOM3String', )      }
      self.realOrder = ['name','Description','ID']
      self.directEditing = [1,1,1]
   def clone(self):
      cloneObject = genericAssociation( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      cloneObject.keyword_ = cloneObject.ID
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.ID
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
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None
   def QOCA(self, params):
      """
      QOCA Constraint Template
      NOTE: DO NOT select a POST/PRE action trigger
      Constraints will be added/removed in a logical manner by other mechanisms.
      """
      return # <--- Remove this if you want to use QOCA
      
      # Get the high level constraint helper and solver
      from Qoca.atom3constraints.OffsetConstraints import OffsetConstraints
      oc = OffsetConstraints(self.parent.qocaSolver)  
      
      # Constraint only makes sense if there exists 2 objects connected to this link
      if(not (self.in_connections_ and self.out_connections_)): return
      
      # Get the graphical objects (subclass of graphEntity/graphLink) 
      graphicalObjectLink = self.graphObject_
      graphicalObjectSource = self.in_connections_[0].graphObject_
      graphicalObjectTarget = self.out_connections_[0].graphObject_
      objTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)
      
      """
      Example constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py
      For more types of constraints
      """
      oc.LeftExactDistance(objTuple, 20)
      oc.resolve() # Resolve immediately after creating entity & constraint 
      
      



