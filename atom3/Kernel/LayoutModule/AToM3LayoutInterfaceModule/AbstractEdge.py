"""
AbstractEdge.py

Abstraction of an edge, most methods must be implemented in a subclass

Denis Dube, Sept. 2005
"""

from AbstractObject import AbstractObject


  
class AbstractEdge(AbstractObject):
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
  
  def __init__(self, semanticObject, sourceTargetTuple):  
    """ AToM3 dependent method """    
    AbstractObject.__init__(self, semanticObject)
  
    self.__sourceNode, self.__targetNode = sourceTargetTuple
      
    self._linkOptimizationTuple = None
    self._doApplyControlPoints = False
    
    self._controlPoints = []
    
            
      
      
  def setLinkOptimization(self, useSplines, arrowCurveInt):
    """
    Use:
       Enables/disables simple link optimization (disable with linkOptDict=None)
    
    If an option dictionary is provided, the following key/values are expected:
       'Spline optimization' : booleanFlag
       'Arrow curvature' : integerValue
    """
    if(useSplines == None or arrowCurveInt == None):
      self._linkOptimizationTuple = None
    else:
      self._linkOptimizationTuple = (useSplines, arrowCurveInt)



  def getSourceTargetNodeTuple(self):
    return (self.__sourceNode, self.__targetNode)
    
  
  
#  def getControlPoints(self):
#    return self.controlPoints


  
  def setControlPoints(self, controlPoints):
    """ 
    Use:
      Sets the control points for the edge and automatically requests that they
      be applied to the visual AToM3 edge
    """
    raise Exception("Must be implemented in subclass")
    
    
    
  def applyControlPoints(self):
    """ 
    Use:
      Applies the edge control points to visual AToM3 edge control points
    """    
    raise Exception("Must be implemented in subclass")
    
    
    
  def isDirected(self):
    return False
    
    
    
  def isHyper(self):
    return False      
      

          
  def _reverseCoordList(self, segCoords):
    """ 
    Input: list of coordinates [x0, y0, x1, y1, ..., xn, yn]
    Output: list of coordinates reversed [xn, yn, ..., x1, y1, x0, y0]
    """    
    reversedCoords = []
    for i in range(len(segCoords) - 1, 0, -2):
      reversedCoords += [segCoords[i - 1], segCoords[i]]
    return reversedCoords  
    

  
