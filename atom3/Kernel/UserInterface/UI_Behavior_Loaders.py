"""
UI_Behavior_Loaders.py

Allows the user to specify customized UI behaviors

Created March 2005, by Denis Dube
"""
    
import sys,tkMessageBox, os, distutils.file_util, Dialog



def loadKeybindsOption( self,initilizationRunOnly ):
  """
  Loads the default or a custom UI behavior model 
  """ 
  keyBindsFile = self.optionsDatabase.get(self.UI_KEYBINDS)
  
  # If not init (User editing options): check if UI has changed
  if( not initilizationRunOnly ):
    if( self.oldKeyBindsFile != keyBindsFile ):
      tkMessageBox.showinfo(
            "New UI key binds set",
            "The new UI key binds will only take effect after closing and"
            +" then restarting AToM3",
            parent = self
      )
      self.oldKeyBindsFile = keyBindsFile
    return
  self.oldKeyBindsFile = keyBindsFile       

  # Keep things clean
  if( sys.modules.has_key( 'KeyBinds' ) ): 
    del sys.modules['KeyBinds']
  
  # Empty string: use default KeyBinds
  if( keyBindsFile == '' ):
    from KeyBinds       import createBindings
    self.createBindingsMethod = createBindings
    
  # Non-existing file: use default KeyBinds and give warning
  elif( not os.path.exists( keyBindsFile ) ):
    tkMessageBox.showwarning(
            "Custom UI Keybinds Not Found",
            "The custom UI Keybinds: '"+str(keyBindsFile)+
            "'\nDoes not exist. Please set Options (F1) to a new UI "+
            "keybinds file, or to '' to use the default UI without warnings." ,
            parent = self
    )
    from KeyBinds       import createBindings
    self.createBindingsMethod = createBindings
    
  # Use custom behavior statechart 
  else:        
    dir, file = os.path.split( keyBindsFile )
    fileName = file[:-3] # Remove .py
    
    # Gimmick the paths so we can import the statechart directly
    sys.path.append( os.getcwd() )
    
    # Copy the statechart file
    tmpFile = os.path.join(os.getcwd(),'Delete_Me.py')
    distutils.file_util.copy_file(keyBindsFile, tmpFile )
              
    
    # Import the temp file
    from Delete_Me import createBindings
    self.createBindingsMethod = createBindings
    
    # Cleanup temp files
    if( os.path.exists( tmpFile ) ): os.remove( tmpFile )
    if( os.path.exists( tmpFile+'c' ) ): os.remove( tmpFile+'c' )
    
    # Restore the system paths
    sys.path = sys.path[:-1] 
    

    
def loadBehaviorModelOption( self,initilizationRunOnly ):
  """
  Loads the default or a custom UI behavior model 
  """ 
  statechartFile = self.optionsDatabase.get(self.UI_BEHAVIOR_MODEL)
  
  # If not init (User editing options): check if UI has changed
  if( not initilizationRunOnly ):
    if( self.oldStatechartFile != statechartFile ):
      tkMessageBox.showinfo(
            "New UI Behavior Set",
            "The new UI behavior will only take effect after closing and"
            +" then restarting AToM3",
            parent = self
      )
      self.oldStatechartFile = statechartFile
    return
  self.oldStatechartFile = statechartFile       


  # Keep things clean
#  if( sys.modules.has_key( 'UI_StateChart' ) ): 
#    del sys.modules['UI_StateChart']
  if( sys.modules.has_key( 'UI_Statechart_MDL' ) ): 
    del sys.modules['UI_Statechart_MDL']
  
  # Empty string: use default statechart
  if( statechartFile == '' ):
    from defaultUI_Statechart.UI_Statechart_MDL_Compiled \
      import UI_Statechart_MDL
    self.UI_Statechart = UI_Statechart_MDL()
#    from UI_StateChart       import UI_StateChart
#    self.UI_Statechart = UI_StateChart()    
    
  # Non-existing file: use default statechart and give warning
  elif( not os.path.exists( statechartFile ) ):
    tkMessageBox.showwarning(
            "Custom UI Behavior Statechart Not Found",
            "The custom UI Behavior statechart: '"+str(statechartFile)+
            "'\nDoes not exist. Please set Options (F1) to a new UI "+
            "statechart, or to '' to use the default UI without warnings." ,
            parent = self
    )
    from defaultUI_Statechart.UI_Statechart_MDL_Compiled \
      import UI_Statechart_MDL
    self.UI_Statechart = UI_Statechart_MDL()
#    from UI_StateChart       import UI_StateChart
#    self.UI_Statechart = UI_StateChart()   
    
  # Use custom behavior statechart 
  else:        
    dir, file = os.path.split( statechartFile )
    fileName = file[:-3] # Remove .py
    
    # Gimmick the paths so we can import the statechart directly
    sys.path.append( os.getcwd() )
    
    # Copy the statechart file
    tmpFile = os.path.join(os.getcwd(),'Delete_Me.txt')
    tmpFile2 = os.path.join(os.getcwd(),'Delete_Me.py')
    distutils.file_util.copy_file(statechartFile, tmpFile )
    f = open( tmpFile, 'r' )
    f2 = open( tmpFile2, 'w+t' )
    # Need to know the class name... so we change it...
    for line in f:
      f2.write( string.replace( line, fileName, 'Delete_Me' ) )
    f.close()
    f2.close()          
    
    # Import the temp file
    from Delete_Me import Delete_Me as UI_Statechart_MDL
#    from Delete_Me import Delete_Me as UI_StateChart
    
    # Cleanup temp files
    if( os.path.exists( tmpFile ) ): os.remove( tmpFile )
    if( os.path.exists( tmpFile2 ) ): os.remove( tmpFile2 )
    if( os.path.exists( tmpFile2+'c' ) ): os.remove( tmpFile2 +'c' )
    
    # Start the new UI Behavior Statechart
    self.UI_Statechart = UI_Statechart_MDL()  
#    self.UI_Statechart = UI_StateChart()  
    
    # Restore the system paths
    sys.path = sys.path[:-1]   
        
        
def visualEnvironmentLoader(self):
  """ 
  Load any formalisms not already open, close ones not in the list
  WARNING: Somewhat buggy, do NOT use until fixed. In particular has difficulty
  closing formalisms.
  """
  
  loadMetaModels = []
  closeMetaModels = []

  def sanitizeMETAnames( nameList ):
    """ Minimize _META extension confusion by just removing all _META tags """
    newList = []
    for name in nameList:
      if( name[-5:] == '_META' ): 
        name = name[:-5]
      newList.append( name )
    return newList
  
  # List of meta-models we want (set in Options)
  metaModelsInOptionsList = sanitizeMETAnames( self.openFormalismsList )
  # List of meta-models that are currently active
  if( self.ASGroot ):
    metaModelsAlreadyOpenList =  self.ASGroot.getEntireASGList()
  else:
    metaModelsAlreadyOpenList = []
  
  # For each 'wantedFormalism' specified in the Options, see if we must load it
  for wantedFormalism in metaModelsInOptionsList:
    if( wantedFormalism not in metaModelsAlreadyOpenList ):
      loadMetaModels.append( wantedFormalism )
      
  # For each 'loadedFormalism', see if we must close it (to be like in Options)
  for loadedFormalism in metaModelsAlreadyOpenList:
    if( loadedFormalism not in metaModelsInOptionsList ):
      closeMetaModels.append( loadedFormalism )
  
  # If mismatch with Options, ask user if we should rectify the situation :D
  if( (loadMetaModels or closeMetaModels) and 
     Dialog.Dialog(None, {'title': 'Multi-Formalism Environment Modified',
                    'text':
                    'If the canvas is empty apply now without consequence'
                    + '\n\nOtherwise, you should wait for the next session, '
                    + 'unless you know what your doing...\n\n'
                    + 'Note: re-ordering the formalisms will happen on next '
                    + 'session regardless.',
                    'bitmap': 'warning',
                    'default': 0,
                    'strings': ('Next AToM3 Session (Recommended)','Now')
                    } ).num == 0 ): return   
                    
  
  # Now for the AToM3 legacy ugliness to close Meta-Models
  models =  self.openMetaModels.getValue()
  modelsStringList = []
  for model in models:
    modelsStringList.append( model.getValue()  )    
  modelsStringList = sanitizeMETAnames( modelsStringList )
  
  # We need to close some formalisms?
  if( closeMetaModels ):
    indexList = []
    # Find the index of the MM
    for closeMM in closeMetaModels:
      indexList.append( modelsStringList.index( closeMM ) )
    # Remove the MM from the MM list
    for index in indexList:
      self.openMetaModels.deleteItem( index )
    # Do the actual MM removal
    numMetaModels = len(modelsStringList)
    self.removeMetaModels( numMetaModels )
    self.putMetaModelName()
    
  # If we have some formalisms that need loading...
  for formalism in loadMetaModels:
    self.GUIModelName = formalism            
    # Put the message in the console
    self.console.appendText("Initializing AToM3 with GUI: "+self.GUIModelName) 	
    # If a metamodel must *really* be loaded...
    if(self.GUIModelName):								
      if( not self.ASGroot):
        # create a new ASGroot if we do not have one
        self.openMetaModel(self.GUIModelName, 0, 1)	
      else:
        # do not create a new ASGroot if we have one.
        self.openMetaModel(self.GUIModelName, 1, 0)	
    
    
  # Toolbar items may have changed
  self.parent.update()  
  self.configureToolbar() 
        
        
def visualEnvironmentLoader_OBSOLETE_KILL_ME_QUICK(self):
  # Load any formalisms not already open, close ones not in the list
  models =  self.openMetaModels.getValue()  
  numMetaModels = len( models )  
    
  # Create list of strings
  stringList = self.getOpenMetaModelsList()

  if( Dialog.Dialog(None, {'title': 'Multi-Formalism Environment Modified',
                    'text':
                    'If the canvas is empty apply now without consequence'
                    + '\n\nOtherwise, you should wait for the next session, '
                    + 'unless you know what your doing...\n\n'
                    + 'Note: re-ordering the formalisms will happen on next '
                    + 'session regardless.',
                    'bitmap': 'warning',
                    'default': 1,
                    'strings': ('Now','Next AToM3 Session')}).num == 1 ): return   
      
  # Close models that are no longer wanted in the visual environment
  index = 0
  for modelString in stringList: 
    if( modelString not in self.openFormalismsList  ):
      # Delete delete delete...
      self.openMetaModels.deleteItem( index )
      self.removeMetaModels( numMetaModels )
      self.putMetaModelName()
      numMetaModels -= 1
      index -= 1
      
    index += 1
    
  # Open models that are not yet in the visual environment
  for formalism in self.openFormalismsList:
    if( formalism in stringList ): pass
    else:
      self.GUIModelName = formalism            
      self.console.appendText("Initializing AToM3 with GUI: "+self.GUIModelName) 	# put the message in the console
      if(self.GUIModelName):								# if a metamodel must be loaded...
          if not self.ASGroot:
            self.openMetaModel(self.GUIModelName, 0, 1)	# create a new ASGroot if we do not have one
          else:
            self.openMetaModel(self.GUIModelName, 1, 0)	# do not create a new ASGroot if we have one.
    
  # Toolbar items may have changed
  self.parent.update()  
  self.configureToolbar() 
  
  