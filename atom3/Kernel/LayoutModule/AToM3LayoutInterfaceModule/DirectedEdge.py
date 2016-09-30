"""
DirectedEdge.py

Denis Dube, Sept. 2005
"""

from random import randint

from MathUtilities import distance
from Utilities import optimizeRegularLink

from AbstractEdge import AbstractEdge

    
class DirectedEdge(AbstractEdge):
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
  
  def __init__(self, semanticObject, sourceTargetTuple):  
    """ NOTE: AToM3 dependent method """  
    AbstractEdge.__init__(self, semanticObject, sourceTargetTuple)    
        
    # Position and size of the edge's center drawing    
    centerObj = self._obj.getCenterObject()
    if(centerObj):
      box = centerObj.getbbox()
      self._pos = (box[0], box[1])
      self._size = (box[2] - box[0], box[3] - box[1])
    else:
      self._pos = (self._obj.x, self._obj.y)
      self._size = (0, 0)
    
    
    
  
  def applyCoordSizeChange(self):
    """
    Use:
      This method will apply the changed coordinates/size in the abstract graph
      back into the corresponding visual AToM3 entity.
    NOTE: AToM3 dependent method
    """
    # Move the object to the new coordinates
    # NOTE: in AToM3 this makes sense, since many edges have an edge drawing
    # in the center which is worth moving.
    if(self._newPos):
      self._obj.moveTo(self._newPos[0], self._newPos[1])
      
    # Resize the object
    # NOTE: this doesn't mean edge thickness, but the edge drawing size
    if(self._newSize):
      print 'applyCoordSizeChange is not implemented', __file__
    
    
    # Do direct control point application to the edge
    if(self._doApplyControlPoints):
      self.applyControlPoints()
    
    # Do a edge optimization (ie: draw the spline nicely)
    elif(self._linkOptimizationTuple):
      doSpline, arrowCurveInt = self._linkOptimizationTuple
      source, target = self.getSourceTargetNodeTuple()   
         
      optimizeRegularLink(self._obj.dc, self._obj, source._obj, target._obj, 
                          doSpline, arrowCurveInt, 0) #randint(0,1))
    

  
  def isDirected(self):
    return True
    
    
    
  def initilizeControlPoints(self):
    """ 
    Control points should be points the edge passes through between two nodes
    This should NOT include the "AToM3" center of the edge point
    """
    '''
    dc = self._obj.dc    
    inboundCoords = dc.coords(self._obj.in_connections_[0][1])[2:-2]     
    outboundCoords = dc.coords(self._obj.out_connections_[0][1])[2:-2]
  
    # To make things complicated AToM3 reverses outbound coords
    outboundCoords = self._reverseCoordList(outboundCoords)
    
    self._controlPoints = inboundCoords + outboundCoords
    '''
    raise Exception("Please uncomment this method, it is ready to use")


  def getControlPoints(self):
    '''
    return self._controlPoints
    '''
    raise Exception("Please uncomment this method, it is ready to use")
    

  
  def setControlPoints(self, controlPoints):
    """ 
    Use:
      Sets the control points for the edge and automatically requests that they
      be applied to the visual AToM3 edge
    """
    self._controlPoints = controlPoints
    self._doApplyControlPoints = True
    
    
    
    
  def applyControlPoints(self):
    """ 
    Use:
      Applies the edge control points to visual AToM3 edge control points
    """    
    controlPoints = self._controlPoints
    numPoints = len(controlPoints) / 2
    inPoint, outPoint = getPointOnConnectNode(self, controlPoints)
    
    # Add 1 or 2 extra control points for odd case (to make splines nice)
    if(numPoints % 2 == 1):
    
      # Example: controlPoints = [x0, y0]
      if(numPoints == 1):
        center = controlPoints        
        midpoint1 = [center[0] + (inPoint[0] - center[0]) / 10,
                     center[1] + (inPoint[1] - center[1]) / 10]
        midpoint2 = [center[0] - (center[0] - outPoint[0]) / 10,
                     center[1] - (center[1] - outPoint[1]) / 10]
        # Re-calculate center (note: not faithful to original coords)
        center = [midpoint1[0] - (midpoint1[0] - midpoint2[0]) / 2,
                  midpoint1[1] - (midpoint1[1] - midpoint2[1]) / 2]
         
        controlPoints = midpoint1 + center + midpoint2 
        centerIndex = numPoints + 1
        
      # Example: controlPoints = [x0, y0, x1, y1, x2, y2] or more points
      else:
        start = controlPoints[:numPoints + 1]
        end = controlPoints[numPoints + 1:]

        center = [start[-2] + (end[0] - start[-2]) / 2, 
                  start[-1] + (end[1] - start[-1]) / 2]
           
        controlPoints = start + center + end 
        centerIndex = numPoints - 1 + 2

    
    # Add 1 extra control point for even case (to make splines nice)
    else:
      start = controlPoints[:numPoints]
      end = controlPoints[numPoints:]
      center = [start[-2] + (end[0] - start[-2]) / 2, 
                start[-1] + (end[1] - start[-1]) / 2]
      controlPoints = start + center + end          
      centerIndex = numPoints
      
      
    # Now I know where the center is... so lets move the center object
    self._obj.moveTo(center[0], center[1])
    
    # Go through the 2 segments in the link
    dc = self._obj.dc
    for connTuple in self._obj.connections:
      itemHandler = connTuple[0]
      direction = connTuple[1]
      
      # Link direction is source to center
      if(direction):   
        segCoords = inPoint + controlPoints[:centerIndex+2]
        
      # Link directin is center to target
      else:           
        segCoords = controlPoints[centerIndex:] + outPoint
        segCoords = self._reverseCoordList(segCoords)
  
      # Applies the changed coords to the canvas
      dc.coords( * [itemHandler] + segCoords )    
      
      # Use splines or straight line segments?
      dc.itemconfigure(itemHandler, smooth=self._linkOptimizationTuple[0])
      
      # This may change the associated link drawings: 
      # move them to the new point 
      if( direction ):
        self._obj.updateDrawingsTo(inPoint[0], inPoint[1], itemHandler, 
                                                      segmentNumber=1)
      else:
        self._obj.updateDrawingsTo(outPoint[0], outPoint[1], itemHandler, 
                                                        segmentNumber=2) 
    
      
      
#===============================================================================
#Utility methods
#===============================================================================
      
            
def getPointOnConnectNode(directedEdge, controlPoints):
  """
  Use:
    Get a coordinate of a connection port on the source/target node of the edge
  """
  
  pointA = controlPoints[:2]
  pointB = controlPoints[-2:]
  
  source, target = directedEdge.getSourceTargetNodeTuple()
  sourceObj = source._obj
  targetObj = target._obj
  #edgeObj = directedEdge._obj
  edgeSemObj = directedEdge._semanticObject
  dc = sourceObj.dc
    
  # Is sourceObj connected to a named port!?!
  if(sourceObj.isConnectedByNamedPort(edgeSemObj)):
    handler = sourceObj.getConnectedByNamedPortHandler(edgeSemObj) 
    coordA = dc.coords(handler)[:2]
      
  # Not a named port...
  else:
    coordA = sourceObj.getClosestConnector2Point(sourceObj, pointA[0], pointA[1])
  
  # Is targetObj connected to a named port!?!
  if(targetObj.isConnectedByNamedPort(edgeSemObj)):
    handler = targetObj.getConnectedByNamedPortHandler(edgeSemObj) 
    coordB = dc.coords(handler)[:2]
      
  # Not a named port...
  else:
    coordB = targetObj.getClosestConnector2Point(targetObj, pointB[0], pointB[1])
  
  return (list(coordA), list(coordB))
  
      


  
  