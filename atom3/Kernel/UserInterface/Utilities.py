"""
Utilities.py

Collection of methods that aren't callbacks but used by the callbacks.
The optimizeConnectionPorts method is particularly important, and is used by
various layout algorithms.

Created June 30, 2004 by Denis Dube
"""

import re, string, os
from random               import randint

from MathUtilities        import vectorLength2D, getMidpoint2D
from ModelSpecificCode    import isConnectionLink, isEntityNode

SEGMENT_SEARCH_PATTERN    = re.compile( 'Seg' )


def selectAllVisibleObjects( self ):
  
  cb = self.cb 
  itemsTuple = cb.getCanvas().find_all()
  
  # Convert the itemsTuple to a LIST
  selected = []
  for itemHandler in itemsTuple:
    # Only add items that are visible
    if( cb.isItemVisible( itemHandler ) ):
      selected.append( itemHandler )
      
  # Store the objects
  cb.updateSelectionDict( selected )
  
  # Enable highlighting on selected items
  cb.highlighter(1)  


def modelChange( self ):
  """ Triggered whenever the UI does something that intrinsically changes the model """

  # If allowing undos, then save whenever model changes
  self.undoer.modelMofificationOccured()
  
  # Change the status bar!
  self.statusbar.event(self.statusbar.MODEL, self.statusbar.MODIFY)
  




def arrowAbortion(self):
  """ Destroys the arrow and resets the selection mode """
  self.pilotArrow.removeArrow()
    
 
def snapIt( objCoord, mouseCoord, gridSize ):
  """ Returns the 1D coordinate nearest to the grid """
  
  snapDist = objCoord % gridSize
  if( snapDist >= (gridSize/2) ): 
    return mouseCoord + gridSize - snapDist
  else: 
    return mouseCoord - snapDist
  

def snapNewEntity( self, newEntity, pos ):
  """ Snaps a newly added entity to the snap grid """
  # Called only by ASG.addNode() and interactively (not during model load)
  
  gridSize = self.snapGridInfoTuple[0]
   
  # Snap the top-left of the object
  x = newEntity.x
  y = newEntity.y 
  sx, sy = [ snapIt( x, x, gridSize), snapIt( y, y, gridSize) ]
  newEntity.Move( sx-x, sy-y )
  
  #todo: new qoca
  # Initiates an automatic QOCA re-solve, since snap screws things up...
  if(self.qocaAutosolve):    
    varValueList = []
    obj = newEntity
    if(obj.qcX.get() != obj.x):
      varValueList.append((obj.qcX, obj.x))
    if(obj.qcY.get() != obj.y):
      varValueList.append((obj.qcY, obj.y))  
#    print 'suggesting'
#    for (var,value) in varValueList:
#      print var, var.name, value
    self.qocaSolver.suggestVarValue(varValueList)    
    self.qocaSolver.resolve()
    self.qocaSolver.endEdit()
  
  '''
  # SNAP TO CENTER OF OBJECT
  # NOTE: Center snap causes problems when saving/loading models because it is 
  # applied to new nodes created by loading a model.  See ASG.py, addNode()
  
  # Move the entity so that it appears centered on the mouse position
  cx,cy = newEntity.getCenterCoord()            
  newEntity.Move( pos[0] - cx, pos[1] - cy )
  
  # Move the entity so that it is snapped to the grid
  cx,cy = newEntity.getCenterCoord()    
  sx,sy = [ snapIt( cx,cx,gridSize), snapIt( cy,cy,gridSize) ]
  newEntity.Move( sx-cx,sy-cy )
  '''
  
          
def optimizeConnectionPorts(self, entityList = None, linkObjectList=None, 
                            doAllLinks = False, cb=None ):
  """ 
  Ensures that the endpoints of the arrows use the optimal connectors 
  Applied only to selected arrows and to the arrows attached to selected nodes
  Does not move arrows attached to named ports :D
  
  4 Modes of operation:
  i) Given entityList, a list of nodes, the links between them will be optimized
  ii) Given linkObjectList, a list of edge graph objects, the links are optimized
  iii) Given doAllLinks, a boolean and self=atom3i, optimizes all links on the canvas
  iv) Given self=atom3i or cb=cb, will optimize everything currently selected on the canvas
  
  NOTES:
  a) self argument should be atom3 instance, required if doAllLinks=True, otherwise, cb=cb is acceptable
  b) cb is an instance of CallbackState
  """
    
  if( not cb ):
    cb = self.cb
  dc = cb.getCanvas() 
  
  # Step 1A: Given entities, not a selection dict, so get all affected links
  if( entityList ): 
    
    augmentedSelection = dict()
    
    # List of node/entity objects
    for obj in entityList:      
      # Any one of its links may need optimization
      augmentTheSelection( dc, obj, augmentedSelection )
        
  # Step 1B: Given list of link objects
  elif( linkObjectList ):
      
    augmentedSelection = dict()  
      
    for linkObject in linkObjectList:	  
      
      linkTag = linkObject.tag + "1stSeg0"        
      itemHandler = dc.find_withtag( linkTag ) 
      if( not itemHandler ):
        print "WARNING: Utilities.optimizeConnectionPorts() cannot find item with tag", linkTag
        continue
#        raise Exception, "optimizeConnectionPorts() having trouble playing " \
#                         + "tag, Step 1B (Try save & load)"

      # Add to the selection, {tag : [itemHandler, Object] }
      augmentedSelection[ linkTag ] = [ itemHandler[0], linkObject ]
        
  # Step 1C: Find all the links!
  elif( doAllLinks ):
    
    augmentedSelection = dict()
    
    nodeTypes = self.ASGroot.nodeTypes
    listNodes = self.ASGroot.listNodes 
    for nodetype in nodeTypes:	
      if( listNodes[nodetype] ):
        if( isConnectionLink( listNodes[nodetype][0].graphObject_ ) ):  
            
          # Iterate over all the links only
          for node in listNodes[nodetype]:	  
      
            linkTag = node.graphObject_.tag + "1stSeg0"        
            itemHandler = dc.find_withtag( linkTag ) 
            if( not itemHandler ):
              print "WARNING: itemhandler not found! Utilities.py --> " \
                    + "optimizeConnectionPorts() fails (Try save & load)"
              continue
              
            # Add to the selection, {tag : [itemHandler, Object] }
            augmentedSelection[ linkTag ] = [ itemHandler[0], node.graphObject_ ]
    
    
  # Step 1D: Augment the selection with links affected by the node movement 
  #          & remove nodes 
  else: 
     
    selection = cb.getSelectionDict()
    augmentedSelection = selection.copy() # <--- This copy() is soooo important
  
    for tag in selection:
      itemHandler, obj = selection[tag]    
      
      # This is a NODE
      if( isEntityNode( obj ) ):
        
        # Any one of its links may need optimization
        augmentTheSelection( dc, obj, augmentedSelection )
       
        # We don't need to optimize nodes, just links... so... bye bye node
        del augmentedSelection[tag]    

  # Step 2: Optimize all the selected links
  for tag in augmentedSelection:
    
    obj = augmentedSelection[tag][1]
    baseTag = obj.tag # Ex: Obj3 , the tag of the intermediate link object
  
    
    # Some links have center objects (labels/drawings) that look way better
    # if they are above the arrow
    centerObj = obj.getCenterObject()
    if( centerObj ):
      dc.tag_raise(centerObj.tag )
    
    
    # Find all the entities that the edge is linking to 
    # (general enough to handle hyperedges)
    objectsFrom = []
    objectsTo = []    
    semObject = obj.getSemanticObject()
    arrowArrowCase = False
    for semObj in semObject.in_connections_: 
      if(isConnectionLink(semObj.graphObject_)):
        arrowArrowCase = True
      objectsFrom.append( semObj.graphObject_ )
    for semObj in semObject.out_connections_: 
      if(isConnectionLink(semObj.graphObject_)):
        arrowArrowCase = True
      objectsTo.append( semObj.graphObject_ )
      
    # Arrow connected to another arrow, this isn't handled!!!
    if(arrowArrowCase):
      continue
  
    # Initial point/s in the connection ---> Object/s From
    for i in range(0, len(objectsFrom) ):
      
      # Get the tag & itemhandler for each from segement
      segTag = baseTag + "1stSeg" + str(i)
      itemHandler = dc.find_withtag( segTag )
      if( not itemHandler ): 
        print "WARNING: Having problems looking up canvas tags!", segTag
        continue
        #raise Exception, "Having problems looking up canvas tags!"
            
      coords = dc.coords( itemHandler )
      objFrom = objectsFrom[i]
      
      # If the object has connectors and they are not NAMED connectors
      if( objFrom.hasConnectors() and 
          not objFrom.isConnectedByNamedPort( obj.semanticObject ) ):
          
        # Snap to the nearest connection port if not already there
        # NOTE: the [obj.x,obj.y] part makes sure we connect directly 
        #       to the intermediate object
        x, y = objFrom.getClosestConnector2Point(objFrom, coords[2],
                                                 coords[3])    
        if( x != coords[0] or y != coords[1]  ):        
          dc.coords(* [itemHandler] + [x, y] + coords[2:-2] + [obj.x, obj.y])
          
          # Check if a link drawing needs moving...
          obj.updateDrawingsTo( x, y, itemHandler[0] )
  
      
    # Final point/s in the connection ---> Object/s To
    for i in range(0, len(objectsTo) ):
      
      # Get the tag & itemhandler for each to segement
      segTag = baseTag + "2ndSeg" + str(i)
      itemHandler = dc.find_withtag( segTag )
      if( not itemHandler ): 
        print "WARNING: Having problems looking up canvas tags!", segTag
        continue
        #raise Exception, "Having problems looking up canvas tags!"
      itemHandler = itemHandler[0]
            
      coords = dc.coords( itemHandler )
      objTo = objectsTo[i]
        
      if( objTo.hasConnectors() and 
          not objTo.isConnectedByNamedPort( obj.semanticObject ) ):
          
        # Snap to the nearest connection port if not already there
        # NOTE: the [obj.x,obj.y] part makes sure we connect directly to the 
        #       intermediate object
        x, y = objTo.getClosestConnector2Point(objTo, coords[2], coords[3])   
        if( x != coords[0] or y != coords[1]  ): 
          dc.coords(* [itemHandler] + [x, y] + coords[2:-2] + [obj.x, obj.y])
          
          
          # Check if a link drawing needs moving...
          obj.updateDrawingsTo( x, y, itemHandler, segmentNumber=2 )

          
def augmentTheSelection( dc, obj, augmentedSelection ):
  """ 
  Adds the given link to the augmented selection dictionary 
  Subroutine for optimizeConnectionPorts
  """
  
  for linkTuple in obj.connections:
  
    if( linkTuple[-1] == None ):   
#      print 'WARNING: Utilities.augmentTheSelection(), None object found and skipped'
#      print 'linkTuple', linkTuple
      continue
    linkTag = linkTuple[-1].tag
          
    # Need the tag on one of the segments, not the intermediate object...
    if( not SEGMENT_SEARCH_PATTERN.search( linkTag ) ):
      linkTag += "1stSeg0"
    
    # If the link is not already selected
    if( not augmentedSelection.has_key( linkTag ) ):
      itemHandler = dc.find_withtag( linkTag ) 
      
      if( not itemHandler ):
        print 'WARNING: Utilities.augmentTheSelection() cannot find tag', linkTag
        continue
#        raise Exception, "optimizeConnectionPorts() having trouble playing " \
#                        + "tag (Try save & load)"
        
      # Add to the selection, {tag : [itemHandler, Object] }
      augmentedSelection[ linkTag ] = [ itemHandler[0], linkTuple[-1] ]
    
    
def optimizeLinks( cb, setSmooth = True, setCurved = 10, selectedLinks=list(), 
                  curveDirection=-1 ):
  """
  Optimizes the links associated with the nodes in entityList or all the nodes
  in the graph if entityList is not provided.
  The links are set straight, with the endpoints at the nearest connectors of
  the nodes they connect.
  Optionally, additional control points can be added to make a smooth arrow,
  and give it some curvature (setCurved is a pixel distance perpendicular to 
  what would have been a straight arrow ). 
  It is possible to pass a list of link objects directly, and optimize those.
  It is also possible to specify the direction of the curve, Random=-1, Right=0, Left=1
  
  Created July 25, 2004 by Denis Dube
  """
  
  dc = cb.getCanvas() 
  
  # Step 1: Find the selected links 
  if( not selectedLinks ):
    selection = cb.getSelectionDict()
    selectedLinks = []
  
    for tag in selection:
      itemHandler, obj = selection[tag]    
      
      # This is a Link
      if( isConnectionLink( obj ) ):
        if( obj not in selectedLinks ):
          selectedLinks.append(  obj )
              
        
  # Step 2: Optimize all the selected links
  for obj in selectedLinks:
          
    # Optimize the end point connection ports
    optimizeConnectionPorts( None, linkObjectList=selectedLinks, cb=cb ) 
    
    # Find all the entities that the edge is linking to 
    # (general enough to handle hyperedges)
    objectsFrom = []
    objectsTo = []    
    semObject = obj.semanticObject #obj.getSemanticObject()
    if(not semObject):
      continue
    arrowArrowCase = False
    for semObj in semObject.in_connections_: 
      if(isConnectionLink(semObj.graphObject_)):
        arrowArrowCase = True
      objectsFrom.append( semObj.graphObject_ )
    for semObj in semObject.out_connections_: 
      if(isConnectionLink(semObj.graphObject_)):
        arrowArrowCase = True
      objectsTo.append( semObj.graphObject_ )
      
    # Arrow connected to another arrow, this isn't handled!!!
    if(arrowArrowCase):
      continue
    
    # Edge with 2 endpoints
    if( len( objectsFrom ) == 1 and len( objectsTo ) == 1  ):
       
      # Edge with both endpoints on one object
      if( objectsFrom[0] == objectsTo[0] ):
        optimizeSelfLink(dc, obj, objectsFrom[0], setSmooth, setCurved)
      
      # Regular edge
      else:
        optimizeRegularLink( dc, obj, objectsFrom[0], objectsTo[0], 
                              setSmooth, setCurved, curveDirection  )
            
    # Hyper-edge with multiple endpoints
    else:
      optimizerHyperLink( dc, obj, objectsFrom, objectsTo, setSmooth, 
                         setCurved, curveDirection  )
      
      
def optimizerHyperLink( dc, interObj, objectsFrom, objectsTo, 
                        setSmooth, curvature, curveDirection, newCenter=None ):
  """ Optimizes one hyper-edge with multiple endpoints in multiple objects """
  #todo: WARNING: the link decoration mover is *UNTESTED* in this method
 
  baseTag = interObj.tag 

  if(newCenter == None):
    # Find the new center point of the hyper-edge
    newCenter = [0, 0]
    # All objects... but no duplicates (ie: if a self-link occurs)
    allObjects = []
    for obj in objectsFrom + objectsTo:
      if(obj not in allObjects):
        allObjects.append(obj) 
    # Find the avg pos of all these objs
    for obj in allObjects:
      x, y = obj.getCenterCoord()
      newCenter = (newCenter[0] + x, newCenter[1] + y)
    newCenter = [ newCenter[0] / len( allObjects ) , 
                  newCenter[1] / len( allObjects )  ]
    # Repeat the process, but now from the center to the nearest port
  #  center = newCenter[:]
  #  newCenter = [0, 0]
  #  for obj in allObjects:
  #    x, y = obj.getClosestConnector2Point(obj, center[0],
  #                                       center[1] )
  #    newCenter = [newCenter[0] + x, newCenter[1] + y]
  #  newCenter = [ newCenter[0] / len( allObjects ) , 
  #                newCenter[1] / len( allObjects )  ]
   
  # Move the intermediate object into the new center point
  oldCenter = interObj.getCenterCoord()
  interObj.setSelectAll()
  dx = newCenter[0] - oldCenter[0]
  dy = newCenter[1] - oldCenter[1]
  interObj.Move( dx, dy )  
  
  segment2curveDirectionMap = dict()
  
  # Initial point/s in the connection ---> Object/s From
  for i in range(0, len(objectsFrom) ):
    
    # Get the tag & itemhandler for each from segement
    segTag = baseTag + "1stSeg" + str(i)
    itemHandler = dc.find_withtag( segTag )
    if( not itemHandler ): 
#      raise Exception, "Having problems looking up canvas tags!"
      print 'WARNING: Utilities.optimizerHyperLink() could not find tag', segTag
    
    coords = dc.coords( itemHandler )
    objFrom = objectsFrom[i]
    
    # If the object has connectors 
    if( objFrom.hasConnectors() ):
       
      # Is it a named port? If so then can't move to another port
      if( objFrom.isConnectedByNamedPort( interObj.semanticObject ) ):
        #fromPoint = coords[:2]
        handler = objFrom.getConnectedByNamedPortHandler(interObj.semanticObject) 
        fromPoint = dc.coords(handler )[:2]
        
        
      # Snap to the nearest connection port (un-named only)
      else: 
        x, y = objFrom.getClosestConnector2Point(objFrom, newCenter[0],
                                              newCenter[1] )
        fromPoint = [x, y]
        
      # Do the coordinate changing magic
      if( curvature ):
        curveDirection = randint(0, 1)
        segment2curveDirectionMap[objFrom] = curveDirection
        v = curvinator( fromPoint, newCenter, curvature, curveDirection )
        extraPoint = getMidpoint2D( fromPoint, newCenter)
        extraPoint = [ extraPoint[0] + v[0], extraPoint[1] + v[1] ]
        dc.coords( * [itemHandler] + fromPoint + extraPoint + newCenter )
      else:
        dc.coords( * [itemHandler] + fromPoint + newCenter )
        
      # Check if a link drawing needs moving...
      interObj.updateDrawingsTo( x, y, itemHandler[0] )


  # Final point/s in the connection ---> Object/s To
  for i in range(0, len(objectsTo) ):
    
    # Get the tag & itemhandler for each to segement
    segTag = baseTag + "2ndSeg" + str(i)
    itemHandler = dc.find_withtag( segTag )
    if( not itemHandler ): 
#      raise Exception, "Having problems looking up canvas tags!"
      print 'WARNING: Utilities.optimizerHyperLink() could not find tag', segTag
    itemHandler = itemHandler[0]
          
    coords = dc.coords( itemHandler )
    objTo = objectsTo[i]
    
    # Avoid taking exactly the same path as the from link in self-loop case
    evasiveAction = False
    if(objTo in objectsFrom):
      evasiveAction = True
    
    # If the object has connectors 
    if( objTo.hasConnectors() ):
       
      # Is it a named port? If so then can't move to another port
      if( objTo.isConnectedByNamedPort( interObj.semanticObject )):
        #toPoint = coords[:2]
        handler = objTo.getConnectedByNamedPortHandler(interObj.semanticObject)
        outPoint = dc.coords(handler)[:2]
        
      # Snap to the nearest connection port if not already there
      else:
        x, y = objTo.getClosestConnector2Point(objTo, newCenter[0],
                                                                newCenter[1] )   
        toPoint = [x, y]
      
      # Do the coordinate changing magic
      if( curvature ):
        # Avoid following exact same path in self-loop situations
        if(evasiveAction):
          curveDirection = (segment2curveDirectionMap[objTo] + 1) % 2
        v = curvinator( toPoint, newCenter, curvature, curveDirection )
        extraPoint = getMidpoint2D( toPoint, newCenter)
        extraPoint = [ extraPoint[0] + v[0], extraPoint[1] + v[1] ]    
        dc.coords( * [itemHandler] + toPoint + extraPoint + newCenter )
      else:
        # Avoid following exact same path in self-loop situations
        if(evasiveAction):
          dx = newCenter[0] - toPoint[0]
          dy = newCenter[1] - toPoint[1]
          evasionDist = 9
          if(dx > evasionDist):
            dx = evasionDist
          elif(dx < -evasionDist):
            dx = -evasionDist
          else:
            dx = evasionDist
          if(dy > evasionDist):
            dy = -evasionDist
          elif(dy < -evasionDist):
            dy = evasionDist
          else:
            dy = evasionDist
          evasivePoint = [newCenter[0] + dx, newCenter[1] + dy]
          dc.coords( * [itemHandler] + toPoint + evasivePoint + newCenter  )
        else:
          dc.coords( * [itemHandler] + toPoint + newCenter  )
        
      # Check if a link drawing needs moving...
      interObj.updateDrawingsTo( x, y, itemHandler, segmentNumber=2 )
        

def curvinator( p1, p2, curveAmount, curveDirection ):
  """ 
  Returns a vector that is orthongonal to the p1-p2 vector with length curveAmount
  """
  v = [ - ( p1[1] - p2[1] ), p1[0] - p2[0] ]
  d = vectorLength2D( v )
  if( d == 0 ): 
    d = 1
    
  # Direction of the curvature bulge is random
  if( curveDirection == -1 and randint(0, 1) or curveDirection == 1 ): 
    curveAmount = -curveAmount

  # Normalized orthogonal vector times the curvature bulge
  v = ( v[0] * curveAmount / d, v[1] * curveAmount / d  )
  
  return v
      
def optimizeRegularLink( dc, interObj, fromObj, toObj, setSmooth, curvature, 
                         curveDirection ):
  """ Optimizes one edge with 2 endpoints in 2 different objects """
    
  # Find the optimally near connector points  
  inPoint, outPoint = fromObj.getNearestConnectors( toObj )
  
  # Is the inPoint *allowed* to move?
  if( fromObj.isConnectedByNamedPort( interObj.semanticObject ) ):
    # Permission denied, named port
    handler = fromObj.getConnectedByNamedPortHandler(interObj.semanticObject) 
    inPoint = dc.coords(handler )[:2]
          
  # Is the outPoint *allowed* to move?  
  if( toObj.isConnectedByNamedPort( interObj.semanticObject )):
    # Permission denied, named port, use old point
    handler = toObj.getConnectedByNamedPortHandler(interObj.semanticObject)
    outPoint = dc.coords(handler)[:2]
    

  newCenter = getMidpoint2D( inPoint, outPoint)
  
  # Move the intermediate object into the new center point  
  oldCenter = interObj.getCenterCoord()
  interObj.setSelectAll()
  dx = newCenter[0] - oldCenter[0]
  dy = newCenter[1] - oldCenter[1]
  
  # Add a bit of curvature (not so straight arrow hehe)
  if( curvature ):
    v = curvinator( inPoint, outPoint, curvature, curveDirection )
    dx += v[0] 
    dy += v[1] 
    finalCenter = [ newCenter[0] + v[0], newCenter[1] + v[1] ]
  else:
    finalCenter = newCenter
    
  # Move the intermediate object
  interObj.Move( dx, dy )
                
  # Go through the 2 segments in the link
  for connTuple in interObj.connections:
    itemHandler = connTuple[0]
    direction = connTuple[1]
    #oldCoords = dc.coords( itemHandler ) 
    
    '''
    NOTE: segCoords = PointA, PointB-Y, PointZ
    Where PointA is a node/entity, PointB-Y is a control point, and
    PointZ is an intermediate object (special control point).
    '''  
        
    # Makes the arrow ready for curvey spliney
    if( setSmooth ):
      
      # Outgoing arrow
      if( direction ):
        
        # Artificially curved control pint
        if( curvature ):
          m = getMidpoint2D(inPoint, newCenter)
          m = [ m[0] + v[0], m[1] + v[1] ]
          segCoords = inPoint + m + finalCenter
          
        # Regular straight control point
        else:
          segCoords = inPoint + getMidpoint2D(inPoint, finalCenter) \
                              + finalCenter
        
      # Incomming arrow
      else:
        
        # Artificially curved control point
        if( curvature ):
          m = getMidpoint2D(outPoint, newCenter)
          m = [ m[0] + v[0], m[1] + v[1] ]
          segCoords = outPoint + m + finalCenter
          
        # Regular straight control point
        else:
          segCoords = outPoint + getMidpoint2D(outPoint, finalCenter) \
                               + finalCenter
                    
      dc.itemconfigure( itemHandler, smooth=True )
              
    # No splines here
    else:
      
      # Incomming or Outgoing arrow
      if( direction ):
        segCoords = inPoint + finalCenter
      else:
        segCoords = outPoint + finalCenter
      
    # Applies the changed coords to the canvas
    dc.coords( * [itemHandler] + segCoords )

    
    # This may change the associated link drawings: move them to the new point  
    
    # Outgoing arrow
    if( direction ):
      interObj.updateDrawingsTo(inPoint[0], inPoint[1], itemHandler, 
                                                    segmentNumber=1)
   
    # Incomming arrow
    else:
      interObj.updateDrawingsTo(outPoint[0], outPoint[1], itemHandler, 
                                                      segmentNumber=2)
      
      

def optimizeSelfLink( dc, interObj, selfObj, setSmooth, curvature ):
  """ 
  Automatically makes a nice loop for objects linked to themselves 
  If curvature evaluates to true, 2 extra points are added to make a loop
  Otherwise, the self-loop will look like a line going back on itself... 
  Can place the loop in 8 cardinal directions, looks to previous position for
  direction cue.
  """
  # Require this much distance between link and entity
  minDistX = 5
  minDistY = 5
  # If no curvature, spread the line apart just a tad bit
  minSpacing = 9
      
  # Add additional minimum distance according to link object size
  (lx, ly) = (interObj.x, interObj.y) # Coords of link object (center point)
  cObj = interObj.getCenterObject()
  if(cObj):
    box = cObj.getbbox()
    minDistX += (box[2] - box[0]) / 2
    minDistY += (box[3] - box[1]) / 2
  
  # Add additional minimum distance according to entity object size
  box = selfObj.getbbox()
  halfW = (box[2] - box[0]) / 2
  halfH = (box[3] - box[1]) / 2
  (cx, cy) = (box[0] + halfW, box[1] + halfH) # Center of object
  minDistX += halfW
  minDistY += halfH
      
  # Link is east of obj
  if(lx > cx + halfW):
    distX = minDistX
  # Link is west of obj
  elif(lx < cx - halfW):
    distX = -minDistX
  # Link is center of obj
  else:
    distX = 0
  
  # Link is south of obj
  if(ly > cy + halfH):
    distY = minDistY
  # Link is north of obj
  elif(ly < cy - halfH):
    distY = -minDistY
  # Link is center of obj
  else:
    distY = 0
    
  # This could maybe someday happen if like the link was dead center...
  if(distX == 0 and distY == 0):
    distX = minDistX
    
  # This is a diagonal situation, since manhattan distances are being used,
  # I find it necessary to bring the link a bit closer to the entity
  elif(distX != 0 and distY != 0):
    diagonalCompensationX = minDistX * 0.2
    diagonalCompensationY = minDistY * 0.2
    if(distX > 0):
      distX -= diagonalCompensationX
    else:
      distX += diagonalCompensationX
    if(distY > 0):
      distY -= diagonalCompensationY
    else:
      distY += diagonalCompensationY

  
  # Move center object to new pos
  finalCenter = [cx + distX, cy + distY]
  interObj.moveTo(finalCenter[0], finalCenter[1])
  
  # If the self-loop is occuring on a named port, don't move arrow start/end
  findNewEndPoints = True
  if( selfObj.isConnectedByNamedPort( interObj.semanticObject ) ):
    inPoint = dc.coords( interObj.tag + "1stSeg0" )[:2]
    outPoint = dc.coords( interObj.tag + "2ndSeg0" )[:2]        
    findNewEndPoints = False

  # Go through the 2 segments in the link
  for connTuple in interObj.connections:
    itemHandler = connTuple[0]
    direction = connTuple[1]
  
    # Add curvature to the arrow, so add 2 extra points near the link center
    if(curvature):
      # Incomming arrow
      if( direction ):
        if(distX == 0 or distY == 0):
          newPoint = [finalCenter[0] + distY / 2, finalCenter[1] + distX / 2]
        else:
          newPoint = [finalCenter[0] + distY / 2, finalCenter[1] - distX / 2]
        
        if(findNewEndPoints): 
          inPoint = list(selfObj.getClosestConnector2Point(selfObj, 
                                  newPoint[0], newPoint[1])) 
        segCoords = inPoint + newPoint + finalCenter
        
      # Outgoing arrow
      else:
        if(distX == 0 or distY == 0):
          newPoint = [finalCenter[0] - distY / 2, finalCenter[1] - distX / 2]
        else:
          newPoint = [finalCenter[0] - distY / 2, finalCenter[1] + distX / 2]
        
        if(findNewEndPoints): 
          outPoint = list(selfObj.getClosestConnector2Point(selfObj, 
                                  newPoint[0], newPoint[1])) 
        segCoords = outPoint + newPoint + finalCenter
      
    # No curvature
    else:    
      if(distX > 0):
        distX = minSpacing
      else:
        distX = -minSpacing
      if(distY > 0):
        distY = minSpacing
      else:
        distY = -minSpacing
      
      # Incomming or Outgoing arrow
      if( direction ):
        if(findNewEndPoints):           
          inPoint = list(selfObj.getClosestConnector2Point(selfObj, 
                             finalCenter[0], finalCenter[1]))
        if(distX == 0 or distY == 0):
          newPoint = [finalCenter[0] + distY, finalCenter[1] + distX]
        else:
          newPoint = [finalCenter[0] + distY, finalCenter[1] - distX]
           
        segCoords = inPoint + newPoint + finalCenter
      else:
        if(findNewEndPoints): 
          outPoint = list(selfObj.getClosestConnector2Point(selfObj, 
                            finalCenter[0], finalCenter[1])) 
        if(distX == 0 or distY == 0):
          newPoint = [finalCenter[0] - distY, finalCenter[1] - distX]
        else:
          newPoint = [finalCenter[0] - distY, finalCenter[1] + distX]
          
        segCoords = outPoint + newPoint + finalCenter
  
    # Applies the changed coords to the canvas
    dc.coords( * [itemHandler] + segCoords )    
    dc.itemconfigure( itemHandler, smooth=setSmooth )
      
      
    # This may change the associated link drawings: move them to the new point  
    
    # Outgoing arrow
    if( direction ):
      interObj.updateDrawingsTo(inPoint[0], inPoint[1], itemHandler, 
                                                    segmentNumber=1)
   
    # Incomming arrow
    else:
      interObj.updateDrawingsTo(outPoint[0], outPoint[1], itemHandler, 
                                                      segmentNumber=2)
    
