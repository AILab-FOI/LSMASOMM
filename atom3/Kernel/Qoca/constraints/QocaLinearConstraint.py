from QocaConstants import *
from QocaVariable import QocaVariable


class QocaLinearConstraint:
  
  UniqueID = 0
  name2ConstraintMap = dict()
  
  def __init__(self, name, lhsTermsDict, relation, rhsValue):
    """
    name should be a string, 
    lhsTerms should be type dictionary,
    relation should be EQ, LE, or GE from QocaConstants
    rhsValue should be integer/double
    """
    QocaLinearConstraint.UniqueID += 1
    
    self.name = name # WARNING: subject to direct external access
    self.lhsTermsDict = lhsTermsDict # {varNameString : coefficientFloat, etc..}
    self.relation = relation
    self.rhsValue = rhsValue # WARNING: subject to direct external access
    
    self.varMap = QocaVariable.Name2VarDict
    if(self.isValid()):
      QocaLinearConstraint.name2ConstraintMap[name] = self

        
  def isValid(self):
    """ Make sure this is a valid constraint """
    
    if(self.relation not in [EQ, LE, GE]):
      raise Exception, 'Bad relation, should be EQ, LE, or GE in QocaConstants'
    
    # Ensure term is unique
    if(QocaLinearConstraint.name2ConstraintMap.has_key(self.name)):
      raise Exception, 'Constraint name already defined'
    
    """ Check that the terms use defined variables """
    #todo: WARNING: variable defined but maybe not sent to Java QOCA solver
    for varNameString in self.lhsTermsDict.keys():
      if(not self.varMap.has_key(varNameString)):
        raise Exception, 'LHS term uses a variable that is not defined'
    return True
  
  def addDependents(self):
    """ This constraint only makes sense if the vars it depends on exist """
    for varNameString in self.lhsTermsDict.keys():
      var = self.varMap[varNameString]
      var.addDependent(self)
          
  def remove(self, name):
    if(QocaLinearConstraint.name2ConstraintMap.has_key(name)):
      del QocaLinearConstraint.name2ConstraintMap[name]
    
    for varNameString in self.lhsTermsDict.keys():
      if(varNameString in self.varMap):
        var = self.varMap[varNameString]
        var.delDependent(self)

      
  def removeSelf(self):
    self.remove(self.name)
    
  def changeRHS(self, val):
    self.rhsValue = val
  
#---------------------------- Constraint to string -----------------------------
      
  def toString(self, command):
    """ String compatible with the message parser for Java QOCA """
    #s += CONSTRAINT_ADD + " c1 1.0,w,-1.0,x " + EQ + " 0.0" + ';'
    return command + " " + self.name + ' ' \
                   + self.__LHS2String() \
                   + " " + self.relation + " " + str(self.rhsValue) + ';'
    
  def __str__(self):
    """ Pretty print """
    return self.name + ': ' + self.__LHS2Str() + ' ' \
          + RELATION_ENUM[self.relation] + ' ' + str(self.rhsValue)
    
    
#-------------------------- LHS terms utility methods --------------------------
               
      
  def __LHS2String(self):
    """ String compatible with the message parser for Java QOCA """
    #s += CONSTRAINT_ADD + " c1 1.0,w,-1.0,x " + EQ + " 0.0" + ';'
    s = ''
    for (variable, coefficient) in self.lhsTermsDict.items():
      s += ',' + str(coefficient) + ',' + variable #.name
    return s[1:]
      
  def __LHS2Str(self):
    """ Pretty print """
    s = ''
    for (variable, coefficient) in self.lhsTermsDict.items():
      s += ' + ' + str(coefficient) + '*' + variable #.name
    return s[3:]  
    
    

