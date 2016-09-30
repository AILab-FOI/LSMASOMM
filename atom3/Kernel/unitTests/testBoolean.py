import unittest

import sys

sys.path.append("../ATOM3Types")
sys.path.append("../UserInterface")
sys.path.append("../GraphGrammar")

from types           import *
from Tkinter         import *
from ATOM3Boolean    import *
from ATOM3Exceptions import *

class ConstraintUnitTest(unittest.TestCase):

   def setUp(self):
      unUsed = Tk()
      self.atc = ATOM3Boolean()

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

   # --- SOME toString() TESTS ---

   def toStringTest_1(self):
      """getValue() should return an integer"""
      ret = self.atc.toString()
      assert type(ret) == StringType

   # --- SOME getValue() TESTS ---

   def getValueTest_isInteger(self):
      """getValue() should return an integer"""
      ret = self.atc.getValue()
      assert type(ret) == IntType

   # --- SOME setValue() TESTS ---

   def setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID values ( "is Ok?", 1 )"""
      self.atc.setValue(( "is Ok?", 1 ))

   def setValueTest_SetValidValues_2 (self):
      """Tries Seting the VALID values ( "is Ok?", 0 )"""
      self.atc.setValue(( "is Ok?", 0 ))

   def setValueTest_SetInValidValues_0 (self):
      """Tries Seting the INVALID value 3 (3 is not a tuple)"""
      self.assertRaises(ATOM3BadAssignmentValue,self.atc.setValue,3)

   def setValueTest_SetInValidValues_1 (self):
      """Tries Seting the INVALID values ( 3, 0 ) (3 is not a string)"""
      self.assertRaises(ATOM3BadAssignmentValue,self.atc.setValue,( 3, 0 ))

   def setValueTest_SetInValidValues_2 (self):
      """Tries Seting the INVALID values ( "is Ok?", -1 ) (-1 is out of range)"""
      self.assertRaises(ATOM3BadAssignmentValue,self.atc.setValue,( "is Ok?", -1 ))

   def setValueTest_SetInValidValues_3 (self):
      """Tries Seting the INVALID values ( "is Ok?", 2 ) (2 is out of range)"""
      self.assertRaises(ATOM3BadAssignmentValue,self.atc.setValue,( "is Ok?", 2 ))

   def setValueTest_SetInValidValues_4 (self):
      """Tries Seting the INVALID values ( "is Ok?", "ok" ) ("ok" is not an integer)"""
      self.assertRaises(ATOM3BadAssignmentValue,self.atc.setValue,( "is Ok?", "ok" ))

   # --- SOME getValue() TESTS ---

   def getValueTest_0 (self):
      """Tries Seting the VALID values ( "is Ok?", 0 ) and checks getValue() result"""
      self.atc.setValue (( "is Ok?", 0 ))
      assert(self.atc.getValue() == 0)

   def getValueTest_1 (self):
      """Tries Seting the VALID values ( "is Ok?", 1 ) and checks getValue() result"""
      self.atc.setValue (( "is Ok?", 1 ))
      assert(self.atc.getValue() == 1)

cts = unittest.TestSuite()
cts.addTest(ConstraintUnitTest("toStringTest_1"))
cts.addTest(ConstraintUnitTest("getValueTest_isInteger"))
cts.addTest(ConstraintUnitTest("setValueTest_SetValidValues_1"))
cts.addTest(ConstraintUnitTest("setValueTest_SetValidValues_2"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_0"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_1"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_2"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_3"))
cts.addTest(ConstraintUnitTest("setValueTest_SetInValidValues_4"))
cts.addTest(ConstraintUnitTest("getValueTest_0"))
cts.addTest(ConstraintUnitTest("getValueTest_1"))

runner = unittest.TextTestRunner()
runner.run(cts)






