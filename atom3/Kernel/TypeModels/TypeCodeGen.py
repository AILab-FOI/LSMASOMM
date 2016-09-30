# _ TypeCodeGen.py ____________________________________________________________________________
# TypeCodeGen : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from TupleGen import *
from UnionGen import *
from TypeGen import *

class TypeCodeGen (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [TupleGen(parent) , UnionGen(parent) , TypeGen(parent)])
   def initialAction(self, graph):
      # create the slot "FILE_" in each node of the graph...
      for tip in graph.listNodes.keys():
        for node in graph.listNodes[tip]:
          if tip == "LeafType" :	# fill the slot, tuple (name, type)
            node.FILE_ = ( node.Type.getValue()[0] ,'ATOM3'+node.Type.getValue()[1])
          elif tip == "TypeName":
            node.FILE_ = node.Name.toString()
          elif tip == "ModelType":
            node.FILE_ = "ASG_"+node.MetaModelName.toString()
          else:
            node.FILE_ = None
      
      

   def finalAction(self, graph):
      for tip in graph.listNodes.keys():
        for node in graph.listNodes[tip]:
          del node.FILE_
      
      

