# __ASG_ClassDiagramB.py_____________________________________________________
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Text import *
from ATOM3List import *
from ATOM3Attribute import *
from ATOM3MSEnum import *
from ATOM3Port import *
from ATOM3Integer import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Link import *
from ATOM3Boolean import *
from ATOM3Connection import *
from ATOM3Enum import *
from ATOM3Constraint import *
from ATOM3BottomType import *
class ASG_ClassDiagramB(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'ClassDiagramB', ASGroot, ['ASG_ClassDiagramB' ,'AtomClass' ,'AtomInheritance' ,'AtomAssociation'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.ModelName=ATOM3String('NewCD')
      self.keyword_= self.ModelName
      self.Author=ATOM3String('')
      self.Description=ATOM3Text('\n', 60,15 )
      self.Attributes=ATOM3List([ 1, 1, 1, 0],ATOM3Attribute,parent.types )
      lcobj0=[]
      self.Attributes.setValue(lcobj0)
      self.Constraints=ATOM3List([ 1, 1, 1, 0],ATOM3Constraint)
      lcobj0=[]
      self.Constraints.setValue(lcobj0)
      self.generatedAttributes = {'ModelName': ('ATOM3String', ),
                                  'Author': ('ATOM3String', ),
                                  'Description': ('ATOM3Text', ),
                                  'Attributes': ('ATOM3List', 'ATOM3Attribute'),
                                  'Constraints': ('ATOM3List', 'ATOM3Constraint')      }
      self.realOrder = ['ModelName','Author','Description','Attributes','Constraints']
      self.directEditing = [1,1,0,1,1]
   def clone(self):
      return self
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      self.keyword_ = self.ModelName
   def open(self, parent, topWindowParent):
       from ATOM3 import *
       a = ATOM3(topWindowParent, 'ClassDiagramB', 0, 1, self)
       #self.writeContents(a)
       return a
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


