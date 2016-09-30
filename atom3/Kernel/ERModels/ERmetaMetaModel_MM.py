from ASG_ERmetaMetaModel import *
from Tkinter import *
from ATOM3TypeDialog import *
from ATOM3Attribute    import *
from ATOM3String       import *
from ATOM3Integer      import *
from ATOM3Float        import *
from ATOM3List         import *
from ATOM3Enum         import *
from ATOM3Constraint   import *
from ATOM3Appearance   import *
from ATOM3TypeDialog   import *
from ATOM3TypeInfo     import *

from graph_ERentity import *
from ERentity import *

from graph_ERrelationship import *
from ERrelationship       import *

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu.add_command(label="new Entity", command=lambda x=self: x.newModeERentity(x) )
    modelMenu.add_command(label="new Relationship", command=lambda x=self: x.newModeERrelationship(x) )

def createNewASGroot(self):
    return ASG_ERmetaMetaModel(self, None )

def setConnectivity(self):
    #self.ConnectivityMap = {}
    self.ConnectivityMap['ERentity'] = { 'ERentity': [('ERrelationship', self.createNewERrelationship)],
                                         'ERrelationship': [] }
    self.ConnectivityMap['ERrelationship'] = { 'ERentity': [],
                                               'ERrelationship': [] }
    self.CardinalityTable['ERentity']={
          'ERrelationship': [('0', 'n', 'Source'), ('0', 'n', 'Destination')]
          ,'ERentity': [] }
    self.CardinalityTable['ERrelationship']={
          'ERrelationship': [('0', 'n', 'Source'), ('0', 'n', 'Destination')]
          ,'ERentity': [('1', 'n', 'Destination'), ('1', 'n', 'Source')] }
    self.entitiesInMetaModel['ERmetaMetaModel'] = ['ERentity','ERrelationship']

def newModeERrelationship(self):
    self.mode = self.NEWERrelationship

def newModeERentity(self):
    self.mode = self.NEWERentity

def createNewERentity(self, wherex, wherey, screenCoordinates = 1):
    self.fromClass = None
    self.toClass = None
    new_semantic_obj = ERentity(self)
    if screenCoordinates:
      new_obj = graph_ERentity(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
    else:
      new_obj = graph_ERentity(wherex, wherey, new_semantic_obj)  
    # check for repetitions on keyword...
    ne = len(self.ASGroot.listNodes["ERentity"])
    new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
    new_semantic_obj.appearance.className = new_semantic_obj.keyword_.toString()

    new_obj.DrawObject(self.UMLmodel,self.editGGLabel)
    self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    new_semantic_obj.graphObject_ = new_obj
    self.ASGroot.addNode(new_semantic_obj)
    self.mode=self.IDLEMODE
    # update status bars...
    if self.editGGLabel :
       self.statusbar.event(self.statusbar.TRANSFORMATION, self.statusbar.CREATE)
    else:
       self.statusbar.event(self.statusbar.MODEL, self.statusbar.CREATE)
    return new_semantic_obj

def createNew_Model(self, wherex, wherey, screenCoordinates = 1):
    self.fromClass = None
    self.toClass = None
    new_semantic_obj = ASG_ERmetaMetaModel(self)
    if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
    else:
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)  
    # check for repetitions on keyword...
    ne = len(self.ASGroot.listNodes["ASG_ERmetaMetaModel"])
    new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))

    new_obj.DrawObject(self.UMLmodel,self.editGGLabel)
    self.UMLmodel.addtag_withtag("ASG_ERmetaMetaModel", new_obj.tag)
    new_semantic_obj.graphObject_ = new_obj
    self.ASGroot.addNode(new_semantic_obj)
    self.mode=self.IDLEMODE
    # update status bars...
    if self.editGGLabel :
       self.statusbar.event(self.statusbar.TRANSFORMATION, self.statusbar.CREATE)
    else:
       self.statusbar.event(self.statusbar.MODEL, self.statusbar.CREATE)
    return new_semantic_obj

def createNewERrelationship(self, wherex, wherey, screenCoordinates = 1):
    self.fromClass = None
    self.toClass = None
    new_semantic_obj = ERrelationship(self)
    # check for repetitions on keyword...
    ne = len(self.ASGroot.listNodes["ERrelationship"])
    new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
    new_semantic_obj.appearance.className = new_semantic_obj.keyword_.toString()
    if screenCoordinates:    
      new_obj = graph_ERrelationship(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
    else:
      new_obj = graph_ERrelationship(wherex, wherey, new_semantic_obj)
    new_obj.DrawObject(self.UMLmodel,self.editGGLabel)
    self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    new_semantic_obj.graphObject_ = new_obj
    self.ASGroot.addNode(new_semantic_obj)
    self.mode=self.IDLEMODE
    # update status bars...
    if self.editGGLabel :
       self.statusbar.event(self.statusbar.TRANSFORMATION, self.statusbar.CREATE)
    else:
       self.statusbar.event(self.statusbar.MODEL, self.statusbar.CREATE)
    # update status bars...
    if self.editGGLabel :
       self.statusbar.event(self.statusbar.TRANSFORMATION, self.statusbar.CREATE)
    else:
       self.statusbar.event(self.statusbar.MODEL, self.statusbar.CREATE)
    return new_semantic_obj

def fillTypesInformation(self):
    "fill information about types and handling functions"

    objList = []
    params  = []

    obj = ATOM3TypeInfo(self)
    obj.setValue(('String', 'ATOM3String', () , 0))
    objList.append(obj)

    params = []
    param = ATOM3String('None')
    params.append(param)
    param = ATOM3String('None')
    params.append(param)
    param = ATOM3String('1')
    params.append(param)

    obj = ATOM3TypeInfo(self)
    obj.setValue(('Boolean', 'ATOM3Boolean', params, 0))
    objList.append(obj)

    obj = ATOM3TypeInfo(self)
    obj.setValue(('Integer', 'ATOM3Integer', () , 0))
    objList.append(obj)

    obj = ATOM3TypeInfo(self)
    obj.setValue(('Float', 'ATOM3Float', () , 0))
    objList.append(obj)

    obj = ATOM3TypeInfo(self)

    params = []

    param = ATOM3String('self.types')
    params.append(param)

    obj.setValue(('Attribute', 'ATOM3Attribute', params , 0))
    objList.append(obj)

    obj = ATOM3TypeInfo(self)
    # fill list attributes
    params = []

    param = ATOM3String('[1,1,1,self.types]')
    params.append(param)

    param = ATOM3String('ATOM3Attribute')
    params.append(param)

    param = ATOM3String('self.types')
    params.append(param)

    obj.setValue(('List', 'ATOM3List', params , 0)) 
    objList.append(obj)

    obj = ATOM3TypeInfo(self)
    # fill list attributes
    params = []

    param = ATOM3String('[]')
    params.append(param)

    param = ATOM3String('1')
    params.append(param)

    param = ATOM3String('1')
    params.append(param)

    obj.setValue(('Enum', 'ATOM3Enum', params , 0)) 
    objList.append(obj)

    obj = ATOM3TypeInfo(self)

    obj.setValue(('Constraint', 'ATOM3Constraint', () , 0))
    objList.append(obj)

    obj = ATOM3TypeInfo(self)

    params = []

    param = ATOM3String("'class0'")
    params.append(param)

    param = ATOM3String('None')
    params.append(param)

    obj.setValue(('Appearance', 'ATOM3Appearance', params , 0))
    objList.append(obj)

    obj = ATOM3TypeInfo(self)
    obj.setValue(('BottomType', 'ATOM3BottomType', () , 0))
    objList.append(obj)

    obj = ATOM3TypeInfo(self)
    obj.setValue(('Link', 'ATOM3Link', () , 0))
    objList.append(obj)

    obj = ATOM3TypeInfo(self)
    obj.setValue(('Port', 'ATOM3Port', () , 0))
    objList.append(obj)

    obj = ATOM3TypeInfo(self)
    obj.setValue(('Connection', 'ATOM3Connection', () , 0))
    objList.append(obj)

    obj = ATOM3TypeInfo(self)
    params = []

    param = ATOM3String("None")
    params.append(param)

    param = ATOM3String("None")
    params.append(param)
    
    param = ATOM3String("1")
    params.append(param)

    obj.setValue(('MSEnum', 'ATOM3MSEnum', params , 0))
    objList.append(obj)

    obj = ATOM3TypeInfo(self)
    obj.setValue(('Text', 'ATOM3Text', (), 0))
    objList.append(obj)
    
    
    self.typeList.setValue(objList)

