# __ASG_Buttons.py_____________________________________________________
from ASG import *
from ATOM3Type       import *
from ATOM3String import *
from ATOM3Integer import *
class ASG_Buttons(ASG, ATOM3Type):

   def __init__(self, parent= None, ASGroot = None):
      ASG.__init__(self, 'Buttons', ASGroot, ['ASG_Buttons' ,'ButtonConfig'])

      ATOM3Type.__init__(self)
      self.parent = parent
      self.Formalism_Name=ATOM3String('')
      self.RowSize=ATOM3Integer(0)
      self.Formalism_File=ATOM3String('')
      self.generatedAttributes = {'Formalism_Name': ('ATOM3String', ),
                                  'RowSize': ('ATOM3Integer', ),
                                  'Formalism_File': ('ATOM3String', )      }
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text='Formalism_Name').grid(row=0,column=0,sticky=W)
      self.Formalism_Name.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'Formalism_Name', 0, 2)
      Label(self.containerFrame, text='RowSize').grid(row=1,column=0,sticky=W)
      self.RowSize.show(self.containerFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'RowSize', 1, 2)
      Label(self.containerFrame, text='Formalism_File').grid(row=2,column=0,sticky=W)
      self.Formalism_File.show(self.containerFrame, parentWindowInfo).grid(row=2,column=1,sticky=W)
      ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, 'Formalism_File', 2, 2)
      #from ATOM3 import *
      #a = ATOM3 (parentWindowInfo , 'Buttons')
      #a.grid(row=3,column=0, columnspan = 2, sticky=W)
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      rs = self.Formalism_Name.toString()+' '+self.RowSize.toString()+' '+self.Formalism_File.toString()
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs


   def getValue(self):
      return (self.Formalism_Name.getValue(),self.RowSize.getValue(),self.Formalism_File.getValue(),)

   def setValue(self, value):
      self.Formalism_Name.setValue(value[0])
      self.RowSize.setValue(value[1])
      self.Formalism_File.setValue(value[2])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
      self.Formalism_Name.writeConstructor2File(file, indent, objName+'.Formalism_Name', depth, generatingCode)
      self.RowSize.writeConstructor2File(file, indent, objName+'.RowSize', depth, generatingCode)
      self.Formalism_File.writeConstructor2File(file, indent, objName+'.Formalism_File', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"
      self.Formalism_Name.writeValue2File(file, indent, objName+'.Formalism_Name', depth, generatingCode)
      self.RowSize.writeValue2File(file, indent, objName+'.RowSize', depth, generatingCode)
      self.Formalism_File.writeValue2File(file, indent, objName+'.Formalism_File', depth, generatingCode)

   def invalid(self):
      ASGNode.GGcheckSetNone(self)
      return self.Formalism_Name.invalid() or self.RowSize.invalid() or self.Formalism_File.invalid() 

   def clone(self):
      return self
      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.Formalism_Name = other.Formalism_Name
      self.RowSize = other.RowSize
      self.Formalism_File = other.Formalism_File
   def destroy(self):
      ASGNode.GGcheckSetNone(self)
      self.destroyNodes()
      self.Formalism_Name.destroy()
      self.RowSize.destroy()
      self.Formalism_File.destroy()
      self.containerFrame = None
   def open(self, parent, topWindowParent):
       from ATOM3 import *
       a = ATOM3(topWindowParent, 'Buttons', 0, 1, self)
       #self.writeContents(a)
       return a
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None


