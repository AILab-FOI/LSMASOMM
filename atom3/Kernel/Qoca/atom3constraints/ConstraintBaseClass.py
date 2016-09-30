"""
ConstraintBaseClass.py

"""

from Qoca.constraints.QocaConstants import EQ, LE, GE
from Qoca.constraints.QocaVariable import QocaVariable
from Qoca.constraints.QocaLinearConstraint import QocaLinearConstraint


class ConstraintBaseClass:
    
  def __init__(self, solver, resolve):
    self.solver = solver
    self.autoResolveFlag = resolve


    
  def resolve(self):
    self.solver.resolve()
    
    
    
  def horizonalConstraint(self, objTuple, offset, relation, percentTuple):
    """ 
    Generic horizontal constraint 
    Offset directly changes the horizontal position by pixels
    Relation chooses between ==, <=, or >= (EQ, LE, GE)
    percentTuple adds in a percentage of the width of the source and target
    """
    objA = objTuple[0] # Entity A
    objB = objTuple[1] # Entity B
    objC = objTuple[2] # Relation connecting Entity A to Entity B
      
#============================================================================
#    Constraint is a name string, terms dictionary, relation operator string,
#    equation right hand side value float
#    -A.x0 + B.x0 = A.width * percentage + offset
#============================================================================
    newConstraintList = [ QocaLinearConstraint(
                  'CX'+str(QocaLinearConstraint.UniqueID), 
                  {objA.qcX.name : -1.0, 
                   objB.qcX.name : 1.0,
                   objA.qcW.name : -percentTuple[0],
                   objB.qcW.name : -percentTuple[1]}, 
                  relation, 
                  offset)  ]
    

    # Make variables active
    self.solver.addVariables([objA.qcX, objA.qcW, objB.qcX, objB.qcW])
    
    # Make constraints active
    self.solver.addConstraints(newConstraintList)
    objC.qocaConstraints.extend(newConstraintList) # If link dies, del consts
    
    # Re-compute layout situation
    if(self.autoResolveFlag): 
      self.solver.resolve()
    
    
  def verticalConstraint(self, objTuple, offset, relation, percentTuple):
    """ 
    Generic vertical constraint 
    Offset directly changes the vertical position by pixels
    Relation chooses between ==, <=, or >= (EQ, LE, GE)
    percentTuple adds in a percentage of the height of the source and target
    """
    objA = objTuple[0] # Entity A
    objB = objTuple[1] # Entity B
    objC = objTuple[2] # Relation connecting Entity A to Entity B
    
#============================================================================
#    Constraint is a name string, terms dictionary, relation operator string,
#    equation right hand side value float
#    -A.y0 + B.y0 = A.height * percentage + offset
#    -A.y0 -A.height * percentageA + B.y0 -B.height * percentageB = offset
#============================================================================
    newConstraintList = [QocaLinearConstraint(
                          'CY'+str(QocaLinearConstraint.UniqueID), 
                          {objA.qcY.name:-1.0, objB.qcY.name:1.0,
                           objA.qcH.name:-percentTuple[0],
                           objB.qcH.name:-percentTuple[1]}, 
                          relation, 
                          offset)
    ]

    # Make variables active
    self.solver.addVariables([objA.qcY, objA.qcH, objB.qcY, objB.qcH])
    
    # Make constraints active
    self.solver.addConstraints(newConstraintList)
    objC.qocaConstraints.extend(newConstraintList) # If link dies, del consts
    
    # Re-compute layout situation
    if(self.autoResolveFlag): 
      self.solver.resolve()
    
    
  def insideHorizontal(self, objTuple, offsetTuple):
    """
    Generic horinzontal insidness constraint --> A is inside B horizontally
    (margin1, margin2) = offsetTuple
    
    The source object(A) will be to the right of the target (B) plus margin1
    For both objects, this is taken from their left hand sides
    
    The source object(A) will be to the left of the target (B) minus margin2
    For both objects, this is taken from their right hand sides
    """
#================================================================================
#     QUICK REFERENCE
#      b.x > a.x + margin
#      b.x + b.w < a.x + a.w - margin
#     OR
#     -a.x + b.x > margin
#     -a.x - a.w + b.x + b.w < -margin
#================================================================================
        
    objA = objTuple[0] # Entity A
    objB = objTuple[1] # Entity B
    objC = objTuple[2] # Relation connecting Entity A to Entity B
    
    newConstraintList = [ 
                  QocaLinearConstraint(
                  'CX'+str(QocaLinearConstraint.UniqueID), 
                  {objA.qcX.name:-1.0, objB.qcX.name:1.0}, 
                  GE, 
                  offsetTuple[0]),
                  QocaLinearConstraint(
                  'CX'+str(QocaLinearConstraint.UniqueID), 
                  {objA.qcX.name:-1.0, objA.qcW.name:-1.0,
                   objB.qcX.name:1.0, objB.qcW.name:1.0}, 
                  LE, 
                  - offsetTuple[1])   ]

    # Make variables active
    self.solver.addVariables([objA.qcX, objA.qcW, objB.qcX, objB.qcW])
    
    # Make constraints active
    self.solver.addConstraints(newConstraintList)
    objC.qocaConstraints.extend(newConstraintList) # If link dies, del consts
    
    # Re-compute layout situation
    if(self.autoResolveFlag): 
      self.solver.resolve()


  def insideVertical(self, objTuple, offsetTuple):
    """
    Generic horinzontal insidness constraint
    (margin1, margin2) = offsetTuple
    The source object(A) will be below target (B) plus margin1
    For both objects, this is taken from their tops
    
    The source object(A) will be above target (B) minus margin2
    For both objects, this is taken from their bottoms
    """
#================================================================================
#     QUICK REFERENCE
#      b.y > a.y + margin
#      b.y + b.h < a.y + a.h - margin
#     OR
#     -a.y + b.y > margin
#     -a.y - a.h + b.y + b.h < -margin
#================================================================================
        
    objA = objTuple[0] # Entity A
    objB = objTuple[1] # Entity B
    objC = objTuple[2] # Relation connecting Entity A to Entity B
    
    newConstraintList = [ 
                  QocaLinearConstraint(
                  'CY'+str(QocaLinearConstraint.UniqueID), 
                  {objA.qcY.name:-1.0, objB.qcY.name:1.0}, 
                  GE, 
                  offsetTuple[0]),
                  QocaLinearConstraint(
                  'CY'+str(QocaLinearConstraint.UniqueID), 
                  {objA.qcY.name:-1.0, objA.qcH.name:-1.0,
                   objB.qcY.name:1.0, objB.qcH.name:1.0}, 
                  LE, 
                  - offsetTuple[1])   ]

    # Make variables active
    self.solver.addVariables([objA.qcY, objA.qcH, objB.qcY, objB.qcH])
    
    # Make constraints active
    self.solver.addConstraints(newConstraintList)
    objC.qocaConstraints.extend(newConstraintList) # If link dies, del consts
    
    # Re-compute layout situation
    if(self.autoResolveFlag): 
      self.solver.resolve()


  def valueConstraint(self, obj, var, relation, value):
    """
    Use this to fix an object's variable to a specific value, a minimum value
    or a maximum value (Depending on relation: EQ, LE, GE).
    """
#================================================================================
#    Quick Reference 
#    var = value
#================================================================================
    newConstraintList = [ 
                  QocaLinearConstraint(
                  'CF'+str(QocaLinearConstraint.UniqueID), 
                  {var.name:1.0}, 
                  relation, 
                  value)      ]

    # Make variables active
    self.solver.addVariables([var])
    
    # Make constraints active
    self.solver.addConstraints(newConstraintList)
    # If object dies, delete constraints
    obj.qocaConstraints.extend(newConstraintList) 
    
    # Re-compute layout situation
    if(self.autoResolveFlag): 
      self.solver.resolve()


  def variableRelationConstraint(self, obj, var1, var2, relation, value):
    """
    Used to set a specific relation between 2 QOCA variables
    The obj argument will hold the constraint so when deleted, constraint dies
    """
#================================================================================
#    Quick Reference 
#    -var1 + var2 = value
#================================================================================
    newConstraintList = [ 
                  QocaLinearConstraint(
                  'CF'+str(QocaLinearConstraint.UniqueID), 
                  {var1.name : -1.0,
                   var2.name : 1.0}, 
                  relation, 
                  value)      ]

    # Make variables active
    self.solver.addVariables([var1, var2])
    
    # Make constraints active
    self.solver.addConstraints(newConstraintList)
    # If object dies, delete constraints
    obj.qocaConstraints.extend(newConstraintList) 
    
    # Re-compute layout situation
    if(self.autoResolveFlag): 
      self.solver.resolve()
    
      

    
      