# _ CD_to_ER.py ____________________________________________________________________________
# CD_to_ER : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from inheritance_semantics import *
class CD_to_ER (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [inheritance_semantics(parent)])
   def initialAction(self, graph):
      pass

   def finalAction(self, graph):
      pass

