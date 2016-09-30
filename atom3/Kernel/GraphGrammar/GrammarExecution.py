# __ File: GrammarExecution.py ______________________________________________________________
# Implements : class GrammarExecution
# Author     : Juan de Lara
# Description: Window with some widgets to edit which graph grammars
#              will be executed (a list can be given) and in which mode (STEP by STEP),
#              Parallel or sequential, and if the entities in the graph can be moved when
#              executing a rule.
#              Initially generated with ATOM3, added some widgets by hand.
# Modified   :
#   - 21 Oct 2001. Header added.
#   - 21 Oct 2001. Widget to control if execution must be parallel or sequential.
#   - 9 Aug. 2002: Possibility to animate the application of a GG.
# ___________________________________________________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3List import *
from ATOM3String import *
from ATOM3Boolean import *
from ATOM3File import *

class GrammarExecution(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.parent = parent
      self.Transformations=ATOM3List([ 1, 1, 1, 0],ATOM3File,
                          [("Executable GraphGrammar", "*_GG_exec.py"),
                           ("Python files", "*.py")], 
                          ATOM3File.OPENFILE)
      lcobj0=[]
      self.Transformations.setValue(lcobj0)
      self.STEPbySTEP=ATOM3Boolean()
      self.STEPbySTEP.setValue(('', 0))
      self.STEPbySTEP.config = 0
      self.LetEntitiesMove=ATOM3Boolean()
      self.LetEntitiesMove.setValue(('', 0))
      self.LetEntitiesMove.config = 0
      self.animate = ATOM3Boolean()
      self.animate.setValue(('', 0))
      self.Execution=ATOM3Enum(['Sequential Random', 'Sequential Manual', 'Parallel'], 0)
      self.generatedAttributes = {'Transformations': ('ATOM3List', ),
                                  'STEPbySTEP': ('ATOM3Boolean', ),
                                  'LetEntitiesMove': ('ATOM3Boolean', ),
                                  'animate': ('ATOM3Boolean', ),
                                  'Execution': ('ATOM3Enum', ) }
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text='Transformations').grid(row=0,column=0,sticky=W)
      self.Transformations.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'Transformations', 0, 2)

      Label(self.containerFrame, text='STEPbySTEP').grid(row=1,column=0,sticky=W)
      self.STEPbySTEP.show(self.containerFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'STEPbySTEP', 1, 2)

      Label(self.containerFrame, text='LetEntitiesMove').grid(row=2,column=0,sticky=W)
      self.LetEntitiesMove.show(self.containerFrame, parentWindowInfo).grid(row=2,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'LetEntitiesMove', 2, 2)

      Label(self.containerFrame, text='Animate').grid(row=3,column=0,sticky=W)
      self.animate.show(self.containerFrame, parentWindowInfo).grid(row=3,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'LetEntitiesMove', 3, 2)

      Label(self.containerFrame, text='Execution').grid(row=4,column=0,sticky=W)
      self.Execution.show(self.containerFrame, parentWindowInfo).grid(row=4,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'Execution', 4, 2)

      ASGNode.editGGLabel(self, self.containerFrame, parentWindowInfo, 5)
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      rs = self.Transformations.toString()+' '+self.STEPbySTEP.toString()+' '+self.LetEntitiesMove.toString()+' '+self.animate.toString()+' '+self.Execution.toString()
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs

   def getValue(self):
      return (self.Transformations.getValue(),self.STEPbySTEP.getValue(),self.LetEntitiesMove.getValue(),self.animate.getValue(), self.Execution.getValue(), )

   def setValue(self, value):
      self.Transformations.setValue(value[0])
      self.STEPbySTEP.setValue(value[1])
      self.LetEntitiesMove.setValue(value[2])
      self.animate.setValue(value[3])      
      self.Execution.setValue(value[4])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
      self.Transformations.writeConstructor2File(file, indent, objName+'.Transformations', depth, generatingCode)
      self.STEPbySTEP.writeConstructor2File(file, indent, objName+'.STEPbySTEP', depth, generatingCode)
      self.LetEntitiesMove.writeConstructor2File(file, indent, objName+'.LetEntitiesMove', depth, generatingCode)
      self.animate.writeConstructor2File(file, indent, objName+'.animate', depth, generatingCode)
      self.Execution.writeConstructor2File(file, indent, objName+'.Execution', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"
      self.Transformations.writeValue2File(file, indent, objName+'.Transformations', depth, generatingCode)
      self.STEPbySTEP.writeValue2File(file, indent, objName+'.STEPbySTEP', depth, generatingCode)
      self.LetEntitiesMove.writeValue2File(file, indent, objName+'.LetEntitiesMove', depth, generatingCode)
      self.animate.writeValue2File(file, indent, objName+'.animate', depth, generatingCode)      
      self.Execution.writeValue2File(file, indent, objName+'.Execution', depth, generatingCode)

   def invalid(self):
      return self.Transformations.invalid() or self.STEPbySTEP.invalid() or self.LetEntitiesMove.invalid() or self.animate.invalid() or self.Execution.invalid()

   def clone(self):
      cloneObject = GrammarExecution( self.parent )
      cloneObject.Transformations = self.Transformations.clone()
      cloneObject.STEPbySTEP      = self.STEPbySTEP.clone()
      cloneObject.LetEntitiesMove = self.LetEntitiesMove.clone()
      cloneObject.animate         = self.animate.clone()      
      cloneObject.Execution       = self.Execution.clone()
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.Transformations = other.Transformations
      self.STEPbySTEP = other.STEPbySTEP
      self.LetEntitiesMove = other.LetEntitiesMove
      self.animate = other.animate
      self.Execution = other.Execution
      ASGNode.copy(self, other)

   def destroy(self):
      ASGNode.GGcheckSetNone(self)
      self.Transformations.destroy()
      self.STEPbySTEP.destroy()
      self.LetEntitiesMove.destroy()
      self.animate.destroy()
      self.Execution.destroy()
      self.containerFrame = None
   def cardinalityCheck(self, selfPosition):
      return None
   def checkConnectedObjectType(self, selfPosition):
      if selfPosition == 'SOURCE':
         last=self.out_connections_[len(self.out_connections_)-1]
         return ('Incorrect connection to ', last.getClass())
      else:
         last=self.in_connections_[len(self.in_connections_)-1]
         return ('Incorrect connection to ', last.getClass())
      return None
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.CONNECT:
         res = self.checkConnectedObjectType(params[0])
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


