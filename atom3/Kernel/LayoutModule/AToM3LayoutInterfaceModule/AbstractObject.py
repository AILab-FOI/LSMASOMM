"""
AbstractObject.py

Denis Dube, Sept. 2005
"""

import ATOM3String



class AbstractObject:
  
  def __init__(self, semanticObject):  
    """ AToM3 dependent method """    
    self._semanticObject = semanticObject
    self._obj = semanticObject.graphObject_
    
    self._newPos = None
    self._newSize = None
    self._size = None
    self._pos = None
    
    self.__distinctiveName = self.__initDistinctiveName()
    #self.__distinctiveName = "Turn on debug in" + __file__
    

  def applyCoordSizeChange(self):
    """
    Use:
      This method will apply the changed coordinates/size in the abstract graph
      back into the corresponding visual AToM3 entity.
    NOTE: AToM3 dependent method
    """
    raise Exception('Abstract method must be overidden')
      
  
  def setNewCoords(self, coords):
    self._newPos = coords
    
  def getNewCoords(self):
    return self._newPos
    
  def setNewSize(self, size):
    self._newSize = size
    
  def getNewSize(self):
    return self._newSize
    
  def getSize(self):
    return self._size
    
  def getPos(self):
    return self._pos
    
  
  def getDistinctiveName(self):
    """ Public method to get a decent name for the node (use in debugging)"""
    return self.__distinctiveName
    
  def __initDistinctiveName(self):
    """ 
    Entirely for debugging, this returns a decent identifier for the node 
    NOTE: AToM3 dependent method + NON-ESSENTIAL
    """
    # Go through all the attributes to find something distintive
    semObj = self._semanticObject
    distinctiveName = ''
    for attr in semObj.getAttributes():
      attrValue = semObj.getAttrValue(attr)  
      # String attribute... excellent      
      if(attrValue.__class__.__name__ == ATOM3String.__name__):
        valueString = attrValue.getValue().strip('\n')
        if(valueString == ''):
          continue
        else:
          distinctiveName = valueString
          # Oooh, it's a name/Name attribute, very distinctive, take it!
          if(attr.upper() == 'NAME'):
            break
    if(not distinctiveName):
      from AbstractEdge import AbstractEdge
      if(isinstance(self, AbstractEdge)):
        return "NoName_E_X" + str(self._obj.x) + "_Y" + str(self._obj.y)
      return "NoName_X" + str(self._obj.x) + "_Y" + str(self._obj.y)
    return distinctiveName
    
    