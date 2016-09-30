# __ATOM3TypeInfo.py_____________________________________________________

from ATOM3Type           import *
from ASG_TypesMetaModel  import *
from TypeName		 import *
from ATOM3String         import *
from ATOM3String         import *
from ATOM3List           import *

class ATOM3TypeInfo(ATOM3Type):

   def __init__(self, ATOM3instance ):
      ATOM3Type.__init__(self)
      self.ATOM3i = ATOM3instance
      self.Name= ATOM3String()
      self.Name.setValue('Type id')
      self.className= ATOM3String()
      self.className.setValue("Name of the type's class")
      self.Parameters= ATOM3List([1,1,1,0], ATOM3String )
      self.typeModel = ASG_TypesMetaModel(ATOM3instance)
      self.mayEditModel = ATOM3Boolean(None, 1)                               # flag to indicate that the type model can be edited
      self.generatedAttributes = {'Name': ('ATOM3String', ),
                                  'className': ('ATOM3String', ),
                                  'Parameters': ('ATOM3List', )      }
   def show(self, parent, topWindowParent = None):
      ATOM3Type.show(self, parent, topWindowParent)
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text='Name').grid(row=0,column=0,sticky=W)
      self.Name.show(self.containerFrame).grid(row=0,column=1,sticky=W)
      Label(self.containerFrame, text='className').grid(row=1,column=0,sticky=W)
      self.className.show(self.containerFrame).grid(row=1,column=1,sticky=W)
      Label(self.containerFrame, text='Parameters').grid(row=2,column=0,sticky=W)
      self.Parameters.show(self.containerFrame).grid(row=2,column=1,sticky=W)
      Label(self.containerFrame, text='Model').grid(row=3,column=0,sticky=W)
      Button( self.containerFrame, text = 'edit', command =  lambda x=self: x.showTypeModel()).grid(row=3,column=1,sticky=W)

      return self.containerFrame

   def fillTypesInTypesWindow (self, AT3Dialog, ATOM3instance, semanticObject):
      for type in ATOM3instance.types.keys():
           del ATOM3instance.types[type]
      objList = self.ATOM3i.typeList.getValue()
      ATOM3instance.typeList.setValue([]+objList)
      ATOM3instance.fillDictionaryWithTypes() 

   def showTypeModel(self):
      "Shows the type model for editing"
      if self.mayEditModel.getValue()[1] == 1:                     # only edit it if mayEditModel is true
         dial = ATOM3TypeDialog(self.containerFrame, self.typeModel, ATOM3TypeDialog.OPEN, (None, self.fillTypesInTypesWindow))
         if dial.result_ok:
            self.typeModel = dial.myWidget.ASGroot
            # check that the type is a correct one ... (basically, invoke the SAVE constraints)
            res = self.typeModel.preCondition(ASG.SAVE)                                         # evaluate global pre-conditions
            if res:
              self.ATOM3i.constraintViolation(res)
              self.showTypeModel()
              return

            # try the local constraints...
            res = self.typeModel.evaluateLocalPreCondition(ASG.SAVE)                            # evaluate global pre-conditions
            if res:
              self.ATOM3i.constraintViolation(res)
              self.showTypeModel()
              return
            # get the name of the type...
            typeNameNodes = self.typeModel.listNodes['TypeName']
            if typeNameNodes and len(typeNameNodes)>0:			# if we have set the node name...
               typeNameNode = typeNameNodes[0]				# get an instance of the node
               self.Name.setValue(typeNameNode.Name.toString())		# get the type name
               self.className.setValue(typeNameNode.Name.toString())	# set the class name

   def toString(self):
      return self.Name.toString()+" "+self.className.toString()+" "+self.Parameters.toString()

   def getValue(self):
      return (self.Name.getValue(), self.className.getValue(), self.Parameters.getValue(), self.mayEditModel.getValue())

   def setValue(self, value):
      self.Name.setValue(value[0])
      self.className.setValue(value[1])
      self.Parameters.setValue(value[2])
      self.mayEditModel.setValue(value[3])

   def clone(self):
      cloneObject = ATOM3TypeInfo( self.ATOM3i )
      cloneObject.Name = self.Name.clone()
      cloneObject.mode = self.mode
      cloneObject.className    = self.className.clone()
      cloneObject.Parameters   = self.Parameters.clone()
      cloneObject.typeModel    = self.typeModel.clone()
      cloneObject.mayEditModel = self.mayEditModel.clone()

      return cloneObject

   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.Name = other.Name
      self.className = other.className
      self.Parameters = other.Parameters
      self.typeModel  = other.typeModel
      self.mayEditModel = other.mayEditModel

   def destroy(self):
      self.Name.destroy()
      self.className.destroy()
      self.Parameters.destroy()
      self.mayEditModel.destroy()
      # ALSO destroy model!!!
      self.containerFrame = None

   def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+"=ATOM3TypeInfo()\n")
       self.writeValue2File(file, indent, objName)

   def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the value of the object. Must be overriden in children"
       file.write(indent+objName+".setValue("+str(self.getValue())+")\n")

