"""
__CD_classDiagramsV3_ER_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Denis Dube
Modified: Thu Jun 08 09:17:19 2006
___________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Entity3 import *
from Relationship3 import *
from graph_Entity3 import *
from graph_Relationship3 import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def CD_classDiagramsV3_ER_MDL(self, rootNode, EntityRelationshipV3RootNode=None):

    # --- Generating attributes code for ASG EntityRelationshipV3 ---
    if( EntityRelationshipV3RootNode ): 
        # attributes
        EntityRelationshipV3RootNode.attributes.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('', 20)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('Annonymous', 20)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Text('\n', 60,15 )
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('attributes', 'List', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
        lcobj2=[]
        cobj2=ATOM3Attribute(self.types)
        cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
        cobj2.initialValue=ATOM3String('', 20)
        cobj2.isDerivedAttribute = False
        lcobj2.append(cobj2)
        cobj2=ATOM3Attribute(self.types)
        cobj2.setValue(('author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
        cobj2.initialValue=ATOM3String('Annonymous', 20)
        cobj2.isDerivedAttribute = False
        lcobj2.append(cobj2)
        cobj2=ATOM3Attribute(self.types)
        cobj2.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
        cobj2.initialValue=ATOM3Text('\n', 60,15 )
        cobj2.isDerivedAttribute = False
        lcobj2.append(cobj2)
        cobj1.initialValue.setValue(lcobj2)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('constraints', 'List', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Constraint)
        lcobj2=[]
        cobj1.initialValue.setValue(lcobj2)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('showAssociationBox', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Boolean()
        cobj1.initialValue.setValue((None, 1))
        cobj1.initialValue.config = 1
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('showAttributes', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Boolean()
        cobj1.initialValue.setValue((None, 1))
        cobj1.initialValue.config = 1
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('showConditions', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Boolean()
        cobj1.initialValue.setValue((None, 1))
        cobj1.initialValue.config = 1
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('showActions', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Boolean()
        cobj1.initialValue.setValue((None, 1))
        cobj1.initialValue.config = 1
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('showCardinalities', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Boolean()
        cobj1.initialValue.setValue((None, 1))
        cobj1.initialValue.config = 1
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        EntityRelationshipV3RootNode.attributes.setValue(lcobj1)

        # author
        EntityRelationshipV3RootNode.author.setValue('Denis')

        # description
        EntityRelationshipV3RootNode.description.setValue('From the creator of EntityRelationship version 3...\n\nComes ClassDiagrams version 3! Bigger, better! You\'ll never go back to the old one! \n')
        EntityRelationshipV3RootNode.description.setHeight(15)

        # name
        EntityRelationshipV3RootNode.name.setValue('CD_ClassDiagramsV3')

        # constraints
        EntityRelationshipV3RootNode.constraints.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        cobj1=ATOM3Constraint()
        cobj1.setValue(('applyBoolOptions', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# applyBoolOptions\n"""\nIdea: We set change some options here in the ASG area and apply immediately after editing\n"""\n\nfrom inheritanceCodeBase import setDisplayInfo\nfor node in self.listNodes[\'CD_Class3\'] + self.listNodes[\'CD_Association3\']:\n    setDisplayInfo(node)\n\n\n# Since messing around with what is displayed can increase the size of classes\n# this can result in overlap... lets deal with it...\n#import ForceTransfer\n#atom3i = self.parent\n\n#selectionList = []\n#for node in self.listNodes[\'CD_Class3\']:\n#    selectionList.append(node.graphObject_)\n#ForceTransfer.applyLayout( atom3i=atom3i , selection=selectionList )\n\n'))
        lcobj1.append(cobj1)
        EntityRelationshipV3RootNode.constraints.setValue(lcobj1)
    # --- ASG attributes over ---


    self.obj23=Entity3(self)
    self.obj23.isGraphObjectVisual = True

    if(hasattr(self.obj23, '_setHierarchicalLink')):
      self.obj23._setHierarchicalLink(False)

    # name
    self.obj23.name.setValue('CD_Class3')

    # displaySelect
    self.obj23.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj23.displaySelect.config = 0

    # Actions
    self.obj23.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('storeKeyword', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.oldKeyword = self.keyword_.toString()\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('addCardinality', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '# see if we are source or destination\ndirection = params[0]\nrelationshipName = \'CD_Association3\'\n\nif direction == "SOURCE&DESTINATION":\n    newestConn = self.out_connections_[-1]\n    if( newestConn.__class__.__name__ != relationshipName ): return\n    at3c = ATOM3Connection( newestConn ) \n    at3c.direction.setValue((None,0))                   # set value of direction\n    self.cardinality.newItem( at3c )\n    \n    newestConn = self.in_connections_[-1]\n    if( newestConn.__class__.__name__ != relationshipName ): return\n    at3c = ATOM3Connection( newestConn )\n    at3c.direction.setValue((None,1))                   # set value of direction\n    self.cardinality.newItem( at3c )\nelif direction == "SOURCE":\n    newestConn = self.out_connections_[-1]\n    if( newestConn.__class__.__name__ != relationshipName ): return\n    at3c = ATOM3Connection( newestConn )\n    at3c.direction.setValue((None,0))                   # set value of direction\nelse:\n    newestConn = self.in_connections_[-1]\n    if( newestConn.__class__.__name__ != relationshipName ): return\n    at3c = ATOM3Connection( newestConn )\n    at3c.direction.setValue((None,1))                   # set value of direction\nself.cardinality.newItem( at3c )\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('updateGraphics', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.Graphical_Appearance.updateGraphicalFile(self.keyword_.toString())\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('removeFromRelationships', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 'for rel in self.in_connections_:\n  cards = rel.cardinality.getValue()				# obtain the list of relationshp\'s cardinalities\n  counter = 0							# an auxiliary counter\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.name.toString() and direction[1] == 1:		# if that\'s me\n        rel.cardinality.deleteItem(counter)\n        break\n      counter = counter + 1\nfor rel in self.out_connections_:\n  cards = rel.cardinality.getValue()				# obtain the list of relationshp\'s cardinalities\n  counter = 0							# an auxiliary counter\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.name.toString() and direction[1] == 0:		# if that\'s me\n        rel.cardinality.deleteItem(counter)\n        break\n      counter = counter + 1\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('removeConnection', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]), 'object    = params[0]\nif params[1] == "SOURCE": direct = "Source"\nelse: direct = "Destination"\n\ncards = self.cardinality.getValue()				# obtain the list of cardinalities\ncounter = 0\nfor card in cards:\n    name, direction, min, max = card.getValue()\n    if name == object.name.toString() and direction[0][direction[1]] == direct:		# if that\'s me\n      self.cardinality.deleteItem(counter)\n      break\n    counter = counter + 1\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('updateRelationships', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'for rel in self.in_connections_:\n  if( not rel.__dict__.has_key( \'cardinality\' ) ): continue\n  cards = rel.cardinality.getValue()\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.oldKeyword and direction[1] == 0:\n        card.setValue((self, None, None, None))\n        break\nfor rel in self.out_connections_:\n  if( not rel.__dict__.has_key( \'cardinality\' ) ): continue\n  cards = rel.cardinality.getValue()\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.oldKeyword and direction[1] == 1:\n        card.setValue((self, None, None, None))\n        break\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('deriveAttributes', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from inheritanceCodeBase import inheritanceCodeBase\ninheritanceCodeBase(self)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('displayList', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0]), 'from inheritanceCodeBase import setDisplayInfo\nsetDisplayInfo(self)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('fixConnections', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '# After re-sizing, arrows may not line up unless we do this\nfrom Utilities import optimizeConnectionPorts\noptimizeConnectionPorts( self.parent )\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('rotateMoveInheritHead', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]), '# rotateMoveInheritHead\nconns = self.in_connections_ + self.out_connections_\nfor conn in conns:\n    if( conn.__class__.__name__ != \'CD_Inheritance3\' ): continue\n    conn.graphObject_.rotateMoveArrowEnd()\n\n'))
    lcobj2.append(cobj2)
    self.obj23.Actions.setValue(lcobj2)

    # Graphical_Appearance
    self.obj23.Graphical_Appearance.setValue( ('CD_Class3', self.obj23))

    # attributes
    self.obj23.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Class_', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Graphical_Appearance', 'Appearance', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Appearance()
    cobj2.initialValue.setValue( ('class0', None))
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 0, 1, 0, self.types],ATOM3Connection)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attributes', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Constraints', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Constraint)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Actions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Action)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('display', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Abstract', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('QOCA', 'Action', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Action()
    cobj2.initialValue.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj23.attributes.setValue(lcobj2)

    # cardinality
    self.obj23.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('CD_Association3', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('CD_Association3', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('CD_Inheritance3', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('CD_Inheritance3', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj23.cardinality.setValue(lcobj2)

    # display
    self.obj23.display.setValue('Attributes:\n  - name :: String\n  - Graphical_Appearance :: Appearance\n  - cardinality :: List\n  - attributes :: List\n  - Constraints :: List\n  - Actions :: List\n  - display :: Text\n  - Abstract :: Boolean\n  - QOCA :: Action\nConstraints:\n  > checkKeywordValidity\n  > checkNameValidity\nActions:\n  < storeKeyword\n  > addCardinality\n  > updateGraphics\n  < removeFromRelationships\n  > removeConnection\n  > updateRelationships\n  > deriveAttributes\n  > displayList\n  > fixConnections\n  > rotateMoveInheritHead\nCardinalities:\n  - To CD_Association3: 0 to N\n  - From CD_Association3: 0 to N\n  - To CD_Inheritance3: 0 to N\n  - From CD_Inheritance3: 0 to N\n')
    self.obj23.display.setHeight(15)

    # Constraints
    self.obj23.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('checkKeywordValidity', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'attrs = self.attributes.getValue()\nnumKeys = 0\nfor attr in attrs:\n  name, selType, ivalue, key, dirEditing = attr.getValue()\n  if key[1] == 1:\n      numKeys = numKeys + 1\n      if numKeys > 1:\n        return ("This entity has more than one keyword", self.graphObject_)\n      if selType != "String":\n        return ("Keyword ("+name+") is not a string", self.graphObject_)\nreturn None\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('checkNameValidity', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import string\nif not self.name.isNone():\n  vname = self.name.getValue()\n  # check if we have a name\n  if (not vname) or (vname == ""):                 # the name is mandatory\n      return "Entity name must be specified"\n  # now check that the name is valid (a variable name)\n  if string.count(vname, " ") > 0:\n      return "Invalid entity name, no white spaces allowed"\n  # check first character\n  if (vname[0] >= \'0\') and (vname[0] <= \'9\'):              # a number\n      return "Invalid variable name, first character must be a letter or \'_\'"\n  if vname[0] != \'_\' and (vname[0]<\'A\' or vname[0]>\'z\'):\n      return "Invalid entity name, first character must be a letter or \'_\'"\n  # now check for the rest of not allowed characters...\n  for c in range(len(vname)-1):\n      if vname[c+1] < \'A\' or vname[c+1] > \'z\':              # not a letter\n        if vname[c+1] < \'0\' or vname[c+1] > \'9\':           # not a number\n            if vname[c+1] != \'_\':                                # not underscore\n              return ("Invalid entity name, character \'"+vname[c+1]+"\' is not allowed", self.graphObject_)\nreturn None\n\n'))
    lcobj2.append(cobj2)
    self.obj23.Constraints.setValue(lcobj2)

    self.obj23.graphClass_= graph_Entity3
    if self.genGraphics:
       new_obj = graph_Entity3(420.0,188.0,self.obj23)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Entity3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.8101226993865032, 6.1584269662921347]
       new_obj.layConstraints['Label Offset'] = [2.0, -10.0]
    else: new_obj = None
    self.obj23.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj23)
    self.globalAndLocalPostcondition(self.obj23, rootNode)
    self.obj23.postAction( rootNode.CREATE )

    self.obj24=Relationship3(self)
    self.obj24.isGraphObjectVisual = True

    if(hasattr(self.obj24, '_setHierarchicalLink')):
      self.obj24._setHierarchicalLink(False)

    # name
    self.obj24.name.setValue('CD_Association3')

    # displaySelect
    self.obj24.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj24.displaySelect.config = 0

    # Actions
    self.obj24.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('storeKeyword', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.oldKeyword = self.keyword_.toString()\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('updateGraphics', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.Graphical_Appearance.updateGraphicalFile(self.keyword_.toString())\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('removeCardinalitiesFromEntities', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]), 'for ent in self.in_connections_:\n  cards = ent.cardinality.getValue()				# obtain the list of relationshp\'s cardinalities\n  counter = 0							# an auxiliary counter\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.name.toString() and direction[1] == 0:		# if that\'s me\n        ent.cardinality.deleteItem(counter)\n        break\n      counter = counter + 1\nfor ent in self.out_connections_:\n  cards = ent.cardinality.getValue()				# obtain the list of relationshp\'s cardinalities\n  counter = 0							# an auxiliary counter\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.name.toString() and direction[1] == 1:		# if that\'s me\n        ent.cardinality.deleteItem(counter)\n        break\n      counter = counter + 1\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('removeConnection', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0]), 'object    = params[0]\nif object == None:						# that means its myself!!\n    object = self\nif params[1] == "SOURCE": direct = "Source"\nelse: direct = "Destination"\ncards = self.cardinality.getValue()				# obtain the list of cardinalities\ncounter = 0\nfor card in cards:\n    name, direction, min, max = card.getValue()\n    if name == object.name.toString() and direction[0][direction[1]] == direct:		# if that\'s me\n      self.cardinality.deleteItem(counter)\n      break\n    counter = counter + 1\nif self == object:						# have to remove the other part...\n    if direct == "Source": direct = "Destination"\n    else: direct = "Source"\n    cards = self.cardinality.getValue()				# obtain the list of cardinalities\n    counter = 0\n    for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == object.name.toString() and direction[0][direction[1]] == direct:		# if that\'s me\n          self.cardinality.deleteItem(counter)\n          break\n      counter = counter + 1\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('addCardinality', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '# see if we are source or destination\ndirection = params[0]\nif direction == "SOURCE&DESTINATION":\n    at3c = ATOM3Connection(self.out_connections_[len(self.out_connections_)-1])\n    at3c.direction.setValue((None,0))                   # set value of direction\n    self.cardinality.newItem( at3c )\n    at3c = ATOM3Connection(self.in_connections_[len(self.in_connections_)-1])\n    at3c.direction.setValue((None,1))                   # set value of direction\n    self.cardinality.newItem( at3c )\nelif direction == "SOURCE":\n    at3c = ATOM3Connection(self.out_connections_[len(self.out_connections_)-1])\n    at3c.direction.setValue((None,0))                   # set value of direction\nelse:\n    at3c = ATOM3Connection(self.in_connections_[len(self.in_connections_)-1])\n    at3c.direction.setValue((None,1))                   # set value of direction\nself.cardinality.newItem( at3c )\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('updateRelationships', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'for rel in self.in_connections_:\n  cards = rel.cardinality.getValue()\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.oldKeyword and direction[1] == 0:\n        card.setValue((self, None, None, None))\n        break\nfor rel in self.out_connections_:\n  cards = rel.cardinality.getValue()\n  for card in cards:\n      name, direction, min, max = card.getValue()\n      if name == self.oldKeyword and direction[1] == 1:\n        card.setValue((self, None, None, None))\n        break\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('displayList', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'bullet = \'  - \'\nbulletPre = \'  < \'\nbulletPost = \'  > \' \ntext = \'\'\n\n# Super parent: get options from the ASG\nmyASG = self.rootNode.getASGbyName(\'CD_ClassDiagramsV3_META\')\nif( not myASG ): \n    showAssociationBox = False\n    showAttributes = False\n    showConstraints = False\n    showActions = False\n    showCardinalities = False\nelse:            \n    showAssociationBox = myASG.showAssociationBox.getValue()[1]    \n    showAttributes = myASG.showAttributes.getValue()[1]    \n    showConstraints = myASG.showConditions.getValue()[1]  \n    showActions = myASG.showActions.getValue()[1]  \n    showCardinalities = myASG.showCardinalities.getValue()[1]  \n\n# Set the visibility of the association box\nif( not showAssociationBox ): showAssociationBox = None\nfor gf in self.graphObject_.centerObject.graphForms:\n    gf.setVisible( showAssociationBox )\n\n\n# Add stuff to the displayable text, depending on if it is hidden or not\nif( showAttributes and len( self.attributes.getValue() ) > 0 ):	\n	text += \'Attributes:\\n\'\n	for item in self.attributes.getValue():\n		val = item.getValue()\n		text += bullet + val[0] + \' :: \' + val[1] + \'\\n\'\n\nif( showConstraints and len( self.Constraints.getValue() ) > 0 ):	\n	text += \'Constraints:\\n\'\n	for item in self.Constraints.getValue():\n		val = item.getValue()\n		if( val[2][1] == 0 ): text += bulletPre\n		else: text += bulletPost\n		text += val[0] + \'\\n\'\n\nif( showActions and len( self.Actions.getValue() ) > 0 ):		\n	text += \'Actions:\\n\'\n	for item in self.Actions.getValue():\n		val = item.getValue()\n		if( val[2][1] == 0 ): text += bulletPre\n		else: text += bulletPost\n		text += val[0]  + \'\\n\'\n\nif( showCardinalities and len( self.cardinality.getValue() ) > 0 ):	\n	text += \'Multiplicities:\\n\'\n	for item in self.cardinality.getValue():\n		val = item.getValue()\n		if( val[1][1] == 0 ): text += bullet + \'To \'\n		else: text += bullet + \'From \'\n		text += val[0] + \': \' + val[2] + \' to \' + val[3] + \'\\n\'\n\nself.display.setValue( text )\n\nif( self.graphObject_ ): self.graphObject_.ModifyAttribute( \'display\',  text )  \n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('fitText', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from inheritanceCodeBase import fitText\nfitText(self)\n'))
    lcobj2.append(cobj2)
    self.obj24.Actions.setValue(lcobj2)

    # Graphical_Appearance
    self.obj24.Graphical_Appearance.setValue( ('CD_Association3', self.obj24))
    self.obj24.Graphical_Appearance.linkInfo=linkEditor(self,self.obj24.Graphical_Appearance.semObject, "CD_Association3")
    self.obj24.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('CD_Association3_1stLink', self.obj24.Graphical_Appearance.linkInfo.FirstLink))
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('CD_Association3_1stSegment', self.obj24.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj24.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj24.Graphical_Appearance.linkInfo.Center.setValue( ('CD_Association3_Center', self.obj24.Graphical_Appearance.linkInfo))
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('CD_Association3_2ndSegment', self.obj24.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj24.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(11)
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(18)
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(6)
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('CD_Association3_2ndLink', self.obj24.Graphical_Appearance.linkInfo.SecondLink))
    self.obj24.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj24.Graphical_Appearance.semObject
    self.obj24.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj24.Graphical_Appearance.semObject
    self.obj24.Graphical_Appearance.linkInfo.Center.semObject=self.obj24.Graphical_Appearance.semObject
    self.obj24.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj24.Graphical_Appearance.semObject
    self.obj24.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj24.Graphical_Appearance.semObject

    # attributes
    self.obj24.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Association_', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Graphical_Appearance', 'Link', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Link()
    cobj2.initialValue.setValue( ('None', None))
    cobj2.initialValue.linkInfo=linkEditor(self,cobj2.initialValue.semObject, "Relationship3")
    cobj2.initialValue.linkInfo.FirstLink= stickylink()
    cobj2.initialValue.linkInfo.FirstLink.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.FirstLink.arrow.setValue((' ', 0))
    cobj2.initialValue.linkInfo.FirstLink.arrow.config = 0
    cobj2.initialValue.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    cobj2.initialValue.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    cobj2.initialValue.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    cobj2.initialValue.linkInfo.FirstLink.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.FirstLink.decoration.setValue( ('Relationship3_1stLink', cobj2.initialValue.linkInfo.FirstLink))
    cobj2.initialValue.linkInfo.FirstSegment= widthXfillXdecoration()
    cobj2.initialValue.linkInfo.FirstSegment.width=ATOM3Integer(2)
    cobj2.initialValue.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    cobj2.initialValue.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    cobj2.initialValue.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    cobj2.initialValue.linkInfo.FirstSegment.arrow.config = 0
    cobj2.initialValue.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    cobj2.initialValue.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    cobj2.initialValue.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    cobj2.initialValue.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.FirstSegment.decoration.setValue( ('Relationship3_1stSegment', cobj2.initialValue.linkInfo.FirstSegment))
    cobj2.initialValue.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    cobj2.initialValue.linkInfo.Center=ATOM3Appearance()
    cobj2.initialValue.linkInfo.Center.setValue( ('Relationship3_Center', cobj2.initialValue.linkInfo))
    cobj2.initialValue.linkInfo.SecondSegment= widthXfillXdecoration()
    cobj2.initialValue.linkInfo.SecondSegment.width=ATOM3Integer(2)
    cobj2.initialValue.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    cobj2.initialValue.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    cobj2.initialValue.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    cobj2.initialValue.linkInfo.SecondSegment.arrow.config = 0
    cobj2.initialValue.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    cobj2.initialValue.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    cobj2.initialValue.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    cobj2.initialValue.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.SecondSegment.decoration.setValue( ('Relationship3_2ndSegment', cobj2.initialValue.linkInfo.SecondSegment))
    cobj2.initialValue.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    cobj2.initialValue.linkInfo.SecondLink= stickylink()
    cobj2.initialValue.linkInfo.SecondLink.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.SecondLink.arrow.setValue((' ', 1))
    cobj2.initialValue.linkInfo.SecondLink.arrow.config = 0
    cobj2.initialValue.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    cobj2.initialValue.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    cobj2.initialValue.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    cobj2.initialValue.linkInfo.SecondLink.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.SecondLink.decoration.setValue( ('Relationship3_2ndLink', cobj2.initialValue.linkInfo.SecondLink))
    cobj2.initialValue.linkInfo.FirstLink.decoration.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.FirstSegment.decoration.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.Center.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.SecondSegment.decoration.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.SecondLink.decoration.semObject=cobj2.initialValue.semObject
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('cardinality', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 0, 1, 0, self.types],ATOM3Connection)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attributes', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Constraints', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Constraint)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Actions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Action)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('display', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Text('\n', 60,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('displaySelect', 'MSEnum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3MSEnum(['attributes', 'constraints', 'actions', 'cardinality'],[0,0,0,0],1,1)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('QOCA', 'Action', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3Action()
    cobj2.initialValue.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj24.attributes.setValue(lcobj2)

    # cardinality
    self.obj24.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('CD_Class3', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('CD_Class3', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj24.cardinality.setValue(lcobj2)

    # display
    self.obj24.display.setValue('Attributes:\n  - name :: String\n  - Graphical_Appearance :: Link\n  - cardinality :: List\n  - attributes :: List\n  - Constraints :: List\n  - Actions :: List\n  - display :: Text\n  - displaySelect :: MSEnum\n  - QOCA :: Action\nConstraints:\n  > checkKeywordValidity\n  > checkNameValidity\nActions:\n  < storeKeyword\n  > updateGraphics\n  > removeCardinalitiesFromEntities\n  > removeConnection\n  > addCardinality\n  > updateRelationships\n  > displayList\n  > fitText\\Multiplicities:\n  - From CD_Class3: 1 to N\n  - To CD_Class3: 1 to N\n')
    self.obj24.display.setHeight(15)

    # Constraints
    self.obj24.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('checkKeywordValidity', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'attrs = self.attributes.getValue()\nnumKeys = 0\nfor attr in attrs:\n  name, selType, ivalue, key, dirEditing = attr.getValue()\n  if key[1] == 1:\n      numKeys = numKeys + 1\n      if numKeys > 1:\n        return ("This entity has more than one keyword", self.graphObject_)\n      if selType != "String":\n        return ("Keyword ("+name+") is not a string", self.graphObject_)\nreturn None\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('checkNameValidity', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import string\nif not self.name.isNone:\n  vname = self.name.getValue()\n  # check if we have a name\n  if (not vname) or (vname == ""):                 # the name is mandatory\n    return "Relationship name must be specified"\n  # now check that the name is valid (a variable name)\n  if string.count(vname, " ") > 0:\n    return "Invalid relationship name, no white spaces allowed"\n  # check first character\n  if (vname[0] >= \'0\') and (vname[0] <= \'9\'):              # a number\n    return "Invalid variable name, first character must be a letter or \'_\'"\n  if vname[0] != \'_\' and (vname[0]<\'A\' or vname[0]>\'z\'):\n    return "Invalid relationship name, first character must be a letter or \'_\'"\n  # now check for the rest of not allowed characters...\n  for c in range(len(vname)-1):\n    if vname[c+1] < \'A\' or vname[c+1] > \'z\':              # not a letter\n        if vname[c+1] < \'0\' or vname[c+1] > \'9\':           # not a number\n          if vname[c+1] != \'_\':                                # not underscore\n              return ("Invalid relationship name, character \'"+vname[c+1]+"\' is not allowed", self.graphObject_)\nreturn None\n'))
    lcobj2.append(cobj2)
    self.obj24.Constraints.setValue(lcobj2)

    self.obj24.graphClass_= graph_Relationship3
    if self.genGraphics:
       new_obj = graph_Relationship3(245.0,302.0,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Relationship3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.75, 5.080645161290323]
    else: new_obj = None
    self.obj24.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)
    self.obj24.postAction( rootNode.CREATE )

    self.obj25=Relationship3(self)
    self.obj25.isGraphObjectVisual = True

    if(hasattr(self.obj25, '_setHierarchicalLink')):
      self.obj25._setHierarchicalLink(False)

    # name
    self.obj25.name.setValue('CD_Inheritance3')

    # displaySelect
    self.obj25.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj25.displaySelect.config = 0

    # Actions
    self.obj25.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('rotateMoveArrowEnd', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1]), '# rotateMoveArrowEnd\nself.graphObject_.rotateMoveArrowEnd()\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('connectDisconnect', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]), 'from inheritanceCodeBase import inheritanceCodeBase\ninheritanceCodeBase(self)\n\n\n'))
    lcobj2.append(cobj2)
    self.obj25.Actions.setValue(lcobj2)

    # Graphical_Appearance
    self.obj25.Graphical_Appearance.setValue( ('CD_Inheritance3', self.obj25))
    self.obj25.Graphical_Appearance.linkInfo=linkEditor(self,self.obj25.Graphical_Appearance.semObject, "CD_Inheritance3")
    self.obj25.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('CD_Inheritance3_1stLink', self.obj25.Graphical_Appearance.linkInfo.FirstLink))
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('CD_Inheritance3_1stSegment', self.obj25.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj25.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj25.Graphical_Appearance.linkInfo.Center.setValue( ('CD_Inheritance3_Center', self.obj25.Graphical_Appearance.linkInfo))
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('CD_Inheritance3_2ndSegment', self.obj25.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj25.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('CD_Inheritance3_2ndLink', self.obj25.Graphical_Appearance.linkInfo.SecondLink))
    self.obj25.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj25.Graphical_Appearance.semObject
    self.obj25.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj25.Graphical_Appearance.semObject
    self.obj25.Graphical_Appearance.linkInfo.Center.semObject=self.obj25.Graphical_Appearance.semObject
    self.obj25.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj25.Graphical_Appearance.semObject
    self.obj25.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj25.Graphical_Appearance.semObject

    # attributes
    self.obj25.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj25.attributes.setValue(lcobj2)

    # cardinality
    self.obj25.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('CD_Class3', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('CD_Class3', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    self.obj25.cardinality.setValue(lcobj2)

    # display
    self.obj25.display.setValue('Actions:\n  > rotateMoveArrowEnd\n  > connectDisconnect\nCardinalities:\n  - To CD_Class3: 1 to 1\n  - From CD_Class3: 1 to 1\n')
    self.obj25.display.setHeight(15)

    # Constraints
    self.obj25.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj25.Constraints.setValue(lcobj2)

    self.obj25.graphClass_= graph_Relationship3
    if self.genGraphics:
       new_obj = graph_Relationship3(860.0,302.0,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Relationship3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.3089999999999999, 1.2193548387096775]
       new_obj.layConstraints['Label Offset'] = [-4.0, 4.0]
    else: new_obj = None
    self.obj25.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)
    self.obj25.postAction( rootNode.CREATE )

    # Connections for obj23 (graphObject_: Obj0) named CD_Class3
    self.drawConnections(
(self.obj23,self.obj24,[429.0, 113.83146067415731, 245.0, 137.0, 245.0, 302.0],"bezier", 3),
(self.obj23,self.obj25,[718.61963190184053, 483.33707865168526, 860.0, 445.0, 860.0, 302.0],"bezier", 3) )
    # Connections for obj24 (graphObject_: Obj1) named CD_Association3
    self.drawConnections(
(self.obj24,self.obj23,[245.0, 302.0, 245.0, 467.0, 429.0, 483.33707865168526],"bezier", 3) )
    # Connections for obj25 (graphObject_: Obj3) named CD_Inheritance3
    self.drawConnections(
(self.obj25,self.obj23,[860.0, 302.0, 860.0, 159.0, 718.61963190184053, 113.83146067415731],"bezier", 3) )

newfunction = CD_classDiagramsV3_ER_MDL

loadedMMName = 'EntityRelationshipV3_META'

atom3version = '0.3'
