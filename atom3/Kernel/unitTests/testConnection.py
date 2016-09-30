import unittest

import sys

sys.path.append("../ATOM3Types")
sys.path.append("../UserInterface")
sys.path.append("../GraphGrammar")

from types           import *
from Tkinter         import *
from ATOM3Connection import *
from ATOM3Exceptions import *
from ASGNode         import *

class ConstraintUnitTest(unittest.TestCase):

   def setUp(self):
      unUsed = Tk()
      self.atc = ATOM3Connection()

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

   # --- SOME getValue() TESTS ---

   def getValueTest_isTuple(self):
      """getValue() should return a tuple"""
      ret = self.atc.getValue()
      assert type(ret) == TupleType

   def getValueTest_has2Elements(self):
      """getValue() should return a 4 elements tuple"""
      ret = self.atc.getValue()
      assert len(ret) == 4

   # --- SOME setValue() TESTS ---

   def setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID values ( "o1", 1, "1", "n" )"""
      self.atc.setValue(( "o1", 1, "1", "n" ))

   def setValueTest_SetValidValues_2 (self):
      """Tries Seting the VALID values ( <ASGNode instance>, 1, "1", "n" )"""
      self.atc.setValue(( ASGNode(), 1, "1", "n" ))

   def setValueTest_SetInValidValues_1 (self):
      """Tries Seting the INVALID values ( 1, 1, "1", "n" ) (1 is not a string nor an ASGNode child)"""
      self.assertRaises(ATOM3BadAssignmentValue, self.atc.setValue, ( 1, 1, "1", "n" ))

   def setValueTest_SetInValidValues_2 (self):
      """Tries Seting the INVALID values ( "o1", 2, "1", "n" ) (2 is out of range)"""
      self.assertRaises(ATOM3BadAssignmentValue, self.atc.setValue, ( "o1", 2, "1", "n" ))

   def setValueTest_SetInValidValues_3 (self):
      """Tries Seting the INVALID values ( "o1", 1, 3, "n" ) (3 is not a string)"""
      self.assertRaises(ATOM3BadAssignmentValue, self.atc.setValue, ( "o1", 1, 3, "n" ))

   def setValueTest_SetInValidValues_4 (self):
      """Tries Seting the INVALID values ( "o1", 0, "1", 4 ) (4 is not a string)"""
      self.assertRaises(ATOM3BadAssignmentValue, self.atc.setValue, ( "o1", 1, "1", 4 ))

   # --- setNone() and getNone() tests ---

   def setNoneTest_isNone(self):
      """if we call setNone(), then isNone() must return 1"""
      self.atc.setNone()
      assert self.atc.isNone() == 1

cts = unittest.TestSuite()
cts.addTest(ConstraintUnitTest("getValueTest_isTuple"))
cts.addTest(ConstraintUnitTest("getValueTest_has2Elements"))
cts.addTest(ConstraintUnitTest("setValueTest_SetValidValues_1"))
cts.addTest(ConstraintUnitTest("setValueTest_SetValidValues_2"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_1"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_2"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_3"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_4"))
cts.addTest(ConstraintUnitTest("setNoneTest_isNone"))

runner = unittest.TextTestRunner()
runner.run(cts)


