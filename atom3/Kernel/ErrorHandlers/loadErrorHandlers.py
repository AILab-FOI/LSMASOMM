"""
loadErrorHandlers.py

Just loads the uncaught exception handling routines
"""
import sys

# This will silence those stupid Syntax Warning we know about but can't fix
# without completely re-writing AToM3
try:
  from warnings import simplefilter
  simplefilter('ignore',category=SyntaxWarning, append=1)
except:
  print 'WARNING: your version of Python lacks the "warnings" module'
  print 'Skipping syntax warning filter... so more spam in your console!\n'
  
# Catch errors directly from the excepthandler, may not always work
# since some modules will bypass this and dump straight to stderr
from excepthandler import excepthandler
sys.excepthandler = excepthandler

# Catches stderr dumps
from exceptionStreamHook import applyHook2stderr
applyHook2stderr()