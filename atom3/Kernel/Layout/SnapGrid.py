"""
SnapGrid.py

Creates an overlay grid over the canvas that snaps objects to itself

NOTE: This file is responsible only for drawing the grid itself, as well as
      configuring the grid attributes and informing AToM3 of the size of the 
      grid and who should snap to what. AToM3 must do the actual position snap.

Created June 26, 2004 by Denis Dube
"""

from OptionDatabase import OptionDatabase
from OptionDialog   import OptionDialog

def applyLayout( atom3i, settingsMode = False, disableForPrinting = False ):
  """ Applies the layout algorithm using the singleton pattern """
  
  # Instantiate the layout algorithm, if not already done  
  if( SnapGrid.instance == None ):
    SnapGrid.instance = SnapGrid(atom3i)
    
  if( disableForPrinting ):
    SnapGrid.instance.destroy( disableForPrinting )
    return
  
  SnapGrid.instance.updateATOM3instance( atom3i )
    
  if( settingsMode ):
    SnapGrid.instance.settings()                      # Change SnapGrid parameters
  else:    
    SnapGrid.instance.drawGrid()                      # Apply SnapGrid
  

class SnapGrid:
  
  instance = None
  highestItemHandler = None
  """
  highestItemHandler variable is used to place items just above the grid lines
  Example pattern:
  dc.tag_lower(myItemHandler) # Under everything
  if(SnapGrid.highestItemHandler):
    dc.tag_raise(myItemHandler, SnapGrid.highestItemHandler) # Above grid
  """
  
  GRID_ENABLED            = 'snapgrid enabled'
  GRID_ARROWNODE          = 'snap arrow node'
  GRID_CONTROLPOINTS      = 'snap control points'
  GRID_PIXELS             = 'gridsquare pixels'
  GRID_WIDTH              = 'gridsquare width'
  GRID_COLOR              = 'gridsquare color'
  GRID_DOT_MODE           = 'use gridsquare dots'
  GRID_SUDIVISIONS        = 'gridsquare subdivisions'
  GRID_SUDIVISIONS_WIDTH  = 'gridsquare sudvision width'
  GRID_SUBDIVISION_COLOR  = 'gridsquare subdivision color'
  GRID_SUBDIVISION_SHOW   = 'enable gridsquare subdivisions'
 
  def __init__(self, atom3i):
        
    # Keep track of item handlers so that the lines can be removed (if needed)
    self.__gridItemHandlers = []    
    
    self.atom3i = atom3i              # AToM3 instance
    self.dc = self.atom3i.getCanvas() 
        
    # Instantiate the Option Database module
    self.__optionsDatabase = OptionDatabase(self.atom3i.parent,
                              'Options_SnapGrid.py', 'Snap Grid Configuration')
    
    # Local methods/variables with short names to make things more readable :D
    newOp = self.__optionsDatabase.createNewOption
    IE = OptionDialog.INT_ENTRY
    CE = OptionDialog.COLOR_ENTRY
    BE = OptionDialog.BOOLEAN_ENTRY
    
    # Create New Options
    # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
    newOp( self.GRID_ENABLED, True, BE, "Enable Snap Grid" )  
    newOp( self.GRID_ARROWNODE, False, BE, "Snap arrow node" )  
    newOp( self.GRID_CONTROLPOINTS, False, BE, "Snap arrow control points" ) 
    
    newOp( self.GRID_PIXELS, 20, IE, "Grid square size in pixels", "Snapping will occur at every X pixels square" )     
    newOp( self.GRID_DOT_MODE, True, BE, "Grid dots", "Dot mode is much slower than using lines" )  
    newOp( self.GRID_WIDTH, 1, IE, "Grid square width in pixels" ) 
    newOp( self.GRID_COLOR, '#c8c8c8', [CE,"Choose Color"], "Grid square color" )
    
    newOp( self.GRID_SUDIVISIONS, 5, IE, "Grid square subdivisions", "Every X number of divisions, a subdivsion will be placed" ) 
    newOp( self.GRID_SUBDIVISION_SHOW, True, BE, "Show subdivision lines","Makes it easier to visually measure distances" )     
    newOp( self.GRID_SUDIVISIONS_WIDTH, 1, IE, "Grid square sudivision width" )    
    newOp( self.GRID_SUBDIVISION_COLOR, '#e8e8e8', [CE,"Choose Color"], "Grid square subdivision color" )
    

    # Load the options from the file, on failure the defaults will be returned.
    self.__optionsDatabase.loadOptionsDatabase()
    self.__processLoadedOptions()

  def __processLoadedOptions(self):
    """ After loading the database, have to get & store each option value """
    
    # Enabled?    
    self.__gridEnabled        = self.__optionsDatabase.get(self.GRID_ENABLED)
    self.__gridArrowNode      = self.__optionsDatabase.get(self.GRID_ARROWNODE)
    self.__gridControlPoints  = self.__optionsDatabase.get(self.GRID_CONTROLPOINTS)

    # Primary Grid
    self.__gridLineSeperation = self.__optionsDatabase.get(self.GRID_PIXELS)
    self.__gridLineColor      = self.__optionsDatabase.get(self.GRID_COLOR)
    self.__gridDotMode        = self.__optionsDatabase.get(self.GRID_DOT_MODE)
    self.__gridWidth          = self.__optionsDatabase.get(self.GRID_SUDIVISIONS_WIDTH)
    
    # Grid Subdivisions
    self.__gridSubdivisions         = self.__optionsDatabase.get(self.GRID_SUDIVISIONS)
    self.__gridLineSubdivisionColor = self.__optionsDatabase.get(self.GRID_SUBDIVISION_COLOR)
    self.__gridSubdivisionShow      = self.__optionsDatabase.get(self.GRID_SUBDIVISION_SHOW)
    self.__gridSubdivisionWidth     = self.__optionsDatabase.get(self.GRID_SUDIVISIONS_WIDTH)
    
  def updateATOM3instance( self, atom3i ):
    self.atom3i = atom3i              # Atom3 instance
    self.dc = self.atom3i.getCanvas()  # Canvas
    
  def settings(self ):
    """ Show the dialog, load the options, snap it on! """
    
    self.__optionsDatabase.showOptionsDatabase()
    self.__processLoadedOptions()
    self.drawGrid()
        
  def drawGrid(self ):
    """ Draws the grid """

    # Do we really want to draw the grid? :D
    if( not self.__gridEnabled ):
      return self.destroy()
    
    # Is the grid already drawn? Wipe it clean, then go at it again!
    elif( self.__gridItemHandlers ):
      self.destroy()
      
    # Starting the Grid up for the first time, let AToM3 know about it...
    else:
      self.__updateMainApp()
    
    canvasBox = self.atom3i.CANVAS_SIZE_TUPLE
    
    # Create the "subdivision grid", this is really just a visual aid
    if( self.__gridSubdivisionShow ):
      subdivisionSeperation = self.__gridLineSeperation * self.__gridSubdivisions 
      for x in range( canvasBox[0], canvasBox[2], subdivisionSeperation ):
        line = self.dc.create_line(x,0,x,canvasBox[3], 
                                  width = self.__gridSubdivisionWidth,
                                  fill=self.__gridLineSubdivisionColor )
        self.__gridItemHandlers.append( line )
                                  
      for y in range( canvasBox[1], canvasBox[3], subdivisionSeperation ):
        line = self.dc.create_line(0,y,canvasBox[2],y,
                                  width = self.__gridSubdivisionWidth,
                                  fill=self.__gridLineSubdivisionColor )
        self.__gridItemHandlers.append( line )
      
    # Create the 'real' grid, this is where snapping occurs 
    
    # Use Dots: less visual clutter but slow since it is O(n^2)
    if( self.__gridDotMode ): 
      for x in range( canvasBox[0], canvasBox[2], self.__gridLineSeperation ):
        for y in range( canvasBox[1], canvasBox[3], self.__gridLineSeperation ):
          oval = self.dc.create_oval( x-self.__gridWidth,y-self.__gridWidth,
                                      x+self.__gridWidth,y+self.__gridWidth, 
                                      width = 0,fill=self.__gridLineColor )
          self.__gridItemHandlers.append( oval )
          
    # Use lines: much faster since it is O(n)
    else:
            
      for x in range( canvasBox[0], canvasBox[2], self.__gridLineSeperation ):
        line = self.dc.create_line(x,0,x,canvasBox[2], 
                                  width = self.__gridWidth,fill=self.__gridLineColor )
        self.__gridItemHandlers.append( line )
                
      for y in range( canvasBox[1], canvasBox[3], self.__gridLineSeperation ):
        line = self.dc.create_line(0,y,canvasBox[3],y, 
                                  width = self.__gridWidth,
                                  fill=self.__gridLineColor )
        self.__gridItemHandlers.append( line )
      
    # Push all this stuff behind what's already on the canvas
    for itemHandler in self.__gridItemHandlers:
      self.dc.tag_lower( itemHandler )
   
    SnapGrid.highestItemHandler = self.__gridItemHandlers[0]
      
  
  def __updateMainApp(self, disableForPrinting = False ):
    """ Updates the main application with information it needs to snap """
    
    if( self.__gridEnabled and not disableForPrinting ):
      self.atom3i.snapGridInfoTuple = ( self.__gridLineSeperation, 
                                       self.__gridArrowNode, 
                                       self.__gridControlPoints )
    else:
      self.atom3i.snapGridInfoTuple = None
    
  def destroy(self, disableForPrinting = False ):
    """ Grid is displayed? Kill it """
    
    SnapGrid.highestItemHandler = None
    if( self.__gridItemHandlers ):
      for itemHandler in self.__gridItemHandlers:
        self.dc.delete( itemHandler )
      self.__gridItemHandlers = []
      
      self.__updateMainApp( disableForPrinting )
      