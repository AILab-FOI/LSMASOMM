"""
ArrowEditor.py

Creates an overlay over an existing arrow, with big knobs at control points.
The knobs can then be easily selected and moved around very precisely...
Supports pixel accurate movement via the arrow keys.
Supports moving the centerObject label/drawing if in moveLabelDrawingMode mode.

Created June 18, 2004 by Denis Dube
"""


from Utilities        import snapIt
from MathUtilities    import point2SegmentDistance

class ArrowEditor:
  
  CONTROL_POINT_SIZE  = 5
  CONTROL_POINT_COLOR = "red"
  
  INTERMEDIATE_OBJ_COLOR  = "white"
  INTERMEDIATE_OBJ_COLOR2 = "orange"
  INTERMEIDATE_OBJ_TAG    = "intObject"
  
  INNER_ARROW_COLOR = "yellow"  
  INNER_ARROW_WIDTH = 1
  
  OUTER_ARROW_COLOR = "orange" 
  OUTER_ARROW_WIDTH = 3 
  OUTER_ARROW_SHAPE = (15,15,3)
  
  HIGHLIGHT_COLOR = "green"
  HIGHLIGHT_COLOR2 = "yellow"
  
  INT_OBJECT    = 0
  POINT_OBJECT  = 1
  
  EPSILON = 0.1
  
  def __init__(self,canvas, TKroot):
      
    self.dc = canvas
    self.windowRoot = TKroot

    self.innerArrowItem = None
    self.outerArrowItem = None
    self.controlPointItems = []         # (itemHandler, color, type) list
    self.activeControlPointTuple = None # (itemHandler, color, type, index)
    
    self.itemsTuple = None              # (seg1_itemHandler,seg2_itemHandler)
    self.connectedObjects = None        # (objFrom, objTo )
    self.intermediateObject = None
    
    self.lastMousePosition = [0, 0]    
    self.realArrowColor = "black"
    self.realWidth = 1
    
    self.moveLabelDrawingMode = False    
    
    self.abortArrowEditor = False
  
  """ Checks to make sure arrow editing mode is really desired """
  def setArrowEditorAbort(self):
    self.abortArrowEditor = True    
  def enteringArrowEditorMode(self, atom3i, event=None):
    if( self.abortArrowEditor ):
      self.abortArrowEditor = False
      atom3i.UI_scope("Reset", event)
      atom3i.UI_scope("Edit Properties", event)
  def enteringActiveControlPointMode(self, atom3i, event=None):
    if(self.activeControlPointTuple == None ):
      atom3i.UI_scope("Done", event)
  
    
  def getArrowHandler(self):
    return self.itemsTuple[0]
     
  def setMoveLabelDrawingMode(self,mode=True):
    """ Instead of moving the node control point, moves the label around """
    self.moveLabelDrawingMode = mode
    if( mode ):
      self.dc.itemconfigure( self.INTERMEIDATE_OBJ_TAG, fill = self.INTERMEDIATE_OBJ_COLOR2 )
    else:
      self.dc.itemconfigure( self.INTERMEIDATE_OBJ_TAG, fill = self.INTERMEDIATE_OBJ_COLOR )
    
  def isMoveLabelDrawingMode(self):
    return self.moveLabelDrawingMode  
  def toggleMoveLabelDrawingMode(self):
    if( self.moveLabelDrawingMode ):    self.setMoveLabelDrawingMode(False)
    else:                               self.setMoveLabelDrawingMode(True)
    
  def optimalConnectionCheck(self):
    """ Ensures that the endpoints of the arrow use the optimal connectors """
    
    objFrom, objTo = self.connectedObjects
    coords = self.dc.coords( self.innerArrowItem )    
    seg1Item, seg2Item = self.itemsTuple
        
    # Check if first connector is optimal
    if( objFrom.hasConnectors() and not objFrom.isConnectedByNamedPort( self.intermediateObject.semanticObject ) ):
      
      x,y = objFrom.getClosestConnector2Point(objFrom, coords[2],coords[3] )

      if( x != coords[0] or y != coords[1] ):
        # It's not so good now is it... fix the color arrows
        coords = [x,y] + coords[2:]
        apply(self.dc.coords, [self.innerArrowItem] + coords )
        apply(self.dc.coords, [self.outerArrowItem] + coords )
        
        # Fix the "real" segment
        coordsSeg1 = self.dc.coords( seg1Item )
        apply(self.dc.coords, [seg1Item] + [x,y] + coordsSeg1[2:] )
        
      # Check if a link drawing needs moving...
      self.intermediateObject.updateDrawingsTo( x,y, seg1Item )
         
             
    # Now check if the 2nd connector is optimal
    if( objTo.hasConnectors() and not objTo.isConnectedByNamedPort( self.intermediateObject.semanticObject ) ):
        
      x,y = objTo.getClosestConnector2Point(objTo, coords[-4],coords[-3] )
    
      if( x != coords[-2] or y != coords[-1] ):
        # It's not so good now is it... fix the color arrows
        coords = coords[:-2] + [x,y]
        apply(self.dc.coords, [self.innerArrowItem] + coords )
        apply(self.dc.coords, [self.outerArrowItem] + coords )
        
        # Fix the "real" segment
        coordsSeg2 = self.dc.coords( seg2Item )
        apply(self.dc.coords, [seg2Item] + [x,y] + coordsSeg2[2:] )
        
      # Check if a link drawing needs moving...
      self.intermediateObject.updateDrawingsTo( x,y, seg2Item, segmentNumber=2 )
  
  def isArrowSmooth(self):
    seg1Item, seg2Item = self.itemsTuple
    if( self.dc.itemcget(seg1Item, "smooth") != "0" ):
      return True
    elif( self.dc.itemcget(seg2Item, "smooth") != "0" ):
      return True
    return False

  def smoothArrow(self ):
    """ Toggles arrow smoothness on/off """
    seg1Item, seg2Item = self.itemsTuple
    if( self.isArrowSmooth() ):
      # Un-Smooth the Real arrow
      self.dc.itemconfigure(seg1Item, smooth = False, width = self.realWidth, fill = self.realArrowColor )
      self.dc.itemconfigure(seg2Item, smooth = False, width = self.realWidth, fill = self.realArrowColor )
      # Re-enable the color arrows
      self.dc.itemconfigure(self.innerArrowItem , fill = self.INNER_ARROW_COLOR, width = self.INNER_ARROW_WIDTH )
      self.dc.itemconfigure(self.outerArrowItem , fill = self.OUTER_ARROW_COLOR, width = self.OUTER_ARROW_WIDTH )
    else:
      # Smooth the Real arrow
      self.dc.itemconfigure(seg1Item, smooth = True, width = 3, fill = self.OUTER_ARROW_COLOR )
      self.dc.itemconfigure(seg2Item, smooth = True, width = 3, fill = self.OUTER_ARROW_COLOR )
      # Disable the colorful arrow
      self.dc.itemconfigure(self.innerArrowItem , fill = "red",width=1 )
      self.dc.itemconfigure(self.outerArrowItem , fill = "" )
      
    
  def constructEditorArrow(self, seg1coords,seg2coords,itemsTuple, connectedObjects, \
                           intermediateObject, snapGridInfoTuple ):
    """ Creates the colorful editor arrow and the big control knobs """
        
    self.connectedObjects = connectedObjects 
    self.itemsTuple = itemsTuple 
    self.intermediateObject = intermediateObject 
    self.realArrowColor = self.dc.itemcget(itemsTuple[0], "fill")
    self.realWidth = float( self.dc.itemcget(itemsTuple[0], "width") )
    self.moveLabelDrawingMode = False 
    self.snapGridInfoTuple = snapGridInfoTuple
    
    # Out with the old...
    self.removeOldEditorArrow() 
    
    # Segment 1 + Segment 2 minus the duplication of the intermediate point
    fullArrowCoords = seg1coords + seg2coords[2:]
    
    if( len( fullArrowCoords ) >= 6 ):

      # Outer Arrow
      self.outerArrowItem = self.dc.create_line(0,0,0,0, arrow="last" ,
                                        width = 3,fill=self.OUTER_ARROW_COLOR,
                                        arrowshape = self.OUTER_ARROW_SHAPE )
      apply(self.dc.coords, [self.outerArrowItem] + fullArrowCoords )
      
      # Inner Arrow
      self.innerArrowItem = self.dc.create_line(0,0,0,0,
                                        width = 1,fill=self.INNER_ARROW_COLOR )
      apply(self.dc.coords, [self.innerArrowItem] + fullArrowCoords )
            
      # Control points in segment 1
      self.constructArrowControlPoint( seg1coords[2:-2], 1 )
      # Intermediate object control point 
      self.constructArrowControlPoint( seg1coords[-2:], 0, isIntermediateObject = True )
      # Control points in segment 2
      self.constructArrowControlPoint( seg2coords[2:-2], 2 )
          
      # I know, this doesn't look right, but it's not as bad as it looks :D
      self.smoothArrow()
      self.smoothArrow()
      
      # Check if the connections are nice...
      self.optimalConnectionCheck()
      
      self.moveActionTriggerHack()
      
    else:
      raise Exception, "Invalid arrow sent to the arrow editor, only " \
                        + str( len( coords ) ) + " coordinates!"

  def constructArrowControlPoint(self,innerCoords,segNum, isIntermediateObject = False ):
    """ Places large control knobs to make control points obvious """
    
    lengthOfCoords = len( innerCoords )
    for i in range( 0, lengthOfCoords, 2):        
      x = innerCoords[i] - self.CONTROL_POINT_SIZE 
      y = innerCoords[i+1] - self.CONTROL_POINT_SIZE 
      
      # This is an intermediate object
      if( isIntermediateObject ):
        color = self.INTERMEDIATE_OBJ_COLOR
        type = self.INT_OBJECT
        controlPoint = self.dc.create_rectangle( x,y,
                                          x+self.CONTROL_POINT_SIZE*2,
                                          y+self.CONTROL_POINT_SIZE*2,
                                          fill=color,
                                          outline="black",
                                          tag = self.INTERMEIDATE_OBJ_TAG )
      # This is a control point
      else:
        color = self.CONTROL_POINT_COLOR
        type = self.POINT_OBJECT
        controlPoint = self.dc.create_oval ( x,y,
                                          x+self.CONTROL_POINT_SIZE*2,
                                          y+self.CONTROL_POINT_SIZE*2,
                                          fill=color,
                                          outline="black",
                                          tag = "Seg"+str(segNum) )                                            
                                                    
      self.controlPointItems.append( (controlPoint,color,type) )
    
      

  def removeOldEditorArrow(self):
    """ Cleanup services... because someone's gotta do it """
    # Delete the outer arrow
    if( self.outerArrowItem ):
      self.dc.delete( self.outerArrowItem )
      self.outerArrowItem = None
    # Delete the inner arrow
    if( self.innerArrowItem ):
      self.dc.delete( self.innerArrowItem )
      self.innerArrowItem  = None
    # Delete the control knobs
    if( self.controlPointItems ):
      for controlPoint,color,type in self.controlPointItems:
        self.dc.delete( controlPoint )
      self.controlPointItems = []
    # Delete the active control knob
    self.clearActiveControlPoint()
    # Reset the main arrow color    
    seg1Item, seg2Item = self.itemsTuple
    self.dc.itemconfigure( seg1Item, fill=self.realArrowColor,width=self.realWidth )
    self.dc.itemconfigure( seg2Item, fill=self.realArrowColor,width=self.realWidth )
    
  def isActiveControlPoint(self):
    return self.activeControlPointTuple != None
    
  def clearActiveControlPoint(self):
    """ Disable Highlighting on last active controlPoint, then nullify it """
    if( self.activeControlPointTuple ):
      self.highlight( self.activeControlPointTuple, 0 )
      self.activeControlPointTuple = None
      
  def setNearestControlPointActive(self, items):
    """ Sets the active control point to the nearest one from the items tuple """
    #todo: calc distance to make sure it is the nearest one, useful 0.1% of the time...
    for itemHandler in items:
      i = 0
      for controlPointTuple in self.controlPointItems:
        if( itemHandler == controlPointTuple[0] ):  
          # Disable Highlighting on last active controlPoint
          self.clearActiveControlPoint()  
                
          # Enable Highlighting on new control point
          knobTag = self.dc.gettags( itemHandler )
          if( knobTag and knobTag[0] == self.INTERMEIDATE_OBJ_TAG ):
            self.highlight( controlPointTuple, 2 )  
          else:
            self.highlight( controlPointTuple, 1 )  
          # Save the new control point
          self.activeControlPointTuple = controlPointTuple + (i,)
          return True
        i += 1
    return False
  
    
  
  def deleteControlPoint(self,pos):
    """ Deletes the control point nearest to pos """
    if( self.activeControlPointTuple ):
      itemHandler,c,type, index = self.activeControlPointTuple
      
      # Is this an intermediate object? Your not deleting that!
      if( type == self.INT_OBJECT ):
        return
      
      coords = self.dc.coords( itemHandler )
      cpX = coords[0] + self.CONTROL_POINT_SIZE 
      cpY = coords[1] + self.CONTROL_POINT_SIZE 
      
      # Remove the point from the controlPointItems and from active duty
      self.controlPointItems = self.controlPointItems[:index] + self.controlPointItems[index+1:]
      self.clearActiveControlPoint()
      
      # Remove the contrl point knob
      self.dc.delete( itemHandler )
      
      # Remove Point from colorful arrows...
      coords = self.dc.coords( self.innerArrowItem )
      i = (index + 1) * 2
      coords = coords[:i] + coords[i+2:]
      self.dc.coords( * [self.innerArrowItem] + coords )
      self.dc.coords( * [self.outerArrowItem] + coords )
      
      
      # Now update the "Real" arrow
      seg1Item,seg2Item = self.itemsTuple
      coords = self.dc.coords( seg1Item )
      seg1Length = len( coords ) 
      # The first segment is where the new point is going
      if( seg1Length > i ):
        coords = coords[:i] + coords[i+2:]    
        self.dc.coords( * [seg1Item] + coords )
        
      # The second segement is where the new point is going
      else:          
        coords = self.dc.coords( seg2Item )
        seg2Length = len(coords)
        # Why does this work? I dunno... I'm sure theres a good reason though.
        #print i, seg1Length,seg2Length
        i = seg2Length - 2 - (i+2 - seg1Length )
        #print coords[:i] , coords[i+2:]  , i
        coords = coords[:i] + coords[i+2:]     
        self.dc.coords( * [seg2Item] + coords )
        
      # Check if the connections are nice...
      self.optimalConnectionCheck()
      
  def moveActionTriggerHack(self):
    # Just to warn stuff that do graphical updates on this trigger
    try:
      semObj = self.intermediateObject.semanticObject
      asg = semObj.parent.ASGroot
      semObj.postAction(asg.MOVE, 0,0,0,0)
    except:
      pass
    
  def setMousePosition(self,event):
    self.lastMousePosition = self.getCanvasCoords( event )
           
  def setInMotion(self,event):
    """ Normal drag operation using mouse motion """
    x0,y0 = self.lastMousePosition
    x1,y1 = self.lastMousePosition = self.getCanvasCoords( event )
    
    # If not dragging anything, no point continuing
    if( not self.activeControlPointTuple ):  return
    
    self.dragOps(  x0,y0, x1,y1 )
    self.moveActionTriggerHack()
    
            
  def dragOps(self, x0,y0, x1,y1, mouseMove = True ):
    """ Drag operation on a control point knob """
    
    deltaX, deltaY = (x1-x0,y1-y0)   
    knob, color, type, index = self.activeControlPointTuple

    knobTag = self.dc.gettags( knob )
    if( not knobTag ): raise Exception, "No tag, no game!"
    
    # Move the "real" arrow. 
    # Step 1: If the knob is the center object of the link
    if( knobTag[0] == self.INTERMEIDATE_OBJ_TAG ):
      
      obj = self.intermediateObject
      # Move the label/drawing attached to the node
      if( self.moveLabelDrawingMode ):
        if( obj.centerObject ):
          obj.centerObject.Move(deltaX, deltaY, 0)	
          
          # Save the offest as a graphical layout constraint for model save/load
          if( not obj.layConstraints.has_key( 'Label Offset' ) ):
            obj.layConstraints['Label Offset'] = [deltaX,deltaY]
          else:
            dx,dy = obj.layConstraints['Label Offset']
            obj.layConstraints['Label Offset'] = [dx+deltaX,dy+deltaY]
            
          return
        
      # Move the actual node & dependencies using the obj.Move method
      else: 
        
        # Snap grid: snap the intermediate object
        if( self.snapGridInfoTuple and mouseMove ):
          gridSize, snapArrowNode, snapControlPoints = self.snapGridInfoTuple
          if( snapControlPoints ):
            cpX,cpY = obj.getCenterCoord()
            x1 = snapIt( cpX+deltaX,x1,gridSize)
            y1 = snapIt( cpY+deltaY,y1,gridSize)         
            self.lastMousePosition = [x1,y1]
            deltaX, deltaY = (x1-x0,y1-y0) 
              
        obj.setCenterSelect()
        obj.Move( deltaX, deltaY  )
    
    # Step 2: If the knob is a regular control point, use the hacky method
    elif( knobTag[0][:3] == "Seg" ):
      controlPointCoords = self.dc.coords(knob)
      cpX = controlPointCoords[0] + self.CONTROL_POINT_SIZE 
      cpY = controlPointCoords[1] + self.CONTROL_POINT_SIZE 
      
      # Snap grid: snap the dragged control points
      if( self.snapGridInfoTuple and mouseMove ):
        gridSize, snapArrowNode, snapControlPoints = self.snapGridInfoTuple
        if( snapControlPoints ):
          x1 = snapIt( cpX+deltaX,x1,gridSize)
          y1 = snapIt( cpY+deltaY,y1,gridSize)         
          self.lastMousePosition = [x1,y1]
          deltaX, deltaY = (x1-x0,y1-y0) 
          
      # Segment 1 coordinates 
      seg1Coords = self.dc.coords( self.itemsTuple[0] )
      # Segment 1 length minus the starting point and the intermediate object
      seg1Len = len( seg1Coords[2:-2] )      
      
      # Segment 1
      if( knobTag[0][-1:] == "1" ):
             
        # Failure case that will never happen... really... it won't... 
        if( index*2 > seg1Len ): raise Exception, "Noooooo! Don't do it Bun-Bun!"
        
        seg1Coords[index*2+2]   += deltaX
        seg1Coords[index*2+3]   += deltaY
        self.dc.coords( * [self.itemsTuple[0]] + seg1Coords )   
        
      # Segment 2
      elif( knobTag[0][-1:] == "2" ): 
        seg2Coords = self.dc.coords( self.itemsTuple[1] )
 
               
        # Segment 2 coordinates minus the starting point and the intermediate object
        seg2Len = len( seg2Coords[2:-2] ) 
        normalizedIndex = index * 2 - seg1Len - 2  # Subtract seg1  & inter. object   
        
        # Failure cases that should *never* happen
        if( normalizedIndex > seg2Len ): raise Exception, "Noooooo! Don't do it Bun-Bun."
        elif( normalizedIndex < 0 ): raise Exception, "Beware the kitten..."
        
        # Flip the index because of some really freaky reversal
        normalizedIndex = seg2Len - normalizedIndex
        
        seg2Coords[normalizedIndex]     += deltaX
        seg2Coords[normalizedIndex+1]   += deltaY
        self.dc.coords( * [self.itemsTuple[1]] + seg2Coords )  
       
      # It will always be segment 1 or 2... or I'm gonna get embarassed here...
      else:
        raise Exception, "Game called on account of naked chick (see www.sluggy.com)."
      
    # Since all knobs are given a tag, this won't happen...
    else:
      raise Exception, "No tag, no game!"
            
    # Move the Control Point Knob
    controlPointCoords = self.dc.coords(knob)
    self.dc.move(knob,deltaX, deltaY  )
    
    # Move the colorful arrows...
    coords = self.dc.coords( self.innerArrowItem )
    coords[ (index + 1) * 2 ] += deltaX
    coords[ (index + 1) * 2 + 1 ] += deltaY
    self.dc.coords( * [self.innerArrowItem] + coords )
    self.dc.coords( * [self.outerArrowItem] + coords )

    # Make sure connections are nice (snap the end points to closest connector)
    self.optimalConnectionCheck()

      
  def insertControlPoint(self,pos):
    """ 
    Inserts a new control point at the given position, in the segment of the
    arrow that is nearest to this position
    """
    
    self.clearActiveControlPoint() # <--- It would just get messed up otherwise
    closestDist = 900000
    closestIndex = -1
    coords = self.dc.coords( self.innerArrowItem )
    length = len(coords)
        
    # Finds the closest and 2nd closest coordinates to the given position
    for i in range(0,length-2,2):
      dist = point2SegmentDistance( pos[0],pos[1],
                                         coords[i],coords[i+1],
                                         coords[i+2],coords[i+3] )
      if( dist < closestDist ):
        closestDist = dist 
        closestIndex = i+2

          
    # Insert the new point into the color arrows...
    coords = coords[:closestIndex] + pos + coords[closestIndex:]    
    apply(self.dc.coords, [self.innerArrowItem] + coords )
    apply(self.dc.coords, [self.outerArrowItem] + coords )
    
    # Insert the new control point...
    x = pos[0] - self.CONTROL_POINT_SIZE 
    y = pos[1] - self.CONTROL_POINT_SIZE 
    color = self.CONTROL_POINT_COLOR  
    # To which segment does this control point belong?  
    if( len( self.dc.coords( self.itemsTuple[0] ) )  > closestIndex ):  segNum = 1
    else:                                                               segNum = 2
    controlPoint = self.dc.create_oval ( x,y,
                                            x+self.CONTROL_POINT_SIZE*2,
                                            y+self.CONTROL_POINT_SIZE*2,
                                            fill=color ,
                                            outline="black",
                                            tag = "Seg"+str(segNum) )
    i = closestIndex / 2 - 1
    self.controlPointItems = self.controlPointItems[:i] + \
                              [(controlPoint,color,self.POINT_OBJECT)] + \
                              self.controlPointItems[i:]    
    
    # Make the control point active
    self.lastMousePosition = pos
    self.setNearestControlPointActive( (controlPoint,) )

        
    # Now update the "Real" arrow
    seg1Item,seg2Item = self.itemsTuple
    coords = self.dc.coords( seg1Item )
    seg1Length = len( coords ) 
    # The first segment is where the new point is going
    if( segNum == 1 ):
      coords = coords[:closestIndex] + pos + coords[closestIndex:]    
      apply(self.dc.coords, [seg1Item] + coords )
      
    # The second segement is where the new point is going
    else:          
      coords = self.dc.coords( seg2Item )
      seg2Length = len(coords)
      # Why does this work? I dunno... I'm sure theres a good reason though.
      i = closestIndex - seg1Length
      i = seg2Length - 2 - i
      innerCoords = coords[2:i] + pos + coords[i:-2]
      #print innerCoords, coords, i
      coords = coords[:2] + innerCoords + coords[-2:]     
      #closestIndex = seg2Length - 2 - (closestIndex - seg1Length )
      #coords = coords[:closestIndex] + pos + coords[closestIndex:]     
      apply(self.dc.coords, [seg2Item] + coords )

  def highlight(self, controlPointTuple, flag ):
    """ 
    Turns highlighting on/off according to flag, on controlPointTuple
    controlPointTuple is, at minimum, a tuple with an itemHandler and a color
    """
    if( flag == 1):
      self.dc.itemconfigure( controlPointTuple[0], fill=self.HIGHLIGHT_COLOR )
    elif( flag == 2):
      self.dc.itemconfigure( controlPointTuple[0], fill=self.HIGHLIGHT_COLOR2 )
    elif( controlPointTuple[2] == self.INT_OBJECT and self.moveLabelDrawingMode ):
      self.dc.itemconfigure( controlPointTuple[0], fill = self.INTERMEDIATE_OBJ_COLOR2 )
    else:
      self.dc.itemconfigure( controlPointTuple[0], fill=controlPointTuple[1] )
      
  # Canvas Coordinate converter
  def getCanvasCoords(self,event):
    return [self.dc.canvasx(event.x),self.dc.canvasy(event.y)]

