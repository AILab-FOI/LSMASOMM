"""
__TMWQDE_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Mon Nov 14 16:55:27 2016
____________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from OrganisationalKnArt import *
from IndividualKnArt import *
from Objective import *
from Process import *
from isPartOfOrgUnit import *
from canHaveRole import *
from canAccessKnArt import *
from isPartOfObjective import *
from hasObjective import *
from canStartProcess import *
from isPartOfRole import *
from graph_canHaveRole import *
from graph_OrganisationalKnArt import *
from graph_canAccessKnArt import *
from graph_Process import *
from graph_isPartOfOrgUnit import *
from graph_isPartOfObjective import *
from graph_hasObjective import *
from graph_isPartOfRole import *
from graph_Objective import *
from graph_OrgUnit import *
from graph_IndividualKnArt import *
from graph_canStartProcess import *
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

def TMWQDE_MDL(self, rootNode, LSMASOMMRootNode=None):

    # --- Generating attributes code for ASG LSMASOMM ---
    if( LSMASOMMRootNode ): 
        # author
        LSMASOMMRootNode.author.setValue('Annonymous')

        # description
        LSMASOMMRootNode.description.setValue('\n')
        LSMASOMMRootNode.description.setHeight(15)

        # name
        LSMASOMMRootNode.name.setValue('')
        LSMASOMMRootNode.name.setNone()
    # --- ASG attributes over ---


    self.obj43=OrgUnit(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # Individual
    self.obj43.Individual.setValue((None, 1))
    self.obj43.Individual.config = 0

    # UnitActions
    self.obj43.UnitActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj43.UnitActions.setValue(lcobj2)

    # UnitSize
    self.obj43.UnitSize.setValue('Group')

    # name
    self.obj43.name.setValue('orgUnitName')

    self.obj43.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(1200.0,700.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=OrgUnit(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # Individual
    self.obj44.Individual.setValue((None, 1))
    self.obj44.Individual.config = 0

    # UnitActions
    self.obj44.UnitActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj44.UnitActions.setValue(lcobj2)

    # UnitSize
    self.obj44.UnitSize.setValue('Individual')

    # name
    self.obj44.name.setValue('orgUnitName')

    self.obj44.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(994.0,792.8,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=OrgUnit(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # Individual
    self.obj45.Individual.setValue((None, 1))
    self.obj45.Individual.config = 0

    # UnitActions
    self.obj45.UnitActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj45.UnitActions.setValue(lcobj2)

    # UnitSize
    self.obj45.UnitSize.setValue('Individual')

    # name
    self.obj45.name.setValue('orgUnitName')

    self.obj45.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(231.4,811.2,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
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
    self.obj46.isMetaRole.setValue(('isMetaRole', 1))
    self.obj46.isMetaRole.config = 0

    # roleActions
    self.obj46.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('LookForItem', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('GatherItem', 20)
    lcobj2.append(cobj2)
    self.obj46.roleActions.setValue(lcobj2)

    # ID
    self.obj46.ID.setValue('Role0001')

    # name
    self.obj46.name.setValue('Gatherer')

    self.obj46.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(194.0,635.2,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
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
    self.obj47.isMetaRole.setValue(('isMetaRole', 0))
    self.obj47.isMetaRole.config = 0

    # roleActions
    self.obj47.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('PickItemUp', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('GoToLocation', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('DropItem', 20)
    lcobj2.append(cobj2)
    self.obj47.roleActions.setValue(lcobj2)

    # ID
    self.obj47.ID.setValue('Role0003')

    # name
    self.obj47.name.setValue('Transporter')

    self.obj47.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(613.2,635.2,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
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
    self.obj48.isMetaRole.setValue(('isMetaRole', 1))
    self.obj48.isMetaRole.config = 0

    # roleActions
    self.obj48.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('MakeItem', 20)
    lcobj2.append(cobj2)
    self.obj48.roleActions.setValue(lcobj2)

    # ID
    self.obj48.ID.setValue('Role0002')

    # name
    self.obj48.name.setValue('Maker')

    self.obj48.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(432.4,636.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=Role(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # isMetaRole
    self.obj49.isMetaRole.setValue(('isMetaRole', 0))
    self.obj49.isMetaRole.config = 0

    # roleActions
    self.obj49.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('Wander', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Retreat', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('LookForItem', 20)
    lcobj2.append(cobj2)
    self.obj49.roleActions.setValue(lcobj2)

    # ID
    self.obj49.ID.setValue('Role0005')

    # name
    self.obj49.name.setValue('Scout')

    self.obj49.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(940.0,640.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=Role(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # isMetaRole
    self.obj50.isMetaRole.setValue(('isMetaRole', 0))
    self.obj50.isMetaRole.config = 0

    # roleActions
    self.obj50.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('Attack', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Defend', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Retreat', 20)
    lcobj2.append(cobj2)
    self.obj50.roleActions.setValue(lcobj2)

    # ID
    self.obj50.ID.setValue('Role0004')

    # name
    self.obj50.name.setValue('Warrior')

    self.obj50.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(770.0,635.2,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=Role(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # isMetaRole
    self.obj51.isMetaRole.setValue(('isMetaRole', 1))
    self.obj51.isMetaRole.config = 0

    # roleActions
    self.obj51.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('LookForQuest', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('TakeQuest', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('FinishQuest', 20)
    lcobj2.append(cobj2)
    self.obj51.roleActions.setValue(lcobj2)

    # ID
    self.obj51.ID.setValue('Role0006')

    # name
    self.obj51.name.setValue('Quester')

    self.obj51.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(1065.2,634.4,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=Role(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # isMetaRole
    self.obj52.isMetaRole.setValue(('isMetaRole', 0))
    self.obj52.isMetaRole.config = 0

    # roleActions
    self.obj52.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('IdentifyHerb', 20)
    lcobj2.append(cobj2)
    self.obj52.roleActions.setValue(lcobj2)

    # ID
    self.obj52.ID.setValue('Role000101')

    # name
    self.obj52.name.setValue('Herbalist')

    self.obj52.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(82.0,465.6,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=Role(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # isMetaRole
    self.obj53.isMetaRole.setValue(('isMetaRole', 0))
    self.obj53.isMetaRole.config = 0

    # roleActions
    self.obj53.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('TrackMob', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('TanSkin', 20)
    lcobj2.append(cobj2)
    self.obj53.roleActions.setValue(lcobj2)

    # ID
    self.obj53.ID.setValue('Role000102')

    # name
    self.obj53.name.setValue('Hunter')

    self.obj53.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(194.0,465.6,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=Role(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # isMetaRole
    self.obj54.isMetaRole.setValue(('isMetaRole', 0))
    self.obj54.isMetaRole.config = 0

    # roleActions
    self.obj54.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('EnhancePotion', 20)
    lcobj2.append(cobj2)
    self.obj54.roleActions.setValue(lcobj2)

    # ID
    self.obj54.ID.setValue('Role000201')

    # name
    self.obj54.name.setValue('PotionsMaster')

    self.obj54.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(352.4,466.4,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=Role(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # isMetaRole
    self.obj55.isMetaRole.setValue(('isMetaRole', 0))
    self.obj55.isMetaRole.config = 0

    # roleActions
    self.obj55.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('EnhanceWeapon', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('EnhanceArmor', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('RepairItem', 20)
    lcobj2.append(cobj2)
    self.obj55.roleActions.setValue(lcobj2)

    # ID
    self.obj55.ID.setValue('Role000202')

    # name
    self.obj55.name.setValue('Smith')

    self.obj55.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(496.4,466.4,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=Role(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # isMetaRole
    self.obj56.isMetaRole.setValue(('isMetaRole', 0))
    self.obj56.isMetaRole.config = 0

    # roleActions
    self.obj56.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj56.roleActions.setValue(lcobj2)

    # ID
    self.obj56.ID.setValue('RoleID000601')

    # name
    self.obj56.name.setValue('QDEQuester')

    self.obj56.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(1065.2,464.8,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=Role(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # isMetaRole
    self.obj57.isMetaRole.setValue(('isMetaRole', 1))
    self.obj57.isMetaRole.config = 0

    # roleActions
    self.obj57.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj57.roleActions.setValue(lcobj2)

    # ID
    self.obj57.ID.setValue('Role00')

    # name
    self.obj57.name.setValue('Player')

    self.obj57.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(638.0,795.2,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=Role(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # isMetaRole
    self.obj58.isMetaRole.setValue(('isMetaRole', 0))
    self.obj58.isMetaRole.config = 0

    # roleActions
    self.obj58.roleActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj58.roleActions.setValue(lcobj2)

    # ID
    self.obj58.ID.setValue('Role01')

    # name
    self.obj58.name.setValue('NPC')

    self.obj58.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(79.2,813.8,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.88, 0.7399999999999999]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=OrganisationalKnArt(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # description
    self.obj59.description.setValue('Basic ontology containing concepts of the game')

    # ID
    self.obj59.ID.setValue('ONTO')

    # name
    self.obj59.name.setValue('GameOntology')

    # KnArtContent
    self.obj59.KnArtContent.setValue('#content of the artifact\n')
    self.obj59.KnArtContent.setHeight(15)

    self.obj59.graphClass_= graph_OrganisationalKnArt
    if self.genGraphics:
       new_obj = graph_OrganisationalKnArt(363.644444444,763.55,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrganisationalKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=OrganisationalKnArt(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # description
    self.obj60.description.setValue('Basic rules of communication in the system')

    # ID
    self.obj60.ID.setValue('COMM')

    # name
    self.obj60.name.setValue('RulesOfCommunication')

    # KnArtContent
    self.obj60.KnArtContent.setValue('#content of the artifact\n')
    self.obj60.KnArtContent.setHeight(15)

    self.obj60.graphClass_= graph_OrganisationalKnArt
    if self.genGraphics:
       new_obj = graph_OrganisationalKnArt(363.644444444,827.55,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrganisationalKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=IndividualKnArt(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # description
    self.obj61.description.setValue('Attributes of a character')

    # ID
    self.obj61.ID.setValue('CHRATTRS')

    # name
    self.obj61.name.setValue('CharacterAttributes')

    # KnArtContent
    self.obj61.KnArtContent.setValue('#content of the artifact\n')
    self.obj61.KnArtContent.setHeight(15)

    self.obj61.graphClass_= graph_IndividualKnArt
    if self.genGraphics:
       new_obj = graph_IndividualKnArt(1186.74722222,824.226388889,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IndividualKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=IndividualKnArt(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # description
    self.obj62.description.setValue('Inventory of a character')

    # ID
    self.obj62.ID.setValue('CHRINVTRY')

    # name
    self.obj62.name.setValue('Characterinventory')

    # KnArtContent
    self.obj62.KnArtContent.setValue('#content of the artifact\n')
    self.obj62.KnArtContent.setHeight(15)

    self.obj62.graphClass_= graph_IndividualKnArt
    if self.genGraphics:
       new_obj = graph_IndividualKnArt(1186.74722222,760.226388889,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IndividualKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=Objective(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # description
    self.obj63.description.setValue('Generic high-level goal')

    # Reward
    self.obj63.Reward.setValue('\n')
    self.obj63.Reward.setHeight(5)

    # ID
    self.obj63.ID.setValue('GTHR')

    # name
    self.obj63.name.setValue('GatherItem')

    # Measurement
    self.obj63.Measurement.setValue('\n')
    self.obj63.Measurement.setHeight(5)

    self.obj63.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(239.266666667,560.266666667,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=Objective(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # description
    self.obj64.description.setValue('Generic high-level goal')

    # Reward
    self.obj64.Reward.setValue('\n')
    self.obj64.Reward.setHeight(5)

    # ID
    self.obj64.ID.setValue('TSPT')

    # name
    self.obj64.name.setValue('TransportItem')

    # Measurement
    self.obj64.Measurement.setValue('\n')
    self.obj64.Measurement.setHeight(5)

    self.obj64.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(658.466666667,560.266666667,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=Objective(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # description
    self.obj65.description.setValue('Generic high-level goal')

    # Reward
    self.obj65.Reward.setValue('\n')
    self.obj65.Reward.setHeight(5)

    # ID
    self.obj65.ID.setValue('MAKE')

    # name
    self.obj65.name.setValue('MakeItem')

    # Measurement
    self.obj65.Measurement.setValue('\n')
    self.obj65.Measurement.setHeight(5)

    self.obj65.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(477.666666667,561.066666667,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=Objective(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # description
    self.obj66.description.setValue('Generic high-level goal')

    # Reward
    self.obj66.Reward.setValue('\n')
    self.obj66.Reward.setHeight(5)

    # ID
    self.obj66.ID.setValue('FIND')

    # name
    self.obj66.name.setValue('Find')

    # Measurement
    self.obj66.Measurement.setValue('\n')
    self.obj66.Measurement.setHeight(5)

    self.obj66.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(875.266666667,553.866666667,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=Objective(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # description
    self.obj67.description.setValue('')
    self.obj67.description.setNone()

    # Reward
    self.obj67.Reward.setValue('\n')
    self.obj67.Reward.setHeight(5)

    # ID
    self.obj67.ID.setValue('QALL')

    # name
    self.obj67.name.setValue('SolveAllQuests')

    # Measurement
    self.obj67.Measurement.setValue('\n')
    self.obj67.Measurement.setHeight(5)

    self.obj67.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1186.46666667,335.466666667,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=Objective(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # description
    self.obj68.description.setValue('Specific Quest')

    # Reward
    self.obj68.Reward.setValue('\n')
    self.obj68.Reward.setHeight(5)

    # ID
    self.obj68.ID.setValue('QDE')

    # name
    self.obj68.name.setValue('QuestForTheDragonEgg')

    # Measurement
    self.obj68.Measurement.setValue('\n')
    self.obj68.Measurement.setHeight(5)

    self.obj68.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(667.266666667,9.86666666667,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=Objective(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # description
    self.obj69.description.setValue('Talk to the Egg Hermit NPC and let him use Hatching Potion on the Dragon Egg')

    # Reward
    self.obj69.Reward.setValue('\n')
    self.obj69.Reward.setHeight(5)

    # ID
    self.obj69.ID.setValue('QDE01')

    # name
    self.obj69.name.setValue('HatchDragonEgg')

    # Measurement
    self.obj69.Measurement.setValue('\n')
    self.obj69.Measurement.setHeight(5)

    self.obj69.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(507.266666667,73.8666666667,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=Objective(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # description
    self.obj70.description.setValue('Upon hatching a dragon talk to ArchWizard NPC')

    # Reward
    self.obj70.Reward.setValue('\n')
    self.obj70.Reward.setHeight(5)

    # ID
    self.obj70.ID.setValue('QDE02')

    # name
    self.obj70.name.setValue('LearnSpell')

    # Measurement
    self.obj70.Measurement.setValue('\n')
    self.obj70.Measurement.setHeight(5)

    self.obj70.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(779.266666667,73.8666666667,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=Objective(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # description
    self.obj71.description.setValue('')
    self.obj71.description.setNone()

    # Reward
    self.obj71.Reward.setValue('\n')
    self.obj71.Reward.setHeight(5)

    # ID
    self.obj71.ID.setValue('QDE0101')

    # name
    self.obj71.name.setValue('BrewHatchingPotion')

    # Measurement
    self.obj71.Measurement.setValue('\n')
    self.obj71.Measurement.setHeight(5)

    self.obj71.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(315.266666667,185.866666667,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=Objective(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # description
    self.obj72.description.setValue('Transport the Dragon Egg item to the Egg Hermit NPC without losing it')

    # Reward
    self.obj72.Reward.setValue('\n')
    self.obj72.Reward.setHeight(5)

    # ID
    self.obj72.ID.setValue('QDE0102')

    # name
    self.obj72.name.setValue('TransportDragonEgg')

    # Measurement
    self.obj72.Measurement.setValue('\n')
    self.obj72.Measurement.setHeight(5)

    self.obj72.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(523.266666667,185.866666667,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=Objective(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # description
    self.obj73.description.setValue('Find the Egg Hermit NPC')

    # Reward
    self.obj73.Reward.setValue('\n')
    self.obj73.Reward.setHeight(5)

    # ID
    self.obj73.ID.setValue('QDE0103')

    # name
    self.obj73.name.setValue('FindEggHermit')

    # Measurement
    self.obj73.Measurement.setValue('\n')
    self.obj73.Measurement.setHeight(5)

    self.obj73.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(731.266666667,185.866666667,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=Objective(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # description
    self.obj74.description.setValue('')
    self.obj74.description.setNone()

    # Reward
    self.obj74.Reward.setValue('\n')
    self.obj74.Reward.setHeight(5)

    # ID
    self.obj74.ID.setValue('QDE010201')

    # name
    self.obj74.name.setValue('FindDragonEgg')

    # Measurement
    self.obj74.Measurement.setValue('\n')
    self.obj74.Measurement.setHeight(5)

    self.obj74.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(715.266666667,297.866666667,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=Objective(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # description
    self.obj75.description.setValue('')
    self.obj75.description.setNone()

    # Reward
    self.obj75.Reward.setValue('\n')
    self.obj75.Reward.setHeight(5)

    # ID
    self.obj75.ID.setValue('QDE010101')

    # name
    self.obj75.name.setValue('GatherPotionIngredients')

    # Measurement
    self.obj75.Measurement.setValue('\n')
    self.obj75.Measurement.setHeight(5)

    self.obj75.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(235.266666667,297.866666667,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=Process(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # Activities
    self.obj76.Activities.setValue('\n')
    self.obj76.Activities.setHeight(10)

    # ID
    self.obj76.ID.setValue('PRCS0')

    # Name
    self.obj76.Name.setValue('')
    self.obj76.Name.setNone()

    self.obj76.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(155.188888889,396.822222222,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=Process(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # Activities
    self.obj77.Activities.setValue('\n')
    self.obj77.Activities.setHeight(10)

    # ID
    self.obj77.ID.setValue('PRCS1')

    # Name
    self.obj77.Name.setValue('')
    self.obj77.Name.setNone()

    self.obj77.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(443.188888889,396.822222222,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj78=Process(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # Activities
    self.obj78.Activities.setValue('\n')
    self.obj78.Activities.setHeight(10)

    # ID
    self.obj78.ID.setValue('PRCS2')

    # Name
    self.obj78.Name.setValue('')
    self.obj78.Name.setNone()

    self.obj78.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(971.188888889,396.822222222,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=Process(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # Activities
    self.obj79.Activities.setValue('\n')
    self.obj79.Activities.setHeight(10)

    # ID
    self.obj79.ID.setValue('PRCS3')

    # Name
    self.obj79.Name.setValue('')
    self.obj79.Name.setNone()

    self.obj79.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(651.188888889,396.822222222,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj80=isPartOfOrgUnit(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(True)

    self.obj80.graphClass_= graph_isPartOfOrgUnit
    if self.genGraphics:
       new_obj = graph_isPartOfOrgUnit(1123.6,759.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfOrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=canHaveRole(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(True)

    self.obj81.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(838.4,820.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=canHaveRole(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(True)

    self.obj82.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(180.4,837.8,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=canAccessKnArt(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    self.obj83.graphClass_= graph_canAccessKnArt
    if self.genGraphics:
       new_obj = graph_canAccessKnArt(1141.4,821.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canAccessKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj84=canAccessKnArt(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    self.obj84.graphClass_= graph_canAccessKnArt
    if self.genGraphics:
       new_obj = graph_canAccessKnArt(520.0,820.0,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canAccessKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj85=isPartOfObjective(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(True)

    self.obj85.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(694.4,96.8,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj86=isPartOfObjective(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(True)

    self.obj86.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(1212.0,40.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=isPartOfObjective(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(True)

    self.obj87.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(516.8,162.4,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj88=isPartOfObjective(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(True)

    self.obj88.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(752.8,489.6,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=isPartOfObjective(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(True)

    self.obj89.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(899.2,488.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=isPartOfObjective(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(True)

    self.obj90.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(669.6,275.2,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=isPartOfObjective(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(True)

    self.obj91.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(274.4,268.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj92=isPartOfObjective(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(True)

    self.obj92.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(320.0,492.0,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj93=isPartOfObjective(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(True)

    self.obj93.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(656.0,492.0,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj94=hasObjective(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(False)

    self.obj94.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(244.4,625.6,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    self.obj95=hasObjective(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(False)

    self.obj95.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(665.6,626.4,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj96=hasObjective(self)
    self.obj96.isGraphObjectVisual = True

    if(hasattr(self.obj96, '_setHierarchicalLink')):
      self.obj96._setHierarchicalLink(False)

    self.obj96.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(481.6,632.0,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj96.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj96)
    self.globalAndLocalPostcondition(self.obj96, rootNode)
    self.obj96.postAction( rootNode.CREATE )

    self.obj97=hasObjective(self)
    self.obj97.isGraphObjectVisual = True

    if(hasattr(self.obj97, '_setHierarchicalLink')):
      self.obj97._setHierarchicalLink(False)

    self.obj97.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(1075.2,658.4,self.obj97)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj97.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj97)
    self.globalAndLocalPostcondition(self.obj97, rootNode)
    self.obj97.postAction( rootNode.CREATE )

    self.obj98=hasObjective(self)
    self.obj98.isGraphObjectVisual = True

    if(hasattr(self.obj98, '_setHierarchicalLink')):
      self.obj98._setHierarchicalLink(False)

    self.obj98.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(179.2,412.8,self.obj98)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj98.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj98)
    self.globalAndLocalPostcondition(self.obj98, rootNode)
    self.obj98.postAction( rootNode.CREATE )

    self.obj99=hasObjective(self)
    self.obj99.isGraphObjectVisual = True

    if(hasattr(self.obj99, '_setHierarchicalLink')):
      self.obj99._setHierarchicalLink(False)

    self.obj99.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(467.2,412.8,self.obj99)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj99.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj99)
    self.globalAndLocalPostcondition(self.obj99, rootNode)
    self.obj99.postAction( rootNode.CREATE )

    self.obj100=hasObjective(self)
    self.obj100.isGraphObjectVisual = True

    if(hasattr(self.obj100, '_setHierarchicalLink')):
      self.obj100._setHierarchicalLink(False)

    self.obj100.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(995.2,412.8,self.obj100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj100.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj100)
    self.globalAndLocalPostcondition(self.obj100, rootNode)
    self.obj100.postAction( rootNode.CREATE )

    self.obj101=hasObjective(self)
    self.obj101.isGraphObjectVisual = True

    if(hasattr(self.obj101, '_setHierarchicalLink')):
      self.obj101._setHierarchicalLink(False)

    self.obj101.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(995.2,412.8,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj101)
    self.globalAndLocalPostcondition(self.obj101, rootNode)
    self.obj101.postAction( rootNode.CREATE )

    self.obj102=hasObjective(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    self.obj102.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(675.2,412.8,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj103=hasObjective(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(False)

    self.obj103.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(952.0,659.2,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj104=canStartProcess(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    self.obj104.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(92.0,489.6,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=canStartProcess(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    self.obj105.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(362.4,490.4,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=canStartProcess(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    self.obj106.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(623.2,659.2,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj107=canStartProcess(self)
    self.obj107.isGraphObjectVisual = True

    if(hasattr(self.obj107, '_setHierarchicalLink')):
      self.obj107._setHierarchicalLink(False)

    self.obj107.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(952.0,659.2,self.obj107)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj107.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj107)
    self.globalAndLocalPostcondition(self.obj107, rootNode)
    self.obj107.postAction( rootNode.CREATE )

    self.obj108=isPartOfRole(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(True)

    self.obj108.graphClass_= graph_isPartOfRole
    if self.genGraphics:
       new_obj = graph_isPartOfRole(441.6,557.6,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj109=isPartOfRole(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(True)

    self.obj109.graphClass_= graph_isPartOfRole
    if self.genGraphics:
       new_obj = graph_isPartOfRole(1076.0,588.8,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj110=isPartOfRole(self)
    self.obj110.isGraphObjectVisual = True

    if(hasattr(self.obj110, '_setHierarchicalLink')):
      self.obj110._setHierarchicalLink(True)

    self.obj110.graphClass_= graph_isPartOfRole
    if self.genGraphics:
       new_obj = graph_isPartOfRole(204.0,573.6,self.obj110)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj110.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj110)
    self.globalAndLocalPostcondition(self.obj110, rootNode)
    self.obj110.postAction( rootNode.CREATE )

    self.obj111=isPartOfRole(self)
    self.obj111.isGraphObjectVisual = True

    if(hasattr(self.obj111, '_setHierarchicalLink')):
      self.obj111._setHierarchicalLink(True)

    self.obj111.graphClass_= graph_isPartOfRole
    if self.genGraphics:
       new_obj = graph_isPartOfRole(622.4,752.8,self.obj111)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 0.8
       new_obj.layConstraints['scale'] = [0.7999999999999999, 0.7999999999999999]
    else: new_obj = None
    self.obj111.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj111)
    self.globalAndLocalPostcondition(self.obj111, rootNode)
    self.obj111.postAction( rootNode.CREATE )

    # Connections for obj43 (graphObject_: Obj0) named orgUnitName
    self.drawConnections(
 )
    # Connections for obj44 (graphObject_: Obj1) named orgUnitName
    self.drawConnections(
(self.obj44,self.obj80,[1008.0, 820.5999999999999, 1123.6, 759.0],"true", 2),
(self.obj44,self.obj81,[1008.0, 820.5999999999999, 838.4, 820.0], 0, 2),
(self.obj44,self.obj83,[1008.0, 820.5999999999999, 1141.4, 821.0], 0, 2) )
    # Connections for obj45 (graphObject_: Obj2) named orgUnitName
    self.drawConnections(
(self.obj45,self.obj82,[244.8, 839.4000000000001, 180.4, 837.8], 0, 2) )
    # Connections for obj46 (graphObject_: Obj3) named Gatherer
    self.drawConnections(
(self.obj46,self.obj94,[205.0, 657.4000000000001, 244.4, 625.6], 0, 2),
(self.obj46,self.obj111,[205.0, 657.4000000000001, 191.0, 750.0, 622.4, 752.8],"true", 3) )
    # Connections for obj47 (graphObject_: Obj4) named Transporter
    self.drawConnections(
(self.obj47,self.obj95,[624.4000000000001, 657.4000000000001, 665.6, 626.4],"true", 2),
(self.obj47,self.obj106,[624.4000000000001, 657.4000000000001, 623.2, 659.2],"true", 2),
(self.obj47,self.obj111,[624.4000000000001, 657.4000000000001, 622.4, 752.8], 0, 2) )
    # Connections for obj48 (graphObject_: Obj5) named Maker
    self.drawConnections(
(self.obj48,self.obj96,[443.79999999999995, 658.0, 481.6, 632.0],"true", 2),
(self.obj48,self.obj111,[443.79999999999995, 658.0, 432.0, 728.0, 622.4, 752.8],"true", 3) )
    # Connections for obj49 (graphObject_: Obj6) named Scout
    self.drawConnections(
(self.obj49,self.obj111,[951.0, 662.2, 991.4, 715.8, 622.4, 752.8],"true", 3),
(self.obj49,self.obj103,[951.0, 662.2, 952.0, 659.2], 0, 2),
(self.obj49,self.obj107,[951.0, 662.2, 952.0, 659.2], 0, 2) )
    # Connections for obj50 (graphObject_: Obj7) named Warrior
    self.drawConnections(
(self.obj50,self.obj111,[781.0, 657.4000000000001, 622.4, 752.8], 0, 2) )
    # Connections for obj51 (graphObject_: Obj8) named Quester
    self.drawConnections(
(self.obj51,self.obj97,[1076.4, 656.8, 1075.2, 658.4],"true", 2),
(self.obj51,self.obj111,[1076.4, 656.8, 1117.4, 768.8, 622.4, 752.8],"true", 3) )
    # Connections for obj52 (graphObject_: Obj9) named Herbalist
    self.drawConnections(
(self.obj52,self.obj110,[93.0, 488.20000000000005, 98.0, 562.6, 204.0, 573.6],"true", 3),
(self.obj52,self.obj104,[93.0, 488.20000000000005, 92.0, 489.6], 0, 2) )
    # Connections for obj53 (graphObject_: Obj10) named Hunter
    self.drawConnections(
(self.obj53,self.obj110,[205.0, 488.20000000000005, 204.0, 573.6], 0, 2) )
    # Connections for obj54 (graphObject_: Obj11) named PotionsMaster
    self.drawConnections(
(self.obj54,self.obj108,[363.79999999999995, 488.79999999999995, 365.59999999999997, 542.6, 441.6, 557.6],"true", 3),
(self.obj54,self.obj105,[363.79999999999995, 488.79999999999995, 362.4, 490.4], 0, 2) )
    # Connections for obj55 (graphObject_: Obj12) named Smith
    self.drawConnections(
(self.obj55,self.obj108,[507.79999999999995, 488.79999999999995, 506.5999999999999, 548.6, 441.6, 557.6],"true", 3) )
    # Connections for obj56 (graphObject_: Obj13) named QDEQuester
    self.drawConnections(
(self.obj56,self.obj109,[1076.4, 487.6, 1076.0, 588.8],"true", 2) )
    # Connections for obj57 (graphObject_: Obj14) named Player
    self.drawConnections(
(self.obj57,self.obj84,[649.0, 817.4000000000001, 520.0, 820.0], 0, 2) )
    # Connections for obj58 (graphObject_: Obj15) named NPC
    self.drawConnections(
 )
    # Connections for obj59 (graphObject_: Obj16) named GameOntology
    self.drawConnections(
 )
    # Connections for obj60 (graphObject_: Obj17) named RulesOfCommunication
    self.drawConnections(
 )
    # Connections for obj61 (graphObject_: Obj18) named CharacterAttributes
    self.drawConnections(
 )
    # Connections for obj62 (graphObject_: Obj19) named Characterinventory
    self.drawConnections(
 )
    # Connections for obj63 (graphObject_: Obj20) named GatherItem
    self.drawConnections(
 )
    # Connections for obj64 (graphObject_: Obj21) named TransportItem
    self.drawConnections(
 )
    # Connections for obj65 (graphObject_: Obj22) named MakeItem
    self.drawConnections(
 )
    # Connections for obj66 (graphObject_: Obj23) named Find
    self.drawConnections(
 )
    # Connections for obj67 (graphObject_: Obj24) named SolveAllQuests
    self.drawConnections(
 )
    # Connections for obj68 (graphObject_: Obj25) named QuestForTheDragonEgg
    self.drawConnections(
(self.obj68,self.obj86,[687.733333334, 35.93333333334, 1212.0, 40.0], 0, 2) )
    # Connections for obj69 (graphObject_: Obj26) named HatchDragonEgg
    self.drawConnections(
(self.obj69,self.obj85,[527.733333334, 99.9333333334, 485.4, 23.799999999999997, 694.4, 96.8],"true", 3) )
    # Connections for obj70 (graphObject_: Obj27) named LearnSpell
    self.drawConnections(
(self.obj70,self.obj85,[799.733333334, 99.9333333334, 694.4, 96.8],"true", 2) )
    # Connections for obj71 (graphObject_: Obj28) named BrewHatchingPotion
    self.drawConnections(
(self.obj71,self.obj87,[335.73333333399995, 211.933333334, 516.8, 162.4], 0, 2),
(self.obj71,self.obj93,[335.73333333399995, 211.933333334, 591.0, 247.0, 656.0, 492.0],"true", 3) )
    # Connections for obj72 (graphObject_: Obj29) named TransportDragonEgg
    self.drawConnections(
(self.obj72,self.obj87,[543.733333334, 211.933333334, 516.8, 162.4], 0, 2),
(self.obj72,self.obj88,[543.733333334, 211.933333334, 724.8, 329.6, 752.8, 489.6],"true", 3) )
    # Connections for obj73 (graphObject_: Obj30) named FindEggHermit
    self.drawConnections(
(self.obj73,self.obj87,[751.733333334, 211.933333334, 516.8, 162.4], 0, 2),
(self.obj73,self.obj89,[751.733333334, 211.933333334, 940.1999999999998, 354.0, 899.2, 488.0],"true", 3) )
    # Connections for obj74 (graphObject_: Obj31) named FindDragonEgg
    self.drawConnections(
(self.obj74,self.obj90,[735.733333334, 323.933333334, 669.6, 275.2], 0, 2),
(self.obj74,self.obj89,[735.733333334, 323.933333334, 717.1999999999999, 504.0, 899.2, 488.0],"true", 3) )
    # Connections for obj75 (graphObject_: Obj32) named GatherPotionIngredients
    self.drawConnections(
(self.obj75,self.obj91,[255.73333333399998, 323.933333334, 274.4, 268.0], 0, 2),
(self.obj75,self.obj92,[255.73333333399998, 323.933333334, 320.0, 492.0], 0, 2) )
    # Connections for obj76 (graphObject_: Obj33) of type Process
    self.drawConnections(
(self.obj76,self.obj98,[179.57777777799998, 412.244444444, 179.2, 412.8], 0, 2) )
    # Connections for obj77 (graphObject_: Obj34) of type Process
    self.drawConnections(
(self.obj77,self.obj99,[467.577777778, 412.244444444, 467.2, 412.8],"true", 2) )
    # Connections for obj78 (graphObject_: Obj35) of type Process
    self.drawConnections(
(self.obj78,self.obj100,[995.5777777780002, 412.244444444, 995.2, 412.8], 0, 2),
(self.obj78,self.obj101,[995.5777777780002, 412.244444444, 995.2, 412.8],"true", 2) )
    # Connections for obj79 (graphObject_: Obj36) of type Process
    self.drawConnections(
(self.obj79,self.obj102,[675.5777777780002, 412.244444444, 675.2, 412.8], 0, 2) )
    # Connections for obj80 (graphObject_: Obj37) of type isPartOfOrgUnit
    self.drawConnections(
(self.obj80,self.obj43,[1123.6, 759.0, 1214.0, 728.0],"true", 2) )
    # Connections for obj81 (graphObject_: Obj39) of type canHaveRole
    self.drawConnections(
(self.obj81,self.obj57,[838.4, 820.0, 649.0, 817.4000000000001], 0, 2) )
    # Connections for obj82 (graphObject_: Obj41) of type canHaveRole
    self.drawConnections(
(self.obj82,self.obj58,[180.4, 837.8, 90.06497942401201, 836.2553721630352], 0, 2) )
    # Connections for obj83 (graphObject_: Obj43) of type canAccessKnArt
    self.drawConnections(
(self.obj83,self.obj61,[1141.4, 821.0, 1203.5944444399997, 843.402777778], 0, 2),
(self.obj83,self.obj62,[1141.4, 821.0, 1203.5944444399997, 779.402777778], 0, 2) )
    # Connections for obj84 (graphObject_: Obj45) of type canAccessKnArt
    self.drawConnections(
(self.obj84,self.obj59,[520.0, 820.0, 381.888888888, 782.0999999999999], 0, 2),
(self.obj84,self.obj60,[520.0, 820.0, 381.888888888, 846.0999999999999], 0, 2) )
    # Connections for obj85 (graphObject_: Obj47) of type isPartOfObjective
    self.drawConnections(
(self.obj85,self.obj68,[694.4, 96.8, 687.733333334, 35.93333333334],"true", 2) )
    # Connections for obj86 (graphObject_: Obj49) of type isPartOfObjective
    self.drawConnections(
(self.obj86,self.obj67,[1212.0, 40.0, 1207.13333334, 362.13333333400004], 0, 2) )
    # Connections for obj87 (graphObject_: Obj51) of type isPartOfObjective
    self.drawConnections(
(self.obj87,self.obj69,[516.8, 162.4, 527.733333334, 99.9333333334], 0, 2) )
    # Connections for obj88 (graphObject_: Obj53) of type isPartOfObjective
    self.drawConnections(
(self.obj88,self.obj64,[752.8, 489.6, 679.1333333340001, 586.733333334],"true", 2) )
    # Connections for obj89 (graphObject_: Obj55) of type isPartOfObjective
    self.drawConnections(
(self.obj89,self.obj66,[899.2, 488.0, 895.733333334, 579.933333334],"true", 2) )
    # Connections for obj90 (graphObject_: Obj57) of type isPartOfObjective
    self.drawConnections(
(self.obj90,self.obj72,[669.6, 275.2, 543.733333334, 211.933333334], 0, 2) )
    # Connections for obj91 (graphObject_: Obj59) of type isPartOfObjective
    self.drawConnections(
(self.obj91,self.obj71,[274.4, 268.0, 335.73333333399995, 211.933333334], 0, 2) )
    # Connections for obj92 (graphObject_: Obj61) of type isPartOfObjective
    self.drawConnections(
(self.obj92,self.obj63,[320.0, 492.0, 259.733333334, 586.733333334], 0, 2) )
    # Connections for obj93 (graphObject_: Obj63) of type isPartOfObjective
    self.drawConnections(
(self.obj93,self.obj65,[656.0, 492.0, 634.0, 581.0, 497.533333334, 587.3333333340001],"true", 3) )
    # Connections for obj94 (graphObject_: Obj65) of type hasObjective
    self.drawConnections(
(self.obj94,self.obj63,[244.4, 625.6, 259.733333334, 586.733333334], 0, 2) )
    # Connections for obj95 (graphObject_: Obj66) of type hasObjective
    self.drawConnections(
(self.obj95,self.obj64,[665.6, 626.4, 679.1333333340001, 586.733333334],"true", 2) )
    # Connections for obj96 (graphObject_: Obj67) of type hasObjective
    self.drawConnections(
(self.obj96,self.obj65,[481.6, 632.0, 497.533333334, 587.3333333340001],"true", 2) )
    # Connections for obj97 (graphObject_: Obj68) of type hasObjective
    self.drawConnections(
(self.obj97,self.obj67,[1075.2, 658.4, 1246.2, 558.4, 1207.13333334, 362.13333333400004],"true", 3) )
    # Connections for obj98 (graphObject_: Obj69) of type hasObjective
    self.drawConnections(
(self.obj98,self.obj75,[179.2, 412.8, 255.73333333399998, 323.933333334], 0, 2) )
    # Connections for obj99 (graphObject_: Obj70) of type hasObjective
    self.drawConnections(
(self.obj99,self.obj71,[467.2, 412.8, 436.2, 280.8, 335.73333333399995, 211.933333334],"true", 3) )
    # Connections for obj100 (graphObject_: Obj71) of type hasObjective
    self.drawConnections(
(self.obj100,self.obj73,[995.2, 412.8, 751.733333334, 211.933333334], 0, 2) )
    # Connections for obj101 (graphObject_: Obj72) of type hasObjective
    self.drawConnections(
(self.obj101,self.obj74,[995.2, 412.8, 802.2, 424.8, 735.733333334, 323.933333334],"true", 3) )
    # Connections for obj102 (graphObject_: Obj73) of type hasObjective
    self.drawConnections(
(self.obj102,self.obj72,[675.2, 412.8, 543.733333334, 211.933333334], 0, 2) )
    # Connections for obj103 (graphObject_: Obj74) of type hasObjective
    self.drawConnections(
(self.obj103,self.obj66,[952.0, 659.2, 895.733333334, 579.933333334], 0, 2) )
    # Connections for obj104 (graphObject_: Obj75) of type canStartProcess
    self.drawConnections(
(self.obj104,self.obj76,[92.0, 489.6, 179.57777777799998, 412.244444444], 0, 2) )
    # Connections for obj105 (graphObject_: Obj76) of type canStartProcess
    self.drawConnections(
(self.obj105,self.obj77,[362.4, 490.4, 467.577777778, 412.244444444], 0, 2) )
    # Connections for obj106 (graphObject_: Obj77) of type canStartProcess
    self.drawConnections(
(self.obj106,self.obj79,[623.2, 659.2, 729.1999999999999, 450.19999999999993, 675.5777777780002, 412.244444444],"true", 3) )
    # Connections for obj107 (graphObject_: Obj78) of type canStartProcess
    self.drawConnections(
(self.obj107,self.obj78,[952.0, 659.2, 995.5777777780002, 412.244444444], 0, 2) )
    # Connections for obj108 (graphObject_: Obj79) of type isPartOfRole
    self.drawConnections(
(self.obj108,self.obj48,[441.6, 557.6, 443.79999999999995, 658.0],"true", 2) )
    # Connections for obj109 (graphObject_: Obj81) of type isPartOfRole
    self.drawConnections(
(self.obj109,self.obj51,[1076.0, 588.8, 1076.4, 656.8],"true", 2) )
    # Connections for obj110 (graphObject_: Obj83) of type isPartOfRole
    self.drawConnections(
(self.obj110,self.obj46,[204.0, 573.6, 205.0, 657.4000000000001],"true", 2) )
    # Connections for obj111 (graphObject_: Obj85) of type isPartOfRole
    self.drawConnections(
(self.obj111,self.obj57,[622.4, 752.8, 649.0, 817.4000000000001],"true", 2) )

newfunction = TMWQDE_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
