"""
CircleLayout.py

Arranges selected entities in a simple circle, possibly setting the stage for
spring layout.

Created Summer 2005, Denis Dube
"""

# @param entities
# @param forceRadius
# @param minNodeSeperation
# @param antiOverlap

import math
import sys

from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog
from Utilities            import optimizeLinks
from ModelSpecificCode    import isConnectionLink

def applyLayout( atom3i = None, settings = False, selection = None ):
  
   # Instantiate the layout algorithm, if not already done  
  if( CircleLayout.instance == None ):
    if( atom3i == None ):   
      raise Exception, "You forgot to initilize "+__name__+" before using it!"
    CircleLayout.instance = CircleLayout(atom3i)    
  
  if( atom3i ):
    CircleLayout.instance.updateATOM3instance( atom3i )
  
  if( settings ):
    CircleLayout.instance.settings( selection ) 
  else:    
    CircleLayout.instance.main( selection )     

    
class CircleLayout:

  instance = None

  
  def __init__(self, atom3i ):
     
    self.cb = atom3i.cb
    self.atom3i = atom3i

    # Instantiate the Option Database module
    self.__optionsDatabase = OptionDatabase( atom3i.parent,
                    'Options_CicleLayout.py', 'Circle Layout Configuration')
    
    # Local methods/variables with short names to make things more readable :D
    newOp = self.__optionsDatabase.createNewOption
    IE = OptionDialog.INT_ENTRY
    BE = OptionDialog.BOOLEAN_ENTRY
      
    # Create New Options
    # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
    
    optionList = [OptionDialog.LABEL, "Times 12", "blue", "left" ]
    
    newOp( 'label0001', None, optionList, 'Node positioning', '' )
    newOp( 'Origin', False, BE, "Start circle at origin?", 
        "If false, the current position of the selected nodes is used" )   
    newOp( 'Offset', 20, IE, "Minimum node spacing", 
        "Minimum distance between any 2 tree nodes (Default 20)" ) 
    
    newOp('sep0000', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
    newOp('label0003', None, optionList, 'Arrow post-processing options', '')
        
    newOp( 'Spline optimization' , True, BE, "Spline optimization", 
        "Sets the arrow to smooth mode and adds 2 extra control points" )
    newOp( 'Arrow curvature', 10, IE, "Arrow curvature", 
        "Adds a curve of magnitude X to the arrows, "
        +"set to 0 for a straight arrow." )    
        
     
    # Load the options from the file, on failure the defaults above are used.
    self.__optionsDatabase.loadOptionsDatabase()
  
  
  
  def updateATOM3instance( self, atom3i ):
    """ Possible to have multiple instances of atom3 """
    self.cb = atom3i.cb 
    self.atom3i = atom3i   
   
   
   
  def settings( self, selection ):
    """
    Dialog to interactively change the spring's behavior
    Automatically applies layout if not canceled
    """
    if( self.__optionsDatabase.showOptionsDatabase() ):
      self.main( selection )
    
    
    
  def main( self, selection ): 
    
    setSmooth    = self.__optionsDatabase.get('Spline optimization')   
    setCurvature = self.__optionsDatabase.get('Arrow curvature') 
        
    entityNodeList = self.__getEntityList(selection)
    if(len(entityNodeList) == 0):
      return
    self.__positionNodes(entityNodeList)
    
    optimizeLinks( self.cb, setSmooth, setCurvature, 
                  selectedLinks=self.__getLinkList(entityNodeList) )



  def __getLinkList(self, entityNodeList):
    """
    Find all links disturbed by the circle layout algorithm
    """
    linkList = []    
    for obj in entityNodeList:
      semObject = obj.semanticObject
      linkNodes = semObject.in_connections_ + semObject.out_connections_
      for semObj in linkNodes:
        if(semObj.graphObject_ not in linkList):
          linkList.append(semObj.graphObject_)
    return linkList

   
    
  def __getEntityList(self, selection):
    """
    If selection is empty, get all nodes on the canvas
    Else filter out links
    """
    entityNodeList = []
    
    # Selection may contain a mixed bag of nodes and links
    if(selection):
      for node in selection:
        if(not isConnectionLink(node)):          
          entityNodeList.append(node)
          
    # No selection? Grab all nodes in diagram
    else:
      if(not self.atom3i.ASGroot):
        return []
      for nodetype in self.atom3i.ASGroot.nodeTypes:  
        for node in self.atom3i.ASGroot.listNodes[nodetype]:      
          if(not isConnectionLink(node.graphObject_)):  
            entityNodeList.append(node.graphObject_)
 
    return entityNodeList
    
    
    
  def __computeCircleRadius(self, entityNodeList):
    """
    Takes a list of entity nodes, computes the perimeter they will occupy and
    resulting radius of circle required
    """  
    # Compute radius automatically
    # Line up all the nodes diagonally (or max of H and W), count length
    # Use eqution: perimeter = 2*pi*r to get radius
    offset = self.__optionsDatabase.get('Offset')     
    perimeter = 0  
    for node in entityNodeList:
      perimeter += max(node.getSize()) + offset
    return (perimeter, perimeter / (2 * math.pi))
    
    
    
  def __positionNodes(self, entityNodeList):
    """
    Position the nodes
    """
    useOrigin = self.__optionsDatabase.get('Origin') 
    if(useOrigin):
      baseX = 0
      baseY = 0
    else:
      (baseX, baseY) = self.__getMaxUpperLeftCoordinate(entityNodeList)
      
    # Compute circle positions
    # Angle per step = 2*pi / # of nodes
    # For each node: 
    # positionX[i] = r + r * sin(i * anglePerStep)
    # positionY[i] = r + r * cos(i * anglePerStep)
    (perimeter, radius) = self.__computeCircleRadius(entityNodeList)    
    anglePerStep = (2.0 * math.pi) / float(len(entityNodeList))

    for i in range(0, len(entityNodeList)):
      x = baseX + radius + radius * math.sin(i * anglePerStep)
      y = baseY + radius + radius * math.cos(i * anglePerStep)
      entityNodeList[i].moveTo(x, y)
    
    
    
  def __getMaxUpperLeftCoordinate(self, entityNodeList):
    """ 
    Returns the maximum upper left coordinate of all the nodes the layout is
    being applied to
    This corresponds to the minumum x and y coords of all the nodes
    """
    minX = sys.maxint
    minY = sys.maxint
    for node in entityNodeList:
      if(node.y < minY):
        minY = node.y
      if(node.x < minX):
        minX = node.x 
    return (minX, minY)
