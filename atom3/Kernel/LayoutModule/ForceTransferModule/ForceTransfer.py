"""
ForceTransfer.py

Applies force to all nodes that are too close to each other
Loops until a stable configuration is reached
Times out after X iterations, to avoid depriving the user of interactivity 
for too long.

Distance specifies how far apart you want your nodes
Force constant determines how much force (and how quickly) is applied

This algorithm is O(k*n^2) where k is the max number of iterations.
Note: typically the max number of iterations is not reached.

Created by Denis Dube
Last updated Sept. 2005
"""

import math
import time
import sys

from FTAOptionsKeys import MIN_NODE_DISTANCE, MIN_LINK_DISTANCE
from FTAOptionsKeys import SEPERATION_FORCE, MAX_TOTAL_ITERATIONS
from FTAOptionsKeys import BORDER_DISTANCE, USE_SPLINES, ARROW_CURVATURE
from FTAOptionsKeys import PROMOTE_EDGE_TO_NODE

from Object import Object

def doForceTransfer(abstractGraph, optionsDict):
  """
  Applies FTA, the node overlap prevention algorithm
  """
  
  # Promote directed edges to hyperedges, useful if the edge has a large drawing
  # then that drawing becomes a node, and two new directed edges are created.
  if(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Always'):
    abstractGraph.promoteDirectedEdge(True)
  elif(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Smart'):
    abstractGraph.promoteDirectedEdge(False)
  
  # Initilize the datastructure for all objects
  Object.objList = []
  
  # Build internal datastructure for nodes
  for abstractNode in abstractGraph.getAbstractNodeList():
    #print 'abstractNode', abstractNode.getDistinctiveName()
    Object(abstractNode, optionsDict[MIN_NODE_DISTANCE])
 
  # Build internal datastructure for edges
  if(optionsDict[MIN_LINK_DISTANCE]):
    for abstractEdge in abstractGraph.getAbstractEdgeList():
      #print 'abstractEdge', abstractEdge, str(abstractEdge)
      Object(abstractEdge, optionsDict[MIN_LINK_DISTANCE])
      
      
  totalNodes = len(Object.objList)  
  
  # Trivial non-overlap case
  if(totalNodes <= 1):
    return
  
      
  # Keep at it till the layout is stable or max iterations reached
  i = 0
  maxIterations = optionsDict[MAX_TOTAL_ITERATIONS]
  seperationForce = optionsDict[SEPERATION_FORCE]
  while(__calculationLoop(seperationForce, totalNodes) and i < maxIterations):
    i += 1
    
  # Keep the whole thing in the viewable area of the canvas
  __forceObjectsIntoViewArea(optionsDict)
  
  # Apply the new coordinates
  for obj in Object.objList:
    obj.applyNewCoords()
      
  # All that moving stuff around can mess up the connections...
  __optimizeArrows(abstractGraph, optionsDict)
      
      
      
def __forceObjectsIntoViewArea(optionsDict):
  """
  Use:
    Keeps the whole thing in the viewable area of the canvas
    Functionality is disabled on negative border distances
  """
  if(optionsDict[BORDER_DISTANCE] < 0):
    return
  
  minY = minX = sys.maxint
  for node in Object.objList:
    x, y = node.getCoords()
    if(x < minX): 
      minX = x
    if(y < minY): 
      minY = y
    
  # Add minimum distance from the edge of the canvas border
  forceIsNeeded = False
  borderDistance = optionsDict[BORDER_DISTANCE]
  if(minX < borderDistance):
    minX = abs(minX) + borderDistance
    forceIsNeeded = True
  else:
    minX = 0
  if(minY < borderDistance):
    minY = abs(minY) + borderDistance
    forceIsNeeded = True
  else:
    minY = 0
    
 
  # Add the position recentering to the position
  if(forceIsNeeded):
    for node in Object.objList:
      node.recenteringPush((minX, minY))
    
      
      
def __optimizeArrows(abstractGraph, optionsDict):
  """
  Post-process to redraw arrows affected by moving nodes
  """
  # Post-process, redraw the arrows
  for arrow in abstractGraph.getAbstractEdgeList():
    arrow.setLinkOptimization(optionsDict[USE_SPLINES], 
                               optionsDict[ARROW_CURVATURE])



def __calculationLoop(seperationForce, totalNodes):
  """ Loop through all the nodes """
  isMoving = False
  
  # Go through all the nodes, and find the overlap forces
  i = 0
  j = 1
  while(i < totalNodes):
    while(j < totalNodes):
      if(i != j):      
        if(__forceCalculation(seperationForce, 
                              Object.objList[i], Object.objList[j])):
          isMoving = True
      j += 1
    i += 1
    j = i
    
  # Go through all the nodes and apply the forces to the positions
  for node in Object.objList:
    node.commitForceApplication()
    
  return isMoving
      
      
def __forceCalculation(seperationForce, n1, n2):
  """
  Use:
    Evaluates distances betweens nodes (ie: do they overlap) and
    calculates a force sufficient to pry them apart.
  Returns:
    True if some nodes are still moving
    False if nothing changes
  """
    
  # Absolute distance along X and Y vectors between the nodes
  pointA = n1.getCenter()
  pointB = n2.getCenter()
  
  dx = pointB[0] - pointA[0] 
  dy = pointB[1] - pointA[1] 
  
  # Zero division error prevention measures
  if (dx == 0.0):      
    dx = 0.1
  if(dy == 0.0):      
    dy = 0.1
    
  # Node-Node Distances
  dist = math.sqrt(dx*dx+dy*dy)
  unitVector = [ dx / dist , dy / dist ]

  # Overlap due to size of nodes
  sizeA = n1.getSize()
  sizeB = n2.getSize()
  sizeOverlap = [ (sizeA[0] + sizeB[0]) / 2 , (sizeA[1] + sizeB[1]) / 2 ]  
    
  # Desired distance with resulting force
  minSeperationDist = min(n1.getSeperationDistance(), n2.getSeperationDistance())
  d1 = (1.0 / unitVector[0]) * (sizeOverlap[0] + minSeperationDist)
  d2 = (1.0 / unitVector[1]) * (sizeOverlap[1] + minSeperationDist)
  forceMagnitude = seperationForce * (dist - min(abs(d1), abs(d2)))
  
  # The force should be less than -1 (or it won't be having much of an effect)
  if (forceMagnitude < -1):     
      
    # Add up the forces to the two interacting objects
    # Maximize compactness by only pushing nodes along a single axis
    if(abs(dx) > abs(dy)):   
      # X force only
      force = forceMagnitude * unitVector[0]
      n1.forceIncrement([force, 0])
      n2.forceIncrement([-force, 0])
    else:                        
      # Y force only
      force = forceMagnitude * unitVector[1]
      n1.forceIncrement([0, force])
      n2.forceIncrement([0, -force])

    # If a force was applied this iteration, definately not stable yet
    return True
  return False    
      

     
 
      

    
