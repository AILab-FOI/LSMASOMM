"""
__CD_Association3.py_____________________________________________________

Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)
Author: Denis Dube
Modified: Sat Feb 04 17:56:37 2006
_________________________________________________________________________
"""
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Link import *
from ATOM3List import *
from ATOM3Connection import *
from ATOM3Attribute import *
from ATOM3Enum import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Float import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *
from graph_CD_Association3 import *
class CD_Association3(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_CD_Association3
      self.isGraphObjectVisual = True
      if(hasattr(self, '_setHierarchicalLink')):
        self._setHierarchicalLink(False)
      if(hasattr(self, '_setHierarchicalNode')):
        self._setHierarchicalNode(False)
      self.parent = parent
      self.name=ATOM3String('Association_')
      self.keyword_= self.name
      self.Graphical_Appearance=ATOM3Link()
      self.Graphical_Appearance.setValue( ('None', self))
      self.Graphical_Appearance.linkInfo=linkEditor(self,self.Graphical_Appearance.semObject, "Relationship3")
      self.Graphical_Appearance.linkInfo.FirstLink= stickylink()
      self.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
      self.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
      self.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
      self.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
      self.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
      self.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
      self.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
      self.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('Relationship3_1stLink', self.Graphical_Appearance.linkInfo.FirstLink))
      self.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
      self.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
      self.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
      self.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
      self.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
      self.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
      self.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
      self.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
      self.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
      self.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
      self.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
      self.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('Relationship3_1stSegment', self.Graphical_Appearance.linkInfo.FirstSegment))
      self.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
      self.Graphical_Appearance.linkInfo.Center.setValue( ('Relationship3_Center', self.Graphical_Appearance.linkInfo))
      self.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
      self.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
      self.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
      self.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
      self.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
      self.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
      self.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
      self.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
      self.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
      self.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
      self.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
      self.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('Relationship3_2ndSegment', self.Graphical_Appearance.linkInfo.SecondSegment))
      self.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.Graphical_Appearance.linkInfo.SecondLink= stickylink()
      self.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
      self.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
      self.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
      self.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
      self.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
      self.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
      self.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
      self.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('Relationship3_2ndLink', self.Graphical_Appearance.linkInfo.SecondLink))
      self.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.Graphical_Appearance.semObject
      self.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.Graphical_Appearance.semObject
      self.Graphical_Appearance.linkInfo.Center.semObject=self.Graphical_Appearance.semObject
      self.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.Graphical_Appearance.semObject
      self.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.Graphical_Appearance.semObject
      self.cardinality=ATOM3List([ 0, 1, 0, 0],ATOM3Connection)
      lcobj0=[]
      self.cardinality.setValue(lcobj0)
      self.attributes=ATOM3List([ 1, 1, 1, 0],ATOM3Attribute,parent.types )
      lcobj0=[]
      self.attributes.setValue(lcobj0)
      self.Constraints=ATOM3List([ 1, 1, 1, 0],ATOM3Constraint)
      lcobj0=[]
      self.Constraints.setValue(lcobj0)
      self.Actions=ATOM3List([ 1, 1, 1, 0],ATOM3Action)
      lcobj0=[]
      self.Actions.setValue(lcobj0)
      self.display=ATOM3Text('\n', 60,15 )
      self.displaySelect=ATOM3MSEnum(['attributes', 'constraints', 'actions', 'cardinality'], [0,0,0,0], 0, 1)
      self.QOCA=ATOM3Action()
      self.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))
      self.generatedAttributes = {'name': ('ATOM3String', ),
                                  'Graphical_Appearance': ('ATOM3Link', ),
                                  'cardinality': ('ATOM3List', 'ATOM3Connection'),
                                  'attributes': ('ATOM3List', 'ATOM3Attribute'),
                                  'Constraints': ('ATOM3List', 'ATOM3Constraint'),
                                  'Actions': ('ATOM3List', 'ATOM3Action'),
                                  'display': ('ATOM3Text', ),
                                  'displaySelect': ('ATOM3MSEnum', ),
                                  'QOCA': ('ATOM3Action', )      }
      self.realOrder = ['name','Graphical_Appearance','cardinality','attributes','Constraints','Actions','display','displaySelect','QOCA']
      self.directEditing = [1,1,1,1,1,1,0,1,0]
   def clone(self):
      cloneObject = CD_Association3( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      cloneObject.keyword_ = cloneObject.name
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.name
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.EDIT:
         res = self.checkKeywordValidity(params)
         if res: return res
      if actionID == self.EDIT:
         res = self.checkNameValidity(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def checkKeywordValidity(self, params):
      attrs = self.attributes.getValue()
      numKeys = 0
      for attr in attrs:
        name, selType, ivalue, key, dirEditing = attr.getValue()
        if key[1] == 1:
            numKeys = numKeys + 1
            if numKeys > 1:
              return ("This entity has more than one keyword", self.graphObject_)
            if selType != "String":
              return ("Keyword ("+name+") is not a string", self.graphObject_)
      return None
      

   def checkNameValidity(self, params):
      import string
      if not self.name.isNone:
        vname = self.name.getValue()
        # check if we have a name
        if (not vname) or (vname == ""):                 # the name is mandatory
          return "Relationship name must be specified"
        # now check that the name is valid (a variable name)
        if string.count(vname, " ") > 0:
          return "Invalid relationship name, no white spaces allowed"
        # check first character
        if (vname[0] >= '0') and (vname[0] <= '9'):              # a number
          return "Invalid variable name, first character must be a letter or '_'"
        if vname[0] != '_' and (vname[0]<'A' or vname[0]>'z'):
          return "Invalid relationship name, first character must be a letter or '_'"
        # now check for the rest of not allowed characters...
        for c in range(len(vname)-1):
          if vname[c+1] < 'A' or vname[c+1] > 'z':              # not a letter
              if vname[c+1] < '0' or vname[c+1] > '9':           # not a number
                if vname[c+1] != '_':                                # not underscore
                    return ("Invalid relationship name, character '"+vname[c+1]+"' is not allowed", self.graphObject_)
      return None
      

   def preAction (self, actionID, * params):
      if actionID == self.EDIT:
         self.storeKeyword(params)
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None
   def postAction (self, actionID, * params):
      if actionID == self.EDIT:
         self.updateGraphics(params)
      if actionID == self.DELETE:
         self.removeCardinalitiesFromEntities(params)
      if actionID == self.DISCONNECT:
         self.removeConnection(params)
      if actionID == self.CONNECT:
         self.addCardinality(params)
      if actionID == self.EDIT:
         self.updateRelationships(params)
      if actionID == self.EDIT or actionID == self.CONNECT:
         self.displayList(params)
      if actionID == self.EDIT or actionID == self.CONNECT:
         self.fitText(params)
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None
   def storeKeyword(self, params):
      self.oldKeyword = self.keyword_.toString()
      

   def updateGraphics(self, params):
      self.Graphical_Appearance.updateGraphicalFile(self.keyword_.toString())
      

   def removeCardinalitiesFromEntities(self, params):
      for ent in self.in_connections_:
        cards = ent.cardinality.getValue()				# obtain the list of relationshp's cardinalities
        counter = 0							# an auxiliary counter
        for card in cards:
            name, direction, min, max = card.getValue()
            if name == self.name.toString() and direction[1] == 0:		# if that's me
              ent.cardinality.deleteItem(counter)
              break
            counter = counter + 1
      for ent in self.out_connections_:
        cards = ent.cardinality.getValue()				# obtain the list of relationshp's cardinalities
        counter = 0							# an auxiliary counter
        for card in cards:
            name, direction, min, max = card.getValue()
            if name == self.name.toString() and direction[1] == 1:		# if that's me
              ent.cardinality.deleteItem(counter)
              break
            counter = counter + 1
      

   def removeConnection(self, params):
      object    = params[0]
      if object == None:						# that means its myself!!
          object = self
      if params[1] == "SOURCE": direct = "Source"
      else: direct = "Destination"
      cards = self.cardinality.getValue()				# obtain the list of cardinalities
      counter = 0
      for card in cards:
          name, direction, min, max = card.getValue()
          if name == object.name.toString() and direction[0][direction[1]] == direct:		# if that's me
            self.cardinality.deleteItem(counter)
            break
          counter = counter + 1
      if self == object:						# have to remove the other part...
          if direct == "Source": direct = "Destination"
          else: direct = "Source"
          cards = self.cardinality.getValue()				# obtain the list of cardinalities
          counter = 0
          for card in cards:
            name, direction, min, max = card.getValue()
            if name == object.name.toString() and direction[0][direction[1]] == direct:		# if that's me
                self.cardinality.deleteItem(counter)
                break
            counter = counter + 1
      
      

   def addCardinality(self, params):
      # see if we are source or destination
      direction = params[0]
      if direction == "SOURCE&DESTINATION":
          at3c = ATOM3Connection(self.out_connections_[len(self.out_connections_)-1])
          at3c.direction.setValue((None,0))                   # set value of direction
          self.cardinality.newItem( at3c )
          at3c = ATOM3Connection(self.in_connections_[len(self.in_connections_)-1])
          at3c.direction.setValue((None,1))                   # set value of direction
          self.cardinality.newItem( at3c )
      elif direction == "SOURCE":
          at3c = ATOM3Connection(self.out_connections_[len(self.out_connections_)-1])
          at3c.direction.setValue((None,0))                   # set value of direction
      else:
          at3c = ATOM3Connection(self.in_connections_[len(self.in_connections_)-1])
          at3c.direction.setValue((None,1))                   # set value of direction
      self.cardinality.newItem( at3c )
      
      

   def updateRelationships(self, params):
      for rel in self.in_connections_:
        cards = rel.cardinality.getValue()
        for card in cards:
            name, direction, min, max = card.getValue()
            if name == self.oldKeyword and direction[1] == 0:
              card.setValue((self, None, None, None))
              break
      for rel in self.out_connections_:
        cards = rel.cardinality.getValue()
        for card in cards:
            name, direction, min, max = card.getValue()
            if name == self.oldKeyword and direction[1] == 1:
              card.setValue((self, None, None, None))
              break
      

   def displayList(self, params):
      bullet = '  - '
      bulletPre = '  < '
      bulletPost = '  > ' 
      text = ''
      
      # Super parent: get options from the ASG
      myASG = self.rootNode.getASGbyName('CD_ClassDiagramsV3_META')
      if( not myASG ): 
          showAssociationBox = False
          showAttributes = False
          showConstraints = False
          showActions = False
          showCardinalities = False
      else:            
          showAssociationBox = myASG.showAssociationBox.getValue()[1]    
          showAttributes = myASG.showAttributes.getValue()[1]    
          showConstraints = myASG.showConditions.getValue()[1]  
          showActions = myASG.showActions.getValue()[1]  
          showCardinalities = myASG.showCardinalities.getValue()[1]  
      
      # Set the visibility of the association box
      if( not showAssociationBox ): showAssociationBox = None
      for gf in self.graphObject_.centerObject.graphForms:
          gf.setVisible( showAssociationBox )
      
      
      # Add stuff to the displayable text, depending on if it is hidden or not
      if( showAttributes and len( self.attributes.getValue() ) > 0 ):	
      	text += 'Attributes:\n'
      	for item in self.attributes.getValue():
      		val = item.getValue()
      		text += bullet + val[0] + ' :: ' + val[1] + '\n'
      
      if( showConstraints and len( self.Constraints.getValue() ) > 0 ):	
      	text += 'Constraints:\n'
      	for item in self.Constraints.getValue():
      		val = item.getValue()
      		if( val[2][1] == 0 ): text += bulletPre
      		else: text += bulletPost
      		text += val[0] + '\n'
      
      if( showActions and len( self.Actions.getValue() ) > 0 ):		
      	text += 'Actions:\n'
      	for item in self.Actions.getValue():
      		val = item.getValue()
      		if( val[2][1] == 0 ): text += bulletPre
      		else: text += bulletPost
      		text += val[0]  + '\n'
      
      if( showCardinalities and len( self.cardinality.getValue() ) > 0 ):	
      	text += 'Multiplicities:\n'
      	for item in self.cardinality.getValue():
      		val = item.getValue()
      		if( val[1][1] == 0 ): text += bullet + 'To '
      		else: text += bullet + 'From '
      		text += val[0] + ': ' + val[2] + ' to ' + val[3] + '\n'
      
      self.display.setValue( text )
      
      if( self.graphObject_ ): self.graphObject_.ModifyAttribute( 'display',  text )  
      
      

   def fitText(self, params):
      from inheritanceCodeBase import fitText
      fitText(self)
      



