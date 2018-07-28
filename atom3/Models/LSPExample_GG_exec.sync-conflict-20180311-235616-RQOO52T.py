# _ LSPExample_GG_exec.py ____________________________________________________________________________
# LSPExample : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from CreateParty_GG_rule import *
class LSPExample_GG_exec (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [CreateParty_GG_rule(parent)])
   def initialAction(self, graph):
      pass

   def finalAction(self, graph):
      pass

importedModules = ['CreateParty_GG_rule']

