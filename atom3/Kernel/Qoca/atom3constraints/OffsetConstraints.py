"""
OffsetConstraints.py

Offers high level constraints for use by AToM3
"""

from Qoca.constraints.QocaConstants import EQ, LE, GE
from Qoca.constraints.QocaVariable import QocaVariable
from Qoca.constraints.QocaLinearConstraint import QocaLinearConstraint
from ConstraintBaseClass import ConstraintBaseClass


#================================================================================
# objTuple means a tuple of 3 instances of VisualObj, or the graphObject_
# attribute of an AToM3 node. 
# The tuple looks like: (object1, object2, object3)
# Where 3 is the link that ties entities 1 and 2 together
#================================================================================


class OffsetConstraints(ConstraintBaseClass):
  
  def __init__(self, solver, resolve=False):
    ConstraintBaseClass.__init__(self, solver, resolve)
  

#================================================================================
# Specific to left of constraints
#================================================================================
  def Left(self, objTuple):   
    """ Object1 lies left of object2 """ 
    self.horizonalConstraint(objTuple, 0, GE, (1.0, 0)) 

  def LeftExactDistance(self, objTuple, offset):
    """ Object1 lies left of object2 with exact distance """   
    self.horizonalConstraint(objTuple, offset, EQ, (1.0, 0))  
  
  def LeftMinDistance(self, objTuple, offset):   
    """ Object1 lies left of object2 with minimum distance """
    self.horizonalConstraint(objTuple, offset, GE, (1.0, 0))
    
  def LeftMaxDistance(self, objTuple, offset):   
    """Object1 lies left of object2 with maximum distance """
    self.horizonalConstraint(objTuple, offset, LE, (1.0, 0))  

#================================================================================
# Specific to right of constraints    
#================================================================================
  def Right(self, objTuple):   
    """ Object1 lies right of object2 """ 
    self.horizonalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                            0, GE, (1.0, 0)) 

  def RightExactDistance(self, objTuple, offset):
    """ Object1 lies right of object2 with exact distance """   
    self.horizonalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                       offset, EQ, (1.0, 0))  
  
  def RightMinDistance(self, objTuple, offset):   
    """ Object1 lies right of object2 with minimum distance """
    self.horizonalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                        offset, GE, (1.0, 0))
    
  def RightMaxDistance(self, objTuple, offset):   
    """ Object1 lies right of object2 with maximum distance """
    self.horizonalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                        offset, LE, (1.0, 0))
         
#================================================================================
#  Highly customizable constraints, combines user-definable distance with 
#  a percentage of the width/height of the object
#================================================================================
  def PercentWidthDistance(self, objTuple, offset, percentTuple):   
    """ Object1 lies exactly some X distance and a tuple percentage of
    the widths of Object1 and Object2 from Object2  """ 
    self.horizonalConstraint(objTuple, offset, EQ, percentTuple) 
    
  def PercentHeightDistance(self, objTuple, offset, percentTuple):   
    """ Object1 lies exactly some Y distance and a tuple percentage of
    the heights of Object1 and Object2 from Object2  """ 
    self.verticalConstraint(objTuple, offset, EQ, percentTuple)
    
#================================================================================
# Specific to top of constraints
#================================================================================
  def Top(self, objTuple):   
    """ Object1 lies top of object2 """ 
    self.verticalConstraint(objTuple, 0, GE, (1.0, 0)) 

  def TopExactDistance(self, objTuple, offset):
    """ Object1 lies top of object2 with exact distance """   
    self.verticalConstraint(objTuple, offset, EQ, (1.0, 0))  
  
  def TopMinDistance(self, objTuple, offset):   
    """ Object1 lies top of object2 with minimum distance """
    self.verticalConstraint(objTuple, offset, GE, (1.0, 0))
    
  def TopMaxDistance(self, objTuple, offset):   
    """Object1 lies top of object2 with maximum distance """
    self.verticalConstraint(objTuple, offset, LE, (1.0, 0))        
    
#================================================================================
# Specific to bottom of constraints    
#================================================================================
  def Bottom(self, objTuple):   
    """ Object1 lies below of object2 """ 
    self.verticalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                             0, GE, (1.0, 0)) 

  def BottomExactDistance(self, objTuple, offset):
    """ Object1 lies below of object2 with exact distance """   
    self.verticalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                        offset, EQ, (1.0, 0))  
  
  def BottomMinDistance(self, objTuple, offset):   
    """ Object1 lies below of object2 with minimum distance """
    self.verticalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                        offset, GE, (1.0, 0))
    
  def BottomMaxDistance(self, objTuple, offset):   
    """Object1 lies below of object2 with maximum distance """
    self.verticalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                        offset, LE, (1.0, 0))
                                                             
#================================================================================
#  Same/Center constraints
#================================================================================
  def SameX(self, objTuple):
    self.horizonalConstraint(objTuple, 0, EQ, (0, 0)) 
  
  def SameY(self, objTuple):
    self.verticalConstraint(objTuple, 0, EQ, (0, 0)) 
    
  def SameW(self, objTuple):
    source = objTuple[0]
    target = objTuple[1]
    link = objTuple[2]
    self.variableRelationConstraint(link, source.qcW, target.qcW, EQ, 0)

  def SameH(self, objTuple):
    source = objTuple[0]
    target = objTuple[1]
    link = objTuple[2]
    self.variableRelationConstraint(link, source.qcH, target.qcH, EQ, 0)
        
  def CenterX(self, objTuple):
    self.horizonalConstraint(objTuple, 0, EQ, (0.5, -0.5)) 
    
  def CenterY(self, objTuple):
    self.verticalConstraint(objTuple, 0, EQ, (0.5, -0.5)) 
    
  def Center(self, objTuple):
    self.horizonalConstraint(objTuple, 0, EQ, (0.5, -0.5)) 
    self.verticalConstraint(objTuple, 0, EQ, (0.5, -0.5)) 
    
#================================================================================
# Size minimum/maximum for height and width at once
#================================================================================
  def minSize(self, obj, value):
    self.minHeight(obj, value)
    self.minWidth(obj, value)
    
  def maxSize(self, obj, value):
    self.maxHeight(obj, value)
    self.maxWidth(obj, value)
    
#================================================================================
#    Single object and variable constraints
#================================================================================

  def fixedHeight(self, obj, value):
    self.valueConstraint(obj, obj.qcH, EQ, value)
    
  def minHeight(self, obj, value):
    self.valueConstraint(obj, obj.qcH, GE, value)
    
  def maxHeight(self, obj, value):
    self.valueConstraint(obj, obj.qcH, LE, value)
    
  def fixedWidth(self, obj, value):
    self.valueConstraint(obj, obj.qcW, EQ, value)
    
  def minWidth(self, obj, value):
    self.valueConstraint(obj, obj.qcW, GE, value)
    
  def maxWidth(self, obj, value):
    self.valueConstraint(obj, obj.qcW, LE, value)
    
  def fixedX(self, obj, value):
    self.valueConstraint(obj, obj.qcX, EQ, value)
    
  def minX(self, obj, value):
    self.valueConstraint(obj, obj.qcX, GE, value)
    
  def maxX(self, obj, value):
    self.valueConstraint(obj, obj.qcX, LE, value)
    
  def fixedY(self, obj, value):
    self.valueConstraint(obj, obj.qcY, EQ, value)
    
  def minY(self, obj, value):
    self.valueConstraint(obj, obj.qcY, GE, value)
    
  def maxY(self, obj, value):
    self.valueConstraint(obj, obj.qcY, LE, value)
    
#================================================================================
#  Insideness Constraints
#================================================================================
  def inside(self, objTuple):
    self.insideHorizontal(objTuple, (0, 0))
    self.insideVertical(objTuple, (0, 0))
    
  def insideMargins(self, objTuple, marginsTuple):
    self.insideHorizontal(objTuple, marginsTuple[:2])
    self.insideVertical(objTuple, marginsTuple[2:])
    
  def insideX(self, objTuple):
    self.insideHorizontal(objTuple, (0, 0))
    
  def insideY(self, objTuple):
    self.insideVertical(objTuple, (0, 0))
    
#=============================================================================
#  Overlap constraints
#=============================================================================  
  def overlap(self, objTuple):
    #todo: test
    self.horizonalConstraint(objTuple, 0, EQ, (0, 0)) 
    self.verticalConstraint(objTuple, 0, EQ, (0, 0)) 
    source = objTuple[0]
    target = objTuple[1]
    link = objTuple[2]
    self.variableRelationConstraint(link, source.qcW, target.qcW, EQ, 0)
    self.variableRelationConstraint(link, source.qcH, target.qcH, EQ, 0)
    
  def overlapMargins(self, objTuple, marginsTuple):
    pass
    #todo: overlapMargins
  
  
#==============================================================================
#  Bounding Constraints (like the left/right/top/bottom but with widith/height)
#==============================================================================

  def boundLeft(self, objTuple, offset=0):
    """ Object1 lies left of object2 with exact distance, same height sides"""   
    self.horizonalConstraint(objTuple, offset, EQ, (1.0, 0))  
    self.SameH(objTuple)
    
  def boundRight(self, objTuple, offset=0):
    """Object1 lies right of object2 with exact distance, same height sides"""   
    self.horizonalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                        offset, EQ, (1.0, 0))  
    self.SameH(objTuple)
    
  def boundTop(self, objTuple, offset):
    """ Object1 lies top of object2 with exact distance, same width sides """   
    self.verticalConstraint(objTuple, offset, EQ, (1.0, 0))  
    self.SameW(objTuple)
    
  def boundBottom(self, objTuple, offset):
    """ Object1 lies below of object2 with exact distance, same width sides"""   
    self.verticalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                        offset, EQ, (1.0, 0))  
    self.SameW(objTuple)
    
#================================================================================
#    Anchor constraints
#================================================================================
  def AnchorRight(self, objTuple, offset):
    """ Object1 lies right of object2 with exact distance, and lies within the
    vertical space occupied by object2 """   
    self.horizonalConstraint(objTuple, offset, EQ, (1.0, 0)) 
    self.insideY(objTuple)
    
  def AnchorLeft(self, objTuple, offset):
    """ Object1 lies left of object2 with exact distance, and lies within the
    vertical space occupied by object2 """   
    self.horizonalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                        offset, EQ, (1.0, 0)) 
    self.insideY(objTuple)

  def AnchorTop(self, objTuple, offset):
    """ Object1 lies top of object2 with exact distance, and lies within the
    horizontal space occupied by object2 """   
    self.verticalConstraint(objTuple, offset, EQ, (1.0, 0)) 
    self.insideX(objTuple)
    
  def AnchorBottom(self, objTuple, offset):
    """ Object1 lies below object2 with exact distance, and lies within the
    horizontal space occupied by object2 """   
    self.verticalConstraint((objTuple[1], objTuple[0], objTuple[2]), 
                                                       offset, EQ, (1.0, 0)) 
    self.insideX(objTuple)
  