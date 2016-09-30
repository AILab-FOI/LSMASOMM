# MyDialog.py
#
# Original version tkSimpleDialog.py - Copyright (c) 1997 by Fredrik Lundh
#
# fredrik@pythonware.com
# http://www.pythonware.com
#

# --------------------------------------------------------------------
# dialog base class

from Tkinter import *
import os, re

GEOMETRY_PATTERN = re.compile( '([0-9]+)x([0-9]+)\+([0-9]+)\+([0-9]+)' )

class MyDialog(Toplevel):

    def __init__(self, parent, title = None, fixed = 0, 
                 waitForWindow=True, topLeftCoords = None ):

        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:
            self.title(title)

        self.parent = parent

        self.result = None

        self.frame1 = Frame(self, bg='blue')
        self.frame2 = Frame(self)

        body = self.frame1 #Frame(self.frame)
        self.initial_focus = self.body(body)
#        if fixed:
#            body.pack(side=TOP, fill="both", expand = 1, padx=5, pady=5)
#        else:
#            body.pack(side=TOP, fill="both", expand = 1, padx = 5, pady = 5)

        if not self.initial_focus:
            self.initial_focus = self

        self.frame1.pack(side=TOP, fill="both", expand=1)
        self.buttonbox()
        self.frame2.pack(side=BOTTOM)


        self.protocol("WM_DELETE_WINDOW", self.cancel)
        
        if( topLeftCoords ):
          self.geometry("+%d+%d" % ( topLeftCoords[0], topLeftCoords[1] ) )
        else:
          try:
            # parent is AToM3 instance, parent.parent is TK root window
            self.geometry("+%d+%d" % (parent.parent.winfo_rootx()+20,
                                    parent.parent.winfo_rooty()+20))
          except:
            # parent is a frame..
            self.geometry("+%d+%d" % (parent.winfo_rootx()+20,
                                    parent.winfo_rooty()+20))

        self.update()
        self.enforceGeometryInScreenspace()

        if fixed: self.resizable(0, 0)
        else:     self.resizable(1, 1)

        self.grab_set()

        self.initial_focus.focus_set()

        if( waitForWindow ):
          self.wait_window(self)

    def enforceGeometryInScreenspace(self):
      """
      This method makes sure that the dialog box will never exceed the bottom
      or right of the screen. I doubt the dialog box will ever exceed the top
      or left, so I don't enforce that.
      Denis Dube
      """
      
      # Convert geometry string to integers... (more accurate)
      m = GEOMETRY_PATTERN.search( self.winfo_geometry() )
      if( m ):
        curWidth, curHeight, curXCoord, curYCoord = map( int, m.groups() )
      else:
        # Not as accurate :(
        curYCoord = self.winfo_rooty()
        curHeight = self.winfo_height()
        curXCoord = self.winfo_rootx()
        curWidth = self.winfo_width()
        
      guiBarHeight = 40 # Not counted in screenheight, the size of WinXP bars..
      maxHeight = self.winfo_screenheight() - guiBarHeight
      if( curYCoord + curHeight > maxHeight ):
        curYCoord = maxHeight - curHeight 
      maxWidth = self.winfo_screenwidth()
      if( curXCoord + curWidth > maxWidth ):
        curXCoord = maxWidth - curWidth 
        
      self.geometry("+%d+%d" % ( curXCoord, curYCoord ) )
      self.update()

    #
    # construction hooks

    def body(self, master):
        # create dialog body.  return widget that should have
        # initial focus.  this method should be overridden

        pass

    def buttonbox(self):
        # add standard button box. override if you don't want the
        # standard buttons

        box = Frame(self.frame2)

        w = Button(box, text="OK", width=10, command=self.ok)
        w.pack(side=LEFT, padx=5, pady=5)
        w = Button(box, text="Cancel", width=10, command=self.cancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)

        box.pack(side=BOTTOM, fill=BOTH, expand=0)
	
    #
    # standard button semantics

    def ok(self, event=None):

        if not self.validate():
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()

    def cancel(self, event=None):

        # put focus back to the parent window
        self.parent.focus_set()
        self.destroy()

    #
    # command hooks

    def validate(self):

        return 1 # override

    def apply(self):

        pass # override
