"""
__GGLPS_Rule2_LHS_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Sun Mar 11 03:54:15 2018
_____________________________________________________________________________
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

def GGLPS_Rule2_LHS_MDL(self, rootNode, LSMASOMMRootNode=None):

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


    self.obj59=OrgUnit(self)
    self.obj59.isGraphObjectVisual = True

    if(hasattr(self.obj59, '_setHierarchicalLink')):
      self.obj59._setHierarchicalLink(False)

    # Individual
    self.obj59.Individual.setNone()
    self.obj59.Individual.config = 0

    # hasActions
    self.obj59.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj59.hasActions.setValue(lcobj2)
    self.obj59.hasActions.setNone()

    # ID
    self.obj59.ID.setValue('')
    self.obj59.ID.setNone()

    # name
    self.obj59.name.setValue('')
    self.obj59.name.setNone()

    # UnitSize
    self.obj59.UnitSize.setValue('Individual')

    self.obj59.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(0,0,self.obj59)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj59.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj59)
    self.globalAndLocalPostcondition(self.obj59, rootNode)
    self.obj59.postAction( rootNode.CREATE )

    self.obj60=Role(self)
    self.obj60.isGraphObjectVisual = True

    if(hasattr(self.obj60, '_setHierarchicalLink')):
      self.obj60._setHierarchicalLink(False)

    # isMetaRole
    self.obj60.isMetaRole.setNone()
    self.obj60.isMetaRole.config = 0

    # hasActions
    self.obj60.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj60.hasActions.setValue(lcobj2)
    self.obj60.hasActions.setNone()

    # ID
    self.obj60.ID.setValue('')
    self.obj60.ID.setNone()

    # name
    self.obj60.name.setValue('PartyFounder')

    self.obj60.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(93,0,self.obj60)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj60.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj60)
    self.globalAndLocalPostcondition(self.obj60, rootNode)
    self.obj60.postAction( rootNode.CREATE )

    self.obj61=canHaveRole(self)
    self.obj61.isGraphObjectVisual = True

    if(hasattr(self.obj61, '_setHierarchicalLink')):
      self.obj61._setHierarchicalLink(True)

    # ID
    self.obj61.ID.setValue('OUR|0')

    self.obj61.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(82.7757140317,49.5328543483,self.obj61)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj61.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj61)
    self.globalAndLocalPostcondition(self.obj61, rootNode)
    self.obj61.postAction( rootNode.CREATE )

    # Connections for obj59 (graphObject_: Obj6) named 
    self.drawConnections(
(self.obj59,self.obj61,[23.0, 63.0, 52.52571403165985, 52.28285434825837, 82.77571403165985, 49.53285434825837],"true", 3) )
    # Connections for obj60 (graphObject_: Obj7) named PartyFounder
    self.drawConnections(
 )
    # Connections for obj61 (graphObject_: Obj8) of type canHaveRole
    self.drawConnections(
(self.obj61,self.obj60,[82.77571403165985, 49.53285434825837, 113.02571403165985, 46.78285434825837, 144.0, 52.0],"true", 3) )

newfunction = GGLPS_Rule2_LHS_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
