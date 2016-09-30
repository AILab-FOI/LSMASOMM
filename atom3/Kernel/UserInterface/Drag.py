"""
Drag.py

Derived from older atom3 code, it is now geared for handling arbitrary numbers
of objects instead of just one at a time. It was moved to a seperate module 
since the drag operation is pretty much self contained (and I hate long files).

Created June 15, 2004 by Denis Dube
"""

import sys

from ASG                 import *
from Utilities import optimizeConnectionPorts
from FilePaths import GRAPHIC_EDITOR_DATA

from SnapGrid import SnapGrid

class Drag:
  CURR_INSTANCE = None # Current instance of Drag object, only one at a time  
  #STIPPLE = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'line.xbm' ) )
  ITEM_HANDLER_LIST = []
  
  def __init__(self, objList, x, y):
    """
    Creates a new drag object
    Includes 2 boxes: 
      #1 indicates the initial position of the dragged items
      #2 indicates the new position of the dragged items
    Note: Dragged items are not moved at all! Only the indicators (for speed)
    """
    assert len(objList) >= 1 # Generic UI statechart guarantees this
    
    self.initialCoords = (x, y)
    self.dc = objList[0].dc 

    tagList = []
    for obj in objList:
      tagList.append(obj.tag)
    bbox = self.dc.bbox(*tagList)
    
    itemHandler = self.dc.create_rectangle(bbox, 
                                        tags='dragBoxVisualAid', 
                                        stipple= '', 
                                        width= '2.0', outline= 'firebrick3', 
                                        fill= '')
    self.dragEndBoxItem = self.dc.create_rectangle(bbox, 
                                        tags='dragBoxVisualAid', 
                                        stipple= 'gray25', 
                                        width= '2.0', outline= 'darkgreen', 
                                        fill= 'lightgreen')  
    Drag.ITEM_HANDLER_LIST.append(itemHandler)
    Drag.ITEM_HANDLER_LIST.append(self.dragEndBoxItem)
                     
    self.dx = 0
    self.dy = 0                                    
                     
    # Lower boxes under everything on canvas
    self.dc.tag_lower(itemHandler)
    self.dc.tag_lower(self.dragEndBoxItem)
    
    # Raise boxes above the grid lines system
    gridItemHandler = SnapGrid.highestItemHandler
    if(gridItemHandler):
      self.dc.tag_raise(itemHandler, gridItemHandler)
      self.dc.tag_raise(self.dragEndBoxItem, gridItemHandler)
    
    
    Drag.CURR_INSTANCE = self
        
        
  def move(self, dx, dy):
    """
    Update the new drag location indicator
    Sum up the movement delta
    """
    self.dc.move(self.dragEndBoxItem, dx, dy)
    self.dx += dx
    self.dy += dy
        
        
  def destroy(self):
    """
    Drag operation over, cleanup time
    Returns initial and final coordinates of the drag operation
    """
    Drag.CURR_INSTANCE = None
    for itemHandler in Drag.ITEM_HANDLER_LIST:
      self.dc.delete(itemHandler) # Remove all boxes created during drag
    Drag.ITEM_HANDLER_LIST = []
    
    finalCoords = (self.initialCoords[0] + self.dx, 
                                     self.initialCoords[1] + self.dy)
    return (self.initialCoords, finalCoords)
    
    
#===============================================================================
#
#===============================================================================



def enteringDragMode(self):
  """ Reset if not dragging anything """
  if( self.cb.isLastSelectionEmpty() ): 
    self.UI_Statechart.event("Reset")
  
  
  
def dragStart(self):
  """
  It starts a drag operation on the selected graphical objects.
  """ 
  
  cb = self.cb
  objectSelectionSet = cb.getSelectionObjectSet()
  x, y = cb.getLastClickCoord()
  
  # If multiple objects, then create a Drag object to efficiently handle them
  if(len(objectSelectionSet) > 1):
    Drag(objectSelectionSet, x, y)
    
  for obj in objectSelectionSet:

    # Evaluate global pre-conditions
    res = self.ASGroot.preCondition(ASG.DRAG, x, y)	                  
    if res: 
      return self.constraintViolation(res)		       
    
    # Evaluate global pre-conditions
    res = obj.semanticObject.preCondition ( ASGNode.DRAG, x, y ) 
    if res: 
      return self.constraintViolation(res)		        
    
    # Execute global pre-actions
    self.ASGroot.preAction(ASG.DRAG, x, y)		
    # Execute local pre-actions                 
    obj.semanticObject.preAction ( ASGNode.DRAG, x, y )           
    
    # Local post condition
    res = obj.semanticObject.postCondition (ASGNode.DRAG, x, y)   	
    if res: 
      self.constraintViolation(res)	             
    
    # Local post condition
    res = self.ASGroot.postCondition (ASG.DRAG, x, y)	            	
    if res: 
      self.constraintViolation(res)	                       
    
    # Execute global post-actions
    self.ASGroot.postAction(ASG.DRAG, x, y)	
    # Execute local post-actions		                  
    obj.semanticObject.postAction ( ASGNode.DRAG, x, y )  




def dragMotion(self, lastCoords, newCoords, objectSelectionSet, 
                applyMultiEntityMotion=False):
  """
  Moves all selected objects on the canvas with the mouse's motion
  """
  
  # Calculate the displacement in x and y
  dx = newCoords[0] - lastCoords[0]          
  dy = newCoords[1] - lastCoords[1]
  
  # Multiple objects moving, speed things up! 
  # If applyMultiEntityMotion, then do the actual moving
  if(not applyMultiEntityMotion and len(objectSelectionSet) > 1):
    Drag.CURR_INSTANCE.move(dx, dy)
    return
    
     
  for obj in objectSelectionSet:
  
    # Evaluate global pre-conditions 
    res = self.ASGroot.preCondition(ASG.MOVE, newCoords[0], newCoords[1], 
          lastCoords[0], lastCoords[1])	         
    if res: 
      return self.undodrag(res)
    
    # Evaluate global pre-conditions
    res = obj.semanticObject.preCondition(ASG.MOVE, newCoords[0], newCoords[1], 
              lastCoords[0], lastCoords[1])	
    if res: 
      return self.undodrag(res)	
    
    # Execute global pre-actions
    self.ASGroot.preAction(ASG.MOVE, newCoords[0], newCoords[1], 
              lastCoords[0], lastCoords[1])			
    # Execute local pre-actions
    obj.semanticObject.preAction(ASG.MOVE, newCoords[0], newCoords[1], 
              lastCoords[0], lastCoords[1])		
    
    # Move object (We do not care wether it is a link or an entity)
    obj.Move(dx, dy)	
    
    # Evaluate global pre-conditions
    res = self.ASGroot.postCondition(ASG.MOVE, newCoords[0], newCoords[1], 
                lastCoords[0], lastCoords[1])		
    if res: 
      return self.dragMotionUndo(res, dx, dy, obj)
    
    # Evaluate global pre-conditions
    res = obj.semanticObject.postCondition(ASG.MOVE, newCoords[0], newCoords[1], 
                lastCoords[0], lastCoords[1])	
    if res: 
      return self.dragMotionUndo(res, dx, dy, obj)	

    # Execute global post-actions
    self.ASGroot.postAction(ASG.MOVE, newCoords[0], newCoords[1], 
                lastCoords[0], lastCoords[1])
    # Execute local post-actions
    obj.semanticObject.postAction(ASG.MOVE, newCoords[0], newCoords[1], 
                lastCoords[0], lastCoords[1])	  

  
       
       
       
def dragMotionUndo(self, res, dx, dy, obj):
  """
  Undoes an entity movement, due to a constraint failure...
  """
  obj.Move(-dx, -dy)
  return self.constraintViolation(res)	


        
def dragDrop(self, objectSelectionSet ):
  """
  Done dragging... drop all the objects where this last event occurs
  """
  #todo: add auto-suggest QOCA
  #
  if(len(objectSelectionSet) > 1):
    lastCoords, newCoords = Drag.CURR_INSTANCE.destroy()
    dragMotion(self, lastCoords, newCoords, objectSelectionSet,
               applyMultiEntityMotion=True)
  
  for obj in objectSelectionSet:

    # Evaluate global pre-conditions
    res = self.ASGroot.preCondition(ASG.DROP)		
    if res: 
      return self.undodrag(res)
    # Evaluate local pre-conditions
    res = obj.semanticObject.preCondition(ASG.DROP)	
    if res: 
      return self.undodrag(res)	
    
    # Execute global pre-actions
    res = self.ASGroot.preAction(ASG.DROP)		
    # Execute local pre-actions
    res = obj.semanticObject.preAction(ASG.DROP)		
        
    # Evaluate global pre-conditions
    res = self.ASGroot.postCondition(ASG.DROP)		
    if res: 
      return self.constraintViolation(res)	
    # Evaluate local pre-conditions
    res = obj.semanticObject.postCondition(ASG.DROP)	
    if res: 
      return self.constraintViolation(res)		
    
    # Execute global post-actions
    res = self.ASGroot.postAction(ASG.DROP)		
    # Execute local post-actions
    res = obj.semanticObject.postAction(ASG.DROP)	
    
  # Status changed!
  self.statusbar.event(self.statusbar.MODEL, self.statusbar.MODIFY)
  
  #todo: new qoca
  # Initiates an automatic QOCA re-solve, since drop action probably changed
  # something... 
  if(self.qocaAutosolve):    
    varValueList = []
    for obj in objectSelectionSet:
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
    
    # QOCA can mess up the arrows :(
    optimizeConnectionPorts(self, entityList=objectSelectionSet)

  
  
