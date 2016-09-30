"""
HyperEdgeComponent.py

This is a component of a hyper edge which can be treated as a directed edge

Why you ask? 
Because I want to deal with just two things in life, vertices and directed edges

Denis Dube, Sept. 2005
"""

from AbstractEdge import AbstractEdge

class HyperEdgeComponent(AbstractEdge):
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
      
  Inherited from AbstractEdge:
    self._linkOptimizationTuple 
    self._doApplyControlPoints 
    self._controlPoints
      
    def setLinkOptimization(self, useSplines, arrowCurveInt):
    def getSourceTargetNodeTuple(self):
    def setControlPoints(self, controlPoints):  <ABSTRACT>
    def applyControlPoints(self):  <ABSTRACT>
    def isDirected(self):
    def isHyper(self):          
    def _reverseCoordList(segCoords):
  """
  SOURCE2CENTER = 0
  CENTER2TARGET = 1
  
  def __init__(self, semanticObject, sourceTargetTuple, hyperEdge, 
               direction, segmentID):    
    """ NOTE: AToM3 dependent method """  
    AbstractEdge.__init__(self, semanticObject, sourceTargetTuple)
            
    # Position and size of the edge's center drawing    
    sourceNode, targetNode = sourceTargetTuple
    sourceX, sourceY = sourceNode.getPos()
    targetX, targetY = sourceNode.getPos()
    self._pos = (sourceX + (targetX - sourceX) / 2,
                 sourceY + (targetY - sourceY) / 2)
    self._size = (0, 0)
    
    # The direction of this hyperedge component 
    # Example: source to center or center to target
    self.__direction = direction
    
    # Identifier of where this hyperedge component fits into bigger picture
    self.__segmentID = segmentID

    # The hyperEdge object associated with this hyperedge component
    self.__hyperEdge = hyperEdge



  def getDirectionIDtuple(self):  
    return (self.__direction, self.__segmentID)
    

  
  def getLinkOptimization(self):
    return self._linkOptimizationTuple



  def applyCoordSizeChange(self):
    """
    Use:
      This method will apply the changed coordinates/size in the abstract graph
      back into the corresponding visual AToM3 entity.
    NOTE: AToM3 dependent method
    """
      
    # NOTE: ignoring new position and new size attributes, they don't make much
    #       sense in this context
    
    # Do direct control point application to the edge
    if(self._doApplyControlPoints):
      self.applyControlPoints()
      
    # Do a edge optimization (ie: draw the spline nicely)
    elif(self._linkOptimizationTuple):
      #doSpline, arrowCurveInt = self._linkOptimizationTuple
      #cb = self._semanticObject.parent.cb
      #optimizeLinks(cb, doSpline, arrowCurveInt, [self._obj])
      self.__hyperEdge.optimizeLinkComponent(self)
    
      
      
  
  def setControlPoints(self, controlPoints):
    """ 
    Use:
      Sets the control points for the edge and automatically requests that they
      be applied to the visual AToM3 edge
    """
    if(self.__direction == self.SOURCE2CENTER):
      self._controlPoints = controlPoints
    else:
      # Must reverse the coordinates for the 2nd segment of AToM3 arrows
      self._controlPoints = self._reverseCoordList(controlPoints)
    self._doApplyControlPoints = True
    
        
    
  def applyControlPoints(self):
    """ 
    Use:
      Applies the edge control points to visual AToM3 edge control points
    """    
    self.__hyperEdge.setControlPoints(self, self._controlPoints)
    
    
        
  def isHyper(self):
    return True      
      
  
  
  