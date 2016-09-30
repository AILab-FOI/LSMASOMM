from Tkinter             import *
from ATOM3Type           import *
from Operator            import *
from LeafType            import *
from TypeName            import *
from ASG_TypesMetaModel  import *
from widthXfillXdecoration import *

class segment (widthXfillXdecoration):
  def createTypeGraph(self, atom3i, rootNode):

    self.obj45=TypeName(atom3i)

    self.obj45.Name.setValue('segment')
    self.obj45.graphClass_= graph_TypeName
    new_obj = graph_TypeName(283.0,197.0,self.obj45)
    self.obj45.graphObject_ = new_obj
    rootNode.addNode(self.obj45)

    self.obj46=LeafType(atom3i)

    self.obj46.Type.setValue(('width', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj46.Type.initialValue=ATOM3Integer(0)
    self.obj46.graphClass_= graph_LeafType
    new_obj = graph_LeafType(161.0,344.0,self.obj46)
    self.obj46.graphObject_ = new_obj
    rootNode.addNode(self.obj46)

    self.obj47=LeafType(atom3i)

    self.obj47.Type.setValue(('fill', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj47.Type.initialValue=ATOM3String('')
    self.obj47.graphClass_= graph_LeafType
    new_obj = graph_LeafType(279.0,387.0,self.obj47)
    self.obj47.graphObject_ = new_obj
    rootNode.addNode(self.obj47)

    self.obj48=LeafType(atom3i)

    self.obj48.Type.setValue(('decoration', 'Appearance', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj48.Type.initialValue=ATOM3Appearance()
    self.obj48.Type.initialValue.setValue( ('class0', self.obj48.Type))
    self.obj48.graphClass_= graph_LeafType
    new_obj = graph_LeafType(401.0,355.0,self.obj48)
    self.obj48.graphObject_ = new_obj
    rootNode.addNode(self.obj48)

    self.obj49=Operator(atom3i)

    self.obj49.Type.setValue( (['U', 'X'], 1) )
    self.obj49.Type.config = 0
    self.obj49.graphClass_= graph_Operator
    new_obj = graph_Operator(312.0,292.0,self.obj49)
    self.obj49.graphObject_ = new_obj
    rootNode.addNode(self.obj49)
    self.obj45.out_connections_.append(self.obj49)
    self.obj49.in_connections_.append(self.obj45)
    self.obj49.out_connections_.append(self.obj46)
    self.obj46.in_connections_.append(self.obj49)
    self.obj49.out_connections_.append(self.obj47)
    self.obj47.in_connections_.append(self.obj49)
    self.obj49.out_connections_.append(self.obj48)
    self.obj48.in_connections_.append(self.obj49)

