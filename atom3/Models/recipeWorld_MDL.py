"""
__recipeWorld_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Wed Jan 25 13:18:53 2017
_________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from OrganisationalKnArt import *
from IndividualKnArt import *
from Objective import *
from Process import *
from canHaveRole import *
from canAccessKnArt import *
from isPartOfObjective import *
from hasObjective import *
from canStartProcess import *
from graph_canHaveRole import *
from graph_OrganisationalKnArt import *
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

def recipeWorld_MDL(self, rootNode, LSMASOMMRootNode=None):

    # --- Generating attributes code for ASG LSMASOMM ---
    if( LSMASOMMRootNode ): 
        # author
        LSMASOMMRootNode.author.setValue('Annonymous')

        # description
        LSMASOMMRootNode.description.setValue('\n')
        LSMASOMMRootNode.description.setHeight(15)

        # name
        LSMASOMMRootNode.name.setValue('recipeWorld')

        # title
        LSMASOMMRootNode.title.setValue('')
        LSMASOMMRootNode.title.setNone()
    # --- ASG attributes over ---


    self.obj44=OrgUnit(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # Individual
    self.obj44.Individual.setValue(('1', 1))
    self.obj44.Individual.config = 0

    # hasActions
    self.obj44.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj44.hasActions.setValue(lcobj2)

    # ID
    self.obj44.ID.setValue('OrgUnit44')

    # name
    self.obj44.name.setValue('Agent')

    # UnitSize
    self.obj44.UnitSize.setValue('Individual')

    self.obj44.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(0,0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    cobj2=ATOM3String('AnswerQuery', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Produce', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Initialise', 20)
    lcobj2.append(cobj2)
    self.obj45.hasActions.setValue(lcobj2)

    # ID
    self.obj45.ID.setValue('Role45')

    # name
    self.obj45.name.setValue('Factory')

    self.obj45.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(213,0,self.obj45)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    cobj2=ATOM3String('SearchForFactories', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('CheckFactoryAvailability', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('WaitFactoryAnswer', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('StartProduction', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('FinishProduction', 20)
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Initialise', 20)
    lcobj2.append(cobj2)
    self.obj46.hasActions.setValue(lcobj2)

    # ID
    self.obj46.ID.setValue('Role46')

    # name
    self.obj46.name.setValue('Order')

    self.obj46.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(213,247,self.obj46)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj46.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46, rootNode)
    self.obj46.postAction( rootNode.CREATE )

    self.obj47=OrganisationalKnArt(self)
    self.obj47.isGraphObjectVisual = True

    if(hasattr(self.obj47, '_setHierarchicalLink')):
      self.obj47._setHierarchicalLink(False)

    # description
    self.obj47.description.setValue('KnArtDesc')

    # ID
    self.obj47.ID.setValue('DomainOntology')

    # name
    self.obj47.name.setValue('DomainOntology')

    # KnArtContent
    self.obj47.KnArtContent.setValue('#content of the artifact\n')
    self.obj47.KnArtContent.setHeight(15)

    self.obj47.graphClass_= graph_OrganisationalKnArt
    if self.genGraphics:
       new_obj = graph_OrganisationalKnArt(423,172,self.obj47)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrganisationalKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj48.ID.setValue('IndividualKnowledge')

    # name
    self.obj48.name.setValue('KnArtName')

    # KnArtContent
    self.obj48.KnArtContent.setValue('#content of the artifact\n')
    self.obj48.KnArtContent.setHeight(15)

    self.obj48.graphClass_= graph_IndividualKnArt
    if self.genGraphics:
       new_obj = graph_IndividualKnArt(132.0,416.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("IndividualKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj49.ID.setValue('STR0')

    # name
    self.obj49.name.setValue('ReceivedPart')

    # Measurement
    self.obj49.Measurement.setValue('\n\n\n  \n')
    self.obj49.Measurement.setHeight(4)

    self.obj49.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(449,0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj50.ID.setValue('STR1')

    # name
    self.obj50.name.setValue('ProducedPart')

    # Measurement
    self.obj50.Measurement.setValue('\n')
    self.obj50.Measurement.setHeight(4)

    self.obj50.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(449,82,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj51.ID.setValue('STR2')

    # name
    self.obj51.name.setValue('ChosenFactory')

    # Measurement
    self.obj51.Measurement.setValue('\n')
    self.obj51.Measurement.setHeight(4)

    self.obj51.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(515,247,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj52.ID.setValue('STR3')

    # name
    self.obj52.name.setValue('StartedProduction')

    # Measurement
    self.obj52.Measurement.setValue('\n')
    self.obj52.Measurement.setHeight(4)

    self.obj52.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(515,329,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj53.ID.setValue('STR4')

    # name
    self.obj53.name.setValue('FinishedProduction')

    # Measurement
    self.obj53.Measurement.setValue('\n')
    self.obj53.Measurement.setHeight(4)

    self.obj53.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(515,411,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
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
    self.obj54.ID.setValue('STR5')

    # name
    self.obj54.name.setValue('ProducedRecipe')

    # Measurement
    self.obj54.Measurement.setValue('\n')
    self.obj54.Measurement.setHeight(4)

    self.obj54.graphClass_= graph_Objective
    if self.genGraphics:
       new_obj = graph_Objective(826,411,self.obj54)
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

    self.obj55=Process(self)
    self.obj55.isGraphObjectVisual = True

    if(hasattr(self.obj55, '_setHierarchicalLink')):
      self.obj55._setHierarchicalLink(False)

    # Activities
    self.obj55.Activities.setValue('\n')
    self.obj55.Activities.setHeight(10)

    # description
    self.obj55.description.setValue('\n')
    self.obj55.description.setHeight(4)

    # ID
    self.obj55.ID.setValue('STR0')

    # name
    self.obj55.name.setValue('')
    self.obj55.name.setNone()

    # Name
    self.obj55.Name.setValue('')
    self.obj55.Name.setNone()

    self.obj55.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(369,82,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    self.obj55.postAction( rootNode.CREATE )

    self.obj56=Process(self)
    self.obj56.isGraphObjectVisual = True

    if(hasattr(self.obj56, '_setHierarchicalLink')):
      self.obj56._setHierarchicalLink(False)

    # Activities
    self.obj56.Activities.setValue('\n')
    self.obj56.Activities.setHeight(10)

    # description
    self.obj56.description.setValue('\n')
    self.obj56.description.setHeight(4)

    # ID
    self.obj56.ID.setValue('STR1')

    # name
    self.obj56.name.setValue('')
    self.obj56.name.setNone()

    # Name
    self.obj56.Name.setValue('')
    self.obj56.Name.setNone()

    self.obj56.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(369,0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.obj56.postAction( rootNode.CREATE )

    self.obj57=Process(self)
    self.obj57.isGraphObjectVisual = True

    if(hasattr(self.obj57, '_setHierarchicalLink')):
      self.obj57._setHierarchicalLink(False)

    # Activities
    self.obj57.Activities.setValue('\n')
    self.obj57.Activities.setHeight(10)

    # description
    self.obj57.description.setValue('\n')
    self.obj57.description.setHeight(4)

    # ID
    self.obj57.ID.setValue('STR2')

    # name
    self.obj57.name.setValue('')
    self.obj57.name.setNone()

    # Name
    self.obj57.Name.setValue('')
    self.obj57.Name.setNone()

    self.obj57.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(435,247,self.obj57)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj57.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj57)
    self.globalAndLocalPostcondition(self.obj57, rootNode)
    self.obj57.postAction( rootNode.CREATE )

    self.obj58=Process(self)
    self.obj58.isGraphObjectVisual = True

    if(hasattr(self.obj58, '_setHierarchicalLink')):
      self.obj58._setHierarchicalLink(False)

    # Activities
    self.obj58.Activities.setValue('\n')
    self.obj58.Activities.setHeight(10)

    # description
    self.obj58.description.setValue('\n')
    self.obj58.description.setHeight(4)

    # ID
    self.obj58.ID.setValue('STR3')

    # name
    self.obj58.name.setValue('')
    self.obj58.name.setNone()

    # Name
    self.obj58.Name.setValue('')
    self.obj58.Name.setNone()

    self.obj58.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(435,329,self.obj58)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj58.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj58)
    self.globalAndLocalPostcondition(self.obj58, rootNode)
    self.obj58.postAction( rootNode.CREATE )

    self.obj59=Process(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # Activities
    self.obj59.Activities.setValue('\n')
    self.obj59.Activities.setHeight(10)

    # description
    self.obj59.description.setValue('\n')
    self.obj59.description.setHeight(4)

    # ID
    self.obj59.ID.setValue('STR4')

    # name
    self.obj59.name.setValue('')
    self.obj59.name.setNone()

    # Name
    self.obj59.Name.setValue('')
    self.obj59.Name.setNone()

    self.obj59.graphClass_= graph_Process
    if self.genGraphics:
       new_obj = graph_Process(435,411,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Process", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=canHaveRole(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(True)

    self.obj60.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(148.0,190.0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=canAccessKnArt(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(False)

    self.obj61.graphClass_= graph_canAccessKnArt
    if self.genGraphics:
       new_obj = graph_canAccessKnArt(381.0,184.0,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canAccessKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    self.obj62=canAccessKnArt(self)
    self.obj62.isGraphObjectVisual = True

    if(hasattr(self.obj62, '_setHierarchicalLink')):
      self.obj62._setHierarchicalLink(False)

    self.obj62.graphClass_= graph_canAccessKnArt
    if self.genGraphics:
       new_obj = graph_canAccessKnArt(90.0,428.0,self.obj62)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canAccessKnArt", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj62.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj62)
    self.globalAndLocalPostcondition(self.obj62, rootNode)
    self.obj62.postAction( rootNode.CREATE )

    self.obj63=isPartOfObjective(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(True)

    self.obj63.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(663.0,26.0,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=isPartOfObjective(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(True)

    self.obj64.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(741.0,273.0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['Text Scale'] = 1.0
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=isPartOfObjective(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(True)

    self.obj65.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(760.0,355.0,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=isPartOfObjective(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(True)

    self.obj66.graphClass_= graph_isPartOfObjective
    if self.genGraphics:
       new_obj = graph_isPartOfObjective(771.0,437.0,self.obj66)
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

    self.obj67=hasObjective(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(False)

    self.obj67.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(435.294124822,14.0455572547,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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

    self.obj68.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(435.809006279,96.3738466577,self.obj68)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj68.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj68)
    self.globalAndLocalPostcondition(self.obj68, rootNode)
    self.obj68.postAction( rootNode.CREATE )

    self.obj69=hasObjective(self)
    self.obj69.isGraphObjectVisual = True

    if(hasattr(self.obj69, '_setHierarchicalLink')):
      self.obj69._setHierarchicalLink(False)

    self.obj69.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(501.724410246,261.134876669,self.obj69)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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

    self.obj70.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(501.430682142,343.163778777,self.obj70)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
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

    self.obj71.graphClass_= graph_hasObjective
    if self.genGraphics:
       new_obj = graph_hasObjective(501.767336361,425.019828421,self.obj71)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj71.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj71)
    self.globalAndLocalPostcondition(self.obj71, rootNode)
    self.obj71.postAction( rootNode.CREATE )

    self.obj72=canStartProcess(self)
    self.obj72.isGraphObjectVisual = True

    if(hasattr(self.obj72, '_setHierarchicalLink')):
      self.obj72._setHierarchicalLink(False)

    self.obj72.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(325.468713942,21.9855212625,self.obj72)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj72.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj72)
    self.globalAndLocalPostcondition(self.obj72, rootNode)
    self.obj72.postAction( rootNode.CREATE )

    self.obj73=canStartProcess(self)
    self.obj73.isGraphObjectVisual = True

    if(hasattr(self.obj73, '_setHierarchicalLink')):
      self.obj73._setHierarchicalLink(False)

    self.obj73.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(308.5,99.0,self.obj73)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj73.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj73)
    self.globalAndLocalPostcondition(self.obj73, rootNode)
    self.obj73.postAction( rootNode.CREATE )

    self.obj74=canStartProcess(self)
    self.obj74.isGraphObjectVisual = True

    if(hasattr(self.obj74, '_setHierarchicalLink')):
      self.obj74._setHierarchicalLink(False)

    self.obj74.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(357.784429858,264.871597535,self.obj74)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj74.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj74)
    self.globalAndLocalPostcondition(self.obj74, rootNode)
    self.obj74.postAction( rootNode.CREATE )

    self.obj75=canStartProcess(self)
    self.obj75.isGraphObjectVisual = True

    if(hasattr(self.obj75, '_setHierarchicalLink')):
      self.obj75._setHierarchicalLink(False)

    self.obj75.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(261.75,347.0,self.obj75)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj75.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj75)
    self.globalAndLocalPostcondition(self.obj75, rootNode)
    self.obj75.postAction( rootNode.CREATE )

    self.obj76=canStartProcess(self)
    self.obj76.isGraphObjectVisual = True

    if(hasattr(self.obj76, '_setHierarchicalLink')):
      self.obj76._setHierarchicalLink(False)

    self.obj76.graphClass_= graph_canStartProcess
    if self.genGraphics:
       new_obj = graph_canStartProcess(256.75,411.0,self.obj76)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj76.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj76)
    self.globalAndLocalPostcondition(self.obj76, rootNode)
    self.obj76.postAction( rootNode.CREATE )

    # Connections for obj44 (graphObject_: Obj0) named Agent
    self.drawConnections(
(self.obj44,self.obj60,[13.159697675852328, 28.849593105656027, 63.20327706005544, 186.92403479751357, 148.0, 190.0],"true", 3),
(self.obj44,self.obj62,[13.159697675852328, 28.849593105656027, 42.0, 428.0, 6.0, 416.0, 90.0, 428.0],"true", 4) )
    # Connections for obj45 (graphObject_: Obj1) named Factory
    self.drawConnections(
(self.obj45,self.obj61,[222.92418015121063, 23.78568773419022, 330.0, 184.0, 242.0, 158.0, 381.0, 184.0],"true", 4),
(self.obj45,self.obj72,[222.92418015121063, 23.78568773419022, 282.97252245100947, 23.89062123754042, 325.4687139416097, 21.985521262471085],"true", 3),
(self.obj45,self.obj73,[222.92418015121063, 23.78568773419022, 256.0, 97.0, 308.5, 99.0],"true", 3) )
    # Connections for obj46 (graphObject_: Obj2) named Order
    self.drawConnections(
(self.obj46,self.obj61,[222.80436475193437, 271.12055469251527, 330.0, 184.0, 291.0, 172.0, 381.0, 184.0],"true", 4),
(self.obj46,self.obj74,[222.80436475193437, 271.12055469251527, 298.6147163749491, 266.9993056802428, 357.78442985817634, 264.8715975346214],"true", 3),
(self.obj46,self.obj75,[222.80436475193437, 271.12055469251527, 234.0, 340.0, 261.75, 347.0],"true", 3),
(self.obj46,self.obj76,[222.80436475193437, 271.12055469251527, 229.0, 404.0, 256.75, 411.0],"true", 3) )
    # Connections for obj47 (graphObject_: Obj3) named DomainOntology
    self.drawConnections(
 )
    # Connections for obj48 (graphObject_: Obj4) named KnArtName
    self.drawConnections(
 )
    # Connections for obj49 (graphObject_: Obj5) named ReceivedPart
    self.drawConnections(
(self.obj49,self.obj63,[473.9432894239676, 31.573783276486324, 568.7663373728377, 38.782548506885604, 663.0, 26.0],"true", 3) )
    # Connections for obj50 (graphObject_: Obj6) named ProducedPart
    self.drawConnections(
 )
    # Connections for obj51 (graphObject_: Obj7) named ChosenFactory
    self.drawConnections(
(self.obj51,self.obj64,[539.9147105811605, 279.24549217014476, 640.146915775672, 266.12756588121493, 741.0, 273.0],"true", 3) )
    # Connections for obj52 (graphObject_: Obj8) named StartedProduction
    self.drawConnections(
(self.obj52,self.obj65,[540.4543604470932, 360.81401218069954, 650.491907620926, 367.9035014464772, 760.0, 355.0],"true", 3) )
    # Connections for obj53 (graphObject_: Obj9) named FinishedProduction
    self.drawConnections(
(self.obj53,self.obj66,[540.2989515814039, 442.83398126690423, 655.3966760385163, 429.920186529875, 771.0, 437.0],"true", 3) )
    # Connections for obj54 (graphObject_: Obj10) named ProducedRecipe
    self.drawConnections(
 )
    # Connections for obj55 (graphObject_: Obj11) named 
    self.drawConnections(
(self.obj55,self.obj68,[393.48582623951086, 98.15272040808202, 415.62268487726385, 92.3593207350572, 435.80900627902844, 96.37384665774437],"true", 3) )
    # Connections for obj56 (graphObject_: Obj12) named 
    self.drawConnections(
(self.obj56,self.obj67,[392.9089461136115, 16.165287833912885, 415.035538994596, 10.193433394067954, 435.294124822185, 14.045557254711314],"true", 3) )
    # Connections for obj57 (graphObject_: Obj13) named 
    self.drawConnections(
(self.obj57,self.obj69,[459.48321868484334, 262.6097221100297, 481.61653727144886, 256.9759341544135, 501.72441024552813, 261.13487666944224],"true", 3) )
    # Connections for obj58 (graphObject_: Obj14) named 
    self.drawConnections(
(self.obj58,self.obj70,[458.64744670787036, 345.1570107041184, 480.97895370680055, 339.24952840790075, 501.43068214160627, 343.16377877704605],"true", 3) )
    # Connections for obj59 (graphObject_: Obj15) named 
    self.drawConnections(
(self.obj59,self.obj71,[459.35544634207554, 426.82565181102837, 481.5314600512443, 421.0177460571811, 501.76733636107645, 425.01982842115007],"true", 3) )
    # Connections for obj60 (graphObject_: Obj16) of type canHaveRole
    self.drawConnections(
(self.obj60,self.obj45,[148.0, 190.0, 178.49771660944882, 198.37848877447306, 222.92418015121063, 23.78568773419022],"true", 3),
(self.obj60,self.obj46,[148.0, 190.0, 225.75, 232.0, 175.5, 193.0, 222.80436475193437, 271.12055469251527],"true", 4) )
    # Connections for obj61 (graphObject_: Obj18) of type canAccessKnArt
    self.drawConnections(
(self.obj61,self.obj47,[381.0, 184.0, 411.59232403329435, 199.77155890637525, 445.789031295974, 195.87058819564925],"true", 3) )
    # Connections for obj62 (graphObject_: Obj20) of type canAccessKnArt
    self.drawConnections(
(self.obj62,self.obj48,[90.0, 428.0, 123.53411477192952, 424.387620305451, 153.21831140380306, 440.40119613706327],"true", 3) )
    # Connections for obj63 (graphObject_: Obj22) of type isPartOfObjective
    self.drawConnections(
(self.obj63,self.obj50,[663.0, 26.0, 496.25, 112.0, 543.5, 82.0, 474.2311118465691, 114.2108240988307],"true", 4) )
    # Connections for obj64 (graphObject_: Obj24) of type isPartOfObjective
    self.drawConnections(
(self.obj64,self.obj52,[741.0, 273.0, 565.25, 359.0, 615.5, 329.0, 540.4543604470932, 360.81401218069954],"true", 4) )
    # Connections for obj65 (graphObject_: Obj26) of type isPartOfObjective
    self.drawConnections(
(self.obj65,self.obj53,[760.0, 355.0, 570.0, 441.0, 625.0, 411.0, 540.2989515814039, 442.83398126690423],"true", 4) )
    # Connections for obj66 (graphObject_: Obj28) of type isPartOfObjective
    self.drawConnections(
(self.obj66,self.obj54,[771.0, 437.0, 811.8259404137248, 429.7835061631077, 851.2799567314212, 442.5199024495719],"true", 3) )
    # Connections for obj67 (graphObject_: Obj30) of type hasObjective
    self.drawConnections(
(self.obj67,self.obj49,[435.294124822185, 14.045557254711314, 455.552710649774, 17.897681115354672, 473.9432894239676, 31.573783276486324],"true", 3) )
    # Connections for obj68 (graphObject_: Obj31) of type hasObjective
    self.drawConnections(
(self.obj68,self.obj50,[435.80900627902844, 96.37384665774437, 455.995327680793, 100.38837258043154, 474.2311118465691, 114.2108240988307],"true", 3) )
    # Connections for obj69 (graphObject_: Obj32) of type hasObjective
    self.drawConnections(
(self.obj69,self.obj51,[501.72441024552813, 261.13487666944224, 521.8322832196075, 265.293819184471, 539.9147105811605, 279.24549217014476],"true", 3) )
    # Connections for obj70 (graphObject_: Obj33) of type hasObjective
    self.drawConnections(
(self.obj70,self.obj52,[501.43068214160627, 343.16377877704605, 521.882410576412, 347.07802914619134, 540.4543604470932, 360.81401218069954],"true", 3) )
    # Connections for obj71 (graphObject_: Obj34) of type hasObjective
    self.drawConnections(
(self.obj71,self.obj53,[501.76733636107645, 425.01982842115007, 522.0032126709086, 429.021910785119, 540.2989515814039, 442.83398126690423],"true", 3) )
    # Connections for obj72 (graphObject_: Obj35) of type canStartProcess
    self.drawConnections(
(self.obj72,self.obj56,[325.4687139416097, 21.985521262471085, 367.9649054322099, 20.08042128740175, 392.9089461136115, 16.165287833912885],"true", 3) )
    # Connections for obj73 (graphObject_: Obj36) of type canStartProcess
    self.drawConnections(
(self.obj73,self.obj55,[308.5, 99.0, 328.0, 106.0, 393.48582623951086, 98.15272040808202],"true", 3) )
    # Connections for obj74 (graphObject_: Obj37) of type canStartProcess
    self.drawConnections(
(self.obj74,self.obj57,[357.78442985817634, 264.8715975346214, 416.95414334140355, 262.74388938900006, 459.48321868484334, 262.6097221100297],"true", 3) )
    # Connections for obj75 (graphObject_: Obj38) of type canStartProcess
    self.drawConnections(
(self.obj75,self.obj58,[261.75, 347.0, 289.5, 354.0, 458.64744670787036, 345.1570107041184],"true", 3) )
    # Connections for obj76 (graphObject_: Obj39) of type canStartProcess
    self.drawConnections(
(self.obj76,self.obj59,[256.75, 411.0, 284.5, 418.0, 459.35544634207554, 426.82565181102837],"true", 3) )

newfunction = recipeWorld_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
