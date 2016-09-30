import unittest

import sys

sys.path.append("../ATOM3Types")
sys.path.append("../UserInterface")
sys.path.append("../GraphGrammar")

from types           import *
from Tkinter         import *
from ATOM3Float      import *
from ATOM3Exceptions import *

class FloatUnitTest(unittest.TestCase):

   def setUp(self):
      self.mainwindow = Tk()
      self.atc = ATOM3Float()

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

   # --- SOME getValue() TESTS ---

   def getValueTest_isFloat(self):
      """getValue() should return a float"""
      ret = self.atc.getValue()
      assert type(ret) == FloatType

   # --- SOME setNone() -- isNone() TESTS ---

   def setNoneIsNoneTest_0(self):
      """Tries setNone() and the isNone()"""
      self.atc.setNone()
      assert self.atc.isNone()

   def setNoneIsNoneTest_1(self):
      """Tries isNone() after setting it to 5.5"""
      self.atc.setValue(5.5)
      assert (not self.atc.isNone())

   # --- SOME setValue() TESTS ---

   def setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID value 0"""
      self.atc.setValue(0)
      assert self.atc.getValue() == 0

   def setValueTest_SetValidValues_2 (self):
      """Tries Seting the VALID value 1010"""
      self.atc.setValue(1010)
      assert self.atc.getValue() == 1010

   def setValueTest_SetValidValues_3 (self):
      """Tries Seting the VALID value 1.010"""
      self.atc.setValue(1.010)
      assert self.atc.getValue() == 1.010

   def setValueTest_SetInValidValues_0 (self):
      """Tries Seting the INVALID value '3'"""
      self.assertRaises(ATOM3BadAssignmentValue,self.atc.setValue,'3')

   def setValueTest_SetInValidValues_1 (self):
      """Tries Seting the INVALID value (3.5,)"""
      self.assertRaises(ATOM3BadAssignmentValue,self.atc.setValue,(3.5,))

   # --- SOME setValue() + show() TESTS ---

   def show_setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID value 0.5 and show widget"""
      self.atc.setValue(0.5)
      self.mainwindow = Tk()
      self.atc.show(self.mainwindow)
      assert self.atc.getValue() == 0.5

   def show_setValueTest_SetValidValues_2 (self):
      """Tries Seting the VALID value 1.010 and show widget"""
      self.atc.setValue(1.010)
      self.mainwindow = Tk()
      self.atc.show(self.mainwindow)
      assert self.atc.getValue() == 1.010

   # --- SOME setValue() + show() + destroy() TESTS ---

   def show_destroy_setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID value 0, shows widget and then destroys"""
      self.atc.setValue(0.5)
      self.mainwindow = Tk()
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert self.atc.getValue() == 0.5

   def show_destroy_setValueTest_SetValidValues_2 (self):
      """Tries Seting the VALID value 1.010, shows widget and then destroys"""
      self.atc.setValue(1.010)
      self.mainwindow = Tk()
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert self.atc.getValue() == 1.010

   # --- toString() TEST ---

   def toStringTest(self):
      """The toString() method must return a string!"""
      self.atc.setValue(5.3)
      c = self.atc.toString()
      assert (type(c) == StringType) and c == '5.3'

class FloatUnitTest1(FloatUnitTest):

   def setUp(self):
      unUsed = Tk()
      self.atc = ATOM3Float(0.5)

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

  # --- SOME MORE getValue() TESTS ---

   def getValueTest_getValue(self):
      """getValue() should return 0.5 (constructor value)"""
      ret = self.atc.getValue()
      assert ret == 0.5

cts = unittest.TestSuite()
cts.addTest(FloatUnitTest("getValueTest_isFloat"))
cts.addTest(FloatUnitTest("setValueTest_SetValidValues_1"))
cts.addTest(FloatUnitTest("setValueTest_SetValidValues_2"))
cts.addTest(FloatUnitTest("setValueTest_SetValidValues_3"))
cts.addTest(FloatUnitTest("setValueTest_SetInValidValues_0"))
cts.addTest(FloatUnitTest("setValueTest_SetInValidValues_1"))
cts.addTest(FloatUnitTest("show_setValueTest_SetValidValues_1"))
cts.addTest(FloatUnitTest("show_setValueTest_SetValidValues_2"))
cts.addTest(FloatUnitTest("show_destroy_setValueTest_SetValidValues_1"))
cts.addTest(FloatUnitTest("show_destroy_setValueTest_SetValidValues_2"))
cts.addTest(FloatUnitTest("toStringTest"))
cts.addTest(FloatUnitTest("setNoneIsNoneTest_0"))
cts.addTest(FloatUnitTest("setNoneIsNoneTest_1"))

cts.addTest(FloatUnitTest1("getValueTest_isFloat"))
cts.addTest(FloatUnitTest1("getValueTest_getValue"))
cts.addTest(FloatUnitTest1("setValueTest_SetValidValues_1"))
cts.addTest(FloatUnitTest1("setValueTest_SetValidValues_2"))
cts.addTest(FloatUnitTest1("setValueTest_SetValidValues_3"))
cts.addTest(FloatUnitTest1("setValueTest_SetInValidValues_0"))
cts.addTest(FloatUnitTest1("setValueTest_SetInValidValues_1"))
cts.addTest(FloatUnitTest1("show_setValueTest_SetValidValues_1"))
cts.addTest(FloatUnitTest1("show_setValueTest_SetValidValues_2"))
cts.addTest(FloatUnitTest1("show_destroy_setValueTest_SetValidValues_1"))
cts.addTest(FloatUnitTest1("show_destroy_setValueTest_SetValidValues_2"))
cts.addTest(FloatUnitTest1("toStringTest"))
cts.addTest(FloatUnitTest1("setNoneIsNoneTest_0"))
cts.addTest(FloatUnitTest1("setNoneIsNoneTest_1"))

runner = unittest.TextTestRunner()
runner.run(cts)






