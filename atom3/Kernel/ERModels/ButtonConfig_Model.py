from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_TypesMetaModel import *
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

def ButtonConfig_Model(self, rootNode):
    rootNode.Author.setValue('')
    rootNode.Comments.setValue('')

    self.globalPrecondition()

    self.obj37=TypeName(self)

    self.obj37.Name.setValue('ButtonConfig')
    self.obj37.graphClass_= graph_TypeName
    from graph_TypeName import *
    new_obj = graph_TypeName(270.0,161.0,self.obj37)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("TypeName", new_obj.tag)
    self.obj37.graphObject_ = new_obj
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37)

    self.globalPrecondition()

    self.obj38=LeafType(self)

    self.obj38.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj38.Type.setValue(('Entity', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj38.Type.initialValue=ATOM3String('')
    self.obj38.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(42.0,336.0,self.obj38)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38)

    self.globalPrecondition()

    self.obj39=LeafType(self)

    self.obj39.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj39.Type.setValue(('Button', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj39.Type.initialValue=ATOM3Enum(['Text', 'Bitmap', 'None'],None,1)
    self.obj39.Type.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3String('Text')
    lcobj1.append(cobj1)
    cobj1=ATOM3String('Bitmap')
    lcobj1.append(cobj1)
    cobj1=ATOM3String('None')
    lcobj1.append(cobj1)
    self.obj39.Type.initialValue.configItems.setValue(lcobj1)
    self.obj39.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(128.0,395.0,self.obj39)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39)

    self.globalPrecondition()

    self.obj40=LeafType(self)

    self.obj40.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj40.Type.setValue(('Text_or_Bitmap', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj40.Type.initialValue=ATOM3String('')
    self.obj40.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(264.0,409.0,self.obj40)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40)

    self.globalPrecondition()

    self.obj41=LeafType(self)

    self.obj41.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj41.Type.setValue(('PreActions', 'Constraint', None, ('Key', 0), ('Direct Editing', 0)))
    self.obj41.Type.initialValue=ATOM3Constraint()
    self.obj41.Type.initialValue.setValue(('PreActions', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
    self.obj41.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(407.0,405.0,self.obj41)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj41.graphObject_ = new_obj
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41)

    self.globalPrecondition()

    self.obj46=LeafType(self)

    self.obj46.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj46.Type.setValue(('PostActions', 'Constraint', None, ('Key', 0), ('Direct Editing', 0)))
    self.obj46.Type.initialValue=ATOM3Constraint()
    self.obj46.Type.initialValue.setValue(('PostActions', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
    self.obj46.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(543.0,393.0,self.obj46)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj46.graphObject_ = new_obj
    rootNode.addNode(self.obj46)
    self.globalAndLocalPostcondition(self.obj46)

    self.globalPrecondition()

    self.obj48=Operator(self)

    self.obj48.type.setValue( (['X', 'U', '->'], 0) )
    self.obj48.type.config = 0
    self.obj48.graphClass_= graph_Operator
    from graph_Operator import *
    new_obj = graph_Operator(303.0,273.0,self.obj48)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("Operator", new_obj.tag)
    self.obj48.graphObject_ = new_obj
    rootNode.addNode(self.obj48)
    self.globalAndLocalPostcondition(self.obj48)
    self.drawConnections((self.obj37,self.obj48,[309.0, 195.0, 311.0, 290.0], 0, 2), (self.obj48,self.obj46,[340.0, 290.0, 553.0, 414.0], 0, 2), (self.obj48,self.obj41,[340.0, 290.0, 417.0, 426.0], 0, 2), (self.obj48,self.obj40,[340.0, 290.0, 324.0, 412.0], 0, 2), (self.obj48,self.obj39,[340.0, 290.0, 239.0, 415.0], 0, 2), (self.obj48,self.obj38,[340.0, 290.0, 153.0, 356.0], 0, 2) )

newfunction = ButtonConfig_Model

loadedMMName = 'TypesMetaModel'
