"""
TreeLikeLayout.py

Creates a simple tree layout, but works on general graphs too (less effective)

Created Summer 2005, Denis Dube
"""

#todo: warning: could affect unselected nodes...

import sys
import time
from tkMessageBox import showinfo

from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog
from Utilities            import optimizeLinks
from ModelSpecificCode    import isConnectionLink


def applyLayout( atom3i = None, settings = False, selection = None ):
  
   # Instantiate the layout algorithm, if not already done  
  if( TreeLikeLayout.instance == None ):
    if( atom3i == None ):   
      raise Exception, "You forgot to initilize "+__name__+" before using it!"
    TreeLikeLayout.instance = TreeLikeLayout(atom3i)    
  
  if( atom3i ):
    TreeLikeLayout.instance.updateATOM3instance( atom3i )
  
  if( settings ):
    TreeLikeLayout.instance.settings( selection ) 
  else:    
    TreeLikeLayout.instance.main( selection )   
    
class TreeLikeLayout:

  instance = None
    
  def __init__(self, atom3i ):
     
    self.cb = atom3i.cb
    self.atom3i = atom3i

    # Instantiate the Option Database module
    self.__optionsDatabase = OptionDatabase( atom3i.parent,
                 'Options_TreeLikeLayout.py', 'TreeLikeLayout Configuration')
    
    # Local methods/variables with short names to make things more readable :D
    newOp = self.__optionsDatabase.createNewOption
    IE = OptionDialog.INT_ENTRY
    BE = OptionDialog.BOOLEAN_ENTRY
      
    # Create New Options
    # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
    
    optionList = [OptionDialog.LABEL, "Times 12", "blue", "left" ]
    
    newOp( 'label0001', None, optionList, 'Node spacing', '' )
    newOp( 'xOffset', 20, IE, "Minimum X Distance", 
        "Minimum horizontal distance between any 2 tree nodes (Default 20)" )   
    newOp( 'yOffset', 70, IE, "Minimum Y Distance", 
        "Minimum vertical distance between any 2 tree nodes (Default 70)" )  
    
    newOp('sep0000', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
    newOp( 'label0002', None, optionList, 'Miscellaneous options', '' )
    newOp( 'Origin', False, BE, "Start tree at origin?", 
        "If false, the current position of the selected nodes is used" )        
    newOp( 'Manual Cycles', False, BE, "Manual Cycle Breaking", 
        "Forces the user to break cycles by manually clicking on nodes" )
    
    newOp('sep0001', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
    newOp('label0003', None, optionList, 'Arrow post-processing options', '')
        
    newOp( 'Spline optimization' , True, BE, "Spline optimization", 
        "Sets the arrow to smooth mode and adds 2 extra control points" )
    newOp( 'Arrow curvature', 10, IE, "Arrow curvature", 
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
    
    setSmooth    = self.__optionsDatabase.get('Spline optimization')   
    setCurvature = self.__optionsDatabase.get('Arrow curvature') 
    doManualCycles = self.__optionsDatabase.get('Manual Cycles') 
    doStartAtOrigin = self.__optionsDatabase.get('Origin') 
     
    # Get all entity nodes (semantic objects)
    entityNodeList = self.__getEntityList(selection)    
    if(len(entityNodeList) == 0):
      return
    
    # Get all root nodes (cycle in children possible), pure cycles will remain
    rootNodes = []
    for node in entityNodeList:
      if(node._treeVisit == False and len(node.in_connections_) == 0):
        node._treeVisit = True
        rootNodes.append(node)
        self.__markChildrenNodesBFS(node, [])
        
    # Gather all the cycle nodes
    cycleNodes = []
    for node in entityNodeList:
      if(node._treeVisit == False):
        cycleNodes.append(node)
    
    # Node cycle breakers --> choice of nodes as root to break the cycle
    if(doManualCycles):
      rootNodes = self.__getCycleRootsManually(cycleNodes, rootNodes)
    else:
      rootNodes = self.__getCycleRootsAuto(cycleNodes, rootNodes)
            
    #self.debugTree(rootNodes) # DFS printer
    
    # This does the actual moving around of nodes
    if(doStartAtOrigin):
      self.__layoutRoots(rootNodes, (0, 0))
    else:
      self.__layoutRoots(rootNodes, 
                         self.__getMaxUpperLeftCoordinate(entityNodeList))
    
    # Clean up
    for node in entityNodeList:
      del node._treeVisit 
      del node._treeChildren 
    
    # Re-wire the links to take into account the new node positions
    optimizeLinks(self.cb, setSmooth, setCurvature, 
             selectedLinks=self.__getLinkListfromEntityList(entityNodeList))
    
    
    
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
        
        
    
  def __getEntityList(self, selection):
    """
    If selection is empty, get all nodes on the canvas
    Else filter out links
    Returns semantic objects, subclasses of ASGNode rather than VisualObj
    """
    entityNodeList = []
    
    # Selection may contain a mixed bag of nodes and links
    if(selection):
      for node in selection:
        if(not isConnectionLink(node)):   
          semObj = node.semanticObject   
          semObj._treeVisit = False
          semObj._treeChildren = []    
          entityNodeList.append(semObj)
          
    # No selection? Grab all nodes in diagram
    else:
      if(not self.atom3i.ASGroot): 
        return []
      for nodetype in self.atom3i.ASGroot.nodeTypes:  
        for node in self.atom3i.ASGroot.listNodes[nodetype]:      
          if(not isConnectionLink(node.graphObject_)):  
            node._treeVisit = False
            node._treeChildren = []   
            entityNodeList.append(node)
 
    return entityNodeList

    
  def __getLinkListfromEntityList(self, entityNodeList):
      """
      Find all links attached to the list of nodes
      """
      linkList = []    
      for semObject in entityNodeList:
        linkNodes = semObject.in_connections_ + semObject.out_connections_
        for semObj in linkNodes:
          if(semObj.graphObject_ not in linkList):
            linkList.append(semObj.graphObject_)
      return linkList
      
      
  def __getCycleRootsAuto(self, cycleNodes, rootNodes):
    """
    Breaks cycles by automatically choosing root nodes
    Nodes with the highest out degree are the preferred choice
    Returns root nodes including the ones that break the cycles
    """
    OutDegree2cycleNodeList = dict()
    # Associate each out degree with a list of nodes
    for node in cycleNodes:
      outDegree = len(node.out_connections_)
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
          self.__markChildrenNodesBFS(node, [])
    return rootNodes
      
      

  def __getCycleRootsManually(self, cycleNodes, rootNodes):
    """
    Allows the user to break cycles by clicking on nodes to choose tree roots
    Returns the final rootNodes (ie: including those that break cycles)
    """
    if(len(cycleNodes) > 0):
      showinfo('TreeLikeLayout: Cycle/s Detected', 
               'Manual cycle breaking mode in effect\n\n'
                + 'Cyclic nodes will be highlighted\n\n'
                + 'Please break the cycle/s by clicking on the node/s'
                + ' you want as tree root/s')
    while(len(cycleNodes) > 0):
      self.cb.clearSelectionDict()          
      index = self.__chooseRoot(cycleNodes)
      if(index != None):
        chosenRootNode = cycleNodes[index]
        chosenRootNode._treeVisit = True
        rootNodes.append(chosenRootNode) 
        self.__markChildrenNodesBFS(chosenRootNode, [])
      # Cleanup: leave only nodes that still form a cycle
      temp = cycleNodes[:]
      for node in temp:
        if(node._treeVisit == True):
          cycleNodes.remove(node)
          node.graphObject_.HighLight(0)
    return rootNodes
  
  def __chooseRoot(self, cycleNodes):  
    """
    Allows the user to manually choose a node in a cycle to be root
    """
    # Makes a special list of the cycle nodes, highlight them on the canvas
    matchList = []
    for node in cycleNodes:
      node.graphObject_.HighLight(1)
      matchList.append([0, [node]])
          
    # Initilize the choosing system. Special behaviour mode in statechart
    # This means that the user MUST choose a node, nothing else will work
    no_value_yet = -1
    self.cb.initMatchChoice( no_value_yet, matchList )
    self.atom3i.UI_Statechart.event("GG Select", None)  
                
    # Now we wait for the user to click somewhere, polling style
    while(self.cb.getMatchChoice() == no_value_yet ):    
      time.sleep( 0.1 ) # Time in seconds
      self.atom3i.parent.update()      
    
    return self.cb.getMatchChoice()
  
  
  def __layoutRoots(self, rootNodes, originPointXY):
    """
    General graph may have more than a single root, so pretend the roots are
    all tied to some imaginary root high in the sky...
    """
    (xPos, yPos) = originPointXY
    xOffset = self.__optionsDatabase.get('xOffset')
    yOffset = self.__optionsDatabase.get('yOffset')
    
    # Find the max height of all the root level nodes
    maxHeight = 0
    for rootNode in rootNodes:
      maxHeight = max(maxHeight, rootNode.graphObject_.getSize()[1])
    
    for rootNode in rootNodes:
      w = 0
      # Layout the children of the root, then we'll know exactly where the
      # root itself goes...
      for childNode in rootNode._treeChildren:
        w0 = self.__layoutNode(childNode, xPos + w, yPos + yOffset + maxHeight,
                        xOffset, yOffset)      
        w += w0 + xOffset
          
      # Okay, now we place the root half-way between its children
      # but move it back a bit to account for its width (center it)
      widthOffset = rootNode.graphObject_.getSize()[0] / 2
      rootNode.graphObject_.moveTo(xPos + w / 2 - widthOffset, yPos)    
      xPos += w
    
       
  def __layoutNode(self, node, xPos, yPos, xOffset, yOffset):    
    """
    Do the layout for an ordinary node
    """
    
    # No children? Then this is very easy to position...
    if(len(node._treeChildren) == 0):
      (w, h) = node.graphObject_.getSize()
      widthOffset = node.graphObject_.getSize()[0] / 2 # Node center offset
      node.graphObject_.moveTo(xPos + (w + xOffset) / 2 - widthOffset, yPos)
      return w
      
    # Has children, doh! Layout children first, then position parent    
    else:
      w = 0
      h = node.graphObject_.getSize()[1] + yOffset
      for childNode in node._treeChildren:
        w0 = self.__layoutNode(childNode, xPos + w, yPos + h, xOffset, yOffset)
        w += w0 + xOffset
      # Position the parent of the children, knowning width children occupy
      widthOffset = node.graphObject_.getSize()[0] / 2 # Node center offset
      node.graphObject_.moveTo(xPos + w / 2 - widthOffset, yPos)
      return w - xOffset
  
  
  def debugTree(self, rootNodes):
    for node in rootNodes:
      print 'Root nodes found', node.name.toString() #node.__class__.__name__, 
      self.debugTreeChildrenDFS(node)
  
  def debugTreeChildrenDFS(self, node):
    for childNode in node._treeChildren:
      print 'Child node',  childNode.name.toString() 
      self.debugTreeChildrenDFS(childNode)

  def __markChildrenNodesDFS(self, node):
    """ 
    Depth first search algorithm
    Descends a tree, marking all children as visited
    In case of cycle, the child node is ignored
    """  
    for link in node.out_connections_:
      for childNode in link.out_connections_:     
        # childNode may not be in the selection, in that case it will not have
        # the _treeVisit attribute
        if(childNode.__dict__.has_key('_treeVisit')
           and childNode._treeVisit == False): 
          node._treeChildren.append(childNode)
          childNode._treeVisit = True    
          self.__markChildrenNodesDFS(childNode)
    
  def __markChildrenNodesBFS(self, node, queuedNodeList):
    """ 
    Breadth first search algorithm
    Descends a tree, marking all children as visited
    In case of cycle, the child node is ignored
    """    
    for link in node.out_connections_:
      for childNode in link.out_connections_:     
        # childNode may not be in the selection, in that case it will not have
        # the _treeVisit attribute
        if(childNode.__dict__.has_key('_treeVisit')
           and childNode._treeVisit == False): 
          node._treeChildren.append(childNode)
          childNode._treeVisit = True    
          queuedNodeList.append(childNode)
    if(len(queuedNodeList) == 1):
      self.__markChildrenNodesBFS(queuedNodeList[0], [])
    elif(len(queuedNodeList) > 1):
      self.__markChildrenNodesBFS(queuedNodeList[0], queuedNodeList[1:])

  
      
  
