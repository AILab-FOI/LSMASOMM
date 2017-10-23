"""
__LSMASOMM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Sun Oct 22 23:29:26 2017
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
        cobj1=ATOM3Attribute(self.types)
        cobj1.setValue(('agentImplementation', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
        cobj1.initialValue=ATOM3Enum(['SPADE', 'Enmasse', 'EveJS'],0,1)
        cobj1.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
        lcobj2 =[]
        cobj2=ATOM3String('SPADE', 20)
        lcobj2.append(cobj2)
        cobj2=ATOM3String('Enmasse', 20)
        lcobj2.append(cobj2)
        cobj2=ATOM3String('EveJS', 20)
        lcobj2.append(cobj2)
        cobj1.initialValue.configItems.setValue(lcobj2)
        cobj1.isDerivedAttribute = False
        lcobj1.append(cobj1)
        CD_ClassDiagramsV3RootNode.attributes.setValue(lcobj1)

        # constraints
        CD_ClassDiagramsV3RootNode.constraints.setActionFlags([ 1, 1, 1, 0])
        lcobj1 =[]
        cobj1=ATOM3Constraint()
        cobj1.setValue(('saveModelElements', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nSaveAll(self)\n\n'))
        lcobj1.append(cobj1)
        cobj1=ATOM3Constraint()
        cobj1.setValue(('addConnectionsToDB', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\naddConnectionToDB(self)\n\n'))
        lcobj1.append(cobj1)
        cobj1=ATOM3Constraint()
        cobj1.setValue(('CheckUniqueID', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\n\nres = checkUniqueID(self)\n\nif res:\n  return ("Duplicate ID: {}! Specify another.".format(res[1]), res[0])\n\n'))
        lcobj1.append(cobj1)
        CD_ClassDiagramsV3RootNode.constraints.setValue(lcobj1)
    # --- ASG attributes over ---


    self.obj212=CD_Class3(self)
    self.obj212.isGraphObjectVisual = True

    if(hasattr(self.obj212, '_setHierarchicalLink')):
      self.obj212._setHierarchicalLink(False)

    # QOCA
    self.obj212.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj212.Graphical_Appearance.setValue( ('OrgUnit', self.obj212))

    # name
    self.obj212.name.setValue('OrgUnit')

    # attributes
    self.obj212.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('OU|', 20)
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
    cobj2.initialValue=ATOM3String('OUname', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj212.attributes.setValue(lcobj2)

    # Abstract
    self.obj212.Abstract.setValue((None, 0))
    self.obj212.Abstract.config = 0

    # cardinality
    self.obj212.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj212.cardinality.setValue(lcobj2)

    # display
    self.obj212.display.setValue('Attributes:\n  - ID :: String\n  - Individual :: Boolean\n  - UnitSize :: String\n  - hasActions :: List\n  - name :: String\nConstraints:\n  > ConstraintOutputOrgUnit\nActions:\n  > determineSize\nMultiplicities:\n  - To isPartOfOrgUnit: 0 to N\n  - From isPartOfOrgUnit: 0 to N\n  - To canHaveRole: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To answersToOrgUnit: 0 to N\n  - From answersToOrgUnit: 0 to N\n')
    self.obj212.display.setHeight(15)

    # Actions
    self.obj212.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('determineSize', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitDetermineSize(self)\nself.UnitSize.setValue(res)\nself.graphObject_.ModifyAttribute(\'UnitSize\', res)\n\n'))
    lcobj2.append(cobj2)
    self.obj212.Actions.setValue(lcobj2)

    # Constraints
    self.obj212.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintOutputOrgUnit', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitCheckOutputs(self)\nif res is "manyKnArts":\n    return ("OrgUnit can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj212.Constraints.setValue(lcobj2)

    self.obj212.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,220.0,self.obj212)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.88
       new_obj.layConstraints['scale'] = [1.11015625, 2.9262295081967213]
    else: new_obj = None
    self.obj212.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj212)
    self.globalAndLocalPostcondition(self.obj212, rootNode)
    self.obj212.postAction( rootNode.CREATE )

    self.obj213=CD_Class3(self)
    self.obj213.isGraphObjectVisual = True

    if(hasattr(self.obj213, '_setHierarchicalLink')):
      self.obj213._setHierarchicalLink(False)

    # QOCA
    self.obj213.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj213.Graphical_Appearance.setValue( ('Role', self.obj213))

    # name
    self.obj213.name.setValue('Role')

    # attributes
    self.obj213.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('R|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('hasActions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 0, 0, 1, self.types],ATOM3String)
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
    self.obj213.attributes.setValue(lcobj2)

    # Abstract
    self.obj213.Abstract.setValue((None, 0))
    self.obj213.Abstract.config = 0

    # cardinality
    self.obj213.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj213.cardinality.setValue(lcobj2)

    # display
    self.obj213.display.setValue('Attributes:\n  - ID :: String\n  - hasActions :: List\n  - isMetaRole :: Boolean\n  - name :: String\nConstraints:\n  > RoleConstraintKnArt\nActions:\n  > checkMetaRole\nMultiplicities:\n  - From canHaveRole: 0 to N\n  - To hasActions: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To hasObjective: 0 to N\n  - To genericAssociation: 0 to N\n  - From genericAssociation: 0 to N\n  - To answersToRole: 0 to N\n  - From answersToRole: 0 to N\n  - To canStartProcess: 0 to N\n  - To isPartOfRole: 0 to N\n  - From isPartOfRole: 0 to N\n')
    self.obj213.display.setHeight(15)

    # Actions
    self.obj213.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('checkMetaRole', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]), 'from CustomCode import RoleHierarchy\nres = RoleHierarchy(self)\n\n'))
    lcobj2.append(cobj2)
    self.obj213.Actions.setValue(lcobj2)

    # Constraints
    self.obj213.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('RoleConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '\nfrom CustomCode import *\n\nres = RoleCheckOutputs(self)\nif res is "manyKnArts":\n    return ("Roles can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelif res is "IndivKnArtError":\n    return ("Roles can have OrganizationalKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj213.Constraints.setValue(lcobj2)

    self.obj213.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(620.0,260.0,self.obj213)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.115625, 3.6147540983606556]
    else: new_obj = None
    self.obj213.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj213)
    self.globalAndLocalPostcondition(self.obj213, rootNode)
    self.obj213.postAction( rootNode.CREATE )

    self.obj214=CD_Class3(self)
    self.obj214.isGraphObjectVisual = True

    if(hasattr(self.obj214, '_setHierarchicalLink')):
      self.obj214._setHierarchicalLink(False)

    # QOCA
    self.obj214.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj214.Graphical_Appearance.setValue( ('Action', self.obj214))

    # name
    self.obj214.name.setValue('Action')

    # attributes
    self.obj214.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ActionCode', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('#action code placeholder or description\n#\n', 80,15 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('A|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('ActionName', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj214.attributes.setValue(lcobj2)

    # Abstract
    self.obj214.Abstract.setValue((None, 0))
    self.obj214.Abstract.config = 0

    # cardinality
    self.obj214.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasActions', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('isPartOfProcess', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasObjective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj214.cardinality.setValue(lcobj2)

    # display
    self.obj214.display.setValue('Attributes:\n  - ActionCode :: Text\n  - ID :: String\n  - name :: String\nActions:\n  > initialActionCodeTemplate\nMultiplicities:\n  - From hasActions: 0 to N\n  - To isPartOfProcess: 0 to N\n  - To hasObjective: 0 to N\n')
    self.obj214.display.setHeight(15)

    # Actions
    self.obj214.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('initialActionCodeTemplate', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import ActionCodeTemplate\n\nres = ActionCodeTemplate(self)\n\nself.setAttrValue(\'ActionCode\', res)\n\n\n'))
    lcobj2.append(cobj2)
    self.obj214.Actions.setValue(lcobj2)

    # Constraints
    self.obj214.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj214.Constraints.setValue(lcobj2)

    self.obj214.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(380.0,1080.0,self.obj214)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.06
       new_obj.layConstraints['scale'] = [1.1484375, 2.0655737704918034]
    else: new_obj = None
    self.obj214.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj214)
    self.globalAndLocalPostcondition(self.obj214, rootNode)
    self.obj214.postAction( rootNode.CREATE )

    self.obj215=CD_Class3(self)
    self.obj215.isGraphObjectVisual = True

    if(hasattr(self.obj215, '_setHierarchicalLink')):
      self.obj215._setHierarchicalLink(False)

    # QOCA
    self.obj215.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj215.Graphical_Appearance.setValue( ('KnowledgeArtifacts', self.obj215))

    # name
    self.obj215.name.setValue('KnowledgeArtifacts')

    # attributes
    self.obj215.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KA|', 20)
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
    self.obj215.attributes.setValue(lcobj2)

    # Abstract
    self.obj215.Abstract.setValue((None, 1))
    self.obj215.Abstract.config = 0

    # cardinality
    self.obj215.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj215.cardinality.setValue(lcobj2)

    # display
    self.obj215.display.setValue('Attributes:\n  - ID :: String\n  - description :: String\n  - name :: String\n')
    self.obj215.display.setHeight(15)

    # Actions
    self.obj215.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj215.Actions.setValue(lcobj2)

    # Constraints
    self.obj215.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj215.Constraints.setValue(lcobj2)

    self.obj215.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(980.0,1080.0,self.obj215)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0454545454545454]
    else: new_obj = None
    self.obj215.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj215)
    self.globalAndLocalPostcondition(self.obj215, rootNode)
    self.obj215.postAction( rootNode.CREATE )

    self.obj216=CD_Class3(self)
    self.obj216.isGraphObjectVisual = True

    if(hasattr(self.obj216, '_setHierarchicalLink')):
      self.obj216._setHierarchicalLink(False)

    # QOCA
    self.obj216.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj216.Graphical_Appearance.setValue( ('OrganisationalKnArt', self.obj216))

    # name
    self.obj216.name.setValue('OrganisationalKnArt')

    # attributes
    self.obj216.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KA|', 20)
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
    self.obj216.attributes.setValue(lcobj2)

    # Abstract
    self.obj216.Abstract.setValue((None, 0))
    self.obj216.Abstract.config = 0

    # cardinality
    self.obj216.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj216.cardinality.setValue(lcobj2)

    # display
    self.obj216.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj216.display.setHeight(15)

    # Actions
    self.obj216.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj216.Actions.setValue(lcobj2)

    # Constraints
    self.obj216.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj216.Constraints.setValue(lcobj2)

    self.obj216.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(660.0,960.0,self.obj216)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj216.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj216)
    self.globalAndLocalPostcondition(self.obj216, rootNode)
    self.obj216.postAction( rootNode.CREATE )

    self.obj217=CD_Class3(self)
    self.obj217.isGraphObjectVisual = True

    if(hasattr(self.obj217, '_setHierarchicalLink')):
      self.obj217._setHierarchicalLink(False)

    # QOCA
    self.obj217.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj217.Graphical_Appearance.setValue( ('IndividualKnArt', self.obj217))

    # name
    self.obj217.name.setValue('IndividualKnArt')

    # attributes
    self.obj217.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('KA|', 20)
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
    self.obj217.attributes.setValue(lcobj2)

    # Abstract
    self.obj217.Abstract.setValue((None, 0))
    self.obj217.Abstract.config = 0

    # cardinality
    self.obj217.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj217.cardinality.setValue(lcobj2)

    # display
    self.obj217.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj217.display.setHeight(15)

    # Actions
    self.obj217.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj217.Actions.setValue(lcobj2)

    # Constraints
    self.obj217.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj217.Constraints.setValue(lcobj2)

    self.obj217.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1220.0,1000.0,self.obj217)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj217.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj217)
    self.globalAndLocalPostcondition(self.obj217, rootNode)
    self.obj217.postAction( rootNode.CREATE )

    self.obj218=CD_Class3(self)
    self.obj218.isGraphObjectVisual = True

    if(hasattr(self.obj218, '_setHierarchicalLink')):
      self.obj218._setHierarchicalLink(False)

    # QOCA
    self.obj218.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj218.Graphical_Appearance.setValue( ('Strategy', self.obj218))

    # name
    self.obj218.name.setValue('Strategy')

    # attributes
    self.obj218.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
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
    self.obj218.attributes.setValue(lcobj2)

    # Abstract
    self.obj218.Abstract.setValue((None, 1))
    self.obj218.Abstract.config = 0

    # cardinality
    self.obj218.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj218.cardinality.setValue(lcobj2)

    # display
    self.obj218.display.setValue('Attributes:\n  - description :: Text\n  - name :: String\n')
    self.obj218.display.setHeight(15)

    # Actions
    self.obj218.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj218.Actions.setValue(lcobj2)

    # Constraints
    self.obj218.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj218.Constraints.setValue(lcobj2)

    self.obj218.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(80.0,320.0,self.obj218)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0454545454545454]
    else: new_obj = None
    self.obj218.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj218)
    self.globalAndLocalPostcondition(self.obj218, rootNode)
    self.obj218.postAction( rootNode.CREATE )

    self.obj219=CD_Class3(self)
    self.obj219.isGraphObjectVisual = True

    if(hasattr(self.obj219, '_setHierarchicalLink')):
      self.obj219._setHierarchicalLink(False)

    # QOCA
    self.obj219.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj219.Graphical_Appearance.setValue( ('Objective', self.obj219))

    # name
    self.obj219.name.setValue('Objective')

    # attributes
    self.obj219.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('O|', 20)
    cobj2.isDerivedAttribute = False
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
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ofActions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 0, 0, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj219.attributes.setValue(lcobj2)

    # Abstract
    self.obj219.Abstract.setValue((None, 0))
    self.obj219.Abstract.config = 0

    # cardinality
    self.obj219.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj219.cardinality.setValue(lcobj2)

    # display
    self.obj219.display.setValue('Attributes:\n  - ID :: String\n  - Measurement :: Text\n  - Reward :: Text\n  - ofActions :: List\nMultiplicities:\n  - To isPartOfObjective: 0 to N\n  - From isPartOfObjective: 0 to N\n  - From hasObjective: 0 to N\n')
    self.obj219.display.setHeight(15)

    # Actions
    self.obj219.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj219.Actions.setValue(lcobj2)

    # Constraints
    self.obj219.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj219.Constraints.setValue(lcobj2)

    self.obj219.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(40.0,600.0,self.obj219)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.26875, 1.8590163934426231]
    else: new_obj = None
    self.obj219.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj219)
    self.globalAndLocalPostcondition(self.obj219, rootNode)
    self.obj219.postAction( rootNode.CREATE )

    self.obj220=CD_Class3(self)
    self.obj220.isGraphObjectVisual = True

    if(hasattr(self.obj220, '_setHierarchicalLink')):
      self.obj220._setHierarchicalLink(False)

    # QOCA
    self.obj220.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj220.Graphical_Appearance.setValue( ('Process', self.obj220))

    # name
    self.obj220.name.setValue('Process')

    # attributes
    self.obj220.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('P|', 20)
    cobj2.isDerivedAttribute = False
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
    cobj2.setValue(('hasActions', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 0, 0, 1, self.types],ATOM3String)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = True
    lcobj2.append(cobj2)
    self.obj220.attributes.setValue(lcobj2)

    # Abstract
    self.obj220.Abstract.setValue((None, 0))
    self.obj220.Abstract.config = 0

    # cardinality
    self.obj220.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canStartProcess', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasObjective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('isPartOfProcess', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj220.cardinality.setValue(lcobj2)

    # display
    self.obj220.display.setValue('Attributes:\n  - ID :: String\n  - Name :: String\n  - hasActions :: List\nMultiplicities:\n  - From canStartProcess: 0 to N\n  - To hasObjective: 0 to N\n  - From isPartOfProcess: 0 to N\n')
    self.obj220.display.setHeight(15)

    # Actions
    self.obj220.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj220.Actions.setValue(lcobj2)

    # Constraints
    self.obj220.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj220.Constraints.setValue(lcobj2)

    self.obj220.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(220.0,80.0,self.obj220)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.23046875, 1.6524590163934427]
    else: new_obj = None
    self.obj220.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj220)
    self.globalAndLocalPostcondition(self.obj220, rootNode)
    self.obj220.postAction( rootNode.CREATE )

    self.obj221=CD_Association3(self)
    self.obj221.isGraphObjectVisual = True

    if(hasattr(self.obj221, '_setHierarchicalLink')):
      self.obj221._setHierarchicalLink(True)

    # QOCA
    self.obj221.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj221.Graphical_Appearance.setValue( ('isPartOfOrgUnit', self.obj221))
    self.obj221.Graphical_Appearance.linkInfo=linkEditor(self,self.obj221.Graphical_Appearance.semObject, "isPartOfOrgUnit")
    self.obj221.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj221.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj221.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj221.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj221.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj221.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj221.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj221.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj221.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfOrgUnit_1stLink', self.obj221.Graphical_Appearance.linkInfo.FirstLink))
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfOrgUnit_1stSegment', self.obj221.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj221.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj221.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfOrgUnit_Center', self.obj221.Graphical_Appearance.linkInfo))
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfOrgUnit_2ndSegment', self.obj221.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj221.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj221.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj221.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj221.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj221.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj221.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj221.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj221.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj221.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfOrgUnit_2ndLink', self.obj221.Graphical_Appearance.linkInfo.SecondLink))
    self.obj221.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj221.Graphical_Appearance.semObject
    self.obj221.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj221.Graphical_Appearance.semObject
    self.obj221.Graphical_Appearance.linkInfo.Center.semObject=self.obj221.Graphical_Appearance.semObject
    self.obj221.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj221.Graphical_Appearance.semObject
    self.obj221.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj221.Graphical_Appearance.semObject

    # name
    self.obj221.name.setValue('isPartOfOrgUnit')

    # displaySelect
    self.obj221.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj221.displaySelect.config = 0

    # attributes
    self.obj221.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('pOU|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj221.attributes.setValue(lcobj2)

    # cardinality
    self.obj221.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj221.cardinality.setValue(lcobj2)

    # display
    self.obj221.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - From OrgUnit: 1 to N\n  - To OrgUnit: 1 to N\n')
    self.obj221.display.setHeight(15)

    # Actions
    self.obj221.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj221.Actions.setValue(lcobj2)

    # Constraints
    self.obj221.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj221.Constraints.setValue(lcobj2)

    self.obj221.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1386.9955984,65.809726225,self.obj221)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.3548387096774195]
    else: new_obj = None
    self.obj221.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj221)
    self.globalAndLocalPostcondition(self.obj221, rootNode)
    self.obj221.postAction( rootNode.CREATE )

    self.obj222=CD_Association3(self)
    self.obj222.isGraphObjectVisual = True

    if(hasattr(self.obj222, '_setHierarchicalLink')):
      self.obj222._setHierarchicalLink(True)

    # QOCA
    self.obj222.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj222.Graphical_Appearance.setValue( ('canHaveRole', self.obj222))
    self.obj222.Graphical_Appearance.linkInfo=linkEditor(self,self.obj222.Graphical_Appearance.semObject, "canHaveRole")
    self.obj222.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj222.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj222.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj222.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj222.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj222.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj222.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj222.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj222.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canHaveRole_1stLink', self.obj222.Graphical_Appearance.linkInfo.FirstLink))
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canHaveRole_1stSegment', self.obj222.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj222.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj222.Graphical_Appearance.linkInfo.Center.setValue( ('canHaveRole_Center', self.obj222.Graphical_Appearance.linkInfo))
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canHaveRole_2ndSegment', self.obj222.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj222.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj222.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj222.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj222.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj222.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj222.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj222.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj222.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj222.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canHaveRole_2ndLink', self.obj222.Graphical_Appearance.linkInfo.SecondLink))
    self.obj222.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj222.Graphical_Appearance.semObject
    self.obj222.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj222.Graphical_Appearance.semObject
    self.obj222.Graphical_Appearance.linkInfo.Center.semObject=self.obj222.Graphical_Appearance.semObject
    self.obj222.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj222.Graphical_Appearance.semObject
    self.obj222.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj222.Graphical_Appearance.semObject

    # name
    self.obj222.name.setValue('canHaveRole')

    # displaySelect
    self.obj222.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj222.displaySelect.config = 0

    # attributes
    self.obj222.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('OUR|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj222.attributes.setValue(lcobj2)

    # cardinality
    self.obj222.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj222.cardinality.setValue(lcobj2)

    # display
    self.obj222.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - From OrgUnit: 0 to N\n  - To Role: 0 to N\n')
    self.obj222.display.setHeight(15)

    # Actions
    self.obj222.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj222.Actions.setValue(lcobj2)

    # Constraints
    self.obj222.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj222.Constraints.setValue(lcobj2)

    self.obj222.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(971.7601868,527.680947659,self.obj222)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.3548387096774195]
    else: new_obj = None
    self.obj222.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj222)
    self.globalAndLocalPostcondition(self.obj222, rootNode)
    self.obj222.postAction( rootNode.CREATE )

    self.obj223=CD_Association3(self)
    self.obj223.isGraphObjectVisual = True

    if(hasattr(self.obj223, '_setHierarchicalLink')):
      self.obj223._setHierarchicalLink(False)

    # QOCA
    self.obj223.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj223.Graphical_Appearance.setValue( ('hasActions', self.obj223))
    self.obj223.Graphical_Appearance.linkInfo=linkEditor(self,self.obj223.Graphical_Appearance.semObject, "hasActions")
    self.obj223.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj223.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj223.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj223.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj223.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj223.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj223.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj223.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj223.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasActions_1stLink', self.obj223.Graphical_Appearance.linkInfo.FirstLink))
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasActions_1stSegment', self.obj223.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj223.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj223.Graphical_Appearance.linkInfo.Center.setValue( ('hasActions_Center', self.obj223.Graphical_Appearance.linkInfo))
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasActions_2ndSegment', self.obj223.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj223.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj223.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj223.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj223.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj223.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj223.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj223.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj223.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj223.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasActions_2ndLink', self.obj223.Graphical_Appearance.linkInfo.SecondLink))
    self.obj223.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj223.Graphical_Appearance.semObject
    self.obj223.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj223.Graphical_Appearance.semObject
    self.obj223.Graphical_Appearance.linkInfo.Center.semObject=self.obj223.Graphical_Appearance.semObject
    self.obj223.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj223.Graphical_Appearance.semObject
    self.obj223.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj223.Graphical_Appearance.semObject

    # name
    self.obj223.name.setValue('hasActions')

    # displaySelect
    self.obj223.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj223.displaySelect.config = 0

    # attributes
    self.obj223.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('aR|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj223.attributes.setValue(lcobj2)

    # cardinality
    self.obj223.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Action', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    self.obj223.cardinality.setValue(lcobj2)

    # display
    self.obj223.display.setValue('Attributes:\n  - ID :: String\nActions:\n  > updateRoleActions\nMultiplicities:\n  - To Action: 1 to N\n  - From Role: 1 to 1\n')
    self.obj223.display.setHeight(15)

    # Actions
    self.obj223.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('updateRoleActions', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]), 'from CustomCode import UpdateActions\n\nres = UpdateActions(self)\n\n'))
    lcobj2.append(cobj2)
    self.obj223.Actions.setValue(lcobj2)

    # Constraints
    self.obj223.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj223.Constraints.setValue(lcobj2)

    self.obj223.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(517.161248615,904.001803815,self.obj223)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.099, 1.8967741935483875]
    else: new_obj = None
    self.obj223.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj223)
    self.globalAndLocalPostcondition(self.obj223, rootNode)
    self.obj223.postAction( rootNode.CREATE )

    self.obj224=CD_Association3(self)
    self.obj224.isGraphObjectVisual = True

    if(hasattr(self.obj224, '_setHierarchicalLink')):
      self.obj224._setHierarchicalLink(False)

    # QOCA
    self.obj224.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj224.Graphical_Appearance.setValue( ('canAccessKnArt', self.obj224))
    self.obj224.Graphical_Appearance.linkInfo=linkEditor(self,self.obj224.Graphical_Appearance.semObject, "canAccessKnArt")
    self.obj224.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj224.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj224.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj224.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj224.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj224.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj224.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj224.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj224.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canAccessKnArt_1stLink', self.obj224.Graphical_Appearance.linkInfo.FirstLink))
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canAccessKnArt_1stSegment', self.obj224.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj224.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj224.Graphical_Appearance.linkInfo.Center.setValue( ('canAccessKnArt_Center', self.obj224.Graphical_Appearance.linkInfo))
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canAccessKnArt_2ndSegment', self.obj224.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj224.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj224.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj224.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj224.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj224.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj224.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj224.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj224.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj224.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canAccessKnArt_2ndLink', self.obj224.Graphical_Appearance.linkInfo.SecondLink))
    self.obj224.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj224.Graphical_Appearance.semObject
    self.obj224.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj224.Graphical_Appearance.semObject
    self.obj224.Graphical_Appearance.linkInfo.Center.semObject=self.obj224.Graphical_Appearance.semObject
    self.obj224.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj224.Graphical_Appearance.semObject
    self.obj224.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj224.Graphical_Appearance.semObject

    # name
    self.obj224.name.setValue('canAccessKnArt')

    # displaySelect
    self.obj224.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj224.displaySelect.config = 0

    # attributes
    self.obj224.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('accKA|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj224.attributes.setValue(lcobj2)

    # cardinality
    self.obj224.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj224.cardinality.setValue(lcobj2)

    # display
    self.obj224.display.setValue('Attributes:\n  - ID :: String\nConstraints:\n  > ConstraintKnArt\nMultiplicities:\n  - To OrganisationalKnArt: 0 to N\n  - From Role: 0 to N\n  - From OrgUnit: 0 to N\n  - To IndividualKnArt: 0 to N\n')
    self.obj224.display.setHeight(15)

    # Actions
    self.obj224.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj224.Actions.setValue(lcobj2)

    # Constraints
    self.obj224.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = canAccessKnArtCheckConnections(self)\n\nif res is "eitherRoleOrUnit":\n    return ("Either Role of OrgUnit can access knowledge.", self.graphObject_)\nelif res is "onlyOneInput":\n    return ("Only one Role or OrgUnit can access one knowledge medium.", self.graphObject_)\nelif res is "RoleWithOrgOnly":\n    return ("Role can access OrganisationalKnArt only!", self.graphObject_)\nelif res is "OrgUnitWithIndivOnly":\n    return ("OrgUnit can access IndividualKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj224.Constraints.setValue(lcobj2)

    self.obj224.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1126.462784,833.548234957,self.obj224)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.6380000000000001, 2.438709677419355]
    else: new_obj = None
    self.obj224.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj224)
    self.globalAndLocalPostcondition(self.obj224, rootNode)
    self.obj224.postAction( rootNode.CREATE )

    self.obj225=CD_Association3(self)
    self.obj225.isGraphObjectVisual = True

    if(hasattr(self.obj225, '_setHierarchicalLink')):
      self.obj225._setHierarchicalLink(True)

    # QOCA
    self.obj225.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj225.Graphical_Appearance.setValue( ('isPartOfObjective', self.obj225))
    self.obj225.Graphical_Appearance.linkInfo=linkEditor(self,self.obj225.Graphical_Appearance.semObject, "isPartOfObjective")
    self.obj225.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj225.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj225.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj225.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj225.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj225.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj225.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj225.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj225.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfObjective_1stLink', self.obj225.Graphical_Appearance.linkInfo.FirstLink))
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfObjective_1stSegment', self.obj225.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj225.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj225.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfObjective_Center', self.obj225.Graphical_Appearance.linkInfo))
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfObjective_2ndSegment', self.obj225.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj225.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj225.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj225.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj225.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj225.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj225.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj225.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj225.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj225.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfObjective_2ndLink', self.obj225.Graphical_Appearance.linkInfo.SecondLink))
    self.obj225.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj225.Graphical_Appearance.semObject
    self.obj225.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj225.Graphical_Appearance.semObject
    self.obj225.Graphical_Appearance.linkInfo.Center.semObject=self.obj225.Graphical_Appearance.semObject
    self.obj225.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj225.Graphical_Appearance.semObject
    self.obj225.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj225.Graphical_Appearance.semObject

    # name
    self.obj225.name.setValue('isPartOfObjective')

    # displaySelect
    self.obj225.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj225.displaySelect.config = 0

    # attributes
    self.obj225.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('pO|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj225.attributes.setValue(lcobj2)

    # cardinality
    self.obj225.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj225.cardinality.setValue(lcobj2)

    # display
    self.obj225.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - From Objective: 0 to N\n  - To Objective: 0 to N\n')
    self.obj225.display.setHeight(15)

    # Actions
    self.obj225.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj225.Actions.setValue(lcobj2)

    # Constraints
    self.obj225.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj225.Constraints.setValue(lcobj2)

    self.obj225.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(131.944046519,946.91223085,self.obj225)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.225, 1.3548387096774195]
    else: new_obj = None
    self.obj225.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj225)
    self.globalAndLocalPostcondition(self.obj225, rootNode)
    self.obj225.postAction( rootNode.CREATE )

    self.obj226=CD_Association3(self)
    self.obj226.isGraphObjectVisual = True

    if(hasattr(self.obj226, '_setHierarchicalLink')):
      self.obj226._setHierarchicalLink(False)

    # QOCA
    self.obj226.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj226.Graphical_Appearance.setValue( ('hasObjective', self.obj226))
    self.obj226.Graphical_Appearance.linkInfo=linkEditor(self,self.obj226.Graphical_Appearance.semObject, "hasObjective")
    self.obj226.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj226.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj226.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj226.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj226.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj226.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj226.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj226.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj226.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasObjective_1stLink', self.obj226.Graphical_Appearance.linkInfo.FirstLink))
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasObjective_1stSegment', self.obj226.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj226.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj226.Graphical_Appearance.linkInfo.Center.setValue( ('hasObjective_Center', self.obj226.Graphical_Appearance.linkInfo))
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasObjective_2ndSegment', self.obj226.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj226.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj226.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj226.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj226.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj226.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj226.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj226.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj226.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj226.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasObjective_2ndLink', self.obj226.Graphical_Appearance.linkInfo.SecondLink))
    self.obj226.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj226.Graphical_Appearance.semObject
    self.obj226.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj226.Graphical_Appearance.semObject
    self.obj226.Graphical_Appearance.linkInfo.Center.semObject=self.obj226.Graphical_Appearance.semObject
    self.obj226.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj226.Graphical_Appearance.semObject
    self.obj226.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj226.Graphical_Appearance.semObject

    # name
    self.obj226.name.setValue('hasObjective')

    # displaySelect
    self.obj226.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj226.displaySelect.config = 0

    # attributes
    self.obj226.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('RPO|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj226.attributes.setValue(lcobj2)

    # cardinality
    self.obj226.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    cobj2=ATOM3Connection()
    cobj2.setValue(('Action', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj226.cardinality.setValue(lcobj2)

    # display
    self.obj226.display.setValue('Attributes:\n  - ID :: String\nActions:\n  > updateObjectiveActions\nMultiplicities:\n  - To Objective: 1 to N\n  - From Role: 0 to N\n  - From Process: 0 to N\n  - From Action: 0 to N\n')
    self.obj226.display.setHeight(15)

    # Actions
    self.obj226.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('updateObjectiveActions', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]), 'from CustomCode import UpdateActions\n\nres = UpdateActions(self)\n'))
    lcobj2.append(cobj2)
    self.obj226.Actions.setValue(lcobj2)

    # Constraints
    self.obj226.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj226.Constraints.setValue(lcobj2)

    self.obj226.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(436.73445957,632.859445861,self.obj226)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.33, 2.438709677419355]
    else: new_obj = None
    self.obj226.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj226)
    self.globalAndLocalPostcondition(self.obj226, rootNode)
    self.obj226.postAction( rootNode.CREATE )

    self.obj227=CD_Association3(self)
    self.obj227.isGraphObjectVisual = True

    if(hasattr(self.obj227, '_setHierarchicalLink')):
      self.obj227._setHierarchicalLink(False)

    # QOCA
    self.obj227.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj227.Graphical_Appearance.setValue( ('genericAssociation', self.obj227))
    self.obj227.Graphical_Appearance.linkInfo=linkEditor(self,self.obj227.Graphical_Appearance.semObject, "genericAssociation")
    self.obj227.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj227.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj227.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj227.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj227.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj227.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj227.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj227.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj227.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('genericAssociation_1stLink', self.obj227.Graphical_Appearance.linkInfo.FirstLink))
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('genericAssociation_1stSegment', self.obj227.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj227.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj227.Graphical_Appearance.linkInfo.Center.setValue( ('genericAssociation_Center', self.obj227.Graphical_Appearance.linkInfo))
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('genericAssociation_2ndSegment', self.obj227.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj227.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj227.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj227.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj227.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj227.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj227.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj227.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj227.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj227.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('genericAssociation_2ndLink', self.obj227.Graphical_Appearance.linkInfo.SecondLink))
    self.obj227.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj227.Graphical_Appearance.semObject
    self.obj227.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj227.Graphical_Appearance.semObject
    self.obj227.Graphical_Appearance.linkInfo.Center.semObject=self.obj227.Graphical_Appearance.semObject
    self.obj227.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj227.Graphical_Appearance.semObject
    self.obj227.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj227.Graphical_Appearance.semObject

    # name
    self.obj227.name.setValue('genericAssociation')

    # displaySelect
    self.obj227.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj227.displaySelect.config = 0

    # attributes
    self.obj227.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Description', 'Text', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Text('\n', 80,10 )
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('genR|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj227.attributes.setValue(lcobj2)

    # cardinality
    self.obj227.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj227.cardinality.setValue(lcobj2)

    # display
    self.obj227.display.setValue('Attributes:\n  - name :: String\n  - Description :: Text\n  - ID :: String\nMultiplicities:\n  - To Role: 1 to N\n  - From Role: 1 to N\n')
    self.obj227.display.setHeight(15)

    # Actions
    self.obj227.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj227.Actions.setValue(lcobj2)

    # Constraints
    self.obj227.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj227.Constraints.setValue(lcobj2)

    self.obj227.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1028.0,327.0,self.obj227)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.015, 1.8967741935483875]
    else: new_obj = None
    self.obj227.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj227)
    self.globalAndLocalPostcondition(self.obj227, rootNode)
    self.obj227.postAction( rootNode.CREATE )

    self.obj228=CD_Association3(self)
    self.obj228.isGraphObjectVisual = True

    if(hasattr(self.obj228, '_setHierarchicalLink')):
      self.obj228._setHierarchicalLink(True)

    # QOCA
    self.obj228.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj228.Graphical_Appearance.setValue( ('answersToRole', self.obj228))
    self.obj228.Graphical_Appearance.linkInfo=linkEditor(self,self.obj228.Graphical_Appearance.semObject, "answersToRole")
    self.obj228.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj228.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj228.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj228.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj228.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj228.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj228.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj228.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj228.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToRole_1stLink', self.obj228.Graphical_Appearance.linkInfo.FirstLink))
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToRole_1stSegment', self.obj228.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj228.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj228.Graphical_Appearance.linkInfo.Center.setValue( ('answersToRole_Center', self.obj228.Graphical_Appearance.linkInfo))
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToRole_2ndSegment', self.obj228.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj228.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj228.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj228.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj228.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj228.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj228.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj228.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj228.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj228.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToRole_2ndLink', self.obj228.Graphical_Appearance.linkInfo.SecondLink))
    self.obj228.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj228.Graphical_Appearance.semObject
    self.obj228.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj228.Graphical_Appearance.semObject
    self.obj228.Graphical_Appearance.linkInfo.Center.semObject=self.obj228.Graphical_Appearance.semObject
    self.obj228.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj228.Graphical_Appearance.semObject
    self.obj228.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj228.Graphical_Appearance.semObject

    # name
    self.obj228.name.setValue('answersToRole')

    # displaySelect
    self.obj228.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj228.displaySelect.config = 0

    # attributes
    self.obj228.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('hR|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj228.attributes.setValue(lcobj2)

    # cardinality
    self.obj228.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj228.cardinality.setValue(lcobj2)

    # display
    self.obj228.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - From Role: 1 to N\n  - To Role: 1 to N\n')
    self.obj228.display.setHeight(15)

    # Actions
    self.obj228.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj228.Actions.setValue(lcobj2)

    # Constraints
    self.obj228.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj228.Constraints.setValue(lcobj2)

    self.obj228.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(887.0,133.0,self.obj228)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.3548387096774195]
    else: new_obj = None
    self.obj228.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj228)
    self.globalAndLocalPostcondition(self.obj228, rootNode)
    self.obj228.postAction( rootNode.CREATE )

    self.obj229=CD_Association3(self)
    self.obj229.isGraphObjectVisual = True

    if(hasattr(self.obj229, '_setHierarchicalLink')):
      self.obj229._setHierarchicalLink(False)

    # QOCA
    self.obj229.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj229.Graphical_Appearance.setValue( ('canStartProcess', self.obj229))
    self.obj229.Graphical_Appearance.linkInfo=linkEditor(self,self.obj229.Graphical_Appearance.semObject, "canStartProcess")
    self.obj229.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj229.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj229.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj229.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj229.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj229.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj229.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj229.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj229.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canStartProcess_1stLink', self.obj229.Graphical_Appearance.linkInfo.FirstLink))
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canStartProcess_1stSegment', self.obj229.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj229.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj229.Graphical_Appearance.linkInfo.Center.setValue( ('canStartProcess_Center', self.obj229.Graphical_Appearance.linkInfo))
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canStartProcess_2ndSegment', self.obj229.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj229.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj229.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj229.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj229.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj229.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj229.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj229.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj229.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj229.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canStartProcess_2ndLink', self.obj229.Graphical_Appearance.linkInfo.SecondLink))
    self.obj229.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj229.Graphical_Appearance.semObject
    self.obj229.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj229.Graphical_Appearance.semObject
    self.obj229.Graphical_Appearance.linkInfo.Center.semObject=self.obj229.Graphical_Appearance.semObject
    self.obj229.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj229.Graphical_Appearance.semObject
    self.obj229.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj229.Graphical_Appearance.semObject

    # name
    self.obj229.name.setValue('canStartProcess')

    # displaySelect
    self.obj229.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj229.displaySelect.config = 0

    # attributes
    self.obj229.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('RP|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj229.attributes.setValue(lcobj2)

    # cardinality
    self.obj229.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Process', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj229.cardinality.setValue(lcobj2)

    # display
    self.obj229.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - To Process: 0 to N\n  - From Role: 0 to N\n')
    self.obj229.display.setHeight(15)

    # Actions
    self.obj229.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj229.Actions.setValue(lcobj2)

    # Constraints
    self.obj229.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj229.Constraints.setValue(lcobj2)

    self.obj229.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(470.4921875,411.163934426,self.obj229)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.036, 1.3548387096774195]
    else: new_obj = None
    self.obj229.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj229)
    self.globalAndLocalPostcondition(self.obj229, rootNode)
    self.obj229.postAction( rootNode.CREATE )

    self.obj230=CD_Association3(self)
    self.obj230.isGraphObjectVisual = True

    if(hasattr(self.obj230, '_setHierarchicalLink')):
      self.obj230._setHierarchicalLink(True)

    # QOCA
    self.obj230.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj230.Graphical_Appearance.setValue( ('answersToOrgUnit', self.obj230))
    self.obj230.Graphical_Appearance.linkInfo=linkEditor(self,self.obj230.Graphical_Appearance.semObject, "answersToOrgUnit")
    self.obj230.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj230.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj230.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj230.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj230.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj230.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj230.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj230.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj230.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToOrgUnit_1stLink', self.obj230.Graphical_Appearance.linkInfo.FirstLink))
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToOrgUnit_1stSegment', self.obj230.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj230.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj230.Graphical_Appearance.linkInfo.Center.setValue( ('answersToOrgUnit_Center', self.obj230.Graphical_Appearance.linkInfo))
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToOrgUnit_2ndSegment', self.obj230.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj230.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj230.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj230.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj230.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj230.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj230.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj230.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj230.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj230.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToOrgUnit_2ndLink', self.obj230.Graphical_Appearance.linkInfo.SecondLink))
    self.obj230.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj230.Graphical_Appearance.semObject
    self.obj230.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj230.Graphical_Appearance.semObject
    self.obj230.Graphical_Appearance.linkInfo.Center.semObject=self.obj230.Graphical_Appearance.semObject
    self.obj230.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj230.Graphical_Appearance.semObject
    self.obj230.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj230.Graphical_Appearance.semObject

    # name
    self.obj230.name.setValue('answersToOrgUnit')

    # displaySelect
    self.obj230.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj230.displaySelect.config = 0

    # attributes
    self.obj230.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('hOU|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj230.attributes.setValue(lcobj2)

    # cardinality
    self.obj230.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj230.cardinality.setValue(lcobj2)

    # display
    self.obj230.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - To OrgUnit: 1 to N\n  - From OrgUnit: 1 to N\n')
    self.obj230.display.setHeight(15)

    # Actions
    self.obj230.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj230.Actions.setValue(lcobj2)

    # Constraints
    self.obj230.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj230.Constraints.setValue(lcobj2)

    self.obj230.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1113.0,79.0,self.obj230)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.3548387096774195]
    else: new_obj = None
    self.obj230.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj230)
    self.globalAndLocalPostcondition(self.obj230, rootNode)
    self.obj230.postAction( rootNode.CREATE )

    self.obj231=CD_Association3(self)
    self.obj231.isGraphObjectVisual = True

    if(hasattr(self.obj231, '_setHierarchicalLink')):
      self.obj231._setHierarchicalLink(True)

    # QOCA
    self.obj231.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj231.Graphical_Appearance.setValue( ('isPartOfRole', self.obj231))
    self.obj231.Graphical_Appearance.linkInfo=linkEditor(self,self.obj231.Graphical_Appearance.semObject, "isPartOfRole")
    self.obj231.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj231.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj231.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj231.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj231.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj231.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj231.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj231.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj231.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfRole_1stLink', self.obj231.Graphical_Appearance.linkInfo.FirstLink))
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfRole_1stSegment', self.obj231.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj231.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj231.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfRole_Center', self.obj231.Graphical_Appearance.linkInfo))
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfRole_2ndSegment', self.obj231.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],0,0)
    self.obj231.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj231.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj231.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj231.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj231.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj231.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj231.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj231.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj231.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfRole_2ndLink', self.obj231.Graphical_Appearance.linkInfo.SecondLink))
    self.obj231.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj231.Graphical_Appearance.semObject
    self.obj231.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj231.Graphical_Appearance.semObject
    self.obj231.Graphical_Appearance.linkInfo.Center.semObject=self.obj231.Graphical_Appearance.semObject
    self.obj231.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj231.Graphical_Appearance.semObject
    self.obj231.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj231.Graphical_Appearance.semObject

    # name
    self.obj231.name.setValue('isPartOfRole')

    # displaySelect
    self.obj231.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj231.displaySelect.config = 0

    # attributes
    self.obj231.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('pR|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj231.attributes.setValue(lcobj2)

    # cardinality
    self.obj231.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj231.cardinality.setValue(lcobj2)

    # display
    self.obj231.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - From Role: 0 to N\n  - To Role: 0 to N\n')
    self.obj231.display.setHeight(15)

    # Actions
    self.obj231.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj231.Actions.setValue(lcobj2)

    # Constraints
    self.obj231.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj231.Constraints.setValue(lcobj2)

    self.obj231.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(675.0,160.0,self.obj231)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.3548387096774195]
    else: new_obj = None
    self.obj231.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj231)
    self.globalAndLocalPostcondition(self.obj231, rootNode)
    self.obj231.postAction( rootNode.CREATE )

    self.obj232=CD_Association3(self)
    self.obj232.isGraphObjectVisual = True

    if(hasattr(self.obj232, '_setHierarchicalLink')):
      self.obj232._setHierarchicalLink(False)

    # QOCA
    self.obj232.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj232.Graphical_Appearance.setValue( ('isPartOfProcess', self.obj232))
    self.obj232.Graphical_Appearance.linkInfo=linkEditor(self,self.obj232.Graphical_Appearance.semObject, "isPartOfProcess")
    self.obj232.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj232.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj232.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj232.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj232.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj232.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj232.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj232.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj232.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfProcess_1stLink', self.obj232.Graphical_Appearance.linkInfo.FirstLink))
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfProcess_1stSegment', self.obj232.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj232.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj232.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfProcess_Center', self.obj232.Graphical_Appearance.linkInfo))
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfProcess_2ndSegment', self.obj232.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj232.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj232.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj232.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj232.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj232.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj232.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj232.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj232.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj232.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfProcess_2ndLink', self.obj232.Graphical_Appearance.linkInfo.SecondLink))
    self.obj232.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj232.Graphical_Appearance.semObject
    self.obj232.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj232.Graphical_Appearance.semObject
    self.obj232.Graphical_Appearance.linkInfo.Center.semObject=self.obj232.Graphical_Appearance.semObject
    self.obj232.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj232.Graphical_Appearance.semObject
    self.obj232.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj232.Graphical_Appearance.semObject

    # name
    self.obj232.name.setValue('isPartOfProcess')

    # displaySelect
    self.obj232.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj232.displaySelect.config = 0

    # attributes
    self.obj232.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('AP|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj232.attributes.setValue(lcobj2)

    # cardinality
    self.obj232.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Action', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Process', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj232.cardinality.setValue(lcobj2)

    # display
    self.obj232.display.setValue('Attributes:\n  - ID :: String\nActions:\n  > updateProcessActions\nMultiplicities:\n  - From Action: 0 to N\n  - To Process: 0 to N\n')
    self.obj232.display.setHeight(15)

    # Actions
    self.obj232.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('updateProcessActions', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]), 'from CustomCode import UpdateActions\n\nres = UpdateActions(self)\n\n\n'))
    lcobj2.append(cobj2)
    self.obj232.Actions.setValue(lcobj2)

    # Constraints
    self.obj232.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj232.Constraints.setValue(lcobj2)

    self.obj232.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(319.0,939.0,self.obj232)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2670000000000001, 1.8967741935483875]
    else: new_obj = None
    self.obj232.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj232)
    self.globalAndLocalPostcondition(self.obj232, rootNode)
    self.obj232.postAction( rootNode.CREATE )

    self.obj233=CD_Inheritance3(self)
    self.obj233.isGraphObjectVisual = True

    if(hasattr(self.obj233, '_setHierarchicalLink')):
      self.obj233._setHierarchicalLink(False)

    self.obj233.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(863.21888986,1199.92763695,self.obj233)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj233.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj233)
    self.globalAndLocalPostcondition(self.obj233, rootNode)
    self.obj233.postAction( rootNode.CREATE )

    self.obj234=CD_Inheritance3(self)
    self.obj234.isGraphObjectVisual = True

    if(hasattr(self.obj234, '_setHierarchicalLink')):
      self.obj234._setHierarchicalLink(False)

    self.obj234.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1278.90914946,1212.75085967,self.obj234)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj234.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj234)
    self.globalAndLocalPostcondition(self.obj234, rootNode)
    self.obj234.postAction( rootNode.CREATE )

    self.obj235=CD_Inheritance3(self)
    self.obj235.isGraphObjectVisual = True

    if(hasattr(self.obj235, '_setHierarchicalLink')):
      self.obj235._setHierarchicalLink(False)

    self.obj235.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(152.858254695,586.846159545,self.obj235)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj235.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj235)
    self.globalAndLocalPostcondition(self.obj235, rootNode)
    self.obj235.postAction( rootNode.CREATE )

    self.obj236=CD_Inheritance3(self)
    self.obj236.isGraphObjectVisual = True

    if(hasattr(self.obj236, '_setHierarchicalLink')):
      self.obj236._setHierarchicalLink(False)

    self.obj236.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(135.466796875,193.786885246,self.obj236)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj236.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj236)
    self.globalAndLocalPostcondition(self.obj236, rootNode)
    self.obj236.postAction( rootNode.CREATE )

    # Connections for obj212 (graphObject_: Obj248) named OrgUnit
    self.drawConnections(
(self.obj212,self.obj221,[1368.8125, 221.22950819672127, 1386.9955983980042, 65.8097262245276, 1386.9955984, 65.809726225],"true", 3),
(self.obj212,self.obj222,[1241.14453125, 515.5737704918033, 967.8422485527899, 481.40176688146084, 971.7601868, 527.680947659],"true", 3),
(self.obj212,self.obj224,[1241.14453125, 515.5737704918033, 1017.8287423035672, 504.3266545159663, 1126.462784, 833.548234957],"true", 3),
(self.obj212,self.obj230,[1280.0, 221.22950819672127, 1130.0, 231.0, 1113.0, 79.0], 0, 3) )
    # Connections for obj213 (graphObject_: Obj249) named Role
    self.drawConnections(
(self.obj213,self.obj223,[660.0, 791.0, 555.1631302538499, 835.356649681594, 532.161248615, 913.001803815],"true", 3),
(self.obj213,self.obj224,[832.921875, 715.2622950819672, 1043.5805784296024, 726.1457487347751, 1126.462784, 833.548234957],"true", 3),
(self.obj213,self.obj226,[620.953125, 506.7377049180328, 522.0012232889502, 553.7739542825374, 436.73445957, 632.859445861],"true", 3),
(self.obj213,self.obj227,[832.921875, 412.3114754098361, 1028.0, 327.0], 0, 2),
(self.obj213,self.obj228,[793.875, 260.8360655737705, 887.0, 133.0], 0, 2),
(self.obj213,self.obj229,[620.953125, 405.5245901639344, 470.4921875, 411.163934426], 0, 2),
(self.obj213,self.obj231,[660.0, 260.8360655737705, 675.0, 160.0],"true", 2) )
    # Connections for obj214 (graphObject_: Obj250) named Action
    self.drawConnections(
(self.obj214,self.obj232,[419.0, 1051.655737704918, 319.0, 939.0],"true", 2),
(self.obj214,self.obj226,[421.0, 1080.7377049180327, 436.73445957, 632.859445861],"true", 2) )
    # Connections for obj215 (graphObject_: Obj251) named KnowledgeArtifacts
    self.drawConnections(
 )
    # Connections for obj216 (graphObject_: Obj252) named OrganisationalKnArt
    self.drawConnections(
(self.obj216,self.obj233,[852.3125, 1107.0, 863.21888986, 1199.92763695],"true", 2) )
    # Connections for obj217 (graphObject_: Obj253) named IndividualKnArt
    self.drawConnections(
(self.obj217,self.obj234,[1264.0, 1147.0, 1278.90914946, 1212.75085967],"true", 2) )
    # Connections for obj218 (graphObject_: Obj254) named Strategy
    self.drawConnections(
 )
    # Connections for obj219 (graphObject_: Obj255) named Objective
    self.drawConnections(
(self.obj219,self.obj235,[135.75, 600.5737704918033, 152.858254695, 586.846159545],"true", 2),
(self.obj219,self.obj225,[139.75, 803.0, 131.94404651894035, 946.9122308488277, 131.944046519, 946.91223085],"true", 3) )
    # Connections for obj220 (graphObject_: Obj256) named Process
    self.drawConnections(
(self.obj220,self.obj226,[313.21875, 283.0, 333.0, 453.0, 436.73445957, 632.859445861],"true", 3),
(self.obj220,self.obj236,[220.93359375, 178.89508196721312, 135.466796875, 193.786885246],"true", 2) )
    # Connections for obj221 (graphObject_: Obj257) named isPartOfOrgUnit
    self.drawConnections(
(self.obj221,self.obj212,[1386.9955984, 65.809726225, 1386.9955983980042, 65.8097262245276, 1368.8125, 221.22950819672127],"true", 3) )
    # Connections for obj222 (graphObject_: Obj259) named canHaveRole
    self.drawConnections(
(self.obj222,self.obj213,[971.7601868, 527.680947659, 975.67812505129, 573.9601284363068, 832.921875, 620.5901639344263],"true", 3) )
    # Connections for obj223 (graphObject_: Obj261) named hasActions
    self.drawConnections(
(self.obj223,self.obj214,[532.161248615, 913.001803815, 494.1593669760688, 981.6469579482074, 498.8125, 1053.4918032786886],"true", 3) )
    # Connections for obj224 (graphObject_: Obj263) named canAccessKnArt
    self.drawConnections(
(self.obj224,self.obj216,[1126.462784, 833.548234957, 1148.2678325033444, 899.9439489105719, 895.5703125, 1002.4545454545455],"true", 3),
(self.obj224,self.obj217,[1126.462784, 833.548234957, 1053.4035107781324, 935.4763808302594, 1220.7421875, 1042.4545454545455],"true", 3) )
    # Connections for obj225 (graphObject_: Obj265) named isPartOfObjective
    self.drawConnections(
(self.obj225,self.obj219,[131.944046519, 946.91223085, 131.94404651894035, 946.9122308488277, 139.75, 803.0],"true", 3) )
    # Connections for obj226 (graphObject_: Obj267) named hasObjective
    self.drawConnections(
(self.obj226,self.obj219,[436.73445957, 632.859445861, 351.4676958509182, 711.9449374392455, 281.65625, 713.0229508196721],"true", 3) )
    # Connections for obj227 (graphObject_: Obj269) named genericAssociation
    self.drawConnections(
(self.obj227,self.obj213,[1028.0, 327.0, 832.921875, 412.3114754098361], 0, 2) )
    # Connections for obj228 (graphObject_: Obj271) named answersToRole
    self.drawConnections(
(self.obj228,self.obj213,[887.0, 133.0, 793.875, 260.8360655737705], 0, 2) )
    # Connections for obj229 (graphObject_: Obj273) named canStartProcess
    self.drawConnections(
(self.obj229,self.obj220,[470.4921875, 411.163934426, 411.65625, 283.0], 0, 2) )
    # Connections for obj230 (graphObject_: Obj275) named answersToOrgUnit
    self.drawConnections(
(self.obj230,self.obj212,[1113.0, 79.0, 1279.0, 145.0, 1280.0, 221.22950819672127], 0, 3) )
    # Connections for obj231 (graphObject_: Obj277) named isPartOfRole
    self.drawConnections(
(self.obj231,self.obj213,[675.0, 160.0, 660.0, 260.8360655737705],"true", 2) )
    # Connections for obj232 (graphObject_: Obj279) named isPartOfProcess
    self.drawConnections(
(self.obj232,self.obj220,[319.0, 939.0, 313.21875, 312.0],"true", 2) )
    # Connections for obj233 (graphObject_: Obj281) of type CD_Inheritance3
    self.drawConnections(
(self.obj233,self.obj215,[863.21888986, 1199.92763695, 981.0, 1199.2295081967213],"true", 2) )
    # Connections for obj234 (graphObject_: Obj283) of type CD_Inheritance3
    self.drawConnections(
(self.obj234,self.obj215,[1278.90914946, 1212.75085967, 1171.0, 1199.2295081967213],"true", 2) )
    # Connections for obj235 (graphObject_: Obj285) of type CD_Inheritance3
    self.drawConnections(
(self.obj235,self.obj218,[152.858254695, 586.846159545, 156.0, 495.0],"true", 2) )
    # Connections for obj236 (graphObject_: Obj287) of type CD_Inheritance3
    self.drawConnections(
(self.obj236,self.obj218,[135.466796875, 193.786885246, 116.0, 320.6363636363636],"true", 2) )

newfunction = LSMASOMM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
