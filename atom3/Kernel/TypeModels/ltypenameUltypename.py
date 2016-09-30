from Tkinter import *
from ATOM3Type import *
from ATOM3String import *
from ATOM3String import *
class ltypenameUltypename (ATOM3Type):
   def __init__(self):
     ATOM3Type.__init__(self)
     self.optMenu = None
     self.selected= None
     self.ltypename= None
     self.ltypename= None

   def createComponents(self):
     if not self.ltypename:
        self.ltypename=ATOM3String('')
     if not self.ltypename:
        self.ltypename=ATOM3String('')

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
     self.selected.set('ltypename')
     self.optMenu = OptionMenu(self.containerFrame, self.selected,'ltypename','ltypename')
     self.selected.trace_variable( 'w', self.valueChanged)
     self.optMenu.grid(row=0,column=1,sticky=W)
     return self.containerFrame

   def valueChanged(self, param1, param2, param3):
     value = self.selected.get()
     if value == 'ltypename':
        if self.lastSelected != 'ltypename':
           self.destroyAllBut(self.ltypename)
           self.showltypename(self.showParent, self.parentWindowInfo)
     if value == 'ltypename':
        if self.lastSelected != 'ltypename':
           self.destroyAllBut(self.ltypename)
           self.showltypename(self.showParent, self.parentWindowInfo)
   def destroyAllBut(self, survivor):
     if survivor != self.ltypename:
        self.ltypename.destroy()
     if survivor != self.ltypename:
        self.ltypename.destroy()

   def showltypename(self, parent, parentWindow = None):
     if self.label and self.widget:
        self.label.grid_forget()
        self.widget.grid_forget()
     self.label = Label(self.containerFrame, text='ltypename')
     self.label.grid(row=1,column=0,sticky=W)
     self.widget = self.ltypename.show(self.containerFrame, self.parentWindowInfo)
     self.widget.grid(row=1,column=1,sticky=W)
     self.lastSelected = 'ltypename'

   def showltypename(self, parent, parentWindow = None):
     if self.label and self.widget:
        self.label.grid_forget()
        self.widget.grid_forget()
     self.label = Label(self.containerFrame, text='ltypename')
     self.label.grid(row=1,column=0,sticky=W)
     self.widget = self.ltypename.show(self.containerFrame, self.parentWindowInfo)
     self.widget.grid(row=1,column=1,sticky=W)
     self.lastSelected = 'ltypename'

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
     file.write(indent+objName+'= ltypenameUltypename()\n')
     self.ltypename.writeConstructor2File(file, indent, objName+'.ltypename', depth, generatingCode)
     self.ltypename.writeConstructor2File(file, indent, objName+'.ltypename', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
     self.createComponents()
     self.ltypename.writeValue2File(file, indent, objName+'.ltypename', depth, generatingCode)
     self.ltypename.writeValue2File(file, indent, objName+'.ltypename', depth, generatingCode)

   def clone(self):
     "Makes an exact copy of itself"
     cloneObject = ltypenameUltypename()
     if self.ltypename: cloneObject.ltypename = self.ltypename.clone()
     if self.ltypename: cloneObject.ltypename = self.ltypename.clone()
     return cloneObject
   def destroy(self):
     "Destroys (i.e. updates) each field"
     cloneObject = ltypenameUltypename()
     if self.ltypename: self.ltypename.destroy()
     if self.ltypename: self.ltypename.destroy()
     return cloneObject
