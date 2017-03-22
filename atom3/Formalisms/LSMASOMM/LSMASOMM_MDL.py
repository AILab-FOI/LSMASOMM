"""
__LSMASOMM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Wed Mar 22 18:38:21 2017
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
        cobj1.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('LSMASOMM', 20)
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
        cobj1.setValue(('title', 'String', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3String('', 20)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        CD_ClassDiagramsV3RootNode.attributes.setValue(lcobj1)

        # constraints
        CD_ClassDiagramsV3RootNode.constraints.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        cobj1=ATOM3Constraint()
        cobj1.setValue(('saveModelElements', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nSaveAll(self)\n'))
        lcobj1.append(cobj1)
        cobj1=ATOM3Constraint()
        cobj1.setValue(('addConnectionsToDB', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\naddConnectionToDB(self)\n\n\n'))
        lcobj1.append(cobj1)
        CD_ClassDiagramsV3RootNode.constraints.setValue(lcobj1)
    # --- ASG attributes over ---


    self.obj20428527910=CD_Class3(self)
    self.obj20428527910.isGraphObjectVisual = True

    if(hasattr(self.obj20428527910, '_setHierarchicalLink')):
      self.obj20428527910._setHierarchicalLink(False)

    # QOCA
    self.obj20428527910.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj20428527910.Graphical_Appearance.setValue( ('OrgUnit', self.obj20428527910))

    # name
    self.obj20428527910.name.setValue('OrgUnit')

    # attributes
    self.obj20428527910.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Individual', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue(('1', 0))
    cobj2.initialValue.config = 1
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('UnitSize', 'String', None, ('Key', 0), ('Direct Editing', 0)))
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
    self.obj20428527910.attributes.setValue(lcobj2)

    # Abstract
    self.obj20428527910.Abstract.setValue((None, 0))
    self.obj20428527910.Abstract.config = 0

    # cardinality
    self.obj20428527910.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj20428527910.cardinality.setValue(lcobj2)

    # display
    self.obj20428527910.display.setValue('Attributes:\n  - ID :: String\n  - Individual :: Boolean\n  - UnitSize :: String\n  - hasActions :: List\n  - name :: String\nConstraints:\n  > ConstraintOutputOrgUnit\nActions:\n  > determineSize\n  > setNodeID\nMultiplicities:\n  - To isPartOfOrgUnit: 0 to N\n  - From isPartOfOrgUnit: 0 to N\n  - To canHaveRole: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To answersToOrgUnit: 0 to N\n  - From answersToOrgUnit: 0 to N\n')
    self.obj20428527910.display.setHeight(15)

    # Actions
    self.obj20428527910.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('determineSize', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitDetermineSize(self)\nself.UnitSize.setValue(res)\nself.graphObject_.ModifyAttribute(\'UnitSize\', res)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n'))
    lcobj2.append(cobj2)
    self.obj20428527910.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428527910.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintOutputOrgUnit', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitCheckOutputs(self)\nif res is "manyKnArts":\n    return ("OrgUnit can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj20428527910.Constraints.setValue(lcobj2)

    self.obj20428527910.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,220.0,self.obj20428527910)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.88
       new_obj.layConstraints['scale'] = [1.11015625, 3.098360655737705]
    else: new_obj = None
    self.obj20428527910.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428527910)
    self.globalAndLocalPostcondition(self.obj20428527910, rootNode)
    self.obj20428527910.postAction( rootNode.CREATE )

    self.obj20428532885=CD_Class3(self)
    self.obj20428532885.isGraphObjectVisual = True

    if(hasattr(self.obj20428532885, '_setHierarchicalLink')):
      self.obj20428532885._setHierarchicalLink(False)

    # QOCA
    self.obj20428532885.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj20428532885.Graphical_Appearance.setValue( ('Role', self.obj20428532885))

    # name
    self.obj20428532885.name.setValue('Role')

    # attributes
    self.obj20428532885.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj20428532885.attributes.setValue(lcobj2)

    # Abstract
    self.obj20428532885.Abstract.setValue((None, 0))
    self.obj20428532885.Abstract.config = 0

    # cardinality
    self.obj20428532885.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj20428532885.cardinality.setValue(lcobj2)

    # display
    self.obj20428532885.display.setValue('Attributes:\n  - ID :: String\n  - hasActions :: List\n  - isMetaRole :: Boolean\n  - name :: String\nConstraints:\n  > RoleConstraintKnArt\nActions:\n  > checkMetaRole\n  > setNodeID\nMultiplicities:\n  - From canHaveRole: 0 to N\n  - To hasActions: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To hasObjective: 0 to N\n  - To genericAssociation: 0 to N\n  - From genericAssociation: 0 to N\n  - To answersToRole: 0 to N\n  - From answersToRole: 0 to N\n  - To canStartProcess: 0 to N\n  - To isPartOfRole: 0 to N\n  - From isPartOfRole: 0 to N\n')
    self.obj20428532885.display.setHeight(15)

    # Actions
    self.obj20428532885.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('checkMetaRole', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]), 'from CustomCode import RoleHierarchy\nres = RoleHierarchy(self)\nself.isMetaRole.setValue((\'isMetaRole\',res))\nself.graphObject_.ModifyAttribute(\'isMetaRole\', res)\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n\n'))
    lcobj2.append(cobj2)
    self.obj20428532885.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428532885.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('RoleConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '\nfrom CustomCode import *\n\nres = RoleCheckOutputs(self)\nif res is "manyKnArts":\n    return ("Roles can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelif res is "IndivKnArtError":\n    return ("Roles can have OrganizationalKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj20428532885.Constraints.setValue(lcobj2)

    self.obj20428532885.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(620.0,260.0,self.obj20428532885)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.115625, 3.7868852459016393]
    else: new_obj = None
    self.obj20428532885.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428532885)
    self.globalAndLocalPostcondition(self.obj20428532885, rootNode)
    self.obj20428532885.postAction( rootNode.CREATE )

    self.obj20428536748=CD_Class3(self)
    self.obj20428536748.isGraphObjectVisual = True

    if(hasattr(self.obj20428536748, '_setHierarchicalLink')):
      self.obj20428536748._setHierarchicalLink(False)

    # QOCA
    self.obj20428536748.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj20428536748.Graphical_Appearance.setValue( ('Action', self.obj20428536748))

    # name
    self.obj20428536748.name.setValue('Action')

    # attributes
    self.obj20428536748.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj20428536748.attributes.setValue(lcobj2)

    # Abstract
    self.obj20428536748.Abstract.setValue((None, 0))
    self.obj20428536748.Abstract.config = 0

    # cardinality
    self.obj20428536748.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasActions', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj20428536748.cardinality.setValue(lcobj2)

    # display
    self.obj20428536748.display.setValue('Attributes:\n  - ActionCode :: Text\n  - name :: String\nMultiplicities:\n  - From hasActions: 0 to N\n')
    self.obj20428536748.display.setHeight(15)

    # Actions
    self.obj20428536748.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428536748.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428536748.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428536748.Constraints.setValue(lcobj2)

    self.obj20428536748.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(380.0,1080.0,self.obj20428536748)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.06
       new_obj.layConstraints['scale'] = [1.02265625, 1.0454545454545454]
    else: new_obj = None
    self.obj20428536748.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428536748)
    self.globalAndLocalPostcondition(self.obj20428536748, rootNode)
    self.obj20428536748.postAction( rootNode.CREATE )

    self.obj20428539790=CD_Class3(self)
    self.obj20428539790.isGraphObjectVisual = True

    if(hasattr(self.obj20428539790, '_setHierarchicalLink')):
      self.obj20428539790._setHierarchicalLink(False)

    # QOCA
    self.obj20428539790.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj20428539790.Graphical_Appearance.setValue( ('KnowledgeArtifacts', self.obj20428539790))

    # name
    self.obj20428539790.name.setValue('KnowledgeArtifacts')

    # attributes
    self.obj20428539790.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj20428539790.attributes.setValue(lcobj2)

    # Abstract
    self.obj20428539790.Abstract.setValue((None, 1))
    self.obj20428539790.Abstract.config = 0

    # cardinality
    self.obj20428539790.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj20428539790.cardinality.setValue(lcobj2)

    # display
    self.obj20428539790.display.setValue('Attributes:\n  - ID :: String\n  - description :: String\n  - name :: String\nActions:\n  > setNodeID\n')
    self.obj20428539790.display.setHeight(15)

    # Actions
    self.obj20428539790.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n'))
    lcobj2.append(cobj2)
    self.obj20428539790.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428539790.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428539790.Constraints.setValue(lcobj2)

    self.obj20428539790.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(980.0,1080.0,self.obj20428539790)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.239344262295082]
    else: new_obj = None
    self.obj20428539790.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428539790)
    self.globalAndLocalPostcondition(self.obj20428539790, rootNode)
    self.obj20428539790.postAction( rootNode.CREATE )

    self.obj20428541587=CD_Class3(self)
    self.obj20428541587.isGraphObjectVisual = True

    if(hasattr(self.obj20428541587, '_setHierarchicalLink')):
      self.obj20428541587._setHierarchicalLink(False)

    # QOCA
    self.obj20428541587.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj20428541587.Graphical_Appearance.setValue( ('OrganisationalKnArt', self.obj20428541587))

    # name
    self.obj20428541587.name.setValue('OrganisationalKnArt')

    # attributes
    self.obj20428541587.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj20428541587.attributes.setValue(lcobj2)

    # Abstract
    self.obj20428541587.Abstract.setValue((None, 0))
    self.obj20428541587.Abstract.config = 0

    # cardinality
    self.obj20428541587.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj20428541587.cardinality.setValue(lcobj2)

    # display
    self.obj20428541587.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj20428541587.display.setHeight(15)

    # Actions
    self.obj20428541587.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428541587.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428541587.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428541587.Constraints.setValue(lcobj2)

    self.obj20428541587.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(700.0,1080.0,self.obj20428541587)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj20428541587.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428541587)
    self.globalAndLocalPostcondition(self.obj20428541587, rootNode)
    self.obj20428541587.postAction( rootNode.CREATE )

    self.obj20428543412=CD_Class3(self)
    self.obj20428543412.isGraphObjectVisual = True

    if(hasattr(self.obj20428543412, '_setHierarchicalLink')):
      self.obj20428543412._setHierarchicalLink(False)

    # QOCA
    self.obj20428543412.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj20428543412.Graphical_Appearance.setValue( ('IndividualKnArt', self.obj20428543412))

    # name
    self.obj20428543412.name.setValue('IndividualKnArt')

    # attributes
    self.obj20428543412.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj20428543412.attributes.setValue(lcobj2)

    # Abstract
    self.obj20428543412.Abstract.setValue((None, 0))
    self.obj20428543412.Abstract.config = 0

    # cardinality
    self.obj20428543412.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj20428543412.cardinality.setValue(lcobj2)

    # display
    self.obj20428543412.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj20428543412.display.setHeight(15)

    # Actions
    self.obj20428543412.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428543412.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428543412.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428543412.Constraints.setValue(lcobj2)

    self.obj20428543412.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,1060.0,self.obj20428543412)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj20428543412.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428543412)
    self.globalAndLocalPostcondition(self.obj20428543412, rootNode)
    self.obj20428543412.postAction( rootNode.CREATE )

    self.obj20428545233=CD_Class3(self)
    self.obj20428545233.isGraphObjectVisual = True

    if(hasattr(self.obj20428545233, '_setHierarchicalLink')):
      self.obj20428545233._setHierarchicalLink(False)

    # QOCA
    self.obj20428545233.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj20428545233.Graphical_Appearance.setValue( ('Strategy', self.obj20428545233))

    # name
    self.obj20428545233.name.setValue('Strategy')

    # attributes
    self.obj20428545233.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj20428545233.attributes.setValue(lcobj2)

    # Abstract
    self.obj20428545233.Abstract.setValue((None, 1))
    self.obj20428545233.Abstract.config = 0

    # cardinality
    self.obj20428545233.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj20428545233.cardinality.setValue(lcobj2)

    # display
    self.obj20428545233.display.setValue('Attributes:\n  - ID :: String\n  - description :: Text\n  - name :: String\nActions:\n  > setNodeID\n')
    self.obj20428545233.display.setHeight(15)

    # Actions
    self.obj20428545233.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('setNodeID', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = setNodeID(self)\nself.graphObject_.ModifyAttribute(\'ID\', res)\n'))
    lcobj2.append(cobj2)
    self.obj20428545233.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428545233.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428545233.Constraints.setValue(lcobj2)

    self.obj20428545233.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(80.0,320.0,self.obj20428545233)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.239344262295082]
    else: new_obj = None
    self.obj20428545233.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428545233)
    self.globalAndLocalPostcondition(self.obj20428545233, rootNode)
    self.obj20428545233.postAction( rootNode.CREATE )

    self.obj20428547107=CD_Class3(self)
    self.obj20428547107.isGraphObjectVisual = True

    if(hasattr(self.obj20428547107, '_setHierarchicalLink')):
      self.obj20428547107._setHierarchicalLink(False)

    # QOCA
    self.obj20428547107.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj20428547107.Graphical_Appearance.setValue( ('Objective', self.obj20428547107))

    # name
    self.obj20428547107.name.setValue('Objective')

    # attributes
    self.obj20428547107.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj20428547107.attributes.setValue(lcobj2)

    # Abstract
    self.obj20428547107.Abstract.setValue((None, 0))
    self.obj20428547107.Abstract.config = 0

    # cardinality
    self.obj20428547107.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj20428547107.cardinality.setValue(lcobj2)

    # display
    self.obj20428547107.display.setValue('Attributes:\n  - Measurement :: Text\n  - Reward :: Text\nMultiplicities:\n  - To isPartOfObjective: 0 to N\n  - From isPartOfObjective: 0 to N\n  - From hasObjective: 0 to N\n')
    self.obj20428547107.display.setHeight(15)

    # Actions
    self.obj20428547107.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428547107.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428547107.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428547107.Constraints.setValue(lcobj2)

    self.obj20428547107.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(40.0,600.0,self.obj20428547107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.26875, 1.4459016393442625]
    else: new_obj = None
    self.obj20428547107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428547107)
    self.globalAndLocalPostcondition(self.obj20428547107, rootNode)
    self.obj20428547107.postAction( rootNode.CREATE )

    self.obj20428548935=CD_Class3(self)
    self.obj20428548935.isGraphObjectVisual = True

    if(hasattr(self.obj20428548935, '_setHierarchicalLink')):
      self.obj20428548935._setHierarchicalLink(False)

    # QOCA
    self.obj20428548935.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj20428548935.Graphical_Appearance.setValue( ('Process', self.obj20428548935))

    # name
    self.obj20428548935.name.setValue('Process')

    # attributes
    self.obj20428548935.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj20428548935.attributes.setValue(lcobj2)

    # Abstract
    self.obj20428548935.Abstract.setValue((None, 0))
    self.obj20428548935.Abstract.config = 0

    # cardinality
    self.obj20428548935.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canStartProcess', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasObjective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj20428548935.cardinality.setValue(lcobj2)

    # display
    self.obj20428548935.display.setValue('Attributes:\n  - Activities :: Text\n  - Name :: String\nMultiplicities:\n  - From canStartProcess: 0 to N\n  - To hasObjective: 0 to N\n')
    self.obj20428548935.display.setHeight(15)

    # Actions
    self.obj20428548935.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428548935.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428548935.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428548935.Constraints.setValue(lcobj2)

    self.obj20428548935.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(280.0,80.0,self.obj20428548935)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.23046875, 1.239344262295082]
    else: new_obj = None
    self.obj20428548935.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428548935)
    self.globalAndLocalPostcondition(self.obj20428548935, rootNode)
    self.obj20428548935.postAction( rootNode.CREATE )

    self.obj20428550758=CD_Association3(self)
    self.obj20428550758.isGraphObjectVisual = True

    if(hasattr(self.obj20428550758, '_setHierarchicalLink')):
      self.obj20428550758._setHierarchicalLink(True)

    # QOCA
    self.obj20428550758.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj20428550758.Graphical_Appearance.setValue( ('isPartOfOrgUnit', self.obj20428550758))
    self.obj20428550758.Graphical_Appearance.linkInfo=linkEditor(self,self.obj20428550758.Graphical_Appearance.semObject, "isPartOfOrgUnit")
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfOrgUnit_1stLink', self.obj20428550758.Graphical_Appearance.linkInfo.FirstLink))
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfOrgUnit_1stSegment', self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428550758.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj20428550758.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfOrgUnit_Center', self.obj20428550758.Graphical_Appearance.linkInfo))
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfOrgUnit_2ndSegment', self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfOrgUnit_2ndLink', self.obj20428550758.Graphical_Appearance.linkInfo.SecondLink))
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj20428550758.Graphical_Appearance.semObject
    self.obj20428550758.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj20428550758.Graphical_Appearance.semObject
    self.obj20428550758.Graphical_Appearance.linkInfo.Center.semObject=self.obj20428550758.Graphical_Appearance.semObject
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj20428550758.Graphical_Appearance.semObject
    self.obj20428550758.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj20428550758.Graphical_Appearance.semObject

    # name
    self.obj20428550758.name.setValue('isPartOfOrgUnit')

    # displaySelect
    self.obj20428550758.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj20428550758.displaySelect.config = 0

    # attributes
    self.obj20428550758.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428550758.attributes.setValue(lcobj2)

    # cardinality
    self.obj20428550758.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj20428550758.cardinality.setValue(lcobj2)

    # display
    self.obj20428550758.display.setValue('Multiplicities:\n  - From OrgUnit: 1 to N\n  - To OrgUnit: 1 to N\n')
    self.obj20428550758.display.setHeight(15)

    # Actions
    self.obj20428550758.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428550758.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428550758.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428550758.Constraints.setValue(lcobj2)

    self.obj20428550758.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1387.9955984,65.809726225,self.obj20428550758)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj20428550758.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428550758)
    self.globalAndLocalPostcondition(self.obj20428550758, rootNode)
    self.obj20428550758.postAction( rootNode.CREATE )

    self.obj20428552537=CD_Association3(self)
    self.obj20428552537.isGraphObjectVisual = True

    if(hasattr(self.obj20428552537, '_setHierarchicalLink')):
      self.obj20428552537._setHierarchicalLink(True)

    # QOCA
    self.obj20428552537.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj20428552537.Graphical_Appearance.setValue( ('canHaveRole', self.obj20428552537))
    self.obj20428552537.Graphical_Appearance.linkInfo=linkEditor(self,self.obj20428552537.Graphical_Appearance.semObject, "canHaveRole")
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canHaveRole_1stLink', self.obj20428552537.Graphical_Appearance.linkInfo.FirstLink))
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canHaveRole_1stSegment', self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428552537.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj20428552537.Graphical_Appearance.linkInfo.Center.setValue( ('canHaveRole_Center', self.obj20428552537.Graphical_Appearance.linkInfo))
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canHaveRole_2ndSegment', self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canHaveRole_2ndLink', self.obj20428552537.Graphical_Appearance.linkInfo.SecondLink))
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj20428552537.Graphical_Appearance.semObject
    self.obj20428552537.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj20428552537.Graphical_Appearance.semObject
    self.obj20428552537.Graphical_Appearance.linkInfo.Center.semObject=self.obj20428552537.Graphical_Appearance.semObject
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj20428552537.Graphical_Appearance.semObject
    self.obj20428552537.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj20428552537.Graphical_Appearance.semObject

    # name
    self.obj20428552537.name.setValue('canHaveRole')

    # displaySelect
    self.obj20428552537.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj20428552537.displaySelect.config = 0

    # attributes
    self.obj20428552537.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428552537.attributes.setValue(lcobj2)

    # cardinality
    self.obj20428552537.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj20428552537.cardinality.setValue(lcobj2)

    # display
    self.obj20428552537.display.setValue('Multiplicities:\n  - From OrgUnit: 0 to N\n  - To Role: 0 to N\n')
    self.obj20428552537.display.setHeight(15)

    # Actions
    self.obj20428552537.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428552537.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428552537.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428552537.Constraints.setValue(lcobj2)

    self.obj20428552537.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(971.7601868,527.680947659,self.obj20428552537)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj20428552537.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428552537)
    self.globalAndLocalPostcondition(self.obj20428552537, rootNode)
    self.obj20428552537.postAction( rootNode.CREATE )

    self.obj20428553926=CD_Association3(self)
    self.obj20428553926.isGraphObjectVisual = True

    if(hasattr(self.obj20428553926, '_setHierarchicalLink')):
      self.obj20428553926._setHierarchicalLink(False)

    # QOCA
    self.obj20428553926.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj20428553926.Graphical_Appearance.setValue( ('hasActions', self.obj20428553926))
    self.obj20428553926.Graphical_Appearance.linkInfo=linkEditor(self,self.obj20428553926.Graphical_Appearance.semObject, "hasActions")
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasActions_1stLink', self.obj20428553926.Graphical_Appearance.linkInfo.FirstLink))
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasActions_1stSegment', self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428553926.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj20428553926.Graphical_Appearance.linkInfo.Center.setValue( ('hasActions_Center', self.obj20428553926.Graphical_Appearance.linkInfo))
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasActions_2ndSegment', self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasActions_2ndLink', self.obj20428553926.Graphical_Appearance.linkInfo.SecondLink))
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj20428553926.Graphical_Appearance.semObject
    self.obj20428553926.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj20428553926.Graphical_Appearance.semObject
    self.obj20428553926.Graphical_Appearance.linkInfo.Center.semObject=self.obj20428553926.Graphical_Appearance.semObject
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj20428553926.Graphical_Appearance.semObject
    self.obj20428553926.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj20428553926.Graphical_Appearance.semObject

    # name
    self.obj20428553926.name.setValue('hasActions')

    # displaySelect
    self.obj20428553926.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj20428553926.displaySelect.config = 0

    # attributes
    self.obj20428553926.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428553926.attributes.setValue(lcobj2)

    # cardinality
    self.obj20428553926.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Action', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    self.obj20428553926.cardinality.setValue(lcobj2)

    # display
    self.obj20428553926.display.setValue('Multiplicities:\n  - To Action: 1 to N\n  - From Role: 1 to 1\n')
    self.obj20428553926.display.setHeight(15)

    # Actions
    self.obj20428553926.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428553926.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428553926.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428553926.Constraints.setValue(lcobj2)

    self.obj20428553926.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(503.161248615,952.001803815,self.obj20428553926)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj20428553926.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428553926)
    self.globalAndLocalPostcondition(self.obj20428553926, rootNode)
    self.obj20428553926.postAction( rootNode.CREATE )

    self.obj20428555345=CD_Association3(self)
    self.obj20428555345.isGraphObjectVisual = True

    if(hasattr(self.obj20428555345, '_setHierarchicalLink')):
      self.obj20428555345._setHierarchicalLink(False)

    # QOCA
    self.obj20428555345.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj20428555345.Graphical_Appearance.setValue( ('canAccessKnArt', self.obj20428555345))
    self.obj20428555345.Graphical_Appearance.linkInfo=linkEditor(self,self.obj20428555345.Graphical_Appearance.semObject, "canAccessKnArt")
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canAccessKnArt_1stLink', self.obj20428555345.Graphical_Appearance.linkInfo.FirstLink))
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canAccessKnArt_1stSegment', self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428555345.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj20428555345.Graphical_Appearance.linkInfo.Center.setValue( ('canAccessKnArt_Center', self.obj20428555345.Graphical_Appearance.linkInfo))
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canAccessKnArt_2ndSegment', self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canAccessKnArt_2ndLink', self.obj20428555345.Graphical_Appearance.linkInfo.SecondLink))
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj20428555345.Graphical_Appearance.semObject
    self.obj20428555345.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj20428555345.Graphical_Appearance.semObject
    self.obj20428555345.Graphical_Appearance.linkInfo.Center.semObject=self.obj20428555345.Graphical_Appearance.semObject
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj20428555345.Graphical_Appearance.semObject
    self.obj20428555345.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj20428555345.Graphical_Appearance.semObject

    # name
    self.obj20428555345.name.setValue('canAccessKnArt')

    # displaySelect
    self.obj20428555345.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj20428555345.displaySelect.config = 0

    # attributes
    self.obj20428555345.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428555345.attributes.setValue(lcobj2)

    # cardinality
    self.obj20428555345.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj20428555345.cardinality.setValue(lcobj2)

    # display
    self.obj20428555345.display.setValue('Constraints:\n  > ConstraintKnArt\nMultiplicities:\n  - To OrganisationalKnArt: 0 to N\n  - From Role: 0 to N\n  - From OrgUnit: 0 to N\n  - To IndividualKnArt: 0 to N\n')
    self.obj20428555345.display.setHeight(15)

    # Actions
    self.obj20428555345.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428555345.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428555345.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = canAccessKnArtCheckConnections(self)\n\nif res is "eitherRoleOrUnit":\n    return ("Either Role of OrgUnit can access knowledge.", self.graphObject_)\nelif res is "onlyOneInput":\n    return ("Only one Role or OrgUnit can access one knowledge medium.", self.graphObject_)\nelif res is "RoleWithOrgOnly":\n    return ("Role can access OrganisationalKnArt only!", self.graphObject_)\nelif res is "OrgUnitWithIndivOnly":\n    return ("OrgUnit can access IndividualKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj20428555345.Constraints.setValue(lcobj2)

    self.obj20428555345.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1106.462784,821.548234957,self.obj20428555345)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.6380000000000001, 1.8967741935483875]
    else: new_obj = None
    self.obj20428555345.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428555345)
    self.globalAndLocalPostcondition(self.obj20428555345, rootNode)
    self.obj20428555345.postAction( rootNode.CREATE )

    self.obj20428556730=CD_Association3(self)
    self.obj20428556730.isGraphObjectVisual = True

    if(hasattr(self.obj20428556730, '_setHierarchicalLink')):
      self.obj20428556730._setHierarchicalLink(True)

    # QOCA
    self.obj20428556730.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj20428556730.Graphical_Appearance.setValue( ('isPartOfObjective', self.obj20428556730))
    self.obj20428556730.Graphical_Appearance.linkInfo=linkEditor(self,self.obj20428556730.Graphical_Appearance.semObject, "isPartOfObjective")
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfObjective_1stLink', self.obj20428556730.Graphical_Appearance.linkInfo.FirstLink))
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfObjective_1stSegment', self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428556730.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj20428556730.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfObjective_Center', self.obj20428556730.Graphical_Appearance.linkInfo))
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfObjective_2ndSegment', self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfObjective_2ndLink', self.obj20428556730.Graphical_Appearance.linkInfo.SecondLink))
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj20428556730.Graphical_Appearance.semObject
    self.obj20428556730.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj20428556730.Graphical_Appearance.semObject
    self.obj20428556730.Graphical_Appearance.linkInfo.Center.semObject=self.obj20428556730.Graphical_Appearance.semObject
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj20428556730.Graphical_Appearance.semObject
    self.obj20428556730.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj20428556730.Graphical_Appearance.semObject

    # name
    self.obj20428556730.name.setValue('isPartOfObjective')

    # displaySelect
    self.obj20428556730.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj20428556730.displaySelect.config = 0

    # attributes
    self.obj20428556730.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428556730.attributes.setValue(lcobj2)

    # cardinality
    self.obj20428556730.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj20428556730.cardinality.setValue(lcobj2)

    # display
    self.obj20428556730.display.setValue('Multiplicities:\n  - From Objective: 0 to N\n  - To Objective: 0 to N\n')
    self.obj20428556730.display.setHeight(15)

    # Actions
    self.obj20428556730.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428556730.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428556730.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428556730.Constraints.setValue(lcobj2)

    self.obj20428556730.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(131.944046519,946.91223085,self.obj20428556730)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.225, 1.0]
    else: new_obj = None
    self.obj20428556730.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428556730)
    self.globalAndLocalPostcondition(self.obj20428556730, rootNode)
    self.obj20428556730.postAction( rootNode.CREATE )

    self.obj20428558011=CD_Association3(self)
    self.obj20428558011.isGraphObjectVisual = True

    if(hasattr(self.obj20428558011, '_setHierarchicalLink')):
      self.obj20428558011._setHierarchicalLink(False)

    # QOCA
    self.obj20428558011.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj20428558011.Graphical_Appearance.setValue( ('hasObjective', self.obj20428558011))
    self.obj20428558011.Graphical_Appearance.linkInfo=linkEditor(self,self.obj20428558011.Graphical_Appearance.semObject, "hasObjective")
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasObjective_1stLink', self.obj20428558011.Graphical_Appearance.linkInfo.FirstLink))
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasObjective_1stSegment', self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428558011.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj20428558011.Graphical_Appearance.linkInfo.Center.setValue( ('hasObjective_Center', self.obj20428558011.Graphical_Appearance.linkInfo))
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasObjective_2ndSegment', self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasObjective_2ndLink', self.obj20428558011.Graphical_Appearance.linkInfo.SecondLink))
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj20428558011.Graphical_Appearance.semObject
    self.obj20428558011.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj20428558011.Graphical_Appearance.semObject
    self.obj20428558011.Graphical_Appearance.linkInfo.Center.semObject=self.obj20428558011.Graphical_Appearance.semObject
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj20428558011.Graphical_Appearance.semObject
    self.obj20428558011.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj20428558011.Graphical_Appearance.semObject

    # name
    self.obj20428558011.name.setValue('hasObjective')

    # displaySelect
    self.obj20428558011.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj20428558011.displaySelect.config = 0

    # attributes
    self.obj20428558011.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428558011.attributes.setValue(lcobj2)

    # cardinality
    self.obj20428558011.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj20428558011.cardinality.setValue(lcobj2)

    # display
    self.obj20428558011.display.setValue('Multiplicities:\n  - To Objective: 1 to N\n  - From Role: 0 to N\n  - From Process: 0 to N\n')
    self.obj20428558011.display.setHeight(15)

    # Actions
    self.obj20428558011.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428558011.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428558011.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428558011.Constraints.setValue(lcobj2)

    self.obj20428558011.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(436.73445957,632.859445861,self.obj20428558011)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.1620000000000001, 1.0838709677419356]
    else: new_obj = None
    self.obj20428558011.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428558011)
    self.globalAndLocalPostcondition(self.obj20428558011, rootNode)
    self.obj20428558011.postAction( rootNode.CREATE )

    self.obj20428559479=CD_Association3(self)
    self.obj20428559479.isGraphObjectVisual = True

    if(hasattr(self.obj20428559479, '_setHierarchicalLink')):
      self.obj20428559479._setHierarchicalLink(False)

    # QOCA
    self.obj20428559479.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj20428559479.Graphical_Appearance.setValue( ('genericAssociation', self.obj20428559479))
    self.obj20428559479.Graphical_Appearance.linkInfo=linkEditor(self,self.obj20428559479.Graphical_Appearance.semObject, "genericAssociation")
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('genericAssociation_1stLink', self.obj20428559479.Graphical_Appearance.linkInfo.FirstLink))
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('genericAssociation_1stSegment', self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428559479.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj20428559479.Graphical_Appearance.linkInfo.Center.setValue( ('genericAssociation_Center', self.obj20428559479.Graphical_Appearance.linkInfo))
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('genericAssociation_2ndSegment', self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('genericAssociation_2ndLink', self.obj20428559479.Graphical_Appearance.linkInfo.SecondLink))
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj20428559479.Graphical_Appearance.semObject
    self.obj20428559479.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj20428559479.Graphical_Appearance.semObject
    self.obj20428559479.Graphical_Appearance.linkInfo.Center.semObject=self.obj20428559479.Graphical_Appearance.semObject
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj20428559479.Graphical_Appearance.semObject
    self.obj20428559479.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj20428559479.Graphical_Appearance.semObject

    # name
    self.obj20428559479.name.setValue('genericAssociation')

    # displaySelect
    self.obj20428559479.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj20428559479.displaySelect.config = 0

    # attributes
    self.obj20428559479.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj20428559479.attributes.setValue(lcobj2)

    # cardinality
    self.obj20428559479.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj20428559479.cardinality.setValue(lcobj2)

    # display
    self.obj20428559479.display.setValue('Attributes:\n  - Name :: String\n  - Description :: Text\nMultiplicities:\n  - To Role: 1 to N\n  - From Role: 1 to N\n')
    self.obj20428559479.display.setHeight(15)

    # Actions
    self.obj20428559479.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428559479.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428559479.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428559479.Constraints.setValue(lcobj2)

    self.obj20428559479.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1044.0,340.0,self.obj20428559479)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.015, 1.6258064516129034]
    else: new_obj = None
    self.obj20428559479.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428559479)
    self.globalAndLocalPostcondition(self.obj20428559479, rootNode)
    self.obj20428559479.postAction( rootNode.CREATE )

    self.obj20428560990=CD_Association3(self)
    self.obj20428560990.isGraphObjectVisual = True

    if(hasattr(self.obj20428560990, '_setHierarchicalLink')):
      self.obj20428560990._setHierarchicalLink(True)

    # QOCA
    self.obj20428560990.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj20428560990.Graphical_Appearance.setValue( ('answersToRole', self.obj20428560990))
    self.obj20428560990.Graphical_Appearance.linkInfo=linkEditor(self,self.obj20428560990.Graphical_Appearance.semObject, "answersToRole")
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToRole_1stLink', self.obj20428560990.Graphical_Appearance.linkInfo.FirstLink))
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToRole_1stSegment', self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428560990.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj20428560990.Graphical_Appearance.linkInfo.Center.setValue( ('answersToRole_Center', self.obj20428560990.Graphical_Appearance.linkInfo))
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToRole_2ndSegment', self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToRole_2ndLink', self.obj20428560990.Graphical_Appearance.linkInfo.SecondLink))
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj20428560990.Graphical_Appearance.semObject
    self.obj20428560990.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj20428560990.Graphical_Appearance.semObject
    self.obj20428560990.Graphical_Appearance.linkInfo.Center.semObject=self.obj20428560990.Graphical_Appearance.semObject
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj20428560990.Graphical_Appearance.semObject
    self.obj20428560990.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj20428560990.Graphical_Appearance.semObject

    # name
    self.obj20428560990.name.setValue('answersToRole')

    # displaySelect
    self.obj20428560990.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj20428560990.displaySelect.config = 0

    # attributes
    self.obj20428560990.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428560990.attributes.setValue(lcobj2)

    # cardinality
    self.obj20428560990.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj20428560990.cardinality.setValue(lcobj2)

    # display
    self.obj20428560990.display.setValue('Multiplicities:\n  - From Role: 1 to N\n  - To Role: 1 to N\n')
    self.obj20428560990.display.setHeight(15)

    # Actions
    self.obj20428560990.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428560990.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428560990.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428560990.Constraints.setValue(lcobj2)

    self.obj20428560990.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(933.0,176.0,self.obj20428560990)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj20428560990.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428560990)
    self.globalAndLocalPostcondition(self.obj20428560990, rootNode)
    self.obj20428560990.postAction( rootNode.CREATE )

    self.obj20428562445=CD_Association3(self)
    self.obj20428562445.isGraphObjectVisual = True

    if(hasattr(self.obj20428562445, '_setHierarchicalLink')):
      self.obj20428562445._setHierarchicalLink(False)

    # QOCA
    self.obj20428562445.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj20428562445.Graphical_Appearance.setValue( ('canStartProcess', self.obj20428562445))
    self.obj20428562445.Graphical_Appearance.linkInfo=linkEditor(self,self.obj20428562445.Graphical_Appearance.semObject, "canStartProcess")
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canStartProcess_1stLink', self.obj20428562445.Graphical_Appearance.linkInfo.FirstLink))
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canStartProcess_1stSegment', self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428562445.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj20428562445.Graphical_Appearance.linkInfo.Center.setValue( ('canStartProcess_Center', self.obj20428562445.Graphical_Appearance.linkInfo))
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canStartProcess_2ndSegment', self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canStartProcess_2ndLink', self.obj20428562445.Graphical_Appearance.linkInfo.SecondLink))
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj20428562445.Graphical_Appearance.semObject
    self.obj20428562445.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj20428562445.Graphical_Appearance.semObject
    self.obj20428562445.Graphical_Appearance.linkInfo.Center.semObject=self.obj20428562445.Graphical_Appearance.semObject
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj20428562445.Graphical_Appearance.semObject
    self.obj20428562445.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj20428562445.Graphical_Appearance.semObject

    # name
    self.obj20428562445.name.setValue('canStartProcess')

    # displaySelect
    self.obj20428562445.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj20428562445.displaySelect.config = 0

    # attributes
    self.obj20428562445.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428562445.attributes.setValue(lcobj2)

    # cardinality
    self.obj20428562445.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Process', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj20428562445.cardinality.setValue(lcobj2)

    # display
    self.obj20428562445.display.setValue('Multiplicities:\n  - To Process: 0 to N\n  - From Role: 0 to N\n')
    self.obj20428562445.display.setHeight(15)

    # Actions
    self.obj20428562445.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428562445.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428562445.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428562445.Constraints.setValue(lcobj2)

    self.obj20428562445.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(470.4921875,411.163934426,self.obj20428562445)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.036, 1.0]
    else: new_obj = None
    self.obj20428562445.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428562445)
    self.globalAndLocalPostcondition(self.obj20428562445, rootNode)
    self.obj20428562445.postAction( rootNode.CREATE )

    self.obj20428563801=CD_Association3(self)
    self.obj20428563801.isGraphObjectVisual = True

    if(hasattr(self.obj20428563801, '_setHierarchicalLink')):
      self.obj20428563801._setHierarchicalLink(True)

    # QOCA
    self.obj20428563801.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj20428563801.Graphical_Appearance.setValue( ('answersToOrgUnit', self.obj20428563801))
    self.obj20428563801.Graphical_Appearance.linkInfo=linkEditor(self,self.obj20428563801.Graphical_Appearance.semObject, "answersToOrgUnit")
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToOrgUnit_1stLink', self.obj20428563801.Graphical_Appearance.linkInfo.FirstLink))
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToOrgUnit_1stSegment', self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428563801.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj20428563801.Graphical_Appearance.linkInfo.Center.setValue( ('answersToOrgUnit_Center', self.obj20428563801.Graphical_Appearance.linkInfo))
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToOrgUnit_2ndSegment', self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToOrgUnit_2ndLink', self.obj20428563801.Graphical_Appearance.linkInfo.SecondLink))
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj20428563801.Graphical_Appearance.semObject
    self.obj20428563801.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj20428563801.Graphical_Appearance.semObject
    self.obj20428563801.Graphical_Appearance.linkInfo.Center.semObject=self.obj20428563801.Graphical_Appearance.semObject
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj20428563801.Graphical_Appearance.semObject
    self.obj20428563801.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj20428563801.Graphical_Appearance.semObject

    # name
    self.obj20428563801.name.setValue('answersToOrgUnit')

    # displaySelect
    self.obj20428563801.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj20428563801.displaySelect.config = 0

    # attributes
    self.obj20428563801.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428563801.attributes.setValue(lcobj2)

    # cardinality
    self.obj20428563801.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj20428563801.cardinality.setValue(lcobj2)

    # display
    self.obj20428563801.display.setValue('Multiplicities:\n  - To OrgUnit: 1 to N\n  - From OrgUnit: 1 to N\n')
    self.obj20428563801.display.setHeight(15)

    # Actions
    self.obj20428563801.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428563801.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428563801.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428563801.Constraints.setValue(lcobj2)

    self.obj20428563801.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1113.0,79.0,self.obj20428563801)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj20428563801.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428563801)
    self.globalAndLocalPostcondition(self.obj20428563801, rootNode)
    self.obj20428563801.postAction( rootNode.CREATE )

    self.obj20428565432=CD_Association3(self)
    self.obj20428565432.isGraphObjectVisual = True

    if(hasattr(self.obj20428565432, '_setHierarchicalLink')):
      self.obj20428565432._setHierarchicalLink(True)

    # QOCA
    self.obj20428565432.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj20428565432.Graphical_Appearance.setValue( ('isPartOfRole', self.obj20428565432))
    self.obj20428565432.Graphical_Appearance.linkInfo=linkEditor(self,self.obj20428565432.Graphical_Appearance.semObject, "isPartOfRole")
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfRole_1stLink', self.obj20428565432.Graphical_Appearance.linkInfo.FirstLink))
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfRole_1stSegment', self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj20428565432.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj20428565432.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfRole_Center', self.obj20428565432.Graphical_Appearance.linkInfo))
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfRole_2ndSegment', self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],0,0)
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfRole_2ndLink', self.obj20428565432.Graphical_Appearance.linkInfo.SecondLink))
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj20428565432.Graphical_Appearance.semObject
    self.obj20428565432.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj20428565432.Graphical_Appearance.semObject
    self.obj20428565432.Graphical_Appearance.linkInfo.Center.semObject=self.obj20428565432.Graphical_Appearance.semObject
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj20428565432.Graphical_Appearance.semObject
    self.obj20428565432.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj20428565432.Graphical_Appearance.semObject

    # name
    self.obj20428565432.name.setValue('isPartOfRole')

    # displaySelect
    self.obj20428565432.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj20428565432.displaySelect.config = 0

    # attributes
    self.obj20428565432.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428565432.attributes.setValue(lcobj2)

    # cardinality
    self.obj20428565432.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj20428565432.cardinality.setValue(lcobj2)

    # display
    self.obj20428565432.display.setValue('Multiplicities:\n  - From Role: 0 to N\n  - To Role: 0 to N\n')
    self.obj20428565432.display.setHeight(15)

    # Actions
    self.obj20428565432.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428565432.Actions.setValue(lcobj2)

    # Constraints
    self.obj20428565432.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20428565432.Constraints.setValue(lcobj2)

    self.obj20428565432.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(675.0,160.0,self.obj20428565432)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj20428565432.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428565432)
    self.globalAndLocalPostcondition(self.obj20428565432, rootNode)
    self.obj20428565432.postAction( rootNode.CREATE )

    self.obj20428566779=CD_Inheritance3(self)
    self.obj20428566779.isGraphObjectVisual = True

    if(hasattr(self.obj20428566779, '_setHierarchicalLink')):
      self.obj20428566779._setHierarchicalLink(False)

    self.obj20428566779.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1056.21888986,1366.92763695,self.obj20428566779)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj20428566779.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428566779)
    self.globalAndLocalPostcondition(self.obj20428566779, rootNode)
    self.obj20428566779.postAction( rootNode.CREATE )

    self.obj20428567182=CD_Inheritance3(self)
    self.obj20428567182.isGraphObjectVisual = True

    if(hasattr(self.obj20428567182, '_setHierarchicalLink')):
      self.obj20428567182._setHierarchicalLink(False)

    self.obj20428567182.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1136.90914946,1358.75085967,self.obj20428567182)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj20428567182.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428567182)
    self.globalAndLocalPostcondition(self.obj20428567182, rootNode)
    self.obj20428567182.postAction( rootNode.CREATE )

    self.obj20428567401=CD_Inheritance3(self)
    self.obj20428567401.isGraphObjectVisual = True

    if(hasattr(self.obj20428567401, '_setHierarchicalLink')):
      self.obj20428567401._setHierarchicalLink(False)

    self.obj20428567401.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(152.858254695,586.846159545,self.obj20428567401)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj20428567401.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428567401)
    self.globalAndLocalPostcondition(self.obj20428567401, rootNode)
    self.obj20428567401.postAction( rootNode.CREATE )

    self.obj20428567595=CD_Inheritance3(self)
    self.obj20428567595.isGraphObjectVisual = True

    if(hasattr(self.obj20428567595, '_setHierarchicalLink')):
      self.obj20428567595._setHierarchicalLink(False)

    self.obj20428567595.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(135.466796875,193.786885246,self.obj20428567595)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj20428567595.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj20428567595)
    self.globalAndLocalPostcondition(self.obj20428567595, rootNode)
    self.obj20428567595.postAction( rootNode.CREATE )

    # Connections for obj20428527910 (graphObject_: Obj0) named OrgUnit
    self.drawConnections(
(self.obj20428527910,self.obj20428550758,[1368.8125, 221.22950819672127, 1387.9955983980042, 65.8097262245276, 1387.9955984, 65.809726225],"true", 3),
(self.obj20428527910,self.obj20428552537,[1241.14453125, 515.5737704918033, 967.8422485527899, 481.40176688146084, 971.7601868, 527.680947659],"true", 3),
(self.obj20428527910,self.obj20428555345,[1241.14453125, 515.5737704918033, 997.8287423035672, 492.3266545159663, 1106.462784, 821.548234957],"true", 3),
(self.obj20428527910,self.obj20428563801,[1280.0, 221.22950819672127, 1130.0, 231.0, 1113.0, 79.0], 0, 3) )
    # Connections for obj20428532885 (graphObject_: Obj1) named Role
    self.drawConnections(
(self.obj20428532885,self.obj20428553926,[660.0, 791.0, 541.1631302538499, 883.356649681594, 503.161248615, 952.001803815],"true", 3),
(self.obj20428532885,self.obj20428555345,[832.921875, 715.2622950819672, 1023.5805784296024, 714.1457487347751, 1106.462784, 821.548234957],"true", 3),
(self.obj20428532885,self.obj20428558011,[620.953125, 518.344262295082, 522.0012232889502, 553.7739542825374, 436.73445957, 632.859445861],"true", 3),
(self.obj20428532885,self.obj20428559479,[832.921875, 412.3114754098361, 1044.0, 340.0], 0, 2),
(self.obj20428532885,self.obj20428560990,[793.875, 260.8360655737705, 933.0, 176.0], 0, 2),
(self.obj20428532885,self.obj20428562445,[620.953125, 412.3114754098361, 470.4921875, 411.163934426], 0, 2),
(self.obj20428532885,self.obj20428565432,[660.0, 260.8360655737705, 675.0, 160.0],"true", 2) )
    # Connections for obj20428536748 (graphObject_: Obj2) named Action
    self.drawConnections(
 )
    # Connections for obj20428539790 (graphObject_: Obj3) named KnowledgeArtifacts
    self.drawConnections(
 )
    # Connections for obj20428541587 (graphObject_: Obj4) named OrganisationalKnArt
    self.drawConnections(
(self.obj20428541587,self.obj20428566779,[935.5703125, 1206.090909090909, 1056.21888986, 1366.92763695],"true", 2) )
    # Connections for obj20428543412 (graphObject_: Obj5) named IndividualKnArt
    self.drawConnections(
(self.obj20428543412,self.obj20428567182,[1240.7421875, 1186.090909090909, 1136.90914946, 1358.75085967],"true", 2) )
    # Connections for obj20428545233 (graphObject_: Obj6) named Strategy
    self.drawConnections(
 )
    # Connections for obj20428547107 (graphObject_: Obj7) named Objective
    self.drawConnections(
(self.obj20428547107,self.obj20428567401,[135.75, 600.5737704918033, 152.858254695, 586.846159545],"true", 2),
(self.obj20428547107,self.obj20428556730,[139.75, 803.0, 131.94404651894035, 946.9122308488277, 131.944046519, 946.91223085],"true", 3) )
    # Connections for obj20428548935 (graphObject_: Obj8) named Process
    self.drawConnections(
(self.obj20428548935,self.obj20428558011,[324.0, 255.0, 333.0, 453.0, 436.73445957, 632.859445861],"true", 3),
(self.obj20428548935,self.obj20428567595,[280.93359375, 199.2295081967213, 135.466796875, 193.786885246],"true", 2) )
    # Connections for obj20428550758 (graphObject_: Obj9) named isPartOfOrgUnit
    self.drawConnections(
(self.obj20428550758,self.obj20428527910,[1387.9955984, 65.809726225, 1387.9955983980042, 65.8097262245276, 1368.8125, 221.22950819672127],"true", 3) )
    # Connections for obj20428552537 (graphObject_: Obj11) named canHaveRole
    self.drawConnections(
(self.obj20428552537,self.obj20428532885,[971.7601868, 527.680947659, 975.67812505129, 573.9601284363068, 832.921875, 620.5901639344263],"true", 3) )
    # Connections for obj20428553926 (graphObject_: Obj13) named hasActions
    self.drawConnections(
(self.obj20428553926,self.obj20428536748,[503.161248615, 952.001803815, 465.1593669760688, 1020.6469579482074, 457.90625, 1080.6363636363635],"true", 3) )
    # Connections for obj20428555345 (graphObject_: Obj15) named canAccessKnArt
    self.drawConnections(
(self.obj20428555345,self.obj20428541587,[1106.462784, 821.548234957, 1128.2678325033444, 887.9439489105719, 935.5703125, 1122.4545454545455],"true", 3),
(self.obj20428555345,self.obj20428543412,[1106.462784, 821.548234957, 1033.4035107781324, 923.4763808302594, 1240.7421875, 1102.4545454545455],"true", 3) )
    # Connections for obj20428556730 (graphObject_: Obj17) named isPartOfObjective
    self.drawConnections(
(self.obj20428556730,self.obj20428547107,[131.944046519, 946.91223085, 131.94404651894035, 946.9122308488277, 139.75, 803.0],"true", 3) )
    # Connections for obj20428558011 (graphObject_: Obj19) named hasObjective
    self.drawConnections(
(self.obj20428558011,self.obj20428547107,[436.73445957, 632.859445861, 351.4676958509182, 711.9449374392455, 281.65625, 698.8950819672131],"true", 3) )
    # Connections for obj20428559479 (graphObject_: Obj21) named genericAssociation
    self.drawConnections(
(self.obj20428559479,self.obj20428532885,[1044.0, 340.0, 832.921875, 412.3114754098361], 0, 2) )
    # Connections for obj20428560990 (graphObject_: Obj23) named answersToRole
    self.drawConnections(
(self.obj20428560990,self.obj20428532885,[933.0, 176.0, 793.875, 260.8360655737705], 0, 2) )
    # Connections for obj20428562445 (graphObject_: Obj25) named canStartProcess
    self.drawConnections(
(self.obj20428562445,self.obj20428548935,[470.4921875, 411.163934426, 471.65625, 255.0], 0, 2) )
    # Connections for obj20428563801 (graphObject_: Obj27) named answersToOrgUnit
    self.drawConnections(
(self.obj20428563801,self.obj20428527910,[1113.0, 79.0, 1279.0, 145.0, 1280.0, 221.22950819672127], 0, 3) )
    # Connections for obj20428565432 (graphObject_: Obj29) named isPartOfRole
    self.drawConnections(
(self.obj20428565432,self.obj20428532885,[675.0, 160.0, 660.0, 260.8360655737705],"true", 2) )
    # Connections for obj20428566779 (graphObject_: Obj31) of type CD_Inheritance3
    self.drawConnections(
(self.obj20428566779,self.obj20428539790,[1056.21888986, 1366.92763695, 1073.0, 1255.0],"true", 2) )
    # Connections for obj20428567182 (graphObject_: Obj33) of type CD_Inheritance3
    self.drawConnections(
(self.obj20428567182,self.obj20428539790,[1136.90914946, 1358.75085967, 1153.0, 1255.0],"true", 2) )
    # Connections for obj20428567401 (graphObject_: Obj35) of type CD_Inheritance3
    self.drawConnections(
(self.obj20428567401,self.obj20428545233,[152.858254695, 586.846159545, 156.0, 495.0],"true", 2) )
    # Connections for obj20428567595 (graphObject_: Obj37) of type CD_Inheritance3
    self.drawConnections(
(self.obj20428567595,self.obj20428545233,[135.466796875, 193.786885246, 116.0, 321.4918032786885],"true", 2) )

newfunction = LSMASOMM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
