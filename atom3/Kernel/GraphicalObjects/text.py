# __text.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3Integer import *
from graph_text import *
class text(ASGNode, ATOM3Type):

   def __init__(self, parent = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.graphClass_ = graph_text
      self.parent = parent
      self.anchor=ATOM3String('')
      self.fill=ATOM3String('')
      self.font=ATOM3String('')
      self.justify=ATOM3String('')
      self.stipple=ATOM3String('')
      self.text=ATOM3String('')
      self.width=ATOM3Integer(0)
      self.generatedAttributes = {'anchor': ('ATOM3String', ),
                                  'fill': ('ATOM3String', ),
                                  'font': ('ATOM3String', ),
                                  'justify': ('ATOM3String', ),
                                  'stipple': ('ATOM3String', ),
                                  'text': ('ATOM3String', ),
                                  'width': ('ATOM3Integer', )      }
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text='anchor').grid(row=0,column=0,sticky=W)
      self.anchor.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'anchor', 0, 2)
      Label(self.containerFrame, text='fill').grid(row=1,column=0,sticky=W)
      self.fill.show(self.containerFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'fill', 1, 2)
      Label(self.containerFrame, text='font').grid(row=2,column=0,sticky=W)
      self.font.show(self.containerFrame, parentWindowInfo).grid(row=2,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'font', 2, 2)
      Label(self.containerFrame, text='justify').grid(row=3,column=0,sticky=W)
      self.justify.show(self.containerFrame, parentWindowInfo).grid(row=3,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'justify', 3, 2)
      Label(self.containerFrame, text='stipple').grid(row=4,column=0,sticky=W)
      self.stipple.show(self.containerFrame, parentWindowInfo).grid(row=4,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'stipple', 4, 2)
      Label(self.containerFrame, text='text').grid(row=5,column=0,sticky=W)
      self.text.show(self.containerFrame, parentWindowInfo).grid(row=5,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'text', 5, 2)
      Label(self.containerFrame, text='width').grid(row=6,column=0,sticky=W)
      self.width.show(self.containerFrame, parentWindowInfo).grid(row=6,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'width', 6, 2)
      ASGNode.editGGLabel(self, self.containerFrame, parentWindowInfo, 7)
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      rs = self.anchor.toString()+' '+self.fill.toString()+' '+self.font.toString()+' '+self.justify.toString()+' '+self.stipple.toString()+' '+self.text.toString()+' '+self.width.toString()
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs


   def getValue(self):
      return (self.anchor.getValue(),self.fill.getValue(),self.font.getValue(),self.justify.getValue(),self.stipple.getValue(),self.text.getValue(),self.width.getValue(),)

   def setValue(self, value):
      self.anchor.setValue(value[0])
      self.fill.setValue(value[1])
      self.font.setValue(value[2])
      self.justify.setValue(value[3])
      self.stipple.setValue(value[4])
      self.text.setValue(value[5])
      self.width.setValue(value[6])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
      self.anchor.writeConstructor2File(file, indent, objName+'.anchor', depth, generatingCode)
      self.fill.writeConstructor2File(file, indent, objName+'.fill', depth, generatingCode)
      self.font.writeConstructor2File(file, indent, objName+'.font', depth, generatingCode)
      self.justify.writeConstructor2File(file, indent, objName+'.justify', depth, generatingCode)
      self.stipple.writeConstructor2File(file, indent, objName+'.stipple', depth, generatingCode)
      self.text.writeConstructor2File(file, indent, objName+'.text', depth, generatingCode)
      self.width.writeConstructor2File(file, indent, objName+'.width', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"
      self.anchor.writeValue2File(file, indent, objName+'.anchor', depth, generatingCode)
      self.fill.writeValue2File(file, indent, objName+'.fill', depth, generatingCode)
      self.font.writeValue2File(file, indent, objName+'.font', depth, generatingCode)
      self.justify.writeValue2File(file, indent, objName+'.justify', depth, generatingCode)
      self.stipple.writeValue2File(file, indent, objName+'.stipple', depth, generatingCode)
      self.text.writeValue2File(file, indent, objName+'.text', depth, generatingCode)
      self.width.writeValue2File(file, indent, objName+'.width', depth, generatingCode)

   def invalid(self):
      ASGNode.GGcheckSetNone(self)
      return self.anchor.invalid() or self.fill.invalid() or self.font.invalid() or self.justify.invalid() or self.stipple.invalid() or self.text.invalid() or self.width.invalid() 

   def clone(self):
      cloneObject = text( self.parent )
      cloneObject.anchor = self.anchor.clone()
      cloneObject.fill = self.fill.clone()
      cloneObject.font = self.font.clone()
      cloneObject.justify = self.justify.clone()
      cloneObject.stipple = self.stipple.clone()
      cloneObject.text = self.text.clone()
      cloneObject.width = self.width.clone()
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.anchor = other.anchor
      self.fill = other.fill
      self.font = other.font
      self.justify = other.justify
      self.stipple = other.stipple
      self.text = other.text
      self.width = other.width
      ASGNode.copy(self, other)

   def destroy(self):
      ASGNode.GGcheckSetNone(self)
      self.anchor.destroy()
      self.fill.destroy()
      self.font.destroy()
      self.justify.destroy()
      self.stipple.destroy()
      self.text.destroy()
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


