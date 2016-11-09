"""
__Role.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: bogdan
Modified: Wed Nov  9 16:40:09 2016
______________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Boolean import *
from ATOM3List import *
from graph_Role import *
class Role(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_Role
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(True)
      self.parent = parent
      self.ID=ATOM3String('RoleID', 20)
      self.isMetaRole=ATOM3Boolean()
      self.isMetaRole.setValue((None, 0))
      self.isMetaRole.config = 0
      self.name=ATOM3String('role name', 20)
      self.roleActions=ATOM3List([ 1, 1, 1, 0],ATOM3String)
      lcobj0=[]
      cobj0=ATOM3String('RoleAction1', 20)
      lcobj0.append(cobj0)
      cobj0=ATOM3String('RoleAction2', 20)
      lcobj0.append(cobj0)
      cobj0=ATOM3String('RoleActionN', 20)
      lcobj0.append(cobj0)
      self.roleActions.setValue(lcobj0)
      self.generatedAttributes = {'ID': ('ATOM3String', ),
                                  'isMetaRole': ('ATOM3Boolean', ),
                                  'name': ('ATOM3String', ),
                                  'roleActions': ('ATOM3List', 'ATOM3String')      }
      self.realOrder = ['ID','isMetaRole','name','roleActions']
      self.directEditing = [0,1,1,1]
   def clone(self):
      cloneObject = Role( self.parent )
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
      if actionID == self.CONNECT:
         res = self.RoleConstraintKnArt(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def RoleConstraintKnArt(self, params):
      
      from CustomCode import *
      
      res = RoleCheckOutputs(self)
      if res is "manyKnArts":
          return ("Roles can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)
      elif res is "IndivKnArtError":
          return ("Roles can have OrganizationalKnArt only!", self.graphObject_)
      else:
          return
      
      

   def preAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if actionID == self.CONNECT or actionID == self.DISCONNECT or actionID == self.SELECT:
         self.checkMetaRole(params)
      if actionID == self.CONNECT or actionID == self.SELECT:
         self.InheritActions(params)
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None
   def QOCA(self, params):
      """
      QOCA Constraint Template
      NOTE: DO NOT select a POST/PRE action trigger
      Constraints will be added/removed in a logical manner by other mechanisms.
      """
      return # <---- Remove this to use QOCA
      
      """ Get the high level constraint helper and solver """
      from Qoca.atom3constraints.OffsetConstraints import OffsetConstraints
      oc = OffsetConstraints(self.parent.qocaSolver)  
      
      """
      Example constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py
      For more types of constraints
      """
      oc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)
      oc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)
      
      

   def checkMetaRole(self, params):
      from CustomCode import RoleHierarchy
      res = RoleHierarchy(self)
      self.isMetaRole.setValue(('isMetaRole',res))
      self.graphObject_.ModifyAttribute('isMetaRole', res)
      
      

   def InheritActions(self, params):
      from CustomCode import RoleInheritance
      res = RoleInheritance(self)
      if res:
      ##    actions = self.roleActions.getValue()
      ##    for r in res:
      ##    	actions.append(r)
      ##    print actions
      ##    self.roleActions.setValue(actions)
          self.graphObject_.ModifyAttribute('roleActions', self.roleActions.toString())
      
      



