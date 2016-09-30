"""
Object.py

Created by Denis Dube
Last updated Sept. 2005
"""


class Object:
  """
  A convenient class to store just the information necessary for the 
  application of the force transfer algorithm.
  """
  
  objList = []
  
  def __init__(self, abstractObject, seperationDist):
    self.__abstractObject = abstractObject
    
    width, height = abstractObject.getSize()
    topLeft = abstractObject.getPos()
    self.__centerPos = (topLeft[0] + width / 2, topLeft[1] + height / 2)
        
    if(width <= 1):
      width = 1
    if(height <= 1):
      height = 1
    self.__size = [width, height]
    self.force = [0, 0]
    self.__seperationDist = seperationDist
    #self.__distance = math.sqrt(center[0]*center[0] + center[1]*center[1])
  
    Object.objList.append(self)
    
  def getSeperationDistance(self):
    return self.__seperationDist
        
  def getSize(self):
    return self.__size
  
  def getCoords(self):
    """ 
    Returns top-left coordinate 
    NOTE: Can't just use self.__abstractObject.getPos() because we have modified
    self.__centerPos over the course of the FTA simulation, but have not yet 
    updated the abstractObject with applyNewCoords()!
    """
    return (self.__centerPos[0] - self.__size[0] / 2, 
            self.__centerPos[1] - self.__size[1] / 2)
    
  def getCenter(self):
    """ Returns object center coordinate """
    return self.__centerPos
    
  def forceIncrement(self, force):
    self.force = force
       
  def commitForceApplication(self):
    """
    Use:
      Updates object position using the x, y force components, then resets the
      force.
    """
    self.__centerPos = [self.__centerPos[0] + self.force[0], 
                        self.__centerPos[1] + self.force[1]]
    self.force = [0, 0] 
    
  def recenteringPush(self, force):
    """ Puts the object back onto the canvas if it got forced off """
    self.__centerPos = [self.__centerPos[0] + force[0], 
                        self.__centerPos[1] + force[1]]
      
  def applyNewCoords(self):
    """
    Use:
      Applies the new coordinates in the abstract graph
    """
    self.__abstractObject.setNewCoords(self.getCoords())

  def __str__(self):
    return self.__abstractObject.getDistinctiveName()