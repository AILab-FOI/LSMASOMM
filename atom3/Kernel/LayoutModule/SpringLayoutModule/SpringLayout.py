"""
SpringLayout.py

  This algorithm does several physical model simulations on a graph in order to 
  achieve a layout. The running time is O(iterations * n^2).
    
  1) The physical spring model. Each pair of connected nodes is treated as two 
  objects with a spring connecting them. These springs will seek to push objects
  that are very close together apart, and objects that are far apart close 
  together... until the objects are exactly the length of the spring distance 
  apart. In practice this won't happen because of all the competing forces 
  acting on the nodes...
  Aesthetic: connected nodes are grouped close together
  
  2) The electrical charge repulsion model. Each pair of nodes (regardless of
  existing connections) is treated as a pair of mutually repulsive electric
  charges. Charge strengths are determined by a user constant multiplied with 
  the diagonal size of a node. The effect of the charge drops with the square
  of the distance, until a threshold distance is reached. 
  Aesthetic: prevents node overlapping and often produce nices symmetries
  
  3) The gravitational force model (simplified model). The center of the graph 
  exerts a constant force towards itself on every node in the graph.
  Aesthetic: compact layout
  
By Denis Dube
Last update: Sept. 2005
"""

import math
import sys
from random               import randint

from SpringOptionsKeys import MAXIMUM_ITERATIONS
from SpringOptionsKeys import SPRING_CONSTANT
from SpringOptionsKeys import SPRING_LENGTH
from SpringOptionsKeys import CHARGE_STRENGTH
from SpringOptionsKeys import CHARGE_THRESHOLD
from SpringOptionsKeys import GRAVITY_STRENGTH
from SpringOptionsKeys import RANDOM_AMOUNT
from SpringOptionsKeys import FORCE_TOPLEFT_TO_ORIGIN
from SpringOptionsKeys import USE_SPLINES
from SpringOptionsKeys import ARROW_CURVATURE
from SpringOptionsKeys import PROMOTE_EDGE_TO_NODE
from SpringOptionsKeys import MINIMUM_FORCE
from SpringOptionsKeys import FORGIVE_ROUNDS


def doSpringLayout(abstractGraph, optionsDict):
  """ Applies the spring layout algorithm """

  # Promote directed edges to hyperedges, useful if the edge has a large drawing
  # then that drawing becomes a node, and two new directed edges are created.
  if(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Always'):
    abstractGraph.promoteDirectedEdge(True)
  elif(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Smart'):
    abstractGraph.promoteDirectedEdge(False)

  nodeList = abstractGraph.getAbstractNodeList()
  chargeStrength = optionsDict[CHARGE_STRENGTH]
  chargeThreshold = optionsDict[CHARGE_THRESHOLD]
  gravityStrength = optionsDict[GRAVITY_STRENGTH]
  
  # Initilize the "new" coords attribute
  for node in nodeList:
    x, y = node.getPos()
    w, h = node.getSize()
    node.setNewCoords((x + w / 2, y + h / 2)) #node.getNewCoords() = centerCoord
    node._electricCharge = chargeStrength * math.sqrt(w * w + h * h)
    node._xForce = 0
    node._yForce = 0
  totalNodes = len(nodeList)
  if(totalNodes <= 1):
    return
    
  # Initial card shuffling :D
  if(optionsDict[RANDOM_AMOUNT]):
    __shakeThingsUp(abstractGraph, optionsDict)

  # Enable if degrees are used
  #abstractGraph.initNodeChildrenParents()

  i = 0
  forgivenessRounds = optionsDict[FORGIVE_ROUNDS]
  while(i < optionsDict[MAXIMUM_ITERATIONS]):
    
    # Calculate electrical charge repulsion forces
    if(chargeStrength):
      __calculateRepulsiveForces(abstractGraph, chargeThreshold)
      
    # Calculate spring forces
    __calculateAttractiveForces(abstractGraph, optionsDict)
    
    # Calculate graviational forces
    if(gravityStrength):
      __calculateGravitationalForces(abstractGraph, gravityStrength)
    
    # Translate the forces on each node into new positions
    maxForce = 0
    for node in nodeList:
      x0, y0 = node.getNewCoords()
      node.setNewCoords((x0 + node._xForce, y0 + node._yForce))
      
      maxForce = max(maxForce, max(node._xForce, node._yForce))
            
      # Reset force values
      node._xForce = 0
      node._yForce = 0
      
    #print 'Iteration', i, 'maxForce', maxForce, '\n'
    
    # CONVERGENCE TEST
    if(maxForce < optionsDict[MINIMUM_FORCE]):
      if(forgivenessRounds == 0):
        break   
      forgivenessRounds -= 1
    else:
      # Reset the forgiveness rounds, still some progress being made
      forgivenessRounds = optionsDict[FORGIVE_ROUNDS]
        
    i += 1
    
  # Cleanup temporary attributes
  for node in nodeList:
    del node._electricCharge 
    del node._xForce
    del node._yForce
    
  # Make sure everything is in the canvas
  if(optionsDict[FORCE_TOPLEFT_TO_ORIGIN]):
    __forceObjectsIntoViewArea(abstractGraph)
    
  # Fix up the arrows
  __optimizeArrows(abstractGraph, optionsDict)

    
    
    
def __calculateGravitationalForces(abstractGraph, gravityStrength):
  """
  Use:
    Calculates a simplified model of gravity to pull nodes closer to the center
    of the graph, thus maximizing the compactness of the layout.
  """
  nodeList = abstractGraph.getAbstractNodeList()
    
  # Step 1: Find the center of the graph  [Barycenter Method]
  sumX, sumY = (0, 0)
  for node in nodeList:
    temp = node.getNewCoords()
    sumX, sumY = (sumX + temp[0], sumY + temp[1])
  center = (sumX / len(nodeList), sumY / len(nodeList))
  
  '''
  # Step 1: Find the center of the graph  [BOUNDING BOX CENTER]
  minX = sys.maxint
  maxX = -(sys.maxint - 1)
  minY = sys.maxint
  maxY = -(sys.maxint - 1)  
  for node in nodeList:
    x, y = node.getNewCoords()
    if(x < minX):
      minX = x
    if(x > maxX):
      maxX = x
    if(y < minY):
      minY = y
    if(y > maxY):
      maxY = y
  
  center = ((maxX - minX) / 2, (maxY - minY) / 2)
  '''
  
  # Step 2: Gravity
  for node in nodeList:
    # Compute unit vector of node to the graph center
    x, y = node.getNewCoords()
    dx = center[0] - x
    dy = center[1] - y
    distance = math.sqrt(dx * dx + dy * dy)
    
    # What if the node is at the center of the gravity maelstrom?
    if(distance == 0): 
      unitVector = (dx, dy)
    else:
      unitVector = (dx / distance, dy / distance)
    
    # Increment the forces acting on the node
    node._xForce += unitVector[0] * gravityStrength
    node._yForce += unitVector[1] * gravityStrength
    
    
    
def __calculateRepulsiveForces(abstractGraph, chargeThreshold):
  """
  Every node exerts a force on every other node, prevent overlap 
  This version of the implementation is more complicated than an older one.
  If a and b are vertices, then the algorithm calculates only one of (a, b) and
  (b, a), also it totally ignores (a, a) since a vertex should not self-repulse!
  Running time is O(0.5 * V * (V - 1))
  """
         
  #debugForces(abstractGraph)
  nodeList = abstractGraph.getAbstractNodeList()
  
  totalNodes = len(nodeList)
  i = 0     # i is always between [0, len(nodeList)]
  j = i + 1 # j is always between ]i, len(nodeList)]
  # Every node repulses every other node
  while(i < totalNodes):
    nodeA = nodeList[i]
    while(j < totalNodes):
        nodeB = nodeList[j]
        
        # Get Manhattan and Euclidean distances
        aX, aY = nodeA.getNewCoords()
        bX, bY = nodeB.getNewCoords()
        dx = aX - bX
        dy = aY - bY
        distance = math.sqrt(dx * dx + dy * dy)
        
        # Maximum distance for a repulsive force
        if(abs(distance) > chargeThreshold):
          j += 1
          continue
  
        charge = nodeA._electricCharge + nodeB._electricCharge
        # Distance is greater than 1
        if(abs(distance) >= 0.1):
          electricForce = charge / (distance * distance) 
          nodeA._xForce += dx * electricForce
          nodeA._yForce += dy * electricForce    
          nodeB._xForce -= dx * electricForce
          nodeB._yForce -= dy * electricForce  
          
        # Distance is really small, probably overlapping
        else:
          electricForce = charge
          if(dx >= 0):
            nodeA._xForce += electricForce
            nodeB._xForce -= electricForce
          else:
            nodeA._xForce -= electricForce
            nodeB._xForce += electricForce
          if(dy >= 0):
            nodeA._yForce += electricForce 
            nodeB._yForce -= electricForce 
          else:
            nodeA._yForce -= electricForce 
            nodeB._yForce += electricForce 
          
        j += 1
    i += 1
    j = i + 1
  
   
          
def __calculateAttractiveForces(abstractGraph, optionsDict):
  """ Every edge exerts forces to draw its nodes close """
  
  # If two nodes overlap, set distance to this value to seperate them
  # Hint: the smaller the distance is relative to the spring rest length, the 
  # greater the serperating force will be.
  springLength = optionsDict[SPRING_LENGTH]
  springConstant = optionsDict[SPRING_CONSTANT]
  minimumDistance = 0.1

  for directedEdge in abstractGraph.getAbstractEdgeList():
    source, target = directedEdge.getSourceTargetNodeTuple()
    
    # No self-loops
    if(source == target):
      continue
      
    # Get Manhattan and Euclidean distances
    aX, aY = source.getNewCoords()
    bX, bY = target.getNewCoords()
    dx = aX - bX
    dy = aY - bY
    distance = math.sqrt(dx * dx + dy * dy)
    #dx, dy, distance = __getManhattanEuclideanTuple(source, target)
    
    # Deal with ugly 0 distance situation
    if(abs(distance) <= minimumDistance):
      if(distance >= 0):
        distance = minimumDistance
      else:
        distance = -minimumDistance
      if(dx >= 0):
        dx = minimumDistance
      else:
        dx = -minimumDistance
      if(dy >= 0):
        dy = minimumDistance
      else:
        dy = -minimumDistance
    
    '''
    Basic Spring Equation: F = - k * x
    Replacing x with (d-l)/d, you get no force at the resting spring length,
    and lots of force the farther away from the spring length you are.
    The neat thing here: the spring will contract when the distance exceeds
    the length and expand when the distance is less than the length.
    Spring Equation: F = k * ( distance - length )  / distance
    '''         
    #degree = len(source.getChildrenList()) + len(source.getParentsList()) \
    #        + len(target.getChildrenList()) + len(target.getParentsList())
    #idealSpringLength = springLength + springLength * float(degree) * 0.1
    attractForce  = springConstant * (distance - springLength)    \
                    / distance 
    xF, yF = (attractForce * dx, attractForce * dy)
    
    # Accumulate the displacement factor at the source & target nodes
    target._xForce += xF
    target._yForce += yF
    source._xForce -= xF
    source._yForce -= yF
    
    

def __optimizeArrows(abstractGraph, optionsDict):
  """
  Post-process to redraw arrows affected by moving nodes
  """
  # Post-process, redraw the arrows
  for arrow in abstractGraph.getAbstractEdgeList():
    arrow.setLinkOptimization(optionsDict[USE_SPLINES], 
                               optionsDict[ARROW_CURVATURE])


    
def __shakeThingsUp(abstractGraph, optionsDict):
  """ Randomizes positions of the nodes forming a link """
  
  randomFloat = float(optionsDict[RANDOM_AMOUNT]) / 100.0
  amount =  int(randomFloat * optionsDict[SPRING_LENGTH])
  for directedEdge in abstractGraph.getAbstractEdgeList():
    source, target = directedEdge.getSourceTargetNodeTuple()
    
    dx = randint( -amount, amount )
    dy = randint( -amount, amount )
    
    source.setNewCoords( [dx, dy] )
    
    dx = randint( -amount, amount )
    dy = randint( -amount, amount )
    
    target.setNewCoords( [dx, dy] )
    
    
    
def __forceObjectsIntoViewArea(abstractGraph):
  """
  Use:
    Keeps the whole thing in the viewable area of the canvas
  """
  minY = minX = sys.maxint
  for node in abstractGraph.getAbstractNodeList():
    x, y = node.getNewCoords()
    if(x < minX): 
      minX = x
    if(y < minY): 
      minY = y
    
  # Add the position recentering to the position
  if(minX != 0 or minY != 0):
    for node in abstractGraph.getAbstractNodeList():
      x, y = node.getNewCoords()
      node.setNewCoords((x - minX, y - minY))
      
      
  
def debugForces(abstractGraph):  
  print '__calculateRepulsiveForces'
  for node in abstractGraph.getAbstractNodeList():
    print node.getDistinctiveName(), node._xForce, node._yForce
    
    

'''
def __getManhattanEuclideanTuple(nodeA, nodeB):
  """
  Purpose:
    Gives the Manhattan distance dx, dy between two nodes. The getNewCoords()
    method on each node returns the top-left coordinate of that node. 
    Also returns the Euclidean distance based on the Manhattan distance.
  Parameters:
    nodeA and nodeB are abstract nodes
  Returns:
    Tuple of dx, dy, distance, where dx and dy are manhattan distance and 
    the last is the euclidean distance.
    
  OBSOLETE: far more complex than necessary! 
  """
  xA, yA = nodeA.getNewCoords()
  sxA, syA = nodeA.getSize()
  
  xB, yB = nodeB.getNewCoords()
  sxB, syB = nodeB.getSize()

  if(xA < xB):             # xA--------sxA
    dx = (xA + sxA) - xB   #      xB---------sxB
    # This means that nodeB is overlapping nodeA
    if(dx > 0):
      dx = xA - xB
  else:
    dx = xA - (xB + sxB)
    # This means that nodeB is overlapping nodeA
    if(dx < 0):
      dx = xA - xB
    
  if(yA < yB):
    dy = (yA + syA) - yB
    # This means that nodeB is overlapping nodeA
    if(dy > 0):
      dy = yA - yB
  else:
    dy = yA - (yB + syB)
    # This means that nodeB is overlapping nodeA
    if(dy < 0):
      dy = yA - yB
    
  distance = math.sqrt(dx * dx + dy * dy)
  return (dx, dy, distance)
'''


'''
def __calculateRepulsiveForces(abstractGraph, chargeThreshold):
  """ 
  Every node exerts a force on every other node, prevent overlap 
  This is the naive version that is simpler but considers each vertex pair
  (a, b) and (b, a) in seperate passes, and is thus slower.
  """
         
  #debugForces(abstractGraph)
  nodeList = abstractGraph.getAbstractNodeList()  
  
  # Every node repulses every other node
  for nodeA in nodeList:
    for nodeB in nodeList:
      
      # A node does not repulse itself though
      if(nodeA == nodeB):
        continue
        
      dx, dy, distance = __getManhattanEuclideanTuple(nodeA, nodeB)
      
      # Maximum distance for a repulsive force
      if(abs(distance) > chargeThreshold):
        continue

      charge = nodeA._electricCharge + nodeB._electricCharge
      # Distance is greater than 1
      if(abs(distance) >= 0.1):
        electricForce = charge / (distance * distance) 
        nodeA._xForce += dx * electricForce
        nodeA._yForce += dy * electricForce    
        
      # Distance is really small, probably overlapping
      else:
        electricForce = charge
        if(dx >= 0):
          nodeA._xForce += electricForce
        else:
          nodeA._xForce -= electricForce
        if(dy >= 0):
          nodeA._yForce += electricForce 
        else:
          nodeA._yForce -= electricForce 
  #debugForces(abstractGraph)
'''
          
