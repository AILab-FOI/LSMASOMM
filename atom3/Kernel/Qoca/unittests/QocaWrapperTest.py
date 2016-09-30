"""
QocaWrapperTest.py

Denis Dube, Summer 2005
"""


import unittest

from Qoca.constraints.QocaConstants import *
from Qoca.constraints.QocaSolver import QocaSolver
from Qoca.constraints.QocaVariable import QocaVariable
from Qoca.constraints.QocaLinearConstraint import QocaLinearConstraint


class QocaWrapperTest(unittest.TestCase):
  
  stayWeight = str(pow(2, 20))
  editWeight = str(pow(2, 60))
  fixedWeight = str(pow(2, 80))
  solver = None
  
  def testA(self):
    """ Check if connect works """
    # NOTE: TCP means you have to start server manually
    do_TCP_test_instead = False 
    if(do_TCP_test_instead):
      QocaWrapperTest.solver = QocaSolver(pipeMode=False, solverType=SOLVER_CASS,
                             ip='127.0.0.1', port=14059)
    else:
      QocaWrapperTest.solver = QocaSolver(pipeMode=True, solverType=SOLVER_CASS,
                             command='java -jar D:\QocaServerB1.jar')
    self.assert_(QocaWrapperTest.solver.connect())
  
  def testB(self):
    """ Check if adding variables works """
    w = QocaVariable('w',10.0, fixedWeight=self.fixedWeight)
    x = QocaVariable('x',10.0, self.stayWeight, self.editWeight)
    y = QocaVariable('y',29.0, self.stayWeight, self.editWeight)
    z = QocaVariable('z',30.0, self.stayWeight, self.editWeight)
    QocaWrapperTest.solver.addVariables([w,x,y,z])
  
  
  def testC(self):
    """ Check if adding constraints works """
    c1 = QocaLinearConstraint('c1', {'w':1.0, 'x':-1.0}, EQ, 0.0)
    c2 = QocaLinearConstraint('c2', {'x':1.0, 'y':-1.0}, LE, -5.0)
    c3 = QocaLinearConstraint('c3', {'z':1.0, 'y':-1.0}, GE, 0.0)
    QocaWrapperTest.solver.addConstraints([c1, c2, c3])
  
  def testD(self):
    """ Check if solving works """
    QocaWrapperTest.solver.solve()
    d = QocaVariable.Name2VarDict
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 29.0)
    self.assertEqual(zVal, 30.0)
  
  def testE(self):
    """ Check if resolve with suggest y=25 works """
    d = QocaVariable.Name2VarDict
    var = d['y']
    QocaWrapperTest.solver.addEditVars([var])
    QocaWrapperTest.solver.suggestVarValue([(var,25.0)])
    QocaWrapperTest.solver.resolve()
    
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 25.0)
    self.assertEqual(zVal, 30.0)
      
  def testF(self):
    """ Check if resolve with suggest y=15 works """
    d = QocaVariable.Name2VarDict
    QocaWrapperTest.solver.suggestNameValue([('y',15.0)])
    QocaWrapperTest.solver.resolve()
    
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 15.0)
    self.assertEqual(zVal, 30.0)
  
  def testG(self):
    """ Check if resolve with suggest y=5 works """
    d = QocaVariable.Name2VarDict
    QocaWrapperTest.solver.suggestNameValue([('y',5.0)])
    QocaWrapperTest.solver.resolve()
    
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 15.0)
    self.assertEqual(zVal, 30.0)
  
  def testH(self):
    """ Check if end edit works """
    QocaWrapperTest.solver.endEdit()
    QocaWrapperTest.solver.resolve()
    
    d = QocaVariable.Name2VarDict
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 15.0)
    self.assertEqual(zVal, 30.0)
    
  def testI(self):
    """ Check if Remove `w == x' constraint, edit x := 15, resolve, works """
    
    constraint = QocaLinearConstraint.name2ConstraintMap['c1']
    QocaWrapperTest.solver.delConstraints([constraint])
    
    d = QocaVariable.Name2VarDict
    var = d['x']
    QocaWrapperTest.solver.addEditVars([var])
    QocaWrapperTest.solver.suggestNameValue([('x',15.0)])
    QocaWrapperTest.solver.resolve()
    
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 15.0)
    self.assertEqual(yVal, 20.0)
    self.assertEqual(zVal, 30.0)
    
  def testJ(self):
    """ Check if resolve with suggest x := 25 works """
    d = QocaVariable.Name2VarDict
    QocaWrapperTest.solver.suggestNameValue([('x',25.0)])
    QocaWrapperTest.solver.resolve()
    
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 25.0)
    self.assertEqual(yVal, 30.0)
    self.assertEqual(zVal, 30.0)
  
  def testK(self):
    """ Check if resolve with suggest x=35 works """
    d = QocaVariable.Name2VarDict
    QocaWrapperTest.solver.suggestNameValue([('x',35.0)])
    QocaWrapperTest.solver.resolve()
    
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 35.0)
    self.assertEqual(yVal, 40.0)
    self.assertEqual(zVal, 40.0)
  
  def testL(self):
    """ Check if end edit works """
    QocaWrapperTest.solver.endEdit()
    QocaWrapperTest.solver.resolve()
    
    d = QocaVariable.Name2VarDict
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 35.0)
    self.assertEqual(yVal, 40.0)
    self.assertEqual(zVal, 40.0)
    
  def testM(self):
    """ Check if Re-add constraint `w == x', solve, works """
    c1 = QocaLinearConstraint('c1', {'w':1.0, 'x':-1.0}, EQ, 0.0)
    QocaWrapperTest.solver.addConstraints([c1])
    QocaWrapperTest.solver.solve()

    d = QocaVariable.Name2VarDict
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 40.0)
    self.assertEqual(zVal, 40.0)
    
  def testN(self):
    """ Check if resolve with suggest z=25 works """
    d = QocaVariable.Name2VarDict
    var = d['z']
    QocaWrapperTest.solver.addEditVars([var])
    QocaWrapperTest.solver.suggestNameValue([('z',25.0)])
    QocaWrapperTest.solver.resolve()
    
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 25.0)
    self.assertEqual(zVal, 25.0)
    
  def testO(self):
    """ Check if resolve with suggest z=15 works """
    d = QocaVariable.Name2VarDict
    QocaWrapperTest.solver.suggestNameValue([('z',15.0)])
    QocaWrapperTest.solver.resolve()
    
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 15.0)
    self.assertEqual(zVal, 15.0)

  def testP(self):
    """ Check if resolve with suggest z=5 works """
    d = QocaVariable.Name2VarDict
    QocaWrapperTest.solver.suggestNameValue([('z',5.0)])
    QocaWrapperTest.solver.resolve()
    
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 15.0)
    self.assertEqual(zVal, 15.0)
    
  def testQ(self):
    """ Check if end edit works """
    QocaWrapperTest.solver.endEdit()
    QocaWrapperTest.solver.resolve()
    
    d = QocaVariable.Name2VarDict
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 15.0)
    self.assertEqual(zVal, 15.0)


  def testR(self):
    """ Check if Change `y - x >= 5' to `>= 10'.  edit y := 25, resolve, works """
    
    constraint = QocaLinearConstraint.name2ConstraintMap['c2']
    QocaWrapperTest.solver.changeConstraints([(constraint,-10.0)])
    
    d = QocaVariable.Name2VarDict
    var = d['y']
    QocaWrapperTest.solver.addEditVars([var])
    QocaWrapperTest.solver.suggestNameValue([('y',25.0)])
    QocaWrapperTest.solver.solve()

    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 20.0)
    self.assertEqual(zVal, 20.0)

  def testT(self):
    """ Check if resolve with suggest y=15 works """
    d = QocaVariable.Name2VarDict
    QocaWrapperTest.solver.suggestNameValue([('y',15.0)])
    QocaWrapperTest.solver.resolve()
    
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 20.0)
    self.assertEqual(zVal, 20.0)
    
  def testU(self):
    """ Check if resolve with suggest y=5 works """
    d = QocaVariable.Name2VarDict
    QocaWrapperTest.solver.suggestNameValue([('y',5.0)])
    QocaWrapperTest.solver.resolve()
    
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 20.0)
    self.assertEqual(zVal, 20.0)

  def testV(self):
    """ Check if end edit works """
    QocaWrapperTest.solver.endEdit()
    QocaWrapperTest.solver.resolve()
    
    d = QocaVariable.Name2VarDict
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 20.0)
    self.assertEqual(zVal, 20.0)
  
  def testW(self):
    """ Check if remove all constraints works """    
    c1 = QocaLinearConstraint.name2ConstraintMap['c1']
    c2 = QocaLinearConstraint.name2ConstraintMap['c2']
    c3 = QocaLinearConstraint.name2ConstraintMap['c3']
    QocaWrapperTest.solver.delConstraints([c1,c2,c3])
    
    QocaWrapperTest.solver.solve()
    
    d = QocaVariable.Name2VarDict
    wVal = d['w'].get()
    xVal = d['x'].get()
    yVal = d['y'].get()
    zVal = d['z'].get()
    self.assertEqual(wVal, 10.0)
    self.assertEqual(xVal, 10.0)
    self.assertEqual(yVal, 20.0)
    self.assertEqual(zVal, 20.0)
    
    # Interesting: desired value != solver value even though no constraints
    # this is the effect of "stay weight" on the previously constrained values
    # Of course if we know start suggesting variables, we'll have no trouble
    ## print '\n'
    ## print 'w',  d['w'].desiredValue, d['w'].solverValue
    ## print 'x',  d['x'].desiredValue, d['x'].solverValue
    ## print 'y',  d['y'].desiredValue, d['y'].solverValue
    ## print 'z',  d['z'].desiredValue, d['z'].solverValue
    
    
  def testX(self):
    """ Check if remove all variables works """    
    d = QocaVariable.Name2VarDict
    w = d['w']
    x = d['x']
    y = d['y']
    z = d['z']
    QocaWrapperTest.solver.delVariables([w, x, y, z])
    

  def testY(self):
    """ Check if constraints/variables really gone """    
    c = QocaLinearConstraint.name2ConstraintMap
    v = QocaVariable.Name2VarDict
    def constReader(const, c=c):
      return c[const]
    def varReader( var, v=v):
      return v[var]
    self.assertRaises( KeyError, constReader, 'c1' )
    self.assertRaises( KeyError, constReader, 'c2' )
    self.assertRaises( KeyError, constReader, 'c3' )
    self.assertRaises( KeyError, varReader, 'w' )
    self.assertRaises( KeyError, varReader, 'x' )
    self.assertRaises( KeyError, varReader, 'y' )
    self.assertRaises( KeyError, varReader, 'z' )

  
  def testZ(self):
    """ Check if disconnect works """
    self.solver.disconnect()
  
  
  