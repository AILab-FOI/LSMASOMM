"""
IconPositioner.py

Places the icon just right :D

Created August 15, 2004 by Denis Dube
"""

import Tkinter 

class IconPositioner:
  
  def __init__(self, editor ):
    self.editor = editor    
    self.root = editor.root
    self.offset = 250.0 
    self.boundingBox = None
    self.propertiesWindow = None
    
  def createDialog( self ):
    
        
    # New toplevel window
    propertiesWindow = Tkinter.Toplevel(self.root)
    propertiesWindow.geometry("+%d+%d" % (150,150))
    propertiesWindow.title("Icon-Editor: Positioner" )
    propertiesWindow.transient(self.root)    
    propertiesWindow.tk_focusFollowsMouse()    
    try:    propertiesWindow.grab_set() 
    except: pass
    propertiesWindow.focus_set()  
    propertiesWindow.focus_force()  
    propertiesWindow.protocol("WM_DELETE_WINDOW", self.destroy )
    self.propertiesWindow = propertiesWindow

    windowFrame = Tkinter.Frame( propertiesWindow ) 
    
    emptyFrame1 = Tkinter.Frame( windowFrame, height = 20 )
    emptyFrame2 = Tkinter.Frame( windowFrame, height = 20 )
    emptyFrame3 = Tkinter.Frame( windowFrame, height = 20 )
    emptyFrame4 = Tkinter.Frame( windowFrame, height = 20 )
    emptyFrame6 = Tkinter.Frame( windowFrame, height = 20 )
        
    autoPositionButtonFrame = Tkinter.Frame( windowFrame )
    emptyFrame5 = Tkinter.Frame( autoPositionButtonFrame, height = 20 )
    upperLeftFrame = Tkinter.Frame( autoPositionButtonFrame )
    centerOriginFrame = Tkinter.Frame( autoPositionButtonFrame )
    
    manualPositionButtonFrame = Tkinter.Frame( windowFrame )
    
    undoCloseButtonFrame = Tkinter.Frame( windowFrame )
    
      
                                
    # Labels & Action buttons    
    labelInfo = Tkinter.Label(windowFrame, height=2,padx=12, font = 'Times 14',
                              text="Auto-position icon for export", 
                              relief=Tkinter.GROOVE, bg='white' )
                              
    # ---------------------- autoPositionButtonFrame -------------------------                     
    def apply(event=None):
        self.editor.iconPlacer( 'nw' )
        self.showBoundingBox() # <-- Refresh the bounding box        
    upperLeftLabel = Tkinter.Label(upperLeftFrame, height=2,padx=12, font = 'Times 12',
                              text='Place icon top-left corner at origin (Nodes & Segements)', relief=Tkinter.RIDGE)
    upperLeftButton = Tkinter.Button(upperLeftFrame, height=2, text='Apply',
                                     width=15, command=apply )
          
    def apply(event=None):
        self.editor.iconPlacer( 'origin' )
        self.showBoundingBox() # <-- Refresh the bounding box        
    centerOriginLabel = Tkinter.Label(centerOriginFrame, height=2,padx=12, font = 'Times 12',
                              text='Center icon on the origin (CenterObjects & Links)', relief=Tkinter.RIDGE)
    centerOriginButton = Tkinter.Button(centerOriginFrame, height=2, text='Apply',
                                        width=15, command=apply )
                         
    # ---------------------- manualPositionButtonFrame -----------------------      
    labelManual = Tkinter.Label(manualPositionButtonFrame, height=2,padx=12, font = 'Times 12',
                              text="Manual offset from origin", relief=Tkinter.RIDGE)
                              
    entryManual = Tkinter.Entry( manualPositionButtonFrame )
    entryManual.insert( 0,str( self.offset )) 
    
    def apply():
      try:
        self.offset = float( entryManual.get() )
      except:
        return
      self.editor.iconPlacer( self.offset )
      self.showBoundingBox() # <-- Refresh the bounding box
      
    applyButton = Tkinter.Button(manualPositionButtonFrame, text="Apply", height=2, 
                                  width=15,command=apply )
           
                              
    text = 'WARNING: if you are modifying an existing formalism, any net change \n'+\
           'in the position of the icon will have adverse effects on existing models!'
    labelWarning = Tkinter.Label(windowFrame, height=2,padx=12, font = 'Times 12', 
                              fg='red', text=text, 
                              relief=Tkinter.GROOVE, bg='white' )
                     
    def undo():
      editor = self.editor
      if( not editor.isUndoStackEmpty() ):
        editor.mainHandler.onUndo()     
        self.showBoundingBox() # <-- Refresh the bounding box        
    undoButton = Tkinter.Button(undoCloseButtonFrame, text="Undo", height=2, 
                                  command=undo )
    cancelButton = Tkinter.Button(undoCloseButtonFrame, text="Close", height=2, 
                                  command=self.destroy )
    
  
    # Pack inside the autoPositionButtonFrame    
    upperLeftLabel.pack( side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1 )
    centerOriginLabel.pack( side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1  )
    upperLeftButton.pack( side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=0 )
    centerOriginButton.pack( side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=0  )    
    upperLeftFrame.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )  
    emptyFrame5.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )  
    centerOriginFrame.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )      
    
    # Pack inside the manualPositionButtonFrame
    labelManual.pack( side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1 )
    entryManual.pack( side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=0  )
    applyButton.pack( side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=0  )
  
    # Pack inside the windowFrame
    labelInfo.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )    
    emptyFrame1.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )    
    autoPositionButtonFrame.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
    emptyFrame2.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
    manualPositionButtonFrame.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
    emptyFrame3.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
    labelWarning.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
    emptyFrame4.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
    
    # Pack the undoCloseButtonFrame
    undoButton.pack( side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1 )
    cancelButton.pack( side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1 )
    undoCloseButtonFrame.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
  
    windowFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
    
    # In the background, lets show the bounding box of what were placing
    self.showBoundingBox()    
    
    # Wait till I'm done here! This will 'block' program execution until
    # this dialog is terminated via self.destroy()  
    self.root.wait_window( propertiesWindow )

  def destroy( self ):
      self.removeBoundingBox()
      self.propertiesWindow.destroy()

  def showBoundingBox(self ):
      """ Shows exactly what the bounding box of the GFs is """
      
      editor = self.editor
      canvas = editor.canvas
      gfList = editor.getGFs()
      
      # Create it only if there are more than 1 GFs!
      if( len( gfList ) < 1 ):    return
      
      coords = editor.getBoundingBox( gfList )
      map( lambda x, z=editor.getZoom(): z*x, coords ) #<--- Zoom the coords

      # If boundingBox already exists, then just refresh it
      if( self.boundingBox ):
          canvas.coords( * [self.boundingBox] + coords ) 
        
      # Create new bounding box
      else:        
          self.boundingBox = canvas.create_rectangle( coords, fill='green',stipple='gray25' )
      
  def removeBoundingBox( self ):
      """ Removes the bounding box if it exists """
      if( self.boundingBox ):         
        self.editor.canvas.delete( self.boundingBox )
        self.boundingBox = None

  