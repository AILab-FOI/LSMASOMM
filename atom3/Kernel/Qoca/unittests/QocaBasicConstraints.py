"""
QocaBasicConstraints.py
"""
import unittest

from Qoca.constraints.QocaLinearConstraint import QocaLinearConstraint
from Qoca.constraints.QocaConstants import *
from Qoca.constraints.QocaVariable import QocaVariable 
from Qoca.constraints.QocaSolver import QocaSolver 

class QocaBasicConstraints(unittest.TestCase):
    
#------------------------------------ setup ------------------------------------
        
    def setUp(self):
      self.v1 = QocaVariable('rect.x', 10.5, 100, 1000)
      self.v2 = QocaVariable('rect.y', 2.0, 100, 1000)
      terms = {'rect.x':5.5, 'rect.y':-3.72}
      self.l1 = QocaLinearConstraint('bigRect', terms, GE, 50.0)
      
    def tearDown(self):
      self.v1.removeSelf()
      self.v2.removeSelf()
      self.l1.removeSelf() ## Not needed anymore, removing var takes care of it
      
#------------------------------------ tests ------------------------------------
          
    def testVariableGet(self):      
      """ Check the QocaVariable get method works """
      self.assertEqual(10.5, self.v1.get())
      
    def testVariableSTR(self):     
      """ Check the QocaVariable string method works """
      self.assertEqual(str(self.v1), 'rect.x = 10.5')
        
    def testConstraintSTR(self):     
      """ Check the QocaLinearConstraint string method works """
      self.assertEqual(str(self.l1), 'bigRect: 5.5*rect.x + -3.72*rect.y >= 50.0')
    
    def testQocaSolverParser(self):
      """ Make sure the parser in QocaSolver works on 'rect.x 10.0;rect.y 30.0;\n' """
      q = QocaSolver()
      q.parse('rect.x 10.0;rect.y 30.0;\n')
      
    def testQocaSolverParserFailure(self):
      """ Make sure the parser in QocaSolver fails on 'bogusVar 5.0;\n' """
      q = QocaSolver()
      self.assertRaises( KeyError, q.parse, 'bogusVar 5.0;\n' )

    
#-------------------------------- end of tests ---------------------------------    