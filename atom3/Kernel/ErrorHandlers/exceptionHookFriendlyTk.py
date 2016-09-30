"""
exceptionHookFriendlyTk.py

A superclass of Tk that passes exceptions to the sys.excepthandler instead
of just dumping it in the stderr stream
"""

import sys, Tkinter

class exceptionHookFriendlyTk( Tkinter.Tk ):
  def report_callback_exception(self, exc, val, tb):
      """ Tkinter error callback, forwarded to the sys.excepthandler """
      sys.last_type = exc
      sys.last_value = val
      sys.last_traceback = tb
      return sys.excepthandler(exc,val,tb)