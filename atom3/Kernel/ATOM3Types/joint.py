from Tkinter             import *
from ATOM3Type           import *
from Operator            import *
from LeafType            import *
from TypeName            import *
from ASG_TypesMetaModel  import *
from stickylink 	 import *

class joint (stickylink):
  def createTypeGraph(self, atom3i, rootNode):

    self.obj35=TypeName(atom3i)

    self.obj35.Name.setValue('joint')
    self.obj35.graphClass_= graph_TypeName
    new_obj = graph_TypeName(334.0,185.0,self.obj35)
    self.obj35.graphObject_ = new_obj
    rootNode.addNode(self.obj35)

    self.obj37=LeafType(atom3i)

    self.obj37.Type.setValue(('arrow', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj37.Type.initialValue=ATOM3Boolean()
    self.obj37.Type.initialValue.setValue((' ', 0))
    self.obj37.Type.initialValue.config = 1
    self.obj37.graphClass_= graph_LeafType
    new_obj = graph_LeafType(141.0,292.0,self.obj37)
    self.obj37.graphObject_ = new_obj
    rootNode.addNode(self.obj37)

    self.obj39=LeafType(atom3i)

    self.obj39.Type.setValue(('arrowShape1', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj39.Type.initialValue=ATOM3Integer(0)
    self.obj39.graphClass_= graph_LeafType
    new_obj = graph_LeafType(194.0,351.0,self.obj39)
    self.obj39.graphObject_ = new_obj
    rootNode.addNode(self.obj39)

    self.obj42=LeafType(atom3i)

    self.obj42.Type.setValue(('arrowShape2', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj42.Type.initialValue=ATOM3Integer(0)
    self.obj42.graphClass_= graph_LeafType
    new_obj = graph_LeafType(328.0,375.0,self.obj42)
    self.obj42.graphObject_ = new_obj
    rootNode.addNode(self.obj42)

    self.obj44=LeafType(atom3i)

    self.obj44.Type.setValue(('arrowShape3', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj44.Type.initialValue=ATOM3Integer(0)
    self.obj44.graphClass_= graph_LeafType
    new_obj = graph_LeafType(473.0,354.0,self.obj44)
    self.obj44.graphObject_ = new_obj
    rootNode.addNode(self.obj44)

    self.obj46=LeafType(atom3i)

    self.obj46.Type.setValue(('decoration', 'Appearance', None, ('Key', 0), ('Direct Editing', 1)))
    self.obj46.Type.initialValue=ATOM3Appearance()
    self.obj46.Type.initialValue.setValue( ('class0', self.obj46.Type))
    self.obj46.graphClass_= graph_LeafType
    new_obj = graph_LeafType(522.0,297.0,self.obj46)
    self.obj46.graphObject_ = new_obj
    rootNode.addNode(self.obj46)

    self.obj48=Operator(atom3i)

    self.obj48.Type.setValue( (['U', 'X'], 1) )
    self.obj48.Type.config = 0
    self.obj48.graphClass_= graph_Operator
    new_obj = graph_Operator(361.0,268.0,self.obj48)
    self.obj48.graphObject_ = new_obj
    rootNode.addNode(self.obj48)
    self.obj35.out_connections_.append(self.obj48)
    self.obj48.in_connections_.append(self.obj35)
    self.obj48.out_connections_.append(self.obj37)
    self.obj37.in_connections_.append(self.obj48)
    self.obj48.out_connections_.append(self.obj39)
    self.obj39.in_connections_.append(self.obj48)
    self.obj48.out_connections_.append(self.obj42)
    self.obj42.in_connections_.append(self.obj48)
    self.obj48.out_connections_.append(self.obj44)
    self.obj44.in_connections_.append(self.obj48)
    self.obj48.out_connections_.append(self.obj46)
    self.obj46.in_connections_.append(self.obj48)

