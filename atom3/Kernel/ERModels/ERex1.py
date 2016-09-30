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

def ERex1(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.attributes.setValue(lcobj1)
    rootNode.name.setValue('NFAMetaModel')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.constraints.setValue(lcobj1)
    rootNode.graphClass_= graph_ASG_ERmetaMetaModel

    self.globalPrecondition()

    self.obj13=ERentity(self)

    self.obj13.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    self.obj13.constraints.setValue(lcobj1)
    self.obj13.name.setValue('NFAState')
    self.obj13.appearance.setValue( ('NFAState', self.obj13))
    self.obj13.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('S')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3Enum(['Initial', 'Regular', 'Terminal'],None,1)
    cobj1.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('Initial')
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Regular')
    lcobj2.append(cobj2)
    cobj2=ATOM3String('Terminal')
    lcobj2.append(cobj2)
    cobj1.initialValue.configItems.setValue(lcobj2)
    lcobj1.append(cobj1)
    self.obj13.attributes.setValue(lcobj1)
    self.obj13.graphClass_= graph_ERentity
    new_obj = graph_ERentity(69.0,239.0,self.obj13)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    self.obj13.graphObject_ = new_obj
    rootNode.addNode(self.obj13)
    self.globalAndLocalPostcondition(self.obj13)

    self.globalPrecondition()

    self.obj14=ERrelationship(self)

    self.obj14.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    self.obj14.constraints.setValue(lcobj1)
    self.obj14.name.setValue('Transition')
    self.obj14.appearance.setValue( ('Transition', self.obj14))
    self.obj14.appearance.linkInfo=linkEditor(self,self.obj14.appearance.semObject, "Transition")
    self.obj14.appearance.linkInfo.FirstLink= stickylink()
    self.obj14.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj14.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj14.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj14.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj14.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj14.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj14.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj14.appearance.linkInfo.FirstLink.decoration.setValue( ('Transition_1stLink', self.obj14.appearance.linkInfo.FirstLink))
    self.obj14.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj14.appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj14.appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
    self.obj14.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj14.appearance.linkInfo.FirstSegment.decoration.setValue( ('Transition_1stSegment', self.obj14.appearance.linkInfo.FirstSegment))
    self.obj14.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj14.appearance.linkInfo.Center.setValue( ('Transition_Center', self.obj14.appearance.linkInfo))
    self.obj14.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj14.appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj14.appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
    self.obj14.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj14.appearance.linkInfo.SecondSegment.decoration.setValue( ('Transition_2ndSegment', self.obj14.appearance.linkInfo.SecondSegment))
    self.obj14.appearance.linkInfo.SecondLink= stickylink()
    self.obj14.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj14.appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj14.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj14.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(2)
    self.obj14.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(4)
    self.obj14.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(2)
    self.obj14.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj14.appearance.linkInfo.SecondLink.decoration.setValue( ('Transition_2ndLink', self.obj14.appearance.linkInfo.SecondLink))
    self.obj14.appearance.linkInfo.FirstLink.decoration.semObject=self.obj14.appearance.semObject
    self.obj14.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj14.appearance.semObject
    self.obj14.appearance.linkInfo.Center.semObject=self.obj14.appearance.semObject
    self.obj14.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj14.appearance.semObject
    self.obj14.appearance.linkInfo.SecondLink.decoration.semObject=self.obj14.appearance.semObject
    self.obj14.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj1 =[]
    cobj1=ATOM3Connection()
    cobj1.setValue(('NFAState', (('FROM entity TO relationship', 'FROM relationship TO entity'), 0), '1', '1'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('NFAState', (('FROM entity TO relationship', 'FROM relationship TO entity'), 1), '1', '1'))
    lcobj1.append(cobj1)
    self.obj14.cardinality.setValue(lcobj1)
    self.obj14.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Label', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    self.obj14.attributes.setValue(lcobj1)
    self.obj14.graphClass_= graph_ERrelationship
    new_obj = graph_ERrelationship(313.0,240.0,self.obj14)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    self.obj14.graphObject_ = new_obj
    rootNode.addNode(self.obj14)
    self.globalAndLocalPostcondition(self.obj14)
    self.drawConnections((self.obj13,self.obj14,[141.0, 331.0, 141.0, 368.0, 357.0, 368.0, 357.0, 326.0],"bezier"), (self.obj14,self.obj13,[362.0, 241.0, 362.0, 190.0, 139.0, 190.0, 139.0, 240.0],"bezier") )

newfunction = ERex1

loadedMMName = 'ERmetaMetaModel'
