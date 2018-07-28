"""
__TMWQuestsTutorialActions_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Tue May  1 04:16:31 2018
______________________________________________________________________________________
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

def TMWQuestsTutorialActions_MDL(self, rootNode, LSMASOMMRootNode=None):

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
       new_obj = graph_Action(0,707,self.obj101)
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
       new_obj = graph_Action(96,202,self.obj105)
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
       new_obj = graph_Action(758,808,self.obj109)
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
    self.obj44.ID.setValue('OTut0')

    # name
    self.obj44.name.setValue('FinishTutorial')

    self.obj44.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1703,1313,self.obj44)
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
    cobj2=ATOM3String('talkToNPC', 20)
    lcobj2.append(cobj2)
    self.obj48.ofActions.setValue(lcobj2)

    # Measurement
    self.obj48.Measurement.setValue('\n')
    self.obj48.Measurement.setHeight(4)

    # Reward
    self.obj48.Reward.setValue('\n')
    self.obj48.Reward.setHeight(4)

    # ID
    self.obj48.ID.setValue('OTut1')

    # name
    self.obj48.name.setValue('answerNPCServerInitial')

    self.obj48.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(154,909,self.obj48)
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
    self.obj49.ID.setValue('OTut2')

    # name
    self.obj49.name.setValue('goToNPCSorfina')

    self.obj49.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(311,606,self.obj49)
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
    cobj2=ATOM3String('talkToNPC', 20)
    lcobj2.append(cobj2)
    self.obj50.ofActions.setValue(lcobj2)

    # Measurement
    self.obj50.Measurement.setValue('\n')
    self.obj50.Measurement.setHeight(4)

    # Reward
    self.obj50.Reward.setValue('\n')
    self.obj50.Reward.setHeight(4)

    # ID
    self.obj50.ID.setValue('OTut3')

    # name
    self.obj50.name.setValue('talkToSorfina')

    self.obj50.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(427,707,self.obj50)
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
    cobj2=ATOM3String('move', 20)
    lcobj2.append(cobj2)
    self.obj51.ofActions.setValue(lcobj2)

    # Measurement
    self.obj51.Measurement.setValue('\n')
    self.obj51.Measurement.setHeight(4)

    # Reward
    self.obj51.Reward.setValue('\n')
    self.obj51.Reward.setHeight(4)

    # ID
    self.obj51.ID.setValue('OTut4')

    # name
    self.obj51.name.setValue('goToNPCCarpet')

    self.obj51.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(521,303,self.obj51)
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
    cobj2=ATOM3String('talkToNPC', 20)
    lcobj2.append(cobj2)
    self.obj52.ofActions.setValue(lcobj2)

    # Measurement
    self.obj52.Measurement.setValue('\n')
    self.obj52.Measurement.setHeight(4)

    # Reward
    self.obj52.Reward.setValue('\n')
    self.obj52.Reward.setHeight(4)

    # ID
    self.obj52.ID.setValue('OTut5')

    # name
    self.obj52.name.setValue('talkToNPCSorfina')

    self.obj52.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(635,505,self.obj52)
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
    self.obj63.ID.setValue('OTut6')

    # name
    self.obj63.name.setValue('goToLocation2924')

    self.obj63.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(758,202,self.obj63)
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

    self.obj64=Objective(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # description
    self.obj64.description.setValue('\n')
    self.obj64.description.setHeight(4)

    # ofActions
    self.obj64.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('talkToNPC', 20)
    lcobj2.append(cobj2)
    self.obj64.ofActions.setValue(lcobj2)

    # Measurement
    self.obj64.Measurement.setValue('\n')
    self.obj64.Measurement.setHeight(4)

    # Reward
    self.obj64.Reward.setValue('\n')
    self.obj64.Reward.setHeight(4)

    # ID
    self.obj64.ID.setValue('OTut7')

    # name
    self.obj64.name.setValue('talkToNPCDresser')

    self.obj64.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(881,606,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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
    self.obj65.description.setValue('\n')
    self.obj65.description.setHeight(4)

    # ofActions
    self.obj65.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('equipItem', 20)
    lcobj2.append(cobj2)
    self.obj65.ofActions.setValue(lcobj2)

    # Measurement
    self.obj65.Measurement.setValue('\n')
    self.obj65.Measurement.setHeight(4)

    # Reward
    self.obj65.Reward.setValue('\n')
    self.obj65.Reward.setHeight(4)

    # ID
    self.obj65.ID.setValue('OTut8')

    # name
    self.obj65.name.setValue('equipItemRaggedShorts')

    self.obj65.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1009,707,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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
    self.obj66.description.setValue('\n')
    self.obj66.description.setHeight(4)

    # ofActions
    self.obj66.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('equipItem', 20)
    lcobj2.append(cobj2)
    self.obj66.ofActions.setValue(lcobj2)

    # Measurement
    self.obj66.Measurement.setValue('\n')
    self.obj66.Measurement.setHeight(4)

    # Reward
    self.obj66.Reward.setValue('\n')
    self.obj66.Reward.setHeight(4)

    # ID
    self.obj66.ID.setValue('OTut9')

    # name
    self.obj66.name.setValue('equipItemCottonShirt')

    self.obj66.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1166,808,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj75=Objective(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # description
    self.obj75.description.setValue('\n')
    self.obj75.description.setHeight(4)

    # ofActions
    self.obj75.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj75.ofActions.setValue(lcobj2)

    # Measurement
    self.obj75.Measurement.setValue('\n')
    self.obj75.Measurement.setHeight(4)

    # Reward
    self.obj75.Reward.setValue('\n')
    self.obj75.Reward.setHeight(4)

    # ID
    self.obj75.ID.setValue('OTut10')

    # name
    self.obj75.name.setValue('equipItems')

    self.obj75.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1545,808,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj78=Objective(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # description
    self.obj78.description.setValue('\n')
    self.obj78.description.setHeight(4)

    # ofActions
    self.obj78.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('move', 20)
    lcobj2.append(cobj2)
    self.obj78.ofActions.setValue(lcobj2)

    # Measurement
    self.obj78.Measurement.setValue('\n')
    self.obj78.Measurement.setHeight(4)

    # Reward
    self.obj78.Reward.setValue('\n')
    self.obj78.Reward.setHeight(4)

    # ID
    self.obj78.ID.setValue('OTut11')

    # name
    self.obj78.name.setValue('goToNPCSorfina')

    self.obj78.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1306,404,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj81=Objective(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # description
    self.obj81.description.setValue('\n')
    self.obj81.description.setHeight(4)

    # ofActions
    self.obj81.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('talkToNPC', 20)
    lcobj2.append(cobj2)
    self.obj81.ofActions.setValue(lcobj2)

    # Measurement
    self.obj81.Measurement.setValue('\n')
    self.obj81.Measurement.setHeight(4)

    # Reward
    self.obj81.Reward.setValue('\n')
    self.obj81.Reward.setHeight(4)

    # ID
    self.obj81.ID.setValue('OTut12')

    # name
    self.obj81.name.setValue('talkToNPCSorfina')

    self.obj81.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1422,303,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    self.obj84=Objective(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(False)

    # description
    self.obj84.description.setValue('\n')
    self.obj84.description.setHeight(4)

    # ofActions
    self.obj84.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('move', 20)
    lcobj2.append(cobj2)
    self.obj84.ofActions.setValue(lcobj2)

    # Measurement
    self.obj84.Measurement.setValue('\n')
    self.obj84.Measurement.setHeight(4)

    # Reward
    self.obj84.Reward.setValue('\n')
    self.obj84.Reward.setHeight(4)

    # ID
    self.obj84.ID.setValue('OTut13')

    # name
    self.obj84.name.setValue('goToLocation4431')

    self.obj84.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1545,101,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj87=isPartOfObjective(self)
    self.obj87.isGraphObjectVisual = True

    if(hasattr(self.obj87, '_setHierarchicalLink')):
      self.obj87._setHierarchicalLink(True)

    # ID
    self.obj87.ID.setValue('pO|0')

    self.obj87.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(1432.0,818.0,self.obj87)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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

    # ID
    self.obj88.ID.setValue('pO|1')

    self.obj88.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(1678.0,515.0,self.obj88)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj88.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88, rootNode)
    self.obj88.postAction( rootNode.CREATE )

    self.obj104=hasObjective(self)
    self.obj104.isGraphObjectVisual = True

    if(hasattr(self.obj104, '_setHierarchicalLink')):
      self.obj104._setHierarchicalLink(False)

    # ID
    self.obj104.ID.setValue('RPO|4')

    self.obj104.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(106.0,717.0,self.obj104)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj104.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj104)
    self.globalAndLocalPostcondition(self.obj104, rootNode)
    self.obj104.postAction( rootNode.CREATE )

    self.obj108=hasObjective(self)
    self.obj108.isGraphObjectVisual = True

    if(hasattr(self.obj108, '_setHierarchicalLink')):
      self.obj108._setHierarchicalLink(False)

    # ID
    self.obj108.ID.setValue('RPO|5')

    self.obj108.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(164.0,212.0,self.obj108)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj108.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj108)
    self.globalAndLocalPostcondition(self.obj108, rootNode)
    self.obj108.postAction( rootNode.CREATE )

    self.obj112=hasObjective(self)
    self.obj112.isGraphObjectVisual = True

    if(hasattr(self.obj112, '_setHierarchicalLink')):
      self.obj112._setHierarchicalLink(False)

    # ID
    self.obj112.ID.setValue('RPO|6')

    self.obj112.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(891.0,818.0,self.obj112)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj112.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj112)
    self.globalAndLocalPostcondition(self.obj112, rootNode)
    self.obj112.postAction( rootNode.CREATE )

    self.obj89=precedentTo(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(True)

    # ID
    self.obj89.ID.setValue('OpO|0')

    self.obj89.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(283.884512801,798.436945736,self.obj89)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj89.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89, rootNode)
    self.obj89.postAction( rootNode.CREATE )

    self.obj90=precedentTo(self)
    self.obj90.isGraphObjectVisual = True

    if(hasattr(self.obj90, '_setHierarchicalLink')):
      self.obj90._setHierarchicalLink(True)

    # ID
    self.obj90.ID.setValue('OpO|1')

    self.obj90.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(420.268652489,694.074436196,self.obj90)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj90.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90, rootNode)
    self.obj90.postAction( rootNode.CREATE )

    self.obj91=precedentTo(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(True)

    # ID
    self.obj91.ID.setValue('OpO|2')

    self.obj91.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(508.537974386,547.508619444,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj92=precedentTo(self)
    self.obj92.isGraphObjectVisual = True

    if(hasattr(self.obj92, '_setHierarchicalLink')):
      self.obj92._setHierarchicalLink(True)

    # ID
    self.obj92.ID.setValue('OpO|3')

    self.obj92.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(638.081604689,444.243618021,self.obj92)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj92.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj92)
    self.globalAndLocalPostcondition(self.obj92, rootNode)
    self.obj92.postAction( rootNode.CREATE )

    self.obj93=precedentTo(self)
    self.obj93.isGraphObjectVisual = True

    if(hasattr(self.obj93, '_setHierarchicalLink')):
      self.obj93._setHierarchicalLink(True)

    # ID
    self.obj93.ID.setValue('OpO|4')

    self.obj93.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(741.190240587,394.7766602,self.obj93)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj93.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj93)
    self.globalAndLocalPostcondition(self.obj93, rootNode)
    self.obj93.postAction( rootNode.CREATE )

    self.obj94=precedentTo(self)
    self.obj94.isGraphObjectVisual = True

    if(hasattr(self.obj94, '_setHierarchicalLink')):
      self.obj94._setHierarchicalLink(True)

    # ID
    self.obj94.ID.setValue('OpO|5')

    self.obj94.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(884.035714723,446.228591438,self.obj94)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj94.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj94)
    self.globalAndLocalPostcondition(self.obj94, rootNode)
    self.obj94.postAction( rootNode.CREATE )

    self.obj95=precedentTo(self)
    self.obj95.isGraphObjectVisual = True

    if(hasattr(self.obj95, '_setHierarchicalLink')):
      self.obj95._setHierarchicalLink(True)

    # ID
    self.obj95.ID.setValue('OpO|6')

    self.obj95.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(1014.24475761,693.64559247,self.obj95)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj95.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj95)
    self.globalAndLocalPostcondition(self.obj95, rootNode)
    self.obj95.postAction( rootNode.CREATE )

    self.obj96=precedentTo(self)
    self.obj96.isGraphObjectVisual = True

    if(hasattr(self.obj96, '_setHierarchicalLink')):
      self.obj96._setHierarchicalLink(True)

    # ID
    self.obj96.ID.setValue('OpO|7')

    self.obj96.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(1159.65860933,794.451682873,self.obj96)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj96.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj96)
    self.globalAndLocalPostcondition(self.obj96, rootNode)
    self.obj96.postAction( rootNode.CREATE )

    self.obj97=precedentTo(self)
    self.obj97.isGraphObjectVisual = True

    if(hasattr(self.obj97, '_setHierarchicalLink')):
      self.obj97._setHierarchicalLink(True)

    # ID
    self.obj97.ID.setValue('OpO|8')

    self.obj97.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(1282.01861605,647.816387842,self.obj97)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj97.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj97)
    self.globalAndLocalPostcondition(self.obj97, rootNode)
    self.obj97.postAction( rootNode.CREATE )

    self.obj98=precedentTo(self)
    self.obj98.isGraphObjectVisual = True

    if(hasattr(self.obj98, '_setHierarchicalLink')):
      self.obj98._setHierarchicalLink(True)

    # ID
    self.obj98.ID.setValue('OpO|9')

    self.obj98.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(1409.23224683,390.796493523,self.obj98)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj98.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj98)
    self.globalAndLocalPostcondition(self.obj98, rootNode)
    self.obj98.postAction( rootNode.CREATE )

    self.obj99=precedentTo(self)
    self.obj99.isGraphObjectVisual = True

    if(hasattr(self.obj99, '_setHierarchicalLink')):
      self.obj99._setHierarchicalLink(True)

    # ID
    self.obj99.ID.setValue('OpO|10')

    self.obj99.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(1528.60777078,241.889920826,self.obj99)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj99.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj99)
    self.globalAndLocalPostcondition(self.obj99, rootNode)
    self.obj99.postAction( rootNode.CREATE )

    # Connections for obj101 (graphObject_: Obj40) named talkToNPC
    self.drawConnections(
(self.obj101,self.obj104,[39.0, 745.0, 76.35593003989909, 740.2266897383299, 106.0, 717.0],"true", 3) )
    # Connections for obj105 (graphObject_: Obj43) named move
    self.drawConnections(
(self.obj105,self.obj108,[116.0, 240.0, 134.96128974475914, 217.36221099101567, 164.0, 212.0],"true", 3) )
    # Connections for obj109 (graphObject_: Obj46) named equipItem
    self.drawConnections(
(self.obj109,self.obj112,[793.0, 846.0, 844.7472112789737, 841.6152394764082, 891.0, 818.0],"true", 3) )
    # Connections for obj44 (graphObject_: Obj0) named FinishTutorial
    self.drawConnections(
 )
    # Connections for obj48 (graphObject_: Obj1) named answerNPCServerInitial
    self.drawConnections(
(self.obj48,self.obj88,[71.3730502873575, 1156.0302404320985, 1588.0, 1046.0, 1311.0, 1147.0, 1195.0, 1144.0, 1055.0, 1152.0, 898.0, 1158.0, 770.0, 1148.0, 647.0, 1147.0, 524.0, 1147.0, 410.0, 1144.0, 316.0, 1137.0, 200.0, 1144.0, 1524.0, 616.0],"true", 13),
(self.obj48,self.obj89,[71.3730502873575, 1156.0302404320985, 250.063108047452, 823.6953032316818, 133.03220061434104, 1097.5012958616283],"true", 3) )
    # Connections for obj49 (graphObject_: Obj2) named goToNPCSorfina
    self.drawConnections(
(self.obj49,self.obj88,[360.6586693012722, 852.996810448074, 1588.0, 945.0, 1311.0, 1046.0, 1195.0, 1043.0, 1055.0, 1051.0, 898.0, 1057.0, 770.0, 1047.0, 647.0, 1046.0, 524.0, 1046.0, 410.0, 1043.0, 316.0, 1036.0, 1524.0, 616.0],"true", 12),
(self.obj49,self.obj90,[360.6586693012722, 852.996810448074, 393.9160987849229, 719.4189020696183, 252.43191195176954, 997.1002958217343],"true", 3) )
    # Connections for obj50 (graphObject_: Obj3) named talkToSorfina
    self.drawConnections(
(self.obj50,self.obj88,[620.0688841195108, 347.61894695485444, 1588.0, 844.0, 1311.0, 945.0, 1195.0, 942.0, 1055.0, 950.0, 898.0, 956.0, 770.0, 946.0, 647.0, 945.0, 524.0, 945.0, 410.0, 942.0, 1524.0, 616.0],"true", 11),
(self.obj50,self.obj91,[620.0688841195108, 347.61894695485444, 482.4627584189369, 572.5616227149533, 357.2910055298654, 896.3019409478243],"true", 3) )
    # Connections for obj51 (graphObject_: Obj4) named goToNPCCarpet
    self.drawConnections(
(self.obj51,self.obj88,[878.3697479874695, 45.40693387134888, 1588.0, 743.0, 1311.0, 844.0, 1195.0, 841.0, 1055.0, 849.0, 898.0, 855.0, 770.0, 845.0, 647.0, 844.0, 524.0, 844.0, 1524.0, 616.0],"true", 10),
(self.obj51,self.obj92,[878.3697479874695, 45.40693387134888, 608.5402816870514, 469.5485823188148, 468.94687695967264, 795.20238559134],"true", 3) )
    # Connections for obj52 (graphObject_: Obj5) named talkToNPCSorfina
    self.drawConnections(
(self.obj52,self.obj88,[1150.5350399968538, -560.8129233212753, 1588.0, 642.0, 1311.0, 743.0, 1195.0, 740.0, 1055.0, 748.0, 898.0, 754.0, 770.0, 744.0, 647.0, 743.0, 1524.0, 616.0],"true", 9),
(self.obj52,self.obj93,[1150.5350399968538, -560.8129233212753, 710.2336508811486, 420.09177398760244, 590.1177897541593, 693.8156824991034],"true", 3) )
    # Connections for obj63 (graphObject_: Obj6) named goToLocation2924
    self.drawConnections(
(self.obj63,self.obj88,[1428.3613988186144, -864.0733784711929, 1588.0, 541.0, 1311.0, 642.0, 1195.0, 639.0, 1055.0, 647.0, 898.0, 653.0, 770.0, 643.0, 1524.0, 616.0],"true", 8),
(self.obj63,self.obj94,[1428.3613988186144, -864.0733784711929, 852.9781954529379, 471.3595962429283, 714.1860877509465, 592.8908418037036],"true", 3) )
    # Connections for obj64 (graphObject_: Obj7) named talkToNPCDresser
    self.drawConnections(
(self.obj64,self.obj88,[1706.5914758976514, -1368.59739768902, 1588.0, 440.0, 1311.0, 541.0, 1195.0, 538.0, 1055.0, 546.0, 898.0, 552.0, 1524.0, 616.0],"true", 7),
(self.obj64,self.obj95,[1706.5914758976514, -1368.59739768902, 978.2889516774572, 718.9304062872477, 848.7508045179128, 491.6530457392652],"true", 3) )
    # Connections for obj65 (graphObject_: Obj8) named equipItemRaggedShorts
    self.drawConnections(
(self.obj65,self.obj87,[2004.4146996376899, -1368.736652958427, 1349.0, 841.0, 1055.0, 445.0, 1278.0, 414.0],"true", 4),
(self.obj65,self.obj96,[2004.4146996376899, -1368.736652958427, 1122.8633375394077, 819.7332134534054, 994.3422700382985, 390.4582755166509],"true", 3) )
    # Connections for obj66 (graphObject_: Obj9) named equipItemCottonShirt
    self.drawConnections(
(self.obj66,self.obj87,[2305.595786786461, -1166.8627752811449, 1349.0, 740.0, 1278.0, 414.0],"true", 3),
(self.obj66,self.obj97,[2305.595786786461, -1166.8627752811449, 1250.039771748176, 673.2196187213889, 1131.3334127734379, 289.5006402903139],"true", 3) )
    # Connections for obj75 (graphObject_: Obj10) named equipItems
    self.drawConnections(
(self.obj75,self.obj88,[2656.0427765396694, -1065.8620741908562, 1619.4428316526357, 436.707870022385, 1524.0, 616.0],"true", 3) )
    # Connections for obj78 (graphObject_: Obj11) named goToNPCSorfina
    self.drawConnections(
(self.obj78,self.obj88,[2587.5111639959364, -763.4756987977307, 1588.0, 137.0, 1311.0, 238.0, 1524.0, 616.0],"true", 4),
(self.obj78,self.obj98,[2587.5111639959364, -763.4756987977307, 1379.172928243175, 415.81750461994136, 1255.2322468257944, 188.79649352290025],"true", 3) )
    # Connections for obj81 (graphObject_: Obj12) named talkToNPCSorfina
    self.drawConnections(
(self.obj81,self.obj88,[2861.7484383264145, -661.5597431858951, 1588.0, 36.0, 1524.0, 616.0],"true", 3),
(self.obj81,self.obj99,[2861.7484383264145, -661.5597431858951, 1497.9016773658216, 267.3243031241967, 1376.781607904176, 87.87031445137387],"true", 3) )
    # Connections for obj84 (graphObject_: Obj13) named goToLocation4431
    self.drawConnections(
(self.obj84,self.obj88,[3138.5728119741234, -561.2972723805888, 1628.3816731543677, 230.72841410397757, 1524.0, 616.0],"true", 3) )
    # Connections for obj87 (graphObject_: Obj14) of type isPartOfObjective
    self.drawConnections(
(self.obj87,self.obj75,[1278.0, 414.0, 1348.682141177642, 441.2915100523963, 2656.0427765396694, -1065.8620741908562],"true", 3) )
    # Connections for obj88 (graphObject_: Obj16) of type isPartOfObjective
    self.drawConnections(
(self.obj88,self.obj44,[1524.0, 616.0, 1551.718465689899, 642.3619287727334, 1742.9521122680558, 449.13234445921603],"true", 3) )
    # Connections for obj104 (graphObject_: Obj41) of type hasObjective
    self.drawConnections(
(self.obj104,self.obj50,[106.0, 717.0, 354.0, 740.0, 197.0, 754.0, 466.0688841195108, 751.6189469548544],"true", 4),
(self.obj104,self.obj48,[106.0, 717.0, 156.75522134995927, 840.0130989336836, 225.3730502873575, 954.0302404320985],"true", 3),
(self.obj104,self.obj52,[106.0, 717.0, 564.0, 538.0, 470.0, 531.0, 354.0, 538.0, 197.0, 653.0, 688.5350399968538, 550.1870766787247],"true", 6),
(self.obj104,self.obj64,[106.0, 717.0, 801.0, 743.0, 678.0, 844.0, 564.0, 841.0, 470.0, 834.0, 354.0, 841.0, 197.0, 855.0, 936.5914758976514, 651.40260231098],"true", 8),
(self.obj104,self.obj81,[106.0, 717.0, 1349.0, 336.0, 1209.0, 445.0, 1052.0, 451.0, 924.0, 441.0, 801.0, 440.0, 678.0, 440.0, 564.0, 437.0, 470.0, 430.0, 354.0, 437.0, 197.0, 552.0, 1475.7484383264145, 348.44025681410494],"true", 12) )
    # Connections for obj108 (graphObject_: Obj44) of type hasObjective
    self.drawConnections(
(self.obj108,self.obj49,[164.0, 212.0, 271.45545967940393, 427.41014863237143, 360.6586693012722, 650.996810448074],"true", 3),
(self.obj108,self.obj51,[164.0, 212.0, 470.0, 329.0, 354.0, 336.0, 570.3697479874695, 348.4069338713489],"true", 4),
(self.obj108,self.obj63,[164.0, 212.0, 678.0, 238.0, 564.0, 235.0, 470.0, 228.0, 354.0, 235.0, 812.3613988186144, 246.92662152880712],"true", 6),
(self.obj108,self.obj78,[164.0, 212.0, 1209.0, 142.0, 1052.0, 148.0, 924.0, 138.0, 801.0, 137.0, 678.0, 137.0, 564.0, 134.0, 470.0, 127.0, 354.0, 134.0, 1355.5111639959364, 448.52430120226927],"true", 10),
(self.obj108,self.obj84,[164.0, 212.0, 1465.0, 36.0, 1349.0, 33.0, 1209.0, 41.0, 1052.0, 47.0, 924.0, 37.0, 801.0, 36.0, 678.0, 36.0, 564.0, 33.0, 470.0, 26.0, 354.0, 33.0, 1598.5728119741234, 145.70272761941123],"true", 12) )
    # Connections for obj112 (graphObject_: Obj47) of type hasObjective
    self.drawConnections(
(self.obj112,self.obj65,[891.0, 818.0, 988.9860272278835, 794.5789098599208, 1080.4146996376899, 752.2633470415731],"true", 3),
(self.obj112,self.obj66,[891.0, 818.0, 1052.0, 855.0, 1227.5957867864608, 853.1372247188551],"true", 3) )
    # Connections for obj89 (graphObject_: Obj18) of type precedentTo
    self.drawConnections(
(self.obj89,self.obj49,[133.03220061434104, 1097.5012958616283, 166.8536053678197, 1072.2429383656222, 360.6586693012722, 852.996810448074],"true", 3) )
    # Connections for obj90 (graphObject_: Obj20) of type precedentTo
    self.drawConnections(
(self.obj90,self.obj50,[252.43191195176954, 997.1002958217343, 278.7844656563292, 971.7558299484294, 620.0688841195108, 347.61894695485444],"true", 3) )
    # Connections for obj91 (graphObject_: Obj22) of type precedentTo
    self.drawConnections(
(self.obj91,self.obj51,[357.2910055298654, 896.3019409478243, 383.3662214968551, 871.2489376769479, 878.3697479874695, 45.40693387134888],"true", 3) )
    # Connections for obj92 (graphObject_: Obj24) of type precedentTo
    self.drawConnections(
(self.obj92,self.obj52,[468.94687695967264, 795.20238559134, 498.4881999620187, 769.8974212931839, 1150.5350399968538, -560.8129233212753],"true", 3) )
    # Connections for obj93 (graphObject_: Obj26) of type precedentTo
    self.drawConnections(
(self.obj93,self.obj63,[590.1177897541593, 693.8156824991034, 621.0743794595994, 668.500568711624, 1428.3613988186144, -864.0733784711929],"true", 3) )
    # Connections for obj94 (graphObject_: Obj28) of type precedentTo
    self.drawConnections(
(self.obj94,self.obj64,[714.1860877509465, 592.8908418037036, 745.2436070207058, 567.7598369992468, 1706.5914758976514, -1368.59739768902],"true", 3) )
    # Connections for obj95 (graphObject_: Obj30) of type precedentTo
    self.drawConnections(
(self.obj95,self.obj65,[848.7508045179128, 491.6530457392652, 884.7066104529224, 466.3682319219135, 2004.4146996376899, -1368.736652958427],"true", 3) )
    # Connections for obj96 (graphObject_: Obj32) of type precedentTo
    self.drawConnections(
(self.obj96,self.obj66,[994.3422700382985, 390.4582755166509, 1031.1375418254913, 365.1767449359714, 2305.595786786461, -1166.8627752811449],"true", 3) )
    # Connections for obj97 (graphObject_: Obj34) of type precedentTo
    self.drawConnections(
(self.obj97,self.obj78,[1131.3334127734379, 289.5006402903139, 1163.3122570758067, 264.09740941116746, 2587.5111639959364, -763.4756987977307],"true", 3) )
    # Connections for obj98 (graphObject_: Obj36) of type precedentTo
    self.drawConnections(
(self.obj98,self.obj81,[1255.2322468257944, 188.79649352290025, 1285.2915654084138, 163.77548242585917, 2861.7484383264145, -661.5597431858951],"true", 3) )
    # Connections for obj99 (graphObject_: Obj38) of type precedentTo
    self.drawConnections(
(self.obj99,self.obj84,[1376.781607904176, 87.87031445137387, 1407.4877013161033, 62.43593215270044, 3138.5728119741234, -561.2972723805888],"true", 3) )

newfunction = TMWQuestsTutorialActions_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
