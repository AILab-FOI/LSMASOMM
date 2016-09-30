"""
Abstract class for communicating with a Java JAR implementation of QOCA

Created by Denis Dube, Summer 2005
"""

import os

from AbstractQocaClient import AbstractQocaClient

class PipeQocaClient(AbstractQocaClient):
  
  def __init__(self, command="java -jar D:\QocaServerB1.jar"):
    self.command = command + ' PIPE'
    self.qocaIn = None
    self.qocaOut = None
  
  def connect(self, verbose=False):
    """ Creates a QOCA process and establishes communication with it """
    (self.qocaIn, self.qocaOut) = os.popen2(self.command)
    
    try:
      status = self.read()      # Could this block? 0_0
    except:
      status = ''
    
    if(status == ''): 
      print 'QOCA PIPE connection failed in', __file__
      print 'Tried to start QOCA with', self.command
      print '\n'
      return False
    
    else:
      if(verbose):
        print 'QOCA PIPE connection successfull, recieved "' \
              +str(status).strip('\n')+'"'
        print '\n'
      return True
    
      
  def disconnect(self):
    """ Kills the QOCA process and kills the comm link to it """
    try:
      self.qocaIn.write("")
      self.qocaIn.close()
      self.qocaOut.close()
      return True
    except:
      return False
    
  def read(self):
    """ Reads data from QOCA """
    return self.qocaOut.readline()
  
  def write(self, message):
    """ Writes data to QOCA """
    self.qocaIn.write(message)
    self.qocaIn.flush() # <-- Required on Linux but not on WinXP...
  
  
