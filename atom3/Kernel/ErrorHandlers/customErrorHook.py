"""
customErrorHook.py

A custom stderr hook by Denis Dube, http://msdl.cs.mcgill.ca/people/denis/

This will supress the traceback in the console, but:
1. It will issue a GUI warning that an exception has occured.
2. It will log the error to a log file.
3. It will issue via GUI and console an incident number unique to the error.
"""

import tkMessageBox, sys, re, string, time, os

try:
#  from FilePaths import BASE_PATH
  from FilePaths import USER_PATH
except:
#  BASE_PATH = os.getcwd()
  USER_PATH = os.getcwd()
  
class customErrorHook:
  """ 
  This class pretends to be an open stderr file stream 
  Perhaps it should subclass File to be safer... but what would be the default
  behaviour then??? Must I override each method on at a time? Bah, like anyone
  uses that on stderr...
  """
  
  def __init__(self):
    self.initilize()
    
    self.logFileName = os.path.join(USER_PATH,'errorLog.log')
    self.loggedErrors = dict()
    
    self.regexpTypeValue = re.compile( '(\w*):([^\n]*)' )
    self.regexpFile = re.compile( ' *File' )
    self.regexpFilenameLineno = re.compile(  '\w*.py", line[^\n]*' )
    
  def initilize(self):
    self.expectTraceback = False    
    self.expectTraceLine = False
    self.expectErrorValue = False
    
    self.errorValue = None
    self.errorType = None
    self.errorTrace = None
    
    self.errorMessage = ''
    self.hashableMessage = ''
    
  def write( self, errorString ):
    """ Simulates the write method of a file stream object """
    # Send the error back where it belongs
    sys.__stderr__.write( errorString ) 
    #print ">"+errorString+"<"
    
    # Dealing with a new exception
    if( errorString[:9] == 'Exception' ): 
      self.initilize()      
      
    # Threads can dump the entire error at once on us...
    if( errorString[:19] == 'Exception in thread' ):
      linesList = string.split( errorString, sep='\n' )
      for i in range( len(linesList) ):
       self.processError(  linesList[i] + '\n' )
       
    # Recieving error one line at a time
    else:
      self.processError( errorString )
    
    
  def processError( self, errorString):    
    """ Extract pertinent info from the error stream """
    
    # Ignore empty lines
    if( string.strip( errorString ) == '' ):  pass
    
    # We are processing strings inside the traceback
    elif( self.expectTraceback ):
      
      # Each line in the error traceback is preceded by a 'File' string
      # This case is entered if the 'File' string is present
      if( self.regexpFile.search(errorString) ): 
        self.expectTraceLine = True
        
        # Gather a hashable string to make a platform independent unique
        # incident number for this execption
        # Typical hash string: 'KeyBinds.py", line 269, in <lambda>'
        match = self.regexpFilenameLineno.search( errorString )
        if( match ):
          self.hashableMessage += match.group(0)
   
      # We expect a traceback line following the 'File' line
      elif( self.expectTraceLine ):
        self.expectTraceLine = False
        
      # Unexpected line, trackeback must be over!
      else:        
        # The accumulated errorMessage is really the complete traceback
        self.errorTrace = self.errorMessage
        self.expectTraceback = False
        
        # The error type follows the traceback
        # Use reg exp to seperate type from value: 'ErrorType: ErrorValue'
        match = self.regexpTypeValue.search( errorString )
        if( match ):
          self.errorType, self.errorValue = match.groups()          
          # All info available, deal with it!  
          return self.handleError()      
        
        # Some errors give 'ErrorType',':', 'ErrorValue'
        else:
          self.errorType = errorString
          self.expectErrorValue = True
          
    elif( self.expectErrorValue and string.strip( errorString ) != ':' ):
      self.expectErrorValue = False
      
      self.errorValue = errorString
      # All info available, deal with it!  
      return self.handleError()      

    # A traceback always starts with the 'Traceback' string
    elif( errorString[:9] == 'Traceback' ): 
      self.expectTraceback = True    
      
    # Accumulate the error message
    self.errorMessage += errorString
    
  def handleError( self ):
    #print 'ERROR type:', self.errorType
    #print 'ERROR value:', self.errorValue
    #print 'ERROR traceback:\n', self.errorTrace
    
    incidentID = str(  hash(self.hashableMessage) % 100000  )
    timeOfError = time.asctime()
    
    print '\n\nUnique error support ticket: ' + incidentID + ' (Error logged to '\
            +self.logFileName + ')'
    
    # Log error to file
    try:
      logFile=open(self.logFileName, "a")
    except:
      print 'ERROR: Unable to log error!', __file__
      return
    if( self.loggedErrors.has_key( incidentID ) ):
      logFile.write( 'Error ID#'+incidentID+' occured again on '
                         +timeOfError + '\n\n' )
    else:
      logFile.write( 'Error ID#'+incidentID+' occured on '+timeOfError 
                        + '\n'+self.errorType+': '+self.errorValue + '\n\n'
                        + self.errorTrace + '\n' )
      self.loggedErrors[incidentID] = True
      print 'Error ID#'+incidentID+' occured on '+timeOfError \
                        + '\n'+self.errorType+': '+self.errorValue + '\n\n' \
                        + self.errorTrace + '\n'
    logFile.close()
    #import Tkinter
    #TkRoot = Tkinter.Tk()
    # Display error to interactive user
    tkMessageBox.showerror( self.errorType,
                          self.errorTrace +'\n\n'+ self.errorValue 
                          + '\n\nUnique error support ticket: '+ incidentID
                          + '\nError logged to '+self.logFileName )  
  
    self.initilize() # Reset vars    
                               
  def close( self, *args ): pass
  def open( self, *args ): pass
  
  
def applyHook2stderr():
  # Redirect error output stream to customized handler
  sys.stderr = customErrorHook()





if __name__ == '__main__':
  print "Testing error redirect"
  applyHook2stderr()
  5/0
  x=bs
  print "Done"