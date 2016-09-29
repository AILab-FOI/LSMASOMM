from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_ERmetaMetaModel import *
from ERentity import *
from ERrelationship import *
from ASG_ERmetaMetaModel import *
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
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def GenericGraph_ER_mdl(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.attributes.setValue(lcobj1)
    rootNode.name.setValue('GenericGraph')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.constraints.setValue(lcobj1)
    rootNode.graphClass_= graph_ASG_ERmetaMetaModel

    self.globalPrecondition( rootNode )

    self.obj28=ERentity(self)

    self.obj28.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj28.attributes.setValue(lcobj2)
    self.obj28.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('GenericGraphEdge', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('GenericGraphEdge', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj28.cardinality.setValue(lcobj2)
    self.obj28.appearance.setValue( ('GenericGraphNode', self.obj28))
    self.obj28.name.setValue('GenericGraphNode')
    self.obj28.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj28.constraints.setValue(lcobj2)
    self.obj28.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(195.0,150.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)

    self.globalPrecondition( rootNode )

    self.obj29=ERrelationship(self)

    self.obj29.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj29.attributes.setValue(lcobj2)
    self.obj29.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('GenericGraphNode', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('GenericGraphNode', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj29.cardinality.setValue(lcobj2)
    self.obj29.appearance.setValue( ('GenericGraphEdge', self.obj29))
    self.obj29.appearance.linkInfo=linkEditor(self,self.obj29.appearance.semObject, "GenericGraphEdge")
    self.obj29.appearance.linkInfo.FirstLink= stickylink()
    self.obj29.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj29.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj29.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj29.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj29.appearance.linkInfo.FirstLink.decoration.setValue( ('GenericGraphEdge_1stLink', self.obj29.appearance.linkInfo.FirstLink))
    self.obj29.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj29.appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj29.appearance.linkInfo.FirstSegment.fill=ATOM3String('purple')
    self.obj29.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj29.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj29.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 1))
    self.obj29.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj29.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(4)
    self.obj29.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(6)
    self.obj29.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(4)
    self.obj29.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj29.appearance.linkInfo.FirstSegment.decoration.setValue( ('GenericGraphEdge_1stSegment', self.obj29.appearance.linkInfo.FirstSegment))
    self.obj29.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj29.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj29.appearance.linkInfo.Center.setValue( ('GenericGraphEdge_Center', self.obj29.appearance.linkInfo))
    self.obj29.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj29.appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj29.appearance.linkInfo.SecondSegment.fill=ATOM3String('purple')
    self.obj29.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj29.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj29.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj29.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj29.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj29.appearance.linkInfo.SecondSegment.decoration.setValue( ('GenericGraphEdge_2ndSegment', self.obj29.appearance.linkInfo.SecondSegment))
    self.obj29.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj29.appearance.linkInfo.SecondLink= stickylink()
    self.obj29.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj29.appearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
    self.obj29.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj29.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj29.appearance.linkInfo.SecondLink.decoration.setValue( ('GenericGraphEdge_2ndLink', self.obj29.appearance.linkInfo.SecondLink))
    self.obj29.appearance.linkInfo.FirstLink.decoration.semObject=self.obj29.appearance.semObject
    self.obj29.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj29.appearance.semObject
    self.obj29.appearance.linkInfo.Center.semObject=self.obj29.appearance.semObject
    self.obj29.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj29.appearance.semObject
    self.obj29.appearance.linkInfo.SecondLink.decoration.semObject=self.obj29.appearance.semObject
    self.obj29.name.setValue('GenericGraphEdge')
    self.obj29.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj29.constraints.setValue(lcobj2)
    self.obj29.graphClass_= graph_ERrelationship
    if self.genGraphics:
       from graph_ERrelationship import *
       new_obj = graph_ERrelationship(408.0,150.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.drawConnections((self.obj28,self.obj29,[269.0, 244.0, 268.0, 272.0, 455.0, 272.0, 454.0, 238.0], 0, 4), (self.obj29,self.obj28,[456.0, 153.00000000000006, 456.99999999999989, 120.0, 266.0, 119.00000000000001, 267.0, 152.99999999999997], 0, 4) )

newfunction = GenericGraph_ER_mdl

loadedMMName = 'EntityRelationship'
