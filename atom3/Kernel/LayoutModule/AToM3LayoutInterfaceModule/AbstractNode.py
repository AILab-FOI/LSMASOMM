"""
AbstractNode.py

Denis Dube, Sept. 2005
"""


import time

from AbstractObject import AbstractObject



class AbstractNode(AbstractObject):
  """
  Inherited from AbstractObject:
    self._semanticObject
    self._obj    
    self._newPos
    self._newSize

    def applyCoordSizeChange(self):  <ABSTRACT>
    def setNewCoords(self, coords):
    def getNewCoords(self):
    def setNewSize(self, size):
    def getNewSize(self):
    def getSize(self):
    def getPos(self):
    def getDistinctiveName(self):    
  """
  SemanticObject2NodeMap = dict()
        
    
  def __init__(self, semanticObject):
    """ NOTE: AToM3 dependent method """
    AbstractObject.__init__(self, semanticObject)
    
    AbstractNode.SemanticObject2NodeMap[semanticObject] = self
       
    self.__children = []
    self.__parents = []
    

    
  def addChild(self, child):
    self.__children.append(child)
    
    
    
  def addParent(self, parent):
    self.__parents.append(parent)
  
  
  
  def isNode(self):
    return False
    
    
    
  def isHyperNode(self):
    return False
 
 
    
  def getChildrenList(self):
    return self.__children
    
    
    
  def getParentsList(self):
    return self.__parents
    
    
  
  def chooseNode(self, possibleChoiceList):
    """
    Use:
      Allows the user to manually choose a node by clicking on it in the drawing
      tool. 
    Parameter:
      possibleChoiceList, a list of objects of type Node
    Returns:
      An index value into possibleChoiceList
    NOTE: AToM3 dependent method + NON-ESSENTIAL
    """
    atom3i = self._semanticObject.parent
    cb = atom3i.cb
    cb.clearSelectionDict()  
    
    # Make sure we don't choose a hyper edge node
#    possibleChoiceList = filter(lambda x: x.isNode(), possibleChoiceList)
    possibleChoiceList = [node for node in possibleChoiceList if node.isNode()]
     
    # Makes a special list of the cycle nodes, highlight them on the canvas
    matchList = []
    for node in possibleChoiceList:
      node._obj.HighLight(1)
      matchList.append([0, [node._obj.semanticObject]])
          
    # Initilize the choosing system. Special behaviour mode in statechart
    # This means that the user MUST choose a node, nothing else will work
    no_value_yet = -1
    cb.initMatchChoice( no_value_yet, matchList )
    atom3i.UI_Statechart.event("GG Select", None)  
                
    # Now we wait for the user to click somewhere, polling style    
    while(cb.getMatchChoice() == no_value_yet ):        
      time.sleep( 0.1 ) # Time in seconds
      atom3i.parent.update()      
    
    # Clean up the highlighting
    for node in possibleChoiceList:
      node._obj.HighLight(0) 
      
    return cb.getMatchChoice()
    
    

  def updateInternally(self):
    """
    Internally pushes the "new position" found by a layout to the "original" 
    position found on the canvas. This makes it possible to do multiple layout
    calls without drawing to the canvas.
    """
    self._pos = self._newPos
    self._newPos = None
    
