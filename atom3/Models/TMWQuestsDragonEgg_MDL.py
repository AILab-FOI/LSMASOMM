"""
__TMWQuestsDragonEgg_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Wed May  2 00:07:08 2018
________________________________________________________________________________
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

def TMWQuestsDragonEgg_MDL(self, rootNode, LSMASOMMRootNode=None):

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
        LSMASOMMRootNode.name.setValue('TMW')

        # title
        LSMASOMMRootNode.title.setValue('QuestDragonEgg')
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
    self.obj44.ID.setValue('O|0')

    # name
    self.obj44.name.setValue('FinishQuestForTheDragonEgg')

    self.obj44.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(544.0,31.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.1
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

    # ofActions
    self.obj45.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj45.ofActions.setValue(lcobj2)

    # Measurement
    self.obj45.Measurement.setValue('\n')
    self.obj45.Measurement.setHeight(4)

    # Reward
    self.obj45.Reward.setValue('\n')
    self.obj45.Reward.setHeight(4)

    # ID
    self.obj45.ID.setValue('O|1')

    # name
    self.obj45.name.setValue('HatchDragonEgg')

    self.obj45.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(464.0,131.0,self.obj45)
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

    # ofActions
    self.obj46.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj46.ofActions.setValue(lcobj2)

    # Measurement
    self.obj46.Measurement.setValue('\n')
    self.obj46.Measurement.setHeight(4)

    # Reward
    self.obj46.Reward.setValue('\n')
    self.obj46.Reward.setHeight(4)

    # ID
    self.obj46.ID.setValue('O|2')

    # name
    self.obj46.name.setValue('LearnSpell')

    self.obj46.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(694.0,131.0,self.obj46)
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
    self.obj47.ID.setValue('O|3')

    # name
    self.obj47.name.setValue('BrewHatchingPotion')

    self.obj47.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(220.0,280.0,self.obj47)
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
    self.obj48.ofActions.setValue(lcobj2)

    # Measurement
    self.obj48.Measurement.setValue('\n')
    self.obj48.Measurement.setHeight(4)

    # Reward
    self.obj48.Reward.setValue('\n')
    self.obj48.Reward.setHeight(4)

    # ID
    self.obj48.ID.setValue('O|4')

    # name
    self.obj48.name.setValue('TransportDragonEgg')

    self.obj48.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(520.0,280.0,self.obj48)
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
    self.obj49.ofActions.setValue(lcobj2)

    # Measurement
    self.obj49.Measurement.setValue('\n')
    self.obj49.Measurement.setHeight(4)

    # Reward
    self.obj49.Reward.setValue('\n')
    self.obj49.Reward.setHeight(4)

    # ID
    self.obj49.ID.setValue('O|5')

    # name
    self.obj49.name.setValue('FindEggHermit')

    self.obj49.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(680.0,280.0,self.obj49)
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
    self.obj50.ofActions.setValue(lcobj2)

    # Measurement
    self.obj50.Measurement.setValue('\n')
    self.obj50.Measurement.setHeight(4)

    # Reward
    self.obj50.Reward.setValue('\n')
    self.obj50.Reward.setHeight(4)

    # ID
    self.obj50.ID.setValue('O|6')

    # name
    self.obj50.name.setValue('FindDragonEgg')

    self.obj50.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(380.0,280.0,self.obj50)
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
    self.obj51.ofActions.setValue(lcobj2)

    # Measurement
    self.obj51.Measurement.setValue('\n')
    self.obj51.Measurement.setHeight(4)

    # Reward
    self.obj51.Reward.setValue('\n')
    self.obj51.Reward.setHeight(4)

    # ID
    self.obj51.ID.setValue('O|7')

    # name
    self.obj51.name.setValue('GatherPotionIngredients')

    self.obj51.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(60.0,280.0,self.obj51)
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
    self.obj52.ofActions.setValue(lcobj2)

    # Measurement
    self.obj52.Measurement.setValue('\n')
    self.obj52.Measurement.setHeight(4)

    # Reward
    self.obj52.Reward.setValue('\n')
    self.obj52.Reward.setHeight(4)

    # ID
    self.obj52.ID.setValue('O|8')

    # name
    self.obj52.name.setValue('FindItemIngredient')

    self.obj52.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(50.0,430.0,self.obj52)
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

    # ofActions
    self.obj53.ofActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj53.ofActions.setValue(lcobj2)

    # Measurement
    self.obj53.Measurement.setValue('\n')
    self.obj53.Measurement.setHeight(4)

    # Reward
    self.obj53.Reward.setValue('\n')
    self.obj53.Reward.setHeight(4)

    # ID
    self.obj53.ID.setValue('O|9')

    # name
    self.obj53.name.setValue('HarvestItemIngredient')

    self.obj53.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(240.0,430.0,self.obj53)
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

    self.obj75=isPartOfObjective(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(True)

    # ID
    self.obj75.ID.setValue('pO|0')

    self.obj75.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(177.0,398.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj80=isPartOfObjective(self)
    self.obj80.isGraphObjectVisual = True

    if(hasattr(self.obj80, '_setHierarchicalLink')):
      self.obj80._setHierarchicalLink(True)

    # ID
    self.obj80.ID.setValue('pO|1')

    self.obj80.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(503.0,249.0,self.obj80)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj80.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj80)
    self.globalAndLocalPostcondition(self.obj80, rootNode)
    self.obj80.postAction( rootNode.CREATE )

    self.obj82=isPartOfObjective(self)
    self.obj82.isGraphObjectVisual = True

    if(hasattr(self.obj82, '_setHierarchicalLink')):
      self.obj82._setHierarchicalLink(True)

    # ID
    self.obj82.ID.setValue('pO|2')

    self.obj82.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(609.0,137.0,self.obj82)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj82.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj82)
    self.globalAndLocalPostcondition(self.obj82, rootNode)
    self.obj82.postAction( rootNode.CREATE )

    self.obj74=precedentTo(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(True)

    # ID
    self.obj74.ID.setValue('OpO|0')

    self.obj74.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(203.489587602,474.039234071,self.obj74)
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

    self.obj76=precedentTo(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(True)

    # ID
    self.obj76.ID.setValue('OpO|1')

    self.obj76.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(202.120938013,322.2623221,self.obj76)
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

    self.obj77=precedentTo(self)
    self.obj77.isGraphObjectVisual = True

    if(hasattr(self.obj77, '_setHierarchicalLink')):
      self.obj77._setHierarchicalLink(True)

    # ID
    self.obj77.ID.setValue('OpO|2')

    self.obj77.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(353.454745276,323.455638382,self.obj77)
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
    self.obj78.ID.setValue('OpO|3')

    self.obj78.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(501.991811703,335.007768111,self.obj78)
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
    self.obj79.ID.setValue('OpO|4')

    self.obj79.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(653.376888985,330.342413802,self.obj79)
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

    self.obj81=precedentTo(self)
    self.obj81.isGraphObjectVisual = True

    if(hasattr(self.obj81, '_setHierarchicalLink')):
      self.obj81._setHierarchicalLink(True)

    # ID
    self.obj81.ID.setValue('OpO|5')

    self.obj81.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(609.357627945,190.638564425,self.obj81)
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

    # Connections for obj44 (graphObject_: Obj0) named FinishQuestForTheDragonEgg
    self.drawConnections(
 )
    # Connections for obj45 (graphObject_: Obj1) named HatchDragonEgg
    self.drawConnections(
(self.obj45,self.obj81,[713.5040855626298, 414.61876178946295, 609.3576279446208, 190.6385644254878],"true", 0),
(self.obj45,self.obj82,[713.5040855626298, 414.61876178946295, 609.0, 137.0],"true", 0) )
    # Connections for obj46 (graphObject_: Obj2) named LearnSpell
    self.drawConnections(
(self.obj46,self.obj82,[1197.9501491946323, 297.20372094102413, 609.0, 137.0],"true", 0) )
    # Connections for obj47 (graphObject_: Obj3) named BrewHatchingPotion
    self.drawConnections(
(self.obj47,self.obj77,[380.61803230937585, 245.72047989466682, 353.4547452756782, 323.45563838240116],"true", 0),
(self.obj47,self.obj80,[380.61803230937585, 245.72047989466682, 503.0, 249.0],"true", 0) )
    # Connections for obj48 (graphObject_: Obj4) named TransportDragonEgg
    self.drawConnections(
(self.obj48,self.obj79,[768.1966051352533, 463.7319071577135, 653.3768889850651, 330.34241380246567],"true", 0),
(self.obj48,self.obj80,[768.1966051352533, 463.7319071577135, 503.0, 249.0],"true", 0) )
    # Connections for obj49 (graphObject_: Obj5) named FindEggHermit
    self.drawConnections(
(self.obj49,self.obj80,[961.6229558403763, 493.8694299102599, 503.0, 249.0],"true", 0) )
    # Connections for obj50 (graphObject_: Obj6) named FindDragonEgg
    self.drawConnections(
(self.obj50,self.obj78,[356.5040855626298, 465.61876178946295, 501.9918117034965, 335.0077681105661],"true", 0),
(self.obj50,self.obj80,[356.5040855626298, 465.61876178946295, 503.0, 249.0],"true", 0) )
    # Connections for obj51 (graphObject_: Obj7) named GatherPotionIngredients
    self.drawConnections(
(self.obj51,self.obj76,[174.70820634999927, 412.068057834965, 202.1209380131943, 322.26232210038927],"true", 0) )
    # Connections for obj52 (graphObject_: Obj8) named FindItemIngredient
    self.drawConnections(
(self.obj52,self.obj74,[-235.0, 141.0, 203.48958760238037, 474.03923407073523],"true", 0),
(self.obj52,self.obj75,[-235.0, 141.0, 177.0, 398.0],"true", 0) )
    # Connections for obj53 (graphObject_: Obj9) named HarvestItemIngredient
    self.drawConnections(
(self.obj53,self.obj75,[607.7082063499993, 576.068057834965, 177.0, 398.0],"true", 0) )
    # Connections for obj75 (graphObject_: Obj12) of type isPartOfObjective
    self.drawConnections(
(self.obj75,self.obj51,[177.0, 398.0, 178.2629049361234, 364.86034626012236, 130.61803230937585, 324.7204798946668],"true", 3) )
    # Connections for obj80 (graphObject_: Obj22) of type isPartOfObjective
    self.drawConnections(
(self.obj80,self.obj45,[503.0, 249.0, 474.52482250400703, 207.10198421398871, 514.9501491946326, 176.20372094102413],"true", 3) )
    # Connections for obj82 (graphObject_: Obj26) of type isPartOfObjective
    self.drawConnections(
(self.obj82,self.obj44,[609.0, 137.0, 597.5812361835442, 111.09174255367876, 633.208815266094, 76.1835387990368],"true", 3) )
    # Connections for obj74 (graphObject_: Obj10) of type precedentTo
    self.drawConnections(
(self.obj74,self.obj53,[203.48958760238037, 474.03923407073523, 233.80899091692658, 491.6543125298483, 304.98581960818404, 474.52837167141706],"true", 3) )
    # Connections for obj76 (graphObject_: Obj14) of type precedentTo
    self.drawConnections(
(self.obj76,self.obj47,[202.1209380131943, 322.26232210038927, 223.34245132650778, 311.9868925740883, 279.5040855626298, 324.61876178946295],"true", 3) )
    # Connections for obj77 (graphObject_: Obj16) of type precedentTo
    self.drawConnections(
(self.obj77,self.obj50,[353.4547452756782, 323.45563838240116, 398.37787516883407, 298.2339247244638, 426.1966051352533, 324.7319071577135],"true", 3) )
    # Connections for obj78 (graphObject_: Obj18) of type precedentTo
    self.drawConnections(
(self.obj78,self.obj48,[501.9918117034965, 335.0077681105661, 536.3483993797774, 326.79214879870267, 580.6229558403768, 324.8694299102599],"true", 3) )
    # Connections for obj79 (graphObject_: Obj20) of type precedentTo
    self.drawConnections(
(self.obj79,self.obj49,[653.3768889850651, 330.34241380246567, 690.9238335175013, 329.0743307794161, 723.8107339701214, 324.7970978180615],"true", 3) )
    # Connections for obj81 (graphObject_: Obj24) of type precedentTo
    self.drawConnections(
(self.obj81,self.obj46,[609.3576279446208, 190.6385644254878, 669.2102720802009, 192.3413202520697, 725.3607257369526, 176.0147442473517],"true", 3) )

newfunction = TMWQuestsDragonEgg_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
