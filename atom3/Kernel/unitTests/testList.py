import unittest

import sys

sys.path.append("../ATOM3Types")
sys.path.append("../UserInterface")
sys.path.append("../GraphGrammar")

from types           import *
from Tkinter         import *
from ATOM3List       import *
from ATOM3String     import *
from ATOM3Exceptions import *

class ListUnitTest(unittest.TestCase):

   def setUp(self):
      self.mainwindow = Tk()
      self.atc = ATOM3List([1,1,1,0], ATOM3String)

   def tearDown(self):
      self.atc.destroy()
      self.atc = None

   # --- SOME getValue() TESTS ---

   def getValueTest_isList(self):
      """getValue() should return an integer"""
      ret = self.atc.getValue()
      assert type(ret) == ListType

   # --- SOME setNone() -- isNone() TESTS ---

   def setNoneIsNoneTest_0(self):
      """Tries setNone() and the isNone()"""
      self.atc.setNone()
      assert self.atc.isNone()

   # --- SOME setValue() TESTS ---

   def setValue_ValidTest_0(self):
      """Tries setValue of [ATOM3String('1'), ATOM3String('2')]"""
      ov = [ATOM3String('1'), ATOM3String('2')]
      self.atc.setValue(ov)
      assert self.atc.getValue() == ov

   def show_setValue_ValidTest_0(self):
      """Tries setValue of [ATOM3String('1'), ATOM3String('2')] (with show)"""
      ov = [ATOM3String('1'), ATOM3String('2')]
      self.atc.setValue(ov)
      self.atc.show(self.mainwindow)
      assert self.atc.getValue() == ov

   def show_destroy_setValue_ValidTest_0(self):
      """Tries setValue of [ATOM3String('1'), ATOM3String('2')] (with show and destroy)"""
      ov = [ATOM3String('1'), ATOM3String('2')]
      self.atc.setValue(ov)
      self.atc.show(self.mainwindow)
      self.atc.destroy()
      assert self.atc.getValue() == ov

   def setValue_InValidTest_0(self):
      """Tries setValue of ATOM3String('1') (an invalid value)"""
      self.assertRaises( ATOM3BadAssignmentValue, self.atc.setValue, ATOM3String('1'))

   # --- SOME newItem() TESTS ---

   def show_setValue_newItem_ValidTest_0(self):
      """Tries setValue of [ATOM3String('1'), ATOM3String('2')] (with show) and then adds a new item ATOM3String('3')"""
      ov = [ATOM3String('1'), ATOM3String('2')]		# Prepare intial value
      self.atc.setValue(ov)
      self.atc.show(self.mainwindow)
      nv = ATOM3String('3')				# Prepare new item...
      self.atc.newItem(nv)
      ov.append(nv)					# This is what we expect!!
      assert self.atc.getValue() == ov

   def setValue_newItem_ValidTest_0(self):
      """Tries setValue of [ATOM3String('1'), ATOM3String('2')] and then adds a new item ATOM3String('3')"""
      ov = [ATOM3String('1'), ATOM3String('2')]		# Prepare intial value
      self.atc.setValue(ov)
      nv = ATOM3String('3')				# Prepare new item...
      self.atc.newItem(nv)
      ov.append(nv)					# This is what we expect!!
      assert self.atc.getValue() == ov

   # --- SOME deleteItem() TESTS ---

   def setValue_show_deleteItem_ValidTest_0(self):
      """Tries setValue of [ATOM3String('1'), ATOM3String('2')] (with show) and then deletes the 2nd element"""
      ov = [ATOM3String('1'), ATOM3String('2')]		# Prepare intial value
      self.atc.setValue(ov)
      self.atc.show(self.mainwindow)
      self.atc.deleteItem(1)				# delete 2nd item
      del ov[1]
      assert self.atc.getValue() == ov

   def setValue_show_deleteItem_InValidTest_0(self):
      """Tries setValue of [ATOM3String('1'), ATOM3String('2')] (with show) and then tries to delete a non-existent element"""
      ov = [ATOM3String('1'), ATOM3String('2')]				# Prepare intial value
      self.atc.setValue(ov)
      self.atc.show(self.mainwindow)
      self.assertRaises(ATOM3ElementOutOfRange, self.atc.deleteItem, 2)	# delete 3nd item -> Error !

   # --- SOME toString() TESTS ---

   def setValue_show_toString_ValidTest_0(self):
      """Tries setValue of [ATOM3String('1'), ATOM3String('2')] (with show) and then call toString"""
      ov = [ATOM3String('1'), ATOM3String('2')]		# Prepare intial value
      self.atc.setValue(ov)
      self.atc.show(self.mainwindow)
      res = self.atc.toString()
      assert type(res) == StringType


cts = unittest.TestSuite()
cts.addTest(ListUnitTest("getValueTest_isList"))
cts.addTest(ListUnitTest("setNoneIsNoneTest_0"))
cts.addTest(ListUnitTest("setValue_ValidTest_0"))
cts.addTest(ListUnitTest("show_setValue_ValidTest_0"))
cts.addTest(ListUnitTest("show_destroy_setValue_ValidTest_0"))
cts.addTest(ListUnitTest("setValue_InValidTest_0"))
cts.addTest(ListUnitTest("show_setValue_newItem_ValidTest_0"))
cts.addTest(ListUnitTest("setValue_newItem_ValidTest_0"))
cts.addTest(ListUnitTest("setValue_show_deleteItem_ValidTest_0"))
cts.addTest(ListUnitTest("setValue_show_deleteItem_InValidTest_0"))
cts.addTest(ListUnitTest("setValue_show_toString_ValidTest_0"))

runner = unittest.TextTestRunner()
runner.run(cts)






