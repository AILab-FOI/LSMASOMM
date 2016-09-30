# __ File: GraphGrammarEdit.py ______________________________________________________________
# Implements : class GraphGrammarEdit
# Author     : Juan de Lara
# Description: Window with some widgets to edit a Graph Grammar
#              Initially generated with ATOM3, added some widgets by hand.
# Modified   :
#   - 21 Oct 2001. Header added
# ___________________________________________________________________________________________

from ASGNode import *

from ATOM3Type import *

from ATOM3String import *
from ATOM3List import *
from ATOM3Constraint import *
from ATOM3Constraint import *
from GGruleEdit import *

import string

class GraphGrammarEdit(ASGNode, ATOM3Type):

   def __init__(self, parent, ATOM3instance):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.ATOM3instance = ATOM3instance
      self.parent = parent
      self.Name=ATOM3String('')
      
      self.Rules=ATOM3List([ 1, 1, 1, 0], GGruleEdit, None, ATOM3instance )
      lcobj0=[]
      self.Rules.setValue(lcobj0)
      self.InitialAction=ATOM3Constraint()      
      self.InitialAction.setValue(('constraint', 
                                   (['Python', 'OCL'], 0), 
                                     (['PREcondition', 'POSTcondition'], 1), 
                                      (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 
                                        'DELETE', 'DISCONNECT', 'TRANSFORM', 
                                        'SELECT', 'DRAG', 'DROP', 
                                        'MOVE OBJECT'], 
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
                                         None))
      
      self.FinalAction=ATOM3Constraint()
      self.FinalAction.setValue(('const', 
                                 (['Python', 'OCL'], 0), 
                                   (['PREcondition', 'POSTcondition'], 1), 
                                     (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 
                                       'DELETE', 'DISCONNECT', 'TRANSFORM', 
                                       'SELECT', 'DRAG', 'DROP', 
                                       'MOVE OBJECT'], 
                                       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
                                        None))
      
      self.generatedAttributes = {'Name': ('ATOM3String', ),
                                  'Rules': ('ATOM3List', ),
                                  'InitialAction': ('ATOM3Constraint', ),
                                  'FinalAction': ('ATOM3Constraint', )      }
                                  
      self.isUsingInitialAction = IntVar()  
      self.isUsingInitialAction.set(0)
      self.isUsingFinalAction = IntVar()                                
      self.isUsingFinalAction.set(0)
                                  
                                  
   def show(self, parent, parentWindowInfo):
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      
      Label(self.containerFrame, 
            text = "WARNING: Name must use Python variable syntax", 
            fg="darkgreen", bg="white", font = ("Helvetica",10), 
            relief = GROOVE, padx=1).grid(row=0,columnspan=4,sticky=EW)
           
      Label(self.containerFrame, text='Name').grid(row=1,column=0,sticky=W)
      self.Name.show(self.containerFrame, parentWindowInfo).grid(
                                                    row=1,column=1,sticky=W)
      
#================================================================================
#      Initial Action
#================================================================================
#      Label(self.containerFrame, text='InitialAction').grid(
#                                                      row=2,column=0,sticky=W)            
      
      self.initialActionButton = Button( self.containerFrame, text = 'InitialAction', 
             command =  lambda x=self : ATOM3TypeDialog(x.containerFrame, 
                          x.InitialAction))
      self.initialActionButton.grid(row=2,column=0,sticky=W)
      Checkbutton(self.containerFrame, text="Enabled?", 
                    variable=self.isUsingInitialAction, 
                    command=self.toggleInitialAction
                    ).grid(row=2,column=1,sticky=W)
      
      if(self.InitialAction.getValue()[4] != None):
        self.isUsingInitialAction.set(1)
        self.initialActionButton.config(state="normal")
      else:
        self.initialActionButton.config(state="disabled")
        
        
#===============================================================================
#      Rules
#===============================================================================
      
      # Re-order the rules...
      ruleList = self.Rules.getValue()[:] # Make copy of the list (important)
      if(ruleList):
        ruleList.sort(lambda a, b: cmp(a.Order.getValue(), b.Order.getValue()))
        self.Rules.setValue(ruleList)
      self.Rules.setHeight(max(len(ruleList), 20)) # Show up to 20 rules at a time
                                                 
      Label(self.containerFrame, text='Rules').grid(row=3,column=0,sticky=W)      
      self.Rules.show(self.containerFrame, parentWindowInfo).grid(
                                                    row=3,column=1,sticky=W)
      
      
#================================================================================
#      Final Action
#================================================================================
#      Label(self.containerFrame, text='FinalAction').grid(
#                                                    row=4,column=0,sticky=W)
      self.finalActionButton = Button( self.containerFrame, text = 'FinalAction', 
             command =  lambda x=self : ATOM3TypeDialog(x.containerFrame, 
                              x.FinalAction))
      self.finalActionButton.grid(row=4,column=0,sticky=W)
      Checkbutton(self.containerFrame, text="Enabled?", 
                    variable=self.isUsingFinalAction, 
                    command=self.toggleFinalAction
                    ).grid(row=4,column=1,sticky=W)       
                    
      if(self.FinalAction.getValue()[4] != None):
        self.isUsingFinalAction.set(1)
        self.finalActionButton.config(state="normal")
      else:
        self.finalActionButton.config(state="disabled")                  
        
        
      # Seperator
      Frame(self.containerFrame, relief='flat', height=14, 
            borderwidth=4).grid(row=5,column=0, columnspan=3,sticky=EW)
      
      buttonFrame = Frame(self.containerFrame, relief='ridge', borderwidth=10)
      buttonFrame.grid(row=6,column=0, columnspan=3,sticky=EW)
            
      atom3i = self.ATOM3instance
      

      def handler(event=None):
        parentWindowInfo.ok() # Close the existing GG dialog window
        atom3i.parent.after(1, atom3i.loadTrans) # Wait for dialog to close
      Button(buttonFrame, text='Load GG', command=handler).pack(side=TOP, fill=BOTH, expand=1)
      
      def handler(event=None):
        parentWindowInfo.ok() # Close the existing GG dialog window
        atom3i.parent.after(1, atom3i.saveTrans) # Wait for dialog to close
      Button(buttonFrame, text='Save GG', command=handler).pack(side=TOP, fill=BOTH, expand=1)

      def handler(event=None):
        parentWindowInfo.ok() # Close the existing GG dialog window
        atom3i.parent.after(1, atom3i.genTransDocumentation) # Wait for dialog to close
      Button(buttonFrame, text='Generate latex document from GG', command=handler).pack(side=TOP, fill=BOTH, expand=1)
      
      def handler(event=None):
        parentWindowInfo.ok() # Close the existing GG dialog window
        atom3i.parent.after(1, atom3i.genCode4Trans) # Wait for dialog to close
      Button(buttonFrame, text='Generate GG code', command=handler).pack(side=TOP, fill=BOTH, expand=1)
      
      def handler(event=None):
        parentWindowInfo.ok() # Close the existing GG dialog window
        atom3i.parent.after(1, atom3i.executeTrans) # Wait for dialog to close
      Button(buttonFrame, text='Execute GG code', command=handler).pack(side=TOP, fill=BOTH, expand=1)
      
      
      
#      genCode4Trans
#      executeTrans
                              
      return self.containerFrame



   def toggleFinalAction(self, event=None):     
     """ Use final action or not? """
     # Was the final action empty already?
     if(self.FinalAction.getValue()[4] != None):
       dialog = Dialog.Dialog(None, {'title': 'Delete Initial Action?',
                    'text': 'If you press Okay, your action code will be lost',
                    'bitmap': 'warning',
                    'default': 1,
                    'strings': ('Okay','Cancel')})
       if(dialog.num == 1):
         self.isUsingFinalAction.set(1)
         self.finalActionButton.config(state="normal")
         return
           
       self.finalActionButton.config(state="disabled")
       templateCode = None
       
     else:
       
       self.finalActionButton.config(state="normal")
       templateCode = \
'''# Template code for an initial action (a full host graph traversal)

#for nodeType in graph.listNodes.keys():
#    for node in graph.listNodes[nodeType]:
#      # Prints the class name of all nodes in graph
#      print node.__class__.__name__ 
#
#      # This part assumes that *ALL* nodes in graph have been given the 
#      # _randomAttribute and that we now want to remove it
#      del node._randomAttribute
pass 

'''
     self.FinalAction=ATOM3Constraint()  
     self.FinalAction.setValue(('constraint', 
                                   (['Python', 'OCL'], 0), 
                                     (['PREcondition', 'POSTcondition'], 1), 
                                      (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 
                                        'DELETE', 'DISCONNECT', 'TRANSFORM', 
                                        'SELECT', 'DRAG', 'DROP', 
                                        'MOVE OBJECT'], 
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
                                         templateCode))
                                         

   def toggleInitialAction(self, event=None):     
     """ Use inital action or not? """
     # Was the inital action empty already?
     if(self.InitialAction.getValue()[4] != None):
       dialog = Dialog.Dialog(None, {'title': 'Delete Initial Action?',
                    'text': 'If you press Okay, your action code will be lost',
                    'bitmap': 'warning',
                    'default': 1,
                    'strings': ('Okay','Cancel')})
       if(dialog.num == 1):
         self.isUsingInitialAction.set(1)
         self.initialActionButton.config(state="normal")
         return
           
       self.initialActionButton.config(state="disabled")
       templateCode = None
       
     else:
       
       self.initialActionButton.config(state="normal")
       templateCode = \
'''# Template code for an initial action (a full host graph traversal)

#idInt = 0
#for nodeType in graph.listNodes.keys():
#    for node in graph.listNodes[nodeType]:
#      # Prints the class name of all nodes in graph
#      print node.__class__.__name__ 
#
#      # This part assumes that *ALL* nodes in graph have ATOM3 Integer 
#      # attribute called "id" and that this attribute is in the visual icon
#      # NOTE: setGenValue() sets the semantic value, updates visually, and
#      # catches attribute name errors and displays correct alternatives
#      node.setGenValue('id', idInt)
#      idInt += 1
pass 

'''
     self.InitialAction=ATOM3Constraint()  
     self.InitialAction.setValue(('constraint', 
                                   (['Python', 'OCL'], 0), 
                                     (['PREcondition', 'POSTcondition'], 1), 
                                      (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 
                                        'DELETE', 'DISCONNECT', 'TRANSFORM', 
                                        'SELECT', 'DRAG', 'DROP', 
                                        'MOVE OBJECT'], 
                                        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 
                                         templateCode))
                                         

   def toString(self, maxWide = None, maxLines = None ):
      rs = self.Name.toString()+' '+self.Rules.toString()+' '+self.InitialAction.toString()+' '+self.FinalAction.toString()
      if maxWide: return self.strValue[0:maxWide-3]+'...'
      else: return rs


   def getValue(self):
      return (self.Name.getValue(),self.Rules.getValue(),self.InitialAction.getValue(),self.FinalAction.getValue(),)

   def setValue(self, value):
      self.Name.setValue(value[0])
      self.Rules.setValue(value[1])
      self.InitialAction.setValue(value[2])
      self.FinalAction.setValue(value[3])

   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the constructor and the value of the object. Must be overriden in children"      
      file.write(indent+objName+'= GraphGrammarEdit(None, self)\n')
      self.Name.writeConstructor2File(file, indent, objName+'.Name', depth, generatingCode)
      self.Rules.writeConstructor2File(file, indent, objName+'.Rules', depth, generatingCode)
      self.InitialAction.writeConstructor2File(file, indent, objName+'.InitialAction', depth, generatingCode)
      self.FinalAction.writeConstructor2File(file, indent, objName+'.FinalAction', depth, generatingCode)

      

   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      "Method that writes into a file the the value of the object. Must be overriden in children"
      self.Name.writeValue2File(file, indent, objName+'.Name', depth, generatingCode)
      self.Rules.writeValue2File(file, indent, objName+'.Rules', depth, generatingCode)
      self.InitialAction.writeValue2File(file, indent, objName+'.InitialAction', depth, generatingCode)
      self.FinalAction.writeValue2File(file, indent, objName+'.FinalAction', depth, generatingCode)

   def clone(self):
      cloneObject = GraphGrammarEdit( self.parent, self.ATOM3instance )
      cloneObject.Name = self.Name.clone()
      cloneObject.Rules = self.Rules.clone()
      cloneObject.InitialAction = self.InitialAction.clone()
      cloneObject.FinalAction = self.FinalAction.clone()
      ASGNode.cloneActions(self, cloneObject)

      return cloneObject
   def copy(self, other):
      ATOM3Type.copy(self, other)
      self.Name = other.Name
      self.Rules = other.Rules
      self.InitialAction = other.InitialAction
      self.FinalAction = other.FinalAction
      ASGNode.copy(self, other)

   def destroy(self):
      self.Name.destroy()
      self.Rules.destroy()
      self.InitialAction.destroy()
      self.FinalAction.destroy()
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
      # 1st. generate code for each rule
      rules = self.Rules.getValue()						# Get the vector of rules...
      for rule in rules:							# for each rule...
         rule.genCode()								# call the code generating method...
      # now Generate the file with the generated class...
      fileName = self.Name.toString()+"_GG_exec.py"		                # compose file name
      if self.ATOM3instance.console: self.ATOM3instance.console.appendText('Generating file: '+fileName+' (main file for transformation).')
      file = open(self.ATOM3instance.codeGenDir+'/'+fileName, "w+t")		# opens the file
      file.write("# _ "+fileName+" ____________________________________________________________________________\n")
      file.write("# "+self.Name.toString()+" : a class that subclasifies GraphGrammar. File generated automatically by ATOM3.\n")
      file.write("# ___________________________________________________________________________________________\n")
      file.write("from GraphGrammar import *\n")
      # for each rule in the graph grammar, import its file
      for rule in rules:
         file.write("from "+rule.Name.toString()+"_GG_rule"+" import *\n")
      file.write("class "+self.Name.toString()+"_GG_exec"+" (GraphGrammar):\n")
      file.write("   def __init__ (self, parent):\n")
      file.write("      GraphGrammar.__init__(self, [")
      # add an object of each rule to the list
      counter = 0
      for rule in rules:
         if counter > 0:
            file.write(" , ")
         file.write(rule.Name.toString()+"_GG_rule"+"(parent)")
         counter = counter + 1
      file.write("])\n")
      # generate the initial action function
      file.write("   def initialAction(self, graph):\n")
      name, language, type, event, code = self.InitialAction.getValue()
      if code != None:								# if there is some code in the method...
         file.write("      "+string.replace( code, '\n', '\n      ')+"\n\n")
      else:
         file.write("      pass\n\n")
      # generate the final action function
      file.write("   def finalAction(self, graph):\n")
      name, language, type, event, code = self.FinalAction.getValue()
      if code != None:								# if there is some code in the method...
         file.write("      "+string.replace( code, '\n', '\n      ')+"\n\n")
      else:
         file.write("      pass\n\n")
      
      # Remove this module from memory! And all dependent rules...      
      importedModules = []
      for rule in rules:
        importedModules.append( rule.Name.toString()+"_GG_rule" )
      file.write("importedModules = " + str(importedModules) + "\n\n" )
      file.close()


# ---------------------------- Added by Denis Feb 2005 -----------------------

   def documentGrammar(self, filePath ):
      """ Documents the grammar """

      filePath = os.path.splitext( filePath )[0]
      
      latexFile = open( filePath + '.tex', "w" )      
      textFile = open( filePath + '.txt', "w" )      
      
      # Grammar header
      self.docLatexHeader(latexFile)
      self.docTextHeader(textFile)
        
      # Initial Grammar Action  
      self.docLatexConstraint(latexFile,self.InitialAction,'Global initial action')          
      self.docTextConstraint(textFile,self.InitialAction,'Global initial action')
      
      # Document each rule of the grammar in GGruleEdit.py
      self.documentRules( latexFile, textFile, filePath )
      
      # Final Grammar Action
      self.docLatexConstraint(latexFile,self.FinalAction,'Global final action')            
      self.docTextConstraint(textFile,self.FinalAction,'Global final action')
                
      # Footer
      latexFile.write( '\n\\end{document}\n' )
                         
      latexFile.close()
      textFile.close()
      
      
   def docLatexConstraint(self, file, constraint, headerString ):
      """ Document a constraint in text format """
      cName,cCode = constraint.getNameCode()
      if( cCode ):
        file.write( '\\hrule \\vspace{6pt}\n')
        file.write( '\\subsubsection*{'+ self.string2LatexString(headerString)
                      +': }\n' )
        file.write( '\\begin{small}\\begin{verbatim}\n'+cCode 
                     + '\n\\end{verbatim}\\end{small}\n\n' ) 
        file.write( '\\hrule \\vspace{6pt}\n')
        file.write( '\\hrule \\vspace{6pt}\n')
        
   def string2LatexString(self, text):
      """ Latex is annoying as hell, won't accept underscores, grrr """
      textList = text.split('_') # split up all the underscores
      text = ''
      for textListPart in textList:
        text += textListPart + '\_'
      return text[:-2] # Added 2 chars too many there...        

      
   def docTextConstraint(self, file, constraint, headerString ):
      """ Document a constraint in text format """
      cName,cCode = constraint.getNameCode()
      if( cCode ):
        file.write( headerString+':\n\n' )
        file.write( cCode + '\n\n' )
        file.write( "************************************************************\n\n" )
      
   def docLatexHeader(self, file):
      """ Document latex header """
      file.write( """
% ------------------------------------------------------------------------
% Graph Grammar Documentation
% ===========================
%
\\documentclass{article}
\\usepackage{graphicx}
\\usepackage{fancybox}
\\usepackage{vmargin}
\\title{ \\huge{""" + self.string2LatexString(str(self.Name.getValue())) + """} \\\\[4mm]
\\small{ Graph grammar documentation generated by \\textbf{AToM$^{3}$Doc} } }
%\\author{ \\small{Author: Denis Dube}} % <-- Put your name here
% Make decent margins
\\setmarginsrb{1.5cm}{0.5cm}{1cm}{2.5cm}{12pt}{25pt}{12pt}{30pt}
% ------------------------------------------------------------------------
% Document Starts here:
% ------------------------------------------------------------------------
\\begin{document}   
\\maketitle         
""")
   
   def docTextHeader(self, file):
      """ Document latex header """
      file.write( "************************************************************\n" )
      file.write( "* " + self.Name.toString() + "              \n" )
      file.write( "*                                           \n" )
      file.write( "* AToM3Doc generated graph Grammar documentation  \n" )
      file.write( "************************************************************\n\n" )
          
   def documentRules(self, latexFile, textFile, filePath ):
      """ Documents all the rules of the grammar in sorted order """
      ruleList = self.Rules.getValue()
      ruleDict = dict()
      for rule in ruleList:
        orderInt = rule.Order.getValue()
        if(not ruleDict.has_key(orderInt)):
          ruleDict[orderInt] = [rule]
        else:
          ruleDict[orderInt].append(rule)
      sortedKeys = ruleDict.keys()
      sortedKeys.sort()   
      uniqueRuleNumber = 1
      for key in sortedKeys:
        for rule in ruleDict[key]:
          rule.documentRule(latexFile, textFile,filePath, uniqueRuleNumber )
          uniqueRuleNumber += 1
