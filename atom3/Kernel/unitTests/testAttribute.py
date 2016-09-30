import unittest

import sys

sys.path.append("../ATOM3Types")
sys.path.append("../UserInterface")
sys.path.append("../GraphGrammar")

from types           import *
from Tkinter         import *
from ATOM3Attribute  import *
from ATOM3Exceptions import *

from ATOM3String     import *
from ATOM3Integer    import *
from ATOM3Float      import *

class AttributeUnitTest(unittest.TestCase):

   def setUp(self):
      self.mainwindow = Tk()
      # declare dictionary with allowed types
      self.types = {'String' : (ATOM3String, () ),
                    'Integer': (ATOM3Integer, () ),
                    'Float'  : (ATOM3Float, ()) }
      self.atc = ATOM3Attribute(self.types)

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

   # --- SOME getValue() TESTS ---

   def getValueTest_is5ElementTuple(self):
      """getValue() should return a 5-element tuple"""
      ret = self.atc.getValue()
      assert type(ret) == TupleType and len(ret) == 5

   # --- SOME setNone() -- isNone() TESTS ---

   def setNoneIsNoneTest_0(self):
      """Tries setNone() and the isNone()"""
      self.atc.setNone()
      assert self.atc.isNone()

   # --- SOME setValue() TESTS ---

   def setValue_Correct0(self):
      """Tries setting the correct value ('StateName', 'String', 'name', 1, 1)"""
      self.atc.setValue(('StateName', 'String', 'name', 1, 1))
      rv = self.atc.getValue()
      assert rv == ('StateName', 'String', 'name', 1, 1)

   def setValue_InCorrect0(self):
      """Tries setting the incorrect value 'StateName'"""
      self.assertRaises(ATOM3BadAssignmentValue, self.atc.setValue, 'StateName')

   def setValue_InCorrect1(self):
      """Tries setting the incorrect value ('StateName', 1) (length of tuple might be 6)"""
      self.assertRaises(ATOM3BadAssignmentValue, self.atc.setValue, ('StateName', 1) )

   def setValue_InCorrect2(self):
      """Tries setting the incorrect value ('StateName', 'non-existent type', 'name', 1, 1)"""
      self.assertRaises(ATOM3BadAssignmentValue, self.atc.setValue, ('StateName', 'non-existent type', 'name', 1, 1))

   def setValue_InCorrect3(self):
      """Tries setting the incorrect value (3, 'non-existent type', 'name', 1, 1) (3 is not a string)"""
      self.assertRaises(ATOM3BadAssignmentValue, self.atc.setValue, (3, 'String', 'name', 1, 1))

   def setValue_InCorrect4(self):
      """Tries setting the incorrect value ('StateName', 'non-existent type', 'name', 1, 1) (5 is not a valid key value)"""
      self.assertRaises(ATOM3BadAssignmentValue, self.atc.setValue, ('StateName', 'String', 'name', 5, 1))

   def setValue_InCorrect5(self):
      """Tries setting the incorrect value ('StateName', 'non-existent type', 'name', 1, 1) (3 is not a valid editing value)"""
      self.assertRaises(ATOM3BadAssignmentValue, self.atc.setValue, ('StateName', 'String', 'name', 1, 4))

   # --- SOME setValue() + show() TESTS ---

   def showSetValue_Correct0(self):
      """Tries setting the correct value ('StateName', 'String', 'name', 1, 1), with show()"""
      self.atc.setValue(('StateName', 'String', 'name', 1, 1))
      self.atc.show(self.mainwindow)
      rv = self.atc.getValue()
      assert rv == ('StateName', 'String', 'name', 1, 1)

   def showSetNone_IsNone(self):
      """Tries calling setNone() and isNone()"""
      self.atc.setNone()
      self.atc.show(self.mainwindow)
      assert self.atc.isNone()

   # --- SOME setValue() + show() + destroy() TESTS ---

   def show_destroy_SetValue_Correct0(self):
      """Tries setting the correct value ('StateName', 'String', 'name', 1, 1), with show() and destroy()"""
      self.atc.setValue(('StateName', 'String', 'name', 1, 1))
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      rv = self.atc.getValue()
      assert rv == ('StateName', 'String', 'name', 1, 1)

   def show_destroy_SetNone_IsNone(self):
      """Tries calling setNone() show() destroy() isNone()"""
      self.atc.setNone()
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert self.atc.isNone()

   # --- toString() test ---

   def show_destroy_toString_test(self):
      """Tries setting the correct value ('StateName', 'String', 'name', 1, 1), and the call toString"""
      self.atc.setValue(('StateName', 'String', 'name', 1, 1))
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      rv = self.atc.toString()
      assert type(rv) == StringType

   def show_toString_test(self):
      """Tries setting the correct value ('StateName', 'String', 'name', 1, 1), and the call toString"""
      self.atc.setValue(('StateName', 'String', 'name', 1, 1))
      self.atc.show(self.mainwindow)
      rv = self.atc.toString()
      assert type(rv) == StringType

   def toString_test(self):
      """Tries setting the correct value ('StateName', 'String', 'name', 1, 1), and the call toString"""
      self.atc.setValue(('StateName', 'String', 'name', 1, 1))
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      rv = self.atc.toString()
      assert type(rv) == StringType



cts = unittest.TestSuite()
cts.addTest(AttributeUnitTest("getValueTest_is5ElementTuple"))
cts.addTest(AttributeUnitTest("setNoneIsNoneTest_0"))
cts.addTest(AttributeUnitTest("setValue_Correct0"))
cts.addTest(AttributeUnitTest("setValue_InCorrect0"))
cts.addTest(AttributeUnitTest("setValue_InCorrect1"))
cts.addTest(AttributeUnitTest("setValue_InCorrect2"))
cts.addTest(AttributeUnitTest("setValue_InCorrect3"))
cts.addTest(AttributeUnitTest("setValue_InCorrect4"))
cts.addTest(AttributeUnitTest("setValue_InCorrect5"))
cts.addTest(AttributeUnitTest("showSetValue_Correct0"))
cts.addTest(AttributeUnitTest("showSetNone_IsNone"))
cts.addTest(AttributeUnitTest("show_destroy_SetValue_Correct0"))
cts.addTest(AttributeUnitTest("show_destroy_SetNone_IsNone"))
cts.addTest(AttributeUnitTest("toString_test"))
cts.addTest(AttributeUnitTest("show_toString_test"))
cts.addTest(AttributeUnitTest("show_destroy_toString_test"))

runner = unittest.TextTestRunner()
runner.run(cts)






