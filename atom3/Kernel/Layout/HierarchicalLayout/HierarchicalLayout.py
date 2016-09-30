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
  
#todo: crossing heuristic improvements

  
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

from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog
from Utilities            import optimizeLinks, optimizerHyperLink
from ModelSpecificCode    import isConnectionLink

from NodeWrapper import NodeWrapper, initilizeNodeWrapper
from LayeringModule import greedyCycleRemover, longestPathLayeringTopDown
from LayeringModule import longestPathLayeringBottomUp, MinimumWidthLayering
from LayeringModule import addDummyNodes
from Debug import debugLevelDict, debugCrossing
from CrossingModule import barycentricOrdering
from HorizontalPositioner import priorityBarycenterPositioner



def applyLayout( atom3i = None, settings = False, selection = None ):
  
   # Instantiate the layout algorithm, if not already done  
  if( HierarchicalLayout.instance == None ):
    if( atom3i == None ):
      raise Exception, "You forgot to initilize "+__name__+" before using it!"
    HierarchicalLayout.instance = HierarchicalLayout(atom3i)    
  
  if( atom3i ):
    HierarchicalLayout.instance.updateATOM3instance( atom3i )
  
  if( settings ):
    HierarchicalLayout.instance.settings( selection ) 
  else:    
    HierarchicalLayout.instance.main( selection )   
    
    
    
class HierarchicalLayout:

  instance = None
    
  def __init__(self, atom3i ):
     
    self.cb = atom3i.cb
    self.atom3i = atom3i
    
    # Instantiate the Option Database module
    self.__optionsDatabase = OptionDatabase( atom3i.parent,
          'Options_HiearchicalLayout.py', 'Hieararchical Layout Configuration')
    
    # Local methods/variables with short names to make things more readable :D
    newOp = self.__optionsDatabase.createNewOption
    IE = OptionDialog.INT_ENTRY
    BE = OptionDialog.BOOLEAN_ENTRY
      
    # Create New Options
    # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
    
    optionList = [OptionDialog.LABEL, "Times 12", "blue", "left" ]
    
    newOp( 'label0001', None, optionList, 'Node spacing', '' )
    newOp( 'xOffset', 30, IE, "Minimum X Distance", 
        "Minimum horizontal distance between any 2 tree nodes (negative" 
        + " values work too) (Default 30)" )   
    newOp( 'yOffset', 30, IE, "Minimum Y Distance", 
        "Minimum vertical distance between any 2 tree nodes (Default 30)" )  
    newOp( 'addEdgeObjHeight', True, BE, "Add edge object height", 
        "Increment spacing between node layers with edge object drawing of"\
        + " maximum height between 2 given layers" ) 
    
    newOp('sep0000', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
    newOp( 'label0002', None, optionList, 'Miscellaneous options', '' )
    newOp( 'Origin', False, BE, "Start tree at origin?", 
        "If false, the current position of the selected nodes is used" )  
#    newOp( 'Manual Cycles', False, BE, "Manual Cycle Breaking", 
#        "Forces the user to break cycles by manually clicking on nodes" )      
    newOp( 'uncrossPhase1', 5, IE, "Maximum uncrossing iterations", 
        "Maximum number of passes to try to reduce edge crossings" \
        + "\nNote: these only count when no progress is being made" )  
    newOp( 'uncrossPhase2', 15, IE, "Maximum uncrossing random restarts", 
        "These can significantly improve quality, but they restart the " \
        + "uncrossing phase to the beginning..." \
        + "\nNote: these only count when no progress is being made" ) 
    newOp( 'baryPlaceMax', 10, IE, "Maximum gridpositioning iterations", 
        "Number of times a barycenter placement heuristic is run to " \
        + "ensure everything is centered" ) 
    
    newOp('sep0001', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
    newOp('label0003', None, optionList, 'Arrow post-processing options', '')
        
    newOp( 'Spline optimization' , False, BE, "Spline optimization", 
        "Sets the arrow to smooth mode and adds 2 extra control points" )
    newOp( 'Arrow curvature', 0, IE, "Arrow curvature", 
        "Adds a curve of magnitude X to the arrows, "
        +"set to 0 for a straight arrow." )    
        
     
    # Load the options from the file, on failure the defaults above are used.
    self.__optionsDatabase.loadOptionsDatabase()
  
  
  
  def updateATOM3instance( self, atom3i ):
    """ Possible to have multiple instances of atom3 """
    self.cb = atom3i.cb 
    self.atom3i = atom3i   
   
   
   
  def settings( self, selection ):
    """
    Dialog to interactively change the spring's behavior
    Automatically applies layout if not canceled
    """
    if( self.__optionsDatabase.showOptionsDatabase() ):
      self.main( selection )
    
    
    
  def main( self, selection ): 
    """
    Main algorithm, does all the high-level steps, delegates details to other
    methods.
    """
    t = time.time()

    # Step 1: Get all entity nodes (semantic objects) and wrap them
    entityNodeList, linkNodeDict = self.__getEntityLinkTuple(selection)    
    if(len(entityNodeList) == 0):
      return
      
    # Initilize the node wrapper class attributes
    initilizeNodeWrapper()
      
    # Wrap the AToM3 semantic nodes to make applying the algorithms easier     
    wrappedNodeList = []
    for node in entityNodeList:
      wrappedNodeList.append(NodeWrapper(node, NodeWrapper.REGULAR_NODE))
          
    # Build a connection map (rapid access maps to children and parents)
    for wrappedNode in wrappedNodeList:
      wrappedNode.buildConnectivityMaps(linkNodeDict)
      
    # Step 2: Build a proper layered hieararchy
    wrappedNodeList = greedyCycleRemover(wrappedNodeList)
    layerTime = time.time()
    if(1):
      levelDictionary = longestPathLayeringTopDown(wrappedNodeList)
      levelDictionary = addDummyNodes(levelDictionary, isGoingDown=True)
    elif(0):
      levelDictionary = longestPathLayeringBottomUp(wrappedNodeList)
      levelDictionary = addDummyNodes(levelDictionary, isGoingDown=False)
    else:
      mwl = MinimumWidthLayering(wrappedNodeList)
      # UBW = 1..4, c = 1..2
      levelDictionary = mwl(2, 2)
      levelDictionary = addDummyNodes(levelDictionary, isGoingDown=False)
    print '   Layering algorithm required', time.time() - layerTime, \
          'seconds to assign each node a layer'
    #return
    print '\n    Added dummy nodes, dumping layers:'
    debugLevelDict(levelDictionary)
          
    # Step 3: Minimize crossings    
    levelDictionary = barycentricOrdering(levelDictionary,
                                  self.__optionsDatabase.get('uncrossPhase1'),
                                  self.__optionsDatabase.get('uncrossPhase2'))
    
    # Step 4: Horizontal grid positioner
    priorityBarycenterPositioner(levelDictionary, 
                                 self.__optionsDatabase.get('baryPlaceMax') )
    
    # Step 5: Draw nodes and edges on the canvas
    if(len(selection) != 0):
      topLeft = self.__getMaxUpperLeftCoordinate(entityNodeList)
    else:
      topLeft = [0, 0]
    self.__drawNodes(levelDictionary, linkNodeDict, topLeft)
            
    debugLevelDict(levelDictionary)
    
    print '\nHierarchical layout took', time.time() - t, 'seconds to compute'
    
    
               

  def __getMaxUpperLeftCoordinate(self, entityNodeList):
    """ 
    Returns the maximum upper left coordinate of all the nodes the layout is
    being applied to
    This corresponds to the minumum x and y coords of all the nodes
    """
    minX = sys.maxint
    minY = sys.maxint
    for node in entityNodeList:
      if(node.graphObject_.y < minY):
        minY = node.graphObject_.y
      if(node.graphObject_.x < minX):
        minX = node.graphObject_.x 
    return (minX, minY)
        
        
    
  def __getEntityLinkTuple(self, selection):
    """
    If selection is empty, get all nodes & links on the canvas
    Else returns the entities and links in the selection
    Returns a tuple containing:
      entityList = List of entity ASG nodes
      linkNodeDict = Mapping of link ASG nodes to VisualObj graph objects
    """
    entityNodeList = []    # Non-edge entities
    linkNodeDict = dict()  # Regular and self-looping edges
    
    # Selection may contain a mixed bag of nodes and links
    if(selection):
      for node in selection:
        semObj = node.semanticObject  
        if(isConnectionLink(node)):   
          #linkNodeList.append(semObj)
          linkNodeDict[semObj] = node
        else:           
          entityNodeList.append(semObj)
          
    # No selection? Grab all nodes in diagram
    else:
      if(not self.atom3i.ASGroot): 
        return ([], [])
      for nodetype in self.atom3i.ASGroot.nodeTypes:  
        for node in self.atom3i.ASGroot.listNodes[nodetype]:      
          if(isConnectionLink(node.graphObject_)):  
            #linkNodeList.append(node)
            linkNodeDict[node] = node.graphObject_
          else:            
            entityNodeList.append(node)

   
    if(selection):
      return (entityNodeList, linkNodeDict)    
    return (entityNodeList, linkNodeDict)    
     
     
      
      
    
  def __drawNodes(self, levelDictionary, linkNodeDict, topLeft):
    """ 
    Takes size of nodes into account to translate grid positions into actual
    canvas coordinates
    """
    setSmooth    = self.__optionsDatabase.get('Spline optimization')   
    setCurvature = self.__optionsDatabase.get('Arrow curvature') 
    minOffsetY = self.__optionsDatabase.get('yOffset') 
    minOffsetX = self.__optionsDatabase.get('xOffset') 
    giveExtraSpaceForLinks = self.__optionsDatabase.get('addEdgeObjHeight') 

    # Caclulate x, y offsets
    offsetX = 0
    levelInt2offsetY = dict()
    for levelInt in levelDictionary.keys():
      currentLevel = levelDictionary[levelInt]
      levelInt2offsetY[levelInt] = 0
      
      # Calculate maximum node size on a per level basis (X is for all levels)
      # Then add minimum seperation distance between nodes
      for node in currentLevel:
        # getSize returns node width, and height of the node & child link icon
        x, y = node.getSize(giveExtraSpaceForLinks)
        offsetX = max(offsetX, x)
        levelInt2offsetY[levelInt] = max(levelInt2offsetY[levelInt], y) 
                                     
        
    maxOffsetX = offsetX + minOffsetX
    halfOffsetX = offsetX / 2
        
    # Send nodes to their final destination, assign final pos to dummy edges
    x, y = topLeft
    for levelInt in levelDictionary.keys():
      currentLevel = levelDictionary[levelInt]      
      longEdgeOffset = [halfOffsetX, levelInt2offsetY[levelInt] / 3]
                    
      # Move each node in the level (Dummy edges save the pos but don't move)
      for node in currentLevel:
        node.moveTo(x + node.getGridPosition() * maxOffsetX, y, longEdgeOffset)
        
      # Increment y for the next iteration
      y += levelInt2offsetY[levelInt] + minOffsetY
      
    # Self-looping edges (Must move these manually into position)
    for selfLoopedEdge in NodeWrapper.SelfLoopList: 
      x, y = selfLoopedEdge.getEdgePosition()
      obj = selfLoopedEdge.getASGNode().graphObject_
      obj.moveTo(x, y)

    # Re-doing links can take a while, lets show something in meanwhile...
    self.atom3i.parent.update()
     
    # Re-wire the links to take into account the new node positions
    selectedLinks = []
    for obj in linkNodeDict.values():
      selectedLinks.append(obj)
    optimizeLinks(self.cb, setSmooth, setCurvature, 
                  selectedLinks=selectedLinks)
    
    # Re-doing links can take a while, lets show something in meanwhile...
    self.atom3i.parent.update()
    
    # Route multi-layer edges
    self.__edgeRouter()
    
    

    
  def __edgeRouter(self):
    """
    Previously, edges traversing multiple layers were represented as a chain
    of dummy nodes. Now these nodes are used as points on a continuous spline.
    """
    def getEndpoint(nodeTuple, pointList, direction, isReversedEdge):
      """ Gets the nearest arrow endpoint. Handles edge reversal """
      if((direction == 'start' and not isReversedEdge)
         or (direction == 'end' and isReversedEdge)):        
        endNode = nodeTuple[0]
        if(isReversedEdge):
          ix = -2
          iy = -1
        else:
          ix = 0
          iy = 1
      else:        
        endNode = nodeTuple[1]
        if(isReversedEdge):
          ix = 0
          iy = 1
        else:
          ix = -2 
          iy = -1        
          
      # Is it connected to a named port!?!
      if(endNode.isConnectedByNamedPort(edgeObject)):
        handler = endNode.getConnectedByNamedPortHandler(nodeTuple[2]) 
        return dc.coords(handler)[:2]
          
      # Not a named port...
      return list(endNode.getClosestConnector2Point( endNode, pointList[ix], 
                                                             pointList[iy]))   
    
    
    
    #todo: improve method for spline arrows + add comments + optimize?
    print '----------------Dummy Edge Routing-----------------'
    for dummyEdge in NodeWrapper.ID2LayerEdgeDict.keys():
      
      dummyList = NodeWrapper.ID2LayerEdgeDict[dummyEdge]
      dummyNode = dummyList[0]
      dummyChild = dummyNode.children.keys()[0]
      linkFlagList = dummyNode.children[dummyChild]
      
      # Real nodes at start/end of the edge
      edgeSourceNode = dummyNode.parents.keys()[0]
      edgeSourceNode = edgeSourceNode.getASGNode().graphObject_
      dummyNode = dummyList[-1]
      edgeTargetNode = dummyNode.children.keys()[0]
      #print 'Dummy edge number', dummyEdge,
      #print dummyList[0].parents.keys()[0].getName(),  edgeTargetNode.getName()
      edgeTargetNode = edgeTargetNode.getASGNode().graphObject_
      nodeTuple = [edgeSourceNode, edgeTargetNode, None]
      
      # Some edges are internally reversed to break cycles, when drawing
      # this must be taken into account
      isReversedEdge = False
      edgesToRoute = []
      for linkNode, isReversed in linkFlagList:
        edgesToRoute.append(linkNode)
        if(isReversed):
          isReversedEdge = True
        
      # Get all the points the edge must pass through (sorted by layer order)
      dummyList.sort(lambda a, b: cmp(a.getLayer(), b.getLayer()))
      if(isReversedEdge):
        dummyList.reverse()
      sortedDummyRouteList = []
      for node in dummyList:
        sortedDummyRouteList += node.getEdgePosition()
      
      # Set the coordinates of the edge directly 
      # This is complicated by the fact that AToM3 treats edges as two
      # segments that join poorly (for spline arrows)
      for edgeObject in edgesToRoute:        
        dc = edgeObject.graphObject_.dc
        linkObj = edgeObject.graphObject_        
        tag = linkObj.tag
        
        if(isReversedEdge):
          inPoint = dc.coords( tag + "2ndSeg0" )[:2]
          outPoint = dc.coords( tag + "1stSeg0" )[:2]
        else:
          inPoint = dc.coords( tag + "1stSeg0" )[:2]
          outPoint = dc.coords( tag + "2ndSeg0" )[:2]
        
        #print 'Dummy route', sortedDummyRouteList
        numPoints = len(sortedDummyRouteList) / 2
        # Add 2 extra control points for odd case (to make splines nice)
        if(numPoints % 2 == 1):
          if(numPoints == 1):
            center = sortedDummyRouteList
          else:
            start = sortedDummyRouteList[:numPoints - 1]
            end = sortedDummyRouteList[numPoints + 1:]
            center = sortedDummyRouteList[numPoints - 1:numPoints + 1]
          
          if(not isReversedEdge):
            newMid1 = [center[0], center[1] - 20]
            newMid2 = [center[0], center[1] + 20]
          else:
            newMid2 = [center[0], center[1] - 20]
            newMid1 = [center[0], center[1] + 20]
            
                              
          if(numPoints == 1):
            sortedDummyRouteList = newMid1 + center + newMid2 
          else:
            sortedDummyRouteList = start + newMid1 + center + newMid2 + end
          centerIndex = numPoints - 1 + 2
          
        # Add 1 extra control point for even case (to make splines nice)
        else:
          start = sortedDummyRouteList[:numPoints]
          end = sortedDummyRouteList[numPoints:]
          center = [start[-2] + (end[0] - start[-2]) / 2, 
                    start[-1] + (end[1] - start[-1]) / 2]
          sortedDummyRouteList = start + center + end          
          centerIndex = numPoints
          
        # Now I know where the center is... so lets move the center object
        # Is the edge object a hyperlink?
        if(len(edgeObject.in_connections_ + edgeObject.out_connections_) > 2):
          fromObjs = []
          for semObj in edgeObject.in_connections_:
            fromObjs.append(semObj.graphObject_)
          toObjs = []
          for semObj in edgeObject.out_connections_:
            toObjs.append(semObj.graphObject_)
          optimizerHyperLink(dc, linkObj, fromObjs, toObjs, 0, 0, 0, center )
          continue
          
        else:
          linkObj.moveTo(* center)
        
        # Go through the 2 segments in the link
        nodeTuple[2] = edgeObject
        for connTuple in linkObj.connections:
          itemHandler = connTuple[0]
          direction = connTuple[1]
          
          if( direction ):     
            inPoint = getEndpoint(nodeTuple, sortedDummyRouteList,
                                  'start', isReversedEdge)

            segCoords = inPoint + sortedDummyRouteList[:centerIndex+2]
          else:           
            outPoint = getEndpoint(nodeTuple, sortedDummyRouteList,
                                   'end', isReversedEdge) 
            segCoords = sortedDummyRouteList[centerIndex:] + outPoint
            segCoords = self.__reverseCoordList(segCoords)
      
          # Applies the changed coords to the canvas
          dc.coords( * [itemHandler] + segCoords )    
          
          # This may change the associated link drawings: 
          # move them to the new point 
          if( direction ):
            linkObj.updateDrawingsTo(inPoint[0], inPoint[1], itemHandler, 
                                                          segmentNumber=1)
          else:
            linkObj.updateDrawingsTo(outPoint[0], outPoint[1], itemHandler, 
                                                            segmentNumber=2)
    
    

  def __reverseCoordList(self, segCoords):
    """ 
    Input: list of coordinates [x0, y0, x1, y1, ..., xn, yn]
    Output: list of coordinates reversed [xn, yn, ..., x1, y1, x0, y0]
    """    
    reversedCoords = []
    for i in range(len(segCoords) - 1, 0, -2):
      reversedCoords += [segCoords[i - 1], segCoords[i]]
    return reversedCoords
      
      
      
    


  