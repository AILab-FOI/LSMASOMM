from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_GenericGraph import *
from ASG_GenericGraph import *
from GenericGraphNode import *
from GenericGraphEdge import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def test_GenericGraph_mdl(self, rootNode):

    self.globalPrecondition( rootNode )

    self.obj52=GenericGraphNode(self)

    self.obj52.graphClass_= graph_GenericGraphNode
    if self.genGraphics:
       from graph_GenericGraphNode import *
       new_obj = graph_GenericGraphNode(182.0,111.0,self.obj52)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("GenericGraphNode", new_obj.tag)
    else: new_obj = None
    self.obj52.graphObject_ = new_obj
    rootNode.addNode(self.obj52)
    self.globalAndLocalPostcondition(self.obj52, rootNode)

    self.globalPrecondition( rootNode )

    self.obj56=GenericGraphEdge(self)

    self.obj56.graphClass_= graph_GenericGraphEdge
    if self.genGraphics:
       from graph_GenericGraphEdge import *
       new_obj = graph_GenericGraphEdge(249.0,218.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("GenericGraphEdge", new_obj.tag)
    else: new_obj = None
    self.obj56.graphObject_ = new_obj
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    self.drawConnections( )

newfunction = test_GenericGraph_mdl

loadedMMName = 'GenericGraph'
