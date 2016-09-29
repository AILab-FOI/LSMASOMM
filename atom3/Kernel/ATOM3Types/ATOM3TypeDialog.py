# __ File: ATOM3TypeDialog.py __________________________________________________________________________________________________
#  Implements  : class ATOM3TypeDialog
#  Author      : Juan de Lara
#  Description :  This is a dialog to edit variables of a certain type. Just puts an instance of AT3Type into a dialog.
#  Modified    : 23 Oct 2001
#   - 16 July 2002: Line 55, changed the dialog box
#   - 21 July 2002: In validate, we support the ASGNode::invalid method to return either an integer (0 or 1) or a String
#   (or None) with the invalid reason.
# _____________________________________________________________________________________________________________________________

from MyDialog  import *
from Tkinter   import *

import copy
import tkMessageBox

class ATOM3TypeDialog(MyDialog):

    # Constants that define the mode in which the object must be edited

    SHOW = 0
    OPEN = 1
    OPEN_NOWAIT = 2

    def __init__(self, parent, AT3object, mode=SHOW, commands=None,
                    topLeftCoords=[100,150], windowTitle=None, extraText=''):
        "constructor for the case that we are editing objects and not types"
        self.parent = parent
        self.mode           = mode            		# store the mode
        AT3object.setMode(self.mode)                    # set the mode of the object
        self.AT3object      = AT3object.clone()		# make a deep copy just for the case that user press cancel
        self.realObject     = AT3object
        self.commands       = commands			# commands to be executed on the object: a tuple (PREmethod, POSTmethod)
        						# PREmethod  = method invoked prior to calling show() on object
        						# POSTmethod = method invoked post to calling show() on object
        if not parent:
            parent = Tkinter._default_root
        self.result_ok = 0
        self.myWidget = None
        self.extraText = extraText
      
        if( mode == ATOM3TypeDialog.OPEN_NOWAIT ): waitForWindow = False          
        else:                                      waitForWindow = True
        
        if( not windowTitle ): 
          windowTitle = 'Editing ' + AT3object.__class__.__name__
        MyDialog.__init__(self, parent, windowTitle, 
                          waitForWindow=waitForWindow,
                          topLeftCoords = topLeftCoords)
        
    def body(self, master):
        "creates the necessary widgets to edit the variable"
        if self.commands and self.commands[0]:			# if there are PRE-commands to execute...
           self.commands[0](self, None, self.AT3object)
        if self.mode == self.SHOW:
           self.myWidget    = self.AT3object.show(master, self)
        else:
           self.myWidget    = self.AT3object.open(master, self)
           
        # Adds a label to the top of the widget
        if(self.extraText):
          b = Label(master, text=self.extraText, fg="darkgreen",
                 bg="white", font = ("Helvetica",10), relief = GROOVE, padx=1)     
          b.pack(side = TOP, fill = X, ipady = 2)
        
        self.myWidget.pack(side=TOP, fill="both", expand=1)
        if self.commands and self.commands[1]:			# if there are POST-commands to execute...
           self.commands[1](self, self.myWidget, self.AT3object)
        return self.myWidget

    def validate(self):
        "Decides if the widget has a valid value"
        invalid = self.AT3object.invalid()                      # may return a string with the reason of invalidity
        if invalid:
            #print "AT3=", self.AT3object.constName.getValue()
            #print "RO=", self.realObject.constName.getValue()
            #self.AT3object.destroy()
            if type(invalid) == IntType:
               tkMessageBox.showwarning(
                  "Illegal value",
                  "Illegal value\nPlease try again",
                  parent = self
               )
               return 0
            elif type(invalid) == StringType:
               tkMessageBox.showwarning(
                  "Illegal value",
                  "Illegal value\n"+invalid,
                  parent = self
               )
               return 0
        # if we have an ASGNode...
        #for bname in self.AT3object.__class__.__bases__:
        #  if bname.__name__ == "ASGNode":
        #    res=self.AT3object.postCondition(self.AT3object.EDIT)
        #    if res:
        #       tkMessageBox.showwarning(
        #          "Post-condition violation!",
        #          res[0] +" "+ res[1],
        #          parent = self
        #       )
        #       return 0
        #    else: return 1

        return 1
    
    def cancel(self, event=None):
        # overwrites Dialog cancel definition, to destroy object
        self.AT3object.destroy()
        MyDialog.cancel(self, event)
	
    def apply(self):
        self.AT3object.destroy()
        self.previousObject = self.realObject.clone()
        self.realObject.copy(self.AT3object)
        self.widget = self.AT3object
        self.result = self.AT3object.toString()
        self.result_ok = 1
