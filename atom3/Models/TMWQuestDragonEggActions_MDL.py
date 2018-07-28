"""
__TMWQuestDragonEggActions_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Wed May  2 00:27:03 2018
______________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from Action import *
from IndividualKnArt import *
from Objective import *
from isPartOfOrgUnit import *
from canHaveRole import *
from hasActions import *
from canAccessKnArt import *
from isPartOfObjective import *
from hasObjective import *
from precedentTo import *
from graph_canHaveRole import *
from graph_canAccessKnArt import *
from graph_isPartOfOrgUnit import *
from graph_Action import *
from graph_precedentTo import *
from graph_Objective import *
from graph_hasObjective import *
from graph_Role import *
from graph_OrgUnit import *
from graph_IndividualKnArt import *
from graph_isPartOfObjective import *
from graph_hasActions import *
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

def TMWQuestDragonEggActions_MDL(self, rootNode, LSMASOMMRootNode=None):

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
        LSMASOMMRootNode.name.setValue('TMW')

        # title
        LSMASOMMRootNode.title.setValue('QuestDragonEgg')
    # --- ASG attributes over ---


    self.obj118=OrgUnit(self)
    self.obj118.isGraphObjectVisual = True

    if(hasattr(self.obj118, '_setHierarchicalLink')):
      self.obj118._setHierarchicalLink(False)

    # Individual
    self.obj118.Individual.setValue(('1', 0))
    self.obj118.Individual.config = 0

    # hasActions
    self.obj118.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj118.hasActions.setValue(lcobj2)

    # ID
    self.obj118.ID.setValue('OU|0')

    # name
    self.obj118.name.setValue('Avatar')

    # UnitSize
    self.obj118.UnitSize.setValue('Individual')

    self.obj118.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(530.0,890.0,self.obj118)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj118.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj118)
    self.globalAndLocalPostcondition(self.obj118, rootNode)
    self.obj118.postAction( rootNode.CREATE )

    self.obj119=OrgUnit(self)
    self.obj119.isGraphObjectVisual = True

    if(hasattr(self.obj119, '_setHierarchicalLink')):
      self.obj119._setHierarchicalLink(False)

    # Individual
    self.obj119.Individual.setValue(('1', 0))
    self.obj119.Individual.config = 0

    # hasActions
    self.obj119.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj119.hasActions.setValue(lcobj2)

    # ID
    self.obj119.ID.setValue('OU|1')

    # name
    self.obj119.name.setValue('Party')

    # UnitSize
    self.obj119.UnitSize.setValue('Group')

    self.obj119.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(370.0,890.0,self.obj119)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj119.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj119)
    self.globalAndLocalPostcondition(self.obj119, rootNode)
    self.obj119.postAction( rootNode.CREATE )

    self.obj104=Role(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # isMetaRole
    self.obj104.isMetaRole.setValue((None, 0))
    self.obj104.isMetaRole.config = 0

    # hasActions
    self.obj104.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('move', 20)
    lcobj2.append(cobj2)
    self.obj104.hasActions.setValue(lcobj2)

    # ID
    self.obj104.ID.setValue('R|0')

    # name
    self.obj104.name.setValue('Scout')

    self.obj104.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(190.0,730.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj105=Role(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # isMetaRole
    self.obj105.isMetaRole.setValue((None, 0))
    self.obj105.isMetaRole.config = 0

    # hasActions
    self.obj105.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('harvestItem', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('craftItem', 20)
    lcobj2.append(cobj2)
    self.obj105.hasActions.setValue(lcobj2)

    # ID
    self.obj105.ID.setValue('R|1')

    # name
    self.obj105.name.setValue('Maker')

    self.obj105.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(340.0,730.0,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj106=Role(self)
    self.obj106.isGraphObjectVisual = True

    if(hasattr(self.obj106, '_setHierarchicalLink')):
      self.obj106._setHierarchicalLink(False)

    # isMetaRole
    self.obj106.isMetaRole.setValue((None, 0))
    self.obj106.isMetaRole.config = 0

    # hasActions
    self.obj106.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('learnSpell', 20)
    lcobj2.append(cobj2)
    self.obj106.hasActions.setValue(lcobj2)

    # ID
    self.obj106.ID.setValue('R|2')

    # name
    self.obj106.name.setValue('Wizard')

    self.obj106.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(790.0,730.0,self.obj106)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj106.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj106)
    self.globalAndLocalPostcondition(self.obj106, rootNode)
    self.obj106.postAction( rootNode.CREATE )

    self.obj125=Role(self)
    self.obj125.isGraphObjectVisual = True

    if(hasattr(self.obj125, '_setHierarchicalLink')):
      self.obj125._setHierarchicalLink(False)

    # isMetaRole
    self.obj125.isMetaRole.setValue((None, 0))
    self.obj125.isMetaRole.config = 0

    # hasActions
    self.obj125.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj125.hasActions.setValue(lcobj2)

    # ID
    self.obj125.ID.setValue('R|3')

    # name
    self.obj125.name.setValue('PartyFounder')

    self.obj125.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(790.0,860.0,self.obj125)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj125.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj125)
    self.globalAndLocalPostcondition(self.obj125, rootNode)
    self.obj125.postAction( rootNode.CREATE )

    self.obj126=Role(self)
    self.obj126.isGraphObjectVisual = True

    if(hasattr(self.obj126, '_setHierarchicalLink')):
      self.obj126._setHierarchicalLink(False)

    # isMetaRole
    self.obj126.isMetaRole.setValue((None, 0))
    self.obj126.isMetaRole.config = 0

    # hasActions
    self.obj126.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj126.hasActions.setValue(lcobj2)

    # ID
    self.obj126.ID.setValue('R|4')

    # name
    self.obj126.name.setValue('PartyMember')

    self.obj126.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(790.0,940.0,self.obj126)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj126.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj126)
    self.globalAndLocalPostcondition(self.obj126, rootNode)
    self.obj126.postAction( rootNode.CREATE )

    self.obj86=Action(self)
    self.obj86.isGraphObjectVisual = True

    if(hasattr(self.obj86, '_setHierarchicalLink')):
      self.obj86._setHierarchicalLink(False)

    # ID
    self.obj86.ID.setValue('A|0')

    # name
    self.obj86.name.setValue('move')

    # ActionCode
    self.obj86.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj86.ActionCode.setHeight(15)

    self.obj86.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(180.0,590.0,self.obj86)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj86.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj86)
    self.globalAndLocalPostcondition(self.obj86, rootNode)
    self.obj86.postAction( rootNode.CREATE )

    self.obj87=Action(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(False)

    # ID
    self.obj87.ID.setValue('A|1')

    # name
    self.obj87.name.setValue('harvestItem')

    # ActionCode
    self.obj87.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj87.ActionCode.setHeight(15)

    self.obj87.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(280.0,590.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj87.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87, rootNode)
    self.obj87.postAction( rootNode.CREATE )

    self.obj88=Action(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    # ID
    self.obj88.ID.setValue('A|2')

    # name
    self.obj88.name.setValue('craftItem')

    # ActionCode
    self.obj88.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj88.ActionCode.setHeight(15)

    self.obj88.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(380.0,590.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=Action(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    # ID
    self.obj89.ID.setValue('A|3')

    # name
    self.obj89.name.setValue('learnSpell')

    # ActionCode
    self.obj89.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj89.ActionCode.setHeight(15)

    self.obj89.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(780.0,590.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.01
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj133=IndividualKnArt(self)
    self.obj133.isGraphObjectVisual = True

    if(hasattr(self.obj133, '_setHierarchicalLink')):
      self.obj133._setHierarchicalLink(False)

    # description
    self.obj133.description.setValue('AvatarInventory')

    # ID
    self.obj133.ID.setValue('AvatarInventory')

    # name
    self.obj133.name.setValue('AvatarInventory')

    # KnArtContent
    self.obj133.KnArtContent.setValue('#content of the artifact\n')
    self.obj133.KnArtContent.setHeight(15)

    self.obj133.graphClass_= graph_IndividualKnArt
    if self.genGraphics:
       new_obj = graph_IndividualKnArt(480.0,1040.0,self.obj133)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IndividualKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj133.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj133)
    self.globalAndLocalPostcondition(self.obj133, rootNode)
    self.obj133.postAction( rootNode.CREATE )

    self.obj134=IndividualKnArt(self)
    self.obj134.isGraphObjectVisual = True

    if(hasattr(self.obj134, '_setHierarchicalLink')):
      self.obj134._setHierarchicalLink(False)

    # description
    self.obj134.description.setValue('KnArtDesc')

    # ID
    self.obj134.ID.setValue('AvatarAttributes')

    # name
    self.obj134.name.setValue('AvatarAttributes')

    # KnArtContent
    self.obj134.KnArtContent.setValue('#content of the artifact\n')
    self.obj134.KnArtContent.setHeight(15)

    self.obj134.graphClass_= graph_IndividualKnArt
    if self.genGraphics:
       new_obj = graph_IndividualKnArt(600.0,1040.0,self.obj134)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IndividualKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj134.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj134)
    self.globalAndLocalPostcondition(self.obj134, rootNode)
    self.obj134.postAction( rootNode.CREATE )

    self.obj44=Objective(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # description
    self.obj44.description.setValue('\n')
    self.obj44.description.setHeight(4)

    # ofActions
    self.obj44.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj44.ofActions.setValue(lcobj2)

    # Measurement
    self.obj44.Measurement.setValue('\n')
    self.obj44.Measurement.setHeight(4)

    # Reward
    self.obj44.Reward.setValue('\n')
    self.obj44.Reward.setHeight(4)

    # ID
    self.obj44.ID.setValue('O|0')

    # name
    self.obj44.name.setValue('FinishQuestForTheDragonEgg')

    self.obj44.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(544.0,31.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.1
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    self.obj45=Objective(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # description
    self.obj45.description.setValue('\n')
    self.obj45.description.setHeight(4)

    # ofActions
    self.obj45.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj45.ofActions.setValue(lcobj2)

    # Measurement
    self.obj45.Measurement.setValue('\n')
    self.obj45.Measurement.setHeight(4)

    # Reward
    self.obj45.Reward.setValue('\n')
    self.obj45.Reward.setHeight(4)

    # ID
    self.obj45.ID.setValue('O|1')

    # name
    self.obj45.name.setValue('HatchDragonEgg')

    self.obj45.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(464.0,131.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj45.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj45)
    self.globalAndLocalPostcondition(self.obj45, rootNode)
    self.obj45.postAction( rootNode.CREATE )

    self.obj46=Objective(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # description
    self.obj46.description.setValue('\n')
    self.obj46.description.setHeight(4)

    # ofActions
    self.obj46.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('learn', 20)
    lcobj2.append(cobj2)
    self.obj46.ofActions.setValue(lcobj2)

    # Measurement
    self.obj46.Measurement.setValue('\n')
    self.obj46.Measurement.setHeight(4)

    # Reward
    self.obj46.Reward.setValue('\n')
    self.obj46.Reward.setHeight(4)

    # ID
    self.obj46.ID.setValue('O|2')

    # name
    self.obj46.name.setValue('LearnSpell')

    self.obj46.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(694.0,131.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=Objective(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # description
    self.obj47.description.setValue('\n')
    self.obj47.description.setHeight(4)

    # ofActions
    self.obj47.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('craftItem', 20)
    lcobj2.append(cobj2)
    self.obj47.ofActions.setValue(lcobj2)

    # Measurement
    self.obj47.Measurement.setValue('\n')
    self.obj47.Measurement.setHeight(4)

    # Reward
    self.obj47.Reward.setValue('\n')
    self.obj47.Reward.setHeight(4)

    # ID
    self.obj47.ID.setValue('O|3')

    # name
    self.obj47.name.setValue('BrewHatchingPotion')

    self.obj47.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(220.0,280.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=Objective(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # description
    self.obj48.description.setValue('\n')
    self.obj48.description.setHeight(4)

    # ofActions
    self.obj48.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('move', 20)
    lcobj2.append(cobj2)
    self.obj48.ofActions.setValue(lcobj2)

    # Measurement
    self.obj48.Measurement.setValue('\n')
    self.obj48.Measurement.setHeight(4)

    # Reward
    self.obj48.Reward.setValue('\n')
    self.obj48.Reward.setHeight(4)

    # ID
    self.obj48.ID.setValue('O|4')

    # name
    self.obj48.name.setValue('TransportDragonEgg')

    self.obj48.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(520.0,280.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=Objective(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # description
    self.obj49.description.setValue('\n')
    self.obj49.description.setHeight(4)

    # ofActions
    self.obj49.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('move', 20)
    lcobj2.append(cobj2)
    self.obj49.ofActions.setValue(lcobj2)

    # Measurement
    self.obj49.Measurement.setValue('\n')
    self.obj49.Measurement.setHeight(4)

    # Reward
    self.obj49.Reward.setValue('\n')
    self.obj49.Reward.setHeight(4)

    # ID
    self.obj49.ID.setValue('O|5')

    # name
    self.obj49.name.setValue('FindEggHermit')

    self.obj49.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(680.0,280.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=Objective(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # description
    self.obj50.description.setValue('\n')
    self.obj50.description.setHeight(4)

    # ofActions
    self.obj50.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('move', 20)
    lcobj2.append(cobj2)
    self.obj50.ofActions.setValue(lcobj2)

    # Measurement
    self.obj50.Measurement.setValue('\n')
    self.obj50.Measurement.setHeight(4)

    # Reward
    self.obj50.Reward.setValue('\n')
    self.obj50.Reward.setHeight(4)

    # ID
    self.obj50.ID.setValue('O|6')

    # name
    self.obj50.name.setValue('FindDragonEgg')

    self.obj50.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(380.0,280.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=Objective(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # description
    self.obj51.description.setValue('\n')
    self.obj51.description.setHeight(4)

    # ofActions
    self.obj51.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj51.ofActions.setValue(lcobj2)

    # Measurement
    self.obj51.Measurement.setValue('\n')
    self.obj51.Measurement.setHeight(4)

    # Reward
    self.obj51.Reward.setValue('\n')
    self.obj51.Reward.setHeight(4)

    # ID
    self.obj51.ID.setValue('O|7')

    # name
    self.obj51.name.setValue('GatherPotionIngredients')

    self.obj51.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(60.0,280.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=Objective(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # description
    self.obj52.description.setValue('\n')
    self.obj52.description.setHeight(4)

    # ofActions
    self.obj52.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('move', 20)
    lcobj2.append(cobj2)
    self.obj52.ofActions.setValue(lcobj2)

    # Measurement
    self.obj52.Measurement.setValue('\n')
    self.obj52.Measurement.setHeight(4)

    # Reward
    self.obj52.Reward.setValue('\n')
    self.obj52.Reward.setHeight(4)

    # ID
    self.obj52.ID.setValue('O|8')

    # name
    self.obj52.name.setValue('FindItemIngredient')

    self.obj52.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(50.0,430.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=Objective(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # description
    self.obj53.description.setValue('\n')
    self.obj53.description.setHeight(4)

    # ofActions
    self.obj53.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('harvestItem', 20)
    lcobj2.append(cobj2)
    self.obj53.ofActions.setValue(lcobj2)

    # Measurement
    self.obj53.Measurement.setValue('\n')
    self.obj53.Measurement.setHeight(4)

    # Reward
    self.obj53.Reward.setValue('\n')
    self.obj53.Reward.setHeight(4)

    # ID
    self.obj53.ID.setValue('O|9')

    # name
    self.obj53.name.setValue('HarvestItemIngredient')

    self.obj53.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(240.0,430.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj132=isPartOfOrgUnit(self)
    self.obj132.isGraphObjectVisual = True

    if(hasattr(self.obj132, '_setHierarchicalLink')):
      self.obj132._setHierarchicalLink(True)

    # ID
    self.obj132.ID.setValue('pOU|0')

    self.obj132.graphClass_= graph_isPartOfOrgUnit
    if self.genGraphics:
       new_obj = graph_isPartOfOrgUnit(486.0,954.0,self.obj132)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfOrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj132.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj132)
    self.globalAndLocalPostcondition(self.obj132, rootNode)
    self.obj132.postAction( rootNode.CREATE )

    self.obj124=canHaveRole(self)
    self.obj124.isGraphObjectVisual = True

    if(hasattr(self.obj124, '_setHierarchicalLink')):
      self.obj124._setHierarchicalLink(True)

    # ID
    self.obj124.ID.setValue('OUR|0')

    self.obj124.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(601.5,788.5,self.obj124)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj124.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj124)
    self.globalAndLocalPostcondition(self.obj124, rootNode)
    self.obj124.postAction( rootNode.CREATE )

    self.obj131=canHaveRole(self)
    self.obj131.isGraphObjectVisual = True

    if(hasattr(self.obj131, '_setHierarchicalLink')):
      self.obj131._setHierarchicalLink(True)

    # ID
    self.obj131.ID.setValue('OUR|1')

    self.obj131.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(678.5,952.5,self.obj131)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj131.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj131)
    self.globalAndLocalPostcondition(self.obj131, rootNode)
    self.obj131.postAction( rootNode.CREATE )

    self.obj113=hasActions(self)
    self.obj113.isGraphObjectVisual = True

    if(hasattr(self.obj113, '_setHierarchicalLink')):
      self.obj113._setHierarchicalLink(False)

    # ID
    self.obj113.ID.setValue('aR|0')

    self.obj113.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(226.0,699.0,self.obj113)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj113.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj113)
    self.globalAndLocalPostcondition(self.obj113, rootNode)
    self.obj113.postAction( rootNode.CREATE )

    self.obj114=hasActions(self)
    self.obj114.isGraphObjectVisual = True

    if(hasattr(self.obj114, '_setHierarchicalLink')):
      self.obj114._setHierarchicalLink(False)

    # ID
    self.obj114.ID.setValue('aR|1')

    self.obj114.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(374.0,701.0,self.obj114)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj114.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj114)
    self.globalAndLocalPostcondition(self.obj114, rootNode)
    self.obj114.postAction( rootNode.CREATE )

    self.obj115=hasActions(self)
    self.obj115.isGraphObjectVisual = True

    if(hasattr(self.obj115, '_setHierarchicalLink')):
      self.obj115._setHierarchicalLink(False)

    # ID
    self.obj115.ID.setValue('aR|2')

    self.obj115.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(827.0,698.0,self.obj115)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj115.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj115)
    self.globalAndLocalPostcondition(self.obj115, rootNode)
    self.obj115.postAction( rootNode.CREATE )

    self.obj145=canAccessKnArt(self)
    self.obj145.isGraphObjectVisual = True

    if(hasattr(self.obj145, '_setHierarchicalLink')):
      self.obj145._setHierarchicalLink(False)

    # ID
    self.obj145.ID.setValue('accKA|0')

    self.obj145.graphClass_= graph_canAccessKnArt
    if self.genGraphics:
       new_obj = graph_canAccessKnArt(563.5,1042.5,self.obj145)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canAccessKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj145.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj145)
    self.globalAndLocalPostcondition(self.obj145, rootNode)
    self.obj145.postAction( rootNode.CREATE )

    self.obj75=isPartOfObjective(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(True)

    # ID
    self.obj75.ID.setValue('pO|0')

    self.obj75.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(177.0,398.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj80=isPartOfObjective(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(True)

    # ID
    self.obj80.ID.setValue('pO|1')

    self.obj80.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(503.0,249.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj82=isPartOfObjective(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(True)

    # ID
    self.obj82.ID.setValue('pO|2')

    self.obj82.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(609.0,137.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj98=hasObjective(self)
    self.obj98.isGraphObjectVisual = True

    if(hasattr(self.obj98, '_setHierarchicalLink')):
      self.obj98._setHierarchicalLink(False)

    # ID
    self.obj98.ID.setValue('RPO|0')

    self.obj98.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(225.354103175,548.534028917,self.obj98)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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

    # ID
    self.obj99.ID.setValue('RPO|1')

    self.obj99.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(325.492909804,550.264185836,self.obj99)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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

    # ID
    self.obj100.ID.setValue('RPO|2')

    self.obj100.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(424.752042781,549.309380895,self.obj100)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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

    # ID
    self.obj101.ID.setValue('RPO|3')

    self.obj101.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(824.680362868,550.007372124,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj101)
    self.globalAndLocalPostcondition(self.obj101, rootNode)
    self.obj101.postAction( rootNode.CREATE )

    self.obj74=precedentTo(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(True)

    # ID
    self.obj74.ID.setValue('OpO|0')

    self.obj74.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(203.489587602,474.039234071,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj76=precedentTo(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(True)

    # ID
    self.obj76.ID.setValue('OpO|1')

    self.obj76.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(202.120938013,322.2623221,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj77=precedentTo(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(True)

    # ID
    self.obj77.ID.setValue('OpO|2')

    self.obj77.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(353.454745276,323.455638382,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj78=precedentTo(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(True)

    # ID
    self.obj78.ID.setValue('OpO|3')

    self.obj78.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(501.991811703,335.007768111,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj79=precedentTo(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(True)

    # ID
    self.obj79.ID.setValue('OpO|4')

    self.obj79.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(653.376888985,330.342413802,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj81=precedentTo(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(True)

    # ID
    self.obj81.ID.setValue('OpO|5')

    self.obj81.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(609.357627945,190.638564425,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    # Connections for obj118 (graphObject_: Obj49) named Avatar
    self.drawConnections(
(self.obj118,self.obj124,[561.0, 953.0, 624.0, 934.0, 601.5, 788.5],"true", 3),
(self.obj118,self.obj131,[561.0, 953.0, 678.5, 952.5],"true", 2),
(self.obj118,self.obj132,[561.0, 953.0, 486.0, 954.0],"true", 2),
(self.obj118,self.obj145,[561.0, 953.0, 489.0, 990.0, 563.5, 1042.5],"true", 3) )
    # Connections for obj119 (graphObject_: Obj50) named Party
    self.drawConnections(
 )
    # Connections for obj104 (graphObject_: Obj40) named Scout
    self.drawConnections(
(self.obj104,self.obj113,[226.0, 782.0, 174.0, 739.0, 226.0, 699.0],"true", 3) )
    # Connections for obj105 (graphObject_: Obj41) named Maker
    self.drawConnections(
(self.obj105,self.obj114,[376.0, 782.0, 320.0, 747.0, 374.0, 701.0],"true", 3) )
    # Connections for obj106 (graphObject_: Obj42) named Wizard
    self.drawConnections(
(self.obj106,self.obj115,[826.0, 782.0, 763.0, 744.0, 827.0, 698.0],"true", 3) )
    # Connections for obj125 (graphObject_: Obj53) named PartyFounder
    self.drawConnections(
 )
    # Connections for obj126 (graphObject_: Obj54) named PartyMember
    self.drawConnections(
 )
    # Connections for obj86 (graphObject_: Obj28) named move
    self.drawConnections(
(self.obj86,self.obj98,[224.0, 628.0, 225.35410317499964, 548.5340289174825],"true", 2) )
    # Connections for obj87 (graphObject_: Obj29) named harvestItem
    self.drawConnections(
(self.obj87,self.obj99,[324.0, 628.0, 325.49290980409205, 550.2641858357085],"true", 2) )
    # Connections for obj88 (graphObject_: Obj30) named craftItem
    self.drawConnections(
(self.obj88,self.obj100,[424.0, 628.0, 424.7520427813149, 549.3093808947315],"true", 2) )
    # Connections for obj89 (graphObject_: Obj31) named learnSpell
    self.drawConnections(
(self.obj89,self.obj101,[824.0, 628.0, 824.6803628684763, 550.0073721236759],"true", 2) )
    # Connections for obj133 (graphObject_: Obj59) named AvatarInventory
    self.drawConnections(
 )
    # Connections for obj134 (graphObject_: Obj60) named AvatarAttributes
    self.drawConnections(
 )
    # Connections for obj44 (graphObject_: Obj0) named FinishQuestForTheDragonEgg
    self.drawConnections(
 )
    # Connections for obj45 (graphObject_: Obj1) named HatchDragonEgg
    self.drawConnections(
(self.obj45,self.obj81,[713.5040855626298, 414.61876178946295, 609.3576279446208, 190.6385644254878],"true", 0),
(self.obj45,self.obj82,[713.5040855626298, 414.61876178946295, 609.0, 137.0],"true", 0) )
    # Connections for obj46 (graphObject_: Obj2) named LearnSpell
    self.drawConnections(
(self.obj46,self.obj82,[1197.9501491946323, 297.20372094102413, 609.0, 137.0],"true", 0) )
    # Connections for obj47 (graphObject_: Obj3) named BrewHatchingPotion
    self.drawConnections(
(self.obj47,self.obj77,[380.61803230937585, 245.72047989466682, 353.4547452756782, 323.45563838240116],"true", 0),
(self.obj47,self.obj80,[380.61803230937585, 245.72047989466682, 503.0, 249.0],"true", 0) )
    # Connections for obj48 (graphObject_: Obj4) named TransportDragonEgg
    self.drawConnections(
(self.obj48,self.obj79,[768.1966051352533, 463.7319071577135, 653.3768889850651, 330.34241380246567],"true", 0),
(self.obj48,self.obj80,[768.1966051352533, 463.7319071577135, 503.0, 249.0],"true", 0) )
    # Connections for obj49 (graphObject_: Obj5) named FindEggHermit
    self.drawConnections(
(self.obj49,self.obj80,[961.6229558403763, 493.8694299102599, 503.0, 249.0],"true", 0) )
    # Connections for obj50 (graphObject_: Obj6) named FindDragonEgg
    self.drawConnections(
(self.obj50,self.obj78,[356.5040855626298, 465.61876178946295, 501.9918117034965, 335.0077681105661],"true", 0),
(self.obj50,self.obj80,[356.5040855626298, 465.61876178946295, 503.0, 249.0],"true", 0) )
    # Connections for obj51 (graphObject_: Obj7) named GatherPotionIngredients
    self.drawConnections(
(self.obj51,self.obj76,[174.70820634999927, 412.068057834965, 202.1209380131943, 322.26232210038927],"true", 0) )
    # Connections for obj52 (graphObject_: Obj8) named FindItemIngredient
    self.drawConnections(
(self.obj52,self.obj74,[-235.0, 141.0, 203.48958760238037, 474.03923407073523],"true", 0),
(self.obj52,self.obj75,[-235.0, 141.0, 177.0, 398.0],"true", 0) )
    # Connections for obj53 (graphObject_: Obj9) named HarvestItemIngredient
    self.drawConnections(
(self.obj53,self.obj75,[607.7082063499993, 576.068057834965, 177.0, 398.0],"true", 0) )
    # Connections for obj132 (graphObject_: Obj57) of type isPartOfOrgUnit
    self.drawConnections(
(self.obj132,self.obj119,[486.0, 954.0, 401.0, 953.0],"true", 2) )
    # Connections for obj124 (graphObject_: Obj51) of type canHaveRole
    self.drawConnections(
(self.obj124,self.obj105,[601.5, 788.5, 487.0, 756.0, 376.0, 782.0],"true", 3),
(self.obj124,self.obj104,[601.5, 788.5, 376.0, 897.0, 226.0, 782.0],"true", 3),
(self.obj124,self.obj106,[601.5, 788.5, 714.0, 803.0, 826.0, 782.0],"true", 3) )
    # Connections for obj131 (graphObject_: Obj55) of type canHaveRole
    self.drawConnections(
(self.obj131,self.obj125,[678.5, 952.5, 826.0, 912.0],"true", 2),
(self.obj131,self.obj126,[678.5, 952.5, 826.0, 992.0],"true", 2) )
    # Connections for obj113 (graphObject_: Obj43) of type hasActions
    self.drawConnections(
(self.obj113,self.obj86,[226.0, 699.0, 272.0, 664.0, 224.0, 628.0],"true", 3) )
    # Connections for obj114 (graphObject_: Obj45) of type hasActions
    self.drawConnections(
(self.obj114,self.obj87,[374.0, 701.0, 377.0, 640.0, 324.0, 628.0],"true", 3),
(self.obj114,self.obj88,[374.0, 701.0, 389.0, 639.0, 424.0, 628.0],"true", 3) )
    # Connections for obj115 (graphObject_: Obj47) of type hasActions
    self.drawConnections(
(self.obj115,self.obj89,[827.0, 698.0, 906.0, 660.0, 824.0, 628.0],"true", 3) )
    # Connections for obj145 (graphObject_: Obj61) of type canAccessKnArt
    self.drawConnections(
(self.obj145,self.obj133,[563.5, 1042.5, 500.0, 1060.0],"true", 2),
(self.obj145,self.obj134,[563.5, 1042.5, 620.0, 1060.0],"true", 2) )
    # Connections for obj75 (graphObject_: Obj12) of type isPartOfObjective
    self.drawConnections(
(self.obj75,self.obj51,[177.0, 398.0, 178.2629049361234, 364.86034626012236, 130.61803230937585, 324.7204798946668],"true", 3) )
    # Connections for obj80 (graphObject_: Obj22) of type isPartOfObjective
    self.drawConnections(
(self.obj80,self.obj45,[503.0, 249.0, 474.52482250400703, 207.10198421398871, 514.9501491946326, 176.20372094102413],"true", 3) )
    # Connections for obj82 (graphObject_: Obj26) of type isPartOfObjective
    self.drawConnections(
(self.obj82,self.obj44,[609.0, 137.0, 597.5812361835442, 111.09174255367876, 633.208815266094, 76.1835387990368],"true", 3) )
    # Connections for obj98 (graphObject_: Obj32) of type hasObjective
    self.drawConnections(
(self.obj98,self.obj52,[225.35410317499964, 548.5340289174825, 158.0, 542.0, 104.70820634999927, 475.068057834965],"true", 3),
(self.obj98,self.obj50,[225.35410317499964, 548.5340289174825, 504.0, 452.0, 426.1966051352533, 324.7319071577135],"true", 3),
(self.obj98,self.obj48,[225.35410317499964, 548.5340289174825, 542.0, 459.0, 580.6229558403768, 324.8694299102599],"true", 3),
(self.obj98,self.obj49,[225.35410317499964, 548.5340289174825, 665.0, 464.0, 723.8107339701214, 324.7970978180615],"true", 3) )
    # Connections for obj99 (graphObject_: Obj34) of type hasObjective
    self.drawConnections(
(self.obj99,self.obj53,[325.49290980409205, 550.2641858357085, 326.0, 496.0, 304.98581960818404, 474.52837167141706],"true", 3) )
    # Connections for obj100 (graphObject_: Obj36) of type hasObjective
    self.drawConnections(
(self.obj100,self.obj47,[424.7520427813149, 549.3093808947315, 423.0, 422.0, 279.5040855626298, 324.61876178946295],"true", 3) )
    # Connections for obj101 (graphObject_: Obj38) of type hasObjective
    self.drawConnections(
(self.obj101,self.obj46,[824.6803628684763, 550.0073721236759, 825.0, 204.0, 725.3607257369526, 176.0147442473517],"true", 3) )
    # Connections for obj74 (graphObject_: Obj10) of type precedentTo
    self.drawConnections(
(self.obj74,self.obj53,[203.48958760238037, 474.03923407073523, 233.80899091692658, 491.6543125298483, 304.98581960818404, 474.52837167141706],"true", 3) )
    # Connections for obj76 (graphObject_: Obj14) of type precedentTo
    self.drawConnections(
(self.obj76,self.obj47,[202.1209380131943, 322.26232210038927, 223.34245132650778, 311.9868925740883, 279.5040855626298, 324.61876178946295],"true", 3) )
    # Connections for obj77 (graphObject_: Obj16) of type precedentTo
    self.drawConnections(
(self.obj77,self.obj50,[353.4547452756782, 323.45563838240116, 398.37787516883407, 298.2339247244638, 426.1966051352533, 324.7319071577135],"true", 3) )
    # Connections for obj78 (graphObject_: Obj18) of type precedentTo
    self.drawConnections(
(self.obj78,self.obj48,[501.9918117034965, 335.0077681105661, 536.3483993797774, 326.79214879870267, 580.6229558403768, 324.8694299102599],"true", 3) )
    # Connections for obj79 (graphObject_: Obj20) of type precedentTo
    self.drawConnections(
(self.obj79,self.obj49,[653.3768889850651, 330.34241380246567, 690.9238335175013, 329.0743307794161, 723.8107339701214, 324.7970978180615],"true", 3) )
    # Connections for obj81 (graphObject_: Obj24) of type precedentTo
    self.drawConnections(
(self.obj81,self.obj46,[609.3576279446208, 190.6385644254878, 669.2102720802009, 192.3413202520697, 725.3607257369526, 176.0147442473517],"true", 3) )

newfunction = TMWQuestDragonEggActions_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
