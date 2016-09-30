"""
Abstract class for communicating with an external server

Created by Denis Dube, Summer 2005
"""

class AbstractClient:
  
  def __init__(self):
    raise Exception, 'Thou shalt not instantiate abstract classes'
  
  def connect(self):
    """ Creates a QOCA process and establishes communication with it """
    raise Exception, 'Thou shalt implement me in concrete classes'
  
  def disconnect(self):
    """ Kills the QOCA process and kills the comm link to it """
    raise Exception, 'Thou shalt implement me in concrete classes'
  
  def read(self):
    """ Reads data from QOCA """
    raise Exception, 'Thou shalt implement me in concrete classes'
  
  def write(self):
    """ Writes data to QOCA """
    raise Exception, 'Thou shalt implement me in concrete classes'
  
  
  
if(__name__ == '__main__' ):
  AbstractClient()