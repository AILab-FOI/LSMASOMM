from graph_ASG_ERmetaMetaModel import *
from ASG_ERmetaMetaModel import *
from ERentity import *
from ERrelationship import *
from ASG_ERmetaMetaModel import *
from ATOM3Enum import *
from ATOM3List import *
from ATOM3Float import *
from ATOM3Integer import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Link import *

def Type_Model2(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Comments', 'String', None, ('Key', 0), ('Direct Editing', 0)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    rootNode.attributes.setValue(lcobj1)
    rootNode.name.setValue('Types')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.constraints.setValue(lcobj1)
    rootNode.graphClass_= graph_ASG_ERmetaMetaModel

    self.globalPrecondition()

    self.obj13=ERentity(self)

    self.obj13.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    self.obj13.constraints.setValue(lcobj1)
    self.obj13.name.setValue('TypeName')
    self.obj13.appearance.setValue( ('TypeName', self.obj13))
    self.obj13.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('typename')
    lcobj1.append(cobj1)
    self.obj13.attributes.setValue(lcobj1)
    self.obj13.graphClass_= graph_ERentity
    new_obj = graph_ERentity(112.0,61.0,self.obj13)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    self.obj13.graphObject_ = new_obj
    rootNode.addNode(self.obj13)
    self.globalAndLocalPostcondition(self.obj13)

    self.globalPrecondition()

    self.obj14=ERentity(self)

    self.obj14.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    self.obj14.constraints.setValue(lcobj1)
    self.obj14.name.setValue('LeafType')
    self.obj14.appearance.setValue( ('LeafType', self.obj14))
    self.obj14.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('type', 'Attribute', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3Attribute(self.types)
    cobj1.initialValue.setValue(('ltypename', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('typeConstraint', 'Constraint', None, ('Key', 0), ('Direct Editing', 0)))
    cobj1.initialValue=ATOM3Constraint()
    cobj1.initialValue.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
    lcobj1.append(cobj1)
    self.obj14.attributes.setValue(lcobj1)
    self.obj14.graphClass_= graph_ERentity
    new_obj = graph_ERentity(112.0,363.0,self.obj14)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    self.obj14.graphObject_ = new_obj
    rootNode.addNode(self.obj14)
    self.globalAndLocalPostcondition(self.obj14)

    self.globalPrecondition()

    self.obj15=ERrelationship(self)

    self.obj15.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    self.obj15.constraints.setValue(lcobj1)
    self.obj15.name.setValue('Operator')
    self.obj15.appearance.setValue( ('Operator', self.obj15))
    self.obj15.appearance.linkInfo=linkEditor(self,self.obj15.appearance.semObject, "Operator")
    self.obj15.appearance.linkInfo.FirstLink= stickylink()
    self.obj15.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj15.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj15.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj15.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj15.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj15.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj15.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj15.appearance.linkInfo.FirstLink.decoration.setValue( ('Operator_1stLink', self.obj15.appearance.linkInfo.FirstLink))
    self.obj15.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj15.appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj15.appearance.linkInfo.FirstSegment.fill=ATOM3String('gray')
    self.obj15.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj15.appearance.linkInfo.FirstSegment.decoration.setValue( ('Operator_1stSegment', self.obj15.appearance.linkInfo.FirstSegment))
    self.obj15.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj15.appearance.linkInfo.Center.setValue( ('Operator_Center', self.obj15.appearance.linkInfo))
    self.obj15.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj15.appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj15.appearance.linkInfo.SecondSegment.fill=ATOM3String('gray')
    self.obj15.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj15.appearance.linkInfo.SecondSegment.decoration.setValue( ('Operator_2ndSegment', self.obj15.appearance.linkInfo.SecondSegment))
    self.obj15.appearance.linkInfo.SecondLink= stickylink()
    self.obj15.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj15.appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj15.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj15.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(3)
    self.obj15.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(9)
    self.obj15.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(3)
    self.obj15.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj15.appearance.linkInfo.SecondLink.decoration.setValue( ('Operator_2ndLink', self.obj15.appearance.linkInfo.SecondLink))
    self.obj15.appearance.linkInfo.FirstLink.decoration.semObject=self.obj15.appearance.semObject
    self.obj15.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj15.appearance.semObject
    self.obj15.appearance.linkInfo.Center.semObject=self.obj15.appearance.semObject
    self.obj15.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj15.appearance.semObject
    self.obj15.appearance.linkInfo.SecondLink.decoration.semObject=self.obj15.appearance.semObject
    self.obj15.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj1 =[]
    cobj1=ATOM3Connection()
    cobj1.setValue(('TypeName', (('FROM entity TO relationship', 'FROM relationship TO entity'), 0), '1', '1'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('LeafType', (('FROM entity TO relationship', 'FROM relationship TO entity'), 1), '1', '1'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('Operator', (('FROM entity TO relationship', 'FROM relationship TO entity'), 1), '1', '1'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('Operator', (('FROM entity TO relationship', 'FROM relationship TO entity'), 0), '1', '1'))
    lcobj1.append(cobj1)
    self.obj15.cardinality.setValue(lcobj1)
    self.obj15.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3Enum(['X', 'U', '->'],0,1)
    cobj1.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('X')
    lcobj2.append(cobj2)
    cobj2=ATOM3String('U')
    lcobj2.append(cobj2)
    cobj2=ATOM3String('->')
    lcobj2.append(cobj2)
    cobj1.initialValue.configItems.setValue(lcobj2)
    lcobj1.append(cobj1)
    self.obj15.attributes.setValue(lcobj1)
    self.obj15.graphClass_= graph_ERrelationship
    new_obj = graph_ERrelationship(211.0,201.0,self.obj15)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    self.obj15.graphObject_ = new_obj
    rootNode.addNode(self.obj15)
    self.globalAndLocalPostcondition(self.obj15)
    self.drawConnections((self.obj13,self.obj15,[184.0, 153.0, 259.0, 204.0], 0), (self.obj15,self.obj14,[257.0, 289.0, 182.0, 364.0], 0), 