"""
Postscript.py

Allows the user to specify exactly what portion of the model to export as a
postscript file for printing. Presents an option dialog. Saves postscript of
canvas to file.

Created July 15, 2004 by Denis Dube
"""

import math, tkFileDialog

from OptionDatabase   import OptionDatabase
from OptionDialog     import OptionDialog
from MathUtilities    import point2SegmentDistance
import SnapGrid

class Postscript:
  
  MASK_STIPPLE  = "gray12"
  
  TOP           = 0
  BOTTOM        = 1
  LEFT          = 2
  RIGHT         = 3
  
  # How close you must click to a mask boundary in order to select it
  MIN_SIDE_DIST = 100
  
  # Option Keys
  COLOR_MODE        = 'Color mode'
  ROTATION          = 'Rotation'
  MASK_COLOR_KEY    = 'Mask color'
  TRANSPARENT_MASK  = 'Mask transparency'
  SVG_EXPORT_MODE   = 'SVG export mode'
  
  def __init__(self, atom3i,dc ):
    self.atom3i = atom3i
    self.dc = dc  # <-- Canvas widget
    
    self.__mask = []
    self.__box = None
    self.__boxOutline = None
    self.__activeSide = None
    self.__lastPos = None
    self.__abort = False
    self.__maskColor = "red"
    self.__transparentMask = True
    self.__restoreSnapGrid = False
    
    # Instantiate the Option Database module
    self.__optionsDatabase = OptionDatabase( atom3i.parent,
                  'Options_Postscript.py', 'Postscript Settings',autoSave=True)
     
    # Local methods/variables with short names to make things more readable :D
    newOp = self.__optionsDatabase.createNewOption
    EN    = OptionDialog.ENUM_ENTRY
    L     = OptionDialog.LABEL
    BE    = OptionDialog.BOOLEAN_ENTRY
    CE    = OptionDialog.COLOR_ENTRY
    
    newOp( self.COLOR_MODE, "color", [EN, 'color', 'grey', 'mono'], "Export color mode" ) 
    newOp( self.ROTATION, "portrait", [EN, 'portrait', 'landscape'], "Export rotation" ) 
    newOp( self.MASK_COLOR_KEY, "red", [CE, 'Choose color'], "Boundary mask color" ) 
    newOp( self.TRANSPARENT_MASK, True, BE, "Transparent boundary mask" )
    newOp( 'L0', None, [L, 'times 12','blue','left'], "" )
    newOp( 'L1', None, [L, 'times 12','blue','left'], "After pressing OK, you must select the canvas area to export as postscript" ) 
    newOp( 'L2', None, [L, 'times 12','blue','left'], "You can modify boundaries by left-clicking and moving the mouse around" )
    newOp( 'L3', None, [L, 'times 12','blue','left'], "Right-clicking will set the new boundary position" )
    newOp( 'L4', None, [L, 'times 12','blue','left'], "Right-clicking again will do the actual postscript export" )
  
    newOp( "seperator1", '', OptionDialog.SEPERATOR, '', '')    
    newOp( self.SVG_EXPORT_MODE, True, BE, "Export to SVG instead of postscript")
    newOp( 'L5', None, [L, 'times 12','blue','left'], "NOTE: SVG exports selected items only (if no selection then entire canvas)" )
    
    # Load the options from the file, on failure the defaults will be returned.
    self.__optionsDatabase.loadOptionsDatabase()
    self.__processLoadedOptions()
     
  def __processLoadedOptions(self):
    """ After loading the database, have to get & store each option value """ 
    self.__colormode        = self.__optionsDatabase.get(self.COLOR_MODE)
    self.__rotation         = self.__optionsDatabase.get(self.ROTATION)
    self.__maskColor        = self.__optionsDatabase.get(self.MASK_COLOR_KEY)
    self.__transparentMask  = self.__optionsDatabase.get(self.TRANSPARENT_MASK)
    self.__svgExportMode    = self.__optionsDatabase.get(self.SVG_EXPORT_MODE)
    
  def enteringPostscript( self ):
    if( self.__abort ):
      self.atom3i.UI_Statechart.event( "Done" )     
    
  def createMask( self, pos ):
    """ 
    Creates 4 transparent rectangles that mask out what won't be included in 
    the postscript generation.
    """  
    
    # Pos could be an event or a [x,y] list
    if( type( pos ) != type( list() ) ):
      pos = [pos.x, pos.y]
  
    minX,minY, maxX,maxY = self.atom3i.CANVAS_SIZE_TUPLE    
    
    # Uh oh snap grid is on! This will mess up the boundary calculation!
    if( self.atom3i.snapGridInfoTuple ):
      self.atom3i.disableSnapGridForPrinting(True)
    self.__box = self.dc.bbox('all') 
 
    # Do we have an initial boundary box? Did the options dialog get OK'd?
    if( self.__box and self.__optionsDatabase.showOptionsDatabase( pos ) ):
      x0,y0, x1,y1 = self.__box
      self.__processLoadedOptions()
      
      if(self.__svgExportMode):
        self.exportSVG()
        self.__abort = True
        return
      else:
        self.__abort = False
      
    # Error! Cancel! Abort!
    else:
      self.__abort = True
      return
    
    # The boundary box outline
    self.__boxOutline = self.dc.create_rectangle(x0,y0,x1,y1, 
                                          outline = 'black',fill='', width=1) 
          
    # Use transparent boundary mask? It's somewhat slower...
    if( self.__transparentMask ):  stipple = self.MASK_STIPPLE
    else:                          stipple = ''
          
    # The masks on the 4 sides of the boundary box
    topBox = self.dc.create_rectangle( minX,minY, maxX, y0, outline = '',
                      fill=self.__maskColor,stipple=stipple, width=1) 
    botBox = self.dc.create_rectangle( minX,y1, maxX, maxY, outline = '',
                      fill=self.__maskColor,stipple=stipple, width=1) 
    leftBox = self.dc.create_rectangle( minX,minY, x0, maxY, outline = '',
                      fill=self.__maskColor,stipple=stipple, width=1) 
    rightBox = self.dc.create_rectangle( x1,minY, maxX, maxY, outline = '',
                      fill=self.__maskColor,stipple=stipple, width=1) 
          
    self.__mask = [topBox,botBox,leftBox,rightBox ]
                                       
  def destroy( self ):
    """ Reset everything back to defaults & remove stuff from canvas """
    for item in self.__mask:
      self.dc.delete( item )
    self.__mask = []
    self.__box = None
    self.__activeSide = None
    self.dc.delete( self.__boxOutline ) 
    self.__boxOutline = None
    
  def setActiveSide( self, pos ):
    """ 
    Sets the nearest side of the bounding box to active modification 
    Side must be within a certain distance of the given position, or the side
    will not be selected, and False will be returned.
    """
        
    x,y = self.__lastPos = pos    
    x0,y0,x1,y1 = self.__box    
    xDist = abs( x1-x0 )
    yDist = abs( y1-y0 )
    closestHitDist = self.MIN_SIDE_DIST 
    closestHitIndex = None
       
    # Quick but not so great method
    if( 0 ):
      # Use top box line
      if(   y < y0 ): self.__activeSide = self.TOP
      
      # Use right box line
      elif( x > x1 ): self.__activeSide = self.RIGHT
        
      # Use bottom box line
      elif( y > y1 ): self.__activeSide = self.BOTTOM
      
      # Use left box line
      else:           self.__activeSide = self.LEFT
      return True
    
    # Slower but more interactive method
    else:
      # Distance to the left-most bounding box segment
      dist = point2SegmentDistance(x,y, x0,y0,x0,y0+yDist)
      if( dist < closestHitDist ): 
        closestHitDist = dist
        closestHitIndex = self.LEFT
      # Distance to the right-most bounding box segment
      dist = point2SegmentDistance(x,y, x1,y0,x1,y0+yDist)
      if( dist < closestHitDist ): 
        closestHitDist = dist
        closestHitIndex = self.RIGHT
      # Distance to the top-most bounding box segment
      dist = point2SegmentDistance(x,y, x0,y0,x0+xDist,y0)
      if( dist < closestHitDist ): 
        closestHitDist = dist
        closestHitIndex = self.TOP
      # Distance to the bottom-most bounding box segment
      dist = point2SegmentDistance(x,y, x0,y1,x0+xDist,y1)
      if( dist < closestHitDist ): 
        closestHitDist = dist
        closestHitIndex = self.BOTTOM
      
      if( closestHitIndex != None ):
        self.__activeSide = closestHitIndex 
        return True
      else:
        self.__activeSide = None
        return False

  def inMotion( self, pos ):
    """ Moves the active side of the selection box with the mouse motion """
    
    if( self.__activeSide == None ):  return
    
    oldX, oldY = self.__lastPos
    newX, newY = self.__lastPos = pos
    dx,dy = ( newX - oldX, newY - oldY )
        
    x0,y0,x1,y1 = self.__box 

    # Apply motion delta to the active side
    if( self.__activeSide == self.LEFT ):
      x0 += dx
    elif(self.__activeSide == self.RIGHT ):
      x1 += dx
    elif(self.__activeSide == self.TOP):
      y0 += dy
    elif(self.__activeSide == self.BOTTOM ):
      y1 += dy
      
    minX,minY, maxX,maxY = self.atom3i.CANVAS_SIZE_TUPLE 
    topBox,botBox,leftBox,rightBox = self.__mask
    
    # Move the mask around
    self.dc.coords( topBox,   minX, minY, maxX, y0   )
    self.dc.coords( botBox,   minX, y1,   maxX, maxY )
    self.dc.coords( leftBox,  minX, minY, x0,   maxY )
    self.dc.coords( rightBox, x1,   minY, maxX, maxY )
    
    # Update the box
    self.__box = [ x0,y0,x1,y1 ]
    self.dc.coords( self.__boxOutline, x0,y0,x1,y1 )
        
  def generatePostscript(self, autoSaveToFileName = None):
    """ Generate the printable postscript file using the bounding box """

    if( self.__rotation == "landscape" ):
      rotation = True
    else:
      rotation = False


    if( autoSaveToFileName ):
      
      # Uh oh snap grid is on! This will mess up the boundary calculation!
      if( self.atom3i.snapGridInfoTuple ):
        self.atom3i.disableSnapGridForPrinting(True)
      
      # Bounding box
      b = self.dc.bbox('all') 
      if( b == None ):  
        print 'Bounding box is empty', b, 'for', autoSaveToFileName
        # b = [0,0, 1,1]  # Empty canvas
        return None # Abort
        
      fileName = autoSaveToFileName 
      if(fileName[-4:] != '.eps' and fileName[-3:] != '.ps'):
        fileName += '.eps'

      
    else:
      # Make the box go bye bye
      b = self.__box
      self.destroy()
  
      # No box? No postscript :p
      if( not b or self.__abort ):  return 

      # Save Dialog
      fileName = tkFileDialog.asksaveasfilename(initialfile='x.eps',
                              filetypes=[ ("Encapsulated Postscript", "*.eps"),
                                          ("Postscript", "*.ps")])  
    
    # Canceled!
    if( fileName == '' ): return
    
    
    # This is for lazy people (like me) who don't add the extension :D
    if( fileName[-4:] != '.eps' and fileName[-3:] != '.ps' ):
      fileName += '.ps'
        
    self.dc.postscript( file      = fileName, 
                        x         = b[0], 
                        y         = b[1],
                        width     = b[2] - b[0], 
                        height    = b[3] - b[1],
                        colormode = self.__colormode,
                        rotate    = rotation )
    return b # return the bounding box
    
    
    
  def exportSVG(self):
    """
    Sends selected objects or the entire canvas (if no selection) to the SVG
    exporter and writes the results to a file.
    """
    
    # Save Dialog
    fileName = tkFileDialog.asksaveasfilename(initialfile='x.svg',
                         filetypes=[ ("SVG", "*.svg"), ("All files", "*.*")])  
    
    # Canceled!
    if( fileName == '' ): 
      return
    
    if(fileName[-4:].lower() == '.svg'):
      from AToM3Selection2SVG import AToM3Selection2SVG
      selectionList = self.atom3i.cb.buildSelectionObjectSet()
      if(not selectionList):
        selectionList = []
        for nodeList in self.atom3i.ASGroot.listNodes.values():
          for node in nodeList:
            selectionList.append(node.graphObject_)
      SVGtext = AToM3Selection2SVG(selectionList)
      #print SVGtext
      f = open(fileName, 'w')
      f.write(SVGtext)
      f.close()
       
