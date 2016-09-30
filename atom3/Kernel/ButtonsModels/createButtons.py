# _ createButtons.py ____________________________________________________________________________
# createButtons : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.
# ___________________________________________________________________________________________
from GraphGrammar import *
from buttonFromEntity import *
from buttonFromRelationship import *
class createButtons (GraphGrammar):
   def __init__ (self, parent):
      GraphGrammar.__init__(self, [buttonFromEntity(parent) , buttonFromRelationship(parent)])
   def initialAction(self, graph):
      self.rewritingSystem.name = self.rewritingSystem.parent.ASGroot.keyword_.toString()
      self.rewritingSystem.NButtons = 0
      fileName = self.rewritingSystem.name+".py"
      cgd = self.rewritingSystem.parent.codeGenDir
      self.rewritingSystem.file = open(cgd+"/"+fileName,"w+t")
      file = self.rewritingSystem.file
      file.write("from ASG_Buttons import *\n")
      file.write("from ButtonConfig import *\n")
      file.write("from ATOM3Enum import *\n")
      file.write("from ATOM3List import *\n")
      file.write("from ATOM3Float import *\n")
      file.write("from ATOM3Integer import *\n")
      file.write("from ATOM3Attribute import *\n")
      file.write("from ATOM3Constraint import *\n")
      file.write("from ATOM3String import *\n")
      file.write("from ATOM3BottomType import *\n")
      file.write("from ATOM3Boolean import *\n")
      file.write("from ATOM3Appearance import *\n")
      file.write("from ATOM3Link import *\n")
      file.write("def "+self.rewritingSystem.name+"(self, rootNode):\n")
      file.write("   rootNode.Formalism_Name.setValue('"+self.rewritingSystem.name+"')\n")
      file.write("   rootNode.RowSize.setValue(4)\n")
      file.write("   rootNode.Formalism_File.setValue('"+cgd+"/"+self.rewritingSystem.name+"_MM.py')\n")
      for nt in graph.listNodes.keys():
         for node in graph.listNodes[nt]:
            node.visited = 0      
      
      
      
      
      

   def finalAction(self, graph):
      file = self.rewritingSystem.file
      
      file.write("newfunction = "+self.rewritingSystem.name+"\n")
      file.write("loadedMMName = 'Buttons'\n")
      
      for nt in graph.listNodes.keys():
         for node in graph.listNodes[nt]:
            del node.visited     
         
      del self.rewritingSystem.file
      del self.rewritingSystem.NButtons
      
      
      

