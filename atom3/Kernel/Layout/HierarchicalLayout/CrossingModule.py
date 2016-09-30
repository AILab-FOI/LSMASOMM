"""
CrossingModule.py

Collection of algorithms responsible for phase II of Sugiyama-style hierarchical
layout... crossing reduction.

By Denis Dube, 2005
"""

import sys
import random

from NodeWrapper import NodeWrapper


def barycentricOrdering(levelDictionary, phaseOneMax, phaseTwoMax):
  """
  Given a dictionary mapping of integer levels to nodes
  Re-orders the nodes on each level to have fewer edge crossings
  Implementation draws from:
    CROSSING REDUCTION FOR LAYERED HIERARCHICAL GRAPH DRAWING
    By PITCH PATARASUK
  However, I don't perform same barycenter order reversals; for some reason
  this yielded MORE crossings rather than less. I DO use random order 
  restarts however, which has given me good to optimal results in tests.
  """

    
  # Init variables
  totalLevelsInt = len(levelDictionary.keys())
  bestGlobalCrossings = sys.maxint   # Minimum # of crossings found so far
  bestLevelDictionary = None         # Copy of the level dict with min cross
  phaseOneIterations = 0
  phaseTwoIterations = 0
  
  # Initilize layer orderings 
  for level in levelDictionary.values():
    __updateOrder(level)
  
  # Main crossing reduction loop
  while(phaseTwoIterations < phaseTwoMax):
    
    # Iterate over all the levels in the level dictionary
    # If totalLevelsInt = 3, then this range yields [0, 1]
    for j in range(0, totalLevelsInt - 1):
      
      ## Down-Barycenter (Parent to child)
      for node in levelDictionary[j]:
        node.computeBarycenter(True)
      # Sort the list in place according to barycenter values
      levelDictionary[j].sort(lambda a, b: cmp(a.getBarycenter(),
                                               b.getBarycenter()))
      # Save the node's sorted position in it's internal parameter
      __updateOrder(levelDictionary[j])
              
      ## Up-Barycenter (Child to parent)
      for node in levelDictionary[j + 1]:
        node.computeBarycenter(False)
      # Sort the list in place according to barycenter values
      levelDictionary[j + 1].sort(lambda a, b: cmp(a.getBarycenter(),
                                                   b.getBarycenter()))
      # Save the node's sorted position in it's internal parameter
      __updateOrder(levelDictionary[j + 1])
      

    # Count crossings
    globalCrossings = 0
    for j in range(0, totalLevelsInt - 1):        
      globalCrossings += countCrossings(levelDictionary[j], 
                                               levelDictionary[j + 1])
      
    # Did the last iteration of the algorithm reduce crossings?
    if(globalCrossings < bestGlobalCrossings):
      # Crossings reduced, reset counter since more reductions are possible
      phaseOneIterations = 0        
      # Store a copy of levelDictionary, best ordering yet
      bestLevelDictionary = __copyDict(levelDictionary)            
      bestGlobalCrossings = globalCrossings    
    else:
      # Crossings not reduced, keep trying, might reduce later
      phaseOneIterations += 1
      if(phaseOneIterations > phaseOneMax):
        # Reductions have ceased, try a random restart...
        phaseOneIterations = 0
        phaseTwoIterations += 1
        
        # Randomize layer orderings
        for currentLevel in levelDictionary.values():
          indexList = range(0, len(currentLevel))
          shuffledList = indexList[:]
          random.shuffle(shuffledList)
          for k in shuffledList:
            currentLevel[indexList.pop()].setOrder(k)
      
  # Return the levelDictionary with the least crossings
  return bestLevelDictionary
         

         
def countCrossings(layerA, layerB):
  """
  Inputs: layerA and layerB are lists of NodeWrapper objects
  Output: # of crossings between two node layers in O(|E| log |Vsmall|)
  
  NOTE: Most other algorithms for this are O(|E| + Number of crossings)
  Implementation of:
    Simple and Efficient Bilayer Cross Counting
    Wilhelm Barth, Michael Junger, and Petra Mutzel
    GD 2002, LNCS 2528, pp. 130-141, 2002
  """
  # Assumed that layerA is above layerB, so children of A are in B
  # Now figure out which layer is smaller to improve running time a bit
  if(len(layerA) < len(layerB)):
    smallLayer = layerA
    largeLayer = layerB
    isParent2Child = False
  else:
    smallLayer = layerB
    largeLayer = layerA
    isParent2Child = True
  
 
  # Sort the edges and come up with a sequence of edges (integer indices)
  edgeSequence = []
  for node in largeLayer:
    tempList = []
    # Get all possible nodes connected to this node
    targetNodeList = NodeWrapper.Source2TargetListMap[node]
    for targetNode in targetNodeList:
      # Restrict ourselves to just those nodes that are in smallLayer
      if(targetNode in smallLayer):
        #print 'targetNode.getOrder()', targetNode, targetNode.getOrder()
        tempList.append(targetNode.getOrder())
    tempList.sort()
    edgeSequence.extend(tempList)
    
  # Build the accumulator tree
  firstindex = 1    
  while(firstindex < len(smallLayer)):
    firstindex *= 2
  treesize = (2 * firstindex) - 1
  firstindex -= 1
  tree = dict() # Heh, python dictionaries are so abused :)
  for i in range(0, treesize):
    tree[i] = 0
  
  # Count the crossings
  crosscount = 0
  for k in range(0, len(edgeSequence)):
    index = edgeSequence[k] + firstindex
    tree[index] += 1
    while(index > 0):
      if(index % 2):
        crosscount += tree[index + 1]
      index = (index - 1) / 2
      tree[index] += 1

  return crosscount
  
  

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
    
def __copyDict(levelDictionary):
  """ Handy method to make a real copy of the levelDictionary """
  newDict = dict()
  for i in levelDictionary.keys():
    newDict[i] = levelDictionary[i][:]
  return newDict
