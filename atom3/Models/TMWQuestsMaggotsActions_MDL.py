"""
__TMWQuestsMaggotsActions_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Tue May  1 04:16:41 2018
_____________________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Action import *
from Objective import *
from isPartOfObjective import *
from hasObjective import *
from precedentTo import *
from graph_isPartOfObjective import *
from graph_Objective import *
from graph_hasObjective import *
from graph_Action import *
from graph_precedentTo import *
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

def TMWQuestsMaggotsActions_MDL(self, rootNode, LSMASOMMRootNode=None):

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
        LSMASOMMRootNode.name.setValue('TMWGeneral')

        # title
        LSMASOMMRootNode.title.setValue('')
        LSMASOMMRootNode.title.setNone()
    # --- ASG attributes over ---


    self.obj101=Action(self)
    self.obj101.isGraphObjectVisual = True

    if(hasattr(self.obj101, '_setHierarchicalLink')):
      self.obj101._setHierarchicalLink(False)

    # ID
    self.obj101.ID.setValue('A|0')

    # name
    self.obj101.name.setValue('talkToNPC')

    # ActionCode
    self.obj101.ActionCode.setValue('#action code template\nclass talkToNPC(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj101.ActionCode.setHeight(15)

    self.obj101.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(0,303,self.obj101)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj101.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj101)
    self.globalAndLocalPostcondition(self.obj101, rootNode)
    self.obj101.postAction( rootNode.CREATE )

    self.obj105=Action(self)
    self.obj105.isGraphObjectVisual = True

    if(hasattr(self.obj105, '_setHierarchicalLink')):
      self.obj105._setHierarchicalLink(False)

    # ID
    self.obj105.ID.setValue('A|1')

    # name
    self.obj105.name.setValue('move')

    # ActionCode
    self.obj105.ActionCode.setValue('#action code template\nclass move(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj105.ActionCode.setHeight(15)

    self.obj105.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(131,202,self.obj105)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj105.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj105)
    self.globalAndLocalPostcondition(self.obj105, rootNode)
    self.obj105.postAction( rootNode.CREATE )

    self.obj109=Action(self)
    self.obj109.isGraphObjectVisual = True

    if(hasattr(self.obj109, '_setHierarchicalLink')):
      self.obj109._setHierarchicalLink(False)

    # ID
    self.obj109.ID.setValue('A|2')

    # name
    self.obj109.name.setValue('equipItem')

    # ActionCode
    self.obj109.ActionCode.setValue('#action code template\nclass equipItem(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj109.ActionCode.setHeight(15)

    self.obj109.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(131,303,self.obj109)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj109.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj109)
    self.globalAndLocalPostcondition(self.obj109, rootNode)
    self.obj109.postAction( rootNode.CREATE )

    self.obj83=Action(self)
    self.obj83.isGraphObjectVisual = True

    if(hasattr(self.obj83, '_setHierarchicalLink')):
      self.obj83._setHierarchicalLink(False)

    # ID
    self.obj83.ID.setValue('A|3')

    # name
    self.obj83.name.setValue('attack')

    # ActionCode
    self.obj83.ActionCode.setValue('#action code template\nclass attack(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj83.ActionCode.setHeight(15)

    self.obj83.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(363,202,self.obj83)
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
    self.obj44.ID.setValue('OMaggots0')

    # name
    self.obj44.name.setValue('FinishMaggots')

    self.obj44.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(892,303,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

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
    cobj2=ATOM3String('talkToNPC', 20)
    lcobj2.append(cobj2)
    self.obj47.ofActions.setValue(lcobj2)

    # Measurement
    self.obj47.Measurement.setValue('\n')
    self.obj47.Measurement.setHeight(4)

    # Reward
    self.obj47.Reward.setValue('\n')
    self.obj47.Reward.setHeight(4)

    # ID
    self.obj47.ID.setValue('OMaggots1')

    # name
    self.obj47.name.setValue('talkToNPCTanisha')

    self.obj47.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(131,404,self.obj47)
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
    cobj2=ATOM3String('equipItem', 20)
    lcobj2.append(cobj2)
    self.obj50.ofActions.setValue(lcobj2)

    # Measurement
    self.obj50.Measurement.setValue('\n')
    self.obj50.Measurement.setHeight(4)

    # Reward
    self.obj50.Reward.setValue('\n')
    self.obj50.Reward.setHeight(4)

    # ID
    self.obj50.ID.setValue('OMaggots2')

    # name
    self.obj50.name.setValue('equipItemKnife')

    self.obj50.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(259,303,self.obj50)
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

    self.obj55=Objective(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # description
    self.obj55.description.setValue('\n')
    self.obj55.description.setHeight(4)

    # ofActions
    self.obj55.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('move', 20)
    lcobj2.append(cobj2)
    self.obj55.ofActions.setValue(lcobj2)

    # Measurement
    self.obj55.Measurement.setValue('\n')
    self.obj55.Measurement.setHeight(4)

    # Reward
    self.obj55.Reward.setValue('\n')
    self.obj55.Reward.setHeight(4)

    # ID
    self.obj55.ID.setValue('OMaggots3')

    # name
    self.obj55.name.setValue('goToLocation10287')

    self.obj55.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(363,303,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj58=Objective(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # description
    self.obj58.description.setValue('\n')
    self.obj58.description.setHeight(4)

    # ofActions
    self.obj58.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('attack', 20)
    lcobj2.append(cobj2)
    self.obj58.ofActions.setValue(lcobj2)

    # Measurement
    self.obj58.Measurement.setValue('\n')
    self.obj58.Measurement.setHeight(4)

    # Reward
    self.obj58.Reward.setValue('\n')
    self.obj58.Reward.setHeight(4)

    # ID
    self.obj58.ID.setValue('OMaggots4')

    # name
    self.obj58.name.setValue('killMobMaggot10')

    self.obj58.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(493,202,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj63=Objective(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # description
    self.obj63.description.setValue('\n')
    self.obj63.description.setHeight(4)

    # ofActions
    self.obj63.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('move', 20)
    lcobj2.append(cobj2)
    self.obj63.ofActions.setValue(lcobj2)

    # Measurement
    self.obj63.Measurement.setValue('\n')
    self.obj63.Measurement.setHeight(4)

    # Reward
    self.obj63.Reward.setValue('\n')
    self.obj63.Reward.setHeight(4)

    # ID
    self.obj63.ID.setValue('OMaggots5')

    # name
    self.obj63.name.setValue('goToNPCTanisha')

    self.obj63.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(608,101,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj68=Objective(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # description
    self.obj68.description.setValue('\n')
    self.obj68.description.setHeight(4)

    # ofActions
    self.obj68.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('talkToNPC', 20)
    lcobj2.append(cobj2)
    self.obj68.ofActions.setValue(lcobj2)

    # Measurement
    self.obj68.Measurement.setValue('\n')
    self.obj68.Measurement.setHeight(4)

    # Reward
    self.obj68.Reward.setValue('\n')
    self.obj68.Reward.setHeight(4)

    # ID
    self.obj68.ID.setValue('OMaggots6')

    # name
    self.obj68.name.setValue('talkToNPCTanisha')

    self.obj68.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(729,0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj71=isPartOfObjective(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(True)

    # ID
    self.obj71.ID.setValue('pO|0')

    self.obj71.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(867.0,313.0,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj80=hasObjective(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # ID
    self.obj80.ID.setValue('RPO|0')

    self.obj80.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(235.010283244,334.513027936,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=hasObjective(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # ID
    self.obj81.ID.setValue('RPO|1')

    self.obj81.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(269.0,212.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj82=hasObjective(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(False)

    # ID
    self.obj82.ID.setValue('RPO|2')

    self.obj82.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(106.0,313.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj90=hasObjective(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(False)

    # ID
    self.obj90.ID.setValue('RPO|3')

    self.obj90.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(463.939825541,233.509677008,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj72=precedentTo(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(True)

    # ID
    self.obj72.ID.setValue('OpO|0')

    self.obj72.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(238.433385235,390.958145418,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=precedentTo(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(True)

    # ID
    self.obj73.ID.setValue('OpO|1')

    self.obj73.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(361.5,338.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=precedentTo(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(True)

    # ID
    self.obj74.ID.setValue('OpO|2')

    self.obj74.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(475.153945772,289.77163693,self.obj74)
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

    self.obj75=precedentTo(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(True)

    # ID
    self.obj75.ID.setValue('OpO|3')

    self.obj75.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(595.497389922,188.902891196,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=precedentTo(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(True)

    # ID
    self.obj76.ID.setValue('OpO|4')

    self.obj76.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(716.684662394,87.746516207,self.obj76)
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

    # Connections for obj101 (graphObject_: Obj19) named talkToNPC
    self.drawConnections(
(self.obj101,self.obj82,[39.0, 341.0, 68.64406996010091, 317.77331026167, 106.0, 313.0],"true", 3) )
    # Connections for obj105 (graphObject_: Obj20) named move
    self.drawConnections(
(self.obj105,self.obj81,[151.0, 240.0, 212.30877292467923, 235.7298287540053, 269.0, 212.0],"true", 3) )
    # Connections for obj109 (graphObject_: Obj21) named equipItem
    self.drawConnections(
(self.obj109,self.obj80,[166.0, 341.0, 200.76028324415523, 332.76302793581885, 235.01028324415523, 334.51302793581885],"true", 3) )
    # Connections for obj83 (graphObject_: Obj28) named attack
    self.drawConnections(
(self.obj83,self.obj90,[384.0, 240.0, 424.189825540549, 231.7596770075297, 463.939825540549, 233.5096770075297],"true", 3) )
    # Connections for obj44 (graphObject_: Obj0) named FinishMaggots
    self.drawConnections(
 )
    # Connections for obj47 (graphObject_: Obj1) named talkToNPCTanisha
    self.drawConnections(
(self.obj47,self.obj71,[187.0, 449.0, 302.0, 433.0, 406.0, 543.0, 536.0, 538.0, 651.0, 540.0, 772.0, 542.0, 867.0, 313.0],"true", 7),
(self.obj47,self.obj72,[187.0, 449.0, 209.43338523505508, 416.2081454184791, 238.43338523505508, 390.9581454184791],"true", 3) )
    # Connections for obj50 (graphObject_: Obj2) named equipItemKnife
    self.drawConnections(
(self.obj50,self.obj71,[303.0, 348.0, 406.0, 442.0, 536.0, 437.0, 651.0, 439.0, 772.0, 441.0, 867.0, 313.0],"true", 6),
(self.obj50,self.obj73,[303.0, 348.0, 332.25, 338.0, 361.5, 338.0],"true", 3) )
    # Connections for obj55 (graphObject_: Obj3) named goToLocation10287
    self.drawConnections(
(self.obj55,self.obj71,[420.0, 348.0, 536.0, 336.0, 651.0, 338.0, 772.0, 340.0, 867.0, 313.0],"true", 5),
(self.obj55,self.obj74,[420.0, 348.0, 444.4039457720786, 315.02163693035317, 475.1539457720786, 289.77163693035317],"true", 3) )
    # Connections for obj58 (graphObject_: Obj4) named killMobMaggot10
    self.drawConnections(
(self.obj58,self.obj71,[543.0, 247.0, 651.0, 237.0, 772.0, 239.0, 867.0, 313.0],"true", 4),
(self.obj58,self.obj75,[543.0, 247.0, 565.9973899222056, 214.15289119624012, 595.4973899222056, 188.90289119624012],"true", 3) )
    # Connections for obj63 (graphObject_: Obj5) named goToNPCTanisha
    self.drawConnections(
(self.obj63,self.obj71,[661.0, 146.0, 772.0, 138.0, 867.0, 313.0],"true", 3),
(self.obj63,self.obj76,[661.0, 146.0, 685.684662394439, 112.99651620703398, 716.684662394439, 87.74651620703398],"true", 3) )
    # Connections for obj68 (graphObject_: Obj6) named talkToNPCTanisha
    self.drawConnections(
(self.obj68,self.obj71,[785.0, 45.0, 835.5624070856283, 176.07418887678537, 867.0, 313.0],"true", 3) )
    # Connections for obj71 (graphObject_: Obj7) of type isPartOfObjective
    self.drawConnections(
(self.obj71,self.obj44,[867.0, 313.0, 905.5764343181738, 321.60864189611954, 935.0, 348.0],"true", 3) )
    # Connections for obj80 (graphObject_: Obj22) of type hasObjective
    self.drawConnections(
(self.obj80,self.obj50,[235.01028324415523, 334.51302793581885, 269.26028324415523, 336.26302793581885, 303.0, 348.0],"true", 3) )
    # Connections for obj81 (graphObject_: Obj24) of type hasObjective
    self.drawConnections(
(self.obj81,self.obj55,[269.0, 212.0, 337.80763442571117, 287.43049413027654, 420.0, 348.0],"true", 3),
(self.obj81,self.obj63,[269.0, 212.0, 406.0, 139.0, 536.0, 134.0, 661.0, 146.0],"true", 4) )
    # Connections for obj82 (graphObject_: Obj26) of type hasObjective
    self.drawConnections(
(self.obj82,self.obj47,[106.0, 313.0, 155.09160638085427, 375.8829403172853, 187.0, 449.0],"true", 3),
(self.obj82,self.obj68,[106.0, 313.0, 174.0, 138.0, 302.0, 130.0, 406.0, 38.0, 536.0, 33.0, 651.0, 35.0, 785.0, 45.0],"true", 7) )
    # Connections for obj90 (graphObject_: Obj29) of type hasObjective
    self.drawConnections(
(self.obj90,self.obj58,[463.939825540549, 233.5096770075297, 503.689825540549, 235.2596770075297, 543.0, 247.0],"true", 3) )
    # Connections for obj72 (graphObject_: Obj9) of type precedentTo
    self.drawConnections(
(self.obj72,self.obj50,[238.43338523505508, 390.9581454184791, 267.4333852350551, 365.7081454184791, 303.0, 348.0],"true", 3) )
    # Connections for obj73 (graphObject_: Obj11) of type precedentTo
    self.drawConnections(
(self.obj73,self.obj55,[361.5, 338.0, 390.75, 338.0, 420.0, 348.0],"true", 3) )
    # Connections for obj74 (graphObject_: Obj13) of type precedentTo
    self.drawConnections(
(self.obj74,self.obj58,[475.1539457720786, 289.77163693035317, 505.9039457720786, 264.52163693035317, 543.0, 247.0],"true", 3) )
    # Connections for obj75 (graphObject_: Obj15) of type precedentTo
    self.drawConnections(
(self.obj75,self.obj63,[595.4973899222056, 188.90289119624012, 624.9973899222056, 163.65289119624012, 661.0, 146.0],"true", 3) )
    # Connections for obj76 (graphObject_: Obj17) of type precedentTo
    self.drawConnections(
(self.obj76,self.obj68,[716.684662394439, 87.74651620703398, 747.684662394439, 62.496516207033984, 785.0, 45.0],"true", 3) )

newfunction = TMWQuestsMaggotsActions_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
