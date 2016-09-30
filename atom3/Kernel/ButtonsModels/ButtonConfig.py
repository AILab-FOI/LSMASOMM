# __ButtonConfig.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ImageText import *
from ATOM3Constraint import *
from ATOM3Boolean import *
from graph_ButtonConfig import *
class ButtonConfig(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_ButtonConfig
      self.parent = parent
      self.Contents= TextUImage()
      self.Contents.Text=ATOM3String('')
      self.Contents.Image=ATOM3String('')
      self.Action=ATOM3Constraint()
      self.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\n'))
      self.Drawing_Mode=ATOM3Boolean()
      self.Drawing_Mode.setValue((' ', 1))
      self.Drawing_Mode.config = 0
      self.generatedAttributes = {'Contents': ('ATOM3ImageText', ),
                                  'Action': ('ATOM3Constraint', ),
                                  'Drawing_Mode': ('ATOM3Boolean', )      }
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      
      Label(self.containerFrame, text='Contents').grid(row=0,column=0,sticky=W)
      self.Contents.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'Contents', 0, 2)
      
      Label(self.containerFrame, text='Action').grid(row=1,column=0,sticky=W)
      Button( self.containerFrame, text = 'edit', command =  lambda x=self : ATOM3TypeDialog(x.containerFrame, x.Action)).grid(row=1,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'Action', 1, 2)
      
      Label(self.containerFrame, text='Drawing_Mode').grid(row=2,column=0,sticky=W)
      self.Drawing_Mode.show(self.containerFrame, parentWindowInfo).grid(row=2,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'Drawing_Mode', 2, 2)
      ASGNode.editGGLabel(self, self.containerFrame, parentWindowInfo, 3)
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      rs = self.Contents.toString()+' '+self.Action.toString()+' '+self.Drawing_Mode.toString()
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs


   def getValue(self):
      return (self.Contents.getValue(),self.Action.getValue(),self.Drawing_Mode.getValue(),)

   def setValue(self, value):
      self.Contents.setValue(value[0])
      self.Action.setValue(value[1])
      self.Drawing_Mode.setValue(value[2])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
      self.Contents.writeConstructor2File(file, indent, objName+'.Contents', depth, generatingCode)
      self.Action.writeConstructor2File(file, indent, objName+'.Action', depth, generatingCode)
      self.Drawing_Mode.writeConstructor2File(file, indent, objName+'.Drawing_Mode', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"
      self.Contents.writeValue2File(file, indent, objName+'.Contents', depth, generatingCode)
      self.Action.writeValue2File(file, indent, objName+'.Action', depth, generatingCode)
      self.Drawing_Mode.writeValue2File(file, indent, objName+'.Drawing_Mode', depth, generatingCode)

   def invalid(self):
      ASGNode.GGcheckSetNone(self)
      return self.Contents.invalid() or self.Action.invalid() or self.Drawing_Mode.invalid() 

   def clone(self):
      cloneObject = ButtonConfig( self.parent )
      cloneObject.Contents = self.Contents.clone()
      cloneObject.Action = self.Action.clone()
      cloneObject.Drawing_Mode = self.Drawing_Mode.clone()
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.Contents = other.Contents
      self.Action = other.Action
      self.Drawing_Mode = other.Drawing_Mode
      ASGNode.copy(self, other)

   def destroy(self):
      ASGNode.GGcheckSetNone(self)
      self.Contents.destroy()
      self.Action.destroy()
      self.Drawing_Mode.destroy()
      self.containerFrame = None
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


