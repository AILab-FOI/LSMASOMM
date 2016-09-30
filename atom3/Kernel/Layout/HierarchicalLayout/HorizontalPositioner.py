"""
HorizontalPositioner.py

Algorithms dealing with the third phase of Sugiyama-style hierarchical layout,
horizontal position assignment of each node (while respecting node order).

By Denis Dube, Sept. 2005
"""

import sys
import math

from NodeWrapper import NodeWrapper


def priorityBarycenterPositioner(levelDictionary, maxIterations):
  """
  Given a layering & ordering of nodes, this will set them on a grid such
  that they respect the layering and ordering but such that nodes are as
  close as possible (horizontally) to their children and parents.
  This is done by sweeping up/down using barycenters.
  """    
  gridSize = 0
    
  # Re-order each level so that self-loops are close to their node 
  # NOTE: self-loops are drawn on the level below their node
  # This actually decreases the # of crossings although they're undetectable
  # by the crossing counting algorithm
  for levelInt in levelDictionary.keys():
    __updateOrder(levelDictionary[levelInt])
    for node in levelDictionary[levelInt]:
      if(node in NodeWrapper.SelfLoopList):
        childParent = node.parents.keys()[0]
        
        # Get the orders of all the children of the self-loop's parent
        childOrders = []
        for child in childParent.children.keys():
          childOrders.append(child.getOrder())
        childOrders.sort()
        
        # Use the median order of all the children
        newOrder = childOrders[int(math.ceil(len(childOrders) / 2))]          
        levelDictionary[levelInt].remove(node)
        levelDictionary[levelInt].insert(newOrder, node)
        
        
  # Set priorities for node placements according to fan in, fan out, edges
  for level in levelDictionary.values():
    i = 0
    for node in level:
      # Set initial grid position and calculate node priority
      node.setGridPosition(i)
      node.calculatePriority() 

      # Get maximum horizontal grid size
      i += 1
      gridSize = max(gridSize , i)
          
  #maxIterations = self.__optionsDatabase.get('baryPlaceMax')  
  movements = 1
  iterations = 0
  # Iterate up/down, preserver order, but move to take advantage of barycenter
  while(movements > 0 and iterations < maxIterations): 
    movements = 0
    # Sweep down/up
    for i in range(0, len(levelDictionary) - 1):
      movements += __prettyNodeBarycenter(levelDictionary[i], True, 
                                                                       gridSize)
      movements += __prettyNodeBarycenter(levelDictionary[i + 1], False,
                                                                       gridSize)
    iterations += 1
    
  # Make sure we are globally flushed to the left
  minGridX = sys.maxint
  for level in levelDictionary.values():
    minGridX = min(minGridX, level[0].getGridPosition())
  if(minGridX != 0):
    for level in levelDictionary.values():
      for node in level:
        node.setGridPosition(node.getGridPosition() - minGridX)
    

def __prettyNodeBarycenter(levelList, isGoingDown, gridSize):
  """
  Submethod of the node placer, works on one level, in given direction
  """         
  movements = 0
  nodeInLevelIndex = 0
  # Iterate over all nodes, get their bary center, try to move them to it
  for node in levelList:
    baryCenterFloat = node.getGridBarycenter(isGoingDown)
    
    # No children/parent
    if(baryCenterFloat == None):
      continue
      
    desiredGridPosition = int(round(baryCenterFloat))      
    currentGridPosition = node.getGridPosition()
    
    # If not at desired spot, try to move there
    if(currentGridPosition != desiredGridPosition):
      isMovingRight = desiredGridPosition > currentGridPosition
      movements += __move(levelList, nodeInLevelIndex, node, isMovingRight, 
                                                                      gridSize)
      
    nodeInLevelIndex += 1   
  return movements
  

def __move(levelList, nodeInLevelIndex, moveNode, isMovingRight, gridSize):
  """
  Sub-submethod... this will recusively try to move a node horizontally
  to the right or left. The recursion occurs if a node moving to a new
  location must displace a node already occupying the spot. Move will
  fail if a node being nudged away has priority or grid boundary reached
  """
  newGridPosition = moveNode.getGridPosition() + (-1, 1)[isMovingRight]
  
  # Can we move there? Target in bounds?
  if(newGridPosition < 0 or newGridPosition > gridSize):
    return 0
        
  neighborIndex = nodeInLevelIndex + (-1, 1)[isMovingRight] # +/- 1 index
  # No neighbor to the right! We can move there
  if(isMovingRight and neighborIndex > len(levelList) - 1):
    isMoving = True
    
  # No neighbor to the left! We can move there
  elif(not isMovingRight and neighborIndex < 0):
    isMoving = True
    
  # Have to shove the neighbor out of his spot...
  else:   
    isMoving = False   
    neighborNode = levelList[neighborIndex]
    neighborGridPosition = neighborNode.getGridPosition()      
    # Neighbor definately in our spot...
    if(neighborGridPosition == newGridPosition):
      movePriority = moveNode.getPriority() 
      neighborPriority = neighborNode.getPriority()
      # Do we out-prioritize the neighbor?
      if(movePriority > neighborPriority):
        isMoving = __move(levelList, neighborIndex, 
                        neighborNode, isMovingRight, gridSize)
    else:
      isMoving = True
    
  # We can move, set new grid position
  if(isMoving):
    moveNode.setGridPosition(newGridPosition)
    return 1  
  return 0


  
    
def __updateOrder(orderedLayer):
    """ 
    The ordering is implicit in the node sequence in the list
    However to do a node sort, it's handy to have each node know its order
    This order is used only within __barycentricOrdering() except for debug
    """
    i = 0
    for node in orderedLayer:
      node.setOrder(i)
      i += 1