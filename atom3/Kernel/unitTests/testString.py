import unittest

import sys

sys.path.append("../ATOM3Types")
sys.path.append("../UserInterface")
sys.path.append("../GraphGrammar")

from types           import *
from Tkinter         import *
from ATOM3String     import *
from ATOM3Exceptions import *

class StringUnitTest(unittest.TestCase):

   def setUp(self):
      unUsed = Tk()
      self.atc = ATOM3String()

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

   # --- SOME getValue() TESTS ---

   def getValueTest_isString(self):
      """getValue() should return an integer"""
      ret = self.atc.getValue()
      assert type(ret) == StringType

   # --- SOME setNone() -- isNone() TESTS ---

   def setNoneIsNoneTest_0(self):
      """Tries setNone() and the isNone()"""
      self.atc.setNone()
      assert self.atc.isNone()

   def setNoneIsNoneTest_1(self):
      """Tries isNone() after setting it to '5'"""
      self.atc.setValue('5')
      assert (not self.atc.isNone())


   # --- SOME setValue() TESTS ---

   def setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID value 'hola caracola'"""
      self.atc.setValue('0')
      assert self.atc.getValue() == '0'

   def setValueTest_SetValidValues_2 (self):
      """Tries Seting the VALID value ''"""
      self.atc.setValue('')
      assert self.atc.getValue() == ''

   def setValueTest_SetValidValues_3 (self):
      """Tries Seting the VALID value '1'"""
      self.atc.setValue('1')
      assert self.atc.getValue() == '1'

   def setValueTest_SetInValidValues_0 (self):
      """Tries Seting the INVALID value 3"""
      self.assertRaises(ATOM3BadAssignmentValue,self.atc.setValue,3)

   def setValueTest_SetInValidValues_1 (self):
      """Tries Seting the INVALID value ('3',)"""
      self.assertRaises(ATOM3BadAssignmentValue,self.atc.setValue,('3',))

   # --- toString() TEST ---

   def toStringTest(self):
      """The toString() method must return a string!"""
      self.atc.setValue('5')
      c = self.atc.toString()
      assert (type(c) == StringType) and c == '5'

class StringUnitTest1(StringUnitTest):

   def setUp(self):
      unUsed = Tk()
      self.atc = ATOM3String('5')

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

  # --- SOME MORE getValue() TESTS ---

   def getValueTest_getValue(self):
      """getValue() should return '5' (constructor value)"""
      ret = self.atc.getValue()
      assert ret == '5'

cts = unittest.TestSuite()
cts.addTest(StringUnitTest("getValueTest_isString"))
cts.addTest(StringUnitTest("setValueTest_SetValidValues_1"))
cts.addTest(StringUnitTest("setValueTest_SetValidValues_2"))
cts.addTest(StringUnitTest("setValueTest_SetValidValues_3"))
cts.addTest(StringUnitTest("setValueTest_SetInValidValues_0"))
cts.addTest(StringUnitTest("setValueTest_SetInValidValues_1"))
cts.addTest(StringUnitTest("setNoneIsNoneTest_0"))
cts.addTest(StringUnitTest("setNoneIsNoneTest_1"))
cts.addTest(StringUnitTest("toStringTest"))

cts.addTest(StringUnitTest1("getValueTest_isString"))
cts.addTest(StringUnitTest1("setValueTest_SetValidValues_1"))
cts.addTest(StringUnitTest1("setValueTest_SetValidValues_2"))
cts.addTest(StringUnitTest1("setValueTest_SetValidValues_3"))
cts.addTest(StringUnitTest1("setValueTest_SetInValidValues_0"))
cts.addTest(StringUnitTest1("setValueTest_SetInValidValues_1"))
cts.addTest(StringUnitTest1("setNoneIsNoneTest_0"))
cts.addTest(StringUnitTest1("setNoneIsNoneTest_1"))
cts.addTest(StringUnitTest1("toStringTest"))
cts.addTest(StringUnitTest1("getValueTest_getValue"))

runner = unittest.TextTestRunner()
runner.run(cts)






