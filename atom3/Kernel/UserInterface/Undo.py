"""
Undo.py

Provides AToM3 with a working though very inefficient undo/redo mechanism
by using/abusing the save/load functionality of AToM3. 

Created July 13, 2004 by Denis Dube
Previously created about 1 week ago then accidently deleted before integration
into the main AToM3 code branch :p
"""

import os, string, sys

from FilePaths import UNDO_DIRECTORY as UNDO_DIR

class Undo:
  
  UNDO_DIRECTORY    = UNDO_DIR
  UNDO_BUFFER_PATH  = os.path.join( UNDO_DIRECTORY, "UndoBuffer.py" )
  UNDO_BUFFER_PATHC = os.path.join( UNDO_DIRECTORY, "UndoBuffer.pyc" )
  
  def __init__(self, atom3i ):
    
    self.atom3i = atom3i
    
    # Don't allow AToM3 secondary instances undo, can cause exceptions!
    self.__isMainKernel = atom3i.IsMainKernel
    if( self.__isMainKernel ):
      self.__undoEnabled = True
    else:
      self.__undoEnabled = False
      
    self.__modificationsPerSave = 0
    self.__modificationsSinceLastSave = 0
    
    self.__undoStackTop = 0
    self.__undoStackCurr = 0
    self.__undoStackBot = 0
    self.__undoStackMax = 20
    
    
  def setUndoParameters(self, enabled, maxUndo, modificationsPerSave ):
    # Don't allow AToM3 secondary instances undo, can cause exceptions!
    if( self.__isMainKernel ):
      self.__undoEnabled = enabled
    else:
      self.__undoEnabled = False
    self.__undoStackMax = maxUndo
    self.__modificationsPerSave = modificationsPerSave
    
  def isUndoable(self):
    """ Return true if it is possible to undo at present """
    
    if( not self.__undoEnabled ): return False
    # Special case: at init no undo possible yet :D
    if( self.__undoStackBot == self.__undoStackTop ): return False    
    # Can't undo, reached the bottom of the stack
    lastSavePointer = ( self.__undoStackCurr - 2 ) % self.__undoStackMax
    if( lastSavePointer == (self.__undoStackBot - 1) % self.__undoStackMax ): return False
    return True
  
  def isRedoable(self):
    """ Return true if it is possible to redo at present """
    
    if( not self.__undoEnabled ):   return False
    # Top of stack reached
    if( self.__undoStackCurr == self.__undoStackTop ):  return False
    return True
    
  def redo( self ):
    """ Redoes an undo... dang that sounds wierd """

    if( self.isRedoable() ):
      number = "%04d" % ( self.__undoStackCurr ) 
      self.__undoStackCurr = (self.__undoStackCurr + 1) % self.__undoStackMax
      numberPath = os.path.join( self.UNDO_DIRECTORY, number )  
      self.__clearAndLoad( numberPath )
    
  def undo(self):
    """ Restores the model to the way it was last modification save """
    
    if( self.isUndoable() ):
      lastSavePointer = ( self.__undoStackCurr - 2 ) % self.__undoStackMax
      number = "%04d" % ( lastSavePointer ) 
      self.__undoStackCurr = (self.__undoStackCurr - 1) % self.__undoStackMax
      numberPath = os.path.join( self.UNDO_DIRECTORY, number )  
      self.__clearAndLoad( numberPath )
          
  def modelMofificationOccured(self):
    """ Modification occured? Better store it (Mmm, typo in method name)"""
    
    if( not self.__undoEnabled ): 
      return
    elif( self.__modificationsSinceLastSave < self.__modificationsPerSave ): 
      self.__modificationsSinceLastSave += 1
      return
    else:
      self.__modificationsSinceLastSave = 0
      
    if(not self.atom3i.ASGroot):
      return
      
    # try the global constraints...
    res = self.atom3i.ASGroot.preCondition(self.atom3i.ASGroot.SAVE)						# evaluate global pre-conditions
    if res: return self.atom3i.constraintViolation(res)					# if violated, show warning and do not save
    
    # try the local constraints...
    res = self.atom3i.ASGroot.evaluateLocalPreCondition(self.atom3i.ASGroot.SAVE)                            # evaluate global pre-conditions
    if res: return self.atom3i.constraintViolation(res)					# if violated, show warning and do not save
    res = self.atom3i.checkModel()
    if res: return self.atom3i.constraintViolation(res)					# if violated, show warning and do not save
    
    # Call the ASG method to save its contents
    self.atom3i.ASGroot.genCode( self.UNDO_BUFFER_PATH, self.atom3i.types, \
                         self.atom3i.genGraphics, 1, self.atom3i.GUIModelName, \
                         False, self.atom3i.newTypes)
                         
    # At this point it should be saved...
    if( not os.path.exists( self.UNDO_BUFFER_PATH ) ): return
      
    # Re-name it to a number so that it can be easily accessed
    number = "%04d" % ( self.__undoStackCurr ) 
    numberName = os.path.join( self.UNDO_DIRECTORY, number )
    if( os.path.exists( numberName ) ):
      os.remove( numberName )
    os.rename( self.UNDO_BUFFER_PATH, numberName )
      
      
    # Increment current undo pointer for the next undo
    self.__undoStackCurr = (self.__undoStackCurr + 1) % self.__undoStackMax
    
    # The top most undo is the current
    self.__undoStackTop = self.__undoStackCurr
    
    # The bottom most undo pointer is one ahead of the top most
    if( self.__undoStackTop == self.__undoStackBot ):
      self.__undoStackBot = (self.__undoStackBot + 1) % self.__undoStackMax
      
  def debug(self, flag = True):
    if( not flag ): return
    print "\n"
    print "Bot %d, Curr %d, Top %d, Max %d" % (self.__undoStackBot,
                                               self.__undoStackCurr,
                                               self.__undoStackTop,
                                               self.__undoStackMax ) 
      
  def __clearAndLoad( self, numberPath ):
    """ Clears the canvas contents and loads the undo at numberPath """
      
    # Clear everything off the canvas
    self.atom3i.ASGroot.removeContents(self.atom3i, 1)
    
    # Remove any temporary stuff    
    if( os.path.exists( self.UNDO_BUFFER_PATH ) ):
      os.remove( self.UNDO_BUFFER_PATH ) 
    
    # Rename the file, load it, rename back
    os.rename( numberPath, self.UNDO_BUFFER_PATH )
    self.__loadUndoFile( self.UNDO_BUFFER_PATH )
    os.rename( self.UNDO_BUFFER_PATH, numberPath )
      
    # Remove any temporary stuff      
    if( os.path.exists( self.UNDO_BUFFER_PATHC ) ):
      os.remove( self.UNDO_BUFFER_PATHC ) 
      
  def __loadUndoFile( self, filePath ):
    """ Loads the undo file """
    
    if( os.path.exists(filePath) ):   
          
      fileName = os.path.split( filePath )[1]
      className   = string.split (fileName, ".")					# compose class name
      atom3i = self.atom3i
      atom3i.newfunction = None
  
      if className[0]:
        # first check if it has been loaded before, to force a recompilation
        if className[0] in sys.modules.keys():       				# file has already been loaded
          del sys.modules[className[0]]		                        # delete to force a reload
  
        exec "from "+className[0]+" import *\n" in atom3i.__dict__, atom3i.__dict__
        if "loadedMMName" in atom3i.__dict__.keys():           	# if we have the meta-model name
          if not atom3i.ASGroot:                                 # we do not have any meta-model opened!
            return       
          elif atom3i.loadedMMName != atom3i.GUIModelName:       	# if we do not have the meta-model opened...
            return
          
        if "loadedTypes" in atom3i.__dict__.keys():		# look for newly defined or loaded types (loadedTypes should be a list)
          return
        
        # Load the copyBuffer model
        atom3i.newfunction(atom3i, atom3i.ASGroot)
