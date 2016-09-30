# __Options.py_____________________________________________________
from ASGNode import *

from ATOM3Type import *

from ATOM3Enum import *
from ATOM3String import *
from ATOM3List import *

class Options(ASGNode, ATOM3Type):
  
   def __init__(self, parent):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.parent = parent
      self.GenerateGraphics=ATOM3Enum(['Yes', 'No'], None, 0)
            
      self.InitialMetaModel=ATOM3String('ERmetaMetaModel')
      self.PathDirectories=ATOM3List([1,1,1,None], ATOM3String )
      self.codeGenDir=ATOM3String('work')
      self.GGforCodeGen=ATOM3String('createButtons')
      self.generatedAttributes = {'Generate Graphics': ('ATOM3Enum', ),
                                  'Use Extra Consoles': ('ATOM3Enum', ),
                                  'Start Fullscreen': ('ATOM3Enum', ),
                                  'Initial Meta-Model': ('ATOM3String', ),
                                  'Path Directories': ('ATOM3List', ATOM3String),
                                  'codeGenDir': ('ATOM3String', ),
                                  'GGforCodeGen': ('ATOM3String', )}
      
                                  
                                  
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      
      i = 0
      
      Label(self.containerFrame, 
            text='Changes take effect only after AToM3 is restarted',
            font='default 14',
            ).grid(row=i,column=0,columnspan=6,sticky=EW)
      i+=1
      Label(self.containerFrame, text='Generate Graphics').grid(row=i,column=0,sticky=W)
      self.GenerateGraphics.show(self.containerFrame, parentWindowInfo).grid(row=i,column=1,sticky=W)
   
      Label(self.containerFrame, text='Valid Models Include:',            
            ).grid(row=i,column=0,sticky=W)      

      modelList = ['ActivityDiagram', 'BaseModel', 'BlockDiagram', 'Buttons',
                    'CBD4OOCSMP', 'CTL', 'ClassDiagrams', 'DCharts', 
                    'EntityRelationship', 'EventGraphs', 'FiniteStateAutomata', 
                    'GPSSMetaModel_All_Buttons', 'OOCSMP', 'PetriNets', 
                    'ProcessInteraction', 'ReachGraph', 'SequenceDiagram', 
                    'StateChart', 'TAutomata', 'TypesMetaModel']
      modelList.sort()
      string = ""
      for model in modelList:
        string += model + " , "

      t=Text(self.containerFrame,height=4)
      t.insert( END,string )
      t.grid(row=i,column=1,columnspan=6,sticky=EW)
      i+=2
      Label(self.containerFrame, text='Initial Meta-Model').grid(row=i,column=0,sticky=W)
      self.InitialMetaModel.show(self.containerFrame, parentWindowInfo).grid(row=i,column=1,sticky=W)
      i+=1
      Label(self.containerFrame, text='Graph Grammar for Code Gen.').grid(row=i,column=0,sticky=W)
      self.GGforCodeGen.show(self.containerFrame, parentWindowInfo).grid(row=i,column=1,sticky=W)     
      i+=1
      Label(self.containerFrame, text='Dir.for Code Generation').grid(row=i,column=0,sticky=W)
      self.codeGenDir.show(self.containerFrame, parentWindowInfo).grid(row=i,column=1,sticky=W)
      i+=1
      Label(self.containerFrame, text='Path Directories').grid(row=i,column=0,sticky=W)
      self.PathDirectories.show(self.containerFrame, parentWindowInfo).grid(row=i,column=1,sticky=W)

      

      return self.containerFrame

   def toString(self):
      return self.GenerateGraphics.toString()+' '+self.InitialMetaModel.toString()+' '+self.codeGenDir.toString()+' '+self.PathDirectories.toString()+' '+self.GGforCodeGen.toString()

   def getValue(self):
      return (self.GenerateGraphics.getValue(),self.InitialMetaModel.getValue(), self.codeGenDir.getValue(), self.PathDirectories.getValue(), self.GGforCodeGen.getValue())

   def setValue(self, value):
      self.GenerateGraphics.setValue(value[0])
      self.InitialMetaModel.setValue(value[1])
      self.codeGenDir.setValue(value[2])
      self.PathDirectories.setValue(value[3])
      self.GGforCodeGen.setValue(value[2])

   def clone(self):
      cloneObject = Options( self.parent )
      cloneObject.GenerateGraphics = self.GenerateGraphics.clone()
      cloneObject.InitialMetaModel = self.InitialMetaModel.clone()
      cloneObject.codeGenDir = self.codeGenDir.clone()      
      cloneObject.PathDirectories = self.PathDirectories.clone()
      cloneObject.GGforCodeGen = self.GGforCodeGen.clone()
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.GenerateGraphics = other.GenerateGraphics
      self.InitialMetaModel = other.InitialMetaModel
      self.codeGenDir = other.codeGenDir
      self.PathDirectories = other.PathDirectories
      self.GGforCodeGen = other.GGforCodeGen
      ASGNode.copy(self, other)

   def destroy(self):
      self.GenerateGraphics.destroy()
      self.InitialMetaModel.destroy()
      self.codeGenDir.destroy()
      self.PathDirectories.destroy()
      self.GGforCodeGen.destroy()
      self.containerFrame = None
      
   def preCondition (self, actionID):
      return None
   def postCondition (self, actionID):
      return None

   def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       self.GenerateGraphics.writeConstructor2File( file, indent, objName+".GenerateGraphics", depth, generatingCode)
       self.InitialMetaModel.writeConstructor2File( file, indent, objName+".InitialMetaModel", depth, generatingCode)
       self.codeGenDir.writeConstructor2File( file, indent, objName+".codeGenDir", depth, generatingCode)
       self.PathDirectories.writeConstructor2File( file, indent, objName+".PathDirectories", depth, generatingCode)
       self.GGforCodeGen.writeConstructor2File( file, indent, objName+".GGforCodeGen", depth, generatingCode)

   def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       self.GenerateGraphics.writeValue2File( file, indent, objName+".GenerateGraphics", depth, generatingCode)
       self.InitialMetaModel.writeValue2File( file, indent, objName+".InitialMetaModel", depth, generatingCode)
       self.codeGenDir.writeValue2File( file, indent, objName+".codeGenDir", depth, generatingCode)
       self.PathDirectories.writeValue2File( file, indent, objName+".PathDirectories", depth, generatingCode)
       self.GGforCodeGen.writeValue2File( file, indent, objName+".GGforCodeGen", depth, generatingCode)

   def invalid(self):
       """checks if the directories in the list (an the code gen text) are valid (returns None if valid, A string
          with the error if valid)"""
       if not os.path.exists(self.codeGenDir.toString()): return "Code Generation Directory ("+self.codeGenDir.toString()+") is not valid"

       direcs = self.PathDirectories.getValue()
       for adir in direcs:
          if not os.path.exists(adir.toString()):
             return "Directory "+adir.toString()+" is not valid."
       return None

