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
    
    self.__outDegree = 0
    
    self.__edgePosition = [0, 0]  # Edge control point position (Dummy edges)
    self.__nodeType = nodeType    # Regular node or some type of edge node?
    self.__node = node            # AToM3 node, subclass of ASGnode
    
    NodeWrapper.Source2TargetListMap[self] = []
        
    # Regular node tracker
    if(nodeType == NodeWrapper.REGULAR_NODE):
      # node is an AToM3 entity, subclass of ASGNode
      NodeWrapper.Node2WrapperDict[node] = self
      
    # Self loop tracker (Special kind of dummy edge)
    elif(nodeType == NodeWrapper.SELF_LOOP_EDGE):
      NodeWrapper.SelfLoopList.append(self) 
#      NodeWrapper.Source2TargetListMap[self] = [self]
    
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
    

  
  def buildConnectivityMaps(self, linkNodeDict):  
    """
    Creates dictionaries that provide rapid access to the wrapped children
    and parent nodes that are connected with this node.
    Also provides access to the actual link entity between the nodes
    A flag is provided to indicate if the algorithm needed to reverse the link
    Self-links are discarded (Hiearchical layout don't care none about those)
    """
    # Children map
    for linkNode in self.__node.out_connections_:
      # Make sure the link is in the selection
      if(not linkNodeDict.has_key(linkNode)):
        continue
        
      for childNode in linkNode.out_connections_:
        wrappedChildNode = NodeWrapper.Node2WrapperDict[childNode]
        NodeWrapper.Source2TargetListMap[self].append(wrappedChildNode)
        
        # Is the child ourselves in an evil self-loop situation?
        # If so, then create a "dummy" node for the loop itself
        if(self == wrappedChildNode):
          newNode = NodeWrapper(linkNode, NodeWrapper.SELF_LOOP_EDGE) 
          self.children[newNode] = [[linkNode, False]]
          self.parents[newNode] = [[linkNode, False]]
          newNode.children[self] = [[linkNode, False]]
          newNode.parents[self] = [[linkNode, False]]
          continue
          
        # Could be more than one link between source and target
        if(self.children.has_key(wrappedChildNode)):
          self.children[wrappedChildNode].append([linkNode, False])
        else:
          self.children[wrappedChildNode] = [[linkNode, False]]
          
    # Out degree
    self.__outDegree = len(self.children)
          
    # Parent map
    for linkNode in self.__node.in_connections_:
      # Make sure the link is in the selection
      if(not linkNodeDict.has_key(linkNode)):
        continue
        
      for parentNode in linkNode.in_connections_:
        wrappedParentNode = NodeWrapper.Node2WrapperDict[parentNode]
        
        # Is the parent ourselves in an evil self-loop situation?
        # If so skip this, we handled this case already in the child map
        if(self == wrappedParentNode):
          continue
        
        # Could be more than one link between source and target
        if(self.parents.has_key(wrappedParentNode)):
          self.parents[wrappedParentNode].append([linkNode, False])
        else:
          self.parents[wrappedParentNode] = [[linkNode, False]]
  
  
  def getOutDegree(self):
    """ Number of children """
    return self.__outDegree
  
     
  def setVisited(self):
    """ Depth first search has visited here """
    self.__visitedFlag = True
                  
  def isVisited(self):
    """ Return the visited flag """
    return self.__visitedFlag
            
#  def getChildrenWrappers(self):
#    children = []
#    for link in self.__node.out_connections_:
#      for childNode in link.out_connections_:
#        children.append(NodeWrapper.Node2WrapperDict[childNode])
#    return children
    
  def __str__(self):
    return self.getName()
    
  def getName(self):
    # DEBUG -- will fail horribly in general formalisms
    if(self.__nodeType == NodeWrapper.MULTI_LAYER_EDGE):
      linkNode = self.__node[0]
      inConn = linkNode.in_connections_[0]
      outConn = linkNode.out_connections_[0]
      inWrappedNode = NodeWrapper.Node2WrapperDict[inConn]
      outWrappedNode = NodeWrapper.Node2WrapperDict[outConn] 
      return 'E_' + inWrappedNode.getName() \
              + '_to_' + outWrappedNode.getName()
    if(self.__node and self.__node.__dict__.has_key('name')):
      return self.__node.name.toString()
    else:
      return 'NO-NAME'
    
  def moveTo(self, x, y, longEdgeOffset):
    if(self.__nodeType == NodeWrapper.REGULAR_NODE):
      self.__node.graphObject_.moveTo(x, y)
    elif(self.__nodeType == NodeWrapper.SELF_LOOP_EDGE):
      #self.__node.graphObject_.moveTo(x, y)
      #print 'Moving loop to', self.getName(), x, y
      centerObj = self.__node.graphObject_.getCenterObject()
      if(centerObj):
        offset = centerObj.getSize()
        self.__edgePosition = [x + offset[0] / 2, y]
        return 
      self.__edgePosition = [x, y]
    else:
      self.__edgePosition = [x + longEdgeOffset[0], y + longEdgeOffset[1]]
      
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
      
    numberOfNodes = len(nodeList)
    
    # No nodes in next layer? Just use the arbitrary original order value
    if(numberOfNodes == 0):
      self.__barycenterValue = self.__order
      return 

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
      return self.__priority
    else:
      self.__priority = len(self.children) + len(self.parents)
      return self.__priority

  def setPriority(self, priority):
    self.__priority = priority
  def getPriority(self):
    return self.__priority
    
  def getASGNode(self):
    return self.__node
    
  def setGridPosition(self, pos):
    self.__gridPosition = pos
  def getGridPosition(self):  
    return self.__gridPosition
    
  def getGridBarycenter(self, isGoingDown):
    if(isGoingDown):
      nodeList = self.children.keys()
    else:
      nodeList = self.parents.keys()
    numberOfNodes = len(nodeList)
    
    if(numberOfNodes == 0):
      return self.__gridPosition

    orderSum = 0
    for node in nodeList:
      orderSum += node.__gridPosition
    return orderSum / float(numberOfNodes)

  def getSize(self, giveExtraSpaceForLinks=True):
    # Long edge traversing multiple layers
    if(self.__nodeType == NodeWrapper.MULTI_LAYER_EDGE):
      maxSize = [0, 0]
      for node in self.__node:
        centerObj = node.graphObject_.getCenterObject()
        if(centerObj):
          tempSize = centerObj.getSize()
          maxSize = [max(maxSize[0], tempSize[0]), 
                     max(maxSize[1], tempSize[1])]
        return maxSize
      return [0, 0]
      
    # Self looping edge
    elif(self.__nodeType == NodeWrapper.SELF_LOOP_EDGE):
      centerObj = self.__node.graphObject_.getCenterObject()
      if(centerObj):
        return centerObj.getSize()
      return [100, 100]
      
    # Check if single layer links have drawings that require additional space
    elif(giveExtraSpaceForLinks):
      maxSingleLayerLinkHeight = 0
      
      def getMaxLinkHeight(linkFlagList, maxSingleLayerLinkHeight):
        for linkFlag in linkFlagList:
          centerObj = linkFlag[0].graphObject_.getCenterObject()
          if(centerObj):
            maxSingleLayerLinkHeight = max(maxSingleLayerLinkHeight, 
                                           centerObj.getSize()[1])
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
     
      size = self.__node.graphObject_.getSize()
      return [size[0], size[1] + maxSingleLayerLinkHeight]
    return self.__node.graphObject_.getSize()
      