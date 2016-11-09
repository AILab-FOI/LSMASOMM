"""
__LSMASOMM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Wed Nov  9 16:40:07 2016
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


    self.obj582=CD_Class3(self)
    self.obj582.isGraphObjectVisual = True

    if(hasattr(self.obj582, '_setHierarchicalLink')):
      self.obj582._setHierarchicalLink(False)

    # QOCA
    self.obj582.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj582.Graphical_Appearance.setValue( ('OrgUnit', self.obj582))

    # name
    self.obj582.name.setValue('OrgUnit')

    # attributes
    self.obj582.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
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
    self.obj582.attributes.setValue(lcobj2)

    # Abstract
    self.obj582.Abstract.setValue((None, 0))
    self.obj582.Abstract.config = 0

    # cardinality
    self.obj582.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj582.cardinality.setValue(lcobj2)

    # display
    self.obj582.display.setValue('Attributes:\n  - Individual :: Boolean\n  - UnitActions :: List\n  - UnitSize :: String\n  - name :: String\nConstraints:\n  > ConstraintOutputOrgUnit\nActions:\n  > determineSize\nMultiplicities:\n  - To isPartOfOrgUnit: 0 to N\n  - From isPartOfOrgUnit: 0 to N\n  - To canHaveRole: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To answersToOrgUnit: 0 to N\n  - From answersToOrgUnit: 0 to N\n')
    self.obj582.display.setHeight(15)

    # Actions
    self.obj582.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('determineSize', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitDetermineSize(self)\nself.UnitSize.setValue(res)\nself.graphObject_.ModifyAttribute(\'UnitSize\', res)\n\n'))
    lcobj2.append(cobj2)
    self.obj582.Actions.setValue(lcobj2)

    # Constraints
    self.obj582.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintOutputOrgUnit', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitCheckOutputs(self)\nif res is "manyKnArts":\n    return ("OrgUnit can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj582.Constraints.setValue(lcobj2)

    self.obj582.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,220.0,self.obj582)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.88
       new_obj.layConstraints['scale'] = [1.11015625, 2.7540983606557377]
    else: new_obj = None
    self.obj582.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj582)
    self.globalAndLocalPostcondition(self.obj582, rootNode)
    self.obj582.postAction( rootNode.CREATE )

    self.obj583=CD_Class3(self)
    self.obj583.isGraphObjectVisual = True

    if(hasattr(self.obj583, '_setHierarchicalLink')):
      self.obj583._setHierarchicalLink(False)

    # QOCA
    self.obj583.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj583.Graphical_Appearance.setValue( ('Role', self.obj583))

    # name
    self.obj583.name.setValue('Role')

    # attributes
    self.obj583.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 0), ('Direct Editing', 0)))
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
    self.obj583.attributes.setValue(lcobj2)

    # Abstract
    self.obj583.Abstract.setValue((None, 0))
    self.obj583.Abstract.config = 0

    # cardinality
    self.obj583.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj583.cardinality.setValue(lcobj2)

    # display
    self.obj583.display.setValue('Attributes:\n  - ID :: String\n  - isMetaRole :: Boolean\n  - name :: String\n  - roleActions :: List\nConstraints:\n  > RoleConstraintKnArt\nActions:\n  > checkMetaRole\n  > InheritActions\nMultiplicities:\n  - From canHaveRole: 0 to N\n  - To hasActions: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To hasObjective: 0 to N\n  - To genericAssociation: 0 to N\n  - From genericAssociation: 0 to N\n  - To answersToRole: 0 to N\n  - From answersToRole: 0 to N\n  - To canStartProcess: 0 to N\n  - To isPartOfRole: 0 to N\n  - From isPartOfRole: 0 to N\n')
    self.obj583.display.setHeight(15)

    # Actions
    self.obj583.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('checkMetaRole', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]), 'from CustomCode import RoleHierarchy\nres = RoleHierarchy(self)\nself.isMetaRole.setValue((\'isMetaRole\',res))\nself.graphObject_.ModifyAttribute(\'isMetaRole\', res)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('InheritActions', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]), 'from CustomCode import RoleInheritance\nres = RoleInheritance(self)\nif res:\n##    actions = self.roleActions.getValue()\n##    for r in res:\n##    	actions.append(r)\n##    print actions\n##    self.roleActions.setValue(actions)\n    self.graphObject_.ModifyAttribute(\'roleActions\', self.roleActions.toString())\n\n'))
    lcobj2.append(cobj2)
    self.obj583.Actions.setValue(lcobj2)

    # Constraints
    self.obj583.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('RoleConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '\nfrom CustomCode import *\n\nres = RoleCheckOutputs(self)\nif res is "manyKnArts":\n    return ("Roles can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelif res is "IndivKnArtError":\n    return ("Roles can have OrganizationalKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj583.Constraints.setValue(lcobj2)

    self.obj583.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(620.0,280.0,self.obj583)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.115625, 3.7868852459016393]
    else: new_obj = None
    self.obj583.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj583)
    self.globalAndLocalPostcondition(self.obj583, rootNode)
    self.obj583.postAction( rootNode.CREATE )

    self.obj584=CD_Class3(self)
    self.obj584.isGraphObjectVisual = True

    if(hasattr(self.obj584, '_setHierarchicalLink')):
      self.obj584._setHierarchicalLink(False)

    # QOCA
    self.obj584.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj584.Graphical_Appearance.setValue( ('Action', self.obj584))

    # name
    self.obj584.name.setValue('Action')

    # attributes
    self.obj584.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj584.attributes.setValue(lcobj2)

    # Abstract
    self.obj584.Abstract.setValue((None, 0))
    self.obj584.Abstract.config = 0

    # cardinality
    self.obj584.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasActions', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj584.cardinality.setValue(lcobj2)

    # display
    self.obj584.display.setValue('Attributes:\n  - ActionCode :: Text\n  - name :: String\nMultiplicities:\n  - From hasActions: 0 to N\n')
    self.obj584.display.setHeight(15)

    # Actions
    self.obj584.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj584.Actions.setValue(lcobj2)

    # Constraints
    self.obj584.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj584.Constraints.setValue(lcobj2)

    self.obj584.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(740.0,820.0,self.obj584)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.06
       new_obj.layConstraints['scale'] = [1.02265625, 1.0454545454545454]
    else: new_obj = None
    self.obj584.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj584)
    self.globalAndLocalPostcondition(self.obj584, rootNode)
    self.obj584.postAction( rootNode.CREATE )

    self.obj585=CD_Class3(self)
    self.obj585.isGraphObjectVisual = True

    if(hasattr(self.obj585, '_setHierarchicalLink')):
      self.obj585._setHierarchicalLink(False)

    # QOCA
    self.obj585.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj585.Graphical_Appearance.setValue( ('KnowledgeArtifacts', self.obj585))

    # name
    self.obj585.name.setValue('KnowledgeArtifacts')

    # attributes
    self.obj585.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj585.attributes.setValue(lcobj2)

    # Abstract
    self.obj585.Abstract.setValue((None, 1))
    self.obj585.Abstract.config = 0

    # cardinality
    self.obj585.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj585.cardinality.setValue(lcobj2)

    # display
    self.obj585.display.setValue('Attributes:\n  - ID :: String\n  - description :: String\n  - name :: String\n')
    self.obj585.display.setHeight(15)

    # Actions
    self.obj585.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj585.Actions.setValue(lcobj2)

    # Constraints
    self.obj585.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj585.Constraints.setValue(lcobj2)

    self.obj585.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(980.0,1080.0,self.obj585)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0454545454545454]
    else: new_obj = None
    self.obj585.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj585)
    self.globalAndLocalPostcondition(self.obj585, rootNode)
    self.obj585.postAction( rootNode.CREATE )

    self.obj586=CD_Class3(self)
    self.obj586.isGraphObjectVisual = True

    if(hasattr(self.obj586, '_setHierarchicalLink')):
      self.obj586._setHierarchicalLink(False)

    # QOCA
    self.obj586.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj586.Graphical_Appearance.setValue( ('OrganisationalKnArt', self.obj586))

    # name
    self.obj586.name.setValue('OrganisationalKnArt')

    # attributes
    self.obj586.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj586.attributes.setValue(lcobj2)

    # Abstract
    self.obj586.Abstract.setValue((None, 0))
    self.obj586.Abstract.config = 0

    # cardinality
    self.obj586.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj586.cardinality.setValue(lcobj2)

    # display
    self.obj586.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj586.display.setHeight(15)

    # Actions
    self.obj586.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj586.Actions.setValue(lcobj2)

    # Constraints
    self.obj586.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj586.Constraints.setValue(lcobj2)

    self.obj586.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(700.0,1080.0,self.obj586)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj586.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj586)
    self.globalAndLocalPostcondition(self.obj586, rootNode)
    self.obj586.postAction( rootNode.CREATE )

    self.obj587=CD_Class3(self)
    self.obj587.isGraphObjectVisual = True

    if(hasattr(self.obj587, '_setHierarchicalLink')):
      self.obj587._setHierarchicalLink(False)

    # QOCA
    self.obj587.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj587.Graphical_Appearance.setValue( ('IndividualKnArt', self.obj587))

    # name
    self.obj587.name.setValue('IndividualKnArt')

    # attributes
    self.obj587.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj587.attributes.setValue(lcobj2)

    # Abstract
    self.obj587.Abstract.setValue((None, 0))
    self.obj587.Abstract.config = 0

    # cardinality
    self.obj587.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj587.cardinality.setValue(lcobj2)

    # display
    self.obj587.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj587.display.setHeight(15)

    # Actions
    self.obj587.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj587.Actions.setValue(lcobj2)

    # Constraints
    self.obj587.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj587.Constraints.setValue(lcobj2)

    self.obj587.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,1060.0,self.obj587)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj587.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj587)
    self.globalAndLocalPostcondition(self.obj587, rootNode)
    self.obj587.postAction( rootNode.CREATE )

    self.obj588=CD_Class3(self)
    self.obj588.isGraphObjectVisual = True

    if(hasattr(self.obj588, '_setHierarchicalLink')):
      self.obj588._setHierarchicalLink(False)

    # QOCA
    self.obj588.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj588.Graphical_Appearance.setValue( ('Strategy', self.obj588))

    # name
    self.obj588.name.setValue('Strategy')

    # attributes
    self.obj588.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('STR', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('description', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj588.attributes.setValue(lcobj2)

    # Abstract
    self.obj588.Abstract.setValue((None, 1))
    self.obj588.Abstract.config = 0

    # cardinality
    self.obj588.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj588.cardinality.setValue(lcobj2)

    # display
    self.obj588.display.setValue('Attributes:\n  - ID :: String\n  - description :: String\n  - name :: String\n')
    self.obj588.display.setHeight(15)

    # Actions
    self.obj588.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj588.Actions.setValue(lcobj2)

    # Constraints
    self.obj588.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj588.Constraints.setValue(lcobj2)

    self.obj588.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(40.0,340.0,self.obj588)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0454545454545454]
    else: new_obj = None
    self.obj588.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj588)
    self.globalAndLocalPostcondition(self.obj588, rootNode)
    self.obj588.postAction( rootNode.CREATE )

    self.obj589=CD_Class3(self)
    self.obj589.isGraphObjectVisual = True

    if(hasattr(self.obj589, '_setHierarchicalLink')):
      self.obj589._setHierarchicalLink(False)

    # QOCA
    self.obj589.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj589.Graphical_Appearance.setValue( ('Objective', self.obj589))

    # name
    self.obj589.name.setValue('Objective')

    # attributes
    self.obj589.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('STR', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Measurement', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 80,5 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Reward', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 80,5 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('description', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj589.attributes.setValue(lcobj2)

    # Abstract
    self.obj589.Abstract.setValue((None, 0))
    self.obj589.Abstract.config = 0

    # cardinality
    self.obj589.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj589.cardinality.setValue(lcobj2)

    # display
    self.obj589.display.setValue('Attributes:\n  - Measurement :: Text\n  - Reward :: Text\nMultiplicities:\n  - To isPartOfObjective: 0 to N\n  - From isPartOfObjective: 0 to N\n  - From hasObjective: 0 to N\n')
    self.obj589.display.setHeight(15)

    # Actions
    self.obj589.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj589.Actions.setValue(lcobj2)

    # Constraints
    self.obj589.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj589.Constraints.setValue(lcobj2)

    self.obj589.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(40.0,600.0,self.obj589)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.26875, 1.4459016393442625]
    else: new_obj = None
    self.obj589.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj589)
    self.globalAndLocalPostcondition(self.obj589, rootNode)
    self.obj589.postAction( rootNode.CREATE )

    self.obj590=CD_Class3(self)
    self.obj590.isGraphObjectVisual = True

    if(hasattr(self.obj590, '_setHierarchicalLink')):
      self.obj590._setHierarchicalLink(False)

    # QOCA
    self.obj590.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj590.Graphical_Appearance.setValue( ('Process', self.obj590))

    # name
    self.obj590.name.setValue('Process')

    # attributes
    self.obj590.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Activities', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 80,10 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('PRCS', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj590.attributes.setValue(lcobj2)

    # Abstract
    self.obj590.Abstract.setValue((None, 0))
    self.obj590.Abstract.config = 0

    # cardinality
    self.obj590.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canStartProcess', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasObjective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj590.cardinality.setValue(lcobj2)

    # display
    self.obj590.display.setValue('Attributes:\n  - Activities :: Text\n  - ID :: String\n  - Name :: String\nMultiplicities:\n  - From canStartProcess: 0 to N\n  - To hasObjective: 0 to N\n')
    self.obj590.display.setHeight(15)

    # Actions
    self.obj590.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj590.Actions.setValue(lcobj2)

    # Constraints
    self.obj590.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj590.Constraints.setValue(lcobj2)

    self.obj590.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(280.0,80.0,self.obj590)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.23046875, 1.4459016393442625]
    else: new_obj = None
    self.obj590.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj590)
    self.globalAndLocalPostcondition(self.obj590, rootNode)
    self.obj590.postAction( rootNode.CREATE )

    self.obj591=CD_Association3(self)
    self.obj591.isGraphObjectVisual = True

    if(hasattr(self.obj591, '_setHierarchicalLink')):
      self.obj591._setHierarchicalLink(True)

    # QOCA
    self.obj591.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj591.Graphical_Appearance.setValue( ('isPartOfOrgUnit', self.obj591))
    self.obj591.Graphical_Appearance.linkInfo=linkEditor(self,self.obj591.Graphical_Appearance.semObject, "isPartOfOrgUnit")
    self.obj591.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj591.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj591.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj591.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj591.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj591.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj591.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj591.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj591.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfOrgUnit_1stLink', self.obj591.Graphical_Appearance.linkInfo.FirstLink))
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfOrgUnit_1stSegment', self.obj591.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj591.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj591.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfOrgUnit_Center', self.obj591.Graphical_Appearance.linkInfo))
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfOrgUnit_2ndSegment', self.obj591.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj591.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj591.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj591.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj591.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj591.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj591.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj591.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj591.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj591.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfOrgUnit_2ndLink', self.obj591.Graphical_Appearance.linkInfo.SecondLink))
    self.obj591.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj591.Graphical_Appearance.semObject
    self.obj591.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj591.Graphical_Appearance.semObject
    self.obj591.Graphical_Appearance.linkInfo.Center.semObject=self.obj591.Graphical_Appearance.semObject
    self.obj591.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj591.Graphical_Appearance.semObject
    self.obj591.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj591.Graphical_Appearance.semObject

    # name
    self.obj591.name.setValue('isPartOfOrgUnit')

    # displaySelect
    self.obj591.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj591.displaySelect.config = 0

    # attributes
    self.obj591.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj591.attributes.setValue(lcobj2)

    # cardinality
    self.obj591.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj591.cardinality.setValue(lcobj2)

    # display
    self.obj591.display.setValue('Multiplicities:\n  - From OrgUnit: 1 to N\n  - To OrgUnit: 1 to N\n')
    self.obj591.display.setHeight(15)

    # Actions
    self.obj591.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj591.Actions.setValue(lcobj2)

    # Constraints
    self.obj591.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj591.Constraints.setValue(lcobj2)

    self.obj591.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1387.9955984,65.809726225,self.obj591)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj591.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj591)
    self.globalAndLocalPostcondition(self.obj591, rootNode)
    self.obj591.postAction( rootNode.CREATE )

    self.obj592=CD_Association3(self)
    self.obj592.isGraphObjectVisual = True

    if(hasattr(self.obj592, '_setHierarchicalLink')):
      self.obj592._setHierarchicalLink(True)

    # QOCA
    self.obj592.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj592.Graphical_Appearance.setValue( ('canHaveRole', self.obj592))
    self.obj592.Graphical_Appearance.linkInfo=linkEditor(self,self.obj592.Graphical_Appearance.semObject, "canHaveRole")
    self.obj592.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj592.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj592.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj592.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj592.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj592.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj592.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj592.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj592.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canHaveRole_1stLink', self.obj592.Graphical_Appearance.linkInfo.FirstLink))
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canHaveRole_1stSegment', self.obj592.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj592.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj592.Graphical_Appearance.linkInfo.Center.setValue( ('canHaveRole_Center', self.obj592.Graphical_Appearance.linkInfo))
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canHaveRole_2ndSegment', self.obj592.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj592.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj592.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj592.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj592.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj592.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj592.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj592.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj592.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj592.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canHaveRole_2ndLink', self.obj592.Graphical_Appearance.linkInfo.SecondLink))
    self.obj592.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj592.Graphical_Appearance.semObject
    self.obj592.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj592.Graphical_Appearance.semObject
    self.obj592.Graphical_Appearance.linkInfo.Center.semObject=self.obj592.Graphical_Appearance.semObject
    self.obj592.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj592.Graphical_Appearance.semObject
    self.obj592.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj592.Graphical_Appearance.semObject

    # name
    self.obj592.name.setValue('canHaveRole')

    # displaySelect
    self.obj592.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj592.displaySelect.config = 0

    # attributes
    self.obj592.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj592.attributes.setValue(lcobj2)

    # cardinality
    self.obj592.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj592.cardinality.setValue(lcobj2)

    # display
    self.obj592.display.setValue('Multiplicities:\n  - From OrgUnit: 0 to N\n  - To Role: 0 to N\n')
    self.obj592.display.setHeight(15)

    # Actions
    self.obj592.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj592.Actions.setValue(lcobj2)

    # Constraints
    self.obj592.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj592.Constraints.setValue(lcobj2)

    self.obj592.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(971.7601868,527.680947659,self.obj592)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj592.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj592)
    self.globalAndLocalPostcondition(self.obj592, rootNode)
    self.obj592.postAction( rootNode.CREATE )

    self.obj593=CD_Association3(self)
    self.obj593.isGraphObjectVisual = True

    if(hasattr(self.obj593, '_setHierarchicalLink')):
      self.obj593._setHierarchicalLink(False)

    # QOCA
    self.obj593.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj593.Graphical_Appearance.setValue( ('hasActions', self.obj593))
    self.obj593.Graphical_Appearance.linkInfo=linkEditor(self,self.obj593.Graphical_Appearance.semObject, "hasActions")
    self.obj593.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj593.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj593.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj593.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj593.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj593.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj593.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj593.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj593.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasActions_1stLink', self.obj593.Graphical_Appearance.linkInfo.FirstLink))
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasActions_1stSegment', self.obj593.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj593.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj593.Graphical_Appearance.linkInfo.Center.setValue( ('hasActions_Center', self.obj593.Graphical_Appearance.linkInfo))
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasActions_2ndSegment', self.obj593.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj593.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj593.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj593.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj593.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj593.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj593.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj593.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj593.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj593.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasActions_2ndLink', self.obj593.Graphical_Appearance.linkInfo.SecondLink))
    self.obj593.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj593.Graphical_Appearance.semObject
    self.obj593.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj593.Graphical_Appearance.semObject
    self.obj593.Graphical_Appearance.linkInfo.Center.semObject=self.obj593.Graphical_Appearance.semObject
    self.obj593.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj593.Graphical_Appearance.semObject
    self.obj593.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj593.Graphical_Appearance.semObject

    # name
    self.obj593.name.setValue('hasActions')

    # displaySelect
    self.obj593.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj593.displaySelect.config = 0

    # attributes
    self.obj593.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj593.attributes.setValue(lcobj2)

    # cardinality
    self.obj593.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Action', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    self.obj593.cardinality.setValue(lcobj2)

    # display
    self.obj593.display.setValue('Multiplicities:\n  - To Action: 1 to N\n  - From Role: 1 to 1\n')
    self.obj593.display.setHeight(15)

    # Actions
    self.obj593.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj593.Actions.setValue(lcobj2)

    # Constraints
    self.obj593.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj593.Constraints.setValue(lcobj2)

    self.obj593.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(503.161248615,952.001803815,self.obj593)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj593.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj593)
    self.globalAndLocalPostcondition(self.obj593, rootNode)
    self.obj593.postAction( rootNode.CREATE )

    self.obj594=CD_Association3(self)
    self.obj594.isGraphObjectVisual = True

    if(hasattr(self.obj594, '_setHierarchicalLink')):
      self.obj594._setHierarchicalLink(False)

    # QOCA
    self.obj594.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj594.Graphical_Appearance.setValue( ('canAccessKnArt', self.obj594))
    self.obj594.Graphical_Appearance.linkInfo=linkEditor(self,self.obj594.Graphical_Appearance.semObject, "canAccessKnArt")
    self.obj594.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj594.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj594.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj594.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj594.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj594.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj594.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj594.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj594.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canAccessKnArt_1stLink', self.obj594.Graphical_Appearance.linkInfo.FirstLink))
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canAccessKnArt_1stSegment', self.obj594.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj594.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj594.Graphical_Appearance.linkInfo.Center.setValue( ('canAccessKnArt_Center', self.obj594.Graphical_Appearance.linkInfo))
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canAccessKnArt_2ndSegment', self.obj594.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj594.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj594.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj594.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj594.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj594.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj594.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj594.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj594.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj594.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canAccessKnArt_2ndLink', self.obj594.Graphical_Appearance.linkInfo.SecondLink))
    self.obj594.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj594.Graphical_Appearance.semObject
    self.obj594.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj594.Graphical_Appearance.semObject
    self.obj594.Graphical_Appearance.linkInfo.Center.semObject=self.obj594.Graphical_Appearance.semObject
    self.obj594.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj594.Graphical_Appearance.semObject
    self.obj594.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj594.Graphical_Appearance.semObject

    # name
    self.obj594.name.setValue('canAccessKnArt')

    # displaySelect
    self.obj594.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj594.displaySelect.config = 0

    # attributes
    self.obj594.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj594.attributes.setValue(lcobj2)

    # cardinality
    self.obj594.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj594.cardinality.setValue(lcobj2)

    # display
    self.obj594.display.setValue('Constraints:\n  > ConstraintKnArt\nMultiplicities:\n  - To OrganisationalKnArt: 0 to N\n  - From Role: 0 to N\n  - From OrgUnit: 0 to N\n  - To IndividualKnArt: 0 to N\n')
    self.obj594.display.setHeight(15)

    # Actions
    self.obj594.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj594.Actions.setValue(lcobj2)

    # Constraints
    self.obj594.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = canAccessKnArtCheckConnections(self)\n\nif res is "eitherRoleOrUnit":\n    return ("Either Role of OrgUnit can access knowledge.", self.graphObject_)\nelif res is "onlyOneInput":\n    return ("Only one Role or OrgUnit can access one knowledge medium.", self.graphObject_)\nelif res is "RoleWithOrgOnly":\n    return ("Role can access OrganisationalKnArt only!", self.graphObject_)\nelif res is "OrgUnitWithIndivOnly":\n    return ("OrgUnit can access IndividualKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj594.Constraints.setValue(lcobj2)

    self.obj594.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1106.462784,821.548234957,self.obj594)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.6380000000000001, 1.8967741935483875]
    else: new_obj = None
    self.obj594.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj594)
    self.globalAndLocalPostcondition(self.obj594, rootNode)
    self.obj594.postAction( rootNode.CREATE )

    self.obj595=CD_Association3(self)
    self.obj595.isGraphObjectVisual = True

    if(hasattr(self.obj595, '_setHierarchicalLink')):
      self.obj595._setHierarchicalLink(True)

    # QOCA
    self.obj595.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj595.Graphical_Appearance.setValue( ('isPartOfObjective', self.obj595))
    self.obj595.Graphical_Appearance.linkInfo=linkEditor(self,self.obj595.Graphical_Appearance.semObject, "isPartOfObjective")
    self.obj595.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj595.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj595.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj595.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj595.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj595.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj595.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj595.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj595.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfObjective_1stLink', self.obj595.Graphical_Appearance.linkInfo.FirstLink))
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfObjective_1stSegment', self.obj595.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj595.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj595.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfObjective_Center', self.obj595.Graphical_Appearance.linkInfo))
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfObjective_2ndSegment', self.obj595.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj595.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj595.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj595.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj595.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj595.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj595.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj595.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj595.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj595.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfObjective_2ndLink', self.obj595.Graphical_Appearance.linkInfo.SecondLink))
    self.obj595.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj595.Graphical_Appearance.semObject
    self.obj595.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj595.Graphical_Appearance.semObject
    self.obj595.Graphical_Appearance.linkInfo.Center.semObject=self.obj595.Graphical_Appearance.semObject
    self.obj595.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj595.Graphical_Appearance.semObject
    self.obj595.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj595.Graphical_Appearance.semObject

    # name
    self.obj595.name.setValue('isPartOfObjective')

    # displaySelect
    self.obj595.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj595.displaySelect.config = 0

    # attributes
    self.obj595.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj595.attributes.setValue(lcobj2)

    # cardinality
    self.obj595.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj595.cardinality.setValue(lcobj2)

    # display
    self.obj595.display.setValue('Multiplicities:\n  - From Objective: 0 to N\n  - To Objective: 0 to N\n')
    self.obj595.display.setHeight(15)

    # Actions
    self.obj595.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj595.Actions.setValue(lcobj2)

    # Constraints
    self.obj595.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj595.Constraints.setValue(lcobj2)

    self.obj595.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(131.944046519,946.91223085,self.obj595)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.225, 1.0]
    else: new_obj = None
    self.obj595.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj595)
    self.globalAndLocalPostcondition(self.obj595, rootNode)
    self.obj595.postAction( rootNode.CREATE )

    self.obj596=CD_Association3(self)
    self.obj596.isGraphObjectVisual = True

    if(hasattr(self.obj596, '_setHierarchicalLink')):
      self.obj596._setHierarchicalLink(False)

    # QOCA
    self.obj596.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj596.Graphical_Appearance.setValue( ('hasObjective', self.obj596))
    self.obj596.Graphical_Appearance.linkInfo=linkEditor(self,self.obj596.Graphical_Appearance.semObject, "hasObjective")
    self.obj596.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj596.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj596.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj596.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj596.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj596.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj596.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj596.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj596.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasObjective_1stLink', self.obj596.Graphical_Appearance.linkInfo.FirstLink))
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasObjective_1stSegment', self.obj596.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj596.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj596.Graphical_Appearance.linkInfo.Center.setValue( ('hasObjective_Center', self.obj596.Graphical_Appearance.linkInfo))
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasObjective_2ndSegment', self.obj596.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj596.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj596.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj596.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj596.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj596.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj596.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj596.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj596.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj596.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasObjective_2ndLink', self.obj596.Graphical_Appearance.linkInfo.SecondLink))
    self.obj596.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj596.Graphical_Appearance.semObject
    self.obj596.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj596.Graphical_Appearance.semObject
    self.obj596.Graphical_Appearance.linkInfo.Center.semObject=self.obj596.Graphical_Appearance.semObject
    self.obj596.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj596.Graphical_Appearance.semObject
    self.obj596.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj596.Graphical_Appearance.semObject

    # name
    self.obj596.name.setValue('hasObjective')

    # displaySelect
    self.obj596.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj596.displaySelect.config = 0

    # attributes
    self.obj596.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj596.attributes.setValue(lcobj2)

    # cardinality
    self.obj596.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj596.cardinality.setValue(lcobj2)

    # display
    self.obj596.display.setValue('Multiplicities:\n  - To Objective: 1 to N\n  - From Role: 0 to N\n  - From Process: 0 to N\n')
    self.obj596.display.setHeight(15)

    # Actions
    self.obj596.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj596.Actions.setValue(lcobj2)

    # Constraints
    self.obj596.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj596.Constraints.setValue(lcobj2)

    self.obj596.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(436.73445957,632.859445861,self.obj596)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.1620000000000001, 1.0838709677419356]
    else: new_obj = None
    self.obj596.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj596)
    self.globalAndLocalPostcondition(self.obj596, rootNode)
    self.obj596.postAction( rootNode.CREATE )

    self.obj597=CD_Association3(self)
    self.obj597.isGraphObjectVisual = True

    if(hasattr(self.obj597, '_setHierarchicalLink')):
      self.obj597._setHierarchicalLink(False)

    # QOCA
    self.obj597.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj597.Graphical_Appearance.setValue( ('genericAssociation', self.obj597))
    self.obj597.Graphical_Appearance.linkInfo=linkEditor(self,self.obj597.Graphical_Appearance.semObject, "genericAssociation")
    self.obj597.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj597.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj597.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj597.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj597.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj597.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj597.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj597.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj597.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('genericAssociation_1stLink', self.obj597.Graphical_Appearance.linkInfo.FirstLink))
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('genericAssociation_1stSegment', self.obj597.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj597.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj597.Graphical_Appearance.linkInfo.Center.setValue( ('genericAssociation_Center', self.obj597.Graphical_Appearance.linkInfo))
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('genericAssociation_2ndSegment', self.obj597.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj597.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj597.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj597.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj597.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj597.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj597.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj597.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj597.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj597.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('genericAssociation_2ndLink', self.obj597.Graphical_Appearance.linkInfo.SecondLink))
    self.obj597.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj597.Graphical_Appearance.semObject
    self.obj597.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj597.Graphical_Appearance.semObject
    self.obj597.Graphical_Appearance.linkInfo.Center.semObject=self.obj597.Graphical_Appearance.semObject
    self.obj597.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj597.Graphical_Appearance.semObject
    self.obj597.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj597.Graphical_Appearance.semObject

    # name
    self.obj597.name.setValue('genericAssociation')

    # displaySelect
    self.obj597.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj597.displaySelect.config = 0

    # attributes
    self.obj597.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj597.attributes.setValue(lcobj2)

    # cardinality
    self.obj597.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj597.cardinality.setValue(lcobj2)

    # display
    self.obj597.display.setValue('Attributes:\n  - Name :: String\n  - Description :: Text\nMultiplicities:\n  - To Role: 1 to N\n  - From Role: 1 to N\n')
    self.obj597.display.setHeight(15)

    # Actions
    self.obj597.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj597.Actions.setValue(lcobj2)

    # Constraints
    self.obj597.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj597.Constraints.setValue(lcobj2)

    self.obj597.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1044.0,340.0,self.obj597)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.015, 1.6258064516129034]
    else: new_obj = None
    self.obj597.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj597)
    self.globalAndLocalPostcondition(self.obj597, rootNode)
    self.obj597.postAction( rootNode.CREATE )

    self.obj598=CD_Association3(self)
    self.obj598.isGraphObjectVisual = True

    if(hasattr(self.obj598, '_setHierarchicalLink')):
      self.obj598._setHierarchicalLink(True)

    # QOCA
    self.obj598.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj598.Graphical_Appearance.setValue( ('answersToRole', self.obj598))
    self.obj598.Graphical_Appearance.linkInfo=linkEditor(self,self.obj598.Graphical_Appearance.semObject, "answersToRole")
    self.obj598.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj598.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj598.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj598.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj598.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj598.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj598.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj598.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj598.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToRole_1stLink', self.obj598.Graphical_Appearance.linkInfo.FirstLink))
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToRole_1stSegment', self.obj598.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj598.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj598.Graphical_Appearance.linkInfo.Center.setValue( ('answersToRole_Center', self.obj598.Graphical_Appearance.linkInfo))
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToRole_2ndSegment', self.obj598.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj598.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj598.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj598.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj598.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj598.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj598.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj598.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj598.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj598.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToRole_2ndLink', self.obj598.Graphical_Appearance.linkInfo.SecondLink))
    self.obj598.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj598.Graphical_Appearance.semObject
    self.obj598.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj598.Graphical_Appearance.semObject
    self.obj598.Graphical_Appearance.linkInfo.Center.semObject=self.obj598.Graphical_Appearance.semObject
    self.obj598.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj598.Graphical_Appearance.semObject
    self.obj598.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj598.Graphical_Appearance.semObject

    # name
    self.obj598.name.setValue('answersToRole')

    # displaySelect
    self.obj598.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj598.displaySelect.config = 0

    # attributes
    self.obj598.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj598.attributes.setValue(lcobj2)

    # cardinality
    self.obj598.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj598.cardinality.setValue(lcobj2)

    # display
    self.obj598.display.setValue('Multiplicities:\n  - From Role: 1 to N\n  - To Role: 1 to N\n')
    self.obj598.display.setHeight(15)

    # Actions
    self.obj598.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj598.Actions.setValue(lcobj2)

    # Constraints
    self.obj598.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj598.Constraints.setValue(lcobj2)

    self.obj598.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(933.0,176.0,self.obj598)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj598.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj598)
    self.globalAndLocalPostcondition(self.obj598, rootNode)
    self.obj598.postAction( rootNode.CREATE )

    self.obj599=CD_Association3(self)
    self.obj599.isGraphObjectVisual = True

    if(hasattr(self.obj599, '_setHierarchicalLink')):
      self.obj599._setHierarchicalLink(False)

    # QOCA
    self.obj599.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj599.Graphical_Appearance.setValue( ('canStartProcess', self.obj599))
    self.obj599.Graphical_Appearance.linkInfo=linkEditor(self,self.obj599.Graphical_Appearance.semObject, "canStartProcess")
    self.obj599.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj599.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj599.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj599.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj599.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj599.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj599.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj599.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj599.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canStartProcess_1stLink', self.obj599.Graphical_Appearance.linkInfo.FirstLink))
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canStartProcess_1stSegment', self.obj599.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj599.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj599.Graphical_Appearance.linkInfo.Center.setValue( ('canStartProcess_Center', self.obj599.Graphical_Appearance.linkInfo))
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canStartProcess_2ndSegment', self.obj599.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj599.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj599.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj599.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj599.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj599.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj599.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj599.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj599.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj599.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canStartProcess_2ndLink', self.obj599.Graphical_Appearance.linkInfo.SecondLink))
    self.obj599.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj599.Graphical_Appearance.semObject
    self.obj599.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj599.Graphical_Appearance.semObject
    self.obj599.Graphical_Appearance.linkInfo.Center.semObject=self.obj599.Graphical_Appearance.semObject
    self.obj599.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj599.Graphical_Appearance.semObject
    self.obj599.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj599.Graphical_Appearance.semObject

    # name
    self.obj599.name.setValue('canStartProcess')

    # displaySelect
    self.obj599.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj599.displaySelect.config = 0

    # attributes
    self.obj599.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj599.attributes.setValue(lcobj2)

    # cardinality
    self.obj599.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Process', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj599.cardinality.setValue(lcobj2)

    # display
    self.obj599.display.setValue('Multiplicities:\n  - To Process: 0 to N\n  - From Role: 0 to N\n')
    self.obj599.display.setHeight(15)

    # Actions
    self.obj599.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj599.Actions.setValue(lcobj2)

    # Constraints
    self.obj599.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj599.Constraints.setValue(lcobj2)

    self.obj599.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(470.4921875,411.163934426,self.obj599)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.036, 1.0]
    else: new_obj = None
    self.obj599.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj599)
    self.globalAndLocalPostcondition(self.obj599, rootNode)
    self.obj599.postAction( rootNode.CREATE )

    self.obj600=CD_Association3(self)
    self.obj600.isGraphObjectVisual = True

    if(hasattr(self.obj600, '_setHierarchicalLink')):
      self.obj600._setHierarchicalLink(True)

    # QOCA
    self.obj600.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj600.Graphical_Appearance.setValue( ('answersToOrgUnit', self.obj600))
    self.obj600.Graphical_Appearance.linkInfo=linkEditor(self,self.obj600.Graphical_Appearance.semObject, "answersToOrgUnit")
    self.obj600.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj600.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj600.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj600.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj600.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj600.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj600.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj600.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj600.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToOrgUnit_1stLink', self.obj600.Graphical_Appearance.linkInfo.FirstLink))
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToOrgUnit_1stSegment', self.obj600.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj600.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj600.Graphical_Appearance.linkInfo.Center.setValue( ('answersToOrgUnit_Center', self.obj600.Graphical_Appearance.linkInfo))
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToOrgUnit_2ndSegment', self.obj600.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj600.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj600.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj600.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj600.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj600.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj600.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj600.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj600.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj600.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToOrgUnit_2ndLink', self.obj600.Graphical_Appearance.linkInfo.SecondLink))
    self.obj600.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj600.Graphical_Appearance.semObject
    self.obj600.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj600.Graphical_Appearance.semObject
    self.obj600.Graphical_Appearance.linkInfo.Center.semObject=self.obj600.Graphical_Appearance.semObject
    self.obj600.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj600.Graphical_Appearance.semObject
    self.obj600.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj600.Graphical_Appearance.semObject

    # name
    self.obj600.name.setValue('answersToOrgUnit')

    # displaySelect
    self.obj600.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj600.displaySelect.config = 0

    # attributes
    self.obj600.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj600.attributes.setValue(lcobj2)

    # cardinality
    self.obj600.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj600.cardinality.setValue(lcobj2)

    # display
    self.obj600.display.setValue('Multiplicities:\n  - To OrgUnit: 1 to N\n  - From OrgUnit: 1 to N\n')
    self.obj600.display.setHeight(15)

    # Actions
    self.obj600.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj600.Actions.setValue(lcobj2)

    # Constraints
    self.obj600.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj600.Constraints.setValue(lcobj2)

    self.obj600.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1113.0,79.0,self.obj600)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj600.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj600)
    self.globalAndLocalPostcondition(self.obj600, rootNode)
    self.obj600.postAction( rootNode.CREATE )

    self.obj601=CD_Association3(self)
    self.obj601.isGraphObjectVisual = True

    if(hasattr(self.obj601, '_setHierarchicalLink')):
      self.obj601._setHierarchicalLink(True)

    # QOCA
    self.obj601.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj601.Graphical_Appearance.setValue( ('isPartOfRole', self.obj601))
    self.obj601.Graphical_Appearance.linkInfo=linkEditor(self,self.obj601.Graphical_Appearance.semObject, "isPartOfRole")
    self.obj601.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj601.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj601.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj601.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj601.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj601.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj601.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj601.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj601.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfRole_1stLink', self.obj601.Graphical_Appearance.linkInfo.FirstLink))
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfRole_1stSegment', self.obj601.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj601.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj601.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfRole_Center', self.obj601.Graphical_Appearance.linkInfo))
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfRole_2ndSegment', self.obj601.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],0,0)
    self.obj601.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj601.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj601.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj601.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj601.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj601.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj601.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj601.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj601.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfRole_2ndLink', self.obj601.Graphical_Appearance.linkInfo.SecondLink))
    self.obj601.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj601.Graphical_Appearance.semObject
    self.obj601.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj601.Graphical_Appearance.semObject
    self.obj601.Graphical_Appearance.linkInfo.Center.semObject=self.obj601.Graphical_Appearance.semObject
    self.obj601.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj601.Graphical_Appearance.semObject
    self.obj601.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj601.Graphical_Appearance.semObject

    # name
    self.obj601.name.setValue('isPartOfRole')

    # displaySelect
    self.obj601.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj601.displaySelect.config = 0

    # attributes
    self.obj601.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj601.attributes.setValue(lcobj2)

    # cardinality
    self.obj601.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj601.cardinality.setValue(lcobj2)

    # display
    self.obj601.display.setValue('Multiplicities:\n  - From Role: 0 to N\n  - To Role: 0 to N\n')
    self.obj601.display.setHeight(15)

    # Actions
    self.obj601.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj601.Actions.setValue(lcobj2)

    # Constraints
    self.obj601.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj601.Constraints.setValue(lcobj2)

    self.obj601.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(675.0,160.0,self.obj601)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj601.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj601)
    self.globalAndLocalPostcondition(self.obj601, rootNode)
    self.obj601.postAction( rootNode.CREATE )

    self.obj602=CD_Inheritance3(self)
    self.obj602.isGraphObjectVisual = True

    if(hasattr(self.obj602, '_setHierarchicalLink')):
      self.obj602._setHierarchicalLink(False)

    self.obj602.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1056.21888986,1366.92763695,self.obj602)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj602.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj602)
    self.globalAndLocalPostcondition(self.obj602, rootNode)
    self.obj602.postAction( rootNode.CREATE )

    self.obj603=CD_Inheritance3(self)
    self.obj603.isGraphObjectVisual = True

    if(hasattr(self.obj603, '_setHierarchicalLink')):
      self.obj603._setHierarchicalLink(False)

    self.obj603.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1136.90914946,1358.75085967,self.obj603)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj603.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj603)
    self.globalAndLocalPostcondition(self.obj603, rootNode)
    self.obj603.postAction( rootNode.CREATE )

    self.obj604=CD_Inheritance3(self)
    self.obj604.isGraphObjectVisual = True

    if(hasattr(self.obj604, '_setHierarchicalLink')):
      self.obj604._setHierarchicalLink(False)

    self.obj604.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(152.858254695,586.846159545,self.obj604)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj604.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj604)
    self.globalAndLocalPostcondition(self.obj604, rootNode)
    self.obj604.postAction( rootNode.CREATE )

    # Connections for obj582 (graphObject_: Obj814) named OrgUnit
    self.drawConnections(
(self.obj582,self.obj591,[1368.8125, 220.52459016393442, 1387.9955983980042, 65.8097262245276, 1387.9955984, 65.80972622499999],"true", 3),
(self.obj582,self.obj592,[1241.14453125, 483.0655737704918, 967.8422485527899, 481.40176688146084, 971.7601868, 527.680947659],"true", 3),
(self.obj582,self.obj594,[1241.14453125, 483.0655737704918, 997.8287423035672, 492.3266545159663, 1106.462784, 821.548234957],"true", 3),
(self.obj582,self.obj600,[1241.14453125, 323.8032786885246, 1130.0, 231.0, 1113.0, 79.0], 0, 3) )
    # Connections for obj583 (graphObject_: Obj815) named Role
    self.drawConnections(
(self.obj583,self.obj593,[660.0, 811.0, 541.1631302538499, 883.356649681594, 503.161248615, 952.001803815],"true", 3),
(self.obj583,self.obj594,[832.921875, 735.2622950819672, 1023.5805784296024, 714.1457487347751, 1106.462784, 821.548234957],"true", 3),
(self.obj583,self.obj596,[620.953125, 538.344262295082, 522.0012232889502, 553.7739542825374, 436.73445957, 632.859445861],"true", 3),
(self.obj583,self.obj597,[832.921875, 432.3114754098361, 1044.0, 340.0], 0, 2),
(self.obj583,self.obj598,[793.875, 280.8360655737705, 933.0, 176.0], 0, 2),
(self.obj583,self.obj599,[620.953125, 432.3114754098361, 470.4921875, 411.163934426], 0, 2),
(self.obj583,self.obj601,[660.0, 280.8360655737705, 675.0, 160.0],"true", 2) )
    # Connections for obj584 (graphObject_: Obj816) named Action
    self.drawConnections(
 )
    # Connections for obj585 (graphObject_: Obj817) named KnowledgeArtifacts
    self.drawConnections(
 )
    # Connections for obj586 (graphObject_: Obj818) named OrganisationalKnArt
    self.drawConnections(
(self.obj586,self.obj602,[935.5703125, 1206.090909090909, 1056.21888986, 1366.92763695],"true", 2) )
    # Connections for obj587 (graphObject_: Obj819) named IndividualKnArt
    self.drawConnections(
(self.obj587,self.obj603,[1240.7421875, 1186.090909090909, 1136.90914946, 1358.75085967],"true", 2) )
    # Connections for obj588 (graphObject_: Obj820) named Strategy
    self.drawConnections(
 )
    # Connections for obj589 (graphObject_: Obj821) named Objective
    self.drawConnections(
(self.obj589,self.obj604,[139.75, 629.4918032786885, 152.858254695, 586.846159545],"true", 2),
(self.obj589,self.obj595,[139.75, 803.0, 131.94404651894035, 946.9122308488277, 131.944046519, 946.91223085],"true", 3) )
    # Connections for obj590 (graphObject_: Obj822) named Process
    self.drawConnections(
(self.obj590,self.obj596,[324.0, 283.0, 333.0, 453.0, 436.73445957, 632.859445861],"true", 3) )
    # Connections for obj591 (graphObject_: Obj823) named isPartOfOrgUnit
    self.drawConnections(
(self.obj591,self.obj582,[1387.9955984, 65.80972622499999, 1387.9955983980042, 65.8097262245276, 1368.8125, 220.52459016393442],"true", 3) )
    # Connections for obj592 (graphObject_: Obj825) named canHaveRole
    self.drawConnections(
(self.obj592,self.obj583,[971.7601868, 527.680947659, 975.67812505129, 573.9601284363068, 832.921875, 538.344262295082],"true", 3) )
    # Connections for obj593 (graphObject_: Obj827) named hasActions
    self.drawConnections(
(self.obj593,self.obj584,[503.161248615, 952.001803815, 465.1593669760688, 1020.6469579482074, 741.20703125, 946.0909090909091],"true", 3) )
    # Connections for obj594 (graphObject_: Obj829) named canAccessKnArt
    self.drawConnections(
(self.obj594,self.obj586,[1106.462784, 821.548234957, 1128.2678325033444, 887.9439489105719, 935.5703125, 1122.4545454545455],"true", 3),
(self.obj594,self.obj587,[1106.462784, 821.548234957, 1033.4035107781324, 923.4763808302594, 1240.7421875, 1102.4545454545455],"true", 3) )
    # Connections for obj595 (graphObject_: Obj831) named isPartOfObjective
    self.drawConnections(
(self.obj595,self.obj589,[131.944046519, 946.91223085, 131.94404651894035, 946.9122308488277, 139.75, 803.0],"true", 3) )
    # Connections for obj596 (graphObject_: Obj833) named hasObjective
    self.drawConnections(
(self.obj596,self.obj589,[436.73445957, 632.859445861, 351.4676958509182, 711.9449374392455, 281.65625, 698.8950819672131],"true", 3) )
    # Connections for obj597 (graphObject_: Obj835) named genericAssociation
    self.drawConnections(
(self.obj597,self.obj583,[1044.0, 340.0, 832.921875, 432.3114754098361], 0, 2) )
    # Connections for obj598 (graphObject_: Obj837) named answersToRole
    self.drawConnections(
(self.obj598,self.obj583,[933.0, 176.0, 793.875, 280.8360655737705], 0, 2) )
    # Connections for obj599 (graphObject_: Obj839) named canStartProcess
    self.drawConnections(
(self.obj599,self.obj590,[470.4921875, 411.163934426, 471.65625, 283.0], 0, 2) )
    # Connections for obj600 (graphObject_: Obj841) named answersToOrgUnit
    self.drawConnections(
(self.obj600,self.obj582,[1113.0, 79.0, 1279.0, 145.0, 1280.0, 220.52459016393442], 0, 3) )
    # Connections for obj601 (graphObject_: Obj843) named isPartOfRole
    self.drawConnections(
(self.obj601,self.obj583,[675.0, 160.0, 660.0, 280.8360655737705],"true", 2) )
    # Connections for obj602 (graphObject_: Obj845) of type CD_Inheritance3
    self.drawConnections(
(self.obj602,self.obj585,[1056.21888986, 1366.92763695, 1073.0, 1255.0],"true", 2) )
    # Connections for obj603 (graphObject_: Obj847) of type CD_Inheritance3
    self.drawConnections(
(self.obj603,self.obj585,[1136.90914946, 1358.75085967, 1153.0, 1255.0],"true", 2) )
    # Connections for obj604 (graphObject_: Obj849) of type CD_Inheritance3
    self.drawConnections(
(self.obj604,self.obj588,[152.858254695, 586.846159545, 156.0, 487.0],"true", 2) )

newfunction = LSMASOMM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
