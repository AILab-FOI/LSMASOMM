from Tkinter import *
from ATOM3Type import *
from itemXStringList import *
from ATOM3String import *
class itemXStringListUhead (ATOM3Type):
   def __init__(self):
ATOM3Type.__init__(self)
self.optMenu = None
self.selected= None
self.itemXStringList= None
self.head= None

   def createComponents(self):
if not self.itemXStringList:
   from itemXStringList import *
   self.itemXStringList=itemXStringList()
if not self.head:
   self.head=ATOM3String('')

   def show(self, parent, parentWindowInfo=None):
ATOM3Type.show(self, parent, parentWindowInfo)
self.createComponents()
self.showParent = parent
self.parentWindowInfo = parentWindowInfo
self.selected = StringVar()
self.lastSelected = None
self.label = None
self.widget = None
self.containerFrame = Frame(parent)
Label(self.containerFrame, text='Select Attribute').grid(row=0,column=0,sticky=W)
self.selected.set('itemXStringList')
self.optMenu = OptionMenu(self.containerFrame, self.selected,'itemXStringList','head')
self.selected.trace_variable( 'w', self.valueChanged)
self.optMenu.grid(row=0,column=1,sticky=W)
return self.containerFrame

   def valueChanged(self, param1, param2, param3):
value = self.selected.get()
if value == 'itemXStringList':
   if self.lastSelected != 'itemXStringList':
self.destroyAllBut(self.itemXStringList)
self.showitemXStringList(self.showParent, self.parentWindowInfo)
if value == 'head':
   if self.lastSelected != 'head':
self.destroyAllBut(self.head)
self.showhead(self.showParent, self.parentWindowInfo)
   def destroyAllBut(self, survivor):
if survivor != self.itemXStringList:
   self.itemXStringList.destroy()
if survivor != self.head:
   self.head.destroy()

   def showitemXStringList(self, parent, parentWindow = None):
if self.label and self.widget:
   self.label.grid_forget()
   self.widget.grid_forget()
self.label = Label(self.containerFrame, text='itemXStringList')
self.label.grid(row=1,column=0,sticky=W)
self.widget = self.itemXStringList.show(self.containerFrame, self.parentWindowInfo)
self.widget.grid(row=1,column=1,sticky=W)
self.lastSelected = 'itemXStringList'

   def showhead(self, parent, parentWindow = None):
if self.label and self.widget:
   self.label.grid_forget()
   self.widget.grid_forget()
self.label = Label(self.containerFrame, text='head')
self.label.grid(row=1,column=0,sticky=W)
self.widget = self.head.show(self.containerFrame, self.parentWindowInfo)
self.widget.grid(row=1,column=1,sticky=W)
self.lastSelected = 'head'

   def toString(self):
self.createComponents()
return  self.itemXStringList.toString()+' '+ self.head.toString()
   def getValue(self):
self.createComponents()
return (self.itemXStringList.getValue(),self.head.getValue(),)

   def setValue(self, value):
self.createComponents()
if value == None:
   self.itemXStringList.setNone()
   self.head.setNone()
else:
   self.itemXStringList.setValue(value[0])
   self.head.setValue(value[1])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
self.createComponents()
file.write(indent+objName+'= itemXStringListUhead()
')
self.itemXStringList.writeConstructor2File(file, indent, objName+'.itemXStringList', depth, generatingCode)
self.head.writeConstructor2File(file, indent, objName+'.head', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
self.createComponents()
self.itemXStringList.writeValue2File(file, indent, objName+'.itemXStringList', depth, generatingCode)
self.head.writeValue2File(file, indent, objName+'.head', depth, generatingCode)

   def clone(self):
     "Makes an exact copy of itself"
     cloneObject = itemXStringListUhead()
     if self.itemXStringList: cloneObject.itemXStringList = self.itemXStringList.clone()
     if self.head: cloneObject.head = self.head.clone()
     return cloneObject
   def destroy(self):
     "Destroys (i.e. updates) each field"
     cloneObject = itemXStringListUhead()
     if self.itemXStringList: self.itemXStringList.destroy()
     if self.head: self.head.destroy()
     return cloneObject
