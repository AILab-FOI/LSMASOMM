from Tkinter import *
from ATOM3Type import *
from ATOM3String import *
from ATOM3String import *
class TextUImage (ATOM3Type):
   def __init__(self):
     ATOM3Type.__init__(self)
     self.optMenu = None
     self.selected= None
     self.lastSelected= None
     self.Text= None
     self.Image= None

   def createComponents(self):
     if not self.Text:
        self.Text=ATOM3String('')
     if not self.Image:
        self.Image=ATOM3String('')

   def show(self, parent, parentWindowInfo=None):
     ATOM3Type.show(self, parent, parentWindowInfo)
     self.createComponents()
     self.showParent = parent
     self.parentWindowInfo = parentWindowInfo
     self.selected = StringVar()
     if not self.lastSelected:
        self.selected.set('Text')
     else:
        self.selected.set(self.lastSelected)
     self.label = None
     self.widget = None
     self.containerFrame = Frame(parent)
     Label(self.containerFrame, text='Select Attribute').grid(row=0,column=0,sticky=W)
     self.optMenu = OptionMenu(self.containerFrame, self.selected,'Text','Image')
     self.selected.trace_variable( 'w', self.valueChanged)
     self.optMenu.grid(row=0,column=1,sticky=W)
     if self.lastSelected == 'Text':
           self.destroyAllBut(self.Text)
           self.showText(self.showParent, self.parentWindowInfo)
     if self.lastSelected == 'Image':
           self.destroyAllBut(self.Image)
           self.showImage(self.showParent, self.parentWindowInfo)
     return self.containerFrame

   def valueChanged(self, param1, param2, param3):
     value = self.selected.get()
     if value == 'Text':
        if self.lastSelected != 'Text':
           self.destroyAllBut(self.Text)
           self.showText(self.showParent, self.parentWindowInfo)
     if value == 'Image':
        if self.lastSelected != 'Image':
           self.destroyAllBut(self.Image)
           self.showImage(self.showParent, self.parentWindowInfo)
   def destroyAllBut(self, survivor):
     if survivor != self.Text:
        self.Text.destroy()
     if survivor != self.Image:
        self.Image.destroy()

   def showText(self, parent, parentWindow = None):
     if self.label and self.widget:
        self.label.grid_forget()
        self.widget.grid_forget()
     self.label = Label(self.containerFrame, text='Text')
     self.label.grid(row=1,column=0,sticky=W)
     self.widget = self.Text.show(self.containerFrame, self.parentWindowInfo)
     self.widget.grid(row=1,column=1,sticky=W)
     self.lastSelected = 'Text'

   def showImage(self, parent, parentWindow = None):
     if self.label and self.widget:
        self.label.grid_forget()
        self.widget.grid_forget()
     self.label = Label(self.containerFrame, text='Image')
     self.label.grid(row=1,column=0,sticky=W)
     self.widget = self.Image.show(self.containerFrame, self.parentWindowInfo)
     self.widget.grid(row=1,column=1,sticky=W)
     self.lastSelected = 'Image'

   def toString(self, fils = 25, cols = 5):
     self.createComponents()
     if self.selected:
        value = self.selected.get()
     elif self.lastSelected:
        value = self.lastSelected
     else:
        value = None
     if value == 'Text':
        return self.Text.toString(fils, cols)
     elif value == 'Image':
        return self.Image.toString(fils, cols)
     return ''

   def getValue(self):
     self.createComponents()
     return (self.Text.getValue(),self.Image.getValue(),)

   def setValue(self, value):
     self.createComponents()
     if value == None:
        self.Text.setNone()
        self.Image.setNone()
     else:
        self.Text.setValue(value[0])
        self.Image.setValue(value[1])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
     self.createComponents()
     file.write(indent+objName+'= TextUImage()\n')
     self.Text.writeConstructor2File(file, indent, objName+'.Text', depth, generatingCode)
     self.Image.writeConstructor2File(file, indent, objName+'.Image', depth, generatingCode)
     if self.lastSelected:
        file.write(indent+objName+'.lastSelected= "'+self.lastSelected+'"\n')

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
     self.createComponents()
     self.Text.writeValue2File(file, indent, objName+'.Text', depth, generatingCode)
     self.Image.writeValue2File(file, indent, objName+'.Image', depth, generatingCode)
     if self.lastSelected:
        file.write(indent+objName+'.lastSelected= "'+self.lastSelected+'"\n')

   def clone(self):
     "Makes an exact copy of itself"
     cloneObject = TextUImage()
     if self.Text: cloneObject.Text = self.Text.clone()
     if self.Image: cloneObject.Image = self.Image.clone()
     cloneObject.lastSelected = self.lastSelected
     return cloneObject
   def copy(self, other):
     "Copies the content of other into itself"
     ATOM3Type.copy(self, other)
     self.Text = other.Text
     self.Image = other.Image
     ASGNode.copy(self,other)
   def destroy(self):
     "Destroys (i.e. updates) each field"
     if self.Text: self.Text.destroy()
     if self.Image: self.Image.destroy()


