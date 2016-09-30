# __AtomClass.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3List import *
from ATOM3Connection import *
from ATOM3Attribute import *
from ATOM3MSEnum import *
from ATOM3Port import *
from ATOM3Integer import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Link import *
from ATOM3Boolean import *
from ATOM3Enum import *
from ATOM3Constraint import *
from ATOM3BottomType import *
from ATOM3Text import *
from graph_AtomClass import *
class AtomClass(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_AtomClass
      self.parent = parent
      self.ClassName=ATOM3String('MyClass')
      self.keyword_= self.ClassName
      self.ClassCardinality=ATOM3List([ 0, 1, 0, 0],ATOM3Connection)
      lcobj0=[]
      self.ClassCardinality.setValue(lcobj0)
      self.ClassAttributes=ATOM3List([ 1, 1, 1, 0],ATOM3Attribute,parent.types )
      lcobj0=[]
      self.ClassAttributes.setValue(lcobj0)
      self.ClassConstraints=ATOM3List([ 1, 1, 1, 0],ATOM3Constraint)
      lcobj0=[]
      self.ClassConstraints.setValue(lcobj0)
      self.ClassAppearance=ATOM3Appearance()
      self.ClassAppearance.setValue( (self.keyword_.toString(), self))
      self.Abstract=ATOM3Boolean()
      self.Abstract.setValue((None, 0))
      self.Abstract.config = 0
      self.generatedAttributes = {'ClassName': ('ATOM3String', ),
                                  'ClassCardinality': ('ATOM3List', 'ATOM3Connection'),
                                  'ClassAttributes': ('ATOM3List', 'ATOM3Attribute'),
                                  'ClassConstraints': ('ATOM3List', 'ATOM3Constraint'),
                                  'ClassAppearance': ('ATOM3Appearance', ),
                                  'Abstract': ('ATOM3Boolean', )      }
      self.realOrder = ['ClassName','ClassCardinality','ClassAttributes','ClassConstraints','ClassAppearance','Abstract']
      self.directEditing = [1,0,1,1,1,1]
   def clone(self):
      cloneObject = AtomClass( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      cloneObject.keyword_ = cloneObject.ClassName
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.ClassName
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if actionID == self.DELETE or actionID == self.DISCONNECT:
         res = self.deleteCardinality(params)
         if res: return res
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
      if actionID == self.EDIT:									# automatically generated post-action
         print "post condition on EDIT"
         self.ClassAppearance.updateGraphicalFile(self.keyword_.toString())         
      if actionID == self.EDIT:
         res = self.updateRelationships(params)
         if res: return res
      if actionID == self.CREATE:									# automatically generated post-action
         print "post condition on CREATE"
         self.ClassAppearance.updateGraphicalFile(self.keyword_.toString())                 
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def createCardinality(self, params):
      #constraint that generates cardinality variables for the associated classes.  
      for a in self.in_connections_:
      	if a.getTypeName() == 'AtomAssociation':         
      		self_source=ATOM3Connection(a, '1', '1')
      		self_source.setValue((a,(["Source", "Destination"], 1),'0','N'))
      		if not self_source in self.ClassCardinality.getValue():
      			self.ClassCardinality.newItem(self_source)
      
      for a in self.out_connections_:
      	if a.getTypeName() == 'AtomAssociation':         
      		self_source=ATOM3Connection(a, '1', '1')
      		self_source.setValue((a,(["Source", "Destination"], 0),'0','N'))
      		if not self_source in self.ClassCardinality.getValue():
      			self.ClassCardinality.newItem(self_source)             

   def deleteCardinality(self, params):
      myname = self.ClassName.getValue()
      in_C = self.in_connections_
      out_C = self.out_connections_
      
      for a in in_C:
      	for b in a.in_connections_:
      		b_card = b.ClassCardinality.getValue()
      		new_b_card = b_card
      		for c in b_card:
      			if c.getValue()[0] == myname:
      				new_b_card.remove(c)
      		b.ClassCardinality.setValue(new_b_card)
      
      for a in out_C:
      	for b in a.out_connections_:
      		b_card = b.ClassCardinality.getValue()
      		new_b_card = b_card
      		for c in b_card:
      			if c.getValue()[0] == myname:
      				new_b_card.remove(c)
      		b.ClassCardinality.setValue(new_b_card) 

   def storeKeyword(self, params):
      self.oldKeyword = self.keyword_.toString()            

   def updateRelationships(self, params):
      for rel in self.in_connections_:
         if rel.getTypeName() == "AtomAssociation":
               cards = rel.AssociationCardinality.getValue()
               print "in updateRelationships:::", cards
               for card in cards:
                  name, direction, min, max = card.getValue()
                  if name == self.oldKeyword and direction[1] == 0:
                     card.setValue((self, None, None, None))
                     break
      for rel in self.out_connections_:
         if rel.getTypeName() == "AtomAssociation":
               cards = rel.AssociationCardinality.getValue()
               print "in updateRelationships:::", cards
               for card in cards:
                  name, direction, min, max = card.getValue()
                  if name == self.oldKeyword and direction[1] == 1:
                     card.setValue((self, None, None, None))
                     break
            
   def attributesToDraw(self, visitedClasses = None):
      """
         Redefined from ASGNode and added by hand 25/02/2005
         return a (Python) list of all the ATOM3Attribute attributes of this object.
         - visitedClasses is a list of the visited classes or none, if the receiving class is in the
           list, an empty list is returned         
      """
      if visitedClasses:  # if we are in the list, return
         if self.ClassName.toString() in visitedClasses:
            return []
         else: visitedClasses.append(self.ClassName.toString())
      else: visitedClasses = [self.ClassName.toString()]
      listOfAttributes = []
      for attr in self.generatedAttributes.keys():
        infoTuple = self.generatedAttributes[attr]
        if infoTuple[0] == 'ATOM3Attribute':
          listOfAttributes.append(self.getAttrValue(attr))
        elif infoTuple[0] == 'ATOM3List' and self.getAttrValue(attr).itemType.__name__ == 'ATOM3Attribute':
          listOfAttributes = listOfAttributes+self.getAttrValue(attr).getValue()
      # now add the attributes of all the superclasses
      for inh in self.out_connections_: # beware: with cyclic inheritance paths it will not work!
         if inh.getClass() == "AtomInheritance":
            parent = inh.out_connections_[0]
            listOfAttributes = listOfAttributes+parent.attributesToDraw(visitedClasses)
      return listOfAttributes
      
      
      
      
