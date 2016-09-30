"""
HierarchicalASGNode.py

Built-in automatic hierarchical tracking by Denis Dube, Sept 2, 2005

Use the following three methods to access the hiearchical structure:
  getHierChildren()
  getAllHierChildren()
  getHierParent()
  
This structure is automatically maintained IF a formalism has an arrow with 
the isHierarchicalStructure flag set to true. See graphical appearence dialog.

Hierarchy code spills over into the following: 
 ASGNode.py --> genAttributesCode() and subclasses HierarchicalASGNode
 ASG.py --> processLoadedLinkNodes() and addNode()
 DrawConnections.py --> drawConnection()
 linkEditor.py --> show()
 ATOM3.py --> deleteConnection() and genCodeFor() and deleteRealEntity()

NOTE: Design error acknowledged, this should be a subclass not a superclass
of ASGNode! However it is too late in AToM3's developement cycle to do that.
The alternative is to mix this code with existing ASGNode.py code, but I felt
it best to seperate the different concerns as much as possible.
"""

class HierarchicalASGNode:

  # List of hierarchical nodes with no parents
  hierarchicalTopLayer = []

  def __init__(self):
     self.__hierChildrenList = []
     self.__hierParent = None
     
     # Used to indicate if a semantic relationship node is hierarchical
     self.__isHierarchicalLink = False
     self.__isHierarchicalNode = False
     
     # Used for non-visual 'insideness' links (when set to False)
     # This is not private simply because it's older code...
     self.isGraphObjectVisual = True

#=============================================================================
#  Public methods
#=============================================================================
  def getHierChildren(self):
    """ 
    Returns a copy of the list of hierarchical children of this node or [] 
    """
    return self.__hierChildrenList[:]
   
  def getAllHierChildren(self):
    """ 
    Returns a list of all the hierarchical children of this node (recursive) 
    """
    allChildren = self.__hierChildrenList[:] # Force a new copy of the list    
    for child in self.__hierChildrenList:
      allChildren += child.getAllHierChildren()
    return allChildren
    
  def getAllHierChildrenAndArrows(self, initialCall=True):
    """
    Use:
      Get all nodes that are hierarchical children of self, as well as all
      non-hierarchical arrows connected to self and children of self.
    Returns:
      A list all children and all non-hierarchical arrows connected to the 
      children without duplicates.
    """
    def getArrowDict(node):
      """
      Returns non-hierarchical arrows in a set, implemented using a dictionary
      """
      linkNodeDict = dict()
      linkNodes = node.in_connections_ + node.out_connections_
      for linkNode in linkNodes:
        if(not linkNode.__isHierarchicalLink):
          linkNodeDict[linkNode] = None # Don't care about value, want a set
      return linkNodeDict
      
    if(initialCall):
      allArrowsDict = dict()
    else:
      allArrowsDict = getArrowDict(self)
    allChildrenList = self.__hierChildrenList[:] # Force a new copy of the list
    
    for child in self.__hierChildrenList:
      childChildrenList, childArrowsDict = \
        child.getAllHierChildrenAndArrows(initialCall=False)
      allChildrenList += childChildrenList
      # a.update(b) ==> for k in b.keys(): a[k] = b[k]  where a, b are dict()
      # Equivelent to set union operation
      allArrowsDict.update(childArrowsDict)
      
    if(initialCall):
      return allChildrenList + allArrowsDict.keys()
    else:
      return (allChildrenList, allArrowsDict)
      
    
  def getHierParent(self):
    """ Returns the hierarchical parent of this node, or None """
    return self.__hierParent
    
  def getHierTopLayer(self):
    """ Returns a copy of the list of all hierarchical nodes with no parents """
    return HierarchicalASGNode.hierarchicalTopLayer[:]
    
  def hierPropagateMethodDown(self, boundMethod):
    """
    Applies the given boundMethod to self and to selfs non-hieararchical arrows,
    and recursively to all children
    """
    boundMethod(self)
    # Apply to non-hierarchical arrows
    linkNodes = self.in_connections_ + self.out_connections_
    for linkNode in linkNodes:
      if(not linkNode.__isHierarchicalLink):
        boundMethod(linkNode)
        
    # Recursion on children
    for child in self.__hierChildrenList:
      child.hierPropagateMethodDown(boundMethod)
    
#----------------------------------------------------- Get/set hierarchical flag

  def isHierarchicalLink(self):
    """ Is the link hierarchical in nature? Returns True/False """
    return self.__isHierarchicalLink
  
  def isHierarchicalNode(self):
    """ 
    Is the node hierarchical in nature? Returns True/False 
    True means that it is *possible* to hierarchically link this node
    """
    return self.__isHierarchicalNode
    
        
#=============================================================================
#  Protected methods
#=============================================================================
      
  def _setHierarchicalLink(self, flagBool):
    """ Set the link to be hierarchical or not, expects boolean value """
    self.__isHierarchicalLink = flagBool  
    
  def _setHierarchicalNode(self, flagBool):
    """ Set the node to be hierarchical or not, expects boolean value """
    self.__isHierarchicalNode = flagBool
      
#------------------------------------------------------------- Add/delete parent

  def _setHierParent(self, node):
    """ Set the hierarchical parent node """
    self.__hierParent = node
    self._removeNodeFromHierarchyTopLayer() # Has parent, not in top layer
    
  def _delHierParent(self):
    """ Delete the hierarchical parent node, sets parent to None """
    self.__hierParent = None
    self._addNodeToHierarchyTopLayer() # Has no parent, add to top layer
    
#-------------------------------------------------------------- Add/delete child
        
  def _addHierChild(self, node):
    """ Appends child node to list of children """
    self.__hierChildrenList.append(node)
        
  def _addHierChildrenList(self, nodeList):
    """ Appends child node to list of children """
    self.__hierChildrenList += nodeList
        
  def _delHierChild(self, node):
    """ Deletes a single child node from the list of children nodes """
    if(self.__hierChildrenList.__contains__(node)):
      self.__hierChildrenList.remove(node)
      
  def _delHierChildrenList(self, nodeList):
    """ 
    Deletes all the given children nodes from the list of children nodes 
    Called by atom3i.deleteConnection()
    """
    for node in nodeList:
      if(self.__hierChildrenList.__contains__(node)):
        self.__hierChildrenList.remove(node)
        
#---------------- Generate code for meta-model and for generated semantic object
        
  def _generateHierarchicalFlagCode(self, openFile, indent, myName): 
    """ 
    This makes it possible for AToM3 to 'remember' the setting in metamodels
    like Class Diagrams or Entity Relationship
    NOTE: Only link entities will ever get these flags set to True
    Called in ASGNode.py
    """
    openFile.write(indent+myName+'.isGraphObjectVisual = '
      +str(self.isGraphObjectVisual)+'\n\n')                
#    openFile.write(indent+myName+'._setHierarchicalLink('
#      +str(self.isHierarchicalLink())+')\n\n')  
    openFile.write(indent+"if(hasattr("+myName+", '_setHierarchicalLink')):\n")
    openFile.write(indent+'  '+myName+'._setHierarchicalLink('
                          + str(self.isHierarchicalLink())+")\n")
                          
  def _generateHierarchicalSemanticCode(self, openFile, indent):
    """
    This sets the is using hierarchical flag on each semantic object
    Only links will ever have the first two flags set to True
    NOTE: All generated nodes and links will have the three attributes below
    Called in ATOM3.py for both links and nodes
    """    
    openFile.write(indent+'self.isGraphObjectVisual = '
      +str(self.isGraphObjectVisual)+"\n")
#    openFile.write(indent+'self.__isHierarchicalLink = '
#      +str(self.__isHierarchicalLink)+"\n")
    #openFile.write(indent+'self._setHierarchicalLink('
    #  +str(self.isHierarchicalLink())+")\n")
    openFile.write(indent+"if(hasattr(self, '_setHierarchicalLink')):\n")
    openFile.write(indent+'  self._setHierarchicalLink('
                          + str(self.isHierarchicalLink())+")\n")
      
    # This is a bit ugly, but remember: it only occurs when you generate code
    # What does it do? If an entity is not a hierarchical link, then it is
    # either a regular link or a node. If it's a node and has a hierarchical
    # link as a direct connection, then we consider this node to be hierarchical
    # in nature. If it's a regular link, this will do nothing...
    if(not self.__isHierarchicalLink):
      allDirectConnections = self.in_connections_ + self.out_connections_
      for entity in allDirectConnections:
        if(entity.__isHierarchicalLink):
          self.__isHierarchicalNode = True
          break
      
    openFile.write(indent+"if(hasattr(self, '_setHierarchicalNode')):\n")
    openFile.write(indent+'  self._setHierarchicalNode('
                          + str(self.isHierarchicalNode())+")\n")
      
#---------------------------------------------- Top layer hierarchy manipulation
  
  def _addNodeToHierarchyTopLayer(self):
    """ 
    When a node is created or a node's children are all removed so it has no
    children, and if the node is hierarchical,
    then it is added to the top layer for quick reference. 
    """
    if(self.__isHierarchicalNode):
      HierarchicalASGNode.hierarchicalTopLayer.append(self)
    
  def _removeNodeFromHierarchyTopLayer(self):
    """ 
    If node is deleted or gains children then remove it from top layer.
    Check first to make sure it is really in the top layer still.
    Called externally in atom3i.deleteRealEntity()
    """
    if(self in HierarchicalASGNode.hierarchicalTopLayer):
      HierarchicalASGNode.hierarchicalTopLayer.remove(self)
    
        