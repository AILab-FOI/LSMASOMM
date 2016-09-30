"""
MinimumWidthLayering.py

By Denis Dube, Sept. 2005
"""

  
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
      UBW should range between 1 to 4 (according to alg. publishers)
      cInteger should range between 1 to 2 (according to alg. publishers)
    
    Returns: 
      levelDictionary, with all the nodes assigned to a layer in that dictionary
    
    WARNING: 
      If you change the nodes, then you must re-instantiate this class
    
    Example usage:
        mwl = MinimumWidthLayering(wrappedNodeList)
        levelDictionary = mwl(2, 2) # Run the algorithm
    """
    currentLayerInt = 0    
    
    # Pre-process, put unconnected elements in the zero-layer
    # NOTE: This is not mentioned in the MWL paper, but helps the layout
    unconnectedElements = False
    for wrappedNode in self.__wrappedNodeList:
      if(len(wrappedNode.parents.keys()) == 0 and 
                                        len(wrappedNode.children.keys()) == 0):
        self.__assignedNodesInSubLayers.append(wrappedNode)
        self.__unassignedNodeList.remove(wrappedNode)
        wrappedNode.setLayer(currentLayerInt)
        unconnectedElements = True
    if(unconnectedElements):
      currentLayerInt += 1
    
#    print '-------------------- Layer ', currentLayerInt, ' --------------'
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
        
#        print '-------------------- Layer ', currentLayerInt, \
#                ' --------------'
    
    
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
      
#    print '    The chosen node:', theChosenNode
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
    

