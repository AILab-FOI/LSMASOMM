from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_TypesMetaModel import *
from ASG_TypesMetaModel import *
from TypeName import *
from LeafType import *
from Operator import *
from ATOM3Port import *
from ATOM3Integer import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Link import *
from ATOM3Boolean import *
from ATOM3Connection import *
from ATOM3List import *
from ATOM3Enum import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *

def StringList_Model(self, rootNode):
    rootNode.Author.setValue('')
    rootNode.Comments.setValue('')

    self.globalPrecondition( rootNode )

    self.obj51=TypeName(self)

    self.obj51.Name.setValue('ListOfStrings')
    self.obj51.graphClass_= graph_TypeName
    if self.genGraphics:
       from graph_TypeName import *
       new_obj = graph_TypeName(111.0,57.0,self.obj51)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("TypeName", new_obj.tag)
    else: new_obj = None
    self.obj51.graphObject_ = new_obj
    rootNode.addNode(self.obj51)
    self.globalAndLocalPostcondition(self.obj51, rootNode)

    self.globalPrecondition( rootNode )

    self.obj52=LeafType(self)

    self.obj52.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj52.Type.setValue(('item', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj52.Type.initialValue=ATOM3String('')
    self.obj52.graphClass_= graph_LeafType
    if self.genGraphics:
       from graph_LeafType import *
       new_obj = graph_LeafType(40.0,293.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    else: new_obj = None
    self.obj52.graphObject_ = new_obj
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)

    self.globalPrecondition( rootNode )

    self.obj53=LeafType(self)

    self.obj53.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj53.Type.setValue(('void', 'BottomType', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj53.Type.initialValue=ATOM3BottomType()
    self.obj53.graphClass_= graph_LeafType
    if self.genGraphics:
       from graph_LeafType import *
       new_obj = graph_LeafType(144.0,342.0,self.obj53)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("LeafType", new_obj.tag)
    else: new_obj = None
    self.obj53.graphObject_ = new_obj
    rootNode.addNode(self.obj53)
    self.globalAndLocalPostcondition(self.obj53, rootNode)

    self.globalPrecondition( rootNode )

    self.obj49=Operator(self)

    self.obj49.type.setValue( (['X', 'U', '->'], 0) )
    self.obj49.type.config = 0
    self.obj49.graphClass_= graph_Operator
    if self.genGraphics:
       from graph_Operator import *
       new_obj = graph_Operator(130.0,169.0,self.obj49)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Operator", new_obj.tag)
    else: new_obj = None
    self.obj49.graphObject_ = new_obj
    rootNode.addNode(self.obj49)
    self.globalAndLocalPostcondition(self.obj49, rootNode)

    self.globalPrecondition( rootNode )

    self.obj50=Operator(self)

    self.obj50.type.setValue( (['X', 'U', '->'], 1) )
    self.obj50.type.config = 0
    self.obj50.graphClass_= graph_Operator
    if self.genGraphics:
       from graph_Operator import *
       new_obj = graph_Operator(177.0,261.0,self.obj50)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("Operator", new_obj.tag)
    else: new_obj = None
    self.obj50.graphObject_ = new_obj
    rootNode.addNode(self.obj50)
    self.globalAndLocalPostcondition(self.obj50, rootNode)
    self.drawConnections((self.obj51,self.obj49,[150.0, 91.0, 150.0, 172.0], 0, 2), (self.obj49,self.obj50,[150.0, 202.0, 197.0, 265.0, 197.0, 264.0], 0, 2), (self.obj49,self.obj52,[150.0, 202.0, 93.0, 296.0], 0, 2), (self.obj50,self.obj53,[197.0, 294.0, 197.0, 345.0], 0, 2), (self.obj50,self.obj49,[212.0, 279.0, 254.0, 261.0, 229.0, 203.0, 205.0, 176.0, 165.0, 187.0],"bezier", 3) )

newfunction = StringList_Model

loadedMMName = 'TypesMetaModel'
