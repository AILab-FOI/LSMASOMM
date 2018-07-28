# _ LSPExample_GG_exec.py ____________________________________________________________________________
# LSPExample : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from AddRoles_GG_rule import *
class LSPExample_GG_exec (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [AddRoles_GG_rule(parent)])
   def initialAction(self, graph):
      pass

   def finalAction(self, graph):
      pass

importedModules = ['AddRoles_GG_rule']

