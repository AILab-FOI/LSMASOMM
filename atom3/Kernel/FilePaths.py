"""
FilePaths.py

Groups the entire hard-coded relative paths structure in one file.
Looks rather ugly... but that's file path manipulation for you :p

Created July 27, 2004 by Denis Dube
"""

import os
import sys
import string
import Dialog

from __init__ import BASE_PATH

class TempFileManager:
  """
  This class stores temporary directories. 
  It deletes the directory if it already exists (and everything in it) and 
  creates a fresh one. 
  When the destroy method is called, all the temporary directories are killed.
  """
  
  PATH_LIST = []
  isINITILIZED = False
  def __init__(self, pathList=None ):
    if( not TempFileManager.isINITILIZED and pathList ):
      TempFileManager.PATH_LIST = pathList
      TempFileManager.isINITILIZED = True
            
      # Remove the directory if it exists & re-place it with an empty
      for path in TempFileManager.PATH_LIST:
        self.DirectoryDeleter( path )
        os.mkdir( path )
      
  def destroyDirContents(self, dir ):
    for d in os.listdir(dir):
      pathname = os.path.join( dir, d )
      if( os.path.isdir( pathname ) ): 
        self.DirectoryDeleter( pathname) 

  def destroy(self):
    for path in TempFileManager.PATH_LIST:
      self.DirectoryDeleter( path )
    
  def DirectoryDeleter( self, dir, isInitialCall=True, showActivity=False ):
    """ Kills a directory & everything in it & show no mercy """
    
    # Sneak attack by a non-directory!
    if( isInitialCall ):
      if( not os.path.exists( dir ) ):
        return
      elif( not os.path.isdir( dir ) ):
        return os.path.remove( dir )  
    
    for f in os.listdir(dir):
      pathname = os.path.join( dir, f )

      # It's a directory, recurse into it
      if( os.path.isdir( pathname ) ):            
        self.DirectoryDeleter(pathname, isInitialCall = False)
        if( showActivity ): print 'Deleting dir: ', pathname
        os.rmdir( pathname )
          
      # It's a file, kick it in the nutz
      elif( os.path.isfile( pathname )  ):            
        if( showActivity ): print 'Deleting file: ', pathname
        os.remove( pathname )
          
      # It's a symbolic link, break it
      elif( os.path.islink( pathname ) ):            
        if( showActivity ): print 'Deleting symbolic link: ', pathname
        os.remove( pathname )
          
      # Unknown file type, print a message
      else:            
        if( showActivity ): print 'Skipping %s' % pathname
            
    if( isInitialCall ):
      if( showActivity ): print 'Deleting root dir: ', dir
      os.rmdir( dir )
      
      
#-------------------------- Class definition over ----------------------------




# Platform specific USER_NAME & USER_PATH
if( sys.platform.lower().find( 'win' ) != -1 ):
  if( os.environ.has_key( 'HOMEDRIVE' ) and os.environ.has_key( 'HOMEPATH' ) ):
    USER_PATH         = os.path.join( os.environ[ 'HOMEDRIVE' ], os.environ[ 'HOMEPATH' ] )
    USER_PATH         = os.path.normpath( os.path.join( USER_PATH, 'AToM3' ) )
  else:
    USER_PATH         = os.path.normpath( os.path.join( BASE_PATH, 'User' ) )
  if( os.environ.has_key( 'USERNAME' ) ):
    USER_NAME         = os.environ[ 'USERNAME' ]
  else:
    USER_NAME         = "Unamed"
else:
  if( os.environ.has_key( 'HOME' ) ):
    USER_PATH         = os.path.normpath( os.path.join( os.environ['HOME'] , '.AToM3' ) )
  else:
    USER_PATH         = os.path.normpath( os.path.join( BASE_PATH, 'User' ) )
  if( os.environ.has_key( 'LOGNAME' ) ):
    USER_NAME         = os.environ[ 'LOGNAME' ]
  else:
    USER_NAME         = "Unamed"

MODEL_PATH            = os.path.normpath( os.path.join( BASE_PATH, 'Models' ) )
META_MODEL_PATH       = os.path.normpath( os.path.join( BASE_PATH, 'Formalisms' ) )
EXTERNAL_SOURCE_PATH  = os.path.normpath( os.path.join( BASE_PATH, 'External' ) )
SOURCE_CODE_PATH      = os.path.normpath( os.path.join( BASE_PATH, 'Kernel' ) )

GRAPHIC_EDITOR_DATA   = os.path.normpath( os.path.join( SOURCE_CODE_PATH, os.path.join( 'GraphicEditor', 'data' ) ) )
HELP_PATH             = os.path.normpath( os.path.join( SOURCE_CODE_PATH, 'HelpDocuments' ) )

SESSION_DATA_PATH     = os.path.normpath( os.path.join( USER_PATH, 'SessionData' ) )

OPTIONS_PATH          = os.path.normpath( os.path.join( SESSION_DATA_PATH, 'Options' ) )
TEMP_FILE_PATH        = os.path.normpath( os.path.join( SESSION_DATA_PATH, 'TempFiles' ) )

COPY_DIRECTORY        = os.path.normpath( os.path.join( TEMP_FILE_PATH, "CopyBuffer_" + str(os.getpid()) ) ) 
UNDO_DIRECTORY        = os.path.normpath( os.path.join( TEMP_FILE_PATH, "Undo_" + str(os.getpid()) ) )


def forcePathExistence( path ):
  """ If the the given directory path doesn't exist, create the directory """
  if( not ( os.path.exists( path ) and os.path.isdir( path ) ) ):
    # Try to make the directory, may fail
    try:     os.mkdir( path )
    except:  return -1    
    print "Creating new directory: " + os.path.normpath( path )
    return 1    
  return 0

    
# Force the existence of the "User" session information. 
USER_AREA_RECREATED = 0
for path in [ USER_PATH, SESSION_DATA_PATH, OPTIONS_PATH, TEMP_FILE_PATH ]:
  code = forcePathExistence( path )
  if( code == -1 ):
    print "ERROR: unable to create user session directory ", path
  elif( code == 1 ):
    USER_AREA_RECREATED += 1
    
    
    
# Stored in the "User" session information lies a script with a path to additional
# user area paths...
oldSysPath = sys.path[:] #<-- copy the old sys.path
sys.path.append( USER_PATH )

try:
  from UserPathScript import USER_AREA_PATH
  
except:
  import tkMessageBox, tkFileDialog
  
  def getUserAreaPath( showDialog = True ):
    """ Gets the user area path from the user... """
    
    if( showDialog ):
      tkMessageBox.showinfo(  "AToM3 Setup",
        "Configuring AToM3 installation...\n\n"+
        "Please choose the directory where you would like to save new:\n"+ 
        "    Models\n"+
        "    Formalisms\n"+
        "    External Resources\n\n"+
        "NOTE: if you need to create a new directory, you may need to "+
        "use an external program/console to do so.")  
    
    try:
      USER_AREA_PATH = tkFileDialog.asksaveasfilename(
                      title="Select a directory for 'User Area'",
                      filetypes=[("All files","*")], 
                      initialfile='Filename_Will_Be_Ignored' )
                      #initialdir='' )
      if( USER_AREA_PATH != '' ): 
        USER_AREA_PATH = os.path.split( USER_AREA_PATH )[0]
    except:
      USER_AREA_PATH = tkFileDialog.askdirectory( title='Select User Area Directory' ) 
    
    # The user cancelled on us! Bah, he/she won't get away with it!
    if( USER_AREA_PATH == '' ):  
      tkMessageBox.showinfo(  "Installation Cancelled",
            "AToM3 will now close since no user area path was given")  
      sys.exit(1)
      #return getUserAreaPath( showDialog=False )
    
    # Doesn't exist? Not a problem.
    if( not os.path.exists( USER_AREA_PATH ) ):
      try:
        os.mkdir( USER_AREA_PATH )
        print "Creating new directory: " + USER_AREA_PATH
      except:
        tkMessageBox.showerror(  "Invalid Directory",
            "Please choose a valid directory for the user area.\n\n"+
            "If creating a new directory, it can only be one level deeper "+
            "than an existing directory.")
        return getUserAreaPath( showDialog=False )
      
    return os.path.normpath( USER_AREA_PATH )
  
  # Get the path, and replace escape characteres with something safe
  USER_AREA_PATH = getUserAreaPath()
  USER_AREA_PATH = string.replace( USER_AREA_PATH, '\\', '\\\\' )
    
  # We now have a new USER_AREA_PATH, so save it
  f = open( os.path.join( USER_PATH, 'UserPathScript.py' ), 'w' )
  f.write( '"""\nUserPathScript.py\n\nAutomatically created script with the path '+
           'to the user area where models, formalisms, and external source is stored '+
           '\n"""\n\nUSER_AREA_PATH = \'' + USER_AREA_PATH + '\'\n' )
  f.close()
  
  tkMessageBox.showinfo(  "Installation setup complete",
            "AToM3 will now close to complete the installation." +
            "\n\nNOTE: Further options will be set for the first time when" +
            'you restart AToM3, so please ignore the "Errors"')
  
sys.path = oldSysPath

USER_MMODEL_PATH      = os.path.normpath( os.path.join( USER_AREA_PATH, 'User Formalisms' ) )
USER_MODEL_PATH       = os.path.normpath( os.path.join( USER_AREA_PATH, 'User Models' ) )
EXTERNAL_USER_PATH    = os.path.normpath( os.path.join( USER_AREA_PATH, 'User External' ) )
    
# Force the existence of the "User" formalisms, models, and external dir paths.
for path in [ USER_MMODEL_PATH, USER_MODEL_PATH, EXTERNAL_USER_PATH ]:
  code = forcePathExistence( path )
  if( code == -1 ):
    print "ERROR: unable to create user directory ", path
    print "Deleting old user-path pointer file. Please re-run AToM3 to choose new user directory"
    try:
      os.remove( os.path.join( USER_PATH, 'UserPathScript.py' ) )
      os.remove( os.path.join( USER_PATH, 'UserPathScript.pyc' ) )
    except:
      print "Failed to remove old user path script. Try removing it manually."
      print "It is located at: ", os.path.join( USER_PATH, 'UserPathScript.py' )
    sys.exit(0)

# This will handle the creation/destruction of temporary Undo & Copy subdirectories
TempFileManager( [ UNDO_DIRECTORY, COPY_DIRECTORY ] )

# The EXTERNAL_USER_PATH path is special, it is expected to have a script in it...
EXTERNAL_USER_SCRIPT = os.path.normpath( os.path.join( EXTERNAL_USER_PATH, 'ExternalUserPaths.py' ) )
if( not ( os.path.exists( EXTERNAL_USER_SCRIPT ) and os.path.isfile( EXTERNAL_USER_SCRIPT ) ) ):
  scriptCode = '''"""
ExternalUserPaths.py

1) Source code dropped into a subdirectory of the External folder will be
automatically placed in the AToM3 import search path (code is ready to use).

2) Source code in an arbitrary location can be added to the AToM3 import search
path by adding an absolute directory path string to the EXTERNAL_PATHS list.

Ex: EXTERNAL_PATHS = [ 'M:\Python23\SVM', 'J:\Utils\LP_SOLVE' ] 

NOTE: This file is automatically re-generated if missing (minus the custom paths).

Created August 13, 2004 by Denis Dube
"""

EXTERNAL_USER_PATHS =  []
'''
  f = open( EXTERNAL_USER_SCRIPT, 'w' )
  f.write( scriptCode )
  f.close()

def doTempFileCleanup():
  TempFileManager().destroy()
  
def doTempCleanupALL():
  TempFileManager().destroyDirContents(TEMP_FILE_PATH)  
  
def doTempCleanupChoice():
  numTempFiles = 0
  for dir in os.listdir(TEMP_FILE_PATH):
    for file in os.listdir(os.path.join(TEMP_FILE_PATH, dir)):
      numTempFiles += 1
  if(numTempFiles > 10):
    dialog = Dialog.Dialog(None, {'title': "Temporary Files",
                      'text': str(numTempFiles) + " temporary files were found"
                      + " in the session folder:\n" + TEMP_FILE_PATH
                      + "\n\nIf you are NOT running another instance of AToM3"
                      + " you may safely delete them",
                      'bitmap': '',
                      'default': 1,
                      'strings': ('Delete!','Cancel')})
    if( dialog.num == 0 ): 
      TempFileManager().destroyDirContents(TEMP_FILE_PATH)      
  

def getCriticalPaths():
  """ 
  These paths contain code essential to the operation of AToM3 
  By adding them to sys.paths they become available for code imports 
  as if they were al in the same directory.
  NOTE: Special care must be taken that 2 files not have the same name!!!
  """

  pathList = [ OPTIONS_PATH, SOURCE_CODE_PATH, COPY_DIRECTORY, UNDO_DIRECTORY,
               EXTERNAL_SOURCE_PATH, EXTERNAL_USER_PATH ]
  
  # Paths to source in the primary SOURCE_CODE_PATH
  pathList = appendPathContentsToList( SOURCE_CODE_PATH, pathList )
     
  # Paths to programs that are somewhat external to AToM3 
  pathList = appendPathContentsToList( EXTERNAL_SOURCE_PATH, pathList )
      
  # Paths to programs that are somewhat external to AToM3 in the User space
  pathList = appendPathContentsToList( EXTERNAL_USER_PATH, pathList )
                               
  # Puts the paths in the sys.path
  appendPathsToSysPath( pathList )
      
  # At this point, EXTERNAL_SOURCE_PATH & EXTERNAL_USER_PATH are in sys.path
  try:
    import ExternalPaths    
    newPaths = ExternalPaths.EXTERNAL_PATHS
    appendPathsToSysPath( newPaths )
    pathList += newPaths 
  except:
    print "WARNING: Could not find the ExternalPaths script in the central area!"
    
  try:
    import ExternalUserPaths  
    newPaths = ExternalUserPaths.EXTERNAL_USER_PATHS
    appendPathsToSysPath( newPaths )
    pathList += newPaths 
  except:
    print "WARNING: Could not find the ExternalPaths script in the user area!"
      
  # Somehow, we may have a duplicate anyway
  nonDuplicatedPaths = []
  for path in sys.path:
    if( path not in nonDuplicatedPaths ):
      nonDuplicatedPaths.append( path )
  sys.path = nonDuplicatedPaths
  
  return pathList
  


# ----------------------------- INTERNAL UTILITIES ---------------------------

def appendPathsToSysPath( pathList ):
  """ Add in the paths to sys.path if necessary """
  for path in pathList:
    if( path not in sys.path ): 
      sys.path.append( path )

def appendPathContentsToList( path, pathList ):
  """ Finds all the subdirectories of path (1st level) and adds to pathList """
  for directoryName in os.listdir( path ):
    directoryName = os.path.join( path, directoryName )
    if( os.path.isdir( directoryName ) ):
      pathList.append( directoryName )
  return pathList
  

  
