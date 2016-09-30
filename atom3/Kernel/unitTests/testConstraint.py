import unittest

import sys

sys.path.append("../ATOM3Types")
sys.path.append("../UserInterface")
sys.path.append("../GraphGrammar")

from types           import *
from Tkinter         import *
from ATOM3Constraint import *
from ATOM3Exceptions import *

class ConstraintUnitTest(unittest.TestCase):

   def setUp(self):
      unUsed = Tk()
      self.atc = ATOM3Constraint(None,"set_graphical_type","self.semanticObject.", [], [])

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

   # --- SOME getValue() TESTS ---

   def getValueTest_isTuple(self):
      """getValue() should return a tuple"""
      ret = self.atc.getValue()
      assert type(ret) == TupleType

   def getValueTest_has5Elements(self):
      """getValue() should return a 5 elements tuple"""
      ret = self.atc.getValue()
      assert len(ret) == 5

   # --- SOME setValue() TESTS ---

   def setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID values ( "c1", 1, None, None, "" )"""
      self.atc.setValue(( "c1", 1, None, None, "" ))

   def setValueTest_SetValidValues_2 (self):
      """Tries Seting the VALID value 'Hola' ( constraint name ) """
      self.atc.setValue('Hola')

   def setValueTest_SetInValidValues_1 (self):
      """Tries Seting the INVALID value 1 """
      self.assertRaises (ATOM3BadAssignmentValue, self.atc.setValue, 1)

   def setValueTest_SetInValidValues_2 (self):
      """Tries Seting the INVALID value (1,2) """
      self.assertRaises (ATOM3BadAssignmentValue, self.atc.setValue, (1,2))

   def setValueTest_SetInValidValues_3 (self):
      """Tries Seting the INVALID values ( "c1", 1, 2, None, "" )"""
      self.assertRaises (ATOM3BadAssignmentValue, self.atc.setValue, ( "c1", 1, 2, None, "" ))

   def setValueTest_SetInValidValues_4 (self):
      """Tries Seting the INVALID values ( "c1", 1, None, 2, "" )"""
      self.assertRaises (ATOM3BadAssignmentValue, self.atc.setValue, ( "c1", 1, None, 2, "" ))

   def setValueTest_SetInValidValues_5 (self):
      """Tries Seting the INVALID values ( "c1", 1, None, None, 3 )"""
      self.assertRaises (ATOM3BadAssignmentValue, self.atc.setValue, ( "c1", 1, None, None, 3))

   def setValueTest_SetInValidValues_6 (self):
      """Tries Seting the INVALID values ('set_graphical_type', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], -4), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), ''), -4 is out of range"""      
      self.assertRaises (ATOM3BadAssignmentValue, self.atc.setValue, ('set_graphical_type', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], -4), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), ''))

   # --- setNone() and getNone() tests ---

   def setNoneTest_isNone(self):
      """if we call setNone(), then isNone() must return 1"""
      self.atc.setNone()
      assert self.atc.isNone() == 1

   # --- invalid() tests ---

   def invalidTest1(self):
      """Checks validity of ( "", 1, None, None, "" ), which must be invalid (constraint name missing) """
      self.atc.setValue( ( "", 1, None, None, "" ) )
      assert self.atc.invalid() != 0

   def invalidTest2(self):
      """Checks validity of ( "c1", 2, None, None, "bad Python code" ), which must be invalid (incorrect Python code) """
      self.atc.setValue( ( "c1", 0, None, None, "bad Python code" ) )
      assert self.atc.invalid() != 0

   def invalidTest3(self):
      """Checks validity of ( "c1", 2, None, None, "for a in b: a = a + 1" ), which must be valid """
      self.atc.setValue( ( "c1", 0, None, None, "for a in b: a = a + 1" ) )
      assert self.atc.invalid() == None

# same tests, but on a differently created ATOM3Constraint...

class ConstraintUnitTest2(ConstraintUnitTest):

   def setUp(self):
      unUsed = Tk()
      self.atc = ATOM3Constraint()


if __name__ == '__main__':
   cts = unittest.TestSuite()

   # 1st class tests

   cts.addTest(ConstraintUnitTest("getValueTest_isTuple"))
   cts.addTest(ConstraintUnitTest("getValueTest_has5Elements"))
   cts.addTest(ConstraintUnitTest("setValueTest_SetValidValues_1"))
   cts.addTest(ConstraintUnitTest("setValueTest_SetValidValues_2"))
   cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_1"))
   cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_2"))
   cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_3"))
   cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_4"))
   cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_5"))
   cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_6"))
   cts.addTest(ConstraintUnitTest("setNoneTest_isNone"))
   cts.addTest(ConstraintUnitTest("invalidTest1"))
   cts.addTest(ConstraintUnitTest("invalidTest2"))
   cts.addTest(ConstraintUnitTest("invalidTest3"))

   # 2nd. class tests

   cts.addTest(ConstraintUnitTest2("getValueTest_isTuple"))
   cts.addTest(ConstraintUnitTest2("getValueTest_has5Elements"))
   cts.addTest(ConstraintUnitTest2("setValueTest_SetValidValues_1"))
   cts.addTest(ConstraintUnitTest2("setValueTest_SetValidValues_2"))
   cts.addTest(ConstraintUnitTest2("setValueTest_SetInValidValues_1"))
   cts.addTest(ConstraintUnitTest2("setValueTest_SetInValidValues_2"))
   cts.addTest(ConstraintUnitTest2("setValueTest_SetInValidValues_3"))
   cts.addTest(ConstraintUnitTest2("setValueTest_SetInValidValues_4"))
   cts.addTest(ConstraintUnitTest2("setValueTest_SetInValidValues_5"))
   cts.addTest(ConstraintUnitTest2("setValueTest_SetInValidValues_6"))
   cts.addTest(ConstraintUnitTest2("setNoneTest_isNone"))
   cts.addTest(ConstraintUnitTest2("invalidTest1"))
   cts.addTest(ConstraintUnitTest2("invalidTest2"))
   cts.addTest(ConstraintUnitTest2("invalidTest3"))

   runner = unittest.TextTestRunner()
   runner.run(cts)






