# __rectangle.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Integer import *
from graph_rectangle import *
class rectangle(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_rectangle
      self.parent = parent
      self.fill=ATOM3String('')
      self.outline=ATOM3String('')
      self.stipple=ATOM3String('')
      self.width=ATOM3Integer(0)
      self.generatedAttributes = {'fill': ('ATOM3String', ),
                                  'outline': ('ATOM3String', ),
                                  'stipple': ('ATOM3String', ),
                                  'width': ('ATOM3Integer', )      }
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text='fill').grid(row=0,column=0,sticky=W)
      self.fill.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'fill', 0, 2)
      Label(self.containerFrame, text='outline').grid(row=1,column=0,sticky=W)
      self.outline.show(self.containerFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'outline', 1, 2)
      Label(self.containerFrame, text='stipple').grid(row=2,column=0,sticky=W)
      self.stipple.show(self.containerFrame, parentWindowInfo).grid(row=2,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'stipple', 2, 2)
      Label(self.containerFrame, text='width').grid(row=3,column=0,sticky=W)
      self.width.show(self.containerFrame, parentWindowInfo).grid(row=3,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'width', 3, 2)
      ASGNode.editGGLabel(self, self.containerFrame, parentWindowInfo, 4)
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      rs = self.fill.toString()+' '+self.outline.toString()+' '+self.stipple.toString()+' '+self.width.toString()
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs


   def getValue(self):
      return (self.fill.getValue(),self.outline.getValue(),self.stipple.getValue(),self.width.getValue(),)

   def setValue(self, value):
      self.fill.setValue(value[0])
      self.outline.setValue(value[1])
      self.stipple.setValue(value[2])
      self.width.setValue(value[3])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
      self.fill.writeConstructor2File(file, indent, objName+'.fill', depth, generatingCode)
      self.outline.writeConstructor2File(file, indent, objName+'.outline', depth, generatingCode)
      self.stipple.writeConstructor2File(file, indent, objName+'.stipple', depth, generatingCode)
      self.width.writeConstructor2File(file, indent, objName+'.width', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"
      self.fill.writeValue2File(file, indent, objName+'.fill', depth, generatingCode)
      self.outline.writeValue2File(file, indent, objName+'.outline', depth, generatingCode)
      self.stipple.writeValue2File(file, indent, objName+'.stipple', depth, generatingCode)
      self.width.writeValue2File(file, indent, objName+'.width', depth, generatingCode)

   def invalid(self):
      ASGNode.GGcheckSetNone(self)
      return self.fill.invalid() or self.outline.invalid() or self.stipple.invalid() or self.width.invalid() 

   def clone(self):
      cloneObject = rectangle( self.parent )
      cloneObject.fill = self.fill.clone()
      cloneObject.outline = self.outline.clone()
      cloneObject.stipple = self.stipple.clone()
      cloneObject.width = self.width.clone()
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.fill = other.fill
      self.outline = other.outline
      self.stipple = other.stipple
      self.width = other.width
      ASGNode.copy(self, other)

   def destroy(self):
      ASGNode.GGcheckSetNone(self)
      self.fill.destroy()
      self.outline.destroy()
      self.stipple.destroy()
      self.width.destroy()
      self.containerFrame = None
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


