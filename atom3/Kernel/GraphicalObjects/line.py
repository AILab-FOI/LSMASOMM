# __line.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3Integer import *
from ATOM3String import *
from graph_line import *
class line(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_line
      self.parent = parent
      self.width=ATOM3Integer(0)
      self.fill=ATOM3String('')
      self.stipple=ATOM3String('')
      self.arrow=ATOM3String('')
      self.arrowshape=ATOM3String('')
      self.capstyle=ATOM3String('')
      self.joinstyle=ATOM3String('')
      self.smooth=ATOM3String('')
      self.splinesteps=ATOM3Integer(0)
      self.generatedAttributes = {'width': ('ATOM3Integer', ),
                                  'fill': ('ATOM3String', ),
                                  'stipple': ('ATOM3String', ),
                                  'arrow': ('ATOM3String', ),
                                  'arrowshape': ('ATOM3String', ),
                                  'capstyle': ('ATOM3String', ),
                                  'joinstyle': ('ATOM3String', ),
                                  'smooth': ('ATOM3String', ),
                                  'splinesteps': ('ATOM3Integer', )      }
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text='width').grid(row=0,column=0,sticky=W)
      self.width.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'width', 0, 2)
      Label(self.containerFrame, text='fill').grid(row=1,column=0,sticky=W)
      self.fill.show(self.containerFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'fill', 1, 2)
      Label(self.containerFrame, text='stipple').grid(row=2,column=0,sticky=W)
      self.stipple.show(self.containerFrame, parentWindowInfo).grid(row=2,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'stipple', 2, 2)
      Label(self.containerFrame, text='arrow').grid(row=3,column=0,sticky=W)
      self.arrow.show(self.containerFrame, parentWindowInfo).grid(row=3,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'arrow', 3, 2)
      Label(self.containerFrame, text='arrowshape').grid(row=4,column=0,sticky=W)
      self.arrowshape.show(self.containerFrame, parentWindowInfo).grid(row=4,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'arrowshape', 4, 2)
      Label(self.containerFrame, text='capstyle').grid(row=5,column=0,sticky=W)
      self.capstyle.show(self.containerFrame, parentWindowInfo).grid(row=5,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'capstyle', 5, 2)
      Label(self.containerFrame, text='joinstyle').grid(row=6,column=0,sticky=W)
      self.joinstyle.show(self.containerFrame, parentWindowInfo).grid(row=6,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'joinstyle', 6, 2)
      Label(self.containerFrame, text='smooth').grid(row=7,column=0,sticky=W)
      self.smooth.show(self.containerFrame, parentWindowInfo).grid(row=7,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'smooth', 7, 2)
      Label(self.containerFrame, text='splinesteps').grid(row=8,column=0,sticky=W)
      self.splinesteps.show(self.containerFrame, parentWindowInfo).grid(row=8,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'splinesteps', 8, 2)
      ASGNode.editGGLabel(self, self.containerFrame, parentWindowInfo, 9)
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      rs = self.width.toString()+' '+self.fill.toString()+' '+self.stipple.toString()+' '+self.arrow.toString()+' '+self.arrowshape.toString()+' '+self.capstyle.toString()+' '+self.joinstyle.toString()+' '+self.smooth.toString()+' '+self.splinesteps.toString()
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs


   def getValue(self):
      return (self.width.getValue(),self.fill.getValue(),self.stipple.getValue(),self.arrow.getValue(),self.arrowshape.getValue(),self.capstyle.getValue(),self.joinstyle.getValue(),self.smooth.getValue(),self.splinesteps.getValue(),)

   def setValue(self, value):
      self.width.setValue(value[0])
      self.fill.setValue(value[1])
      self.stipple.setValue(value[2])
      self.arrow.setValue(value[3])
      self.arrowshape.setValue(value[4])
      self.capstyle.setValue(value[5])
      self.joinstyle.setValue(value[6])
      self.smooth.setValue(value[7])
      self.splinesteps.setValue(value[8])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
      self.width.writeConstructor2File(file, indent, objName+'.width', depth, generatingCode)
      self.fill.writeConstructor2File(file, indent, objName+'.fill', depth, generatingCode)
      self.stipple.writeConstructor2File(file, indent, objName+'.stipple', depth, generatingCode)
      self.arrow.writeConstructor2File(file, indent, objName+'.arrow', depth, generatingCode)
      self.arrowshape.writeConstructor2File(file, indent, objName+'.arrowshape', depth, generatingCode)
      self.capstyle.writeConstructor2File(file, indent, objName+'.capstyle', depth, generatingCode)
      self.joinstyle.writeConstructor2File(file, indent, objName+'.joinstyle', depth, generatingCode)
      self.smooth.writeConstructor2File(file, indent, objName+'.smooth', depth, generatingCode)
      self.splinesteps.writeConstructor2File(file, indent, objName+'.splinesteps', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"
      self.width.writeValue2File(file, indent, objName+'.width', depth, generatingCode)
      self.fill.writeValue2File(file, indent, objName+'.fill', depth, generatingCode)
      self.stipple.writeValue2File(file, indent, objName+'.stipple', depth, generatingCode)
      self.arrow.writeValue2File(file, indent, objName+'.arrow', depth, generatingCode)
      self.arrowshape.writeValue2File(file, indent, objName+'.arrowshape', depth, generatingCode)
      self.capstyle.writeValue2File(file, indent, objName+'.capstyle', depth, generatingCode)
      self.joinstyle.writeValue2File(file, indent, objName+'.joinstyle', depth, generatingCode)
      self.smooth.writeValue2File(file, indent, objName+'.smooth', depth, generatingCode)
      self.splinesteps.writeValue2File(file, indent, objName+'.splinesteps', depth, generatingCode)

   def invalid(self):
      ASGNode.GGcheckSetNone(self)
      return self.width.invalid() or self.fill.invalid() or self.stipple.invalid() or self.arrow.invalid() or self.arrowshape.invalid() or self.capstyle.invalid() or self.joinstyle.invalid() or self.smooth.invalid() or self.splinesteps.invalid() 

   def clone(self):
      cloneObject = line( self.parent )
      cloneObject.width = self.width.clone()
      cloneObject.fill = self.fill.clone()
      cloneObject.stipple = self.stipple.clone()
      cloneObject.arrow = self.arrow.clone()
      cloneObject.arrowshape = self.arrowshape.clone()
      cloneObject.capstyle = self.capstyle.clone()
      cloneObject.joinstyle = self.joinstyle.clone()
      cloneObject.smooth = self.smooth.clone()
      cloneObject.splinesteps = self.splinesteps.clone()
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.width = other.width
      self.fill = other.fill
      self.stipple = other.stipple
      self.arrow = other.arrow
      self.arrowshape = other.arrowshape
      self.capstyle = other.capstyle
      self.joinstyle = other.joinstyle
      self.smooth = other.smooth
      self.splinesteps = other.splinesteps
      ASGNode.copy(self, other)

   def destroy(self):
      ASGNode.GGcheckSetNone(self)
      self.width.destroy()
      self.fill.destroy()
      self.stipple.destroy()
      self.arrow.destroy()
      self.arrowshape.destroy()
      self.capstyle.destroy()
      self.joinstyle.destroy()
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


