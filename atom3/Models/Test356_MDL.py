"""
__Test356_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Wed Jun 21 15:53:36 2017
_____________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from Objective import *
from Process import *
from canHaveRole import *
from isPartOfObjective import *
from hasObjective import *
from canStartProcess import *
from graph_canHaveRole import *
from graph_Process import *
from graph_isPartOfObjective import *
from graph_hasObjective import *
from graph_Role import *
from graph_Objective import *
from graph_OrgUnit import *
from graph_canStartProcess import *
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

def Test356_MDL(self, rootNode, LSMASOMMRootNode=None):

    # --- Generating attributes code for ASG LSMASOMM ---
    if( LSMASOMMRootNode ): 
        # author
        LSMASOMMRootNode.author.setValue('Annonymous')

        # description
        LSMASOMMRootNode.description.setValue('\n')
        LSMASOMMRootNode.description.setHeight(15)

        # name
        LSMASOMMRootNode.name.setValue('Test356')

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
    self.obj44.name.setValue('Player')

    # UnitSize
    self.obj44.UnitSize.setValue('Individual')

    self.obj44.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(460.0,120.0,self.obj44)
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
    self.obj45.isMetaRole.setValue(('isMetaRole', 0))
    self.obj45.isMetaRole.config = 0

    # hasActions
    self.obj45.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj45.hasActions.setValue(lcobj2)

    # ID
    self.obj45.ID.setValue('R|0')

    # name
    self.obj45.name.setValue('Wizard')

    self.obj45.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(100.0,100.0,self.obj45)
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
    self.obj47.ID.setValue('R|1')

    # name
    self.obj47.name.setValue('Shadow')

    self.obj47.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(200.0,280.0,self.obj47)
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

    self.obj44=Objective(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # description
    self.obj44.description.setValue('\n')
    self.obj44.description.setHeight(4)

    # Reward
    self.obj44.Reward.setValue('\n')
    self.obj44.Reward.setHeight(4)

    # ID
    self.obj44.ID.setValue('O|0')

    # name
    self.obj44.name.setValue('')
    self.obj44.name.setNone()

    # Measurement
    self.obj44.Measurement.setValue('\n')
    self.obj44.Measurement.setHeight(4)

    self.obj44.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(500.0,300.0,self.obj44)
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

    self.obj45=Objective(self)
    self.obj45.isGraphObjectVisual = True

    if(hasattr(self.obj45, '_setHierarchicalLink')):
      self.obj45._setHierarchicalLink(False)

    # description
    self.obj45.description.setValue('\n')
    self.obj45.description.setHeight(4)

    # Reward
    self.obj45.Reward.setValue('\n')
    self.obj45.Reward.setHeight(4)

    # ID
    self.obj45.ID.setValue('O|1')

    # name
    self.obj45.name.setValue('')
    self.obj45.name.setNone()

    # Measurement
    self.obj45.Measurement.setValue('\n')
    self.obj45.Measurement.setHeight(4)

    self.obj45.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(780.0,300.0,self.obj45)
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

    # Reward
    self.obj46.Reward.setValue('\n')
    self.obj46.Reward.setHeight(4)

    # ID
    self.obj46.ID.setValue('O|2')

    # name
    self.obj46.name.setValue('')
    self.obj46.name.setNone()

    # Measurement
    self.obj46.Measurement.setValue('\n')
    self.obj46.Measurement.setHeight(4)

    self.obj46.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(660.0,300.0,self.obj46)
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

    self.obj47=Process(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # Activities
    self.obj47.Activities.setValue('\n')
    self.obj47.Activities.setHeight(10)

    # description
    self.obj47.description.setValue('\n')
    self.obj47.description.setHeight(4)

    # ID
    self.obj47.ID.setValue('P|0')

    # name
    self.obj47.name.setValue('')
    self.obj47.name.setNone()

    # Name
    self.obj47.Name.setValue('')
    self.obj47.Name.setNone()

    self.obj47.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(1040.0,340.0,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj47.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj47)
    self.globalAndLocalPostcondition(self.obj47, rootNode)
    self.obj47.postAction( rootNode.CREATE )

    self.obj48=Process(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # Activities
    self.obj48.Activities.setValue('\n')
    self.obj48.Activities.setHeight(10)

    # description
    self.obj48.description.setValue('\n')
    self.obj48.description.setHeight(4)

    # ID
    self.obj48.ID.setValue('P|1')

    # name
    self.obj48.name.setValue('')
    self.obj48.name.setNone()

    # Name
    self.obj48.Name.setValue('')
    self.obj48.Name.setNone()

    self.obj48.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(1160.0,380.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=Process(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(False)

    # Activities
    self.obj49.Activities.setValue('\n')
    self.obj49.Activities.setHeight(10)

    # description
    self.obj49.description.setValue('\n')
    self.obj49.description.setHeight(4)

    # ID
    self.obj49.ID.setValue('P|2')

    # name
    self.obj49.name.setValue('')
    self.obj49.name.setNone()

    # Name
    self.obj49.Name.setValue('')
    self.obj49.Name.setNone()

    self.obj49.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(1280.0,380.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    self.obj46=canHaveRole(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(True)

    # ID
    self.obj46.ID.setValue('OUR|0')

    self.obj46.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(362.0,248.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj59=isPartOfObjective(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(True)

    # ID
    self.obj59.ID.setValue('pO|0')

    self.obj59.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(601.0,345.0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj61=hasObjective(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    # ID
    self.obj61.ID.setValue('RPO|0')

    self.obj61.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(870.5,363.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj55=canStartProcess(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # ID
    self.obj55.ID.setValue('RP|0')

    self.obj55.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(651.0,464.5,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj57=canStartProcess(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # ID
    self.obj57.ID.setValue('RP|1')

    self.obj57.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(658.0,285.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    # Connections for obj44 (graphObject_: Obj9) named Player
    self.drawConnections(
(self.obj44,self.obj46,[491.0, 183.0, 361.6234237415075, 237.56783919598], 0, 2) )
    # Connections for obj45 (graphObject_: Obj7) named Wizard
    self.drawConnections(
(self.obj45,self.obj57,[136.0, 152.0, 658.0, 285.5],"true", 2) )
    # Connections for obj47 (graphObject_: Obj8) named Shadow
    self.drawConnections(
(self.obj47,self.obj55,[236.0, 332.0, 651.0, 464.5],"true", 2) )
    # Connections for obj44 (graphObject_: Obj0) named 
    self.drawConnections(
 )
    # Connections for obj45 (graphObject_: Obj1) named 
    self.drawConnections(
 )
    # Connections for obj46 (graphObject_: Obj2) named 
    self.drawConnections(
(self.obj46,self.obj59,[681.0, 345.0, 601.0, 345.0],"true", 0) )
    # Connections for obj47 (graphObject_: Obj3) named 
    self.drawConnections(
(self.obj47,self.obj61,[1060.0, 381.0, 870.5, 363.0],"true", 0) )
    # Connections for obj48 (graphObject_: Obj4) named 
    self.drawConnections(
 )
    # Connections for obj49 (graphObject_: Obj5) named 
    self.drawConnections(
 )
    # Connections for obj46 (graphObject_: Obj10) of type canHaveRole
    self.drawConnections(
(self.obj46,self.obj45,[361.6234237415075, 237.56783919598, 136.0, 152.0], 0, 2),
(self.obj46,self.obj47,[361.6234237415075, 237.56783919598, 236.0, 332.0], 0, 2) )
    # Connections for obj59 (graphObject_: Obj16) of type isPartOfObjective
    self.drawConnections(
(self.obj59,self.obj44,[601.0, 345.0, 521.0, 345.0],"true", 2) )
    # Connections for obj61 (graphObject_: Obj18) of type hasObjective
    self.drawConnections(
(self.obj61,self.obj46,[870.5, 363.0, 681.0, 345.0],"true", 2) )
    # Connections for obj55 (graphObject_: Obj12) of type canStartProcess
    self.drawConnections(
(self.obj55,self.obj47,[651.0, 464.5, 1060.0, 381.0],"true", 2) )
    # Connections for obj57 (graphObject_: Obj14) of type canStartProcess
    self.drawConnections(
(self.obj57,self.obj48,[658.0, 285.5, 1180.0, 421.0],"true", 2),
(self.obj57,self.obj49,[658.0, 285.5, 1300.0, 421.0],"true", 2) )

newfunction = Test356_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
