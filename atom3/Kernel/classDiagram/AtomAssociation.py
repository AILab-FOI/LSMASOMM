# __AtomAssociation.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3List import *
from ATOM3Connection import *
from ATOM3Constraint import *
from ATOM3Link import *
from ATOM3Attribute import *
from ATOM3MSEnum import *
from ATOM3Port import *
from ATOM3Integer import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Boolean import *
from ATOM3Enum import *
from ATOM3BottomType import *
from ATOM3Text import *
from graph_AtomAssociation import *
class AtomAssociation(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_AtomAssociation
      self.parent = parent
      self.AssociationName=ATOM3String('MyAssociation')
      self.keyword_= self.AssociationName
      self.AssociationCardinality=ATOM3List([ 0, 1, 0, 0],ATOM3Connection)
      lcobj0=[]
      self.AssociationCardinality.setValue(lcobj0)
      self.AssociationConstraints=ATOM3List([ 1, 1, 1, 0],ATOM3Constraint)
      lcobj0=[]
      self.AssociationConstraints.setValue(lcobj0)
      self.AssociationAppearance=ATOM3Link()
      self.AssociationAppearance.setValue( ('None', self))
      #self.AssociationAppearance.linkInfo=linkEditor(self,self.AssociationAppearance.semObject, "Class_information_not_available")
      self.AssociationAppearance.linkInfo=linkEditor(self,self.AssociationAppearance.semObject, self.keyword_.toString())
      self.AssociationAppearance.linkInfo.FirstLink= stickylink()
      self.AssociationAppearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
      self.AssociationAppearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
      self.AssociationAppearance.linkInfo.FirstLink.arrow.config = 0
      self.AssociationAppearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
      self.AssociationAppearance.linkInfo.FirstLink.decoration.setValue( (self.keyword_.toString()+'_1stLink', self.AssociationAppearance.linkInfo.FirstLink))
      self.AssociationAppearance.linkInfo.FirstSegment= widthXfillXdecoration()
      self.AssociationAppearance.linkInfo.FirstSegment.width=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.FirstSegment.fill=ATOM3String('black')
      self.AssociationAppearance.linkInfo.FirstSegment.stipple=ATOM3String('')
      self.AssociationAppearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
      self.AssociationAppearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
      self.AssociationAppearance.linkInfo.FirstSegment.arrow.config = 0
      self.AssociationAppearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
      self.AssociationAppearance.linkInfo.FirstSegment.decoration.setValue( (self.keyword_.toString()+'_1stSegment', self.AssociationAppearance.linkInfo.FirstSegment))
      self.AssociationAppearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.AssociationAppearance.linkInfo.Center=ATOM3Appearance()
      self.AssociationAppearance.linkInfo.Center.setValue( (self.AssociationName.toString()+'_Center', self.AssociationAppearance.linkInfo))
      self.AssociationAppearance.linkInfo.SecondSegment= widthXfillXdecoration()
      self.AssociationAppearance.linkInfo.SecondSegment.width=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.SecondSegment.fill=ATOM3String('black')
      self.AssociationAppearance.linkInfo.SecondSegment.stipple=ATOM3String('')
      self.AssociationAppearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
      self.AssociationAppearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
      self.AssociationAppearance.linkInfo.SecondSegment.arrow.config = 0
      self.AssociationAppearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
      self.AssociationAppearance.linkInfo.SecondSegment.decoration.setValue( (self.keyword_.toString()+'_2ndSegment', self.AssociationAppearance.linkInfo.SecondSegment))
      self.AssociationAppearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.AssociationAppearance.linkInfo.SecondLink= stickylink()
      self.AssociationAppearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
      self.AssociationAppearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
      self.AssociationAppearance.linkInfo.SecondLink.arrow.config = 0
      self.AssociationAppearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
      self.AssociationAppearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
      self.AssociationAppearance.linkInfo.SecondLink.decoration.setValue( (self.keyword_.toString()+'_2ndLink', self.AssociationAppearance.linkInfo.SecondLink))
      self.AssociationAppearance.linkInfo.FirstLink.decoration.semObject=self.AssociationAppearance.semObject
      self.AssociationAppearance.linkInfo.FirstSegment.decoration.semObject=self.AssociationAppearance.semObject
      self.AssociationAppearance.linkInfo.Center.semObject=self.AssociationAppearance.semObject
      self.AssociationAppearance.linkInfo.SecondSegment.decoration.semObject=self.AssociationAppearance.semObject
      self.AssociationAppearance.linkInfo.SecondLink.decoration.semObject=self.AssociationAppearance.semObject
      self.AssociationAttributes=ATOM3List([ 1, 1, 1, 0],ATOM3Attribute,parent.types )
      lcobj0=[]
      self.AssociationAttributes.setValue(lcobj0)
      self.generatedAttributes = {'AssociationName': ('ATOM3String', ),
                                  'AssociationCardinality': ('ATOM3List', 'ATOM3Connection'),
                                  'AssociationConstraints': ('ATOM3List', 'ATOM3Constraint'),
                                  'AssociationAppearance': ('ATOM3Link', ),
                                  'AssociationAttributes': ('ATOM3List', 'ATOM3Attribute')      }
      self.realOrder = ['AssociationName','AssociationCardinality','AssociationConstraints','AssociationAppearance','AssociationAttributes']
      self.directEditing = [1,0,1,1,1]
   def clone(self):
      cloneObject = AtomAssociation( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      cloneObject.keyword_ = cloneObject.AssociationName
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.AssociationName
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if actionID == self.EDIT:
         res = self.storeKeyword(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.CONNECT:
         res = self.createCardinality(params)
         if res: return res
      if actionID == self.EDIT:
         res = self.updateRelationships(params)
         if res: return res
      if actionID == self.EDIT:									# automatically generated post-action
         # Added 19 January 2004
         self.AssociationAppearance.updateGraphicalFile(self.keyword_.toString())
      if actionID == self.CREATE:									# automatically generated post-action
         # Added 19 January 2004
         self.AssociationAppearance.updateGraphicalFile(self.keyword_.toString())                
         
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def createCardinality(self, params):
      in_C = self.in_connections_
      out_C = self.out_connections_
      
      for a in in_C:
      	if a.getTypeName() == 'AtomClass':
      		#self.AssociationCardinality.newItem(ATOM3Connection(a, 1, 1))
      		source=ATOM3Connection(a, 1, 1)
      		source.setValue((a,(["Source", "Destination"], 1),'1','1'))
      		if not source in self.AssociationCardinality.getValue():
      			self.AssociationCardinality.newItem(source)
      
      for a in out_C:
      	if a.getTypeName() == 'AtomClass':
      		#self.AssociationCardinality.newItem(ATOM3Connection(a, 1, 1))
      		source=ATOM3Connection(a, 1, 1)
      		source.setValue((a,(["Source", "Destination"], 0),'1','1'))
      		if not source in self.AssociationCardinality.getValue():
      			self.AssociationCardinality.newItem(source)
      
      
      
      
      
      
      
      
      
      
      
      
      

   def storeKeyword(self, params):
      self.oldKeyword = self.keyword_.toString()
      
      

   def updateRelationships(self, params):
      for rel in self.in_connections_:
          if rel.getTypeName() == "AtomClass":
               cards = rel.ClassCardinality.getValue()
               for card in cards:
                  name, direction, min, max = card.getValue()
                  if name == self.oldKeyword and direction[1] == 0:
                     card.setValue((self, None, None, None))
                     break
      for rel in self.out_connections_:
         if rel.getTypeName() == "AtomClass":
               cards = rel.ClassCardinality.getValue()
               for card in cards:
                  name, direction, min, max = card.getValue()
                  if name == self.oldKeyword and direction[1] == 1:
                     card.setValue((self, None, None, None))
                     break
      
      
      



