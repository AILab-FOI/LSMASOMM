# _ GGLlistRule1.py ______________________________________________________
# Simple Graph Grammar rule for inserting an element in the list
# _______________________________________________________________________

from GGrule 	        import *
from ASG_LinkedListMM   import *
from Element       	import *
from Bottom       	import *
from Top       		import *
from LLink       	import *

class GGLListRule1(GGrule):

   def __init__(self, parent):
      GGrule.__init__(self,1)                   		# this is the first rule to be executed
      # create the pattern...
      self.LHS = ASG_LinkedListMM()             		# create LHS

      self.LHSnode1 = Top(parent)                  		# List head
      self.LHSnode1.graphObject_ = graph_Top(10,10,self.LHSnode1) # graphical representation...
      self.LHSnode1.setGGLabel(1)				# Set Graph Grammar Label...

      self.LHSnode2 = LLink(parent)                		# Link to 1st. element
      self.LHSnode2.graphObject_ = graph_LLink(30,60,self.LHSnode2) # graphical representation...
      self.LHSnode2.setGGLabel(2)				# Set Graph Grammar Label...

      self.LHSnode3 = Element(parent)              		# Any value
      self.LHSnode3.graphObject_ = graph_Element(10,150,self.LHSnode3) # graphical representation...
      self.LHSnode3.Label.setNone()
      self.LHSnode3.setGGLabel(3)				# Set Graph Grammar Label...

      self.LHSnode1.out_connections_.append(self.LHSnode2)    	# n1 -> n2
      self.LHSnode2.in_connections_.append(self.LHSnode1)

      self.LHSnode2.out_connections_.append(self.LHSnode3)    	# n2 -> n3
      self.LHSnode3.in_connections_.append(self.LHSnode2)

      self.LHS.addNode(self.LHSnode1)
      self.LHS.addNode(self.LHSnode2)
      self.LHS.addNode(self.LHSnode3)

      # create RHS...

      self.RHS = ASG_LinkedListMM()				# Also a Linked List...

      self.RHSnode1 = Top(parent)				# List head
      self.RHSnode1.graphObject_ = graph_Top(10,10, self.RHSnode1) # graphical representation...
      self.RHSnode1.setGGLabel(1)				# Set Graph Grammar Label...

      self.RHSnode2 = LLink(parent)				# Link to inserted element
      self.RHSnode2.graphObject_ = graph_LLink(30,60, self.RHSnode2) # graphical representation...
      self.RHSnode2.setGGLabel(2)				# Set Graph Grammar Label...

      self.RHSnode3 = Element(parent)				# NEW ELEMENT
      self.RHSnode3.Label.setValue('NEW ELEMENT')
      self.RHSnode3.graphObject_ = graph_Element(10,150, self.RHSnode3) # graphical representation...
      self.RHSnode3.setGGLabel(4)				# Set Graph Grammar Label (NEW LABEL)

      self.RHSnode4 = LLink(parent)				# Link to inserted element
      self.RHSnode4.graphObject_ = graph_LLink(30,220,self.RHSnode4) # graphical representation...
      self.RHSnode4.setGGLabel(5)				# Set Graph Grammar Label...

      self.RHSnode5 = Element(parent)              		# Any value
      self.RHSnode5.Label.setNone()
      self.RHSnode5.graphObject_ = graph_Element(10,280, self.RHSnode5) # graphical representation...
      self.RHSnode5.setGGLabel(3)				# Set Graph Grammar Label...

      self.RHSnode1.out_connections_.append(self.RHSnode2)    	# n1 -> n2
      self.RHSnode2.in_connections_.append(self.RHSnode1)

      self.RHSnode2.out_connections_.append(self.RHSnode3)    	# n2 -> n3
      self.RHSnode3.in_connections_.append(self.RHSnode2)

      self.RHSnode3.out_connections_.append(self.RHSnode4)    	# n3 -> n4
      self.RHSnode4.in_connections_.append(self.RHSnode3)

      self.RHSnode4.out_connections_.append(self.RHSnode5)    	# n4 -> n5
      self.RHSnode5.in_connections_.append(self.RHSnode4)

      self.RHS.addNode(self.RHSnode1)
      self.RHS.addNode(self.RHSnode2)
      self.RHS.addNode(self.RHSnode3)
      self.RHS.addNode(self.RHSnode4)
      self.RHS.addNode(self.RHSnode5)

   def condition(self, isograph):
      "Condition that must be satisfied for the rule to be applicable on the isograph"
      return 1								# condition hold

   def action(self, isograph):
      pass


