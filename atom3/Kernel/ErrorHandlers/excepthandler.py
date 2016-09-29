"""
excepthandler.py

A custom sys.excepthandler by Denis Dube, http://msdl.cs.mcgill.ca/people/denis/

Special handling of uncaught errors:
1. It will issue a GUI warning that an exception has occured.
2. It will log the error to a log file.
3. It will issue (via GUI,log, and console) an incident number unique to the error.
"""

import tkMessageBox, sys, re, string, time, os, traceback

# HV 18/1/2008
# Log to errorLog.log in user-specific temp directory
# Fixes problems with central installation where writing
# to a central log file is impossible due to:
#  1. permissions (users are not allowed to write to central installation directory)
#  2. multiple concurrent users (need their own individual log files)
# Used to be: 
#
#try:
#  from FilePaths import BASE_PATH
#except:
#  BASE_PATH = os.getcwd()
#
# LOG_FILENAME = os.path.join(BASE_PATH,'errorLog.log')

try:
  from FilePaths import TEMP_FILE_PATH 
except:
  TEMP_FILE_PATH = os.getcwd()

LOG_FILENAME = os.path.join(TEMP_FILE_PATH,'errorLog.log')
LOGGED_ERRORS_DICT = dict()
MAX_SUPPORT_TICKET = 100000


def excepthandler( exceptionTypeObject, exceptionValueObject, tracebackObject ):

  # The type of the error
  exceptionTypeString = ''
  for line in traceback.format_exception_only(exceptionTypeObject, ''):
    exceptionTypeString += line
  exceptionTypeString = string.replace( exceptionTypeString, '\n', '' )
  
  # The value of the error
  exceptionValueString = str( exceptionValueObject )
    
  # Get the traceback string
  tracebackTuple = traceback.format_exception(exceptionTypeObject, 
                                        exceptionValueObject,tracebackObject)
  tracebackString = ''
  for tracebackLine in tracebackTuple[:-1]:
    tracebackString += tracebackLine
  
  # Generate a unique number that is platform independent for the error
  tracebackQuadTuple = traceback.extract_tb(tracebackObject)
  hashableString = ''
  for tracebackLine in tracebackQuadTuple:
    for element in tracebackLine[1:]:
      hashableString += str( element )
  incidentID = str(  hash( hashableString ) % MAX_SUPPORT_TICKET  )
  
  # Get the time :D
  timeOfError = time.asctime()
  
  # Have the error reporters deal with this...
  args = [exceptionTypeString, exceptionValueString, tracebackString,
          incidentID, timeOfError]
  consoleReporter( *args )
  logReporter( *args )
  guiReporter( *args )
  
def consoleReporter( type, value, trace, ID, time ):
  """ Show error info in console """
  print '\n\nUnique error support ticket: ' + ID + \
                  ' ('+type+' logged to ' +LOG_FILENAME + ')'
  
  if(not LOGGED_ERRORS_DICT.has_key( ID ) ):
    print '--------------------------------------------------'
    print type+': '+value + '\n\n' + trace 
    print '--------------------------------------------------'
          
def logReporter( type, value, trace, ID, time ):
  """ Log error to file """
  logFile=open(LOG_FILENAME, "a")
  # Check if the error has already been logged this session, if so, short ver.
  if( LOGGED_ERRORS_DICT.has_key( ID ) ):
    logFile.write( 'Error ID#'+ID+' occured again on '
                      +time + '\n\n' )
  else:
    logFile.write( 'Error ID#'+ID+' occured on '+time 
                      + '\n'+type+': '+value + '\n\n'
                      + trace + '\n' )
    LOGGED_ERRORS_DICT[ID] = True
  logFile.close()
  
def guiReporter( type, value, trace, ID, time ):   
  """ Display error to interactive user """
  tkMessageBox.showerror( type,
                        trace +'\n\n'+ value 
                        + '\n\nUnique error support ticket: '+ ID
                        + '\nError logged to '+LOG_FILENAME )  

 
