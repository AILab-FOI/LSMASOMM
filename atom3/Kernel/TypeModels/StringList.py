from Tkinter             import *
from ATOM3Type           import *
from Operator            import *
from LeafType             import *
from TypeName            import *
from ASG_TypesMetaModel import *
from ltypenameUltypename import *

class StringList (ltypenameUltypename):
  def createTypeGraph(self, atom3i, rootNode):

    self.obj37=TypeName(atom3i)

    self.obj37.Name.setValue('StringList')
    self.obj37.graphClass_= graph_TypeName
    new_obj = graph_TypeName(147.0,102.0,self.obj37)
    self.obj37.graphObject_ = new_obj
    rootNode.addNode(self.obj37)

    self.obj38=LeafType(atom3i)

    self.obj38.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj38.Type.setValue(('ltypename', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj38.Type.initialValue=ATOM3String('')
    self.obj38.graphClass_= graph_LeafType
    new_obj = graph_LeafType(60.0,316.0,self.obj38)
    self.obj38.graphObject_ = new_obj
    rootNode.addNode(self.obj38)

    self.obj39=LeafType(atom3i)

    self.obj39.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj39.Type.setValue(('ltypename', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj39.Type.initialValue=ATOM3String('')
    self.obj39.graphClass_= graph_LeafType
    new_obj = graph_LeafType(249.0,317.0,self.obj39)
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)

    self.obj40=Operator(atom3i)

    self.obj40.type.setValue( (['X', 'U', '->'], 1) )
    self.obj40.type.config = 0
    self.obj40.graphClass_= graph_Operator
    new_obj = graph_Operator(177.0,229.0,self.obj40)
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)
    self.obj37.out_connections_.append(self.obj40)
    self.obj40.in_connections_.append(self.obj37)
    self.obj40.out_connections_.append(self.obj39)
    self.obj39.in_connections_.append(self.obj40)
    self.obj40.out_connections_.append(self.obj38)
    self.obj38.in_connections_.append(self.obj40)

