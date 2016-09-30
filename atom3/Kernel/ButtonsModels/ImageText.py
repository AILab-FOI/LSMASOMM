from Tkinter             import *
from ATOM3Type           import *
from Operator            import *
from LeafType             import *
from TypeName            import *
from ASG_TypesMetaModel import *
from TextUImage import *

class ImageText (TextUImage):
  def createTypeGraph(self, atom3i, rootNode):

    self.obj39=TypeName(atom3i)

    self.obj39.Name.setValue('ImageText')
    self.obj39.graphClass_= graph_TypeName
    from graph_TypeName import *
    new_obj = graph_TypeName(178.0,177.0,self.obj39)
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)

    self.obj40=LeafType(atom3i)

    self.obj40.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj40.Type.setValue(('Image', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj40.Type.initialValue=ATOM3String('')
    self.obj40.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(70.0,400.0,self.obj40)
    self.obj40.graphObject_ = new_obj
    rootNode.addNode(self.obj40)

    self.obj41=LeafType(atom3i)

    self.obj41.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj41.Type.setValue(('Text', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj41.Type.initialValue=ATOM3String('')
    self.obj41.graphClass_= graph_LeafType
    from graph_LeafType import *
    new_obj = graph_LeafType(253.0,402.0,self.obj41)
    self.obj41.graphObject_ = new_obj
    rootNode.addNode(self.obj41)

    self.obj42=Operator(atom3i)

    self.obj42.type.setValue( (['X', 'U', '->'], 1) )
    self.obj42.type.config = 0
    self.obj42.graphClass_= graph_Operator
    from graph_Operator import *
    new_obj = graph_Operator(198.0,308.0,self.obj42)
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)
    self.obj39.out_connections_.append(self.obj42)
    self.obj42.in_connections_.append(self.obj39)
    self.obj42.out_connections_.append(self.obj41)
    self.obj41.in_connections_.append(self.obj42)
    self.obj42.out_connections_.append(self.obj40)
    self.obj40.in_connections_.append(self.obj42)

