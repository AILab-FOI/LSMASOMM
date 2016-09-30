"""
HierarchicalLayout.py

This algorithm examines the semantics of the graph structure to come up with an
aesthetic layout for most graph types. 
It starts by finding roots to the graph and removing cycles by reversing back
arcs. Then it assigns each node in the graph to a layer, creating a proper
layered hiearchy. Between each layer, it performs crossing minimization on the
edges. Finally, it tries to align nodes with children/parents in other
layers before finally drawing everything. 

This implementation can deal with edges traversing multiple layers, self-loops,
and to some degree, with hyperedges (edges that have multiple children/parents).

Based on the Sugiyama layout algorithm
   
Created Summer 2005, Denis Dube
"""
__revision__ = 0.1
__author__ = 'Denis Dube'
__date__ = 'Summer 2005'

import sys
import time
#import random
#import math
#from tkMessageBox import showinfo

from NodeWrapper import NodeWrapper, initilizeNodeWrapper

from LayeringModule.MinimumWidthLayering import MinimumWidthLayering
from LayeringModule.BFSLayering import BFSLayering
from LayeringModule.LongestPathLayering import LongestPathLayering
from LayeringModule.GreedyCycleRemoval import GreedyCycleRemoval
from LayeringModule.MakeLayeringProper import MakeLayeringProper

from CrossingModule.BarycenterHeuristic import BarycenterHeuristic
from CrossingModule.AdjacentExchange import AdjacentExchange

from PositioningModule.PriorityBarycenter import PriorityBarycenter

from Debug import debugLevelDict, debugCrossing

from HierarchicalOptionsKeys import LAYERING_ALGORITHM
from HierarchicalOptionsKeys import MIN_HORIZONTAL_DISTANCE
from HierarchicalOptionsKeys import MIN_VERTICAL_DISTANCE
from HierarchicalOptionsKeys import MAX_NO_PROGRESS_ROUNDS   
from HierarchicalOptionsKeys import MAX_TOTAL_ROUNDS         
from HierarchicalOptionsKeys import CROSS_ALG_CHOICE     
from HierarchicalOptionsKeys import USE_RANDOM_RESTARTS     
from HierarchicalOptionsKeys import MAX_BARYCENTER_ITER
from HierarchicalOptionsKeys import FORCE_TOPLEFT_TO_ORIGIN
from HierarchicalOptionsKeys import USE_SPLINES
from HierarchicalOptionsKeys import ARROW_CURVATURE
from HierarchicalOptionsKeys import PROMOTE_EDGE_TO_NODE
from HierarchicalOptionsKeys import LAYOUT_DIRECTION


def doHierarchicalLayout(abstractGraph, optionsDict):
    """
    Does all the high-level steps, delegates details to other methods.
    """
    t = time.time()
    
    # Promote directed edges to hyperedges, useful if the edge has a large 
    # drawing then that drawing becomes a node, and two new directed edges are 
    # created.
    if(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Always'):
      abstractGraph.promoteDirectedEdge(True)
    elif(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Smart'):
      abstractGraph.promoteDirectedEdge(False)
      
    # Initilize the node wrapper class attributes
    initilizeNodeWrapper()
          
    # Create a wrapping around each abstract node, but keep a mapping...
    abstractNode2WrappedNodeMap = dict()   
    wrappedNodeList = [] 
    for node in abstractGraph.getAbstractNodeList():
      wrappedNode = NodeWrapper(node, NodeWrapper.REGULAR_NODE)
      
      wrappedNodeList.append(wrappedNode)
      abstractNode2WrappedNodeMap[node] = wrappedNode
        
    __buildConnectionMap(abstractGraph, abstractNode2WrappedNodeMap)    


#===============================================================================
#    Phase 1: Build a proper layered hieararchy
#===============================================================================
    wrappedNodeList = GreedyCycleRemoval(wrappedNodeList)
    layerTime = time.time()
    if(optionsDict[LAYERING_ALGORITHM] == 'BFS'):
      levelDictionary = BFSLayering(wrappedNodeList)
      levelDictionary = MakeLayeringProper(levelDictionary)
    elif(optionsDict[LAYERING_ALGORITHM] == 'Longest-path'):
      levelDictionary = LongestPathLayering(wrappedNodeList)
      levelDictionary = MakeLayeringProper(levelDictionary)
    elif(optionsDict[LAYERING_ALGORITHM] == 'Minimum-width'):
      mwl = MinimumWidthLayering(wrappedNodeList)
      # UBW = 1..4, c = 1..2
      levelDictionary = mwl(2, 2)
      levelDictionary = MakeLayeringProper(levelDictionary)
    else:
      raise Exception('No valid layering algorithm selected')
    print '\n**   Layering algorithm required', time.time() - layerTime, \
          'seconds to assign each node a layer   **\n'

#    print '\n    Added dummy nodes, dumping layers:'
#    debugLevelDict(levelDictionary)
    

#===============================================================================
#    Phase 2: Crossing minimization  
#===============================================================================
    currentAlg = ('Barycenter', 'Both')
    if(optionsDict[CROSS_ALG_CHOICE] in currentAlg):
      crossTime = time.time()
      levelDictionary = BarycenterHeuristic(levelDictionary,
                                 optionsDict[MAX_NO_PROGRESS_ROUNDS], 
                                 optionsDict[MAX_TOTAL_ROUNDS],
                                 optionsDict[USE_RANDOM_RESTARTS] in currentAlg)
      print '**   Barycenter crossing reduction algorithm required',  \
            time.time() - crossTime, 'seconds   **\n'
    
    currentAlg = ('Transpose', 'Both')
    if(optionsDict[CROSS_ALG_CHOICE] in currentAlg):
      crossTime = time.time()
      levelDictionary = AdjacentExchange(levelDictionary,  
                                optionsDict[MAX_NO_PROGRESS_ROUNDS], 
                                optionsDict[MAX_TOTAL_ROUNDS],
                                optionsDict[USE_RANDOM_RESTARTS] in currentAlg)
      print '**   Transpose crossing reduction algorithm required',  \
            time.time() - crossTime, 'seconds   **\n'

#===============================================================================
#    Phase 3: Horizontal grid positioner
#===============================================================================
    positioningTime = time.time()
    PriorityBarycenter(levelDictionary, 
                                 optionsDict[MAX_BARYCENTER_ITER])
    print '\n**   Final positioning algorithm required',  \
          time.time() - positioningTime, 'seconds   **\n'
    
    
    # Draw nodes and edges on the canvas
    if(optionsDict[LAYOUT_DIRECTION] in ['North', 'South']):
      __drawNodesNS(levelDictionary, abstractGraph, optionsDict)
    else:
      __drawNodesEW(levelDictionary, abstractGraph, optionsDict)
    __edgeRouter(abstractGraph, optionsDict)        
            
#    debugLevelDict(levelDictionary)
    
    print '\n**   Hierarchical layout required', time.time() - t, \
                                                   'seconds to compute   **\n'
    
        
    

def __buildConnectionMap(abstractGraph, abstractNode2WrappedNodeMap):
    """
    Use:
      Builds a connection map (rapid access maps to children and parents)
    """
    
    # Directed edges with a single source and a single target node
    for directedEdge in abstractGraph.getAbstractEdgeList():
      source, target = directedEdge.getSourceTargetNodeTuple()
      sourceWrap = abstractNode2WrappedNodeMap[source]
      targetWrap = abstractNode2WrappedNodeMap[target]
            
      NodeWrapper.Source2TargetListMap[sourceWrap].append(
                                                    [targetWrap, directedEdge])
      
      # Self-loop --> Split into a node and 2 edges
      if(source == target):
        targetWrap = NodeWrapper(directedEdge, NodeWrapper.SELF_LOOP_EDGE) 
        targetWrap.children[sourceWrap] = [[directedEdge, False]]
        targetWrap.parents[sourceWrap] = [[directedEdge, False]]
        

      # Could be more than one link between source and target
      if(sourceWrap.children.has_key(targetWrap)):
        sourceWrap.children[targetWrap].append([directedEdge, False])
      else:
        sourceWrap.children[targetWrap] = [[directedEdge, False]]
        
      # Self-loop: must set the parent of the source to be the new node
      if(source == target):
        temp = targetWrap
        targetWrap = sourceWrap
        sourceWrap = temp

      if(targetWrap.parents.has_key(sourceWrap)):
        targetWrap.parents[sourceWrap].append([directedEdge, False])
      else:
        targetWrap.parents[sourceWrap] = [[directedEdge, False]]
        
        
    # Hyper edges with N source nodes and M target nodes. 
#    for hyperEdge in abstractGraph.getHyperEdgeList():
#      sourceList, targetList = hyperEdge.getSourceTargetNodeListsTuple()
#      for source in sourceList:
#        sourceWrap = abstractNode2WrappedNodeMap[source]
#        for target in targetList:
#          targetWrap = abstractNode2WrappedNodeMap[target]
#          
#          NodeWrapper.Source2TargetListMap[sourceWrap].append(targetWrap)
#          
#          # Could be more than one link between source and target
#          if(sourceWrap.children.has_key(targetWrap)):
#            sourceWrap.children[targetWrap].append([directedEdge, False])
#          else:
#            sourceWrap.children[targetWrap] = [[directedEdge, False]]
#            
#          if(targetWrap.parents.has_key(sourceWrap)):
#            targetWrap.parents[sourceWrap].append([directedEdge, False])
#          else:
#            targetWrap.parents[sourceWrap] = [[directedEdge, False]]
    
    
    
def __drawNodesEW(levelDictionary, abstractGraph, optionsDict):
  """ 
  Takes size of nodes into account to translate grid positions into actual
  canvas coordinates. This version does East or West directed drawings. 
  Please read the NS version first, this one just doesn't feel as intuitive...
  """  
  minOffsetX = optionsDict[MIN_HORIZONTAL_DISTANCE] 
  minOffsetY = optionsDict[MIN_VERTICAL_DISTANCE]
  layoutDirection = optionsDict[LAYOUT_DIRECTION]

  if(optionsDict[FORCE_TOPLEFT_TO_ORIGIN]):
    topLeft = [0, 0]
  else:
    topLeft = abstractGraph.getMaxUpperLeftCoordinate()

  # Caclulate x, y offsets
  offsetY = 0
  levelInt2offsetX = dict()
  for levelInt in levelDictionary.keys():
    currentLevel = levelDictionary[levelInt]
    levelInt2offsetX[levelInt] = 0
    
    # Calculate maximum node size on a per level basis (X is for all levels)
    # Then add minimum seperation distance between nodes
    for node in currentLevel:
      # getSize returns node width, and height of the node
      x, y = node.getSize(False) 
      offsetY = max(offsetY, y)
      levelInt2offsetX[levelInt] = max(levelInt2offsetX[levelInt], x) 
      
  if(layoutDirection == 'West'):
    # Need the maximum X coordinate so we can start in the east and move west
    maxX = 0    
    for levelInt in range(0, len(levelDictionary) - 1):
      maxX += levelInt2offsetX[levelInt] + minOffsetX                         
      
  maxOffsetY = offsetY + minOffsetY
  halfOffsetY = offsetY / 2
        
  # Send nodes to their final destination, assign final pos to dummy edges    
  x, y = topLeft
  for levelInt in levelDictionary.keys():
    currentLevel = levelDictionary[levelInt]      
    longEdgeOffset = [halfOffsetY, levelInt2offsetX[levelInt] / 3]
                  
    # Move each node in the level (This includes dummy nodes for edges)
    # moveTo(newPositionTuple, offsetForDummyEdgesInt)
    if(layoutDirection == 'East'):
      for node in currentLevel:
        node.moveTo((x, y + node.getGridPosition() * maxOffsetY), longEdgeOffset)
    elif(layoutDirection == 'West'):
      for node in currentLevel:
        node.moveTo((maxX - x, y + node.getGridPosition() * maxOffsetY), 
                     longEdgeOffset)
                        
    # Increment y for the next iteration
    x += levelInt2offsetX[levelInt] + minOffsetX
    
    
    
def __drawNodesNS(levelDictionary, abstractGraph, optionsDict):
  """ 
  Takes size of nodes into account to translate grid positions into actual
  canvas coordinates. This version does North and South directed drawings.
  """  
  minOffsetX = optionsDict[MIN_HORIZONTAL_DISTANCE] 
  minOffsetY = optionsDict[MIN_VERTICAL_DISTANCE]
  layoutDirection = optionsDict[LAYOUT_DIRECTION]


  if(optionsDict[FORCE_TOPLEFT_TO_ORIGIN]):
    topLeft = [0, 0]
  else:
    topLeft = abstractGraph.getMaxUpperLeftCoordinate()

  # Caclulate x, y offsets
  offsetX = 0
  levelInt2offsetY = dict()
  for levelInt in levelDictionary.keys():
    currentLevel = levelDictionary[levelInt]
    levelInt2offsetY[levelInt] = 0
    
    # Calculate maximum node size on a per level basis (X is for all levels)
    # Then add minimum seperation distance between nodes
    for node in currentLevel:
      # getSize returns node width, and height of the node
      x, y = node.getSize(False) 
      offsetX = max(offsetX, x)
      levelInt2offsetY[levelInt] = max(levelInt2offsetY[levelInt], y) 
                                   
      
  maxOffsetX = offsetX + minOffsetX
  halfOffsetX = offsetX / 2
  
  if(layoutDirection == 'North'):
    # Need the maximum Y coordinate so we can start in the south and move north
    maxY = 0    
    for levelInt in range(0, len(levelDictionary) - 1):
      maxY += levelInt2offsetY[levelInt] + minOffsetY 
      
      
  # Send nodes to their final destination, assign final pos to dummy edges    
  x, y = topLeft
  for levelInt in levelDictionary.keys():
    currentLevel = levelDictionary[levelInt]      
    longEdgeOffset = [halfOffsetX, levelInt2offsetY[levelInt] / 3]
                  
    # Move each node in the level (This includes dummy nodes for edges)
    # moveTo(newPositionTuple, offsetForDummyEdgesInt)
    if(layoutDirection == 'South'):
      for node in currentLevel:
        node.moveTo((x + node.getGridPosition() * maxOffsetX, y), longEdgeOffset)
    elif(layoutDirection == 'North'):
      for node in currentLevel:
        node.moveTo((x + node.getGridPosition() * maxOffsetX, maxY - y), 
                     longEdgeOffset)
                        
    # Increment y for the next iteration
    y += levelInt2offsetY[levelInt] + minOffsetY
    
        
    
    
def __edgeRouter(abstractGraph, optionsDict):
  """
  Use:
    Sets the coordinates for all the edges
  """
  
#===============================================================================
#  Self-looping edges (Must move these manually into position)
#===============================================================================
  for selfLoopedEdge in NodeWrapper.SelfLoopList: 
    x, y = selfLoopedEdge.getEdgePosition()
    abstractEdge = selfLoopedEdge.getAbstractNode()
    abstractEdge.setNewCoords((x, y))


#===============================================================================
#  Request simple edge optimization for all edges
#=============================================================================== 
  # Post-process, redraw the arrows
  for arrow in abstractGraph.getAbstractEdgeList():
    arrow.setLinkOptimization(optionsDict[USE_SPLINES],
                               optionsDict[ARROW_CURVATURE])
  
#===============================================================================
#  Multi-layer edge routing
#===============================================================================
  for dummyEdge in NodeWrapper.ID2LayerEdgeDict.keys():
    # The multi-layer edge is made up of a list of dummy nodes
    dummyList = NodeWrapper.ID2LayerEdgeDict[dummyEdge]
    
    # Grab one dummy node, get the value for one of the children of it,
    # this will be a list of abstactEdges and isReversed flags
    linkFlagList = dummyList[0].children.values()[0]   

    # Could have a multiple edges with same source/target 
    multipleEdgeList = []
    for abstractEdge, isReversedEdge in linkFlagList:
      multipleEdgeList.append(abstractEdge) 
                
    # Get all the points the edge must pass through (sorted by layer order)
    dummyList.sort(lambda a, b: cmp(a.getLayer(), b.getLayer()))
    
    # Reverse the edge direction if necessary
    if(isReversedEdge):
      dummyList.reverse()
    sortedDummyRouteList = []
    for node in dummyList:
      sortedDummyRouteList += node.getEdgePosition()
      
    # SIMPLE CASE: There is only one edge between source and target node
    if(len(multipleEdgeList) == 1):
      # Cancel simple edge routing in favour of direct control point application
      abstractEdge = multipleEdgeList[0]
      #abstractEdge.setLinkOptimization(None, None)    
      abstractEdge.setControlPoints(sortedDummyRouteList)
      continue
    
    # COMPLEX CASE: There is multiple edges between source and target node
    i = 0
    multiEdgeScale = 10
    for abstractEdge in multipleEdgeList:      
      
      # Cancel simple edge routing in favour of direct control point application
      #abstractEdge.setLinkOptimization(None, None)    
      
      # First edge, set it along the computed path
      if(i == 0):
        abstractEdge.setControlPoints(sortedDummyRouteList)
        
      # Odd edge, add some horizontal distance to the computed path
      elif((i % 2) == 1):
        multiEdgeRoute = []
        for pos in sortedDummyRouteList:
          multiEdgeRoute.append(pos + (multiEdgeScale * ((i + 1) / 2)))
        abstractEdge.setControlPoints(multiEdgeRoute)
        
      # Even edge, subtract some horizontal distance from the computed path
      else:
        multiEdgeRoute = []
        for pos in sortedDummyRouteList:
          multiEdgeRoute.append(pos - (multiEdgeScale * (i / 2)))
        abstractEdge.setControlPoints(multiEdgeRoute)
        
      i += 1
    
    