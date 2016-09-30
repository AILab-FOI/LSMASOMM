from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_Buttons import *
from ButtonConfig import *
from graph_ButtonConfig import *
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

def EntityRelationship_META(self, rootNode):
    rootNode.RowSize.setValue(1)
    rootNode.Formalism_File.setValue('ERModels/ERmetaMetaModel_MM.py')
    rootNode.Formalism_Name.setValue('Entity Relationship')

    self.globalPrecondition( rootNode )

    self.obj25=ButtonConfig(self)

    self.obj25.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewERentity (self, wherex, wherey)\n'))
    self.obj25.Drawing_Mode.setValue((' ', 1))
    self.obj25.Drawing_Mode.config = 0
    self.obj25.Contents.Text.setValue('Entity')
    self.obj25.Contents.Image.setValue('ERModels/Entity.gif')
    self.obj25.Contents.lastSelected= "Image"
    self.obj25.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(20.0,20.0,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.8800000000000006, 0.7799999999999998]
    else: new_obj = None
    self.obj25.graphObject_ = new_obj
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)

    self.globalPrecondition( rootNode )

    self.obj26=ButtonConfig(self)

    self.obj26.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewERrelationship (self, wherex, wherey)\n\n'))
    self.obj26.Drawing_Mode.setValue((' ', 1))
    self.obj26.Drawing_Mode.config = 0
    self.obj26.Contents.Text.setValue('Relationship')
    self.obj26.Contents.Image.setValue('ERModels/Relationship.gif')
    self.obj26.Contents.lastSelected= "Image"
    self.obj26.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(20.0,80.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.8800000000000006, 0.7799999999999998]
    else: new_obj = None
    self.obj26.graphObject_ = new_obj
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)

    self.globalPrecondition( rootNode )

    self.obj27=ButtonConfig(self)

    self.obj27.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nself.genCode()\n\n\n\n\n'))
    self.obj27.Drawing_Mode.setValue((' ', 0))
    self.obj27.Drawing_Mode.config = 0
    self.obj27.Contents.Text.setValue('Generate Code')
    self.obj27.Contents.Image.setValue('ERModels/gen.gif')
    self.obj27.Contents.lastSelected= "Image"
    self.obj27.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(20.0,140.0,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.8800000000000006, 0.7799999999999998]
    else: new_obj = None
    self.obj27.graphObject_ = new_obj
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)

    self.globalPrecondition( rootNode )

    self.obj28=ButtonConfig(self)

    self.obj28.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nself.modelAttributes()\n\n\n\n\n\n'))
    self.obj28.Drawing_Mode.setValue((' ', 0))
    self.obj28.Drawing_Mode.config = 0
    self.obj28.Contents.Text.setValue('Edit Attributes')
    self.obj28.Contents.Image.setValue('ERModels/edit.gif')
    self.obj28.Contents.lastSelected= "Image"
    self.obj28.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(20.0,200.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.8800000000000006, 0.7799999999999998]
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)
    self.drawConnections( )

newfunction = EntityRelationship_META

loadedMMName = 'Buttons'
