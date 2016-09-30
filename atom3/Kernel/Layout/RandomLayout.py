""" 
RandomLayout.py

Generates a random layout by moving all the nodes positions randomly in 
a 640x480 pixel box. The connections are then optimized for the new layout.

Guaranteed to hit an aesthetic layout at infinity, not recognize it, and 
keep on going for another infinity :p

Created Summer 2004, Denis Dube
"""


from random               import randint

from Utilities            import selectAllVisibleObjects, optimizeLinks
from ModelSpecificCode    import isEntityNode

def applyLayout(self):
  
  for nodetype in self.ASGroot.nodeTypes:	
    for node in self.ASGroot.listNodes[nodetype]:
      
      if( isEntityNode( node.graphObject_ ) ):
        
        # Move the nodes around
        currPos = node.graphObject_.getCenterCoord()        
        newPos = [ randint(0,640), randint(0,480) ]
        node.graphObject_.Move( -currPos[0],-currPos[1], False) # Go back to the origin
        node.graphObject_.Move( newPos[0], newPos[1], False)    # Move to random location
             
      
      else:
        
        # Move the links around 
        currPos= node.graphObject_.getCenterCoord()
        newPos = [ randint(0,640), randint(0,480) ]
        node.graphObject_.Move( -currPos[0],-currPos[1]) # Go back to the origin
        node.graphObject_.Move( newPos[0], newPos[1])    # Move to random location
            
            
  selectAllVisibleObjects( self )
  optimizeLinks( self.cb )      
  
  """
    # This code fragment can spill all the co-ordinates making up an edge
    for nodetype in core.ASGroot.nodeTypes:	
      for node in core.ASGroot.listNodes[nodetype]:
        
        size = node.graphObject_.getSize()
        if( size[0] == 0 ):
          print "Size is 0", node, node.graphObject_.getCenterCoord(), "<--conns"
          node.graphObject_.Move(20,20)
        else:
          if( node.graphObject_.getConnectionCoordinates( "OUT", node.graphObject_) != None ):
            coords = node.graphObject_.getConnectionCoordinates( "OUT", node.graphObject_)[0]
            middlePos = [coords[2],coords[3] ]
            print node,middlePos, "<--getConn"
    """