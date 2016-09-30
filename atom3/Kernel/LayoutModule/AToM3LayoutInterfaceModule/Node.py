"""
Node.py

Denis Dube, Sept. 2005
"""


from AbstractNode import AbstractNode


class Node(AbstractNode):
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
  
  def __init__(self, semanticObject):
    """ NOTE: AToM3 dependent method """
    AbstractNode.__init__(self, semanticObject)
    
    box = self._obj.getbbox()
    self._pos = (box[0], box[1])
    self._size = (box[2] - box[0], box[3] - box[1])
    
    
    
  def isNode(self):
    return True
    
    
    
    
  def applyCoordSizeChange(self):
    """
    Use:
      This method will apply the changed coordinates/size in the abstract graph
      back into the corresponding visual AToM3 entity.
    NOTE: AToM3 dependent method
    """
    if(self._newPos):
      self._obj.moveTo(self._newPos[0], self._newPos[1])
      
      # This makes sure that if the object has hierarchical children, that they
      # are moved as well. This is what we would expect since if you move a
      # container, the contained should move as well.
      if(self._semanticObject and self._semanticObject.isHierarchicalNode()):
        #allChildrenList = self._semanticObject.getAllHierChildren()
        allChildrenList = self._semanticObject.getAllHierChildrenAndArrows()
        dX = self._newPos[0] - self._pos[0]
        dY = self._newPos[1] - self._pos[1]
        for child in allChildrenList:
          #print 'moving', child.name.toString()
          child.graphObject_.Move(dX, dY)

    if(self._newSize):
      print 'applyCoordSizeChange is not implemented', __file__
    