from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_Buttons import *
from ASG_Buttons import *
from ButtonConfig import *
from ATOM3BottomType import *
from ATOM3String import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Enum import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Link import *
from ATOM3File import *
from ATOM3Text import *
from ATOM3Integer import *
from ATOM3List import *
from ATOM3Port import *
from ATOM3MSEnum import *

def ClassDiagrams(self, rootNode):
    rootNode.RowSize.setValue(1)
    rootNode.Formalism_File.setValue('classDiagrams_2/ClassDiagramB_MM.py')
    rootNode.Formalism_Name.setValue('Class Diagrams')

    self.globalPrecondition( rootNode )

    self.obj25=ButtonConfig(self)

    self.obj25.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAtomClass (self, wherex, wherey)\n'))
    self.obj25.Drawing_Mode.setValue((' ', 1))
    self.obj25.Drawing_Mode.config = 0
    self.obj25.Contents.Text.setValue('Class')
    self.obj25.Contents.Image.setValue('classDiagram/Class.gif')
    self.obj25.Contents.lastSelected= "Image"
    self.obj25.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(10,10,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj25.graphObject_ = new_obj
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)

    self.globalPrecondition( rootNode )

    self.obj26=ButtonConfig(self)

    self.obj26.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAtomInheritance (self, wherex, wherey)\n'))
    self.obj26.Drawing_Mode.setValue((' ', 1))
    self.obj26.Drawing_Mode.config = 0
    self.obj26.Contents.Text.setValue('Inheritance')
    self.obj26.Contents.Image.setValue('classDiagram/Inherits.gif')
    self.obj26.Contents.lastSelected= "Image"
    self.obj26.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(11.0,70.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj26.graphObject_ = new_obj
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)

    self.globalPrecondition( rootNode )

    self.obj27=ButtonConfig(self)

    self.obj27.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAtomAssociation (self, wherex, wherey)\n'))
    self.obj27.Drawing_Mode.setValue((' ', 1))
    self.obj27.Drawing_Mode.config = 0
    self.obj27.Contents.Text.setValue('Association')
    self.obj27.Contents.Image.setValue('classDiagram/Association.gif')
    self.obj27.Contents.lastSelected= "Image"
    self.obj27.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(11.0,129.0,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj27.graphObject_ = new_obj
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)

    self.globalPrecondition( rootNode )

    self.obj28=ButtonConfig(self)

    self.obj28.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\nfrom CDCodeGeneratorHelper import *\n\ngenCodeClassDiagram(self)\n\n'))
    self.obj28.Drawing_Mode.setValue((' ', 0))
    self.obj28.Drawing_Mode.config = 0
    self.obj28.Contents.Text.setValue('Generate Code')
    self.obj28.Contents.Image.setValue('classDiagram/genCode.gif')
    self.obj28.Contents.lastSelected= "Image"
    self.obj28.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(12.0,189.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)
    self.drawConnections( )

newfunction = ClassDiagrams

loadedMMName = 'Buttons'
