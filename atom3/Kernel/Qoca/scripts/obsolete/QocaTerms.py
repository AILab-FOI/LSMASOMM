#----------------------------- WARNING: DEAD FILE ------------------------------

#------------------------------- NO LONGER USED --------------------------------


class QocaTerms:
  """
  Use this to build up the LHS of a Qoca linear constraint
  """
  def __init__(self):
    self.terms = dict()
    
  def addTerm(self, coefficient, variable):
    """
    Term needs to be unique 
    coefficient should be integer or double
    variable should be a QocaVariable
    """
    if(self.terms.has_key(variable)):
      raise Exception, 'Variable '+str(variable)+' is already in the terms'
    else:
      self.terms[variable] = coefficient
      
      
  def removeVariable(self, variable):
    if(self.terms.has_key(variable)):
      del self.terms[variable]
      
      
  def toString(self):
    """ String compatible with the message parser for Java QOCA """
    #s += CONSTRAINT_ADD + " c1 1.0,w,-1.0,x " + EQ + " 0.0" + ';'
    s = ''
    for (variable, coefficient) in self.terms.items():
      s += ',' + str(coefficient) + ',' + variable.name
    return s[1:]
      
  def __str__(self):
    s = ''
    for (variable,coefficient) in self.terms.items():
      s += ' + ' + str(coefficient) + '*' + variable.name
    return s[3:]  
    