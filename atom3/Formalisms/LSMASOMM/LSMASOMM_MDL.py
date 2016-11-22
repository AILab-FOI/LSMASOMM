"""
__LSMASOMM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Tue Nov 22 17:27:43 2016
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


    self.obj26=CD_Class3(self)
    self.obj26.isGraphObjectVisual = True

    if(hasattr(self.obj26, '_setHierarchicalLink')):
      self.obj26._setHierarchicalLink(False)

    # QOCA
    self.obj26.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj26.Graphical_Appearance.setValue( ('OrgUnit', self.obj26))

    # name
    self.obj26.name.setValue('OrgUnit')

    # attributes
    self.obj26.attributes.setActionFlags([ 1, 1, 1, 0])
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
    cobj2.setValue(('UnitSize', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('Individual', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('hasActions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj3=ATOM3String('ChangeRole', 20)
    lcobj3.append(cobj3)
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('orgUnitName', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj26.attributes.setValue(lcobj2)

    # Abstract
    self.obj26.Abstract.setValue((None, 0))
    self.obj26.Abstract.config = 0

    # cardinality
    self.obj26.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj26.cardinality.setValue(lcobj2)

    # display
    self.obj26.display.setValue('Attributes:\n  - ID :: String\n  - Individual :: Boolean\n  - UnitSize :: String\n  - hasActions :: List\n  - name :: String\nConstraints:\n  > ConstraintOutputOrgUnit\nActions:\n  > determineSize\n  > setNodeID\nMultiplicities:\n  - To isPartOfOrgUnit: 0 to N\n  - From isPartOfOrgUnit: 0 to N\n  - To canHaveRole: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To answersToOrgUnit: 0 to N\n  - From answersToOrgUnit: 0 to N\n')
    self.obj26.display.setHeight(15)

    # Actions
    self.obj26.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('determineSize', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitDetermineSize(self)\nself.UnitSize.setValue(res)\nself.graphObject_.ModifyAttribute(\'UnitSize\', res)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n'))
    lcobj2.append(cobj2)
    self.obj26.Actions.setValue(lcobj2)

    # Constraints
    self.obj26.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintOutputOrgUnit', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitCheckOutputs(self)\nif res is "manyKnArts":\n    return ("OrgUnit can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj26.Constraints.setValue(lcobj2)

    self.obj26.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,220.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.88
       new_obj.layConstraints['scale'] = [1.11015625, 3.098360655737705]
    else: new_obj = None
    self.obj26.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)
    self.obj26.postAction( rootNode.CREATE )

    self.obj27=CD_Class3(self)
    self.obj27.isGraphObjectVisual = True

    if(hasattr(self.obj27, '_setHierarchicalLink')):
      self.obj27._setHierarchicalLink(False)

    # QOCA
    self.obj27.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj27.Graphical_Appearance.setValue( ('Role', self.obj27))

    # name
    self.obj27.name.setValue('Role')

    # attributes
    self.obj27.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('RoleID', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('hasActions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
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
    self.obj27.attributes.setValue(lcobj2)

    # Abstract
    self.obj27.Abstract.setValue((None, 0))
    self.obj27.Abstract.config = 0

    # cardinality
    self.obj27.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj27.cardinality.setValue(lcobj2)

    # display
    self.obj27.display.setValue('Attributes:\n  - ID :: String\n  - hasActions :: List\n  - isMetaRole :: Boolean\n  - name :: String\nConstraints:\n  > RoleConstraintKnArt\nActions:\n  > checkMetaRole\n  > setNodeID\nMultiplicities:\n  - From canHaveRole: 0 to N\n  - To hasActions: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To hasObjective: 0 to N\n  - To genericAssociation: 0 to N\n  - From genericAssociation: 0 to N\n  - To answersToRole: 0 to N\n  - From answersToRole: 0 to N\n  - To canStartProcess: 0 to N\n  - To isPartOfRole: 0 to N\n  - From isPartOfRole: 0 to N\n')
    self.obj27.display.setHeight(15)

    # Actions
    self.obj27.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('checkMetaRole', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]), 'from CustomCode import RoleHierarchy\nres = RoleHierarchy(self)\nself.isMetaRole.setValue((\'isMetaRole\',res))\nself.graphObject_.ModifyAttribute(\'isMetaRole\', res)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n\n'))
    lcobj2.append(cobj2)
    self.obj27.Actions.setValue(lcobj2)

    # Constraints
    self.obj27.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('RoleConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '\nfrom CustomCode import *\n\nres = RoleCheckOutputs(self)\nif res is "manyKnArts":\n    return ("Roles can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelif res is "IndivKnArtError":\n    return ("Roles can have OrganizationalKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj27.Constraints.setValue(lcobj2)

    self.obj27.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(620.0,260.0,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.115625, 3.7868852459016393]
    else: new_obj = None
    self.obj27.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)
    self.obj27.postAction( rootNode.CREATE )

    self.obj28=CD_Class3(self)
    self.obj28.isGraphObjectVisual = True

    if(hasattr(self.obj28, '_setHierarchicalLink')):
      self.obj28._setHierarchicalLink(False)

    # QOCA
    self.obj28.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj28.Graphical_Appearance.setValue( ('Action', self.obj28))

    # name
    self.obj28.name.setValue('Action')

    # attributes
    self.obj28.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj28.attributes.setValue(lcobj2)

    # Abstract
    self.obj28.Abstract.setValue((None, 0))
    self.obj28.Abstract.config = 0

    # cardinality
    self.obj28.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasActions', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj28.cardinality.setValue(lcobj2)

    # display
    self.obj28.display.setValue('Attributes:\n  - ActionCode :: Text\n  - name :: String\nMultiplicities:\n  - From hasActions: 0 to N\n')
    self.obj28.display.setHeight(15)

    # Actions
    self.obj28.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj28.Actions.setValue(lcobj2)

    # Constraints
    self.obj28.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj28.Constraints.setValue(lcobj2)

    self.obj28.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(740.0,820.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.06
       new_obj.layConstraints['scale'] = [1.02265625, 1.0454545454545454]
    else: new_obj = None
    self.obj28.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)
    self.obj28.postAction( rootNode.CREATE )

    self.obj29=CD_Class3(self)
    self.obj29.isGraphObjectVisual = True

    if(hasattr(self.obj29, '_setHierarchicalLink')):
      self.obj29._setHierarchicalLink(False)

    # QOCA
    self.obj29.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj29.Graphical_Appearance.setValue( ('KnowledgeArtifacts', self.obj29))

    # name
    self.obj29.name.setValue('KnowledgeArtifacts')

    # attributes
    self.obj29.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj29.attributes.setValue(lcobj2)

    # Abstract
    self.obj29.Abstract.setValue((None, 1))
    self.obj29.Abstract.config = 0

    # cardinality
    self.obj29.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj29.cardinality.setValue(lcobj2)

    # display
    self.obj29.display.setValue('Attributes:\n  - ID :: String\n  - description :: String\n  - name :: String\nActions:\n  > setNodeID\n')
    self.obj29.display.setHeight(15)

    # Actions
    self.obj29.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n'))
    lcobj2.append(cobj2)
    self.obj29.Actions.setValue(lcobj2)

    # Constraints
    self.obj29.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj29.Constraints.setValue(lcobj2)

    self.obj29.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(980.0,1080.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.239344262295082]
    else: new_obj = None
    self.obj29.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.obj29.postAction( rootNode.CREATE )

    self.obj30=CD_Class3(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # QOCA
    self.obj30.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj30.Graphical_Appearance.setValue( ('OrganisationalKnArt', self.obj30))

    # name
    self.obj30.name.setValue('OrganisationalKnArt')

    # attributes
    self.obj30.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj30.attributes.setValue(lcobj2)

    # Abstract
    self.obj30.Abstract.setValue((None, 0))
    self.obj30.Abstract.config = 0

    # cardinality
    self.obj30.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj30.cardinality.setValue(lcobj2)

    # display
    self.obj30.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj30.display.setHeight(15)

    # Actions
    self.obj30.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj30.Actions.setValue(lcobj2)

    # Constraints
    self.obj30.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj30.Constraints.setValue(lcobj2)

    self.obj30.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(700.0,1080.0,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj31=CD_Class3(self)
    self.obj31.isGraphObjectVisual = True

    if(hasattr(self.obj31, '_setHierarchicalLink')):
      self.obj31._setHierarchicalLink(False)

    # QOCA
    self.obj31.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj31.Graphical_Appearance.setValue( ('IndividualKnArt', self.obj31))

    # name
    self.obj31.name.setValue('IndividualKnArt')

    # attributes
    self.obj31.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj31.attributes.setValue(lcobj2)

    # Abstract
    self.obj31.Abstract.setValue((None, 0))
    self.obj31.Abstract.config = 0

    # cardinality
    self.obj31.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj31.cardinality.setValue(lcobj2)

    # display
    self.obj31.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj31.display.setHeight(15)

    # Actions
    self.obj31.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj31.Actions.setValue(lcobj2)

    # Constraints
    self.obj31.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj31.Constraints.setValue(lcobj2)

    self.obj31.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,1060.0,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj31.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)
    self.obj31.postAction( rootNode.CREATE )

    self.obj32=CD_Class3(self)
    self.obj32.isGraphObjectVisual = True

    if(hasattr(self.obj32, '_setHierarchicalLink')):
      self.obj32._setHierarchicalLink(False)

    # QOCA
    self.obj32.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj32.Graphical_Appearance.setValue( ('Strategy', self.obj32))

    # name
    self.obj32.name.setValue('Strategy')

    # attributes
    self.obj32.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj32.attributes.setValue(lcobj2)

    # Abstract
    self.obj32.Abstract.setValue((None, 1))
    self.obj32.Abstract.config = 0

    # cardinality
    self.obj32.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj32.cardinality.setValue(lcobj2)

    # display
    self.obj32.display.setValue('Attributes:\n  - ID :: String\n  - description :: Text\n  - name :: String\nActions:\n  > setNodeID\n')
    self.obj32.display.setHeight(15)

    # Actions
    self.obj32.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n'))
    lcobj2.append(cobj2)
    self.obj32.Actions.setValue(lcobj2)

    # Constraints
    self.obj32.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj32.Constraints.setValue(lcobj2)

    self.obj32.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(80.0,320.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.239344262295082]
    else: new_obj = None
    self.obj32.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.obj32.postAction( rootNode.CREATE )

    self.obj33=CD_Class3(self)
    self.obj33.isGraphObjectVisual = True

    if(hasattr(self.obj33, '_setHierarchicalLink')):
      self.obj33._setHierarchicalLink(False)

    # QOCA
    self.obj33.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj33.Graphical_Appearance.setValue( ('Objective', self.obj33))

    # name
    self.obj33.name.setValue('Objective')

    # attributes
    self.obj33.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj33.attributes.setValue(lcobj2)

    # Abstract
    self.obj33.Abstract.setValue((None, 0))
    self.obj33.Abstract.config = 0

    # cardinality
    self.obj33.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj33.cardinality.setValue(lcobj2)

    # display
    self.obj33.display.setValue('Attributes:\n  - Measurement :: Text\n  - Reward :: Text\nMultiplicities:\n  - To isPartOfObjective: 0 to N\n  - From isPartOfObjective: 0 to N\n  - From hasObjective: 0 to N\n')
    self.obj33.display.setHeight(15)

    # Actions
    self.obj33.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj33.Actions.setValue(lcobj2)

    # Constraints
    self.obj33.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj33.Constraints.setValue(lcobj2)

    self.obj33.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(40.0,600.0,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.26875, 1.4459016393442625]
    else: new_obj = None
    self.obj33.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)
    self.obj33.postAction( rootNode.CREATE )

    self.obj34=CD_Class3(self)
    self.obj34.isGraphObjectVisual = True

    if(hasattr(self.obj34, '_setHierarchicalLink')):
      self.obj34._setHierarchicalLink(False)

    # QOCA
    self.obj34.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj34.Graphical_Appearance.setValue( ('Process', self.obj34))

    # name
    self.obj34.name.setValue('Process')

    # attributes
    self.obj34.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj34.attributes.setValue(lcobj2)

    # Abstract
    self.obj34.Abstract.setValue((None, 0))
    self.obj34.Abstract.config = 0

    # cardinality
    self.obj34.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canStartProcess', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasObjective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj34.cardinality.setValue(lcobj2)

    # display
    self.obj34.display.setValue('Attributes:\n  - Activities :: Text\n  - Name :: String\nMultiplicities:\n  - From canStartProcess: 0 to N\n  - To hasObjective: 0 to N\n')
    self.obj34.display.setHeight(15)

    # Actions
    self.obj34.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj34.Actions.setValue(lcobj2)

    # Constraints
    self.obj34.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj34.Constraints.setValue(lcobj2)

    self.obj34.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(280.0,80.0,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.23046875, 1.239344262295082]
    else: new_obj = None
    self.obj34.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)
    self.obj34.postAction( rootNode.CREATE )

    self.obj35=CD_Association3(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(True)

    # QOCA
    self.obj35.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj35.Graphical_Appearance.setValue( ('isPartOfOrgUnit', self.obj35))
    self.obj35.Graphical_Appearance.linkInfo=linkEditor(self,self.obj35.Graphical_Appearance.semObject, "isPartOfOrgUnit")
    self.obj35.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj35.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj35.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj35.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj35.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj35.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj35.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj35.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj35.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfOrgUnit_1stLink', self.obj35.Graphical_Appearance.linkInfo.FirstLink))
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfOrgUnit_1stSegment', self.obj35.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj35.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj35.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfOrgUnit_Center', self.obj35.Graphical_Appearance.linkInfo))
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfOrgUnit_2ndSegment', self.obj35.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj35.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj35.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj35.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj35.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj35.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj35.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj35.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj35.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj35.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfOrgUnit_2ndLink', self.obj35.Graphical_Appearance.linkInfo.SecondLink))
    self.obj35.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj35.Graphical_Appearance.semObject
    self.obj35.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj35.Graphical_Appearance.semObject
    self.obj35.Graphical_Appearance.linkInfo.Center.semObject=self.obj35.Graphical_Appearance.semObject
    self.obj35.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj35.Graphical_Appearance.semObject
    self.obj35.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj35.Graphical_Appearance.semObject

    # name
    self.obj35.name.setValue('isPartOfOrgUnit')

    # displaySelect
    self.obj35.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj35.displaySelect.config = 0

    # attributes
    self.obj35.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj35.attributes.setValue(lcobj2)

    # cardinality
    self.obj35.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj35.cardinality.setValue(lcobj2)

    # display
    self.obj35.display.setValue('Multiplicities:\n  - From OrgUnit: 1 to N\n  - To OrgUnit: 1 to N\n')
    self.obj35.display.setHeight(15)

    # Actions
    self.obj35.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj35.Actions.setValue(lcobj2)

    # Constraints
    self.obj35.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj35.Constraints.setValue(lcobj2)

    self.obj35.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1387.9955984,65.809726225,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=CD_Association3(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(True)

    # QOCA
    self.obj36.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj36.Graphical_Appearance.setValue( ('canHaveRole', self.obj36))
    self.obj36.Graphical_Appearance.linkInfo=linkEditor(self,self.obj36.Graphical_Appearance.semObject, "canHaveRole")
    self.obj36.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj36.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj36.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj36.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj36.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj36.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj36.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj36.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj36.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canHaveRole_1stLink', self.obj36.Graphical_Appearance.linkInfo.FirstLink))
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canHaveRole_1stSegment', self.obj36.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj36.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj36.Graphical_Appearance.linkInfo.Center.setValue( ('canHaveRole_Center', self.obj36.Graphical_Appearance.linkInfo))
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canHaveRole_2ndSegment', self.obj36.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj36.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj36.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj36.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj36.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj36.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj36.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj36.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj36.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj36.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canHaveRole_2ndLink', self.obj36.Graphical_Appearance.linkInfo.SecondLink))
    self.obj36.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj36.Graphical_Appearance.semObject
    self.obj36.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj36.Graphical_Appearance.semObject
    self.obj36.Graphical_Appearance.linkInfo.Center.semObject=self.obj36.Graphical_Appearance.semObject
    self.obj36.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj36.Graphical_Appearance.semObject
    self.obj36.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj36.Graphical_Appearance.semObject

    # name
    self.obj36.name.setValue('canHaveRole')

    # displaySelect
    self.obj36.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj36.displaySelect.config = 0

    # attributes
    self.obj36.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj36.attributes.setValue(lcobj2)

    # cardinality
    self.obj36.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj36.cardinality.setValue(lcobj2)

    # display
    self.obj36.display.setValue('Multiplicities:\n  - From OrgUnit: 0 to N\n  - To Role: 0 to N\n')
    self.obj36.display.setHeight(15)

    # Actions
    self.obj36.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj36.Actions.setValue(lcobj2)

    # Constraints
    self.obj36.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj36.Constraints.setValue(lcobj2)

    self.obj36.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(971.7601868,527.680947659,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=CD_Association3(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # QOCA
    self.obj37.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj37.Graphical_Appearance.setValue( ('hasActions', self.obj37))
    self.obj37.Graphical_Appearance.linkInfo=linkEditor(self,self.obj37.Graphical_Appearance.semObject, "hasActions")
    self.obj37.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj37.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj37.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj37.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj37.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj37.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj37.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj37.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj37.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasActions_1stLink', self.obj37.Graphical_Appearance.linkInfo.FirstLink))
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasActions_1stSegment', self.obj37.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj37.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj37.Graphical_Appearance.linkInfo.Center.setValue( ('hasActions_Center', self.obj37.Graphical_Appearance.linkInfo))
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasActions_2ndSegment', self.obj37.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj37.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj37.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj37.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj37.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj37.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj37.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj37.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj37.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj37.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasActions_2ndLink', self.obj37.Graphical_Appearance.linkInfo.SecondLink))
    self.obj37.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj37.Graphical_Appearance.semObject
    self.obj37.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj37.Graphical_Appearance.semObject
    self.obj37.Graphical_Appearance.linkInfo.Center.semObject=self.obj37.Graphical_Appearance.semObject
    self.obj37.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj37.Graphical_Appearance.semObject
    self.obj37.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj37.Graphical_Appearance.semObject

    # name
    self.obj37.name.setValue('hasActions')

    # displaySelect
    self.obj37.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj37.displaySelect.config = 0

    # attributes
    self.obj37.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj37.attributes.setValue(lcobj2)

    # cardinality
    self.obj37.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Action', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    self.obj37.cardinality.setValue(lcobj2)

    # display
    self.obj37.display.setValue('Multiplicities:\n  - To Action: 1 to N\n  - From Role: 1 to 1\n')
    self.obj37.display.setHeight(15)

    # Actions
    self.obj37.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj37.Actions.setValue(lcobj2)

    # Constraints
    self.obj37.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj37.Constraints.setValue(lcobj2)

    self.obj37.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(503.161248615,952.001803815,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj38=CD_Association3(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # QOCA
    self.obj38.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj38.Graphical_Appearance.setValue( ('canAccessKnArt', self.obj38))
    self.obj38.Graphical_Appearance.linkInfo=linkEditor(self,self.obj38.Graphical_Appearance.semObject, "canAccessKnArt")
    self.obj38.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canAccessKnArt_1stLink', self.obj38.Graphical_Appearance.linkInfo.FirstLink))
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canAccessKnArt_1stSegment', self.obj38.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj38.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj38.Graphical_Appearance.linkInfo.Center.setValue( ('canAccessKnArt_Center', self.obj38.Graphical_Appearance.linkInfo))
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canAccessKnArt_2ndSegment', self.obj38.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj38.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canAccessKnArt_2ndLink', self.obj38.Graphical_Appearance.linkInfo.SecondLink))
    self.obj38.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj38.Graphical_Appearance.semObject
    self.obj38.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj38.Graphical_Appearance.semObject
    self.obj38.Graphical_Appearance.linkInfo.Center.semObject=self.obj38.Graphical_Appearance.semObject
    self.obj38.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj38.Graphical_Appearance.semObject
    self.obj38.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj38.Graphical_Appearance.semObject

    # name
    self.obj38.name.setValue('canAccessKnArt')

    # displaySelect
    self.obj38.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj38.displaySelect.config = 0

    # attributes
    self.obj38.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj38.attributes.setValue(lcobj2)

    # cardinality
    self.obj38.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj38.cardinality.setValue(lcobj2)

    # display
    self.obj38.display.setValue('Constraints:\n  > ConstraintKnArt\nMultiplicities:\n  - To OrganisationalKnArt: 0 to N\n  - From Role: 0 to N\n  - From OrgUnit: 0 to N\n  - To IndividualKnArt: 0 to N\n')
    self.obj38.display.setHeight(15)

    # Actions
    self.obj38.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj38.Actions.setValue(lcobj2)

    # Constraints
    self.obj38.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = canAccessKnArtCheckConnections(self)\n\nif res is "eitherRoleOrUnit":\n    return ("Either Role of OrgUnit can access knowledge.", self.graphObject_)\nelif res is "onlyOneInput":\n    return ("Only one Role or OrgUnit can access one knowledge medium.", self.graphObject_)\nelif res is "RoleWithOrgOnly":\n    return ("Role can access OrganisationalKnArt only!", self.graphObject_)\nelif res is "OrgUnitWithIndivOnly":\n    return ("OrgUnit can access IndividualKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj38.Constraints.setValue(lcobj2)

    self.obj38.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1106.462784,821.548234957,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.6380000000000001, 1.8967741935483875]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=CD_Association3(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(True)

    # QOCA
    self.obj39.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj39.Graphical_Appearance.setValue( ('isPartOfObjective', self.obj39))
    self.obj39.Graphical_Appearance.linkInfo=linkEditor(self,self.obj39.Graphical_Appearance.semObject, "isPartOfObjective")
    self.obj39.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfObjective_1stLink', self.obj39.Graphical_Appearance.linkInfo.FirstLink))
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfObjective_1stSegment', self.obj39.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj39.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfObjective_Center', self.obj39.Graphical_Appearance.linkInfo))
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfObjective_2ndSegment', self.obj39.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfObjective_2ndLink', self.obj39.Graphical_Appearance.linkInfo.SecondLink))
    self.obj39.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.Center.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj39.Graphical_Appearance.semObject
    self.obj39.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj39.Graphical_Appearance.semObject

    # name
    self.obj39.name.setValue('isPartOfObjective')

    # displaySelect
    self.obj39.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj39.displaySelect.config = 0

    # attributes
    self.obj39.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj39.attributes.setValue(lcobj2)

    # cardinality
    self.obj39.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj39.cardinality.setValue(lcobj2)

    # display
    self.obj39.display.setValue('Multiplicities:\n  - From Objective: 0 to N\n  - To Objective: 0 to N\n')
    self.obj39.display.setHeight(15)

    # Actions
    self.obj39.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj39.Actions.setValue(lcobj2)

    # Constraints
    self.obj39.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj39.Constraints.setValue(lcobj2)

    self.obj39.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(131.944046519,946.91223085,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.225, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=CD_Association3(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # QOCA
    self.obj40.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj40.Graphical_Appearance.setValue( ('hasObjective', self.obj40))
    self.obj40.Graphical_Appearance.linkInfo=linkEditor(self,self.obj40.Graphical_Appearance.semObject, "hasObjective")
    self.obj40.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasObjective_1stLink', self.obj40.Graphical_Appearance.linkInfo.FirstLink))
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasObjective_1stSegment', self.obj40.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj40.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.Center.setValue( ('hasObjective_Center', self.obj40.Graphical_Appearance.linkInfo))
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasObjective_2ndSegment', self.obj40.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasObjective_2ndLink', self.obj40.Graphical_Appearance.linkInfo.SecondLink))
    self.obj40.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.Center.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj40.Graphical_Appearance.semObject
    self.obj40.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj40.Graphical_Appearance.semObject

    # name
    self.obj40.name.setValue('hasObjective')

    # displaySelect
    self.obj40.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj40.displaySelect.config = 0

    # attributes
    self.obj40.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj40.attributes.setValue(lcobj2)

    # cardinality
    self.obj40.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj40.cardinality.setValue(lcobj2)

    # display
    self.obj40.display.setValue('Multiplicities:\n  - To Objective: 1 to N\n  - From Role: 0 to N\n  - From Process: 0 to N\n')
    self.obj40.display.setHeight(15)

    # Actions
    self.obj40.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj40.Actions.setValue(lcobj2)

    # Constraints
    self.obj40.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj40.Constraints.setValue(lcobj2)

    self.obj40.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(436.73445957,632.859445861,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.1620000000000001, 1.0838709677419356]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=CD_Association3(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # QOCA
    self.obj41.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj41.Graphical_Appearance.setValue( ('genericAssociation', self.obj41))
    self.obj41.Graphical_Appearance.linkInfo=linkEditor(self,self.obj41.Graphical_Appearance.semObject, "genericAssociation")
    self.obj41.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('genericAssociation_1stLink', self.obj41.Graphical_Appearance.linkInfo.FirstLink))
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('genericAssociation_1stSegment', self.obj41.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj41.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.Center.setValue( ('genericAssociation_Center', self.obj41.Graphical_Appearance.linkInfo))
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('genericAssociation_2ndSegment', self.obj41.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('genericAssociation_2ndLink', self.obj41.Graphical_Appearance.linkInfo.SecondLink))
    self.obj41.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.Center.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj41.Graphical_Appearance.semObject
    self.obj41.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj41.Graphical_Appearance.semObject

    # name
    self.obj41.name.setValue('genericAssociation')

    # displaySelect
    self.obj41.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj41.displaySelect.config = 0

    # attributes
    self.obj41.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj41.attributes.setValue(lcobj2)

    # cardinality
    self.obj41.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj41.cardinality.setValue(lcobj2)

    # display
    self.obj41.display.setValue('Attributes:\n  - Name :: String\n  - Description :: Text\nMultiplicities:\n  - To Role: 1 to N\n  - From Role: 1 to N\n')
    self.obj41.display.setHeight(15)

    # Actions
    self.obj41.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj41.Actions.setValue(lcobj2)

    # Constraints
    self.obj41.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj41.Constraints.setValue(lcobj2)

    self.obj41.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1044.0,340.0,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.015, 1.6258064516129034]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=CD_Association3(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(True)

    # QOCA
    self.obj42.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj42.Graphical_Appearance.setValue( ('answersToRole', self.obj42))
    self.obj42.Graphical_Appearance.linkInfo=linkEditor(self,self.obj42.Graphical_Appearance.semObject, "answersToRole")
    self.obj42.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToRole_1stLink', self.obj42.Graphical_Appearance.linkInfo.FirstLink))
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToRole_1stSegment', self.obj42.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj42.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj42.Graphical_Appearance.linkInfo.Center.setValue( ('answersToRole_Center', self.obj42.Graphical_Appearance.linkInfo))
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToRole_2ndSegment', self.obj42.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj42.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToRole_2ndLink', self.obj42.Graphical_Appearance.linkInfo.SecondLink))
    self.obj42.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj42.Graphical_Appearance.semObject
    self.obj42.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj42.Graphical_Appearance.semObject
    self.obj42.Graphical_Appearance.linkInfo.Center.semObject=self.obj42.Graphical_Appearance.semObject
    self.obj42.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj42.Graphical_Appearance.semObject
    self.obj42.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj42.Graphical_Appearance.semObject

    # name
    self.obj42.name.setValue('answersToRole')

    # displaySelect
    self.obj42.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj42.displaySelect.config = 0

    # attributes
    self.obj42.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj42.attributes.setValue(lcobj2)

    # cardinality
    self.obj42.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj42.cardinality.setValue(lcobj2)

    # display
    self.obj42.display.setValue('Multiplicities:\n  - From Role: 1 to N\n  - To Role: 1 to N\n')
    self.obj42.display.setHeight(15)

    # Actions
    self.obj42.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj42.Actions.setValue(lcobj2)

    # Constraints
    self.obj42.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj42.Constraints.setValue(lcobj2)

    self.obj42.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(933.0,176.0,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=CD_Association3(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # QOCA
    self.obj43.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj43.Graphical_Appearance.setValue( ('canStartProcess', self.obj43))
    self.obj43.Graphical_Appearance.linkInfo=linkEditor(self,self.obj43.Graphical_Appearance.semObject, "canStartProcess")
    self.obj43.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canStartProcess_1stLink', self.obj43.Graphical_Appearance.linkInfo.FirstLink))
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canStartProcess_1stSegment', self.obj43.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj43.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj43.Graphical_Appearance.linkInfo.Center.setValue( ('canStartProcess_Center', self.obj43.Graphical_Appearance.linkInfo))
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canStartProcess_2ndSegment', self.obj43.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj43.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canStartProcess_2ndLink', self.obj43.Graphical_Appearance.linkInfo.SecondLink))
    self.obj43.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj43.Graphical_Appearance.semObject
    self.obj43.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj43.Graphical_Appearance.semObject
    self.obj43.Graphical_Appearance.linkInfo.Center.semObject=self.obj43.Graphical_Appearance.semObject
    self.obj43.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj43.Graphical_Appearance.semObject
    self.obj43.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj43.Graphical_Appearance.semObject

    # name
    self.obj43.name.setValue('canStartProcess')

    # displaySelect
    self.obj43.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj43.displaySelect.config = 0

    # attributes
    self.obj43.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj43.attributes.setValue(lcobj2)

    # cardinality
    self.obj43.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Process', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj43.cardinality.setValue(lcobj2)

    # display
    self.obj43.display.setValue('Multiplicities:\n  - To Process: 0 to N\n  - From Role: 0 to N\n')
    self.obj43.display.setHeight(15)

    # Actions
    self.obj43.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj43.Actions.setValue(lcobj2)

    # Constraints
    self.obj43.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj43.Constraints.setValue(lcobj2)

    self.obj43.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(470.4921875,411.163934426,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.036, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=CD_Association3(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(True)

    # QOCA
    self.obj44.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj44.Graphical_Appearance.setValue( ('answersToOrgUnit', self.obj44))
    self.obj44.Graphical_Appearance.linkInfo=linkEditor(self,self.obj44.Graphical_Appearance.semObject, "answersToOrgUnit")
    self.obj44.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToOrgUnit_1stLink', self.obj44.Graphical_Appearance.linkInfo.FirstLink))
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToOrgUnit_1stSegment', self.obj44.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj44.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj44.Graphical_Appearance.linkInfo.Center.setValue( ('answersToOrgUnit_Center', self.obj44.Graphical_Appearance.linkInfo))
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToOrgUnit_2ndSegment', self.obj44.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj44.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToOrgUnit_2ndLink', self.obj44.Graphical_Appearance.linkInfo.SecondLink))
    self.obj44.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj44.Graphical_Appearance.semObject
    self.obj44.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj44.Graphical_Appearance.semObject
    self.obj44.Graphical_Appearance.linkInfo.Center.semObject=self.obj44.Graphical_Appearance.semObject
    self.obj44.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj44.Graphical_Appearance.semObject
    self.obj44.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj44.Graphical_Appearance.semObject

    # name
    self.obj44.name.setValue('answersToOrgUnit')

    # displaySelect
    self.obj44.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj44.displaySelect.config = 0

    # attributes
    self.obj44.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj44.attributes.setValue(lcobj2)

    # cardinality
    self.obj44.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj44.cardinality.setValue(lcobj2)

    # display
    self.obj44.display.setValue('Multiplicities:\n  - To OrgUnit: 1 to N\n  - From OrgUnit: 1 to N\n')
    self.obj44.display.setHeight(15)

    # Actions
    self.obj44.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj44.Actions.setValue(lcobj2)

    # Constraints
    self.obj44.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj44.Constraints.setValue(lcobj2)

    self.obj44.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1113.0,79.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=CD_Association3(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(True)

    # QOCA
    self.obj45.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj45.Graphical_Appearance.setValue( ('isPartOfRole', self.obj45))
    self.obj45.Graphical_Appearance.linkInfo=linkEditor(self,self.obj45.Graphical_Appearance.semObject, "isPartOfRole")
    self.obj45.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfRole_1stLink', self.obj45.Graphical_Appearance.linkInfo.FirstLink))
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfRole_1stSegment', self.obj45.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj45.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj45.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfRole_Center', self.obj45.Graphical_Appearance.linkInfo))
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfRole_2ndSegment', self.obj45.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],0,0)
    self.obj45.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfRole_2ndLink', self.obj45.Graphical_Appearance.linkInfo.SecondLink))
    self.obj45.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj45.Graphical_Appearance.semObject
    self.obj45.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj45.Graphical_Appearance.semObject
    self.obj45.Graphical_Appearance.linkInfo.Center.semObject=self.obj45.Graphical_Appearance.semObject
    self.obj45.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj45.Graphical_Appearance.semObject
    self.obj45.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj45.Graphical_Appearance.semObject

    # name
    self.obj45.name.setValue('isPartOfRole')

    # displaySelect
    self.obj45.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj45.displaySelect.config = 0

    # attributes
    self.obj45.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj45.attributes.setValue(lcobj2)

    # cardinality
    self.obj45.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj45.cardinality.setValue(lcobj2)

    # display
    self.obj45.display.setValue('Multiplicities:\n  - From Role: 0 to N\n  - To Role: 0 to N\n')
    self.obj45.display.setHeight(15)

    # Actions
    self.obj45.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj45.Actions.setValue(lcobj2)

    # Constraints
    self.obj45.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj45.Constraints.setValue(lcobj2)

    self.obj45.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(675.0,160.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=CD_Inheritance3(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    self.obj46.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1056.21888986,1366.92763695,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=CD_Inheritance3(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    self.obj47.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1136.90914946,1358.75085967,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=CD_Inheritance3(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    self.obj48.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(152.858254695,586.846159545,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=CD_Inheritance3(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    self.obj49.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(135.466796875,193.786885246,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    # Connections for obj26 (graphObject_: Obj0) named OrgUnit
    self.drawConnections(
(self.obj26,self.obj35,[1368.8125, 220.52459016393442, 1387.9955983980042, 65.8097262245276, 1387.9955984, 65.80972622499999],"true", 3),
(self.obj26,self.obj36,[1241.14453125, 515.5737704918033, 967.8422485527899, 481.40176688146084, 971.7601868, 527.680947659],"true", 3),
(self.obj26,self.obj38,[1241.14453125, 515.5737704918033, 997.8287423035672, 492.3266545159663, 1106.462784, 821.548234957],"true", 3),
(self.obj26,self.obj44,[1241.14453125, 323.8032786885246, 1130.0, 231.0, 1113.0, 79.0], 0, 3) )
    # Connections for obj27 (graphObject_: Obj1) named Role
    self.drawConnections(
(self.obj27,self.obj37,[660.0, 791.0, 541.1631302538499, 883.356649681594, 503.161248615, 952.001803815],"true", 3),
(self.obj27,self.obj38,[832.921875, 715.2622950819672, 1023.5805784296024, 714.1457487347751, 1106.462784, 821.548234957],"true", 3),
(self.obj27,self.obj40,[620.953125, 518.344262295082, 522.0012232889502, 553.7739542825374, 436.73445957, 632.859445861],"true", 3),
(self.obj27,self.obj41,[832.921875, 412.3114754098361, 1044.0, 340.0], 0, 2),
(self.obj27,self.obj42,[793.875, 260.8360655737705, 933.0, 176.0], 0, 2),
(self.obj27,self.obj43,[620.953125, 412.3114754098361, 470.4921875, 411.163934426], 0, 2),
(self.obj27,self.obj45,[660.0, 260.8360655737705, 675.0, 160.0],"true", 2) )
    # Connections for obj28 (graphObject_: Obj2) named Action
    self.drawConnections(
 )
    # Connections for obj29 (graphObject_: Obj3) named KnowledgeArtifacts
    self.drawConnections(
 )
    # Connections for obj30 (graphObject_: Obj4) named OrganisationalKnArt
    self.drawConnections(
(self.obj30,self.obj46,[935.5703125, 1206.090909090909, 1056.21888986, 1366.92763695],"true", 2) )
    # Connections for obj31 (graphObject_: Obj5) named IndividualKnArt
    self.drawConnections(
(self.obj31,self.obj47,[1240.7421875, 1186.090909090909, 1136.90914946, 1358.75085967],"true", 2) )
    # Connections for obj32 (graphObject_: Obj6) named Strategy
    self.drawConnections(
 )
    # Connections for obj33 (graphObject_: Obj7) named Objective
    self.drawConnections(
(self.obj33,self.obj48,[135.75, 600.5737704918033, 152.858254695, 586.846159545],"true", 2),
(self.obj33,self.obj39,[139.75, 803.0, 131.94404651894035, 946.9122308488277, 131.944046519, 946.91223085],"true", 3) )
    # Connections for obj34 (graphObject_: Obj8) named Process
    self.drawConnections(
(self.obj34,self.obj40,[324.0, 255.0, 333.0, 453.0, 436.73445957, 632.859445861],"true", 3),
(self.obj34,self.obj49,[280.93359375, 199.2295081967213, 135.466796875, 193.786885246],"true", 2) )
    # Connections for obj35 (graphObject_: Obj9) named isPartOfOrgUnit
    self.drawConnections(
(self.obj35,self.obj26,[1387.9955984, 65.80972622499999, 1387.9955983980042, 65.8097262245276, 1368.8125, 220.52459016393442],"true", 3) )
    # Connections for obj36 (graphObject_: Obj11) named canHaveRole
    self.drawConnections(
(self.obj36,self.obj27,[971.7601868, 527.680947659, 975.67812505129, 573.9601284363068, 832.921875, 620.5901639344263],"true", 3) )
    # Connections for obj37 (graphObject_: Obj13) named hasActions
    self.drawConnections(
(self.obj37,self.obj28,[503.161248615, 952.001803815, 465.1593669760688, 1020.6469579482074, 741.20703125, 946.0909090909091],"true", 3) )
    # Connections for obj38 (graphObject_: Obj15) named canAccessKnArt
    self.drawConnections(
(self.obj38,self.obj30,[1106.462784, 821.548234957, 1128.2678325033444, 887.9439489105719, 935.5703125, 1122.4545454545455],"true", 3),
(self.obj38,self.obj31,[1106.462784, 821.548234957, 1033.4035107781324, 923.4763808302594, 1240.7421875, 1102.4545454545455],"true", 3) )
    # Connections for obj39 (graphObject_: Obj17) named isPartOfObjective
    self.drawConnections(
(self.obj39,self.obj33,[131.944046519, 946.91223085, 131.94404651894035, 946.9122308488277, 139.75, 803.0],"true", 3) )
    # Connections for obj40 (graphObject_: Obj19) named hasObjective
    self.drawConnections(
(self.obj40,self.obj33,[436.73445957, 632.859445861, 351.4676958509182, 711.9449374392455, 281.65625, 698.8950819672131],"true", 3) )
    # Connections for obj41 (graphObject_: Obj21) named genericAssociation
    self.drawConnections(
(self.obj41,self.obj27,[1044.0, 340.0, 832.921875, 412.3114754098361], 0, 2) )
    # Connections for obj42 (graphObject_: Obj23) named answersToRole
    self.drawConnections(
(self.obj42,self.obj27,[933.0, 176.0, 793.875, 260.8360655737705], 0, 2) )
    # Connections for obj43 (graphObject_: Obj25) named canStartProcess
    self.drawConnections(
(self.obj43,self.obj34,[470.4921875, 411.163934426, 471.65625, 255.0], 0, 2) )
    # Connections for obj44 (graphObject_: Obj27) named answersToOrgUnit
    self.drawConnections(
(self.obj44,self.obj26,[1113.0, 79.0, 1279.0, 145.0, 1280.0, 220.52459016393442], 0, 3) )
    # Connections for obj45 (graphObject_: Obj29) named isPartOfRole
    self.drawConnections(
(self.obj45,self.obj27,[675.0, 160.0, 660.0, 260.8360655737705],"true", 2) )
    # Connections for obj46 (graphObject_: Obj31) of type CD_Inheritance3
    self.drawConnections(
(self.obj46,self.obj29,[1056.21888986, 1366.92763695, 1073.0, 1255.0],"true", 2) )
    # Connections for obj47 (graphObject_: Obj33) of type CD_Inheritance3
    self.drawConnections(
(self.obj47,self.obj29,[1136.90914946, 1358.75085967, 1153.0, 1255.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj35) of type CD_Inheritance3
    self.drawConnections(
(self.obj48,self.obj32,[152.858254695, 586.846159545, 156.0, 495.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj37) of type CD_Inheritance3
    self.drawConnections(
(self.obj49,self.obj32,[135.466796875, 193.786885246, 116.0, 321.4918032786885],"true", 2) )

newfunction = LSMASOMM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
