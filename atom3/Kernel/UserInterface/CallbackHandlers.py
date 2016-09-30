"""
CallbackHandlers.py

The KeyBinds file was getting unmanageably large, and behaviour was being 
obscured in the forest of implementations. Hence this file, which is called on
by both keybinds and popup menus. 

The following are equivelent statements:
  dc.coords( itemHandler,x0,y0,x1,y1 )
  apply( dc.coords, [itemHandler] + [x0,y0] + [x1,y1] )
  dc.coords( * [itemHandler] + [x0,y0] + [x1,y1]  )

Created June 18, 2004 by Denis Dube
"""

import string, sys, os, Dialog

import ForceTransfer 
from ATOM3TypeDialog      import ATOM3TypeDialog
#from ATOM3TypeDialog      import *
from Drag                 import dragStart, dragMotion  
from Drag                 import dragDrop, enteringDragMode  
from ModelSpecificCode    import isConnectionLink, isEntityNode, isHyperEdge
from DrawConnections      import drawConnection
from Utilities            import arrowAbortion, snapIt
from Utilities            import optimizeConnectionPorts
from Utilities            import selectAllVisibleObjects, modelChange
from Qoca.constraints.QocaSolverAbstract import isAbstract as isNotUsingQoca


def arrowRollback(self, event):
  """ Rolls back the arrow by one point, or removes it entirely """
  if(self.pilotArrow.rollbackArrow(self.cb.getCanvasCoords(event))):
    arrowAbortion(self)


def getFinalSelectionBoxItems(self):
  """ Removes the selection box, returns newly selected items """
  
  cb = self.cb
  dc = cb.getCanvas()
  
  # Get the final selection box coordinates
  box = self.selectionBox.getSelectionBox()  
  coords = dc.coords(box)
  
  # Make the selection box go away... its work is done
  self.selectionBox.removeSelectionBox() 
    
  # Get list of handlers of all objects in the selection box
  cb.appendSelectionTuple(dc.find_enclosed(* coords))
                                                            
  # Convert the selection tuple to a LIST
  selected = []
  for itemHandler in cb.getSelectionTuple():
    # Only add items that are visible
    if(cb.isItemVisible(itemHandler)):
      selected.append(itemHandler)
  cb.clearSelectionTuple()
  
  return selected
    


def editPoint(self, event):
  """ 
  Arrow Edit Mode : Interactively mess around with the control points 
  Returns True if it has activated a control point for editing
  Returns False otherwise
  """
        
  # Check if cursor struck a control point, if so set the point active for drag
  dc = self.cb.getCanvas()
  x, y = self.cb.getCanvasCoords(event) 
  limit = 5
  items = dc.find_overlapping(x-limit, y-limit, x+limit, y+limit)
  if(items and items[0] != -1):
    if(self.arrowEditor.setNearestControlPointActive(items)):
      self.arrowEditor.setMousePosition(event)
      return True
  return False


  
def startNewSelectionBox(self, event, color):
  """ Create a new selection box and place it on the canvas at event """
  
  cb = self.cb
  dc = cb.getCanvas()
  
  # Create the selection box
  self.selectionBox.setSelectionBox(color)
  x, y = cb.getCanvasCoords(event)
  dc.coords(self.selectionBox.getSelectionBox(), x, y, x, y)
      


def createDynamicMenu(self, event):
  """ Create a dynamic context sensitive popup menu system  """

  cb = self.cb  
  selectionIsEmpty = cb.isLastSelectionEmpty()
  
  # Item under cursor?
  itemTuple = cb.getItemUnderCursor(self, event)
  if(itemTuple and cb.isItemVisible(itemTuple[0])):
    obj = itemTuple[2]
        
    # Graph Entity Object Selected
    if(isEntityNode(obj)):
      if(selectionIsEmpty):
        self.popupMenuCreator.EntityAtCursorNoSelectPopup(event)
      else:
        self.popupMenuCreator.EntityAtCursorMultiSelectPopup(event)

    # Graph Link Object Selected
    elif(isConnectionLink(obj)): 
      if(selectionIsEmpty):
        self.popupMenuCreator.LinkAtCursorNoSelectPopup(event)
      else:
        self.popupMenuCreator.LinkAtCursorMultiSelectPopup(event)
    
    # Uknown Object Selected
    else:
      raise Exception, \
        "Not an entity, not a link, what is it? Superman? " + str(obj) 
  
  # No item under cursor, no items selected
  elif(selectionIsEmpty):   
    self.popupMenuCreator.NoCursorNoSelectPopup(event)
    
  # No item under cursor, but multiple items selected
  else:   
    self.popupMenuCreator.NoCursorMultiSelectPopup(event)



def startArrowEditorMode(self, event):
  """ 
  Checks that the selected object is a link, then starts the editor 
  Return True if editor is started
  """
  
  cb = self.cb
  dc = cb.getCanvas()
  
  itemTuple = cb.getItemUnderCursor(self, event)
  if(itemTuple):
    itemHandler, tag, obj = itemTuple
    
    # This is a link --> Proceed
    if(isConnectionLink(obj)): 
      
      # Get information from the tag, segment type and segmenet number
      segTuple = cb.getSegmentTagInfoTuple(tag)
      if(not segTuple): 
        return self.arrowEditor.setArrowEditorAbort()
      
      objNum, segType, segNum = segTuple
      
      # This is the 1st segment, so get the 2nd part
      if(segType == 1):
        nextSegmentTag = "Obj" + str(objNum) + "2ndSeg0"
        nextItemHandler = cb.findItemHandlerWithTag(nextSegmentTag)
        
      # This is the 2nd segment, so get the 1st part
      elif(segType == 2):
        nextSegmentTag = tag
        nextItemHandler = itemHandler
        tag = "Obj" + str(objNum) + "1stSeg0"
        itemHandler = cb.findItemHandlerWithTag(tag)
        
      # Never!
      else:  
        raise Exception, \
          "This will never happen... setType must be 1 or 2!" + str(segType)
          
      seg1coords = dc.coords(itemHandler)
      # Reverse the 2nd segments coords 
      # (so that they are in same direction as the 1st )
      seg2coords = obj.reverseList2by2(dc.coords(nextItemHandler))
      
      # Get the connected objects: objFrom and objTo
      semObject = obj.getSemanticObject()
      if(not semObject.in_connections_ or not semObject.out_connections_): 
        return self.arrowEditor.setArrowEditorAbort()
      
      if(segType == 1):
        connectedObjects = (semObject.in_connections_[segNum].graphObject_, 
                           semObject.out_connections_[0].graphObject_) 
      else:
        connectedObjects = (semObject.in_connections_[0].graphObject_, 
                           semObject.out_connections_[segNum].graphObject_) 
           
      # Now construct the interactive editor arrow
      self.arrowEditor.constructEditorArrow(seg1coords, seg2coords, 
                              (itemHandler, nextItemHandler), 
                               connectedObjects, obj, self.snapGridInfoTuple)
      return
  
  # Things didn't work out... abort!
  self.arrowEditor.setArrowEditorAbort()




def getSelectedItemsForDelete(self, entityOnlyFlag=False):
  """ 
  Use:
    Finds all the selected nodes and links, then creates a custom event, 
    DeleteEvent, which it sends to the UI_scope that then sends the event
    to whichever scoped statechart will handle it. The DeleteEvent uses the
    x, y coordinates of the node/link to be deleted, so potentially, each
    node/link's deletion could be handled by a different scoped statechart. 
  Parameters:
    self, ATOM3 instance
    entityOnlyFlag, if this boolean flag is True, then deleting an entity will
                    NOT automatically delete arrows that connect to that entity
  """
  
  class DeleteEvent:
    """
    A special event that mimics the x, y coordinates of a Tkinter binding
    generated event, but lacks many of the normal attributes, and includes
    tag and itemHandler attributes not normally found there...
    """
    def __init__(self, obj, tag=None,
                itemHandlerTagList=None, entityOnlyFlag=False):
      self.x = obj.x
      self.y = obj.y
      self.tag = tag
      self.semanticObject = obj.semanticObject
      self.atom3i = obj.semanticObject.parent
      self.itemHandlerTagList = itemHandlerTagList
      self.entityOnlyFlag = entityOnlyFlag
      
    def destroy(self):
      """ Deletes the associated ATOM3 node or link """
      if(self.itemHandlerTagList):
        tag2objMap = self.atom3i.cb.getTag2ObjMap()
        for itemHandler, tag in self.itemHandlerTagList:
          # Deleting one segment of an arrow, can delete the other, so careful!
          if(tag2objMap.has_key(tag)):
            self.atom3i.deleteConnection(itemHandler, tag)
      else:
        self.atom3i.deleteRealEntity(self.tag, entityOnly=self.entityOnlyFlag)
    
    def getSemanticObject(self):
      """ Returns the ASGNode instance being deleted """
      return self.semanticObject
  
  selectionDict = self.cb.getSelectionDict() # Dict of selected items
  objTagDict = dict()
  
  self.fromClass = None
  self.toClass = None
  
  # This little dictionary gymnastic is being used to prevent duplicate objects
  for tag in selectionDict:
    obj = selectionDict[tag][1]
    objTagDict.update({obj:tag})

  # Now do the connections first, since if entities disappear, 
  # connections might too. And we DO NOT want that to happen... crash crash :p
  for obj in objTagDict:
    tag = objTagDict[obj]
    
    # Connection
    if(isConnectionLink(obj)):  
      #print "Now deleting connection: ", tag, obj, selectionDict[tag][0]
      # This may seem like overkill, but it's necessary for hyper-edges
      connList = []
      for connTuple in obj.in_connections_:  
        connList.append(connTuple)
      for connTuple in obj.out_connections_: 
        connList.append(connTuple)
        
      itemHandlerTagList = []
      for connTuple in connList:
        itemHandlerTagList.append(connTuple[:2])          
      event = DeleteEvent(obj, itemHandlerTagList=itemHandlerTagList)
      self.UI_scope('<serviceLinkDeleteRequest>', event)
      
    # Entity
    else:  
      event = DeleteEvent(obj, tag=tag, entityOnlyFlag=entityOnlyFlag)
      self.UI_scope('<serviceNodeDeleteRequest>', event)
      
  # Model changed!
  modelChange(self)
    
  # No more selected objects :-(
  self.cb.clearSelectionDict()

  



  
def startArrowDrawing(self, event):
  """ 
  User has clicked on an object and wishes to start drawing an arrow from it 
  """
  
  cb = self.cb                        # User-interface callback object
  dc = cb.getCanvas()
  x, y = cb.getCanvasCoords(event)   # Event coordinates  
  arrow = self.pilotArrow.getArrow()
  
  # Find the closest item to the arrow
  itemTuple = cb.getItemUnderCursor(self, event, ignore=arrow)
  if(itemTuple):
    itemHandler, tag, obj = itemTuple
    
    dc.coords(arrow, x, y, x, y)    
          
    # Start the arrow at the nearest connector... if it exists...
    if(obj.hasConnectors()):
      x, y = obj.getMinDistance_Connectors2Fixed(obj, x, y)
      
      # The object has named ports, perhaps we should lock the first point...
      if(obj.hasNamedPorts()):
        self.pilotArrow.setSnapLock(True)
        name = obj.guesstimateNamedConnAtPoint(x, y)
        if(self.showNamedPortMessage and name):
          text = 'Arrow started on named port: ' + name \
                  + '\n\nThis message is shown only when you start an arrow' \
                  + ' directly on a named port' \
                  + '\n\nIf you choose the 2nd option and want to see these ' \
                  + 'messages again, restart AToM3'
          dialog = Dialog.Dialog(None, {'title': 'Lock Current Named Port', 
                      'text': text, 
                      'bitmap': '', 
                      'default': 0, 
                      'strings': (name, 'Abort arrow', 
                                  'Never show this message')})         
          if(dialog.num == 1):
            return arrowAbortion(self)
          if(dialog.num == 2):
            self.showNamedPortMessage = False
   
    # The edge just happens to have a connector...   
    elif(obj.hasCenterObjectConnector()):
      x, y = obj.getCenterCoord()     
    
    # Hyperedge! Snap to the center point of the edge
    elif(isHyperEdge(obj)):
      x, y = obj.getCenterCoord()
    
    # Failure! The object had no connectors, some connection! Oooops.
    else:        
      return arrowAbortion(self)
  
    # New coords
    dc.coords(arrow, x, y, x, y)             
    
    # Keep a copy of this object under the pillow
    self.pilotArrow.setFromObject(obj)
    self.pilotArrow.setFromTag(tag)
    
                      
  # Bad arrow start, no object, cancel
  else: 
    arrowAbortion(self)
    
      

def realtimeArrowMotion(self, event, snap = True):
  """ 
  Animated arrow that has no semantic meaning, but aids interactive drawing 
  """

  cb = self.cb
  dc = cb.getCanvas()
  arrow = self.pilotArrow.getArrow(create=False)
  if(not arrow):
    print 'arrow motion'
    return
  
  coords = dc.coords(arrow)
  x, y = cb.getCanvasCoords(event)

  # Snap Grid
  if(self.snapGridInfoTuple and self.snapGridInfoTuple[2]):
    gridSize = self.snapGridInfoTuple[0]
    x, y = [ snapIt(x, x, gridSize), snapIt(y, y, gridSize) ]

  # If still have 2 points, do object Snapping on first point 
  # Don't snap if we have a lock in effect (useful for Named Ports) 
  if(snap and len(coords) == 4 and not self.pilotArrow.getSnapLock()):
    fromObj = self.pilotArrow.getFromObject()
    if(fromObj):
      # Regular entity
      if(fromObj.hasConnectors()):
        x0, y0 = fromObj.getMinDistance_Connectors2Fixed(fromObj, x, y)
        coords = [x0, y0, x, y] 
        dc.coords(* [arrow] + coords)
        
  # Look under the mouse pointer for treasures :D
  itemTuple = cb.getItemUnderCursor(self, event, ignore=arrow)
  if(not itemTuple): 
    return dc.coords(* [ arrow ] + coords[:-2] + [x, y])
  obj = itemTuple[2]

  # Snap the final point to the nearest object connector (Avoid snapping to self)
  if(snap and obj != self.pilotArrow.getFromObject()):

    # Regular Entity
    if(obj.hasConnectors()):
      # Calc distance from before last point to the nearest connector
      x, y = obj.getMinDistance_Connectors2Fixed(obj, coords[-4], coords[-3])

    # Hyperedge! Snap to the center point of the edge
    elif(isHyperEdge(obj)): 
      x, y = obj.getCenterCoord()
           
  dc.coords(* [ arrow ] + coords[:-2] + [x, y])



      
def dropArrowPoints(self, event, snap = True, filterLinkTypeList=None):
  """ 
  Drops intermediate points in the arrow or connects the arrow to the final
  object. If connection is not possible due to the final object not having 
  connectors, the arrow will be rolled back 1 connection point, or destroyed
  """
  
  cb = self.cb                        # User-interface callback object
  dc = cb.getCanvas()
  x, y = cb.getCanvasCoords(event)   # Event coordinates     
  
  arrow = self.pilotArrow.getArrow()
  coords = dc.coords(arrow)
    
  # Find the closest item to the arrow
  itemTuple = cb.getItemUnderCursor(self, event, ignore=arrow, allTags=True)
  if(itemTuple and snap):
    itemHandler, tags, obj = itemTuple
    
    # Embedded model  ---> WARNING: Not tested, original AToM3 code
    if(len(tags) >= 2 and tags[1][:4] == 'ASG_'):
      self.toClass = tags[0]   
      # Open to select the entity inside the model
      ATOM3TypeDialog(self, obj.semanticObject, ATOM3TypeDialog.OPEN, 
                      (None, self.setConnectMode))	
      # Check if we have both sides...
      if self.sem_objFrom and self.sem_objTo:	# we have both sides...
        drawConnection(self)
      
    # Object
    elif(tags[0][:3] == 'Obj'):
    
      # Get the actual connector point that we are going to connect to
      # coords[-4],coords[-3] are the before last point, so the min distance 
      # that point to the connector yields the optimal final point.
      # Some objects may not have connectors, in this case gracefully rollback 
      # the arrow
      if(obj.hasConnectors()): 
        coords[-2], coords[-1] = obj.getMinDistance_Connectors2Fixed(obj, 
                                                         coords[-4], coords[-3])
        if(obj.hasNamedPorts() and self.showNamedPortMessage):
          name = obj.guesstimateNamedConnAtPoint(coords[-2], coords[-1])
          if(name):
            text = 'Arrow ended on named port: '  \
                    + name \
                    + '\n\nThis message is shown only when you end an arrow' \
                    + ' directly on a named port' \
                    + '\n\nIf you choose the 2nd option and want to see these '\
                    + 'messages again, restart AToM3'
            dialog = Dialog.Dialog(None, {'title': 'Lock Current Named Port', 
                        'text': text, 
                        'bitmap': '', 
                        'default': 0, 
                        'strings': (name, 'Rollback arrow', 
                                    'Never show this message')})         
            if(dialog.num == 1):
              return
            if(dialog.num == 2):
              self.showNamedPortMessage = False
      
      # Edge just happens to have a connector
      elif(obj.hasCenterObjectConnector()):
        coords[-2], coords[-1] = obj.getCenterCoord()
      
      # Hyperedge! This means that links can connect to links
      elif(isHyperEdge(obj)): 
        coords[-2], coords[-1] = obj.getCenterCoord()
        
      else:
        # Failure! The object had no connectors. Oooops.
        if(self.pilotArrow.rollbackArrow([x, y])):
#          self.UI_scope.event("Reset")
          self.UI_scope("Reset", None)
        return
      
      
      # Get the semantic object
      self.sem_objTo = obj.semanticObject	        
      self.sem_objFrom = self.pilotArrow.getFromObject().semanticObject 
      self.toClass = tags[0]
      self.fromClass = self.pilotArrow.getFromTag()
      
      # Arrow is connecting the object to itself with just 2 points! BAD
      if(self.sem_objTo == self.sem_objFrom and len(coords) <= 4):
        pass
      
      # Draw the connection, turn off simpleConnect, since using intermediate 
      # points
      else:             
        smooth = self.pilotArrow.getSmoothness()
        self.inter_connect_points = coords
        drawConnection(self, smooth, simpleConnect = False, 
                         filterLinkTypeList=filterLinkTypeList)
                
    # Unknown something...
    else:
      raise Exception, tags
      
                  
    # Empty variables
    self.fromClass   = None				
    self.toClass     = None
    self.sem_objFrom = None
    self.sem_objTo   = None

    # Model changed!
    modelChange(self)
    
    # Pilot arrow is no longer needed, GOODBYE!      
    self.pilotArrow.removeArrow(False)
    self.UI_scope("<Arrow Created>", None) # Tell UI we succeeded!
    
  # Nope, keep adding intermediate points
  else:

    # Snap Grid
    if(self.snapGridInfoTuple and self.snapGridInfoTuple[2]):
      gridSize = self.snapGridInfoTuple[0]
      coords[-2:] = [ snapIt(x, x, gridSize), snapIt(y, y, gridSize) ]
    
    # No grid snapping
    else:
      coords[-2:] = [ x, y ]
      
    # Apply coords & add a duplicate point
    dc.coords(* [arrow] + coords + coords[-2:])
    
      
def atom3ActionMap(self, event):
  """ 
  Applies the AToM3 action map with the current mode.
  Actions are usually model specific and add entities to the model.
  """
  
  # If mode is "idle" gets the last non-idle action
  action = self.cb.getAction(self.mode)
  
  # Apply the action map from AToM3, includes dynamic model specific actions
  if(self.userActionsMap.has_key(action)):
      self.userActionsMap[action](self, event.x, event.y)

    

      
    
def selectionBoxDragging(self, event):
  """ Updates the selection box dimensions with the mouse movement """
  
  dc = self.cb.getCanvas()
  box = self.selectionBox.getSelectionBox()
  
  # Update the selection box coordinates
  x0, y0, x1, y1 = dc.coords(box)
  x, y = self.cb.getCanvasCoords(event)
  # The following gymnastics cause the minimum change to the selection box
  if(abs(x - x0) < abs(x - x1)): 
    x0 = x
  else: 
    x1 = x
  if(abs(y - y0) < abs(y - y1)): 
    y0 = y
  else: 
    y1 = y
  dc.coords(box, x0, y0, x1, y1)
      
      
          
def toggleCreateAsSmooth(self):
   """    
   New arrows will be created with smoothing enabled if this is toggled On 
   """
   self.pilotArrow.toggleCreateSmooth()
   value = 1-self.optionsDatabase.get(self.SMOOTH_ARROWS)
   self.optionsDatabase.set(self.SMOOTH_ARROWS, value)
   self.optionsDatabase.saveOptionsDatabase()
   


def dragFinish(self, event=None):
  """ Stops dragging """
  dragDrop(self, self.cb.getSelectionObjectSet())
    
  # If auto force transfer: apply it after dragging to push things apart
  if(self.isAutoForceTransferEnabled):
    ForceTransfer.applyLayout()
  
  modelChange(self) # Model changed, update statusbar & undo
  
  
  
def dragLabelsInMotion(self, event):
  """ Drags all selected labels around """
    
  cb = self.cb
  
  x0, y0 = cb.getLastClickCoord() 
  x1, y1 = cb.getCanvasCoords(event)
  dx, dy = [x1-x0, y1-y0]
  selectionSet = cb.getSelectionObjectSet()
  
  # All selected objects 
  for obj in selectionSet:
    
    # Graph Entities (not links)
    if(isEntityNode(obj)): 
      
      objectLabelMoved = False
      
      # Associated graphical forms
      for gf in obj.graphForms:	
        
        # Text label
        if(gf.elementType == 'text'):
          self.cb.getCanvas().move(gf.handler, dx, dy)
          objectLabelMoved = True
          
      # Save the offest as a graphical layout constraint for model save/load
      if(objectLabelMoved):        
        if(not obj.layConstraints.has_key('Label Offset')):
          obj.layConstraints['Label Offset'] = [dx, dy ]
        else:
          deltaX, deltaY = obj.layConstraints['Label Offset']
          obj.layConstraints['Label Offset'] = [dx+deltaX, dy+deltaY]
         
    # This is a link
    else:
      
      # Label is the centerObject
      if(obj.centerObject):
        obj.centerObject.Move(dx, dy, 0)
        
        # Save the offest as a graphical layout constraint for model save/load
        if(not obj.layConstraints.has_key('Label Offset')):
          obj.layConstraints['Label Offset'] = [dx, dy]
        else:
          deltaX, deltaY = obj.layConstraints['Label Offset']
          obj.layConstraints['Label Offset'] = [dx+deltaX, dy+deltaY]
    
def dragInMotion(self, event):
  """ 
  Dragged objects follow mouse motion 
  If snap mode, snaps the top-left of the object. 
  Replaced object.x, object.y with the x,y = object.getCenterCoord() , for 
  a center snap. Do the same to the snapNewEntity method in Utilities. 
  NOTE: Center snap causes problems when saving/loading models because it is 
  applied to new nodes created by loading a model. See ASG.py, addNode()
  """
  
  cb = self.cb
  
  x0, y0 = cb.getLastClickCoord() 
  x1, y1 = cb.getCanvasCoords(event)
  dx, dy = [x1-x0, y1-y0]
  selectionSet = cb.getSelectionObjectSet()
  
  # Many entities, try to make dragging more responsive (faster)
  if(len(selectionSet) > 1):
    dragMotion(self, [x0, y0], [x1, y1], selectionSet)
    
  
  elif(self.snapGridInfoTuple):
    
    gridSize, snapArrowNode, snapControlPoints = self.snapGridInfoTuple
    
    # Apply Snap only to entities, exclude arrows
    if(not snapArrowNode):    
      for object in selectionSet:      
        if(isEntityNode(object)):      
          #x,y = object.getCenterCoord() 
          x1 = snapIt(object.x + dx, x1, gridSize)
          y1 = snapIt(object.y + dy, y1, gridSize)        
          cb.setLastClickCoords([x1, y1])
          break
          
    # Snap Entities or Arrows
    else:
      for object in selectionSet:      
        #x,y = object.getCenterCoord() 
        x1 = snapIt(object.x + dx, x1, gridSize)
        y1 = snapIt(object.y + dy, y1, gridSize)               
        cb.setLastClickCoords([x1, y1])
        break
    
    dragMotion(self, [x0, y0], [x1, y1], selectionSet)
    optimizeConnectionPorts(self)
  


  
def scaleWithMotion(self, event, textMode = False):
  """ Scales selected entities with the mouse motion """

  cb = self.cb                     

  x0, y0 = cb.getLastClickCoord() 
  x1, y1 = cb.getCanvasCoords(event)  
  
  allScalableEntityObjects = []
  for object in cb.getSelectionObjectSet():
      if(isEntityNode(object)):
          allScalableEntityObjects.append(object)
      elif(object.getCenterObject()):
          allScalableEntityObjects.append(object.getCenterObject())
  
  # Re-Size the text of an Entity or Link
  if(textMode):
    dx, dy = [ float(x1-x0) / 100.0 , float(y1-y0) / 100.0 ]
                 
    for object in allScalableEntityObjects:
        # Get the last scale factor, and add the movement delta
        if(not object.layConstraints.has_key('Text Scale')):
          object.layConstraints['Text Scale'] = 1.00
            
        newSize = object.layConstraints['Text Scale'] + dy
        
        # Bigger is better, too small is unreadable :D
        if(newSize < 0.2): 
          newSize = 0.2
          
        object.ScaleText(newSize)
        object.layConstraints['Text Scale'] = newSize  
        
        
  # Re-Size an entity node - NO QOCA 
  elif(isNotUsingQoca()):
    dx, dy = [ float(x1-x0) / 100.0 , float(y1-y0) / 100.0 ]
    for object in allScalableEntityObjects:
        
        # Get the last scale factor, and add the movement delta
        if(not object.layConstraints.has_key('scale')):
          object.layConstraints['scale'] = [1.00, 1.00]
        sx, sy = object.layConstraints['scale']
        newSize = [sx + dx, sy + dy]
        
        # Too small is not good :p
        if(newSize[0] < 0.2): 
          newSize[0] = 0.2
        if(newSize[1] < 0.2): 
          newSize[1] = 0.2
        
        # The final scale factor
        sx, sy = [ newSize[0] / sx, newSize[1] / sy ]  
  
        # Note: moveLinks is false only because optimizeConnectionPorts is better
        #object.Scale(sx, sy, moveLinks = False)
        x0, y0 = object.getbbox()[:2]
        object.dc.scale(object.tag, x0, y0, sx, sy) 
        object.moveTo(object.x, object.y)
        object.layConstraints['scale'] = newSize
      
    optimizeConnectionPorts(self)
        
  # Re-Size an entity node - WITH QOCA constraints
  else:  
    dx, dy = [float(x1-x0), float(y1-y0) ]
    
    # Make the width/height editable
    editVarList = []
    for obj in allScalableEntityObjects:
      editVarList.append(obj.qcW)
      editVarList.append(obj.qcH)      
    self.qocaSolver.addEditVars(editVarList)
    
    # Suggest new width/height values
    for obj in allScalableEntityObjects:     
      self.qocaSolver.suggestVarValue([(obj.qcW, obj.qcW.get() + dx), 
                                       (obj.qcH, obj.qcH.get() + dy)])   
      
    # Solve to get the new width/height of the entity
    self.qocaSolver.resolve(forceSolve=True)
    self.qocaSolver.endEdit() 
    object.layConstraints['scale'] = [obj.qcW.get() / obj.sizeX, 
                                      obj.qcH.get() / obj.sizeY]
    optimizeConnectionPorts(self)
    
    
  modelChange(self) # Model changed, update statusbar & undo
  

def scaleReset(self, textMode = False):
  """ Restores scale to 1.0 """
  
  # Re-Size the text of an Entity or Link
  if(textMode):
    
    allScalableEntityObjects = []
    for object in self.cb.getSelectionObjectSet():
        if(isEntityNode(object)):
            allScalableEntityObjects.append(object)
        elif(object.getCenterObject()):
            allScalableEntityObjects.append(object.getCenterObject())
            
            
    for object in allScalableEntityObjects:
        # Get the last scale factor
        if(not object.layConstraints.has_key('Text Scale')):
          object.layConstraints['Text Scale'] = 1.00                          
        object.ScaleText(1.00)
        object.layConstraints['Text Scale'] = 1.00  
    
  # Re-Size an entity node - NO QOCA 
  elif(isNotUsingQoca()):
    for object in self.cb.getSelectionObjectSet():
      if(isEntityNode(object)):  
        
        # Get the last scale factor
        if(not object.layConstraints.has_key('scale')):
          object.layConstraints['scale'] = [1.00, 1.00]
        sx, sy = object.layConstraints['scale']
        newSize = [1.00, 1.00]
                
        # The final scale factor
        sx, sy = [ newSize[0] / sx, newSize[1] / sy ]  
  
        # Note: moveLinks is fals only because optimizeConnectionPorts is better
        #object.Scale(sx, sy, moveLinks = False)
        x0, y0 = object.getbbox()[:2]
        object.dc.scale(object.tag, x0, y0, sx, sy) 
        object.moveTo(object.x, object.y)
        object.layConstraints['scale'] = newSize
      
    optimizeConnectionPorts(self)
    
  # Re-Size an entity node - WITH QOCA constraints
  else:
    allScalableEntityObjects = []
    for object in self.cb.getSelectionObjectSet():
        if(isEntityNode(object)):
            allScalableEntityObjects.append(object)
          
    # Make the width/height editable
    editVarList = []
    for obj in allScalableEntityObjects:
      editVarList.append(obj.qcW)
      editVarList.append(obj.qcH)
    self.qocaSolver.addEditVars(editVarList)
    
    # Suggest new width/height values
    for obj in allScalableEntityObjects:     
      self.qocaSolver.suggestVarValue([(obj.qcW, obj.sizeX), 
                                       (obj.qcH, obj.sizeY)])   
      
    # Solve to get the new width/height of the entity
    self.qocaSolver.resolve(forceSolve=True)
    self.qocaSolver.endEdit() 
    optimizeConnectionPorts(self)
    
  modelChange(self) # Model changed, update statusbar & undo

  
def cutSave(self):
  """ Saves selected objects in the copyBuffer and cuts them from the canvas """
  
  copySave(self)
#  deleteSelected(self)
  getSelectedItemsForDelete(self) # This will do modelChange
  
#  modelChange(self) # Model changed, update statusbar & undo
  
def copySave(self):
  """ Saves the selected objects in the copyBuffer """
  
  self.cb.buildSelectionObjectSet()
  graphObjectList = self.cb.getSelectionObjectSet()
  nodesToSaveList = []
  # iterate on all the node types...
  for nodetype in self.ASGroot.nodeTypes:						
    for node in self.ASGroot.listNodes[nodetype]:
      if(node.graphObject_ in graphObjectList):
        nodesToSaveList.append(node)
  
  ASG = self.ASGroot
  # try the global constraints...
  # evaluate global pre-conditions
  res = self.ASGroot.preCondition(ASG.SAVE)	
  # if violated, show warning and do not save					
  if res: 
    return self.constraintViolation(res)		
  			
  # try the local constraints...
  # evaluate global pre-conditions
  res = self.ASGroot.evaluateLocalPreCondition(ASG.SAVE)
  # if violated, show warning and do not save
  if res: 
    return self.constraintViolation(res)					
  res = self.checkModel()
  # if violated, show warning and do not save
  if res: 
    return self.constraintViolation(res)					
  
  self.cb.highlighter(0)
  # Call the ASG method to save its contents
  self.ASGroot.genCode(self.cb.COPY_BUFFER_PATH, self.types, self.genGraphics, 
                                   1, self.GUIModelName, False, self.newTypes, 
                                   nodesToGenList = nodesToSaveList)

  self.cb.highlighter(1)    
  self.cb.initilizeCopyBuffer()
  
def pasteLoader(self, event):
  """ 
  Pastes the objects in the copyBuffer, selects them, and starts dragging mode
  """
    
  # Auto De-Select
  self.cb.clearSelectionDict() 
    
  filePath = self.cb.COPY_BUFFER_PATH
  if(os.path.exists(filePath)):   
    # compose class name
    className   = string.split (self.cb.COPY_BUFFER_NAME, ".")					
    self.newfunction = None

    if className[0]:
      # first check if it has been loaded before, to force a recompilation
      # file has already been loaded
      if className[0] in sys.modules.keys(): 
        # delete to force a reload      				
        del sys.modules[className[0]]		                        

      exec "from "+className[0]+" import *\n" in self.__dict__, self.__dict__
      # if we have the meta-model name
      if "loadedMMName" in self.__dict__.keys():     
        # we do not have any meta-model opened!      
        if not self.ASGroot:                                 
          return       
        # if we do not have the meta-model opened...
        elif self.loadedMMName != self.GUIModelName:       
          return        
      # look for newly defined or loaded types (loadedTypes should be a list)
      if "loadedTypes" in self.__dict__.keys():		
        return
      
      cb = self.cb   
      dc = cb.getCanvas()       
            
      # Find all the old items
      itemsTuple = dc.find_all()  
      # Convert the itemsTuple to a LIST
      oldItems = []
      for itemHandler in itemsTuple:
        oldItems.append(itemHandler)
      
      # Load the copyBuffer model
      self.newfunction(self, self.ASGroot)
      
      # Find all the new items (ignore old ones!)
      itemsTuple = dc.find_all()
      # Convert the itemsTuple to a LIST
      pasteSelection = []
      for itemHandler in itemsTuple:
        # Only add items that are visible
        if(itemHandler not in oldItems):
          pasteSelection.append(itemHandler)
          
      if(not pasteSelection): 
        return
             
      # Select the new items & highlight them
      cb.updateSelectionDict(pasteSelection)
      cb.highlighter(1)  
      
      # Convert selection to a non-duplicating object list & start dragging
      objectSet = cb.buildSelectionObjectSet()
      
      # Some of these objects may be duplicating existing keyword attributes
      for obj in objectSet:
          node = obj.semanticObject
          if(node.keyword_):               
              keyword = node.keyword_.getValue()
              attrList = []
              for value in node.getValue():
                  if(value == keyword): 
                    attrList.append(value + ' ' +  str(node.objectNumber)) 
                  else:                   
                    attrList.append(value)
                  
              # Set the pasted attributes
              node.setValue(attrList)
              node.updateAppearanceAttributes()
    
              # Make sure the visual appearence is updated
              for visualAttr in obj.attr_display.keys():       
                  obj.ModifyAttribute(visualAttr, 
                                     node.__dict__[visualAttr].toString(25, 5))
      
      dragStart(self)
        
      # But wouldn't it be cool if what your dragging was right under the mouse?
      itemHandler = pasteSelection[0]
      itemCoords = dc.coords(itemHandler)[:2]
      dragMotion(self, itemCoords, cb.getCanvasCoords(event), 
                                                     cb.getSelectionObjectSet())
      
  
      
def copyObjectAttributes(self, event):
  """ Copies the attributes of the entity or link under the cursor """
 
  itemTuple = self.cb.getItemUnderCursor(self, event)
  if(not itemTuple): 
    return
  
  obj = itemTuple[2]    
  for nodetype in self.ASGroot.nodeTypes:		# iterate on all the node types...
    for node in self.ASGroot.listNodes[nodetype]:
      if(node.graphObject_ == obj):
        self.cb.copyAttributes(node, nodetype)
        return

  
def pasteObjectAttributes(self, event):
  """ Pastes attributes to the entity or link under the cursor """

  itemTuple = self.cb.getItemUnderCursor(self, event)
  if(not itemTuple): 
    return
  
  obj = itemTuple[2]    
  for nodetype in self.ASGroot.nodeTypes:		# iterate on all the node types...
    for node in self.ASGroot.listNodes[nodetype]:
      if(node.graphObject_ == obj):
        self.cb.pasteCompatibleAttributes(node, nodetype)
        modelChange(self) # Model changed, update statusbar & undo
        return
      
