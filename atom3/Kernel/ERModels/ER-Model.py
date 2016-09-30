from ASG_ER-Model import *
from graph_ASG_UMLmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from ATOM3TypeDialog import *

from DFAState       import *
from graph_DFAState import *
from DFATransition       import *
from graph_DFATransition import *
# Some constants for defining operation modes
NEWDFAState = "NEWDFAState"
NEWDFATransition = "NEWDFATransition"
def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu = Menu(self.mmtoolMenu, tearoff=0)
    modelMenu.add_command(label="new DFAState", command=lambda x=self: x.newModesDFAState(x) )
    modelMenu.add_command(label="new DFATransition", command=lambda x=self: x.newModesDFATransition(x) )
def addButtons(self, createNewASGroot = 0):
    mmToolBar = Frame(self.toolBar, relief = RAISED)
    b = Label(mmToolBar, text = "ER-Model", font = ("Helvetica",8), relief = GROOVE)
    b.pack(side = TOP, fill = X, ipady = 5)
    self.openMetaModels.newItem(ATOM3String("ER-Model"))
    newDFAState=Button(mmToolBar, text="new DFAState", command=lambda x=self: x.newModeDFAState(x) )
    newDFAState.pack(side=LEFT, padx=2, pady=2)

    newDFATransition=Button(mmToolBar, text="new DFATransition", command=lambda x=self: x.newModeDFATransition(x) )
    newDFATransition.pack(side=LEFT, padx=2, pady=2)

    if createNewASGroot:
       self.ASGroot = ASG_ER-Model(self)
    self.buttonList.append((mmToolBar, "ER-Model"))
    return mmToolBar
def configureUserActions(self):
    self.userActionsMap[self.IDLEMODE] = self.drag
    self.userActionsMap[self.CONNECTstate] = self.connectClass
    self.userActionsMap[self.INSERTModel] = self.createNew_Model
    self.userActionsMap[self.EXPANDModel] = self.expandModel
    self.userActionsMap[self.NEWDFAState] = self.createNewDFAState
    self.userActionsMap[self.NEWDFATransition] = self.createNewDFATransition
    self.userActionsMap[self.EDITstate]   = self.editEntity
    self.userActionsMap[self.DELETEstate] = self.deleteEntity
def newModeDFAState(self):
   self.mode = self.NEWDFAState

def newModeDFATransition(self):
   self.mode = self.NEWDFATransition

def createNewDFAState(self, wherex, wherey):
   new_semantic_obj = DFAState(self)
   ne = len(self.ASGroot.listNodes["DFAState"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   new_obj = graph_DFAState(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel)
   self.UMLmodel.addtag_withtag("DFAState", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   self.mode=self.IDLEMODE
def createNewDFATransition(self, wherex, wherey):
   new_semantic_obj = DFATransition(self)
   ne = len(self.ASGroot.listNodes["DFATransition"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   new_obj = graph_DFATransition(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel)
   self.UMLmodel.addtag_withtag("DFATransition", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   self.mode=self.IDLEMODE
def createNew_Model(self, wherex, wherey):
   new_semantic_obj = ASG_ER-Model(self)
   ne = len(self.ASGroot.listNodes["ASG_ER-Model"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   new_obj = graph_ASG_UMLmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel)
   self.UMLmodel.addtag_withtag("ASG_ER-Model", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   self.mode=self.IDLEMODE
def fillTypesInformation(self):
    objs = []
    obj = ATOM3TypeInfo()
    params  = []
    obj.setValue(("String", "ATOM3String", params ))
    objs.append(obj)
    obj = ATOM3TypeInfo()
    params  = []
    obj.setValue(("Integer", "ATOM3Integer", params ))
    objs.append(obj)
    obj = ATOM3TypeInfo()
    params  = []
    obj.setValue(("Float", "ATOM3Float", params ))
    objs.append(obj)
    obj = ATOM3TypeInfo()
    params  = []
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("Attribute", "ATOM3Attribute", params ))
    objs.append(obj)
    obj = ATOM3TypeInfo()
    params  = []
    param = ATOM3String("[1,1,1,self.types]")
    params.append(param)
    param = ATOM3String("ATOM3Attribute")
    params.append(param)
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("List", "ATOM3List", params ))
    objs.append(obj)
    obj = ATOM3TypeInfo()
    params  = []
    param = ATOM3String("[]")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Enum", "ATOM3Enum", params ))
    objs.append(obj)
    obj = ATOM3TypeInfo()
    params  = []
    obj.setValue(("Constraint", "ATOM3Constraint", params ))
    objs.append(obj)
    obj = ATOM3TypeInfo()
    params  = []
    param = ATOM3String("'class0'")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    obj.setValue(("Appearance", "ATOM3Appearance", params ))
    objs.append(obj)
    obj = ATOM3TypeInfo()
    params  = []
    obj.setValue(("BottomType", "ATOM3BottomType", params ))
    objs.append(obj)
    self.typeList.setValue(objs)

