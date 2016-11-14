"""
__LSMASOMM_META.py_____________________________________________________

Automatically generated AToM3 Model File (Do not modify directly)
Author: bogdan
Modified: Mon Nov 14 16:13:04 2016
_______________________________________________________________________
"""
from stickylink import *
from widthXfillXdecoration import *
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
from ATOM3Action import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def LSMASOMM_META(self, rootNode, ButtonsRootNode=None):

    # --- Generating attributes code for ASG Buttons ---
    if( ButtonsRootNode ): 
        # RowSize
        ButtonsRootNode.RowSize.setValue(4)

        # Formalism_File
        ButtonsRootNode.Formalism_File.setValue('LSMASOMM_MM.py')

        # Formalism_Name
        ButtonsRootNode.Formalism_Name.setValue('LSMASOMM_META')
    # --- ASG attributes over ---


    self.obj21=ButtonConfig(self)
    self.obj21.isGraphObjectVisual = True

    if(hasattr(self.obj21, '_setHierarchicalLink')):
      self.obj21._setHierarchicalLink(False)

    # Action
    self.obj21.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nself.modelAttributes(self.ASGroot.getASGbyName("LSMASOMM_META")) '))

    # Drawing_Mode
    self.obj21.Drawing_Mode.setValue((' ', 0))
    self.obj21.Drawing_Mode.config = 0

    # Contents
    self.obj21.Contents.Text.setValue('Edit')
    self.obj21.Contents.Image.setValue('')
    self.obj21.Contents.Image.setNone()
    self.obj21.Contents.lastSelected= "Text"

    self.obj21.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(10,10,self.obj21)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj21.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj21)
    self.globalAndLocalPostcondition(self.obj21, rootNode)
    self.obj21.postAction( rootNode.CREATE )

    self.obj22=ButtonConfig(self)
    self.obj22.isGraphObjectVisual = True

    if(hasattr(self.obj22, '_setHierarchicalLink')):
      self.obj22._setHierarchicalLink(False)

    # Action
    self.obj22.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nfrom HelpDialog import HelpDialog\nHelpDialog(["LSMASOMM_METAHelp.txt"])\n '))

    # Drawing_Mode
    self.obj22.Drawing_Mode.setValue((' ', 0))
    self.obj22.Drawing_Mode.config = 0

    # Contents
    self.obj22.Contents.Text.setValue('Help')
    self.obj22.Contents.Image.setValue('')
    self.obj22.Contents.Image.setNone()
    self.obj22.Contents.lastSelected= "Text"

    self.obj22.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,80,self.obj22)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj22.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj22)
    self.globalAndLocalPostcondition(self.obj22, rootNode)
    self.obj22.postAction( rootNode.CREATE )

    self.obj23=ButtonConfig(self)
    self.obj23.isGraphObjectVisual = True

    if(hasattr(self.obj23, '_setHierarchicalLink')):
      self.obj23._setHierarchicalLink(False)

    # Action
    self.obj23.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOrgUnit (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj23.Drawing_Mode.setValue((' ', 1))
    self.obj23.Drawing_Mode.config = 0

    # Contents
    self.obj23.Contents.Text.setValue('New OrgUnit')
    self.obj23.Contents.Image.setValue('')
    self.obj23.Contents.Image.setNone()
    self.obj23.Contents.lastSelected= "Text"

    self.obj23.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(260,150,self.obj23)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj23.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj23)
    self.globalAndLocalPostcondition(self.obj23, rootNode)
    self.obj23.postAction( rootNode.CREATE )

    self.obj24=ButtonConfig(self)
    self.obj24.isGraphObjectVisual = True

    if(hasattr(self.obj24, '_setHierarchicalLink')):
      self.obj24._setHierarchicalLink(False)

    # Action
    self.obj24.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewRole (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj24.Drawing_Mode.setValue((' ', 1))
    self.obj24.Drawing_Mode.config = 0

    # Contents
    self.obj24.Contents.Text.setValue('New Role')
    self.obj24.Contents.Image.setValue('')
    self.obj24.Contents.Image.setNone()
    self.obj24.Contents.lastSelected= "Text"

    self.obj24.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(10,10,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj24.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)
    self.obj24.postAction( rootNode.CREATE )

    self.obj25=ButtonConfig(self)
    self.obj25.isGraphObjectVisual = True

    if(hasattr(self.obj25, '_setHierarchicalLink')):
      self.obj25._setHierarchicalLink(False)

    # Action
    self.obj25.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAction (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj25.Drawing_Mode.setValue((' ', 1))
    self.obj25.Drawing_Mode.config = 0

    # Contents
    self.obj25.Contents.Text.setValue('New Action')
    self.obj25.Contents.Image.setValue('')
    self.obj25.Contents.Image.setNone()
    self.obj25.Contents.lastSelected= "Text"

    self.obj25.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,80,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj25.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)
    self.obj25.postAction( rootNode.CREATE )

    self.obj26=ButtonConfig(self)
    self.obj26.isGraphObjectVisual = True

    if(hasattr(self.obj26, '_setHierarchicalLink')):
      self.obj26._setHierarchicalLink(False)

    # Action
    self.obj26.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewKnowledgeArtifacts (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj26.Drawing_Mode.setValue((' ', 1))
    self.obj26.Drawing_Mode.config = 0

    # Contents
    self.obj26.Contents.Text.setValue('New KnowledgeArtifacts')
    self.obj26.Contents.Image.setValue('')
    self.obj26.Contents.Image.setNone()
    self.obj26.Contents.lastSelected= "Text"

    self.obj26.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(260,150,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj26.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)
    self.obj26.postAction( rootNode.CREATE )

    self.obj27=ButtonConfig(self)
    self.obj27.isGraphObjectVisual = True

    if(hasattr(self.obj27, '_setHierarchicalLink')):
      self.obj27._setHierarchicalLink(False)

    # Action
    self.obj27.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOrganisationalKnArt (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj27.Drawing_Mode.setValue((' ', 1))
    self.obj27.Drawing_Mode.config = 0

    # Contents
    self.obj27.Contents.Text.setValue('New OrganisationalKnArt')
    self.obj27.Contents.Image.setValue('')
    self.obj27.Contents.Image.setNone()
    self.obj27.Contents.lastSelected= "Text"

    self.obj27.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(10,10,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj27.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)
    self.obj27.postAction( rootNode.CREATE )

    self.obj28=ButtonConfig(self)
    self.obj28.isGraphObjectVisual = True

    if(hasattr(self.obj28, '_setHierarchicalLink')):
      self.obj28._setHierarchicalLink(False)

    # Action
    self.obj28.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewIndividualKnArt (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj28.Drawing_Mode.setValue((' ', 1))
    self.obj28.Drawing_Mode.config = 0

    # Contents
    self.obj28.Contents.Text.setValue('New IndividualKnArt')
    self.obj28.Contents.Image.setValue('')
    self.obj28.Contents.Image.setNone()
    self.obj28.Contents.lastSelected= "Text"

    self.obj28.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,80,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj28.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)
    self.obj28.postAction( rootNode.CREATE )

    self.obj29=ButtonConfig(self)
    self.obj29.isGraphObjectVisual = True

    if(hasattr(self.obj29, '_setHierarchicalLink')):
      self.obj29._setHierarchicalLink(False)

    # Action
    self.obj29.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewStrategy (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj29.Drawing_Mode.setValue((' ', 1))
    self.obj29.Drawing_Mode.config = 0

    # Contents
    self.obj29.Contents.Text.setValue('New Strategy')
    self.obj29.Contents.Image.setValue('')
    self.obj29.Contents.Image.setNone()
    self.obj29.Contents.lastSelected= "Text"

    self.obj29.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(260,150,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj29.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.obj29.postAction( rootNode.CREATE )

    self.obj30=ButtonConfig(self)
    self.obj30.isGraphObjectVisual = True

    if(hasattr(self.obj30, '_setHierarchicalLink')):
      self.obj30._setHierarchicalLink(False)

    # Action
    self.obj30.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewObjective (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj30.Drawing_Mode.setValue((' ', 1))
    self.obj30.Drawing_Mode.config = 0

    # Contents
    self.obj30.Contents.Text.setValue('New Objective')
    self.obj30.Contents.Image.setValue('')
    self.obj30.Contents.Image.setNone()
    self.obj30.Contents.lastSelected= "Text"

    self.obj30.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(10,10,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj30.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)
    self.obj30.postAction( rootNode.CREATE )

    self.obj31=ButtonConfig(self)
    self.obj31.isGraphObjectVisual = True

    if(hasattr(self.obj31, '_setHierarchicalLink')):
      self.obj31._setHierarchicalLink(False)

    # Action
    self.obj31.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewProcess (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj31.Drawing_Mode.setValue((' ', 1))
    self.obj31.Drawing_Mode.config = 0

    # Contents
    self.obj31.Contents.Text.setValue('New Process')
    self.obj31.Contents.Image.setValue('')
    self.obj31.Contents.Image.setNone()
    self.obj31.Contents.lastSelected= "Text"

    self.obj31.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,80,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj31.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)
    self.obj31.postAction( rootNode.CREATE )

    self.obj32=ButtonConfig(self)
    self.obj32.isGraphObjectVisual = True

    if(hasattr(self.obj32, '_setHierarchicalLink')):
      self.obj32._setHierarchicalLink(False)

    # Action
    self.obj32.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewisPartOfOrgUnit (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj32.Drawing_Mode.setValue((' ', 1))
    self.obj32.Drawing_Mode.config = 0

    # Contents
    self.obj32.Contents.Text.setValue('New isPartOfOrgUnit')
    self.obj32.Contents.Image.setValue('')
    self.obj32.Contents.Image.setNone()
    self.obj32.Contents.lastSelected= "Text"

    self.obj32.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(260,150,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj32.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.obj32.postAction( rootNode.CREATE )

    self.obj33=ButtonConfig(self)
    self.obj33.isGraphObjectVisual = True

    if(hasattr(self.obj33, '_setHierarchicalLink')):
      self.obj33._setHierarchicalLink(False)

    # Action
    self.obj33.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewcanHaveRole (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj33.Drawing_Mode.setValue((' ', 1))
    self.obj33.Drawing_Mode.config = 0

    # Contents
    self.obj33.Contents.Text.setValue('New canHaveRole')
    self.obj33.Contents.Image.setValue('')
    self.obj33.Contents.Image.setNone()
    self.obj33.Contents.lastSelected= "Text"

    self.obj33.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(10,10,self.obj33)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj33.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj33)
    self.globalAndLocalPostcondition(self.obj33, rootNode)
    self.obj33.postAction( rootNode.CREATE )

    self.obj34=ButtonConfig(self)
    self.obj34.isGraphObjectVisual = True

    if(hasattr(self.obj34, '_setHierarchicalLink')):
      self.obj34._setHierarchicalLink(False)

    # Action
    self.obj34.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewhasActions (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj34.Drawing_Mode.setValue((' ', 1))
    self.obj34.Drawing_Mode.config = 0

    # Contents
    self.obj34.Contents.Text.setValue('New hasActions')
    self.obj34.Contents.Image.setValue('')
    self.obj34.Contents.Image.setNone()
    self.obj34.Contents.lastSelected= "Text"

    self.obj34.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,80,self.obj34)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj34.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj34)
    self.globalAndLocalPostcondition(self.obj34, rootNode)
    self.obj34.postAction( rootNode.CREATE )

    self.obj35=ButtonConfig(self)
    self.obj35.isGraphObjectVisual = True

    if(hasattr(self.obj35, '_setHierarchicalLink')):
      self.obj35._setHierarchicalLink(False)

    # Action
    self.obj35.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewcanAccessKnArt (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj35.Drawing_Mode.setValue((' ', 1))
    self.obj35.Drawing_Mode.config = 0

    # Contents
    self.obj35.Contents.Text.setValue('New canAccessKnArt')
    self.obj35.Contents.Image.setValue('')
    self.obj35.Contents.Image.setNone()
    self.obj35.Contents.lastSelected= "Text"

    self.obj35.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(260,150,self.obj35)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj35.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj35)
    self.globalAndLocalPostcondition(self.obj35, rootNode)
    self.obj35.postAction( rootNode.CREATE )

    self.obj36=ButtonConfig(self)
    self.obj36.isGraphObjectVisual = True

    if(hasattr(self.obj36, '_setHierarchicalLink')):
      self.obj36._setHierarchicalLink(False)

    # Action
    self.obj36.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewisPartOfObjective (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj36.Drawing_Mode.setValue((' ', 1))
    self.obj36.Drawing_Mode.config = 0

    # Contents
    self.obj36.Contents.Text.setValue('New isPartOfObjective')
    self.obj36.Contents.Image.setValue('')
    self.obj36.Contents.Image.setNone()
    self.obj36.Contents.lastSelected= "Text"

    self.obj36.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(10,10,self.obj36)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj36.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj36)
    self.globalAndLocalPostcondition(self.obj36, rootNode)
    self.obj36.postAction( rootNode.CREATE )

    self.obj37=ButtonConfig(self)
    self.obj37.isGraphObjectVisual = True

    if(hasattr(self.obj37, '_setHierarchicalLink')):
      self.obj37._setHierarchicalLink(False)

    # Action
    self.obj37.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewhasObjective (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj37.Drawing_Mode.setValue((' ', 1))
    self.obj37.Drawing_Mode.config = 0

    # Contents
    self.obj37.Contents.Text.setValue('New hasObjective')
    self.obj37.Contents.Image.setValue('')
    self.obj37.Contents.Image.setNone()
    self.obj37.Contents.lastSelected= "Text"

    self.obj37.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,80,self.obj37)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj37.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj37)
    self.globalAndLocalPostcondition(self.obj37, rootNode)
    self.obj37.postAction( rootNode.CREATE )

    self.obj38=ButtonConfig(self)
    self.obj38.isGraphObjectVisual = True

    if(hasattr(self.obj38, '_setHierarchicalLink')):
      self.obj38._setHierarchicalLink(False)

    # Action
    self.obj38.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewgenericAssociation (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj38.Drawing_Mode.setValue((' ', 1))
    self.obj38.Drawing_Mode.config = 0

    # Contents
    self.obj38.Contents.Text.setValue('New genericAssociation')
    self.obj38.Contents.Image.setValue('')
    self.obj38.Contents.Image.setNone()
    self.obj38.Contents.lastSelected= "Text"

    self.obj38.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(260,150,self.obj38)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj38.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj38)
    self.globalAndLocalPostcondition(self.obj38, rootNode)
    self.obj38.postAction( rootNode.CREATE )

    self.obj39=ButtonConfig(self)
    self.obj39.isGraphObjectVisual = True

    if(hasattr(self.obj39, '_setHierarchicalLink')):
      self.obj39._setHierarchicalLink(False)

    # Action
    self.obj39.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewanswersToRole (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj39.Drawing_Mode.setValue((' ', 1))
    self.obj39.Drawing_Mode.config = 0

    # Contents
    self.obj39.Contents.Text.setValue('New answersToRole')
    self.obj39.Contents.Image.setValue('')
    self.obj39.Contents.Image.setNone()
    self.obj39.Contents.lastSelected= "Text"

    self.obj39.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(10,10,self.obj39)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj39.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj39)
    self.globalAndLocalPostcondition(self.obj39, rootNode)
    self.obj39.postAction( rootNode.CREATE )

    self.obj40=ButtonConfig(self)
    self.obj40.isGraphObjectVisual = True

    if(hasattr(self.obj40, '_setHierarchicalLink')):
      self.obj40._setHierarchicalLink(False)

    # Action
    self.obj40.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewcanStartProcess (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj40.Drawing_Mode.setValue((' ', 1))
    self.obj40.Drawing_Mode.config = 0

    # Contents
    self.obj40.Contents.Text.setValue('New canStartProcess')
    self.obj40.Contents.Image.setValue('')
    self.obj40.Contents.Image.setNone()
    self.obj40.Contents.lastSelected= "Text"

    self.obj40.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(135,80,self.obj40)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj40.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj40)
    self.globalAndLocalPostcondition(self.obj40, rootNode)
    self.obj40.postAction( rootNode.CREATE )

    self.obj41=ButtonConfig(self)
    self.obj41.isGraphObjectVisual = True

    if(hasattr(self.obj41, '_setHierarchicalLink')):
      self.obj41._setHierarchicalLink(False)

    # Action
    self.obj41.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewanswersToOrgUnit (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj41.Drawing_Mode.setValue((' ', 1))
    self.obj41.Drawing_Mode.config = 0

    # Contents
    self.obj41.Contents.Text.setValue('New answersToOrgUnit')
    self.obj41.Contents.Image.setValue('')
    self.obj41.Contents.Image.setNone()
    self.obj41.Contents.lastSelected= "Text"

    self.obj41.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(260,150,self.obj41)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj41.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj41)
    self.globalAndLocalPostcondition(self.obj41, rootNode)
    self.obj41.postAction( rootNode.CREATE )

    self.obj42=ButtonConfig(self)
    self.obj42.isGraphObjectVisual = True

    if(hasattr(self.obj42, '_setHierarchicalLink')):
      self.obj42._setHierarchicalLink(False)

    # Action
    self.obj42.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewisPartOfRole (self, wherex, wherey)\n'))

    # Drawing_Mode
    self.obj42.Drawing_Mode.setValue((' ', 1))
    self.obj42.Drawing_Mode.config = 0

    # Contents
    self.obj42.Contents.Text.setValue('New isPartOfRole')
    self.obj42.Contents.Image.setValue('')
    self.obj42.Contents.Image.setNone()
    self.obj42.Contents.lastSelected= "Text"

    self.obj42.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(10,10,self.obj42)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj42.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj42)
    self.globalAndLocalPostcondition(self.obj42, rootNode)
    self.obj42.postAction( rootNode.CREATE )

    self.obj43=ButtonConfig(self)
    self.obj43.isGraphObjectVisual = True

    if(hasattr(self.obj43, '_setHierarchicalLink')):
      self.obj43._setHierarchicalLink(False)

    # Action
    self.obj43.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\nfrom CustomCode import *\nRoleInheritanceAllRoles(self)\nprintAllNodeNames(self)\nprintSpecificNodeClassNames(self, \'OrgUnit\')\nprintSpecificNodeClassNames(self, \'Role\')\n\n'))

    # Drawing_Mode
    self.obj43.Drawing_Mode.setValue((' ', 0))
    self.obj43.Drawing_Mode.config = 0

    # Contents
    self.obj43.Contents.Text.setValue('Generate')
    self.obj43.Contents.Image.setValue('')
    self.obj43.Contents.Image.setNone()
    self.obj43.Contents.lastSelected= "Text"

    self.obj43.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(60.0,220.0,self.obj43)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj43.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj43)
    self.globalAndLocalPostcondition(self.obj43, rootNode)
    self.obj43.postAction( rootNode.CREATE )

    self.obj44=ButtonConfig(self)
    self.obj44.isGraphObjectVisual = True

    if(hasattr(self.obj44, '_setHierarchicalLink')):
      self.obj44._setHierarchicalLink(False)

    # Action
    self.obj44.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\nfrom CustomCode import *\nSaveAll(self)\n\n'))

    # Drawing_Mode
    self.obj44.Drawing_Mode.setValue((' ', 0))
    self.obj44.Drawing_Mode.config = 0

    # Contents
    self.obj44.Contents.Text.setValue('Save All')
    self.obj44.Contents.Image.setValue('')
    self.obj44.Contents.Image.setNone()
    self.obj44.Contents.lastSelected= "Text"

    self.obj44.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       new_obj = graph_ButtonConfig(180.0,220.0,self.obj44)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.0]
    else: new_obj = None
    self.obj44.graphObject_ = new_obj

    # Add node to the root: rootNode
    rootNode.addNode(self.obj44)
    self.globalAndLocalPostcondition(self.obj44, rootNode)
    self.obj44.postAction( rootNode.CREATE )

    # Connections for obj21 (graphObject_: Obj0) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj22 (graphObject_: Obj1) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj23 (graphObject_: Obj2) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj24 (graphObject_: Obj3) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj25 (graphObject_: Obj4) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj26 (graphObject_: Obj5) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj27 (graphObject_: Obj6) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj28 (graphObject_: Obj7) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj29 (graphObject_: Obj8) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj30 (graphObject_: Obj9) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj31 (graphObject_: Obj10) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj32 (graphObject_: Obj11) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj33 (graphObject_: Obj12) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj34 (graphObject_: Obj13) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj35 (graphObject_: Obj14) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj36 (graphObject_: Obj15) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj37 (graphObject_: Obj16) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj38 (graphObject_: Obj17) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj39 (graphObject_: Obj18) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj40 (graphObject_: Obj19) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj41 (graphObject_: Obj20) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj42 (graphObject_: Obj21) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj43 (graphObject_: Obj22) of type ButtonConfig
    self.drawConnections(
 )
    # Connections for obj44 (graphObject_: Obj23) of type ButtonConfig
    self.drawConnections(
 )

newfunction = LSMASOMM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
