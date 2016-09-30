"""
NodeWrapper.py

By Denis Dube
"""

import sys


def initilizeNodeWrapper():
  """ 
  Utility method to reset the class attributes of NodeWrapper 
  """
  NodeWrapper.SelfLoopList = []
  NodeWrapper.Node2WrapperDict = dict()    
  NodeWrapper.ID2LayerEdgeDict = dict() 
  NodeWrapper.Source2TargetListMap = dict() 


class NodeWrapper:
  """
  The Hierarchical layout algorithm works exclusively on objects instantiated
  from this class. For the most part, this is a wrapper around the real entity
  nodes in the original diagram. However, special edges are also treated as
  nodes to improve the final layout.
  """
  
  # These need to be reset for each new run of HierarchicalLayout
  SelfLoopList = []  
  Node2WrapperDict = dict() # Map of ASGNode to NodeWrapper
  ID2LayerEdgeDict = dict() # Map of uniqueID's to NodeWrapper
  Source2TargetListMap = dict() # Map of source NodeWrappers with a directed 
                                # edge to target NodeWrapper
  
  REGULAR_NODE = 0
  MULTI_LAYER_EDGE = 1
  SELF_LOOP_EDGE = 2

  def __init__(self, node, nodeType, layer = 0):  
    self.__visitedFlag = False # Used for DFS 
    self.__layer = layer       # Layer node belongs to
    self.__order = -1          # Node order on the layer
    self.__gridPosition = -1   # Actual node pos on grid (cannot violate order)
    self.__priority = 0        # Priority to push other nodes for new grid pos
    self.__barycenterValue = 0 # Barycenter used for crossing minimization
        
    # Dict format: self.children[childNode] = [[linkNode, isReversed],...]
    self.children = dict() 
    self.parents = dict() 
    
    self.__edgePosition = [0, 0]  # Edge control point position (Dummy edges)
    self.__nodeType = nodeType    # Regular node or some type of edge node?
    self.__node = node            # AbstractGraph Node
    
    NodeWrapper.Source2TargetListMap[self] = []
        
    # Regular node tracker
    if(nodeType == NodeWrapper.REGULAR_NODE):
      NodeWrapper.Node2WrapperDict[node] = self
      
    # Self loop tracker (Special kind of dummy edge)
    elif(nodeType == NodeWrapper.SELF_LOOP_EDGE):
      NodeWrapper.SelfLoopList.append(self) 
    
    # Multi-layer edge node tracker (Dummy edge)
    else:
      self.__node = []        # self.__node = [linkNode,...]
      linkFlagList = node[1]
      for i in range(0, len(linkFlagList)):
        self.__node.append(linkFlagList[i][0]) # The link node object/s
      node = node[0]        # A unique ID number for the dummy tracker
      
      # Add/append self to the tracker with key "node" which is an ID here
      if(NodeWrapper.ID2LayerEdgeDict.has_key(node)):
        NodeWrapper.ID2LayerEdgeDict[node].append(self)
      else:
        NodeWrapper.ID2LayerEdgeDict[node] = [self]
        
    
    
  def isStraightPart(self):
    if(self.__nodeType == self.MULTI_LAYER_EDGE):
      # Only one child/parent for a dummy edge
      child = self.children.keys()[0]
      parent = self.parents.keys()[0]
      if(child.getType() == self.MULTI_LAYER_EDGE and
         parent.getType() == self.MULTI_LAYER_EDGE):
         return True
    return False
      
  def getType(self):
    return self.__nodeType

  
  def getOutDegree(self):
    """ Number of children """
    return len(self.children)
  
     
  def setVisited(self):
    """ Depth first search has visited here """
    self.__visitedFlag = True
                  
  def isVisited(self):
    """ Return the visited flag """
    return self.__visitedFlag
            
    
  def __str__(self):
    """ Return a string representing this wrapped node """
    if(self.__nodeType == NodeWrapper.MULTI_LAYER_EDGE):
      abstractEdge = self.__node[0]
      return abstractEdge.getDistinctiveName()      
    elif(self.__node):
      return self.__node.getDistinctiveName()
    else:
      return 'NO-NAME'
    
  def moveTo(self, newPos, longEdgeOffset=None):
    """ Does not actually move nodes, but sets new coords """
    if(self.__nodeType == NodeWrapper.REGULAR_NODE):
      self.__node.setNewCoords(newPos)
      
    # Dummy node with multiple edge control points...
    else:
      self.__edgePosition = [newPos[0] + longEdgeOffset[0], 
                             newPos[1] + longEdgeOffset[1]]
      
  def getEdgePosition(self):
    return self.__edgePosition 
        
  def setLayer(self, layer):
    self.__layer = layer
  def getLayer(self):
    return self.__layer
    
  def setOrder(self, order):
    self.__order = order
  def getOrder(self):
    return self.__order
    
  def computeBarycenter(self, isGoingDown):
    """
    Implements the barycenter heuristic. Basic idea: if a node in layer A is
    connected to node1, node2, and node3 in layer B, then the node in layer
    A should be placed at the average of the positions (order integers) of the
    three nodes in layer B. This must be done from layer A to layer B and then
    from layer B to layer A many times to converge on a global solution. 
    The isGoingDown parameter determines if we are moving from root layer to
    leaf layer (True), or from leaf layer to root layer (False)
    
    Implementation according to:
      http://etd.lib.fsu.edu/theses/available/etd-05062004-232310/
      unrestricted/Pitch_Patarasuk_Thesis.pdf
      CROSSING REDUCTION FOR LAYERED HIERARCHICAL GRAPH DRAWING
      By PITCH PATARASUK
    """
    if(isGoingDown):
      nodeList = self.children.keys()
    else:
      nodeList = self.parents.keys()
      
    # Filter out nodes that are not in the expected next layer
    # NOTE: filter is a built-in that applies a function to each list element
    #nodeList = filter(lambda node: abs(node.getLayer() - self.__layer) == 1, 
    #                  nodeList)
    nodeList = [node for node in nodeList
                  if abs(node.getLayer() - self.__layer) == 1]
    numberOfNodes = len(nodeList)
    
    # No nodes in next layer? Just use the arbitrary original order value
    if(numberOfNodes == 0):
      self.__barycenterValue = self.__order
      return 

#    if(numberOfNodes % 2 == 1):
#      # Calculate the mediancenter for nodes of odd degree
#      self.__barycenterValue = nodeList[numberOfNodes / 2].__order
#    else:
    # Calculate the barycenter
    orderSum = 0
    for node in nodeList:
      orderSum += node.__order
    self.__barycenterValue = orderSum / float(numberOfNodes)
    
    
    
    
  def getBarycenter(self):
    """ Retrieve the barycenter computed by computeBarycenter() """
    return self.__barycenterValue
    
    

  def calculatePriority(self):
    """ Priority = Fan in + Fan out, and max level priority for dummies """
    if(self.__nodeType == NodeWrapper.MULTI_LAYER_EDGE
       or self.__nodeType == NodeWrapper.SELF_LOOP_EDGE):
      self.__priority = sys.maxint
    else:
      self.__priority = len(self.children) + len(self.parents)
    return self.__priority



  def setPriority(self, priority):
    self.__priority = priority
    
  def getPriority(self):
    return self.__priority 
    
    
    
  def getAbstractNode(self):
    return self.__node
    
    
    
  def setGridPosition(self, pos):
    self.__gridPosition = pos
    
    
    
    
  def getGridPosition(self):  
    return self.__gridPosition
    
    
    
  def getGridBarycenter(self, isGoingDown):
    """
    Use:
      Calculates and returns a barycenter grid position for the final horizontal
      coordinate assignment phase of the hierarchical layout algorithm.
    """    
    if(isGoingDown):
      nodeList = self.children.keys()
    else:
      nodeList = self.parents.keys()
      
    # Filter out nodes that are not in the expected next layer
    # NOTE: filter is a built-in that applies a function to each list element
    nodeList = filter(lambda node: abs(node.getLayer() - self.__layer) == 1, 
                      nodeList)
      
    numberOfNodes = len(nodeList)
    if(numberOfNodes == 0):
      return self.__gridPosition

    orderSum = 0
    for node in nodeList:
      orderSum += node.__gridPosition
    return orderSum / float(numberOfNodes)



  def getSize(self, giveExtraSpaceForLinks=True):
    """
    Returns: size of node
    
    If node is a multi-layer edge: size is the greatest of all (dummy) 
      vertices making up the edge. Should probably just return [0, 0] though
      since dummy vertices are all [0, 0] and the center drawing of the edge
      is now treated as a real vertex by the abstraction layer.
      
    If the node is a self-loop edge, then returns size of the loop edge unless
      this is smaller than the minimum. Probably always [0, 0], so the minimum
      [100, 100] is used. Gives enough space to fit in the loop somewhere. 
      
    The last possibility is giveExtraSpaceForLinks, which is obsoleted by the
      abstraction layer.
    """
    minLoopEdgeSize = [100, 100]
    
    # Long edge traversing multiple layers
    if(self.__nodeType == NodeWrapper.MULTI_LAYER_EDGE):
      maxSize = [0, 0]
      for node in self.__node:
        w, h = node.getSize()
        maxSize = [max(maxSize[0], w), 
                   max(maxSize[1], h)]
      return maxSize
      
    # Self looping edge
    elif(self.__nodeType == NodeWrapper.SELF_LOOP_EDGE):
      w, h = self.__node.getSize()
      if(w < minLoopEdgeSize[0]):
        w = minLoopEdgeSize[0]
      if(h < minLoopEdgeSize[1]):
        h = minLoopEdgeSize[1]
      return [w, h]
      
      
    # Check if single layer links have drawings that require additional space
    elif(giveExtraSpaceForLinks):
      maxSingleLayerLinkHeight = 0
      
      def getMaxLinkHeight(linkFlagList, maxSingleLayerLinkHeight):
        for linkFlag in linkFlagList:
          abstractEdge = linkFlag[0]
          maxSingleLayerLinkHeight = max(maxSingleLayerLinkHeight, 
                                         abstractEdge.getSize()[1])
        return maxSingleLayerLinkHeight
        
    
      # Children
      for wrappedChildNode in self.children.keys():
        if(wrappedChildNode.__layer == self.__layer + 1):
          maxSingleLayerLinkHeight = getMaxLinkHeight(
                                            self.children[wrappedChildNode], 
                                            maxSingleLayerLinkHeight)
                    
      # Parents (for links going in reverse direction)
      for wrappedParentNode in self.parents.keys():
        if(wrappedParentNode.__layer == self.__layer - 1):
          maxSingleLayerLinkHeight = getMaxLinkHeight(
                                            self.parents[wrappedParentNode], 
                                            maxSingleLayerLinkHeight)
     
      size = self.__node.getSize()
      return [size[0], size[1] + maxSingleLayerLinkHeight]
    return self.__node.getSize()
     
     
  def addDummyToList(self, dummyNodeList):
    if(self.__nodeType == self.MULTI_LAYER_EDGE):
      dummyNodeList.append(self)
      
