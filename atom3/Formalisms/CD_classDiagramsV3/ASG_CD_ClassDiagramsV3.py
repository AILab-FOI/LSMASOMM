"""
__ASG_CD_ClassDiagramsV3.py_____________________________________________________

Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)
Author: Denis Dube
Modified: Sat Feb 04 17:56:37 2006
________________________________________________________________________________
"""
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
from ATOM3List import *
from ATOM3Attribute import *
from ATOM3Enum import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Float import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *
class ASG_CD_ClassDiagramsV3(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'CD_ClassDiagramsV3', ASGroot, ['ASG_CD_ClassDiagramsV3' ,'CD_Class3' ,'CD_Association3' ,'CD_Inheritance3'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.name=ATOM3String('')
      self.keyword_= self.name
      self.author=ATOM3String('Annonymous')
      self.description=ATOM3Text('\n', 60,15 )
      self.attributes=ATOM3List([ 1, 1, 1, 0],ATOM3Attribute,parent.types )
      lcobj0=[]
      cobj0=ATOM3Attribute(parent.types)
      cobj0.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
      cobj0.initialValue=ATOM3String('')
      cobj0.isDerivedAttribute = False
      lcobj0.append(cobj0)
      cobj0=ATOM3Attribute(parent.types)
      cobj0.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
      cobj0.initialValue=ATOM3String('Annonymous')
      cobj0.isDerivedAttribute = False
      lcobj0.append(cobj0)
      cobj0=ATOM3Attribute(parent.types)
      cobj0.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
      cobj0.initialValue=ATOM3Text('\n', 60,15 )
      cobj0.isDerivedAttribute = False
      lcobj0.append(cobj0)
      self.attributes.setValue(lcobj0)
      self.constraints=ATOM3List([ 1, 1, 1, 0],ATOM3Constraint)
      lcobj0=[]
      self.constraints.setValue(lcobj0)
      self.showAssociationBox=ATOM3Boolean()
      self.showAssociationBox.setValue((None, 1))
      self.showAssociationBox.config = 0
      self.showAttributes=ATOM3Boolean()
      self.showAttributes.setValue((None, 1))
      self.showAttributes.config = 0
      self.showConditions=ATOM3Boolean()
      self.showConditions.setValue((None, 1))
      self.showConditions.config = 0
      self.showActions=ATOM3Boolean()
      self.showActions.setValue((None, 1))
      self.showActions.config = 0
      self.showCardinalities=ATOM3Boolean()
      self.showCardinalities.setValue((None, 1))
      self.showCardinalities.config = 0
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'author': ('ATOM3String', ),
                                  'description': ('ATOM3Text', ),
                                  'attributes': ('ATOM3List', 'ATOM3Attribute'),
                                  'constraints': ('ATOM3List', 'ATOM3Constraint'),
                                  'showAssociationBox': ('ATOM3Boolean', ),
                                  'showAttributes': ('ATOM3Boolean', ),
                                  'showConditions': ('ATOM3Boolean', ),
                                  'showActions': ('ATOM3Boolean', ),
                                  'showCardinalities': ('ATOM3Boolean', )      }
      self.realOrder = ['name','author','description','attributes','constraints','showAssociationBox','showAttributes','showConditions','showActions','showCardinalities']
      self.directEditing = [1,1,1,1,1,1,1,1,1,1]
   def clone(self):
      return self
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.name
   def open(self, parent, topWindowParent):
       from ATOM3 import *
       a = ATOM3(topWindowParent, 'CD_ClassDiagramsV3', 0, 1, self)
       #self.writeContents(a)
       return a
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.EDIT:
         res = self.applyBoolOptions(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def applyBoolOptions(self, params):
      # applyBoolOptions
      """
      Idea: We set change some options here in the ASG area and apply immediately after editing
      """
      
      from inheritanceCodeBase import setDisplayInfo
      for node in self.listNodes['CD_Class3'] + self.listNodes['CD_Association3']:
          setDisplayInfo(node)
      
      
      # Since messing around with what is displayed can increase the size of classes
      # this can result in overlap... lets deal with it...
#      import ForceTransfer
#      atom3i = self.parent
#      
#      selectionList = []
#      for node in self.listNodes['CD_Class3']:
#          selectionList.append(node.graphObject_)
#      ForceTransfer.applyLayout( atom3i=atom3i , selection=selectionList )
      
      

   def preAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None


