"""
__MinionWars_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Wed Jun 21 01:31:04 2017
________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from IndividualKnArt import *
from Objective import *
from Process import *
from canHaveRole import *
from canAccessKnArt import *
from isPartOfObjective import *
from hasObjective import *
from canStartProcess import *
from graph_canHaveRole import *
from graph_canAccessKnArt import *
from graph_Process import *
from graph_isPartOfObjective import *
from graph_hasObjective import *
from graph_Role import *
from graph_Objective import *
from graph_OrgUnit import *
from graph_IndividualKnArt import *
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

def MinionWars_MDL(self, rootNode, LSMASOMMRootNode=None):

    # --- Generating attributes code for ASG LSMASOMM ---
    if( LSMASOMMRootNode ): 
        # author
        LSMASOMMRootNode.author.setValue('Bogdan')

        # description
        LSMASOMMRootNode.description.setValue('\n')
        LSMASOMMRootNode.description.setHeight(15)

        # name
        LSMASOMMRootNode.name.setValue('MinionWars')

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
       new_obj = graph_OrgUnit(411,0,self.obj44)
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
    cobj2=ATOM3String('VisitLocation', 20)
    lcobj2.append(cobj2)
    self.obj45.hasActions.setValue(lcobj2)

    # ID
    self.obj45.ID.setValue('R|0')

    # name
    self.obj45.name.setValue('Scout')

    self.obj45.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(411,183,self.obj45)
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
    self.obj46.isMetaRole.setValue(('isMetaRole', 0))
    self.obj46.isMetaRole.config = 0

    # hasActions
    self.obj46.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('Attack', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Defend', 20)
    lcobj2.append(cobj2)
    self.obj46.hasActions.setValue(lcobj2)

    # ID
    self.obj46.ID.setValue('R|1')

    # name
    self.obj46.name.setValue('Warrior')

    self.obj46.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(0,519,self.obj46)
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
    self.obj47.isMetaRole.setValue(('isMetaRole', 0))
    self.obj47.isMetaRole.config = 0

    # hasActions
    self.obj47.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ProcessInformation', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Reason', 20)
    lcobj2.append(cobj2)
    self.obj47.hasActions.setValue(lcobj2)

    # ID
    self.obj47.ID.setValue('R|3')

    # name
    self.obj47.name.setValue('Student')

    self.obj47.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(137,519,self.obj47)
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

    self.obj48=IndividualKnArt(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(False)

    # description
    self.obj48.description.setValue('KnArtDesc')

    # ID
    self.obj48.ID.setValue('KA|0')

    # name
    self.obj48.name.setValue('KnArtName')

    # KnArtContent
    self.obj48.KnArtContent.setValue('#content of the artifact\n')
    self.obj48.KnArtContent.setHeight(15)

    self.obj48.graphClass_= graph_IndividualKnArt
    if self.genGraphics:
       new_obj = graph_IndividualKnArt(558.0,380.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IndividualKnArt", new_obj.tag)
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

    # Reward
    self.obj49.Reward.setValue('\n')
    self.obj49.Reward.setHeight(4)

    # ID
    self.obj49.ID.setValue('OP|0')

    # name
    self.obj49.name.setValue('TowerOfLondon')

    # Measurement
    self.obj49.Measurement.setValue('\n')
    self.obj49.Measurement.setHeight(4)

    self.obj49.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(300.0,980.0,self.obj49)
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

    # Reward
    self.obj50.Reward.setValue('\n')
    self.obj50.Reward.setHeight(4)

    # ID
    self.obj50.ID.setValue('OP|1')

    # name
    self.obj50.name.setValue('KillChief')

    # Measurement
    self.obj50.Measurement.setValue('\n')
    self.obj50.Measurement.setHeight(4)

    self.obj50.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(0,848,self.obj50)
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

    # Reward
    self.obj51.Reward.setValue('\n')
    self.obj51.Reward.setHeight(4)

    # ID
    self.obj51.ID.setValue('OP|2')

    # name
    self.obj51.name.setValue('LearnBackstory')

    # Measurement
    self.obj51.Measurement.setValue('\n')
    self.obj51.Measurement.setHeight(4)

    self.obj51.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(274,848,self.obj51)
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

    # Reward
    self.obj52.Reward.setValue('\n')
    self.obj52.Reward.setHeight(4)

    # ID
    self.obj52.ID.setValue('OP|3')

    # name
    self.obj52.name.setValue('ExploreLandmark')

    # Measurement
    self.obj52.Measurement.setValue('\n')
    self.obj52.Measurement.setHeight(4)

    self.obj52.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(420.0,660.0,self.obj52)
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

    self.obj53=Objective(self)
    self.obj53.isGraphObjectVisual = True

    if(hasattr(self.obj53, '_setHierarchicalLink')):
      self.obj53._setHierarchicalLink(False)

    # description
    self.obj53.description.setValue('\n')
    self.obj53.description.setHeight(4)

    # Reward
    self.obj53.Reward.setValue('\n')
    self.obj53.Reward.setHeight(4)

    # ID
    self.obj53.ID.setValue('OP|4')

    # name
    self.obj53.name.setValue('VisitInnerWard')

    # Measurement
    self.obj53.Measurement.setValue('\n')
    self.obj53.Measurement.setHeight(4)

    self.obj53.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(411,519,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
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

    # Reward
    self.obj54.Reward.setValue('\n')
    self.obj54.Reward.setHeight(4)

    # ID
    self.obj54.ID.setValue('OP|5')

    # name
    self.obj54.name.setValue('VisitOuterWard')

    # Measurement
    self.obj54.Measurement.setValue('\n')
    self.obj54.Measurement.setHeight(4)

    self.obj54.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(512.0,522.0,self.obj54)
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

    # Reward
    self.obj55.Reward.setValue('\n')
    self.obj55.Reward.setHeight(4)

    # ID
    self.obj55.ID.setValue('OP|6')

    # name
    self.obj55.name.setValue('VisitInnermostWard')

    # Measurement
    self.obj55.Measurement.setValue('\n')
    self.obj55.Measurement.setHeight(4)

    self.obj55.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(274,519,self.obj55)
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

    # Reward
    self.obj56.Reward.setValue('\n')
    self.obj56.Reward.setHeight(4)

    # ID
    self.obj56.ID.setValue('OP|7')

    # name
    self.obj56.name.setValue('KillMinions')

    # Measurement
    self.obj56.Measurement.setValue('\n')
    self.obj56.Measurement.setHeight(4)

    self.obj56.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(137,848,self.obj56)
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

    # Reward
    self.obj57.Reward.setValue('\n')
    self.obj57.Reward.setHeight(4)

    # ID
    self.obj57.ID.setValue('OP|8')

    # name
    self.obj57.name.setValue('DecipherClues')

    # Measurement
    self.obj57.Measurement.setValue('\n')
    self.obj57.Measurement.setHeight(4)

    self.obj57.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(411,848,self.obj57)
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

    self.obj73=Process(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    # Activities
    self.obj73.Activities.setValue('\n')
    self.obj73.Activities.setHeight(10)

    # description
    self.obj73.description.setValue('\n')
    self.obj73.description.setHeight(4)

    # ID
    self.obj73.ID.setValue('OP|0')

    # name
    self.obj73.name.setValue('')
    self.obj73.name.setNone()

    # Name
    self.obj73.Name.setValue('')
    self.obj73.Name.setNone()

    self.obj73.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(411,322,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=Process(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    # Activities
    self.obj74.Activities.setValue('\n')
    self.obj74.Activities.setHeight(10)

    # description
    self.obj74.description.setValue('\n')
    self.obj74.description.setHeight(4)

    # ID
    self.obj74.ID.setValue('OP|1')

    # name
    self.obj74.name.setValue('')
    self.obj74.name.setNone()

    # Name
    self.obj74.Name.setValue('')
    self.obj74.Name.setNone()

    self.obj74.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(0,672,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=Process(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    # Activities
    self.obj75.Activities.setValue('\n')
    self.obj75.Activities.setHeight(10)

    # description
    self.obj75.description.setValue('\n')
    self.obj75.description.setHeight(4)

    # ID
    self.obj75.ID.setValue('OP|2')

    # name
    self.obj75.name.setValue('')
    self.obj75.name.setNone()

    # Name
    self.obj75.Name.setValue('')
    self.obj75.Name.setNone()

    self.obj75.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(137,672,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj58=canHaveRole(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(True)

    # ID
    self.obj58.ID.setValue('OUR|0')

    self.obj58.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(292.0,141.0,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj91=canAccessKnArt(self)
    self.obj91.isGraphObjectVisual = True

    if(hasattr(self.obj91, '_setHierarchicalLink')):
      self.obj91._setHierarchicalLink(False)

    # ID
    self.obj91.ID.setValue('accKA|1')

    self.obj91.graphClass_= graph_canAccessKnArt
    if self.genGraphics:
       new_obj = graph_canAccessKnArt(568.0,294.0,self.obj91)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canAccessKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj91.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj91)
    self.globalAndLocalPostcondition(self.obj91, rootNode)
    self.obj91.postAction( rootNode.CREATE )

    self.obj66=isPartOfObjective(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(True)

    # ID
    self.obj66.ID.setValue('pO|3')

    self.obj66.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(284.0,954.0,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj72=isPartOfObjective(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(True)

    # ID
    self.obj72.ID.setValue('pO|2')

    self.obj72.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(421.0,652.0,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj84=isPartOfObjective(self)
    self.obj84.isGraphObjectVisual = True

    if(hasattr(self.obj84, '_setHierarchicalLink')):
      self.obj84._setHierarchicalLink(True)

    # ID
    self.obj84.ID.setValue('pO|2')

    self.obj84.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(421.0,778.0,self.obj84)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj84.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84, rootNode)
    self.obj84.postAction( rootNode.CREATE )

    self.obj77=hasObjective(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(False)

    # ID
    self.obj77.ID.setValue('RPO|0')

    self.obj77.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(421.0,403.0,self.obj77)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj77.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj77)
    self.globalAndLocalPostcondition(self.obj77, rootNode)
    self.obj77.postAction( rootNode.CREATE )

    self.obj80=hasObjective(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(False)

    # ID
    self.obj80.ID.setValue('RPO|1')

    self.obj80.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(10.0,778.0,self.obj80)
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

    self.obj85=hasObjective(self)
    self.obj85.isGraphObjectVisual = True

    if(hasattr(self.obj85, '_setHierarchicalLink')):
      self.obj85._setHierarchicalLink(False)

    # ID
    self.obj85.ID.setValue('RPO|2')

    self.obj85.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(147.0,778.0,self.obj85)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj85.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj85)
    self.globalAndLocalPostcondition(self.obj85, rootNode)
    self.obj85.postAction( rootNode.CREATE )

    self.obj76=canStartProcess(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    # ID
    self.obj76.ID.setValue('RP|0')

    self.obj76.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(421.0,302.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    self.obj78=canStartProcess(self)
    self.obj78.isGraphObjectVisual = True

    if(hasattr(self.obj78, '_setHierarchicalLink')):
      self.obj78._setHierarchicalLink(False)

    # ID
    self.obj78.ID.setValue('RP|1')

    self.obj78.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(10.0,652.0,self.obj78)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj78.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj78)
    self.globalAndLocalPostcondition(self.obj78, rootNode)
    self.obj78.postAction( rootNode.CREATE )

    self.obj81=canStartProcess(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(False)

    # ID
    self.obj81.ID.setValue('RP|2')

    self.obj81.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(147.0,652.0,self.obj81)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj81.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj81)
    self.globalAndLocalPostcondition(self.obj81, rootNode)
    self.obj81.postAction( rootNode.CREATE )

    # Connections for obj44 (graphObject_: Obj0) named Player
    self.drawConnections(
(self.obj44,self.obj58,[434.0, 63.0, 367.81444792985104, 110.76476417998526, 292.0, 141.0],"true", 3),
(self.obj44,self.obj91,[434.0, 63.0, 568.0, 294.0],"true", 2) )
    # Connections for obj45 (graphObject_: Obj1) named Scout
    self.drawConnections(
(self.obj45,self.obj76,[444.0, 235.0, 423.0417786357556, 265.25314788988624, 421.0, 302.0],"true", 3) )
    # Connections for obj46 (graphObject_: Obj2) named Warrior
    self.drawConnections(
(self.obj46,self.obj78,[29.0, 571.0, 29.235745697868076, 613.7836934353024, 10.0, 652.0],"true", 3) )
    # Connections for obj47 (graphObject_: Obj3) named Student
    self.drawConnections(
(self.obj47,self.obj81,[186.0, 571.0, 157.489983302409, 607.161843812271, 147.0, 652.0],"true", 3) )
    # Connections for obj48 (graphObject_: Obj4) named KnArtName
    self.drawConnections(
 )
    # Connections for obj49 (graphObject_: Obj5) named TowerOfLondon
    self.drawConnections(
 )
    # Connections for obj50 (graphObject_: Obj6) named KillChief
    self.drawConnections(
(self.obj50,self.obj66,[25.0, 893.0, 156.7924880058632, 913.7663214177284, 284.0, 954.0],"true", 3) )
    # Connections for obj51 (graphObject_: Obj7) named LearnBackstory
    self.drawConnections(
(self.obj51,self.obj66,[320.0, 893.0, 310.6120746269472, 928.5825358454115, 284.0, 954.0],"true", 3) )
    # Connections for obj52 (graphObject_: Obj8) named ExploreLandmark
    self.drawConnections(
(self.obj52,self.obj84,[471.0, 705.0, 411.5685843424414, 713.8797069212493, 421.0, 778.0],"true", 3) )
    # Connections for obj53 (graphObject_: Obj9) named VisitInnerWard
    self.drawConnections(
(self.obj53,self.obj72,[455.0, 564.0, 428.67201865594404, 604.3960072079784, 421.0, 652.0],"true", 3) )
    # Connections for obj54 (graphObject_: Obj10) named VisitOuterWard
    self.drawConnections(
(self.obj54,self.obj72,[557.0, 567.0, 498.0, 616.0, 421.0, 652.0],"true", 3) )
    # Connections for obj55 (graphObject_: Obj11) named VisitInnermostWard
    self.drawConnections(
(self.obj55,self.obj72,[332.0, 564.0, 369.4689939353234, 615.1109038608661, 421.0, 652.0],"true", 3) )
    # Connections for obj56 (graphObject_: Obj12) named KillMinions
    self.drawConnections(
(self.obj56,self.obj66,[169.0, 893.0, 231.18593471839486, 914.6658607767965, 284.0, 954.0],"true", 3) )
    # Connections for obj57 (graphObject_: Obj13) named DecipherClues
    self.drawConnections(
(self.obj57,self.obj66,[455.0, 893.0, 372.85987451405515, 932.9186646213676, 284.0, 954.0],"true", 3) )
    # Connections for obj73 (graphObject_: Obj36) named 
    self.drawConnections(
(self.obj73,self.obj77,[431.0, 363.0, 416.29857499854666, 380.57464374963666, 421.0, 403.0],"true", 3) )
    # Connections for obj74 (graphObject_: Obj37) named 
    self.drawConnections(
(self.obj74,self.obj80,[20.0, 713.0, 24.88371697650617, 747.0205718425394, 10.0, 778.0],"true", 3) )
    # Connections for obj75 (graphObject_: Obj38) named 
    self.drawConnections(
(self.obj75,self.obj85,[157.0, 713.0, 142.11628302349382, 743.9794281574606, 147.0, 778.0],"true", 3) )
    # Connections for obj58 (graphObject_: Obj14) of type canHaveRole
    self.drawConnections(
(self.obj58,self.obj45,[292.0, 141.0, 373.2596930228915, 179.4949644736223, 444.0, 235.0],"true", 3),
(self.obj58,self.obj46,[292.0, 141.0, 195.0, 216.0, 195.0, 298.0, 195.0, 342.0, 195.0, 399.0, 58.0, 451.0, 29.0, 571.0],"true", 7),
(self.obj58,self.obj47,[292.0, 141.0, 332.0, 216.0, 332.0, 298.0, 332.0, 342.0, 332.0, 399.0, 195.0, 451.0, 186.0, 571.0],"true", 7) )
    # Connections for obj91 (graphObject_: Obj66) of type canAccessKnArt
    self.drawConnections(
(self.obj91,self.obj48,[568.0, 294.0, 582.9557950271408, 346.06077405404335, 578.0, 400.0],"true", 3) )
    # Connections for obj66 (graphObject_: Obj30) of type isPartOfObjective
    self.drawConnections(
(self.obj66,self.obj49,[284.0, 954.0, 287.1303926521413, 1026.5942352282777, 347.0, 1025.0],"true", 3) )
    # Connections for obj72 (graphObject_: Obj34) of type isPartOfObjective
    self.drawConnections(
(self.obj72,self.obj52,[421.0, 652.0, 396.97157776758877, 703.5111254683464, 471.0, 705.0],"true", 3) )
    # Connections for obj84 (graphObject_: Obj54) of type isPartOfObjective
    self.drawConnections(
(self.obj84,self.obj57,[421.0, 778.0, 447.58966193466375, 832.6647956019254, 455.0, 893.0],"true", 3) )
    # Connections for obj77 (graphObject_: Obj41) of type hasObjective
    self.drawConnections(
(self.obj77,self.obj53,[421.0, 403.0, 469.0, 451.0, 455.0, 564.0],"true", 3),
(self.obj77,self.obj54,[421.0, 403.0, 503.4649367072628, 444.85432132847393, 557.0, 567.0],"true", 3),
(self.obj77,self.obj55,[421.0, 403.0, 332.0, 451.0, 332.0, 564.0],"true", 3) )
    # Connections for obj80 (graphObject_: Obj47) of type hasObjective
    self.drawConnections(
(self.obj80,self.obj50,[10.0, 778.0, 27.416004111862218, 834.2066081593223, 25.0, 893.0],"true", 3),
(self.obj80,self.obj56,[10.0, 778.0, 95.36048605807203, 827.3972410153613, 169.0, 893.0],"true", 3) )
    # Connections for obj85 (graphObject_: Obj56) of type hasObjective
    self.drawConnections(
(self.obj85,self.obj57,[147.0, 778.0, 297.5021024047178, 844.8682822551906, 455.0, 893.0],"true", 3),
(self.obj85,self.obj51,[147.0, 778.0, 227.96411178736219, 843.8279013981421, 320.0, 893.0],"true", 3) )
    # Connections for obj76 (graphObject_: Obj39) of type canStartProcess
    self.drawConnections(
(self.obj76,self.obj73,[421.0, 302.0, 416.13172334894466, 334.1177502706648, 431.0, 363.0],"true", 3) )
    # Connections for obj78 (graphObject_: Obj43) of type canStartProcess
    self.drawConnections(
(self.obj78,self.obj74,[10.0, 652.0, 24.86827665105534, 680.8822497293352, 20.0, 713.0],"true", 3) )
    # Connections for obj81 (graphObject_: Obj49) of type canStartProcess
    self.drawConnections(
(self.obj81,self.obj75,[147.0, 652.0, 142.13172334894466, 684.1177502706648, 157.0, 713.0],"true", 3) )

newfunction = MinionWars_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
