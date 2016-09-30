from graph_ASG_ERmetaMetaModel import *
from ASG_TypesMetaModel import *
from TypeName import *
from LeafType import *
from Operator import *
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

def InvType(self, rootNode):
    rootNode.Author.setValue('')
    rootNode.Comments.setValue('')

    self.globalPrecondition()

    self.obj14=TypeName(self)

    self.obj14.Name.setValue('Inv.Type')
    self.obj14.graphClass_= graph_TypeName
    new_obj = graph_TypeName(94.0,68.0,self.obj14)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("TypeName", new_obj.tag)
    self.obj14.graphObject_ = new_obj
    rootNode.addNode(self.obj14)
    self.globalAndLocalPostcondition(self.obj14)

    self.globalPrecondition()

    self.obj15=LeafType(self)

    self.obj15.typeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
    self.obj15.type.setValue(('item1', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj15.type.initialValue=ATOM3Integer(0)
    self.obj15.graphClass_= graph_LeafType
    new_obj = graph_LeafType(5.0,259.0,self.obj15)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj15.graphObject_ = new_obj
    rootNode.addNode(self.obj15)
    self.globalAndLocalPostcondition(self.obj15)

    self.globalPrecondition()

    self.obj16=LeafType(self)

    self.obj16.typeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
    self.obj16.type.setValue(('item2', 'Float', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj16.type.initialValue=ATOM3Float(0.0)
    self.obj16.graphClass_= graph_LeafType
    new_obj = graph_LeafType(135.0,259.0,self.obj16)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj16.graphObject_ = new_obj
    rootNode.addNode(self.obj16)
    self.globalAndLocalPostcondition(self.obj16)

    self.globalPrecondition()

    self.obj17=Operator(self)

    self.obj17.type.setValue( (['X', 'U', '->'], 1) )
    self.obj17.type.config = 0
    self.obj17.graphClass_= graph_Operator
    new_obj = graph_Operator(111.0,141.0,self.obj17)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("Operator", new_obj.tag)
    self.obj17.graphObject_ = new_obj
    rootNode.addNode(self.obj17)
    self.globalAndLocalPostcondition(self.obj17)

    self.globalPrecondition()

    self.obj18=Operator(self)

    self.obj18.type.setValue( (['X', 'U', '->'], 0) )
    self.obj18.type.config = 0
    self.obj18.graphClass_= graph_Operator
    new_obj = graph_Operator(157.0,195.0,self.obj18)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("Operator", new_obj.tag)
    self.obj18.graphObject_ = new_obj
    rootNode.addNode(self.obj18)
    self.globalAndLocalPostcondition(self.obj18)

    self.globalPrecondition()

    self.obj21=Operator(self)

    self.obj21.type.setValue( (['X', 'U', '->'], 0) )
    self.obj21.type.config = 0
    self.obj21.graphClass_= graph_Operator
    new_obj = graph_Operator(64.0,195.0,self.obj21)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("Operator", new_obj.tag)
    self.obj21.graphObject_ = new_obj
    rootNode.addNode(self.obj21)
    self.globalAndLocalPostcondition(self.obj21)
    self.drawConnections((self.obj14,self.obj17,[133.0, 102.0, 133.0, 143.0], 0), (self.obj17,self.obj18,[179.0, 197.0, 181.0, 197.5, 148.0, 158.0], 0), (self.obj17,self.obj21,[86.0, 197.0, 86.5, 197.0, 119.0, 158.0], 0), (self.obj18,self.obj16,[179.0, 227.0, 195.0, 262.0], 0), (self.obj18,self.obj14,[194.0, 212.0, 240.0, 192.0, 237.0, 40.0, 128.0, 28.0, 133.0, 71.0],"bezier"), (self.obj21,self.obj18,[165.0, 212.0, 166.0, 212.0, 101.0, 212.0], 0), (self.obj21,self.obj15,[86.0, 227.0, 65.0, 262.0], 0) )

newfunction = InvType

loadedMMName = 'TypesMetaModel'
