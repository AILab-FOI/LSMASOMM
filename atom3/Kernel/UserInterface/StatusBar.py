# __ File: StatusBar.py ______________________________________________________________________________________________
#  Implements  : class StatusBar
#  Author      : Juan de Lara
#  Description : This class implements a Status Bar that shows the status of models and graph-grammars
#  Modified    : 4 Jan 2001
#   - 4 Jan 2001: added transition CLEAR from state NOT_MODIFIED of component MODEL.
# ____________________________________________________________________________________________________________________
from Tkinter import *
import os

class StatusBar(Frame):
   # States which this status bar can be in...
   NONETRANS    = 0                # No transformation loaded
   NOT_MODIFIED = 1                # Editing model or transformation ...
   MODIFIED     = 2                # Editing and modified, not saved
   # Events that can occur...
   MODIFY    = 0                # A model or trans has been modified
   SAVE      = 1                # Model or transformation saved
   LOAD      = 2                # Model or transformation loaded
   CREATE    = 3                # A new model or transf. has been created
   CLEAR     = 4                # The model has been cleaned
   # Some constants to identify MODEL or TRANSFORMATION
   MODEL          = 0
   TRANSFORMATION = 1
   # Some constants with the messages to be shown
   messages = [["",
                "Editing '%s' (not modified)",
                "Editing '%s' (modified)"],
               ["Editing transf. '%s' (not modified) in file '%s'",
                "Editing transf. '%s' (not modified) in file '%s'",
                "Editing '%s' (modified) in file '%s'"]]
   automata = [ { NOT_MODIFIED: [(MODIFY, MODIFIED), (CREATE, MODIFIED), (LOAD, NOT_MODIFIED), (SAVE, NOT_MODIFIED), (CLEAR, NOT_MODIFIED)],
                  MODIFIED:[(MODIFY, MODIFIED), (SAVE, NOT_MODIFIED), (CLEAR, NOT_MODIFIED), (LOAD, NOT_MODIFIED)]
                },
                { NONETRANS    : [(LOAD, NOT_MODIFIED), (CREATE, MODIFIED), (MODIFY, MODIFIED)],
                  NOT_MODIFIED : [(MODIFY, MODIFIED), (CREATE, MODIFIED), (LOAD, NOT_MODIFIED), (SAVE, NOT_MODIFIED)],
                  MODIFIED     : [(MODIFY, MODIFIED), (SAVE, NOT_MODIFIED), (LOAD, NOT_MODIFIED), (CREATE, MODIFIED)]
                } ]

   def __init__ (self, master):
      Frame.__init__(self, master)
      # Two ortogonal states, one to store Model state and other to store Transf.
      self.state = [ ( self.NOT_MODIFIED,   ("Nonamed",)   ),
                     ( self.NONETRANS, ( "Nonamed", "Nonamed") )]

      label1 = Label(self, bd=1, relief = SUNKEN, anchor = W, bg="light gray", fg = "blue", width = 25, font=("Helvetica", 10))
      label1.pack(side = LEFT, fill=X, expand = 1)

      label2 = Label(self, bd=1, relief = SUNKEN, anchor = W, bg="light gray", fg = "dark green", width = 25, font=("Helvetica", 10))
      label2.pack(side = RIGHT, fill=X, expand = 1)

      self.label = [label1, label2]

      for i in range(2):
        self.updateInformation(i)

   def event(self, whichOrto, eventOcc, * params ):
      "Run the automaton to see next state"
      oldState = self.state[whichOrto]                  # obtain current state
      nsl = self.automata[whichOrto][oldState[0]]       # look for transition rules...
      for ev in nsl:                                    # search the appropriate event
         if ev[0] == eventOcc:                          # if we hav found the appropriate transition rule...
            newState = ev[1]
            break
      else:                                             # Tranitions does not exist!
         return
      if params:
         theParams = []                                 	# replace only the non-None parameters
         counter = 0
         for param in params:					# go through all the parameters
            if param: theParams.append(param)			# if present, then use it for the state
            else: theParams.append(oldState[1][counter])	# if not present, then use the old state information...
            counter = counter + 1
         self.state[whichOrto] = (newState, tuple(theParams))
      else:
         self.state[whichOrto] = (newState, oldState[1])
      if oldState != self.state[whichOrto]:
         self.updateInformation(whichOrto)

   def getState(self, which):
      return self.state[which]				# returns a tuple (state, file)

   def updateInformation (self, whichOrto):
      "Updates information of appropriate status bar..."
      message = self.messages[whichOrto][self.state[whichOrto][0]]		# search the message to be shown
      params = self.state[whichOrto][1]						# search the parameters to be applied to the message
      # calculate length...
      length = len(message)-2*len(params)          				# initialize total length
      messageParameters = [whichOrto, message]					# build the parameter list for method 'set'
      hasParams = 0								# flag to indicate if we have parameters...
      for param in params:
         if param != None:              					# if we have some parameter...
	    length = length + len(param)					# add each parameter's length
            hasParams = hasParams + 1

      if length > 80 and hasParams:
         lenParam = (80-(len(message)-2*len(params)))/hasParams
         for param in params:
            if param != None:              					# if we have some parameter...
               shortParam = '...'+param[lenParam-3:]
               messageParameters.append(shortParam)
      elif hasParams:
         for param in params:
            if param != None:              					# if we have some parameter...
               messageParameters.append(param)
      else: messageParameters.append(None)

      apply( self.set, messageParameters)

   def set(self, which, format, *args):

      if args[0] != None:
         text = format % args
         # /blah/blah/blah/my_blah_MDL.py --> my_blah_MDL.py
         text = os.path.split(text)[1] 
         self.label[which].config(text=text)
         #self.label[which].config(text = format % args)
      else:
         # /blah/blah/blah/my_blah_MDL.py --> my_blah_MDL.py
         text = os.path.split(format)[1]
         self.label[which].config(text=text)
         #self.label[which].config(text = format  )
      self.label[which].update_idletasks()

  
