"""
CrossingCounter.py

By Denis Dube, 2005
"""


def countAllCrossings(levelDictionary):
  """
  Returns all the edge crossings in the graph
  Input: levelDictionary where each level is a list of NodeWrapper objects
  Output: # of crossings between all the layers
  """
  edgeCrossings = 0
  for i in range(0, len(levelDictionary) - 1):
    edgeCrossings += countCrossings(levelDictionary[i], levelDictionary[i+1])
  return edgeCrossings
  

         
def countCrossings(layerA, layerB, debug=False):
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
    if(isParent2Child):
      targetNodeList = node.children.keys()
    else:
      targetNodeList = node.parents.keys()

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
  