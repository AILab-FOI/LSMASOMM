from Tkinter             import *
from ATOM3Type           import *
from Operator            import *
from LeafType             import *
from TypeName            import *
from ModelType           import *
from ASG_TypesMetaModel import *
from aXStateChartUCBD4OOCSMP import *

class testModels (aXStateChartUCBD4OOCSMP):
  def createTypeGraph(self, atom3i, rootNode):
    self.types = atom3i.types

    self.obj28=TypeName(atom3i)

    self.obj28.Name.setValue('testModels')
    self.obj28.graphClass_= graph_TypeName
    if atom3i.genGraphics:
       from graph_TypeName import *
       new_obj = graph_TypeName(74.0,59.0,self.obj28)
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)

    self.obj29=LeafType(atom3i)

    self.obj29.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    self.obj29.Type.setValue(('a', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj29.Type.initialValue=ATOM3String('a')
    self.obj29.graphClass_= graph_LeafType
    if atom3i.genGraphics:
       from graph_LeafType import *
       new_obj = graph_LeafType(29.0,198.0,self.obj29)
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)

    self.obj30=ModelType(atom3i)

    self.obj30.MetaModelName.setValue('StateChart')
    self.obj30.Name.setValue('Method_SC')
    self.obj30.graphClass_= graph_ModelType
    if atom3i.genGraphics:
       from graph_ModelType import *
       new_obj = graph_ModelType(139.0,286.0,self.obj30)
    else: new_obj = None
    self.obj30.graphObject_ = new_obj
    rootNode.addNode(self.obj30)

    self.obj31=ModelType(atom3i)

    self.obj31.MetaModelName.setValue('CBD4OOCSMP')
    self.obj31.Name.setValue('Method_CBD')
    self.obj31.graphClass_= graph_ModelType
    if atom3i.genGraphics:
       from graph_ModelType import *
       new_obj = graph_ModelType(302.0,289.0,self.obj31)
    else: new_obj = None
    self.obj31.graphObject_ = new_obj
    rootNode.addNode(self.obj31)

    self.obj32=Operator(atom3i)

    self.obj32.type.setValue( (['X', 'U', '->'], 0) )
    self.obj32.type.config = 0
    self.obj32.graphClass_= graph_Operator
    if atom3i.genGraphics:
       from graph_Operator import *
       new_obj = graph_Operator(106.0,127.0,self.obj32)
    else: new_obj = None
    self.obj32.graphObject_ = new_obj
    rootNode.addNode(self.obj32)

    self.obj33=Operator(atom3i)

    self.obj33.type.setValue( (['X', 'U', '->'], 1) )
    self.obj33.type.config = 0
    self.obj33.graphClass_= graph_Operator
    if atom3i.genGraphics:
       from graph_Operator import *
       new_obj = graph_Operator(192.0,183.0,self.obj33)
    else: new_obj = None
    self.obj33.graphObject_ = new_obj
    rootNode.addNode(self.obj33)
    self.obj28.out_connections_.append(self.obj32)
    self.obj32.in_connections_.append(self.obj28)
    self.obj28.graphObject_.pendingConnections.append((self.obj28.graphObject_.tag, self.obj32.graphObject_.tag, [113.0, 93.0, 112.0, 145.0], 2, 0))
    self.obj32.out_connections_.append(self.obj29)
    self.obj29.in_connections_.append(self.obj32)
    self.obj32.graphObject_.pendingConnections.append((self.obj32.graphObject_.tag, self.obj29.graphObject_.tag, [133.0, 218.0, 141.0, 145.0], 2, 0))
    self.obj32.out_connections_.append(self.obj33)
    self.obj33.in_connections_.append(self.obj32)
    self.obj32.graphObject_.pendingConnections.append((self.obj32.graphObject_.tag, self.obj33.graphObject_.tag, [169.0, 173.0, 141.0, 145.0], 2, 0))
    self.obj33.out_connections_.append(self.obj30)
    self.obj30.in_connections_.append(self.obj33)
    self.obj33.graphObject_.pendingConnections.append((self.obj33.graphObject_.tag, self.obj30.graphObject_.tag, [234.0, 307.0, 227.0, 201.0], 2, 0))
    self.obj33.out_connections_.append(self.obj31)
    self.obj31.in_connections_.append(self.obj33)
    self.obj33.graphObject_.pendingConnections.append((self.obj33.graphObject_.tag, self.obj31.graphObject_.tag, [305.0, 312.0, 227.0, 201.0], 2, 0))

