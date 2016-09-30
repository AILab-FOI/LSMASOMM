from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_Buttons import *
from ASG_Buttons import *
from ButtonConfig import *
from ATOM3Port import *
from ATOM3Integer import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Link import *
from ATOM3Boolean import *
from ATOM3Connection import *
from ATOM3List import *
from ATOM3Enum import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *

def TypesMetaModel(self, rootNode):
    rootNode.Formalism_Name.setValue('TypesMetaModel')
    rootNode.Formalism_File.setValue('TypeModels/TypesMetaModel_MM.py')
    rootNode.RowSize.setValue(1)

    self.globalPrecondition( rootNode )

    self.obj22=ButtonConfig(self)

    self.obj22.Contents.Text.setValue('New TypeName')
    self.obj22.Contents.Image.setValue('')
    self.obj22.Contents.lastSelected= "Text"
    self.obj22.Drawing_Mode.setValue((' ', 1))
    self.obj22.Drawing_Mode.config = 0
    self.obj22.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewTypeName (self, wherex, wherey)\n'))
    self.obj22.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(10,10,self.obj22)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj22.graphObject_ = new_obj
    rootNode.addNode(self.obj22)
    self.globalAndLocalPostcondition(self.obj22, rootNode)

    self.globalPrecondition( rootNode )

    self.obj23=ButtonConfig(self)

    self.obj23.Contents.Text.setValue('New LeafType')
    self.obj23.Contents.Image.setValue('')
    self.obj23.Contents.lastSelected= "Text"
    self.obj23.Drawing_Mode.setValue((' ', 1))
    self.obj23.Drawing_Mode.config = 0
    self.obj23.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewLeafType (self, wherex, wherey)\n'))
    self.obj23.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(135,10,self.obj23)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj23.graphObject_ = new_obj
    rootNode.addNode(self.obj23)
    self.globalAndLocalPostcondition(self.obj23, rootNode)

    self.globalPrecondition( rootNode )

    self.obj24=ButtonConfig(self)

    self.obj24.Contents.Text.setValue('New ModelType')
    self.obj24.Contents.Image.setValue('')
    self.obj24.Contents.lastSelected= "Text"
    self.obj24.Drawing_Mode.setValue((' ', 1))
    self.obj24.Drawing_Mode.config = 0
    self.obj24.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewModelType (self, wherex, wherey)\n'))
    self.obj24.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(260,10,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj24.graphObject_ = new_obj
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)

    self.globalPrecondition( rootNode )

    self.obj25=ButtonConfig(self)

    self.obj25.Contents.Text.setValue('New Operator')
    self.obj25.Contents.Image.setValue('')
    self.obj25.Contents.lastSelected= "Text"
    self.obj25.Drawing_Mode.setValue((' ', 1))
    self.obj25.Drawing_Mode.config = 0
    self.obj25.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOperator (self, wherex, wherey)\n'))
    self.obj25.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(10,80,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj25.graphObject_ = new_obj
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)

    self.globalPrecondition( rootNode )

    self.obj26=ButtonConfig(self)

    self.obj26.Contents.Text.setValue('Gen.Python')
    self.obj26.Contents.Image.setValue('')
    self.obj26.Contents.lastSelected= "Text"
    self.obj26.Drawing_Mode.setValue((' ', 0))
    self.obj26.Drawing_Mode.config = 0
    self.obj26.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\nfrom GraphRewritingSys import GraphRewritingSys\nfrom TypeCodeGen import TypeCodeGen\nself.grs = GraphRewritingSys(self, [TypeCodeGen(self)], self.ASGroot)\nself.grs.evaluate(0, 0, self.grs.SEQ_RANDOM)\n\n'))
    self.obj26.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(139.0,81.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj26.graphObject_ = new_obj
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)
    self.drawConnections( )

newfunction = TypesMetaModel

loadedMMName = 'Buttons'
