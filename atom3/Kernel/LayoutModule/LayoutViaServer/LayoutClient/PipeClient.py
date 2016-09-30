"""
Abstract class for communicating with

Created by Denis Dube, Summer 2005
"""

import os

from AbstractClient import AbstractClient

class PipeClient(AbstractClient):
  
  def __init__(self, command=""):
    if(not command):
      from __init__ import SERVER_PATH
      command = SERVER_PATH
    self.command = command + ' -p'
    self.pipeIn = None  # The process' stdin
    self.pipeOut = None # The process' stdout
  
  def connect(self, verbose=False):
    """ Creates a process and establishes communication with it """
    (self.pipeIn, self.pipeOut) = os.popen2(self.command)
    
    try:
      status = self.read()      # Could this block? 0_0
    except:
      status = ''
    
    if(status == ''): 
      print 'PIPE connection failed in', __file__
      print 'Tried to start with', self.command
      print '\n'
      return False
    
    else:
      if(verbose):
        print 'PIPE connection successfull, recieved "' \
              +str(status).strip('\n')+'"'
        print '\n'
      return True
    
      
  def disconnect(self):
    """ Kills the process and kills the comm link to it """
    try:
      self.pipeIn.flush()
      self.pipeIn.close()
      self.pipeOut.close() 
      return True
    except:
      return False
    
  def read(self):
    """ Reads data from """
    return self.pipeOut.readline()
  
  def write(self, message):
    """ Writes data to """
    self.pipeIn.write(message)
    self.pipeIn.flush() # <-- Required on Linux but not on WinXP...
  
  
