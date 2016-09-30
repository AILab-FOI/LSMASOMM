"""
ForceTransfer.py

Applies force to all nodes that are too close to each other
Loops until a stable configuration is reached
Times out after 50 iterations, to avoid depriving the user of interactivity for too long.

Distance specifies how far apart you want your nodes
Force constant determines how much force (and how quickly) is applied
Animation time slows down the process so that it can be visualized
Max animation iteration cuts off the animation to save time

Performance:
  I tried sorting the nodes along an axis, but it didn't give me any noticable
  performance benefits. I suspect I did something wrong because it should have
  reduced the number of iterations required to find a stable layout. To be
  investigated in greater detail...
  
Animation:
  Would be better if the final positions of the objects was computed without
  moving them. Then animate the movement from the starting position to the final
  position. 
      
Overhauled June 29, 2004 by Denis Dube
"""

import math, time
from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog
from Utilities            import optimizeConnectionPorts
from ModelSpecificCode    import isConnectionLink

def applyLayout( atom3i = None, settingsMode = False, selection = None,
                                                   initilizeOnly = False ):
  """ Applies a force transfer algorithm to prevent node overlap """
  
  # Instantiate the layout algorithm, if not already done  
  if( ForceTransfer.instance == None ):
    if( atom3i == None ):   
      raise Exception, "You forgot to initilize ForceTransfer.py before using it!"
    ForceTransfer.instance = ForceTransfer( atom3i )    
  if( initilizeOnly ):  return
  
  if( atom3i ):
    ForceTransfer.instance.updateATOM3instance( atom3i )
    
  if( settingsMode ):
    ForceTransfer.instance.settings( selection ) # Change FTA parameters
  else:    
    ForceTransfer.instance.main( selection )  # Apply FTA


class ForceTransfer:
  
  instance = None
  
  MIN_NODE_DISTANCE       = 'Minimum node distance'
  MIN_LINK_DISTANCE       = 'Minimum link distance'
  MIN_CONTROL_DISTANCE    = 'Minimum control point distance'
  SEPERATION_FORCE        = 'Seperation Force'
  ANIMATION_TIME          = 'Animation Time Updates'
  MAX_ANIM_ITERATIONS     = 'Max Animation Iterations'
  MAX_TOTAL_ITERATIONS    = 'Max Total Iterations'
  USE_STATUSBAR           = 'Use Statusbar'
  AUTO_APPLY              = 'Auto apply'
  BORDER_DISTANCE         = 'Border Distance'
  
  def __init__(self, atom3i ):
    
    self.atom3i = atom3i            # AToM3 instance
    self.dc = self.atom3i.UMLmodel  # Canvas
    
    # Instantiate the Option Database module
    self.__optionsDatabase = OptionDatabase(self.atom3i.parent,
                    'Options_ForceTransfer.py', 'Force Transfer Configuration')
    
    # Local methods/variables with short names to make things more readable :D
    newOp = self.__optionsDatabase.createNewOption
    IE = OptionDialog.INT_ENTRY
    FE = OptionDialog.FLOAT_ENTRY
    BE = OptionDialog.BOOLEAN_ENTRY
    LA = OptionDialog.LABEL
    
    # Create New Options
    # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
    optionList = [ LA, "Times 12", "blue", "left" ]
    newOp( 'label0', False, optionList, "\nThis algorithm is applied only to selected "+
          "nodes.\nHowever, if no nodes are selected it is applied globally.\n")
    newOp( self.AUTO_APPLY, False, BE, "Always active", 
        "Runs force transfer whenever a node is added/dragged in the model" )
    newOp( self.USE_STATUSBAR, False, BE, "Enable statusbar info", 
        "Shows number of iterations used to find stable configuration in the statusbar" ) 
    newOp( self.MIN_NODE_DISTANCE, 20, IE, "Minimum node seperation", 
        "Node entities will be seperated by a minimum of this many pixels")        
    newOp( self.MIN_LINK_DISTANCE, 20, IE, "Minimum link node seperation", 
        "Distance in pixels that link nodes should be seperated from other nodes")
    newOp( self.MIN_CONTROL_DISTANCE, 20, IE, "Minimum link control point seperation", 
        "Distance that link control points should be seperated from other nodes")        
    newOp( self.SEPERATION_FORCE, 0.2, FE, "Seperation force",
        "Magnitude of the force that will seperate overlapping nodes")
    newOp( self.ANIMATION_TIME, 0.01, FE, "Animation time",
        "Seconds between animation frame updates, set 0 to disable animations" )
    newOp( self.MAX_ANIM_ITERATIONS, 15, IE, "Max animation iterations",
        "Stop updating animation to screen after max iterations to speed process up")
    newOp( self.MAX_TOTAL_ITERATIONS, 50, IE, "Max total iterations",
        "Stop iterating, even if stable configuration not reached, to prevent unreasonably long periods of non-interactivity")
    newOp( self.BORDER_DISTANCE, 30, IE, "Border distance",
        "If an entity is pushed off the canvas, the canvas will be re-centered plus this pixel offset to the top left")

    # Load the options from the file, on failure the defaults will be returned.
    self.__optionsDatabase.loadOptionsDatabase()
    self.__processLoadedOptions()
 
    
  def __processLoadedOptions(self):
    """ After loading the database, have to get & store each option value """
      
    self.__autoApply            = self.__optionsDatabase.get(self.AUTO_APPLY)  
    self.__useStatusBar         = self.__optionsDatabase.get(self.USE_STATUSBAR)  
    self.__minNodeDist          = self.__optionsDatabase.get(self.MIN_NODE_DISTANCE)  
    self.__minLinkDist          = self.__optionsDatabase.get(self.MIN_LINK_DISTANCE)  
    self.__minControlDist       = self.__optionsDatabase.get(self.MIN_CONTROL_DISTANCE)  
    self.__seperationForce      = self.__optionsDatabase.get(self.SEPERATION_FORCE)  
    self.__animationTime        = self.__optionsDatabase.get(self.ANIMATION_TIME)  
    self.__maxAnimIterations    = self.__optionsDatabase.get(self.MAX_ANIM_ITERATIONS)  
    self.__maxIterations        = self.__optionsDatabase.get(self.MAX_TOTAL_ITERATIONS)  
    self.__borderDistance       = self.__optionsDatabase.get(self.BORDER_DISTANCE) 
        
    # Inform AToM3 that it should call this algorithm whenever a node is
    # added or dragged
    if( self.__autoApply ):
      self.atom3i.isAutoForceTransferEnabled = True
    else:
      self.atom3i.isAutoForceTransferEnabled = False
    
  def updateATOM3instance( self, atom3i ):
    """ Possible to have multiple instances of atom3 """
    self.atom3i = atom3i            # AToM3 instance
    self.dc = self.atom3i.UMLmodel  # Canvas  
    
  def settings(self, selection):
    """ Show the dialog, load the options, transfer some force! """    
    if( self.__optionsDatabase.showOptionsDatabase() ):
      self.__processLoadedOptions()

            
  def main(self, selection):

    Object.objList = []
    atom3i = self.atom3i
    dc = self.dc

    # Specific objects have been chosen on the canvas
    if( selection ):
        for obj in selection:
            self.__grabInfoFromGraphicalObject( obj )          
        
    # Nothing on canvas selected, do all!
    else:
   
      # Grab all the nodes in the diagram, except those with 0 size (arrows)
      # Store them in the "nodeObject" and reference them by objList
      for nodetype in atom3i.ASGroot.nodeTypes:	
        for node in atom3i.ASGroot.listNodes[nodetype]:        
          obj =   node.graphObject_
          #print obj
          self.__grabInfoFromGraphicalObject( obj )  

                
    self.__totalNodes = len( Object.objList )  
    
    #self.__sortNodes()     
    
    # Trivial non-overlap case
    if( self.__totalNodes <= 1 ):
      return
    
    self.__isLayoutStable = False
        
    # Keep at it till the layout is stable
    i = 0
    while( not self.__isLayoutStable ):
      self.__isLayoutStable = True # Optimism is good...
      self.__calculationLoop()
      
      # Disgusting: I have to actually sleep, otherwise I'll be done so fast
      # you won't have even seen it move :p
      if( self.__animationTime and i < self.__maxAnimIterations):
        self.dc.update_idletasks()
        time.sleep(self.__animationTime)  
        
      if( i > self.__maxIterations ):   break
      i += 1
      
      
    # Hijack the status bar to show what the FTA is doing...
    if( self.__useStatusBar ):
      if( i >= self.__maxIterations ):
        atom3i.statusbar.set(1,"FTA halted at max iterations, layout unstable",None)
      else:
        atom3i.statusbar.set(1,"FTA needed "+str(i)+" iterations to find stable layout",None)

    # Keep the whole thing in the viewable area of the canvas
    minY = minX = 10000
    for node in Object.objList:
      if( isinstance( node, NodeObject ) ):
        x,y = node.getTopLeftPos()
      else:
        x,y = node.getCoords()
      if( x < minX ): minX = x
      if( y < minY ): minY = y
      
    if( minX < self.__borderDistance ):
      minX = abs(minX) + self.__borderDistance
    else:
      minX = 0
    if( minY < self.__borderDistance ):
      minY = abs(minY) + self.__borderDistance
    else:
      minY = 0
   
    # Push on it!
    for node in Object.objList:
      node.recenteringPush(minX, minY )
      
    # All that moving stuff around can mess up the connections...
    if( selection ):
        optimizeConnectionPorts(atom3i, entityList=selection )
    else:
        optimizeConnectionPorts(atom3i, doAllLinks=True )
      
  
  def __grabInfoFromGraphicalObject( self, obj ):
          """ Takes a graphical object and stores relevent info in a data structure """
      
          # This be a node/entity object
          if( not isConnectionLink( obj ) ):
            
            try: 
              x0,y0,x1,y1 = obj.getbbox()  
              width  = abs( (x0 - x1) )
              height = abs( (y0 - y1) )
              center = [ x0 + width/2, y0 + height/2 ]
            except:
              print "ERROR caught and handled in ForceTransfer.py in __grabInfoFromGraphicalObject"
              width = 4
              height = 4
              center = [obj.x, obj.y]
              x0 = obj.x - 2
              y0 = obj.y - 2
                          
            NodeObject( obj, center, [width,height], self.__minNodeDist, topLeftPos = [x0,y0] )
                    
          # This be a link/edge object
          elif( self.__minLinkDist > 0 ) :
          
            # Treat the link center as a repulsive object
            EdgeObject( obj, obj.getCenterCoord(), self.__minLinkDist )
          
            # Treat each control point as a repulsive object
            if( self.__minControlDist > 0 ):
              
              if( not self.dc ): return
              for connTuple in obj.connections:
                itemHandler = connTuple[0]
                c = self.dc.coords( itemHandler )    
                for i in range(2,len(c)-2,2): 
                  ControlPoint( c[i:i+2], self.__minControlDist, itemHandler, i, self.dc )
    
    
  def __sortNodes(self):
    """ 
    Sorts the nodes according to their distance from the origin (0,0) 
    This can have a large impact on performance, especially as the number
    of objects in contact with one another goes up.
    """
    
    sortedList = []
    for node in Object.objList:
      sortedList.append( (node.getDistanceFromOrigin(),node) )
  
    sortedList.sort()
    Object.objList = []
    for x,node in sortedList:
      Object.objList.append( node )
            
  def __calculationLoop(self):
    """ Loop through all the nodes """
    
    # Go through all the nodes, and find the overlap forces
    i = 0
    j = 1
    while( i < self.__totalNodes ):
      while( j < self.__totalNodes ):
        if( i != j ):      
          self.__forceCalculation( Object.objList[i], \
                                   Object.objList[j] )
        j+=1
      i += 1
      j = i
      
    # Go through all the nodes and apply the forces to the positions
    for node in Object.objList:
      node.commitForceApplication()
      
      
  def __forceCalculation(self, n1,n2 ):
    """
    Evaluates distances betweens nodes (ie: do they overlap) and
    calculates a force sufficient to pry them apart.
    """
    
    # Absolute distance along X and Y vectors between the nodes
    pointA = n1.getCoords()
    pointB = n2.getCoords()
 
    dx = abs( pointB[0] - pointA[0] ) 
    dy = abs( pointB[1] - pointA[1] ) 
    
    # Zero division error prevention measures
    if (dx == 0.0 ):      dx = 0.1
    if( dy == 0.0 ):      dy = 0.1
    
    # Node-Node Distances
    dist = math.sqrt(dx*dx+dy*dy)
    
    # Normalized-Vector
    norm = [ dx / dist , dy / dist ]

    # Overlap due to size of nodes
    sizeA = n1.getSize()
    sizeB = n2.getSize()
    sizeOverlap = [ ( sizeA[0] + sizeB[0] ) / 2 , ( sizeA[1] + sizeB[1] ) / 2 ]  
    
    # Desired distance with resulting force
    minSeperationDist = min( n1.getSeperationDistance(),n2.getSeperationDistance() )
    d1 = (1.0 / norm[0]) * (sizeOverlap[0] + minSeperationDist)
    d2 = (1.0 / norm[1]) * (sizeOverlap[1] + minSeperationDist)
    forceMagnitude = self.__seperationForce * ( dist - min(d1,d2) )
  
    # The force should be less than -1 (or it won't be having much of an effect)
    if (forceMagnitude < -1):     
      #print forceMagnitude, dist, d1,d2 , (sizeOverlap[0] + minSeperationDist),(sizeOverlap[1] + minSeperationDist),(1.0 / norm[0]),(1.0 / norm[1])
      force = [ forceMagnitude * norm[0],  forceMagnitude * norm[1] ]
      
      # Maximize compactness by only pushing nodes along a single axis
      if( force[0] > force[1] ):   force[0] = 0
      else:                        force[1] = 0
      
      # Determine the direction of the force
      direction = [ 1, 1 ]
      if( pointA[0] > pointB[0] ): direction[0] = -1
      if( pointA[1] > pointB[1] ): direction[1] = -1
  
      # Add up the forces to the two interacting objects
      n1.forceIncrement( [  direction[0] * force[0],  direction[1] * force[1] ] )
      n2.forceIncrement( [ -direction[0] * force[0], -direction[1] * force[1] ] )
      
      # If a force was applied this iteration, definately not stable yet
      self.__isLayoutStable = False      
      
class Object:
  """
  A convenient class to store just the information necessary for the 
  application of the force transfer algorithm.
  """
  
  objList = []
  
  def __init__(self, graphObject, pos, size, seperationDist):
    self.__graphObject = graphObject
    self.pos = pos
    self.__size = size
    self.force = [0,0]
    self.__seperationDist = seperationDist
    self.__distance = math.sqrt( pos[0]*pos[0] + pos[1]*pos[1] )
  
    Object.objList.append( self )
    
  def getDistanceFromOrigin(self):
    return self.__distance
    
  def getSeperationDistance(self):
    return self.__seperationDist
        
  def getSize(self):
    return self.__size
  
  def getCoords(self):
    return self.pos
  
  def forceIncrement(self, force):
    self.force = force
       
  def commitForceApplication(self):
    """
    Moves the object to the origin, then to the position it is forced to
    Forces are then reset
    """
    try:
      self.__graphObject.Move( self.force[0],self.force[1]  ) # Go go go
      self.pos = [ self.pos[0] + self.force[0], self.pos[1] + self.force[1] ]
    except:
      print "WARNING: commitForceApplication() in ForceTransfer.py failed"
    self.force = [0,0] 
    
  def recenteringPush(self, x, y):
    """ Puts the object back onto the canvas if it got forced off """
    self.__graphObject.Move( x,y ) 
      
      
class NodeObject(Object):
  """ Regular node entity with position and size attributes """
  
  def __init__(self, graphObject, pos, size, seperationDist, topLeftPos ):    
    Object.__init__(self, graphObject, pos, size,seperationDist )
    self.__topLeftPos = topLeftPos
    
  def getTopLeftPos(self):
   return self.__topLeftPos
      
class EdgeObject(Object):
  """ 
  Idea for improvement: find the label/drawing attached to the center of the
  edge, and use its size instead of treating this as an object with no size.
  """
                                                      
  def __init__(self, graphObject, pos, seperationDist ):    
    Object.__init__(self, graphObject, pos, [1,1],seperationDist )

class ControlPoint(Object):
  """ 
  Control point is merely a point along the edge, thus it needs a customized
  approach for moving it around. It also has no real size concept.
  """

  def __init__(self, pos, seperationDist,itemHandler,index, dc ):    
    Object.__init__(self,None, pos, [1,1],seperationDist )
    self.__itemHandler = itemHandler
    self.__index = index
    self.dc = dc
    
  def recenteringPush(self, x, y):
    """ No need for this since the Edge 'Move' method handles it """
    return
    cCoords = self.dc.coords( self.__itemHandler )
    cCoords[self.__index] += x
    cCoords[self.__index+1] += y
    self.dc.coords( * [self.__itemHandler] + cCoords )
    
  def commitForceApplication(self):
    
    cCoords = self.dc.coords( self.__itemHandler )
    cCoords[self.__index] += self.force[0]
    cCoords[self.__index+1] += self.force[1]
    self.dc.coords( * [self.__itemHandler] + cCoords )
    
    self.pos = [ self.pos[0] + self.force[0], self.pos[1] + self.force[1] ]
    self.force = [0,0] 
      
