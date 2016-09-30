"""
SpringLayout.py

  This algorithm is based on the physical spring model, in the sense that nodes
  with a link between them will want to pull each other together until the
  distance between them equals the resting length of the 'spring'. The further
  apart they are, the more force that is applied to bring them to the ideal 
  length. 
  The algorithm also takes inspiration from electrical repulsive charges. To 
  this end, each node is modeled as an electrical charge. The charge is 
  determined by the screen size of the node. The force of the charge diminishes
  with the square of the distance, however forces are accumulated from the
  interaction of each node on every every other node. 
  Finally, the algorithm uses the concept of friction to prevent nodes from
  slowly sliding away when they are getting nudged by minor electrical forces.  
  
  The good: it gives pleasent layouts in many cases, and can be applied to any
  subsets of nodes & edges in any meta-model in AToM3... so long as the subset 
  doesn't contain any hyper-edges :D
    
  Problems and possible solutions with this algorithm:
  
  1) Local minima solutions, which prevent the algorithm from finding better solns.
    a) Add more random displacements
    
  2) Running time
    a) Implement an approximate spring based system that is less than O(n^2)
    
  3) Edge crossings, intrinsic problem with this type of algorithm.
  
  4) Compactness of representation: spring layouts are intrinsincally space innefficient

  5) Oscillation
    a) Add temperature control to reduce both back and forth oscillation 
    b) Detect and dampen rotational oscillation  
    
  6) 'Random' Tkinter errors at runtime, occuring with large graphs and overlapping nodes
    a) Do a pre-processing step that guarantees no overlapping nodes
  
Overhauled July 19, 2004 by Denis Dube  
"""

import math
from random               import randint

from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog
from Utilities            import optimizeLinks
from ModelSpecificCode    import isConnectionLink

def applyLayout( selection = None, atom3i = None, settingsMode = False ):
  
   # Instantiate the layout algorithm, if not already done  
  if( SpringLayout.instance == None ):
    if( atom3i == None ):   
      raise Exception, "You forgot to initilize "+__name__+" before using it!"
    SpringLayout.instance = SpringLayout(atom3i)    
        
  if( atom3i ):
    SpringLayout.instance.updateATOM3instance( atom3i )  
    
  if( settingsMode ):
    SpringLayout.instance.settings(selection) # Change spring parameters
  elif( selection ):    
    SpringLayout.instance.main(selection)     # Apply spring
    
class SpringLayout:
  
  instance = None
  
  # Option keys
  MAXIMUM_ITERATIONS      = 'Maximum iterations'  
  ANIMATION_UPDATES       = 'Animation updates'
  SPRING_CONSTANT         = 'Spring constant'
  SPRING_LENGTH           = 'Spring rest length'
  CHARGE_STRENGTH         = 'Charge strength'
  FRICTION                = 'Friction'  
  RANDOM_AMOUNT           = 'Random amount'
  ARROW_CURVATURE         = 'Arrow curvature'
  SPLINE_ARROWS           = 'Spline arrows'
  STICKY_BOUNDARY         = 'Sticky boundary'
  INFO0                   = 'Info0'
  INFO1                   = 'Info1'
  INFO2                   = 'Info2'
  INFO3                   = 'Info3'
  INFO4                   = 'Info4'
  
  def __init__(self, atom3i ):
      
    self.atom3i = atom3i
    self.dc     = atom3i.UMLmodel
          
    # Instantiate the Option Database module
    self.__optionsDatabase = OptionDatabase(self.atom3i.parent,
                    'Options_SpringLayout.py', 'Spring Layout Configuration')
    
    # Local methods/variables with short names to make things more readable :D
    newOp = self.__optionsDatabase.createNewOption
    IE = OptionDialog.INT_ENTRY
    FE = OptionDialog.FLOAT_ENTRY
    BE = OptionDialog.BOOLEAN_ENTRY
    L  = OptionDialog.LABEL
      
    # Create New Options
    # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
    
    newOp( self.INFO0, None, [L,"Times 12","black", "center" ],
          "This spring-electrical algorithm:", "" )
    newOp( self.INFO1, None, [L,"Times 12","black", "left" ], 
          "Has O(n^2) complexity", "" )    
    newOp( self.INFO3, None, [L,"Times 12","black", "left" ], 
          "Does not work with hyper-edges", "" )  
    newOp( self.INFO2, None, [L,"Times 12","black", "left" ], 
          "Is applied only on selected nodes & edges", "" )
    newOp( self.INFO4, None, [L,"Times 12","black", "left" ],"", "" )
    
    newOp( self.MAXIMUM_ITERATIONS, 100, IE, "Maximum Iterations", 
        "Duration of the spring simulation, longer generally gives better results." )    
    newOp( self.ANIMATION_UPDATES, 5, IE, "Animation updates", 
        "Force update of the canvas every X simulation frames." )
                        
    newOp( self.SPRING_CONSTANT, 0.1, FE, "Spring Constant",
        "The restoring force of the spring, larger values make the spring \"stiffer\"")
    newOp( self.SPRING_LENGTH, 100, IE, "Spring rest length",
        "This is the minimum distance between the 2 nodes")
        
    newOp( self.CHARGE_STRENGTH, 1000.00, FE, "Charge strength", 
        "A multiplier on the repulsive force between each and every node." )
    newOp( self.FRICTION, 0.01, FE, "Friction", 
        "Limits the ability of the repulsive force to affect another node." )
    newOp( self.RANDOM_AMOUNT, 0.0, FE, "Initial randomization", 
        "Randomizes the initial position of linked nodes as a percentage of spring length." )    
                
    newOp( self.ARROW_CURVATURE, 10, IE, "Arrow curvature", 
        "Adds a curve of magnitude X to the arrows, set to 0 for a straight arrow." )
    newOp( self.SPLINE_ARROWS, True, BE, "Spline arrows", 
        "Arrows are set to smooth/spline mode and given additional control points." ) 
    newOp( self.STICKY_BOUNDARY, True, BE, "Sticky boundary", 
        "Prevents nodes from escaping the canvas boundaries." )
       
    # Load the options from the file, on failure the defaults above are used.
    self.__optionsDatabase.loadOptionsDatabase()
    self.__processLoadedOptions()
    
    
  def __processLoadedOptions(self):
    """ After loading the database, have to get & store each option value """
      
    self.__maxIterations         = self.__optionsDatabase.get(self.MAXIMUM_ITERATIONS)  
    self.__animationUpdates      = self.__optionsDatabase.get(self.ANIMATION_UPDATES)  
    self.__springConstant        = self.__optionsDatabase.get(self.SPRING_CONSTANT)  
    self.__springLength          = self.__optionsDatabase.get(self.SPRING_LENGTH)  
    self.__chargeStrength        = self.__optionsDatabase.get(self.CHARGE_STRENGTH)  
    self.__friction              = self.__optionsDatabase.get(self.FRICTION)  
    self.__stickyBoundary        = self.__optionsDatabase.get(self.STICKY_BOUNDARY)  
    self.__splineArrows          = self.__optionsDatabase.get(self.SPLINE_ARROWS)  
    self.__arrowCurvature        = self.__optionsDatabase.get(self.ARROW_CURVATURE)  
    self.__randomness            = self.__optionsDatabase.get(self.RANDOM_AMOUNT)  

  def updateATOM3instance( self, atom3i ):
    self.atom3i = atom3i
  
  
  def settings(self, selection):
    """
    Dialog to interactively change the spring's behavior
    Automatically applies spring layout if not canceled
    """
    if( self.__optionsDatabase.showOptionsDatabase() ):
      self.__processLoadedOptions()  
      self.main(selection)
    
  def main(self, selection):

    if( not selection ): return
    
    atom3i = self.atom3i
    nodeObject.nodeList = []
    edgeObject.edgeList = []
    edgeObject.dc       = self.dc   
       
    #------------------------- INFORMATION GATHERING -------------------------
       
    # Generate a datastructure for the Nodes and Edges in the diagram, containing
    # only the information needed by this algorithm.
    edgeList   = []
    nodeDict   = dict()
    self.sourceTargetDict = dict()
    for obj in selection:
        
        if( isConnectionLink( obj ) ):  
          # Edge!
          edgeList.append( obj.getSemanticObject() )                    
        else:
          # Node
          pos = obj.getCenterCoord()
          boundBox = obj.getbbox()
          if( self.__stickyBoundary ):
            boundary = self.atom3i.CANVAS_SIZE_TUPLE
          else:
            boundary = None
          n = nodeObject( obj, pos, boundBox, self.__chargeStrength, boundary )
          nodeDict.update( { obj : n } )
           
    # Now lets go through the "node" edges...
    for node in edgeList:
      # Source object
      key = node.in_connections_[0].graphObject_
      if( not nodeDict.has_key( key ) ): continue
      source = nodeDict[ key ]
      
      # Target object
      key = node.out_connections_[0].graphObject_
      if( not nodeDict.has_key( key ) ): continue
      target = nodeDict[ key ]
      
      # Make the edge object with the info...         
      edgeObject(node, source, target)
      self.sourceTargetDict[ source ] = target
      
      # These nodes have edges...
      source.setHasEdgeTrue()
      target.setHasEdgeTrue()
      
    # Count the beans...
    self.__totalNodes = len( nodeObject.nodeList )
    if( self.__totalNodes <= 1 ):  return                          
                              
    #-------------------------- MAIN SIMULATION LOOP -------------------------
    
    # Initial card shuffling :D
    if( self.__randomness ):
      self.__shakeThingsUp( self.__randomness )

    i = 0
    while( i < self.__maxIterations ):
      
      # Calculate the powers that be
      self.__calculateRepulsiveForces()
      self.__calculateAttractiveForces()
        
      # Move move move!
      for node in nodeObject.nodeList:
        node.commitMove()  
          
      # Force a screen update every x calculation
      if( i % self.__animationUpdates == 0 ):
        self.dc.update_idletasks()

      i+=1
          
    #--------------------------- FINAL OPTIMIZATIONS -------------------------

    # Optimize the arrows to use the nearest connectors
    optimizeLinks( self.atom3i.cb, self.__splineArrows, self.__arrowCurvature )
    
    # Make sure the canvas is updated
    self.dc.update_idletasks()
     
  
  def __shakeThingsUp( self, randomness ):
    """ Randomizes positions of the nodes forming a link """
    
    amount =  int( randomness * self.__springLength  )
    for edgeObj in edgeObject.edgeList:
      source = edgeObj.getSource()
      target = edgeObj.getTarget()
      
      dx = randint( -amount, amount )
      dy = randint( -amount, amount )
      
      source.incrementDisplacement( [dx,dy] )
      source.commitMove()  
      
      dx = randint( -amount, amount )
      dy = randint( -amount, amount )
      
      target.incrementDisplacement( [dx,dy] )
      target.commitMove()  
       
              
  def __calculateRepulsiveForces(self):
    """ Every node exerts a force on every other node, prevent overlap """
           
    # If two nodes overlap, set the distance to this value to seperate them
    # Hint: the closer two nodes are, the more powerful the repulsion
    overlapDistance = 1 
    
    i = 0    
    while( i < self.__totalNodes ):
      j = 0
      ax = ay = 0
      source = nodeObject.nodeList[i]
      iPos = source.getCoords()
      sourceCharge = source.getCharge()   
      sourceHasEdge = source.hasEdge()
      while( j < self.__totalNodes ):
          
        if( i == j ):
          j += 1
          continue
        target = nodeObject.nodeList[j] 
        j += 1
                                    
        # This prevents an unattached node from affecting attached nodes
        if( sourceHasEdge and not target.hasEdge() ):
          continue
       
        dx, dy, distance = self.__getDistancesTuple( source, target, overlapDistance )
        
        # Reduce repulsion of nodes that are tied together by springs
        if( self.sourceTargetDict.has_key( source ) and self.sourceTargetDict[ source ] == target ):
            distance *= 2          
        elif( self.sourceTargetDict.has_key( target ) and self.sourceTargetDict[ target ] == source ):
            distance *= 2   
          
        charge = max( sourceCharge, target.getCharge() )
        electricForce = charge / ( distance * distance ) 
                    
        # The cutoff prevents unnecessary movement 
        if( electricForce < self.__friction ):
          continue  
          
        # Accumlate displacement factor
        ax += dx * electricForce
        ay += dy * electricForce           
              
      # Store the accumlated displacement
      source.incrementDisplacement( [ax,ay] ) 
      #print vDisp, "<-- Repulsion displacement"
      i+=1
     
            
  def __calculateAttractiveForces(self):
    """ Every edge exerts forces to draw its nodes close """
    
    # If two nodes overlap, set distance to this value to seperate them
    # Hint: the smaller the distance is relative to the spring rest length, the 
    # greater the serperating force will be.
    overlapDistance = self.__springLength * 0.75
    
    for edge in edgeObject.edgeList:
      
      source = edge.getSource()
      target = edge.getTarget()
      
      # No fake edges permitted!
      if( source == target or source == None or target == None):
        continue
                  
      dx, dy, distance = self.__getDistancesTuple( source, target, overlapDistance )
      
      '''
      Basic Spring Equation: F = - k * x
      Replacing x with (d-l)/d, you get no force at the resting spring length,
      and lots of force the farther away from the spring length you are.
      The neat thing here: the spring will contract when the distance exceeds
      the length and expand when the distance is less than the length.
      Spring Equation: F = k * ( distance - length )  / distance
      '''         
      attractForce  = self.__springConstant * (distance - self.__springLength )
      if( abs(distance) > 0 ):
        attractForce /= distance 
      disp = [ attractForce * dx, attractForce * dy ]
      #print attractForce, disp, "<---- attract, disp"
  
      # Accumulate the displacement factor at the source & target nodes
      target.incrementDisplacement( disp ) 
      source.incrementDisplacement( [-disp[0], -disp[1]] )
  
        
  def __vectorLength2D(self, v ):
    """ Calculates the length of the 2D vector v """
    return math.sqrt( v[0] * v[0] + v[1] * v[1] ) 
             
            
  def __getDistancesTuple( self, sourceNode, targetNode, overlapDistance ):
      """ 
      Finds the distance between two nodes and handles overlapping. 
      Returns normalized dx,dy components as well as the magnitude of the distance
      in a tuple.      
      """
      
      def normalizeAndFixDistance( dx, dy, distance, overlapDistance, overlap=False ):
        """ 
        Normalizes the dx & dy variables
        If distance is too small, then it modifies dx & dy arbitrarily
        and sets the distance so that the spring will expand violently or
        the electrical charge will blast away...
        """
        if( distance < 1 or overlap ):
          if( abs( dx ) < 1 ):
              if( dx < 0 ): dx = -1
              else:         dx =  1
          if( abs( dy ) < 1 ):
              if( dy < 0 ): dy = -1
              else:         dy =  1
          return (dx,dy, overlapDistance )
        else:
          return ( dx / distance, dy / distance, distance )
      
      sx, sy, sw, sh = sourceNode.getCoordsAndSize()
      tx, ty, tw, th = targetNode.getCoordsAndSize()
      
      # Position Delta
      dx = sx - tx 
      dy = sy - ty 
      
      # Overlap area      
      ox = ( sw + tw ) / 2.0
      oy = ( sh + th ) / 2.0
      if( dx < 0 ):   ox = -ox
      if( dy < 0 ):   oy = -oy
                
      # Total Node overlap
      if( abs( dx ) < abs( ox ) and abs( dy ) < abs( oy ) ): 
         distance = self.__vectorLength2D( [dx,dy] )
         return normalizeAndFixDistance( dx, dy, distance, overlapDistance, overlap=True)

         
      # No Node Overlap (but maybe overlap along an axis)
      else:
         # If the distance exceeds the size of the nodes, subtract the size
         # otherwsie, set the distance to zero.
         if( abs( dx ) > abs( ox ) ):  dx -= ox
         else:                         dx = 0
         if( abs( dy ) > abs( oy ) ):  dy -= oy
         else:                         dy = 0
         distance = self.__vectorLength2D( [dx,dy] )
         return normalizeAndFixDistance( dx, dy, distance, overlapDistance)
         
      
  
class nodeObject:
  
  nodeList = []
      
  def __init__(self, graphObject, pos, boundBox, chargeStrength, boundary ):   
    self.graphObject = graphObject
    self.__hasEdge = False
    self.__boundBox = boundBox
    self.__pos = pos
    self.__displacement = [0,0]
    self.__boundary = boundary
    self.__boundaryPad = 50
    self.__width = abs( (boundBox[0] - boundBox[2])  )
    self.__height = abs( (boundBox[1] - boundBox[3]) )
    self.__charge = chargeStrength * math.sqrt( self.__width*self.__width + self.__height*self.__height )
    nodeObject.nodeList.append( self )
    
  def setHasEdgeTrue(self):
    self.__hasEdge = True
    
  def hasEdge(self):
    return self.__hasEdge
    
  def getBoundaryBox(self):
    return self.__boundBox

  def getCoordsAndSize( self ):
    return ( self.__pos[0], self.__pos[1], self.__width , self.__height )
              
  def getCoords(self):
    return self.__pos
  
  def getCharge(self):
    return self.__charge
  
  def incrementDisplacement(self, vDisp, ):
    self.__displacement = [ self.__displacement[0] + vDisp[0], 
                            self.__displacement[1] + vDisp[1] ]
      
  def commitMove( self ):
    dx, dy = self.__displacement
    self.__displacement = [0,0]
    self.movePositionAndBoundary( dx,dy )
    
    # Prevent objects from leaving the canvas area
    if( self.__boundary ):
            
      x0,y0,x1,y1 = self.__boundary
      if( self.__boundBox[0] < x0 + self.__boundaryPad ):
        return self.movePositionAndBoundary( -dx,-dy )
      elif( self.__boundBox[1] < y0 + self.__boundaryPad ):
        return self.movePositionAndBoundary( -dx,-dy )
      elif( self.__boundBox[2] + self.__boundaryPad > x1  ):
        return self.movePositionAndBoundary( -dx,-dy )
      elif( self.__boundBox[3] + self.__boundaryPad > y1 ):
        return self.movePositionAndBoundary( -dx,-dy )
        
    self.graphObject.Move( dx,dy ) 
                                   
  def movePositionAndBoundary( self, dx,dy ):
    
    self.__pos = [ self.__pos[0] + dx , self.__pos[1] + dy ]
    
    self.__boundBox = [ self.__boundBox[0] + dx, self.__boundBox[1] + dy,
                        self.__boundBox[2] + dx, self.__boundBox[3] + dy ]
    
    
class edgeObject:
  
  edgeList = []
  dc       = None
  
  def __init__(self,ASGnode, source, target):
    self.ASGnode = ASGnode
    
    # These are of type nodeObject
    self.__source = source
    self.__target = target
    
    edgeObject.edgeList.append( self )  

  def getSource(self):
    return self.__source
  
  def getTarget(self):
    return self.__target
  
  def getGrpahicalObject(self):
    return self.ASGnode.graphObject_
  


    
      
      
      