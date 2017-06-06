"""
__ASG_LSMASOMM.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: bogdan
Modified: Tue Jun  6 19:48:52 2017
______________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
class ASG_LSMASOMM(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'LSMASOMM', ASGroot, ['ASG_LSMASOMM' ,'OrgUnit' ,'Role' ,'Action' ,'KnowledgeArtifacts' ,'OrganisationalKnArt' ,'IndividualKnArt' ,'Strategy' ,'Objective' ,'Process' ,'isPartOfOrgUnit' ,'canHaveRole' ,'hasActions' ,'canAccessKnArt' ,'isPartOfObjective' ,'hasObjective' ,'genericAssociation' ,'answersToRole' ,'canStartProcess' ,'answersToOrgUnit' ,'isPartOfRole'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.name=ATOM3String('LSMASOMM', 20)
      self.author=ATOM3String('Annonymous', 20)
      self.description=ATOM3Text('\n', 60,15 )
      self.title=ATOM3String('', 20)
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'author': ('ATOM3String', ),
                                  'description': ('ATOM3Text', ),
                                  'title': ('ATOM3String', )      }
      self.realOrder = ['name','author','description','title']
      self.directEditing = [1,1,1,1]
   def clone(self):
      return self
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
   def open(self, parent, topWindowParent):
       from ATOM3 import *
       a = ATOM3(topWindowParent, 'LSMASOMM', 0, 1, self)
       #self.writeContents(a)
       return a
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.SAVE:
         res = self.saveModelElements(params)
         if res: return res
      if actionID == self.CONNECT:
         res = self.addConnectionsToDB(params)
         if res: return res
      if actionID == self.EDIT or actionID == self.CREATE:
         res = self.CheckUniqueID(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def saveModelElements(self, params):
      from CustomCode import *
      
      SaveAll(self)
      
      

   def addConnectionsToDB(self, params):
      from CustomCode import *
      
      #addConnectionToDB(self)
      
      

   def CheckUniqueID(self, params):
      from CustomCode import *
      
      res = checkUniqueID(self)
      
      if res:
        return ("Duplicate ID: {}! Specify another.".format(res[1]), res[0])
      
      

   def preAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None


