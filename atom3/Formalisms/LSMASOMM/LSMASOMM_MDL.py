"""
__LSMASOMM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Wed Nov 16 13:34:52 2016
______________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from CD_Class3 import *
from CD_Association3 import *
from CD_Inheritance3 import *
from graph_CD_Association3 import *
from graph_CD_Class3 import *
from graph_CD_Inheritance3 import *
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

def LSMASOMM_MDL(self, rootNode, CD_ClassDiagramsV3RootNode=None):

    # --- Generating attributes code for ASG CD_ClassDiagramsV3 ---
    if( CD_ClassDiagramsV3RootNode ): 
        # name
        CD_ClassDiagramsV3RootNode.name.setValue('LSMASOMM')

        # author
        CD_ClassDiagramsV3RootNode.author.setValue('Bogdan')

        # showCardinalities
        CD_ClassDiagramsV3RootNode.showCardinalities.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showCardinalities.config = 0

        # showAssociationBox
        CD_ClassDiagramsV3RootNode.showAssociationBox.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showAssociationBox.config = 0

        # description
        CD_ClassDiagramsV3RootNode.description.setValue('\n')
        CD_ClassDiagramsV3RootNode.description.setHeight(15)

        # showAttributes
        CD_ClassDiagramsV3RootNode.showAttributes.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showAttributes.config = 0

        # showActions
        CD_ClassDiagramsV3RootNode.showActions.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showActions.config = 0

        # showConditions
        CD_ClassDiagramsV3RootNode.showConditions.setValue((None, 1))
        CD_ClassDiagramsV3RootNode.showConditions.config = 0

        # attributes
        CD_ClassDiagramsV3RootNode.attributes.setActionFlags([ 1, 1, 1, 0])
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
        CD_ClassDiagramsV3RootNode.attributes.setValue(lcobj1)

        # constraints
        CD_ClassDiagramsV3RootNode.constraints.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        CD_ClassDiagramsV3RootNode.constraints.setValue(lcobj1)
    # --- ASG attributes over ---


    self.obj109=CD_Class3(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # QOCA
    self.obj109.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj109.Graphical_Appearance.setValue( ('OrgUnit', self.obj109))

    # name
    self.obj109.name.setValue('OrgUnit')

    # attributes
    self.obj109.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Individual', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 1))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('UnitActions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj3=ATOM3String('ChangeRole', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('UnitSize', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Individual', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('orgUnitName', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj109.attributes.setValue(lcobj2)

    # Abstract
    self.obj109.Abstract.setValue((None, 0))
    self.obj109.Abstract.config = 0

    # cardinality
    self.obj109.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('isPartOfOrgUnit', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('isPartOfOrgUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('canHaveRole', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('answersToOrgUnit', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('answersToOrgUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj109.cardinality.setValue(lcobj2)

    # display
    self.obj109.display.setValue('Attributes:\n  - ID :: String\n  - Individual :: Boolean\n  - UnitActions :: List\n  - UnitSize :: String\n  - name :: String\nConstraints:\n  > ConstraintOutputOrgUnit\nActions:\n  > determineSize\n  > setNodeID\nMultiplicities:\n  - To isPartOfOrgUnit: 0 to N\n  - From isPartOfOrgUnit: 0 to N\n  - To canHaveRole: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To answersToOrgUnit: 0 to N\n  - From answersToOrgUnit: 0 to N\n')
    self.obj109.display.setHeight(15)

    # Actions
    self.obj109.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('determineSize', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitDetermineSize(self)\nself.UnitSize.setValue(res)\nself.graphObject_.ModifyAttribute(\'UnitSize\', res)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n'))
    lcobj2.append(cobj2)
    self.obj109.Actions.setValue(lcobj2)

    # Constraints
    self.obj109.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintOutputOrgUnit', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitCheckOutputs(self)\nif res is "manyKnArts":\n    return ("OrgUnit can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj109.Constraints.setValue(lcobj2)

    self.obj109.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,220.0,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.88
       new_obj.layConstraints['scale'] = [1.11015625, 3.098360655737705]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=CD_Class3(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(False)

    # QOCA
    self.obj110.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj110.Graphical_Appearance.setValue( ('Role', self.obj110))

    # name
    self.obj110.name.setValue('Role')

    # attributes
    self.obj110.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('RoleID', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('isMetaRole', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('role name', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('roleActions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj3=ATOM3String('RoleAction1', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('RoleAction2', 20)
    lcobj3.append(cobj3)
    cobj3=ATOM3String('RoleActionN', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj110.attributes.setValue(lcobj2)

    # Abstract
    self.obj110.Abstract.setValue((None, 0))
    self.obj110.Abstract.config = 0

    # cardinality
    self.obj110.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canHaveRole', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasActions', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasObjective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('genericAssociation', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('genericAssociation', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('answersToRole', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('answersToRole', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('canStartProcess', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('isPartOfRole', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('isPartOfRole', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj110.cardinality.setValue(lcobj2)

    # display
    self.obj110.display.setValue('Attributes:\n  - ID :: String\n  - isMetaRole :: Boolean\n  - name :: String\n  - roleActions :: List\nConstraints:\n  > RoleConstraintKnArt\nActions:\n  > checkMetaRole\n  > setNodeID\nMultiplicities:\n  - From canHaveRole: 0 to N\n  - To hasActions: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To hasObjective: 0 to N\n  - To genericAssociation: 0 to N\n  - From genericAssociation: 0 to N\n  - To answersToRole: 0 to N\n  - From answersToRole: 0 to N\n  - To canStartProcess: 0 to N\n  - To isPartOfRole: 0 to N\n  - From isPartOfRole: 0 to N\n')
    self.obj110.display.setHeight(15)

    # Actions
    self.obj110.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('checkMetaRole', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]), 'from CustomCode import RoleHierarchy\nres = RoleHierarchy(self)\nself.isMetaRole.setValue((\'isMetaRole\',res))\nself.graphObject_.ModifyAttribute(\'isMetaRole\', res)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n\n'))
    lcobj2.append(cobj2)
    self.obj110.Actions.setValue(lcobj2)

    # Constraints
    self.obj110.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('RoleConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '\nfrom CustomCode import *\n\nres = RoleCheckOutputs(self)\nif res is "manyKnArts":\n    return ("Roles can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelif res is "IndivKnArtError":\n    return ("Roles can have OrganizationalKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj110.Constraints.setValue(lcobj2)

    self.obj110.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(620.0,260.0,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.115625, 3.7868852459016393]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=CD_Class3(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(False)

    # QOCA
    self.obj111.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj111.Graphical_Appearance.setValue( ('Action', self.obj111))

    # name
    self.obj111.name.setValue('Action')

    # attributes
    self.obj111.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ActionCode', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('#action code placeholder or description\n#\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('ActionName', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj111.attributes.setValue(lcobj2)

    # Abstract
    self.obj111.Abstract.setValue((None, 0))
    self.obj111.Abstract.config = 0

    # cardinality
    self.obj111.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasActions', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj111.cardinality.setValue(lcobj2)

    # display
    self.obj111.display.setValue('Attributes:\n  - ActionCode :: Text\n  - name :: String\nMultiplicities:\n  - From hasActions: 0 to N\n')
    self.obj111.display.setHeight(15)

    # Actions
    self.obj111.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj111.Actions.setValue(lcobj2)

    # Constraints
    self.obj111.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj111.Constraints.setValue(lcobj2)

    self.obj111.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(740.0,820.0,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.06
       new_obj.layConstraints['scale'] = [1.02265625, 1.0454545454545454]
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    self.obj112=CD_Class3(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # QOCA
    self.obj112.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj112.Graphical_Appearance.setValue( ('KnowledgeArtifacts', self.obj112))

    # name
    self.obj112.name.setValue('KnowledgeArtifacts')

    # attributes
    self.obj112.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KnArtID', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('description', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KnArtDesc', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KnArtName', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj112.attributes.setValue(lcobj2)

    # Abstract
    self.obj112.Abstract.setValue((None, 1))
    self.obj112.Abstract.config = 0

    # cardinality
    self.obj112.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj112.cardinality.setValue(lcobj2)

    # display
    self.obj112.display.setValue('Attributes:\n  - ID :: String\n  - description :: String\n  - name :: String\nActions:\n  > setNodeID\n')
    self.obj112.display.setHeight(15)

    # Actions
    self.obj112.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n'))
    lcobj2.append(cobj2)
    self.obj112.Actions.setValue(lcobj2)

    # Constraints
    self.obj112.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj112.Constraints.setValue(lcobj2)

    self.obj112.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(980.0,1080.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.239344262295082]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj113=CD_Class3(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # QOCA
    self.obj113.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj113.Graphical_Appearance.setValue( ('OrganisationalKnArt', self.obj113))

    # name
    self.obj113.name.setValue('OrganisationalKnArt')

    # attributes
    self.obj113.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KnArtID', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('KnArtContent', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('#content of the artifact\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('description', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KnArtDesc', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KnArtName', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj113.attributes.setValue(lcobj2)

    # Abstract
    self.obj113.Abstract.setValue((None, 0))
    self.obj113.Abstract.config = 0

    # cardinality
    self.obj113.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj113.cardinality.setValue(lcobj2)

    # display
    self.obj113.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj113.display.setHeight(15)

    # Actions
    self.obj113.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj113.Actions.setValue(lcobj2)

    # Constraints
    self.obj113.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj113.Constraints.setValue(lcobj2)

    self.obj113.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(700.0,1080.0,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj114=CD_Class3(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # QOCA
    self.obj114.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj114.Graphical_Appearance.setValue( ('IndividualKnArt', self.obj114))

    # name
    self.obj114.name.setValue('IndividualKnArt')

    # attributes
    self.obj114.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KnArtID', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('KnArtContent', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('#content of the artifact\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('description', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KnArtDesc', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KnArtName', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj114.attributes.setValue(lcobj2)

    # Abstract
    self.obj114.Abstract.setValue((None, 0))
    self.obj114.Abstract.config = 0

    # cardinality
    self.obj114.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj114.cardinality.setValue(lcobj2)

    # display
    self.obj114.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj114.display.setHeight(15)

    # Actions
    self.obj114.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj114.Actions.setValue(lcobj2)

    # Constraints
    self.obj114.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj114.Constraints.setValue(lcobj2)

    self.obj114.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,1060.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=CD_Class3(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    # QOCA
    self.obj115.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj115.Graphical_Appearance.setValue( ('Strategy', self.obj115))

    # name
    self.obj115.name.setValue('Strategy')

    # attributes
    self.obj115.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('STR', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 80,4 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj115.attributes.setValue(lcobj2)

    # Abstract
    self.obj115.Abstract.setValue((None, 1))
    self.obj115.Abstract.config = 0

    # cardinality
    self.obj115.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj115.cardinality.setValue(lcobj2)

    # display
    self.obj115.display.setValue('Attributes:\n  - ID :: String\n  - description :: Text\n  - name :: String\nActions:\n  > setNodeID\n')
    self.obj115.display.setHeight(15)

    # Actions
    self.obj115.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n'))
    lcobj2.append(cobj2)
    self.obj115.Actions.setValue(lcobj2)

    # Constraints
    self.obj115.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj115.Constraints.setValue(lcobj2)

    self.obj115.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(40.0,340.0,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.239344262295082]
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj116=CD_Class3(self)
    self.obj116.isGraphObjectVisual = True

    if(hasattr(self.obj116, '_setHierarchicalLink')):
      self.obj116._setHierarchicalLink(False)

    # QOCA
    self.obj116.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj116.Graphical_Appearance.setValue( ('Objective', self.obj116))

    # name
    self.obj116.name.setValue('Objective')

    # attributes
    self.obj116.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('STR', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Measurement', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 80,4 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Reward', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 80,4 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 80,4 )
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj116.attributes.setValue(lcobj2)

    # Abstract
    self.obj116.Abstract.setValue((None, 0))
    self.obj116.Abstract.config = 0

    # cardinality
    self.obj116.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('isPartOfObjective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('isPartOfObjective', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasObjective', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj116.cardinality.setValue(lcobj2)

    # display
    self.obj116.display.setValue('Attributes:\n  - Measurement :: Text\n  - Reward :: Text\nMultiplicities:\n  - To isPartOfObjective: 0 to N\n  - From isPartOfObjective: 0 to N\n  - From hasObjective: 0 to N\n')
    self.obj116.display.setHeight(15)

    # Actions
    self.obj116.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj116.Actions.setValue(lcobj2)

    # Constraints
    self.obj116.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj116.Constraints.setValue(lcobj2)

    self.obj116.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(40.0,600.0,self.obj116)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.26875, 1.4459016393442625]
    else: new_obj = None
    self.obj116.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj116)
    self.globalAndLocalPostcondition(self.obj116, rootNode)
    self.obj116.postAction( rootNode.CREATE )

    self.obj117=CD_Class3(self)
    self.obj117.isGraphObjectVisual = True

    if(hasattr(self.obj117, '_setHierarchicalLink')):
      self.obj117._setHierarchicalLink(False)

    # QOCA
    self.obj117.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj117.Graphical_Appearance.setValue( ('Process', self.obj117))

    # name
    self.obj117.name.setValue('Process')

    # attributes
    self.obj117.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Activities', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 80,10 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('STR', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 80,4 )
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj117.attributes.setValue(lcobj2)

    # Abstract
    self.obj117.Abstract.setValue((None, 0))
    self.obj117.Abstract.config = 0

    # cardinality
    self.obj117.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canStartProcess', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasObjective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj117.cardinality.setValue(lcobj2)

    # display
    self.obj117.display.setValue('Attributes:\n  - Activities :: Text\n  - Name :: String\nMultiplicities:\n  - From canStartProcess: 0 to N\n  - To hasObjective: 0 to N\n')
    self.obj117.display.setHeight(15)

    # Actions
    self.obj117.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj117.Actions.setValue(lcobj2)

    # Constraints
    self.obj117.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj117.Constraints.setValue(lcobj2)

    self.obj117.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(280.0,100.0,self.obj117)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.23046875, 1.239344262295082]
    else: new_obj = None
    self.obj117.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj117)
    self.globalAndLocalPostcondition(self.obj117, rootNode)
    self.obj117.postAction( rootNode.CREATE )

    self.obj118=CD_Association3(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(True)

    # QOCA
    self.obj118.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj118.Graphical_Appearance.setValue( ('isPartOfOrgUnit', self.obj118))
    self.obj118.Graphical_Appearance.linkInfo=linkEditor(self,self.obj118.Graphical_Appearance.semObject, "isPartOfOrgUnit")
    self.obj118.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfOrgUnit_1stLink', self.obj118.Graphical_Appearance.linkInfo.FirstLink))
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfOrgUnit_1stSegment', self.obj118.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj118.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj118.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfOrgUnit_Center', self.obj118.Graphical_Appearance.linkInfo))
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfOrgUnit_2ndSegment', self.obj118.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj118.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfOrgUnit_2ndLink', self.obj118.Graphical_Appearance.linkInfo.SecondLink))
    self.obj118.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj118.Graphical_Appearance.semObject
    self.obj118.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj118.Graphical_Appearance.semObject
    self.obj118.Graphical_Appearance.linkInfo.Center.semObject=self.obj118.Graphical_Appearance.semObject
    self.obj118.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj118.Graphical_Appearance.semObject
    self.obj118.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj118.Graphical_Appearance.semObject

    # name
    self.obj118.name.setValue('isPartOfOrgUnit')

    # displaySelect
    self.obj118.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj118.displaySelect.config = 0

    # attributes
    self.obj118.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj118.attributes.setValue(lcobj2)

    # cardinality
    self.obj118.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj118.cardinality.setValue(lcobj2)

    # display
    self.obj118.display.setValue('Multiplicities:\n  - From OrgUnit: 1 to N\n  - To OrgUnit: 1 to N\n')
    self.obj118.display.setHeight(15)

    # Actions
    self.obj118.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj118.Actions.setValue(lcobj2)

    # Constraints
    self.obj118.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj118.Constraints.setValue(lcobj2)

    self.obj118.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1387.9955984,65.809726225,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=CD_Association3(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(True)

    # QOCA
    self.obj119.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj119.Graphical_Appearance.setValue( ('canHaveRole', self.obj119))
    self.obj119.Graphical_Appearance.linkInfo=linkEditor(self,self.obj119.Graphical_Appearance.semObject, "canHaveRole")
    self.obj119.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canHaveRole_1stLink', self.obj119.Graphical_Appearance.linkInfo.FirstLink))
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canHaveRole_1stSegment', self.obj119.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj119.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj119.Graphical_Appearance.linkInfo.Center.setValue( ('canHaveRole_Center', self.obj119.Graphical_Appearance.linkInfo))
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canHaveRole_2ndSegment', self.obj119.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj119.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canHaveRole_2ndLink', self.obj119.Graphical_Appearance.linkInfo.SecondLink))
    self.obj119.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj119.Graphical_Appearance.semObject
    self.obj119.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj119.Graphical_Appearance.semObject
    self.obj119.Graphical_Appearance.linkInfo.Center.semObject=self.obj119.Graphical_Appearance.semObject
    self.obj119.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj119.Graphical_Appearance.semObject
    self.obj119.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj119.Graphical_Appearance.semObject

    # name
    self.obj119.name.setValue('canHaveRole')

    # displaySelect
    self.obj119.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj119.displaySelect.config = 0

    # attributes
    self.obj119.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj119.attributes.setValue(lcobj2)

    # cardinality
    self.obj119.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj119.cardinality.setValue(lcobj2)

    # display
    self.obj119.display.setValue('Multiplicities:\n  - From OrgUnit: 0 to N\n  - To Role: 0 to N\n')
    self.obj119.display.setHeight(15)

    # Actions
    self.obj119.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj119.Actions.setValue(lcobj2)

    # Constraints
    self.obj119.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj119.Constraints.setValue(lcobj2)

    self.obj119.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(971.7601868,527.680947659,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj120=CD_Association3(self)
    self.obj120.isGraphObjectVisual = True

    if(hasattr(self.obj120, '_setHierarchicalLink')):
      self.obj120._setHierarchicalLink(False)

    # QOCA
    self.obj120.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj120.Graphical_Appearance.setValue( ('hasActions', self.obj120))
    self.obj120.Graphical_Appearance.linkInfo=linkEditor(self,self.obj120.Graphical_Appearance.semObject, "hasActions")
    self.obj120.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasActions_1stLink', self.obj120.Graphical_Appearance.linkInfo.FirstLink))
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasActions_1stSegment', self.obj120.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj120.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj120.Graphical_Appearance.linkInfo.Center.setValue( ('hasActions_Center', self.obj120.Graphical_Appearance.linkInfo))
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasActions_2ndSegment', self.obj120.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj120.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasActions_2ndLink', self.obj120.Graphical_Appearance.linkInfo.SecondLink))
    self.obj120.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj120.Graphical_Appearance.semObject
    self.obj120.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj120.Graphical_Appearance.semObject
    self.obj120.Graphical_Appearance.linkInfo.Center.semObject=self.obj120.Graphical_Appearance.semObject
    self.obj120.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj120.Graphical_Appearance.semObject
    self.obj120.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj120.Graphical_Appearance.semObject

    # name
    self.obj120.name.setValue('hasActions')

    # displaySelect
    self.obj120.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj120.displaySelect.config = 0

    # attributes
    self.obj120.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj120.attributes.setValue(lcobj2)

    # cardinality
    self.obj120.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Action', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    self.obj120.cardinality.setValue(lcobj2)

    # display
    self.obj120.display.setValue('Multiplicities:\n  - To Action: 1 to N\n  - From Role: 1 to 1\n')
    self.obj120.display.setHeight(15)

    # Actions
    self.obj120.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj120.Actions.setValue(lcobj2)

    # Constraints
    self.obj120.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj120.Constraints.setValue(lcobj2)

    self.obj120.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(503.161248615,952.001803815,self.obj120)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj120.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj120)
    self.globalAndLocalPostcondition(self.obj120, rootNode)
    self.obj120.postAction( rootNode.CREATE )

    self.obj121=CD_Association3(self)
    self.obj121.isGraphObjectVisual = True

    if(hasattr(self.obj121, '_setHierarchicalLink')):
      self.obj121._setHierarchicalLink(False)

    # QOCA
    self.obj121.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj121.Graphical_Appearance.setValue( ('canAccessKnArt', self.obj121))
    self.obj121.Graphical_Appearance.linkInfo=linkEditor(self,self.obj121.Graphical_Appearance.semObject, "canAccessKnArt")
    self.obj121.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canAccessKnArt_1stLink', self.obj121.Graphical_Appearance.linkInfo.FirstLink))
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canAccessKnArt_1stSegment', self.obj121.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj121.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj121.Graphical_Appearance.linkInfo.Center.setValue( ('canAccessKnArt_Center', self.obj121.Graphical_Appearance.linkInfo))
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canAccessKnArt_2ndSegment', self.obj121.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj121.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canAccessKnArt_2ndLink', self.obj121.Graphical_Appearance.linkInfo.SecondLink))
    self.obj121.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj121.Graphical_Appearance.semObject
    self.obj121.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj121.Graphical_Appearance.semObject
    self.obj121.Graphical_Appearance.linkInfo.Center.semObject=self.obj121.Graphical_Appearance.semObject
    self.obj121.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj121.Graphical_Appearance.semObject
    self.obj121.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj121.Graphical_Appearance.semObject

    # name
    self.obj121.name.setValue('canAccessKnArt')

    # displaySelect
    self.obj121.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj121.displaySelect.config = 0

    # attributes
    self.obj121.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj121.attributes.setValue(lcobj2)

    # cardinality
    self.obj121.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrganisationalKnArt', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('IndividualKnArt', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj121.cardinality.setValue(lcobj2)

    # display
    self.obj121.display.setValue('Constraints:\n  > ConstraintKnArt\nMultiplicities:\n  - To OrganisationalKnArt: 0 to N\n  - From Role: 0 to N\n  - From OrgUnit: 0 to N\n  - To IndividualKnArt: 0 to N\n')
    self.obj121.display.setHeight(15)

    # Actions
    self.obj121.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj121.Actions.setValue(lcobj2)

    # Constraints
    self.obj121.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = canAccessKnArtCheckConnections(self)\n\nif res is "eitherRoleOrUnit":\n    return ("Either Role of OrgUnit can access knowledge.", self.graphObject_)\nelif res is "onlyOneInput":\n    return ("Only one Role or OrgUnit can access one knowledge medium.", self.graphObject_)\nelif res is "RoleWithOrgOnly":\n    return ("Role can access OrganisationalKnArt only!", self.graphObject_)\nelif res is "OrgUnitWithIndivOnly":\n    return ("OrgUnit can access IndividualKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj121.Constraints.setValue(lcobj2)

    self.obj121.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1106.462784,821.548234957,self.obj121)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.6380000000000001, 1.8967741935483875]
    else: new_obj = None
    self.obj121.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj121)
    self.globalAndLocalPostcondition(self.obj121, rootNode)
    self.obj121.postAction( rootNode.CREATE )

    self.obj122=CD_Association3(self)
    self.obj122.isGraphObjectVisual = True

    if(hasattr(self.obj122, '_setHierarchicalLink')):
      self.obj122._setHierarchicalLink(True)

    # QOCA
    self.obj122.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj122.Graphical_Appearance.setValue( ('isPartOfObjective', self.obj122))
    self.obj122.Graphical_Appearance.linkInfo=linkEditor(self,self.obj122.Graphical_Appearance.semObject, "isPartOfObjective")
    self.obj122.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfObjective_1stLink', self.obj122.Graphical_Appearance.linkInfo.FirstLink))
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfObjective_1stSegment', self.obj122.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj122.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj122.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfObjective_Center', self.obj122.Graphical_Appearance.linkInfo))
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfObjective_2ndSegment', self.obj122.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj122.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfObjective_2ndLink', self.obj122.Graphical_Appearance.linkInfo.SecondLink))
    self.obj122.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj122.Graphical_Appearance.semObject
    self.obj122.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj122.Graphical_Appearance.semObject
    self.obj122.Graphical_Appearance.linkInfo.Center.semObject=self.obj122.Graphical_Appearance.semObject
    self.obj122.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj122.Graphical_Appearance.semObject
    self.obj122.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj122.Graphical_Appearance.semObject

    # name
    self.obj122.name.setValue('isPartOfObjective')

    # displaySelect
    self.obj122.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj122.displaySelect.config = 0

    # attributes
    self.obj122.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj122.attributes.setValue(lcobj2)

    # cardinality
    self.obj122.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj122.cardinality.setValue(lcobj2)

    # display
    self.obj122.display.setValue('Multiplicities:\n  - From Objective: 0 to N\n  - To Objective: 0 to N\n')
    self.obj122.display.setHeight(15)

    # Actions
    self.obj122.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj122.Actions.setValue(lcobj2)

    # Constraints
    self.obj122.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj122.Constraints.setValue(lcobj2)

    self.obj122.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(131.944046519,946.91223085,self.obj122)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.225, 1.0]
    else: new_obj = None
    self.obj122.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj122)
    self.globalAndLocalPostcondition(self.obj122, rootNode)
    self.obj122.postAction( rootNode.CREATE )

    self.obj123=CD_Association3(self)
    self.obj123.isGraphObjectVisual = True

    if(hasattr(self.obj123, '_setHierarchicalLink')):
      self.obj123._setHierarchicalLink(False)

    # QOCA
    self.obj123.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj123.Graphical_Appearance.setValue( ('hasObjective', self.obj123))
    self.obj123.Graphical_Appearance.linkInfo=linkEditor(self,self.obj123.Graphical_Appearance.semObject, "hasObjective")
    self.obj123.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasObjective_1stLink', self.obj123.Graphical_Appearance.linkInfo.FirstLink))
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasObjective_1stSegment', self.obj123.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj123.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj123.Graphical_Appearance.linkInfo.Center.setValue( ('hasObjective_Center', self.obj123.Graphical_Appearance.linkInfo))
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasObjective_2ndSegment', self.obj123.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj123.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasObjective_2ndLink', self.obj123.Graphical_Appearance.linkInfo.SecondLink))
    self.obj123.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj123.Graphical_Appearance.semObject
    self.obj123.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj123.Graphical_Appearance.semObject
    self.obj123.Graphical_Appearance.linkInfo.Center.semObject=self.obj123.Graphical_Appearance.semObject
    self.obj123.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj123.Graphical_Appearance.semObject
    self.obj123.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj123.Graphical_Appearance.semObject

    # name
    self.obj123.name.setValue('hasObjective')

    # displaySelect
    self.obj123.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj123.displaySelect.config = 0

    # attributes
    self.obj123.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj123.attributes.setValue(lcobj2)

    # cardinality
    self.obj123.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Process', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj123.cardinality.setValue(lcobj2)

    # display
    self.obj123.display.setValue('Multiplicities:\n  - To Objective: 1 to N\n  - From Role: 0 to N\n  - From Process: 0 to N\n')
    self.obj123.display.setHeight(15)

    # Actions
    self.obj123.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj123.Actions.setValue(lcobj2)

    # Constraints
    self.obj123.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj123.Constraints.setValue(lcobj2)

    self.obj123.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(436.73445957,632.859445861,self.obj123)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.1620000000000001, 1.0838709677419356]
    else: new_obj = None
    self.obj123.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj123)
    self.globalAndLocalPostcondition(self.obj123, rootNode)
    self.obj123.postAction( rootNode.CREATE )

    self.obj124=CD_Association3(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(False)

    # QOCA
    self.obj124.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj124.Graphical_Appearance.setValue( ('genericAssociation', self.obj124))
    self.obj124.Graphical_Appearance.linkInfo=linkEditor(self,self.obj124.Graphical_Appearance.semObject, "genericAssociation")
    self.obj124.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('genericAssociation_1stLink', self.obj124.Graphical_Appearance.linkInfo.FirstLink))
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('genericAssociation_1stSegment', self.obj124.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj124.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.Center.setValue( ('genericAssociation_Center', self.obj124.Graphical_Appearance.linkInfo))
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('genericAssociation_2ndSegment', self.obj124.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('genericAssociation_2ndLink', self.obj124.Graphical_Appearance.linkInfo.SecondLink))
    self.obj124.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.Center.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj124.Graphical_Appearance.semObject
    self.obj124.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj124.Graphical_Appearance.semObject

    # name
    self.obj124.name.setValue('genericAssociation')

    # displaySelect
    self.obj124.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj124.displaySelect.config = 0

    # attributes
    self.obj124.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 80,10 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj124.attributes.setValue(lcobj2)

    # cardinality
    self.obj124.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj124.cardinality.setValue(lcobj2)

    # display
    self.obj124.display.setValue('Attributes:\n  - Name :: String\n  - Description :: Text\nMultiplicities:\n  - To Role: 1 to N\n  - From Role: 1 to N\n')
    self.obj124.display.setHeight(15)

    # Actions
    self.obj124.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj124.Actions.setValue(lcobj2)

    # Constraints
    self.obj124.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj124.Constraints.setValue(lcobj2)

    self.obj124.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1044.0,340.0,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.015, 1.6258064516129034]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj125=CD_Association3(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(True)

    # QOCA
    self.obj125.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj125.Graphical_Appearance.setValue( ('answersToRole', self.obj125))
    self.obj125.Graphical_Appearance.linkInfo=linkEditor(self,self.obj125.Graphical_Appearance.semObject, "answersToRole")
    self.obj125.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj125.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj125.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj125.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj125.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj125.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj125.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj125.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj125.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToRole_1stLink', self.obj125.Graphical_Appearance.linkInfo.FirstLink))
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToRole_1stSegment', self.obj125.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj125.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj125.Graphical_Appearance.linkInfo.Center.setValue( ('answersToRole_Center', self.obj125.Graphical_Appearance.linkInfo))
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToRole_2ndSegment', self.obj125.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj125.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj125.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj125.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj125.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj125.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj125.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj125.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj125.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj125.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToRole_2ndLink', self.obj125.Graphical_Appearance.linkInfo.SecondLink))
    self.obj125.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj125.Graphical_Appearance.semObject
    self.obj125.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj125.Graphical_Appearance.semObject
    self.obj125.Graphical_Appearance.linkInfo.Center.semObject=self.obj125.Graphical_Appearance.semObject
    self.obj125.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj125.Graphical_Appearance.semObject
    self.obj125.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj125.Graphical_Appearance.semObject

    # name
    self.obj125.name.setValue('answersToRole')

    # displaySelect
    self.obj125.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj125.displaySelect.config = 0

    # attributes
    self.obj125.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj125.attributes.setValue(lcobj2)

    # cardinality
    self.obj125.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj125.cardinality.setValue(lcobj2)

    # display
    self.obj125.display.setValue('Multiplicities:\n  - From Role: 1 to N\n  - To Role: 1 to N\n')
    self.obj125.display.setHeight(15)

    # Actions
    self.obj125.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj125.Actions.setValue(lcobj2)

    # Constraints
    self.obj125.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj125.Constraints.setValue(lcobj2)

    self.obj125.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(933.0,176.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=CD_Association3(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # QOCA
    self.obj126.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj126.Graphical_Appearance.setValue( ('canStartProcess', self.obj126))
    self.obj126.Graphical_Appearance.linkInfo=linkEditor(self,self.obj126.Graphical_Appearance.semObject, "canStartProcess")
    self.obj126.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj126.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj126.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj126.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj126.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj126.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj126.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj126.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj126.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canStartProcess_1stLink', self.obj126.Graphical_Appearance.linkInfo.FirstLink))
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canStartProcess_1stSegment', self.obj126.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj126.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj126.Graphical_Appearance.linkInfo.Center.setValue( ('canStartProcess_Center', self.obj126.Graphical_Appearance.linkInfo))
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canStartProcess_2ndSegment', self.obj126.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj126.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj126.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj126.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj126.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj126.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj126.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj126.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj126.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj126.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canStartProcess_2ndLink', self.obj126.Graphical_Appearance.linkInfo.SecondLink))
    self.obj126.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj126.Graphical_Appearance.semObject
    self.obj126.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj126.Graphical_Appearance.semObject
    self.obj126.Graphical_Appearance.linkInfo.Center.semObject=self.obj126.Graphical_Appearance.semObject
    self.obj126.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj126.Graphical_Appearance.semObject
    self.obj126.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj126.Graphical_Appearance.semObject

    # name
    self.obj126.name.setValue('canStartProcess')

    # displaySelect
    self.obj126.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj126.displaySelect.config = 0

    # attributes
    self.obj126.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj126.attributes.setValue(lcobj2)

    # cardinality
    self.obj126.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Process', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj126.cardinality.setValue(lcobj2)

    # display
    self.obj126.display.setValue('Multiplicities:\n  - To Process: 0 to N\n  - From Role: 0 to N\n')
    self.obj126.display.setHeight(15)

    # Actions
    self.obj126.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj126.Actions.setValue(lcobj2)

    # Constraints
    self.obj126.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj126.Constraints.setValue(lcobj2)

    self.obj126.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(470.4921875,411.163934426,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.036, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj127=CD_Association3(self)
    self.obj127.isGraphObjectVisual = True

    if(hasattr(self.obj127, '_setHierarchicalLink')):
      self.obj127._setHierarchicalLink(True)

    # QOCA
    self.obj127.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj127.Graphical_Appearance.setValue( ('answersToOrgUnit', self.obj127))
    self.obj127.Graphical_Appearance.linkInfo=linkEditor(self,self.obj127.Graphical_Appearance.semObject, "answersToOrgUnit")
    self.obj127.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj127.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj127.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj127.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj127.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj127.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj127.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj127.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj127.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToOrgUnit_1stLink', self.obj127.Graphical_Appearance.linkInfo.FirstLink))
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToOrgUnit_1stSegment', self.obj127.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj127.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj127.Graphical_Appearance.linkInfo.Center.setValue( ('answersToOrgUnit_Center', self.obj127.Graphical_Appearance.linkInfo))
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToOrgUnit_2ndSegment', self.obj127.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj127.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj127.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj127.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj127.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj127.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj127.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj127.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj127.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj127.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToOrgUnit_2ndLink', self.obj127.Graphical_Appearance.linkInfo.SecondLink))
    self.obj127.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj127.Graphical_Appearance.semObject
    self.obj127.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj127.Graphical_Appearance.semObject
    self.obj127.Graphical_Appearance.linkInfo.Center.semObject=self.obj127.Graphical_Appearance.semObject
    self.obj127.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj127.Graphical_Appearance.semObject
    self.obj127.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj127.Graphical_Appearance.semObject

    # name
    self.obj127.name.setValue('answersToOrgUnit')

    # displaySelect
    self.obj127.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj127.displaySelect.config = 0

    # attributes
    self.obj127.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj127.attributes.setValue(lcobj2)

    # cardinality
    self.obj127.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj127.cardinality.setValue(lcobj2)

    # display
    self.obj127.display.setValue('Multiplicities:\n  - To OrgUnit: 1 to N\n  - From OrgUnit: 1 to N\n')
    self.obj127.display.setHeight(15)

    # Actions
    self.obj127.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj127.Actions.setValue(lcobj2)

    # Constraints
    self.obj127.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj127.Constraints.setValue(lcobj2)

    self.obj127.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1113.0,79.0,self.obj127)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj127.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj127)
    self.globalAndLocalPostcondition(self.obj127, rootNode)
    self.obj127.postAction( rootNode.CREATE )

    self.obj128=CD_Association3(self)
    self.obj128.isGraphObjectVisual = True

    if(hasattr(self.obj128, '_setHierarchicalLink')):
      self.obj128._setHierarchicalLink(True)

    # QOCA
    self.obj128.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj128.Graphical_Appearance.setValue( ('isPartOfRole', self.obj128))
    self.obj128.Graphical_Appearance.linkInfo=linkEditor(self,self.obj128.Graphical_Appearance.semObject, "isPartOfRole")
    self.obj128.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj128.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj128.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj128.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj128.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj128.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj128.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj128.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj128.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfRole_1stLink', self.obj128.Graphical_Appearance.linkInfo.FirstLink))
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfRole_1stSegment', self.obj128.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj128.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj128.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfRole_Center', self.obj128.Graphical_Appearance.linkInfo))
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfRole_2ndSegment', self.obj128.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],0,0)
    self.obj128.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj128.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj128.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj128.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj128.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj128.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj128.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj128.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj128.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfRole_2ndLink', self.obj128.Graphical_Appearance.linkInfo.SecondLink))
    self.obj128.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj128.Graphical_Appearance.semObject
    self.obj128.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj128.Graphical_Appearance.semObject
    self.obj128.Graphical_Appearance.linkInfo.Center.semObject=self.obj128.Graphical_Appearance.semObject
    self.obj128.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj128.Graphical_Appearance.semObject
    self.obj128.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj128.Graphical_Appearance.semObject

    # name
    self.obj128.name.setValue('isPartOfRole')

    # displaySelect
    self.obj128.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj128.displaySelect.config = 0

    # attributes
    self.obj128.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj128.attributes.setValue(lcobj2)

    # cardinality
    self.obj128.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj128.cardinality.setValue(lcobj2)

    # display
    self.obj128.display.setValue('Multiplicities:\n  - From Role: 0 to N\n  - To Role: 0 to N\n')
    self.obj128.display.setHeight(15)

    # Actions
    self.obj128.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj128.Actions.setValue(lcobj2)

    # Constraints
    self.obj128.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj128.Constraints.setValue(lcobj2)

    self.obj128.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(675.0,160.0,self.obj128)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj128.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj128)
    self.globalAndLocalPostcondition(self.obj128, rootNode)
    self.obj128.postAction( rootNode.CREATE )

    self.obj129=CD_Inheritance3(self)
    self.obj129.isGraphObjectVisual = True

    if(hasattr(self.obj129, '_setHierarchicalLink')):
      self.obj129._setHierarchicalLink(False)

    self.obj129.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1056.21888986,1366.92763695,self.obj129)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj129.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj129)
    self.globalAndLocalPostcondition(self.obj129, rootNode)
    self.obj129.postAction( rootNode.CREATE )

    self.obj130=CD_Inheritance3(self)
    self.obj130.isGraphObjectVisual = True

    if(hasattr(self.obj130, '_setHierarchicalLink')):
      self.obj130._setHierarchicalLink(False)

    self.obj130.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1136.90914946,1358.75085967,self.obj130)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj130.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj130)
    self.globalAndLocalPostcondition(self.obj130, rootNode)
    self.obj130.postAction( rootNode.CREATE )

    self.obj131=CD_Inheritance3(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(False)

    self.obj131.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(152.858254695,586.846159545,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj132=CD_Inheritance3(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(False)

    self.obj132.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(135.466796875,193.786885246,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    # Connections for obj109 (graphObject_: Obj113) named OrgUnit
    self.drawConnections(
(self.obj109,self.obj118,[1368.8125, 220.52459016393442, 1387.9955983980042, 65.8097262245276, 1387.9955984, 65.80972622499999],"true", 3),
(self.obj109,self.obj119,[1241.14453125, 467.5737704918033, 967.8422485527899, 481.40176688146084, 971.7601868, 527.680947659],"true", 3),
(self.obj109,self.obj121,[1241.14453125, 467.5737704918033, 997.8287423035672, 492.3266545159663, 1106.462784, 821.548234957],"true", 3),
(self.obj109,self.obj127,[1241.14453125, 323.8032786885246, 1130.0, 231.0, 1113.0, 79.0], 0, 3) )
    # Connections for obj110 (graphObject_: Obj114) named Role
    self.drawConnections(
(self.obj110,self.obj120,[660.0, 791.0, 541.1631302538499, 883.356649681594, 503.161248615, 952.001803815],"true", 3),
(self.obj110,self.obj121,[832.921875, 715.2622950819672, 1023.5805784296024, 714.1457487347751, 1106.462784, 821.548234957],"true", 3),
(self.obj110,self.obj123,[620.953125, 518.344262295082, 522.0012232889502, 553.7739542825374, 436.73445957, 632.859445861],"true", 3),
(self.obj110,self.obj124,[832.921875, 412.3114754098361, 1044.0, 340.0], 0, 2),
(self.obj110,self.obj125,[793.875, 260.8360655737705, 933.0, 176.0], 0, 2),
(self.obj110,self.obj126,[620.953125, 412.3114754098361, 470.4921875, 411.163934426], 0, 2),
(self.obj110,self.obj128,[660.0, 260.8360655737705, 675.0, 160.0],"true", 2) )
    # Connections for obj111 (graphObject_: Obj115) named Action
    self.drawConnections(
 )
    # Connections for obj112 (graphObject_: Obj116) named KnowledgeArtifacts
    self.drawConnections(
 )
    # Connections for obj113 (graphObject_: Obj117) named OrganisationalKnArt
    self.drawConnections(
(self.obj113,self.obj129,[935.5703125, 1206.090909090909, 1056.21888986, 1366.92763695],"true", 2) )
    # Connections for obj114 (graphObject_: Obj118) named IndividualKnArt
    self.drawConnections(
(self.obj114,self.obj130,[1240.7421875, 1186.090909090909, 1136.90914946, 1358.75085967],"true", 2) )
    # Connections for obj115 (graphObject_: Obj119) named Strategy
    self.drawConnections(
 )
    # Connections for obj116 (graphObject_: Obj120) named Objective
    self.drawConnections(
(self.obj116,self.obj131,[139.75, 629.4918032786885, 152.858254695, 586.846159545],"true", 2),
(self.obj116,self.obj122,[139.75, 803.0, 131.94404651894035, 946.9122308488277, 131.944046519, 946.91223085],"true", 3) )
    # Connections for obj117 (graphObject_: Obj121) named Process
    self.drawConnections(
(self.obj117,self.obj123,[324.0, 247.0, 333.0, 453.0, 436.73445957, 632.859445861],"true", 3),
(self.obj117,self.obj132,[280.93359375, 191.2295081967213, 135.466796875, 193.786885246],"true", 2) )
    # Connections for obj118 (graphObject_: Obj122) named isPartOfOrgUnit
    self.drawConnections(
(self.obj118,self.obj109,[1387.9955984, 65.80972622499999, 1387.9955983980042, 65.8097262245276, 1368.8125, 220.52459016393442],"true", 3) )
    # Connections for obj119 (graphObject_: Obj124) named canHaveRole
    self.drawConnections(
(self.obj119,self.obj110,[971.7601868, 527.680947659, 975.67812505129, 573.9601284363068, 832.921875, 620.5901639344263],"true", 3) )
    # Connections for obj120 (graphObject_: Obj126) named hasActions
    self.drawConnections(
(self.obj120,self.obj111,[503.161248615, 952.001803815, 465.1593669760688, 1020.6469579482074, 741.20703125, 946.0909090909091],"true", 3) )
    # Connections for obj121 (graphObject_: Obj128) named canAccessKnArt
    self.drawConnections(
(self.obj121,self.obj113,[1106.462784, 821.548234957, 1128.2678325033444, 887.9439489105719, 935.5703125, 1122.4545454545455],"true", 3),
(self.obj121,self.obj114,[1106.462784, 821.548234957, 1033.4035107781324, 923.4763808302594, 1240.7421875, 1102.4545454545455],"true", 3) )
    # Connections for obj122 (graphObject_: Obj130) named isPartOfObjective
    self.drawConnections(
(self.obj122,self.obj116,[131.944046519, 946.91223085, 131.94404651894035, 946.9122308488277, 139.75, 803.0],"true", 3) )
    # Connections for obj123 (graphObject_: Obj132) named hasObjective
    self.drawConnections(
(self.obj123,self.obj116,[436.73445957, 632.859445861, 351.4676958509182, 711.9449374392455, 281.65625, 698.8950819672131],"true", 3) )
    # Connections for obj124 (graphObject_: Obj134) named genericAssociation
    self.drawConnections(
(self.obj124,self.obj110,[1044.0, 340.0, 832.921875, 412.3114754098361], 0, 2) )
    # Connections for obj125 (graphObject_: Obj136) named answersToRole
    self.drawConnections(
(self.obj125,self.obj110,[933.0, 176.0, 793.875, 260.8360655737705], 0, 2) )
    # Connections for obj126 (graphObject_: Obj138) named canStartProcess
    self.drawConnections(
(self.obj126,self.obj117,[470.4921875, 411.163934426, 471.65625, 247.0], 0, 2) )
    # Connections for obj127 (graphObject_: Obj140) named answersToOrgUnit
    self.drawConnections(
(self.obj127,self.obj109,[1113.0, 79.0, 1279.0, 145.0, 1280.0, 220.52459016393442], 0, 3) )
    # Connections for obj128 (graphObject_: Obj142) named isPartOfRole
    self.drawConnections(
(self.obj128,self.obj110,[675.0, 160.0, 660.0, 260.8360655737705],"true", 2) )
    # Connections for obj129 (graphObject_: Obj144) of type CD_Inheritance3
    self.drawConnections(
(self.obj129,self.obj112,[1056.21888986, 1366.92763695, 1073.0, 1255.0],"true", 2) )
    # Connections for obj130 (graphObject_: Obj146) of type CD_Inheritance3
    self.drawConnections(
(self.obj130,self.obj112,[1136.90914946, 1358.75085967, 1153.0, 1255.0],"true", 2) )
    # Connections for obj131 (graphObject_: Obj148) of type CD_Inheritance3
    self.drawConnections(
(self.obj131,self.obj115,[152.858254695, 586.846159545, 156.0, 487.0],"true", 2) )
    # Connections for obj132 (graphObject_: Obj150) of type CD_Inheritance3
    self.drawConnections(
(self.obj132,self.obj115,[135.466796875, 193.786885246, 116.0, 341.4918032786885],"true", 2) )

newfunction = LSMASOMM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
