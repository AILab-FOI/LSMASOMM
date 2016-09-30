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
def ClassDiagramB(self, rootNode):
   rootNode.Formalism_Name.setValue('ClassDiagramB')
   rootNode.RowSize.setValue(4)
   rootNode.Formalism_File.setValue('classDiagram/ClassDiagramB_MM.py')
   self.globalPrecondition(rootNode)

   self.objAtomClass=ButtonConfig(self)
   self.objAtomClass.Contents.Text.setValue('New AtomClass')
   self.objAtomClass.Contents.Image.setValue('')
   self.objAtomClass.Contents.lastSelected= 'Text'
   self.objAtomClass.Drawing_Mode.setValue(1)
   self.objAtomClass.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAtomClass (self, wherex, wherey)\n'))
   self.objAtomClass.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objAtomClass)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objAtomClass.graphObject_ = new_obj
   rootNode.addNode(self.objAtomClass)
   self.globalAndLocalPostcondition(self.objAtomClass, rootNode)
   self.globalPrecondition(rootNode)

   self.objAtomInheritance=ButtonConfig(self)
   self.objAtomInheritance.Contents.Text.setValue('New AtomInheritance')
   self.objAtomInheritance.Contents.Image.setValue('')
   self.objAtomInheritance.Contents.lastSelected= 'Text'
   self.objAtomInheritance.Drawing_Mode.setValue(1)
   self.objAtomInheritance.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAtomInheritance (self, wherex, wherey)\n'))
   self.objAtomInheritance.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 10,self.objAtomInheritance)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objAtomInheritance.graphObject_ = new_obj
   rootNode.addNode(self.objAtomInheritance)
   self.globalAndLocalPostcondition(self.objAtomInheritance, rootNode)
   self.globalPrecondition(rootNode)

   self.objAtomAssociation=ButtonConfig(self)
   self.objAtomAssociation.Contents.Text.setValue('New AtomAssociation')
   self.objAtomAssociation.Contents.Image.setValue('')
   self.objAtomAssociation.Contents.lastSelected= 'Text'
   self.objAtomAssociation.Drawing_Mode.setValue(1)
   self.objAtomAssociation.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAtomAssociation (self, wherex, wherey)\n'))
   self.objAtomAssociation.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 10,self.objAtomAssociation)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objAtomAssociation.graphObject_ = new_obj
   rootNode.addNode(self.objAtomAssociation)
   self.globalAndLocalPostcondition(self.objAtomAssociation, rootNode)
newfunction = ClassDiagramB
loadedMMName = 'Buttons'
