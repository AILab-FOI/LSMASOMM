from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_TypesMetaModel import *
from ASG_TypesMetaModel import *
from TypeName import *
from LeafType import *
from Operator import *
from ButtonConfig import *
from ATOM3Integer import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Link import *
from ATOM3Boolean import *
from ATOM3List import *
from ATOM3Enum import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *

def FormalismConfig_Model(self, rootNode):
    rootNode.Author.setValue('')
    rootNode.Comments.setValue('')

    self.globalPrecondition()

    self.obj84=TypeName(self)

    self.obj84.Name.setValue('FormalismConfig')
    self.obj84.graphClass_= graph_TypeName
    from graph_TypeName import *
    new_obj = graph_TypeName(199.0,148.0,self.obj84)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("TypeName", new_obj.tag)
    self.obj84.graphObject_ = new_obj
    rootNode.addNode(self.obj84)
    self.globalAndLocalPostcondition(self.obj84)

    self.globalPrecondition()

    self.obj88=LeafType(self)

    self.obj88.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj88.Type.setValue(('Formalism_Name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj88.Type.initialValue=ATOM3String('')
    self.obj88.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(72.0,359.0,self.obj88)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj88.graphObject_ = new_obj
    rootNode.addNode(self.obj88)
    self.globalAndLocalPostcondition(self.obj88)

    self.globalPrecondition()

    self.obj89=LeafType(self)

    self.obj89.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj89.Type.setValue(('Buttons_Per_Row', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj89.Type.initialValue=ATOM3Integer(0)
    self.obj89.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(244.0,363.0,self.obj89)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj89.graphObject_ = new_obj
    rootNode.addNode(self.obj89)
    self.globalAndLocalPostcondition(self.obj89)

    self.globalPrecondition()

    self.obj90=LeafType(self)

    self.obj90.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj90.Type.setValue(('Buttons', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj90.Type.initialValue=ATOM3List([ 1, 1, 1, self.types],ButtonConfig)
    lcobj1=[]
    self.obj90.Type.initialValue.setValue(lcobj1)
    self.obj90.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(435.0,378.0,self.obj90)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj90.graphObject_ = new_obj
    rootNode.addNode(self.obj90)
    self.globalAndLocalPostcondition(self.obj90)

    self.globalPrecondition()

    self.obj87=Operator(self)

    self.obj87.type.setValue( (['X', 'U', '->'], 0) )
    self.obj87.type.config = 0
    self.obj87.graphClass_= graph_Operator
    from graph_Operator import *
    new_obj = graph_Operator(199.0,239.0,self.obj87)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("Operator", new_obj.tag)
    self.obj87.graphObject_ = new_obj
    rootNode.addNode(self.obj87)
    self.globalAndLocalPostcondition(self.obj87)
    self.drawConnections((self.obj84,self.obj87,[238.0, 182.0, 207.0, 256.0], 0, 2), (self.obj87,self.obj88,[236.0, 256.0, 183.0, 379.0], 0, 2), (self.obj87,self.obj89,[236.0, 256.0, 304.0, 366.0], 0, 2), (self.obj87,self.obj90,[236.0, 256.0, 445.0, 399.0], 0, 2) )

newfunction = FormalismConfig_Model

loadedMMName = 'TypesMetaModel'
