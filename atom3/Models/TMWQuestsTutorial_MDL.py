"""
__TMWQuestsTutorial_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Tue May  1 03:32:52 2018
_______________________________________________________________________________
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

def TMWQuestsTutorial_MDL(self, rootNode, LSMASOMMRootNode=None):

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
    self.obj44.ID.setValue('O|0')

    # name
    self.obj44.name.setValue('FinishTutorial')

    self.obj44.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1549,606,self.obj44)
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
    self.obj48.ofActions.setValue(lcobj2)

    # Measurement
    self.obj48.Measurement.setValue('\n')
    self.obj48.Measurement.setHeight(4)

    # Reward
    self.obj48.Reward.setValue('\n')
    self.obj48.Reward.setHeight(4)

    # ID
    self.obj48.ID.setValue('O|1')

    # name
    self.obj48.name.setValue('answerNPCServerInitial')

    self.obj48.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(0,1111,self.obj48)
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
    self.obj49.ID.setValue('O|2')

    # name
    self.obj49.name.setValue('goToNPCSorfina')

    self.obj49.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(157,1010,self.obj49)
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
    self.obj50.ID.setValue('O|3')

    # name
    self.obj50.name.setValue('talkToSorfina')

    self.obj50.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(273,909,self.obj50)
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
    self.obj51.ID.setValue('O|4')

    # name
    self.obj51.name.setValue('goToNPCCarpet')

    self.obj51.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(367,808,self.obj51)
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
    self.obj52.ID.setValue('O|5')

    # name
    self.obj52.name.setValue('talkToNPCSorfina')

    self.obj52.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(481,707,self.obj52)
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
    self.obj63.ofActions.setValue(lcobj2)

    # Measurement
    self.obj63.Measurement.setValue('\n')
    self.obj63.Measurement.setHeight(4)

    # Reward
    self.obj63.Reward.setValue('\n')
    self.obj63.Reward.setHeight(4)

    # ID
    self.obj63.ID.setValue('O|6')

    # name
    self.obj63.name.setValue('goToLocation2924')

    self.obj63.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(604,606,self.obj63)
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
    self.obj64.ofActions.setValue(lcobj2)

    # Measurement
    self.obj64.Measurement.setValue('\n')
    self.obj64.Measurement.setHeight(4)

    # Reward
    self.obj64.Reward.setValue('\n')
    self.obj64.Reward.setHeight(4)

    # ID
    self.obj64.ID.setValue('O|7')

    # name
    self.obj64.name.setValue('talkToNPCDresser')

    self.obj64.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(727,505,self.obj64)
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
    self.obj65.ofActions.setValue(lcobj2)

    # Measurement
    self.obj65.Measurement.setValue('\n')
    self.obj65.Measurement.setHeight(4)

    # Reward
    self.obj65.Reward.setValue('\n')
    self.obj65.Reward.setHeight(4)

    # ID
    self.obj65.ID.setValue('O|8')

    # name
    self.obj65.name.setValue('equipItemRaggedShorts')

    self.obj65.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(855,404,self.obj65)
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
    self.obj66.ofActions.setValue(lcobj2)

    # Measurement
    self.obj66.Measurement.setValue('\n')
    self.obj66.Measurement.setHeight(4)

    # Reward
    self.obj66.Reward.setValue('\n')
    self.obj66.Reward.setHeight(4)

    # ID
    self.obj66.ID.setValue('O|9')

    # name
    self.obj66.name.setValue('equipItemCottonShirt')

    self.obj66.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1012,303,self.obj66)
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
    self.obj75.ID.setValue('O|10')

    # name
    self.obj75.name.setValue('equipItems')

    self.obj75.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1391,404,self.obj75)
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
    self.obj78.ofActions.setValue(lcobj2)

    # Measurement
    self.obj78.Measurement.setValue('\n')
    self.obj78.Measurement.setHeight(4)

    # Reward
    self.obj78.Reward.setValue('\n')
    self.obj78.Reward.setHeight(4)

    # ID
    self.obj78.ID.setValue('O|11')

    # name
    self.obj78.name.setValue('goToNPCSorfina')

    self.obj78.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1152,202,self.obj78)
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
    self.obj81.ofActions.setValue(lcobj2)

    # Measurement
    self.obj81.Measurement.setValue('\n')
    self.obj81.Measurement.setHeight(4)

    # Reward
    self.obj81.Reward.setValue('\n')
    self.obj81.Reward.setHeight(4)

    # ID
    self.obj81.ID.setValue('O|12')

    # name
    self.obj81.name.setValue('talkToNPCSorfina')

    self.obj81.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1268,101,self.obj81)
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
    self.obj84.ofActions.setValue(lcobj2)

    # Measurement
    self.obj84.Measurement.setValue('\n')
    self.obj84.Measurement.setHeight(4)

    # Reward
    self.obj84.Reward.setValue('\n')
    self.obj84.Reward.setHeight(4)

    # ID
    self.obj84.ID.setValue('O|13')

    # name
    self.obj84.name.setValue('goToLocation4431')

    self.obj84.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(1391,0,self.obj84)
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
       new_obj = graph_isPartOfObjective(1278.0,414.0,self.obj87)
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
       new_obj = graph_isPartOfObjective(1524.0,616.0,self.obj88)
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

    self.obj89=precedentTo(self)
    self.obj89.isGraphObjectVisual = True

    if(hasattr(self.obj89, '_setHierarchicalLink')):
      self.obj89._setHierarchicalLink(True)

    # ID
    self.obj89.ID.setValue('OpO|0')

    self.obj89.graphClass_= graph_precedentTo
    if self.genGraphics:
       new_obj = graph_precedentTo(133.032200614,1097.50129586,self.obj89)
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
       new_obj = graph_precedentTo(252.431911952,997.100295822,self.obj90)
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
       new_obj = graph_precedentTo(357.29100553,896.301940948,self.obj91)
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
       new_obj = graph_precedentTo(468.94687696,795.202385591,self.obj92)
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
       new_obj = graph_precedentTo(590.117789754,693.815682499,self.obj93)
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
       new_obj = graph_precedentTo(714.186087751,592.890841804,self.obj94)
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
       new_obj = graph_precedentTo(848.750804518,491.653045739,self.obj95)
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
       new_obj = graph_precedentTo(994.342270038,390.458275517,self.obj96)
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
       new_obj = graph_precedentTo(1131.33341277,289.50064029,self.obj97)
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
       new_obj = graph_precedentTo(1255.23224683,188.796493523,self.obj98)
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
       new_obj = graph_precedentTo(1376.7816079,87.8703144514,self.obj99)
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

    # Connections for obj44 (graphObject_: Obj0) named FinishTutorial
    self.drawConnections(
 )
    # Connections for obj48 (graphObject_: Obj1) named answerNPCServerInitial
    self.drawConnections(
(self.obj48,self.obj88,[71.3730502873575, 1156.0302404320985, 200.0, 1144.0, 316.0, 1137.0, 410.0, 1144.0, 524.0, 1147.0, 647.0, 1147.0, 770.0, 1148.0, 898.0, 1158.0, 1055.0, 1152.0, 1195.0, 1144.0, 1311.0, 1147.0, 1434.0, 1147.0, 1524.0, 616.0],"true", 13),
(self.obj48,self.obj89,[71.3730502873575, 1156.0302404320985, 99.21079586086235, 1122.7596533576345, 133.03220061434104, 1097.5012958616283],"true", 3) )
    # Connections for obj49 (graphObject_: Obj2) named goToNPCSorfina
    self.drawConnections(
(self.obj49,self.obj88,[206.6586693012722, 1054.996810448074, 316.0, 1036.0, 410.0, 1043.0, 524.0, 1046.0, 647.0, 1046.0, 770.0, 1047.0, 898.0, 1057.0, 1055.0, 1051.0, 1195.0, 1043.0, 1311.0, 1046.0, 1434.0, 1046.0, 1524.0, 616.0],"true", 12),
(self.obj49,self.obj90,[206.6586693012722, 1054.996810448074, 226.07935824720988, 1022.4447616950392, 252.43191195176954, 997.1002958217343],"true", 3) )
    # Connections for obj50 (graphObject_: Obj3) named talkToSorfina
    self.drawConnections(
(self.obj50,self.obj88,[312.0688841195108, 953.6189469548544, 410.0, 942.0, 524.0, 945.0, 647.0, 945.0, 770.0, 946.0, 898.0, 956.0, 1055.0, 950.0, 1195.0, 942.0, 1311.0, 945.0, 1434.0, 945.0, 1524.0, 616.0],"true", 11),
(self.obj50,self.obj91,[312.0688841195108, 953.6189469548544, 331.2157895628757, 921.3549442187007, 357.2910055298654, 896.3019409478243],"true", 3) )
    # Connections for obj51 (graphObject_: Obj4) named goToNPCCarpet
    self.drawConnections(
(self.obj51,self.obj88,[416.3697479874695, 853.4069338713489, 524.0, 844.0, 647.0, 844.0, 770.0, 845.0, 898.0, 855.0, 1055.0, 849.0, 1195.0, 841.0, 1311.0, 844.0, 1434.0, 844.0, 1524.0, 616.0],"true", 10),
(self.obj51,self.obj92,[416.3697479874695, 853.4069338713489, 439.40555395732656, 820.507349889496, 468.94687695967264, 795.20238559134],"true", 3) )
    # Connections for obj52 (graphObject_: Obj5) named talkToNPCSorfina
    self.drawConnections(
(self.obj52,self.obj88,[534.5350399968538, 752.1870766787247, 647.0, 743.0, 770.0, 744.0, 898.0, 754.0, 1055.0, 748.0, 1195.0, 740.0, 1311.0, 743.0, 1434.0, 743.0, 1524.0, 616.0],"true", 9),
(self.obj52,self.obj93,[534.5350399968538, 752.1870766787247, 559.1612000487191, 719.1307962865828, 590.1177897541593, 693.8156824991034],"true", 3) )
    # Connections for obj63 (graphObject_: Obj6) named goToLocation2924
    self.drawConnections(
(self.obj63,self.obj88,[658.3613988186144, 650.9266215288071, 770.0, 643.0, 898.0, 653.0, 1055.0, 647.0, 1195.0, 639.0, 1311.0, 642.0, 1434.0, 642.0, 1524.0, 616.0],"true", 8),
(self.obj63,self.obj94,[658.3613988186144, 650.9266215288071, 683.1285684811872, 618.0218466081603, 714.1860877509465, 592.8908418037036],"true", 3) )
    # Connections for obj64 (graphObject_: Obj7) named talkToNPCDresser
    self.drawConnections(
(self.obj64,self.obj88,[782.5914758976514, 550.40260231098, 898.0, 552.0, 1055.0, 546.0, 1195.0, 538.0, 1311.0, 541.0, 1434.0, 541.0, 1524.0, 616.0],"true", 7),
(self.obj64,self.obj95,[782.5914758976514, 550.40260231098, 812.7949985829032, 516.9378595566169, 848.7508045179128, 491.6530457392652],"true", 3) )
    # Connections for obj65 (graphObject_: Obj8) named equipItemRaggedShorts
    self.drawConnections(
(self.obj65,self.obj87,[926.4146996376899, 449.26334704157307, 1055.0, 445.0, 1195.0, 437.0, 1278.0, 414.0],"true", 4),
(self.obj65,self.obj96,[926.4146996376899, 449.26334704157307, 957.5469982511057, 415.73980609733036, 994.3422700382985, 390.4582755166509],"true", 3) )
    # Connections for obj66 (graphObject_: Obj9) named equipItemCottonShirt
    self.drawConnections(
(self.obj66,self.obj87,[1073.5957867864608, 348.1372247188551, 1195.0, 336.0, 1278.0, 414.0],"true", 3),
(self.obj66,self.obj97,[1073.5957867864608, 348.1372247188551, 1099.3545684710691, 314.9038711694604, 1131.3334127734379, 289.5006402903139],"true", 3) )
    # Connections for obj75 (graphObject_: Obj10) named equipItems
    self.drawConnections(
(self.obj75,self.obj88,[1424.0427765396694, 449.1379258091438, 1465.4428316526357, 537.707870022385, 1524.0, 616.0],"true", 3) )
    # Connections for obj78 (graphObject_: Obj11) named goToNPCSorfina
    self.drawConnections(
(self.obj78,self.obj88,[1201.5111639959364, 246.52430120226927, 1311.0, 238.0, 1434.0, 238.0, 1524.0, 616.0],"true", 4),
(self.obj78,self.obj98,[1201.5111639959364, 246.52430120226927, 1225.172928243175, 213.81750461994133, 1255.2322468257944, 188.79649352290025],"true", 3) )
    # Connections for obj81 (graphObject_: Obj12) named talkToNPCSorfina
    self.drawConnections(
(self.obj81,self.obj88,[1321.7484383264145, 146.44025681410494, 1434.0, 137.0, 1524.0, 616.0],"true", 3),
(self.obj81,self.obj99,[1321.7484383264145, 146.44025681410494, 1346.0755144922489, 113.3046967500473, 1376.781607904176, 87.87031445137387],"true", 3) )
    # Connections for obj84 (graphObject_: Obj13) named goToLocation4431
    self.drawConnections(
(self.obj84,self.obj88,[1444.5728119741234, 44.702727619411235, 1474.3816731543677, 331.72841410397757, 1524.0, 616.0],"true", 3) )
    # Connections for obj87 (graphObject_: Obj14) of type isPartOfObjective
    self.drawConnections(
(self.obj87,self.obj75,[1278.0, 414.0, 1348.682141177642, 441.2915100523963, 1424.0427765396694, 449.1379258091438],"true", 3) )
    # Connections for obj88 (graphObject_: Obj16) of type isPartOfObjective
    self.drawConnections(
(self.obj88,self.obj44,[1524.0, 616.0, 1551.718465689899, 642.3619287727334, 1588.9521122680558, 651.132344459216],"true", 3) )
    # Connections for obj89 (graphObject_: Obj18) of type precedentTo
    self.drawConnections(
(self.obj89,self.obj49,[133.03220061434104, 1097.5012958616283, 166.8536053678197, 1072.2429383656222, 206.6586693012722, 1054.996810448074],"true", 3) )
    # Connections for obj90 (graphObject_: Obj20) of type precedentTo
    self.drawConnections(
(self.obj90,self.obj50,[252.43191195176954, 997.1002958217343, 278.7844656563292, 971.7558299484294, 312.0688841195108, 953.6189469548544],"true", 3) )
    # Connections for obj91 (graphObject_: Obj22) of type precedentTo
    self.drawConnections(
(self.obj91,self.obj51,[357.2910055298654, 896.3019409478243, 383.3662214968551, 871.2489376769479, 416.3697479874695, 853.4069338713489],"true", 3) )
    # Connections for obj92 (graphObject_: Obj24) of type precedentTo
    self.drawConnections(
(self.obj92,self.obj52,[468.94687695967264, 795.20238559134, 498.4881999620187, 769.8974212931839, 534.5350399968538, 752.1870766787247],"true", 3) )
    # Connections for obj93 (graphObject_: Obj26) of type precedentTo
    self.drawConnections(
(self.obj93,self.obj63,[590.1177897541593, 693.8156824991034, 621.0743794595994, 668.500568711624, 658.3613988186144, 650.9266215288071],"true", 3) )
    # Connections for obj94 (graphObject_: Obj28) of type precedentTo
    self.drawConnections(
(self.obj94,self.obj64,[714.1860877509465, 592.8908418037036, 745.2436070207058, 567.7598369992468, 782.5914758976514, 550.40260231098],"true", 3) )
    # Connections for obj95 (graphObject_: Obj30) of type precedentTo
    self.drawConnections(
(self.obj95,self.obj65,[848.7508045179128, 491.6530457392652, 884.7066104529224, 466.3682319219135, 926.4146996376899, 449.26334704157307],"true", 3) )
    # Connections for obj96 (graphObject_: Obj32) of type precedentTo
    self.drawConnections(
(self.obj96,self.obj66,[994.3422700382985, 390.4582755166509, 1031.1375418254913, 365.1767449359714, 1073.5957867864608, 348.1372247188551],"true", 3) )
    # Connections for obj97 (graphObject_: Obj34) of type precedentTo
    self.drawConnections(
(self.obj97,self.obj78,[1131.3334127734379, 289.5006402903139, 1163.3122570758067, 264.09740941116746, 1201.5111639959364, 246.52430120226927],"true", 3) )
    # Connections for obj98 (graphObject_: Obj36) of type precedentTo
    self.drawConnections(
(self.obj98,self.obj81,[1255.2322468257944, 188.79649352290025, 1285.2915654084138, 163.77548242585917, 1321.7484383264145, 146.44025681410494],"true", 3) )
    # Connections for obj99 (graphObject_: Obj38) of type precedentTo
    self.drawConnections(
(self.obj99,self.obj84,[1376.781607904176, 87.87031445137387, 1407.4877013161033, 62.43593215270044, 1444.5728119741234, 44.702727619411235],"true", 3) )

newfunction = TMWQuestsTutorial_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
