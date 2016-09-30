"""
QocaSolverAbstract.py

This is an abstract wrapper around the Java implementation of the QOCA 
constraint toolkit
If the user wishes to disable QOCA solving, instantiating this implementation
free class is an easy way to achieve this...

Created Summer 2005 by Denis Dube
""" 

def getSolver():
  """ Return the one and only solver instance (could be concrete or abstract)"""
  return QocaSolverAbstract.SOLVER_INSTANCE

def isAbstract():
  from QocaSolver import QocaSolver
  return not isinstance(QocaSolverAbstract.SOLVER_INSTANCE, QocaSolver)

class QocaSolverAbstract:
  
  SOLVER_INSTANCE = None
  
#--------------------------------- Init/Final ----------------------------------
    
  def __init__(self):
    QocaSolverAbstract.SOLVER_INSTANCE = self
    
  def isAbstract(self):
    return True
                    
  def connect(self):
    """ Connects to the Java QOCA toolkit via pipe or TCP/IP, selects solver """
    return True
       
  def disconnect(self):
    """ Disconnects from the QOCA client """   
    return True
    
  def restart(self):
    """ Tries to disconnect, re-connect, and re-store the solver state """
    pass
       
#--------------------------------- Add/Remove ----------------------------------
       
          
  def addVariables(self, varList):
    """ 
    Add list of variables to the QOCA solver 
    Input: List of variable instances
    """
    pass
    
  def delVariables(self, varList):
    """ 
    Remove list of variables from the QOCA solver 
    Input: List of variable instances
    """
    pass
              
  def addConstraints(self, constList):
    """ 
    Add list of constraints to the QOCA solver 
    Input: List of constraint instances
    """
    pass
      
  def delConstraints(self, constList):
    """ 
    Remove list of constraints from the QOCA solver 
    Input: List of constraint instances
    """
    pass
    
  def changeConstraints(self, constValueList):
    """ 
    Change the right hand side value of a constraint 
    Input: List of (constraint, RHSvalue) tuples
    """
    pass
    
#----------------------------------- Editing -----------------------------------
    
  
  def addEditVars(self, varList):
    """ 
    Add list of variables that whose values can be edited to the solver 
    If in edit mode, end edit mode, and load in all the variables
    Input: List of variable instances
    """
    pass
    
  def suggestNameValue(self, varnameValueList):
    """ 
    Change the desired value for the given variable name strings
    The variable in question must have already been sent to addEditVars()
    If not it will be automatically added to the editable variables
    Input: List of (variableNameString, desiredValueFloat) tuples
    """
    pass
    
  def suggestVarValue(self, varValueList):
    """ 
    Change the desired value for the given variables
    The variable in question must have already been sent to addEditVars()
    If not it will be automatically added to the editable variables
    Input: List of (variableInstance, desiredValueFloat) tuples
    """
    pass
        
  def endEdit(self):
    """ Call this when done editing values of variables """
    pass
    
#------------------------------- Solve/Re-Solve --------------------------------
     
  def solve(self):
    """ Use after add/remove variables/constraints """
    return None
  
  def resolve(self):
    """ Use after editing variables (suggesting new values) """
    return None
           
  def solveAll(self):
    """ Use after add/remove variables/constraints """
    return None
  
  def resolveAll(self):
    """ Use after editing variables (suggesting new values) """
    return None
  
  def parse(self, s):
    """ 
    Takes solved string output from QOCA and updates Python variables 
    If the variable has a callback, then the update will trigger it
    """
    return None
        
#------------------------------- Variable Maker --------------------------------
    
  def makeVar(self, name, value, stayWeight=None, editWeight=None, callback=None):
    """ Convenience method to make variables using the solver """
    return None
  
  def makeFixedVar(self, name, value, fixedWeight=None, callback=None):
    """ Convenience method to make fixed variables using the solver """
    return None   
    
  def makeConstraint(self, name, lhsTermsDict, relation, rhsValue):
    """ Convenience method to make constraints using the solver """
    return None
