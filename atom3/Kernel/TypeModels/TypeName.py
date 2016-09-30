# __TypeName.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from graph_TypeName import *
class TypeName(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_TypeName
      self.parent = parent
      self.Name=ATOM3String('typename')
      self.keyword_= self.Name
      self.generatedAttributes = {'Name': ('ATOM3String', )      }
      self.realOrder = ['Name']
      self.directEditing = [1]
   def clone(self):
      cloneObject = TypeName( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      cloneObject.keyword_ = cloneObject.Name
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.Name
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.EDIT:
         res = self.validName(params)
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None
   def validName(self, params):
      import string
      vname = self.Name.getValue()
      # check if we have a name
      if (not vname) or (vname == ""):                 # the name is mandatory
         return "Entity name must be specified", ""
      # now check that the name is valid (a variable name)
      if string.count(vname, " ") > 0:
         return "Invalid entity name, no white spaces allowed",""
      # check first character
      if (vname[0] >= '0') and (vname[0] <= '9'):              # a number
         return "Invalid variable name, first character must be a letter or '_'",""
      if vname[0] != '_' and (vname[0]<'A' or vname[0]>'z'):
         return "Invalid entity name, first character must be a letter or '_'",""
      # now check for the rest of not allowed characters...
      for c in range(len(vname)-1):
       if vname[c+1] < 'A' or vname[c+1] > 'z':              # not a letter
        if vname[c+1] < '0' or vname[c+1] > '9':           # not a number
         if vname[c+1] != '_':                                # not underscore
          return "Invalid entity name, character '"+vname[c+1]+"' is not allowed",""
      
      
      
      



