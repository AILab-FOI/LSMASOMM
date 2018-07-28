"""
__recipeWorldNew_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Sun Apr 15 00:57:44 2018
____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from Action import *
from Objective import *
from canHaveRole import *
from hasActions import *
from isPartOfObjective import *
from hasObjective import *
from precedentTo import *
from graph_canHaveRole import *
from graph_Action import *
from graph_precedentTo import *
from graph_isPartOfObjective import *
from graph_hasObjective import *
from graph_Role import *
from graph_Objective import *
from graph_OrgUnit import *
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

def recipeWorldNew_MDL(self, rootNode, LSMASOMMRootNode=None):

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
        LSMASOMMRootNode.name.setValue('recipeWorldNew')

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
    self.obj44.name.setValue('SimpleUnit')

    # UnitSize
    self.obj44.UnitSize.setValue('Individual')

    self.obj44.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(442,0,self.obj44)
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

    self.obj45=Role(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # isMetaRole
    self.obj45.isMetaRole.setValue((None, 0))
    self.obj45.isMetaRole.config = 0

    # hasActions
    self.obj45.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('SearchForFactories', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('CheckFactoryAvailability', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('WaitForFactoryAnswer', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('StartProduction', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('FinishProduction', 20)
    lcobj2.append(cobj2)
    self.obj45.hasActions.setValue(lcobj2)

    # ID
    self.obj45.ID.setValue('R|0')

    # name
    self.obj45.name.setValue('Order')

    self.obj45.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(296,203,self.obj45)
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
    cobj2=ATOM3String('AnswerQuery', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Produce', 20)
    lcobj2.append(cobj2)
    self.obj46.hasActions.setValue(lcobj2)

    # ID
    self.obj46.ID.setValue('R|1')

    # name
    self.obj46.name.setValue('Factory')

    self.obj46.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(816,203,self.obj46)
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

    self.obj47=Action(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # ID
    self.obj47.ID.setValue('A|0')

    # name
    self.obj47.name.setValue('SearchForFactories')

    # ActionCode
    self.obj47.ActionCode.setValue('#action code template\nclass SearchForFactories(spade.Behaviour.OneShotBehaviour):\n    """Search for factories and their services"""\n    def onStart(self):\n        if not self.myAgent.startProductionFlag and not self.myAgent.finishProductionFlag:\n            self.myAgent.possibleFactories = {}\n\n            s = spade.DF.Service(\n                name="Service{}".format(\n                    self.myAgent.recipe[-1][\'value\']))\n            search = self.myAgent.searchService(s)\n\n            self.myAgent.possibleFactories = {x.getOwner().getName(): x.getName() for x in search}\n            if self.myAgent.triedFactories:\n                try:\n                    for f in self.myAgent.triedFactories:\n                        del self.myAgent.possibleFactories[f]\n                except Exception as e:\n                    print e\n\n                say("{}: Already tried {}".format(\n                    self.myAgent.getName(),\n                    self.myAgent.triedFactories))\n\n            say("{}: Considered factories are {} ({}, {})".format(\n                   self.myAgent.getName(),\n                   self.myAgent.possibleFactories,\n                   self.myAgent.finishProductionFlag,\n                   self.myAgent.startProductionFlag))\n\n        if self.myAgent.finishProductionFlag:\n            self._exitcode = self.myAgent.transition2To4\n        elif self.myAgent.startProductionFlag:\n            self._exitcode = self.myAgent.transition2To5\n        else:\n            self._exitcode = self.myAgent.transition2To3\n\n    def _process(self):\n        pass\n')
    self.obj47.ActionCode.setHeight(45)

    self.obj47.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(0,427,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=Action(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # ID
    self.obj48.ID.setValue('A|1')

    # name
    self.obj48.name.setValue('CheckFactoryAvailability')

    # ActionCode
    self.obj48.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj48.ActionCode.setHeight(15)

    self.obj48.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(143,427,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=Action(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # ID
    self.obj49.ID.setValue('A|2')

    # name
    self.obj49.name.setValue('WaitForFactoryAnswer')

    # ActionCode
    self.obj49.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj49.ActionCode.setHeight(15)

    self.obj49.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(322,427,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj50=Action(self)
    self.obj50.isGraphObjectVisual = True

    if(hasattr(self.obj50, '_setHierarchicalLink')):
      self.obj50._setHierarchicalLink(False)

    # ID
    self.obj50.ID.setValue('A|3')

    # name
    self.obj50.name.setValue('StartProduction')

    # ActionCode
    self.obj50.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj50.ActionCode.setHeight(15)

    self.obj50.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(488,427,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj50.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.obj50.postAction( rootNode.CREATE )

    self.obj51=Action(self)
    self.obj51.isGraphObjectVisual = True

    if(hasattr(self.obj51, '_setHierarchicalLink')):
      self.obj51._setHierarchicalLink(False)

    # ID
    self.obj51.ID.setValue('A|4')

    # name
    self.obj51.name.setValue('FinishProduction')

    # ActionCode
    self.obj51.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj51.ActionCode.setHeight(15)

    self.obj51.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(612,427,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj51.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)
    self.obj51.postAction( rootNode.CREATE )

    self.obj52=Action(self)
    self.obj52.isGraphObjectVisual = True

    if(hasattr(self.obj52, '_setHierarchicalLink')):
      self.obj52._setHierarchicalLink(False)

    # ID
    self.obj52.ID.setValue('A|5')

    # name
    self.obj52.name.setValue('AnswerQuery')

    # ActionCode
    self.obj52.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj52.ActionCode.setHeight(15)

    self.obj52.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(761,385,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj52.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)
    self.obj52.postAction( rootNode.CREATE )

    self.obj53=Action(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # ID
    self.obj53.ID.setValue('A|6')

    # name
    self.obj53.name.setValue('Produce')

    # ActionCode
    self.obj53.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj53.ActionCode.setHeight(15)

    self.obj53.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(902,385,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj53.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)
    self.obj53.postAction( rootNode.CREATE )

    self.obj54=Objective(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # description
    self.obj54.description.setValue('\n')
    self.obj54.description.setHeight(4)

    # ofActions
    self.obj54.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj54.ofActions.setValue(lcobj2)

    # Measurement
    self.obj54.Measurement.setValue('\n')
    self.obj54.Measurement.setHeight(4)

    # Reward
    self.obj54.Reward.setValue('\n')
    self.obj54.Reward.setHeight(4)

    # ID
    self.obj54.ID.setValue('O|0')

    # name
    self.obj54.name.setValue('ProduceRecipePart')

    self.obj54.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(492,674,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

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
    self.obj55.ofActions.setValue(lcobj2)

    # Measurement
    self.obj55.Measurement.setValue('\n')
    self.obj55.Measurement.setHeight(4)

    # Reward
    self.obj55.Reward.setValue('\n')
    self.obj55.Reward.setHeight(4)

    # ID
    self.obj55.ID.setValue('O|1')

    # name
    self.obj55.name.setValue('SelectFactory')

    self.obj55.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(5,674,self.obj55)
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

    self.obj56=Objective(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # description
    self.obj56.description.setValue('\n')
    self.obj56.description.setHeight(4)

    # ofActions
    self.obj56.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('StartProduction', 20)
    lcobj2.append(cobj2)
    self.obj56.ofActions.setValue(lcobj2)

    # Measurement
    self.obj56.Measurement.setValue('\n')
    self.obj56.Measurement.setHeight(4)

    # Reward
    self.obj56.Reward.setValue('\n')
    self.obj56.Reward.setHeight(4)

    # ID
    self.obj56.ID.setValue('O|2')

    # name
    self.obj56.name.setValue('ProductionStarted')

    self.obj56.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(491,528,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=Objective(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # description
    self.obj57.description.setValue('\n')
    self.obj57.description.setHeight(4)

    # ofActions
    self.obj57.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('FinishProduction', 20)
    lcobj2.append(cobj2)
    self.obj57.ofActions.setValue(lcobj2)

    # Measurement
    self.obj57.Measurement.setValue('\n')
    self.obj57.Measurement.setHeight(4)

    # Reward
    self.obj57.Reward.setValue('\n')
    self.obj57.Reward.setHeight(4)

    # ID
    self.obj57.ID.setValue('O|3')

    # name
    self.obj57.name.setValue('ProductionFinished')

    self.obj57.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(617,528,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

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
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('SearchForFactories', 20)
    lcobj2.append(cobj2)
    self.obj58.ofActions.setValue(lcobj2)

    # Measurement
    self.obj58.Measurement.setValue('\n')
    self.obj58.Measurement.setHeight(4)

    # Reward
    self.obj58.Reward.setValue('\n')
    self.obj58.Reward.setHeight(4)

    # ID
    self.obj58.ID.setValue('O|4')

    # name
    self.obj58.name.setValue('SearchSuitableFactories')

    self.obj58.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(0,528,self.obj58)
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

    self.obj59=Objective(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # description
    self.obj59.description.setValue('\n')
    self.obj59.description.setHeight(4)

    # ofActions
    self.obj59.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('CheckFactoryAvailability', 20)
    lcobj2.append(cobj2)
    self.obj59.ofActions.setValue(lcobj2)

    # Measurement
    self.obj59.Measurement.setValue('\n')
    self.obj59.Measurement.setHeight(4)

    # Reward
    self.obj59.Reward.setValue('\n')
    self.obj59.Reward.setHeight(4)

    # ID
    self.obj59.ID.setValue('O|5')

    # name
    self.obj59.name.setValue('CheckIfFactoryAvailable')

    self.obj59.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(148,528,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=Objective(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # description
    self.obj60.description.setValue('\n')
    self.obj60.description.setHeight(4)

    # ofActions
    self.obj60.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('WaitForFactoryAnswer', 20)
    lcobj2.append(cobj2)
    self.obj60.ofActions.setValue(lcobj2)

    # Measurement
    self.obj60.Measurement.setValue('\n')
    self.obj60.Measurement.setHeight(4)

    # Reward
    self.obj60.Reward.setValue('\n')
    self.obj60.Reward.setHeight(4)

    # ID
    self.obj60.ID.setValue('O|6')

    # name
    self.obj60.name.setValue('ReceiveAnswer')

    self.obj60.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(327,528,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=Objective(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # description
    self.obj61.description.setValue('\n')
    self.obj61.description.setHeight(4)

    # ofActions
    self.obj61.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj61.ofActions.setValue(lcobj2)

    # Measurement
    self.obj61.Measurement.setValue('\n')
    self.obj61.Measurement.setHeight(4)

    # Reward
    self.obj61.Reward.setValue('\n')
    self.obj61.Reward.setHeight(4)

    # ID
    self.obj61.ID.setValue('O|7')

    # name
    self.obj61.name.setValue('ProduceSingleRecipePart')

    self.obj61.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(740,632,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=Objective(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # description
    self.obj62.description.setValue('\n')
    self.obj62.description.setHeight(4)

    # ofActions
    self.obj62.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('AnswerQuery', 20)
    lcobj2.append(cobj2)
    self.obj62.ofActions.setValue(lcobj2)

    # Measurement
    self.obj62.Measurement.setValue('\n')
    self.obj62.Measurement.setHeight(4)

    # Reward
    self.obj62.Reward.setValue('\n')
    self.obj62.Reward.setHeight(4)

    # ID
    self.obj62.ID.setValue('O|8')

    # name
    self.obj62.name.setValue('ReplyToOrder')

    self.obj62.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(769,486,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
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
    self.obj63.description.setValue('\n')
    self.obj63.description.setHeight(4)

    # ofActions
    self.obj63.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ActionName', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Produce', 20)
    lcobj2.append(cobj2)
    self.obj63.ofActions.setValue(lcobj2)

    # Measurement
    self.obj63.Measurement.setValue('\n')
    self.obj63.Measurement.setHeight(4)

    # Reward
    self.obj63.Reward.setValue('\n')
    self.obj63.Reward.setHeight(4)

    # ID
    self.obj63.ID.setValue('O|9')

    # name
    self.obj63.name.setValue('ProducePart')

    self.obj63.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(901,486,self.obj63)
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

    self.obj64=canHaveRole(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(True)

    # ID
    self.obj64.ID.setValue('OUR|0')

    self.obj64.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(484.0,151.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=hasActions(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # ID
    self.obj65.ID.setValue('aR|0')

    self.obj65.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(362.0,392.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=hasActions(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # ID
    self.obj66.ID.setValue('aR|1')

    self.obj66.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(852.0,350.0,self.obj66)
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

    self.obj67=isPartOfObjective(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(True)

    # ID
    self.obj67.ID.setValue('pO|0')

    self.obj67.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(544.0,644.0,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=isPartOfObjective(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(True)

    # ID
    self.obj68.ID.setValue('pO|1')

    self.obj68.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(41.0,644.0,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=isPartOfObjective(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(True)

    # ID
    self.obj69.ID.setValue('pO|2')

    self.obj69.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(810.0,602.0,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj69.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj69)
    self.globalAndLocalPostcondition(self.obj69, rootNode)
    self.obj69.postAction( rootNode.CREATE )

    self.obj70=hasObjective(self)
    self.obj70.isGraphObjectVisual = True

    if(hasattr(self.obj70, '_setHierarchicalLink')):
      self.obj70._setHierarchicalLink(False)

    # ID
    self.obj70.ID.setValue('RPO|0')

    self.obj70.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(90.9965715265,518.62969312,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj70.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj70)
    self.globalAndLocalPostcondition(self.obj70, rootNode)
    self.obj70.postAction( rootNode.CREATE )

    self.obj71=hasObjective(self)
    self.obj71.isGraphObjectVisual = True

    if(hasattr(self.obj71, '_setHierarchicalLink')):
      self.obj71._setHierarchicalLink(False)

    # ID
    self.obj71.ID.setValue('RPO|1')

    self.obj71.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(245.397062206,521.026552632,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=hasObjective(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    # ID
    self.obj72.ID.setValue('RPO|2')

    self.obj72.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(407.815764559,524.186640483,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=hasObjective(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # ID
    self.obj73.ID.setValue('RPO|3')

    self.obj73.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(563.499142716,518.814822753,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=hasObjective(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # ID
    self.obj74.ID.setValue('RPO|4')

    self.obj74.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(692.499142716,518.814822753,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=hasObjective(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # ID
    self.obj75.ID.setValue('RPO|5')

    self.obj75.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(829.499142716,476.814822753,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=hasObjective(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # ID
    self.obj76.ID.setValue('RPO|6')

    self.obj76.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(954.969207064,475.890599608,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
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
    self.obj77.ID.setValue('OpO|0')

    self.obj77.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(608.5,553.0,self.obj77)
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
    self.obj78.ID.setValue('OpO|1')

    self.obj78.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(146.0,553.0,self.obj78)
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
    self.obj79.ID.setValue('OpO|2')

    self.obj79.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(297.0,553.0,self.obj79)
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

    self.obj80=precedentTo(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(True)

    # ID
    self.obj80.ID.setValue('OpO|3')

    self.obj80.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(289.373367524,626.807787856,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("precedentTo", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj81=precedentTo(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(True)

    # ID
    self.obj81.ID.setValue('OpO|4')

    self.obj81.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(874.0,511.0,self.obj81)
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

    # Connections for obj44 (graphObject_: Obj0) named SimpleUnit
    self.drawConnections(
(self.obj44,self.obj64,[779.0, 63.0, 471.52714344810283, 108.59802068964474, 774.0, 146.0],"true", 3) )
    # Connections for obj45 (graphObject_: Obj1) named Order
    self.drawConnections(
(self.obj45,self.obj65,[507.1674107207881, 245.34828460519736, 401.9561258922564, 331.4978677757374, 769.0, 377.0],"true", 3) )
    # Connections for obj46 (graphObject_: Obj2) named Factory
    self.drawConnections(
(self.obj46,self.obj66,[666.1674107207882, 245.34828460519736, 877.7959088574821, 286.46598480958033, 958.0, 377.0],"true", 3) )
    # Connections for obj47 (graphObject_: Obj3) named SearchForFactories
    self.drawConnections(
(self.obj47,self.obj70,[826.0, 445.0, 90.4965715261315, 492.87969311996744, 841.9971730116598, 496.20879275705516],"true", 3) )
    # Connections for obj48 (graphObject_: Obj4) named CheckFactoryAvailability
    self.drawConnections(
(self.obj48,self.obj71,[655.0, 445.0, 246.19706220578408, 510.8265526319616, 655.0999999999999, 532.5999999999999],"true", 3) )
    # Connections for obj49 (graphObject_: Obj5) named WaitForFactoryAnswer
    self.drawConnections(
(self.obj49,self.obj72,[459.0, 445.0, 407.81576455901285, 474.18664048361734, 467.0, 581.0],"true", 3) )
    # Connections for obj50 (graphObject_: Obj6) named StartProduction
    self.drawConnections(
(self.obj50,self.obj73,[244.0, 445.0, 278.16683142430304, 734.0461019976268, 278.0, 632.0, 563.3323112922214, 265.7687207547202, 278.0, 783.0],"true", 5) )
    # Connections for obj51 (graphObject_: Obj7) named FinishProduction
    self.drawConnections(
(self.obj51,self.obj74,[60.0, 445.0, 88.735427443303, 734.0682218236268, 89.0, 632.0, 692.7637152727834, 265.74660092913484, 89.0, 783.0],"true", 5) )
    # Connections for obj52 (graphObject_: Obj8) named AnswerQuery
    self.drawConnections(
(self.obj52,self.obj75,[1182.0, 445.0, 831.2491427124538, 451.0648227525632, 1193.4654791360715, 497.5170713975971],"true", 3) )
    # Connections for obj53 (graphObject_: Obj9) named Produce
    self.drawConnections(
(self.obj53,self.obj76,[975.0, 445.0, 954.6192070644487, 465.6905996078802, 1028.4499999999998, 532.5999999999999],"true", 3) )
    # Connections for obj54 (graphObject_: Obj10) named ProduceRecipePart
    self.drawConnections(
 )
    # Connections for obj55 (graphObject_: Obj11) named SelectFactory
    self.drawConnections(
(self.obj55,self.obj67,[608.0, 952.0, 656.0, 1138.0, 812.0, 459.0, 388.0, 1220.0],"true", 4),
(self.obj55,self.obj80,[608.0, 952.0, 333.6233675241962, 601.5577878547101, 526.9341559502739, 1015.5281742890938],"true", 3) )
    # Connections for obj56 (graphObject_: Obj12) named ProductionStarted
    self.drawConnections(
(self.obj56,self.obj67,[-130.8660993239755, 819.5505071588908, 623.0, 561.0, 388.0, 1220.0],"true", 3),
(self.obj56,self.obj77,[-130.8660993239755, 819.5505071588908, 654.9999999999543, 527.750000003403, 345.157941874857, 1116.6819523635982],"true", 3) )
    # Connections for obj57 (graphObject_: Obj13) named ProductionFinished
    self.drawConnections(
(self.obj57,self.obj67,[-204.41814550765912, 441.1089149235471, 478.7858726619261, 597.3806092324933, 388.0, 1220.0],"true", 3) )
    # Connections for obj58 (graphObject_: Obj14) named SearchSuitableFactories
    self.drawConnections(
(self.obj58,self.obj68,[828.0, 548.0, 845.0, 734.0, 308.99999999999955, 459.0, 577.0, 816.0],"true", 4),
(self.obj58,self.obj78,[828.0, 548.0, 193.24999999995435, 527.7500000000339, 740.5697203588142, 611.7294767110483],"true", 3) )
    # Connections for obj59 (graphObject_: Obj15) named CheckIfFactoryAvailable
    self.drawConnections(
(self.obj59,self.obj68,[-116.65824780483604, 673.6585074361592, 120.0, 561.0, 577.0, 816.0],"true", 3),
(self.obj59,self.obj79,[-116.65824780483604, 673.6585074361592, 350.5000000000978, 527.7500000001161, 538.4022149697663, 713.0650891438612],"true", 3) )
    # Connections for obj60 (graphObject_: Obj16) named ReceiveAnswer
    self.drawConnections(
(self.obj60,self.obj68,[-749.1518174345697, 699.0268602843801, -29.025728871780757, 597.241072553192, 577.0, 816.0],"true", 3) )
    # Connections for obj61 (graphObject_: Obj17) named ProduceSingleRecipePart
    self.drawConnections(
 )
    # Connections for obj62 (graphObject_: Obj18) named ReplyToOrder
    self.drawConnections(
(self.obj62,self.obj69,[1175.0, 548.0, 889.0, 519.0, 1144.0, 715.0],"true", 3),
(self.obj62,self.obj81,[1175.0, 548.0, 922.2500000041096, 485.7499999999685, 1085.454958204394, 611.7901676579015],"true", 3) )
    # Connections for obj63 (graphObject_: Obj19) named ProducePart
    self.drawConnections(
(self.obj63,self.obj69,[617.4640821290151, 631.6126978088166, 723.3405466902973, 582.8913853965432, 1144.0, 715.0],"true", 3) )
    # Connections for obj64 (graphObject_: Obj20) of type canHaveRole
    self.drawConnections(
(self.obj64,self.obj45,[774.0, 146.0, 783.9495115628281, 201.9330601671422, 507.1674107207881, 245.34828460519736],"true", 3),
(self.obj64,self.obj46,[774.0, 146.0, 870.5026338719281, 209.01977194326085, 666.1674107207882, 245.34828460519736],"true", 3) )
    # Connections for obj65 (graphObject_: Obj22) of type hasActions
    self.drawConnections(
(self.obj65,self.obj47,[769.0, 377.0, 808.9955577103624, 401.364017801608, 826.0, 445.0],"true", 3),
(self.obj65,self.obj48,[769.0, 377.0, 719.6841745181231, 423.8822925745004, 655.0, 445.0],"true", 3),
(self.obj65,self.obj49,[769.0, 377.0, 617.2139098420363, 425.65164780928285, 459.0, 445.0],"true", 3),
(self.obj65,self.obj50,[769.0, 377.0, 508.4267622816439, 425.87573820386854, 244.0, 445.0],"true", 3),
(self.obj65,self.obj51,[769.0, 377.0, 415.9320744629807, 425.9314822684313, 60.0, 445.0],"true", 3) )
    # Connections for obj66 (graphObject_: Obj24) of type hasActions
    self.drawConnections(
(self.obj66,self.obj52,[958.0, 377.0, 1074.3572240543556, 396.6467913503584, 1182.0, 445.0],"true", 3),
(self.obj66,self.obj53,[958.0, 377.0, 981.05213750218, 407.361965624455, 975.0, 445.0],"true", 3) )
    # Connections for obj67 (graphObject_: Obj26) of type isPartOfObjective
    self.drawConnections(
(self.obj67,self.obj54,[388.0, 1220.0, 423.9533169633664, 1246.6384871817397, 435.0, 1290.0],"true", 3) )
    # Connections for obj68 (graphObject_: Obj28) of type isPartOfObjective
    self.drawConnections(
(self.obj68,self.obj55,[577.0, 816.0, 607.1248771941662, 880.6663882866239, 608.0, 952.0],"true", 3) )
    # Connections for obj69 (graphObject_: Obj30) of type isPartOfObjective
    self.drawConnections(
(self.obj69,self.obj61,[1144.0, 715.0, 1162.9663030762888, 789.4683110297149, 1209.0, 851.0],"true", 3) )
    # Connections for obj70 (graphObject_: Obj32) of type hasObjective
    self.drawConnections(
(self.obj70,self.obj58,[841.9971730116598, 496.20879275705516, 842.4971730116598, 521.9587927570551, 828.0, 548.0],"true", 3) )
    # Connections for obj71 (graphObject_: Obj34) of type hasObjective
    self.drawConnections(
(self.obj71,self.obj59,[655.0999999999999, 532.5999999999999, 654.3, 542.8, -116.65824780483604, 673.6585074361592],"true", 3) )
    # Connections for obj72 (graphObject_: Obj36) of type hasObjective
    self.drawConnections(
(self.obj72,self.obj60,[467.0, 581.0, 467.0, 632.0, -749.1518174345697, 699.0268602843801],"true", 3) )
    # Connections for obj73 (graphObject_: Obj38) of type hasObjective
    self.drawConnections(
(self.obj73,self.obj56,[278.0, 783.0, 278.0, 935.0, 278.0, 834.0, -130.8660993239755, 819.5505071588908],"true", 4) )
    # Connections for obj74 (graphObject_: Obj40) of type hasObjective
    self.drawConnections(
(self.obj74,self.obj57,[89.0, 783.0, 89.0, 1036.0, 89.0, 935.0, 89.0, 834.0, -204.41814550765912, 441.1089149235471],"true", 5) )
    # Connections for obj75 (graphObject_: Obj42) of type hasObjective
    self.drawConnections(
(self.obj75,self.obj62,[1193.4654791360715, 497.5170713975971, 1191.7154791360715, 523.2670713975971, 1175.0, 548.0],"true", 3) )
    # Connections for obj76 (graphObject_: Obj44) of type hasObjective
    self.drawConnections(
(self.obj76,self.obj63,[1028.4499999999998, 532.5999999999999, 1028.8, 542.8, 617.4640821290151, 631.6126978088166],"true", 3) )
    # Connections for obj77 (graphObject_: Obj46) of type precedentTo
    self.drawConnections(
(self.obj77,self.obj57,[345.157941874857, 1116.6819523635982, 298.657941874857, 1141.9319523635982, -204.41814550765912, 441.1089149235471],"true", 3) )
    # Connections for obj78 (graphObject_: Obj48) of type precedentTo
    self.drawConnections(
(self.obj78,self.obj59,[740.5697203588142, 611.7294767110483, 693.3197203588142, 636.9794767110483, -116.65824780483604, 673.6585074361592],"true", 3) )
    # Connections for obj79 (graphObject_: Obj50) of type precedentTo
    self.drawConnections(
(self.obj79,self.obj60,[538.4022149697663, 713.0650891438612, 484.90221496976625, 738.3150891438612, -749.1518174345697, 699.0268602843801],"true", 3) )
    # Connections for obj80 (graphObject_: Obj52) of type precedentTo
    self.drawConnections(
(self.obj80,self.obj56,[526.9341559502739, 1015.5281742890938, 482.6841559502739, 1040.7781742890938, -130.8660993239755, 819.5505071588908],"true", 3) )
    # Connections for obj81 (graphObject_: Obj54) of type precedentTo
    self.drawConnections(
(self.obj81,self.obj63,[1085.454958204394, 611.7901676579015, 1037.204958204394, 637.0401676579015, 617.4640821290151, 631.6126978088166],"true", 3) )

newfunction = recipeWorldNew_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
