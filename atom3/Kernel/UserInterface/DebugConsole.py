# __ File: DebugConsole.py ____________________________________________________________________________
#  Implements  : class DebugConsole
#  Author      : Juan de Lara
#  Description : Class that implements a simple console to enter python expressions that are executed
#  Modified    : 23 Nov 2001
# ______________________________________________________________________________________________

from Tkinter import *

class DebugConsole(Frame):
     """ This is a window in which ATOM3 will display some logging messages """

     prompt = "ATOM3:> "

     def __init__(self, parent):
        """ init receives the object which will communicate with this console """
        self.rootWindow = Tk()											# create a new window...
        Frame.__init__(self, self.rootWindow)									# init the frame as a regular window
        self.rootWindow.title("ATOM3 Debugging Console")									# set window title
        self.rootWindow.geometry("+%d+%d"%(450,0)) 
        self.parent = parent											# store a reference to the parent
        
        
        textFrame = Frame(self)
        self.commandsWidget= Entry(textFrame, width = 64)
        self.commandsWidget.pack(side=TOP)
        yscrollbar = Scrollbar(textFrame)
        yscrollbar.pack(side=RIGHT, fill = Y)
        self.displayWidget = Text(textFrame, width=64, relief=GROOVE, height=16, bg = "white", state=DISABLED, yscrollcommand = yscrollbar.set)	
        # create text widget (read-only)
        self.displayWidget.pack(side=LEFT, fill = BOTH, expand=1)	# place it on window top
        yscrollbar.config(command = self.displayWidget.yview)
        textFrame.pack(side=TOP, fill=BOTH, expand=1)
        
        
        buttonPanel = Frame(self, relief=RAISED)								# create a panel to store the buttons
        clearButton = Button(buttonPanel, text="Execute", command = self.executeCommand)				# create a button to clear the console
        clearButton.pack(side = LEFT)
        clearButton = Button(buttonPanel, text="Clear", command = self.clearAllWindows)				# create a button to clear the console
        clearButton.pack(side = LEFT)         
        closeButton = Button(buttonPanel, text="Close", command = self.closeWindow)				# create a button to close the console
        closeButton.pack(side = LEFT)
        buttonPanel.pack(side=BOTTOM)										# show panel
        self.commandsWidget.bind("<Return>", self.executeCommand )				# bind mouseClicked
        self.pack(fill=BOTH, expand=1)
        self.isDestroyed = False

     def executeCommand(self, event = None):
         command2exec = self.commandsWidget.get()
         if(command2exec[:6] == 'atom3i'):
           command2exec = 'ASGroot.parent' + command2exec[6:]
         elif(command2exec[:4] == 'self'):
           command2exec = 'ASGroot.parent' + command2exec[4:]
         self.clearWindow()
         try:
           result = eval(command2exec, self.parent.__dict__, self.parent.__dict__)
         except:
           result = 'ERROR: Command failed\n'
           result += 'NOTE: To obtain an instance of ATOM3, use atom3i or self\n'
           result += 'Traceback of error follows:\n\n'
           #import traceback
           #result += str(traceback.print_last())
           import sys, cgitb, traceback, inspect
           tbt,tbv,tb = sys.exc_info()
           result += 'traceback\n',''.join(traceback.format_exception(tbt,tbv,tb))
           #print '\n\ncgitb\n',cgitb.text((tbt,tbv,tb),1)
         
         if(not self.isDestroyed):
           self.appendText(str(result))
         #self.commandsWidget.delete(0, END)

     def clearAllWindows(self):
         self.clearWindow()
         self.commandsWidget.delete(0, END)

     def clearWindow(self):
         self.displayWidget.config(state=NORMAL)
         self.displayWidget.delete(1.0, END)
         self.displayWidget.config(state=DISABLED)

     def appendText(self, whichText):
         self.displayWidget.config(state=NORMAL)
         self.displayWidget.insert(END, self.prompt+whichText+"\n")
         self.displayWidget.config(state=DISABLED)
     

     def closeWindow(self):
         self.rootWindow.withdraw()

     def showWindow(self):
         self.rootWindow.deiconify()
         
     def getRootTK(self):
         return self.rootWindow
        
     def destroy(self):
         if( not self.isDestroyed ):
           self.isDestroyed = True
           self.rootWindow.destroy()
           
