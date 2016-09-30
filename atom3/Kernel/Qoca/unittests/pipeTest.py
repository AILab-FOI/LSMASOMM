"""
QOCA Client tests

Denis Dube, Summer 2005
"""
import unittest

from Qoca.constraints.QocaConstants import *
from Qoca.client.PipeQocaClient import PipeQocaClient
from Qoca.client.TcpQocaClient import TcpQocaClient


class PipeTest(unittest.TestCase):
  
  command = 'java -jar D:\QocaServerB1.jar' # Start the Java Qoca Toolkit
  stayWeight = str(pow(2, 20))
  editWeight = str(pow(2, 60))
  fixedWeight = str(pow(2, 80))
  client = None

  def checkEquality(self, input, reference):
    """ Parses the two strings into two dictionary maps and compares them """
    def parse(s):
      d = dict()
      # 'x 10.0;z 30.0;w 10.0;y 29.0;\n'
      lineList = s.split('\n')
      # ['x 10.0;z 30.0;w 10.0;y 29.0;', '']
      for line in lineList:      
        variableList = line.split(';')
        # ['x 10.0','z 30.0','w 10.0','y 29.0', ''] 
        for variable in variableList:        
          if(variable == ''): continue
          variableTuple = variable.split(' ')
          d[variableTuple[0]] = float(variableTuple[1])
      return d
    return parse(input) == parse(reference)
    

  def testAConnect(self):
    """ Test pipe connect """
    do_TCP_test_instead = False
    if(do_TCP_test_instead):
      PipeTest.client = TcpQocaClient('127.0.0.1',14059)
    else:
      PipeTest.client = PipeQocaClient(self.command)
    self.assert_(PipeTest.client.connect())
    
  def testBAddVarsConstraints(self):
    """ Test adding variables, constraints, and then solving """
    # Initilize variables: w, x, y, z
    s = SOLVER_CASS +';'
    s += FLOAT_FIXED_ADD + " w 10.0 " + self.fixedWeight + ';'
    s += FLOAT_ADD + " x 10.0 "+self.stayWeight+" "+self.editWeight + ';'
    s += FLOAT_ADD + " y 29.0 "+self.stayWeight+" "+self.editWeight + ';'
    s += FLOAT_ADD + " z 30.0 "+self.stayWeight+" "+self.editWeight + ';'
    
    # Add constraints: w == x; y - x >= 5; y <= z
    s += CONSTRAINT_ADD + " c1 1.0,w,-1.0,x " + EQ + " 0.0" + ';'
    s += CONSTRAINT_ADD + " c2 1.0,x,-1.0,y " + LE + " -5.0" + ';'
    s += CONSTRAINT_ADD + " c3 1.0,z,-1.0,y " + GE + " 0.0" + ';'
    
    # Ask the server to solve and return the solution
    s += SOLVER_SOLVE + ';'
    s += SOLVER_GET_ALL + '\n'
    PipeTest.client.write( s )   
     
    ref = 'x 10.0;z 30.0;w 10.0;y 29.0;\n'
    self.assert_(self.checkEquality(PipeTest.client.read(), ref))
    
  def testCManipulation1(self):
    """ First manipulation, Edit y := 25, SOLVER_RESOLVE."""
    
    s = EDIT_ADDVAR + " y;"
    s += EDIT_BEGIN + ';'
    s += EDIT_SUGGEST + " y 25.0;"
    s += SOLVER_RESOLVE + ';'
    s += SOLVER_GET_ALL + '\n'
    PipeTest.client.write( s )    
    
    ref = 'x 10.0;z 30.0;w 10.0;y 25.0;\n'
    self.assert_(self.checkEquality(PipeTest.client.read(), ref))
    
  def testDManipulation1(self):
    """ Edit y := 15, resolve. """
    s = EDIT_SUGGEST + " y 15.0;"
    s += SOLVER_RESOLVE + ';'
    s += SOLVER_GET_ALL + '\n'
    PipeTest.client.write( s )    
    
    ref = 'x 10.0;z 30.0;w 10.0;y 15.0;\n'
    self.assert_(self.checkEquality(PipeTest.client.read(), ref))
    
  def testEManipulation1(self):
    """ Edit y := 5, resolve. """
    s = EDIT_SUGGEST + " y 5.0;"
    s += SOLVER_RESOLVE + ';'
    s += SOLVER_GET_ALL + '\n'
    PipeTest.client.write( s )    
    
    ref = 'x 10.0;z 30.0;w 10.0;y 15.0;\n'
    self.assert_(self.checkEquality(PipeTest.client.read(), ref))
    
  def testFManipulation1(self):
    """ End edit. """
    s = EDIT_END + ';'
    s += SOLVER_GET_ALL + '\n'
    PipeTest.client.write( s ); 
    
    ref = 'x 10.0;z 30.0;w 10.0;y 15.0;\n'
    self.assert_(self.checkEquality(PipeTest.client.read(), ref))
    
    
    
  def testZDisconnect(self):
    """ Test disconnect pipe """
    self.assert_(PipeTest.client.disconnect())
