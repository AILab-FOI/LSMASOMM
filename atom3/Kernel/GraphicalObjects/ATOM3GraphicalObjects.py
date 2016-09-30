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
def ATOM3GraphicalObjects(self, rootNode):
   rootNode.Formalism_Name.setValue('ATOM3GraphicalObjects')
   rootNode.RowSize.setValue(4)
   rootNode.Formalism_File.setValue('UserInterface/ATOM3GraphicalObjects_MM.py')
   self.globalPrecondition(rootNode)

   self.objline=ButtonConfig(self)
   self.objline.Contents.Text.setValue('New line')
   self.objline.Contents.Image.setValue('')
   self.objline.Contents.lastSelected= 'Text'
   self.objline.Drawing_Mode.setValue(1)
   self.objline.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewline (self, wherex, wherey)\n'))
   self.objline.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objline)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objline.graphObject_ = new_obj
   rootNode.addNode(self.objline)
   self.globalAndLocalPostcondition(self.objline, rootNode)
   self.globalPrecondition(rootNode)

   self.objoval=ButtonConfig(self)
   self.objoval.Contents.Text.setValue('New oval')
   self.objoval.Contents.Image.setValue('')
   self.objoval.Contents.lastSelected= 'Text'
   self.objoval.Drawing_Mode.setValue(1)
   self.objoval.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewoval (self, wherex, wherey)\n'))
   self.objoval.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 10,self.objoval)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objoval.graphObject_ = new_obj
   rootNode.addNode(self.objoval)
   self.globalAndLocalPostcondition(self.objoval, rootNode)
   self.globalPrecondition(rootNode)

   self.objpolygon=ButtonConfig(self)
   self.objpolygon.Contents.Text.setValue('New polygon')
   self.objpolygon.Contents.Image.setValue('')
   self.objpolygon.Contents.lastSelected= 'Text'
   self.objpolygon.Drawing_Mode.setValue(1)
   self.objpolygon.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewpolygon (self, wherex, wherey)\n'))
   self.objpolygon.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 10,self.objpolygon)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objpolygon.graphObject_ = new_obj
   rootNode.addNode(self.objpolygon)
   self.globalAndLocalPostcondition(self.objpolygon, rootNode)
   self.globalPrecondition(rootNode)

   self.objrectangle=ButtonConfig(self)
   self.objrectangle.Contents.Text.setValue('New rectangle')
   self.objrectangle.Contents.Image.setValue('')
   self.objrectangle.Contents.lastSelected= 'Text'
   self.objrectangle.Drawing_Mode.setValue(1)
   self.objrectangle.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewrectangle (self, wherex, wherey)\n'))
   self.objrectangle.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 80,self.objrectangle)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objrectangle.graphObject_ = new_obj
   rootNode.addNode(self.objrectangle)
   self.globalAndLocalPostcondition(self.objrectangle, rootNode)
   self.globalPrecondition(rootNode)

   self.objtext=ButtonConfig(self)
   self.objtext.Contents.Text.setValue('New text')
   self.objtext.Contents.Image.setValue('')
   self.objtext.Contents.lastSelected= 'Text'
   self.objtext.Drawing_Mode.setValue(1)
   self.objtext.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewtext (self, wherex, wherey)\n'))
   self.objtext.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objtext)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objtext.graphObject_ = new_obj
   rootNode.addNode(self.objtext)
   self.globalAndLocalPostcondition(self.objtext, rootNode)
newfunction = ATOM3GraphicalObjects
loadedMMName = 'Buttons'
