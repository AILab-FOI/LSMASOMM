"""
CircleLayout.py

Arranges selected entities in a simple circle, possibly setting the stage for
spring layout.

Running time is O(n)

Created Summer 2005, Denis Dube
"""

import math

from CircleOptionsKeys import FORCE_TOPLEFT_TO_ORIGIN
from CircleOptionsKeys import MIN_NODE_SPACING
from CircleOptionsKeys import USE_SPLINES
from CircleOptionsKeys import ARROW_CURVATURE
from CircleOptionsKeys import PROMOTE_EDGE_TO_NODE
    
    
    
def doCircleLayout(abstractGraph, optionsDict):
  """
  Position the nodes in a simple circle configuration
  """
  
  #__getStronglyConnectedComponents(abstractGraph)
  #return 
  
  # Promote directed edges to hyperedges, useful if the edge has a large drawing
  # then that drawing becomes a node, and two new directed edges are created.
  if(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Always'):
    abstractGraph.promoteDirectedEdge(True)
  elif(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Smart'):
    abstractGraph.promoteDirectedEdge(False)
    
  nodeList = __getTopologicalSort(abstractGraph)
  nodeListLength = len(nodeList)
  
  useOrigin = optionsDict[FORCE_TOPLEFT_TO_ORIGIN]
  offset = optionsDict[MIN_NODE_SPACING]  
  
  if(useOrigin):
    baseX = 0
    baseY = 0
  else:
    (baseX, baseY) = abstractGraph.getMaxUpperLeftCoordinate()
  
  # If we lay down each node side by side, how long would that be?
  perimeter = __computeCirclePerimeter(nodeList, offset)  
  # Convert the perimeter into a circle diameter
  diameter = perimeter / math.pi 
    
  # Initilize the base coordinates so the top-left of the circle is at either
  # the origin or the top-left of the original drawing. This position will be 
  # the bottom-right of the drawn circle.
  baseX += diameter 
  baseY += diameter 

  # This is a float that ranges from a bit over 0.0 to a bit over 1.0
  currentSumFloat = float(nodeList[-1]._boundingCircleDiameter) 
  currentSumFloat /= (2.0 * perimeter)
  for i in range(0, nodeListLength):
    currentNode = nodeList[i]
            
    # Convert the 0..1 float into a radian angle, and figure out actual x, y
    angleRadianFloat = currentSumFloat * 2.0 * math.pi    
    x = baseX - diameter * math.sin(angleRadianFloat)
    y = baseY - diameter * math.cos(angleRadianFloat)
    nodeList[i].setNewCoords((x, y))
    
    # Take the average of the contributions of this node and the next node
    # to the perimeter of the circle, and add it to the currentSumFloat
    current = float(currentNode._boundingCircleDiameter) 
    # NOTE: Modulo is used to wrap around to 0 when we reach circle end
    next = float(nodeList[(i+1) % nodeListLength]._boundingCircleDiameter)     
    currentSumFloat += (current + next) / (2.0 * perimeter )
    
    
  # Post Processing: Fix up the arrows
  __optimizeArrows(abstractGraph, optionsDict)
    


def __computeCirclePerimeter(nodeList, offset):
  """
  Takes a list of entity nodes, computes the perimeter they will occupy and
  resulting radius of circle required
  """  
  # Compute the circles perimeter
  # Line up all the nodes diagonally (or max of H and W), count length
  # Use eqution: perimeter = 2*pi*r to get radius
     
  perimeter = 0.0
  for node in nodeList:
    sx, sy = node.getSize()
    boundingCircleDiameter = math.sqrt(sx * sx + sy * sy)
    node._boundingCircleDiameter = boundingCircleDiameter + offset
    perimeter += node._boundingCircleDiameter
  return perimeter 


  

def __getTopologicalSort(abstractGraph):
  """
  Returns the node list as topologically sorted with forward arcs running 
  from left to right (if cycles exist, there will be backward arcs too)
  """
  def DFSlookup(node, sortedNodeList):
    """ Sub-method for topological sort, does depth first search """
    for childNode in node.getChildrenList(): 
      if(not childNode._tempIsVisited):
        childNode._tempIsVisited = True
        DFSlookup(childNode, sortedNodeList)
    sortedNodeList.append(node)
  
  
  # Gather all the nodes in the graph and add a "isVisited" attribute
#  nodeList = abstractGraph.getNodeList()
  nodeList = abstractGraph.getAbstractNodeList()
  abstractGraph.initNodeChildrenParents() # Make sure getChildrenList works
  for node in nodeList:
    node._tempIsVisited = False
  
  # Build up the topoligically sorted list
  sortedNodeList = []
  for node in nodeList:
    if(not node._tempIsVisited):    
      node._tempIsVisited = True    
      DFSlookup(node, sortedNodeList)
      
  # Remove the visit attribute
  for node in nodeList:
    del node._tempIsVisited
      
  sortedNodeList.reverse()
  return sortedNodeList
  
    
    
def __optimizeArrows(abstractGraph, optionsDict):
  """
  Post-process to redraw arrows affected by moving nodes
  """
  # Post-process, redraw the arrows
  arrowList = abstractGraph.getAbstractEdgeList() 
#  arrowList = abstractGraph.getDirectedEdgeList() \
#              + abstractGraph.getHyperEdgeList()
  for arrow in arrowList:
    arrow.setLinkOptimization(optionsDict[USE_SPLINES],
                               optionsDict[ARROW_CURVATURE])
      
      
    
      
'''
def __getDegreeSort(abstractGraph):
  """
  Returns the node list as sorted by degrees
  Layout is nowhere near as nice as with topological sort
  """
  nodeList = abstractGraph.getAbstractNodeList()
  abstractGraph.initNodeChildrenParents() # Make sure getChildrenList works
  
  degree2NodeDict = dict()
  for node in nodeList:
    degree = len(node.getChildrenList()) + len(node.getParentsList())
    if(degree2NodeDict.has_key(degree)):
      degree2NodeDict[degree].append(node)
    else:
      degree2NodeDict[degree] = [node]
  
  degreeKeys = degree2NodeDict.keys()
  degreeKeys.sort()
  
  sortedNodeList = []
  for degreeKey in degreeKeys:
    for node in degree2NodeDict[degreeKey]:
      sortedNodeList.append(node)
  return sortedNodeList
'''
      
'''
def __getStronglyConnectedComponents(abstractGraph):
  """
  Use:
    Finds all the strongly connected components in the abstract graph
    Two vertices of directed graph are in the same component if and only if 
    they are reachable from each other.
  """
  
  
  def DFSlookup(node, finishOrder):
    """ Depth first search with finishing time attribution """
    for childNode in node.getChildrenList(): 
      if(not childNode._tempIsVisited):
        childNode._tempIsVisited = True
        finishOrder = max(finishOrder, DFSlookup(childNode, finishOrder))
    node._finishOrder = finishOrder + 1
    return node._finishOrder
        
  # Initilize
  nodeList = abstractGraph.getNodeList()
  for node in nodeList:
    node._tempIsVisited = False
    
  # Do DFS lookup to get the finishing times of each node
  for node in nodeList:
    if(not node._tempIsVisited):    
      node._tempIsVisited = True    
      DFSlookup(node, 0)
      
  # Sort according to decreasing finishing order
  nodeList.sort(lambda a, b: -cmp(a._finishOrder, b._finishOrder))
  for node in nodeList:
    print node.getDistinctiveName(), node._finishOrder
            
  def reverseDFS(node, strongComponent):
    for parentNode in node.getParentsList(): 
      if(not parentNode._tempIsVisited):
        parentNode._tempIsVisited = True
        reverseDFS(parentNode, strongComponent)
    strongComponent.append(node)
            
  # Re-initilize visit flag    
  for node in nodeList:
    node._tempIsVisited = False
    
  stronglyConnectedComponentList = []
  for node in nodeList:
    if(not node._tempIsVisited):   
      strongComponent = []
      node._tempIsVisited = True 
      reverseDFS(node, strongComponent)
      stronglyConnectedComponentList.append(strongComponent)
  
  for scc in stronglyConnectedComponentList:
    print '\nComponent:'
    for node in scc:
      print node.getDistinctiveName()
    
  # Remove the visit attribute
  for node in nodeList:
    del node._tempIsVisited
    del node._finishOrder
'''    