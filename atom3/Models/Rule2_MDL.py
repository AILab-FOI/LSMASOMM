"""
__Rule2_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Tue May  1 01:18:03 2018
___________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from isPartOfOrgUnit import *
from canHaveRole import *
from graph_isPartOfOrgUnit import *
from graph_canHaveRole import *
from graph_OrgUnit import *
from graph_Role import *
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

def Rule2_MDL(self, rootNode, LSMASOMMRootNode=None):

    # --- Generating attributes code for ASG LSMASOMM ---
    if( LSMASOMMRootNode ): 
        # agentImplementation
        LSMASOMMRootNode.agentImplementation.setValue( (['SPADE', 'Enmasse', 'EveJS'], 0) )
        LSMASOMMRootNode.agentImplementation.config = 0

        # author
        LSMASOMMRootNode.author.setValue('Annonymous')

        # description
        LSMASOMMRootNode.description.setValue('\n')
        LSMASOMMRootNode.description.setHeight(15)

        # name
        LSMASOMMRootNode.name.setValue('LSMASOMM')

        # title
        LSMASOMMRootNode.title.setValue('')
        LSMASOMMRootNode.title.setNone()
    # --- ASG attributes over ---


    self.obj44=OrgUnit(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # Individual
    self.obj44.Individual.setNone()
    self.obj44.Individual.config = 0

    # hasActions
    self.obj44.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj44.hasActions.setValue(lcobj2)
    self.obj44.hasActions.setNone()

    # ID
    self.obj44.ID.setValue('<ID>')

    # name
    self.obj44.name.setValue('4:Agent')

    # UnitSize
    self.obj44.UnitSize.setValue('Individual')

    self.obj44.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(190.0,110.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj51=OrgUnit(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # Individual
    self.obj51.Individual.setValue(('1', 0))
    self.obj51.Individual.config = 0

    # hasActions
    self.obj51.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj51.hasActions.setValue(lcobj2)

    # ID
    self.obj51.ID.setValue('OU|1')

    # name
    self.obj51.name.setValue('9:Party')

    # UnitSize
    self.obj51.UnitSize.setValue('Group')

    self.obj51.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(310.0,20.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj45=Role(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # isMetaRole
    self.obj45.isMetaRole.setNone()
    self.obj45.isMetaRole.config = 0

    # hasActions
    self.obj45.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj45.hasActions.setValue(lcobj2)
    self.obj45.hasActions.setNone()

    # ID
    self.obj45.ID.setValue('')
    self.obj45.ID.setNone()

    # name
    self.obj45.name.setValue('5:PartyFounder')

    self.obj45.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(110.0,40.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=Role(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # isMetaRole
    self.obj46.isMetaRole.setValue((None, 0))
    self.obj46.isMetaRole.config = 0

    # hasActions
    self.obj46.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj46.hasActions.setValue(lcobj2)

    # ID
    self.obj46.ID.setValue('R|1')

    # name
    self.obj46.name.setValue('6:Wizard')

    self.obj46.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(395.0,37.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=Role(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # isMetaRole
    self.obj47.isMetaRole.setValue((None, 0))
    self.obj47.isMetaRole.config = 0

    # hasActions
    self.obj47.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj47.hasActions.setValue(lcobj2)

    # ID
    self.obj47.ID.setValue('R|2')

    # name
    self.obj47.name.setValue('7:Warrior')

    self.obj47.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(395.0,117.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=Role(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # isMetaRole
    self.obj48.isMetaRole.setValue((None, 0))
    self.obj48.isMetaRole.config = 0

    # hasActions
    self.obj48.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj48.hasActions.setValue(lcobj2)

    # ID
    self.obj48.ID.setValue('R|3')

    # name
    self.obj48.name.setValue('8:Rogue')

    self.obj48.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(395.0,197.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj54=isPartOfOrgUnit(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(True)

    # ID
    self.obj54.ID.setValue('pOU|0')

    self.obj54.graphClass_= graph_isPartOfOrgUnit
    if self.genGraphics:
       new_obj = graph_isPartOfOrgUnit(281.0,125.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfOrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj49=canHaveRole(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(True)

    # ID
    self.obj49.ID.setValue('OUR|0')

    self.obj49.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(164.313601367,184.51517325,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.01
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=canHaveRole(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(True)

    # ID
    self.obj50.ID.setValue('OUR|1')

    self.obj50.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(355.0,213.200313212,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    # Connections for obj44 (graphObject_: Obj0) named 4:Agent
    self.drawConnections(
(self.obj44,self.obj49,[217.0, 173.0, 189.56360136704075, 202.51517324964826, 164.31360136704075, 184.51517324964829],"true", 3),
(self.obj44,self.obj50,[217.0, 173.0, 305.6555677534886, 177.93308108723073, 355.0, 213.20031321170455],"true", 3),
(self.obj44,self.obj54,[217.0, 173.0, 253.0, 163.0, 281.0, 125.0],"true", 3) )
    # Connections for obj51 (graphObject_: Obj9) named 9:Party
    self.drawConnections(
 )
    # Connections for obj45 (graphObject_: Obj1) named 5:PartyFounder
    self.drawConnections(
 )
    # Connections for obj46 (graphObject_: Obj2) named 6:Wizard
    self.drawConnections(
 )
    # Connections for obj47 (graphObject_: Obj3) named 7:Warrior
    self.drawConnections(
 )
    # Connections for obj48 (graphObject_: Obj4) named 8:Rogue
    self.drawConnections(
 )
    # Connections for obj54 (graphObject_: Obj10) of type isPartOfOrgUnit
    self.drawConnections(
(self.obj54,self.obj51,[281.0, 125.0, 303.0, 95.0, 341.0, 83.0],"true", 3) )
    # Connections for obj49 (graphObject_: Obj5) of type canHaveRole
    self.drawConnections(
(self.obj49,self.obj45,[164.313601367, 184.51517325, 128.06360136704077, 141.51517324964829, 168.0, 92.0],"true", 3) )
    # Connections for obj50 (graphObject_: Obj7) of type canHaveRole
    self.drawConnections(
(self.obj50,self.obj46,[355.0, 213.200313212, 378.4004858684716, 114.16690138881552, 426.0, 89.0],"true", 3),
(self.obj50,self.obj47,[355.0, 213.20031321170455, 388.8393270686922, 168.72872841309487, 428.0, 169.0],"true", 3),
(self.obj50,self.obj48,[355.0, 213.20031321170455, 428.0663407567719, 247.35243175707808, 426.0, 249.0],"true", 3) )

newfunction = Rule2_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
