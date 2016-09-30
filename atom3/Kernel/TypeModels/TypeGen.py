# _ TypeGen.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from ASG_TypesMetaModel import *
from ModelType import *
from Operator import *
from TypeName import *
from LeafType import *
class TypeGen (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 2)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_TypesMetaModel(parent)

      self.obj39=TypeName(parent)

      self.obj39.Name.setValue('')
      self.obj39.GGLabel.setValue(1)
      self.obj39.graphClass_= graph_TypeName
      if parent.genGraphics:
         from graph_TypeName import *
         new_obj = graph_TypeName(207.0,272.0,self.obj39)
      else: new_obj = None
      self.obj39.graphObject_ = new_obj
      self.LHS.addNode(self.obj39)
      self.RHS = ASG_TypesMetaModel(parent)

      self.obj41=TypeName(parent)

      self.obj41.Name.setValue('typename0')
      self.obj41.GGLabel.setValue(1)
      self.obj41.graphClass_= graph_TypeName
      if parent.genGraphics:
         from graph_TypeName import *
         new_obj = graph_TypeName(211.0,254.0,self.obj41)
      else: new_obj = None
      self.obj41.graphObject_ = new_obj
      self.obj410= AttrCalc()
      self.obj410.Copy=ATOM3Boolean()
      self.obj410.Copy.setValue(('Copy from LHS', 1))
      self.obj410.Copy.config = 0
      self.obj410.Specify=ATOM3Constraint()
      self.obj410.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj41.GGset2Any['Name']= self.obj410
      self.RHS.addNode(self.obj41)
   def condition(self, graphID, isograph, atom3i):
      "Condition that must be satisfied for the rule to be applicable on the isograph"
      # we can have multiple matches of the rule!
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      if node.FILE_!=isograph[0].Name.toString():                # This node has been processed yet!
         return 0
      
      self.generatedChilds = []
      for child in node.out_connections_:			# All childs must have the FILE_ slot filled...
         if child.FILE_:						# if this is the case, add to list
            self.generatedChilds.append(child)
         else:
            return 0							# otherwise, the condition does not hold...
      return 1	
      
      
      
      

   def action(self, graphID, isograph, atom3i):
      # compose the class name
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      className = node.FILE_
      childNode = node.out_connections_[0]                       # get child node
      fileName = className+".py"
      file = open(atom3i.codeGenDir+"/"+fileName, "w+t")			
      file.write("from Tkinter             import *\n")                              
      file.write("from ATOM3Type           import *\n")
      file.write("from Operator            import *\n")
      file.write("from LeafType             import *\n")
      file.write("from TypeName            import *\n")
      file.write("from ModelType           import *\n")
      file.write("from ASG_TypesMetaModel import *\n")
      # generate imports...
      file.write("from "+childNode.FILE_+" import *\n\n")
      
      
      file.write("class "+className+" ("+childNode.FILE_+"):\n")
      file.write("  def createTypeGraph(self, atom3i, rootNode):\n")
      file.write("    self.types = atom3i.types\n")
      node.rootNode.writeGraph2File(file, parentName="atom3i")
      file.write("\n")
      file.close()
      node.FILE_= None
      
      
      
      
      
      
      
      
      
      
      
      
      
      

