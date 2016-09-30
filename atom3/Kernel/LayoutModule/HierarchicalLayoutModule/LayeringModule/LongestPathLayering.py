"""
LongestPathLayering.py

By Denis Dube, Sept. 2005
"""


def LongestPathLayering(wrappedNodeList):
  """
  This is a simple layering algorithm that places nodes in layers from the 
  leaves to the root. The height is no greater than the longest path from
  a leaf to the root. 
  The implementation is provided for reference in the LNCS article:
    A Heuristic for Minimum-Width Graph Layering with Consideration of Dummy 
    odes.
    By: Alexandre Tarassov and Nikola S. Nikolov and Jurgen Branke
  This algorithm is implemented as O(n^2)
  Requires approximately 0.3 seconds for 127 nodes, 135 edges on P4-3.2ghz
  
  NOTE: Algorithm not optimized. It has a O(n) implementation according to 
  "Drawing graphs: methods and models" 
  by Oliver Bastert and Christian Matuszewski
  """
  
  unassignedNodeList = wrappedNodeList[:]
  assignedNodesCurrentLayer = [] # U
  assignedNodesInSubLayers = [] # Z
  currentLayerInt = 0
#  print '-------------------- Layer 0 --------------'
  while(unassignedNodeList):

    # Choose an unassigned node
    for node in unassignedNodeList:
#      print 'Node:', node, node.children.keys()
      
      # Check if this node has a successor that is not already layer assigned
      wasNodeSelected = True
      for child in node.children.keys():
        if(child not in assignedNodesInSubLayers):
          wasNodeSelected = False
          break
      
      # If selected, no successor in unassigned layer, set the nodes layer!
      if(wasNodeSelected):
        unassignedNodeList.remove(node)
        node.setLayer(currentLayerInt) # Make each node aware of its layer
        assignedNodesCurrentLayer.append(node)
        break

    if(not wasNodeSelected):
      currentLayerInt += 1
      assignedNodesInSubLayers += assignedNodesCurrentLayer
      assignedNodesCurrentLayer = []
#      print '-------------------- Layer ', currentLayerInt, ' --------------'
  
  # Re-order all the layers to be consistent with my other layering alg.
  for node in wrappedNodeList:
    node.setLayer(currentLayerInt - node.getLayer())
    
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