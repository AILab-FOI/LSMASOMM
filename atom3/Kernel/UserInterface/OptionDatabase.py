"""
OptionDatabase.py

A flexible application option loader/saver/modifier 

Public Methods:

  - __init__( tkRoot, databaseFilename ):
    Initilizes the database's variables. The databaseFilename is the actual name
    of the file that will be created/modified in the current working directory.
    
  - createNewOption(self,optionKey,initialValue,valueType, promptString):
    Adds the option with the given parameters to the internal option dictionary.
    
  - get(self,optionKey): 
    Returns the current value of the option given by optionKey
    
  - getOptionValueMap(self):
    Returns a dictionary of optionString optionValue pairs
    
  - cloneDatabase(self):
    Creates a database clone and returns it
    
  - set(self,optionKey, value):
    Manually set the value of the option at optionKey.
    
  - showOptionsDatabase(self,position):
    Shows a dialog to modify any of the options interactively. Automatically saves
    if the user presses OK. The dialog can optionally be given a starting position.
    
  - loadOptionsDatabase(self):
    Loads the saved database file. If in doubt, it assumes that the file is 
    corrupt/missing and uses the default values for the options. 
    
  - saveOptionsDatabase(self):
    Saves the database to a file, but only if a lock on it can be acquired.
        
  - releaseOptionLock(self):
    Makes the database available for saving to other AToM3 instances.

Everything else is private! I can't believe it took me more than a year to find
out that this was possible in Python. Oh the horrible bugs I contended with when
I had everything public and lacked even the self-discipline to not use it as such!
I just love the absolute guarantee that the contents of this class won't be 
buggered with on the outside :D

Created June 23, 2004 by Denis Dube
"""

import sys,os,time,string,tkMessageBox,Dialog

from OptionDialog import OptionDialog
from FilePaths    import OPTIONS_PATH, USER_NAME, USER_AREA_RECREATED


class OptionDatabase:
  
  LOCK_TIME_EXPIRATION = 60 * 60 * 8 # <--- 8 hours
  
  def __init__(self, TKroot, databaseFilename, configLabel = "Options Database",
                                                              autoSave = True  ):    
    self.__TKroot = TKroot    
    self.__optionDictionary = dict() # { optionKey : [ value, valueType, promptString,helpString ] }
    self.__optionOrder = []          # [optionKey, ... ] <-- Order to display in
    self.__databaseFilename = databaseFilename
    self.__configLabel = configLabel
    self.__autoSave = autoSave       # Should options be saved when closing dialog
    self.__showWarnings = autoSave   # Displays a warning if options not loaded
    self.__lockFileName = os.path.join( OPTIONS_PATH, 'optionLock.txt' )
    self.__warnIfLocked = True
    #todo: Denis disabled the locks because they were too bloody annoying
    self.__useLocks = False
    
  def get(self, optionKey ):
    """ Returns the value of the option """
    if( self.__optionDictionary.has_key( optionKey ) ):
      return self.__optionDictionary[optionKey][0]
    return None
    
  def getOptionValueMap(self):
    """ Returns a dictionary of optionString optionValue pairs """
    optionValueMap = dict()
    for key in self.__optionDictionary.keys():
      optionValueMap[key] = self.__optionDictionary[key][0]
    return optionValueMap
    
  def cloneDatabase(self):
    """ Creates a database clone and returns it """
    cloneDB = dict()
    for key, value in self.__optionDictionary.items():
      cloneDB[key] = value
    return cloneDB   
    
  def set(self, optionKey, value ):
    """ Sets the value of the option """
    if( self.__optionDictionary.has_key( optionKey ) ):
      self.__optionDictionary[optionKey][0] = value
    
  def createNewOption(self,optionKey,initialValue,optionTuple,promptString,helpString=""):
    """ 
    Stores the option to the option dictionary
    Keeps track of the order in which options are added
    """
    if( not self.__optionDictionary.has_key( optionKey ) ):
      self.__optionDictionary[optionKey] = [initialValue,optionTuple,promptString,helpString]
      self.__optionOrder.append( optionKey )
    
  def showOptionsDatabase(self, position = [100,100] ):
    """ 
    Presents a dialog to configure the options database 
    Returns True if successful, False if canceled
    """    

    dialog = OptionDialog( self.__TKroot,self.__configLabel,
                          self.__optionDictionary,self.__optionOrder,position)
    
    # If not canceled, get the new options and save them to file
    if( not dialog.isCanceled() ):
      self.__optionDictionary = dialog.getOptionsDatabase() 
      if( self.__autoSave ):
        self.saveOptionsDatabase()
      return True
    return False
  

  def loadOptionsDatabase(self):
    """ Loads the options database from a file, on failure, uses defaults """
    
    if(self.__useLocks):
      self.__getOptionDatabaseLock()
    
    # Check if the database file even exists
    databaseFile = os.path.normpath( os.path.join( OPTIONS_PATH, self.__databaseFilename ) )
    if( not os.path.exists( databaseFile ) ):
      if( self.__showWarnings and USER_AREA_RECREATED == 0 ):
        title = 'WARNING: Option Database Error'
        error = 'The following database does not exist: ' + self.__databaseFilename + '\n'
        default = 'A default option datbase will now replace it.\n'
        
        tkMessageBox.showwarning(title, error+'\n'+default, parent=self.__TKroot)
        print title,error,default
        
      # Since it doesn't exist, go ahead and save the defaults
      if( self.__autoSave ):
        self.saveOptionsDatabase()
        
      return
    
    try:  
      # Get rid of the .py extension
      moduleName = string.split( self.__databaseFilename, '.' )[0]

      # Make sure an old copy isn't in memory
      if( sys.modules.has_key( moduleName ) ):
        del sys.modules[ moduleName ]    

      # Place the DB in memory
      exec 'import ' + moduleName
  
      # Load the contents of the dictionary here
      loadedDictionary = eval( moduleName + '.getOptionDictionary()' )
          
    except:
      if( self.__showWarnings ):
        title = 'WARNING: Option Database Error'
        error = 'The following database could not be loaded: ' + self.__databaseFilename + '\n'
        default = 'Default options have been loaded instead\n'
        
        tkMessageBox.showwarning(title, error+'\n'+default, parent=self.__TKroot)
        print title,error,default
        
      return
    
    # Use the loaded dictionary if it is valid
    if( self.__isOptionDictIsValid( loadedDictionary ) ):      
      self.__optionDictionary = loadedDictionary
      
    # Otherwise inform the user of the bad news :p
    elif( self.__showWarnings ):
      title = 'WARNING: Option Database Error'
      error = 'The following database contained an invalid entry: ' + self.__databaseFilename + '\n'
      default = 'Default options have been loaded instead\n'
      
      tkMessageBox.showwarning(title, error+'\n'+default, parent=self.__TKroot)
      print title,error,default
      
            
  def __isOptionDictIsValid( self, loadedDictionary ):
    """ Returns True if the loadedDictionary is valid and can be used """
    
    # Quick check: does the dictionary have the right number of keys & values?
    if( len( loadedDictionary ) != len( self.__optionDictionary ) ):
      return False
    
    # Okay, now it gets hairy, check entry by entry. Remember the dict format...
    # { optionKey : [ value, valueType, promptString, helpString ] }
    for key in loadedDictionary.keys():
      if(key not in loadedDictionary): return False
      if(key not in self.__optionDictionary): return False
      loadEntry = loadedDictionary[ key ]
      defEntry = self.__optionDictionary[ key ]
      
      # Only the value of the option is allowed to be different
      if( loadEntry[1:] != defEntry[1:] ):
        return False
      
    return True
  
     
  def saveOptionsDatabase(self):
    """
    Saves the option database
    Creates a text file with a method that can return the entire DB
    No saving will occur if the DB is locked by another AToM3 instance.
    """
    
    if(not self.__useLocks or self.__isOptionDatabaseUnlocked()):
      
      if(self.__useLocks):
        self.__getOptionDatabaseLock()
        self.__warnIfLocked = True
      
      # Overwrite if exists
      fp=open( os.path.join( OPTIONS_PATH, self.__databaseFilename ) ,"w")
  
      fp.write('"""\n')
      fp.write( self.__databaseFilename + '\n\n')
      fp.write('This file is automatically generated/modified when Options are configured.\n')
      fp.write('If this file is corrupted/deleted, it will be re-created next time Options are configured.\n')
      fp.write('So use the Options dialog instead of messing around in here :D\n\n')
      fp.write('Format: [ initialValue, typeCode, stringPrompt, helpString ] \n')
      fp.write('See OptionDialog.py in UserInterface for typeCodes. \n\n')
      fp.write('Last modified on '+str( time.asctime() )+' by '+USER_NAME+'\n')
      fp.write('"""\n\n')
      
      fp.write( self.__generateDatabaseCode() )
                                
      fp.close()
      return None
      
    elif( self.__warnIfLocked ):
        
      self.__warnIfLocked = False
      lockPID, lockTime, lockUSERNAME = self.__getLockInfoTuple()
      elapsedTime = time.time() - lockTime
      expireTime = ( self.LOCK_TIME_EXPIRATION - elapsedTime ) / 3600
      elapsedTime /= 3600   # <--- Elapsed hours 
      
      shortTitle = "WARNING: Options cannot be saved to file"
      title  = "WARNING: Options cannot be saved because your instance of AToM3 does"
      title += " not have a lock on the option database.\n"
      text  = "This AToM3 instance has process ID: " + str( os.getpid() ) + "\n"
      text += "The options are locked by process ID: " + str( lockPID ) + ", created by user: "+str(lockUSERNAME)+"\n\n"
      text += "The lock is " + str( round( elapsedTime, 2 ) ) + " hours old,"
      text += "and will expire on its own in another " + str( round( expireTime, 2) ) + " hours\n\n"
      text += "The lock file is located here: "
      text += self.__lockFileName + "\n\n"
      print title, text
      
      
      # Note: you could disable lock override if user-names don't match...
      if( USER_NAME == lockUSERNAME ): overideText = 'Override Lock'
      else:                            overideText = 'Override Lock\n(Not Recommended)'
      
      lockDialog = Dialog.Dialog(None, {'title': shortTitle,
                    'text': text,
                    'bitmap': 'warning',
                    'default': 0,
                    'strings': ('Proceed',overideText)})
          
       
      if( lockDialog.num == 0 ):
          return False
      elif( lockDialog.num == 1 ):
          os.remove( self.__lockFileName )
          self.saveOptionsDatabase()
          return True
        
          

    
  def __getOptionDatabaseLock(self):
    """ 
    Acquire a lock on the options database, then only this instance of AToM3
    will have the privilige of being able to save
    """
    
    # Create a new lock file if the options are not locked
    if( self.__isOptionDatabaseUnlocked() ):
      f = open( self.__lockFileName, 'w' )
      f.write( str(os.getpid()) + '\n' )
      f.write( str(time.time()) + '\n' )
      f.write( str(USER_NAME) + '\n' )
      f.close()
                 
    # It is locked, warn the user... but does the user really care yet?
    # NO! He/she doesn't care! Only when they try to save will they cry in agony!
    """
    else:
      text = ""
      text += "AToM3 could not lock down the option database!\n"
      text += "This means either another AToM3 instance is running or AToM3 did"
      text += " not close properly in a previous session.\n"
      text += "If the latter case applies, then feel free to manually delete: "
      text += self.__lockFileName + "\n\n"
    """
      
    
  def __isOptionDatabaseUnlocked( self ):
    """ 
    Determines is unlocked / ready for writing
    If the lock does not match our PID, but is outdated, override the lock
    """
    lockPID, lockTime, lockUSERNAME = self.__getLockInfoTuple()
    
    # Does the lock even exist? 
    if( lockPID or lockTime or lockUSERNAME ):

      # The lockfile has our process ID on it, unlocked :D
      if( lockPID == os.getpid() ):
        return True
      
      # The lock file is locked by someone else... for the past 8 hours!
      # Unlock it. They have no right to hog it that long :p
      elif( lockTime + self.LOCK_TIME_EXPIRATION < time.time() ):
        return True
      
      # It's locked, and we ain't got the key or the time!
      else:
        return False
      
    # No lock!
    return True
  
  def __getLockInfoTuple( self ):
    """ 
    Returns the process ID of the last AToM3 instance to lock the option DB,
    and the time at which it did so. If no lock file, returns an empty tuple.
    Uses a Try/Except clause in case the lock file is corrupted.
    """    
    if( os.path.exists( self.__lockFileName ) and os.path.isfile( self.__lockFileName ) ):
      try:
        f = open( self.__lockFileName, 'r' )
        lockPID = int( float( f.readline() ) )
        lockTIME = float( f.readline() ) 
        lockUSERNAME = f.readline()
        lockUSERNAME = string.strip( lockUSERNAME, '\n' )
        f.close()
        return (lockPID,lockTIME,lockUSERNAME)
      except:
        return (None,None,None)
    return (None,None,None)
    
  def releaseOptionLock( self ):
    """ 
    Releases the lock on the OptionDatabase so other AToM3 instance can save options.
    The lock is meant to last the duration of an AToM3 session.
    
    WARNING: Failure to release the lock means other AToM3 sessions will not be
    able to save options until the time limit expires ( 8 hours ).
    """
    
    # Does the lock even exist?
    if( os.path.exists( self.__lockFileName ) and os.path.isfile( self.__lockFileName ) ):
      
      # Do we *own* the lock?
      if( self.__isOptionDatabaseUnlocked() ):
        
        os.remove( self.__lockFileName )
        
  
        

  def __generateDatabaseCode(self):
    """ Generates code to export the option dictionary, internal subroutine """

    code = ""
    code += "def getOptionDictionary():\n\n"
    code += "  optionDictionary = dict()\n"
    
    for option in self.__optionOrder:
      
      initialValue,optionTuple,promptString,helpString = self.__optionDictionary[option]
            
      code += "\n"
      
      # Save the option the quick & easy way (but also less readable way)
      code += "  optionDictionary['" + str(option) + "'] = "+ str( self.__optionDictionary[option] )
        
      '''        
      # Save the option the long & quickly out of sync with OptionDialog.py way
      
      # Initial Value
      if( type(initialValue) == type(str()) ):
        code += "  optionDictionary['" + str(option) + "'] = ['"+initialValue+"'] # Saved Value\n" 
      else:
        code += "  optionDictionary['" + str(option) + "'] = ["+str(initialValue)+"] # Saved Value\n" 
      
      # Just one typeCode
      if( len( optionTuple) >= 1 ):        
        code += "  optionDictionary['" + str(option) + "'].append( ["+str(optionTuple[0])+"] ) # Dialog Type Code\n" 
      
      # Label Options
      if( optionTuple[0] == OptionDialog.LABEL ):
        code += "  optionDictionary['" + str(option) + "'][1].append('"+str(optionTuple[1])+"') # Font\n" 
        code += "  optionDictionary['" + str(option) + "'][1].append('"+str(optionTuple[2])+"') # Color\n" 
        code += "  optionDictionary['" + str(option) + "'][1].append('"+str(optionTuple[3])+"') # Justification\n" 
      
      # Enumeration Options
      elif( optionTuple[0] == OptionDialog.ENUM_ENTRY ):        
        for i in range( 1, len(optionTuple) ):
          code += "  optionDictionary['" + str(option) + "'][1].append('"+str(optionTuple[i])+"') # Enumeration String "+str(i)+"\n" 
        
      else:
        # typeCode and a button label
        if( len( optionTuple) >= 2 ):      
          code += "  optionDictionary['" + str(option) + "'][1].append('"+str(optionTuple[1])+"') # Button Label\n" 
        # typeCode, label, and a file type mask
        if( len( optionTuple) >= 3 ):          
          code += "  optionDictionary['" + str(option) + "'][1].append("+str(optionTuple[2])+") # File Type Mask\n" 
      
      # Prompt String
      code += "  optionDictionary['" + str(option) + "'].append('"+str(promptString)+"') # Prompt String\n"
      
      # Help String
      if( helpString != "" ):
        code += "  optionDictionary['" + str(option) + "'].append('"+str(helpString)+"') # Help String\n" 
      else:
        code += "  optionDictionary['" + str(option) + "'].append( '' ) # Help String\n" 
      '''
    code += "\n  return optionDictionary\n"
    return code          
