from ASG_Buttons import *
from ButtonConfig import *
from ATOM3Enum import *
from ATOM3List import *
from ATOM3Float import *
from ATOM3Integer import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Link import *
def NewCD(self, rootNode):
   rootNode.Formalism_Name.setValue('NewCD')
   rootNode.RowSize.setValue(4)
   rootNode.Formalism_File.setValue('classDiagrams_2/NewCD_MM.py')
   self.globalPrecondition(rootNode)

   self.objMyClass0=ButtonConfig(self)
   self.objMyClass0.Contents.Text.setValue('New MyClass0')
   self.objMyClass0.Contents.Image.setValue('')
   self.objMyClass0.Contents.lastSelected= 'Text'
   self.objMyClass0.Drawing_Mode.setValue(1)
   self.objMyClass0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMyClass0 (self, wherex, wherey)\n'))
   self.objMyClass0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objMyClass0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMyClass0.graphObject_ = new_obj
   rootNode.addNode(self.objMyClass0)
   self.globalAndLocalPostcondition(self.objMyClass0, rootNode)
   self.globalPrecondition(rootNode)

   self.objMyClass1=ButtonConfig(self)
   self.objMyClass1.Contents.Text.setValue('New MyClass1')
   self.objMyClass1.Contents.Image.setValue('')
   self.objMyClass1.Contents.lastSelected= 'Text'
   self.objMyClass1.Drawing_Mode.setValue(1)
   self.objMyClass1.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMyClass1 (self, wherex, wherey)\n'))
   self.objMyClass1.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 10,self.objMyClass1)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMyClass1.graphObject_ = new_obj
   rootNode.addNode(self.objMyClass1)
   self.globalAndLocalPostcondition(self.objMyClass1, rootNode)
   self.globalPrecondition(rootNode)

   self.objMyClass2=ButtonConfig(self)
   self.objMyClass2.Contents.Text.setValue('New MyClass2')
   self.objMyClass2.Contents.Image.setValue('')
   self.objMyClass2.Contents.lastSelected= 'Text'
   self.objMyClass2.Drawing_Mode.setValue(1)
   self.objMyClass2.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMyClass2 (self, wherex, wherey)\n'))
   self.objMyClass2.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 10,self.objMyClass2)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMyClass2.graphObject_ = new_obj
   rootNode.addNode(self.objMyClass2)
   self.globalAndLocalPostcondition(self.objMyClass2, rootNode)
   self.globalPrecondition(rootNode)

   self.objMyAssociation0=ButtonConfig(self)
   self.objMyAssociation0.Contents.Text.setValue('New MyAssociation0')
   self.objMyAssociation0.Contents.Image.setValue('')
   self.objMyAssociation0.Contents.lastSelected= 'Text'
   self.objMyAssociation0.Drawing_Mode.setValue(1)
   self.objMyAssociation0.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewMyAssociation0 (self, wherex, wherey)\n'))
   self.objMyAssociation0.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 80,self.objMyAssociation0)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objMyAssociation0.graphObject_ = new_obj
   rootNode.addNode(self.objMyAssociation0)
   self.globalAndLocalPostcondition(self.objMyAssociation0, rootNode)
newfunction = NewCD
loadedMMName = 'Buttons'
