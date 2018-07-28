"""
__testT_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Sat Oct 21 17:47:58 2017
___________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from Action import *
from canHaveRole import *
from graph_canHaveRole import *
from graph_OrgUnit import *
from graph_Role import *
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

def testT_MDL(self, rootNode, LSMASOMMRootNode=None):

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
        LSMASOMMRootNode.name.setValue('t')

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
    self.obj44.name.setValue('Agent')

    # UnitSize
    self.obj44.UnitSize.setValue('Individual')

    self.obj44.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(100.0,160.0,self.obj44)
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

    self.obj47=Role(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # isMetaRole
    self.obj47.isMetaRole.setValue(('isMetaRole', 0))
    self.obj47.isMetaRole.config = 0

    # hasActions
    self.obj47.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj47.hasActions.setValue(lcobj2)

    # ID
    self.obj47.ID.setValue('R|0')

    # name
    self.obj47.name.setValue('Scout')

    self.obj47.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(380.0,100.0,self.obj47)
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
    self.obj48.isMetaRole.setValue(('isMetaRole', 0))
    self.obj48.isMetaRole.config = 0

    # hasActions
    self.obj48.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj48.hasActions.setValue(lcobj2)

    # ID
    self.obj48.ID.setValue('R|1')

    # name
    self.obj48.name.setValue('Communicator')

    self.obj48.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(400.0,220.0,self.obj48)
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
    self.obj49.isMetaRole.setValue(('isMetaRole', 0))
    self.obj49.isMetaRole.config = 0

    # hasActions
    self.obj49.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj49.hasActions.setValue(lcobj2)

    # ID
    self.obj49.ID.setValue('R|2')

    # name
    self.obj49.name.setValue('DefaultSPADE')

    self.obj49.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(360.0,320.0,self.obj49)
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

    self.obj56=Action(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # ID
    self.obj56.ID.setValue('A|0')

    # name
    self.obj56.name.setValue('goToNPC')

    # ActionCode
    self.obj56.ActionCode.setValue('#action code placeholder or description\n#\nclass goToNPC(spade.Behaviour.OneShotBehaviour):\n    """Behaviour to change the Role of the Agent. The Agent will acquire behaviours of the needed Role."""\n    def _process(self):\n        pass\n')
    self.obj56.ActionCode.setHeight(15)

    self.obj56.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(600.0,40.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=Action(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # ID
    self.obj57.ID.setValue('A|1')

    # name
    self.obj57.name.setValue('goToLocation')

    # ActionCode
    self.obj57.ActionCode.setValue('#action code placeholder or description\n#\nclass goToLocation(spade.Behaviour.OneShotBehaviour):\n    """Behaviour to change the Role of the Agent. The Agent will acquire behaviours of the needed Role."""\n    def _process(self):\n        pass\n')
    self.obj57.ActionCode.setHeight(15)

    self.obj57.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(640.0,100.0,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj62=Action(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    # ID
    self.obj62.ID.setValue('A|2')

    # name
    self.obj62.name.setValue('talkToNPC')

    # ActionCode
    self.obj62.ActionCode.setValue('#action code placeholder or description\n#\nclass talkToNPC(spade.Behaviour.OneShotBehaviour):\n    """Behaviour to change the Role of the Agent. The Agent will acquire behaviours of the needed Role."""\n    def _process(self):\n        pass\n')
    self.obj62.ActionCode.setHeight(15)

    self.obj62.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(660.0,200.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj65=Action(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # ID
    self.obj65.ID.setValue('A|3')

    # name
    self.obj65.name.setValue('answerNPC')

    # ActionCode
    self.obj65.ActionCode.setValue('#action code placeholder or description\n#\nclass answerNPC(spade.Behaviour.OneShotBehaviour):\n    """Behaviour to change the Role of the Agent. The Agent will acquire behaviours of the needed Role."""\n    def _process(self):\n        pass\n')
    self.obj65.ActionCode.setHeight(15)

    self.obj65.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(620.0,280.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj68=canHaveRole(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(True)

    # ID
    self.obj68.ID.setValue('OUR|0')

    self.obj68.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(262.5,241.5,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    # Connections for obj44 (graphObject_: Obj0) named Agent
    self.drawConnections(
(self.obj44,self.obj68,[131.0, 223.0, 262.5, 241.5],"true", 2) )
    # Connections for obj47 (graphObject_: Obj1) named Scout
    self.drawConnections(
 )
    # Connections for obj48 (graphObject_: Obj2) named Communicator
    self.drawConnections(
 )
    # Connections for obj49 (graphObject_: Obj3) named DefaultSPADE
    self.drawConnections(
 )
    # Connections for obj56 (graphObject_: Obj4) named goToNPC
    self.drawConnections(
 )
    # Connections for obj57 (graphObject_: Obj5) named goToLocation
    self.drawConnections(
 )
    # Connections for obj62 (graphObject_: Obj6) named talkToNPC
    self.drawConnections(
 )
    # Connections for obj65 (graphObject_: Obj7) named answerNPC
    self.drawConnections(
 )
    # Connections for obj68 (graphObject_: Obj8) of type canHaveRole
    self.drawConnections(
(self.obj68,self.obj47,[262.5, 241.5, 416.0, 152.0],"true", 2),
(self.obj68,self.obj48,[262.5, 241.5, 436.0, 272.0],"true", 2),
(self.obj68,self.obj49,[262.5, 241.5, 396.0, 372.0],"true", 2) )

newfunction = testT_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
