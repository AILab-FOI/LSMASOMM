"""
__TMWRolesActions_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Tue May  1 04:07:37 2018
_____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from Action import *
from canHaveRole import *
from hasActions import *
from graph_canHaveRole import *
from graph_OrgUnit import *
from graph_Role import *
from graph_hasActions import *
from graph_Action import *
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

def TMWRolesActions_MDL(self, rootNode, LSMASOMMRootNode=None):

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


    self.obj56=OrgUnit(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # Individual
    self.obj56.Individual.setValue(('1', 0))
    self.obj56.Individual.config = 0

    # hasActions
    self.obj56.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj56.hasActions.setValue(lcobj2)

    # ID
    self.obj56.ID.setValue('OU|0')

    # name
    self.obj56.name.setValue('Agent')

    # UnitSize
    self.obj56.UnitSize.setValue('Individual')

    self.obj56.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(108,0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

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
    cobj2=ATOM3String('move', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('talkToNPC', 20)
    lcobj2.append(cobj2)
    self.obj48.hasActions.setValue(lcobj2)

    # ID
    self.obj48.ID.setValue('R|0')

    # name
    self.obj48.name.setValue('Scout')

    self.obj48.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(172,202,self.obj48)
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
    cobj2=ATOM3String('attack', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('equipItem', 20)
    lcobj2.append(cobj2)
    self.obj49.hasActions.setValue(lcobj2)

    # ID
    self.obj49.ID.setValue('R|1')

    # name
    self.obj49.name.setValue('Warrior')

    self.obj49.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(32,202,self.obj49)
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
       new_obj = graph_Action(194,384,self.obj101)
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
       new_obj = graph_Action(141,384,self.obj105)
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
       new_obj = graph_Action(59,384,self.obj109)
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
       new_obj = graph_Action(5,384,self.obj83)
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

    self.obj59=canHaveRole(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(True)

    # ID
    self.obj59.ID.setValue('OUR|0')

    self.obj59.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(134.0,150.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj54=hasActions(self)
    self.obj54.isGraphObjectVisual = True

    if(hasattr(self.obj54, '_setHierarchicalLink')):
      self.obj54._setHierarchicalLink(False)

    # ID
    self.obj54.ID.setValue('aR|0')

    self.obj54.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(202.0,349.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)
    self.obj54.postAction( rootNode.CREATE )

    self.obj55=hasActions(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # ID
    self.obj55.ID.setValue('aR|1')

    self.obj55.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(62.0,349.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    # Connections for obj56 (graphObject_: Obj10) named Agent
    self.drawConnections(
(self.obj56,self.obj59,[131.0, 63.0, 112.51188001292824, 107.18924551679558, 134.0, 150.0],"true", 3) )
    # Connections for obj48 (graphObject_: Obj4) named Scout
    self.drawConnections(
(self.obj48,self.obj54,[201.7067257860162, 254.42953456731163, 181.8534590616701, 301.77678935417276, 202.0, 349.0],"true", 3) )
    # Connections for obj49 (graphObject_: Obj5) named Warrior
    self.drawConnections(
(self.obj49,self.obj55,[61.3413839290904, 253.87509036477832, 41.671171323140584, 301.5760158075433, 62.0, 349.0],"true", 3) )
    # Connections for obj101 (graphObject_: Obj0) named talkToNPC
    self.drawConnections(
 )
    # Connections for obj105 (graphObject_: Obj1) named move
    self.drawConnections(
 )
    # Connections for obj109 (graphObject_: Obj2) named equipItem
    self.drawConnections(
 )
    # Connections for obj83 (graphObject_: Obj3) named attack
    self.drawConnections(
 )
    # Connections for obj59 (graphObject_: Obj11) of type canHaveRole
    self.drawConnections(
(self.obj59,self.obj49,[134.0, 150.0, 81.28205591320747, 190.47401133035237, 61.3413839290904, 253.87509036477832],"true", 3),
(self.obj59,self.obj48,[134.0, 150.0, 151.07183741739775, 213.0950431400595, 201.7067257860162, 254.42953456731163],"true", 3) )
    # Connections for obj54 (graphObject_: Obj6) of type hasActions
    self.drawConnections(
(self.obj54,self.obj105,[202.0, 349.0, 164.14544889353556, 375.52288418612693, 161.15864352926405, 421.64781690953146],"true", 3),
(self.obj54,self.obj101,[202.0, 349.0, 198.8557785183645, 393.23972560260796, 232.60256157852712, 422.018086973783],"true", 3) )
    # Connections for obj55 (graphObject_: Obj8) of type hasActions
    self.drawConnections(
(self.obj55,self.obj83,[62.0, 349.0, 26.072797519074648, 376.6910931151533, 26.031502454371434, 422.0514151018316],"true", 3),
(self.obj55,self.obj109,[62.0, 349.0, 59.65447642313099, 393.51942188107927, 93.95246581723075, 421.9997366440411],"true", 3) )

newfunction = TMWRolesActions_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
