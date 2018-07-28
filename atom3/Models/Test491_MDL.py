"""
__Test491_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Wed Jun 21 16:55:58 2017
_____________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from Objective import *
from Process import *
from canHaveRole import *
from hasObjective import *
from canStartProcess import *
from graph_canHaveRole import *
from graph_Process import *
from graph_Objective import *
from graph_hasObjective import *
from graph_Role import *
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

def Test491_MDL(self, rootNode, LSMASOMMRootNode=None):

    # --- Generating attributes code for ASG LSMASOMM ---
    if( LSMASOMMRootNode ): 
        # author
        LSMASOMMRootNode.author.setValue('Annonymous')

        # description
        LSMASOMMRootNode.description.setValue('\n')
        LSMASOMMRootNode.description.setHeight(15)

        # name
        LSMASOMMRootNode.name.setValue('Test392')

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
    cobj2=ATOM3String('Login', 20)
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
       new_obj = graph_OrgUnit(160.0,80.0,self.obj44)
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
    cobj2=ATOM3String('Move', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Stroll', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Charge', 20)
    lcobj2.append(cobj2)
    self.obj45.hasActions.setValue(lcobj2)

    # ID
    self.obj45.ID.setValue('R|0')

    # name
    self.obj45.name.setValue('role name')

    self.obj45.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(360.0,100.0,self.obj45)
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

    self.obj47=Objective(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # description
    self.obj47.description.setValue('\n')
    self.obj47.description.setHeight(4)

    # Reward
    self.obj47.Reward.setValue('\n')
    self.obj47.Reward.setHeight(4)

    # ID
    self.obj47.ID.setValue('O|0')

    # name
    self.obj47.name.setValue('MoveTo')

    # Measurement
    self.obj47.Measurement.setValue('\n')
    self.obj47.Measurement.setHeight(4)

    self.obj47.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(680.0,120.0,self.obj47)
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

    self.obj46=Process(self)
    self.obj46.isGraphObjectVisual = True

    if(hasattr(self.obj46, '_setHierarchicalLink')):
      self.obj46._setHierarchicalLink(False)

    # Activities
    self.obj46.Activities.setValue('\n')
    self.obj46.Activities.setHeight(10)

    # description
    self.obj46.description.setValue('\n')
    self.obj46.description.setHeight(4)

    # ID
    self.obj46.ID.setValue('P|0')

    # name
    self.obj46.name.setValue('Walking')

    # Name
    self.obj46.Name.setValue('Walking')

    self.obj46.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(540.0,180.0,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj57=canHaveRole(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(True)

    # ID
    self.obj57.ID.setValue('OUR|0')

    self.obj57.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(293.5,147.5,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj48=hasObjective(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # ID
    self.obj48.ID.setValue('RPO|0')

    self.obj48.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(630.5,193.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj58=canStartProcess(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # ID
    self.obj58.ID.setValue('RP|0')

    self.obj58.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(478.0,186.5,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    # Connections for obj44 (graphObject_: Obj0) named OUname
    self.drawConnections(
(self.obj44,self.obj57,[191.0, 143.0, 293.5, 147.5],"true", 2) )
    # Connections for obj45 (graphObject_: Obj1) named role name
    self.drawConnections(
(self.obj45,self.obj58,[396.0, 152.0, 478.0, 186.5],"true", 2) )
    # Connections for obj47 (graphObject_: Obj3) named MoveTo
    self.drawConnections(
 )
    # Connections for obj46 (graphObject_: Obj2) named Walking
    self.drawConnections(
(self.obj46,self.obj48,[560.0, 221.0, 630.5, 193.0],"true", 2) )
    # Connections for obj57 (graphObject_: Obj6) of type canHaveRole
    self.drawConnections(
(self.obj57,self.obj45,[293.5, 147.5, 396.0, 152.0],"true", 2) )
    # Connections for obj48 (graphObject_: Obj4) of type hasObjective
    self.drawConnections(
(self.obj48,self.obj47,[630.5, 193.0, 701.0, 165.0],"true", 2) )
    # Connections for obj58 (graphObject_: Obj8) of type canStartProcess
    self.drawConnections(
(self.obj58,self.obj46,[478.0, 186.5, 560.0, 221.0],"true", 2) )

newfunction = Test491_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
