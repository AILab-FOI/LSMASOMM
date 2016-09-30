from Tkinter import *
from ATOM3Type import *
from ATOM3Boolean import *
from ATOM3Enum import *
from ATOM3Integer import *
from ATOM3String import *
from ATOM3Appearance import *
class widthXfillXdecoration (ATOM3Type):
   def __init__(self):
      ATOM3Type.__init__(self)
      self.width= None
      self.fill= None
      self.decoration= None
      self.decoration_Position = None
      self.stipple = None                    # Added (by Hand) 17-10-2002
      self.arrow = None                      # Added (by Hand) 17-10-2002
      self.arrowShape1 = None                # Added (by Hand) 17-10-2002
      self.arrowShape2 = None                # Added (by Hand) 17-10-2002
      self.arrowShape3 = None                # Added (by Hand) 17-10-2002

   def createComponents(self):
      if not self.width:
         self.width=ATOM3Integer(0)
      if not self.fill:
         self.fill=ATOM3String('')


      # This block's been added (by Hand) 17-10-2002
      if not self.stipple:                   
         self.stipple=ATOM3String('')        
      if not self.arrow:
         self.arrow=ATOM3Boolean()
         self.arrow.setValue((' ', 0))
         self.arrow.config = 0
      if not self.arrowShape1:
         self.arrowShape1=ATOM3Integer(0)
      if not self.arrowShape2:
         self.arrowShape2=ATOM3Integer(0)
      if not self.arrowShape3:
         self.arrowShape3=ATOM3Integer(0)
      # END BLOCK. This block's been added (by Hand) 17-10-2002   

      if not self.decoration:
         self.decoration=ATOM3Appearance()
         self.decoration.setValue( ('class0', self))
      if not self.decoration_Position:
         self.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'], 3)

   def show(self, parent, parentWindowInfo=None):
      self.createComponents()
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      Label(self.containerFrame, text='width').grid(row=0,column=0,sticky=W)
      self.width.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      Label(self.containerFrame, text='fill').grid(row=1,column=0,sticky=W)
      self.fill.show(self.containerFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
      
      # BLOCK Added (by Hand) 17-10-2002
      Label(self.containerFrame, text='stipple').grid(row=2,column=0,sticky=W)
      self.stipple.show(self.containerFrame, parentWindowInfo).grid(row=2,column=1,sticky=W)

      Label(self.containerFrame, text='arrow').grid(row=3,column=0,sticky=W)
      self.arrow.show(self.containerFrame, parentWindowInfo).grid(row=3,column=1,sticky=W)
      
      Label(self.containerFrame, text='arrowShape (base to tip)').grid(row=4,column=0,sticky=W)
      self.arrowShape1.show(self.containerFrame, parentWindowInfo).grid(row=4,column=1,sticky=W)
      
      Label(self.containerFrame, text='arrowShape (wing to tip)').grid(row=5,column=0,sticky=W)
      self.arrowShape2.show(self.containerFrame, parentWindowInfo).grid(row=5,column=1,sticky=W)
      
      Label(self.containerFrame, text='arrowShape (wing to base)').grid(row=6,column=0,sticky=W)
      self.arrowShape3.show(self.containerFrame, parentWindowInfo).grid(row=6,column=1,sticky=W)
      # END BLOCK Added (by Hand) 17-10-2002
      
      Label(self.containerFrame, text='decoration').grid(row=7,column=0,sticky=W)
      self.decoration.show(self.containerFrame, parentWindowInfo).grid(row=7,column=1,sticky=W)
          
      Label(self.containerFrame, text='decoration_Position').grid(row=8,column=0,sticky=W)
      self.decoration_Position.show(self.containerFrame, parentWindowInfo).grid(row=8,column=1,sticky=W)

      # Arrow Preview Added by Denis 2005
      dc = Canvas(self.containerFrame,width=200, height=60, bg='light blue')
      itemHandler = dc.create_line(0,30,180,30,arrow='last', 
                                   width=self.width.getValue(),
                                   fill=self.fill.getValue(),
                                   stipple=self.stipple.getValue(),
                                   arrowshape=(   self.arrowShape1.getValue(),
                                                  self.arrowShape2.getValue(),
                                                  self.arrowShape3.getValue()))
      dc.grid( row=10,column=0,columnspan=2,sticky=W)
      
      def handler( dc=dc,itemHandler=itemHandler, event=None):         
        dc.itemconfigure(itemHandler, 
                                   width=self.width.getValue(),
                                   fill=self.fill.getValue(),
                                   stipple=self.stipple.getValue(),
                                   arrowshape=(self.arrowShape1.getValue(),
                                                self.arrowShape2.getValue(),
                                                self.arrowShape3.getValue()))
      self.previewButton = Button( self.containerFrame, bg='dark blue',
                                  fg='white', relief='groove',
                                  text='Refresh Arrow Preview', 
                                  command=handler)
      self.previewButton.grid(row=9,column=0,columnspan=2,sticky=W)

      return self.containerFrame

   def toString(self):
      self.createComponents()
      # Changed (by Hand) 17-10-2002. Added self.stipple
      return  self.width.toString()+' '+ self.fill.toString()+' '+ self.stipple.toString()+' '+self.arrow.toString()+' '+ self.arrowShape1.toString()+' '+ self.arrowShape2.toString()+' '+self.arrowShape3.toString()+' '+self.decoration.toString()+' '+ self.decoration_Position.toString()

   def getValue(self):
      self.createComponents()
      # Changed (by Hand) 17-10-2002. Added self.stipple
      return (self.width.getValue(),self.fill.getValue(),self.stipple.getValue(),
              self.arrow.getValue(),self.arrowShape1.getValue(),self.arrowShape2.getValue(),self.arrowShape3.getValue(),
              self.decoration.getValue(),self.decoration_Position.getValue(),)

   def setValue(self, value):
      self.createComponents()
      if value == None:
         self.width.setNone()
         self.fill.setNone()
         self.stipple.setNone()                 # Changed (by Hand) 17-10-2002. Added self.stipple
         self.arrow.setNone()
         self.arrowShape1.setNone()
         self.arrowShape2.setNone()
         self.arrowShape3.setNone()         
         self.decoration.setNone()
         self.decoration_Position.setNone()
      else:
         self.width.setValue(value[0])
         self.fill.setValue(value[1])
         self.stipple.setValue(value[2])        # Changed (by Hand) 17-10-2002. Added self.stipple
         self.arrow.setValue(value[3])
         self.arrowShape1.setValue(value[4])
         self.arrowShape2.setValue(value[5])
         self.arrowShape3.setValue(value[6])         
         self.decoration.setValue(value[7])
         self.decoration_Position.setValue(value[8])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      self.createComponents()
      file.write(indent+objName+'= widthXfillXdecoration()\n')
      self.width.writeConstructor2File(file, indent, objName+'.width', depth, generatingCode)
      self.fill.writeConstructor2File(file, indent, objName+'.fill', depth, generatingCode)
      self.stipple.writeConstructor2File(file, indent, objName+'.stipple', depth, generatingCode)   # Changed (by Hand) 17-10-2002. Added self.stipple
      self.arrow.writeConstructor2File(file, indent, objName+'.arrow', depth, generatingCode)
      self.arrowShape1.writeConstructor2File(file, indent, objName+'.arrowShape1', depth, generatingCode)
      self.arrowShape2.writeConstructor2File(file, indent, objName+'.arrowShape2', depth, generatingCode)
      self.arrowShape3.writeConstructor2File(file, indent, objName+'.arrowShape3', depth, generatingCode)      
      self.decoration.writeConstructor2File(file, indent, objName+'.decoration', depth, generatingCode)      
      self.decoration_Position.writeConstructor2File(file, indent, objName+'.decoration_Position', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      self.createComponents()
      self.width.writeValue2File(file, indent, objName+'.width', depth, generatingCode)
      self.fill.writeValue2File(file, indent, objName+'.fill', depth, generatingCode)
      self.stipple.writeValue2File(file, indent, objName+'.stipple', depth, generatingCode)   # Changed (by Hand) 17-10-2002. Added self.stipple
      self.arrow.writeValue2File(file, indent, objName+'.arrow', depth, generatingCode)
      self.arrowShape1.writeValue2File(file, indent, objName+'.arrowShape1', depth, generatingCode)
      self.arrowShape2.writeValue2File(file, indent, objName+'.arrowShape2', depth, generatingCode)
      self.arrowShape3.writeValue2File(file, indent, objName+'.arrowShape3', depth, generatingCode)      
      self.decoration.writeValue2File(file, indent, objName+'.decoration', depth, generatingCode)
      self.decoration_Position.writeValue2File(file, indent, objName+'.decoration_Position', depth, generatingCode)

   def clone(self):
     "Makes an exact copy of itself"
     cloneObject = widthXfillXdecoration()
     if self.width: cloneObject.width = self.width.clone()
     if self.fill: cloneObject.fill = self.fill.clone()
     if self.stipple: cloneObject.stipple = self.stipple.clone()   # Changed (by Hand) 17-10-2002. Added self.stipple
     if self.arrow: cloneObject.arrow = self.arrow.clone()
     if self.arrowShape1: cloneObject.arrowShape1 = self.arrowShape1.clone()
     if self.arrowShape2: cloneObject.arrowShape2 = self.arrowShape2.clone()
     if self.arrowShape3: cloneObject.arrowShape3 = self.arrowShape3.clone()     
     if self.decoration: cloneObject.decoration = self.decoration.clone()
     if self.decoration_Position: cloneObject.decoration_Position = self.decoration_Position.clone()
     return cloneObject
   def destroy(self):
     "Destroys (i.e. updates) each field"
     if self.width: self.width.destroy()
     if self.fill: self.fill.destroy()
     if self.stipple: self.stipple.destroy()                      # Changed (by Hand) 17-10-2002. Added self.stipple
     if self.arrow: self.arrow.destroy()
     if self.arrowShape1: self.arrowShape1.destroy()
     if self.arrowShape2: self.arrowShape2.destroy()
     if self.arrowShape3: self.arrowShape3.destroy()     
     if self.decoration: self.decoration.destroy()
     if self.decoration_Position: self.decoration_Position.destroy()

   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.width = other.width
      self.fill = other.fill
      self.stipple = other.stipple                                # Changed (by Hand) 17-10-2002. Added self.stipple
      self.arrow = other.arrow
      self.arrowShape1 = other.arrowShape1
      self.arrowShape2 = other.arrowShape2
      self.arrowShape3 = other.arrowShape3      
      self.decoration = other.decoration
      self.decoration_Position = other.decoration_Position

   def invalid(self):
      # this was missing! (added 15 Jan 2002)
      # Changed (by Hand) 17-10-2002. Added self.stipple 
      if self.width and self.width.invalid(): return 1
      if self.fill and self.fill.invalid(): return 1
      if self.stipple and self.stipple.invalid(): return 1
      if self.arrow and self.arrow.invalid(): return 1
      if self.arrowShape1 and self.arrowShape1.invalid(): return 1
      if self.arrowShape2 and self.arrowShape2.invalid(): return 1
      if self.arrowShape3 and self.arrowShape3.invalid(): return 1
      if self.decoration and self.decoration.invalid(): return 1
      if self.decoration_Position and self.decoration_Position.invalid(): return 1






