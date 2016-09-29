"""
__LSMASOMM_META.py_____________________________________________________

Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)
Author: bogdan
Modified: Sat Jul  9 19:13:25 2016
______________________________________________________________________
"""
from ASG_Buttons import *
from ButtonConfig import *
from ATOM3Enum import *
from ATOM3List import *
from ATOM3Float import *
from ATOM3Integer import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3Action import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Link import *
def LSMASOMM_META(self, rootNode, ButtonsRootNode):
   ButtonsRootNode.Formalism_Name.setValue('LSMASOMM_META')
   ButtonsRootNode.RowSize.setValue(4)
   ButtonsRootNode.Formalism_File.setValue( 'LSMASOMM_MM.py' )


   self.globalPrecondition(rootNode)

   self.objEdit=ButtonConfig(self)
   self.objEdit.Contents.Text.setValue('Edit')
   self.objEdit.Contents.Image.setValue('')
   self.objEdit.Contents.lastSelected= 'Text'
   self.objEdit.Drawing_Mode.setValue(0)
   self.objEdit.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nself.modelAttributes(self.ASGroot.getASGbyName("LSMASOMM_META")) ') )
   self.objEdit.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objEdit)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objEdit.graphObject_ = new_obj
   rootNode.addNode(self.objEdit)
   self.globalAndLocalPostcondition(self.objEdit, rootNode)



   self.globalPrecondition(rootNode)

   self.objHelp=ButtonConfig(self)
   self.objHelp.Contents.Text.setValue('Help')
   self.objHelp.Contents.Image.setValue('')
   self.objHelp.Contents.lastSelected= 'Text'
   self.objHelp.Drawing_Mode.setValue(0)
   self.objHelp.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nfrom HelpDialog import HelpDialog\nHelpDialog(["LSMASOMM_METAHelp.txt"])\n ') )
   self.objHelp.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objHelp)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objHelp.graphObject_ = new_obj
   rootNode.addNode(self.objHelp)
   self.globalAndLocalPostcondition(self.objHelp, rootNode)

   self.globalPrecondition(rootNode)

   self.objOrgUnit=ButtonConfig(self)
   self.objOrgUnit.Contents.Text.setValue('New OrgUnit')
   self.objOrgUnit.Contents.Image.setValue('')
   self.objOrgUnit.Contents.lastSelected= 'Text'
   self.objOrgUnit.Drawing_Mode.setValue(1)
   self.objOrgUnit.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOrgUnit (self, wherex, wherey)\n'))
   self.objOrgUnit.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objOrgUnit)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objOrgUnit.graphObject_ = new_obj
   rootNode.addNode(self.objOrgUnit)
   self.globalAndLocalPostcondition(self.objOrgUnit, rootNode)
   self.globalPrecondition(rootNode)

   self.objRole=ButtonConfig(self)
   self.objRole.Contents.Text.setValue('New Role')
   self.objRole.Contents.Image.setValue('')
   self.objRole.Contents.lastSelected= 'Text'
   self.objRole.Drawing_Mode.setValue(1)
   self.objRole.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewRole (self, wherex, wherey)\n'))
   self.objRole.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objRole)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objRole.graphObject_ = new_obj
   rootNode.addNode(self.objRole)
   self.globalAndLocalPostcondition(self.objRole, rootNode)
   self.globalPrecondition(rootNode)

   self.objAction=ButtonConfig(self)
   self.objAction.Contents.Text.setValue('New Action')
   self.objAction.Contents.Image.setValue('')
   self.objAction.Contents.lastSelected= 'Text'
   self.objAction.Drawing_Mode.setValue(1)
   self.objAction.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAction (self, wherex, wherey)\n'))
   self.objAction.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objAction)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objAction.graphObject_ = new_obj
   rootNode.addNode(self.objAction)
   self.globalAndLocalPostcondition(self.objAction, rootNode)
   self.globalPrecondition(rootNode)

   self.objKnowledgeArtifacts=ButtonConfig(self)
   self.objKnowledgeArtifacts.Contents.Text.setValue('New KnowledgeArtifacts')
   self.objKnowledgeArtifacts.Contents.Image.setValue('')
   self.objKnowledgeArtifacts.Contents.lastSelected= 'Text'
   self.objKnowledgeArtifacts.Drawing_Mode.setValue(1)
   self.objKnowledgeArtifacts.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewKnowledgeArtifacts (self, wherex, wherey)\n'))
   self.objKnowledgeArtifacts.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objKnowledgeArtifacts)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objKnowledgeArtifacts.graphObject_ = new_obj
   rootNode.addNode(self.objKnowledgeArtifacts)
   self.globalAndLocalPostcondition(self.objKnowledgeArtifacts, rootNode)
   self.globalPrecondition(rootNode)

   self.objOrganisationalKnArt=ButtonConfig(self)
   self.objOrganisationalKnArt.Contents.Text.setValue('New OrganisationalKnArt')
   self.objOrganisationalKnArt.Contents.Image.setValue('')
   self.objOrganisationalKnArt.Contents.lastSelected= 'Text'
   self.objOrganisationalKnArt.Drawing_Mode.setValue(1)
   self.objOrganisationalKnArt.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewOrganisationalKnArt (self, wherex, wherey)\n'))
   self.objOrganisationalKnArt.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objOrganisationalKnArt)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objOrganisationalKnArt.graphObject_ = new_obj
   rootNode.addNode(self.objOrganisationalKnArt)
   self.globalAndLocalPostcondition(self.objOrganisationalKnArt, rootNode)
   self.globalPrecondition(rootNode)

   self.objIndividualKnArt=ButtonConfig(self)
   self.objIndividualKnArt.Contents.Text.setValue('New IndividualKnArt')
   self.objIndividualKnArt.Contents.Image.setValue('')
   self.objIndividualKnArt.Contents.lastSelected= 'Text'
   self.objIndividualKnArt.Drawing_Mode.setValue(1)
   self.objIndividualKnArt.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewIndividualKnArt (self, wherex, wherey)\n'))
   self.objIndividualKnArt.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objIndividualKnArt)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objIndividualKnArt.graphObject_ = new_obj
   rootNode.addNode(self.objIndividualKnArt)
   self.globalAndLocalPostcondition(self.objIndividualKnArt, rootNode)
   self.globalPrecondition(rootNode)

   self.objStrategy=ButtonConfig(self)
   self.objStrategy.Contents.Text.setValue('New Strategy')
   self.objStrategy.Contents.Image.setValue('')
   self.objStrategy.Contents.lastSelected= 'Text'
   self.objStrategy.Drawing_Mode.setValue(1)
   self.objStrategy.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewStrategy (self, wherex, wherey)\n'))
   self.objStrategy.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objStrategy)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objStrategy.graphObject_ = new_obj
   rootNode.addNode(self.objStrategy)
   self.globalAndLocalPostcondition(self.objStrategy, rootNode)
   self.globalPrecondition(rootNode)

   self.objObjective=ButtonConfig(self)
   self.objObjective.Contents.Text.setValue('New Objective')
   self.objObjective.Contents.Image.setValue('')
   self.objObjective.Contents.lastSelected= 'Text'
   self.objObjective.Drawing_Mode.setValue(1)
   self.objObjective.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewObjective (self, wherex, wherey)\n'))
   self.objObjective.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objObjective)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objObjective.graphObject_ = new_obj
   rootNode.addNode(self.objObjective)
   self.globalAndLocalPostcondition(self.objObjective, rootNode)
   self.globalPrecondition(rootNode)

   self.objProcess=ButtonConfig(self)
   self.objProcess.Contents.Text.setValue('New Process')
   self.objProcess.Contents.Image.setValue('')
   self.objProcess.Contents.lastSelected= 'Text'
   self.objProcess.Drawing_Mode.setValue(1)
   self.objProcess.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewProcess (self, wherex, wherey)\n'))
   self.objProcess.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objProcess)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objProcess.graphObject_ = new_obj
   rootNode.addNode(self.objProcess)
   self.globalAndLocalPostcondition(self.objProcess, rootNode)
   self.globalPrecondition(rootNode)

   self.objisPartOfOrgUnit=ButtonConfig(self)
   self.objisPartOfOrgUnit.Contents.Text.setValue('New isPartOfOrgUnit')
   self.objisPartOfOrgUnit.Contents.Image.setValue('')
   self.objisPartOfOrgUnit.Contents.lastSelected= 'Text'
   self.objisPartOfOrgUnit.Drawing_Mode.setValue(1)
   self.objisPartOfOrgUnit.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewisPartOfOrgUnit (self, wherex, wherey)\n'))
   self.objisPartOfOrgUnit.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objisPartOfOrgUnit)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objisPartOfOrgUnit.graphObject_ = new_obj
   rootNode.addNode(self.objisPartOfOrgUnit)
   self.globalAndLocalPostcondition(self.objisPartOfOrgUnit, rootNode)
   self.globalPrecondition(rootNode)

   self.objcanHaveRole=ButtonConfig(self)
   self.objcanHaveRole.Contents.Text.setValue('New canHaveRole')
   self.objcanHaveRole.Contents.Image.setValue('')
   self.objcanHaveRole.Contents.lastSelected= 'Text'
   self.objcanHaveRole.Drawing_Mode.setValue(1)
   self.objcanHaveRole.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewcanHaveRole (self, wherex, wherey)\n'))
   self.objcanHaveRole.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objcanHaveRole)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objcanHaveRole.graphObject_ = new_obj
   rootNode.addNode(self.objcanHaveRole)
   self.globalAndLocalPostcondition(self.objcanHaveRole, rootNode)
   self.globalPrecondition(rootNode)

   self.objhasActions=ButtonConfig(self)
   self.objhasActions.Contents.Text.setValue('New hasActions')
   self.objhasActions.Contents.Image.setValue('')
   self.objhasActions.Contents.lastSelected= 'Text'
   self.objhasActions.Drawing_Mode.setValue(1)
   self.objhasActions.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewhasActions (self, wherex, wherey)\n'))
   self.objhasActions.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objhasActions)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objhasActions.graphObject_ = new_obj
   rootNode.addNode(self.objhasActions)
   self.globalAndLocalPostcondition(self.objhasActions, rootNode)
   self.globalPrecondition(rootNode)

   self.objcanAccessKnArt=ButtonConfig(self)
   self.objcanAccessKnArt.Contents.Text.setValue('New canAccessKnArt')
   self.objcanAccessKnArt.Contents.Image.setValue('')
   self.objcanAccessKnArt.Contents.lastSelected= 'Text'
   self.objcanAccessKnArt.Drawing_Mode.setValue(1)
   self.objcanAccessKnArt.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewcanAccessKnArt (self, wherex, wherey)\n'))
   self.objcanAccessKnArt.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objcanAccessKnArt)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objcanAccessKnArt.graphObject_ = new_obj
   rootNode.addNode(self.objcanAccessKnArt)
   self.globalAndLocalPostcondition(self.objcanAccessKnArt, rootNode)
   self.globalPrecondition(rootNode)

   self.objisPartOfObjective=ButtonConfig(self)
   self.objisPartOfObjective.Contents.Text.setValue('New isPartOfObjective')
   self.objisPartOfObjective.Contents.Image.setValue('')
   self.objisPartOfObjective.Contents.lastSelected= 'Text'
   self.objisPartOfObjective.Drawing_Mode.setValue(1)
   self.objisPartOfObjective.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewisPartOfObjective (self, wherex, wherey)\n'))
   self.objisPartOfObjective.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objisPartOfObjective)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objisPartOfObjective.graphObject_ = new_obj
   rootNode.addNode(self.objisPartOfObjective)
   self.globalAndLocalPostcondition(self.objisPartOfObjective, rootNode)
   self.globalPrecondition(rootNode)

   self.objhasObjective=ButtonConfig(self)
   self.objhasObjective.Contents.Text.setValue('New hasObjective')
   self.objhasObjective.Contents.Image.setValue('')
   self.objhasObjective.Contents.lastSelected= 'Text'
   self.objhasObjective.Drawing_Mode.setValue(1)
   self.objhasObjective.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewhasObjective (self, wherex, wherey)\n'))
   self.objhasObjective.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objhasObjective)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objhasObjective.graphObject_ = new_obj
   rootNode.addNode(self.objhasObjective)
   self.globalAndLocalPostcondition(self.objhasObjective, rootNode)
   self.globalPrecondition(rootNode)

   self.objgenericAssociation=ButtonConfig(self)
   self.objgenericAssociation.Contents.Text.setValue('New genericAssociation')
   self.objgenericAssociation.Contents.Image.setValue('')
   self.objgenericAssociation.Contents.lastSelected= 'Text'
   self.objgenericAssociation.Drawing_Mode.setValue(1)
   self.objgenericAssociation.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewgenericAssociation (self, wherex, wherey)\n'))
   self.objgenericAssociation.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objgenericAssociation)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objgenericAssociation.graphObject_ = new_obj
   rootNode.addNode(self.objgenericAssociation)
   self.globalAndLocalPostcondition(self.objgenericAssociation, rootNode)
   self.globalPrecondition(rootNode)

   self.objanswersToRole=ButtonConfig(self)
   self.objanswersToRole.Contents.Text.setValue('New answersToRole')
   self.objanswersToRole.Contents.Image.setValue('')
   self.objanswersToRole.Contents.lastSelected= 'Text'
   self.objanswersToRole.Drawing_Mode.setValue(1)
   self.objanswersToRole.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewanswersToRole (self, wherex, wherey)\n'))
   self.objanswersToRole.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objanswersToRole)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objanswersToRole.graphObject_ = new_obj
   rootNode.addNode(self.objanswersToRole)
   self.globalAndLocalPostcondition(self.objanswersToRole, rootNode)
   self.globalPrecondition(rootNode)

   self.objcanStartProcess=ButtonConfig(self)
   self.objcanStartProcess.Contents.Text.setValue('New canStartProcess')
   self.objcanStartProcess.Contents.Image.setValue('')
   self.objcanStartProcess.Contents.lastSelected= 'Text'
   self.objcanStartProcess.Drawing_Mode.setValue(1)
   self.objcanStartProcess.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewcanStartProcess (self, wherex, wherey)\n'))
   self.objcanStartProcess.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(135, 80,self.objcanStartProcess)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objcanStartProcess.graphObject_ = new_obj
   rootNode.addNode(self.objcanStartProcess)
   self.globalAndLocalPostcondition(self.objcanStartProcess, rootNode)
   self.globalPrecondition(rootNode)

   self.objanswersToOrgUnit=ButtonConfig(self)
   self.objanswersToOrgUnit.Contents.Text.setValue('New answersToOrgUnit')
   self.objanswersToOrgUnit.Contents.Image.setValue('')
   self.objanswersToOrgUnit.Contents.lastSelected= 'Text'
   self.objanswersToOrgUnit.Drawing_Mode.setValue(1)
   self.objanswersToOrgUnit.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewanswersToOrgUnit (self, wherex, wherey)\n'))
   self.objanswersToOrgUnit.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(260, 150,self.objanswersToOrgUnit)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objanswersToOrgUnit.graphObject_ = new_obj
   rootNode.addNode(self.objanswersToOrgUnit)
   self.globalAndLocalPostcondition(self.objanswersToOrgUnit, rootNode)
   self.globalPrecondition(rootNode)

   self.objisPartOfRole=ButtonConfig(self)
   self.objisPartOfRole.Contents.Text.setValue('New isPartOfRole')
   self.objisPartOfRole.Contents.Image.setValue('')
   self.objisPartOfRole.Contents.lastSelected= 'Text'
   self.objisPartOfRole.Drawing_Mode.setValue(1)
   self.objisPartOfRole.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1),(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewisPartOfRole (self, wherex, wherey)\n'))
   self.objisPartOfRole.graphClass_= graph_ButtonConfig
   if self.genGraphics:
      from graph_ButtonConfig import *
      new_obj = graph_ButtonConfig(10, 10,self.objisPartOfRole)
      new_obj.DrawObject(self.UMLmodel)
      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)
   else: new_obj = None
   self.objisPartOfRole.graphObject_ = new_obj
   rootNode.addNode(self.objisPartOfRole)
   self.globalAndLocalPostcondition(self.objisPartOfRole, rootNode)

newfunction = LSMASOMM_META

loadedMMName = 'Buttons'

atom3version = '0.3'
