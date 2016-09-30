"""
ButtonGenerator.py

By Denis Dube, 2006
Because I'm fed up of re-doing buttons grammars for code generation
Or switching between different grammars. ugh. 
"""

import time, os, Dialog
from FilePaths           import USER_NAME
from OptionDialog import OptionDialog, simpleOptionWrapper

def ButtonGenerator(self, ASGroot):
  
  
  nameButtonBar = ASGroot.keyword_.toString()
  metaNameString = nameButtonBar + "_META"
  newMetaModelPath = os.path.join( self.codeGenDir, nameButtonBar+"_META.py" )
  buttonModelExists = os.path.exists(newMetaModelPath)

#===============================================================================
#  Figure out what (nodeTypes) to generate buttons for 
#===============================================================================
  nodeTypesToGenList = []

  optsDB = simpleOptionWrapper()
  for nodeType in ASGroot.listNodes:
    optsDB.add(str(nodeType), [0, OptionDialog.BOOLEAN_ENTRY, str(nodeType), ""])
  
  if(buttonModelExists):
    optEntry = 'DO NOT RE-GENERATE BUTTONS'
    help = 'If you re-generate, you lose any manually added buttons'
    optsDB.add(optEntry, [True, OptionDialog.BOOLEAN_ENTRY, optEntry, help])
    
  # Call optsDB to show the Options Dialog to the user
  result = optsDB(self.parent, 'Select entities to generate buttons for')
  if( result.isCanceled() ):
    print "Dialog aborted by user cancel"
  else:
    resultDict = result.getOptionsDatabase()
    for option in optsDB.getOrderedOptionsKeys():
      if(buttonModelExists and option == optEntry):
        if(resultDict[option][0]):
          return # We didn't want to re-generate the buttons
      elif(resultDict[option][0]):
        nodeTypesToGenList.append(option)
       
  
#===============================================================================
#  Header
#===============================================================================
  
  file = open( newMetaModelPath, 'w' )
  file.write('"""\n')
  file.write("__"+ nameButtonBar+"_META.py_____________________________________________________\n")
  file.write("\n")
  file.write("Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)\n")
  file.write("Author: "+USER_NAME+"\n")
  file.write("Modified: "+time.asctime()+"\n")
  file.write("__"+ len(nameButtonBar+"_META.py")*"_" +"_____________________________________________________\n")
  file.write('"""\n')  
   
  file.write("from ASG_Buttons import *\n")
  file.write("from ButtonConfig import *\n")
  file.write("from ATOM3Enum import *\n")
  file.write("from ATOM3List import *\n")
  file.write("from ATOM3Float import *\n")
  file.write("from ATOM3Integer import *\n")
  file.write("from ATOM3Attribute import *\n")
  file.write("from ATOM3Constraint import *\n")
  file.write("from ATOM3Action import *\n")
  file.write("from ATOM3String import *\n")
  file.write("from ATOM3BottomType import *\n")
  file.write("from ATOM3Boolean import *\n")
  file.write("from ATOM3Appearance import *\n")
  file.write("from ATOM3Link import *\n")
  file.write("def "+metaNameString+"(self, rootNode, ButtonsRootNode):\n")
  file.write("   ButtonsRootNode.Formalism_Name.setValue('"
                                              +metaNameString+"')\n")
  file.write("   ButtonsRootNode.RowSize.setValue(4)\n")
  
  formFile = nameButtonBar + "_MM.py" 
  file.write("   ButtonsRootNode.Formalism_File.setValue( '" + formFile + "' )\n" )
      
  numberOfButtons = 0
      
#===============================================================================
#  Insert a 'Edit' button
#===============================================================================

  file.write("\n\n")
  posx, posy = 10, 10
  numberOfButtons += 1
  ename = 'Edit'
  file.write("   self.globalPrecondition(rootNode)\n\n")
  file.write("   self.obj"+ename+"=ButtonConfig(self)\n")
  file.write("   self.obj"+ename+".Contents.Text.setValue('"+ename+"')\n")
  file.write("   self.obj"+ename+".Contents.Image.setValue('')\n")
  file.write("   self.obj"+ename+".Contents.lastSelected= 'Text'\n")
  file.write("   self.obj"+ename+".Drawing_Mode.setValue(0)\n")
  file.write("   self.obj"+ename+".Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), ")
  file.write("(['PREcondition', 'POSTcondition'], 1),")
  file.write("(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], ")
  file.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")
  file.write("'# This method has as parameters:\\n")
  file.write("#   - wherex : X Position in window coordinates where the user clicked.\\n")
  file.write("#   - wherey : Y Position in window coordinates where the user clicked.\\n")
  file.write("self.modelAttributes(self.ASGroot.getASGbyName(\"%s\")) ') )\n" % 
                                          (metaNameString) )
  ename = 'obj' + ename
  file.write("   self."+ename+".graphClass_= graph_ButtonConfig\n")
  file.write("   if self.genGraphics:\n")
  file.write("      from graph_ButtonConfig import *\n")
  file.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self."+ename+")\n")
  file.write("      new_obj.DrawObject(self.UMLmodel)\n")
  file.write("      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)\n")
  file.write("   else: new_obj = None\n")
  file.write("   self."+ename+".graphObject_ = new_obj\n")
  file.write("   rootNode.addNode(self."+ename+")\n")
  file.write("   self.globalAndLocalPostcondition(self."+ename+", rootNode)\n\n")
      

#===============================================================================
#  Insert a 'Help' button
#===============================================================================

  file.write("\n\n")
  posx, posy = 10+125*(numberOfButtons%3), 10+70*(numberOfButtons%3)
  numberOfButtons += 1
  ename = 'Help'
  file.write("   self.globalPrecondition(rootNode)\n\n")
  file.write("   self.obj"+ename+"=ButtonConfig(self)\n")
  file.write("   self.obj"+ename+".Contents.Text.setValue('"+ename+"')\n")
  file.write("   self.obj"+ename+".Contents.Image.setValue('')\n")
  file.write("   self.obj"+ename+".Contents.lastSelected= 'Text'\n")
  file.write("   self.obj"+ename+".Drawing_Mode.setValue(0)\n")
  file.write("   self.obj"+ename+".Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), ")
  file.write("(['PREcondition', 'POSTcondition'], 1),")
  file.write("(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], ")
  file.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")
  
  file.write("'# This method has as parameters:\\n")
  file.write("#   - wherex : X Position in window coordinates where the user clicked.\\n")
  file.write("#   - wherey : Y Position in window coordinates where the user clicked.\\n")
  file.write("from HelpDialog import HelpDialog\\n")
  file.write("HelpDialog([\"%s\"])\\n" % (metaNameString+'Help.txt') ) 
  file.write(" ') )\n" )
  
  ename = 'obj' + ename
  file.write("   self."+ename+".graphClass_= graph_ButtonConfig\n")
  file.write("   if self.genGraphics:\n")
  file.write("      from graph_ButtonConfig import *\n")
  file.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self."+ename+")\n")
  file.write("      new_obj.DrawObject(self.UMLmodel)\n")
  file.write("      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)\n")
  file.write("   else: new_obj = None\n")
  file.write("   self."+ename+".graphObject_ = new_obj\n")
  file.write("   rootNode.addNode(self."+ename+")\n")
  file.write("   self.globalAndLocalPostcondition(self."+ename+", rootNode)\n\n")
      
      
#===============================================================================
#  Button Generator
#===============================================================================

  for nodeType in nodeTypesToGenList:
    for entity in ASGroot.listNodes[nodeType]:
  
      posx, posy = 10+125*(numberOfButtons%3), 10+70*(numberOfButtons%3)
      numberOfButtons += 1
      ename = entity.name.toString()
      file.write("   self.globalPrecondition(rootNode)\n\n")
      file.write("   self.obj"+ename+"=ButtonConfig(self)\n")
      file.write("   self.obj"+ename+".Contents.Text.setValue('New "+ename+"')\n")
      file.write("   self.obj"+ename+".Contents.Image.setValue('')\n")
      file.write("   self.obj"+ename+".Contents.lastSelected= 'Text'\n")
      file.write("   self.obj"+ename+".Drawing_Mode.setValue(1)\n")
      file.write("   self.obj"+ename+".Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), ")
      file.write("(['PREcondition', 'POSTcondition'], 1),")
      file.write("(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], ")
      file.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")
      file.write("'# This method has as parameters:\\n")
      file.write("#   - wherex : X Position in window coordinates where the user clicked.\\n")
      file.write("#   - wherey : Y Position in window coordinates where the user clicked.\\n")
      file.write("newPlace = self.createNew"+ename+" (self, wherex, wherey)\\n'))\n")
      file.write("   self.obj"+ename+".graphClass_= graph_ButtonConfig\n")
      file.write("   if self.genGraphics:\n")
      file.write("      from graph_ButtonConfig import *\n")
      file.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+ename+")\n")
      file.write("      new_obj.DrawObject(self.UMLmodel)\n")
      file.write("      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)\n")
      file.write("   else: new_obj = None\n")
      file.write("   self.obj"+ename+".graphObject_ = new_obj\n")
      file.write("   rootNode.addNode(self.obj"+ename+")\n")
      file.write("   self.globalAndLocalPostcondition(self.obj"+ename+", rootNode)\n")



#===============================================================================
#  Footer
#===============================================================================

  file.write("\nnewfunction = "+metaNameString+"\n")
  file.write("\nloadedMMName = 'Buttons'\n")
  file.write( '\natom3version = \'0.3\'\n' )
  file.close() 

      
   