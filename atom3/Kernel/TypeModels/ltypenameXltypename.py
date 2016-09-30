from Tkinter import *
from ATOM3Type import *
from ATOM3String import *
from ATOM3String import *
class ltypenameXltypename (ATOM3Type):
   def __init__(self):
      ATOM3Type.__init__(self)
      self.ltypename= None
      self.ltypename= None

   def createComponents(self):
      if not self.ltypename:
         self.ltypename=ATOM3String('')
      if not self.ltypename:
         self.ltypename=ATOM3String('')

   def show(self, parent, parentWindowInfo=None):
      self.createComponents()
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text='ltypename').grid(row=0,column=0,sticky=W)
      self.ltypename.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      Label(self.containerFrame, text='ltypename').grid(row=1,column=0,sticky=W)
      self.ltypename.show(self.containerFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
      return self.containerFrame

   def toString(self):
      self.createComponents()
      return  self.ltypename.toString()+' '+ self.ltypename.toString()
   def getValue(self):
      self.createComponents()
      return (self.ltypename.getValue(),self.ltypename.getValue(),)

   def setValue(self, value):
      self.createComponents()
      if value == None:
         self.ltypename.setNone()
         self.ltypename.setNone()
      else:
         self.ltypename.setValue(value[0])
         self.ltypename.setValue(value[1])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      self.createComponents()
      file.write(indent+objName+'= ltypenameXltypename()\n')
      self.ltypename.writeConstructor2File(file, indent, objName+'.ltypename', depth, generatingCode)
      self.ltypename.writeConstructor2File(file, indent, objName+'.ltypename', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      self.createComponents()
      self.ltypename.writeValue2File(file, indent, objName+'.ltypename', depth, generatingCode)
      self.ltypename.writeValue2File(file, indent, objName+'.ltypename', depth, generatingCode)

   def clone(self):
     "Makes an exact copy of itself"
     cloneObject = ltypenameXltypename()
     if self.ltypename: cloneObject.ltypename = self.ltypename.clone()
     if self.ltypename: cloneObject.ltypename = self.ltypename.clone()
     return cloneObject
   def destroy(self):
     "Destroys (i.e. updates) each field"
     cloneObject = ltypenameXltypename()
     if self.ltypename: self.ltypename.destroy()
     if self.ltypename: self.ltypename.destroy()
     return cloneObject
