# __LeafType.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3Attribute import *
from ATOM3Constraint import *
from graph_LeafType import *
class LeafType(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_LeafType
      self.parent = parent
      self.Type=ATOM3Attribute(parent.types)
      self.Type.setValue(('ltypename', 'String', None, ('Key', 0), ('Direct Editing', 1)))
      self.Type.initialValue=ATOM3String('')
      self.TypeConstraint=ATOM3Constraint()
      self.TypeConstraint.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
      self.generatedAttributes = {'Type': ('ATOM3Attribute', ),
                                  'TypeConstraint': ('ATOM3Constraint', )      }
      self.realOrder = ['Type','TypeConstraint']
      self.directEditing = [1,0]
   def clone(self):
      cloneObject = LeafType( self.parent )
      for atr in self.realOrder:
         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      for atr in self.realOrder:
         self.setAttrValue(atr, other.getAttrValue(atr) )
      ASGNode.copy(self, other)

   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


