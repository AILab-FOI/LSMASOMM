# _ THIS CLASS IS NOT USED!!!! GraphGrammarType.py ___________________________________________________________________________
# GraphGrammarType: a class that sobclasifies GraphGrammar. It is used to generate code
# for the types.
# ______________________________________________________________________________________________________

from GraphGrammar import *
from GGTypeRule1  import *
from GGTypeRule2  import *
from GGTypeRule3  import *

class GraphGrammarType (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [GGTypeRule1(parent), GGTypeRule2(parent), GGTypeRule3(parent)])		# for the moment a unique rule!

   def initialAction(self, graph):
      "action to be performed before the graph grammar starts its execution"
      # create the slot "FILE_" in each node of the graph...
      for tip in graph.listNodes.keys():
         for node in graph.listNodes[tip]:
            if tip == "SubType" :					# fill the slot, tuple (name, type)
                node.FILE_ = ( node.Type.getValue()[0] ,'ATOM3'+node.Type.getValue()[1])
            elif tip == "TypeName":
                node.FILE_ = node.Name.toString()
            else:
            	node.FILE_ = None

   def finalAction(self, graph):
      "action to be performed when the graph grammar finishes its execution"
      # delete the slot "FILE_" in each node of the graph...
      for tip in graph.listNodes.keys():
         for node in graph.listNodes[tip]:
            del node.FILE_


