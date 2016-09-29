from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_Buttons import *
from ASG_Buttons import *
from ButtonConfig import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def GenericGraph(self, rootNode):
    rootNode.RowSize.setValue(1)
    rootNode.Formalism_File.setValue('GenericGraph/GenericGraph_MM.py')
    rootNode.Formalism_Name.setValue('GenericGraph')

    self.globalPrecondition( rootNode )

    self.obj27=ButtonConfig(self)

    self.obj27.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewGenericGraphNode (self, wherex, wherey)\n'))
    self.obj27.Drawing_Mode.setValue((' ', 1))
    self.obj27.Drawing_Mode.config = 0
    self.obj27.Contents.Text.setValue('New GenericGraphNode')
    self.obj27.Contents.Image.setValue('GenericGraph/GenericGraphNode.gif')
    self.obj27.Contents.lastSelected= "Image"
    self.obj27.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(68.0,33.0,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj27.graphObject_ = new_obj
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)

    self.globalPrecondition( rootNode )

    self.obj28=ButtonConfig(self)

    self.obj28.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewGenericGraphEdge (self, wherex, wherey)\n'))
    self.obj28.Drawing_Mode.setValue((' ', 1))
    self.obj28.Drawing_Mode.config = 0
    self.obj28.Contents.Text.setValue('New GenericGraphEdge')
    self.obj28.Contents.Image.setValue('GenericGraph/GenericGraphEdge.gif')
    self.obj28.Contents.lastSelected= "Image"
    self.obj28.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(67.0,109.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)
    self.drawConnections( )

newfunction = GenericGraph

loadedMMName = 'Buttons'
