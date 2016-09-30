"""
HyperEdge.py

This is the "master" abstraction of a hyperedge. 
It is further broken down into HyperEdgeComponent (ie: each source/target pair
reached by this hyper-edge is made into a directed edge) and into a HyperNode
(ie: the center drawing of the hyperedge is made into a node). 

This class can be used in its own right to get all the sources/targets of the
hyperedge, however the functionality ends there.

Otherwise, this class can collate information from HyperEdgeComponent's and a
HyperNode to re-generate an AToM3 hyperedge from the layout of the piecemeal
directed edges and node. 

Denis Dube, Sept. 2005
"""

from random import randint

from MathUtilities import vectorLength2D, getMidpoint2D

from AbstractObject import AbstractObject
from AbstractNode import AbstractNode


class HyperEdge(AbstractObject):
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
  SOURCE2CENTER = 0
  CENTER2TARGET = 1
  
  
  
  def __init__(self, semanticObject):    
    """ NOTE: AToM3 dependent method """  
    AbstractObject.__init__(self, semanticObject)
           
    semObj2NodeMap = AbstractNode.SemanticObject2NodeMap
           
    self.__sourceNodeList = []
    for source in semanticObject.in_connections_:      
      self.__sourceNodeList.append(semObj2NodeMap[source])
      
    self.__targetNodeList = []
    for target in semanticObject.out_connections_:      
      self.__targetNodeList.append(semObj2NodeMap[target])
      
      
    # Position and size of the edge's center drawing    
    self.__centerObj = self._obj.getCenterObject()
    if(self.__centerObj):
      box = self.__centerObj.getbbox()
      self._pos = (box[0], box[1])
      self._size = (box[2] - box[0], box[3] - box[1])
    else:
      self._pos = (self._obj.x, self._obj.y)
      self._size = (0, 0)
      
    # Store info for final processing of the hyperedge
    self.__edgeComponent2ControlPointsMap = dict() 
    
    
    
  def getSourceTargetNodeListsTuple(self):
    return (self.__sourceNodeList, self.__targetNodeList)
  
        
    
  def setControlPoints(self, hyperEdgeComponent, controlPoints):
    """
    The hyper-edge component will exactly recieve the given control points
    """
    self.__edgeComponent2ControlPointsMap[hyperEdgeComponent] = controlPoints
   
   
    
  def optimizeLinkComponent(self, hyperEdgeComponent):
    """ 
    Similar to setControlPoints, but here control points will be arbitrarily
    assigned at the drawing phase
    """
    self.__edgeComponent2ControlPointsMap[hyperEdgeComponent] = None
    
    
    
  def applyCoordSizeChange(self):
    """
    Use:
      This method will apply the changed coordinates/size in the abstract graph
      back into the corresponding visual AToM3 entity.
    NOTE: AToM3 dependent method
    """
    # The new (old if it didn't change) center coordinate of the hyperedge
    center = self.__getCenterCoordinate()
    
    # Not all AToM3 hyperedges will have a center drawing
    # Apply changes to the center object's size
    if(self.__centerObj and self._newSize):
      print 'applyCoordSizeChange --> size change not implemented in', \
            __file__
      # self.__centerObj.scaleTo(self._size)
        
    # Apply changes to the center object's position
    if(self._newPos or self._newSize):   
      #dx = self._newPos[0] - self._pos[0]
      #dy = self._newPos[1] - self._pos[1]
      #if(dx != 0 or dy != 0):
        #self._obj.Move(-dx, dy, self._obj.CENTER_SELECTED, moveCenter=False)
      self._obj.moveTo(center[0], center[1], moveCenter=False)
      
      # Do center object seperately. Denis can't figure out Juan De Lara's code
      # so this is a reasonable work-around for that spagetti :p
      if(self.__centerObj):
        self.__centerObj.moveTo(self._newPos[0], self._newPos[1])

    # Optimize the hyperlink segments according to supplied control points or
    # to simple edge routing rules
    if(self.__edgeComponent2ControlPointsMap):
      self.__applyHyperlinkOptimizer(center)
              
    # Raise the hyperedge center drawing above the edge lines
    if(self.__centerObj):
      self._obj.dc.tag_raise(self._obj.tag )
      
      
      
  def __getCenterCoordinate(self):
    """
    Returns:
      The center of the hyperedge drawing (if there is a drawing), using the new
      coordinate (if it exists, if not, then uses the original coordinate).
      If there is no drawing, or the drawing has obscene dimensions, the topleft
      coordinate is returned.
    """
    if(self._newSize):
      size = self._newSize
    else:
      size = self._size
      
    if(self._newPos):
      pos = self._newPos
    else:
      pos = self._pos
      
    if(size[0] != 0 and size[1] != 0):
      return [pos[0] + size[0] / 2, pos[1] + size[1] / 2]
    else:
      return self._pos
    
      
      
  def __applyHyperlinkOptimizer(self, center):
    """
    Use:
      Having modified the abstract graph where everything is represented as 
      directed edges between nodes, we now wish to map the individual directed
      edges back into the hyperedge that exists in AToM3. 
      
      1) We may supply control points to explicitly define where a given segment
      of the hyperedge goes.
      2) We may request a simple edge routing with given curve degree, spline...
      3) Any mixture of the above.
      
    Parameter:
      center is the center coordinate of the hyperedge
      
    NOTE: AToM3 dependent method
    """
    
    baseTag = self._obj.tag
    dc = self._obj.dc
    curveDirectionSeed = randint(0, 1)
        
    for hyperEdgeComponent, controlPoints in \
                                  self.__edgeComponent2ControlPointsMap.items():
            
      source, target = hyperEdgeComponent.getSourceTargetNodeTuple()
      direction, segID = hyperEdgeComponent.getDirectionIDtuple()
      if(controlPoints == None):
        useSplines, curvatureInt = hyperEdgeComponent.getLinkOptimization()
      
      
      # Source object incomming to center of hyperedge
      if(direction == self.SOURCE2CENTER):
        itemHandler = dc.find_withtag(baseTag + "1stSeg" + str(segID))
        sourceObj = source._obj
        targetObj = target._obj
        targetSemObj = target._semanticObject
        curveDirection = curveDirectionSeed
        
#===============================================================================
#     ATTENTION: sourceObj and targetObj are reversed in this case
#===============================================================================
      # Center of hyperedge outgoing to the target object
      else:
        itemHandler = dc.find_withtag(baseTag + "2ndSeg" + str(segID))
        sourceObj = target._obj
        targetObj = source._obj
        targetSemObj = source._semanticObject
        curveDirection = (curveDirectionSeed + 1) % 2
        
      # Make sure everything is kosher here...
      if(not itemHandler):
        print 'WARNING: Cannot optimize hyperedge:', \
              self.getDistinctiveName(), 'because of a missing itemHandler'
        print 'Between:', source.getDistinctiveName(), 'and', \
                          target.getDistinctiveName()
        continue
      elif(not sourceObj.hasConnectors()):
        print 'WARNING: Cannot optimize hyperedge:', \
              self.getDistinctiveName(), 'because of a missing connector port'
        print 'Between:', source.getDistinctiveName(), 'and', \
                          target.getDistinctiveName()
        continue
      
      # dc.find_withtag returns a list, get just the handler
      itemHandler = itemHandler[0] 
    
      # Is it a named port? If so then can't move to another port
      if(sourceObj.isConnectedByNamedPort(targetSemObj)):
        handler = sourceObj.getConnectedByNamedPortHandler(targetSemObj) 
        fromPoint = dc.coords(handler)[:2]
        
      # Snap to the nearest connection port (un-named only)
      else: 
        fromPoint = list(sourceObj.getClosestConnector2Point(sourceObj, 
                                                       center[0], center[1]))

      # We have control points, apply them directly 
      if(controlPoints != None):
        apply(dc.coords, [itemHandler] + fromPoint + controlPoints + center)
        dc.itemconfigure(itemHandler, smooth=True)
        
      # We want a simple curvature, calculate it and apply it
      elif(curvatureInt):        
        v = curvinator(fromPoint, center, curvatureInt, curveDirection)
        extraPoint = getMidpoint2D(fromPoint, center)
        extraPoint = [extraPoint[0] + v[0], extraPoint[1] + v[1]]
        apply(dc.coords, [itemHandler] + fromPoint + extraPoint + center)
        dc.itemconfigure(itemHandler, smooth=useSplines)
        
      # No curvature desired, just a straight line
      else:
        apply(dc.coords, [itemHandler] + fromPoint + center)
        dc.itemconfigure(itemHandler, smooth=useSplines)

      # Check if a link drawing needs moving...
      self._obj.updateDrawingsTo(fromPoint[0], fromPoint[1], itemHandler)
        
        
        
        
#===============================================================================
#Utility methods
#===============================================================================
    
def curvinator( p1, p2, curveAmount, curveDirection ):
  """ 
  Use:
    Returns a vector that is orthongonal to the p1-p2 vector in direction
    curveDirection,  with length curveAmount
  """
  v = [ - ( p1[1] - p2[1] ), p1[0] - p2[0] ]
  d = vectorLength2D( v )
  if( d == 0 ): 
    d = 1
    
  # Direction of the curvature bulge is random
  if( curveDirection == -1 and randint(0, 1) or curveDirection == 1 ): 
    curveAmount = -curveAmount

  # Normalized orthogonal vector times the curvature bulge
  v = ( v[0] * curveAmount / d, v[1] * curveAmount / d  )
  
  return v     
