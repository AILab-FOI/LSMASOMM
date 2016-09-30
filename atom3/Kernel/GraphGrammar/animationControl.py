# __ File: animationControl.py ______________________________________________________________
# Implements : class executionControl
# Author     : Juan de Lara
# Description: Window with some widgets to control the execution of the
#              graph grammars if animation has been selected. This window
#              permits to stop, pause and continue the gg execution.
# Modified   :
#   - 27 Aug 2002. File created
# ___________________________________________________________________________________________

from Tkinter import *

class animationControl(Frame):

    def __init__(self, grs):
       """
          Constructor, takes the frame's parent and the GraphRewritingSys instance as arguments
       """
       self.rootWindow = Tk()                                            # create a new window...
       Frame.__init__(self, self.rootWindow)                             # call the Frame constructor
       self.rootWindow.title("Graph-Grammar animation controls")         # set window's title

       self.grs = grs                                                    # Pointer to the graph rewriting system

       ggpanel = Frame(self.rootWindow, relief = RAISED)
       
       self.stopButton = Button(ggpanel, text="Stop", command = self.doStop)
       self.stopButton.grid(row=0, column=0, sticky=W)

       self.pauseButton = Button(ggpanel, text="Pause", command = self.doPause)
       self.pauseButton.grid(row=0, column=1, sticky=W)

       self.restartButton = Button(ggpanel, text="Continue", command = self.doRestart)
       self.restartButton.grid(row=0, column=2, sticky=W)

       self.closeButton = Button(ggpanel, text="Close", command = self.closeWindow)
       self.closeButton.grid(row=0, column=3, sticky=W)

       ggpanel.grid(row=0, column=0)

    def closeWindow(self):
       """
          Closes this window
       """
       self.rootWindow.withdraw()

    def doPause(self):
       """
          pauses the gg execution
       """
       self.grs.pause = 1 

    def doRestart(self):
       """
          restarts the gg execution
       """
       self.grs.pause = 0

    def doStop(self):
       """
          stops the gg execution
       """
       self.grs.stop = 1
       
