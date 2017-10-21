"""
__canAccessKnArt.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: bogdan
Modified: Sat Oct 21 18:15:29 2017
________________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from graph_canAccessKnArt import *
class canAccessKnArt(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_canAccessKnArt
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(False)
      self.parent = parent
      self.ID=ATOM3String('accKA|', 20)
      self.keyword_= self.ID
      self.generatedAttributes = {'ID': ('ATOM3String', )      }
      self.realOrder = ['ID']
      self.directEditing = [1]
   def clone(self):
      cloneObject = canAccessKnArt( self.parent )
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
      if actionID == self.CONNECT:
         res = self.ConstraintKnArt(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def ConstraintKnArt(self, params):
      from CustomCode import *
      res = canAccessKnArtCheckConnections(self)
      
      if res is "eitherRoleOrUnit":
          return ("Either Role of OrgUnit can access knowledge.", self.graphObject_)
      elif res is "onlyOneInput":
          return ("Only one Role or OrgUnit can access one knowledge medium.", self.graphObject_)
      elif res is "RoleWithOrgOnly":
          return ("Role can access OrganisationalKnArt only!", self.graphObject_)
      elif res is "OrgUnitWithIndivOnly":
          return ("OrgUnit can access IndividualKnArt only!", self.graphObject_)
      else:
          return
      
      

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
      
      



