"""
__Test534_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Sun Apr 15 20:50:58 2018
_____________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from Action import *
from Objective import *
from Process import *
from canHaveRole import *
from hasActions import *
from hasObjective import *
from canStartProcess import *
from isPartOfRole import *
from graph_canHaveRole import *
from graph_Process import *
from graph_Action import *
from graph_Objective import *
from graph_hasObjective import *
from graph_Role import *
from graph_OrgUnit import *
from graph_canStartProcess import *
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

def Test534_MDL(self, rootNode, LSMASOMMRootNode=None):

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
        LSMASOMMRootNode.name.setValue('ttt')

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
    self.obj44.name.setValue('OUname')

    # UnitSize
    self.obj44.UnitSize.setValue('Individual')

    self.obj44.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(120.0,130.0,self.obj44)
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
    self.obj45.isMetaRole.setValue((None, 1))
    self.obj45.isMetaRole.config = 0

    # hasActions
    self.obj45.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj45.hasActions.setValue(lcobj2)

    # ID
    self.obj45.ID.setValue('R|0')

    # name
    self.obj45.name.setValue('Wizard')

    self.obj45.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(330.0,140.0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.03
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
    self.obj46.name.setValue('Necromancer')

    self.obj46.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(510.0,100.0,self.obj46)
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
    cobj2=ATOM3String('ConjureItem', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('CastSpell', 20)
    lcobj2.append(cobj2)
    self.obj47.hasActions.setValue(lcobj2)

    # ID
    self.obj47.ID.setValue('R|2')

    # name
    self.obj47.name.setValue('Mage')

    self.obj47.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(520.0,210.0,self.obj47)
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

    self.obj58=Action(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # ID
    self.obj58.ID.setValue('A|0')

    # name
    self.obj58.name.setValue('ConjureItem')

    # ActionCode
    self.obj58.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj58.ActionCode.setHeight(15)

    self.obj58.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(680.0,230.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=Action(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # ID
    self.obj59.ID.setValue('A|1')

    # name
    self.obj59.name.setValue('CastSpell')

    # ActionCode
    self.obj59.ActionCode.setValue('#action code template\nclass BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):\n    """Behaviour available to agents."""\n    def _process(self):\n        pass\n')
    self.obj59.ActionCode.setHeight(15)

    self.obj59.graphClass_= graph_Action
    if self.genGraphics:
       new_obj = graph_Action(680.0,320.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Action", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

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
    self.obj61.ID.setValue('O|0')

    # name
    self.obj61.name.setValue('HaveFriends')

    self.obj61.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(900.0,100.0,self.obj61)
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
    self.obj62.ofActions.setValue(lcobj2)

    # Measurement
    self.obj62.Measurement.setValue('\n')
    self.obj62.Measurement.setHeight(4)

    # Reward
    self.obj62.Reward.setValue('\n')
    self.obj62.Reward.setHeight(4)

    # ID
    self.obj62.ID.setValue('O|1')

    # name
    self.obj62.name.setValue('HaveItem')

    self.obj62.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(900.0,250.0,self.obj62)
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
    self.obj63.ofActions.setValue(lcobj2)

    # Measurement
    self.obj63.Measurement.setValue('\n')
    self.obj63.Measurement.setHeight(4)

    # Reward
    self.obj63.Reward.setValue('\n')
    self.obj63.Reward.setHeight(4)

    # ID
    self.obj63.ID.setValue('O|2')

    # name
    self.obj63.name.setValue('HaveSpell')

    self.obj63.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(900.0,340.0,self.obj63)
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

    self.obj60=Process(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # description
    self.obj60.description.setValue('\n')
    self.obj60.description.setHeight(4)

    # hasActions
    self.obj60.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj60.hasActions.setValue(lcobj2)

    # ID
    self.obj60.ID.setValue('P|0')

    # name
    self.obj60.name.setValue('RaiseDear')

    # Name
    self.obj60.Name.setValue('')
    self.obj60.Name.setNone()

    self.obj60.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(670.0,100.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj49=canHaveRole(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(True)

    # ID
    self.obj49.ID.setValue('OUR|0')

    self.obj49.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(258.5,192.5,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj77=hasActions(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # ID
    self.obj77.ID.setValue('aR|0')

    self.obj77.graphClass_= graph_hasActions
    if self.genGraphics:
       new_obj = graph_hasActions(640.0,265.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj66=hasObjective(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(False)

    # ID
    self.obj66.ID.setValue('RPO|0')

    self.obj66.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(805.5,144.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=hasObjective(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    # ID
    self.obj67.ID.setValue('RPO|1')

    self.obj67.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(822.5,281.5,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    self.obj68=hasObjective(self)
    self.obj68.isGraphObjectVisual = True

    if(hasattr(self.obj68, '_setHierarchicalLink')):
      self.obj68._setHierarchicalLink(False)

    # ID
    self.obj68.ID.setValue('RPO|2')

    self.obj68.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(822.5,371.5,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj65=canStartProcess(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # ID
    self.obj65.ID.setValue('RP|0')

    self.obj65.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(618.0,147.5,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj48=isPartOfRole(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(True)

    # ID
    self.obj48.ID.setValue('pR|0')

    self.obj48.graphClass_= graph_isPartOfRole
    if self.genGraphics:
       new_obj = graph_isPartOfRole(456.0,172.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    # Connections for obj44 (graphObject_: Obj0) named OUname
    self.drawConnections(
(self.obj44,self.obj49,[151.0, 193.0, 258.5, 192.5],"true", 2) )
    # Connections for obj45 (graphObject_: Obj1) named Wizard
    self.drawConnections(
 )
    # Connections for obj46 (graphObject_: Obj2) named Necromancer
    self.drawConnections(
(self.obj46,self.obj48,[546.0, 152.0, 456.0, 172.0],"true", 2),
(self.obj46,self.obj65,[546.0, 152.0, 618.0, 147.5],"true", 2) )
    # Connections for obj47 (graphObject_: Obj3) named Mage
    self.drawConnections(
(self.obj47,self.obj48,[556.0, 262.0, 456.0, 172.0],"true", 2),
(self.obj47,self.obj77,[556.0, 262.0, 640.0, 265.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj8) named ConjureItem
    self.drawConnections(
(self.obj58,self.obj67,[724.0, 268.0, 822.5, 281.5],"true", 2) )
    # Connections for obj59 (graphObject_: Obj9) named CastSpell
    self.drawConnections(
(self.obj59,self.obj68,[724.0, 358.0, 822.5, 371.5],"true", 2) )
    # Connections for obj61 (graphObject_: Obj11) named HaveFriends
    self.drawConnections(
 )
    # Connections for obj62 (graphObject_: Obj12) named HaveItem
    self.drawConnections(
 )
    # Connections for obj63 (graphObject_: Obj13) named HaveSpell
    self.drawConnections(
 )
    # Connections for obj60 (graphObject_: Obj10) named RaiseDear
    self.drawConnections(
(self.obj60,self.obj66,[690.0, 143.0, 805.5, 144.0],"true", 2) )
    # Connections for obj49 (graphObject_: Obj6) of type canHaveRole
    self.drawConnections(
(self.obj49,self.obj45,[258.5, 192.5, 366.0, 192.0],"true", 2) )
    # Connections for obj77 (graphObject_: Obj24) of type hasActions
    self.drawConnections(
(self.obj77,self.obj58,[640.0, 265.0, 724.0, 268.0],"true", 2),
(self.obj77,self.obj59,[640.0, 265.0, 724.0, 358.0],"true", 2) )
    # Connections for obj66 (graphObject_: Obj18) of type hasObjective
    self.drawConnections(
(self.obj66,self.obj61,[805.5, 144.0, 921.0, 145.0],"true", 2) )
    # Connections for obj67 (graphObject_: Obj20) of type hasObjective
    self.drawConnections(
(self.obj67,self.obj62,[822.5, 281.5, 921.0, 295.0],"true", 2) )
    # Connections for obj68 (graphObject_: Obj22) of type hasObjective
    self.drawConnections(
(self.obj68,self.obj63,[822.5, 371.5, 921.0, 385.0],"true", 2) )
    # Connections for obj65 (graphObject_: Obj16) of type canStartProcess
    self.drawConnections(
(self.obj65,self.obj60,[618.0, 147.5, 690.0, 143.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj4) of type isPartOfRole
    self.drawConnections(
(self.obj48,self.obj45,[456.0, 172.0, 366.0, 192.0],"true", 2) )

newfunction = Test534_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
