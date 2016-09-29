# __ File: GGruleEdit.py ______________________________________________________________
# Implements : class GGruleEdit
# Author     : Juan de Lara
# Description: Window with some widgets to edit a Graph Grammar rule
#              Generated automatically with ATOM3, added some code by hand.
# Modified   :
#   - 21 Oct 2001. Header added
#   - 9 Aug 2002  : TimeDelay attribute added (by hand)
#   - 9 Sept 2002 : SubtypesMatching attribute added.
# ___________________________________________________________________________________________
from ASGNode 		  import *

from ATOM3Type 		  import *

from ATOM3String 	  import *
from ATOM3Integer 	  import *
from ATOM3String 	  import *
from ATOM3String 	  import *
from ATOM3Constraint 	  import *
from ATOM3Constraint 	  import *
from graph_GGruleEdit 	  import *

from Embedded_Images import Embedded_Images


class GGruleEdit(ASGNode, ATOM3Type):

   UNIQUE_RULE_ID = 0

   def __init__(self, parent, ATOM3instance ):
     
      GGruleEdit.UNIQUE_RULE_ID += 1
      self.uniqueRuleID = GGruleEdit.UNIQUE_RULE_ID
     
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.ATOM3instance = ATOM3instance
      self.parent = parent
      self.Name=ATOM3String('rule')
      self.Order=ATOM3Integer(1)
      self.TimeDelay=ATOM3Integer(2)                           # Added 09 Aug. 2002 by JL
      self.SubtypesMatching=ATOM3Boolean(None, 0)              # Added 09 Sept. 2002 by JL

      # get the Meta-Model that is being used currently by the ATOM3 instance

      if(not ATOM3instance.ASGroot):
        raise Exception("Error: No meta-model loaded, please load one before creating a new rule") 
      currMetaModelName = ATOM3instance.ASGroot.getClass()
      exec "from "+currMetaModelName+" import *\n"
      currMetaModel = eval(currMetaModelName)

      """
      Some default code templates:
        
      ACTION
      self.getMatched(graphID, self.LHS.nodeWithLabel(1)).vehiclesPNPlaceGenerated=True
      
      CONDITION
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return not node.vehiclesPNPlaceGenerated
      """

      self.LHS=currMetaModel(ATOM3instance, None)
      self.RHS=currMetaModel(ATOM3instance, None)
      self.LHS.isInsideGraphGrammar = True
      self.RHS.isInsideGraphGrammar = True
      
      self.Condition=ATOM3Constraint()     
      self.Condition.setValue(('condition', (['Python', 'OCL'], 0), 
          (['PREcondition', 'POSTcondition'], 1), 
          (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 
            'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
             'return 1\n'))
      self.Action=ATOM3Constraint()
      self.Action.setValue(('action', (['Python', 'OCL'], 0), 
          (['PREcondition', 'POSTcondition'], 1), 
          (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 
            'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
             None))
             
      self.generatedAttributes = {'Name': ('ATOM3String', ),
                                  'Order': ('ATOM3Integer', ),
                                  'TimeDelay': ('ATOM3Integer', ),            # Added 09 Aug. 2002 by JL
                                  'SubtypesMatching': ('ATOM3Boolean', ),     # Added 09 Sep. 2002 by JL
                                  'LHS': ('ATOM3String', ),
                                  'RHS': ('ATOM3String', ),
                                  'Condition': ('ATOM3Constraint', ),
                                  'Action': ('ATOM3Constraint', )      }

      self.postscriptHack = None
      
      self.isUsingAction = IntVar()  
      self.isUsingAction.set(0)
      self.isUsingCondition = IntVar()                                
      self.isUsingCondition.set(0)

   def setGGEditLHS(self, AT3Dialog, ATOM3instance, semanticObject):
      ATOM3instance.editGGLabel = self.INLHS
      ATOM3instance.reDrawGGLabels()
      ATOM3instance.addCopyFromLHSButton(self) # Adds a generic link button
      
      self.LHSimage = Embedded_Images().getLHS()
      ATOM3instance.atom3MenuButton.configure(image=self.LHSimage)
      
      # Hack: allows you to force a postaction trigger
      ASGroot = ATOM3instance.ASGroot
      for nodeType in ASGroot.listNodes.keys():
        for node in ASGroot.listNodes[nodeType]:
          node.postAction(ASGroot.CONNECT, None)
      
      if( self.postscriptHack ):        
        # Store bounding box in "self.postscriptHack", could be None
        self.postscriptHack = ATOM3instance.postscriptBox.generatePostscript( 
                              autoSaveToFileName=self.postscriptHack)

   def setGGEditRHS(self, AT3Dialog, ATOM3instance, semanticObject):
      ATOM3instance.editGGLabel = self.INRHS
      ATOM3instance.reDrawGGLabels()
      ATOM3instance.addCopyFromLHSButton(self)
      
      self.RHSimage = Embedded_Images().getRHS()
      ATOM3instance.atom3MenuButton.configure(image=self.RHSimage)
      
      # Hack: allows you to force a postaction trigger
      ASGroot = ATOM3instance.ASGroot
      for nodeType in ASGroot.listNodes.keys():
        for node in ASGroot.listNodes[nodeType]:
          node.postAction(ASGroot.CONNECT, None)
      
      if( self.postscriptHack ):
        # Store bounding box in "self.postscriptHack", could be None
        self.postscriptHack = ATOM3instance.postscriptBox.generatePostscript( 
                              autoSaveToFileName=self.postscriptHack)




   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)

#===============================================================================
#Top Frame
#===============================================================================
      self.topFrame = Frame(self.containerFrame)

      Label(self.topFrame, text='Name (Python variable syntax required)').grid(row=1,column=0,sticky=W)
      self.Name.show(self.topFrame, parentWindowInfo).grid(row=1,column=1,sticky=W)
      Label(self.topFrame, text='Order').grid(row=2,column=0,sticky=W)
      self.Order.show(self.topFrame, parentWindowInfo).grid(row=2,column=1,sticky=W)
      
      Label(self.topFrame, text='TimeDelay').grid(row=3,column=0,sticky=W)        # Added 09 Aug. 2002 by JL
      self.TimeDelay.show(self.topFrame, parentWindowInfo).grid(row=3,column=1,sticky=W)

      Label(self.topFrame, text='Subtypes Matching (if rule matches A then it also matches B if B has all attributes in A)').grid(row=4,column=0,sticky=W)        # Added 09 Sep. 2002 by JL
      self.SubtypesMatching.show(self.topFrame, parentWindowInfo).grid(row=4,column=1,sticky=W)     
      
      
      # Condition
      Label(self.topFrame, text='Condition').grid(row=7,column=0,sticky=W)
      self.conditionButton = Button( self.topFrame, text = 'Edit', 
             command =  lambda x=self : ATOM3TypeDialog(x.topFrame, 
                                                        x.Condition))
      self.conditionButton.grid(row=7,column=1,sticky=W)
      
      Checkbutton(self.topFrame, text="Enabled?", 
                    variable=self.isUsingCondition, 
                    command=self.toggleCondition
                    ).grid(row=7,column=2,sticky=W)
      
      if(self.Condition.getValue()[4] != 'return 1\n'):
        self.isUsingCondition.set(1)
        self.conditionButton.config(state="normal")
      else:
        self.conditionButton.config(state="disabled")
        
        
      # Action
      Label(self.topFrame, text='Action').grid(row=8,column=0,sticky=W)
      self.actionButton = Button( self.topFrame, text = 'Edit', 
             command =  lambda x=self : ATOM3TypeDialog(x.topFrame, 
                                                        x.Action))
      self.actionButton.grid(row=8,column=1,sticky=W)
      
      Checkbutton(self.topFrame, text="Enabled?", 
                    variable=self.isUsingAction, 
                    command=self.toggleAction
                    ).grid(row=8,column=2,sticky=W)
                    
      if(self.Action.getValue()[4] != None):
        self.isUsingAction.set(1)
        self.actionButton.config(state="normal")
      else:
        self.actionButton.config(state="disabled")

#===============================================================================
#Bottom Frame --> Scrollable canvas containing LHS and RHS rule sides
#===============================================================================
      self.bottomFrame = Frame(self.containerFrame)

      self.toolBarFrame = Frame(self.bottomFrame)
      self.toolBarBottomFrame = Frame(self.toolBarFrame)  
      
      self.toolBarCanvas = Canvas(master=self.toolBarFrame,
                            takefocus=1,
                            width=600, height=300,                         
                            scrollregion= (0,0,1100,400) )
                             
      self.toolBarCanvas.scrollX = Scrollbar(self.toolBarBottomFrame, takefocus=0, orient=HORIZONTAL)                  
      self.toolBarCanvas.square = Canvas(self.toolBarBottomFrame, width=16, height=16)
      
      self.toolBarCanvas.scrollY = Scrollbar(self.toolBarFrame, takefocus=0, orient=VERTICAL)
       
      # Configure the scrollies
      self.toolBarCanvas.scrollX.config(command=self.toolBarCanvas.xview )
      self.toolBarCanvas.config( xscrollcommand=self.toolBarCanvas.scrollX.set) 
      self.toolBarCanvas.scrollY.config(command=self.toolBarCanvas.yview )
      self.toolBarCanvas.config( yscrollcommand=self.toolBarCanvas.scrollY.set)  
      
      
      # This is the beautiful part: the Frame is tucked into the canvas
      self.toolBar = Frame(self.toolBarCanvas)  
      self.toolBarCanvasHandler = self.toolBarCanvas.create_window(0,0, 
                                              window=self.toolBar, anchor=NW )
      
      
      # LHS and RHS AToM3 windows
      self.LHSframe = Frame(self.toolBar)
      self.LHSframe.pack(side=LEFT, fill='both', expand=1)
      atom3iLHS = self.LHS.open(self.LHSframe, self.LHSframe)
      self.setGGEditLHS(None, atom3iLHS, None)
      
      self.RHSframe = Frame(self.toolBar)
      self.RHSframe.pack(side=LEFT, fill='both', expand=1)
      atom3iRHS = self.RHS.open(self.RHSframe, self.RHSframe)
      self.setGGEditRHS(None, atom3iRHS, None)
      
      # Packing 
      self.toolBarFrame.pack( side=TOP, fill=BOTH, expand=1)                                        
      self.toolBarCanvas.scrollX.pack(side = LEFT, fill=X, expand=1)  
      self.toolBarCanvas.square.pack(side = RIGHT, fill=X, expand=0) 
      self.toolBarBottomFrame.pack(side = BOTTOM,fill=X, expand=0)
      
      self.toolBarCanvas.pack(side = LEFT,fill=BOTH, expand=1)   
      self.toolBarCanvas.scrollY.pack(side = LEFT,fill=Y, expand=0)
      

#===============================================================================
#Final Pack      
#===============================================================================
      self.topFrame.pack(side=TOP)
      self.bottomFrame.pack(side=TOP, fill='both', expand=1)
      return self.containerFrame
      
      
  


   def toggleAction(self, event=None):     
     """ Use condition or not? """
     # Was the condition empty already?
     if(self.Action.getValue()[4] != None):
       dialog = Dialog.Dialog(None, {'title': 'Delete Initial Action?',
                    'text': 'If you press Okay, your action code will be lost',
                    'bitmap': 'warning',
                    'default': 1,
                    'strings': ('Okay','Cancel')})
       if(dialog.num == 1):
         self.isUsingAction.set(1)
         self.actionButton.config(state="normal")
         return
           
       self.actionButton.config(state="disabled")
       templateCode = None
       
     else:
       
       self.actionButton.config(state="normal")

       templateCode = '# If you want to apply this rule at most once on a'
       templateCode += 'single host graph node, \n# then uncomment the next'
       templateCode += ' two lines. Change the default GG label (1) if needed.'
       
       templateCode += '\n\n# Make sure to enable the CONDITION code as well'
       templateCode += '\n# And to use the same label & unique name in the ACTION'      
       templateCode += '\n# WARNING: _uniqueName' + str(self.uniqueRuleID)
       templateCode += ' is not guaranteed to be unique (so change it, be safe!)'
       
       templateCode += '\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))'
       templateCode += '\n#node._uniqueName' +str(self.uniqueRuleID) + ' = True'
       templateCode += '\npass\n'

     self.Action=ATOM3Constraint()  
     self.Action.setValue(('action', (['Python', 'OCL'], 0), 
          (['PREcondition', 'POSTcondition'], 1), 
          (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 
            'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
             templateCode))



   def toggleCondition(self, event=None):     
     """ Use condition or not? """
     # Was the condition empty already?
     if(self.Condition.getValue()[4] != 'return 1\n'):
       dialog = Dialog.Dialog(None, {'title': 'Delete Initial Action?',
                    'text': 'If you press Okay, your action code will be lost',
                    'bitmap': 'warning',
                    'default': 1,
                    'strings': ('Okay','Cancel')})
       if(dialog.num == 1):
         self.isUsingCondition.set(1)
         self.conditionButton.config(state="normal")
         return
           
       self.conditionButton.config(state="disabled")
       templateCode = 'return 1\n'
       
     else:
       
       self.conditionButton.config(state="normal")

       templateCode = '# If you want to apply this rule at most once on a'
       templateCode += 'single host graph node, \n# then uncomment the next'
       templateCode += ' two lines. Change the default GG label (1) if needed.'
       
       templateCode += '\n\n# Make sure to enable the ACTION code as well'
       templateCode += '\n# And to use the same label & unique name in the ACTION'
       templateCode += '\n# WARNING: _uniqueName' + str(self.uniqueRuleID)
       templateCode += ' is not guaranteed to be unique (so change it, be safe!)'
       
       templateCode += '\n\n#node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))'
       templateCode += '\n#return not hasattr(node, "_uniqueName' 
       templateCode += str(self.uniqueRuleID) + '")\n'
       templateCode += 'return 1\n'

     self.Condition=ATOM3Constraint()  
     self.Condition.setValue(('condition', (['Python', 'OCL'], 0), 
          (['PREcondition', 'POSTcondition'], 1), 
          (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 
            'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], 
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
             templateCode))
                                         


   def showLeftHandSide (self):
      dial = ATOM3TypeDialog(self.containerFrame, self.LHS, ATOM3TypeDialog.OPEN, (None, self.setGGEditLHS))
      if dial.result_ok:
         self.LHS = dial.myWidget.ASGroot

   def showRightHandSide (self):
      dial = ATOM3TypeDialog(self.containerFrame, self.RHS, ATOM3TypeDialog.OPEN, (None, self.setGGEditRHS))
      if dial.result_ok:
         self.RHS = dial.myWidget.ASGroot

   def toString(self, maxWide = None, maxLines = None ):
      #rs = self.Name.toString()+' '+self.Order.toString()+' '+self.LHS.toString()+' '+self.RHS.toString()+' '+self.Condition.toString()+' '+self.Action.toString()
      rs = self.Name.toString()+' '+self.Order.toString()
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs


   def getValue(self):
      return (self.Name.getValue(),self.Order.getValue(),
              self.TimeDelay.getValue(),           # added 09 Aug 2002 by JL
              self.SubtypesMatching.getValue(),    # added 09 Sep 2002 by JL
              self.LHS.getValue(),self.RHS.getValue(),self.Condition.getValue(),self.Action.getValue(),) 

   def setValue(self, value):
      self.Name.setValue(value[0])
      self.Order.setValue(value[1])
      self.TimeDelay.setValue(value[2])                  # added 09 Aug 2002 by JL
      self.SubtypesMatching.setValue(value[3])           # added 09 Sep 2002 by JL
      self.LHS.setValue(value[4])
      self.RHS.setValue(value[5])
      self.Condition.setValue(value[6])
      self.Action.setValue(value[7])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"      
      file.write(indent+objName+'= GGruleEdit(None, self)\n')
      self.Name.writeConstructor2File(file, indent, objName+'.Name', depth, generatingCode)
      self.Order.writeConstructor2File(file, indent, objName+'.Order', depth, generatingCode)
      self.TimeDelay.writeConstructor2File(file, indent, objName+'.TimeDelay', depth, generatingCode)                # added 09 Aug 2002 by JL
      self.SubtypesMatching.writeConstructor2File(file, indent, objName+'.SubtypesMatching', depth, generatingCode)  # added 09 Sep 2002 by JL
      # import necessary node classes...
      classes2Import = []             			# create a list with the necessary classes to import...
      for c2i in self.LHS.listNodes.keys():		# add node names to the list...
         if not c2i in classes2Import:
            classes2Import.append(c2i)

      for c2i in self.RHS.listNodes.keys():             # add node names to the list...
         if not c2i in classes2Import:
            classes2Import.append(c2i)

      file.write("\n")
      for c2i in classes2Import:
         file.write(indent+"from "+c2i+" import *\n")
      file.write("\n")

      # call constructor for LHS graph appropriately!
      file.write(indent+objName+".LHS = "+self.LHS.getClass()+"(self)\n")
      # ey! we can have nested graphs!, generate the appropriate code for nesting...
      for merged_asg in self.LHS.mergedASG:
         file.write(indent+objName+".LHS.merge("+merged_asg.getClass()+"(self))\n")

      if generatingCode:
         self.LHS.writeGraph2File(file, 1, 0, objName+".LHS", indent, 0, '', ASGNode.INLHS, "parent")
      else:
         self.LHS.writeGraph2File(file, 1, 0, objName+".LHS", indent, 0, '', ASGNode.INLHS, "self")
      # call constructor for RHS graph appropriately!
      file.write(indent+objName+".RHS = "+self.RHS.getClass()+"(self)\n")
      # ey! we can have nested graphs!, generate the appropriate code for nesting...
      for merged_asg in self.RHS.mergedASG:
         file.write(indent+objName+".RHS.merge("+merged_asg.getClass()+"(self))\n")

      if generatingCode:
         self.RHS.writeGraph2File(file, 1, 0, objName+".RHS", indent, 0, '', ASGNode.INRHS, "parent")
      else:
         self.RHS.writeGraph2File(file, 1, 0, objName+".RHS", indent, 0, '', ASGNode.INRHS, "self")
      self.Condition.writeConstructor2File(file, indent, objName+'.Condition', depth, generatingCode)
      self.Action.writeConstructor2File(file, indent, objName+'.Action', depth, generatingCode)

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"
      self.Name.writeValue2File(file, indent, objName+'.Name', depth, generatingCode)
      self.Order.writeValue2File(file, indent, objName+'.Order', depth, generatingCode)
      self.TimeDelay.writeValue2File(file, indent, objName+'.TimeDelay', depth, generatingCode)                   # Added 09 Aug 2002 by JL
      self.SubtypesMatching.writeValue2File(file, indent, objName+'.SubtypesMatching', depth, generatingCode)     # Added 09 Sep 2002 by JL
      self.LHS.writeValue2File(file, indent, objName+'.LHS', depth, generatingCode)
      self.RHS.writeValue2File(file, indent, objName+'.RHS', depth, generatingCode)
      self.Condition.writeValue2File(file, indent, objName+'.Condition', depth, generatingCode)
      self.Action.writeValue2File(file, indent, objName+'.Action', depth, generatingCode)
      
   
   def clone(self):
      cloneObject = GGruleEdit( self.parent, self.ATOM3instance )
      cloneObject.Name = self.Name.clone()
      cloneObject.Order = self.Order.clone()
      cloneObject.TimeDelay = self.TimeDelay.clone()                       # Added 09 Aug 2002 by JL
      cloneObject.SubtypesMatching = self.SubtypesMatching.clone()         # Added 09 Sep 2002 by JL      
      cloneObject.LHS = self.LHS.clone()
      cloneObject.RHS = self.RHS.clone()
      cloneObject.Condition = self.Condition.clone()
      cloneObject.Action = self.Action.clone()
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.Name = other.Name
      self.Order = other.Order
      self.TimeDelay = other.TimeDelay                                     # Added 09 Aug 2002 by JL
      self.SubtypesMatching = other.SubtypesMatching                       # Added 09 Sep 2002 by JL
      self.LHS = other.LHS
      self.RHS = other.RHS
      self.Condition = other.Condition
      self.Action = other.Action
      ASGNode.copy(self, other)

   def destroy(self):
      self.Name.destroy()
      self.Order.destroy()
      self.TimeDelay.destroy()                                             # Added 09 Aug 2002 by JL
      self.SubtypesMatching.destroy()                                      # Added 09 Sep 2002 by JL      
      #self.LHS.destroy()
      #self.RHS.destroy()
      self.Condition.destroy()
      self.Action.destroy()
      self.containerFrame = None
   def cardinalityCheck(self, selfPosition):
      return None
   def checkConnectedObjectType(self, selfPosition):
      if selfPosition == 'SOURCE':
         last=self.out_connections_[len(self.out_connections_)-1]
      else:
         last=self.in_connections_[len(self.in_connections_)-1]
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
         return self.graphObject_.preCondition(actionID, params)
      else: return None

   def genCode(self):
      "Generates code for this class"
      fileName = self.Name.toString()+"_GG_rule.py"	# compose the file name
      if self.ATOM3instance.console: self.ATOM3instance.console.appendText('Generating file: '+fileName+' (file for rule).')
      file = open(self.ATOM3instance.codeGenDir+'/'+fileName, "w+t")	# opens the file
      file.write("# _ "+fileName+" ____________________________________________________________________________\n")
      file.write("# File generated automatically by ATOM3. Graph Grammar Rule\n")
      file.write("# ___________________________________________________________________________________________\n")
      file.write("from GGrule import *\n")
      # import the necessary files for LHS and RHS graphs
      importedFiles = []                    				# create a list, in order to not repeat file names!
      for importFile in self.LHS.listNodes.keys():			# import all node types of LHS
         if not importFile in importedFiles:
            file.write("from "+importFile+" import *\n")
            importedFiles.append(importFile)
      for importFile in self.RHS.listNodes.keys():			# # import all node types of RHS
         if not importFile in importedFiles:
            file.write("from "+importFile+" import *\n")
            importedFiles.append(importFile)

      file.write("class "+self.Name.toString()+"_GG_rule"+" (GGrule):\n\n")
      file.write("   def __init__(self, parent):\n")
      file.write("      GGrule.__init__(self, "+self.Order.toString()+")\n")
      if not self.TimeDelay.isNone() and not self.TimeDelay.invalid():                       # Added 09 Aug 2002 by JL.   
         file.write("      self.TimeDelay = ATOM3Integer("+self.TimeDelay.toString()+")\n")  # Added 09 Aug 2002 by JL.
      if self.SubtypesMatching.getValue()[1]:                                                # Added 09 Sep 2002 by JL.
         file.write("      self.exactMatch = 0\n")                                           # Added 09 Sep 2002 by JL.
      else:
         file.write("      self.exactMatch = 1\n")                                           # Added 09 Sep 2002 by JL.
      # write LHS and RHS graphs...
      # 1st call appropriate constructor for LHS...
      file.write("      self.LHS = "+self.LHS.getClass()+"(parent)\n")
      # ey! check if we have to merge the graph with some other...
      for merged_asg in self.LHS.mergedASG:
         file.write("      self.LHS.merge("+merged_asg.getClass()+"(parent))\n")

      self.LHS.writeGraph2File( file, 1, 0, "self.LHS", "      ", 0, '', ASGNode.INLHS, "parent")
      # 1st call appropriate constructor for RHS...
      file.write("      self.RHS = "+self.RHS.getClass()+"(parent)\n")
      for merged_asg in self.RHS.mergedASG:
         file.write("      self.RHS.merge("+merged_asg.getClass()+"(parent))\n")

      self.RHS.writeGraph2File( file, 1, 0, "self.RHS", "      ", 0, '', ASGNode.INRHS, "parent")

      file.write("   def condition(self, graphID, isograph, atom3i):\n")
      name, language, type, event, code = self.Condition.getValue()
      if code != None:							# if there is some code in the method...
         file.write("      "+string.replace( code, '\n', '\n      ')+"\n\n")
      else:
         file.write("      pass\n\n")
      file.write("   def action(self, graphID, isograph, atom3i):\n")
      name, language, type, event, code = self.Action.getValue()
      if code != None:							# if there is some code in the method...
         file.write("      "+string.replace( code, '\n', '\n      ')+"\n\n")
      else:
         file.write("      pass\n\n")
      file.close()

# --------------------------- GG Auto Documentation ---------------------------

   def documentRule(self, latexFile, textFile, filePath, uniqueRuleNumber):
      """ Automatic rule documentation """
          
      # Rule header
      self.docLatexHeader(latexFile,uniqueRuleNumber)
      self.docTextHeader(textFile,uniqueRuleNumber)
      
      # Generate postscript of the LHS and RHS visual part
      self.docPostscript( latexFile, filePath, uniqueRuleNumber )
      
      # Precondition & Action
      self.docLatexConstraint(latexFile,self.Condition,'Precondition','return 1')
      self.docLatexConstraint(latexFile,self.Action,'Post action')
                   
      self.docTextConstraint(textFile,self.Condition,'--> Precondition','return 1')
      self.docTextConstraint(textFile,self.Action,'--> Post action')
      
      # RHS node attributes that have been specified
      self.docNodeSpecify( latexFile, textFile )
      
      # Rule footer
      latexFile.write( '\n\\hrule \\vspace{6pt}\n')
      textFile.write( "************************************************************\n\n" )


   def docNodeSpecify(self, latexFile, textFile ):
      """ Output the RHS node attributes that have been specified """
      isFirst = True
      for nodeKind in self.RHS.listNodes:
        for node in self.RHS.listNodes[nodeKind]:
          for name in node.GGset2Any.keys():     
            tuple = node.GGset2Any[name].getValue()
            # Lookup the attr dictionary for attribute name,
            # then pick the last attribute (usually one), and remove the first
            # 5 letters... 'ATOM3' so that 'ATOM3Integer' becomes 'Integer'
            attrType = node.generatedAttributes[name][-1][5:]
            attrTuple = (name, attrType)
            
            # Specified attribute
            if( tuple[0][1] == False ):
              if(tuple[1][4] == None): 
                print '\n\nERROR: RHS of grammar rule', self.Name.getValue()
                print 'Specify rule for node', node.GGLabel.getValue()
                print 'No code detected for attribute: '+name+'\nPlease fix!'
                raise Exception, 'See console for explanation'
              if( strip(tuple[1][4]) == '' ): continue
              if( isFirst ):
                isFirst = False
                textFile.write( "******** RHS Specifications ********\n\n" )        
              self.docLatexSpecify( latexFile, str(nodeKind),
                    str(node.GGLabel.getValue()), strip(tuple[1][4]), attrTuple)
              self.docTextSpecify(textFile, str(nodeKind),
                   str(node.GGLabel.getValue()), strip(tuple[1][4]), attrTuple )
                
              

   def docTextSpecify(self, file, typeStr, labelStr, code, attrTuple):
      """ Documents a node specification """
      file.write( '-> ' + attrTuple[0] + ':' + attrTuple[1] + ' in ' 
                  + typeStr+' #'+labelStr+": \n\n"+code+"\n\n" )
                         
   def docLatexSpecify(self, file, typeStr, labelStr, code, attrTuple):
      """ Documents a node specification """
      file.write( '\\subsubsection*{Specify \\bf{'+
                  self.string2LatexString(attrTuple[0]) + '}\\rm:'
                  + self.string2LatexString(attrTuple[1]) +' in \\em{'
                  + self.string2LatexString(typeStr)
                  +' \#'+labelStr+"}}\n" )
      file.write( '\\begin{small}\\begin{verbatim}\n'+code 
                   + '\n\\end{verbatim}\\end{small}\n\n' )
      file.write( '\\hrule \\vspace{6pt}\n')

   def docLatexConstraint(self, file, constraint, headerString, ignoreString='' ):
      """ Document a constraint in text format """
      cName,cCode = constraint.getNameCode()
      if( cCode and cCode != ignoreString ):
        file.write( '\\subsubsection*{'+ headerString+': }\n' )
        file.write( '\\begin{small}\\begin{verbatim}\n'+cCode 
                   + '\n\\end{verbatim}\\end{small}\n\n' ) 
        file.write( '\\hrule \\vspace{6pt}\n')
      
   def docTextConstraint(self, file, constraint, headerString, ignoreString='' ):
      """ Document a constraint in text format """
      cName,cCode = constraint.getNameCode()
      if( cCode and cCode != ignoreString ):
        file.write( headerString+':\n\n' )
        file.write( cCode + '\n\n' )
        file.write( "************************************************************\n\n" )
      
   def string2LatexString(self, text):
      """ Latex is annoying as hell, won't accept underscores, grrr """
      textList = text.split('_') # split up all the underscores
      text = ''
      for textListPart in textList:
        text += textListPart + '\_'
      return text[:-2] # Added 2 chars too many there...
      
   def docLatexHeader(self, file, uniqueRuleNumber):
     # '\\section*{  Rule '+str(uniqueRuleNumber)
      file.write( '\\section*{  Rule \\ref{fig:'+str(self.Name.getValue())+'}'
                   +' (Order '+str(self.Order.getValue())+'): '
                   + self.string2LatexString(str(self.Name.getValue())) + '}\n')
    
    
   def docTextHeader(self, file, uniqueRuleNumber):      
      file.write( "Rule #"+str(uniqueRuleNumber)
                 + "(Order "+self.Order.toString() +")"
                 +": "+ self.Name.toString() + "\n" )            

   def docPostscript(self, latexFile, filePath, uniqueRuleNumber ):
      """ Generates postscript for the LHS and RHS of the rule """
      
      # Target dir
      import os
      dir = os.path.split( filePath )[0] # split --> [dir, filename]
      
      # Output postscript for LHS of rule
      self.postscriptHack = os.path.join(dir, "Rule_"+str(uniqueRuleNumber)+"_LHS" )
      dial = ATOM3TypeDialog(self.ATOM3instance, self.LHS, 
                      ATOM3TypeDialog.OPEN_NOWAIT, (None, self.setGGEditLHS))
      dial.myWidget.exitFromATOM3() 
      
      # If successful, the postscriptHack will now have the bounding box 
      if(self.postscriptHack != None):
        widthLHS = self.postscriptHack[2] - self.postscriptHack[0]
        heightLHS = self.postscriptHack[3] - self.postscriptHack[1]
        self.postscriptHack = None
      else:
        widthLHS = 0
      
      # Output postscript for RHS of rule
      self.postscriptHack = os.path.join(dir, "Rule_"+str(uniqueRuleNumber)+"_RHS" )
      dial = ATOM3TypeDialog(self.ATOM3instance, self.RHS, 
                      ATOM3TypeDialog.OPEN_NOWAIT, (None, self.setGGEditRHS))
      dial.myWidget.exitFromATOM3()      
    
      if(self.postscriptHack != None):
        widthRHS = self.postscriptHack[2] - self.postscriptHack[0]
        heightRHS = self.postscriptHack[3] - self.postscriptHack[1]
        self.postscriptHack = None
      else:
        widthRHS = 0
        
      # Empty Rule postscript
      if(widthLHS == 0 or widthRHS == 0):
        thisFilesDir = os.path.split(__file__)[0] # [dir, filename][0]
        emptyRuleFilePath = os.path.join(thisFilesDir, 'EmptyRule.eps')
        f = open(emptyRuleFilePath, 'r')
          
        targetDir = os.path.split(filePath)[0]
        targetFile = os.path.join(targetDir, 'EmptyRule.eps')
        if(not os.path.exists(targetFile)):
          f2 = open(targetFile, 'w')
          f2.write(f.read())
          f2.close()
        f.close()
        
        
      
      ruleNo = str( uniqueRuleNumber )
#      latexFile.write("""
#\\Ovalbox{
#\\begin{tabular}{ c c c  }
#  LHS &  $\\rightarrow$& RHS \\\\
#   \\Ovalbox{ \\includegraphics[width=2.50in]{Rule_"""+ruleNo
#   +"""_LHS.eps}} &  $\\rightarrow$&  \\Ovalbox{ \\includegraphics[width=2.50in]{Rule_"""
#   +ruleNo+"""_RHS.eps}} \\\\
#\\end{tabular}}
#\\vspace{8pt}
#"""     )

      # Calculate the exact size ratio of LHS versus RHS
      # 0.82 is the percent of horizontal space available (0.18 used for arrows)
      # So widthLHS + widthRHS = 0.82
      if(widthLHS == 0):
        LHSratio = 0.1
        RHSratio = 0.72
      elif(widthRHS == 0):
        RHSratio = 0.1
        LHSratio = 0.72
      else:
        widthRatio = float(widthLHS) / float(widthRHS)        
        RHSratio = 0.82 / (1 + widthRatio) 
        LHSratio = widthRatio * RHSratio
        
#      print 'widthLHS', widthLHS
#      print 'widthRHS', widthRHS
#      print 'widthRatio', widthRatio
#      print 'RHSratio', RHSratio
#      print 'LHSratio', LHSratio
      
      figureLabel = str(self.Name.getValue())
      figureLabelEscaped = self.string2LatexString(figureLabel)
      #latexFile.write('\\ref{fig:'+figureLabel+'}\n\n')
      latexFile.write("""
\\begin{figure*}[ht]
  \\begin{center}
  \\Ovalbox{
   \\begin{tabular}{ c c c  }
    LHS &  $\\rightarrow$& RHS \\\\""")
    
      # LHS BLOCK #
      # The LHS is EMPTY, so use a fake "EMPTY" graphic
      if(widthLHS == 0):
        #latexFile.write('\\Ovalbox{\\em{Empty}} & \\\n    $\\rightarrow$&  \\')
        latexFile.write('\n    \\Ovalbox{\\includegraphics[width=' 
                        + str(LHSratio) + '\\hsize, totalheight='
                        + str(heightRHS) + 'bp]{EmptyRule.eps}}'
                        + ' & \\\n    $\\rightarrow$&  \\')
        
      # The RHS is EMPTY, so force preservation of aspect ratio in the LHS
      elif(widthRHS == 0):
        latexFile.write('\n    \\Ovalbox{\\includegraphics[width=' 
                        + str(LHSratio) + '\\hsize, totalheight=' 
                        + str(heightLHS) + 'bp, keepaspectratio=true]{Rule_'
                        + ruleNo + '_LHS.eps}} & \\\n    $\\rightarrow$&  \\')
      
      # Normal case: Both an LHS and RHS exist, LHS uses a percentage of space
      else:
        latexFile.write('\n    \\Ovalbox{\\includegraphics[width=' 
                        + str(LHSratio) + '\\hsize]{Rule_'
                        + ruleNo + '_LHS.eps}} & \\\n    $\\rightarrow$&  \\')
                        
      # RHS BLOCK #
      # The RHS is EMPTY, so use a fake "EMPTY" graphic
      if(widthRHS == 0):
        latexFile.write('\n    \\Ovalbox{ \\includegraphics[width=' +
                        str(RHSratio) + '\\hsize, totalheight=' +
                        str(heightLHS) + 'bp]{EmptyRule.eps}} \\\\')         
      # The LHS is EMPTY, so force preservation of aspect ratio in the RHS
      elif(widthLHS == 0):
        latexFile.write('\n    \\Ovalbox{ \\includegraphics[width=' +
                        str(RHSratio) + '\\hsize, totalheight=' 
                        + str(heightRHS) + 'bp, keepaspectratio=true]{Rule_'+
                        ruleNo +'_RHS.eps}} \\\\')  
      
      # Normal case: Both an LHS and RHS exist, RHS uses a percentage of space               
      else:
        latexFile.write('\n    \\Ovalbox{ \\includegraphics[width=' +
                        str(RHSratio) + '\\hsize]{Rule_'+
                        ruleNo +'_RHS.eps}} \\\\')    
   
   
      # Finalize the figure...
      latexFile.write("""
   \\end{tabular}}
  \\caption{"""+figureLabelEscaped+"""}
  \\label{fig:"""+figureLabel+"""}
\\end{center}
%\\vspace{8pt}
\\end{figure*}
%\\hrule \\vspace{6pt}
""")
        
        
# Sample latex code:
"""
\begin{figure*}[ht]
  \begin{center}
  \Ovalbox{
   \begin{tabular}{ c c c  }
    LHS &  $\rightarrow$& RHS \\
    \Ovalbox{ \includegraphics[width=0.72\hsize, totalheight=141bp, keepaspectratio=true]{Rule_5_LHS.eps}} & \
    $\rightarrow$&  \
    \Ovalbox{ \includegraphics[width=0.1\hsize, totalheight=141bp]{EmptyRule.eps}} \\
   \end{tabular}}
  \caption{delete\_RWM\_Load}
  \label{fig:delete_RWM_Load}
\end{center}
"""
