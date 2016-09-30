"""
__Buttons_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: Denis Dube
Modified: Mon Mar 28 23:16:55 2005
______________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
from ButtonConfig import *
from graph_ButtonConfig import *
from ImageText import *
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
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def Buttons_META(self, rootNode, ButtonsRootNode=None):

    # --- Generating attributes code for ASG Buttons ---
    if( ButtonsRootNode ): 
        # RowSize
        ButtonsRootNode.RowSize.setValue(4)

        # Formalism_File
        ButtonsRootNode.Formalism_File.setValue('Buttons_MM.py')

        # Formalism_Name
        ButtonsRootNode.Formalism_Name.setValue('Buttons_MM')
    # --- ASG attributes over ---


    self.obj54=ButtonConfig(self)
    self.obj54.isGraphObjectVisual = True


    # Action
    self.obj54.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewButtonConfig (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj54.Drawing_Mode.setValue((' ', 1))
    self.obj54.Drawing_Mode.config = 0

    # Contents
    self.obj54.Contents.Text.setValue('New ButtonConfig')
    self.obj54.Contents.Image.setValue('ButtonsModels/Button.gif')
    self.obj54.Contents.lastSelected= "Image"

    self.obj54.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(80.0,120.0,self.obj54)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.8100000000000005, 0.98999999999999999]
    else: new_obj = None
    self.obj54.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj54)
    self.globalAndLocalPostcondition(self.obj54, rootNode)

    self.obj56=ButtonConfig(self)
    self.obj56.isGraphObjectVisual = True


    # Action
    self.obj56.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\nself.modelAttributes(self.ASGroot.getASGbyName("Buttons_META")) \n'))

    # Drawing_Mode
    self.obj56.Drawing_Mode.setValue((' ', 0))
    self.obj56.Drawing_Mode.config = 0

    # Contents
    self.obj56.Contents.Text.setValue('')
    self.obj56.Contents.Text.setNone()
    self.obj56.Contents.Image.setValue('ButtonsModels/edit.gif')
    self.obj56.Contents.lastSelected= "Image"

    self.obj56.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(80.0,280.0,self.obj56)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.7900000000000007, 1.1000000000000001]
    else: new_obj = None
    self.obj56.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj56)
    self.globalAndLocalPostcondition(self.obj56, rootNode)
    
    self.obj55=ButtonConfig(self)
    self.obj55.isGraphObjectVisual = True


    # Action
    self.obj55.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\nfrom HelpDialog import HelpDialog\nHelpDialog( [\'ButtonsHelp.txt\'] )\n\n'))

    # Drawing_Mode
    self.obj55.Drawing_Mode.setValue((' ', 0))
    self.obj55.Drawing_Mode.config = 0

    # Contents
    self.obj55.Contents.Text.setValue('Close all other formalisms FIRST')
    self.obj55.Contents.Image.setValue('ButtonsModels/help.gif')
    self.obj55.Contents.lastSelected= "Image"

    self.obj55.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(80.0,200.0,self.obj55)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.7800000000000007, 1.03]
    else: new_obj = None
    self.obj55.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj55)
    self.globalAndLocalPostcondition(self.obj55, rootNode)
    
    
    self.drawConnections( )

newfunction = Buttons_META

loadedMMName = 'Buttons'

atom3version = '0.3'
