"""
AbstractGraph.py

The purpose of this file is to abstract away the internal representation of 
graphs in AToM3 so that the layout algorithms referenced herein only deal with
the most generic description of graphs. 

Why do this? Any Python application that implements the AToM3LayoutInterface.py
and AToM3LayoutInterfaceModule methods that are AToM3 specific (they are 
commented as such) can use all the layout algorithms "for free".

WARNING: Tkinter may be assumed present in some of the layout algorithms just
to display a simple warning/notification message. Feel free to disable/modify 
these if you have problems. Ie: TreeLikeLayout.py uses a tkMessageBox.


Responsibilities:
  1) Convert AToM3 graph to a generic graph
  2) Convert changes to the generic graph back into AToM3 changes
  3) Provide an intermediate layer for layout options 
  

Class Diagram (associations & inheritance):           
             
                    AbstractObject                    
                          ^
                          |
                __________|_____________
               |          |             |
         AbstractEdge  HyperEdge  AbstractNode
               ^           |______      ^     \______
               |                  |     |            |
        _______|___________       |   __|_____       |
       |                   |      |  |        |      |
  DirectedEdge  HyperEdgeComponent| Node  HyperNode  |
           \        \      |  ____|  /      /       /
            \_______ \__   | /  ____/  ____/   ____/
                    \   \  | | /  ____/   ____/   
                     \   \ | |/  /_______/    
                     AbstractGraph     
                        
Why is this so complicated?
  Short answer: 
    Hyperedges
  Long answer: 
    The hyperedges require special treatment to convert them into a 
      node with simple directed edges, thus making this quite complex.  
    The benefit is that all the layout algorithms can then work on hyperedges 
      very easily.
      
What are pseudo-hyperedges?
  These are "normal" directed edges that are being treated as a hyperedge with 
  a single source and target. The advantage of this is that if the edge has a
  large center drawing, that drawing is treated as a node, resulting in a better
  layout. This of course increases the workload on the layout algorithm, because
  one directed edge effectively becomes one node and two edges and a controller
  object to put everything back together...


By Denis Dube, Sept 2005
"""

import sys

from ModelSpecificCode    import isConnectionLink

from DirectedEdge import DirectedEdge
from Node import Node
from HyperEdge import HyperEdge
from HyperEdgeComponent import HyperEdgeComponent
from HyperNode import HyperNode
from AbstractNode import AbstractNode


class AbstractGraph:
  """
  Container object for an abstraction of a graph into lists of Nodes and Edges
  
  Graph is abstracted into lists of:
    Nodes --> Node and HyperNode 
    Directed edges --> DirectedEdge and HyperEdgeComponent
    Hyper edges --> HyperEdge (controller object for HyperNode and HyperEdgeC.)
    
  NOTE: from the point of view of a client of this abstraction, the two types
        of nodes and edges are exactly the same.
  """  
  
  def __init__(self, atom3i, selectionList):
    """ NOTE: AToM3 dependent method """
    self.__atom3i = atom3i
    
    self.__NodeList = []
    self.__DirectedEdgeList = []
    self.__HyperEdgeList = []
    self.__HyperEdgeComponentList = []
    self.__HyperEdgeNodeList = []
          
              
    # Build the abstract graph structure
    if(selectionList):
      self.__buildAbstractGraphSelectOnly(selectionList)
    else:
      self.__buildAbstractGraphEntireCanvas(atom3i)



  def initNodeChildrenParents(self):
    """
    Use:
      For layout algorithms that need to rapidly traverse to the 
      children/parents of a node. This is an alternative method to using the
      edges themselves to figure out who is connected to what.
      
    Result:
      After application, use the getChildrenList/getParentsList methods defined
      in AbstractNode to get the children or parents of a node.
    """
    for edge in self.getAbstractEdgeList():
      source, target = edge.getSourceTargetNodeTuple()
      source.addChild(target)
      target.addParent(source)
      
      
      
  def getNodeList(self):
    """ 
    Consider using getAbstractNodeList instead, this ignores hyperedges and
    pseudo-hyperedgs (edges with node drawings)
    """
    return self.__NodeList
    
    
    
  def getAbstractNodeList(self):
    """ Returns both real nodes and the center point of a hyper edge """
    return self.__NodeList + self.__HyperEdgeNodeList
    
    
    
  def getDirectedEdgeList(self):
    """
    Consider using getAbstractEdgeList instead, this ignores hyperedges and
    pseudo-hyperedgs (edges with node drawings) 
    """
    return self.__DirectedEdgeList  
    
    
    
  def getHyperEdgeList(self):
    """ 
    DO NOT USE 
    (unless you really want to deal with hyper edges in a special way)
    """
    return self.__HyperEdgeList
    
    
        
    
  def getAbstractEdgeList(self):
    """ 
    Includes directed edges and the directed components of hyperedges and pseudo
    hyperedges (edges with node drawings) 
    """
    return self.__DirectedEdgeList + self.__HyperEdgeComponentList
    


  def getMaxUpperLeftCoordinate(self):
    """ 
    Returns the maximum upper left coordinate of all the nodes in the abstract
    graph.
    This corresponds to the minumum x and y coords of all the nodes
    """
    minX = sys.maxint
    minY = sys.maxint
    for node in self.__NodeList:
      x, y = node.getPos()
      if(y < minY):
        minY = y
      if(x < minX):
        minX = x 
    return (minX, minY)
    
    

  def promoteDirectedEdge(self, doAllEdges = False):
    """
    Use:
      Promotes directed edges into hyperedges, whereby the edge is split into
      a virtual node and two virtual directed edges. If the center drawing of 
      the edge is large, this can lead to far superiour layout. 
    Parameter:
      If doAllEdges is true, all edges are promoted
      Else only edges with a center drawing of non-zero size are promoted
    """
    
    # Promote non-zero sized center drawing possesing edges to hyperedges
    if(not doAllEdges):
      edgeListCopy = self.__DirectedEdgeList[:]
      for directedEdge in edgeListCopy:
        centerObj = directedEdge._obj.getCenterObject()
        if(centerObj):
          sx, sy = centerObj.getSize()
          if(sx != 0 and sy != 0):
            self.__buildHyperEdge(directedEdge._semanticObject)
            self.__DirectedEdgeList.remove(directedEdge)
            
    # Promote all the edges to hyperedges
    else:
      for directedEdge in self.__DirectedEdgeList:
        self.__buildHyperEdge(directedEdge._semanticObject)
      self.__DirectedEdgeList = []
      
      
      
  def updateInternally(self):
    """
    Intention in context:
      Multiple layouts are being used in succession, don't want to redraw on
      the screen between each layout! This will push 'newPos' variables to 'pos'
      Example: Circle --> Spring --> FTA layout gives nice results on class diag
    """
    for obj in self.__NodeList:
      obj.updateInternally()
    for obj in self.__HyperEdgeNodeList:
      obj.updateInternally()
      
      
          
  def updateAToM3(self, quickUpdate=True):
    """ 
    Updates changes to the abstract graph representation back into visual
    AToM3 entities.
    """
    # Update the plain vanilla nodes
    for obj in self.__NodeList:
      obj.applyCoordSizeChange()
      
    # Links can take a long time to draw, so user gets feedback quicker
    if(quickUpdate):
      self.__atom3i.parent.update()
    
    # Update the plain vanilla directed edges
    for obj in self.__DirectedEdgeList:
      obj.applyCoordSizeChange()
      
    # Setup the changes to hyper-edge center nodes
    for obj in self.__HyperEdgeNodeList:
      obj.applyCoordSizeChange()
      
    # Setup the changes to the hyper-edge links
    for obj in self.__HyperEdgeComponentList:
      obj.applyCoordSizeChange()
      
    # Apply all the changes made to center/links of the hyperedge      
    for obj in self.__HyperEdgeList:
      obj.applyCoordSizeChange()

        
      
     
  def __buildAbstractGraphSelectOnly(self, selectionList):
    """
    Generate abstraction of graph found in selection list
    NOTE: AToM3 dependent method
    """
    # Go through all the nodes    
    #nodeList = filter(lambda x: not isConnectionLink(x), selectionList)
    nodeList = [node for node in selectionList if not isConnectionLink(node)]
    for node in nodeList:
      self.__NodeList.append(Node(node.semanticObject))
        
    # Go through all the edges
    #edgeList = filter(isConnectionLink, selectionList)    
    edgeList = [node for node in selectionList if isConnectionLink(node)]
    for edge in edgeList:
      semObj = edge.semanticObject
        
      # Directed edge (could be self-loop)
      if(len(semObj.in_connections_) == len(semObj.out_connections_) == 1):
        self.__buildDirectedEdge(semObj)
        
      # Hyper-edge, multiple sources/targets
      else:
        self.__buildHyperEdge(semObj)
    
    
        
  def __buildAbstractGraphEntireCanvas(self, atom3i):
    """
    Generate abstraction of graph found on the whole atom3i canvas
    NOTE: AToM3 dependent method
    """
    if(not atom3i.ASGroot): 
      return
      
    edgeList = []
    for nodetype in atom3i.ASGroot.nodeTypes:  
      for node in atom3i.ASGroot.listNodes[nodetype]:      

        # Regular node
        if(not isConnectionLink(node.graphObject_)):   
          self.__NodeList.append(Node(node))
          
        # Edge
        else:
          edgeList.append(node)
          
    # Do edges in a 2nd phase, otherwise might try to lookup a Node object
    # that does not exist yet.
    for edge in edgeList:
      # Regular edge (could be self-loop)          
      if(len(edge.in_connections_) == len(edge.out_connections_) == 1):
        self.__buildDirectedEdge(edge)
        
      # Hyper-edge
      else:
        self.__buildHyperEdge(edge)
      
      
      
  def __buildDirectedEdge(self, node):
    """
    Use:
      Creates an absraction of a simple directed edge.
      
    NOTE: AToM3 dependent method
    """         
    # Regular directed edge handling, no special tricks
    source = node.in_connections_[0]   
    target = node.out_connections_[0]    
    
    semObj2NodeMap = AbstractNode.SemanticObject2NodeMap
    sourceTargetTuple = (semObj2NodeMap[source], semObj2NodeMap[target])

    self.__DirectedEdgeList.append(DirectedEdge(node, sourceTargetTuple))
          
          
  
  def __buildHyperEdge(self, node):
    """
    Use:
      Creates a complex abstraction of the hyperedge. 
      1) HyperEdge --> Represends the multiple sources/outputs of the edge
      2) HyperNode --> Represents just the center of the edge
      3) HyperEdgeComponent --> Represents each source-target pair as a directed
                                edge.
    Parameter:
      node is an ASGNode of the AToM3 variety, representing a hyper-edge
      
    NOTE: AToM3 dependent method
    """
    semObj2NodeMap = AbstractNode.SemanticObject2NodeMap
    
    # Create a HyperEdge "master" for this edge's representation
    hyperEdge = HyperEdge(node)
    self.__HyperEdgeList.append(hyperEdge)         
  
    # Create a new HyperNode representing the center of the hyperedge
    hyperNode = HyperNode(node, hyperEdge)
    self.__HyperEdgeNodeList.append(hyperNode)
    semObj2NodeMap[node] = hyperNode
    
#===============================================================================
#    Create HyperEdgeComponent, a set of directed edges equivelent to
#    the original hyper edge
#===============================================================================
    # Source object incomming to the hyperedge center
    direction = HyperEdgeComponent.SOURCE2CENTER
    i = 0 
    for i in range(0, len(node.in_connections_)):
      sourceSemObj = node.in_connections_[i]
      sourceTargetTuple = (semObj2NodeMap[sourceSemObj], hyperNode)
      
      hyperEdgeComponent = HyperEdgeComponent(node, sourceTargetTuple, 
                                              hyperEdge, direction, i)
      self.__HyperEdgeComponentList.append(hyperEdgeComponent)
      
      
    # Hyperedge center outgoing to the target object
    direction = HyperEdgeComponent.CENTER2TARGET
    i = 0
    for i in range(0, len(node.out_connections_)):
      targetSemObj = node.out_connections_[i]
      sourceTargetTuple = (hyperNode, semObj2NodeMap[targetSemObj])
      
      hyperEdgeComponent = HyperEdgeComponent(node, sourceTargetTuple, 
                                              hyperEdge, direction, i)
      self.__HyperEdgeComponentList.append(hyperEdgeComponent)
      
      
      
      