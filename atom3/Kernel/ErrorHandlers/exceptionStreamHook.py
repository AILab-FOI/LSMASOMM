"""
exceptionStreamHook.py

A custom stderr hook by Denis Dube, http://msdl.cs.mcgill.ca/people/denis/
"""

import tkMessageBox, sys

  
class exceptionStreamHook:
  """ 
  This class pretends to be an open stderr file stream 
  Perhaps it should subclass File to be safer... but what would be the default
  behaviour then??? Must I override each method on at a time? Bah, like anyone
  uses that on stderr...
  """

    
  def write( self, errorString ):
    """ Simulates the write method of a file stream object """
    
    # Send the error back where it belongs
    sys.__stderr__.write( errorString ) 
    #print ">"+errorString+"<"
    
    # Dealing with a new exception
    if( errorString[:9] == 'Exception' ): 
      tkMessageBox.showerror( 'Uncaught Exception', 
                             'See console for details\n\n' + errorString )    
                               
  def close( self, *args ): pass
  def open( self, *args ): pass
  
  
def applyHook2stderr():
  # Redirect error output stream to customized handler
  sys.stderr = exceptionStreamHook()





if __name__ == '__main__':
  print "Testing error redirect"
  applyHook2stderr()
  5/0
  x=bs
  print "Done"