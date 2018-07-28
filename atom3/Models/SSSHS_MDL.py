"""
__SSSHS_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Sun Apr 15 21:24:44 2018
___________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from Action import *
from Objective import *
from isPartOfOrgUnit import *
from canHaveRole import *
from hasActions import *
from isPartOfObjective import *
from hasObjective import *
from isPartOfRole import *
from graph_canHaveRole import *
from graph_isPartOfOrgUnit import *
from graph_Action import *
from graph_Objective import *
from graph_hasObjective import *
from graph_Role import *
from graph_OrgUnit import *
from graph_isPartOfObjective import *
from graph_hasActions import *
from graph_isPartOfRole import *
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

def SSSHS_MDL(self, rootNode, LSMASOMMRootNode=None):

    # --- Generating attributes code for ASG LSMASOMM ---
    if( LSMASOMMRootNode ): 
        # agentImplementation
        LSMASOMMRootNode.agentImplementation.setValue( (['SPADE', 'Enmasse', 'EveJS'], 0) )
        LSMASOMMRootNode.agentImplementation.config = 0

        # author
        LSMASOMMRootNode.author.setValue('Bogdan')

        # description
        LSMASOMMRootNode.description.setValue('\n')
        LSMASOMMRootNode.description.setHeight(15)

        # name
        LSMASOMMRootNode.name.setValue('SSSHS')

        # title
        LSMASOMMRootNode.title.setValue('')
        LSMASOMMRootNode.title.setNone()
    # --- ASG attributes over ---


    self.obj44=OrgUnit(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # Individual
    self.obj44.Individual.setValue(('1', 0))
    self.obj44.Individual.config = 0

    # hasActions
    self.obj44.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj44.hasActions.setValue(lcobj2)

    # ID
    self.obj44.ID.setValue('OU|0')

    # name
    self.obj44.name.setValue('IndividualAgent')

    # UnitSize
    self.obj44.UnitSize.setValue('Individual')

    self.obj44.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(343,0,self.obj44)
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

    self.obj45=OrgUnit(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # Individual
    self.obj45.Individual.setValue(('1', 0))
    self.obj45.Individual.config = 0

    # hasActions
    self.obj45.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj45.hasActions.setValue(lcobj2)

    # ID
    self.obj45.ID.setValue('OU|1')

    # name
    self.obj45.name.setValue('Aggregated')

    # UnitSize
    self.obj45.UnitSize.setValue('Group')

    self.obj45.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(38.0,39.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
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
    self.obj46.isMetaRole.setValue((None, 1))
    self.obj46.isMetaRole.config = 0

    # hasActions
    self.obj46.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('Negotiate', 20)
    lcobj2.append(cobj2)
    self.obj46.hasActions.setValue(lcobj2)

    # ID
    self.obj46.ID.setValue('R|0')

    # name
    self.obj46.name.setValue('Negotiator')

    self.obj46.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(23.0,222.0,self.obj46)
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
    cobj2=ATOM3String('StoreResource', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('SupportSelfSustainability', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Interact', 20)
    lcobj2.append(cobj2)
    self.obj47.hasActions.setValue(lcobj2)

    # ID
    self.obj47.ID.setValue('R|1')

    # name
    self.obj47.name.setValue('Storage')

    self.obj47.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(151.0,212.0,self.obj47)
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
    cobj2=ATOM3String('UseResource', 20)
    lcobj2.append(cobj2)
    self.obj48.hasActions.setValue(lcobj2)

    # ID
    self.obj48.ID.setValue('R|2')

    # name
    self.obj48.name.setValue('User')

    self.obj48.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(434.0,212.0,self.obj48)
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

    self.obj49=Role(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # isMetaRole
    self.obj49.isMetaRole.setValue((None, 0))
    self.obj49.isMetaRole.config = 0

    # hasActions
    self.obj49.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ProduceResource', 20)
    lcobj2.append(cobj2)
    self.obj49.hasActions.setValue(lcobj2)

    # ID
    self.obj49.ID.setValue('R|3')

    # name
    self.obj49.name.setValue('Producer')

    self.obj49.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(558.0,212.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj63=Action(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # ID
    self.obj63.ID.setValue('A|0')

    # name
    self.obj63.name.setValue('StoreResource')

    # ActionCode
    self.obj63.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj63.ActionCode.setHeight(15)

    self.obj63.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(41.0,408.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj68=Action(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # ID
    self.obj68.ID.setValue('A|1')

    # name
    self.obj68.name.setValue('UseResource')

    # ActionCode
    self.obj68.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj68.ActionCode.setHeight(15)

    self.obj68.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(420.0,331.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=Action(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    # ID
    self.obj69.ID.setValue('A|2')

    # name
    self.obj69.name.setValue('ProduceResource')

    # ActionCode
    self.obj69.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj69.ActionCode.setHeight(15)

    self.obj69.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(545.0,331.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=Action(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # ID
    self.obj70.ID.setValue('A|3')

    # name
    self.obj70.name.setValue('Negotiate')

    # ActionCode
    self.obj70.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj70.ActionCode.setHeight(15)

    self.obj70.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(28.0,341.0,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj82=Action(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # ID
    self.obj82.ID.setValue('A|4')

    # name
    self.obj82.name.setValue('SupportSelfSustainability')

    # ActionCode
    self.obj82.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj82.ActionCode.setHeight(15)

    self.obj82.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(155.0,408.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj83=Action(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # ID
    self.obj83.ID.setValue('A|5')

    # name
    self.obj83.name.setValue('Interact')

    # ActionCode
    self.obj83.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj83.ActionCode.setHeight(15)

    self.obj83.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(347.0,408.0,self.obj83)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj83.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj83)
    self.globalAndLocalPostcondition(self.obj83, rootNode)
    self.obj83.postAction( rootNode.CREATE )

    self.obj88=Objective(self)
    self.obj88.isGraphObjectVisual = True

    if(hasattr(self.obj88, '_setHierarchicalLink')):
      self.obj88._setHierarchicalLink(False)

    # description
    self.obj88.description.setValue('\n')
    self.obj88.description.setHeight(4)

    # ofActions
    self.obj88.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('StoreResource', 20)
    lcobj2.append(cobj2)
    self.obj88.ofActions.setValue(lcobj2)

    # Measurement
    self.obj88.Measurement.setValue('\n')
    self.obj88.Measurement.setHeight(4)

    # Reward
    self.obj88.Reward.setValue('\n')
    self.obj88.Reward.setHeight(4)

    # ID
    self.obj88.ID.setValue('O|0')

    # name
    self.obj88.name.setValue('StoredResource')

    self.obj88.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(46.0,509.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj89=Objective(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(False)

    # description
    self.obj89.description.setValue('\n')
    self.obj89.description.setHeight(4)

    # ofActions
    self.obj89.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('UseResource', 20)
    lcobj2.append(cobj2)
    self.obj89.ofActions.setValue(lcobj2)

    # Measurement
    self.obj89.Measurement.setValue('\n')
    self.obj89.Measurement.setHeight(4)

    # Reward
    self.obj89.Reward.setValue('\n')
    self.obj89.Reward.setHeight(4)

    # ID
    self.obj89.ID.setValue('O|1')

    # name
    self.obj89.name.setValue('UsedResource')

    self.obj89.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(426.0,432.0,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=Objective(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # description
    self.obj90.description.setValue('\n')
    self.obj90.description.setHeight(4)

    # ofActions
    self.obj90.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ProduceResource', 20)
    lcobj2.append(cobj2)
    self.obj90.ofActions.setValue(lcobj2)

    # Measurement
    self.obj90.Measurement.setValue('\n')
    self.obj90.Measurement.setHeight(4)

    # Reward
    self.obj90.Reward.setValue('\n')
    self.obj90.Reward.setHeight(4)

    # ID
    self.obj90.ID.setValue('O|2')

    # name
    self.obj90.name.setValue('ProducedResource')

    self.obj90.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(550.0,432.0,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=Objective(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # description
    self.obj91.description.setValue('\n')
    self.obj91.description.setHeight(4)

    # ofActions
    self.obj91.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj91.ofActions.setValue(lcobj2)

    # Measurement
    self.obj91.Measurement.setValue('\n')
    self.obj91.Measurement.setHeight(4)

    # Reward
    self.obj91.Reward.setValue('\n')
    self.obj91.Reward.setHeight(4)

    # ID
    self.obj91.ID.setValue('O|3')

    # name
    self.obj91.name.setValue('MaintainSustainability')

    self.obj91.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(411.0,578.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj81=isPartOfOrgUnit(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(True)

    # ID
    self.obj81.ID.setValue('pOU|0')

    self.obj81.graphClass_= graph_isPartOfOrgUnit
    if self.genGraphics:
       new_obj = graph_isPartOfOrgUnit(248.372732048,80.4575390344,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfOrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj80=canHaveRole(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(True)

    # ID
    self.obj80.ID.setValue('OUR|0')

    self.obj80.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(394.0,160.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj66=hasActions(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # ID
    self.obj66.ID.setValue('aR|0')

    self.obj66.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(218.0,373.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj75=hasActions(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # ID
    self.obj75.ID.setValue('aR|1')

    self.obj75.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(626.477362754,315.548697012,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=hasActions(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # ID
    self.obj76.ID.setValue('aR|2')

    self.obj76.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(489.0,316.5,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj79=hasActions(self)
    self.obj79.isGraphObjectVisual = True

    if(hasattr(self.obj79, '_setHierarchicalLink')):
      self.obj79._setHierarchicalLink(False)

    # ID
    self.obj79.ID.setValue('aR|3')

    self.obj79.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(82.0,326.5,self.obj79)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj79.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj79)
    self.globalAndLocalPostcondition(self.obj79, rootNode)
    self.obj79.postAction( rootNode.CREATE )

    self.obj103=isPartOfObjective(self)
    self.obj103.isGraphObjectVisual = True

    if(hasattr(self.obj103, '_setHierarchicalLink')):
      self.obj103._setHierarchicalLink(True)

    # ID
    self.obj103.ID.setValue('pO|0')

    self.obj103.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(470.0,548.0,self.obj103)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj103.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj103)
    self.globalAndLocalPostcondition(self.obj103, rootNode)
    self.obj103.postAction( rootNode.CREATE )

    self.obj100=hasObjective(self)
    self.obj100.isGraphObjectVisual = True

    if(hasattr(self.obj100, '_setHierarchicalLink')):
      self.obj100._setHierarchicalLink(False)

    # ID
    self.obj100.ID.setValue('RPO|0')

    self.obj100.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(627.492288413,423.555341345,self.obj100)
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
    self.obj101.ID.setValue('RPO|1')

    self.obj101.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(489.499142716,422.814822753,self.obj101)
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

    self.obj102=hasObjective(self)
    self.obj102.isGraphObjectVisual = True

    if(hasattr(self.obj102, '_setHierarchicalLink')):
      self.obj102._setHierarchicalLink(False)

    # ID
    self.obj102.ID.setValue('RPO|2')

    self.obj102.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(114.0,500.0,self.obj102)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj102.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj102)
    self.globalAndLocalPostcondition(self.obj102, rootNode)
    self.obj102.postAction( rootNode.CREATE )

    self.obj104=isPartOfRole(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(True)

    # ID
    self.obj104.ID.setValue('pR|0')

    self.obj104.graphClass_= graph_isPartOfRole
    if self.genGraphics:
       new_obj = graph_isPartOfRole(136.0,262.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    # Connections for obj44 (graphObject_: Obj0) named IndividualAgent
    self.drawConnections(
(self.obj44,self.obj80,[111.0, 253.0, 394.0, 160.0],"true", 0),
(self.obj44,self.obj81,[111.0, 253.0, 248.3727320482865, 80.45753903439848],"true", 0) )
    # Connections for obj45 (graphObject_: Obj1) named Aggregated
    self.drawConnections(
 )
    # Connections for obj46 (graphObject_: Obj2) named Negotiator
    self.drawConnections(
(self.obj46,self.obj79,[30.0, -174.0, 82.0, 326.5],"true", 2) )
    # Connections for obj47 (graphObject_: Obj3) named Storage
    self.drawConnections(
(self.obj47,self.obj66,[422.0, 387.0, 218.0, 373.0],"true", 2),
(self.obj47,self.obj104,[686.0, 345.0, 136.0, 262.0],"true", 0) )
    # Connections for obj48 (graphObject_: Obj4) named User
    self.drawConnections(
(self.obj48,self.obj76,[366.0, 361.0, 489.0, 316.5],"true", 2) )
    # Connections for obj49 (graphObject_: Obj5) named Producer
    self.drawConnections(
(self.obj49,self.obj75,[356.0, 451.0, 626.4773627544887, 315.548697011691],"true", 2) )
    # Connections for obj63 (graphObject_: Obj8) named StoreResource
    self.drawConnections(
(self.obj63,self.obj102,[704.0, 327.0, 114.0, 500.0],"true", 0) )
    # Connections for obj68 (graphObject_: Obj11) named UseResource
    self.drawConnections(
(self.obj68,self.obj101,[654.0, 417.0, 489.499142716303, 422.8148227526268],"true", 0) )
    # Connections for obj69 (graphObject_: Obj12) named ProduceResource
    self.drawConnections(
(self.obj69,self.obj100,[644.0, 537.0, 627.4922884130543, 423.55534134480706],"true", 0) )
    # Connections for obj70 (graphObject_: Obj13) named Negotiate
    self.drawConnections(
 )
    # Connections for obj82 (graphObject_: Obj24) named SupportSelfSustainability
    self.drawConnections(
 )
    # Connections for obj83 (graphObject_: Obj25) named Interact
    self.drawConnections(
 )
    # Connections for obj88 (graphObject_: Obj26) named StoredResource
    self.drawConnections(
(self.obj88,self.obj103,[94.0, 554.0, 282.31910830986897, 570.9974540851223, 470.0, 548.0],"true", 3) )
    # Connections for obj89 (graphObject_: Obj27) named UsedResource
    self.drawConnections(
(self.obj89,self.obj103,[470.0, 477.0, 450.0, 512.5, 470.0, 548.0],"true", 3) )
    # Connections for obj90 (graphObject_: Obj28) named ProducedResource
    self.drawConnections(
(self.obj90,self.obj103,[606.0, 477.0, 528.7442249580248, 494.770628088611, 470.0, 548.0],"true", 3) )
    # Connections for obj91 (graphObject_: Obj29) named MaintainSustainability
    self.drawConnections(
 )
    # Connections for obj81 (graphObject_: Obj22) of type isPartOfOrgUnit
    self.drawConnections(
(self.obj81,self.obj45,[248.3727320482865, 80.45753903439848, 159.8727320482865, 110.20753903439848, 80.0, 102.0],"true", 3) )
    # Connections for obj80 (graphObject_: Obj20) of type canHaveRole
    self.drawConnections(
(self.obj80,self.obj47,[394.0, 160.0, 315.63188626225275, 229.24369104248782, 217.0, 264.0],"true", 3),
(self.obj80,self.obj48,[394.0, 160.0, 447.7218066355901, 200.30158175318024, 469.0, 264.0],"true", 3),
(self.obj80,self.obj49,[394.0, 160.0, 507.87593037352303, 194.07744828423222, 604.0, 264.0],"true", 3),
(self.obj80,self.obj46,[394.0, 160.0, 170.66429574491633, 185.973664095018, 62.0, 274.0],"true", 3) )
    # Connections for obj66 (graphObject_: Obj9) of type hasActions
    self.drawConnections(
(self.obj66,self.obj63,[565.0, 270.0, 704.0, 327.0],"true", 2),
(self.obj66,self.obj82,[565.0, 270.0, 814.0, 287.0],"true", 0),
(self.obj66,self.obj83,[565.0, 270.0, 844.0, 227.0],"true", 0) )
    # Connections for obj75 (graphObject_: Obj14) of type hasActions
    self.drawConnections(
(self.obj75,self.obj69,[560.0, 485.0, 644.0, 537.0],"true", 2) )
    # Connections for obj76 (graphObject_: Obj16) of type hasActions
    self.drawConnections(
(self.obj76,self.obj68,[570.0, 380.0, 654.0, 417.0],"true", 2) )
    # Connections for obj79 (graphObject_: Obj18) of type hasActions
    self.drawConnections(
(self.obj79,self.obj70,[630.0, 150.0, 21.0, 147.0],"true", 2) )
    # Connections for obj103 (graphObject_: Obj36) of type isPartOfObjective
    self.drawConnections(
(self.obj103,self.obj91,[470.0, 548.0, 452.54429684286777, 586.8303802104755, 475.0, 623.0],"true", 3) )
    # Connections for obj100 (graphObject_: Obj30) of type hasObjective
    self.drawConnections(
(self.obj100,self.obj90,[627.4922884130543, 423.55534134480706, 626.7422884130543, 450.55534134480706, 606.0, 477.0],"true", 3) )
    # Connections for obj101 (graphObject_: Obj32) of type hasObjective
    self.drawConnections(
(self.obj101,self.obj89,[489.499142716303, 422.8148227526268, 489.749142716303, 449.8148227526268, 470.0, 477.0],"true", 3) )
    # Connections for obj102 (graphObject_: Obj34) of type hasObjective
    self.drawConnections(
(self.obj102,self.obj88,[114.0, 500.0, 114.0, 527.0, 94.0, 554.0],"true", 3) )
    # Connections for obj104 (graphObject_: Obj38) of type isPartOfRole
    self.drawConnections(
(self.obj104,self.obj46,[136.0, 262.0, 84.5, 264.0, 62.0, 274.0],"true", 3) )

newfunction = SSSHS_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
