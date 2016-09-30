"""
AdjacentExchange.py

Greedy crossing minimization algorithm. It is best used as a post-processing
step since it works very locally. Complexity is O(n^2).
On the other hand, even when used on its own it can sometimes yield better 
results than a deterministic Adjacent Exchange. 

Algorithm Adjacent Exchange = Greedy Switching = Transpose (3 different names!)

Litterature behind this algorithm: 
  "Drawing graphs: methods and models"
  by Oliver Bastert and Christian Matuszewski in Springer-Verlag book, 2001
  
  "Heuristics for reducing crossings in 2-layered networks"
  by P. Eades and D. Kelly in Ars Combinatoria, 21(a):89--98, 1986.
  
  The 1986 source had a description of how to compute crossing numbers I found
  quite helpful. Although I still had to do some paperwork to figure it out.

By Denis Dube, 2005
"""

import sys
from random import shuffle

from Utilities import updateOrder
from Utilities import copyDict
#from Utilities import prettyPrintList # Debug

from CrossingCounter import countAllCrossings




def AdjacentExchange(levelDictionary, maxNoProgressRounds, maxTotalRounds,
                                                          useRandomRestarts):
  """
  This is just a layer-by-layer sweeper. Pretty much the same as that used in
  the Barycenter and HorizontalPositioner algorithms. Litterally a copy-paste
  job. The meat of this algorithm is in the getCrossingMatrix() and 
  adjacentExchangeHeuristic() methods.
  
  Use:
    Reduces crossings between each pair of layers in a k-layer graph by sweeping
    down/up the layers. This is done by re-ordering the nodes.
  Parameters:
    levelDictionary, dictionary where keys are levels, values are node lists
    maxTotalRounds, hard maximum on number of crossing reduction rounds
    maxNoProgressRounds, maximum number of consecutive rounds with no crossing
                         reduction
    useRandomRestarts, enables random restarting when no progress is being made
  Returns:
    levelDictionary, modified with a reduced crossing ordering.
  """
    
  # Init variables
  totalLevelsInt = len(levelDictionary.keys())
  currentRound = 0
  currentNoProgressRound = 0
  if(useRandomRestarts):
    roundsUntilTryRandom = 0
  else:
    roundsUntilTryRandom = sys.maxint # In other words: NEVER!
    
  # Initilize layer orderings 
  for level in levelDictionary.values():
    updateOrder(level)
    
  bestGlobalCrossingsInt = countAllCrossings(levelDictionary)
  bestOrderingDict = copyDict(levelDictionary)
  
  print 'Edge crossings before Adjacent Exchange crossing reduction:', 
  print bestGlobalCrossingsInt, '\n'
  
  if(bestGlobalCrossingsInt == 0):
    return levelDictionary
  
  # Global-graph crossing reduction loop: runs infintely long because
  # the down and up sweeps will undo each other's work at some point.
  # Therefore, must halt after maxTotalRounds iterations, or check for 
  # convergence in the number of global crossings.
  while(currentRound < maxTotalRounds):
    currentRound += 1
    
#===============================================================================
#    Down layer sweeper
#    The main down-sweep loop will run at most |levelDictionary| times
#===============================================================================
    isMakingProgress = True
    while(isMakingProgress):
      crossingMatrix = getCrossingMatrix(levelDictionary, True)
      if(adjacentExchangeHeuristic(levelDictionary, crossingMatrix, True)):
        isMakingProgress = True
      else:
        isMakingProgress = False
          
#===============================================================================
#    Up layer sweeper
#    The main up-sweep loop will run at most |levelDictionary| times
#===============================================================================
    isMakingProgress = True
    while(isMakingProgress):
      crossingMatrix = getCrossingMatrix(levelDictionary, False)
      if(adjacentExchangeHeuristic(levelDictionary, crossingMatrix, False)):
        isMakingProgress = True
      else:
        isMakingProgress = False
      
#===============================================================================
#    Convergence Test: Check if crossings are still reducing
#===============================================================================
  
    currentCrossings = countAllCrossings(levelDictionary)
    print 'Current round:', currentRound, 'of', maxTotalRounds
    print '    Current crossings:', currentCrossings, '(Best so far:',
    print str(bestGlobalCrossingsInt) + ')'
        
    # No crossings: HALT
    if(currentCrossings == 0):
      print '\nCrossing minimization yielded 0 crossings in', currentRound, 
      print 'rounds!\n'
      return levelDictionary
    
    # Better crossings than ever seen before, save it!
    elif(currentCrossings < bestGlobalCrossingsInt):
      bestGlobalCrossingsInt = currentCrossings
      bestOrderingDict = copyDict(levelDictionary)
      currentNoProgressRound = 0
      
    # No crossing reduction... *cries*
    else:
      currentNoProgressRound += 1      
      print '<< No progress round:', currentNoProgressRound, 'of', 
      print maxNoProgressRounds, '>>'
      
      # No progress: HALT
      if(currentNoProgressRound >= maxNoProgressRounds):
        print '\nCrossing minimization terminated early, max rounds without', \
              'crossing reduction reached at round', currentRound
        print 'Edge crossings after Adjacent Exchange crossing reduction:', 
        print bestGlobalCrossingsInt, '\n'  
        for layer in bestOrderingDict.values():
          updateOrder(layer)
        return bestOrderingDict
        
      # Randomization: roundsUntilTryRandom is sys.maxint if disabled
      elif(roundsUntilTryRandom <= 0):
        # Reset roundsUntilTryRandom, proportional to number of levels
        # Why? Because more levels need more time to propagate changes...
        roundsUntilTryRandom = max(1, int(totalLevelsInt / 10))
        for layer in levelDictionary.values():
          shuffle(layer)
          updateOrder(layer)
        print '|| Vertex ordering randomized ||'
          
      else:
        roundsUntilTryRandom -= 1
    
  print '\nCrossing minimization reached max rounds', currentRound
  print 'Edge crossings after Adjacent Exchange crossing reduction:', 
  print bestGlobalCrossingsInt, '\n'  
  return bestOrderingDict



def adjacentExchangeHeuristic(levelDictionary, crossingMatrix, isGoingDown):
  """
  This heuristic is run on all the layers of the levelDictionary until no more
  improvements can be made. Switching two vertices always yields a reduction
  in crossings from the affected layer's point of view. The reduction is exactly
  equal to the crossing number of the previous order of the nodes minus the
  crossing number of the new order of the nodes that have just been switched.
  Parameters:
    levelDictionary: dictionary of levels containing lists of nodes
    crossingMatrix: dictionary of matrices for each layer, crossing numbers
    isGoingDown: boolean flag, True indicates scan from top to bottom
  Return:
    True if progress made, False otherwise
  """
  if(isGoingDown):
    layerRange = range(0, len(levelDictionary) - 1) # From 0 to |L| - 2
  else:
    layerRange = range(len(levelDictionary) - 1, 0, -1) # From |L| - 1 to 1
    
  currentRound = 0
  isStillSwitching = True
  while(isStillSwitching):
    currentRound += 1
    isStillSwitching = False
    for i in layerRange:
      layerMatrix = crossingMatrix[i]
      level = levelDictionary[i]
      for j in range(0, len(level) - 1): # |level| = 5 then j = [0,1,2,3]
        nodeA = level[j]
        nodeB = level[j + 1]
        # Swap them!
        if(layerMatrix[nodeA][nodeB] > layerMatrix[nodeB][nodeA]):
          #print 'Swapping', nodeA, 'with', nodeB, 'on level', i
          #printCrossingMatrix(levelDictionary, crossingMatrix, i)
          #print 'Before AE', prettyPrintList(level)
          level[j] = nodeB
          level[j + 1] = nodeA
          nodeB.setOrder(j)
          nodeA.setOrder(j + 1)
          isStillSwitching = True
          #print 'After AE', prettyPrintList(level), '\n'
  if(currentRound > 1):
    return True
  return False



def getCrossingMatrix(levelDictionary, isGoingDown):
  """
  Computes a crossing matrix for each layer of levelDictionary. For each layer
  there is a dictionary for each vertex. Each vertex then has a key that is
  another vertex on the same layer. The value is initially 0, or 0 crossings.
  The crossing numbers do not actually tell you how many crossinigs there are,
  but they do give you a tight lower bound. 
  Parameters:
    levelDictionary: dictionary of levels containing lists of nodes
    isGoingDown: True if going from top layer to bottom layer
                 False if going from bottom layer to top layer
  """
  if(isGoingDown):
    layerRange = range(0, len(levelDictionary) - 1) # From 0 to |L| - 2
    nextLayerIncrement = 1
  else:
    layerRange = range(len(levelDictionary) - 1, 0, -1) # From |L| - 1 to 1
    nextLayerIncrement = -1
    
  crossingMatrix = dict()
  for i in layerRange:
    # Create one crossing matrix for each level
    layerA = levelDictionary[i]
    layerB = levelDictionary[i + nextLayerIncrement]
    layerMatrix = dict()

    # Init layerMatrix
    for node in layerA:   
      layerMatrix[node] = dict()
    for j in range(0, len(layerA)):
      nodeA = layerA[j]
      for k in range(j, len(layerA)):
        nodeB = layerA[k]
        layerMatrix[nodeA][nodeB] = 0
        layerMatrix[nodeB][nodeA] = 0
    
    # What is a node in layerA connected to in layerB?
    for sourceNode in layerA:   
      # Get all neighbors of sourceNode in layerA that happen to be in layerB
      if(isGoingDown):
        targetNodeList = sourceNode.children.keys()
      else:
        targetNodeList = sourceNode.parents.keys()
      targetNodeList = [node for node in targetNodeList
                         if node in layerB]
      sourceNode._connectedTo = []
      for targetNode in targetNodeList:
        sourceNode._connectedTo.append(targetNode)
    
    # Go through each node in layer, in order
    for j in range(0, len(layerA) - 1):
      nodeA = layerA[j]
      for k in range(j + 1, len(layerA)):
        nodeB = layerA[k]
        # Okay, now we have that nodeA.order < nodeB.order
        # So check if in layer i + 1, neighbors of nodeA are > in order than 
        # the orders of the neighbors of nodeB
        for neighborA in nodeA._connectedTo:
          neighborAorder = neighborA.getOrder()
          for neighborB in nodeB._connectedTo:
            if(neighborAorder > neighborB.getOrder()):
              layerMatrix[nodeA][nodeB] += 1
            elif(neighborAorder < neighborB.getOrder()):
              layerMatrix[nodeB][nodeA] += 1
    
    # Cleanup
    for sourceNode in layerA: 
      del sourceNode._connectedTo
    crossingMatrix[i] = layerMatrix
  return crossingMatrix
  
  
  
def compareCrossingMatrices(c1, c2):
  """ DEBUG:  Returns True if c1 == c2, else False """
  for i in range(0, len(c1)):
    layerMatrixA = c1[i]
    layerMatrixB = c2[i]
    for nodeA in layerMatrixA.keys():
      for nodeB in layerMatrixA.keys():
        if(layerMatrixA[nodeA][nodeB] != layerMatrixB[nodeA][nodeB]):
          print 'COMPARE', layerMatrixA[nodeA][nodeB] , layerMatrixB[nodeA][nodeB]
          print str(nodeA), str(nodeB)
          return False
  return True
      
  
  
def printCrossingMatrix(levelDictionary, crossingMatrix, thisLevelOnly=None):
  """ DEBUG:   does what the name says  """
  def list2string(someList):
    newString = ''
    for item in someList:
      newString += ' ' + str(item) + ' |'
    return newString
    
    
  if(thisLevelOnly):
    layer = levelDictionary[thisLevelOnly]
    layerMatrix = crossingMatrix[thisLevelOnly]
    # Top line
    print '|    |' + list2string(layer)
    for rowNode in layer:
      print '| ' + str(rowNode) + ' |',
      for colNode in layer:
        print ' ' + str(layerMatrix[rowNode][colNode]) + ' |',
      print '\n'
  else:    
    for i in range(0, len(levelDictionary)):
      layer = levelDictionary[i]
      layerMatrix = crossingMatrix[i]
      # Top line
      print '|    |' + list2string(layer)
      for rowNode in layer:
        print '| ' + str(rowNode) + ' |',
        for colNode in layer:
          print ' ' + str(layerMatrix[rowNode][colNode]) + ' |',
        print '\n'

  