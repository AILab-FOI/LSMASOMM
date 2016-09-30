"""
Simple TCP/IP Client to interface with 

Denis Dube, Summer 2005
"""

from socket import AF_INET, SOCK_STREAM, socket
import os
from threading import Thread




from AbstractClient import AbstractClient

class TcpClient(AbstractClient):
  
  def __init__(self, serverIP='127.0.0.1', serverPort=14059, 
               debug=True):

    self.serverIP = serverIP
    self.serverPort = serverPort
    self.debug = debug
    self.sock = None
    
  
            
    
  def connect(self):
    """ Establishes a TCP/IP connection to self.serverIP on self.serverPort """
     
    self.sock = socket(AF_INET, SOCK_STREAM)

    try:
      self.sock.connect((self.serverIP, self.serverPort))
    except:
      print 'Could not connect to QOCA at',self.serverIP, self.serverPort
      print 'QOCA connection failed in', __file__
      return False

    
      
    input = self.read() 
    input = input.strip()
    input = input.strip('\n')
    status, count = input.split(';')
    if( status == 'BUSY' ):
      print 'ERROR: QOCA server is too busy at IP:',self.serverIP, \
            'Port:',self.serverPort  
      print 'QOCA server has',count, 'simultaneous connections currently'
      print 'QOCA connection failed in', __file__
      return False
    
    elif( self.debug ):
      print 'TCP/IP socket connection established with', self.sock.getpeername() 
      print 'Server status message:',status
      print 'Server load:',int(count)+1,'\n'
      
      
    return True
    
  def read(self):
    """ 
    Reads one newline terminated string from the socket
    Blocks until newline reached
    Returns the string if successful, returns None on error
    """
    buffer = ''
    while( 1 ):
      try:
        buffer += self.sock.recv(32)
      except:
        return None
      if( buffer[-1] == '\n' ): break
    return buffer
  
  
  def write(self, message):
    """
    Sends out message to the socket
    If it is 
    Returns length of message sent on success, None on error
    """
    sentLen = 0
    totalLen = len(message)
    while( sentLen < totalLen ):
      try: 
        sentLen += self.sock.send(message)
      except:
        return None
    return sentLen


  def disconnect(self):
    """ 
    Close the TCP/IP socket connection if it exists 
    Return True if close worked, None if could not close, 
           False if nothing to close
    """
    if( self.sock ):
      try:
        self.write("") # This should do the trick...        
      except:
        raise
      try:
        self.sock.close() 
        return True               
      except:
        return None
    return False
    
    

