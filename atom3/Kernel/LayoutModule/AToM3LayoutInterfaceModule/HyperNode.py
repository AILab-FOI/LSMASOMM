"""
HyperNode.py

This is a hyper-edge center drawing pretending to be a node.

Why you ask? 
Because I want to deal with just two things in life, vertices and directed edges 

Denis Dube, Sept. 2005
"""


import time

from AbstractNode import AbstractNode



class HyperNode(AbstractNode):
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
      
  Inherited from AbstractNode:
    def addChild(self, child): 
    def addParent(self, parent):
    def isNode(self):
    def isHyperNode(self):
    def getChildrenList(self):
    def getParentsList(self):
    def chooseNode(self, possibleChoiceList):
    def updateInternally(self):
  """
        
    
  def __init__(self, semanticObject, hyperEdge):
    """ NOTE: AToM3 dependent method """
    AbstractNode.__init__(self, semanticObject)
    
    # Position and size of the edge's center drawing    
    centerObj = self._obj.getCenterObject()
    if(centerObj):
      box = centerObj.getbbox()
      self._pos = (box[0], box[1])
      self._size = (box[2] - box[0], box[3] - box[1])
    else:
      self._pos = (self._obj.x, self._obj.y)
      self._size = (0, 0)
      
    # The hyperEdge object associated with this centerpoint node
    self.__hyperEdge = hyperEdge
      
  
  
  def isHyperNode(self):
    return True
  
  
    
  def applyCoordSizeChange(self):
    """
    Use:
      This method will apply the changed coordinates/size in the abstract graph
      back into the corresponding visual AToM3 entity.
    NOTE: AToM3 dependent method
    """
    self.__hyperEdge.setNewCoords(self._newPos)
    self.__hyperEdge.setNewSize(self._newSize)
      
  

    
    
  