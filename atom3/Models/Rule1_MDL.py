"""
__Rule1_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Tue May  1 00:05:34 2018
___________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from canHaveRole import *
from graph_canHaveRole import *
from graph_OrgUnit import *
from graph_Role import *
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

def Rule1_MDL(self, rootNode, LSMASOMMRootNode=None):

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
        LSMASOMMRootNode.name.setValue('LSMASOMM')

        # title
        LSMASOMMRootNode.title.setValue('')
        LSMASOMMRootNode.title.setNone()
    # --- ASG attributes over ---


    self.obj140=OrgUnit(self)
    self.obj140.isGraphObjectVisual = True

    if(hasattr(self.obj140, '_setHierarchicalLink')):
      self.obj140._setHierarchicalLink(False)

    # Individual
    self.obj140.Individual.setValue(('1', 0))
    self.obj140.Individual.config = 0

    # hasActions
    self.obj140.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj140.hasActions.setValue(lcobj2)

    # ID
    self.obj140.ID.setValue('<ID>')

    # name
    self.obj140.name.setValue('4:Agent')

    # UnitSize
    self.obj140.UnitSize.setValue('Individual')

    self.obj140.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(350.0,70.0,self.obj140)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj140.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj140)
    self.globalAndLocalPostcondition(self.obj140, rootNode)
    self.obj140.postAction( rootNode.CREATE )

    self.obj157=Role(self)
    self.obj157.isGraphObjectVisual = True

    if(hasattr(self.obj157, '_setHierarchicalLink')):
      self.obj157._setHierarchicalLink(False)

    # isMetaRole
    self.obj157.isMetaRole.setValue((None, 0))
    self.obj157.isMetaRole.config = 0

    # hasActions
    self.obj157.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj157.hasActions.setValue(lcobj2)

    # ID
    self.obj157.ID.setValue('R|0')

    # name
    self.obj157.name.setValue('5:Wizard')

    self.obj157.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(490.0,170.0,self.obj157)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj157.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj157)
    self.globalAndLocalPostcondition(self.obj157, rootNode)
    self.obj157.postAction( rootNode.CREATE )

    self.obj158=Role(self)
    self.obj158.isGraphObjectVisual = True

    if(hasattr(self.obj158, '_setHierarchicalLink')):
      self.obj158._setHierarchicalLink(False)

    # isMetaRole
    self.obj158.isMetaRole.setValue((None, 0))
    self.obj158.isMetaRole.config = 0

    # hasActions
    self.obj158.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj158.hasActions.setValue(lcobj2)

    # ID
    self.obj158.ID.setValue('R|1')

    # name
    self.obj158.name.setValue('6:Warrior')

    self.obj158.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(490.0,90.0,self.obj158)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj158.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj158)
    self.globalAndLocalPostcondition(self.obj158, rootNode)
    self.obj158.postAction( rootNode.CREATE )

    self.obj163=Role(self)
    self.obj163.isGraphObjectVisual = True

    if(hasattr(self.obj163, '_setHierarchicalLink')):
      self.obj163._setHierarchicalLink(False)

    # isMetaRole
    self.obj163.isMetaRole.setValue((None, 0))
    self.obj163.isMetaRole.config = 0

    # hasActions
    self.obj163.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj163.hasActions.setValue(lcobj2)

    # ID
    self.obj163.ID.setValue('R|2')

    # name
    self.obj163.name.setValue('7:Rogue')

    self.obj163.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(490.0,10.0,self.obj163)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj163.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj163)
    self.globalAndLocalPostcondition(self.obj163, rootNode)
    self.obj163.postAction( rootNode.CREATE )

    self.obj167=Role(self)
    self.obj167.isGraphObjectVisual = True

    if(hasattr(self.obj167, '_setHierarchicalLink')):
      self.obj167._setHierarchicalLink(False)

    # isMetaRole
    self.obj167.isMetaRole.setValue((None, 0))
    self.obj167.isMetaRole.config = 0

    # hasActions
    self.obj167.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj167.hasActions.setValue(lcobj2)

    # ID
    self.obj167.ID.setValue('R|3')

    # name
    self.obj167.name.setValue('8:PartyFounder')

    self.obj167.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(170.0,130.0,self.obj167)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj167.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj167)
    self.globalAndLocalPostcondition(self.obj167, rootNode)
    self.obj167.postAction( rootNode.CREATE )

    self.obj168=Role(self)
    self.obj168.isGraphObjectVisual = True

    if(hasattr(self.obj168, '_setHierarchicalLink')):
      self.obj168._setHierarchicalLink(False)

    # isMetaRole
    self.obj168.isMetaRole.setValue((None, 0))
    self.obj168.isMetaRole.config = 0

    # hasActions
    self.obj168.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj168.hasActions.setValue(lcobj2)

    # ID
    self.obj168.ID.setValue('R|4')

    # name
    self.obj168.name.setValue('9:PartyMember')

    self.obj168.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(170.0,40.0,self.obj168)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj168.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj168)
    self.globalAndLocalPostcondition(self.obj168, rootNode)
    self.obj168.postAction( rootNode.CREATE )

    self.obj166=canHaveRole(self)
    self.obj166.isGraphObjectVisual = True

    if(hasattr(self.obj166, '_setHierarchicalLink')):
      self.obj166._setHierarchicalLink(True)

    # ID
    self.obj166.ID.setValue('OUR|0')

    self.obj166.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(451.0,124.0,self.obj166)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj166.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj166)
    self.globalAndLocalPostcondition(self.obj166, rootNode)
    self.obj166.postAction( rootNode.CREATE )

    self.obj173=canHaveRole(self)
    self.obj173.isGraphObjectVisual = True

    if(hasattr(self.obj173, '_setHierarchicalLink')):
      self.obj173._setHierarchicalLink(True)

    # ID
    self.obj173.ID.setValue('OUR|1')

    self.obj173.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(323.0,133.0,self.obj173)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj173.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj173)
    self.globalAndLocalPostcondition(self.obj173, rootNode)
    self.obj173.postAction( rootNode.CREATE )

    # Connections for obj140 (graphObject_: Obj0) named 4:Agent
    self.drawConnections(
(self.obj140,self.obj166,[377.15245037442077, 132.9781934866436, 411.6907697000491, 125.91611040200831, 451.0, 124.0],"true", 3),
(self.obj140,self.obj173,[377.15245037442077, 132.9781934866436, 353.57584758951015, 144.45152802708537, 323.0, 133.0],"true", 3) )
    # Connections for obj157 (graphObject_: Obj6) named 5:Wizard
    self.drawConnections(
 )
    # Connections for obj158 (graphObject_: Obj7) named 6:Warrior
    self.drawConnections(
 )
    # Connections for obj163 (graphObject_: Obj8) named 7:Rogue
    self.drawConnections(
 )
    # Connections for obj167 (graphObject_: Obj11) named 8:PartyFounder
    self.drawConnections(
 )
    # Connections for obj168 (graphObject_: Obj12) named 9:PartyMember
    self.drawConnections(
 )
    # Connections for obj166 (graphObject_: Obj9) of type canHaveRole
    self.drawConnections(
(self.obj166,self.obj157,[451.0, 124.0, 497.81015662335403, 233.75474360113765, 520.7646700780256, 221.71630493643204],"true", 3),
(self.obj166,self.obj163,[451.0, 124.0, 479.95322451867656, 90.73608259216303, 521.0357076315616, 62.1306708486411],"true", 3),
(self.obj166,self.obj158,[451.0, 124.0, 480.88685569274503, 149.06833793710763, 523.3947734975173, 142.42484006358814],"true", 3) )
    # Connections for obj173 (graphObject_: Obj13) of type canHaveRole
    self.drawConnections(
(self.obj173,self.obj167,[323.0, 133.0, 277.3380557975534, 171.87613650595642, 228.0, 182.0],"true", 3),
(self.obj173,self.obj168,[323.0, 133.0, 264.8308882092855, 128.47325227512886, 226.0, 92.0],"true", 3) )

newfunction = Rule1_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
