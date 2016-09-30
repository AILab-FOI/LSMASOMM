from ASG             import *
from ATOM3Type       import *
from ATOM3List       import *
from ATOM3Constraint import *
from ATOM3Attribute  import *
from copy            import *

from graph_ASG_ERmetaMetaModel import *

class ASG_ERmetaMetaModel(ASG, ATOM3Type):

  def __init__(self, parent=None, ASGroot = None):
      ASG.__init__(self, 'ERmetaMetaModel', ASGroot, ["ERentity", "ERrelationship", "ASG_ERmetaMetaModel"] )
      ATOM3Type.__init__(self)
      self.parent         = parent
      self.name           = ATOM3String('ERModel')
      self.attributes     = ATOM3List([1,1,1, None], ATOM3Attribute, parent.types)
      self.constraints    = ATOM3List([1,1,1, None], ATOM3Constraint)
      self.containerFrame = None

      self.graphClass_    = graph_ASG_ERmetaMetaModel

      self.keyword_       = self.name

      self.generatedAttributes = { 'name'       : ('ATOM3String', ),
                                   'attributes' : ('ATOM3List', 'ATOM3Attribute'),
                                   'constraints': ('ATOM3List', 'ATOM3Constraint')}

  def show(self, parent, parentWindow):
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text="name").grid(row=0, column=0, sticky=W)
      self.name.show       (self.containerFrame, parentWindow).grid(row=0, column=1, sticky=W)   # pack the widget to edit the name

      Label(self.containerFrame, text="atributes").grid(row=1, column=0, sticky=W)
      self.attributes.show(self.containerFrame, parentWindow).grid(row=1, column=1, sticky=W)   # attributes to generate

      Label(self.containerFrame, text="constraints").grid(row=2, column=0, sticky=W)
      self.constraints.show(self.containerFrame, parentWindow).grid(row=2, column=1, sticky=W)   # constraints to generate
      return self.containerFrame

  def open(self, parent, parentWindow):
      "Method to open an ATOM3 instance to edit the entities (to be overwritten)"
      from ATOM3	     import ATOM3
      a = ATOM3 (parentWindow , "EntityRelationship", 0, 1, self)
      return a

  def toString(self):
      return (self.name.toString(), self.attributes.toString(), self.constraints.toString())

  def clone(self):
      "creates an exact copy of this object"
      #cloneObject      = ASG_UMLmetaMetaModel(self.parent)
      #cloneObject.listNodes     = copy.copy(self.listNodes)
      #cloneObject.name          = self.name.clone()
      #cloneObject.attributes    = self.attributes.clone()
      #cloneObject.constraints   = self.constraints.clone()
      #cloneObject.containerFrame= self.containerFrame
      #cloneObject.keyword_      = cloneObject.keyword_
      #return cloneObject
      return self

  def copy(self, other):
      "copies each field of the other object into its own state"
      ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
      self.name          = other.name
      self.constraints   = other.constraints
      self.attributes    = other.attributes
      self.keyword_      = self.name
      self.containerFrame= other.containerFrame

  def destroy(self):
      ASGNode.GGcheckSetNone(self)
      self.destroyNodes()            
      self.name.destroy()
      self.attributes.destroy()
      self.constraints.destroy()
      self.containerFrame = None

  def allClassesDistinct(self):
      for node1 in self.listNodes["ERentity"]:
         for node2 in self.listNodes["ERentity"]:
            if (node1 != node2) and (node1.keyword_.toString() == node2.keyword_.toString()):
               return ("allClassesDistinct: classes have the same keyword: ", node1.keyword_.toString())
      return None

  def allRelationshipsDistinct(self):
      for node1 in self.listNodes["ERrelationship"]:
         for node2 in self.listNodes["ERrelationship"]:
            if (node1 != node2) and (node1.keyword_.toString() == node2.keyword_.toString()):
               return ("allRelationshipsDistinct: Relationships have the same keyword: ", node1.keyword_.toString())
      return None

  def preCondition(self, actionID, * params):
      if actionID==ASG.SAVE:
         res = self.allClassesDistinct()
         if res: return res
         res = self.allRelationshipsDistinct()
         if res: return res
      return None

  def invalid(self):
      "Decides if the attribute is valid, that is, if the initial value (if any) is valid"
      import string
      vname = self.name.getValue()
      # check if we have a name
      if (not vname) or (vname == ""):                 # the name is mandatory
         return "Entity name must be specified"
      # now check that the name is valid (a variable name)
      if string.count(vname, " ") > 0:
         return "Invalid entity name, no white spaces allowed"
      # check first character
      if (vname[0] >= '0') and (vname[0] <= '9'):              # a number
         return "Invalid variable name, first character must be a letter or '_'"
      if vname[0] != '_' and (vname[0]<'A' or vname[0]>'z'):
         return "Invalid entity name, first character must be a letter or '_'"
      # now check for the rest of not allowed characters...
      for c in range(len(vname)-1):
         if vname[c+1] < 'A' or vname[c+1] > 'z':              # not a letter
            if vname[c+1] < '0' or vname[c+1] > '9':           # not a number
               if vname[c+1] != '_':                                # not underscore
                  return "Invalid model name, character '"+vname[c+1]+"' is not allowed"
      return ASG.invalid(self)

    
