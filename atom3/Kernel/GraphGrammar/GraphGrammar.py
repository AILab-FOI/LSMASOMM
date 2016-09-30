# _ GraphGrammar.py __________________________________________________
# This class implements a graph grammar, that is basically an ordered
# collecttion of GGrule's
# ____________________________________________________________________

from GGrule import *

class GraphGrammar:

   def __init__(self, GGrules = None):
      "Constructor, it receives GGrules, that is a list of GGrule elements"

      self.GGrules = []				# We'll insert rules by order of execution
      self.rewritingSystem = None               # No rewriting system assigned yet

      while len(self.GGrules) < len(GGrules):   # iterate until each rule is inserted
         min = 30000				# set mininum number to a very high number
         minRule = None				# pointer to rule to be inserted
         for rule in GGrules:			# search for the minimum execution order that is not inserted
            if rule.executionOrder < min and not rule in self.GGrules:
               min = rule.executionOrder
               minRule = rule
         self.GGrules.append(minRule)

   def setGraphRewritingSystem(self, rs):
      "Sets the attribute rewritingSystem to rs and also calls the same method for each rule"
      self.rewritingSystem = rs
      for rule in self.GGrules:
         rule.setGraphGrammar(self)
         rule.setGraphRewritingSystem(rs)

   def initialAction(self, graph): # , atom3i = None):
      "action to be performed before the graph grammar starts its execution (must be overriden)"
      pass

   def finalAction(self, graph): #, atom3i = None):
      "action to be performed after the graph grammar starts its execution (must be overriden)"
      pass
