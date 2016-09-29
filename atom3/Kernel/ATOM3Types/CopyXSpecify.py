from Tkinter import *
import Dialog

from ATOM3Type import *
from ATOM3Boolean import *
from ATOM3Constraint import *


class CopyXSpecify (ATOM3Type):
   def __init__(self):
      ATOM3Type.__init__(self)
      self.Copy= None
      self.Specify= None
      
      self.isUsingSpecifyCode = IntVar()  
      self.isUsingSpecifyCode.set(0)

   def createComponents(self):
      if not self.Copy:
         self.Copy=ATOM3Boolean()
         self.Copy.setValue(('Copy from LHS', 1))
         self.Copy.config = 0
      if not self.Specify:
         self.initilizeSpecifyCode()

   def show(self, parent, parentWindowInfo=None):
      self.createComponents()
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      
#================================================================================
#     Copy
#================================================================================
      Label(self.containerFrame, text='Copy').grid(row=0,column=0,sticky=W)
      self.Copy.show(self.containerFrame, parentWindowInfo).grid(row=0,column=1,sticky=W)
      
#================================================================================
#     Specify
#================================================================================
      Label(self.containerFrame, text='Specify').grid(row=1,column=0,sticky=W)      
      self.specifyButton = Button( self.containerFrame, text = 'Specify code', 
              command =  lambda x=self : 
              ATOM3TypeDialog(x.containerFrame, x.Specify))
      self.specifyButton.grid(row=1,column=1,sticky=W)
              
      Checkbutton(self.containerFrame, text="Enabled?", 
                    variable=self.isUsingSpecifyCode, 
                    command=self.toggleSpecifyCode
                    ).grid(row=1,column=2,sticky=W)
      
      if(self.isSpecifyCodePresent()):
        self.isUsingSpecifyCode.set(1)
        self.specifyButton.config(state="normal")
      else:
        self.specifyButton.config(state="disabled")
        self.initilizeSpecifyCode()      
              
      return self.containerFrame
      
      
      
   def isSpecifyCodePresent(self):
     """ Check if specify code is really... specified """
     if(not self.Specify):
       return False
     code = self.Specify.getValue()[4]
     if(not code):
       return False
     temp = code.replace('\n', '')
     temp = temp.replace(' ', '')
     temp = temp.replace('\t', '')
     if(temp == ''):
       return False
     return True
     
     
   def initilizeSpecifyCode(self, value=None):
     self.Specify=ATOM3Constraint()                  
     self.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), 
                            (['PREcondition', 'POSTcondition'], 1), 
                            (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 
                              'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 
                              'DROP', 'MOVE OBJECT'], 
                              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
                               value))
     
     
      
   def toggleSpecifyCode(self, event=None):     
     """ Use specify code or not? """
     # Was the specify code empty already?
     if(self.Specify and self.Specify.getValue()[4] != None):
       dialog = Dialog.Dialog(None, {'title': 'Delete specify code?',
                    'text': 'If you press Okay, your specify code will be lost',
                    'bitmap': 'warning',
                    'default': 1,
                    'strings': ('Okay','Cancel')})
       if(dialog.num == 1):
         self.isUsingSpecifyCode.set(1)
         self.specifyButton.config(state="normal")
         return
           
       self.specifyButton.config(state="disabled")
       templateCode = None
       
     else:
       
       self.specifyButton.config(state="normal")
       templateCode = \
'''# Template for typical GG specify code (specified field is a string)
# See atom3\Kernel\ATOM3Types directory for info on specific types
      
# return self.getMatched(graphID, self.LHS.nodeWithLabel(1)).Name.getValue()

# "self.LHS.nodeWithLabel(1)" gets the node with GG label 1 in the LHS of the GG
# "self.getMatched(graphID, self.LHS.nodeWithLabel(1))" gets node in host graph
# ".Name" will access that node\'s Name attribute, an ATOM3 string object
# ".getValue()" will return the ATOM3 string as a regular Python string
# Finally, a Python string is returned, and becomes the value of the specified
# field

# A more complicated template (specified field is an integer)
  
# # Source loses one car
# sourceNode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
# currentNumCars = sourceNode.num_vehicles.getValue()
# # If source has an infinite supply (infinite_supply = ATOM3 boolean value)
# if(source.infinite_supply.getValueBoolean()): 
#     return currentNumCars
# return currentNumCars - 1

'''
     self.initilizeSpecifyCode(templateCode)
                                         

   def toString(self):
      self.createComponents()
      return  self.Copy.toString()+' '+ self.Specify.toString()
   def getValue(self):
      self.createComponents()
      return (self.Copy.getValue(),self.Specify.getValue(),)

   def setValue(self, value):
      self.createComponents()
      self.Copy.setValue(value[0])
      self.Specify.setValue(value[1])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      self.createComponents()
      self.Copy.writeConstructor2File(file, indent, objName+'.Copy', depth, generatingCode)
      self.Specify.writeConstructor2File(file, indent, objName+'.Specify', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      self.createComponents()
      self.Copy.writeValue2File(file, indent, objName+'.Copy', depth, generatingCode)
      self.Specify.writeValue2File(file, indent, objName+'.Specify', depth, generatingCode)

