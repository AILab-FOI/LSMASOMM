"""
__TMWQuestsMaggots_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Tue May  1 03:55:42 2018
______________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from Objective import *
from isPartOfObjective import *
from precedentTo import *
from graph_isPartOfObjective import *
from graph_Objective import *
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

def TMWQuestsMaggots_MDL(self, rootNode, LSMASOMMRootNode=None):

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
       new_obj = graph_Objective(761,303,self.obj44)
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
       new_obj = graph_Objective(0,505,self.obj47)
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
       new_obj = graph_Objective(128,404,self.obj50)
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
       new_obj = graph_Objective(232,303,self.obj55)
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
       new_obj = graph_Objective(362,202,self.obj58)
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
       new_obj = graph_Objective(477,101,self.obj63)
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
       new_obj = graph_Objective(598,0,self.obj68)
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
       new_obj = graph_isPartOfObjective(736.0,313.0,self.obj71)
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

    self.obj72=precedentTo(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(True)

    # ID
    self.obj72.ID.setValue('OpO|0')

    self.obj72.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(107.433385235,491.958145418,self.obj72)
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
       new_obj = graph_precedentTo(223.965485908,390.930315358,self.obj73)
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
       new_obj = graph_precedentTo(344.153945772,289.77163693,self.obj74)
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
       new_obj = graph_precedentTo(464.497389922,188.902891196,self.obj75)
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
       new_obj = graph_precedentTo(585.684662394,87.746516207,self.obj76)
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

    # Connections for obj44 (graphObject_: Obj0) named FinishMaggots
    self.drawConnections(
 )
    # Connections for obj47 (graphObject_: Obj1) named talkToNPCTanisha
    self.drawConnections(
(self.obj47,self.obj71,[56.0, 550.0, 171.0, 534.0, 275.0, 543.0, 405.0, 538.0, 520.0, 540.0, 641.0, 542.0, 736.0, 313.0],"true", 7),
(self.obj47,self.obj72,[56.0, 550.0, 78.4333852350551, 517.2081454184791, 107.4333852350551, 491.9581454184791],"true", 3) )
    # Connections for obj50 (graphObject_: Obj2) named equipItemKnife
    self.drawConnections(
(self.obj50,self.obj71,[172.0, 449.0, 275.0, 442.0, 405.0, 437.0, 520.0, 439.0, 641.0, 441.0, 736.0, 313.0],"true", 6),
(self.obj50,self.obj73,[172.0, 449.0, 194.71548590754864, 416.1803153582494, 223.96548590754864, 390.9303153582494],"true", 3) )
    # Connections for obj55 (graphObject_: Obj3) named goToLocation10287
    self.drawConnections(
(self.obj55,self.obj71,[289.0, 348.0, 405.0, 336.0, 520.0, 338.0, 641.0, 340.0, 736.0, 313.0],"true", 5),
(self.obj55,self.obj74,[289.0, 348.0, 313.4039457720786, 315.02163693035317, 344.1539457720786, 289.77163693035317],"true", 3) )
    # Connections for obj58 (graphObject_: Obj4) named killMobMaggot10
    self.drawConnections(
(self.obj58,self.obj71,[412.0, 247.0, 520.0, 237.0, 641.0, 239.0, 736.0, 313.0],"true", 4),
(self.obj58,self.obj75,[412.0, 247.0, 434.9973899222055, 214.15289119624012, 464.4973899222055, 188.90289119624012],"true", 3) )
    # Connections for obj63 (graphObject_: Obj5) named goToNPCTanisha
    self.drawConnections(
(self.obj63,self.obj71,[530.0, 146.0, 641.0, 138.0, 736.0, 313.0],"true", 3),
(self.obj63,self.obj76,[530.0, 146.0, 554.684662394439, 112.99651620703398, 585.684662394439, 87.74651620703398],"true", 3) )
    # Connections for obj68 (graphObject_: Obj6) named talkToNPCTanisha
    self.drawConnections(
(self.obj68,self.obj71,[654.0, 45.0, 685.4375929143717, 181.92581112321463, 736.0, 313.0],"true", 3) )
    # Connections for obj71 (graphObject_: Obj7) of type isPartOfObjective
    self.drawConnections(
(self.obj71,self.obj44,[736.0, 313.0, 765.4235656818262, 339.39135810388046, 804.0, 348.0],"true", 3) )
    # Connections for obj72 (graphObject_: Obj9) of type precedentTo
    self.drawConnections(
(self.obj72,self.obj50,[107.4333852350551, 491.9581454184791, 136.43338523505508, 466.7081454184791, 172.0, 449.0],"true", 3) )
    # Connections for obj73 (graphObject_: Obj11) of type precedentTo
    self.drawConnections(
(self.obj73,self.obj55,[223.96548590754864, 390.9303153582494, 253.21548590754864, 365.6803153582494, 289.0, 348.0],"true", 3) )
    # Connections for obj74 (graphObject_: Obj13) of type precedentTo
    self.drawConnections(
(self.obj74,self.obj58,[344.1539457720786, 289.77163693035317, 374.9039457720786, 264.52163693035317, 412.0, 247.0],"true", 3) )
    # Connections for obj75 (graphObject_: Obj15) of type precedentTo
    self.drawConnections(
(self.obj75,self.obj63,[464.4973899222055, 188.90289119624012, 493.9973899222055, 163.65289119624012, 530.0, 146.0],"true", 3) )
    # Connections for obj76 (graphObject_: Obj17) of type precedentTo
    self.drawConnections(
(self.obj76,self.obj68,[585.684662394439, 87.74651620703398, 616.684662394439, 62.496516207033984, 654.0, 45.0],"true", 3) )

newfunction = TMWQuestsMaggots_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
