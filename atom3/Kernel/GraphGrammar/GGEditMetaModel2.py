from ASG_GGEditMetaModel2 import *
from graph_ASG_UMLmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from ATOM3TypeDialog import *

from GraphGrammarEdit       import *
# Some constants for defining operation modes
NEWGraphGrammarEdit = "NEWGraphGrammarEdit"
def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu = Menu(self.mmtoolMenu, tearoff=0)
    modelMenu.add_command(label="new GraphGrammarEdit", command=lambda x=self: x.newModesGraphGrammarEdit(x) )
def addButtons(self, createNewASGroot = 0):
    mmToolBar = Frame(self.toolBar, relief = RAISED)
    b = Label(mmToolBar, text = "GGEditMetaModel2", font = ("Helvetica",8), relief = GROOVE)
    b.pack(side = TOP, fill = X, ipady = 5)
    self.openMetaModels.newItem(ATOM3String("GGEditMetaModel2"))
    newGraphGrammarEdit=Button(mmToolBar, text="new GraphGrammarEdit", command=lambda x=self: x.newModeGraphGrammarEdit(x) )
    newGraphGrammarEdit.pack(side=LEFT, padx=2, pady=2)

    if createNewASGroot:
       self.ASGroot = ASG_GGEditMetaModel2(self)
    self.buttonList.append((mmToolBar, "GGEditMetaModel2"))
    return mmToolBar
def configureUserActions(self):
    self.userActionsMap[self.IDLEMODE] = self.drag
    self.userActionsMap[self.CONNECTstate] = self.connectClass
    self.userActionsMap[self.INSERTModel] = self.createNew_Model
    self.userActionsMap[self.EXPANDModel] = self.expandModel
    self.userActionsMap[self.NEWGraphGrammarEdit] = self.createNewGraphGrammarEdit
    self.userActionsMap[self.EDITstate]   = self.editEntity
    self.userActionsMap[self.DELETEstate] = self.deleteEntity
def newModeGraphGrammarEdit(self):
   self.mode = self.NEWGraphGrammarEdit

def createNewGraphGrammarEdit(self, wherex, wherey):
   new_semantic_obj = GraphGrammarEdit(self)
   ne = len(self.ASGroot.listNodes["GraphGrammarEdit"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   new_obj = graph_GraphGrammarEdit(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel)
   self.UMLmodel.addtag_withtag("GraphGrammarEdit", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   self.mode=self.IDLEMODE
def createNew_Model(self, wherex, wherey):
   new_semantic_obj = ASG_GGEditMetaModel2(self)
   ne = len(self.ASGroot.listNodes["ASG_GGEditMetaModel2"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   new_obj = graph_ASG_UMLmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel)
   self.UMLmodel.addtag_withtag("ASG_GGEditMetaModel2", new_obj.tag)
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

