"""
BFSLayering.py

By Denis Dube, Sept. 2005
"""


def BFSLayering(wrappedNodeList):
  """
  This algorithm assigns each node in the wrappedNodeList a layer, working 
  its way from the root nodes all the way to the leaves.
  This algorithm is the simplest & fastest for layering, and minimizes height.
  Unfortunately, it does not bound the width at all!
  The algorithm works in O(n)
  Requires approximately 0 seconds for 127 nodes, 135 edges on P4-3.2ghz 
  """
    
  # Get roots in the acyclic graph (wrappedNodeList is topologically sorted)
  rootNodes = []
  for wrappedNode in wrappedNodeList:
    if(len(wrappedNode.parents.keys()) == 0):
      rootNodes.append(wrappedNode)
                 
#  print "rootNodes"
#  for node in rootNodes:
#    print '   ', str(node)
  
  # Place each node on a layer, does BFS
  # NOTE: This may set a single node's layer more than once but since
  #       a topological sort is in effect, the last one is the "right" one...
  queuedNodes = rootNodes[:]
  currentLevelInt = 0
  while(len(queuedNodes) > 0):
    tempQueue = list()
    for node in queuedNodes:
      node.setLayer(currentLevelInt) # Make each node aware of its layer
      tempQueue += node.children.keys() # Children of this node
    queuedNodes = tempQueue
    currentLevelInt += 1

  return __buildLevelDictionary(wrappedNodeList)
  
  

def __buildLevelDictionary(wrappedNodeList):
  """
  wrappedNodeList assumed to contain nodes already assigned a layer
  Returns a dictionary indexed by integer level of lists of nodes
  """
      
  # Build the level dictionary for easy access to node layers
  levelDictionary = dict()
  for node in wrappedNodeList:
    currentLevelInt = node.getLayer()
    if(not levelDictionary.has_key(currentLevelInt)):
      levelDictionary[currentLevelInt] = [node]
    else:
      levelDictionary[currentLevelInt].append(node)
      
  #debugLevelDict(levelDictionary)
    
  # Add dummy nodes as neccessary to finish the levelDictionary...
  return levelDictionary