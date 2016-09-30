# __ File: linkEditor.py ______________________________________________________________________________________________
#  Implements  : class linkEditor
#  Author      : Juan de Lara
#  Description : Dialow window for hyper-links. Links are composed of a Center, and incoming
#                and outgoing lines, with a joint at the end. Centers, joints, and segments can be
#                configured.
#  Modified    : 26 Oct 2001
# ____________________________________________________________________________________________________________________

from tkMessageBox import showinfo
from ASGNode import *

from ATOM3Type import *

from ATOM3Enum             import *
from ATOM3Appearance       import *

#from GraphicEditor import Editor
from GraphicEditor.GraphicEditor import Editor

class linkEditor(ATOM3Type):

   
   # string constants for composing the appearance file names
   firstLink     = "_1stLink"
   firstSegment  = "_1stSegment"
   center        = "_Center"
   secondSegment = "_2ndSegment"
   secondLink    = "_2ndLink"      

   def __init__(self, parent, semObject, className):
      from segment               import *
      from stickylink            import *
      from widthXfillXdecoration import *

      ATOM3Type.__init__(self)
      self.parent    = parent
      self.semObject = semObject
      self.className = className
      
      self.FirstLink= stickylink()
      self.FirstLink.arrow=ATOM3Boolean()
      self.FirstLink.arrow.setValue((' ', 0))
      self.FirstLink.arrow.config = 0
      self.FirstLink.arrowShape1=ATOM3Integer(0)
      self.FirstLink.arrowShape2=ATOM3Integer(0)
      self.FirstLink.arrowShape3=ATOM3Integer(0)
      self.FirstLink.decoration=ATOM3Appearance()
      self.FirstLink.decoration.setValue( (className+self.firstLink, self.semObject))
      
      self.FirstSegment= widthXfillXdecoration()
      self.FirstSegment.width=ATOM3Integer(0)
      self.FirstSegment.fill=ATOM3String('')
      self.FirstSegment.decoration=ATOM3Appearance()
      self.FirstSegment.decoration.setValue( (className+self.firstSegment, self.semObject))
      
      self.Center=ATOM3Appearance()
      self.Center.setValue( (className+self.center, self.semObject))
      
      self.SecondSegment= widthXfillXdecoration()
      self.SecondSegment.width=ATOM3Integer(0)
      self.SecondSegment.fill=ATOM3String('')
      self.SecondSegment.decoration=ATOM3Appearance()
      self.SecondSegment.decoration.setValue( (className+self.secondSegment, self.semObject))
      
      self.SecondLink= stickylink()
      self.SecondLink.arrow=ATOM3Boolean()
      self.SecondLink.arrow.setValue((' ', 0))
      self.SecondLink.arrow.config = 0
      self.SecondLink.arrowShape1=ATOM3Integer(0)
      self.SecondLink.arrowShape2=ATOM3Integer(0)
      self.SecondLink.arrowShape3=ATOM3Integer(0)
      self.SecondLink.decoration=ATOM3Appearance()
      self.SecondLink.decoration.setValue( (className+self.secondLink, self.semObject))
      
      self.generatedAttributes = {'FirstLink': ('ATOM3Enum', ),
                                  'FirstSegment': ('ATOM3segment', ),
                                  'Center': ('ATOM3Appearance', ),
                                  'SecondSegment': ('ATOM3segment', ),
                                  'SecondLink': ('ATOM3joint', )      }
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      
      # ------------------------ First Link ICON -------------------------
      Label(self.containerFrame, text='FirstLink').grid(row=0,column=0,sticky=W)
      Button( self.containerFrame, text = 'edit', command =  lambda x=self : 
        ATOM3TypeDialog(x.containerFrame, x.FirstLink)).grid(row=0,column=1,sticky=W)

      
      # ------------------------ First Segement ICON -------------------------
      Label(self.containerFrame, text='FirstSegment').grid(row=1,column=0,sticky=W)
      Button( self.containerFrame, text = 'edit', command =  lambda x=self : 
        ATOM3TypeDialog(x.containerFrame, x.FirstSegment)).grid(row=1,column=1,sticky=W)

      # ----------------------------- CENTER ICON ----------------------------      
      Label(self.containerFrame, text='Center').grid(row=2,column=0,sticky=W)
      self.Center.show(self.containerFrame, parentWindowInfo).grid(row=2,column=1,sticky=W)      
    
              
      # ------------------------ Second Segement ICON ------------------------
      Label(self.containerFrame, text='SecondSegment').grid(row=3,column=0,sticky=W)
      Button( self.containerFrame, text = 'edit', command =  lambda x=self : 
        ATOM3TypeDialog(x.containerFrame, x.SecondSegment)).grid(row=3,column=1,sticky=W)

      # -------------------------- Second Link ICON --------------------------
      Label(self.containerFrame, text='SecondLink').grid(row=4,column=0,sticky=W)
      Button( self.containerFrame, text = 'edit', command =  lambda x=self : 
            ATOM3TypeDialog(x.containerFrame, x.SecondLink)).grid(row=4,column=1,sticky=W)


#================================================================================
#      Allow for non-visual links, such as insideness relations       
#================================================================================
      def handler( event=None, self=self ):
        self.semObject.isGraphObjectVisual = self.isGraphObjectVisualVar.get()
      Label(self.containerFrame, text='Is visual?').grid(row=5,column=0,sticky=W)
      self.isGraphObjectVisualVar = BooleanVar()
      if(self.semObject):
        self.isGraphObjectVisualVar.set( self.semObject.isGraphObjectVisual )
      else:
        self.isGraphObjectVisualVar.set(True)
      self.chkEntry = Checkbutton(self.containerFrame, 
                                  variable = self.isGraphObjectVisualVar, 
                                  command=handler )
      self.chkEntry.grid(row=5,column=1,sticky=W) 
      
      def handler(event=None):
        showinfo('Visual relationship?', 
                 'If you want the relationship to have no visual appearence,'
                 + ' uncheck this box.\nAll the other visual arrow attributes'
                 + ' will then be ignored.')
      b = Button(self.containerFrame, text='Help', command=handler)
      b.grid(row=5,column=2,sticky=W) 
      
#================================================================================
#      Allow for hieararchical containment relationships 
#      See See HierarchicalASGNode.py for more info
#================================================================================
      def handler(event=None, self=self):
        self.semObject._setHierarchicalLink(self.isHierarchicalVar.get())
      Label(self.containerFrame, text='Is hierarchical?').grid(row=6, column=0, sticky=W)
      self.isHierarchicalVar = BooleanVar()
      if(self.semObject):
        self.isHierarchicalVar.set(self.semObject.isHierarchicalLink())
      else:
        self.isHierarchicalVar.set(False)
      self.chkEntry = Checkbutton(self.containerFrame, 
                                  variable = self.isHierarchicalVar, 
                                  command=handler)
      self.chkEntry.grid(row=6, column=1, sticky=W) 
      
      def handler(event=None):
        showinfo('Hierarchical Relationship?', 
                 'If you want to enable automatic hierarchical tracking for this'
                 + ' relationship, check the box.\nYou may also want to make'
                 + ' this an invisible relationship.\n\nThe following accessor'
                 + ' methods are available on semantic entities'
                 + ' (not relations):\n getHierChildren(), getAllHierChildren()'
                 + ' and getHierParent()\n'
                 + 'These methods are implemented in HierarchicalASGNode.py')
      b = Button(self.containerFrame, text='Help', command=handler)
      b.grid(row=6, column=2, sticky=W) 
      return self.containerFrame

   def toString(self, maxWide = None, maxLines = None ):
      rs = self.FirstLink.toString()+' '+self.FirstSegment.toString()+' '+self.Center.toString()+' '+self.SecondSegment.toString()+' '+self.SecondLink.toString()
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs


   def getValue(self):
      return (self.FirstLink.getValue(),self.FirstSegment.getValue(),self.Center.getValue(),self.SecondSegment.getValue(),self.SecondLink.getValue(),)

   def setValue(self, value):
      self.FirstLink.setValue(value[0])
      self.FirstSegment.setValue(value[1])
      self.Center.setValue(value[2])
      self.SecondSegment.setValue(value[3])
      self.SecondLink.setValue(value[4])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
      if "." in objName:
          objectName = objName[:string.rfind( objName, "." )]
      else:
          objectName = objName
      file.write(indent+objName+'=linkEditor(self,'+objectName+'.semObject, "'+self.className+'")\n')
      
      # Only if this is a visual link (as opposed to an insideness relation)
      if( not self.semObject 
         or ( self.semObject and self.semObject.isGraphObjectVisual ) ):      
        self.FirstLink.writeConstructor2File(file, indent, objName+'.FirstLink', depth, generatingCode)
        self.FirstSegment.writeConstructor2File(file, indent, objName+'.FirstSegment', depth, generatingCode)
        self.Center.writeConstructor2File(file, indent, objName+'.Center', depth, generatingCode)
        self.SecondSegment.writeConstructor2File(file, indent, objName+'.SecondSegment', depth, generatingCode)
        self.SecondLink.writeConstructor2File(file, indent, objName+'.SecondLink', depth, generatingCode)
        self.correctSemObjects(file, indent, objName)
      else:
        file.write(indent+'# This is a non-visual link\n' )

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"
            
      self.FirstLink.writeValue2File(file, indent, objName+'.FirstLink', depth, generatingCode)
      self.FirstSegment.writeValue2File(file, indent, objName+'.FirstSegment', depth, generatingCode)
      self.Center.writeValue2File(file, indent, objName+'.Center', depth, generatingCode)
      self.SecondSegment.writeValue2File(file, indent, objName+'.SecondSegment', depth, generatingCode)
      self.SecondLink.writeValue2File(file, indent, objName+'.SecondLink', depth, generatingCode)
      self.correctSemObjects(file, indent, objName)

   def correctSemObjects(self, file, indent, objName):
      "corrects the attribute semObjects of the ATOM3appearance attributes"
      if "." in objName:
          objectName = objName[:string.rfind( objName, "." )]
      else:
          objectName = objName
      file.write(indent+objName+'.FirstLink.decoration.semObject='+objectName+'.semObject\n')
      file.write(indent+objName+'.FirstSegment.decoration.semObject='+objectName+'.semObject\n')
      file.write(indent+objName+'.Center.semObject='+objectName+'.semObject\n')
      file.write(indent+objName+'.SecondSegment.decoration.semObject='+objectName+'.semObject\n')
      file.write(indent+objName+'.SecondLink.decoration.semObject='+objectName+'.semObject\n')

   def invalid(self):
      return self.FirstLink.invalid() or self.FirstSegment.invalid() or self.Center.invalid() or self.SecondSegment.invalid() or self.SecondLink.invalid() 

   def clone(self):
      cloneObject = linkEditor( self.parent, self.semObject, self.className )
      cloneObject.FirstLink = self.FirstLink.clone()
      cloneObject.FirstSegment = self.FirstSegment.clone()
      cloneObject.Center = self.Center.clone()
      cloneObject.SecondSegment = self.SecondSegment.clone()
      cloneObject.SecondLink = self.SecondLink.clone()
      return cloneObject

   def copy(self, other):      
      ATOM3Type.copy(self, other)
      self.FirstLink = other.FirstLink
      self.FirstSegment = other.FirstSegment
      self.Center = other.Center
      self.SecondSegment = other.SecondSegment
      self.SecondLink = other.SecondLink

   def destroy(self):
      self.FirstLink.destroy()
      self.FirstSegment.destroy()
      self.Center.destroy()
      self.SecondSegment.destroy()
      self.SecondLink.destroy()
      self.containerFrame = None
   def cardinalityCheck(self, selfPosition):
      return None
   def checkConnectedObjectType(self, selfPosition):
      if selfPosition == 'SOURCE':
         last=self.out_connections_[len(self.out_connections_)-1]
         return ('Incorrect connection to ', last.getClass())
      else:
         last=self.in_connections_[len(self.in_connections_)-1]
         return ('Incorrect connection to ', last.getClass())
      return None
   def preCondition (self, actionID, * params):
      if self.graphObject_:
         return self.graphObject_.preCondition(actionID, params)
      else: return None
   def postCondition (self, actionID, * params):
      if actionID == self.CONNECT:
         res = self.checkConnectedObjectType(params[0])
         if res: return res
      if self.graphObject_:
         return self.graphObject_.postCondition(actionID, params)
      else: return None

   def updateGraphicalFile(self, newClassName):
      "if class name has changed, update graphical file of each appearance..."
      if self.className != newClassName:
         self.className = newClassName
         self.FirstLink.decoration.updateGraphicalFile(newClassName+self.firstLink)
         self.FirstSegment.decoration.updateGraphicalFile(newClassName+self.firstSegment)
         self.Center.updateGraphicalFile(newClassName+self.center)
         self.SecondLink.decoration.updateGraphicalFile(newClassName+self.secondLink)
         self.SecondSegment.decoration.updateGraphicalFile(newClassName+self.secondSegment)

