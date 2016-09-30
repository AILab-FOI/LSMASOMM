"""
PriorityBarycenter.py

By Denis Dube, Sept. 2005
"""

import sys
import math

from HierarchicalLayoutModule.NodeWrapper import NodeWrapper



def PriorityBarycenter(levelDictionary, maxTotalRounds):
  """
  Given a layering & ordering of nodes, this will set them on a grid such
  that they respect the layering and ordering but such that nodes are as
  close as possible (horizontally) to their children and parents.
  This is done by sweeping up/down using barycenters.
  """    
    
  # Re-order each level so that self-loops are close to their node 
  # NOTE: self-loops are drawn on the level below their node
  # This actually decreases the # of crossings although they're undetectable
  # by the crossing counting algorithm
  # NOTE2: This should be a post-process of crossing reduction no?
  for levelInt in levelDictionary.keys():
    __updateOrder(levelDictionary[levelInt])
    for node in levelDictionary[levelInt]:
      if(node in NodeWrapper.SelfLoopList):
        childParent = node.parents.keys()[0]
        
        # Get the orders of all the children of the self-loop's parent
        childOrders = []
        for child in childParent.children.keys():
          childOrders.append(child.getOrder()) # What if on a distant layer?!
        childOrders.sort()
        
        # Use the median order of all the children
        newOrder = childOrders[int(math.ceil(len(childOrders) / 2))]          
        levelDictionary[levelInt].remove(node)
        levelDictionary[levelInt].insert(newOrder, node)
        
        
  # Set initial grid position and calculate node priority
  # Priority = vertex degree or infinity for dummy vertices
  for level in levelDictionary.values():
    for i in range(0, len(level)):
      level[i].setGridPosition(i)
      level[i].calculatePriority() 
      
#===============================================================================
#  Layer-by-layer sweeper
#===============================================================================
      
  # Global-graph horizontal positioning loop: runs infintely long because
  # the down and up sweeps will undo each other's work at some point.
  # Therefore, must halt after maxTotalRounds iterations.
  currentRound = 0
  totalLevelsInt = len(levelDictionary)
  while(currentRound < maxTotalRounds):
    currentRound += 1
    lastGridPosDict = copyGridPos(levelDictionary)
#===============================================================================
#    Down Barycenter layer sweeper
#    The main down-sweep loop will run at most |levelDictionary| times
#===============================================================================
    isMakingProgress = True
    while(isMakingProgress):
      isMakingProgress = False
      # Iterate over all the levels in the level dictionary
      # If totalLevelsInt = 3, then this range yields [0, 1]
      for j in range(0, totalLevelsInt - 1):
        # Sort the list in place according to barycenter values
        if(__prettyNodeBarycenter(levelDictionary[j], True)):          
          isMakingProgress = True
    
#===============================================================================
#    Up Barycenter layer sweeper
#    The main up-sweep loop will run at most |levelDictionary| times
#===============================================================================
    isMakingProgress = True
    while(isMakingProgress):
      isMakingProgress = False
      # Iterate over all the levels in the level dictionary
      # If totalLevelsInt = 3, then this range yields [2, 1, 0]
      for j in range(totalLevelsInt - 1, -1, -1):                  
        # Sort the list in place according to barycenter values
        if(__prettyNodeBarycenter(levelDictionary[j], False)):          
          isMakingProgress = True

#===============================================================================
#    Convergence Testing
#===============================================================================
    isMakingProgress = False
    for i in range(0, len(levelDictionary)):
      newLayer = levelDictionary[i]
      layerSize = len(newLayer)
      lastLayerGridPos = lastGridPosDict[i]
      for j in range(0, layerSize):
        # Did a grid position change? Yes --> still making progress
        if(newLayer[j].getGridPosition() != lastLayerGridPos[j]):
          isMakingProgress = True
          break
      # This check prevents the positions from shifting by 1 each iteration
      # without actually changing anything (Fake progress).
      if(newLayer[0].getGridPosition() > 0 \
        or newLayer[-1].getGridPosition() < layerSize - 1):
        isMakingProgress = False
        break
      elif(isMakingProgress):
        break
        
    if(not isMakingProgress):
      print '   Convergence occured after round:', currentRound
      break
    else:
      print '   Completed round:', currentRound, 'of', maxTotalRounds
      

            
#===============================================================================
#  Post-processing: Make sure nodes are globally flushed to the left
#===============================================================================
  minGridX = sys.maxint
  for level in levelDictionary.values():
    minGridX = min(minGridX, level[0].getGridPosition())
    
  if(minGridX != 0):
    for level in levelDictionary.values():
      for node in level:
        node.setGridPosition(node.getGridPosition() - minGridX)
  
  

def __prettyNodeBarycenter(levelList, isGoingDown):
  """
  Submethod of the node placer, works on one level, in given direction
  """         
  isMakingProgress = False
  # Iterate over all nodes, get their bary center, try to move them to it
  for node in levelList:
    # NOTE: Bad software design here, I just defined a new variable for node
    # todo: add this properly to NodeWrapper.py
    node._desiredGridPosition = int(round(node.getGridBarycenter(isGoingDown)))
    
  #for node in levelList:
  for i in range(0, len(levelList)):
    node = levelList[i]
    desiredGridPosition = node._desiredGridPosition
    currentGridPosition = node.getGridPosition()
    
    # If not at desired spot, try to move there (and push anyone there away)
    if(desiredGridPosition > currentGridPosition and pushMove(levelList, i, 1)):
      isMakingProgress = True
    elif(desiredGridPosition < currentGridPosition and \
                                                    pushMove(levelList, i, -1)):
      isMakingProgress = True
  return isMakingProgress
  
  
  
def pushMove(levelList, i, d):
  """
  Attempts to move the vertex at index i in levelList in the direction d, if
  a vertex V2 blocks this move, then recursive calls attempt to move V2.
  
  Parameters:
    levelList: a layer represented as a list of nodes
    i: an index into levelList, value in 0...|levelList| - 1
    d: move direction, value is either -1 (left) or +1 (right)
  """
  node = levelList[i]
  canMove = False
  # If moving left and on left margin or if moving right and on right margin
  if((d < 0 and i == 0) or (d > 0 and i == len(levelList) - 1)):
    canMove = True
    
  # No one occupies the desired position! What luck, move there.
  elif(node.getGridPosition() + d != levelList[i + d].getGridPosition()):
    canMove = True
  
  # Desired spot is blocked, if priority sufficient try to push the blocker out!
  elif(node.getPriority() > levelList[i + d].getPriority()):
    canMove = pushMove(levelList, i + d, d) 
  
  # We can move, set new grid position
  if(canMove):
    #print 'MOVING', str(node), node.getGridPosition(),'to', node.getGridPosition() + d
    node.setGridPosition(node.getGridPosition() + d)
    return True
  return False
  


def copyGridPos(levelDictionary):
  """ 
  Makes a copy of all the grid positions of the vertices in levelDictionary
  """
  layerGridDict = dict()
  for i in levelDictionary.keys():
    layerGridDict[i] = []
    for node in levelDictionary[i]:
      layerGridDict[i].append(node.getGridPosition())
  return layerGridDict
    
    
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