"""
TreeLikeLayout.py

Creates a simple tree layout, but works on general graphs too (less effective)

Running time is O(n)

Created Summer 2005, Denis Dube
"""

from tkMessageBox import showinfo

from TreeLikeOptionsKeys import MIN_HORIZONTAL_DISTANCE
from TreeLikeOptionsKeys import MIN_VERTICAL_DISTANCE
from TreeLikeOptionsKeys import MANUAL_CYCLE_BREAKING
from TreeLikeOptionsKeys import FORCE_TOPLEFT_TO_ORIGIN
from TreeLikeOptionsKeys import USE_SPLINES
from TreeLikeOptionsKeys import ARROW_CURVATURE
from TreeLikeOptionsKeys import PROMOTE_EDGE_TO_NODE
from TreeLikeOptionsKeys import TIP_OVER_STYLE



def doTreeLikeLayout(abstractGraph, optionsDict):
  """
  Do tree-like layout, works best on real trees, but can be applied to general
  directed graphs.
  """
  doManualCycles = optionsDict[MANUAL_CYCLE_BREAKING]
  doStartAtOrigin = optionsDict[FORCE_TOPLEFT_TO_ORIGIN] 
  
  if(optionsDict.has_key(TIP_OVER_STYLE)):
    doTipOverStyle = optionsDict[TIP_OVER_STYLE]
  else:
    doTipOverStyle = True
  
  # Promote directed edges to hyperedges, useful if the edge has a large drawing
  # then that drawing becomes a node, and two new directed edges are created.
  if(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Always'):
    abstractGraph.promoteDirectedEdge(True)
  elif(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Smart'):
    abstractGraph.promoteDirectedEdge(False)
  
  # We want to use getParentsList() on nodes, so must initilize this
  abstractGraph.initNodeChildrenParents()
  
  entityNodeList = abstractGraph.getAbstractNodeList()
  if(len(entityNodeList) == 0):
    return
    
  # Initilize the nodes with some extra attributes
  for node in entityNodeList:
    node._treeVisit = False
    node._treeChildren = []   

  # Get all root nodes (cycle in children possible), pure cycles will remain
  rootNodes = []
  for node in entityNodeList:
    if(node._treeVisit == False and len(node.getParentsList()) == 0):
      node._treeVisit = True
      rootNodes.append(node)
      __markChildrenNodesBFS(node, [])
  
  # Gather all the cycle nodes
  cycleNodes = []
  for node in entityNodeList:
    if(node._treeVisit == False):
      cycleNodes.append(node)
    
  # Node cycle breakers --> choice of nodes as root to break the cycle
  if(doManualCycles):
    rootNodes.extend(__getCycleRootsManually(cycleNodes))
  else:
    rootNodes = __getCycleRootsAuto(cycleNodes, rootNodes)
      
  #self.debugTree(rootNodes) # DFS printer
  
  # This does the actual moving around of nodes
  if(doStartAtOrigin):
    origin = (0, 0)
  else:
    origin = abstractGraph.getMaxUpperLeftCoordinate()
  
  if(doTipOverStyle):
    __layoutRootsTipOver(rootNodes, origin, optionsDict)
    __edginator(abstractGraph)
  else:
    __layoutRoots(rootNodes, origin, optionsDict)

  
  # Clean up
  for node in entityNodeList:
    del node._treeVisit 
    del node._treeChildren 
    
  # Fix up the arrows
  __optimizeArrows(abstractGraph, optionsDict)
  
  
    
def __optimizeArrows(abstractGraph, optionsDict):
  """
  Post-process to redraw arrows affected by moving nodes
  """
  # Post-process, redraw the arrows
  for arrow in abstractGraph.getAbstractEdgeList():
    arrow.setLinkOptimization(optionsDict[USE_SPLINES],
                              optionsDict[ARROW_CURVATURE])
  


def __getCycleRootsAuto(cycleNodes, rootNodes):
  """
  Breaks cycles by automatically choosing root nodes
  Nodes with the highest out degree are the preferred choice
  Returns root nodes including the ones that break the cycles
  """
  OutDegree2cycleNodeList = dict()
  # Associate each out degree with a list of nodes
  for node in cycleNodes:
    outDegree = len(node.getChildrenList())
    if(OutDegree2cycleNodeList.has_key(outDegree)):
      OutDegree2cycleNodeList[outDegree].append(node)
    else:
      OutDegree2cycleNodeList[outDegree] = [node]
  
  # Get the list of out degrees, and sort them from big to small
  degreeList = OutDegree2cycleNodeList.keys()
  degreeList.sort()
  degreeList.reverse()
  
  # Now go through each node in the order of big to small
  for outDegree in degreeList:
    for node in OutDegree2cycleNodeList[outDegree]:
      if(node._treeVisit == False):
        node._treeVisit = True
        rootNodes.append(node) 
        __markChildrenNodesBFS(node, [])
  return rootNodes
      
      

def __getCycleRootsManually(cycleNodes):
  """
  Allows the user to break cycles by clicking no nodes to choose tree roots
  Returns the final rootNodes (ie: including those that break cycles)
  """
  if(len(cycleNodes) > 0):
    showinfo('TreeLikeLayout: Cycle/s Detected', 
             'Manual cycle breaking mode in effect\n\n'
              + 'Cyclic nodes will be highlighted\n\n'
              + 'Please break the cycle/s by clicking on the node/s'
              + ' you want as tree root/s')
  rootNodes = []
  while(len(cycleNodes) > 0):
        
    index = cycleNodes[0].chooseNode(cycleNodes)
    if(index != None):
      chosenRootNode = cycleNodes[index]
      chosenRootNode._treeVisit = True
      rootNodes.append(chosenRootNode) 
      __markChildrenNodesBFS(chosenRootNode, [])
    # Cleanup: leave only nodes that still form a cycle
    temp = cycleNodes[:]
    for node in temp:
      if(node._treeVisit == True):
        cycleNodes.remove(node)
        
  return rootNodes
  
  
  
  

def debugTree(rootNodes):
  for node in rootNodes:
    print 'Root nodes found', node.getDistinctiveName() 
    debugTreeChildrenDFS(node)

def debugTreeChildrenDFS(node):
  for childNode in node._treeChildren:
    print 'Child node',  childNode.node.getDistinctiveName() 
    debugTreeChildrenDFS(childNode)
      
    
def __markChildrenNodesBFS(node, queuedNodeList):
  """ 
  Breadth first search algorithm
  Descends a tree, marking all children as visited
  In case of cycle, the child node is ignored
  """    
  for childNode in node.getChildrenList():
    # childNode may not be in the selection, in that case it will not have
    # the _treeVisit attribute
    if(childNode.__dict__.has_key('_treeVisit')
       and childNode._treeVisit == False): 
      node._treeChildren.append(childNode)
      childNode._treeVisit = True    
      queuedNodeList.append(childNode)
  if(len(queuedNodeList) == 1):
    __markChildrenNodesBFS(queuedNodeList[0], [])
  elif(len(queuedNodeList) > 1):
    __markChildrenNodesBFS(queuedNodeList[0], queuedNodeList[1:])
      
      
#def __markChildrenNodesDFS(node):
#  """ 
#  Depth first search algorithm
#  Descends a tree, marking all children as visited
#  In case of cycle, the child node is ignored
#  """  
#  for link in node.getChildrenList():
#    # childNode may not be in the selection, in that case it will not have
#    # the _treeVisit attribute
#    if(childNode.__dict__.has_key('_treeVisit')
#       and childNode._treeVisit == False): 
#      node._treeChildren.append(childNode)
#      childNode._treeVisit = True    
#      __markChildrenNodesDFS(childNode)

      
      
def __edginator(abstractGraph):
  """
  Add extra control points to make the tip over style look even nicer
  """
  edgeList = abstractGraph.getAbstractEdgeList()
  for edge in edgeList:
    source, target = edge.getSourceTargetNodeTuple()
    x0, y0 = source.getNewCoords()
    x1, y1 = target.getNewCoords()
    if(y0 != y1):
      w = x1 - x0     
      edge.setControlPoints([x0 + w * 0.5, y1,
                             x0 + w * 0.75, y1 + target.getSize()[1] / 2])

        

def __layoutRootsTipOver(rootNodes, originPointXY, optionsDict):
  """
  General graph may have more than a single root, so pretend the roots are
  all tied to some imaginary root high in the sky...
  """
  (xPos, yPos) = originPointXY
  xOffset = optionsDict[MIN_HORIZONTAL_DISTANCE]
  yOffset = optionsDict[MIN_VERTICAL_DISTANCE]
  
  # Find the max height of all the root level nodes
  maxHeight = 0
  for rootNode in rootNodes:
    maxHeight = max(maxHeight, rootNode.getSize()[1])
    
  
  for rootNode in rootNodes:
    rootNode.setNewCoords((xPos, yPos))
    w = rootNode.getSize()[0]
    
    treeHeight = 0
    for childNode in rootNode._treeChildren:
      
      treeHeight += __layoutNodeTipOver(childNode, xPos + w + xOffset, 
                                yPos + treeHeight, xOffset, yOffset) 
    yPos += treeHeight
  
     
     
def __layoutNodeTipOver(node, xPos, yPos, xOffset, yOffset):    
  """
  Do the layout for an ordinary node
  """
  
  # No children? Then this is very easy to position...
  if(len(node._treeChildren) == 0):
    node.setNewCoords((xPos, yPos))
    return node.getSize()[1] + yOffset
    
  # Has children, doh! Layout children first, then position parent    
  else:
    node.setNewCoords((xPos, yPos))
    
    treeHeight = 0
    w, h = node.getSize()
    for childNode in node._treeChildren:
      treeHeight += __layoutNodeTipOver(childNode, xPos + w + xOffset, 
                                yPos + treeHeight, 
                                xOffset, yOffset)          
    return treeHeight

   
      
      
      
def __layoutRoots(rootNodes, originPointXY, optionsDict):
  """
  General graph may have more than a single root, so pretend the roots are
  all tied to some imaginary root high in the sky...
  """
  (xPos, yPos) = originPointXY
  xOffset = optionsDict[MIN_HORIZONTAL_DISTANCE]
  yOffset = optionsDict[MIN_VERTICAL_DISTANCE]
  
  # Find the max height of all the root level nodes
  maxHeight = 0
  for rootNode in rootNodes:
    maxHeight = max(maxHeight, rootNode.getSize()[1])
    
  
  for rootNode in rootNodes:
    treeWidth = 0
    # Layout the children of the root, then we'll know exactly where the
    # root itself goes...
    for childNode in rootNode._treeChildren:
      treeWidth += __layoutNode(childNode, xPos + treeWidth, 
                                yPos + yOffset + maxHeight,
                                  xOffset, yOffset)      
        
    rootNode.setNewCoords(
            (xPos + (treeWidth - rootNode.getSize()[0] - xOffset) / 2, yPos))
    xPos += treeWidth
      
      
      
def __layoutNode(node, xPos, yPos, xOffset, yOffset):    
  """
  Do the layout for an ordinary node
  """
  
  # No children? Then this is very easy to position...
  if(len(node._treeChildren) == 0):
    node.setNewCoords((xPos + xOffset / 2, yPos))
    return node.getSize()[0] + xOffset
    
  # Has children, doh! Layout children first, then position parent    
  else:
    treeWidth = 0
    w, h = node.getSize()
    for childNode in node._treeChildren:
      treeWidth += __layoutNode(childNode, xPos + treeWidth, 
                                yPos + h + yOffset, 
                                xOffset, yOffset)
 
     # Special case: the subtree can actually be smaller than this vertex's w
    if(treeWidth - xOffset < w):
      node.setNewCoords((xPos, yPos))
      return w
    else:
      node.setNewCoords((xPos + (treeWidth - w - xOffset) / 2, yPos))
    return treeWidth    
  