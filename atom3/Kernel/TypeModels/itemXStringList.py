from Tkinter import *
from ATOM3Type import *
from ATOM3String import *
from StringList import *
class itemXStringList (ATOM3Type):
   def __init__(self):
      ATOM3Type.__init__(self)
      self.item= None
      self.StringList= None

   def createComponents(self):
      if not self.item:
         self.item=ATOM3String('')
      if not self.StringList:
         from StringList import *
         self.StringList=StringList()

   def show(self, parent, parentWindowInfo=None):
      self.createComponents()
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text='item').grid(row=0,column=0,sticky=W)
      self.item.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      Label(self.containerFrame, text='StringList').grid(row=1,column=0,sticky=W)
      self.StringList.show(self.containerFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
      return self.containerFrame

   def toString(self):
      self.createComponents()
      return  self.item.toString()+' '+ self.StringList.toString()
   def getValue(self):
      self.createComponents()
      return (self.item.getValue(),self.StringList.getValue(),)

   def setValue(self, value):
      self.createComponents()
      if value == None:
         self.item.setNone()
         self.StringList.setNone()
      else:
         self.item.setValue(value[0])
         self.StringList.setValue(value[1])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      self.createComponents()
      file.write(indent+objName+'= itemXStringList()
')
      self.item.writeConstructor2File(file, indent, objName+'.item', depth, generatingCode)
      self.StringList.writeConstructor2File(file, indent, objName+'.StringList', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      self.createComponents()
      self.item.writeValue2File(file, indent, objName+'.item', depth, generatingCode)
      self.StringList.writeValue2File(file, indent, objName+'.StringList', depth, generatingCode)

   def clone(self):
     "Makes an exact copy of itself"
     cloneObject = itemXStringList()
     if self.item: cloneObject.item = self.item.clone()
     if self.StringList: cloneObject.StringList = self.StringList.clone()
     return cloneObject
   def destroy(self):
     "Destroys (i.e. updates) each field"
     cloneObject = itemXStringList()
     if self.item: self.item.destroy()
     if self.StringList: self.StringList.destroy()
     return cloneObject
