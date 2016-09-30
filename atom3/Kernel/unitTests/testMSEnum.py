import unittest

import sys

sys.path.append("../ATOM3Types")
sys.path.append("../UserInterface")
sys.path.append("../GraphGrammar")

from types           import *
from Tkinter         import *
from ATOM3MSEnum     import *
from ATOM3Exceptions import *

class MSEnumUnitTest(unittest.TestCase):

   def setUp(self):
      self.mainwindow = Tk()
      self.atc = ATOM3MSEnum()

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

   # --- SOME setNone() - isNone() TESTS ---

   def setNone_Test(self):
      """Tries setNone() and isNone()"""
      self.atc.setNone()
      assert self.atc.isNone()

   def show_setNone_Test(self):
      """Tries setNone() show() isNone()"""
      self.atc.setNone()
      self.atc.show(self.mainwindow)
      assert self.atc.isNone()

   def show_destroy_setNone_Test(self):
      """Tries setNone() show() isNone()"""
      self.atc.setNone()
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert self.atc.isNone()

   # --- SOME getValue() TESTS ---

   def getValueTest_isTuple(self):
      """getValue() should return a tuple"""
      ret = self.atc.getValue()
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert type(ret) == TupleType

   def getValueTest_has2Elements(self):
      """getValue() should return a 2 elements tuple"""
      ret = self.atc.getValue()
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert len(ret) == 2

   # --- SOME setValue() TESTS ---

   def setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID values ( ["e1", "e2"], [1, 0] )"""
      self.atc.setValue(( ["e1", "e2"], [1, 0] ))
      res = self.atc.getValue()
      assert res == (["e1", "e2"], [1, 0])

   def show_setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID values ( ["e1", "e2"], [1, 0] ), with show"""
      self.atc.setValue(( ["e1", "e2"], [1, 0] ))
      self.atc.show(self.mainwindow)
      res = self.atc.getValue()
      assert res == (["e1", "e2"], [1, 0])

   def show_destroy_setValueTest_SetValidValues_1 (self):
      """Tries Seting the VALID values ( ["e1", "e2"], [1, 0] ), with show"""
      self.atc.setValue(( ["e1", "e2"], [1, 0] ))
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      res = self.atc.getValue()
      assert res == (["e1", "e2"], [1, 0])

   def setValueTest_SetInValidValues_1 (self):
      """Tries Seting the INVALID values ( ["e1", "e2"], 1 ) ( 1 is not a list of selected things)"""
      self.assertRaises ( ATOM3BadAssignmentValue, self.atc.setValue, ( ["e1", "e2"], 1 ))

   def setValueTest_SetInValidValues_2 (self):
      """Tries Seting the INVALID values ( ["e1", "e2"], [1, 0, 0] ) ( wrong list sizes )"""
      self.assertRaises ( ATOM3BadAssignmentValue, self.atc.setValue, ( ["e1", "e2"], [1, 0, 0] ))

   def setValueTest_SetInValidValues_3 (self):
      """Tries Seting the INVALID values ( [1, "e2"], [1, 0] ) ( 1 is not a string)"""
      self.assertRaises ( ATOM3BadAssignmentValue, self.atc.setValue, ( [1, "e2"], [1, 0] ))

   # --- toString() TEST ---

   def toStringTest(self):
      """The toString() method must return a string!"""
      self.atc.setValue(( ["e1", "e2"], [1, 0] ))
      c = self.atc.toString()
      assert (type(c) == StringType)

class MSEnumUnitTest1(MSEnumUnitTest):

   def setUp(self):
      self.mainwindow = Tk()
      self.atc = ATOM3MSEnum(["e0", "e1"])	# a valid value!

   def getValueTest_1(self):
      """getValue() should return (["e0", "e1"], [0, 0])"""
      ret = self.atc.getValue()
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert ret == (["e0", "e1"], [0, 0])

class MSEnumUnitTest2(MSEnumUnitTest):

   def setUp(self):
      self.mainwindow = Tk()
      self.atc = ATOM3MSEnum(["e0", "e1"], [1, 1])	# a valid value!

   def getValueTest_1(self):
      """getValue() should return (["e0", "e1"], [1, 1])"""
      ret = self.atc.getValue()
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert ret == (["e0", "e1"], [1, 1])

class MSEnumUnitTest3(MSEnumUnitTest):

   def setUp(self):
      self.mainwindow = Tk()
      self.atc = ATOM3MSEnum(["e0", "e1"], [1, 1], 1)	# a valid value!

   def getValueTest_1(self):
      """getValue() should return (["e0", "e1"], [1, 1])"""
      ret = self.atc.getValue()
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert ret == (["e0", "e1"], [1, 1])

class MSEnumUnitTest4(MSEnumUnitTest):

   def setUp(self):
      self.mainwindow = Tk()
      self.atc = ATOM3MSEnum(["e0", "e1"], [1, 1], 0, ATOM3MSEnum.LISTBOX)	# a valid value!

   def getValueTest_1(self):
      """getValue() should return (["e0", "e1"], [1, 1])"""
      ret = self.atc.getValue()
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert ret == (["e0", "e1"], [1, 1])


cts = unittest.TestSuite()
cts.addTest(MSEnumUnitTest("setNone_Test"))
cts.addTest(MSEnumUnitTest("show_setNone_Test"))
cts.addTest(MSEnumUnitTest("show_destroy_setNone_Test"))
cts.addTest(MSEnumUnitTest("getValueTest_isTuple"))
cts.addTest(MSEnumUnitTest("getValueTest_has2Elements"))
cts.addTest(MSEnumUnitTest("setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest("show_setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest("show_destroy_setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest("setValueTest_SetInValidValues_1"))
cts.addTest(MSEnumUnitTest("setValueTest_SetInValidValues_2"))
cts.addTest(MSEnumUnitTest("setValueTest_SetInValidValues_3"))
cts.addTest(MSEnumUnitTest("toStringTest"))

cts.addTest(MSEnumUnitTest1("getValueTest_1"))
cts.addTest(MSEnumUnitTest1("setNone_Test"))
cts.addTest(MSEnumUnitTest1("show_setNone_Test"))
cts.addTest(MSEnumUnitTest1("show_destroy_setNone_Test"))
cts.addTest(MSEnumUnitTest1("getValueTest_isTuple"))
cts.addTest(MSEnumUnitTest1("getValueTest_has2Elements"))
cts.addTest(MSEnumUnitTest1("setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest1("show_setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest1("show_destroy_setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest1("setValueTest_SetInValidValues_1"))
cts.addTest(MSEnumUnitTest1("setValueTest_SetInValidValues_2"))
cts.addTest(MSEnumUnitTest1("setValueTest_SetInValidValues_3"))
cts.addTest(MSEnumUnitTest1("toStringTest"))

cts.addTest(MSEnumUnitTest2("getValueTest_1"))
cts.addTest(MSEnumUnitTest2("setNone_Test"))
cts.addTest(MSEnumUnitTest2("show_setNone_Test"))
cts.addTest(MSEnumUnitTest2("show_destroy_setNone_Test"))
cts.addTest(MSEnumUnitTest2("getValueTest_isTuple"))
cts.addTest(MSEnumUnitTest2("getValueTest_has2Elements"))
cts.addTest(MSEnumUnitTest2("setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest2("show_setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest2("show_destroy_setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest2("setValueTest_SetInValidValues_1"))
cts.addTest(MSEnumUnitTest2("setValueTest_SetInValidValues_2"))
cts.addTest(MSEnumUnitTest2("setValueTest_SetInValidValues_3"))
cts.addTest(MSEnumUnitTest2("toStringTest"))

cts.addTest(MSEnumUnitTest3("getValueTest_1"))
cts.addTest(MSEnumUnitTest3("setNone_Test"))
cts.addTest(MSEnumUnitTest3("show_setNone_Test"))
cts.addTest(MSEnumUnitTest3("show_destroy_setNone_Test"))
cts.addTest(MSEnumUnitTest3("getValueTest_isTuple"))
cts.addTest(MSEnumUnitTest3("getValueTest_has2Elements"))
cts.addTest(MSEnumUnitTest3("setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest3("show_setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest3("show_destroy_setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest3("setValueTest_SetInValidValues_1"))
cts.addTest(MSEnumUnitTest3("setValueTest_SetInValidValues_2"))
cts.addTest(MSEnumUnitTest3("setValueTest_SetInValidValues_3"))
cts.addTest(MSEnumUnitTest3("toStringTest"))

cts.addTest(MSEnumUnitTest4("getValueTest_1"))
cts.addTest(MSEnumUnitTest4("setNone_Test"))
cts.addTest(MSEnumUnitTest4("show_setNone_Test"))
cts.addTest(MSEnumUnitTest4("show_destroy_setNone_Test"))
cts.addTest(MSEnumUnitTest4("getValueTest_isTuple"))
cts.addTest(MSEnumUnitTest4("getValueTest_has2Elements"))
cts.addTest(MSEnumUnitTest4("setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest4("show_setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest4("show_destroy_setValueTest_SetValidValues_1"))
cts.addTest(MSEnumUnitTest4("setValueTest_SetInValidValues_1"))
cts.addTest(MSEnumUnitTest4("setValueTest_SetInValidValues_2"))
cts.addTest(MSEnumUnitTest4("setValueTest_SetInValidValues_3"))
cts.addTest(MSEnumUnitTest4("toStringTest"))

runner = unittest.TextTestRunner()
runner.run(cts)






