"""
LayeringModule.py

This module is responsible for creating a proper layering of an arbitrary
directed graph. The optimal solution (minmal height and width layering) is an
NP-complete problem.

Responsibilities:
  1) Eliminate cycles
  2) Assign each node to a layer
  3) Assign dummy nodes to layers wherever edges traverse multipler layers
  
Known layering algorithms:
  1) Longest-path heuristic, minimizes height
  2) Coffman-Graham heuristic, minimizes width given an upperbound on the width
  3) Gansner et al. ILP, minimizes dummy edges
  4) Healy et al. ILP, minimizes width and dummy edges, given upperbound on
                      both the width and the height
  5) Tarassov et al. heuristic, minimizes width and width of dummy edges
  
By Denis Dube, Sept. 2005
"""
import time

from Debug import debugLevelDict, debugCrossing
from NodeWrapper import NodeWrapper



def longestPathLayeringTopDown(wrappedNodeList):
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
                 
  print "rootNodes"
  for node in rootNodes:
    print '   ', node.getName()
  
  # Place each node on a layer 
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


def longestPathLayeringBottomUp(wrappedNodeList):
  """
  This is a simple layering algorithm that places nodes in layers from the 
  leaves to the root. The height is no greater than the longest path from
  a leaf to the root. 
  The implementation is provided for reference in the LNCS article:
    A Heuristic for Minimum-Width Graph Layering with Consideration of Dummy 
    odes.
    By: Alexandre Tarassov and Nikola S. Nikolov and Jurgen Branke
  This algorithm is O(n^2)
  Requires approximately 0.3 seconds for 127 nodes, 135 edges on P4-3.2ghz
  """
  
  rejectedNodeList = []
  unassignedNodeList = wrappedNodeList[:]
  assignedNodesCurrentLayer = []
  assignedNodesInSubLayers = []
  currentLayerInt = 0
  print '-------------------- Layer 0 --------------'
  while(unassignedNodeList):

    # Choose an unassigned node
    wasNodeSelected = False
    for node in unassignedNodeList:
      # Slight optimization: ignore already rejected nodes on current layer
      if(node in rejectedNodeList):
        continue
      print 'Node:', node, node.children.keys()
      
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
      else:
        rejectedNodeList.append(node)

    if(not wasNodeSelected):
      currentLayerInt += 1
      assignedNodesInSubLayers += assignedNodesCurrentLayer
      rejectedNodeList = []
      print '-------------------- Layer ', currentLayerInt, ' --------------'
  
#  # Re-order all the layers to be consistent with my other layering alg.
#  for node in wrappedNodeList:
#    node.setLayer(currentLayerInt - node.getLayer())
    
  return __buildLevelDictionary(wrappedNodeList)
    
    
  
        

def greedyCycleRemover(wrappedNodeList):
  """
  Uses topological sort then reverses backward edges to eliminate cycles
  Returns nodes in topological sort order
  """

#    TODO: implement this idea
#    From: A Technique for Drawing Directed Graphs
#    Emden R. Gansner, Eleftherios Koutsofios, Stephen C. North, Kiem-Phong Vo
#    AT&T Bell Laboratories Murray Hill, New Jersey 07974
#It seems reasonable to try to reverse a smaller or even minimal set of edges. 
#One difficulty is that finding a minimal set (the feedback arc set problem) 
#is NP-complete [EMW] [GJ]. More important, this would probably not improve the 
#drawings. We implemented a heuristic to reverse edges that participate in many 
#cycles. The heuristic takes one non-trivial strongly connected component at a 
#time, in an arbitrary order. Within each component, it counts the number of 
#times each edge forms a cycle in a depth-first traversal. An edge with a 
#maximal count is reversed. This is repeated until there are no more 
#non-trivial strongly connected components.

    
  topSort = __getTopologicalSort(wrappedNodeList)
  
  # Debug
  print 'Topological sorting'
  for wrappedNode in wrappedNodeList:
    print '   ', wrappedNode.getName()
  
  # Reverse backward arcs to eliminate cycles 
  for nodeIndex in range(0, len(topSort)):
    wrappedNode = topSort[nodeIndex]         
    wrappedChildrenNodes = wrappedNode.children.keys()
    
    for wrappedChildrenNode in wrappedChildrenNodes:
      # If the child has a smaller index than the current node it is left
      # of the current node. That means it forms a cycle!
      if(nodeIndex > topSort.index(wrappedChildrenNode)):
                  
        # Get the link (or maybe more than one link) between parent
        # wrappedNode and child wrappedChildrenNode
        linkFlagList = wrappedNode.children[wrappedChildrenNode][:]
        
        # Remove it
        del wrappedNode.children[wrappedChildrenNode]
        del wrappedChildrenNode.parents[wrappedNode]
        
        # Reverse it
        tempList = []
        for linkFlag in linkFlagList:
          tempList.append([linkFlag[0], True]) # Reverse flag set to True
        wrappedChildrenNode.children[wrappedNode] = tempList[:]
        wrappedNode.parents[wrappedChildrenNode] = tempList[:]
      
      # Self-loop situation
      elif(nodeIndex == topSort.index(wrappedChildrenNode)):
        print 'SELFLOOP', wrappedChildrenNode.getName()
        
  return topSort
    


def addDummyNodes(levelDictionary, isGoingDown=True):
  """
  If an edge crosses more than 1 layer, a dummy node is added so the edge
  can be bent around other nodes (thus avoiding overlap, min crossing)
  """
  
  uniqueID = 0  
  # Add dummy nodes if an edge traverses > 1 layer
  for currentLevelInt in levelDictionary.keys():
    for node in levelDictionary[currentLevelInt]:       
    
      # Go through each node connected to this node
      for targetNode in NodeWrapper.Source2TargetListMap[node]:
                
        # Is the connected node more than 1 layer distant?
        targetNodeLayer = targetNode.getLayer()
        if(abs(targetNodeLayer - currentLevelInt) > 1):
        
          # Insert a dummy node here! One for each layer crossed
          
          dummyParent = node            
          linkFlagList = node.children[targetNode][:]
          del node.children[targetNode] # Why did I do this? Mmm... 
          uniqueID += 1
          
          if(targetNodeLayer > currentLevelInt):
            print 'HERE'
            i = currentLevelInt - 1
            increment = 1
            stopLevel = targetNodeLayer
          else:
            i = currentLevelInt - 1
            increment = -1
            stopLevel = targetNodeLayer
            
          #while(i != stopLevel):
          for i in range(currentLevelInt+1, targetNode.getLayer()):
            print 'I need a dummy on level', i,'to',targetNode.getLayer(), 'for child', targetNode.getName()
            # Create the dummy node, add it to level dict
            dummyNode = NodeWrapper((uniqueID, linkFlagList), 
                                     NodeWrapper.MULTI_LAYER_EDGE, i)
            levelDictionary[i].append(dummyNode)
            
            # I need to be able to trace links back and forth
            # Including the dummy nodes...
            dummyParent.children[dummyNode] = linkFlagList              
            dummyNode.parents[dummyParent] = linkFlagList
            dummyParent = dummyNode
            i += increment
            
            
          dummyNode.children[targetNode] = linkFlagList
            
  return levelDictionary


#def addDummyNodes(levelDictionary):
#  """
#  If an edge crosses more than 1 layer, a dummy node is added so the edge
#  can be bent around other nodes (thus avoiding overlap, min crossing)
#  """
#  uniqueID = 0  
#  # Add dummy nodes if an edge traverses > 1 layer
#  for currentLevelInt in levelDictionary.keys():
#    for node in levelDictionary[currentLevelInt]:       
#    
#      children = node.children.keys() # Children of this node
#      for child in children:
#        
#        # Child should be exactly 1 layer below the parent at current level
#        if(currentLevelInt < child.getLayer() - 1):
#          # Insert a dummy node here! One for each layer crossed
#          
#          dummyParent = node            
#          linkFlagList = node.children[child][:]
#          del node.children[child] 
#          uniqueID += 1
#                      
#          for i in range(currentLevelInt+1, child.getLayer()):
#            #print 'I need a dummy on level', i, 'for child', child.getName()
#            # Create the dummy node, add it to level dict
#            dummyNode = NodeWrapper((uniqueID, linkFlagList), 
#                                     NodeWrapper.MULTI_LAYER_EDGE, i)
#            levelDictionary[i].append(dummyNode)
#            
#            # I need to be able to trace links back and forth
#            # Including the dummy nodes...
#            dummyParent.children[dummyNode] = linkFlagList              
#            dummyNode.parents[dummyParent] = linkFlagList
#            dummyParent = dummyNode
#          dummyNode.children[child] = linkFlagList
#            
#  return levelDictionary

  
  
def __getTopologicalSort(wrappedNodeList):
  """
  Returns the node list as topologically sorted with forward arcs running 
  from left to right (if cycles exist, there will be backward arcs too)
  """
  def DFSlookup(node, sortedNodeList):
    """ Sub-method for topological sort, does depth first search """
    for childNode in node.children.keys(): #node.getChildrenWrappers():
      if(not childNode.isVisited()):
        childNode.setVisited()
        DFSlookup(childNode, sortedNodeList)
    sortedNodeList.append(node)
  
  sortedNodeList = []
  for node in wrappedNodeList:
    if(not node.isVisited()):    
      node.setVisited()    
      DFSlookup(node, sortedNodeList)
  sortedNodeList.reverse()
  return sortedNodeList
  
  
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
   
   
   
class MinimumWidthLayering:
  """
  This heuristic algorithm will attempt to create a layering such that 
  width is minimized (at the expense of height of course). This should
  yield far more compact layouts, and speed up the crossing minimization
  phase immensely.
  The implementation is provided for reference in the LNCS article:
    A Heuristic for Minimum-Width Graph Layering with Consideration of Dummy 
    odes.
    By: Alexandre Tarassov and Nikola S. Nikolov and Jurgen Branke
  This algorithm is O(n^2) but will be far slower than longestPathLayering
  """
  EdgeWidth = 1
  
  def __init__(self, wrappedNodeList):
    self.__wrappedNodeList = wrappedNodeList

    self.__unassignedNodeList = wrappedNodeList[:]
    self.__assignedNodesCurrentLayer = []
    self.__assignedNodesInSubLayers = []
    
    self.__currentWidthInt = 0
    self.__widthUpInt = 0  
    
  
  def __call__(self, UBW, cInteger):
    """ 
    Usage:
      Execute the heuristic on the wrapped nodes provided in init call 
    
    Parameters:
      #todo: Parameters
    
    Returns: 
      levelDictionary, with all the nodes assigned to a layer in that dictionary
    
    WARNING: 
      If you change the nodes, then you must re-instantiate this class
    
    Example usage:
        mwl = MinimumWidthLayering(wrappedNodeList)
        levelDictionary = mwl() # Run the algorithm
    """
    currentLayerInt = 0    
    print '-------------------- Layer ', currentLayerInt, ' --------------'
    while(self.__unassignedNodeList):
  
      theChosenNode = self.__chooseNode()
      
      if(theChosenNode):
        # Make the node aware of its layer
        theChosenNode.setLayer(currentLayerInt) 
        
        # Update current width and the estimate of upper layer widths
        outDegree = theChosenNode.getOutDegree()
        self.__currentWidthInt += \
          - MinimumWidthLayering.EdgeWidth * outDegree \
          + theChosenNode.getSize(giveExtraSpaceForLinks=False)[0]
          
        inDegree = len(theChosenNode.parents)
        self.__widthUpInt += MinimumWidthLayering.EdgeWidth * inDegree
                            
        
        # Prevent the layer from getting too wide...
        if(self.__conditionGoUp(outDegree, UBW, cInteger)):
          theChosenNode = None
  
      if(theChosenNode == None):
        currentLayerInt += 1        
        self.__assignedNodesInSubLayers += self.__assignedNodesCurrentLayer
        self.__currentWidthInt = self.__widthUpInt
        self.__widthUpInt = 0
        
        print '-------------------- Layer ', currentLayerInt, \
                ' --------------'
    
    
    # Build the level dictionary for easy access to node layers
    maxLayerInt = currentLayerInt
    levelDictionary = dict()
    for node in self.__wrappedNodeList:
      # Set them up by order of top nodes to bottom nodes
      currentLevelInt = node.getLayer()
      currentLevelInt = maxLayerInt - node.getLayer()
      node.setLayer(currentLevelInt)
      if(not levelDictionary.has_key(currentLevelInt)):
        levelDictionary[currentLevelInt] = [node]
      else:
        levelDictionary[currentLevelInt].append(node)
        
    #debugLevelDict(levelDictionary)
    return levelDictionary
     
   
      
   
  
  def __chooseNode(self):
    """ 
    Choose an unassigned node of maximum outdegree who has successors only in
    assigned layers (or no successors)
    """
    
    theChosenNode = None
    maxOutDegree = -1
    rejectedNodeList = []
    
    # Go through all unassigned nodes
    for node in self.__unassignedNodeList:
      
      # Slight optimization: ignore already rejected nodes on current layer
      if(node in rejectedNodeList):
        continue
        
#      print 'Node:', node, '  OutDegree:', node.getOutDegree()
      
      # Check if this node has a successor that is not already layer assigned
      isNodeInvalid = False
      for child in node.children.keys():
        if(child not in self.__assignedNodesInSubLayers):
          isNodeInvalid = True 
          break
      # Node has successor in unassigned layer, we can't possibly pick it
      if(isNodeInvalid):
        rejectedNodeList.append(node)
        continue
        
      # Does the node have maximum outdegree of all the candidates?
      if(node.getOutDegree() > maxOutDegree):
        maxOutDegree = node.getOutDegree()
        theChosenNode = node
      
      
    # Okay, we pick this node, shuffle it from unassigned to assigned!
    if(theChosenNode):
      self.__unassignedNodeList.remove(theChosenNode)
      self.__assignedNodesCurrentLayer.append(theChosenNode)      
      
    print '    The chosen node:', theChosenNode
    return theChosenNode # Could be None
     
     
  def __conditionGoUp(self, outDegree, UBW, cInteger):  
    """
    Return True if we should skip to the next layer
    """
    if(self.__currentWidthInt >= UBW and outDegree < 1):
      return True
    elif(self.__widthUpInt >= cInteger * UBW):
      return True
    return False
    

  