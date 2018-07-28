"""
__test_MDL.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Wed Jun  7 00:21:39 2017
__________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from OrgUnit import *
from Role import *
from canHaveRole import *
from isPartOfRole import *
from graph_canHaveRole import *
from graph_OrgUnit import *
from graph_isPartOfRole import *
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

def test_MDL(self, rootNode, LSMASOMMRootNode=None):

    # --- Generating attributes code for ASG LSMASOMM ---
    if( LSMASOMMRootNode ): 
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
       new_obj = graph_OrgUnit(0,278,self.obj44)
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
       new_obj = graph_Role(170,417,self.obj45)
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
    self.obj46.isMetaRole.setValue(('isMetaRole', 1))
    self.obj46.isMetaRole.config = 0

    # hasActions
    self.obj46.hasActions.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj46.hasActions.setValue(lcobj2)

    # ID
    self.obj46.ID.setValue('R|1')

    # name
    self.obj46.name.setValue('Shadow')

    self.obj46.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(349,139,self.obj46)
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
    self.obj47.hasActions.setValue(lcobj2)

    # ID
    self.obj47.ID.setValue('R|2')

    # name
    self.obj47.name.setValue('Melee')

    self.obj47.graphClass_= graph_Role
    if self.genGraphics:
       new_obj = graph_Role(170,0,self.obj47)
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

    self.obj48=canHaveRole(self)
    self.obj48.isGraphObjectVisual = True

    if(hasattr(self.obj48, '_setHierarchicalLink')):
      self.obj48._setHierarchicalLink(True)

    # ID
    self.obj48.ID.setValue('OUR|0')

    self.obj48.graphClass_= graph_canHaveRole
    if self.genGraphics:
       new_obj = graph_canHaveRole(111.0,310.0,self.obj48)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj48.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48, rootNode)
    self.obj48.postAction( rootNode.CREATE )

    self.obj49=isPartOfRole(self)
    self.obj49.isGraphObjectVisual = True

    if(hasattr(self.obj49, '_setHierarchicalLink')):
      self.obj49._setHierarchicalLink(True)

    # ID
    self.obj49.ID.setValue('pR|0')

    self.obj49.graphClass_= graph_isPartOfRole
    if self.genGraphics:
       new_obj = graph_isPartOfRole(294.633294761,113.60172833,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("isPartOfRole", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj49.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)
    self.obj49.postAction( rootNode.CREATE )

    # Connections for obj44 (graphObject_: Obj0) named Player
    self.drawConnections(
(self.obj44,self.obj48,[23.0, 341.0, 70.32259422668119, 334.93188038541757, 111.0, 310.0],"true", 3) )
    # Connections for obj45 (graphObject_: Obj1) named Wizard
    self.drawConnections(
 )
    # Connections for obj46 (graphObject_: Obj2) named Shadow
    self.drawConnections(
 )
    # Connections for obj47 (graphObject_: Obj3) named Melee
    self.drawConnections(
(self.obj47,self.obj49,[199.0, 52.0, 249.88329476073784, 78.85172832969732, 294.63329476073784, 113.60172832969732],"true", 3) )
    # Connections for obj48 (graphObject_: Obj4) of type canHaveRole
    self.drawConnections(
(self.obj48,self.obj45,[111.0, 310.0, 146.25065158692985, 394.342406668869, 199.0, 469.0],"true", 3),
(self.obj48,self.obj46,[111.0, 310.0, 219.0, 298.0, 378.0, 191.0],"true", 3) )
    # Connections for obj49 (graphObject_: Obj6) of type isPartOfRole
    self.drawConnections(
(self.obj49,self.obj46,[294.63329476073784, 113.60172832969732, 339.38329476073784, 148.35172832969732, 378.0, 191.0],"true", 3) )

newfunction = test_MDL

loadedMMName = 'LSMASOMM_META'

atom3version = '0.3'
