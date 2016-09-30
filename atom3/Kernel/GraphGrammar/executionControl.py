# __ File: executionControl.py ______________________________________________________________
# Implements : class executionControl
# Author     : Juan de Lara
# Description: Window with some widgets to control the execution of the
#              graph grammars if STEP by STEP mode has been selected.
#              Initially generated with ATOM3, added some widgets by hand.
# Modified   :
#   - 21 Oct 2001. Header added
#   - 12 Feb 2005. Continuous mode can now be Stopped.
# ___________________________________________________________________________________________

from Tkinter import *

class executionControl(Frame):

    def __init__(self, grs):
       "Constructor, takes the frame's parent and the GraphRewritingSys instance as arguments"
       self.rootWindow = Tk()                                                                                 # create a new window...
       Frame.__init__(self, self.rootWindow)                             # call the Frame constructor
       self.graphRWS = grs                                      # Store the Graph Rewriting System
       self.finished = 0                                                # indicates if the GG have finished
       self.rootWindow.title("Graph-Grammar execution controls")    # set window's title
       ggpanel = Frame(self.rootWindow, relief = RAISED)
       Label(ggpanel,text="Executing Graph-Grammar: ").grid(row=1, column=0, sticky=W)
       self.currGG = Label(ggpanel,text=self.graphRWS.getCurrentGG())
       self.currGG.grid(row=1, column=1, sticky=W)

       Label(ggpanel,text="Last executed rule: ").grid(row=2, column=0, sticky=W)
       self.curRule = Label(ggpanel,text="")
       self.curRule.grid(row=2, column=1, sticky=W)

       self.stepButton = Button(ggpanel, text="Step", command = self.doStep)
       self.stepButton.grid(row=3, column=0, sticky=W)

       self.contButton = Button(ggpanel, text="Continuous", command = self.continuous)
       self.contButton.grid(row=3, column=2, sticky=W)

       self.closeButton = Button(ggpanel, text="Close", command = self.closeWindow)
       self.closeButton.grid(row=3, column=3, sticky=W)

       ggpanel.grid(row=0, column=0)
       
       self.continuousModeActive = False
       self.isDestroyed = False
       self.buttonsDict = dict()
       self.buttonsDict['Step'] = self.stepButton
       self.buttonsDict['Continuous'] = self.contButton
       self.buttonsDict['Close'] = self.closeButton
       
    def setButtonsState( self, buttonList, state ):
      """ Takes a list of button string names, and sets them to disabled if 
      state is false, enabled if state is true """
      if( self.isDestroyed ): return
      if( state ): stateStr = 'normal'
      else: stateStr = 'disabled'
      for button in buttonList:
        if( self.buttonsDict.has_key(button) ):
          self.buttonsDict[button].config( state=stateStr )
       
    def continuous(self, closeWhenDone = False ):
       "Steps in the GG's execution until it finishes"
       
       # Toggle Continuous mode on/off
       if( self.continuousModeActive ):
          self.continuousModeActive = False
          self.contButton.config( text = "Continuous" )
          self.setButtonsState( ['Continuous'], True )
          return
       self.setButtonsState( ['Step'], False )
       self.contButton.config( text = "Stop Continuous" )
       self.continuousModeActive = True
       
       self.finished = False
       legg = self.graphRWS.lastExecutedGG  #epp
       ggs  = self.graphRWS.GraphGrammars   #epp
       while not (legg >= len(ggs)  ):        #epp          
          self.rootWindow.update()  # <-- Redraws window, critically important
          if( not self.continuousModeActive ): break
          
          self.finished = self.graphRWS.doStep()
          if( self.isDestroyed ): return
          
          self.curRule.config(text=self.graphRWS.getLastRule())
          if( self.finished):
             self.currGG.config(text="Execution finished!")
          else:
             self.currGG.config(text=self.graphRWS.getCurrentGG())
          legg = self.graphRWS.lastExecutedGG  #epp
          ggs  = self.graphRWS.GraphGrammars   #epp
       self.continuousModeActive = False
       self.graphRWS.parent.closeUnusedMetaModels()               # Modified 09 Sep 2002 by JL
       if( self.finished and closeWhenDone ): self.closeWindow()

    def doStep(self):
       "makes one step in the GG's execution"
       legg = self.graphRWS.lastExecutedGG  #epp
       ggs  = self.graphRWS.GraphGrammars   #epp
       done = (legg >= len(ggs))            #epp
       if( not done):            # if we have not finished yet
          self.finished = self.graphRWS.doStep()
          if( self.isDestroyed ): return
          
          self.curRule.config(text=self.graphRWS.getLastRule())
          if self.finished:
             self.currGG.config(text="Execution finished!")
             self.graphRWS.parent.closeUnusedMetaModels()               # Modified 09 Sep 2002 by JL
          else:
             self.currGG.config(text=self.graphRWS.getCurrentGG())

        # self.graphRWS.parent.closeUnusedMetaModels()                  # Modified 09 Sep 2002 by JL

    def closeWindow(self):
       if( self.continuousModeActive ):
         self.continuousModeActive = False
       #self.rootWindow.withdraw()
       self.rootWindow.destroy()
       self.graphRWS.parent.closeUnusedMetaModels()
 
