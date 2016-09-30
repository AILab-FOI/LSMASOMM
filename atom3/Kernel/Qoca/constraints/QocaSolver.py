"""
QocaSolver.py

This is a wrapper around the Java implementation of the QOCA constraint toolkit
Created Summer 2005 by Denis Dube
"""
 
from QocaConstants import *
from QocaVariable import QocaVariable
from QocaLinearConstraint import QocaLinearConstraint
from QocaSolverAbstract import QocaSolverAbstract
from Qoca.client.PipeQocaClient import PipeQocaClient
from Qoca.client.TcpQocaClient import TcpQocaClient
 

class QocaSolver(QocaSolverAbstract):
  
#--------------------------------- Init/Final ----------------------------------
    
  def __init__(self, pipeMode=True, command='java -jar D:\QocaServerB1.jar', 
               ip=None, port=None, solverType=SOLVER_CASS):
    QocaSolverAbstract.__init__(self)
    
    self.pipeMode = pipeMode
    self.command = command
    self.ip = ip
    self.port = port
    self.solverType = solverType
    
    self.client = None
    
    # Local bind to the mapping of variable names to variable instances
    self.varMap = QocaVariable.Name2VarDict
    
    # Keep track of active state, if QOCA fails, can restore everything with this
    self.activeVariables = []
    self.activeEditVariables = []
    self.activeConstraints = []
    
    # Boolean flags
    self.isConnected = False
    self.canAddEditVars = False
    
    # Default weights, of dubious robustness
    self.stayWeight = 8
    self.editWeight = 512
    self.fixedWeight = 65536
          
    # Set True for print spam
    self.debug = False
          
  def isAbstract(self):
    return False
                    
  def connect(self):
    """ Connects to the Java QOCA toolkit via pipe or TCP/IP, selects solver """
    
    if(self.isConnected):
      try:
        self.client.write('\n')  
        print 'WARNING: Attempted to connect when connection alive and well'
        return
      except IOError:
        self.isConnected = False
    
    if(self.pipeMode):
      self.client = PipeQocaClient(self.command)
    elif(self.ip != None and self.port != None):
      self.client = TcpQocaClient(self.ip, self.port)
    else:
      raise Exception, 'Bad arguments'
      
       
    # todo: should I give exception on connect failure?
    if(not self.client.connect()):      
      raise Exception, 'QOCA connection failure'
    
    # Create a new instance of the chosen solver... [Cassowary, Equality, Ineq]
    self.client.write(self.solverType+';\n')
    self.isConnected = True
    return True
       
  def disconnect(self):
    """ Disconnects from the QOCA client """
    if(self.isConnected):
      self.isConnected = False
      result = self.client.disconnect()      
      return result
    return True
    
  def restart(self):
    """ Tries to disconnect, re-connect, and re-store the solver state """
    self.disconnect()
    self.connect()
    
    temp = self.activeVariables
    self.activeVariables = []
    self.addVariables(temp)
    
    temp = self.activeConstraints
    self.activeConstraints = []
    self.addConstraints(temp)
    
    temp = self.activeEditVariables
    self.activeEditVariables = []
    self.addEditVars(temp)
       
#--------------------------------- Add/Remove ----------------------------------
       
          
  def addVariables(self, varList):
    """ 
    Add list of variables to the QOCA solver 
    Input: List of variable instances
    """
    s = ''
    for var in varList:
      if(var in self.activeVariables): 
        continue
      self.activeVariables.append(var)
      s += var.toString(FLOAT_ADD)
    if(self.debug): 
      print 'addVariables', s
    self.client.write(s+'\n')
    
  def delVariables(self, varList):
    """ 
    Remove list of variables from the QOCA solver 
    Input: List of variable instances
    """
    s = ''
    for var in varList:
      # Woops, variable never made it to the solver
      if(var not in self.activeVariables):
        var.removeSelf() 
        continue
      
      s += var.toString(FLOAT_REMOVE)
      
      # Remove from active vars list
      self.activeVariables.remove(var)
      
      # Remove from active editing vars list 
      if(var in self.activeEditVariables):
        self.activeEditVariables.remove(var)
        
      # Remove var from name2variable map
      var.removeSelf() 
            
      # Must destroy constraints that require this variable
      constList = var.getDependents()
      self.delConstraints(constList)    
    if(s != ''):
      self.client.write(s+'\n')
              
  def addConstraints(self, constList):
    """ 
    Add list of constraints to the QOCA solver 
    Input: List of constraint instances
    """
    s = ''
    for const in constList:
      if(const in self.activeConstraints): 
        continue
      const.addDependents() # Keep track of vars this constraint uses
      self.activeConstraints.append(const) # Keep track of active constraints
      s += const.toString(CONSTRAINT_ADD)
    if(self.debug): 
      print 'addConstraints', s
    self.client.write(s+'\n')
      
  def delConstraints(self, constList):
    """ 
    Remove list of constraints from the QOCA solver 
    Input: List of constraint instances
    """
    s = ''
    for const in constList:
      if(const not in self.activeConstraints):
        const.removeSelf() 
        continue
        
      self.activeConstraints.remove(const) # Remove from active constraint list
      const.removeSelf() # Remove var from name2constraint map
      s += const.toString(CONSTRAINT_REMOVE)
    if(s != ''):
      self.client.write(s+'\n')
    
  def changeConstraints(self, constValueList):
    """ 
    Change the right hand side value of a constraint 
    Input: List of (constraint, RHSvalue) tuples
    """
    s = ''
    for (const, value) in constValueList:
      const.changeRHS(value)
      s += CONSTRAINT_CHANGE + ' ' + const.name + ' ' + str(value) + ';'
    self.client.write(s+'\n')
    
#----------------------------------- Editing -----------------------------------
    
  
  def addEditVars(self, varList):
    """ 
    Add list of variables that whose values can be edited to the solver 
    If in edit mode, end edit mode, and load in all the variables
    Input: List of variable instances
    """
    
    # We have already called Edit Begin, no new variables can be added O_O
    if(not self.canAddEditVars):
      self.client.write(EDIT_END + ';')
      self.canAddEditVars = True
      varList = self.activeEditVariables + varList
      self.activeEditVariables = []
      self.addEditVars(varList) # But we can add them all back in! W00t!
      return     

    activateVarList = []
    s = ''
    for var in varList:
      # Is the variable already in edit mode?
      if(var in self.activeEditVariables): 
        ##raise Exception, 'Variable already being edited' + var.name
        continue
      # Has the variable been sent to the QOCA solver?
      if(var not in self.activeVariables):
        activateVarList.append(var)
      # Okay, the var is in edit mode now
      self.activeEditVariables.append(var)
      s += EDIT_ADDVAR + ' ' + var.name + ';'
    # Add variables not already defined on the QOCA solver first!
    if(activateVarList):
      self.addVariables(activateVarList)
    self.client.write(s+'\n')
    
  def suggestNameValue(self, varnameValueList):
    """ 
    Change the desired value for the given variable name strings
    The variable in question must have already been sent to addEditVars()
    If not it will be automatically added to the editable variables
    Input: List of (variableNameString, desiredValueFloat) tuples
    """
    s = ''
    if(self.canAddEditVars):
      self.canAddEditVars = False
      s += EDIT_BEGIN + ';'
      
    makeEditableVars = []
    for (varname, value) in varnameValueList:
      if(varname in self.varMap):
        var = self.varMap[varname]
        if(var not in self.activeEditVariables):   
          makeEditableVars.append(var)
        s += EDIT_SUGGEST + " " + varname + " " + str(value) + ";"
      else:
        raise Exception, 'Variable name '+varname+'does not exist'
       
    # Super-convenience, if try to suggest non-editable var, make it editable
    if(makeEditableVars):       
      self.addEditVars(makeEditableVars)    
    self.client.write(s+'\n')  
    
  def suggestVarValue(self, varValueList):
    """ 
    Change the desired value for the given variables
    The variable in question must have already been sent to addEditVars()
    If not it will be automatically added to the editable variables
    Input: List of (variableInstance, desiredValueFloat) tuples
    """
    s = ''
    if(self.canAddEditVars):
      self.canAddEditVars = False
      s += EDIT_BEGIN + ';'
      
    makeEditableVars = []
    for (var, value) in varValueList:
      if(var not in self.activeEditVariables):      
        makeEditableVars.append(var)  
      s += EDIT_SUGGEST + " " + var.name + " " + str(value) + ";" 
        
    # Super-convenience, if try to suggest non-editable var, make it editable
    if(makeEditableVars): 
      self.addEditVars(makeEditableVars)

    self.client.write(s+'\n')  
        
  def endEdit(self):
    """ Call this when done editing values of variables """
    self.canAddEditVars = True
    self.activeEditVariables = []
    self.client.write(EDIT_END + ';\n')
    
#------------------------------- Solve/Re-Solve --------------------------------
     
  #todo: implement dirty bit to indicate if anything changed since last solve
  def solve(self, forceSolve=False):
    """ Use after add/remove variables/constraints """
    if(self.activeConstraints or forceSolve):
      self.client.write(SOLVER_SOLVE + ';' + SOLVER_GET_CHANGED + '\n')
      self.parse(self.client.read())
  
  def resolve(self, forceSolve=False):
    """ Use after editing variables (suggesting new values) """
    if(self.activeConstraints or forceSolve):
      self.client.write(SOLVER_RESOLVE + ';' + SOLVER_GET_CHANGED + '\n')
      self.parse(self.client.read())
           
  def solveAll(self, forceSolve=False):
    """ Use after add/remove variables/constraints """
    if(self.activeConstraints or forceSolve):
      self.client.write(SOLVER_SOLVE + ';' + SOLVER_GET_ALL + '\n')
      self.parse(self.client.read())
  
  def resolveAll(self, forceSolve=False):
    """ Use after editing variables (suggesting new values) """
    if(self.activeConstraints or forceSolve):
      self.client.write(SOLVER_RESOLVE + ';' + SOLVER_GET_ALL + '\n')
      self.parse(self.client.read())
  
  def parse(self, s):
    """ 
    Takes solved string output from QOCA and updates Python variables 
    If the variable has a callback, then the update will trigger it
    """
    if(self.debug): 
      print 'parsing', s
    if(s is None):
      print 'ERROR! Connection lost'
      self.restart()
      return 
    # 'x 10.0;z 30.0;w 10.0;y 29.0;\n'
    lineList = s.split('\n')
    # ['x 10.0;z 30.0;w 10.0;y 29.0;', '']
    for line in lineList:      
      variableList = line.split(';')
      # ['x 10.0','z 30.0','w 10.0','y 29.0', ''] 
      for variable in variableList:        
        if(variable in ['', '\r', '\f', '\t']): 
          continue
        variableTuple = variable.split(' ')
        # [['x','10.0'],['z','30.0'],['w','10.0'],['y','29.0']] 
        #print 'Your variable is ', variableTuple[0], ' = ', variableTuple[1]
        #self.varMap[varNameString].update(varFloatValue)
        '''
        varNameString = variableTuple[0]
        if(not self.varMap.has_key(varNameString)):
          raise KeyError, 'Variable ' + varNameString + ' does not exist locally' 
        self.varMap[varNameString].update(float(variableTuple[1]))
        '''
        self.varMap[variableTuple[0]].update(float(variableTuple[1]))
        
#------------------------------- Variable Maker --------------------------------
    
  def makeVar(self, name, value, stayWeight=None, editWeight=None, callback=None):
    """ Convenience method to make variables using the solver """
    if(not stayWeight):
      stayWeight = self.stayWeight
    if(not editWeight):
      editWeight = self.editWeight
    if(callback):
      return QocaVariable(name, value, stayWeight, editWeight, callback=callback)
    else:
      return QocaVariable(name, value, stayWeight, editWeight)
  
  def makeFixedVar(self, name, value, fixedWeight=None, callback=None):
    """ Convenience method to make fixed variables using the solver """
    if(not fixedWeight):
      fixedWeight = self.fixedWeight
    if(callback):
      return QocaVariable(name, value, fixedWeight=fixedWeight, callback=callback)  
    else:
      return QocaVariable(name, value, fixedWeight=fixedWeight)  
   
    
  def makeConstraint(self, name, lhsTermsDict, relation, rhsValue):
    """ Convenience method to make constraints using the solver """
    return QocaLinearConstraint(name, lhsTermsDict, relation, rhsValue)
