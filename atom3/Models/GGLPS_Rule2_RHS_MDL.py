"""
__GGLPS_Rule2_RHS_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Sun Mar 11 03:53:45 2018
_____________________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from isPartOfOrgUnit import *
from canHaveRole import *
from graph_isPartOfOrgUnit import *
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

def GGLPS_Rule2_RHS_MDL(self, rootNode, LSMASOMMRootNode=None):

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


    self.obj63=OrgUnit(self)
    self.obj63.isGraphObjectVisual = True

    if(hasattr(self.obj63, '_setHierarchicalLink')):
      self.obj63._setHierarchicalLink(False)

    # Individual
    self.obj63.Individual.setNone()
    self.obj63.Individual.config = 0

    # hasActions
    self.obj63.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj63.hasActions.setValue(lcobj2)
    self.obj63.hasActions.setNone()

    # ID
    self.obj63.ID.setValue('')
    self.obj63.ID.setNone()

    # name
    self.obj63.name.setValue('')
    self.obj63.name.setNone()

    # UnitSize
    self.obj63.UnitSize.setValue('Individual')

    self.obj63.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(0,104,self.obj63)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj63.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj63)
    self.globalAndLocalPostcondition(self.obj63, rootNode)
    self.obj63.postAction( rootNode.CREATE )

    self.obj64=OrgUnit(self)
    self.obj64.isGraphObjectVisual = True

    if(hasattr(self.obj64, '_setHierarchicalLink')):
      self.obj64._setHierarchicalLink(False)

    # Individual
    self.obj64.Individual.setValue(('1', 0))
    self.obj64.Individual.config = 0

    # hasActions
    self.obj64.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('ChangeRole', 20)
    lcobj2.append(cobj2)
    self.obj64.hasActions.setValue(lcobj2)

    # ID
    self.obj64.ID.setValue('OU|99')

    # name
    self.obj64.name.setValue('Party')

    # UnitSize
    self.obj64.UnitSize.setValue('Group')

    self.obj64.graphClass_= graph_OrgUnit
    if self.genGraphics:
       new_obj = graph_OrgUnit(124,0,self.obj64)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj64.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj64)
    self.globalAndLocalPostcondition(self.obj64, rootNode)
    self.obj64.postAction( rootNode.CREATE )

    self.obj65=Role(self)
    self.obj65.isGraphObjectVisual = True

    if(hasattr(self.obj65, '_setHierarchicalLink')):
      self.obj65._setHierarchicalLink(False)

    # isMetaRole
    self.obj65.isMetaRole.setNone()
    self.obj65.isMetaRole.config = 0

    # hasActions
    self.obj65.hasActions.setActionFlags([ 0, 0, 1, 0])
    lcobj2 =[]
    self.obj65.hasActions.setValue(lcobj2)
    self.obj65.hasActions.setNone()

    # ID
    self.obj65.ID.setValue('')
    self.obj65.ID.setNone()

    # name
    self.obj65.name.setValue('PartyFounder')

    self.obj65.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(206,104,self.obj65)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Role", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj65.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj65)
    self.globalAndLocalPostcondition(self.obj65, rootNode)
    self.obj65.postAction( rootNode.CREATE )

    self.obj66=isPartOfOrgUnit(self)
    self.obj66.isGraphObjectVisual = True

    if(hasattr(self.obj66, '_setHierarchicalLink')):
      self.obj66._setHierarchicalLink(True)

    # ID
    self.obj66.ID.setValue('pOU|0')

    self.obj66.graphClass_= graph_isPartOfOrgUnit
    if self.genGraphics:
       new_obj = graph_isPartOfOrgUnit(84.8158842791,109.370539238,self.obj66)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfOrgUnit", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj66.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj66)
    self.globalAndLocalPostcondition(self.obj66, rootNode)
    self.obj66.postAction( rootNode.CREATE )

    self.obj67=canHaveRole(self)
    self.obj67.isGraphObjectVisual = True

    if(hasattr(self.obj67, '_setHierarchicalLink')):
      self.obj67._setHierarchicalLink(True)

    # ID
    self.obj67.ID.setValue('OUR|0')

    self.obj67.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(169.95,122.35,self.obj67)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj67.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj67)
    self.globalAndLocalPostcondition(self.obj67, rootNode)
    self.obj67.postAction( rootNode.CREATE )

    # Connections for obj63 (graphObject_: Obj10) named 
    self.drawConnections(
(self.obj63,self.obj67,[39.0, 167.0, 159.6, 122.9, 169.95, 122.35],"true", 3),
(self.obj63,self.obj66,[39.0, 167.0, 59.06588427909951, 135.37053923795432, 84.8158842790995, 109.37053923795432],"true", 3) )
    # Connections for obj64 (graphObject_: Obj11) named Party
    self.drawConnections(
 )
    # Connections for obj65 (graphObject_: Obj12) named PartyFounder
    self.drawConnections(
 )
    # Connections for obj66 (graphObject_: Obj13) of type isPartOfOrgUnit
    self.drawConnections(
(self.obj66,self.obj64,[84.8158842790995, 109.37053923795432, 110.5658842790995, 83.37053923795432, 142.0, 63.0],"true", 3) )
    # Connections for obj67 (graphObject_: Obj15) of type canHaveRole
    self.drawConnections(
(self.obj67,self.obj65,[169.95, 122.35, 180.3, 121.8, 246.0, 156.0],"true", 3) )

newfunction = GGLPS_Rule2_RHS_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
