# __polygon.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Integer import *
from graph_polygon import *
class polygon(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_polygon
      self.parent = parent
      self.fill=ATOM3String('')
      self.stipple=ATOM3String('')
      self.outline=ATOM3String('')
      self.width=ATOM3Integer(0)
      self.smooth=ATOM3String('')
      self.splinesteps=ATOM3Integer(0)
      self.generatedAttributes = {'fill': ('ATOM3String', ),
                                  'stipple': ('ATOM3String', ),
                                  'outline': ('ATOM3String', ),
                                  'width': ('ATOM3Integer', ),
                                  'smooth': ('ATOM3String', ),
                                  'splinesteps': ('ATOM3Integer', )      }
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text='fill').grid(row=0,column=0,sticky=W)
      self.fill.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'fill', 0, 2)
      Label(self.containerFrame, text='stipple').grid(row=1,column=0,sticky=W)
      self.stipple.show(self.containerFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'stipple', 1, 2)
      Label(self.containerFrame, text='outline').grid(row=2,column=0,sticky=W)
      self.outline.show(self.containerFrame, parentWindowInfo).grid(row=2,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'outline', 2, 2)
      Label(self.containerFrame, text='width').grid(row=3,column=0,sticky=W)
      self.width.show(self.containerFrame, parentWindowInfo).grid(row=3,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'width', 3, 2)
      Label(self.containerFrame, text='smooth').grid(row=4,column=0,sticky=W)
      self.smooth.show(self.containerFrame, parentWindowInfo).grid(row=4,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'smooth', 4, 2)
      Label(self.containerFrame, text='splinesteps').grid(row=5,column=0,sticky=W)
      self.splinesteps.show(self.containerFrame, parentWindowInfo).grid(row=5,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'splinesteps', 5, 2)
      ASGNode.editGGLabel(self, self.containerFrame, parentWindowInfo, 6)
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      rs = self.fill.toString()+' '+self.stipple.toString()+' '+self.outline.toString()+' '+self.width.toString()+' '+self.smooth.toString()+' '+self.splinesteps.toString()
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs


   def getValue(self):
      return (self.fill.getValue(),self.stipple.getValue(),self.outline.getValue(),self.width.getValue(),self.smooth.getValue(),self.splinesteps.getValue(),)

   def setValue(self, value):
      self.fill.setValue(value[0])
      self.stipple.setValue(value[1])
      self.outline.setValue(value[2])
      self.width.setValue(value[3])
      self.smooth.setValue(value[4])
      self.splinesteps.setValue(value[5])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
      self.fill.writeConstructor2File(file, indent, objName+'.fill', depth, generatingCode)
      self.stipple.writeConstructor2File(file, indent, objName+'.stipple', depth, generatingCode)
      self.outline.writeConstructor2File(file, indent, objName+'.outline', depth, generatingCode)
      self.width.writeConstructor2File(file, indent, objName+'.width', depth, generatingCode)
      self.smooth.writeConstructor2File(file, indent, objName+'.smooth', depth, generatingCode)
      self.splinesteps.writeConstructor2File(file, indent, objName+'.splinesteps', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"
      self.fill.writeValue2File(file, indent, objName+'.fill', depth, generatingCode)
      self.stipple.writeValue2File(file, indent, objName+'.stipple', depth, generatingCode)
      self.outline.writeValue2File(file, indent, objName+'.outline', depth, generatingCode)
      self.width.writeValue2File(file, indent, objName+'.width', depth, generatingCode)
      self.smooth.writeValue2File(file, indent, objName+'.smooth', depth, generatingCode)
      self.splinesteps.writeValue2File(file, indent, objName+'.splinesteps', depth, generatingCode)

   def invalid(self):
      ASGNode.GGcheckSetNone(self)
      return self.fill.invalid() or self.stipple.invalid() or self.outline.invalid() or self.width.invalid() or self.smooth.invalid() or self.splinesteps.invalid() 

   def clone(self):
      cloneObject = polygon( self.parent )
      cloneObject.fill = self.fill.clone()
      cloneObject.stipple = self.stipple.clone()
      cloneObject.outline = self.outline.clone()
      cloneObject.width = self.width.clone()
      cloneObject.smooth = self.smooth.clone()
      cloneObject.splinesteps = self.splinesteps.clone()
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.fill = other.fill
      self.stipple = other.stipple
      self.outline = other.outline
      self.width = other.width
      self.smooth = other.smooth
      self.splinesteps = other.splinesteps
      ASGNode.copy(self, other)

   def destroy(self):
      ASGNode.GGcheckSetNone(self)
      self.fill.destroy()
      self.stipple.destroy()
      self.outline.destroy()
      self.width.destroy()
      self.smooth.destroy()
      self.splinesteps.destroy()
      self.containerFrame = None
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


