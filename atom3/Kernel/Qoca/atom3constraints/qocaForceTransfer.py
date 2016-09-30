"""
qocaForceTransfer.py

Applies force to all nodes that are too close to each other
Loops until a stable configuration is reached
Times out after 50 iterations, to avoid depriving the user of interactivity for too long.

Distance specifies how far apart you want your nodes
Force constant determines how much force (and how quickly) is applied
Animation time slows down the process so that it can be visualized
Max animation iteration cuts off the animation to save time

WARNING: I think this was just a test (that didn't work properly). 
         Probably should delete this file - Jan 2006
      
Refactored July 12, 2005 by Denis Dube
"""

import math
#import time
#from Utilities            import optimizeConnectionPorts

class qocaForceTransfer:
  
  def __init__(self):   
    # parent, link, child, options  
    self.__minNodeDist          = 20  
    self.__seperationForce      = 0.2  
    self.__maxIterations        = 50
    self.__isLayoutStable = False
    
                
  def antiOverlap(self, graphicalObjList):
       
    totalNodes = len(graphicalObjList) 

    # Trivial non-overlap case
    if(self.__totalNodes <= 1):
      return
      
    # Initilize...
    for obj in graphicalObjList:
      obj._temporaryX = obj.qcX.get()
      obj._temporaryY = obj.qcY.get()
      obj._temporaryH = obj.qcH.get()
      obj._temporaryW = obj.qcW.get()
    
        
    # Keep at it till the layout is stable
    k = 0
    while( not self.__isLayoutStable ):
      self.__isLayoutStable = True # Optimism is good...
      
      # Go through all the nodes, and find the overlap forces
      i = 0
      j = 1
      while( i < totalNodes ):
        while( j < totalNodes ):
          if( i != j ):      
            self.__forceCalculation( graphicalObjList[i], \
                                     graphicalObjList[j] )
          j += 1
        i += 1
        j = i
  
      if( k > self.__maxIterations ):   
        break
      k += 1
          
    # Finilize...
    for obj in graphicalObjList:
      obj.qcX.update(obj._temporaryX)
      obj.qcY.update(obj._temporaryY) 
      obj.qcH.update(obj._temporaryH) 
      obj.qcW.update(obj._temporaryW) 
      del obj._temporaryX 
      del obj._temporaryY 
      del obj._temporaryH 
      del obj._temporaryW 
  
                
      
  def __forceCalculation(self, n1, n2):
    """
    Evaluates distances betweens nodes (ie: do they overlap) and
    calculates a force sufficient to pry them apart.
    """
    
    # Absolute distance along X and Y vectors between the nodes 
    dx = abs(n2.obj._temporaryX - n1.obj._temporaryX) 
    dy = abs(n2.obj._temporaryY - n1.obj._temporaryY) 
    
    # Zero division error prevention measures
    if (dx == 0.0 ):      
      dx = 0.1
    if( dy == 0.0 ):      
      dy = 0.1
    
    # Node-Node Distances
    dist = math.sqrt(dx * dx + dy * dy)
    
    # Normalized-Vector
    norm = [ dx / dist , dy / dist ]

    # Overlap due to size of nodes
    sizeOverlap = [ (n1._temporaryW + n2._temporaryW) / 2 ,
                     (n1._temporaryH + n2._temporaryH) / 2 ]  
    
    # Desired distance with resulting force
    d1 = (1.0 / norm[0]) * (sizeOverlap[0] + self.__minNodeDist)
    d2 = (1.0 / norm[1]) * (sizeOverlap[1] + self.__minNodeDist)
    forceMagnitude = self.__seperationForce * (dist - min(d1, d2))
  
    # The force should be less than -1 (or it won't be having much of an effect)
    if (forceMagnitude < -1):     
      #print forceMagnitude, dist, d1,d2 , 
      # print (sizeOverlap[0] + minSeperationDist),
      # print (sizeOverlap[1] + minSeperationDist),(1.0 / norm[0]),
      # print (1.0 / norm[1])
      force = [ forceMagnitude * norm[0],  forceMagnitude * norm[1] ]
      
      # Maximize compactness by only pushing nodes along a single axis
      if( force[0] > force[1] ):   
        force[0] = 0
      else:                        
        force[1] = 0
      
      # Determine the direction of the force and apply the movement
      if(n1.obj._temporaryX > n2.obj._temporaryX): 
        n1.obj._temporaryX -= force[0]      
        n2.obj._temporaryX += force[0]
      else:
        n1.obj._temporaryX += force[0]      
        n2.obj._temporaryX -= force[0]
      
      if(n1.obj._temporaryY > n2.obj._temporaryY): 
        n1.obj._temporaryY -= force[1]
        n2.obj._temporaryY += force[1]
      else:
        n1.obj._temporaryY += force[1]
        n2.obj._temporaryY -= force[1]
   
      # If a force was applied this iteration, definately not stable yet
      self.__isLayoutStable = False      
   
      
      
