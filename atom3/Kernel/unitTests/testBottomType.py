import unittest

import sys

sys.path.append("../ATOM3Types")
sys.path.append("../UserInterface")
sys.path.append("../GraphGrammar")

from types           import *
from Tkinter         import *
from ATOM3BottomType import *
from ATOM3Exceptions import *

class BottomTypeUnitTest(unittest.TestCase):

   def setUp(self):
      self.mainwindow = Tk()
      self.atc = ATOM3BottomType()

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

   # --- SOME getValue() TESTS ---

   def getValueTest_isNone(self):
      """getValue() should return None"""
      ret = self.atc.getValue()
      assert ret == None

   # --- SOME setNone() -- isNone() TESTS ---

   def setNoneIsNoneTest_0(self):
      """Tries setNone() and the isNone()"""
      self.atc.setNone()
      assert self.atc.isNone()

   # --- SOME show() TESTS ---

   def show_setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID value 0 and show widget"""
      self.mainwindow = Tk()
      self.atc.show(self.mainwindow)
      assert self.atc.getValue() == None

   # --- SOME setValue() + show() + destroy() TESTS ---

   def show_destroy_setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID value 0, shows widget and then destroys"""
      self.mainwindow = Tk()
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert self.atc.getValue() == None

   # --- toString() TEST ---

   def toStringTest(self):
      """The toString() method must return a string!"""
      c = self.atc.toString()
      assert (type(c) == StringType) and c == ""


cts = unittest.TestSuite()
cts.addTest(BottomTypeUnitTest("getValueTest_isNone"))
cts.addTest(BottomTypeUnitTest("setNoneIsNoneTest_0"))
cts.addTest(BottomTypeUnitTest("show_setValueTest_SetValidValues_1"))
cts.addTest(BottomTypeUnitTest("show_destroy_setValueTest_SetValidValues_1"))
cts.addTest(BottomTypeUnitTest("toStringTest"))

runner = unittest.TextTestRunner()
runner.run(cts)






