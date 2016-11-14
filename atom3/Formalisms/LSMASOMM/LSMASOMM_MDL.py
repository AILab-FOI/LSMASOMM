"""
__LSMASOMM_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Mon Nov 14 17:13:20 2016
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


    self.obj154=CD_Class3(self)
    self.obj154.isGraphObjectVisual = True

    if(hasattr(self.obj154, '_setHierarchicalLink')):
      self.obj154._setHierarchicalLink(False)

    # QOCA
    self.obj154.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj154.Graphical_Appearance.setValue( ('OrgUnit', self.obj154))

    # name
    self.obj154.name.setValue('OrgUnit')

    # attributes
    self.obj154.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj154.attributes.setValue(lcobj2)

    # Abstract
    self.obj154.Abstract.setValue((None, 0))
    self.obj154.Abstract.config = 0

    # cardinality
    self.obj154.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj154.cardinality.setValue(lcobj2)

    # display
    self.obj154.display.setValue('Attributes:\n  - Individual :: Boolean\n  - UnitActions :: List\n  - UnitSize :: String\n  - name :: String\nConstraints:\n  > ConstraintOutputOrgUnit\nActions:\n  > determineSize\nMultiplicities:\n  - To isPartOfOrgUnit: 0 to N\n  - From isPartOfOrgUnit: 0 to N\n  - To canHaveRole: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To answersToOrgUnit: 0 to N\n  - From answersToOrgUnit: 0 to N\n')
    self.obj154.display.setHeight(15)

    # Actions
    self.obj154.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('determineSize', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitDetermineSize(self)\nself.UnitSize.setValue(res)\nself.graphObject_.ModifyAttribute(\'UnitSize\', res)\n\n'))
    lcobj2.append(cobj2)
    self.obj154.Actions.setValue(lcobj2)

    # Constraints
    self.obj154.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintOutputOrgUnit', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = OrgUnitCheckOutputs(self)\nif res is "manyKnArts":\n    return ("OrgUnit can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj154.Constraints.setValue(lcobj2)

    self.obj154.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,220.0,self.obj154)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.88
       new_obj.layConstraints['scale'] = [1.11015625, 2.7540983606557377]
    else: new_obj = None
    self.obj154.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj154)
    self.globalAndLocalPostcondition(self.obj154, rootNode)
    self.obj154.postAction( rootNode.CREATE )

    self.obj155=CD_Class3(self)
    self.obj155.isGraphObjectVisual = True

    if(hasattr(self.obj155, '_setHierarchicalLink')):
      self.obj155._setHierarchicalLink(False)

    # QOCA
    self.obj155.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj155.Graphical_Appearance.setValue( ('Role', self.obj155))

    # name
    self.obj155.name.setValue('Role')

    # attributes
    self.obj155.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj155.attributes.setValue(lcobj2)

    # Abstract
    self.obj155.Abstract.setValue((None, 0))
    self.obj155.Abstract.config = 0

    # cardinality
    self.obj155.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj155.cardinality.setValue(lcobj2)

    # display
    self.obj155.display.setValue('Attributes:\n  - ID :: String\n  - isMetaRole :: Boolean\n  - name :: String\n  - roleActions :: List\nConstraints:\n  > RoleConstraintKnArt\nActions:\n  > checkMetaRole\nMultiplicities:\n  - From canHaveRole: 0 to N\n  - To hasActions: 0 to N\n  - To canAccessKnArt: 0 to N\n  - To hasObjective: 0 to N\n  - To genericAssociation: 0 to N\n  - From genericAssociation: 0 to N\n  - To answersToRole: 0 to N\n  - From answersToRole: 0 to N\n  - To canStartProcess: 0 to N\n  - To isPartOfRole: 0 to N\n  - From isPartOfRole: 0 to N\n')
    self.obj155.display.setHeight(15)

    # Actions
    self.obj155.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Action()
    cobj2.setValue(('checkMetaRole', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]), 'from CustomCode import RoleHierarchy\nres = RoleHierarchy(self)\nself.isMetaRole.setValue((\'isMetaRole\',res))\nself.graphObject_.ModifyAttribute(\'isMetaRole\', res)\n\n'))
    lcobj2.append(cobj2)
    self.obj155.Actions.setValue(lcobj2)

    # Constraints
    self.obj155.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('RoleConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '\nfrom CustomCode import *\n\nres = RoleCheckOutputs(self)\nif res is "manyKnArts":\n    return ("Roles can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)\nelif res is "IndivKnArtError":\n    return ("Roles can have OrganizationalKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj155.Constraints.setValue(lcobj2)

    self.obj155.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(620.0,280.0,self.obj155)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.85
       new_obj.layConstraints['scale'] = [1.115625, 3.6147540983606556]
    else: new_obj = None
    self.obj155.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj155)
    self.globalAndLocalPostcondition(self.obj155, rootNode)
    self.obj155.postAction( rootNode.CREATE )

    self.obj156=CD_Class3(self)
    self.obj156.isGraphObjectVisual = True

    if(hasattr(self.obj156, '_setHierarchicalLink')):
      self.obj156._setHierarchicalLink(False)

    # QOCA
    self.obj156.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj156.Graphical_Appearance.setValue( ('Action', self.obj156))

    # name
    self.obj156.name.setValue('Action')

    # attributes
    self.obj156.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj156.attributes.setValue(lcobj2)

    # Abstract
    self.obj156.Abstract.setValue((None, 0))
    self.obj156.Abstract.config = 0

    # cardinality
    self.obj156.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasActions', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj156.cardinality.setValue(lcobj2)

    # display
    self.obj156.display.setValue('Attributes:\n  - ActionCode :: Text\n  - name :: String\nMultiplicities:\n  - From hasActions: 0 to N\n')
    self.obj156.display.setHeight(15)

    # Actions
    self.obj156.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj156.Actions.setValue(lcobj2)

    # Constraints
    self.obj156.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj156.Constraints.setValue(lcobj2)

    self.obj156.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(740.0,820.0,self.obj156)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.06
       new_obj.layConstraints['scale'] = [1.02265625, 1.0454545454545454]
    else: new_obj = None
    self.obj156.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj156)
    self.globalAndLocalPostcondition(self.obj156, rootNode)
    self.obj156.postAction( rootNode.CREATE )

    self.obj157=CD_Class3(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    # QOCA
    self.obj157.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj157.Graphical_Appearance.setValue( ('KnowledgeArtifacts', self.obj157))

    # name
    self.obj157.name.setValue('KnowledgeArtifacts')

    # attributes
    self.obj157.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj157.attributes.setValue(lcobj2)

    # Abstract
    self.obj157.Abstract.setValue((None, 1))
    self.obj157.Abstract.config = 0

    # cardinality
    self.obj157.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj157.cardinality.setValue(lcobj2)

    # display
    self.obj157.display.setValue('Attributes:\n  - ID :: String\n  - description :: String\n  - name :: String\n')
    self.obj157.display.setHeight(15)

    # Actions
    self.obj157.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj157.Actions.setValue(lcobj2)

    # Constraints
    self.obj157.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj157.Constraints.setValue(lcobj2)

    self.obj157.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(980.0,1080.0,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0454545454545454]
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    self.obj158=CD_Class3(self)
    self.obj158.isGraphObjectVisual = True

    if(hasattr(self.obj158, '_setHierarchicalLink')):
      self.obj158._setHierarchicalLink(False)

    # QOCA
    self.obj158.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj158.Graphical_Appearance.setValue( ('OrganisationalKnArt', self.obj158))

    # name
    self.obj158.name.setValue('OrganisationalKnArt')

    # attributes
    self.obj158.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj158.attributes.setValue(lcobj2)

    # Abstract
    self.obj158.Abstract.setValue((None, 0))
    self.obj158.Abstract.config = 0

    # cardinality
    self.obj158.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj158.cardinality.setValue(lcobj2)

    # display
    self.obj158.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj158.display.setHeight(15)

    # Actions
    self.obj158.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj158.Actions.setValue(lcobj2)

    # Constraints
    self.obj158.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj158.Constraints.setValue(lcobj2)

    self.obj158.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(700.0,1080.0,self.obj158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj158)
    self.globalAndLocalPostcondition(self.obj158, rootNode)
    self.obj158.postAction( rootNode.CREATE )

    self.obj159=CD_Class3(self)
    self.obj159.isGraphObjectVisual = True

    if(hasattr(self.obj159, '_setHierarchicalLink')):
      self.obj159._setHierarchicalLink(False)

    # QOCA
    self.obj159.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj159.Graphical_Appearance.setValue( ('IndividualKnArt', self.obj159))

    # name
    self.obj159.name.setValue('IndividualKnArt')

    # attributes
    self.obj159.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj159.attributes.setValue(lcobj2)

    # Abstract
    self.obj159.Abstract.setValue((None, 0))
    self.obj159.Abstract.config = 0

    # cardinality
    self.obj159.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canAccessKnArt', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj159.cardinality.setValue(lcobj2)

    # display
    self.obj159.display.setValue('Attributes:\n  - KnArtContent :: Text\nMultiplicities:\n  - From canAccessKnArt: 0 to N\n')
    self.obj159.display.setHeight(15)

    # Actions
    self.obj159.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj159.Actions.setValue(lcobj2)

    # Constraints
    self.obj159.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj159.Constraints.setValue(lcobj2)

    self.obj159.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(1240.0,1060.0,self.obj159)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.2359375000000001, 1.0454545454545454]
    else: new_obj = None
    self.obj159.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj159)
    self.globalAndLocalPostcondition(self.obj159, rootNode)
    self.obj159.postAction( rootNode.CREATE )

    self.obj160=CD_Class3(self)
    self.obj160.isGraphObjectVisual = True

    if(hasattr(self.obj160, '_setHierarchicalLink')):
      self.obj160._setHierarchicalLink(False)

    # QOCA
    self.obj160.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj160.Graphical_Appearance.setValue( ('Strategy', self.obj160))

    # name
    self.obj160.name.setValue('Strategy')

    # attributes
    self.obj160.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj160.attributes.setValue(lcobj2)

    # Abstract
    self.obj160.Abstract.setValue((None, 1))
    self.obj160.Abstract.config = 0

    # cardinality
    self.obj160.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj160.cardinality.setValue(lcobj2)

    # display
    self.obj160.display.setValue('Attributes:\n  - ID :: String\n  - description :: Text\n  - name :: String\n')
    self.obj160.display.setHeight(15)

    # Actions
    self.obj160.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj160.Actions.setValue(lcobj2)

    # Constraints
    self.obj160.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj160.Constraints.setValue(lcobj2)

    self.obj160.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(40.0,340.0,self.obj160)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0454545454545454]
    else: new_obj = None
    self.obj160.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj160)
    self.globalAndLocalPostcondition(self.obj160, rootNode)
    self.obj160.postAction( rootNode.CREATE )

    self.obj161=CD_Class3(self)
    self.obj161.isGraphObjectVisual = True

    if(hasattr(self.obj161, '_setHierarchicalLink')):
      self.obj161._setHierarchicalLink(False)

    # QOCA
    self.obj161.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj161.Graphical_Appearance.setValue( ('Objective', self.obj161))

    # name
    self.obj161.name.setValue('Objective')

    # attributes
    self.obj161.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj161.attributes.setValue(lcobj2)

    # Abstract
    self.obj161.Abstract.setValue((None, 0))
    self.obj161.Abstract.config = 0

    # cardinality
    self.obj161.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj161.cardinality.setValue(lcobj2)

    # display
    self.obj161.display.setValue('Attributes:\n  - Measurement :: Text\n  - Reward :: Text\nMultiplicities:\n  - To isPartOfObjective: 0 to N\n  - From isPartOfObjective: 0 to N\n  - From hasObjective: 0 to N\n')
    self.obj161.display.setHeight(15)

    # Actions
    self.obj161.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj161.Actions.setValue(lcobj2)

    # Constraints
    self.obj161.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj161.Constraints.setValue(lcobj2)

    self.obj161.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(40.0,600.0,self.obj161)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.26875, 1.4459016393442625]
    else: new_obj = None
    self.obj161.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj161)
    self.globalAndLocalPostcondition(self.obj161, rootNode)
    self.obj161.postAction( rootNode.CREATE )

    self.obj162=CD_Class3(self)
    self.obj162.isGraphObjectVisual = True

    if(hasattr(self.obj162, '_setHierarchicalLink')):
      self.obj162._setHierarchicalLink(False)

    # QOCA
    self.obj162.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <---- Remove this to use QOCA\n\n""" Get the high level constraint helper and solver """\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.fixedWidth(self.graphObject_, self.graphObject_.sizeX)\noc.fixedHeight(self.graphObject_, self.graphObject_.sizeY)\n\n'))

    # Graphical_Appearance
    self.obj162.Graphical_Appearance.setValue( ('Process', self.obj162))

    # name
    self.obj162.name.setValue('Process')

    # attributes
    self.obj162.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj162.attributes.setValue(lcobj2)

    # Abstract
    self.obj162.Abstract.setValue((None, 0))
    self.obj162.Abstract.config = 0

    # cardinality
    self.obj162.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('canStartProcess', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('hasObjective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj162.cardinality.setValue(lcobj2)

    # display
    self.obj162.display.setValue('Attributes:\n  - Activities :: Text\n  - ID :: String\n  - Name :: String\nMultiplicities:\n  - From canStartProcess: 0 to N\n  - To hasObjective: 0 to N\n')
    self.obj162.display.setHeight(15)

    # Actions
    self.obj162.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj162.Actions.setValue(lcobj2)

    # Constraints
    self.obj162.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj162.Constraints.setValue(lcobj2)

    self.obj162.graphClass_= graph_CD_Class3
    if self.genGraphics:
       new_obj = graph_CD_Class3(280.0,80.0,self.obj162)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Class3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.23046875, 1.4459016393442625]
    else: new_obj = None
    self.obj162.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj162)
    self.globalAndLocalPostcondition(self.obj162, rootNode)
    self.obj162.postAction( rootNode.CREATE )

    self.obj163=CD_Association3(self)
    self.obj163.isGraphObjectVisual = True

    if(hasattr(self.obj163, '_setHierarchicalLink')):
      self.obj163._setHierarchicalLink(True)

    # QOCA
    self.obj163.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj163.Graphical_Appearance.setValue( ('isPartOfOrgUnit', self.obj163))
    self.obj163.Graphical_Appearance.linkInfo=linkEditor(self,self.obj163.Graphical_Appearance.semObject, "isPartOfOrgUnit")
    self.obj163.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj163.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj163.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj163.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj163.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj163.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj163.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj163.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj163.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfOrgUnit_1stLink', self.obj163.Graphical_Appearance.linkInfo.FirstLink))
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfOrgUnit_1stSegment', self.obj163.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj163.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj163.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfOrgUnit_Center', self.obj163.Graphical_Appearance.linkInfo))
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfOrgUnit_2ndSegment', self.obj163.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj163.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj163.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj163.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj163.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj163.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj163.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj163.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj163.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj163.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfOrgUnit_2ndLink', self.obj163.Graphical_Appearance.linkInfo.SecondLink))
    self.obj163.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj163.Graphical_Appearance.semObject
    self.obj163.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj163.Graphical_Appearance.semObject
    self.obj163.Graphical_Appearance.linkInfo.Center.semObject=self.obj163.Graphical_Appearance.semObject
    self.obj163.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj163.Graphical_Appearance.semObject
    self.obj163.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj163.Graphical_Appearance.semObject

    # name
    self.obj163.name.setValue('isPartOfOrgUnit')

    # displaySelect
    self.obj163.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj163.displaySelect.config = 0

    # attributes
    self.obj163.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj163.attributes.setValue(lcobj2)

    # cardinality
    self.obj163.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj163.cardinality.setValue(lcobj2)

    # display
    self.obj163.display.setValue('Multiplicities:\n  - From OrgUnit: 1 to N\n  - To OrgUnit: 1 to N\n')
    self.obj163.display.setHeight(15)

    # Actions
    self.obj163.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj163.Actions.setValue(lcobj2)

    # Constraints
    self.obj163.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj163.Constraints.setValue(lcobj2)

    self.obj163.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1387.9955984,65.809726225,self.obj163)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj163.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj163)
    self.globalAndLocalPostcondition(self.obj163, rootNode)
    self.obj163.postAction( rootNode.CREATE )

    self.obj164=CD_Association3(self)
    self.obj164.isGraphObjectVisual = True

    if(hasattr(self.obj164, '_setHierarchicalLink')):
      self.obj164._setHierarchicalLink(True)

    # QOCA
    self.obj164.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj164.Graphical_Appearance.setValue( ('canHaveRole', self.obj164))
    self.obj164.Graphical_Appearance.linkInfo=linkEditor(self,self.obj164.Graphical_Appearance.semObject, "canHaveRole")
    self.obj164.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj164.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj164.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj164.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj164.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj164.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj164.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj164.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj164.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canHaveRole_1stLink', self.obj164.Graphical_Appearance.linkInfo.FirstLink))
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canHaveRole_1stSegment', self.obj164.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj164.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj164.Graphical_Appearance.linkInfo.Center.setValue( ('canHaveRole_Center', self.obj164.Graphical_Appearance.linkInfo))
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canHaveRole_2ndSegment', self.obj164.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj164.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj164.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj164.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj164.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj164.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj164.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj164.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj164.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj164.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canHaveRole_2ndLink', self.obj164.Graphical_Appearance.linkInfo.SecondLink))
    self.obj164.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj164.Graphical_Appearance.semObject
    self.obj164.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj164.Graphical_Appearance.semObject
    self.obj164.Graphical_Appearance.linkInfo.Center.semObject=self.obj164.Graphical_Appearance.semObject
    self.obj164.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj164.Graphical_Appearance.semObject
    self.obj164.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj164.Graphical_Appearance.semObject

    # name
    self.obj164.name.setValue('canHaveRole')

    # displaySelect
    self.obj164.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj164.displaySelect.config = 0

    # attributes
    self.obj164.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj164.attributes.setValue(lcobj2)

    # cardinality
    self.obj164.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj164.cardinality.setValue(lcobj2)

    # display
    self.obj164.display.setValue('Multiplicities:\n  - From OrgUnit: 0 to N\n  - To Role: 0 to N\n')
    self.obj164.display.setHeight(15)

    # Actions
    self.obj164.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj164.Actions.setValue(lcobj2)

    # Constraints
    self.obj164.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj164.Constraints.setValue(lcobj2)

    self.obj164.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(971.7601868,527.680947659,self.obj164)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj164.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj164)
    self.globalAndLocalPostcondition(self.obj164, rootNode)
    self.obj164.postAction( rootNode.CREATE )

    self.obj165=CD_Association3(self)
    self.obj165.isGraphObjectVisual = True

    if(hasattr(self.obj165, '_setHierarchicalLink')):
      self.obj165._setHierarchicalLink(False)

    # QOCA
    self.obj165.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj165.Graphical_Appearance.setValue( ('hasActions', self.obj165))
    self.obj165.Graphical_Appearance.linkInfo=linkEditor(self,self.obj165.Graphical_Appearance.semObject, "hasActions")
    self.obj165.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj165.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj165.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj165.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj165.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj165.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj165.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj165.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj165.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasActions_1stLink', self.obj165.Graphical_Appearance.linkInfo.FirstLink))
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasActions_1stSegment', self.obj165.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj165.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj165.Graphical_Appearance.linkInfo.Center.setValue( ('hasActions_Center', self.obj165.Graphical_Appearance.linkInfo))
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasActions_2ndSegment', self.obj165.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj165.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj165.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj165.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj165.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj165.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj165.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj165.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj165.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj165.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasActions_2ndLink', self.obj165.Graphical_Appearance.linkInfo.SecondLink))
    self.obj165.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj165.Graphical_Appearance.semObject
    self.obj165.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj165.Graphical_Appearance.semObject
    self.obj165.Graphical_Appearance.linkInfo.Center.semObject=self.obj165.Graphical_Appearance.semObject
    self.obj165.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj165.Graphical_Appearance.semObject
    self.obj165.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj165.Graphical_Appearance.semObject

    # name
    self.obj165.name.setValue('hasActions')

    # displaySelect
    self.obj165.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj165.displaySelect.config = 0

    # attributes
    self.obj165.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj165.attributes.setValue(lcobj2)

    # cardinality
    self.obj165.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Action', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    self.obj165.cardinality.setValue(lcobj2)

    # display
    self.obj165.display.setValue('Multiplicities:\n  - To Action: 1 to N\n  - From Role: 1 to 1\n')
    self.obj165.display.setHeight(15)

    # Actions
    self.obj165.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj165.Actions.setValue(lcobj2)

    # Constraints
    self.obj165.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj165.Constraints.setValue(lcobj2)

    self.obj165.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(503.161248615,952.001803815,self.obj165)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj165.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj165)
    self.globalAndLocalPostcondition(self.obj165, rootNode)
    self.obj165.postAction( rootNode.CREATE )

    self.obj166=CD_Association3(self)
    self.obj166.isGraphObjectVisual = True

    if(hasattr(self.obj166, '_setHierarchicalLink')):
      self.obj166._setHierarchicalLink(False)

    # QOCA
    self.obj166.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj166.Graphical_Appearance.setValue( ('canAccessKnArt', self.obj166))
    self.obj166.Graphical_Appearance.linkInfo=linkEditor(self,self.obj166.Graphical_Appearance.semObject, "canAccessKnArt")
    self.obj166.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj166.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj166.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj166.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj166.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj166.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj166.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj166.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj166.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canAccessKnArt_1stLink', self.obj166.Graphical_Appearance.linkInfo.FirstLink))
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canAccessKnArt_1stSegment', self.obj166.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj166.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj166.Graphical_Appearance.linkInfo.Center.setValue( ('canAccessKnArt_Center', self.obj166.Graphical_Appearance.linkInfo))
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canAccessKnArt_2ndSegment', self.obj166.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj166.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj166.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj166.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj166.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj166.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj166.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj166.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj166.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj166.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canAccessKnArt_2ndLink', self.obj166.Graphical_Appearance.linkInfo.SecondLink))
    self.obj166.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj166.Graphical_Appearance.semObject
    self.obj166.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj166.Graphical_Appearance.semObject
    self.obj166.Graphical_Appearance.linkInfo.Center.semObject=self.obj166.Graphical_Appearance.semObject
    self.obj166.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj166.Graphical_Appearance.semObject
    self.obj166.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj166.Graphical_Appearance.semObject

    # name
    self.obj166.name.setValue('canAccessKnArt')

    # displaySelect
    self.obj166.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj166.displaySelect.config = 0

    # attributes
    self.obj166.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj166.attributes.setValue(lcobj2)

    # cardinality
    self.obj166.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj166.cardinality.setValue(lcobj2)

    # display
    self.obj166.display.setValue('Constraints:\n  > ConstraintKnArt\nMultiplicities:\n  - To OrganisationalKnArt: 0 to N\n  - From Role: 0 to N\n  - From OrgUnit: 0 to N\n  - To IndividualKnArt: 0 to N\n')
    self.obj166.display.setHeight(15)

    # Actions
    self.obj166.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj166.Actions.setValue(lcobj2)

    # Constraints
    self.obj166.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('ConstraintKnArt', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'from CustomCode import *\nres = canAccessKnArtCheckConnections(self)\n\nif res is "eitherRoleOrUnit":\n    return ("Either Role of OrgUnit can access knowledge.", self.graphObject_)\nelif res is "onlyOneInput":\n    return ("Only one Role or OrgUnit can access one knowledge medium.", self.graphObject_)\nelif res is "RoleWithOrgOnly":\n    return ("Role can access OrganisationalKnArt only!", self.graphObject_)\nelif res is "OrgUnitWithIndivOnly":\n    return ("OrgUnit can access IndividualKnArt only!", self.graphObject_)\nelse:\n    return\n\n'))
    lcobj2.append(cobj2)
    self.obj166.Constraints.setValue(lcobj2)

    self.obj166.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1106.462784,821.548234957,self.obj166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.6380000000000001, 1.8967741935483875]
    else: new_obj = None
    self.obj166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj166)
    self.globalAndLocalPostcondition(self.obj166, rootNode)
    self.obj166.postAction( rootNode.CREATE )

    self.obj167=CD_Association3(self)
    self.obj167.isGraphObjectVisual = True

    if(hasattr(self.obj167, '_setHierarchicalLink')):
      self.obj167._setHierarchicalLink(True)

    # QOCA
    self.obj167.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj167.Graphical_Appearance.setValue( ('isPartOfObjective', self.obj167))
    self.obj167.Graphical_Appearance.linkInfo=linkEditor(self,self.obj167.Graphical_Appearance.semObject, "isPartOfObjective")
    self.obj167.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj167.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj167.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj167.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj167.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj167.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj167.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj167.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj167.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfObjective_1stLink', self.obj167.Graphical_Appearance.linkInfo.FirstLink))
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfObjective_1stSegment', self.obj167.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj167.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj167.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfObjective_Center', self.obj167.Graphical_Appearance.linkInfo))
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfObjective_2ndSegment', self.obj167.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj167.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj167.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj167.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj167.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj167.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj167.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj167.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj167.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj167.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfObjective_2ndLink', self.obj167.Graphical_Appearance.linkInfo.SecondLink))
    self.obj167.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj167.Graphical_Appearance.semObject
    self.obj167.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj167.Graphical_Appearance.semObject
    self.obj167.Graphical_Appearance.linkInfo.Center.semObject=self.obj167.Graphical_Appearance.semObject
    self.obj167.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj167.Graphical_Appearance.semObject
    self.obj167.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj167.Graphical_Appearance.semObject

    # name
    self.obj167.name.setValue('isPartOfObjective')

    # displaySelect
    self.obj167.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj167.displaySelect.config = 0

    # attributes
    self.obj167.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj167.attributes.setValue(lcobj2)

    # cardinality
    self.obj167.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Objective', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj167.cardinality.setValue(lcobj2)

    # display
    self.obj167.display.setValue('Multiplicities:\n  - From Objective: 0 to N\n  - To Objective: 0 to N\n')
    self.obj167.display.setHeight(15)

    # Actions
    self.obj167.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj167.Actions.setValue(lcobj2)

    # Constraints
    self.obj167.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj167.Constraints.setValue(lcobj2)

    self.obj167.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(131.944046519,946.91223085,self.obj167)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.225, 1.0]
    else: new_obj = None
    self.obj167.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj167)
    self.globalAndLocalPostcondition(self.obj167, rootNode)
    self.obj167.postAction( rootNode.CREATE )

    self.obj168=CD_Association3(self)
    self.obj168.isGraphObjectVisual = True

    if(hasattr(self.obj168, '_setHierarchicalLink')):
      self.obj168._setHierarchicalLink(False)

    # QOCA
    self.obj168.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj168.Graphical_Appearance.setValue( ('hasObjective', self.obj168))
    self.obj168.Graphical_Appearance.linkInfo=linkEditor(self,self.obj168.Graphical_Appearance.semObject, "hasObjective")
    self.obj168.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj168.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj168.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj168.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj168.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj168.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj168.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj168.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj168.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('hasObjective_1stLink', self.obj168.Graphical_Appearance.linkInfo.FirstLink))
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('hasObjective_1stSegment', self.obj168.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj168.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj168.Graphical_Appearance.linkInfo.Center.setValue( ('hasObjective_Center', self.obj168.Graphical_Appearance.linkInfo))
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('hasObjective_2ndSegment', self.obj168.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj168.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj168.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj168.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj168.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj168.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj168.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj168.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj168.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj168.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('hasObjective_2ndLink', self.obj168.Graphical_Appearance.linkInfo.SecondLink))
    self.obj168.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj168.Graphical_Appearance.semObject
    self.obj168.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj168.Graphical_Appearance.semObject
    self.obj168.Graphical_Appearance.linkInfo.Center.semObject=self.obj168.Graphical_Appearance.semObject
    self.obj168.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj168.Graphical_Appearance.semObject
    self.obj168.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj168.Graphical_Appearance.semObject

    # name
    self.obj168.name.setValue('hasObjective')

    # displaySelect
    self.obj168.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj168.displaySelect.config = 0

    # attributes
    self.obj168.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj168.attributes.setValue(lcobj2)

    # cardinality
    self.obj168.cardinality.setActionFlags([ 0, 1, 0, 0])
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
    self.obj168.cardinality.setValue(lcobj2)

    # display
    self.obj168.display.setValue('Multiplicities:\n  - To Objective: 1 to N\n  - From Role: 0 to N\n  - From Process: 0 to N\n')
    self.obj168.display.setHeight(15)

    # Actions
    self.obj168.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj168.Actions.setValue(lcobj2)

    # Constraints
    self.obj168.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj168.Constraints.setValue(lcobj2)

    self.obj168.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(436.73445957,632.859445861,self.obj168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.1620000000000001, 1.0838709677419356]
    else: new_obj = None
    self.obj168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj168)
    self.globalAndLocalPostcondition(self.obj168, rootNode)
    self.obj168.postAction( rootNode.CREATE )

    self.obj169=CD_Association3(self)
    self.obj169.isGraphObjectVisual = True

    if(hasattr(self.obj169, '_setHierarchicalLink')):
      self.obj169._setHierarchicalLink(False)

    # QOCA
    self.obj169.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj169.Graphical_Appearance.setValue( ('genericAssociation', self.obj169))
    self.obj169.Graphical_Appearance.linkInfo=linkEditor(self,self.obj169.Graphical_Appearance.semObject, "genericAssociation")
    self.obj169.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj169.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj169.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj169.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj169.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj169.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj169.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj169.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj169.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('genericAssociation_1stLink', self.obj169.Graphical_Appearance.linkInfo.FirstLink))
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('genericAssociation_1stSegment', self.obj169.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj169.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj169.Graphical_Appearance.linkInfo.Center.setValue( ('genericAssociation_Center', self.obj169.Graphical_Appearance.linkInfo))
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('genericAssociation_2ndSegment', self.obj169.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj169.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj169.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj169.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj169.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj169.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj169.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj169.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj169.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj169.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('genericAssociation_2ndLink', self.obj169.Graphical_Appearance.linkInfo.SecondLink))
    self.obj169.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj169.Graphical_Appearance.semObject
    self.obj169.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj169.Graphical_Appearance.semObject
    self.obj169.Graphical_Appearance.linkInfo.Center.semObject=self.obj169.Graphical_Appearance.semObject
    self.obj169.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj169.Graphical_Appearance.semObject
    self.obj169.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj169.Graphical_Appearance.semObject

    # name
    self.obj169.name.setValue('genericAssociation')

    # displaySelect
    self.obj169.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj169.displaySelect.config = 0

    # attributes
    self.obj169.attributes.setActionFlags([ 1, 1, 1, 0])
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
    self.obj169.attributes.setValue(lcobj2)

    # cardinality
    self.obj169.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj169.cardinality.setValue(lcobj2)

    # display
    self.obj169.display.setValue('Attributes:\n  - Name :: String\n  - Description :: Text\nMultiplicities:\n  - To Role: 1 to N\n  - From Role: 1 to N\n')
    self.obj169.display.setHeight(15)

    # Actions
    self.obj169.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj169.Actions.setValue(lcobj2)

    # Constraints
    self.obj169.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj169.Constraints.setValue(lcobj2)

    self.obj169.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1044.0,340.0,self.obj169)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.015, 1.6258064516129034]
    else: new_obj = None
    self.obj169.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj169)
    self.globalAndLocalPostcondition(self.obj169, rootNode)
    self.obj169.postAction( rootNode.CREATE )

    self.obj170=CD_Association3(self)
    self.obj170.isGraphObjectVisual = True

    if(hasattr(self.obj170, '_setHierarchicalLink')):
      self.obj170._setHierarchicalLink(True)

    # QOCA
    self.obj170.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj170.Graphical_Appearance.setValue( ('answersToRole', self.obj170))
    self.obj170.Graphical_Appearance.linkInfo=linkEditor(self,self.obj170.Graphical_Appearance.semObject, "answersToRole")
    self.obj170.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj170.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj170.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj170.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj170.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj170.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj170.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj170.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj170.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToRole_1stLink', self.obj170.Graphical_Appearance.linkInfo.FirstLink))
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToRole_1stSegment', self.obj170.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj170.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj170.Graphical_Appearance.linkInfo.Center.setValue( ('answersToRole_Center', self.obj170.Graphical_Appearance.linkInfo))
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToRole_2ndSegment', self.obj170.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj170.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj170.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj170.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj170.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj170.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj170.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj170.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj170.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj170.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToRole_2ndLink', self.obj170.Graphical_Appearance.linkInfo.SecondLink))
    self.obj170.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj170.Graphical_Appearance.semObject
    self.obj170.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj170.Graphical_Appearance.semObject
    self.obj170.Graphical_Appearance.linkInfo.Center.semObject=self.obj170.Graphical_Appearance.semObject
    self.obj170.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj170.Graphical_Appearance.semObject
    self.obj170.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj170.Graphical_Appearance.semObject

    # name
    self.obj170.name.setValue('answersToRole')

    # displaySelect
    self.obj170.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj170.displaySelect.config = 0

    # attributes
    self.obj170.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj170.attributes.setValue(lcobj2)

    # cardinality
    self.obj170.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj170.cardinality.setValue(lcobj2)

    # display
    self.obj170.display.setValue('Multiplicities:\n  - From Role: 1 to N\n  - To Role: 1 to N\n')
    self.obj170.display.setHeight(15)

    # Actions
    self.obj170.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj170.Actions.setValue(lcobj2)

    # Constraints
    self.obj170.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj170.Constraints.setValue(lcobj2)

    self.obj170.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(933.0,176.0,self.obj170)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj170.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj170)
    self.globalAndLocalPostcondition(self.obj170, rootNode)
    self.obj170.postAction( rootNode.CREATE )

    self.obj171=CD_Association3(self)
    self.obj171.isGraphObjectVisual = True

    if(hasattr(self.obj171, '_setHierarchicalLink')):
      self.obj171._setHierarchicalLink(False)

    # QOCA
    self.obj171.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj171.Graphical_Appearance.setValue( ('canStartProcess', self.obj171))
    self.obj171.Graphical_Appearance.linkInfo=linkEditor(self,self.obj171.Graphical_Appearance.semObject, "canStartProcess")
    self.obj171.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj171.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj171.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj171.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj171.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj171.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj171.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj171.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj171.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('canStartProcess_1stLink', self.obj171.Graphical_Appearance.linkInfo.FirstLink))
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('canStartProcess_1stSegment', self.obj171.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj171.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj171.Graphical_Appearance.linkInfo.Center.setValue( ('canStartProcess_Center', self.obj171.Graphical_Appearance.linkInfo))
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('canStartProcess_2ndSegment', self.obj171.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj171.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj171.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj171.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj171.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj171.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj171.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj171.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj171.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj171.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('canStartProcess_2ndLink', self.obj171.Graphical_Appearance.linkInfo.SecondLink))
    self.obj171.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj171.Graphical_Appearance.semObject
    self.obj171.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj171.Graphical_Appearance.semObject
    self.obj171.Graphical_Appearance.linkInfo.Center.semObject=self.obj171.Graphical_Appearance.semObject
    self.obj171.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj171.Graphical_Appearance.semObject
    self.obj171.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj171.Graphical_Appearance.semObject

    # name
    self.obj171.name.setValue('canStartProcess')

    # displaySelect
    self.obj171.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj171.displaySelect.config = 0

    # attributes
    self.obj171.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj171.attributes.setValue(lcobj2)

    # cardinality
    self.obj171.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Process', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj171.cardinality.setValue(lcobj2)

    # display
    self.obj171.display.setValue('Multiplicities:\n  - To Process: 0 to N\n  - From Role: 0 to N\n')
    self.obj171.display.setHeight(15)

    # Actions
    self.obj171.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj171.Actions.setValue(lcobj2)

    # Constraints
    self.obj171.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj171.Constraints.setValue(lcobj2)

    self.obj171.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(470.4921875,411.163934426,self.obj171)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.036, 1.0]
    else: new_obj = None
    self.obj171.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj171)
    self.globalAndLocalPostcondition(self.obj171, rootNode)
    self.obj171.postAction( rootNode.CREATE )

    self.obj172=CD_Association3(self)
    self.obj172.isGraphObjectVisual = True

    if(hasattr(self.obj172, '_setHierarchicalLink')):
      self.obj172._setHierarchicalLink(True)

    # QOCA
    self.obj172.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj172.Graphical_Appearance.setValue( ('answersToOrgUnit', self.obj172))
    self.obj172.Graphical_Appearance.linkInfo=linkEditor(self,self.obj172.Graphical_Appearance.semObject, "answersToOrgUnit")
    self.obj172.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj172.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj172.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj172.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj172.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj172.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj172.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj172.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj172.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('answersToOrgUnit_1stLink', self.obj172.Graphical_Appearance.linkInfo.FirstLink))
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('answersToOrgUnit_1stSegment', self.obj172.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj172.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj172.Graphical_Appearance.linkInfo.Center.setValue( ('answersToOrgUnit_Center', self.obj172.Graphical_Appearance.linkInfo))
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('answersToOrgUnit_2ndSegment', self.obj172.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj172.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj172.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj172.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj172.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj172.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj172.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj172.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj172.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj172.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('answersToOrgUnit_2ndLink', self.obj172.Graphical_Appearance.linkInfo.SecondLink))
    self.obj172.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj172.Graphical_Appearance.semObject
    self.obj172.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj172.Graphical_Appearance.semObject
    self.obj172.Graphical_Appearance.linkInfo.Center.semObject=self.obj172.Graphical_Appearance.semObject
    self.obj172.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj172.Graphical_Appearance.semObject
    self.obj172.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj172.Graphical_Appearance.semObject

    # name
    self.obj172.name.setValue('answersToOrgUnit')

    # displaySelect
    self.obj172.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj172.displaySelect.config = 0

    # attributes
    self.obj172.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj172.attributes.setValue(lcobj2)

    # cardinality
    self.obj172.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('OrgUnit', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj172.cardinality.setValue(lcobj2)

    # display
    self.obj172.display.setValue('Multiplicities:\n  - To OrgUnit: 1 to N\n  - From OrgUnit: 1 to N\n')
    self.obj172.display.setHeight(15)

    # Actions
    self.obj172.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj172.Actions.setValue(lcobj2)

    # Constraints
    self.obj172.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj172.Constraints.setValue(lcobj2)

    self.obj172.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(1113.0,79.0,self.obj172)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.141, 1.0]
    else: new_obj = None
    self.obj172.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj172)
    self.globalAndLocalPostcondition(self.obj172, rootNode)
    self.obj172.postAction( rootNode.CREATE )

    self.obj173=CD_Association3(self)
    self.obj173.isGraphObjectVisual = True

    if(hasattr(self.obj173, '_setHierarchicalLink')):
      self.obj173._setHierarchicalLink(True)

    # QOCA
    self.obj173.QOCA.setValue(('QOCA', (['Python', 'OCL'], 1), (['PREaction', 'POSTaction'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '"""\nQOCA Constraint Template\nNOTE: DO NOT select a POST/PRE action trigger\nConstraints will be added/removed in a logical manner by other mechanisms.\n"""\nreturn # <--- Remove this if you want to use QOCA\n\n# Get the high level constraint helper and solver\nfrom Qoca.atom3constraints.OffsetConstraints import OffsetConstraints\noc = OffsetConstraints(self.parent.qocaSolver)  \n\n# Constraint only makes sense if there exists 2 objects connected to this link\nif(not (self.in_connections_ and self.out_connections_)): return\n\n# Get the graphical objects (subclass of graphEntity/graphLink) \ngraphicalObjectLink = self.graphObject_\ngraphicalObjectSource = self.in_connections_[0].graphObject_\ngraphicalObjectTarget = self.out_connections_[0].graphObject_\nobjTuple = (graphicalObjectSource, graphicalObjectTarget, graphicalObjectLink)\n\n"""\nExample constraint, see Kernel/QOCA/atom3constraints/OffsetConstraints.py\nFor more types of constraints\n"""\noc.LeftExactDistance(objTuple, 20)\noc.resolve() # Resolve immediately after creating entity & constraint \n\n'))

    # Graphical_Appearance
    self.obj173.Graphical_Appearance.setValue( ('isPartOfRole', self.obj173))
    self.obj173.Graphical_Appearance.linkInfo=linkEditor(self,self.obj173.Graphical_Appearance.semObject, "isPartOfRole")
    self.obj173.Graphical_Appearance.linkInfo.FirstLink= stickylink()
    self.obj173.Graphical_Appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj173.Graphical_Appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj173.Graphical_Appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj173.Graphical_Appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(8)
    self.obj173.Graphical_Appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(10)
    self.obj173.Graphical_Appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(3)
    self.obj173.Graphical_Appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj173.Graphical_Appearance.linkInfo.FirstLink.decoration.setValue( ('isPartOfRole_1stLink', self.obj173.Graphical_Appearance.linkInfo.FirstLink))
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.width=ATOM3Integer(2)
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.fill=ATOM3String('black', 20)
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.stipple=ATOM3String('', 20)
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(8)
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(10)
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(3)
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.decoration.setValue( ('isPartOfRole_1stSegment', self.obj173.Graphical_Appearance.linkInfo.FirstSegment))
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj173.Graphical_Appearance.linkInfo.Center=ATOM3Appearance()
    self.obj173.Graphical_Appearance.linkInfo.Center.setValue( ('isPartOfRole_Center', self.obj173.Graphical_Appearance.linkInfo))
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.width=ATOM3Integer(2)
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.fill=ATOM3String('black', 20)
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.stipple=ATOM3String('', 20)
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(8)
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(10)
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(3)
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.decoration.setValue( ('isPartOfRole_2ndSegment', self.obj173.Graphical_Appearance.linkInfo.SecondSegment))
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],0,0)
    self.obj173.Graphical_Appearance.linkInfo.SecondLink= stickylink()
    self.obj173.Graphical_Appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj173.Graphical_Appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj173.Graphical_Appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj173.Graphical_Appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(8)
    self.obj173.Graphical_Appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj173.Graphical_Appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj173.Graphical_Appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj173.Graphical_Appearance.linkInfo.SecondLink.decoration.setValue( ('isPartOfRole_2ndLink', self.obj173.Graphical_Appearance.linkInfo.SecondLink))
    self.obj173.Graphical_Appearance.linkInfo.FirstLink.decoration.semObject=self.obj173.Graphical_Appearance.semObject
    self.obj173.Graphical_Appearance.linkInfo.FirstSegment.decoration.semObject=self.obj173.Graphical_Appearance.semObject
    self.obj173.Graphical_Appearance.linkInfo.Center.semObject=self.obj173.Graphical_Appearance.semObject
    self.obj173.Graphical_Appearance.linkInfo.SecondSegment.decoration.semObject=self.obj173.Graphical_Appearance.semObject
    self.obj173.Graphical_Appearance.linkInfo.SecondLink.decoration.semObject=self.obj173.Graphical_Appearance.semObject

    # name
    self.obj173.name.setValue('isPartOfRole')

    # displaySelect
    self.obj173.displaySelect.setValue( (['attributes', 'constraints', 'actions', 'cardinality'], [0, 0, 0, 0]) )
    self.obj173.displaySelect.config = 0

    # attributes
    self.obj173.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj173.attributes.setValue(lcobj2)

    # cardinality
    self.obj173.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('Role', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj173.cardinality.setValue(lcobj2)

    # display
    self.obj173.display.setValue('Multiplicities:\n  - From Role: 0 to N\n  - To Role: 0 to N\n')
    self.obj173.display.setHeight(15)

    # Actions
    self.obj173.Actions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj173.Actions.setValue(lcobj2)

    # Constraints
    self.obj173.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj173.Constraints.setValue(lcobj2)

    self.obj173.graphClass_= graph_CD_Association3
    if self.genGraphics:
       new_obj = graph_CD_Association3(675.0,160.0,self.obj173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Association3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj173)
    self.globalAndLocalPostcondition(self.obj173, rootNode)
    self.obj173.postAction( rootNode.CREATE )

    self.obj174=CD_Inheritance3(self)
    self.obj174.isGraphObjectVisual = True

    if(hasattr(self.obj174, '_setHierarchicalLink')):
      self.obj174._setHierarchicalLink(False)

    self.obj174.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1056.21888986,1366.92763695,self.obj174)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj174.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj174)
    self.globalAndLocalPostcondition(self.obj174, rootNode)
    self.obj174.postAction( rootNode.CREATE )

    self.obj175=CD_Inheritance3(self)
    self.obj175.isGraphObjectVisual = True

    if(hasattr(self.obj175, '_setHierarchicalLink')):
      self.obj175._setHierarchicalLink(False)

    self.obj175.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(1136.90914946,1358.75085967,self.obj175)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj175.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj175)
    self.globalAndLocalPostcondition(self.obj175, rootNode)
    self.obj175.postAction( rootNode.CREATE )

    self.obj176=CD_Inheritance3(self)
    self.obj176.isGraphObjectVisual = True

    if(hasattr(self.obj176, '_setHierarchicalLink')):
      self.obj176._setHierarchicalLink(False)

    self.obj176.graphClass_= graph_CD_Inheritance3
    if self.genGraphics:
       new_obj = graph_CD_Inheritance3(152.858254695,586.846159545,self.obj176)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("CD_Inheritance3", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj176.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj176)
    self.globalAndLocalPostcondition(self.obj176, rootNode)
    self.obj176.postAction( rootNode.CREATE )

    # Connections for obj154 (graphObject_: Obj185) named OrgUnit
    self.drawConnections(
(self.obj154,self.obj163,[1368.8125, 220.52459016393442, 1387.9955983980042, 65.8097262245276, 1387.9955984, 65.80972622499999],"true", 3),
(self.obj154,self.obj164,[1241.14453125, 483.0655737704918, 967.8422485527899, 481.40176688146084, 971.7601868, 527.680947659],"true", 3),
(self.obj154,self.obj166,[1241.14453125, 483.0655737704918, 997.8287423035672, 492.3266545159663, 1106.462784, 821.548234957],"true", 3),
(self.obj154,self.obj172,[1241.14453125, 323.8032786885246, 1130.0, 231.0, 1113.0, 79.0], 0, 3) )
    # Connections for obj155 (graphObject_: Obj186) named Role
    self.drawConnections(
(self.obj155,self.obj165,[660.0, 811.0, 541.1631302538499, 883.356649681594, 503.161248615, 952.001803815],"true", 3),
(self.obj155,self.obj166,[832.921875, 735.2622950819672, 1023.5805784296024, 714.1457487347751, 1106.462784, 821.548234957],"true", 3),
(self.obj155,self.obj168,[620.953125, 538.344262295082, 522.0012232889502, 553.7739542825374, 436.73445957, 632.859445861],"true", 3),
(self.obj155,self.obj169,[832.921875, 432.3114754098361, 1044.0, 340.0], 0, 2),
(self.obj155,self.obj170,[793.875, 280.8360655737705, 933.0, 176.0], 0, 2),
(self.obj155,self.obj171,[620.953125, 432.3114754098361, 470.4921875, 411.163934426], 0, 2),
(self.obj155,self.obj173,[660.0, 280.8360655737705, 675.0, 160.0],"true", 2) )
    # Connections for obj156 (graphObject_: Obj187) named Action
    self.drawConnections(
 )
    # Connections for obj157 (graphObject_: Obj188) named KnowledgeArtifacts
    self.drawConnections(
 )
    # Connections for obj158 (graphObject_: Obj189) named OrganisationalKnArt
    self.drawConnections(
(self.obj158,self.obj174,[935.5703125, 1206.090909090909, 1056.21888986, 1366.92763695],"true", 2) )
    # Connections for obj159 (graphObject_: Obj190) named IndividualKnArt
    self.drawConnections(
(self.obj159,self.obj175,[1240.7421875, 1186.090909090909, 1136.90914946, 1358.75085967],"true", 2) )
    # Connections for obj160 (graphObject_: Obj191) named Strategy
    self.drawConnections(
 )
    # Connections for obj161 (graphObject_: Obj192) named Objective
    self.drawConnections(
(self.obj161,self.obj176,[139.75, 629.4918032786885, 152.858254695, 586.846159545],"true", 2),
(self.obj161,self.obj167,[139.75, 803.0, 131.94404651894035, 946.9122308488277, 131.944046519, 946.91223085],"true", 3) )
    # Connections for obj162 (graphObject_: Obj193) named Process
    self.drawConnections(
(self.obj162,self.obj168,[324.0, 283.0, 333.0, 453.0, 436.73445957, 632.859445861],"true", 3) )
    # Connections for obj163 (graphObject_: Obj194) named isPartOfOrgUnit
    self.drawConnections(
(self.obj163,self.obj154,[1387.9955984, 65.80972622499999, 1387.9955983980042, 65.8097262245276, 1368.8125, 220.52459016393442],"true", 3) )
    # Connections for obj164 (graphObject_: Obj196) named canHaveRole
    self.drawConnections(
(self.obj164,self.obj155,[971.7601868, 527.680947659, 975.67812505129, 573.9601284363068, 832.921875, 538.344262295082],"true", 3) )
    # Connections for obj165 (graphObject_: Obj198) named hasActions
    self.drawConnections(
(self.obj165,self.obj156,[503.161248615, 952.001803815, 465.1593669760688, 1020.6469579482074, 741.20703125, 946.0909090909091],"true", 3) )
    # Connections for obj166 (graphObject_: Obj200) named canAccessKnArt
    self.drawConnections(
(self.obj166,self.obj158,[1106.462784, 821.548234957, 1128.2678325033444, 887.9439489105719, 935.5703125, 1122.4545454545455],"true", 3),
(self.obj166,self.obj159,[1106.462784, 821.548234957, 1033.4035107781324, 923.4763808302594, 1240.7421875, 1102.4545454545455],"true", 3) )
    # Connections for obj167 (graphObject_: Obj202) named isPartOfObjective
    self.drawConnections(
(self.obj167,self.obj161,[131.944046519, 946.91223085, 131.94404651894035, 946.9122308488277, 139.75, 803.0],"true", 3) )
    # Connections for obj168 (graphObject_: Obj204) named hasObjective
    self.drawConnections(
(self.obj168,self.obj161,[436.73445957, 632.859445861, 351.4676958509182, 711.9449374392455, 281.65625, 698.8950819672131],"true", 3) )
    # Connections for obj169 (graphObject_: Obj206) named genericAssociation
    self.drawConnections(
(self.obj169,self.obj155,[1044.0, 340.0, 832.921875, 432.3114754098361], 0, 2) )
    # Connections for obj170 (graphObject_: Obj208) named answersToRole
    self.drawConnections(
(self.obj170,self.obj155,[933.0, 176.0, 793.875, 280.8360655737705], 0, 2) )
    # Connections for obj171 (graphObject_: Obj210) named canStartProcess
    self.drawConnections(
(self.obj171,self.obj162,[470.4921875, 411.163934426, 471.65625, 283.0], 0, 2) )
    # Connections for obj172 (graphObject_: Obj212) named answersToOrgUnit
    self.drawConnections(
(self.obj172,self.obj154,[1113.0, 79.0, 1279.0, 145.0, 1280.0, 220.52459016393442], 0, 3) )
    # Connections for obj173 (graphObject_: Obj214) named isPartOfRole
    self.drawConnections(
(self.obj173,self.obj155,[675.0, 160.0, 660.0, 280.8360655737705],"true", 2) )
    # Connections for obj174 (graphObject_: Obj216) of type CD_Inheritance3
    self.drawConnections(
(self.obj174,self.obj157,[1056.21888986, 1366.92763695, 1073.0, 1255.0],"true", 2) )
    # Connections for obj175 (graphObject_: Obj218) of type CD_Inheritance3
    self.drawConnections(
(self.obj175,self.obj157,[1136.90914946, 1358.75085967, 1153.0, 1255.0],"true", 2) )
    # Connections for obj176 (graphObject_: Obj220) of type CD_Inheritance3
    self.drawConnections(
(self.obj176,self.obj160,[152.858254695, 586.846159545, 156.0, 487.0],"true", 2) )

newfunction = LSMASOMM_MDL

loadedMMName = 'CD_ClassDiagramsV3_META'

atom3version = '0.3'
