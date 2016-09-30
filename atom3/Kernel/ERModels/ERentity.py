"""
__ERentity.py_____________________________________________________
 
ERModel generated file ---> DO NOT MODIFY DIRECTLY
__________________________________________________________________
"""
from ASGNode import *

from graph_ERentity  import *
from ATOM3String     import *
from ATOM3List       import *
from ATOM3Appearance import *
from ATOM3Attribute  import *
from ATOM3Constraint import *
from ATOM3Connection import *

#from GraphicEditor import Editor

class ERentity(ASGNode, ATOM3Type):

   def __init__(self, parent, name = 'entity'):

      ASGNode.__init__(self)
      ATOM3Type.__init__(self)

      # Generated Attributes

      self.parent = parent

      self.name=ATOM3String()				# name attribute
      self.name.setValue(name)

      self.cardinality = ATOM3List([0,1,0,None], ATOM3Connection)			# only editing allowed
      self.attributes  = ATOM3List([1,1,1,None], ATOM3Attribute, parent.types )
      self.constraints = ATOM3List([1,1,1,None], ATOM3Constraint, self.attributes.objectList)
      self.appearance  = ATOM3Appearance(self.name.getValue(), self )
      self.realOrder = ['name', 'cardinality', 'attributes', 'constraints',
                         'appearance']

      # Common Attributes

      self.graphClass_    = graph_ERentity
      self.keyword_       = self.name

      self.generatedAttributes = { 'name'       : ('ATOM3String', ),
                                   'cardinality': ('ATOM3List', 'ATOM3Connection'),
                                   'attributes' : ('ATOM3List', 'ATOM3Attribute'),
                                   'constraints': ('ATOM3List', 'ATOM3Constraint'),
                                   'appearance' : ('ATOM3Appearance', ) }

   def show(self, parent, topWindowParent):
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text="Name").grid(row=0, column=0, sticky=W)
      self.name.show       (self.containerFrame, topWindowParent).grid(row=0, column=1, sticky=W)   # pack the widget to edit the name
      ASGNode.setGGAnyWidget (self, self.containerFrame, topWindowParent, 'name', 0, 2)

      Label(self.containerFrame, text="Cardinalities").grid(row=1, column=0, sticky=W)
      Button( self.containerFrame, text = 'edit', command =  lambda x=self : ATOM3TypeDialog(x.containerFrame, x.cardinality)).grid(row=1,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, topWindowParent, 'cardinality', 1, 2)

      Label(self.containerFrame, text="Attributes").grid(row=2, column=0, sticky=W)
      self.attributes.show (self.containerFrame, topWindowParent).grid(row=2, column=1, sticky=W)   # pack the widget to add attributes
      ASGNode.setGGAnyWidget (self, self.containerFrame, topWindowParent, 'attributes', 2, 2)

      Label(self.containerFrame, text="Constraints").grid(row=3, column=0, sticky=W)
      self.constraints.show(self.containerFrame, topWindowParent).grid(row=3, column=1, sticky=W)   # constraints
      ASGNode.setGGAnyWidget (self, self.containerFrame, topWindowParent, 'constraints', 3, 2)

      Label(self.containerFrame, text="Appearance").grid(row=4, column=0, sticky=W)  	
      self.appearance.show(self.containerFrame, topWindowParent).grid(row=4, column=1, sticky=W)   # constraints
      ASGNode.setGGAnyWidget (self, self.containerFrame, topWindowParent, 'appearance', 4, 2)

      '''
      def IconEditorHandler(event=None):
        return Editor( self, self.name.getValue() )
      Button( self.containerFrame, text = 'Icon-Editor', 
              command=IconEditorHandler ).grid(row=5,column=1,sticky=W)
      '''
      #ASGNode.editGGLabel(self, self.containerFrame, topWindowParent, 5)
      ASGNode.editGGLabel(self, self.containerFrame, topWindowParent, 4)
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      rs = self.name.toString()+self.attributes.toString()+self.constraints.toString()+self.appearance.toString()
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs

   def clone(self):
      "creates an exact copy of this object"
      cloneObject            = ERentity( self.parent, self.name.getValue() )
      cloneObject.cardinality= self.cardinality.clone()
      cloneObject.attributes = self.attributes.clone()                        # clone each field
      cloneObject.constraints= self.constraints.clone()
      cloneObject.appearance = self.appearance.clone()
      cloneObject.keyword_   = cloneObject.name

      ASGNode.cloneActions(self, cloneObject)

      return cloneObject

   def copy(self, other):
      "copies each field of the other object into its own state"
      ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
      self.name       = other.name
      self.cardinality= other.cardinality
      self.attributes = other.attributes
      self.constraints= other.constraints
      self.appearance = other.appearance
      self.keyword_   = self.name
      ASGNode.copy(self, other)

   def destroy(self):
      ASGNode.GGcheckSetNone(self)
      self.name.destroy()
      self.attributes.destroy()
      self.constraints.destroy()
      self.appearance.destroy()
      self.cardinality.destroy()
      self.containerFrame = None

   def classes2relationships(self):
      for c in self.in_connections_:
         if c.getClass() != 'ERrelationship':
            return ( c.toString(), 'is not a relationship' )
      for c in self.out_connections_:
         if c.getClass() != 'ERrelationship':
            return ( c.toString(), 'is not a relationship' )
      return None

   def storeKeyword(self):
      self.oldKeyword = self.keyword_.toString()

   def updateRelationships(self):
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

   def removeFromRelationships(self):
      for rel in self.in_connections_:
         cards = rel.cardinality.getValue()				# obtain the list of relationshp's cardinalities
         counter = 0							# an auxiliary counter
         for card in cards:
            name, direction, min, max = card.getValue()
            if name == self.name.toString() and direction[1] == 1:		# if that's me
               rel.cardinality.deleteItem(counter)
               break
            counter = counter + 1
      for rel in self.out_connections_:
         cards = rel.cardinality.getValue()				# obtain the list of relationshp's cardinalities
         counter = 0							# an auxiliary counter
         for card in cards:
            name, direction, min, max = card.getValue()
            if name == self.name.toString() and direction[1] == 0:		# if that's me
               rel.cardinality.deleteItem(counter)
               break
            counter = counter + 1

   def removeConnection(self, params):
       object    = params[0]
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

   def addCardinality(self, direction):
       # see if we are source or destination
       if direction == "SOURCE":
          at3c = ATOM3Connection(self.out_connections_[len(self.out_connections_)-1])
          at3c.direction.setValue((None,0))                   # set value of direction
       else:
          at3c = ATOM3Connection(self.in_connections_[len(self.in_connections_)-1])
          at3c.direction.setValue((None,1))                   # set value of direction
       self.cardinality.newItem( at3c )

   def preAction(self, actionID, * params):
      if actionID == self.EDIT:						# automatically generated pre-action
         self.storeKeyword()
      elif actionID == self.DELETE:
         self.removeFromRelationships()
      if self.graphObject_:
         return self.graphObject_.preAction(actionID, params)
      else: return None

   def postAction(self, actionID, * params):
      if actionID == self.CONNECT:
         self.addCardinality(params[0])
      if actionID == self.DISCONNECT:
         self.removeConnection(params)
      if actionID == self.EDIT:
         self.updateRelationships()
      if actionID == self.EDIT:									# automatically generated post-action
         self.appearance.updateGraphicalFile(self.keyword_.toString())
      if self.graphObject_:
         return self.graphObject_.postAction(actionID, params)
      else: return None

   def preCondition(self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None

   def invalid(self):
      "Decides if the attribute is valid, that is, if the initial value (if any) is valid"
      ASGNode.GGcheckSetNone(self)
      return None

   def checkNameValidity(self):   
      import string
      if not self.name.isNone():
         vname = self.name.getValue()
         # check if we have a name
         if (not vname) or (vname == ""):                 # the name is mandatory
            return "Entity name must be specified"
         # now check that the name is valid (a variable name)
         if string.count(vname, " ") > 0:
            return "Invalid entity name, no white spaces allowed"
         # check first character
         if (vname[0] >= '0') and (vname[0] <= '9'):              # a number
            return "Invalid variable name, first character must be a letter or '_'"
         if vname[0] != '_' and (vname[0]<'A' or vname[0]>'z'):
            return "Invalid entity name, first character must be a letter or '_'"
         # now check for the rest of not allowed characters...
         for c in range(len(vname)-1):
            if vname[c+1] < 'A' or vname[c+1] > 'z':              # not a letter
               if vname[c+1] < '0' or vname[c+1] > '9':           # not a number
                  if vname[c+1] != '_':                                # not underscore
                     return ("Invalid entity name, character '"+vname[c+1]+"' is not allowed", self.graphObject_)
      return None

   def postCondition(self, actionID, * params):
      if actionID == self.CONNECT:
         res = self.classes2relationships()
         if res: return res
      if actionID == self.EDIT:
         res = self.checkKeywordValidity()
         if res: return res
      if actionID == self.EDIT:
         res = self.checkNameValidity()
         if res: return res      
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


   def checkKeywordValidity(self):
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
