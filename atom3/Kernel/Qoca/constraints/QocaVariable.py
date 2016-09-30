"""
QocaVariable.py

Created Summmer 2005, Denis Dube
"""
from QocaConstants import *
 
class QocaVariable:
  
  Name2VarDict = dict()
  
#--------------------------------- Constructor ---------------------------------
    
  def __init__(self, name, value, stayWeight=None, editWeight=None, 
               fixedWeight=None, callback=None):
    self.name = name # WARNING: This member is directly accessed externally
    self.solverValue = value
    
    if(stayWeight and editWeight):
      self.stayWeight = stayWeight
      self.editWeight = editWeight
    elif(fixedWeight):
      self.stayWeight = fixedWeight
      self.editWeight = fixedWeight
    else:
      raise Exception, 'Bad arguments to QocaVariable'
      
    # Call this function if solution changes with the changed value as paramater
    if(callback):
      self.callback = callback
    else:
      self.resetCallback()

    #print 'varname created', name
    if(QocaVariable.Name2VarDict.has_key(name)):
      #print QocaVariable.Name2VarDict
      raise Exception, 'Variable '+name+' already exists'
    else:
      QocaVariable.Name2VarDict[name] = self
      
    # Constraints dependent on this variable, list of instances with removeSelf()
    self.dependents = []
    
    self.isDeleted = False
      
#----------------------------------- Cleanup -----------------------------------

  def addDependent(self, constraint):
    """ A constraint using this variable """
    self.dependents.append(constraint)
    
  def getDependents(self):
    """ Return all constraints dependent on this variable """
    return self.dependents
      
  def delDependent(self, constraint):
    """ Remove constraint formerly using this variable """
    if(constraint in self.dependents):
      self.dependents.remove(constraint)
    
  def remove(self, name):
    if(QocaVariable.Name2VarDict.has_key(name)):
      del QocaVariable.Name2VarDict[name]
    self.isDeleted = True

  def removeSelf(self):
    self.remove(self.name)
      
#----------------------------------- Methods -----------------------------------

       
  def get(self):
    if(self.isDeleted): 
      raise Exception, "Variable is deleted: " + self.name
    return self.solverValue
  
  
  def toString(self, command):    
    """ String compatible with the message parser for Java QOCA """  
    #return FLOAT_ADD + " z 30.0 "+self.stayWeight+" "+self.editWeight + ';'
    if(self.isDeleted): 
      raise Exception, "Variable is deleted: " + self.name
    return command + " " + self.name + " " + str(self.solverValue) + " " \
                     + str(self.stayWeight) + " " + str(self.editWeight) + ';'
  
  
  def __str__(self):
    if(self.isDeleted): 
      raise Exception, "Variable is deleted: " + self.name
    return str(self.name) + ' = ' + str(self.solverValue)
    
    
#---------------------------------- Callbacks ----------------------------------
    
  # Call method when variable is changed
  def registerCallback(self, callback):
    self.callback = callback
    
    
    
  def resetCallback(self):
    self.callback = lambda x:x
    
    
    
  def update(self, solvedValue):
    # print 'update', self.name, solvedValue
    if(self.isDeleted): 
      raise Exception, "Variable is deleted: " + self.name
    self.solverValue = solvedValue
    self.callback(solvedValue)
  
