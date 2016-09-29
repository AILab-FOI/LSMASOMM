"""
ModelSpecificCode.py

This file is meant to contain methods that are dependent on the unique 
properties of a given meta-model,
or that have a chance of being 'broken' by some model. 

Created July 26, 2004 by Denis Dube
"""

import string

#from graphLink            import graphLink
#from graphEntity          import graphEntity


# If your model has hyper-edges and uses a different class name, please add it to this list
HYPER_EDGE_CLASSES = [ 'graph_Hyperedge', 'graph_ERrelationship',
                      'graph_Relationship3', 'graph_Association3' ]

# If your model knows how to scale itself when saved/loaded, add it here
PARTIALLY_SELF_SCALING_CLASSES = [ 'graph_Basic', 'graph_History' ]
SELF_SCALING_CLASSES           = []

# If your model knows how to offset its labels when saved/loaded add it here
SELF_LABEL_OFFSETTING_OBJECTS = [ 'graph_Basic', 'graph_History' ]

def isSubclass( object, className ):
  """
  Utility that determines if an object has a given subclass by string name only
  """
  
  # Obtain the list of all the node's base classes
  bases = object.__class__.__bases__		
  # Iterate over all the base classes				
  for base in bases:							
    if( base.__name__ == className ): 
      return True					
  return False								

def isHyperEdge( object ):
  """
  A non-statisfactory method for determining if an edge should be allowed 
  to connect more than 2 objects. Hopefully a better way can be found...
  """
  className = string.split( str(object.__class__) , '.' )[1]
  if( className in HYPER_EDGE_CLASSES ):
      return True
  return False



def isConnectionLink( object ):
    """
    Assumes all links are a subclass of graphLink (assumption seems quite valid)
    """
    #return issubclass( object.__class__, graphLink ) 
    return isSubclass( object, "graphLink" ) 

def isEntityNode( object ):
    """
    Assumes all entities are a subclass of graphEntity (assumption seems quite valid)
    """
    #return issubclass( object.__class__, graphEntity ) 
    return isSubclass( object, "graphEntity" ) 



def isObject_Scaling_Neutral( object ):
    """ Object that when saved/loaded does not retain the scaled size at all """
    if( object.__class__.__name__ in SELF_SCALING_CLASSES ):
        return False
    elif( object.__class__.__name__ in PARTIALLY_SELF_SCALING_CLASSES ):
        return False
    return True
    
    
def isObject_Partially_Self_Scaling( object ):
    """ 
    Object that when saved/loaded retains the scaled size of the graphical form
    but does not retain the connectors scaled positions
    """
    if( object.__class__.__name__ in PARTIALLY_SELF_SCALING_CLASSES ):
        return True
    return False

def isObject_Self_Label_Offseting( object ):
    """ Object that when saved/loaded retains label offsets """
    if( object.__class__.__name__ in SELF_LABEL_OFFSETTING_OBJECTS ):
        return True
    return False


