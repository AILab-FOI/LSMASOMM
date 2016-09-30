# __ File: Console.py ____________________________________________________________________________
#  Implements  : class Console
#  Author      : Juan de Lara
#  Description : Class that implements a simple console in which ATOM3 can write messages
#  Modified    : 23 Oct 2001
#  Changes :
#   - 23 Oct 2001 : added method "hasGenerativeAttributes"
# ______________________________________________________________________________________________

from Tkinter import *

class Console(Frame):
     """ This is a window in which ATOM3 will display some logging messages """

     prompt = "ATOM3:> "

     def __init__(self, parent):
        """ init receives the object which will communicate with this console """
        self.rootWindow = Tk()											# create a new window...
        Frame.__init__(self, self.rootWindow)									# init the frame as a regular window
        self.rootWindow.title("ATOM3 Info Console")									# set window title
        self.rootWindow.geometry("+%d+%d"%(0,0)) 
        textFrame = Frame(self)
        self.parent = parent											# store a reference to the parent
        yscrollbar = Scrollbar(textFrame)
        yscrollbar.pack(side=RIGHT, fill = Y)
        self.displayWidget = Text(textFrame, width=64, relief=GROOVE, height=16, bg = "white", state=DISABLED, yscrollcommand = yscrollbar.set)	
        # create text widget (read-only)
        self.displayWidget.pack(side=LEFT, fill = BOTH)							# place it on window top
        yscrollbar.config(command = self.displayWidget.yview)
        textFrame.pack(side=TOP)
        buttonPanel = Frame(self, relief=RAISED)								# create a panel to store the buttons
        clearButton = Button(buttonPanel, text="Clear", command = self.clearWindow)				# create a button to clear the console
        clearButton.pack(side = LEFT)
        closeButton = Button(buttonPanel, text="Close", command = self.closeWindow)				# create a button to close the console
        closeButton.pack(side = LEFT)
        buttonPanel.pack(side=BOTTOM)										# show panel
        self.rootWindow.protocol("WM_DELETE_WINDOW", self.closeWindow)
        self.closed = 0
        self.pack()
        self.isDestroyed=False

     def clearWindow(self):
         """
            Cleans the Text widget
         """
     	 if not self.closed:
            self.displayWidget.config(state=NORMAL)
            self.displayWidget.delete(1.0, END)
            self.displayWidget.config(state=DISABLED)

     def closeWindow(self):
         """
            Iconifies window.
         """
         self.rootWindow.withdraw()
         self.closed = 1

     def showWindow(self):
         """
            Shows window (if previously iconified)
         """
         self.rootWindow.deiconify()
         self.closed = 0

     def appendText(self, whichText):
         """
            Appends some text to the one that is displayed now.
         """
         self.displayWidget.config(state=NORMAL)
         self.displayWidget.insert(END, self.prompt+whichText+"\n")
         self.displayWidget.config(state=DISABLED)

     def getRootTK(self):
         return self.rootWindow
        
     def destroy(self):
        if( not self.isDestroyed ):
          self.isDestroyed = True
          self.rootWindow.destroy()
