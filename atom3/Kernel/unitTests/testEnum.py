import unittest

import sys

sys.path.append("../ATOM3Types")
sys.path.append("../UserInterface")
sys.path.append("../GraphGrammar")

from types           import *
from Tkinter         import *
from ATOM3Enum       import *
from ATOM3Exceptions import *

class ConstraintUnitTest(unittest.TestCase):

   def setUp(self):
      unUsed = Tk()
      self.atc = ATOM3Enum()

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

   # --- SOME getValue() TESTS ---

   def getValueTest_isTuple(self):
      """getValue() should return a tuple"""
      ret = self.atc.getValue()
      assert type(ret) == TupleType

   def getValueTest_has2Elements(self):
      """getValue() should return a 2 elements tuple"""
      ret = self.atc.getValue()
      assert len(ret) == 2

   # --- SOME setValue() TESTS ---

   def setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID values ( ["e1", "e2"], 1 )"""
      self.atc.setValue(( ["e1", "e2"], 1 ))

   def setValueTest_SetInValidValues_1 (self):
      """Tries Seting the INVALID value ( 1 ) (1 is not a tuple)"""
      self.assertRaises (ATOM3BadAssignmentValue, self.atc.setValue, 1)

   def setValueTest_SetInValidValues_2 (self):
      """Tries Seting the INVALID values ( ["e1", "e2"], 2 ) (2 is out of range)"""
      self.assertRaises (ATOM3BadAssignmentValue, self.atc.setValue, ( ["e1", "e2"], 2 ))

   def setValueTest_SetInValidValues_3 (self):
      """Tries Seting the INVALID values ( ["e1", "e2"], -2 ) (-2 is out of range)"""
      self.assertRaises (ATOM3BadAssignmentValue, self.atc.setValue, ( ["e1", "e2"], -2 ))

   def setValueTest_SetInValidValues_4 (self):
      """Tries Seting the INVALID values ( ["e1", "e2"], "e") ("e" is not a number )"""
      self.assertRaises (ATOM3BadAssignmentValue, self.atc.setValue, ( ["e1", "e2"], "e" ))

   def setValueTest_SetInValidValues_5 (self):
      """Tries Seting the INVALID values ( "e1", 1) ("e" is not a list )"""
      self.assertRaises (ATOM3BadAssignmentValue, self.atc.setValue, ( "e1", 1 ))

   def setValue_getValue (self):
      """setValue((["1","2"],0)) and then getValue() must return (["1","2"],0)"""
      self.atc.setValue((["1","2"],0))
      print self.atc.getValue()
      assert self.atc.getValue() == (["1","2"],0)

   # --- setNone() and getNone() tests ---

   def setNoneTest_isNone(self):
      """if we call setNone(), then isNone() must return 1"""
      self.atc.setNone()
      assert self.atc.isNone() == 1

cts = unittest.TestSuite()
cts.addTest(ConstraintUnitTest("getValueTest_isTuple"))
cts.addTest(ConstraintUnitTest("getValueTest_has2Elements"))
cts.addTest(ConstraintUnitTest("setValueTest_SetValidValues_1"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_1"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_2"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_3"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_4"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_5"))
cts.addTest(ConstraintUnitTest("setValue_getValue"))
cts.addTest(ConstraintUnitTest("setNoneTest_isNone"))

runner = unittest.TextTestRunner()
runner.run(cts)






