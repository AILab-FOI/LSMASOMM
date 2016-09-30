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

def ImageText_Model(self, rootNode):
    rootNode.Author.setValue('')
    rootNode.Comments.setValue('')

    self.globalPrecondition()

    self.obj39=TypeName(self)

    self.obj39.Name.setValue('ImageText')
    self.obj39.graphClass_= graph_TypeName
    from graph_TypeName import *
    new_obj = graph_TypeName(178.0,177.0,self.obj39)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("TypeName", new_obj.tag)
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39)

    self.globalPrecondition()

    self.obj40=LeafType(self)

    self.obj40.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj40.Type.setValue(('Image', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj40.Type.initialValue=ATOM3String('')
    self.obj40.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(70.0,400.0,self.obj40)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40)

    self.globalPrecondition()

    self.obj41=LeafType(self)

    self.obj41.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj41.Type.setValue(('Text', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj41.Type.initialValue=ATOM3String('')
    self.obj41.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(253.0,402.0,self.obj41)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    self.obj41.graphObject_ = new_obj
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41)

    self.globalPrecondition()

    self.obj42=Operator(self)

    self.obj42.type.setValue( (['X', 'U', '->'], 1) )
    self.obj42.type.config = 0
    self.obj42.graphClass_= graph_Operator
    from graph_Operator import *
    new_obj = graph_Operator(198.0,308.0,self.obj42)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("Operator", new_obj.tag)
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42)
    self.drawConnections((self.obj39,self.obj42,[217.0, 211.0, 220.0, 310.0], 0, 2), (self.obj42,self.obj41,[235.0, 325.0, 313.0, 405.0], 0, 2), (self.obj42,self.obj40,[206.0, 325.0, 130.0, 403.0], 0, 2) )

newfunction = ImageText_Model

loadedMMName = 'TypesMetaModel'
