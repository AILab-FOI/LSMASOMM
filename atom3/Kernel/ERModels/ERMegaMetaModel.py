from ASG_ERMegaMetaModel import *
from graph_ASG_UMLmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from relationship       import *
# Some constants for defining operation modes
NEWrelationship = "NEWrelationship"
def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu = Menu(self.mmtoolMenu, tearoff=0)
    modelMenu.add_command(label="new relationship", command=lambda x=self: x.newModesrelationship(x) )
def addButtons(self, createNewASGroot = 0):
    mmToolBar = Frame(self.toolBar, relief = RAISED)
    b = Label(mmToolBar, text = "ERMegaMetaModel", font = ("Helvetica",8), relief = GROOVE)
    b.pack(side = TOP, fill = X, ipady = 5)
    self.openMetaModels.newItem(ATOM3String("ERMegaMetaModel"))
    newrelationship=Button(mmToolBar, text="new relationship", command=lambda x=self: x.newModerelationship(x) )
    newrelationship.pack(side=LEFT, padx=2, pady=2)

    if createNewASGroot:
       self.ASGroot = ASG_ERMegaMetaModel(self)
    self.buttonList.append((mmToolBar, "ERMegaMetaModel"))
    return mmToolBar
def configureUserActions(self):
    self.userActionsMap[self.IDLEMODE] = self.drag
    self.userActionsMap[self.CONNECTstate] = self.connectClass
    self.userActionsMap[self.INSERTModel] = self.createNew_Model
    self.userActionsMap[self.EXPANDModel] = self.expandModel
    self.userActionsMap[self.NEWrelationship] = self.createNewrelationship
    self.userActionsMap[self.EDITstate]   = self.editEntity
    self.userActionsMap[self.DELETEstate] = self.deleteEntity
    self.userActionsMap[self.SELECTgraph] = self.selectGraph
def newModerelationship(self):
   self.mode = self.NEWrelationship

def createNewrelationship(self, wherex, wherey):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = relationship(self)
   ne = len(self.ASGroot.listNodes["relationship"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   new_obj = graph_relationship(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("relationship", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
def createNew_Model(self, wherex, wherey):
   self.toClass = None
   self.fromClass = None
   new_semantic_obj = ASG_ERMegaMetaModel(self)
   ne = len(self.ASGroot.listNodes["ASG_ERMegaMetaModel"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   new_obj = graph_ASG_UMLmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_ERMegaMetaModel", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
def fillTypesInformation(self):
    objs = []
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("String", "ATOM3String", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Boolean", "ATOM3Boolean", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Integer", "ATOM3Integer", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Float", "ATOM3Float", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("Attribute", "ATOM3Attribute", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[1,1,1,self.types]")
    params.append(param)
    param = ATOM3String("ATOM3Attribute")
    params.append(param)
    param = ATOM3String("self.types")
    params.append(param)
    obj.setValue(("List", "ATOM3List", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("[]")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    param = ATOM3String("1")
    params.append(param)
    obj.setValue(("Enum", "ATOM3Enum", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Constraint", "ATOM3Constraint", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    param = ATOM3String("'class0'")
    params.append(param)
    param = ATOM3String("None")
    params.append(param)
    obj.setValue(("Appearance", "ATOM3Appearance", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("BottomType", "ATOM3BottomType", params, (None, 0) ))
    objs.append(obj)
    obj = ATOM3TypeInfo(self)
    params  = []
    obj.setValue(("Link", "ATOM3Link", params, (None, 0) ))
    objs.append(obj)
    self.typeList.setValue(objs)

