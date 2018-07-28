"""
__LSMASOMM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Fri Feb  2 01:44:47 2018
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


    self.obj52=CD_Class3(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # QOCA
    self.obj52.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj52.Graphical_Appearance.setValue( ('OrgUnit', self.obj52))

    # name
    self.obj52.name.setValue('OrgUnit')

    # attributes
    self.obj52.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj52.attributes.setValue(lcobj2)

    # Abstract
    self.obj52.Abstract.setValue((None, 0))
    self.obj52.Abstract.config = 0

    # cardinality
    self.obj52.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj52.cardinality.setValue(lcobj2)

    # display
    self.obj52.display.setValue('Attributes:\n  - ID :: String\n  - Individual :: Boolean\n  - UnitSize :: String\n  - hasActions :: List\n  - name :: String\nConstraints:\n  > ConstraintOutputOrgUnit\nActions:\n  > determineSize\nMultiplicities:\n  - To isPartOfOrgUnit: 0 to N\n  - From isPartOfOrgUnit: 0 to N\n  - To canHaveRole: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To answersToOrgUnit: 0 to N\n  - From answersToOrgUnit: 0 to N\n')
    self.obj52.display.setHeight(15)

    # Actions
    self.obj52.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('determineSize', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitDetermineSize(self)\nself.UnitSize.setValue(res)\nself.graphObject_.ModifyAttribute(\'UnitSize\', res)\n\n'))
    lcobj2.append(cobj2)
    self.obj52.Actions.setValue(lcobj2)

    # Constraints
    self.obj52.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintOutputOrgUnit', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitCheckOutputs(self)\nif res is "manyKnArts":\n    return ("OrgUnit can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj52.Constraints.setValue(lcobj2)

    self.obj52.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,220.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.88
       new_obj.layConstraints['scale'] = [1.11015625, 2.9262295081967213]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=CD_Class3(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # QOCA
    self.obj53.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj53.Graphical_Appearance.setValue( ('Role', self.obj53))

    # name
    self.obj53.name.setValue('Role')

    # attributes
    self.obj53.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj53.attributes.setValue(lcobj2)

    # Abstract
    self.obj53.Abstract.setValue((None, 0))
    self.obj53.Abstract.config = 0

    # cardinality
    self.obj53.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj53.cardinality.setValue(lcobj2)

    # display
    self.obj53.display.setValue('Attributes:\n  - ID :: String\n  - hasActions :: List\n  - isMetaRole :: Boolean\n  - name :: String\nConstraints:\n  > RoleConstraintKnArt\nActions:\n  > checkMetaRole\nMultiplicities:\n  - From canHaveRole: 0 to N\n  - To hasActions: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To hasObjective: 0 to N\n  - To genericAssociation: 0 to N\n  - From genericAssociation: 0 to N\n  - To answersToRole: 0 to N\n  - From answersToRole: 0 to N\n  - To canStartProcess: 0 to N\n  - To isPartOfRole: 0 to N\n  - From isPartOfRole: 0 to N\n')
    self.obj53.display.setHeight(15)

    # Actions
    self.obj53.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('checkMetaRole', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]), 'from CustomCode import RoleHierarchy\nres = RoleHierarchy(self)\n\n'))
    lcobj2.append(cobj2)
    self.obj53.Actions.setValue(lcobj2)

    # Constraints
    self.obj53.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('RoleConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '\nfrom CustomCode import *\n\nres = RoleCheckOutputs(self)\nif res is "manyKnArts":\n    return ("Roles can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelif res is "IndivKnArtError":\n    return ("Roles can have OrganizationalKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj53.Constraints.setValue(lcobj2)

    self.obj53.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(760.0,260.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.115625, 3.6147540983606556]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=CD_Class3(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # QOCA
    self.obj54.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj54.Graphical_Appearance.setValue( ('Action', self.obj54))

    # name
    self.obj54.name.setValue('Action')

    # attributes
    self.obj54.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj54.attributes.setValue(lcobj2)

    # Abstract
    self.obj54.Abstract.setValue((None, 0))
    self.obj54.Abstract.config = 0

    # cardinality
    self.obj54.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj54.cardinality.setValue(lcobj2)

    # display
    self.obj54.display.setValue('Attributes:\n  - ActionCode :: Text\n  - ID :: String\n  - name :: String\nActions:\n  > initialActionCodeTemplate\nMultiplicities:\n  - From hasActions: 0 to N\n  - To isPartOfProcess: 0 to N\n  - To hasObjective: 0 to N\n')
    self.obj54.display.setHeight(15)

    # Actions
    self.obj54.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('initialActionCodeTemplate', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import ActionCodeTemplate\n\nres = ActionCodeTemplate(self)\n\nself.setAttrValue(\'ActionCode\', res)\n\n\n'))
    lcobj2.append(cobj2)
    self.obj54.Actions.setValue(lcobj2)

    # Constraints
    self.obj54.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj54.Constraints.setValue(lcobj2)

    self.obj54.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(330.0,420.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.06
       new_obj.layConstraints['scale'] = [1.1484375, 2.0655737704918034]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=CD_Class3(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # QOCA
    self.obj55.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj55.Graphical_Appearance.setValue( ('KnowledgeArtifacts', self.obj55))

    # name
    self.obj55.name.setValue('KnowledgeArtifacts')

    # attributes
    self.obj55.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj55.attributes.setValue(lcobj2)

    # Abstract
    self.obj55.Abstract.setValue((None, 1))
    self.obj55.Abstract.config = 0

    # cardinality
    self.obj55.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj55.cardinality.setValue(lcobj2)

    # display
    self.obj55.display.setValue('Attributes:\n  - ID :: String\n  - description :: String\n  - name :: String\n')
    self.obj55.display.setHeight(15)

    # Actions
    self.obj55.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj55.Actions.setValue(lcobj2)

    # Constraints
    self.obj55.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj55.Constraints.setValue(lcobj2)

    self.obj55.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(680.0,860.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0454545454545454]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=CD_Class3(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # QOCA
    self.obj56.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj56.Graphical_Appearance.setValue( ('OrganisationalKnArt', self.obj56))

    # name
    self.obj56.name.setValue('OrganisationalKnArt')

    # attributes
    self.obj56.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj56.attributes.setValue(lcobj2)

    # Abstract
    self.obj56.Abstract.setValue((None, 0))
    self.obj56.Abstract.config = 0

    # cardinality
    self.obj56.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj56.cardinality.setValue(lcobj2)

    # display
    self.obj56.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj56.display.setHeight(15)

    # Actions
    self.obj56.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj56.Actions.setValue(lcobj2)

    # Constraints
    self.obj56.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj56.Constraints.setValue(lcobj2)

    self.obj56.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(931.0,782.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=CD_Class3(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # QOCA
    self.obj57.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj57.Graphical_Appearance.setValue( ('IndividualKnArt', self.obj57))

    # name
    self.obj57.name.setValue('IndividualKnArt')

    # attributes
    self.obj57.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj57.attributes.setValue(lcobj2)

    # Abstract
    self.obj57.Abstract.setValue((None, 0))
    self.obj57.Abstract.config = 0

    # cardinality
    self.obj57.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj57.cardinality.setValue(lcobj2)

    # display
    self.obj57.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj57.display.setHeight(15)

    # Actions
    self.obj57.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj57.Actions.setValue(lcobj2)

    # Constraints
    self.obj57.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj57.Constraints.setValue(lcobj2)

    self.obj57.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(931.0,942.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=CD_Class3(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # QOCA
    self.obj58.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj58.Graphical_Appearance.setValue( ('Strategy', self.obj58))

    # name
    self.obj58.name.setValue('Strategy')

    # attributes
    self.obj58.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj58.attributes.setValue(lcobj2)

    # Abstract
    self.obj58.Abstract.setValue((None, 1))
    self.obj58.Abstract.config = 0

    # cardinality
    self.obj58.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj58.cardinality.setValue(lcobj2)

    # display
    self.obj58.display.setValue('Attributes:\n  - description :: Text\n  - name :: String\n')
    self.obj58.display.setHeight(15)

    # Actions
    self.obj58.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj58.Actions.setValue(lcobj2)

    # Constraints
    self.obj58.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj58.Constraints.setValue(lcobj2)

    self.obj58.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(10.0,310.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0454545454545454]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=CD_Class3(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # QOCA
    self.obj59.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj59.Graphical_Appearance.setValue( ('Objective', self.obj59))

    # name
    self.obj59.name.setValue('Objective')

    # attributes
    self.obj59.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj59.attributes.setValue(lcobj2)

    # Abstract
    self.obj59.Abstract.setValue((None, 0))
    self.obj59.Abstract.config = 0

    # cardinality
    self.obj59.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    cobj2=ATOM3Connection()
    cobj2.setValue(('precedentTo', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('precedentTo', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj59.cardinality.setValue(lcobj2)

    # display
    self.obj59.display.setValue('Attributes:\n  - ID :: String\n  - Measurement :: Text\n  - Reward :: Text\n  - ofActions :: List\nMultiplicities:\n  - To isPartOfObjective: 0 to N\n  - From isPartOfObjective: 0 to N\n  - From hasObjective: 0 to N\n  - To precedentTo: 0 to N\n  - From precedentTo: 0 to N\n')
    self.obj59.display.setHeight(15)

    # Actions
    self.obj59.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj59.Actions.setValue(lcobj2)

    # Constraints
    self.obj59.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj59.Constraints.setValue(lcobj2)

    self.obj59.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(20.0,440.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.26875, 2.2721311475409838]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=CD_Class3(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # QOCA
    self.obj60.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj60.Graphical_Appearance.setValue( ('Process', self.obj60))

    # name
    self.obj60.name.setValue('Process')

    # attributes
    self.obj60.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj60.attributes.setValue(lcobj2)

    # Abstract
    self.obj60.Abstract.setValue((None, 0))
    self.obj60.Abstract.config = 0

    # cardinality
    self.obj60.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj60.cardinality.setValue(lcobj2)

    # display
    self.obj60.display.setValue('Attributes:\n  - ID :: String\n  - Name :: String\n  - hasActions :: List\nMultiplicities:\n  - From canStartProcess: 0 to N\n  - To hasObjective: 0 to N\n  - From isPartOfProcess: 0 to N\n')
    self.obj60.display.setHeight(15)

    # Actions
    self.obj60.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj60.Actions.setValue(lcobj2)

    # Constraints
    self.obj60.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj60.Constraints.setValue(lcobj2)

    self.obj60.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(10.0,10.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.23046875, 1.6524590163934427]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=CD_Association3(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(True)

    # QOCA
    self.obj61.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj61.Graphical_Appearance.setValue( ('isPartOfOrgUnit', self.obj61))
    self.obj61.Graphical_Appearance.linkInfo=linkEditor(self,self.obj61.Graphical_Appearance.semObject, "isPartOfOrgUnit")
    self.obj61.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj61.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj61.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj61.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj61.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj61.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj61.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj61.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj61.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfOrgUnit_1stLink', self.obj61.Graphical_Appearance.linkInfo.FirstLink))
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfOrgUnit_1stSegment', self.obj61.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj61.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj61.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfOrgUnit_Center', self.obj61.Graphical_Appearance.linkInfo))
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfOrgUnit_2ndSegment', self.obj61.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj61.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj61.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj61.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj61.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj61.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj61.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj61.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj61.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj61.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfOrgUnit_2ndLink', self.obj61.Graphical_Appearance.linkInfo.SecondLink))
    self.obj61.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj61.Graphical_Appearance.semObject
    self.obj61.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj61.Graphical_Appearance.semObject
    self.obj61.Graphical_Appearance.linkInfo.Center.semObject=self.obj61.Graphical_Appearance.semObject
    self.obj61.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj61.Graphical_Appearance.semObject
    self.obj61.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj61.Graphical_Appearance.semObject

    # name
    self.obj61.name.setValue('isPartOfOrgUnit')

    # displaySelect
    self.obj61.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj61.displaySelect.config = 0

    # attributes
    self.obj61.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('pOU|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj61.attributes.setValue(lcobj2)

    # cardinality
    self.obj61.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj61.cardinality.setValue(lcobj2)

    # display
    self.obj61.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - From OrgUnit: 1 to N\n  - To OrgUnit: 1 to N\n')
    self.obj61.display.setHeight(15)

    # Actions
    self.obj61.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj61.Actions.setValue(lcobj2)

    # Constraints
    self.obj61.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj61.Constraints.setValue(lcobj2)

    self.obj61.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1385.9955984,75.809726225,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.3548387096774195]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=CD_Association3(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(True)

    # QOCA
    self.obj62.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj62.Graphical_Appearance.setValue( ('canHaveRole', self.obj62))
    self.obj62.Graphical_Appearance.linkInfo=linkEditor(self,self.obj62.Graphical_Appearance.semObject, "canHaveRole")
    self.obj62.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj62.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj62.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj62.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj62.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj62.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj62.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj62.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj62.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canHaveRole_1stLink', self.obj62.Graphical_Appearance.linkInfo.FirstLink))
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canHaveRole_1stSegment', self.obj62.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj62.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj62.Graphical_Appearance.linkInfo.Center.setValue( ('canHaveRole_Center', self.obj62.Graphical_Appearance.linkInfo))
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canHaveRole_2ndSegment', self.obj62.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj62.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj62.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj62.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj62.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj62.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj62.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj62.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj62.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj62.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canHaveRole_2ndLink', self.obj62.Graphical_Appearance.linkInfo.SecondLink))
    self.obj62.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj62.Graphical_Appearance.semObject
    self.obj62.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj62.Graphical_Appearance.semObject
    self.obj62.Graphical_Appearance.linkInfo.Center.semObject=self.obj62.Graphical_Appearance.semObject
    self.obj62.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj62.Graphical_Appearance.semObject
    self.obj62.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj62.Graphical_Appearance.semObject

    # name
    self.obj62.name.setValue('canHaveRole')

    # displaySelect
    self.obj62.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj62.displaySelect.config = 0

    # attributes
    self.obj62.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('OUR|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj62.attributes.setValue(lcobj2)

    # cardinality
    self.obj62.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj62.cardinality.setValue(lcobj2)

    # display
    self.obj62.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - From OrgUnit: 0 to N\n  - To Role: 0 to N\n')
    self.obj62.display.setHeight(15)

    # Actions
    self.obj62.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj62.Actions.setValue(lcobj2)

    # Constraints
    self.obj62.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj62.Constraints.setValue(lcobj2)

    self.obj62.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1115.7601868,587.680947659,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.3548387096774195]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=CD_Association3(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # QOCA
    self.obj63.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj63.Graphical_Appearance.setValue( ('hasActions', self.obj63))
    self.obj63.Graphical_Appearance.linkInfo=linkEditor(self,self.obj63.Graphical_Appearance.semObject, "hasActions")
    self.obj63.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj63.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj63.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj63.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj63.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj63.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj63.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj63.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj63.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasActions_1stLink', self.obj63.Graphical_Appearance.linkInfo.FirstLink))
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasActions_1stSegment', self.obj63.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj63.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj63.Graphical_Appearance.linkInfo.Center.setValue( ('hasActions_Center', self.obj63.Graphical_Appearance.linkInfo))
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasActions_2ndSegment', self.obj63.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj63.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj63.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj63.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj63.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj63.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj63.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj63.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj63.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj63.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasActions_2ndLink', self.obj63.Graphical_Appearance.linkInfo.SecondLink))
    self.obj63.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj63.Graphical_Appearance.semObject
    self.obj63.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj63.Graphical_Appearance.semObject
    self.obj63.Graphical_Appearance.linkInfo.Center.semObject=self.obj63.Graphical_Appearance.semObject
    self.obj63.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj63.Graphical_Appearance.semObject
    self.obj63.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj63.Graphical_Appearance.semObject

    # name
    self.obj63.name.setValue('hasActions')

    # displaySelect
    self.obj63.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj63.displaySelect.config = 0

    # attributes
    self.obj63.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('aR|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj63.attributes.setValue(lcobj2)

    # cardinality
    self.obj63.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Action', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    self.obj63.cardinality.setValue(lcobj2)

    # display
    self.obj63.display.setValue('Attributes:\n  - ID :: String\nActions:\n  > updateRoleActions\nMultiplicities:\n  - To Action: 1 to N\n  - From Role: 1 to 1\n')
    self.obj63.display.setHeight(15)

    # Actions
    self.obj63.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('updateRoleActions', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]), 'from CustomCode import UpdateActions\n\nres = UpdateActions(self)\n\n'))
    lcobj2.append(cobj2)
    self.obj63.Actions.setValue(lcobj2)

    # Constraints
    self.obj63.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj63.Constraints.setValue(lcobj2)

    self.obj63.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(650.161248615,384.001803815,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.099, 1.8967741935483875]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=CD_Association3(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # QOCA
    self.obj64.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj64.Graphical_Appearance.setValue( ('canAccessKnArt', self.obj64))
    self.obj64.Graphical_Appearance.linkInfo=linkEditor(self,self.obj64.Graphical_Appearance.semObject, "canAccessKnArt")
    self.obj64.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj64.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj64.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj64.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj64.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj64.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj64.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj64.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj64.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canAccessKnArt_1stLink', self.obj64.Graphical_Appearance.linkInfo.FirstLink))
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canAccessKnArt_1stSegment', self.obj64.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj64.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj64.Graphical_Appearance.linkInfo.Center.setValue( ('canAccessKnArt_Center', self.obj64.Graphical_Appearance.linkInfo))
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canAccessKnArt_2ndSegment', self.obj64.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj64.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj64.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj64.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj64.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj64.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj64.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj64.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj64.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj64.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canAccessKnArt_2ndLink', self.obj64.Graphical_Appearance.linkInfo.SecondLink))
    self.obj64.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj64.Graphical_Appearance.semObject
    self.obj64.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj64.Graphical_Appearance.semObject
    self.obj64.Graphical_Appearance.linkInfo.Center.semObject=self.obj64.Graphical_Appearance.semObject
    self.obj64.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj64.Graphical_Appearance.semObject
    self.obj64.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj64.Graphical_Appearance.semObject

    # name
    self.obj64.name.setValue('canAccessKnArt')

    # displaySelect
    self.obj64.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj64.displaySelect.config = 0

    # attributes
    self.obj64.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('accKA|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj64.attributes.setValue(lcobj2)

    # cardinality
    self.obj64.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj64.cardinality.setValue(lcobj2)

    # display
    self.obj64.display.setValue('Attributes:\n  - ID :: String\nConstraints:\n  > ConstraintKnArt\nMultiplicities:\n  - To OrganisationalKnArt: 0 to N\n  - From Role: 0 to N\n  - From OrgUnit: 0 to N\n  - To IndividualKnArt: 0 to N\n')
    self.obj64.display.setHeight(15)

    # Actions
    self.obj64.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj64.Actions.setValue(lcobj2)

    # Constraints
    self.obj64.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = canAccessKnArtCheckConnections(self)\n\nif res is "eitherRoleOrUnit":\n    return ("Either Role of OrgUnit can access knowledge.", self.graphObject_)\nelif res is "onlyOneInput":\n    return ("Only one Role or OrgUnit can access one knowledge medium.", self.graphObject_)\nelif res is "RoleWithOrgOnly":\n    return ("Role can access OrganisationalKnArt only!", self.graphObject_)\nelif res is "OrgUnitWithIndivOnly":\n    return ("OrgUnit can access IndividualKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj64.Constraints.setValue(lcobj2)

    self.obj64.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1338.462784,841.548234957,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.6380000000000001, 2.438709677419355]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=CD_Association3(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(True)

    # QOCA
    self.obj65.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj65.Graphical_Appearance.setValue( ('isPartOfObjective', self.obj65))
    self.obj65.Graphical_Appearance.linkInfo=linkEditor(self,self.obj65.Graphical_Appearance.semObject, "isPartOfObjective")
    self.obj65.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj65.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj65.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj65.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj65.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj65.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj65.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj65.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj65.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfObjective_1stLink', self.obj65.Graphical_Appearance.linkInfo.FirstLink))
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfObjective_1stSegment', self.obj65.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj65.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj65.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfObjective_Center', self.obj65.Graphical_Appearance.linkInfo))
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfObjective_2ndSegment', self.obj65.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj65.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj65.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj65.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj65.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj65.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj65.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj65.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj65.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj65.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfObjective_2ndLink', self.obj65.Graphical_Appearance.linkInfo.SecondLink))
    self.obj65.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj65.Graphical_Appearance.semObject
    self.obj65.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj65.Graphical_Appearance.semObject
    self.obj65.Graphical_Appearance.linkInfo.Center.semObject=self.obj65.Graphical_Appearance.semObject
    self.obj65.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj65.Graphical_Appearance.semObject
    self.obj65.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj65.Graphical_Appearance.semObject

    # name
    self.obj65.name.setValue('isPartOfObjective')

    # displaySelect
    self.obj65.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj65.displaySelect.config = 0

    # attributes
    self.obj65.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('pO|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj65.attributes.setValue(lcobj2)

    # cardinality
    self.obj65.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj65.cardinality.setValue(lcobj2)

    # display
    self.obj65.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - From Objective: 0 to N\n  - To Objective: 0 to N\n')
    self.obj65.display.setHeight(15)

    # Actions
    self.obj65.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj65.Actions.setValue(lcobj2)

    # Constraints
    self.obj65.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj65.Constraints.setValue(lcobj2)

    self.obj65.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(131.944046519,946.91223085,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.225, 1.3548387096774195]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=CD_Association3(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # QOCA
    self.obj66.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj66.Graphical_Appearance.setValue( ('hasObjective', self.obj66))
    self.obj66.Graphical_Appearance.linkInfo=linkEditor(self,self.obj66.Graphical_Appearance.semObject, "hasObjective")
    self.obj66.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj66.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj66.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj66.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasObjective_1stLink', self.obj66.Graphical_Appearance.linkInfo.FirstLink))
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasObjective_1stSegment', self.obj66.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj66.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj66.Graphical_Appearance.linkInfo.Center.setValue( ('hasObjective_Center', self.obj66.Graphical_Appearance.linkInfo))
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasObjective_2ndSegment', self.obj66.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj66.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj66.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj66.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj66.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasObjective_2ndLink', self.obj66.Graphical_Appearance.linkInfo.SecondLink))
    self.obj66.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj66.Graphical_Appearance.semObject
    self.obj66.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj66.Graphical_Appearance.semObject
    self.obj66.Graphical_Appearance.linkInfo.Center.semObject=self.obj66.Graphical_Appearance.semObject
    self.obj66.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj66.Graphical_Appearance.semObject
    self.obj66.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj66.Graphical_Appearance.semObject

    # name
    self.obj66.name.setValue('hasObjective')

    # displaySelect
    self.obj66.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj66.displaySelect.config = 0

    # attributes
    self.obj66.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('RPO|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj66.attributes.setValue(lcobj2)

    # cardinality
    self.obj66.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj66.cardinality.setValue(lcobj2)

    # display
    self.obj66.display.setValue('Attributes:\n  - ID :: String\nActions:\n  > updateObjectiveActions\nMultiplicities:\n  - To Objective: 1 to N\n  - From Role: 0 to N\n  - From Process: 0 to N\n  - From Action: 0 to N\n')
    self.obj66.display.setHeight(15)

    # Actions
    self.obj66.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('updateObjectiveActions', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]), 'from CustomCode import UpdateActions\n\nres = UpdateActions(self)\n'))
    lcobj2.append(cobj2)
    self.obj66.Actions.setValue(lcobj2)

    # Constraints
    self.obj66.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj66.Constraints.setValue(lcobj2)

    self.obj66.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(568.73445957,873.859445861,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.33, 2.438709677419355]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=CD_Association3(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # QOCA
    self.obj67.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj67.Graphical_Appearance.setValue( ('genericAssociation', self.obj67))
    self.obj67.Graphical_Appearance.linkInfo=linkEditor(self,self.obj67.Graphical_Appearance.semObject, "genericAssociation")
    self.obj67.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj67.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj67.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj67.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj67.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj67.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj67.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj67.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj67.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('genericAssociation_1stLink', self.obj67.Graphical_Appearance.linkInfo.FirstLink))
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('genericAssociation_1stSegment', self.obj67.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj67.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj67.Graphical_Appearance.linkInfo.Center.setValue( ('genericAssociation_Center', self.obj67.Graphical_Appearance.linkInfo))
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('genericAssociation_2ndSegment', self.obj67.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj67.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj67.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj67.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj67.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj67.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj67.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj67.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj67.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj67.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('genericAssociation_2ndLink', self.obj67.Graphical_Appearance.linkInfo.SecondLink))
    self.obj67.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj67.Graphical_Appearance.semObject
    self.obj67.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj67.Graphical_Appearance.semObject
    self.obj67.Graphical_Appearance.linkInfo.Center.semObject=self.obj67.Graphical_Appearance.semObject
    self.obj67.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj67.Graphical_Appearance.semObject
    self.obj67.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj67.Graphical_Appearance.semObject

    # name
    self.obj67.name.setValue('genericAssociation')

    # displaySelect
    self.obj67.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj67.displaySelect.config = 0

    # attributes
    self.obj67.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj67.attributes.setValue(lcobj2)

    # cardinality
    self.obj67.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj67.cardinality.setValue(lcobj2)

    # display
    self.obj67.display.setValue('Attributes:\n  - name :: String\n  - Description :: Text\n  - ID :: String\nMultiplicities:\n  - To Role: 1 to N\n  - From Role: 1 to N\n')
    self.obj67.display.setHeight(15)

    # Actions
    self.obj67.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj67.Actions.setValue(lcobj2)

    # Constraints
    self.obj67.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj67.Constraints.setValue(lcobj2)

    self.obj67.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1089.0,378.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.015, 1.8967741935483875]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=CD_Association3(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(True)

    # QOCA
    self.obj68.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj68.Graphical_Appearance.setValue( ('answersToRole', self.obj68))
    self.obj68.Graphical_Appearance.linkInfo=linkEditor(self,self.obj68.Graphical_Appearance.semObject, "answersToRole")
    self.obj68.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj68.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj68.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj68.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToRole_1stLink', self.obj68.Graphical_Appearance.linkInfo.FirstLink))
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToRole_1stSegment', self.obj68.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj68.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj68.Graphical_Appearance.linkInfo.Center.setValue( ('answersToRole_Center', self.obj68.Graphical_Appearance.linkInfo))
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToRole_2ndSegment', self.obj68.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj68.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj68.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj68.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj68.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToRole_2ndLink', self.obj68.Graphical_Appearance.linkInfo.SecondLink))
    self.obj68.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj68.Graphical_Appearance.semObject
    self.obj68.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj68.Graphical_Appearance.semObject
    self.obj68.Graphical_Appearance.linkInfo.Center.semObject=self.obj68.Graphical_Appearance.semObject
    self.obj68.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj68.Graphical_Appearance.semObject
    self.obj68.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj68.Graphical_Appearance.semObject

    # name
    self.obj68.name.setValue('answersToRole')

    # displaySelect
    self.obj68.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj68.displaySelect.config = 0

    # attributes
    self.obj68.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('hR|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj68.attributes.setValue(lcobj2)

    # cardinality
    self.obj68.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj68.cardinality.setValue(lcobj2)

    # display
    self.obj68.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - From Role: 1 to N\n  - To Role: 1 to N\n')
    self.obj68.display.setHeight(15)

    # Actions
    self.obj68.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj68.Actions.setValue(lcobj2)

    # Constraints
    self.obj68.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj68.Constraints.setValue(lcobj2)

    self.obj68.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(931.0,105.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.3548387096774195]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=CD_Association3(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # QOCA
    self.obj69.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj69.Graphical_Appearance.setValue( ('canStartProcess', self.obj69))
    self.obj69.Graphical_Appearance.linkInfo=linkEditor(self,self.obj69.Graphical_Appearance.semObject, "canStartProcess")
    self.obj69.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj69.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj69.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj69.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canStartProcess_1stLink', self.obj69.Graphical_Appearance.linkInfo.FirstLink))
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canStartProcess_1stSegment', self.obj69.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj69.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj69.Graphical_Appearance.linkInfo.Center.setValue( ('canStartProcess_Center', self.obj69.Graphical_Appearance.linkInfo))
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canStartProcess_2ndSegment', self.obj69.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj69.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj69.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj69.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj69.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canStartProcess_2ndLink', self.obj69.Graphical_Appearance.linkInfo.SecondLink))
    self.obj69.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj69.Graphical_Appearance.semObject
    self.obj69.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj69.Graphical_Appearance.semObject
    self.obj69.Graphical_Appearance.linkInfo.Center.semObject=self.obj69.Graphical_Appearance.semObject
    self.obj69.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj69.Graphical_Appearance.semObject
    self.obj69.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj69.Graphical_Appearance.semObject

    # name
    self.obj69.name.setValue('canStartProcess')

    # displaySelect
    self.obj69.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj69.displaySelect.config = 0

    # attributes
    self.obj69.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('RP|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj69.attributes.setValue(lcobj2)

    # cardinality
    self.obj69.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Process', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj69.cardinality.setValue(lcobj2)

    # display
    self.obj69.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - To Process: 0 to N\n  - From Role: 0 to N\n')
    self.obj69.display.setHeight(15)

    # Actions
    self.obj69.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj69.Actions.setValue(lcobj2)

    # Constraints
    self.obj69.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj69.Constraints.setValue(lcobj2)

    self.obj69.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(519.4921875,78.163934426,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.036, 1.3548387096774195]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=CD_Association3(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(True)

    # QOCA
    self.obj70.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj70.Graphical_Appearance.setValue( ('answersToOrgUnit', self.obj70))
    self.obj70.Graphical_Appearance.linkInfo=linkEditor(self,self.obj70.Graphical_Appearance.semObject, "answersToOrgUnit")
    self.obj70.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj70.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj70.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj70.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj70.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj70.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj70.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj70.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj70.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToOrgUnit_1stLink', self.obj70.Graphical_Appearance.linkInfo.FirstLink))
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToOrgUnit_1stSegment', self.obj70.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj70.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj70.Graphical_Appearance.linkInfo.Center.setValue( ('answersToOrgUnit_Center', self.obj70.Graphical_Appearance.linkInfo))
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToOrgUnit_2ndSegment', self.obj70.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj70.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj70.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj70.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj70.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj70.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj70.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj70.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj70.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj70.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToOrgUnit_2ndLink', self.obj70.Graphical_Appearance.linkInfo.SecondLink))
    self.obj70.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj70.Graphical_Appearance.semObject
    self.obj70.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj70.Graphical_Appearance.semObject
    self.obj70.Graphical_Appearance.linkInfo.Center.semObject=self.obj70.Graphical_Appearance.semObject
    self.obj70.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj70.Graphical_Appearance.semObject
    self.obj70.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj70.Graphical_Appearance.semObject

    # name
    self.obj70.name.setValue('answersToOrgUnit')

    # displaySelect
    self.obj70.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj70.displaySelect.config = 0

    # attributes
    self.obj70.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('hOU|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj70.attributes.setValue(lcobj2)

    # cardinality
    self.obj70.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj70.cardinality.setValue(lcobj2)

    # display
    self.obj70.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - To OrgUnit: 1 to N\n  - From OrgUnit: 1 to N\n')
    self.obj70.display.setHeight(15)

    # Actions
    self.obj70.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj70.Actions.setValue(lcobj2)

    # Constraints
    self.obj70.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj70.Constraints.setValue(lcobj2)

    self.obj70.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1153.0,98.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.3548387096774195]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=CD_Association3(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(True)

    # QOCA
    self.obj71.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj71.Graphical_Appearance.setValue( ('isPartOfRole', self.obj71))
    self.obj71.Graphical_Appearance.linkInfo=linkEditor(self,self.obj71.Graphical_Appearance.semObject, "isPartOfRole")
    self.obj71.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj71.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj71.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj71.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfRole_1stLink', self.obj71.Graphical_Appearance.linkInfo.FirstLink))
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfRole_1stSegment', self.obj71.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj71.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj71.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfRole_Center', self.obj71.Graphical_Appearance.linkInfo))
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfRole_2ndSegment', self.obj71.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],0,0)
    self.obj71.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj71.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj71.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj71.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfRole_2ndLink', self.obj71.Graphical_Appearance.linkInfo.SecondLink))
    self.obj71.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj71.Graphical_Appearance.semObject
    self.obj71.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj71.Graphical_Appearance.semObject
    self.obj71.Graphical_Appearance.linkInfo.Center.semObject=self.obj71.Graphical_Appearance.semObject
    self.obj71.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj71.Graphical_Appearance.semObject
    self.obj71.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj71.Graphical_Appearance.semObject

    # name
    self.obj71.name.setValue('isPartOfRole')

    # displaySelect
    self.obj71.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj71.displaySelect.config = 0

    # attributes
    self.obj71.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('pR|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj71.attributes.setValue(lcobj2)

    # cardinality
    self.obj71.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj71.cardinality.setValue(lcobj2)

    # display
    self.obj71.display.setValue('Attributes:\n  - ID :: String\nMultiplicities:\n  - From Role: 0 to N\n  - To Role: 0 to N\n')
    self.obj71.display.setHeight(15)

    # Actions
    self.obj71.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj71.Actions.setValue(lcobj2)

    # Constraints
    self.obj71.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj71.Constraints.setValue(lcobj2)

    self.obj71.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(756.0,97.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.3548387096774195]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=CD_Association3(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # QOCA
    self.obj72.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj72.Graphical_Appearance.setValue( ('isPartOfProcess', self.obj72))
    self.obj72.Graphical_Appearance.linkInfo=linkEditor(self,self.obj72.Graphical_Appearance.semObject, "isPartOfProcess")
    self.obj72.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj72.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj72.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj72.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj72.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj72.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj72.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj72.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj72.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfProcess_1stLink', self.obj72.Graphical_Appearance.linkInfo.FirstLink))
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfProcess_1stSegment', self.obj72.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj72.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj72.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfProcess_Center', self.obj72.Graphical_Appearance.linkInfo))
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfProcess_2ndSegment', self.obj72.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj72.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj72.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj72.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj72.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj72.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj72.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj72.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj72.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj72.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfProcess_2ndLink', self.obj72.Graphical_Appearance.linkInfo.SecondLink))
    self.obj72.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj72.Graphical_Appearance.semObject
    self.obj72.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj72.Graphical_Appearance.semObject
    self.obj72.Graphical_Appearance.linkInfo.Center.semObject=self.obj72.Graphical_Appearance.semObject
    self.obj72.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj72.Graphical_Appearance.semObject
    self.obj72.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj72.Graphical_Appearance.semObject

    # name
    self.obj72.name.setValue('isPartOfProcess')

    # displaySelect
    self.obj72.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj72.displaySelect.config = 0

    # attributes
    self.obj72.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ID', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('AP|', 20)
    cobj2.isDerivedAttribute = False
    lcobj2.append(cobj2)
    self.obj72.attributes.setValue(lcobj2)

    # cardinality
    self.obj72.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Action', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Process', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj72.cardinality.setValue(lcobj2)

    # display
    self.obj72.display.setValue('Attributes:\n  - ID :: String\nActions:\n  > updateProcessActions\nMultiplicities:\n  - From Action: 0 to N\n  - To Process: 0 to N\n')
    self.obj72.display.setHeight(15)

    # Actions
    self.obj72.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('updateProcessActions', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0]), 'from CustomCode import UpdateActions\n\nres = UpdateActions(self)\n\n\n'))
    lcobj2.append(cobj2)
    self.obj72.Actions.setValue(lcobj2)

    # Constraints
    self.obj72.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj72.Constraints.setValue(lcobj2)

    self.obj72.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(441.0,297.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2670000000000001, 1.8967741935483875]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=CD_Association3(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # QOCA
    self.obj73.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj73.Graphical_Appearance.setValue( ('Association_12', self.obj73))
    self.obj73.Graphical_Appearance.linkInfo=linkEditor(self,self.obj73.Graphical_Appearance.semObject, "Association_12")
    self.obj73.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj73.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj73.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj73.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj73.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj73.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj73.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj73.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj73.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('Association_12_1stLink', self.obj73.Graphical_Appearance.linkInfo.FirstLink))
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('Association_12_1stSegment', self.obj73.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj73.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj73.Graphical_Appearance.linkInfo.Center.setValue( ('Association_12_Center', self.obj73.Graphical_Appearance.linkInfo))
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('Association_12_2ndSegment', self.obj73.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj73.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj73.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj73.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj73.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj73.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj73.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj73.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj73.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj73.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('Association_12_2ndLink', self.obj73.Graphical_Appearance.linkInfo.SecondLink))
    self.obj73.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj73.Graphical_Appearance.semObject
    self.obj73.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj73.Graphical_Appearance.semObject
    self.obj73.Graphical_Appearance.linkInfo.Center.semObject=self.obj73.Graphical_Appearance.semObject
    self.obj73.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj73.Graphical_Appearance.semObject
    self.obj73.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj73.Graphical_Appearance.semObject

    # name
    self.obj73.name.setValue('precedentTo')

    # displaySelect
    self.obj73.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj73.displaySelect.config = 0

    # attributes
    self.obj73.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj73.attributes.setValue(lcobj2)

    # cardinality
    self.obj73.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj73.cardinality.setValue(lcobj2)

    # display
    self.obj73.display.setValue('Multiplicities:\n  - From Objective: 0 to N\n  - To Objective: 0 to N\n')
    self.obj73.display.setHeight(15)

    # Actions
    self.obj73.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj73.Actions.setValue(lcobj2)

    # Constraints
    self.obj73.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj73.Constraints.setValue(lcobj2)

    self.obj73.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(340.0,962.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.225, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=CD_Inheritance3(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    self.obj74.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(913.21888986,906.92763695,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=CD_Inheritance3(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    self.obj75.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(916.90914946,984.75085967,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=CD_Inheritance3(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    self.obj76.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(151.858254695,480.846159545,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=CD_Inheritance3(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    self.obj77.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(86.466796875,272.786885246,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    # Connections for obj52 (graphObject_: Obj43) named OrgUnit
    self.drawConnections(
(self.obj52,self.obj61,[1368.8125, 221.327868852459, 1385.9955983980042, 75.8097262245276, 1385.9955984, 75.809726225],"true", 3),
(self.obj52,self.obj62,[1241.14453125, 572.4754098360655, 1111.84224855279, 541.4017668814608, 1115.7601868000002, 587.680947659],"true", 3),
(self.obj52,self.obj64,[1324.40625, 631.0, 1343.8287423035672, 659.3266545159663, 1338.462784, 841.548234957],"true", 3),
(self.obj52,self.obj70,[1241.14453125, 338.37704918032784, 1170.0, 250.0, 1153.0, 98.0], 0, 3) )
    # Connections for obj53 (graphObject_: Obj44) named Role
    self.drawConnections(
(self.obj53,self.obj63,[760.953125, 405.5245901639344, 688.1631302538499, 315.35664968159404, 650.161248615, 384.001803815],"true", 3),
(self.obj53,self.obj64,[972.921875, 694.7049180327868, 1255.5805784296024, 734.1457487347751, 1338.462784, 841.548234957],"true", 3),
(self.obj53,self.obj66,[760.953125, 694.7049180327868, 654.0012232889502, 794.7739542825374, 568.73445957, 873.859445861],"true", 3),
(self.obj53,self.obj67,[972.921875, 405.5245901639344, 1089.0, 378.0], 0, 2),
(self.obj53,self.obj68,[933.875, 260.93442622950823, 931.0, 105.0], 0, 2),
(self.obj53,self.obj69,[800.0, 260.93442622950823, 519.4921875, 78.16393442599997], 0, 2),
(self.obj53,self.obj71,[800.0, 260.93442622950823, 756.0, 97.0],"true", 2) )
    # Connections for obj54 (graphObject_: Obj45) named Action
    self.drawConnections(
(self.obj54,self.obj72,[462.875, 420.8196721311475, 441.0, 297.0],"true", 2),
(self.obj54,self.obj66,[508.8125, 710.0, 568.73445957, 873.859445861],"true", 2) )
    # Connections for obj55 (graphObject_: Obj46) named KnowledgeArtifacts
    self.drawConnections(
 )
    # Connections for obj56 (graphObject_: Obj47) named OrganisationalKnArt
    self.drawConnections(
(self.obj56,self.obj74,[931.7421875, 908.0909090909091, 913.21888986, 906.92763695], 0, 2) )
    # Connections for obj57 (graphObject_: Obj48) named IndividualKnArt
    self.drawConnections(
(self.obj57,self.obj75,[931.7421875, 984.4545454545455, 916.90914946, 984.75085967],"true", 2) )
    # Connections for obj58 (graphObject_: Obj49) named Strategy
    self.drawConnections(
 )
    # Connections for obj59 (graphObject_: Obj50) named Objective
    self.drawConnections(
(self.obj59,self.obj76,[166.5, 498.9016393442623, 151.858254695, 480.846159545],"true", 2),
(self.obj59,self.obj65,[115.75, 817.0, 131.94404651894035, 946.9122308488277, 131.944046519, 946.91223085],"true", 3),
(self.obj59,self.obj73,[217.25, 817.0, 340.0, 962.0],"true", 2) )
    # Connections for obj60 (graphObject_: Obj51) named Process
    self.drawConnections(
(self.obj60,self.obj66,[201.65625, 242.0, 323.0, 995.0, 568.73445957, 873.859445861],"true", 3),
(self.obj60,self.obj77,[103.21875, 242.0, 86.466796875, 272.786885246],"true", 2) )
    # Connections for obj61 (graphObject_: Obj52) named isPartOfOrgUnit
    self.drawConnections(
(self.obj61,self.obj52,[1385.9955984, 75.809726225, 1385.9955983980042, 75.8097262245276, 1368.8125, 221.327868852459],"true", 3) )
    # Connections for obj62 (graphObject_: Obj54) named canHaveRole
    self.drawConnections(
(self.obj62,self.obj53,[1115.7601868000002, 587.680947659, 1119.67812505129, 633.9601284363068, 972.921875, 604.3360655737705],"true", 3) )
    # Connections for obj63 (graphObject_: Obj56) named hasActions
    self.drawConnections(
(self.obj63,self.obj54,[650.161248615, 384.001803815, 627.1593669760688, 461.6469579482074, 549.0078125, 503.44262295081967],"true", 3) )
    # Connections for obj64 (graphObject_: Obj58) named canAccessKnArt
    self.drawConnections(
(self.obj64,self.obj56,[1338.462784, 841.548234957, 1204.2678325033444, 884.9439489105719, 1166.5703125, 881.9545454545455],"true", 3),
(self.obj64,self.obj57,[1338.462784, 841.548234957, 1314.4035107781324, 1039.4763808302594, 1166.5703125, 1041.9545454545455],"true", 3) )
    # Connections for obj65 (graphObject_: Obj60) named isPartOfObjective
    self.drawConnections(
(self.obj65,self.obj59,[131.944046519, 946.91223085, 131.94404651894035, 946.9122308488277, 115.75, 817.0],"true", 3) )
    # Connections for obj66 (graphObject_: Obj62) named hasObjective
    self.drawConnections(
(self.obj66,self.obj59,[568.73445957, 873.859445861, 483.4676958509182, 952.9449374392455, 261.65625, 771.5573770491803],"true", 3) )
    # Connections for obj67 (graphObject_: Obj64) named genericAssociation
    self.drawConnections(
(self.obj67,self.obj53,[1089.0, 378.0, 972.921875, 405.5245901639344], 0, 2) )
    # Connections for obj68 (graphObject_: Obj66) named answersToRole
    self.drawConnections(
(self.obj68,self.obj53,[931.0, 105.0, 933.875, 260.93442622950823], 0, 2) )
    # Connections for obj69 (graphObject_: Obj68) named canStartProcess
    self.drawConnections(
(self.obj69,self.obj60,[519.4921875, 78.16393442599997, 244.72265625, 76.75409836065572], 0, 2) )
    # Connections for obj70 (graphObject_: Obj70) named answersToOrgUnit
    self.drawConnections(
(self.obj70,self.obj52,[1153.0, 98.0, 1319.0, 164.0, 1324.40625, 221.327868852459], 0, 3) )
    # Connections for obj71 (graphObject_: Obj72) named isPartOfRole
    self.drawConnections(
(self.obj71,self.obj53,[756.0, 97.0, 800.0, 260.93442622950823],"true", 2) )
    # Connections for obj72 (graphObject_: Obj74) named isPartOfProcess
    self.drawConnections(
(self.obj72,self.obj60,[441.0, 297.0, 244.72265625, 208.95081967213116],"true", 2) )
    # Connections for obj73 (graphObject_: Obj76) named precedentTo
    self.drawConnections(
(self.obj73,self.obj59,[340.0, 962.0, 217.25, 817.0],"true", 2) )
    # Connections for obj74 (graphObject_: Obj78) of type CD_Inheritance3
    self.drawConnections(
(self.obj74,self.obj55,[913.21888986, 906.92763695, 880.0, 898.4545454545455], 0, 2) )
    # Connections for obj75 (graphObject_: Obj80) of type CD_Inheritance3
    self.drawConnections(
(self.obj75,self.obj55,[916.90914946, 984.75085967, 880.0, 982.0909090909091],"true", 2) )
    # Connections for obj76 (graphObject_: Obj82) of type CD_Inheritance3
    self.drawConnections(
(self.obj76,self.obj58,[151.858254695, 480.846159545, 166.0, 457.0],"true", 2) )
    # Connections for obj77 (graphObject_: Obj84) of type CD_Inheritance3
    self.drawConnections(
(self.obj77,self.obj58,[86.466796875, 272.786885246, 86.0, 310.6363636363636],"true", 2) )

newfunction = LSMASOMM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
