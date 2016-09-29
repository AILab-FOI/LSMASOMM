# __ File: ATOM3.py __________________________________________________________________________________________________
#                                                                              
#  Implements  : class ATOM3                                                  
#  Author      : Juan de Lara and Denis Dube                                   
#  Description : This is the ATOM3 kernel.                                    
#  Modified    : 26 Feb, 2005                                                
#  Changes :                                                                  
#   About halfway through this file, where there's a lot of dashes, the
#   code is from Juan de Lara without modification. The rest is new/modified 
#   by Denis Dube between Summer 2004 and Winter 2005
#   Note: This isn't 100% true, I've somehow managed to modify stuff everywhere...
# ____________________________________________________________________________________________________________________

PRINT_TIME_INFO = True

#if( PRINT_TIME_INFO ): print "\nStarting AToM3\n"
import time
t = time.time()

# Python code imports
import sys
import os
import tkFileDialog
import string
import Dialog
import re
import distutils.file_util
import threading
from Tkinter import *

# Path setting
try:
  from FilePaths           import getCriticalPaths
except:
  sys.exit(1)
CRITICAL_PATHS = getCriticalPaths()


if( PRINT_TIME_INFO ): 
  print "Python code imports & path setting completed in: %.3f seconds" % ( time.time() - t )
t = time.time()

from ASGNode             import *
from ASG                 import *
from ATOM3TypeDialog     import *
from ATOM3List           import *
from ATOM3TypeInfo       import *
from GGrule              import *
from GraphGrammarEdit    import *
from GraphRewritingSys   import *
from StatusBar           import *
from Console             import *
from DebugConsole        import *
from GrammarExecution    import *
#from TypeCodeGen         import *
from Buttons             import *
#from createButtons       import *

if( PRINT_TIME_INFO ): 
  print "ATOM3 core source code imported in:              %.3f seconds" % ( time.time() - t )
t = time.time()

#--------------- Summer 2004+ imports added by Denis Dube -----------------
#from UI_StateChart       import UI_StateChart
#from KeyBinds            import createBindings
from NoConsole           import NoConsole
from DrawConnections     import drawConnections as drawConnectionsBridge
from DrawConnections     import showConnection  as showConnectionBridge
from CallbackState       import CallbackState
from ArrowEditor         import ArrowEditor
from PilotArrow          import PilotArrow
from SelectionBox        import SelectionBox
from StaticMenus         import buildAllMenus, toggleMainToolMenu
from popupMenuCreator    import PopupMenuCreator
from OptionDatabase      import OptionDatabase
from OptionDialog        import OptionDialog
from Undo                import Undo
from Postscript          import Postscript
from Utilities           import selectAllVisibleObjects, optimizeConnectionPorts
from Exporter            import Exporter
from Embedded_Images     import Embedded_Images
from FilePaths           import SOURCE_CODE_PATH, META_MODEL_PATH, MODEL_PATH
from FilePaths           import OPTIONS_PATH, USER_MMODEL_PATH, USER_MODEL_PATH
from FilePaths           import USER_AREA_RECREATED, USER_PATH,USER_NAME
from FilePaths           import doTempFileCleanup, doTempCleanupALL
from FilePaths           import doTempCleanupChoice
from Cursors             import setCursor
from __init__            import BASE_PATH
from UI_Behavior_Loaders import loadKeybindsOption, loadBehaviorModelOption
from UI_Scoping          import UI_Scoping
import ForceTransfer
import SnapGrid
from Qoca.constraints.QocaSolver import QocaSolver
from Qoca.constraints.QocaSolverAbstract import QocaSolverAbstract
from Qoca.client.__init__ import QOCAPATH
from Qoca.constraints.QocaConstants import SOLVER_CASS, SOLVER_EQ, SOLVER_INEQ


if( PRINT_TIME_INFO ): 
  print "User-interface source code imported in:          %.3f seconds\n" % ( time.time() - t )


    
class ATOM3(Frame): 
  

    VERSION = 'v0.3'
    ROOT_ATOM3_INSTANCE = None 
  
    # Constants that define the operations' mode
    IDLEMODE           = "IDLEMODE"
    EXPANDModel        = "EXPANDModel"
    INSERTModel        = "INSERTModel"
    SELECTgraph        = "SELECTgraph"
    
    # Constants that define option keys
    FULLSCREEN        = 'Fullscreen'
    EXTRA_CONSOLES    = 'Extra Consoles'
    GEN_GRAPHICS      = 'Generate Graphics'
    UI_BEHAVIOR_MODEL = 'UI Behavior Model'
    UI_KEYBINDS       = 'UI Key Bindings'
    #INIT_METAMODEL    = 'Initial Meta-Model'
    OPEN_FORMALISMS   = 'Open Formalisms'
    GG_CODE_GEN       = 'Graph Grammar Code Gen.'
    CODE_GEN_DIR      = 'Code Gen. Dir.'
    STATIC_MENUBAR    = 'Menubar'
    SMOOTH_ARROWS     = 'Smooth Arrows'    
    LASTOPEN_MODEL    = 'Last open model'
    LASTOPEN_MMODEL   = 'Last open meta-model'
    LAST_INITIAL_DIRS = 'Last Initial Dirs'
    SOURCE_PATHS      = 'Model Source Paths'
    UNDO_ENABLED      = 'Enable Undo'
    UNDO_MODS_PER_SAVE= 'Modifications per undo'
    UNDO_DEPTH        = 'Undo depth'
    TOOLBAR_HEIGHT    = 'Toolbar height'
    BUTTONS_PER_ROW   = 'Buttons per row'
    QOCA_OPTIONS      = 'QOCA Options'
    
    # Main Canvas Size (minimum size) & Scrollable region
    MODEL_AREA = ( 300, 300 ) 
    CANVAS_SIZE_TUPLE = (0,0,1500,1500)  
      
    # Attributes for whom we use 'fill'
    fillAttributes    = ['line', 'text']     
    # How many recent models/meta-models to keep in memory
    FILE_HISTORY_DEPTH= 10     
    # Loaded Meta-Model String Pattern
    LOADED_MM_PATTERN =  re.compile( "\AloadedMMName *= *'(\w*)'" ) 
    # Loaded Meta-Model List Pattern
    LOADED_MM_LIST_PATTERN = re.compile( "\AloadedMMName *= *\[[\s\,\'\w]*\]" )

    def __init__(self, parent, GUIModelName=None, IsMainKernel = 0, 
                 genGraphics = 1, ASGroot = None, editGGLabels = 0):

       Frame.__init__(self, parent)						# call the Frame constructor
                     
       # Makes sure that AToM3 has the focus
       parent.focus_force() 
       
       # Let's make AToM3 a bit more accessible... - Denis
       if(ATOM3.ROOT_ATOM3_INSTANCE == None):
          ATOM3.ROOT_ATOM3_INSTANCE = self
       
       self.parent = parent            
       #self.opBar = Frame(self.parent)
       self.isOpBarPresent = 0
       #self.grphBar = Frame(self.parent)
       self.isGrphBarPresent = 0
       self.numImg = -1                                             # Number of images loaded in the buttons. Added 27/Jul/2002.
       self.buttonImage = []                                        # List with the images loaded. Added 27/Jul/2002.
       self.GGforCodeGen = "createButtons"                          # Name of the graph grammar for code generation. Added 27/Jul/2002.
       self.name2GGdict = {}

       self.editGGLabel = editGGLabels							# store if we are editing a Graph Grammar Rule
       self.ASGroot = ASGroot
       self.userActionsMap = {}								# mapping between user actions and functions
       self.types = {}									# dictionary to store the types and handling functions
       self.newTypes = []                                                               # list with the newly added types
       self.IsMainKernel = IsMainKernel							# Wether I'm the main Kernel Window or Not.
       self.option=None
       self.codeGenDir = ""
       self.coupledGG = None                                                            # info (object of type GraphGrammarExecution) with the graph-grammars to be executed on the model
       self.console = None
       self.entitiesInMetaModel = {}                                                    # dictionary with the entities defined by each meta-model.
       self.GUIModelName = None								# name of the GUI Model currently in use
       self.metaModelName = None							# name of the meta-model
       self.modes = {}                                                                  # dictionary in which the keys are the buttons, and the contents are the modes
       self.mode = self.IDLEMODE
       self.openGUI_ModelDict = dict()        # *_MM classname to *_META classname mapping
       self.showNamedPortMessage = True
              
       self.setupOptionDatabase()   
       self.assembleToolbar()  
       self.isLoadingModel = False
       self.inGGeditDialog = False
              
       if self.IsMainKernel:
          if not GUIModelName:								# no metamodel specified, see default
             #self.GUIModelName = self.optionsDatabase.get(self.INIT_METAMODEL)
             if( self.openFormalismsList ): self.GUIModelName = self.openFormalismsList[0]
             else: self.GUIModelName = None
          else:										# override the options
             self.GUIModelName = GUIModelName       
       else:
          self.GUIModelName = GUIModelName						# meta model name currently in use
     
        
       # Start AToM3 with full screen coverage
       try:
         if( self.optionsDatabase.get(self.FULLSCREEN) ):
            if( sys.platform == 'win32' ): parent.wm_state('zoomed')
            else: parent.geometry("%dx%d+0+0"%(1600,1200))
         # Start in "Debugging" mode. Covers up the console as little as possible.
         else: parent.geometry("+%d+%d"%(0,0)) 
       except:
         pass # Occurs if using AToM3 inside a Tkinter Frame instead of Toplevel window
         
       self.openMetaModels = ATOM3List([0,0,1,0], ATOM3String)                          # list with the names of the open metamodels
       self.metaModelFileNames = []							# list with the file names of the open metamodels
       self.ConnectivityMap = {}							# A dictionary to store how to connect entities.
       self.CardinalityTable= {}							# A table to store the cardinalities...

       self.buttonList = []								# A list of buttons.
      
              
       #------------------------- Canvas Panel Init --------------------------

       canvasPanel= Frame(self.parent, name = "canvaspanel")#, width=800, height=500)
       
       # Create the modelling zone, width=700, height=500,
       self.UMLmodel = Canvas(canvasPanel, name = "modelcanvas", 
                              borderwidth=5, scrollregion=self.CANVAS_SIZE_TUPLE, 
                              relief=RIDGE, bg = 'white',
                              width=self.MODEL_AREA[0],
                              height=self.MODEL_AREA[1])   
       # scrollbars for drawarea
       bottom_scrollbar = Frame(canvasPanel)
       self.UMLmodel.scrollX = Scrollbar(bottom_scrollbar, orient=HORIZONTAL)
       self.UMLmodel.scrollY = Scrollbar(canvasPanel, orient=VERTICAL)

       # link canvas, scrollbars, and events
       self.UMLmodel['xscrollcommand'] = self.UMLmodel.scrollX.set
       self.UMLmodel['yscrollcommand'] = self.UMLmodel.scrollY.set
       self.UMLmodel.scrollX['command'] = self.UMLmodel.xview
       self.UMLmodel.scrollY['command'] = self.UMLmodel.yview

       self.UMLmodel.square = Canvas(bottom_scrollbar,  width=20, height=20)

       self.UMLmodel.scrollX.pack(side=LEFT, fill = X, expand = 1)
       self.UMLmodel.square.pack(side=RIGHT)
       bottom_scrollbar.pack(side=BOTTOM, fill = X, expand = 0)
       self.UMLmodel.pack(side=LEFT, fill = BOTH, expand=1)
       self.UMLmodel.scrollY.pack(side=LEFT, fill = Y, expand = 0)
       self.statusbar = StatusBar(parent)

       
       # ------------------------------- Final Packing ---------------------------       
       
       #self.toolBarFrame.pack(side=TOP, fill=X, expand = 1)        # Make toolbar visible       
       
       self.isConstraintBarActive = False  # Afraid to remove this...
       
       canvasPanel.pack(side=TOP, fill=BOTH, expand=1)
       self.canvasPanel = canvasPanel
    
       self.statusbar.pack(side = TOP, fill = X, expand = 0)

       #------------------------ User Interface Init -------------------------

       self.exporter = Exporter( self )
       self.cb = CallbackState( self.UMLmodel, VisualObj.Tag2ObjMap, self.parent )
       self.pilotArrow = PilotArrow( self.UMLmodel )       
       self.selectionBox = SelectionBox( self.UMLmodel )
       self.postscriptBox = Postscript( self, self.UMLmodel )
       self.arrowEditor = ArrowEditor( self.UMLmodel, self.parent )
       self.undoer = Undo( self )
       self.undoer.setUndoParameters( self.optionsDatabase.get(self.UNDO_ENABLED),
                                      self.optionsDatabase.get(self.UNDO_DEPTH),
                                      self.optionsDatabase.get(self.UNDO_MODS_PER_SAVE) )
               
       # Should new arrows be drawn as smooth?
       if( self.optionsDatabase.get(self.SMOOTH_ARROWS) ):
         self.pilotArrow.toggleCreateSmooth()
         
       # Get the snapGrid rolling...
       self.snapGridInfoTuple = None
       SnapGrid.applyLayout(self)
       
       # Deploy automatic force transfer? WARNING: Uses obsolete version of FTA!
       self.isAutoForceTransferEnabled = False
       ForceTransfer.applyLayout( self, initilizeOnly = True )
  
       # Warn the user if the User area (directories, options, etc. ) has been rebuilt
       if( USER_AREA_RECREATED ):
          tkMessageBox.showinfo( 
               "User Settings Folders Created",
               "AToM3 has created " + str( USER_AREA_RECREATED ) + " new directories "+
               "to contain user settings. The root directory of these settings is: "+
               USER_PATH + "\n\nThese directories contain only option preferences and "+
               "temporary files. There should not be any need to modify these files manually.",
               parent=self)
            
       # Warn the user why graphics aren't working the way they should :D
       if( not self.genGraphics ):
        tkMessageBox.showwarning( 
               "Warning: Generate Graphics Disabled!",
               "You will not be able to open models with graphical attributes\n\n"+
               "If this is not what you wanted, please visit the options",
               parent=self)
       
       # Creates popup menus
       self.popupMenuCreator = PopupMenuCreator( self )
       
        
       # Behaviour model for the user interface          
       # Assumes the statechart is going to need a TkInstance for timed behavior
       try:
         self.UI_Statechart.initModel( TkInstance=self )
       except:
         print 'ERROR: Your probably trying to use a UI StateChart compiled' \
               +'with the regular threaded version of SCC. This will not work!'
         raise 
       self.UI_Statechart.event("Start",self)
       
       # Setup UI zones, makes it possible to use different UI charts for
       # different zones of the canvas
       self.UI_scope = UI_Scoping(self.UMLmodel, self.UI_Statechart)
       
       # Loads model paths from options into sys.paths
       self.sourcePathOptionLoad()
       
       #---------------------- OPEN INITIAL META MODEL -----------------------
       
       #print "self.GUIModelName, ASGroot = ", self.GUIModelName, ASGroot 
       #print "Opening MetaModel : ", self.GUIModelName
       
       # The initial meta-model may do stuff that requires fill type info...
       self.typeList = ATOM3List([1,1,1,0], ATOM3TypeInfo, self )
       from defaultFillTypesInfo import defaultFillTypesInformation
       defaultFillTypesInformation(self)   
       self.fillDictionaryWithTypes() 
       
      
       # Secondary AToM3 instance...
       if(GUIModelName):
          # Special situation: We want to open a model, not just a formalism!
          if(GUIModelName[-7:].upper() == '_MDL.PY'):
            self.open(GUIModelName) # GUIModelName = Full path to a model file
            
          # Opening a formalism
          else:         
            self.console.appendText("Initializing AToM3 with GUI: "+self.GUIModelName) 	# put the message in the console
            if(self.GUIModelName):								# if a metamodel must be loaded...
                if not self.ASGroot:
                  self.openMetaModel(self.GUIModelName, 0, 1)				# create a new ASGroot if we do not have one
                else:
                  self.openMetaModel(self.GUIModelName, 0, 0)				# do not create a new ASGroot if we have one.
       
       # Case when AToM3 started up for the first time
       else:       
          for formalism in self.openFormalismsList:
            self.GUIModelName = formalism
            if( ASGroot and
                formalism == ASGroot.getGUIName( ASGroot.metaModelName )[0] ):
              pass
  
            self.console.appendText("Initializing AToM3 with GUI: "+self.GUIModelName) 	# put the message in the console
            if(self.GUIModelName):								# if a metamodel must be loaded...
                if not self.ASGroot:
                  self.openMetaModel(self.GUIModelName, 0, 1)				# create a new ASGroot if we do not have one
                else:
                  self.openMetaModel(self.GUIModelName, 1, 0)				# do not create a new ASGroot if we have one.

       
       #------------------------- Final Initilization ------------------------

       # Binds & Menus
       try:
        self.parent.protocol("WM_DELETE_WINDOW", self.exitFromATOM3)
       except:
        pass # Occurs if using AToM3 inside a Tkinter Frame instead of Toplevel window
        
       if( not self.__dict__.has_key( 'mmtoolMenu' ) ):
         buildAllMenus(self)								# Creates a topLevel menu     
       
       # Parms: AToM3_instance, TK_Canvas, TK_Root_Window
       self.createBindingsMethod(self, self.UMLmodel, self.parent ) 

       
       if self.metaModelName:								# if a metamodel must be loaded...
          try:
             self.typeList = ATOM3List([1,1,1,0], ATOM3TypeInfo, self )
             self.fillTypesInformation(self)                                               # fill the types list
             self.fillDictionaryWithTypes()                                                # Convert list into a dictionary
          except AttributeError:
             print "File "+self.metaModelName+" is not a valid meta-model... Aborting"
             self.quit()
             sys.exit(1)

       self.fromClass = None								# initial class in a connection operation
       self.toClass   = None								# second class in a connection operation
       #self.globalConstraintsDict = {}							# global constraints dictionary

       self.sem_objFrom = None								# For connecting objects
       self.sem_objTo   = None                                                          # For connecting objects

       self.EditingGraphGrammar = None							# Graph Grammar being edited currently
       self.theKeyword = None
       self.inter_connect_points = []							# list of intermediate connecting points

       # Not sure what this is doing! - Denis
       if( self.ASGroot and not IsMainKernel ):
          # open the necessary metamodels (look over the merged ASGs)!
          mergeds = []+self.ASGroot.mergedASG
          for asg_merged in mergeds:
             print "Opening metamodel::", asg_merged.metaModelName
             #name = ASGroot.getGUIName( asg_merged.metaModelName )[0]
             #if( name not in self.openFormalismsList ):
             # print name, self.openFormalismsList 
             self.openMetaModel(asg_merged.metaModelName, 0, 0)
          self.ASGroot.writeContents(self, genGraphics) # draw contents of ASGroot if any

       # Don't ask politely, just grab the bloody focus :D
       # NOTE: this is *needed* because a tkMessageBox can steal the focus
       # on startup, thus killing all the keybindings! Ewwww.
       self.parent.focus_force()
       
       self.systemRestorePoint = ( sys.modules.copy() , sys.path[:] )
       #print sys.path, "<--- System restore point\n\n"
       

       
    def debug(self, console=True ):
      # Handy way to find how you get to some piece of code...
      from traceback import print_stack
      if( console ): print print_stack()
      return str( print_stack() )
      
      """
      # Here's how to get the name of the file your in (and just that)
      from traceback import format_stack
      stack = format_stack(limit=1)
      if( stack ): 
        text = stack[0].split('\n')[0]
        if( text[:7] == '  File ' ): text = text[7:]
      """
      
      
    def getCanvas( self ):
      return self.UMLmodel

    def assembleToolbar(self):
      """ 
      This method creates a self.toolBar Frame that is inside a XY-scrollable
      canvas area. The frame can be used just like a regular frame :D 
      """
      self.toolBarFrame = Frame(self.parent)	
      self.toolBarBottomFrame = Frame(self.toolBarFrame)	
      
      self.toolBarCanvas = Canvas(master=self.toolBarFrame,
                            takefocus=1,
                            height= self.optionsDatabase.get(self.TOOLBAR_HEIGHT),                         
                            scrollregion= (0,0,0,0) )
                             
      self.toolBarCanvas.scrollX = Scrollbar(self.toolBarBottomFrame, takefocus=0, orient=HORIZONTAL)                  
      self.toolBarCanvas.square = Canvas(self.toolBarBottomFrame, width=16, height=16)
      
      self.toolBarCanvas.scrollY = Scrollbar(self.toolBarFrame, takefocus=0, orient=VERTICAL)
       
      # Configure the scrollies
      self.toolBarCanvas.scrollX.config(command=self.toolBarCanvas.xview )
      self.toolBarCanvas.config( xscrollcommand=self.toolBarCanvas.scrollX.set) 
      self.toolBarCanvas.scrollY.config(command=self.toolBarCanvas.yview )
      self.toolBarCanvas.config( yscrollcommand=self.toolBarCanvas.scrollY.set)  
      
      
      # This is the beautiful part: the Frame is tucked into the canvas
      self.toolBar = Frame(self.toolBarCanvas)	
      self.toolBarCanvasHandler = self.toolBarCanvas.create_window(0,0, 
                                              window=self.toolBar, anchor=NW )
           
      
      # This image is displayed in the TOP-Left of AToM3 at all times, also triggers old menu system      
      self.mainLogoPhotoimage = Embedded_Images().getMainLogo()
#      self.atom3MenuButton = Button(self.toolBarFrame, 
#           image=self.mainLogoPhotoimage, bg="white", fg="white", 
#           command=lambda s=self,e=None: s.UI_Statechart.event("Options",e))
      def handler():
        if(self.optionsDatabase.showOptionsDatabase()):
          self.loadImmediateOptions()
      self.atom3MenuButton = Button(self.toolBarFrame, 
                       image=self.mainLogoPhotoimage, bg="white", fg="white", 
                       command=handler)

      #command=lambda s=self: toggleMainToolMenu(s) )
      self.atom3MenuButton.pack( side=LEFT,fill=Y ) 
             
            
      def handler( event, button = self.atom3MenuButton ):
          button.configure( bg='DarkOrchid4', activebackground='SpringGreen',
                          borderwidth=2, relief='groove' )
      self.atom3MenuButton.bind( '<Enter>', handler)
      def handler( event, button = self.atom3MenuButton ):
          button.configure( bg='white', activebackground='white',
                          borderwidth=2, relief='raised' )
      self.atom3MenuButton.bind( '<Leave>', handler)
                 
                                              
      self.toolBarFrame.pack( side=TOP, fill=X, expand=0)                                        
      self.toolBarCanvas.scrollX.pack(side = LEFT, fill=X, expand=1)  
      self.toolBarCanvas.square.pack(side = RIGHT, fill=X, expand=0) 
      #self.toolBarBottomFrame.pack(side = BOTTOM,fill=BOTH, expand=1)
      
      #self.toolBarCanvas.pack(side = LEFT,fill=BOTH, expand=1)   
      #self.toolBarCanvas.scrollY.pack(side = LEFT,fill=Y, expand=0)  
      
      self.configureToolbar()
      
    def configureToolbar( self, event=None ):
      """ 
      Packs the toolbar. Scrollbars are packed only if needed. Scroll region
      is set to just big enough to see everything.
      """
      
      # This is the width, height that the toolbar is using 'virtually'
      vx = self.toolBar.winfo_width()
      vy = self.toolBar.winfo_height()
      
      # This is the width,height that the toolbar is actually getting on screen
      ax = self.toolBarCanvas.winfo_width()     
      ay = self.toolBarFrame.winfo_height()
      
      xScroll = False
      yScroll = False
      useScrollbarY = bool( self.optionsDatabase.get(self.TOOLBAR_HEIGHT) )
      
      if( useScrollbarY and vy > ay + 10 ): yScroll = True
      if( vx > ax + 10 ):                   xScroll = True
        
      # Configure the scrollable region
      self.toolBarCanvas.configure( scrollregion = (0,0,vx,vy ) )
      if( useScrollbarY ):
        self.toolBarCanvas.configure( height=self.optionsDatabase.get(self.TOOLBAR_HEIGHT) )
      else:
        self.toolBarCanvas.configure( height=vy )
                        
      # What was previously packed... shall be forgotten!
      self.toolBarCanvas.pack_forget()
      self.toolBarBottomFrame.pack_forget()
      self.toolBarCanvas.scrollY.pack_forget()
      
      # Pack it all anew
      if( xScroll ): self.toolBarBottomFrame.pack(side = BOTTOM,fill=X, expand=1)
      self.toolBarCanvas.pack(side = LEFT,fill=X, expand=1)  
      if( yScroll ): self.toolBarCanvas.scrollY.pack(side = LEFT,fill=Y, expand=0)  
        
          
    def disableSnapGridForPrinting( self, flag=False):
      """ Turns the SnapGrid on/off for printing/postscript """
      SnapGrid.applyLayout( self, disableForPrinting = flag )  
      
    def toggleSnapGrid(self):
      """ Quick way of toggling the Snap Grid on off """
      if( self.snapGridInfoTuple ):   
        SnapGrid.applyLayout(self,disableForPrinting=True) 
        self.snapGridInfoTuple = None
      else:
        SnapGrid.applyLayout(self) 
        self.parent.update_idletasks()

    def setupOptionDatabase( self ):
      """ 
      Options Dictionary, save/load/dialog configuration 
      Default values are used if the database cannot be loaded
      The database is saved/overwritten whenever the user presses "Ok"
      """
      
      # Instantiate the Option Database module
      self.optionsDatabase = OptionDatabase(self.parent,'Options_AToM3.py', 'AToM3 Options Configuration')
      
      # Local methods/variables with short names to make things more readable :D
      newOp = self.optionsDatabase.createNewOption
      BE = OptionDialog.BOOLEAN_ENTRY
      FE = OptionDialog.FILE_ENTRY
      NE = OptionDialog.NO_ENTRY
      IE = OptionDialog.INT_ENTRY
      LFE = OptionDialog.LIST_FILE_ENTRY
      SEP = OptionDialog.SEPERATOR
      SE = OptionDialog.STRING_ENTRY
      
      # Create New Options
      # Format: OptionKey, defaultValue, valueType, promptString, helpString
      # valueType = [ fileTypeCode, buttonLabel, fileType ]
      # valueType = [ colorTypeCode, buttonLabel ]
      # valueType = [ TypeCode ]
      
      userAreaPath = os.path.split( USER_MODEL_PATH )[0]
      
      
      newOp( self.STATIC_MENUBAR, False, BE ,"Enable top menubar", """
A static toolbar on the top of the window like many applications have.

This is legacy code from the 0.2 AToM3 version series.
It lacks many of the items present in the dynamically created popup-menus!

WARNING: Not recommended simply because it's missing so much... if you are
interested in upgrading it, please see StaticMenus.py, popupMenuElements.py,
and popupMenuCreator.py files in atom3/kernel/UserInterface/
""" )
         
      newOp( self.EXTRA_CONSOLES, False, BE, "Enable debugging consoles", """
These consoles can allow you to query the state of variables & run methods at 
run-time.

These consoles are legacies of the 0.2 AToM3 version series. 

WARNING: They are a bit buggy...
""")
      
      newOp( self.FULLSCREEN, False, BE, "Start AToM3 in fullscreen", """
This option is equivelent to starting AToM3 in Windowed mode and then maximizing
the window to occupy the entire screen. 

WARNING: May not work on all platforms. Works on Windows though! :) """ )
                         
      newOp( self.GEN_GRAPHICS, True, BE ,"Generate graphics",
          "If disabled, AToM3 will not be able to open models containing graphics" )
      
      newOp( self.SMOOTH_ARROWS, True, BE ,"Smooth arrows by default",
                              "If enabled, new arrows will be drawn smooth." ) 
      
      newOp('line1','',SEP,'','' )
      
      newOp( self.UI_BEHAVIOR_MODEL,
            '',
            [ FE, "Choose UI Model",[("Python File", "*.py")], 
             OptionDialog.FILEPATH, userAreaPath ],
            "UI Behavior Model",
            "Choose the statechart GUI behavior model you wish to use with AToM3\n\n"
            +"Hint: the current model is located in:\n"
            +"atom3/Kernel/UserInterface/defaultUI_Statechart/UI_Statechart_MDL.py\n"
            +"\nSo you can simple load this up, then save it in the UserArea and"
            +" modify it there.\n"
            +"When done, Generate DES, and choose Compile with the Tkinter option\n"
            +"Now you just need to point this here option to the compiled statechart"
            +"\n\nNOTE: The class name of your statechart must be 'UI_Statechart_MDL'")
            
      newOp( self.UI_KEYBINDS,
            '',
            [ FE, "Choose UI Keybinds",[("Python File", "*.py")], 
             OptionDialog.FILEPATH, userAreaPath ],
            "UI Keybindings",
            "This allows you to choose a customized keybinding file for use"
            +" with AToM3.\n"
            +"ie. You can copy the KeyBinds.py file in the Kerenl.UserInterface"
            +"\ndirectory to the user area, modify it, then tell AToM3 to load"
            +"\nit here, instead of the default one." ) 
            
      # The Formalisms to have open...
      newOp( self.OPEN_FORMALISMS, [], 
            [LFE, "Choose File",[("Meta-Model","*_META.py"),
                                 ("Python File", "*.py")], 
             OptionDialog.FILENAME_ONLY, META_MODEL_PATH  ], 
             'Multi-Formalism Environment', """
Set which formalisms/meta-models you want AToM3 to START with by default. 
All new formalisms can be found by the *_META.py extension, for old formalisms
you'll need to hunt and peck until you find the correct *.py file. 

NOTE: This is overriden if you start atom3.py with arguments...
Example 1: 
atom3.py CD_ClassDiagramsV3 
This opens the formalism CD_ClassDiagramsV3_META.py

Example 2: 
atom3.py D:\atom3\Kernel\UserInterface\defaultUI_Statechart\UI_Statechart_MDL.py
This opens all the formalisms needed for the model file. The model file must
have the _MDL.py extension or it will not be recognized. Spaces are allowed in
the path (the script atom3.py can put it together again), but make sure the path
is absolute, that is that it starts with a drive letter (for Windows users). 
""") 
      

#       newOp( self.GG_CODE_GEN, '',
#             [ FE, "Choose Grammar", [("Grammar File", "*_GG_exec.py"),
#                                      ("Python File", "*.py")],
#              OptionDialog.FILENAME_ONLY, userAreaPath ], 
#             "Button Grammar (Obsolete)", """
# When generating formalisms from meta-models, a grammar will automatically 
# generate a button for each entity.
# 
# UPDATE: In the Feb, 2006 version of AToM3 0.3 button generation grammars were
# removed from AToM3.
# """)
            
      
      # Yeah, like we really need this:
#       newOp( self.CODE_GEN_DIR, '',
#             [ FE, "Choose Directory",[("Choose any file in directory", "*")],
#              OptionDialog.RELATIVE_DIRNAME, userAreaPath ],
#             "Directory for Code Generation",
#             "Must be in the SourceCode or MetaModel subdirectories of AToM3\n\n"+
#             "Note: Denis is trying to phase this thing out and use the path of the current open ER model instead." )
      
      
      newOp( self.LASTOPEN_MODEL, [], NE, '' ) # List of open models
      newOp( self.LASTOPEN_MMODEL, [], NE, '' ) # List of open meta-models
      newOp( self.LAST_INITIAL_DIRS, [], NE, '' ) # Initial directories
      newOp( self.SOURCE_PATHS, [], NE, '' ) # Paths to source code...
      
      

      newOp('line2','',SEP,'','' )

      newOp( self.UNDO_ENABLED, False, BE, "Enable Undo (Not recommended)", """
WARNING: Undo is not supported anymore. Undo CAN create unhandled exceptions!
Enabled (and working), it simply saves and loads the model (which is slow).
Part of the problem is that it does not save the model after each change.

Why no working undo? Because it was not built-in to AToM3 originally!
Adding it in afterwards is like putting a broken egg back together :p""")
      newOp( self.UNDO_MODS_PER_SAVE, 0, IE, "Modifications per undo", "Saves the model every X modfications to provide undo ability" )
      newOp( self.UNDO_DEPTH, 20, IE, "Maximum undo depth", "When maximum undo depth reached, old undo files are overwritten" )

      newOp( self.TOOLBAR_HEIGHT, 0, IE, "Toolbar height", 
            "How many pixels high the toolbar will be\n\n"+
            "If the value \"0\" is set, the toolbar will always be just high enough\n"+
            "Otherwise, if the height is set too low, scrolling in Y will be necessary" )
      newOp( self.BUTTONS_PER_ROW, 12, IE, "Buttons per row", 
            "Maximum buttons a meta-model can display on a single row\n"+
            "Additional rows will be added to fit extra buttons\n\n"+
            "If the value \"0\" is set, the per meta-model defaults will be used\n\n"+
            "This option only takes effect when openning new meta-models" )
    
      newOp('line3','',SEP,'','' )
      
      labelOpts = [OptionDialog.LABEL,"Times 12","red", "left" ]
      connOpts = [OptionDialog.ENUM_ENTRY, "Pipe", "TCP/IP"]
      solverOpts = [OptionDialog.ENUM_ENTRY, "Cassowary", "Equality", "Inequality" ]
      optionList = [OptionDialog.SINGLE_LIST_ENTRY,
                      'Enable QOCA constraint solver', True, BE, 
                      'If disabled, layout will not function correctly for some formalisms',  
                                       
                      'Enable QOCA auto-solve', True, BE, 
                      'Certain events trigger a re-solve automatically',
                                          
                      'QOCA solver type', "Cassowary", solverOpts,
                      'The various solver types use different metrics...',
                      
                      'QOCA connection type', "Pipe", connOpts,
                      'Pipe connection automatically starts a the QOCA java jar'
                      +' file\nTCP/IP requires manually starting the QOCA java'
                      +' jar server',
                      
                      'QOCA server IP', '127.0.0.1', SE, 
                      'IP address string if using TCP/IP connection mode',
                      
                      'QOCA server port', 14059, IE, 
                      'Port address integer if using TCP/IP connection mode',
                      
                      '\nNote 1: Changes will take effect on AToM3 restart only'
                      +'\nNote 2: Pipe option assumes Java is in environment'
                      +' path', None,labelOpts,'',                       
                      ]
      newOp( self.QOCA_OPTIONS, [[False, True, "Cassowary", "Pipe", 
                                  '127.0.0.1', 14059, None]], 
            optionList, 'QOCA options', 
            'QOCA is an incremental constraint solver used for graphic layout')
              
         
    
      # Load the options from the file, on failure the defualts will be returned.
      self.optionsDatabase.loadOptionsDatabase()
      self.loadImmediateOptions( initilizationRunOnly = True )
      
      
    def loadImmediateOptions(self, initilizationRunOnly = False ):
      """ Instead of waiting for AToM3 restart, applies option changes immediately """
      
      def relativeToAbsolutePath( pathDir ):
        """ Converts a relative path to an absolute path in the ATOM3 context """        
        # Is it already absolute?
        if( os.path.exists( pathDir ) ):
          return pathDir 
        # Try in the User/Formalisms path
        p = os.path.join( USER_MMODEL_PATH, pathDir )
        if( os.path.exists( p ) ):
          return p 
        # Try in the Formalisms path
        p = os.path.join( META_MODEL_PATH, pathDir )
        if( os.path.exists( p ) ):
          return p  
        # Try in the source code path (kernel)
        p = os.path.join( SOURCE_CODE_PATH, pathDir )
        if( os.path.exists( p ) ):
          return p  
        return ''   
      
      self.genGraphics  = self.optionsDatabase.get(self.GEN_GRAPHICS)
      self.GGforCodeGen = '' # self.optionsDatabase.get(self.GG_CODE_GEN)
      self.codeGenDir   = USER_MMODEL_PATH #self.optionsDatabase.get(self.CODE_GEN_DIR)
      #self.codeGenDir   = relativeToAbsolutePath( self.codeGenDir )
      
      # openFormalismsList is a misleading name, what it really is: 
      # A list of Formalisms in the Options to be openned when AToM3 starts
      self.openFormalismsList = self.optionsDatabase.get(self.OPEN_FORMALISMS)       
      
      
      # Show Debugging Consoles?
      if( self.optionsDatabase.get(self.EXTRA_CONSOLES) ):
        if( initilizationRunOnly ):
          self.console      = Console(self)			
          self.debugConsole = DebugConsole(self)
        else:
          self.showConsole()
      else:
          if( not initilizationRunOnly ):
            self.console.destroy()
            self.debugConsole.destroy()          
          self.console      = NoConsole(self)
          self.debugConsole = NoConsole(self)
                                  
      # Setup Initial Directories (for convenience)
      self.initialDirectoryDict = self.optionsDatabase.get(self.LAST_INITIAL_DIRS)
      if( not self.initialDirectoryDict ):
        self.initialDirectoryDict = dict()  
        self.initialDirectoryDict[ 'OpenSaveModel' ] = MODEL_PATH    
        self.initialDirectoryDict[ 'OpenMetaModel' ] = META_MODEL_PATH   
        self.initialDirectoryDict[ 'OpenSaveTrans' ] = ""   
        self.initialDirectoryDict[ 'Documentation' ] = os.path.split( USER_MMODEL_PATH )[0]
      
      # Load UI Behavior Statechart, and Keybinds
      # Generates: self.UI_Statechart and self.createBindingsMethod
      loadBehaviorModelOption(self, initilizationRunOnly) 
      loadKeybindsOption(self, initilizationRunOnly) 
      
      #todo: qoca
      if(initilizationRunOnly):
        qocaOptList = self.optionsDatabase.get(self.QOCA_OPTIONS)[0]
             
        # If QOCA is enabled
        if(qocaOptList[0]):   
          # If automatic re-solve is enabled 
          self.qocaAutosolve = qocaOptList[1]
                 
          solverTypeMap = {"Cassowary":SOLVER_CASS, "Equality":SOLVER_EQ,
                           "Inequality":SOLVER_INEQ}
          solverType = solverTypeMap[qocaOptList[2]]
          usePipe = (qocaOptList[3] == "Pipe")      
          command='java -jar "' + QOCAPATH + '"'   # Java in environment path!
          ip =  qocaOptList[4]
          port =  qocaOptList[5]
          self.qocaSolver = QocaSolver(usePipe, command, ip, port, solverType)   
                            
        # QOCA disabled... implementation free interface presented
        else:
          self.qocaAutosolve = False
          self.qocaSolver = QocaSolverAbstract()
  
      try:
        self.qocaSolver.connect()
      except:
        tkMessageBox.showinfo(  "Could not start QOCA solver",
                              "See console for more details...",parent = self)  
      
      # If AToM3 is just starting,  QUIT
      if( initilizationRunOnly ):  return   
         
      self.undoer.setUndoParameters( self.optionsDatabase.get(self.UNDO_ENABLED),
                                     self.optionsDatabase.get(self.UNDO_DEPTH),
                                     self.optionsDatabase.get(self.UNDO_MODS_PER_SAVE) )
       
      # Show the top menu bar?
      toggleMainToolMenu( self,
                    setState=self.optionsDatabase.get( self.STATIC_MENUBAR ) )

      # Update the toolbar height
      self.configureToolbar()
      
      
           
    def historyManager( self, historyKey, newFilename ):
      """ Adds the new filename to the options database at historyKey """
      
      historyFiles = self.optionsDatabase.get( historyKey )
      
      # Optimize the file history by removing models that no longer exist
      optimizedList = []
      for historyFile in historyFiles:
        if( os.path.exists( historyFile ) ): optimizedList.append( historyFile )
             
      # File is already there! Remove it (we want most recent on top)
      if( newFilename in optimizedList ):
        optimizedList.remove( newFilename )
        
      # Add the new file to list
      optimizedList = [newFilename] + optimizedList
      
      # Cap the history depth
      if( len( optimizedList ) > self.FILE_HISTORY_DEPTH ): 
        optimizedList = optimizedList[:-1]
      
      # Set & save :D
      self.optionsDatabase.set(historyKey, optimizedList)
      self.optionsDatabase.saveOptionsDatabase()

   
    """ 
    Bridge to the connection drawing module 
    Otherwise older models would become incompatible :-(
    Note: I had to relabel them with a "Bridge" in their names, because of name
    clashes.
    """
    def drawConnections(self, * listOfConnections ):      
      drawConnectionsBridge(self, * listOfConnections )      
    def showConnection( self, *args ):
      return showConnectionBridge( self, *args )
    
    
      
    
    def sourcePathOptionSave(self, showDialog = True ):
      """ Saves the model paths to the option database """

      # Gets paths that are in one of the two Formalisms directories
      paths = []
      for pathName in sys.path:  
        pathName = os.path.normpath( pathName )
        if( os.path.commonprefix( [META_MODEL_PATH, pathName] ) == META_MODEL_PATH ):            
          paths.append( pathName )
        elif(os.path.commonprefix( [USER_MMODEL_PATH, pathName] ) == USER_MMODEL_PATH ):            
          paths.append( pathName )
                       
      # No point saving if nothing has changed
      if( paths == self.optionsDatabase.get(self.SOURCE_PATHS) ):
        return
          
      if( showDialog ):
        myText = ''
        myText += 'Save source paths\n'
        myText += 'If not saved, path modifications will be lost when AToM3 is restarted'
        dialog = Dialog.Dialog(None, {'title': "Source Paths",
                    'text': myText,
                    'bitmap': '',
                    'default': 1,
                    'strings': ('Save','Don\'t Save')})
        if( dialog.num == 1 ): return
          
      self.optionsDatabase.set(self.SOURCE_PATHS, paths)
      self.optionsDatabase.saveOptionsDatabase()
      
    def sourcePathOptionLoad(self):
      """ Loads the model paths from the option database """
      
      paths = self.optionsDatabase.get(self.SOURCE_PATHS)
      for path in paths:
        path = os.path.normpath( path )
        if( path not in sys.path ):
          sys.path.append( path )

    def sourcePathManager(self, actionCode=0 ):
      
      # Add new source path
      if( actionCode == 0 ):
        
        try:          
          dir = tkFileDialog.askdirectory(
                    title="Add source path",
                    initialdir=USER_MMODEL_PATH )	
        except:
          dir = tkFileDialog.askopenfilename(
                      title="Add source path",
                      filetypes=[("Choose any file in model directory", "*")],
                      initialdir=USER_MMODEL_PATH )        
          if( dir ):  
            dir = os.path.split( dir )[0] 
    
        
        if( dir == '' ): return # Cancel
        self.checkInSearchPath( dir )
        
        # Did the added path create conflicts? If so, should we save it anyway? Probably...
        if( self.sourcePathConflictAwareness() ):
          return self.sourcePathOptionSave()
        
        # Add more paths...
        myText = 'If not saved, they will be lost on AToM3 exit'
        dialog = Dialog.Dialog(None, {'title': "Adding Source Paths",
                    'text': myText,
                    'bitmap': '',
                    'default': 1,
                    'strings': ('Save & Close','Close', 'Add more paths')})
        
        # Quit & save new paths
        if( dialog.num == 0 ): 
            return self.sourcePathOptionSave( showDialog = False )
          
        # Quit & dont' save
        if( dialog.num == 1 ): 
            return
          
        # Keep adding paths
        if( dialog.num == 2 ): 
            return self.sourcePathManager(0)
                      
      # Remove source path
      elif( actionCode == 1 ):
        
        # Make a list of all the loaded meta-model paths
        paths = []
        indexMap = dict()
        i = 0
        j = 1
        normModelPath = os.path.normpath( META_MODEL_PATH )
        normUserModelPath = os.path.normpath( USER_MMODEL_PATH )
        for loadedPath in sys.path:          
          normLoadedPath = os.path.normpath( loadedPath )

          # The loaded path and the model path have the model path in common
          # Therefore this is a model path that can be safely removed 
          if( os.path.commonprefix( [  normLoadedPath,normModelPath ] ) == normModelPath  ):
            paths.append( normLoadedPath )
            indexMap[j] = i    
            j += 1     
          elif( os.path.commonprefix( [  normLoadedPath,normUserModelPath ] ) == normModelPath ):
            paths.append( normLoadedPath )
            indexMap[j] = i    
            j += 1   
          i += 1
            
        # Let the user chose the index of the path to remove
        title = 'Path Removal Menu'
        actionLabel = 'Remove'
        index = self.popupMenuCreator.listChoicePopup(title, paths,actionLabel )  
        
        # Quit the menu
        if( index == 0 ): return self.sourcePathOptionSave()   
        
        # Delete the path at index         
        del sys.path[ indexMap[index] ]
        
        # Delete more menu items...
        return self.sourcePathManager(1)
        
      # Source path conflict finder
      elif( actionCode == 2 ):
        if( not self.sourcePathConflictAwareness() ):
          tkMessageBox.showinfo(  "Source Path Conflicts","None found.",parent = self)    
          
          
    
      # Help
      else:
        tkMessageBox.showinfo(
              "Source Path Help",
              "Some AToM3 models require the source path to other models\n"+
              "Unfortunately, they simply assume that the source path is available to them\n"+
              "Since there is no simple way to automatically add these paths, it is up to the user to do this.\n"+
              "\nWARNING: When loading extra source paths, you may end up with duplicate source files!\n"+
              "If this happens you will be explicitly warned and shown which files are duplicated.\n"
              ,parent = self)
              
    def sourcePathConflictAwareness(self, showDialog=True, printToConsole=True ):
      """ 
      Finds potential problems arising from multiple files with same name in 
      directories that have been simultaneously loaded.
      """          
 
      # Get the AToM3 base path, and the paths of all its loaded subdirectories      
      atom3Pattern = re.compile( '.*' + os.path.split( BASE_PATH )[1] )
      sourcePaths = []
      for pathname in sys.path:
        if( atom3Pattern.search( pathname ) ):  
          sourcePaths.append( os.path.normpath( pathname ) )
   
      # Find all duplicated files 
      sourceFileDict = dict()
      ingoreFilenameList = ['__init__.py', 'ByteCodeCleaner.py']
      duplicateSourceFileList = []
      for dir in sourcePaths:
        if( not os.path.exists(dir) ): continue
        for fileName in os.listdir(dir):
          pathName = os.path.join(dir,fileName)
         
          # Ignore directories
          if( os.path.isdir(pathName) ): continue
            
          # Ignore __init__.py files
          elif( fileName in ingoreFilenameList ): continue
                        
          # File without a duplicate
          elif( not sourceFileDict.has_key( fileName) ):
            sourceFileDict[ fileName ] = pathName
                        
          # Source file with a duplicate            
          else:
            splitName = string.split( str(fileName), '.' )        
            if( splitName and len(splitName) > 1 and splitName[1] == 'py' ):
              duplicateSourceFileList.append( (sourceFileDict[ fileName ],pathName) )
                
      
      # Show warning if duplicates occured
      if( duplicateSourceFileList ):
        
        from filecmp import cmp

        safeDuplicationString = ""
        dangerousDuplicationString = ""
        for file1,file2 in duplicateSourceFileList: 
          # Do the files have identical implementations?
          if( cmp( file1, file2 ) ):
            safeDuplicationString += "i) " + str(file1) + "\n" + "ii) " + str(file2) + "\n\n"
            #safeDuplicationString += "Identical source pair (safe):\n" + \
            #              str(file1) + "\n" + str(file2) + "\n\n"
          else:
            dangerousDuplicationString += "i) " + str(file1) + "\n" + "ii) " + str(file2) + "\n\n"
            #dangerousDuplicationString += "Different implementation source pair (dangerous):\n" + \
            #              str(file1) + "\n" + str(file2) + "\n\n"
          
        if( safeDuplicationString ):
          if( showDialog ):
            if( len( safeDuplicationString ) < 300 ):
              tkMessageBox.showwarning(  "Safe Source Path Conflicts",safeDuplicationString,parent = self)
            else:
              tkMessageBox.showwarning(  "Safe Source Path Conflicts",
                  safeDuplicationString[:300] + '\n\nSee console for more...\n',parent = self)  
          if( printToConsole ):
            print "***********************************************************\n"
            print "Safe Source Path Conflict Detected (Source files with ",
            print "same implementation pairs and AToM3 cannot know which ",
            print "to use)\n\n", safeDuplicationString  
            print "***********************************************************\n"
            
        if( dangerousDuplicationString ):
          if( showDialog ):
            if( len( dangerousDuplicationString ) < 300 ):
              tkMessageBox.showwarning(  "Dangerous Source Path Conflicts",dangerousDuplicationString,parent = self)
            else:
              tkMessageBox.showwarning(  "Dangerous Source Path Conflicts",
                  dangerousDuplicationString[:300] + '\n\nSee console for more...\n',parent = self)  
          if( printToConsole ):
            print "***********************************************************\n"
            print "Dangerous Source Path Conflict Detected (Source files with ",
            print "different implementation pairs and AToM3 cannot know which ",
            print "to use)\n\n", dangerousDuplicationString
            print "***********************************************************\n"

        
        return True
    
      else:
        return False
            
      
      
    def addDirectoryWithModelName(self, modelName, noWarning = False ):
      """ 
      Given just a model name, finds the model directory & adds it to path
      Returns True on success, False on failure.
      Created June 24,2004 by Denis Dube
      """
      #noWarning = False
      
      def findModelInPath( modelName, basePath ):                        
        # Find all the model paths that potentially contain the model 
        modelDirList = []
        for dirName in os.listdir(basePath):
          if( os.path.isdir( os.path.join( basePath,dirName) ) ):
            modelDirList.append(dirName)
             
        # Searches through all the potential model paths, adds model if found
        for modelDirName in modelDirList:  
          for fileName in os.listdir(os.path.join(basePath,modelDirName)):
            if( modelName == fileName ):
              modelSysPath = os.path.join(basePath,modelDirName)
              self.checkInSearchPath( modelSysPath )   
              return True
        return False
                  
      # Model could be in the meta model directory or source code directory
      if( findModelInPath(modelName+'.py',USER_MMODEL_PATH ) ): return True
      if( findModelInPath(modelName+'.py',META_MODEL_PATH  ) ): return True      
      if( findModelInPath(modelName+'.py',SOURCE_CODE_PATH ) ): return True
              
      # What if it's not found?
      # That means its not in an immediate subfolder of AToM3. 
      # In that case I should probably give an error message...
      if( not noWarning ):
        if(len(modelName) > 10 and modelName[-10:] == '_META_META'):
          modelName = modelName[:-5]
        title = "ERROR in addDirectoryWithModelName() of: " + __file__
        msg = "The formalism "+modelName+" could be found in neither of:\n\n" + \
              META_MODEL_PATH + "\n\n" +SOURCE_CODE_PATH+"\n\n"+USER_MMODEL_PATH \
              + '\n\n'
        msg += '\nExamples (for the X formalism):\n'
        msg += '    Valid: ~\User Formalisms\X\X_META.py\n'
        msg += '    Valid: ~\User Formalisms\Foobar\X_META.py\n'
        msg += '    Invalid: ~\User Formalisms\X_META.py\n'
        msg += '    Invalid: ~\User Formalisms\X\X\X_META.py\n'
        msg += '    Invalid: C:\X_META.py'
        print title
        print msg
        tkMessageBox.showerror(title, msg, parent=self)
        #self.debug()
        #raise Exception
      return False
          
    def configureUserActions(self):
       """
          Fills the common actions for all formalisms...
       """
       def doNaught(*args): pass
       self.userActionsMap[self.IDLEMODE] = doNaught  
       self.userActionsMap[self.INSERTModel] = self.createNew_Model
       self.userActionsMap[self.EXPANDModel] = self.expandModel       
       self.userActionsMap[self.SELECTgraph] = self.selectGraph
             


    def closeMetaModel(self):
      """
      Presents a window that shows the open metamodels, 
      allow to check some of them to be deleted
      """

      # The old way of doing things...
      if( 0 ):
        numMetaModels = len(self.openMetaModels.getValue())
        cm = ATOM3TypeDialog(self, self.openMetaModels)          # Select the meta-model to delete
        if cm.result_ok:                                         # The user pressed Ok
          self.removeMetaModels(numMetaModels)
          self.putMetaModelName()
      
      # The popup way...
      else:
        models =  self.openMetaModels.getValue()
        numMetaModels = len( models )
        
        # Create list of strings for the popup, add a cancel option...
        stringList = []        
        for model in models:
          stringList.append( model.getValue()  )
          
        # Popup/Dialog config
        title = 'Meta-Model Menu'
        actionLabel = 'Remove'
        
        # Subtract 1 from index, since added a Cancel button
        index = self.popupMenuCreator.listChoicePopup( title,stringList,actionLabel ) - 1
        if( index < 0 or index > numMetaModels  ): return
        
        # Delete delete delete...
        self.openMetaModels.deleteItem( index )
        self.removeMetaModels( numMetaModels )
        self.putMetaModelName()
        
      # Toolbar items may have changed
      self.parent.update()  
      self.configureToolbar()  
                
        
    def putMetaModelName(self):
       """ Updates the name of the current meta model and presents it in the Windows title bar """
       
       mmodels = self.openMetaModels.getValue()
       name = ""
       if len(mmodels) > 0:
          counter = 0
          for mm in mmodels:
            if counter == 0:
               name = name + mm.toString()
            else:
               name = name + " + " + mm.toString()
            counter = counter + 1
       try:
         if name == "":
           self.parent.title("AToM3 " + self.VERSION)
         else:
           self.parent.title("AToM3 "+ self.VERSION + " using: "+name)
       except:
         pass # Occurs if using AToM3 inside a Tkinter Frame instead of Toplevel window

    def removeMetaModels(self, numMetaModels):
       """
          Closes one or more of the loaded metamodels (leaves only the present in
          self.openMetaModels).
          - numMetaModels: is the number of meta-models currently loaded
       """
       omm = self.openMetaModels.getValue()                  # obtain the list of remaining meta-models     
       somm = []                                             # list with the meta-models' names
       for openmm in omm:                                    # for each ATOM3String...
          somm.append(openmm.toString())                     # append its value to somm
       index, erased = 0, 0
       while ( index < numMetaModels-erased ):
          # The elements of buttonList are tuples ( <frame>, <formalism name>, <meta-model file>, <button1>, ...)

          mm = self.buttonList[index][1]                     # get the GUI name
          trueMM = self.buttonList[index][2]                 # get the name of the file where the meta-model is stored
          dir, fileName   = os.path.split(trueMM)
          mmName = fileName[:len(fileName)-6]                # that must be the name of the meta-model stored in entitiesInMetaModel
          if not mm in somm:                                 # It is not in the list, so we have erased it
             
             exec "from ASG_"+mmName+" import ASG_"+mmName+"\n"
             anASG = eval("ASG_"+mmName+"(self)")
             
             # Remove the model from sys.path as well, added by Denis Dube, June 25, 2004
             if( dir in sys.path and dir not in CRITICAL_PATHS ):
                sys.path.remove( dir ) 
             
                # Remove sys modules loaded with that meta model
                pattern = re.compile( "<module '\w*' from '"+mmName+"\w*" )
                tmpModules = sys.modules.copy()
                for key in tmpModules.keys():
                  match = pattern.search( str( tmpModules[key] ) )
                  if( match ):   del sys.modules[ key ]
              
                
             frame2delete = self.buttonList[index][0]
             frame2delete.pack_forget()                     # erase panel from User Interface
             # Delete the 'modes' of the buttons that we are to delete...
             for idx in range(3, len(self.buttonList[index])):  # iterate on the buttons of the meta-model
                button2delete = self.buttonList[index][idx]               # get the idx-button of the mm
                if button2delete in self.modes.keys():                    # check if the button has an associated mode
                   mode2delete = self.modes[button2delete]                
                   del self.userActionsMap[mode2delete]                   # delete the associated action to that mode
                   del self.modes[button2delete]                          # delete that mode
             erased = erased + 1                             # increment the counter of erased metamodels
             self.buttonList.remove(self.buttonList[index])  # remove element from the List                   
             if self.console: self.console.appendText('Closing Meta-Model '+mm)
             if mmName in self.entitiesInMetaModel.keys():
                for entity in self.entitiesInMetaModel[mmName]:      # for each entity defined in the meta-model
                  del self.CardinalityTable[entity]              # delete also the info in CardinalityTable
                  if entity in self.ConnectivityMap.keys(): del self.ConnectivityMap[entity]
                del self.entitiesInMetaModel[mmName]
             
             # Map *_MM classnames to the *_META classnames             
             metaModelName = self.openGUI_ModelDict[ mmName + '_MM' ] 
             if( metaModelName[-5:] == '_META' ): metaModelName=metaModelName[:-5]
             
             result = self.ASGroot.unMerge(anASG, metaModelName=metaModelName,
                                           atom3i = self )
             if type(result) != IntType:
               self.ASGroot = result
          else:
             index = index+1             

       if self.openMetaModels.getValue() == []:              # no meta-models are left
          self.ASGroot.removeContents(self, 1)               # clear contents (if any) 
          self.statusbar.event(StatusBar.MODEL, StatusBar.CLEAR, "Nonamed")
          if self.console: self.console.appendText('Clearing model')
          self.ASGroot = None
          # empty the cardinality tables and the connectivity map.
          self.CardinalityTable = {}
          self.ConnectivityMap = {}

    def loadGUImodel(self, file):
       """
          Loads a model of the GUI in the 'Buttons' formalism. Returns this graph.
       """
       oldGraphics = self.genGraphics
       self.genGraphics = 0          				# disble graphics for a while...
       if( file in sys.modules.keys()):     # file has already been loaded
         del sys.modules[file]

       #exec "from "+file+" import *\n" in self.__dict__, self.__dict__
       exec "import "+file
       GUImodelDictionary = eval( file+'.__dict__' )
                       
       # Get the AToM3 version that generated the buttons model
       if( GUImodelDictionary.has_key( 'atom3version' ) ):
          version = GUImodelDictionary[ 'atom3version' ]  
       else:
          version = None
                
       # if we have the meta-model name
       if( GUImodelDictionary.has_key( 'loadedMMName' ) ):
           self.loadedMMName = GUImodelDictionary[ 'loadedMMName' ]
           
           if( self.loadedMMName == 'Buttons_META' ):
             self.loadedMMName = "Buttons"
           
           if self.loadedMMName != "Buttons":			# This should be a 'Buttons' model
              tkMessageBox.showerror(
                 "Couldn't open Formalism!",
                 "Selected file "+self.metaModelName
                 +" does not contain a valid formalism (loadedMMName != Buttons)"
                 +"\n" + self.debug(),
                 parent = self
              )              
              return
            
           # Create a 'Buttons' root node
           from ASG_Buttons import ASG_Buttons
           buttonsRoot = ASG_Buttons(self)           
           del self.loadedMMName
           
           # Do we have a newfunction???
           if( GUImodelDictionary.has_key( 'newfunction' ) ):
             self.newfunction = GUImodelDictionary[ 'newfunction' ]
           else:
              tkMessageBox.showerror(
                 "Couldn't open Formalism!",
                 "Selected file "+file+" does not contain a valid GUI model"
                 +"\nMissing a newfunction method\n" + self.debug()
                 ,parent = self
              )
              return
           
           # look for newly defined or loaded types (loadedTypes should be a list)
           if( GUImodelDictionary.has_key( 'loadedTypes' ) ):
              self.genGraphics = 1
              self.loadTypes( GUImodelDictionary['loadedTypes'] )	# load the new types...
              self.genGraphics = 0
           try:
              if( version != None ):
                self.newfunction(self, buttonsRoot, ButtonsRootNode=buttonsRoot)
              else:
                self.newfunction(self, buttonsRoot)
           except TypeError:              
              tkMessageBox.showerror(
                 "Couldn't open Formalism!",
                 "Selected file "+file+" does not contain a valid GUI model"
                 +"\nTypeERROR encountered\n" + self.debug()
                 ,parent = self
              )
              raise
              return
       else:     
           tkMessageBox.showerror(
                 "Couldn't open Formalism!",
                 "Selected file "+file+" does not contain a valid GUI model\n"
                 +"LoadedMMName not found in dict, import problem...\n"
                 + self.debug()
                 ,parent = self
           )
           return

                   
       self.genGraphics = oldGraphics    			# restore graphics
       return buttonsRoot



    def openMetaModel(self, GUIModel = None, merge = 1, createNewRoot = 1, 
                      fileName = None, printToConsole=True, printToConsoleIndent=''):
       """
          Opens a meta-model, adding the information to the previous ones (if merge == 1). If
          GUIModel is None, then opens a dialog box to ask for the name. GUIModel is the name of the
          GUI Model to be opened previous to the meta-model.
       """
       historyName = None
       if( GUIModel == None):
          if( not fileName ):
              
            text = "Please choose the starting directory for the file dialog\n"
            text += "Last/Default dir is: " + self.initialDirectoryDict[ 'OpenMetaModel' ]
            openDialog = Dialog.Dialog(None, {'title': 'Opening Formalism',
                    'text': text,
                    'bitmap': '',
                    'default': 0,
                    'strings': ('Central Formalism Dir','User Formalism Dir','Last/Default Dir', 'Cancel')})
            if( openDialog.num == 0 ):
              initialDir = META_MODEL_PATH
            elif( openDialog.num == 1 ):
              initialDir = USER_MMODEL_PATH
            elif( openDialog.num == 2 ):
              initialDir = self.initialDirectoryDict[ 'OpenMetaModel' ] 
            else:
              return
              
            fileName = tkFileDialog.askopenfilename(title='Open Formalism/Meta-Model',
                                filetypes=[("Meta-Model files", "*_META.py"),
                                           ("Python files", "*.py")],
                                initialdir=initialDir  )
                      
            # File dialog was cancelled
            if( not fileName):   return                  	
            # Save the directory for next openMetaModel operation
            else: 
              # Get the path for fileName, which is a subdirectory of a Formalism dir
              # So then get the Formalism dir itself, if possible, and save that
              newPath = os.path.dirname( fileName )
              if( newPath ): newPath = os.path.dirname( newPath )
              self.initialDirectoryDict[ 'OpenMetaModel' ] = newPath
        
          dir, file   = os.path.split(fileName)  
          
          # Add the directory to the sys.path              
          self.checkInSearchPath( dir )
          
          className   = string.split (file, ".")                                   # compose class name
          self.GUIModelName = className[0]
          historyName = fileName
        
       # Make sure we can find the GUIModel
       elif( self.addDirectoryWithModelName(GUIModel, noWarning = True ) ):          
          self.GUIModelName = GUIModel
          
       # Uh oh, we couldn't find the GUIModel
       else:
          # If a model is "upgraded" to the new AToM3, the Meta-model name
          # changes from "metaname.py" to "metaname_META.py"
          # So lets check for this as well
          if( GUIModel[-8:] != '_META.py' ):
            pathExtTuple = os.path.splitext( GUIModel )
            GUIModel = pathExtTuple[0] + '_META' + pathExtTuple[1]        
          if( self.addDirectoryWithModelName( GUIModel ) ): 
            self.GUIModelName = GUIModel
          else:
            return  # Nothing worked, give it up
          
       # Wait a sec, is the meta-model already loaded!?!?!
       if(self.ASGroot and self.ASGroot.getASGbyName(self.GUIModelName)):
         print 'WARNING: Attempt to load formalism', self.GUIModelName, \
               'a second time was blocked in', __file__
         return
                   
       if( printToConsole ):    
          t = time.time()
          #print "-----------------------------------------------------------"
          print printToConsoleIndent + "Meta-Model: " + self.GUIModelName
       setCursor( self.parent, 'Busy' )
          
       # Check if newly added paths are causing problems
       self.sourcePathConflictAwareness() 
          
       GUIModel = self.loadGUImodel(self.GUIModelName)				# load the GUImodel
       if GUIModel == None:
          setCursor( self.parent, 'Default' )
          return
        
  
       # retrieve some elements of the GUI...
       fileName    = GUIModel.Formalism_File.toString()				# File where the meta-model is stored.
       dir, file   = os.path.split(fileName)                                    # split directory and file name
       className   = string.split (file, ".")                                   # split file name and extension
       self.metaModelName = className[0]                                        # store the name of the file
 
       ##print '_META file name', self.GUIModelName
       ##print '_MM file name', self.metaModelName 
 
       if not self.ASGroot and not self.editGGLabel:                            # DO NOT DO THIS IF WE ARE A CHILD WINDOW (THAT IS A gg RULE)
          if self.metaModelName in sys.modules.keys():                             # file has already been loaded
             del sys.modules[self.metaModelName]

       if( self.metaModelName == '' ): 
         print 'Cannot open a meta-model with no name!'
         return

       try:
         exec "from "+self.metaModelName+" import *\n" in self.__dict__, self.__dict__
       except ImportError:       
         print "MetaModel "+self.metaModelName+" could not be found... Aborting"
         setCursor( self.parent, 'Default' )
         raise
         ## self.quit()
         ## sys.exit(1)
       except AttributeError:
         print "File "+self.metaModelName+" is not a valid meta-model... Aborting"
         setCursor( self.parent, 'Default' )
         raise
         ## self.quit()
         ## sys.exit(1)

       # If we already have a menu, add to it
       if( self.__dict__.has_key( 'modelMenu' ) ):
          self.modelMenu.add_separator()
          self.createModelMenu(self, self.modelMenu )   
       else:    
          self.parent.config(menu=None)    # eliminate old menu
          buildAllMenus(self)							# Creates a topLevel menu
       
       
       self.configureUserActions()
       self.setConnectivity(self)
       if self.console: self.console.appendText('Opening Formalism '+self.metaModelName)
 
       # delete buttons (if the metamodel they represent is not needed...) and then add the new ones
       if not merge:
         if self.buttonList != []:
           for bt in self.buttonList:
             if not self.__buttonsNeeded(bt):
               try:
                 bt.pack_forget()
                 self.buttonList.remove(bt)
                 del bt
               except AttributeError:
                 buttons = list(bt)[3:]
                 for b in buttons:
                   b.pack_forget()
                   del b
                 self.buttonList.remove(bt)
#         self.toolBar.pack_forget()
       oldASGroot = self.ASGroot 							# keep old instantce of ASGroot
       newASGroot = self.createNewASGroot(self)						# make a new instance of ASG
              
       # Add the buttons to the toolbar
       self.addButtons2ToolBar(GUIModel)	

       if( merge and oldASGroot):								# if we have to merge...
          self.ASGroot.merge(newASGroot  )
       elif( not oldASGroot):        							# if we did not have an ASGroot	
          self.ASGroot = newASGroot
                  
       # Restore old ASG if we did not have to create a new one
       if( createNewRoot == 0 and oldASGroot != None): 
          self.ASGroot = oldASGroot  
        
       # Now lets track the new attributes
       self.ASGroot.trackNewASGroot( newASGroot, self.GUIModelName )
          
       # Put the name on the title bar
       self.putMetaModelName()
       
       # Recently used files history tracker
       if( historyName ):
         self.historyManager( self.LASTOPEN_MMODEL, historyName )
       
       # Map *_MM classnames to the *_META classnames
       self.openGUI_ModelDict[ self.metaModelName ] = self.GUIModelName 
       setCursor( self.parent, 'Default' )
       
       if( printToConsole ):   
          print printToConsoleIndent+"            loaded in %0.3f seconds" % ( time.time() - t )
          #print "-----------------------------------------------------------\n"
       
    def getOpenMetaModelsList( self, getAllModels=False ):
      """ 
      Returns a list of the *_META classnames that can be used to opn a formalism
      You'll notice that this is just a great big ugly hack and is no longer used
      By Denis Dube :D
      """
      raise Exception, 'getOpenMetaModelsList is still being used, DANGIT!!! Send mayday to d3n14@yahoo.com'
      '''
      openModelStringList = []
      numOpenMetaModels = len( self.openMetaModels.getValue() )
      if( numOpenMetaModels > 1 or getAllModels ):
          for i in range( 0, numOpenMetaModels ):
              # Get the name of the file where the meta-model is stored
              d, trueMMname = os.path.split( self.buttonList[i][2] )
              # Remove the .py extension
              trueMMname = trueMMname[:len(trueMMname)-3]  
              if( self.openGUI_ModelDict.has_key( trueMMname ) ):
                  openModelStringList.append( self.openGUI_ModelDict[ trueMMname ] )
              else:
                  print "ERROR: " + trueMMname + " not found in open-meta-model dict"
                  return []
      return openModelStringList  
      '''
 
    def save (self, export = 0, fileName = None):
      """
         Saves the model into disk
      """      
      # try the global constraints...
      res = self.ASGroot.preCondition(ASG.SAVE)						# evaluate global pre-conditions
      if res: return self.constraintViolation(res)					# if violated, show warning and do not save
      # try the local constraints...
      res = self.ASGroot.evaluateLocalPreCondition(ASG.SAVE)                            # evaluate global pre-conditions
      if res: return self.constraintViolation(res)					# if violated, show warning and do not save
      res = self.checkModel()
      if res: return self.constraintViolation(res)					# if violated, show warning and do not save
       
      
      #todo: add choice
      # Do we even have a fileName? If not, we must harass the user...
      if( not fileName or (fileName == "Nonamed") ):  
    
        text = "Please choose the starting directory for the file dialog\n"
        text += "Last/Default dir is: " + self.initialDirectoryDict[ 'OpenSaveModel' ]
        openDialog = Dialog.Dialog(None, {'title': 'Saving Model',
                    'text': text,
                    'bitmap': '',
                    'default': 0,
                    'strings': ('Central Models','Central Formalisms','Last/Default',
                                'User Models','User Formalisms','Cancel')})
        if( openDialog.num == 0 ):
          initialDir = MODEL_PATH
        elif( openDialog.num == 1 ):
          initialDir = META_MODEL_PATH
        elif( openDialog.num == 2 ):
          initialDir = self.initialDirectoryDict[ 'OpenSaveModel' ] 
        elif( openDialog.num == 3 ):
          initialDir = USER_MODEL_PATH
        elif( openDialog.num == 4 ):
          initialDir = USER_MMODEL_PATH
        else:
          return
              
        # Save As Dialog
        fileName = tkFileDialog.asksaveasfilename(
                          filetypes=[("Model files", "*_MDL.py"),
                          ("Python files", "*.py"),("All files","*")], 
                          initialdir=initialDir )	
      
      if( not fileName): return   # File dialog was cancelled               	
      setCursor( self.parent, 'Busy' )
      
         
      # ER model naming convention: finishes with '_model' 
      models =  self.openMetaModels.getValue()
      ERModelNames = [ 'Entity Relationship', 'EntityRelationshipV3' ]
      if(  len( models ) == 1 and models[0].getValue() in ERModelNames ):
        if(  not re.search( '\w*_ER_MDL', fileName ) ):
          fileName = os.path.splitext( fileName )[0] #string.split( fileName, '.' )[0]
          fileName += '_ER_MDL.py'
          
        # Add the ER model to the sys.path if not already, 
        # since the modeler may want to generate code
        ERmodelPath = os.path.split( fileName )[0]
        self.checkInSearchPath( ERmodelPath )
                
      # Python source code must have always have its .py extension...
      if( fileName[-3:] != '.py' ):  
        # Does it have the "Model" extension?
        if( fileName[-4:] == '_MDL' ):
          fileName += '.py'      
        else:
          fileName += '_MDL.py'
        
      # See if file exists:
      if os.path.exists(fileName):        # file exists!!          
          # see if back already exists...
          backupFilename = fileName + ".back"
          if os.path.exists( backupFilename ):         # backup file exists!!
              os.remove( backupFilename )                 # remove it first
          try:
            os.rename( fileName, backupFilename )
          except:
            print "ERROR: Failed to create backup file due to cruel and unusual bug"
      
      # Store all the open meta-models to make this a truly Multi-Formalism system :D
      # NOTE: Old AToM3 builds won't have a clue what this means!!!
      #openModelStringList = self.getOpenMetaModelsList()
      openModelStringList = self.ASGroot.getEntireASGList()
              
      # Call the ASG method to save its contents 
      self.ASGroot.genCode(fileName, self.types, self.genGraphics, 1, 
                           self.GUIModelName, export, self.newTypes, 
                           openModelStringList=openModelStringList,
                           attrGenFix=True ) 
      
      # Update status bar information...
      self.statusbar.event(StatusBar.MODEL, StatusBar.SAVE, fileName)
      if self.console: self.console.appendText('Saving model in file '+fileName)
      
      # Recently used files history tracker
      self.historyManager( self.LASTOPEN_MODEL, fileName )
      
      # Save the directory for next Open or Save operation
      self.initialDirectoryDict[ 'OpenSaveModel' ] = os.path.dirname( fileName )
      setCursor( self.parent, 'Default' )

 
    def checkInSearchPath(self, dir):
      """
         checks if the given directory is in the Python search path.
         If this is not the case, it adds the directory to the path
         Method simplified by Denis Dube, July 26, 2004 because all 
         the sys paths are now in absolute form.
      
      """
      dir = os.path.normpath( dir ) 
      
      # Windows thinks capitilization doesn't matter...     
      if( sys.platform == 'win32' ):
        capitalDir = dir.upper()
        for path in sys.path:
          if( capitalDir == path.upper() ):
            return False
            
      # Linux knows caps make a difference :D
      else:
        if( dir in sys.path ):
          return False
        
      sys.path.append(dir)     
      return True   
        
    def openModelErrorDialog(self, model='N/A'):
        """
        Indicate exactly what went wrong and allow user to reset AToM3 paths
        """
        
        from SimpleDialog import SimpleDialog

        myText = ''
        myText += 'Unable to automatically load the model\'s formalism: "'
        if( model[-5:] == '_META' ): model = model[:-5] 
        myText += model + '"\n\n'
        myText += 'Please make sure the formalism directory is located in ONE of the '
        myText += 'following two directories:\n\n'
        myText += META_MODEL_PATH + '\n'
        myText += USER_MMODEL_PATH
        myText += '\n\nExamples:\n'
        myText += 'Valid: ~\User Formalisms\X\X_META.py\n'
        myText += 'Invalid: ~\User Formalisms\X_META.py\n'
        myText += 'Invalid: ~\User Formalisms\X\X\X_META.py'
     
        d = SimpleDialog(self.parent, text=myText, 
                buttons=['Ok I will try that', 'Still not working? Click here to reset paths (Closes AToM3)'], 
                default=0, 
                title="ERROR loading model: " + model)

        if(d.go() == 1):
          from uninstall import uninstall
          uninstall(useDialogs=False)
          tkMessageBox.showinfo( "Paths Reset",
                                "Paths have been reset, shutting down AToM3",
                                parent = self )
          try:
            self.console.destroy()
          except:
            pass # So what? Won't lose any sleep over this
          try:
            self.debugConsole.destroy()
          except:
            pass # Ditto for the debug console
          self.parent.update()
          self.parent.destroy()
          self.parent.update()
          sys.exit(1)
          
        
        setCursor( self.parent, 'Default' )
        return False
                      
         
        

    def open (self, fileName = None, printToConsole=True ):
      """
         opens a model from disk
      """
      
      if( not fileName ):
          
        text = "Please choose the initial file dialog directory\n\n"
        text += "Last/Default dir is: \n" + self.initialDirectoryDict[ 'OpenSaveModel' ] 
        openDialog = Dialog.Dialog(None, {'title': 'Opening Model',
                    'text': text,
                    'bitmap': '',
                    'default': 0,
                    'strings': ('Central Models','Central Formalisms','Last/Default',
                                'User Models','User Formalisms','Cancel')})
        if( openDialog.num == 0 ):
          initialDir = MODEL_PATH
        elif( openDialog.num == 1 ):
          initialDir = META_MODEL_PATH
        elif( openDialog.num == 3 ):
          initialDir = USER_MODEL_PATH
        elif( openDialog.num == 4 ):
          initialDir = USER_MMODEL_PATH
        elif( openDialog.num == 2 ):
          initialDir = self.initialDirectoryDict[ 'OpenSaveModel' ] 
        else:
          return
                    
        fileName = tkFileDialog.askopenfilename(filetypes=[
                    ("Model files", "*_MDL.py"),("Button Models", "*_META.py")
                    ,("Python files", "*.py")],
                     initialdir=initialDir)	
      # File dialog was cancelled
      if( not fileName):  return                  	
      
      # Save the directory for next Open or Save operation
      self.initialDirectoryDict[ 'OpenSaveModel' ] = os.path.dirname( fileName )
        
      setCursor( self.parent, 'Busy' )
      self.parent.update()
      
      if( not os.path.exists( fileName ) ):  
        tkMessageBox.showerror( "File Not Found          ",
                                "ATOM3.open() could not find:\n\n" + fileName,
                                parent = self )
        setCursor( self.parent, 'Default' )
        return
            
      dir, file   = os.path.split(fileName) 
      
      if( printToConsole ):
        t = time.time()
        #print "***********************************************************\n"
        print "\nLoading model: ", file[:-3] 
        
      # Lets find out which meta-model this model was made with (search the file line by line)
      f = open( fileName , 'r' )
      model = None
      isModelAList = False
      for line in f:
        # Look for a string with the meta-model name
        match = self.LOADED_MM_PATTERN.search( line )
        if( match ):  
            model = match.group(1)           
            break
        
        # Look for  a list with the meta-model names      
        match =  self.LOADED_MM_LIST_PATTERN.search( line )
        if( match ):  
            stringLine = match.group()
            exec( stringLine )            
            isModelAList = True
            break 
      
      #print 'Meta-model: ', model, '== "LIN_FUN_V0_META":', model == 'LIN_FUN_V0_META' 
            
        
      # Add the source path corresponding to each model in the list
      if( isModelAList ):
          for model in loadedMMName:
              if( not self.addDirectoryWithModelName( model, noWarning = True ) ):
                  tkMessageBox.showerror( "Open model error",
                                      "Could not find the following meta-model: "
                                      +str(model)+"\n\nSince the model you are "+
                                      "attempting to load requires that "+
                                      "meta-model, AToM3 will now abort." , 
                                      parent=self)
                  return         
                            
      # No model at all found in the file...
      elif( not model ):
          dir = self.openModelErrorDialog( 'unknown meta-model' )
        
      # Add the source path corresponding to the single model string
      elif( not self.addDirectoryWithModelName( model, noWarning = True ) ):
          
          # If a model is "upgraded" to the new AToM3, the Meta-model name
          # changes from "metaname.py" to "metaname_META.py"
          # So lets check for this as well
          if( model[-8:] != '_META.py' ):
            pathExtTuple = os.path.splitext(model)
            model = pathExtTuple[0] + '_META' + pathExtTuple[1]          
          if( not self.addDirectoryWithModelName( model, noWarning = True ) ): 
            # Everything failed, ask the user to find the meta-model...
            dir = self.openModelErrorDialog(model) 
             
      if( not dir ): return
            
      className   = string.split (file, ".")					# compose class name
      self.newfunction = None
      if className[0]:
        self.checkInSearchPath(dir)
        
        # first check if it has been loaded before, to force a recompilation
        if className[0] in sys.modules.keys():       				# file has already been loaded
           del sys.modules[className[0]]	
           # delete to force a reload

        # Load the model from the file, new method (Doesn't contaminate local namespace)
        try:
          exec  "import "+className[0]+"\n"  
        except:
          raise
          tkMessageBox.showerror("Error", "Could not open model, importation problem" )
          return
        # Load newfunction (name of the method which loads the saved model)
        try:            
          newfunction = eval( className[0] + '.newfunction' )     
        except:
          tkMessageBox.showerror("Error", "Could not open model, newfunction attribute not found" )
          print className[0] + '.newfunction'
          raise
          return
        # Load meta-model environments required for this model to load
        try:
          loadedMMName = eval( className[0] + '.loadedMMName' )
        except:
          loadedMMName = None
        # Load any special types required by this model
        try:
          typeInfoList = eval( className[0] + '.loadedTypes' )
        except:
          typeInfoList = []
        try:
          self.loadTypes(typeInfoList)
        except:
          print '\nERROR: AToM3.open() is unable to load the types defined in',
          print 'the model:', typeInfoList
          print '\nAs a quick fix: edit the *_MDL.py file (end part) and remove',
          print 'the line starting with "loadedTypes = "'
          print '\nThe raw error message will now be raised',
          print '(and AToM3 will close ungracefully):\n'
          raise # <-- You can remove this if you want, it IS informative though
          
        # Load the AToM3 version that saved this model
        try:
          version = eval( className[0] + '.atom3version' )
        except:
          version = '0.2.2'         
        
        # List of meta-models to load (needed for this model)
        if( type( loadedMMName ) == type( list() ) ):
          #todo: warn loading
          for loadName in loadedMMName: 
          
            # No meta-model open, just open this new meta-model
            if( not self.ASGroot):                                 
              self.openMetaModel( loadName, 0, 1,
                                  printToConsole=printToConsole, 
                                  printToConsoleIndent='    ')   
                                                
            # No non-root secondary meta-model open by that name
            elif( not self.ASGroot.getASGbyName( loadName ) ):
              self.openMetaModel(loadName, 1, 0, 
                                  printToConsole=printToConsole, 
                                  printToConsoleIndent='    ') 
                    
        # Single meta-model to load (needed for this model)
        elif( type( loadedMMName ) == type( str() ) ):
                    
          # No meta-model open, just open this new meta-model
          if( not self.ASGroot):                                 
            self.openMetaModel( loadedMMName, 0, 1, 
                  printToConsole=printToConsole, printToConsoleIndent='    ') 
                                       
          # No non-root secondary meta-model open by that name
          elif( not self.ASGroot.getASGbyName( loadedMMName ) ):
            self.openMetaModel(loadedMMName, 1, 0, 
                  printToConsole=printToConsole, printToConsoleIndent='    ') 
                  
          loadedMMName = [loadedMMName] # Make this a list for later...
          
        # No Meta-Model? WTF? Abort!
        else:
          raise Exception, 'Could not load model, no meta-model name found'
          return
            
                                                    
        #print "Running newfunction of model to be opened ", newfunction
        setCursor( self.parent, 'Busy' )
        self.isLoadingModel = True
        #todo: if N formalisms, then N root nodes
        if( version == '0.3' ):
          #allASGnames = self.ASGroot.getEntireASGList()
          allASGlist = []
          for name in loadedMMName:
            ASG = self.ASGroot.getASGbyName(name) 
            if( ASG ): allASGlist.append( ASG  )
            else: print "\n\nUh oh! This is *not* good...",loadedMMName 
          newfunction(self, self.ASGroot, *allASGlist )
        else: 
          newfunction(self, self.ASGroot)
        self.isLoadingModel = False
                          
        # if we have loaded successfully a file, then update status bar...
        self.statusbar.event(StatusBar.MODEL, StatusBar.LOAD, fileName)       # update status bar
        if self.console: self.console.appendText('Loading model from file '+fileName)
        
        # Optimize the loaded model
        #selectAllVisibleObjects( self ) 
        #optimizeConnectionPorts( self )
        self.cb.highlighter(0)
        self.cb.clearSelectionDict()
        
        # For QOCA constraints... See ASG.processLoadedLinkNodes() for more
        self.ASGroot.processLoadedLinkNodes(True)
        
        # Sometimes after loading a large model AToM3 takes a break
        # But there are no unpaid breaks now! Ahahaha. Haha. Bah.
        self.parent.update()
       
        # Recently used files history tracker
        self.historyManager( self.LASTOPEN_MODEL, fileName )
              
        if( printToConsole ):        
          print "Model %s opened in %0.3f seconds" % (file[:-3], time.time() - t )
          #print "***********************************************************\n"
        setCursor( self.parent, 'Default' )
        
    def isATOM3LoadingModel(self):
        """ Can be handy to know this... """
        return self.isLoadingModel
       
    def exitFromATOM3(self, unUsed = None, noDialog=False):
      """ 
      Exits from the current ATOM3 instance
      Returns True if it really exited, and False if the user chickened out.
      """
      if self.IsMainKernel:
        # check status, and if we have not saved, present a message...
        st, fl = self.statusbar.getState(StatusBar.MODEL)
        if(fl):
          lastFile = fl[0]
          print '\nQuick start AToM3 with last model (E-mail denkkar@gmail.com if not working on Linux):'
          lastFile = string.replace(lastFile, '\\\\', '/')
          print 'atom3nosplash.py ' + lastFile#string.replace(lastFile, '\\', '\\\\')
        
        if(st == StatusBar.MODIFIED and not noDialog):
  
          if( fl ):
            filename = fl[0]
          else:
            filename = "unknown"
          saveDialog = Dialog.Dialog(None, {'title': 'Model Modified',
                    'text':
                    '"'+str(filename)+'"'
                    ' has been modified since the last time it was saved.'
                    '\n\nDo you want to save it before exiting the application?',
                    'bitmap': '',
                    'default': 0,
                    'strings': ('Save Model','Discard Changes','Return to AToM3')})
          # Return to editor
          if( saveDialog.num == 2 ):
            return False
          # Save changes
          elif( saveDialog.num == 0 ):
            if fl != 'Nonamed': self.save(0, fl[0]) # Quick save
            else: self.save(0)                      # Full save dialog
                
        # Save initial directories
        self.optionsDatabase.set(self.LAST_INITIAL_DIRS, self.initialDirectoryDict)
        if( self.optionsDatabase.saveOptionsDatabase() == True ):
          doTempCleanupALL() #<-- REMOVE ALL TEMP FILES!
        else:
          try:
            doTempFileCleanup() #<--- Remove temporary Undo & Copy files...
            doTempCleanupChoice() # <-- and other temp files....
          except:
            pass
        #self.optionsDatabase.releaseOptionLock() #<--- Let others be able to save options
        try:
          self.console.getRootTK().destroy()
        except:
          pass # So what? Won't lose any sleep over this
        try:
          self.debugConsole.getRootTK().destroy()
        except:
          pass # Ditto for the debug console
        self.parent.destroy()
        #self.quit()
        #sys.exit(1)
      else:
        #  self.destroy()
        self.parent.destroy()        
    
      return True
        
        
    def addButtons2ToolBar (self, GUIModel):
       """
          Adds the buttons to the toolbar. The specific buttons (that must be created here on the fly) of
          the meta-model are in the GUIModel.
       """

       formalismName = GUIModel.Formalism_Name.toString()			# 'User-friendly' name of the formalism
       
       # Buttons per row, use the meta-models value if there isn't a global overide in effect
       rowSize = self.optionsDatabase.get(self.BUTTONS_PER_ROW)
       if( rowSize <= 0 ):
         rowSize       = GUIModel.RowSize.getValue()				
              
       formalismFile = GUIModel.Formalism_File.toString()			# meta-model file
       fName         = string.replace(formalismName, " ", "_")
       mmToolBar = Frame(self.toolBar, relief = RAISED)       
       b = Label(mmToolBar, text = formalismName, fg="darkgreen",
       bg="white", font = ("Helvetica",10), relief = GROOVE, padx=1)     
       b.pack(side = TOP, fill = X, ipady = 2)
       self.openMetaModels.newItem(ATOM3String(formalismName))
       metaModelInfo = [mmToolBar, formalismName, formalismFile]
       auxPanel = Frame(mmToolBar, relief = GROOVE)
       counter = 0
       
       def findImageFile( fileName ):
          """ Finds the image by looking in all dirs with Formalisms """
          
          filePath = os.path.normpath( os.path.join( META_MODEL_PATH,  
                                       os.path.normpath( fileName ) ) )
          #print 'filePath', filePath
          if( os.path.exists( filePath ) ):  return filePath
          
          filePath = os.path.normpath( os.path.join( USER_MMODEL_PATH,  
                                       os.path.normpath( fileName ) ) )
          if( os.path.exists( filePath ) ):  return filePath
          
          filePath = os.path.normpath( os.path.join( SOURCE_CODE_PATH,  
                                       os.path.normpath( fileName ) ) )
          if( os.path.exists( filePath ) ):  return filePath
          
          return None
       
       # Important Notice: To correctly create buttons with images, we have to create
       # a different attribute name for each...

       # imgAttrName = "ImgButton"       
       for node in GUIModel.listNodes['ButtonConfig']:                          # for each 'ButtonConfig' in the model...
         text = 1
         if node.Contents.lastSelected == 'Text':                              # check if we should put a text in the button
           buttonText = node.Contents.Text.toString()                         # get the button text...
         elif node.Contents.lastSelected == 'Image':
           text = 0
           buttonImageFileName = findImageFile( node.Contents.Image.toString() )     
           if( not buttonImageFileName ):
              text = 1
              buttonText = node.Contents.Image.toString()
           
         if( not text ):
           self.buttonImage.append(PhotoImage(file = buttonImageFileName))
           self.numImg = self.numImg+1

         newDrawingMode = node.Drawing_Mode.getValue()[1]                   # see if we have to create a new mode

         name, lang, kind, act, code = node.Action.getValue()     		# Unwrap action...
         
         """
         #if newDrawingMode:
         functionName   = fName+str(counter)                                 # compose function name
         # see if the function is present yet
         if( not functionName in self.__dict__.keys() ):
           functionHeader = "def "+functionName+"(self, wherex, wherey ):\n"   # compose function header
           functionBody   = "   " +string.replace(code,'\n', '\n   ')+"\n"     # compose function body
           
           # Path to a temp file (make sure it's empty)   
           path = os.path.split(  __file__ )[0]  
           path = os.path.join( path, 'temporaryFILE923.py' )                      
           if( os.path.exists( path ) ): os.remove( path ) 
           
           # Open the temp file and create our method...
           tempFile = open( path, 'w')
           tempFile.write( functionHeader + functionBody )
           tempFile.close()
           
           # Make sure an earlier method is not in memory...
           if( sys.modules.has_key( 'temporaryFILE923' ) ):
             del sys.modules['temporaryFILE923']
             
           import temporaryFILE923   
           
           # Cleanup temp files
           try:        
             if( os.path.exists( path ) ):     os.remove( path ) 
             if( os.path.exists( path+'c' ) ): os.remove( path+'c' ) 
           except:
             pass

           # Extract our compiled method
           if( temporaryFILE923.__dict__.has_key(functionName) ):
             self.__dict__[functionName] = temporaryFILE923.__dict__[functionName]
           
         method = self.__dict__[functionName]		 # obtain a reference to the method
         newMode = "NEWMODE"+fName+str(counter)  # create a new Mode for the button
         if not node.Drawing_Mode.getValue()[1]: # Is it a method 2b executed right away? (added 27 July 2002, JL)
            newMode = newMode+"&&EXEC"           # This distinguishes the executable modes (added 27 July 2002, JL)

         self.userActionsMap[newMode] = method   # set the userACtionsMap dictionary           
         """
         
         #if newDrawingMode:
         functionName   = fName+str(counter)                                 # compose function name
         # see if the function is present yet
         if not functionName in self.__dict__.keys():
           functionHeader = "def "+functionName+"(self, wherex, wherey ):\n"   # compose function header
           functionBody   = "   " +string.replace(code,'\n', '\n   ')+"\n"     # compose function body
           #todo: BAD CODE
           # This generates a Syntax Warning whenever a from x import * statement occurs
           # This really should not have been necessary!!! 
           # Fix idea: save method to a file, then load the file, not sure if it'd will do though...
           # Why it's bad: http://www.python.org/doc/2.2.3/whatsnew/node9.html
           exec functionHeader+functionBody in self.__dict__, self.__dict__    # 'create' new method
            
         method = self.__dict__[functionName]				       # obtain a reference to the method
         newMode = "NEWMODE"+fName+str(counter)                             # create a new Mode for the button
         if not node.Drawing_Mode.getValue()[1]:                            # Is it a method 2b executed right away? (added 27 July 2002, JL)
            newMode = newMode+"&&EXEC"                                      # This distinguishes the executable modes (added 27 July 2002, JL)

         self.userActionsMap[newMode] = method                              # set the userACtionsMap dictionary     
         
         
         if text:
           newButton = Button(auxPanel, text = buttonText,
                              bg="white", activebackground="white" )
         else:
           newButton = Button(auxPanel,
                              image = self.buttonImage[self.numImg],
                              bg="white", activebackground="white"  )

         self.modes[newButton] = newMode      # set the bind newButton->changeMode
         newButton.bind("<ButtonRelease-1>", self.changeMode)
         
       
         # Proof of concept: could have a window popup up with help info...
         # This stuff merely makes passing a cursor over a button VERY obvious
         def handler( event, button = newButton ):
            button.configure( bg='firebrick2', activebackground='SpringGreen2',
                             borderwidth=2, relief='groove' )
         newButton.bind( '<Enter>', handler)
         def handler( event, button = newButton ):
            button.configure( bg='white', activebackground='white',
                             borderwidth=2, relief='raised' )
         newButton.bind( '<Leave>', handler)
 

         # This makes the right mouse button behave just like the left mouse button
         def modelButtonPress3( button ):
            button.configure( relief = "sunken" )
         def modelButtonRelease3(self,event,button):
            button.configure( relief = "raised" )
            self.changeMode(event)
         newButton.bind("<Button-3>", 
                        lambda event,n=newButton: modelButtonPress3(n) )
         newButton.bind("<ButtonRelease-3>", 
                lambda event,n=newButton,s=self: modelButtonRelease3(s,event,n) )

         newButton.pack(side=LEFT, padx=2)#, pady=2, fill=X, expand=1)
         counter = counter + 1
         if(counter % rowSize == 0):      # check if we have rowSize elements in the row
           auxPanel.pack(side=TOP)#, ipady=10, ipadx=10)
           auxPanel = Frame(mmToolBar, relief = GROOVE)
           
         metaModelInfo.append(newButton)

       self.buttonList.append(tuple(metaModelInfo))
       auxPanel.pack(side=TOP, fill=X)#, ipady=20)
       
       emptyPanel = Frame(mmToolBar)
       emptyPanel.pack(side=BOTTOM, fill=Y, expand=1)
       
       mmToolBar.pack(side=LEFT, fill=Y)
       # To push the buttons to the top of the panel, put an empty frame
       # in the bottom.
       #emptyPanel = Frame(self.toolBar, bg="black")
       #emptyPanel.pack(side=BOTTOM, fill=BOTH,expand=1)
       
       # Toolbar items may have changed
       self.parent.update()     
       self.configureToolbar()  


    #....................................................

    def chooseLinkType(self, listOfLinks):
      """ Function that presents a dialog box to choose a link type
          - listOfLinks: is a list of tuples (<class-name>, <method-2-create-instance-of-class>)
          - returns the tuple that's been selected
      """
      # first we create a list of ATOM3Strings using the first component of the tuples...
      if( 0 ):
        A3StringList = []
        for link in listOfLinks:
            ns = ATOM3String(link[0])
            A3StringList.append(ns)
        # create an ATOM3List of Strings with the initial value set to the previous list
        atl = ATOM3List([0,0,0,0], ATOM3String)
        atl.setValue(A3StringList)
        # Present the previous list in a dialog box
        dlb = ATOM3TypeDialog(self, atl)
        if dlb.result_ok:
          return listOfLinks[dlb.widget.lastSelection]
          
      # Popup menus are more l33t :D
      else:
        stringList = []        
        for link in listOfLinks:
          stringList.append( link[0] )
          
        title = 'Link Type'
        actionLabel = 'Select'
        index = self.popupMenuCreator.listChoicePopup( title,stringList,actionLabel )
                
        # Unacceptable result, must have a valid choice or exception will occur
        if( index == 0 ): return self.chooseLinkType( listOfLinks )
        return listOfLinks[ index-1 ]

    
    def modelAttributes(self, metaModelASG = None ):
      """
      Edits model attributes, including global constraints...
      Can handle multiple meta-models at once.
      """
      # User provides a specific ASG to edit...
      if( metaModelASG ): 
         val = ATOM3TypeDialog(self, metaModelASG )
         # Now we know when the user has finished editing the ASG options
         metaModelASG.postCondition (ASGNode.EDIT) 
      # We'll try and figure out which ASG to edit...
      else: 
        self.ASGroot.showASGattributesDialog( self )
        # Now we know when the user has finished editing the ASG options
        self.ASGroot.postCondition (ASGNode.EDIT) 
      return 
    
      #todo: site of a major hack
      """
      metaModelASG = self.ASGroot
      if( metaModelASG.mergedASG ):
          ASGList = metaModelASG.mergedASG[:] + [metaModelASG]
          stringList = []
          for ASG in ASGList:
              stringList.append( ASG.__class__.__name__ )
          
          title = 'Choose Meta-Model'
          actionLabel = 'Select'
          index = self.popupMenuCreator.listChoicePopup( title,stringList,actionLabel )
                  
          # Invalid result? Quit
          if( index == 0 ): return
          
          # Valid result? Use this metaModelASG then.
          metaModelASG = ASGList[ index-1 ]
      
      ATOM3TypeDialog(self, metaModelASG )
      """
      
    def showConsole(self):
      """ Shows the console, if it is hidden """
      if( self.debugConsole.showWindow() == -1 ):
        self.debugConsole = DebugConsole(self)
        self.debugConsole.showWindow() 
        
      if( self.console.showWindow() == -1 ):	
        self.console = Console(self)
        self.console.showWindow()     
          
       
        
    def find_visible_closest (self, x, y, canvas, limit=50,ignore=None):
      """
         Returns the closest item to (x, y) which is visible.
         If the item has 4 or more coordinates, then the distance of (x0,y0) to the segments defined by each
         4 consecutives coordinates (x1, y1) (x2, y2) are calculated:
         Added : 10 July 2002 JL
      """
      
      # Check if a "current" item is selected, could save us some trouble
      itemHandler = canvas.find_closest(x,y)   
      if( itemHandler and itemHandler[0] != ignore \
                      and self.__isItemVisible(itemHandler[0], canvas) ):
        tags = canvas.gettags( itemHandler[0] )  
        if( "current" in tags ): 
          return (itemHandler[0], )
          
      
      minDistance = 20000                                       # mimimum distance
      minDistItem = -1                                          # item with minimum distance
      
      # items tuple with all the items within a certain region
      items = canvas.find_overlapping(x-limit, y-limit, x+limit, y+limit)  
      segmin = None
      for item in items:                                        # get the item with minimum distance
        if( self.__isItemVisible(item, canvas) and (item != ignore) ):          
           if canvas.type(item) == 'text':
             crd = canvas.bbox(item)
           else:
             crd = canvas.coords(item)
           ncoords = len(crd)
           
           # Entity or link... [0,0, 1,1, 2,2, 3,3]  [0,2,4]
           if ncoords >=4:
             for i in range(0, ncoords-3, 2):
               
               # Check if x0 == x1 and y0 == y1, point object
               if crd[i] == crd[i+2] and crd[i+1] == crd[i+3]:
                 distance = self.__dist(crd[i], crd[i+1], x, y) # math.sqrt(abs((crd[i]-x)*(crd[i]-x)+(crd[i+1]-y)*(crd[i+1]-y)))                 
               
               # Check distance between event and the segement line described by x0,y0,x1,y1
               else:
                 distance = self.__point2Segment(x, y, crd[i], crd[i+1], crd[i+2], crd[i+3])
               
               if( distance < minDistance ):
                
                 # Ignore items without tags --> Probably the snap grid
                 tags = canvas.gettags( item )
                 if( len(tags) == 0 or tags[0] == 'current' ): continue
                 
                 segmin = crd[i], crd[i+1], crd[i+2], crd[i+3]
                 minDistance = distance
                 minDistItem = item  
                 
            # Point object
           else:
               distance = self.__dist(crd[0], crd[1], x, y) # math.sqrt(abs((crd[0]-x)*(crd[0]-x)+(crd[1]-y)*(crd[1]-y)))
               if distance < minDistance:
                 segmin = crd[0], crd[1]
                 minDistance = distance
                 minDistItem = item
           #print " type = ", self.UMLmodel.type(item)
           #print "    - coords = ", crd
           #print "    - dist = ", distance
      #print "************************", minDistance, x, y              
      return (minDistItem, )




    def editclass(self, x, y, itemHandler = None ):
      """
      Edits the nearest class that can be found in the canvas,
      UNLESS you specify an itemHandler, in which case will use that one
      """
      self.cb.setEditState(None, None) # Reset edit state
      dc = self.getCanvas() 
   
      # Get an itemHandler to edit...
      if( itemHandler ):
        ct = itemHandler
      else:               
        # Assume we recieve x,y as event.rootx,event.rooty pair
        # So must normalize to put them back in the canvas area
        xx,yy = self.cb.getLastClickCoord()
        ct = self.find_visible_closest(xx,yy, dc)
        
      # Get the tag and then have fun...
      tags = dc.gettags(ct)
      if tags:
          # try the global constraints...
         if not self.editGGLabel:
            res = self.ASGroot.preCondition(ASG.EDIT)
            if res:                                                                          # global constraint do not hold!
                self.constraintViolation(res)
                return
         if( VisualObj.Tag2ObjMap.has_key( tags[0] ) ):
           obj = VisualObj.Tag2ObjMap[tags[0]]
         else:
          return
         if not self.editGGLabel:
            res = obj.semanticObject.preCondition ( ASGNode.EDIT )         # Local preconditions...
            if res:
                self.constraintViolation(res)
                return
         self.ASGroot.preAction(ASGNode.EDIT)
         obj.semanticObject.preAction ( ASGNode.EDIT )
         
         
         # Position the edit box with care :D
         #margin = dc.winfo_screenwidth() / 2
         #if( x > margin ): x = margin
         #margin = dc.winfo_screenheight() / 3
         #if( y > margin ): y = margin
         if(self.editGGLabel == ASG.INLHS):
           extraText = "WARNING: use the attribute field OR Set to any"
         elif(self.editGGLabel == ASG.INRHS):
           extraText = "WARNING: use only Copy OR Specify (and not both)"
         else:
           extraText = ''
         ma = ATOM3TypeDialog(self, obj.semanticObject, 0, 
                            (self.setEditGGLabel ,None),topLeftCoords=[x,y],
                            extraText=extraText)
         if ma.result_ok:   # update ATOM3Appearance with the keyword change...
            # Check that the GG label is unique (IMPORTANT), if in GG 
            if(self.editGGLabel):
              currentGGlabelInt = obj.semanticObject.GGLabel.getValue()
              for nodeType in self.ASGroot.listNodes.keys():
                for node in self.ASGroot.listNodes[nodeType]:
                  if(node.GGLabel.getValue() == currentGGlabelInt):
                    # Woops, not a duplicate if that's ourself...
                    if(obj.semanticObject == node):
                      continue
                    self.constraintViolation(("Duplicate GG label: "
                                                +str(currentGGlabelInt),""))   
                    # restore old information     
                    obj.semanticObject.copy(ma.previousObject)  
                    self.editclass(x, y)
                    return
            
            # Check that the keyword of the entity is still unique, if it has one.
            if obj.semanticObject.keyword_:
               for element in self.ASGroot.listNodes[obj.semanticObject.__class__.__name__]:
                  if obj.semanticObject != element and obj.semanticObject.keyword_.toString() == element.keyword_.toString():   # different elements and same keyword, so invalidate the previous editing
                     # it is not an error if both are None and we are in a graph-grammar rule
                     if obj.semanticObject.keyword_.isNone() and element.keyword_.isNone() and self.editGGLabel:
                        pass
                     else:
                        self.constraintViolation(("Duplicate keyword: "+element.keyword_.toString(),""))            # we should undo the editing
                        obj.semanticObject.copy(ma.previousObject)                                               # restore old information
                        self.editclass(x, y)
                        return

            if not self.editGGLabel:
               res = obj.semanticObject.postCondition ( ASGNode.EDIT )          # if we are not in a GG rule
               if res:
                  self.constraintViolation(res)                                                         # Present an error message
                  obj.semanticObject.copy(ma.previousObject)                                            # restore old information
                  self.editclass(x, y)                                                                  # edit again!
                  return

            if not self.editGGLabel:
               res = self.ASGroot.postCondition(ASGNode.EDIT)
               if res:
                  self.constraintViolation(res)                                                          # Present an error message
                  obj.semanticObject.copy(ma.previousObject)                                             # restore old information
                  self.editclass(x, y)                                                                      # edit again!
                  return

            obj.semanticObject.postAction ( ASGNode.EDIT )
            self.ASGroot.postAction(ASGNode.EDIT)
            
            # Modify the visual attributes
            for attr in obj.semanticObject.generatedAttributes.keys():
               types = obj.semanticObject.generatedAttributes[attr]
               for t in types:
                 if t == 'ATOM3Appearance':                             # if it is appearance
                    appAttr = obj.semanticObject.getAttrValue( attr )
                    if obj.semanticObject.keyword_:
                       appAttr.setValue( (obj.semanticObject.keyword_.toString(), ) )
                   
            def modifyVisualAttribute( visualAttr, obj ):
              """ 
              Text char area set to unlimited by Denis Dube, March 5, 2005
              Text char area set to [80,10] by Denis Dube, Aug 24, 2004 
              Text char area set to [25,5] by JL, July 16, 2002      
              NOTE: The Kernel.GraphicEditor.SaveGFVisitor.visitAttribute() method
                    must use the same text character area as here for consistency
                    with newly created Formalisms (whose Icons are created with
                    the graphic editor). 
              """        
              valueStr = obj.semanticObject.__dict__[visualAttr].toString()
              obj.ModifyAttribute(visualAttr, valueStr)  
              
            # Modify also the visual attributes  
            for visualAttr in obj.attr_display.keys():
               if self.editGGLabel== ASG.INLHS and obj.semanticObject.__dict__[visualAttr].isNone():
                  obj.ModifyAttribute(visualAttr, "<ANY>")
               elif self.editGGLabel== ASG.INRHS:                                   # Modified 22 July 2002, JL
                  if obj.semanticObject.GGset2Any.has_key(visualAttr):
                    if obj.semanticObject.GGset2Any[visualAttr].Copy.getValue()[1]:
                       obj.ModifyAttribute(visualAttr, "<COPIED>")
                    elif not obj.semanticObject.GGset2Any[visualAttr].Specify.getValue()[4] in ["", "\n", None]:
                       obj.ModifyAttribute(visualAttr, "<SPECIFIED>")
                    else:
                       modifyVisualAttribute( visualAttr, obj )                                    
               else:
                  modifyVisualAttribute( visualAttr, obj )       
            # update status bars...
            if self.editGGLabel :
               self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.MODIFY)
               obj.drawGGLabel(self.UMLmodel)
            else:
               self.statusbar.event(StatusBar.MODEL, StatusBar.MODIFY)
               
            # Store edit state, obviously everything worked out here!
            # But what if a postStatechart wants to restore the old state? NP!
            self.cb.setEditState(obj.semanticObject, ma.previousObject) 
      self.mode = self.IDLEMODE
      
      
        
    def codeGenerationDialog( self ):
        """ Now you know where the heck that code is being generated to :D """
        modelPathAndFile = self.statusbar.getState(self.statusbar.MODEL)[1][0]      
        modelPath, modelName = os.path.split(modelPathAndFile)
        modelName = modelName.split('.')[0]
        
        if( self.ASGroot and hasattr( self.ASGroot, 'name' ) ):
          if( self.ASGroot.name.getValue() == 'ERModel' ): 
            myText = 'The model name "ERModel" is reserved!\n\n' \
                     + 'Please choose a different name' 
            dialog = Dialog.Dialog(None, {'title': 'Naming Error',
                      'text': myText,
                      'bitmap': '',
                      'default': 0,
                      'strings': ('Set new name','Generate anyway','Cancel')})
            # Set new name...
            if( dialog.num == 0 ):
              self.modelAttributes()
              return self.codeGenerationDialog()
            # Proceed anyway
            elif( dialog.num == 1): pass
            #Cancel
            else: return
          
          elif( self.ASGroot.name.getValue() == '' ): 
            myText = 'Attempted to generate code for model with no name!\n' \
                      +'Please give your model a name'
            dialog = Dialog.Dialog(None, {'title': 'Naming Error',
                      'text': myText,
                      'bitmap': '',
                      'default': 0,
                      'strings': ('Set name','Use '+modelName+' as name','Cancel')})
            # Set new name...
            if( dialog.num == 0 ):
              self.modelAttributes()
              return self.codeGenerationDialog()
            # Proceed anyway
            elif( dialog.num == 1):               
              self.ASGroot.name.setValue(modelName)
              self.modelAttributes()
              return self.codeGenerationDialog()
            #Cancel
            else: return
          
      
        
      
        myText = ''
        myText += 'In which directory shall the code be generated?:\n'
        myText += 'NOTE: this directory must contain all graph_*.py files that make up the model.\n\n'
        myText += 'Current model directory: ' + modelPath + '\n\n'
        myText += 'Default directory: ' + self.codeGenDir + '\n\n'
        myText += 'You can also choose any directory in the User Formalisms area\n'
        
        dialog = Dialog.Dialog(None, {'title': 'Code Generation',
                    'text': myText,
                    'bitmap': '',
                    'default': 0,
                    'strings': ('Current Model Dir.','Default Dir.', 'User Formalisms','Cancel')})
             
        # Set Code Gen. Dir to the current Model Dir.
        if( dialog.num == 0 ):  
          oldCodeGenDir = self.codeGenDir
          self.codeGenDir = os.path.normpath( modelPath )
          g = self.genCode( showDialog = False ) 
          self.codeGenDir = oldCodeGenDir
          return g
      
        # Use the Code Gen. Dir. from Options
        elif( dialog.num == 1 ):
          return self.genCode( showDialog = False )
        
        # Choose a new Code Gen. Dir manually
        elif( dialog.num == 2 ):         
          try:          
            pathFile = tkFileDialog.asksaveasfilename(
                      title="Code generation directory",
                      initialfile='Filename_Will_Be_Ignored',
                      filetypes=[("All files","*")], 
                      initialdir=USER_MMODEL_PATH)	
          except:
            pathFile = tkFileDialog.askopenfilename(
                         title="Code generation directory",
                        filetypes=[("Choose any file in Code Gen. Dir.", "*")]
                        ,initialdir = USER_MMODEL_PATH ) 
          if( pathFile ):  
            pathFile = os.path.split( pathFile )[0] 
       
                        
          # Cancel
          if( pathFile == '' ): 
            return None 
          oldCodeGenDir = self.codeGenDir
          self.codeGenDir = os.path.normpath( pathFile )
          g = self.genCode( showDialog = False ) 
          self.codeGenDir = oldCodeGenDir
          return g
        
        # Cancel
        elif( dialog.num == 3 ):
          return None
     
  
         
    def genCode(self, showDialog = True ):
       """
          Generates Python code from the model information
       """
       if not self.existGenerativeAttributes():                         # no code to generate, model is not generative!
          tkMessageBox.showerror(
               "No code can be generated",
               "Trying to produce code from a non-generative model",
               parent = self
          )
          return    
          
       # Check if multiple-formalisms are being used while generating code
       if(len(self.ASGroot.getEntireASGList()) > 1):         
         myText = "Trying to generate code in the presence of " \
                 + "multiple-formalisms\n" \
                 + str(self.ASGroot.getEntireASGList()) \
                 + '\n\nWARNING: This will only work if the generating ' \
                 + 'formalism was opened first (it appears to the left in ' \
                 + 'the toolbar)'
         dialog = Dialog.Dialog(None, {'title': 'Code Generation Warning',
                    'text': myText,
                    'bitmap': 'warning',
                    'default': 0,
                    'strings': ('Abort','Continue')})
         if(dialog.num == 0):
           return
                               
       if( showDialog ):
         return self.codeGenerationDialog()

       hasGraph = 0							# flag that indicates if we have a graphical attribute
       cardConstObjects = []
       if self.ASGroot.keyword_:
          if self.console: self.console.appendText('Generating code for model '+self.ASGroot.keyword_.toString())
       else:
          if self.console: self.console.appendText('Generating code for model.')
       for nodeType in self.ASGroot.nodeTypes:				# for each node type
          for UMLobject in self.ASGroot.listNodes[nodeType]:		# for each object of any type
              self.genCodeFor (UMLobject, cardConstObjects)		# Generate code for this particular entity	              								# in cardConstObjects, we are storing the objects with cardinality constraints
       # see first if we have generative attributes...
       self.genASGCode(cardConstObjects)                                # generate code for the ASG node
       self.genButtons()                                                # generate the file for the syntax actions
       # now generate the file with the GUI model...
       self.genButtonsModel()   
        
       tkMessageBox.showinfo(
         "Code generated",
         "Please restart AToM3 before trying to load the newly generated "
         + "formalism\n\nHINT: starting another instance of AToM3 works too",
         parent = self
          )
          
        
    def genButtonsModel(self, ASGroot=None):
       """
          Generates a model in the "Buttons" formalism with the button layout and associated actions. It is
          done by executing the graph grammar createButtons.
       """
       if(ASGroot == None):
         ASGroot = self.ASGroot
         
       from ButtonGenerator import ButtonGenerator
       print 'NOTE: Buttons grammar bypassed by Denis Dube (denkkar@gmail.com), 2006', __file__
       return ButtonGenerator(self, ASGroot)
       
#        nameButtonBar = ASGroot.keyword_.toString()
#        
#        # Old path = where it will be generated by the GG, new path is where we want it
#        oldMetaModelPath = os.path.join( self.codeGenDir,nameButtonBar+".py" )
#        newMetaModelPath = os.path.join( self.codeGenDir,nameButtonBar+"_META.py" )
#        
#        # The button model already exists! Re-generate or not...?
#        if( os.path.exists( newMetaModelPath ) ):
#           myText = ''
#           myText += 'Old buttons model detected: ' + newMetaModelPath
#           myText += '\n\nDo you wish to re-generate the buttons model?'
#           myText += '\n\nRe-generation is only useful if entities have been added/removed to/from your model'
#           
#           dialog = Dialog.Dialog(None, {'title': 'Overwrite Buttons Model?',
#                       'text': myText,
#                       'bitmap': '',
#                       'default': 0,
#                       'strings': ('Keep old model','Overwrite')})
#                
#           # Keep the old model
#           if( dialog.num == 0 ):  
#             return
#        
#        oldGenGraphics = self.genGraphics
#        self.genGraphics = 0       
#        if self.console: self.console.appendText('Generating file '
#                         +nameButtonBar+'_META.py in directory '+self.codeGenDir
#                         +' (User Interface file)')
#        try:         
#          # get the graph grammar to execute from the options... (modified 29/July 2002)
#          exec "from "+self.GGforCodeGen+" import *\n" 
#          # in self.__dict__, self.__dict__      
#          self.GraphGrammars = [ eval(self.GGforCodeGen+"(self)") ]      
#        except:
#          eText = 'ERROR: Graph grammar not found (or incorrect). Tried:' 
#          eText += "from "+self.GGforCodeGen+" import *\n" 
#          eText += 'Please make sure that was the right graph grammar'
#          eText += ' in AToM3 main options is selected\n\n'
#          eText += 'For example: Class Diagrams and Entity Relationships have'
#          eText += 'different graph grammars for generating buttons.\n'
#          eText += '\nDue to error, no buttons model (*_META.py) was generated'
#          print eText
#          showerror('Buttons Graph Grammar', eText)         
#          return
#                    
#        # get the graph grammar to execute from the options... (modified 29/July 2002)
#        self.grs = GraphRewritingSys(self, self.GraphGrammars, ASGroot )
#        self.grs.evaluate(stepByStep = 0, moveEntities = 0, 
#                          execute = self.grs.SEQ_RANDOM, graphics = 0)	
#                          # no graphics (the canvas with the model is closed!)
#        self.genGraphics = oldGenGraphics  
#    
#        # The following is ugly: to add the following header, the file generated
#        # by the graph re-writing system must be read in then writed out again.
#        file = open( oldMetaModelPath, 'r' )
#        fileText = file.read()
#        file.close()   
#        os.remove( oldMetaModelPath )
#          
#        # Header + Generated File
#        file = open( newMetaModelPath, 'w+t' )
#        file.write('"""\n')
#        file.write("__"+ nameButtonBar+"_META.py_____________________________________________________\n")
#        file.write("\n")
#        file.write("Automatically generated AToM3 button model (DO NOT MODIFY DIRECTLY)\n")
#        try: 
#         file.write("Generated by graph grammar: "
#                    +self.GraphGrammars[0].__class__.__name__+'\n')
#        except: pass
#        file.write("Author: "+USER_NAME+"\n")
#        file.write("Modified: "+time.asctime()+"\n")
#        file.write("__"+ len(nameButtonBar+"_META.py")*"_" +"_____________________________________________________\n")
#        file.write('"""\n')
#        file.write(fileText)     
#        file.close()
     
        
    def addCopyFromLHSButton(self, GGrule):
       """
        Adds a button to copy the nodes in the LHS when editing a graph grammar.
        - GGrule is an object of type GGruleEdit, which contains the semantic 
        information of the rule being edited. A reference to this object is 
        kept in self.GGSemanticRule for latter use in callback method copyFromLHS.
        Added 20/July/2002 by JL
       """
       if(self.editGGLabel == ASGNode.INRHS):  # add a button to copy from LHS's
           self.GGSemanticRule = GGrule
           
           mmToolBar = Frame(self.toolBar, relief = RAISED)       
           b = Label(mmToolBar, text = "Transformation", fg="darkgreen",
           bg="white", font = ("Helvetica",10), relief = GROOVE, padx=1)     
           b.pack(side = TOP, fill = X, ipady = 2)
           bcopy = Button( mmToolBar, text="Copy LHS", command=self.copyFromLHS )
           bcopy.pack(side=LEFT, padx=2, pady=1)
           
           from DrawConnections import allowGenericLinks
           g = Button( mmToolBar, text="Generic Links", 
                      command=lambda s=self: allowGenericLinks(s))
           g.pack(side=LEFT, padx=2, pady=1)
                      
           mmToolBar.pack(side=LEFT, fill=Y)
           
           # Toolbar items may have changed
           self.parent.update()     
           self.configureToolbar()  
           
       # Adds button to allow generic links between any entities
       elif(self.editGGLabel == ASGNode.INLHS):
           mmToolBar = Frame(self.toolBar, relief = RAISED)       
           b = Label(mmToolBar, text = "Transformation", fg="darkgreen",
           bg="white", font = ("Helvetica",10), relief = GROOVE, padx=1)     
           b.pack(side = TOP, fill = X, ipady = 2)
                      
           from DrawConnections import allowGenericLinks
           g = Button( mmToolBar, text="Generic Links", 
                      command=lambda s=self: allowGenericLinks(s))
           g.pack(side=LEFT, padx=2, pady=1)
           
           # Allow seperation of an association from it's connecting entities
           from CallbackHandlers import getSelectedItemsForDelete           
           ff = Button( mmToolBar, text="Isolate Association", 
                      command=lambda s=self: getSelectedItemsForDelete(s, entityOnlyFlag=True))
           ff.pack(side=LEFT, padx=2, pady=1)
           
           mmToolBar.pack(side=LEFT, fill=Y)
           
           # Toolbar items may have changed
           self.parent.update()     
           self.configureToolbar()     
                  
       
    def deleteRealEntity (self, tag, obj = None, entityOnly=False ):
       """ 
       Deletes the entity with tag 'tag' invoking corresponding 
       pre and post conditions 
       Parameters:
         tag: the tag of a graphical object
         obj: the semantic object (optional), can use any value for tag...
       """    
       if( not  obj ):
         if( not VisualObj.Tag2ObjMap.has_key( tag ) ):
           print "The following tag was not found, so it was probably already deleted: ", tag
           return 
         obj = VisualObj.Tag2ObjMap[tag]                          # obtain the visual object

       res = self.ASGroot.preCondition (ASGNode.DELETE)         # Test global pre condition
       if res:
          self.constraintViolation(res)
          return

       res = obj.semanticObject.preCondition (ASGNode.DELETE)   # Test local pre condition
       if res:
          self.constraintViolation(res)
          return

       self.ASGroot.preAction ( ASGNode.DELETE )
       obj.semanticObject.preAction ( ASGNode.DELETE )

       obj.erase(self, entityOnly=entityOnly)
       # remove from ASG and from all its connected nodes...
       obj.semanticObject.removeNode()

       res = self.ASGroot.postCondition (ASGNode.DELETE)         # Test global post condition
       if res:
          self.constraintViolation(res)
          return

       res = obj.semanticObject.postCondition (ASGNode.DELETE)   # Test local post condition
       if res:
          self.constraintViolation(res)
          return
  
       self.ASGroot.postAction ( ASGNode.DELETE )
       obj.semanticObject.postAction ( ASGNode.DELETE )
       
#================================================================================
#Hierarchical structure maintenance, see HierarchicalASGNode.py for more info
#================================================================================
       if(obj.semanticObject.isHierarchicalNode()):
         obj.semanticObject._removeNodeFromHierarchyTopLayer()
           
    """
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # 
    # 
    # Above these lines, code has been created / modified by Denis Dube during the Summer of 2004
    # 
    # 
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    # ----------------------------------------------------------------------------------------------------------------
    """
    
    def closeUnusedMetaModels(self):
       """
          Closes the meta-models which do not have entities in the current model.
       """
       # This method disabled by Denis - Feb 12, 2005
       # Its the non-interactive method, and it does annoying things
       # Ex: toolbars are now meta-models and they are of course "unused" on
       # the canvas, so they get automatically closed. Yuck!!! 
       return 
       """
       MetaModels2Leave = []                                    # List of meta-models that we will not erase
       # Search for each entity of each meta-model, to see if there is any instance, in that case, we cannot erase the mm. 
       for mm in self.entitiesInMetaModel.keys():		# for each opened metamodel
          delete = 1
          for entity in self.entitiesInMetaModel[mm]:           # for each entity of that meta-model
             if self.ASGroot.listNodes[entity] != []:           # if we do not have any...
                MetaModels2Leave.append(mm)                     # then we should not erase that metamodel
                break

       trueNames = []                                           # now get the name of the GUI Model that corresponds to this meta-model
       for mm in MetaModels2Leave:
	  for mminfo in self.buttonList:                        # look in buttonList, becasue we have tuples (<frame>, <GUIName>, <MMName>, ...)
	     if type(mminfo) == TupleType:                      # Some other elements of this list are not tuples.
	        mmFile = mminfo[2]                              # get the filename
	        dir, fileName   = os.path.split(mmFile)           
	        mmName = fileName[:len(fileName)-6]             # erase the trailing "_MM.py"
  	        if mmName == mm:
	           trueNames.append(ATOM3String(mminfo[1]))
	           break
       numMM = len(self.openMetaModels.getValue())              # now remove the meta-models, calling self.removeMetaModels
       self.openMetaModels.setValue(trueNames)
       self.removeMetaModels(numMM)
       self.putMetaModelName()
       """
    
    def loadTypes(self, listOfNewTypes):
      """
         Adds the components of the 2nd paramater into self.typeList, wrapping them into an ATOM3TypeInfo and loads them
         in the types dictionary.
         listOfNewTypes is a list of tuples: ( 'user-friendly name', 'class name', tuple-with-parameters, may-edit-model)
      """
      tl = self.typeList.getValue()		        # obtain the list of types...
      for newType in listOfNewTypes:		        # for each tuple in the list...
         obj = ATOM3TypeInfo(self)                      # wrap it into an ATOM3TypeInfo
         ufname, cname, params, medt = newType          # unwrap the tuple
         exec "from "+cname+" import "+cname+"\n"       # Modified 23 Sept 2002
         className = eval(cname)                        # obtain the class name
         objType   = className()                        # create a new type object...
         obj.setValue (newType)                         # sets the value to the component...
         objType.createTypeGraph(self, obj.typeModel)   # create the graph
         tl.append(obj)				        # add the element to the list
         if not newType in self.newTypes:               # add the type in the list of newly added types...
            self.newTypes.append(newType)
         self.types[ufname] = ( eval(cname), tuple(params) )    # Update immediatelly the types dictionary
                                                                # Necessary as other types following this may use this type definition....
         
      # self.fillDictionaryWithTypes()		# call the function to add new types in the dictionary (NO LONGER NECESARRY - 23 Sept 2002)
    
    
    def expandModel(self, unUsed, wx, wy):
       "Opens a new ATOM3 instance to edit the model components"
       x = self.UMLmodel.canvasx (wx)							# convert to canvas coordinate system
       y = self.UMLmodel.canvasy (wy)
       ct = self.find_visible_closest(x, y, self.UMLmodel)
       tags = self.UMLmodel.gettags(ct)
       if tags[1][:4] == "ASG_":
         tags = self.UMLmodel.gettags(ct)
         if tags:
            obj = VisualObj.Tag2ObjMap[tags[0]]
            ma = ATOM3TypeDialog(self, obj.semanticObject, ATOM3TypeDialog.OPEN )                  # edit types...

       self.mode=self.IDLEMODE
       

    def fillDictionaryWithTypes(self):
       "Given an ATOM3List of ATOM3TypeInfo, extracts each object and fills a dictionary"
       objList = self.typeList.getValue()			       			# retrieve the list of ATOM3TypeList's
       for obj in objList:
          name, strClassName, strParams, mayEditModel = obj.getValue()                                # (Name, className, (param1, param2,...))
          realParams = []								# Form the list of parameters
          for param in strParams:							# for each ATOM3String parameter
             stringParam = param.toString()
             rp = eval(stringParam)     						# de-Stringize
             realParams.append(rp)							# append to the list
          # first import the library
          exec "from "+strClassName+" import "+strClassName+"\n"
          self.types[name] = ( eval(strClassName), tuple(realParams) )              	# for the dictionary entry

       

    def editEntity(self, unUsed, wx, wy):
       "check the type of entity that we have to edit and do it"
       x = self.UMLmodel.canvasx (wx)							# convert to canvas coordinate system
       y = self.UMLmodel.canvasy (wy)
       ct = self.find_visible_closest(x, y, self.UMLmodel)
       tags = self.UMLmodel.gettags(ct)
       if tags and tags[0] != 'current':                 # i.e. we don't have a connection
          self.editclass( x, y)
       self.mode=self.IDLEMODE
      

    def find_closest_connector(self, x, y):
       """
          Finds the closest connctor to the coordinate (x, y). Returns the handle of this connector or -1 if there is not any.
       """
       import math
       connectors = self.UMLmodel.find_withtag("connector")						# get tuple with all the connectors
       maxDistance, minconnector = 10000, -1
       for connector in connectors:									# iterate to look for the closest
	  coords = self.UMLmodel.coords(connector)							# get an n-tuple with the coordinates of connector
	  distance = math.sqrt((x-coords[0])*(x-coords[0])+(y-coords[1])*(y-coords[1]))			# get the distance to 2 first coordinates (connectors are just a point)
	  if distance < maxDistance:
	     maxDistance  = distance
	     minconnector = connector
       return minconnector


       
    def __buttonsNeeded(self, buttonsTuple):
       """
          Returns true if the buttons are needed (the ASGroot is the meta-model the buttons represent or has
          a merged graph).
          Added 12 Nov. 2002
       """
       fileName = buttonsTuple[2]           # get the fileName <ddd>/<xxx>_MM
       if self.ASGroot:
          fName = self.ASGroot.metaModelName+"_MM.py"
          if string.find(fileName, fName) != -1: return -1
       for merged in self.ASGroot.mergedASG:
          fName = merged.metaModelName+"_MM.py"
          if string.find(fileName, fName) != -1: return -1         
       return 0

    def clearModel(self, showDialog = True ):
      "Clears the current model"
       
      doClean = 1
      st, fl = self.statusbar.getState(StatusBar.MODEL)
      if( showDialog and st == StatusBar.MODIFIED ):
            if tkMessageBox.askyesno(
                "Model has changed...",
                "Are you sure you want to clean the canvas?",
                parent = self
            ) == 0:
              doClean = 0
      if( doClean and self.ASGroot ):
          self.ASGroot.removeContents(self, 1)
          self.statusbar.event(StatusBar.MODEL, StatusBar.CLEAR, "Nonamed")
          if self.console: self.console.appendText('Clearing model')
         

    def globalPrecondition(self, whichRoot = None ):
       """
          Evaluates a global precondition, on CREATE. This method is usually called while a model is being loaded.
          This API is intended to make such models more readable
       """
       if whichRoot == None:                                    # By default evaluate the preCondition on the ASGroot...
           root = self.ASGroot
       else:
           root = whichRoot                                     # Unless another 'root' node is passed
       res= root.preCondition(ASG.CREATE)
       if res:
          self.constraintViolation(res)
          self.mode=self.IDLEMODE
          return

    def globalAndLocalPostcondition(self, node, whichRoot = None):
       """
          Evaluates a global and local postcondition, on CREATE. This method is usually called while a model is being loaded.
          This API is intended to make such models more readable
       """
              
       if whichRoot == None:     # By default evaluate the preCondition on the ASGroot...
          root = self.ASGroot
       else:
          root = whichRoot      # Unless another 'root' node is passed
       res=  root.postCondition(ASG.CREATE)
       if res:
          self.constraintViolation(res)
          self.mode=self.IDLEMODE
          return
       
       res=  node.postCondition(ASG.CREATE)
       if res:
          self.constraintViolation(res)
          self.mode=self.IDLEMODE
          return
        
       # Hacked in by Denis, 2005
       #node.postAction(ASG.CREATE)
       
    def editDialogIsOpen( self, errorString ):
      """ Most transformation methods assume that no GG editing dialog is
      not open when they are executed """
      if( self.inGGeditDialog ):
        tkMessageBox.showerror( "Failed to "+errorString+"       ",
                  "Please close the GG editing dialog first", parent = self )
        return True
      return False
  
    def editTrans(self, statusbarState = StatusBar.MODIFY, name = None ):
       """
          Edits the current graph grammar
       """
       
       if( self.editDialogIsOpen( 'edit transformation' ) ): return          
       
       # Clear out the selections
       self.cb.clearSelectionDict()
       
       # checks if there are some graph grammar being edited...
       if self.EditingGraphGrammar == None:	
          self.EditingGraphGrammar = GraphGrammarEdit(None, self)     # none
       self.inGGeditDialog = True
       ma = ATOM3TypeDialog(self, self.EditingGraphGrammar)	# edit the GG
       if ma.result_ok:
          self.statusbar.event(StatusBar.TRANSFORMATION, statusbarState, 
                               self.EditingGraphGrammar.Name.toString(), name)
       self.inGGeditDialog = False



    def createTrans(self):
       """
          creates and edits a new graph grammar
       """
       self.editTrans( StatusBar.CREATE, "Nonamed")
      

    def genTransDocumentation(self, editAfter=True):
      """ Generates documentation in latex/text form for the graph grammar """
      
      # An open GG editing dialog somehow throws a monkey wrench so destroy it
      if( self.editDialogIsOpen( 'gen transformation documentation' ) ): return   
                         
      if not self.EditingGraphGrammar:
          tkMessageBox.showerror(
              "Couldn't generate documentation!",
              "There is no transformation loaded",
              parent = self
          )
          return
      
      initFile = self.statusbar.getState(StatusBar.TRANSFORMATION)[1][1] 
      if( initFile[-10:] == '_GG_mdl.py' ): initFile = initFile[:-10]
      print initFile
      try:
        fileName = tkFileDialog.asksaveasfilename(
                      title="Choose documentation directory",
                      initialfile=initFile,
                      filetypes=[("All files","*")], 
                      initialdir=self.initialDirectoryDict[ 'Documentation' ])
      except:
        fileName = tkFileDialog.asksaveasfilename(
                      title="Choose documentation directory",
                      filetypes=[("All files","*")], 
                      initialdir=self.initialDirectoryDict[ 'Documentation' ])
      if( fileName == '' ): return
      self.initialDirectoryDict[ 'Documentation' ] = os.path.split(fileName)[0]
      # Save the Graph Grammar model too, just to be safe
      self.saveTrans( saveAsFile = os.path.splitext( fileName )[0] )
      self.EditingGraphGrammar.documentGrammar(fileName)
      
      if(editAfter):
        self.editTrans()



    def genCode4Trans(self, editAfter=True):
      """
          Generates code for the current graph grammar
      """
      
      if( self.editDialogIsOpen( 'save transformation' ) ): return   
       
      if not self.EditingGraphGrammar:
          tkMessageBox.showerror(
              "Couldn't generate code!",
              "There is no transformation loaded",
              parent = self
          )
          return
        
      def doCodeGen():
        # Call the object's code-generating method
        if self.console: 
          self.console.appendText('Generating code for transformation '
                                  +self.EditingGraphGrammar.Name.toString())                                  
        self.EditingGraphGrammar.genCode()		

      def dialogThenCodeGen( initialDir ):
        oldCodeGenDir = self.codeGenDir
        
        try:          
          self.codeGenDir = tkFileDialog.asksaveasfilename(
                     title="Save generated code files to...",
                     initialfile=self.EditingGraphGrammar.Name.toString()+'_GG_exec.py',
                     filetypes = [('Only directory needed','*')],
                     initialdir=initialDir)	
        except:
          self.codeGenDir = tkFileDialog.askopenfilename(filetypes=[
                       ("Pick any file in directory", "*")],
                       title="Code generation directory",
                       initialdir=initialDir)
     
        if( self.codeGenDir):  
           self.codeGenDir = os.path.split( self.codeGenDir)[0] 
                     
        # File dialog was *NOT* cancelled
        if( self.codeGenDir):  
          doCodeGen()
          
        self.codeGenDir = oldCodeGenDir
      
      myText  = 'In which directory shall the code be generated?\n\n' \
                + 'Note: *ANY* directory will work\n\n' \
                + 'Code generation directory (set in AToM3 options): ' \
                + self.codeGenDir + '\n\n'
            
      dialog = Dialog.Dialog(None, {'title': 'Code Generation',
                  'text': myText,
                  'bitmap': '',
                  'default': 1,
                  'strings': ('Code Gen. Dir', 'User Models',
                              'User Formalisms','Central Models', 
                              'Central Formalisms','Cancel')})
          
      # Set Code Gen. Dir to the current Model Dir.
      if( dialog.num == 0 ):  
        doCodeGen()
      elif( dialog.num == 1 ):  
        dialogThenCodeGen(USER_MODEL_PATH)
      elif( dialog.num == 2 ):
        dialogThenCodeGen(USER_MMODEL_PATH)
      elif( dialog.num == 3 ):  
        dialogThenCodeGen(MODEL_PATH)
      elif( dialog.num == 4 ):
        dialogThenCodeGen(META_MODEL_PATH)
      else:
        return
      
      if(editAfter):
        self.editTrans()    
           
        
    def saveTrans(self, saveAsFile = None, editAfter=True ):
      """
      Saves a transformation in a file, 
      in a similar way as saving a regular model
      Updated January 26, 2005 by Denis
      """    
      if( self.editDialogIsOpen( 'save transformation' ) ): return   
          
      # Check if the transformation already has a name
      if( saveAsFile ):  
        fileName = None
        showDialog = False
      else:
        fileName = self.statusbar.getState(StatusBar.TRANSFORMATION)[1][1] 
        showDialog = True
      
      # If the fileName is known, then offer to overwrite previous trans
      if( fileName and (fileName != "Nonamed") ):
        saveDialog = Dialog.Dialog(None, {'title': 'Save Transformation',
                    'text':
                    'Overwrite the previous transformation "' \
                    +str(fileName)+'" ?',
                    'bitmap': '',
                    'default': 0,
                    'strings': ('Overwrite','Save as dialog')})
        if( saveDialog.num == 0 ):
          showDialog = False
      
      # Save As Dialog
      if( showDialog ):        
        # Choose an initialdir for the file dialog
        if( self.initialDirectoryDict[ 'OpenSaveTrans' ] ):
          initialdir = self.initialDirectoryDict[ 'OpenSaveTrans' ]
        else:
          initialdir = self.initialDirectoryDict[ 'OpenSaveModel' ]
              
        fileName = tkFileDialog.asksaveasfilename(
                filetypes=[("All files","*"),("GraphGrammar models", "*_GG_mdl.py")], 
                initialdir=initialdir )	
      
      if( saveAsFile ): fileName = saveAsFile
      if( not fileName): return   # File dialog was cancelled               	
      setCursor( self.parent, 'Busy' )

      # Python source code must have always have its .py extension...
      if( fileName[-3:] != '.py' ):  fileName += '.py'   
      
      # Easy identification of Transformation
      if(  not re.search( '\w*_GG_mdl', fileName ) ):
        fileName = os.path.splitext( fileName )[0] #string.split( fileName, '.' )[0]
        fileName += '_GG_mdl.py'
      
      # See if file exists:
      if os.path.exists(fileName):        # File exists!!          
        # see if back already exists...
        backupFilename = fileName + ".back"
        if os.path.exists( backupFilename ):         # backup file exists!!
            os.remove( backupFilename )                 # remove it first
        try:
          os.rename( fileName, backupFilename )
        except:
          tkMessageBox.showerror( "Failed to backup file!          \n",
                                 fileName + "\nAborting...", parent = self )
          return
      file = open(fileName, "w+t")          # Open file
      
          
      # import the subclass ...
      file.write('from GraphGrammarEdit import *\n')   # generate imports...
      file.write('from GGruleEdit import *\n\n')
      file.write('def savedTrans(self):\n')      # create a method called 'savedTrans'
      try:
        self.EditingGraphGrammar.writeConstructor2File(file, "   ", "self.EditingGraphGrammar", 0,  0) # call the method to generate the constructor...          									
      except:
        print "Failed to generate code! Restarting AToM3 recommended"
        tkMessageBox.showerror( "Failed to generate code!          \n",
                                "Restarting AToM3 recommended", parent = self )
      file.write('\n\n')
      file.close()
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.SAVE, None, fileName )
      transName = self.statusbar.getState(StatusBar.TRANSFORMATION)[1][0]
      if self.console: self.console.appendText('Saving transformation '+transName+' into file '+fileName)

      # Save the directory for next Open or Save operation
      self.initialDirectoryDict[ 'OpenSaveTrans' ] = os.path.dirname( fileName )
      setCursor( self.parent, 'Default' )

      if(editAfter):
        self.editTrans()
        
        
    
    def loadTrans(self, editAfterLoading=True):
      """
      Loads a transformation for editing.
      In the future, this must be the same as opening a model.
      """
      
      if( self.editDialogIsOpen( 'load transformation' ) ): return   
      
      # Choose an initialdir for the file dialog
      if( self.initialDirectoryDict[ 'OpenSaveTrans' ] ):
        initialdir = self.initialDirectoryDict[ 'OpenSaveTrans' ]
      else:
        initialdir = self.initialDirectoryDict[ 'OpenSaveModel' ]
               
      text = "Please choose the starting directory for the file dialog\n"
      text += "Last/Default dir is: " + initialdir
      openDialog = Dialog.Dialog(None, {'title': 'Opening Model',
                  'text': text,
                  'bitmap': '',
                  'default': 0,
                  'strings': ('Central Models','Central Formalisms','Last/Default',
                                'User Models','User Formalisms','Cancel')})
      if( openDialog.num == 0 ):
        initialDir = MODEL_PATH
      elif( openDialog.num == 1 ):
        initialDir = META_MODEL_PATH
      elif( openDialog.num == 2 ):
        initialDir = initialdir
      elif( openDialog.num == 3 ):
        initialDir = USER_MODEL_PATH
      elif( openDialog.num == 4 ):
        initialDir = USER_MMODEL_PATH
      else:
        return
                          
      fileName = tkFileDialog.askopenfilename(filetypes=[
                  ("GraphGrammar models", "*_GG_mdl.py"),("Python files", "*.py")],
                  initialdir=initialDir)	
      # File dialog was cancelled
      if( not fileName):   return   
           
      # Check if the file actually exists
      if( not os.path.exists( fileName ) ):  
        tkMessageBox.showerror( "File Not Found          ",
                                "ATOM3.loadTrans() could not find:\n\n" + fileName,
                                parent = self )
        return    
           
      # Save the directory for next Open or Save operation
      self.initialDirectoryDict[ 'OpenSaveTrans' ] = os.path.dirname( fileName )
        

      dir, file   = os.path.split(fileName)		# Split path and file name
      className   = string.split (file, ".")	# Separate file name and extension
      
      # No className? Doh
      if not className[0]: return							
        
      # Load the dir in memory and import the file
      self.isLoadingModel = True
      self.checkInSearchPath(dir)
      exec "from "+className[0]+" import *\n" in self.__dict__, self.__dict__	
      
            
      try:
        self.savedTrans(self)      # call method to load data
        self.isLoadingModel = False
      except AttributeError:
        tkMessageBox.showerror(
        "Couldn't load transformation! (AttributeError)",
        "Selected file "+file+" does not contain a valid transformation",
        parent = self
        )
        self.isLoadingModel = False
        raise
        #raise Exception, "Transformation load failed due to 'AttributeError'"

      except TypeError:
        tkMessageBox.showerror(
          "Couldn't load transformation! (TypeError)",
          "Selected file "+file+" does not contain a valid transformation",
          parent = self
        )
        self.isLoadingModel = False
        raise Exception, "Transformation load failed due to 'TypeError'"
      else:
        self.isLoadingModel = False
        transName = self.EditingGraphGrammar.Name.toString()
        self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.LOAD, transName, fileName )
        if self.console: self.console.appendText('Loading transformation '+transName+' from file '+fileName)
        
      if(editAfterLoading):
        self.editTrans()
      


    def executeTrans(self):
      """
      Loads an executable Graph Grammar and executes it on the actual graph...
      """
      
      
      if not self.coupledGG:
        self.coupledGG = GrammarExecution(self)
      exeT = ATOM3TypeDialog(self, self.coupledGG )
      
      if exeT.result_ok:						# OK pressed...
        # Get the attributes values
        graphGrammars, stepByStep, entitiesMove, animate, execution = self.coupledGG.getValue() 
      else: return
      
      t = time.time() 
      self.GraphGrammars = []       # Empty the list of loaded Graph Grammars
      
      for gg in graphGrammars:			# For each Graph Grammar
          fileName, directory = gg.getValue()
          # separate file name and extension
          className   = string.split (fileName, ".")
                                                	
          # Import the selected file...      
          if className[0]:			   # if successful...
            self.checkInSearchPath(directory)
            # first check if it has been loaded before, to force a recompilation
            if className[0] in sys.modules.keys():  # file has already been loaded
              
              text = "This GraphGrammar already exists in memory!\n\n"
              text += 'If you have modified the GG, and do not flush the old'
              text += ' GG, you will be executing the old GG'
              openDialog = Dialog.Dialog(None, {'title': 'WARNING',
                          'text': text,
                          'bitmap': '',
                          'default': 0,
                          'strings': ('Proceed','Flush GG from memory',
                                      'Cancel')})
              if(openDialog.num == 2): 
                return
              elif(openDialog.num == 1):
                # This is the existing graph grammar in memory, kill the rules
                # that it will have imported, as well as the GG itself.
                GG = sys.modules[className[0]] 
                if( hasattr( GG, 'importedModules') ):
                  for iModule in GG.importedModules:
                    del sys.modules[iModule]
                del sys.modules[className[0]]		      # delete to force a reload
              else:
                # Already in memory, just re-use it                       
                self.GraphGrammars.append(self.name2GGdict[className[0]])  
                continue
   
            # Now the GG is loaded into memory
            exec "from "+className[0]+" import *\n"	# import the file name
            try:
              GG = eval(className[0])(self)         # create an instance of the last GG loaded
            except NameError:
              tkMessageBox.showerror(
                "Couldn't execute transformation! (NameError)",
                "Selected file "+fileName+" does not contain a valid transformation",
                parent = self
              )
              GG = eval(className[0])(self)  # Give the actual run-time error
              return
            except TypeError:
              tkMessageBox.showerror(
                "Couldn't execute transformation! (TypeError)",
                "Selected file "+fileName+" does not contain a valid transformation",
                parent = self
              )
              GG = eval(className[0])(self)  # Give the actual run-time error
              return
            if self.console: self.console.appendText('Executing transformation '+GG.__class__.__name__)
            self.GraphGrammars.append(GG)						# append it to the list
            self.name2GGdict[className[0]] = GG   
      
      self.grs = GraphRewritingSys(self, self.GraphGrammars, self.ASGroot)		# create a new rewriting system
      self.grs.evaluate(stepByStep[1], entitiesMove[1], execution[1], self.genGraphics, animate[1])# evaluate the GG using the current graph
      self.closeUnusedMetaModels()                       # Modified 09 Sep 2002 by JL
      if( PRINT_TIME_INFO ): 
        print "GG loaded in:          %.3f seconds\n" % ( time.time() - t )
   

    
    def closeDialog (self, unused, eventx, eventy):
       ct              = self.find_visible_closest(eventx, eventy, self.UMLmodel) 	        # find the closest thing
       tags            = self.UMLmodel.gettags(ct)              				# get the tags
       if tags:
          if len(tags) >= 2 and tags[1][:4] == 'ASG_':          				# it's an embedded model
             # open an instance of ATOM3 to select the entity to connect to
             obj = VisualObj.Tag2ObjMap[tags[0]]						# get the graphical object
             ma = ATOM3TypeDialog(self, obj.semanticObject, ATOM3TypeDialog.OPEN, ( None, self.setConnectMode))
          elif tags[0][:3] == 'Obj':                						# then it's a class
             if self.ATOM3parent.fromClass and self.ATOM3parent.toClass:			# it is the 2nd one
                self.ATOM3parent.sem_objTo = VisualObj.Tag2ObjMap[tags[0]].semanticObject  	# get the semantic object
             else:										# it is the 1st one
                self.ATOM3parent.sem_objFrom = VisualObj.Tag2ObjMap[tags[0]].semanticObject	# get the semantic object

       self.dialogInstance.ok()
       del self.dialogInstance
       del self.ATOM3parent

    def setEditGGLabel (self, AT3Dialog, ATOM3instance, semanticObject):
       "Sets the flag to edit the Graph Grammar Numbering Label conveniently"
       semanticObject.editGGLabel = self.editGGLabel
      
    
    def checkCardinalities(self, objFrom, objTo):
       """
          Before connecting these two objects, check if the connection is valid. If it is valid, it returns None, if invalid, returns a
          tuple with the error. The 1st component of the tuple is the error message, the second one is the actual object (to be highlighted)
       """
       classFrom, classTo = objFrom.__class__.__name__, objTo.__class__.__name__
   
       cardinality1 = self.CardinalityTable[classFrom][classTo]						# get cardinality info
       cardinality2 = self.CardinalityTable[classTo][classFrom]						# get cardinality info
       if cardinality1 == [] or cardinality2 == []:							# if something is missing, then raise an error
          return ("Objects of types "+classFrom+" and "+classTo+" cannot be connected.", objFrom)

       card1 = self.checkDirectionOfCardinality(cardinality1, "Source")					# Check that the direction of connection is allowed
       if not card1:
          if objFrom.keyword_:
	     return ("Wrong connection direction for object: "+objFrom.keyword_.toString(), objFrom)
	  else:
	     return ("Wrong connection direction for source object.", objFrom)	

       numObjects1 = self.countObjectOfClass(objFrom.out_connections_, objTo.__class__.__name__)
       min1, max1 = self.getCardinalityValues(card1)
       if numObjects1 > max1:
          if objFrom.keyword_:
	     return ("Too many objects of type "+classTo+" connected to "+objFrom.keyword_.toString(), objFrom)
	  else:
             return ("Too many objects of type "+classTo+" connected to source object", objFrom)

       card2 = self.checkDirectionOfCardinality(cardinality2, "Destination")                            # Check that the direction of connection is allowed
       if not card2:
          if objTo.keyword_:
	     return ("Wrong connection direction for object: "+objTo.keyword_.toString(), objTo)
	  else:
	     return ("Wrong connection direction for destination object.", objTo)	

       numObjects2 = self.countObjectOfClass(objTo.in_connections_, objFrom.__class__.__name__)
       min2, max2 = self.getCardinalityValues(card2)
       if numObjects2 > max2:
          if objTo.keyword_:
	     return ("Too many objects of type "+classFrom+" connected to "+objTo.keyword_.toString(), objTo)
	  else:
             return ("Too many objects of type "+classFrom+" connected to source object", objTo)
       return None

    def getCardinalityValues (self, cardinality ):
       """
          gets the numeric values of the cardinality tuple
       """
       if cardinality[0] in ["n", "N", "m", "M"]: min = 1000000
       else: min = int(cardinality[0])
       if cardinality[1] in ["n", "N", "m", "M"]: max = 1000000
       else: max = int(cardinality[1])
       return (min, max)

    def hardCardinalityCheck(self, node):
       """
          Performs a cardinality check of node 'node'. If the check is not passed, then a tuple with the error is returned, else None.
       """
       entities = self.CardinalityTable.keys()				# Get the type of nodes we will have to check...
       nodeClass= node.getClass()					# Get node's class name
       for entity in entities:
          if entity in self.CardinalityTable[nodeClass].keys():
            cards = self.CardinalityTable[nodeClass][entity]		# Get cardinalities to check.
            for card in cards:
                if card[2] == "Source": theList = node.out_connections_
                else: theList = node.in_connections_
                numObjects = self.countObjectOfClass(theList, entity)
                min, max = self.getCardinalityValues ( card )
                if numObjects < min:
                   if node.keyword_:
  	              return ("Too few objects of type "+entity+" connected to "+node.keyword_.toString()+"("+str(min)+" are needed)", node)
  	           else:
                      return ("Too few objects of type "+entity+" connected to source object ("+str(min)+" are needed)", node)
                elif numObjects > max:
                   if node.keyword_:
  	              return ("Too many objects of type "+entity+" connected to "+node.keyword_.toString()+"( "+str(max)+" is the maximum)", node)
	           else:
                      return ("Too many objects of type "+entity+" connected to source object ( "+str(max)+" is the maximum)", node)
       return None

    def checkModel(self):
       """
          Iterates over all the objects of the model, performing a hard cardinality check.
       """
       for nodeType in self.ASGroot.listNodes.keys():
          for object in self.ASGroot.listNodes[nodeType]:
             res = self.hardCardinalityCheck(object)				# perform a 'hard' cardinality check...
             if res: return res
       return None

    def countObjectOfClass(self, objectList, className):
       """
          Count the number of objects of class 'className' that there are in objectList
       """
       counter = 0
       for obj in objectList:
          if obj.getClass() == className: counter = counter + 1
       return counter

    def checkDirectionOfCardinality(self, cardInfo, direction):
       """
          cardInfo is a list of tuples with a connection information: (min, max, 'direction'). Tries to find a tuple that has the
          direction 'direction'.
       """
       card1 = None
       for card in cardInfo:									# look for source information for objFrom
          if card[2] == direction:
            card1 = card
            break
       return card1

    def deleteGraphicalConnections(self, node):
       "deletes graphical connections of the given entity"
       obj = node.graphObject_
       obj.erase(self) # Modified Aug 9, 2005 by Denis Dube
#       while obj.connections != []:
#            c = obj.connections[0]
#            obj.connections.remove(c)
#            self.UMLmodel.delete(c[0])
       return obj

    def showGraphicalConnections(self, node):
      "Given the node 'node', shows its connections (none of them must be visible!)"
      for conObject in node.in_connections_:
         if node.graphObject_.hasGraphicalConnection(conObject.graphObject_) < 0:	# no connections between them...
            self.fromClass = conObject.graphObject_.tag
            self.toClass   = node.graphObject_.tag
            self.showConnection(conObject.graphObject_.tag, node.graphObject_.tag)
            self.fromClass = None
            self.toClass   = None
      for conObject in node.out_connections_:
         if node.graphObject_.hasGraphicalConnection(conObject.graphObject_) < 0:	# no connections between them...
            self.fromClass = node.graphObject_.tag
            self.toClass   = conObject.graphObject_.tag
            self.showConnection(node.graphObject_.tag, conObject.graphObject_.tag)
            self.fromClass = None
            self.toClass   = None


    def deleteGraphicsOfSemanticEntity (self, node):
       "deletes the corresponding graphic entity of the given node"
       obj = self.deleteGraphicalConnections(node)
       cts = self.UMLmodel.find_withtag(obj.tag)
       for c in cts: self.UMLmodel.delete(c)

    def getConnectedEntities (self, grHandler):
       "Returns a tuple with the semantic entities connected by grHandler"
       source, destination = None, None
       for nt in self.ASGroot.listNodes.keys():
          for node in self.ASGroot.listNodes[nt]:
             if node.graphObject_:                                              # if node has graphical Object
                htuple = node.graphObject_.hasConnectHandler(grHandler)         # see if the object has this handler
                if htuple:                  
                   if htuple[1] == 0: source = node
                   else: destination = node
       return (source, destination)




    def deleteConnection(self, handler, tag):
       """
       Deletes the connection given by handler, 
       invoking the corresponding pre and post action
       -Modified by Denis to take hyperedges into full account
       """
       obj = VisualObj.Tag2ObjMap[tag]    # obtain the visual object
       connSemantic = obj.semanticObject  # obtain the semantic object
       
       # Preconditions 
       # Root
       res = self.ASGroot.preCondition(ASGNode.DISCONNECT)
       if res:
          self.constraintViolation(res)
          return
        
       # Connnection
       res = connSemantic.preCondition(ASGNode.DISCONNECT)
       if res:
          self.constraintViolation(res)
          return

       sourceList = connSemantic.in_connections_
       destinationList = connSemantic.out_connections_

       # Sources
       for source in sourceList:		
          for destination in destinationList:	
            res = source.preCondition (ASGNode.DISCONNECT,destination, "SOURCE" )
            if res:
               self.constraintViolation(res)
               return
       # Destinations
       for destination in destinationList:		
          for source in sourceList:		
            res = destination.preCondition (ASGNode.DISCONNECT, source, "DESTINATION")
            if res:
               self.constraintViolation(res)
               return

       # Pre-actions
       # Root
       self.ASGroot.preAction(ASGNode.DISCONNECT)       
       # Connection
       connSemantic.preAction(ASGNode.DISCONNECT)       
       # Sources & Destinations
       for source in sourceList:		
          for destination in destinationList:	
            source.preAction(ASGNode.DISCONNECT, destination, "SOURCE")
       for destination in destinationList:		
          for source in sourceList:	
            destination.preAction(ASGNode.DISCONNECT, source, "DESTINATION")

       #
       # Now check if we have to erase it from a named port (added 7 Oct 2002)
       #

       namedPort_Source = None
       namedPort_Destination = None
       for source in sourceList:
         namedPort_Source = source.graphObject_.getNamedPort(handler)
         if namedPort_Source:
           if(obj.semanticObject in source.getAttrValue(namedPort_Source)):
            source.getAttrValue(namedPort_Source).remove(obj.semanticObject)
           else:
             print 'WARNING (deleteConnection): Remove source failed', __file__
       for destination in destinationList:
         namedPort_Destination = destination.graphObject_.getNamedPort(handler)
         if namedPort_Destination:
           if(obj.semanticObject in destination.getAttrValue(namedPort_Destination)):
            destination.getAttrValue(namedPort_Destination).remove(obj.semanticObject)
           else:
             print 'WARNING destination.getAttrValue(namedPort_Destination): Remove destination failed', __file__

       #
       # End named port processing...
       #
       
       # Delete graphical and semantic connections
       link_removed = obj.removeConnection(self, handler)
       
       # This is needed when deleting hyperedges
       for source in sourceList:		
          for destination in destinationList:	
             if( source != None and source.graphObject_ != None and
                issubclass( destination.graphObject_.__class__, graphLink )  ):
               source.graphObject_.removeConnection(self, handler)  
       if( obj.centerObject and VisualObj.Tag2ObjMap.has_key( obj.centerObject.tag ) ):
        self.deleteRealEntity( obj.centerObject.tag )
        
       for destination in destinationList:
         destination.graphObject_.removeConnection(self, handler)   # may be destination is None (an unconnected connection)
       
       for source in sourceList:
         for destination in destinationList:
           self.deleteSemConnection( [source, destination] )
   
       if link_removed == 2:		  # a 2 means that the whole link has been removed
         obj.semanticObject.removeNode()

       # Post Conditions
       res = self.ASGroot.postCondition (ASGNode.DISCONNECT)
       if res:
          self.constraintViolation(res)
          return
        
       res = connSemantic.postCondition (ASGNode.DISCONNECT)
       if res:
          self.constraintViolation(res)
          return

       for source in sourceList:		
          for destination in destinationList:	
            res = source.postCondition (ASGNode.DISCONNECT,destination, "SOURCE" )
            if res:
               self.constraintViolation(res)
               return

       for destination in destinationList:		
          for source in sourceList:	
            res = destination.postCondition (ASGNode.DISCONNECT, source, "DESTINATION")
            if res:
               self.constraintViolation(res)
               return

       # Disconnect root, connection, source, destination POST ACTIONS
       self.ASGroot.postAction(ASGNode.DISCONNECT)
       
       for source in sourceList:		
          for destination in destinationList:	
            #print 'source', source.__class__.__name__, 'disconnect'
            source.postAction(ASGNode.DISCONNECT, destination, "SOURCE")
            connSemantic.postAction(ASGNode.DISCONNECT, destination, "SOURCE")
       for destination in destinationList:		
          for source in sourceList:	
            #print 'destination', destination.__class__.__name__, 'disconnect'
            destination.postAction(ASGNode.DISCONNECT, source, "DESTINATION")
            connSemantic.postAction(ASGNode.DISCONNECT, source, "DESTINATION")

#================================================================================
#Hierarchical structure maintenance, see HierarchicalASGNode.py for more info
#================================================================================
       if(connSemantic.isHierarchicalLink()):
         for parent in sourceList :
           parent._delHierChildrenList(destinationList)
         for child in destinationList:
           child._delHierParent()
           

    def deleteSemConnection (self, objects):
       """ delete the connections from the semantic entities..."""
       if( objects[0] == None or objects[1] == None ):
          print "\nWARNING: Nothing to delete! Atom3.deleteSemConnection() ", objects
          return
    
       # Unary relations: both ends of connection are the same object
       if( not objects[0]) :                                             
          objects[0] = objects[1]                                        
       elif( not objects[1] ):
          objects[1] = objects[0]
          
       # Remove 1 from 0's outgoing connections
       if( objects[1] in objects[0].out_connections_ ): 
        objects[0].out_connections_.remove(objects[1])
       # Remove 0 from 1's incomming connections
       if( objects[0] in objects[1].in_connections_ ):  
        objects[1].in_connections_.remove(objects[0])
       self.mode = self.IDLEMODE

    def changeMode (self, event):
       """
          Changes the mode (the user clicked in a button created on the fly).
          If the mode ends with "&&EXEC" then it is not a drawing mode and the method should be executed right away (Added 27 July 2002, JL)
       """

       self.mode = self.modes[event.widget]
       if find (self.mode, "&&EXEC") > -1:            # ey, not a drawing mode... (Added 27 July 2002, JL)
          action = self.mode
          self.mode = self.IDLEMODE                   # set back to idle mode
          self.userActionsMap[action](self, 0, 0)     # in this case, no information about the click coordinates         

       
    def newModeModel(self):
       """
          enters in the INSERTModel mode
       """      
       self.mode = self.INSERTModel

    def expandModeModel(self):
       """
          enters in the EXPANDModel mode
       """            
       self.mode = self.EXPANDModel


    def highLightGraphs(self, graphList, flag = True):
      """
         highlights all the graphs contained in the list for the user to select one.
         - graphList: is a list of graphs. A graph is a tuple ( <id>, [nodes]). Where id is an integer and
         [nodes] is a list of nodes. Enters in the mode SELECTgraph
      """      
      self.graphs2select = graphList				# save the list, because, we'll have to wait for the user to click on some node
      self.highLightNodesInGraphs(self.graphs2select, flag)	# Highlight each node
      self.mode = self.SELECTgraph				# put system in select graph mode

    def selectGraph(self, unUsed, wx, wy):
      """This function is called when the user clicks on canvas and the mode is SELECTgraph"""
      x, y = self.UMLmodel.canvasx(wx), self.UMLmodel.canvasy(wy)	# convert to canvas coordinate system
      ct = self.find_visible_closest(x, y, self.UMLmodel)
      tags = self.UMLmodel.gettags(ct)
      if tags and tags[0] != 'current':                 		# i.e. we don't have a connection
        obj = VisualObj.Tag2ObjMap[tags[0]].semanticObject		# get semanticObject
        # Now look for the graph whose node have been clicked
        for graphTuple in self.graphs2select:
          id, graph = graphTuple					# unwrap graph information
          if obj in graph:          					# ey, we've found the subraph that's been clicked   	
            self.mode = self.IDLEMODE				# only if the clicked node belongs to some graph return to IDLE state
            self.highLightNodesInGraphs(self.graphs2select, 0)	# un-Highlight each node          	
            self.grs.executeRule(graphTuple)			# execute the rule that's been selected
            self.graphs2select = []
            return
              
    def highLightNodesInGraphs(self, graphList, flag):
      """
         Highlights (flag = 1) or LowLights (flag = 0) all the VISIBLE elements with the 'selected' tag.
         - graphList: is a list of tuples (id,[node])
      """
      highLighted = []						# list of highlighted nodes (do not highlight them twice, or we'll lost their color)
      for grp in graphList:     				# for each graph
         id, graph = grp
         for node in graph:
            if not node in highLighted:				# if not highlighted yet, do it
               node.graphObject_.HighLight( flag)
               highLighted.append(node)

    def __isItemVisible (self, itemHandler, canvas ):
      """
         Returns 1 if the item is visible, 0 otherwise
      """
#      itemtype = canvas.type(item)
#      if( itemtype == 'image' ): return 1
#      elif not itemtype in ['line', 'text']:
#         if (canvas.itemcget(item, "outline" ) in ["", None]) and (canvas.itemcget(item, "fill") in ["", None]): return 0
#         else: return 1
#      else:
#         if canvas.itemcget(item, "fill") in ["", None]: return 0
#         else: return 1
#      return 1
      dc = canvas
      itemtype = dc.type(itemHandler)
     
      # Images
      if(itemtype == 'image'): 
        return True
        
      # Line/Text uses the fill attribute to be visible
      elif(itemtype in ['line', 'text']):
        if(dc.itemcget(itemHandler, "fill") in ["", None]):
          return False
        return True
        
      # Window
      elif(itemtype == 'window'):
        return False
      
      # Anything else: polygon, etc. 
      else:
        if(dc.itemcget(itemHandler, "outline") in ["", None] 
          and dc.itemcget(itemHandler, "fill") in ["", None]): 
          return False
      return True

    
    def __dist ( self, x0, y0, x1, y1 ):
      """
           calculates the distance between 2 points
           Added : 10 July 2002 JL
      """
      return math.sqrt(abs((x0-x1)*(x0-x1)+(y0-y1)*(y0-y1)))

    def __point2Segment ( self, px, py, sx0, sy0, sx1, sy1):
      """
         calculates distance from a point to a segment. I use the algorithm given in:
         http://geometryalgorithms.com/Archive/algorithm_0102/algorithm_0102.htm
         Added : 10 July 2002 JL
      """

      def dot ( w, v):
        """
           calculates the dot product of two vectors
        """
        return w[0]*v[0]+w[1]*v[1]
     
      v = (sx1 - sx0, sy1 - sy0)    # v = s[1]-[s0]
      w = (px - sx0, py - sy0)      # w = P-s[0]

      c1 = dot(w,v)
      if ( c1 <= 0 ): return self.__dist(px, py, sx0, sy0)

      c2 = dot(v,v)
      if ( c2 <= c1 ): return self.__dist(px, py, sx1, sy1)

      b = c1 / c2
      Pb = sx0 + b * v[0], sy0 + b * v[1]
      return self.__dist(px, py, Pb[0], Pb[1])



    def constraintViolation(self, res):
       """
          A constraint violation has occurred, and a message has to be given. The message is the 1st component
          of the tuple 'res'. The 2nd component is the object to be highlighted.
       """
       if res[1] and (type(res[1])!= StringType):
          if issubclass(res[1].__class__, VisualObj):
            res[1].HighLight(1)
          elif issubclass( res[1].__class__, ASGNode):
            res[1].graphObject_.HighLight(1)

       tkMessageBox.showwarning("constraint violation! ",res[0],parent = self)

       if res[1] and type(res[1])!= StringType:
          if issubclass(res[1].__class__, VisualObj):
            res[1].HighLight(0)
          elif issubclass( res[1].__class__,ASGNode):
            res[1].graphObject_.HighLight(0)
       return 0

    def writeSetValue(self, f, obj, objName, indent, deep = 0):
       """
          writes in the file 'f' the value of obj (an ATOM3Type). The object name must be objName.
          This is a 'visitor' method.
       """
       f.write(indent+objName+"="+obj.getTypeName()+"()\n")					# write the constructor
       if obj.getTypeName() == 'ATOM3String':						# if it is a string, enclose between quotes
          f.write(indent+objName+".setValue('"+str(obj.getValue())+"')\n")
       elif obj.getTypeName() == 'ATOM3List':						# if it is a list
          f.write(indent+"objlist"+str(deep)+" =[]\n")
	  value = obj.getValue()
	  for ob in value:
  	     self.writeSetValue(f, ob, objName+str(deep+1), indent, deep+1)		# write object value
             f.write(indent+"objlist"+str(deep)+".append("+objName+")\n")		
             f.write(indent+objName+".setValue(objlist"+str(deep)+")\n")
          actFlags = obj.getActionFlags()					# get the ATOM3List
          actFlags = actFlags[:3].append(0)						# eliminate the meta-flag
          f.write(indent+objName+".setActionFlags("+str(actFlags)+")\n")

       else:
          f.write(indent+objName+"="+obj.getTypeName()+"()\n")				# write the constructor
          f.write(indent+objName+".setValue("+str(obj.getValue())+")\n")

    def findKeywordAndIcons(self, f, item, counter):
       """Searches for the keyword attribute and icons. Writes the keyword (if any). This ensures that the keyword is written first.
          - f is the file
          - item is an instance of ATOM3Attribute
          - counter: the order of the attribute
          This is a 'visitor' method to be called by visitorOnAttributes, for code generation purposes.
       """
       value = item.getValue()                          # (attrName, typeID, initialValue|None, isKey, directEditing)
       if value[3][1] == 1:				# only write to file if it is the keyword.
          item.initialValue.writeConstructor2File( f, '      ', 'self.'+str(value[0]), 0, 1 )
          f.write('      self.keyword_= self.'+str(value[0])+'\n')
          self.theKeyword = str(value[0])
       if value[1] == "Appearance":			# if it has an attribute of type appearance, write it down. If it has an appearance...
          self.hasAppearance = 1			# ... it must also have a keyword.
       attribType = self.types[str(value[1])][0].__name__
       if attribType == 'ATOM3List':
          if item.initialValue:
             itl = item.initialValue.itemType.__name__				# get the initial value...
             if itl == "ATOM3Appearance":
                self.hasAppearance = 1
             elif itl in ["ATOM3List", "ATOM3Attribute"]:
                items = item.initialValue.getValue()				# get items, and look for 'Appearances'
                for element in items:
               	   if self.findIcon(element): return               	

    def findIcon(self, item):
       """
          Sets the flag 'self.hasAppearance' to 1 if the item is an ATOM3Appearance. Proceeds recursively if the item is an
          ATOM3Attibute or a list. This is an auxiliary method for code generation.
       """
       if item.getTypeName() == "ATOM3Appearance":				# check if it is an appearance...
          self.hasAppearance = 1
          return 1
       elif item.getTypeName() == "ATOM3List":
          theType = item.itemType.__name__					# get the Type...
          if theType == "ATOM3Appearance":
             self.hasAppearance = 1
             return 1
          elif theType in ["ATOM3List", "ATOM3Attribute"]:
             items = item.getValue()						# get items, and look for 'Appearances'
             for element in items:
                 if self.findIcon(element): return 1
             return 0
       elif item.getTypeName() == "ATOM3Attribute":
          if item.initialValue: return self.findIcon(item.initialValue)		# check the initial value
          return 0
       return 0

    def writeCreation(self, f, item, counter):
       """writes in f the statements necessary to create the object. Does not write the keyword, because the previous function was supposed to do it.
          - f is the file
          - item is an instance of ATOM3Attribute
          - counter: the order of the attribute
          These are 'visitor' methods called by visitorOnAttributes for code generation purposes.
       """
       value = item.getValue()                          # (attrName, typeID, initialValue|None, isKey, directEditing)
       if value[1] == 'Port':                           # if it is a Port... (Added by JL, 24 July 2002)
          f.write('      self.'+str(value[0])+' = []\n')
          return
       if value[3][1] != 1:				# only write it if it is not a keyword.
          item.initialValue.writeConstructor2File( f, '      ', 'self.'+str(value[0]), 0, 1 )
       if value[1] == "Appearance":			# if it has an attribute of type appearance, write it down. If it has an appearance...
          self.hasAppearance = 1			# ... it must also have a keyword.

    def writeGeneratedDictionary(self, f, item, counter):
       """
          write in f the contents of the dicitionary of generated attributes.
          These are 'visitor' methods called by visitorOnAttributes for code generation purposes.
       """
       value = item.getValue()
       if value[1] != 'Port':          # Added 24 July 2002 by JL  
         if self.writed == 1:
           f.write(",\n                                  ")          
         f.write( "'"+str(value[0])+"': ('ATOM3"+str(value[1])+"'")
         if value[1] == 'List' and item.initialValue.itemType:        # Added 25 July 2002 by JL
            f.write(", '"+item.initialValue.itemType.__name__+"')")   # Added 25 July 2002 by JL
         else:
           f.write(", )")
         self.writed = 1

    def writeDirectEditingList (self, f, item, counter):
       """
          write in f the contents of the list with the flag that tells if the widget should be edite directly.
          These are 'visitor' methods called by visitorOnAttributes for code generation purposes.
          Added 31 July 2002, by JL.
       """
       value = item.getValue()
       if self.writed == 1: f.write(",")
       f.write( str(value[4][1]) )
       self.writed = 1

    def writeRealOrderList(self, f, item, counter):
       """
          write in f the contents of the list with the order of generated attributes.
          These are 'visitor' methods called by visitorOnAttributes for code generation purposes.
       """
       value = item.getValue()
       if value[1] != 'Port':                           # Added 24 July 2002 by JL     
         if self.writed == 1: f.write(",")
         f.write( "'"+str(value[0])+"'")
         self.writed = 1
   
    def genImport(self, f, item, counter):
       """
          adds in the list importedTypes the necessary types to be imported.
          These are 'visitor' methods called by visitorOnAttributes for code generation purposes.          
       """
       value = item.getValue()
       attribType = self.types[str(value[1])][0].__name__
       if not attribType in self.importedTypes:
          self.importedTypes.append(attribType)
       # if it is a list, import the list' type
       if attribType == 'ATOM3List':
          if item.initialValue:
             itl = item.initialValue.itemType.__name__
             if not itl in self.importedTypes:
                self.importedTypes.append(itl)
             if itl == "ATOM3Attribute":
                self.addAllTypes2List(self.importedTypes)
             elif itl == "ATOM3List":
                # no look for initial items, and import each one type...
                initialItems = item.initialValue.getValue()			# get a list of items...
                for item in initialItems:
                   self.addItemType2List(item, self.importedTypes)
                if initialItems == []:						# no initial items, so add the default type for lists (attributes)
                   if not "ATOM3Attribute" in self.importedTypes:
                      self.importedTypes.append("ATOM3Attribute")
                      # if it is of type ATOM3Attribute, then add all the available types...
                      self.addAllTypes2List(self.importedTypes)
          else:
             if not "ATOM3Attribute" in self.importedTypes:
                self.importedTypes.append("ATOM3Attribute")
                # if it is of type ATOM3Attribute, then add all the available types...
                self.addAllTypes2List(self.importedTypes)
                
         
    def addAllTypes2List(self, list):
      """
         Auxiliary method for genImport. adds the name of all the available types to the list
      """
      for typeName in self.types.keys():
          tupleType = self.types[typeName]
          name = tupleType[0].__name__
          if not name in list: list.append(name)

    def addItemType2List(self, item, list):
      """
         Auxiliary method for genImport. adds the type of item to the list (if it is not present yet)
      """
      theType = item.getTypeName()
      if not theType in list: list.append(theType)
      if theType == "ATOM3List": 						# check for its initial value, and repeat for each item
         # import the list' type:
         theType = item.itemType.__name__
         if not theType in list: list.append(theType)
      if theType == "ATOM3Attribute" :						# check for it is an Attribute, we have to add each available type...
         self.addAllTypes2List(list)

    def visitorOnAttributes(self, f, UMLobject, function):
       """
          iterates over the attributes of type ATOM3Attribute of the object UMLobject, performing a certain function
       """
       self.writed = 0
       counter = 0 # an auxiliary counter
       for attr in UMLobject.generatedAttributes.keys():
          type = UMLobject.generatedAttributes[attr]					# A tuple with the types...

          if type[0] == 'ATOM3Attribute':
             function(f, UMLobject.getAttrValue(attr), counter)                         # perform function
             counter = counter + 1							# increment counter
          elif type[0] == 'ATOM3List' and type[1] == 'ATOM3Attribute':			# A list of generative elements...
             items = UMLobject.getAttrValue(attr).getValue()                                # obtain a list of generative elements
             for item in items:								# look over the array
                function(f, item, counter)
                counter = counter + 1
       return counter

    def writeActionConstraint (self, file, value, which):
      """
          writes part of the function to evaluate local constraints
          These are 'visitor' methods called by visitorOnConstraints for code generation purposes.                        
      """
      listAct, selAct = value[3]
      listKnd, selKnd = value[2]
       
      # Abort if there's no code...
      tempCode = value[4]
      if(tempCode == None):
          return
      tempCode = tempCode.replace( '\n', '')
      tempCode = tempCode.replace( ' ', '')
      tempCode = tempCode.replace( '\t', '')
      tempCode = tempCode.replace( '\r', '')
      if(len(tempCode) == 0):
        return
       
      if listKnd[selKnd] == which:
          # iterate on the specified event...
          file.write("      if actionID == ")
          conta = 0
          writed = 0
          for event in selAct:
              if event == 1:
                 if not writed:
                    file.write("self."+listAct[conta])
                 else:
                    file.write(" or actionID == self."+listAct[conta])
                 writed = 1
              conta = conta + 1
          file.write(":\n")
          file.write("         res = self."+value[0]+"(params)\n")
          file.write("         if res: return res\n")

    def writeConstraintCode (self, file, value, unUsed):
       """
          writes the constraint code.
          These are 'visitor' methods called by visitorOnAttributes for code generation purposes.                        
       """
       # Abort if there's no code...
       tempCode = value[4]
       if(tempCode == None):
          return
       tempCode = tempCode.replace( '\n', '')
       tempCode = tempCode.replace( ' ', '')
       tempCode = tempCode.replace( '\t', '')
       tempCode = tempCode.replace( '\r', '')
       if(len(tempCode) == 0):
         return
        
       file.write ("   def "+value[0]+"(self, params):\n")
       file.write ("      "+string.replace(value[4],'\n', '\n      '))
       file.write ("\n\n")
     
    def visitorOnConstraints (self, which, file, UMLobject, function ):
       """
          Generates code for the constraints. In a 'visitor' pattern way.
       """
       # find a list of constraints, or a single constraint generator       
       for attr in UMLobject.generatedAttributes.keys():
          type = UMLobject.generatedAttributes[attr]					# A tuple with the types...
          if( type[0] == 'ATOM3Constraint' ):            
             value = UMLobject.getAttrValue(attr).getValue()                                # obtain the value
             function(file, value, which)
          elif( type[0] == 'ATOM3List' and type[1] == 'ATOM3Constraint' ):
               items = UMLobject.getAttrValue(attr).getValue()
               for item in items:
                  value = item.getValue()
                  function(file, value, which)

    def writeDirectionalCheck(self, file, value, counter, direct):
       """
          Generates type checking for the connection direction
          I THINK THIS METHOD IS NOT USED ANY MORE.
       """
       # value is a tuple with (className, direction, minValue, maxValue)
       className, direction, minVal, maxVal = value             # unpack the values
       if direction[1] == direct:                               # check the constraint direction
          if self.writedDirection == 0:                         # if it is the 1st., begin the if
             file.write("         if ")
             self.writedDirection = 1
          else:
             file.write("      and ")
          file.write("( last.getClass()!='"+value[0]+"') ")
   
    def writeObjectTypeCheck(self, file, value, counter):
       """
          Generates the type checking for the connection
          I THINK THIS METHOD IS NOT USED ANY MORE.          
       """
       if counter == 0:				# if it is the first cardinality, add some preliminary code
          file.write("      if selfPosition == 'SOURCE':\n")
          file.write("         last=self.out_connections_[len(self.out_connections_)-1]\n")
          file.write("      else:\n")
          file.write("         last=self.in_connections_[len(self.in_connections_)-1]\n")
          file.write("      if ")
       else:
          file.write(" and ")
       file.write("( last.getClass()!='"+value[0]+"') ")

    def writeSoftCardinalityCheck(self, file, value, counter):
       """
          Generates soft (not taking into account minimum values) cardinality checking
          I THINK THIS METHOD IS NOT USED ANY MORE.          
       """
       # value is a tuple (<objectCLass>, <direction>, <minValue>, <maxValue>)
       objectClass, direction, minValue, maxValue = value					# unpack ATOM3Connection value
       file.write("      counter = 0\n")							# cardinality counter
       if direction[1] == 0:									# From Entity TO relationship
          file.write("      for item in self.in_connections_:\n")				# WE ARE A RELATIONSHIP
       else:
          file.write("      for item in self.out_connections_:\n")
       file.write("         if '"+ objectClass +"'== item.getClass(): counter = counter+1\n")
       if not maxValue in ["n", "N", "m", "M"] :
          file.write("      if counter > "+maxValue+":\n")
          file.write("         return ( 'Number of "+objectClass+" objects exceeded!', '')\n")

    def writeHardCardinalityCheck(self, file, value, counter):
       """
          Generates hard (taking into account minimum values) cardinality checking
          I THINK THIS METHOD IS NOT USED ANY MORE.          
       """
       # value is a tuple (<objectCLass>, <direction>, <minValue>, <maxValue>)
       objectClass, direction, minValue, maxValue = value					# unpack ATOM3Connection value
       file.write("      counter = 0\n")
       if direction[1] == 0:									# From Entity TO relationship
          file.write("      for item in self.in_connections_:\n")				# WE ARE A RELATIONSHIP
       else:
          file.write("      for item in self.out_connections_:\n")
       file.write("         if '"+ objectClass +"'== item.getClass(): counter = counter+1\n")
       if not maxValue in ["n", "N", "m", "M"] :
          file.write("      if counter > "+maxValue+":\n")
          file.write("         return ( 'Number of "+objectClass+" objects exceeded!', '')\n")
       if not minValue in ["n", "N", "m", "M"]:
          file.write("      if counter < "+minValue+":\n")
          file.write("         return ( 'Number of "+objectClass+" objects insuficient("+str(minValue)+" are needed)!', '')\n")
       else:
          file.write("      if counter == 0:\n")
          file.write("         return ( 'Number of "+value[0]+" objects insuficient("+str(minValue)+" are needed)!', '')\n")

    def visitorOnCardinality (self, file, UMLobject, function, param = None ):
       """
          Generates constraints from the cardinality attributes found, in a 'visitor pattern way'
       """       
       counter = 0
       for attr in UMLobject.generatedAttributes.keys():
          type = UMLobject.generatedAttributes[attr]					# A tuple with the types...
          if type[0] == 'ATOM3Connection':            
             value = UMLobject.getAttrValue(attr).getValue()                                # obtain the value
             if param:
                function(file, value, counter, param )
             else:
                function(file, value, counter )
             counter = counter + 1
          elif type[0] == 'ATOM3List' and type[1] == 'ATOM3Connection':
             items = UMLobject.getAttrValue(attr).getValue()
             for item in items:
                value = item.getValue()
                if param != None:
                   function(file, value, counter, param)
                else:
                   function(file, value, counter)
                counter = counter+1
       return counter

    def genASGCode(self, cardConstObjects, ASGroot=None):
       """
          Generates Python code for the ASGroot node
       """      
       if(not ASGroot):
         ASGroot = self.ASGroot

       fileName = "ASG_"+ASGroot.keyword_.toString()+".py"
       if self.console: self.console.appendText('Generating file '+fileName+' in directory '+self.codeGenDir)
       f = open( os.path.join( self.codeGenDir,fileName) , "w+t" )
                            
       f.write('"""\n')
       f.write("__"+ fileName +"_____________________________________________________\n")
       f.write("\n")
       f.write("Automatically generated AToM3 ASGroot node (DO NOT MODIFY DIRECTLY)\n")
       f.write("Author: "+USER_NAME+"\n")
       f.write("Modified: "+time.asctime()+"\n")
       f.write("__"+ len(fileName)*"_" +"_____________________________________________________\n")
       f.write('"""\n')
       f.write("from ASG import *\n")
       f.write("from ATOM3Type       import *\n")
       self.importedTypes = []									# list where the necessary types will be placed
       self.visitorOnAttributes( f, ASGroot, self.genImport)
       # now write each type of the list to the file...
       for typename in self.importedTypes:
          f.write("from "+typename+" import *\n")
       f.write("class ASG_"+ASGroot.keyword_.toString()+"(ASG, ATOM3Type):\n\n")		# generate class definition
       f.write("   def __init__(self, parent= None, ASGroot = None):\n")                	# declare init method
       metaModelName = ASGroot.keyword_.toString()                                           # get the metamodel name
       f.write("      ASG.__init__(self, '"+metaModelName+"', ASGroot, ['ASG_"+ASGroot.keyword_.toString()+"'") # add also the own name (for hierarchical modelling)
       # add the node types...
       counter = 0
       for nodeType in ASGroot.nodeTypes:							# for each node type
          for UMLobject in ASGroot.listNodes[nodeType]:					# for each object
             if UMLobject.keyword_:     # Added 7 April 2003 by JL
               f.write(" ,")             
               f.write("'"+UMLobject.keyword_.toString()+"'")
               counter = counter + 1
       f.write("])\n\n")								
       f.write("      ATOM3Type.__init__(self)\n")
       self.genASGNodeCode(f, ASGroot, 1)							# != None -> globalModel
       f.write("\n\n")
       f.close()

    def genCodeFor ( self, entity, objsWithCardConstraints ):
       """
          Generates Python code for the entity
       """
       # check 
       if not entity.keyword_:                                                          # entity does not have a keyword, raise an error, we cannot generate code
          tkMessageBox.showerror(
               "Error: entity has no keyword!",
               "Entity does not have a keyword, " + str(entity),
               parent = self
          )
          return

       # generate code for the ATOM3Links, because a graphical file must be generated

       for attr in entity.generatedAttributes.keys():
          type = entity.generatedAttributes[attr]					# A tuple with the types...
          if type[0] == 'ATOM3Link':                                                    # ey! an ATOM3Link has been found...
             at3link = entity.getAttrValue(attr)
             if at3link and not at3link.isNone():                                       # if it has some value...
                entity.getAttrValue(attr).genGraphicalFile( self.codeGenDir, self.parent )
             else:
                tkMessageBox.showerror(
                   "Error: entity has no graphical appearance!",
                   "Entity "+entity.keyword_.toString()+" does not have a graphical appearance",
                   parent = self
                )
                return                
       fileName = entity.keyword_.toString()+".py"			      			# Prepare file name, with the keyword
       if self.console: self.console.appendText('Generating file '+fileName+' in directory '+self.codeGenDir)
       filePath =  os.path.join( self.codeGenDir, fileName)
       f = open( filePath, "w+t")                                          # open file name and print header
       #f.write("# __"+ fileName +"_____________________________________________________\n")
       f.write('"""\n')
       f.write("__"+ fileName +"_____________________________________________________\n")
       f.write("\n")
       f.write("Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)\n")
       f.write("Author: "+USER_NAME+"\n")
       f.write("Modified: "+time.asctime()+"\n")
       f.write("__"+ len(fileName)*"_" +"_____________________________________________________\n")
       f.write('"""\n')
       
       f.write("from ASGNode import *\n\n")						# generate imports
       f.write("from ATOM3Type import *\n\n")                           		# generate imports
       self.importedTypes = []								# list where the necessary types will be placed
    
       self.visitorOnAttributes( f, entity, self.genImport)             		# generate import for ATOM3Types

       # now write each type of the list to the file...
       for typename in self.importedTypes:
          f.write("from "+typename+" import *\n")
       
       # Open the graphical appearence file (may not exist)
       graphicName = "graph_"+entity.keyword_.toString()+".py"            
       if( os.path.exists( os.path.join( self.codeGenDir, graphicName ) ) ):
          hasGraph = True
          f.write("from graph_"+entity.keyword_.toString()+" import *\n")
       
       # Not there... doh!
       else:
          hasGraph = False
          # if we should generate graphics, then give a warning!
          if self.genGraphics:  # generate == Yes
             tkMessageBox.showwarning(
               "Warning: Undefined icon!                           ",
               "Entity '"+entity.keyword_.toString()+"' does not have an icon",
               parent = self
             )   
        
       f.write("class "+entity.keyword_.toString()+"(ASGNode, ATOM3Type):\n\n")		# generate class definition
       f.write("   def __init__(self, parent = None):\n")		  	      	# declare init method
       f.write("      ASGNode.__init__(self)\n")
       f.write("      ATOM3Type.__init__(self)\n")
       if hasGraph:                             # then write down the class name
           f.write("      self.graphClass_ = graph_"+entity.keyword_.toString()+"\n")
           #f.write("      self.isGraphObjectVisual = "+str(entity.isGraphObjectVisual)+"\n")
           # See HierarchicalASGNode.py for hierarchical code...
           entity._generateHierarchicalSemanticCode(f, '      ')
       self.genASGNodeCode(f, entity)				      	# call method to generate the rest of the code
       f.write("\n\n")
       f.close()
  

    def existGenerativeAttributes(self):
       """
          Returns 1 if the actual model has some generative attributes...
       """
       # first look in the ASGroot
       if self.ASGroot.hasGenerativeAttributes(): return 1
       # now look in each entity of the model...
       for entype in self.ASGroot.listNodes.keys():
         for entity in self.ASGroot.listNodes[entype]:
            if entity.hasGenerativeAttributes(): return 1
       return 0


    def genButtons(self, ASGroot=None):
       """
          generates the file which has the actions to create the defined entities.
       """
       if(ASGroot == None):
         ASGroot = self.ASGroot
       
       # get the name from the model name...
       nameButtonBar = ASGroot.keyword_.toString()+"_MM"
       if self.console: self.console.appendText('Generating file '+nameButtonBar+'.py in directory '+self.codeGenDir+' (Meta-model file)')
       file = open(  os.path.join( self.codeGenDir,nameButtonBar+".py"), "w+t" )
       # see if we have to import graph_ASG_<nameButtonBar>, or graph_ASG_UMLmetaMetaModel
       # try to open the file to see if it exists
       grFName = 'graph_ASG_'+ASGroot.keyword_.toString()
       # check if a drawing was made, and if not, use the default drawing
       # try to open it...
       try:
         f = open (grFName+'.py', "r+t")
       except IOError:									# not found, so use default drawing file
         grFName = 'graph_ASG_ERmetaMetaModel'   							
       else:
         f.close()
       
       file.write('"""\n')
       file.write("__"+ nameButtonBar+".py______________________________________________________\n")
       file.write("\n")
       file.write("Automatically generated AToM3 MetaModel (DO NOT MODIFY DIRECTLY)\n")
       file.write("Author: "+USER_NAME+"\n")
       file.write("Modified: "+time.asctime()+"\n")
       file.write("__"+ len(nameButtonBar+".py")*"_" +"______________________________________________________\n")
       file.write('"""\n')

       file.write('from ASG_'+ASGroot.keyword_.toString()+' import *\n')   	# the class of root node
       file.write('from '+grFName+' import *\n')					# the class of the graphic for the root node
       file.write('from Tkinter         import *\n')
       file.write('from ATOM3TypeInfo   import *\n')
       file.write('from ATOM3String     import *\n')
       file.write('from StatusBar       import *\n')
       file.write('from ATOM3TypeDialog import *\n\n')

       # import all the ASGNodes...
       for UMLclass in ASGroot.nodeTypes:
          for obj in ASGroot.listNodes[UMLclass]:
             if obj.keyword_:       # Added 7 April 2003 
                file.write('from '+obj.keyword_.toString()+'       import *\n')
                # check if there exist the file with the graphical class
                nameFile = "graph_"+obj.keyword_.toString()+".py"
                try:
                    f = open (nameFile, "r+t")
                except IOError:
                    pass
                else:      								
                    f.close ()
                    file.write('from graph_'+obj.keyword_.toString()+' import *\n')

       # generate function "createNewASGroot(self):"
       file.write('def createNewASGroot(self):\n')
       file.write('   return ASG_'+ASGroot.keyword_.toString()+'(self, None)\n\n')

       # generate function "createModelMenu"
       file.write('def createModelMenu(self, modelMenu):\n')
       file.write('    "Creates a customized Model Menu for the actual formalism"\n')
       # Modified by Denis Dube, summer 2004, why the heck do you declare a new modelMenu 
       # when your given one as a parameter? It definately doesn't work at all on my Win XP box 
       # if you do that. 
       #file.write('    modelMenu = Menu(self.mmtoolMenu, tearoff=0)\n')
       for UMLclass in ASGroot.nodeTypes:
          for obj in ASGroot.listNodes[UMLclass]:
             if obj.keyword_:       # Added 7 April 2003 
                file.write('    modelMenu.add_command(label="New '
                           +obj.keyword_.toString()
                           +'", command=lambda x=self: x.createNew'
                           +obj.keyword_.toString()+'(x, 100, 100) )\n') # 

       # generate the function setConnectivity
       self.genSetConnectivity(file)

       # generate the functions 'createNew<class>(self, wherex, wherey):
       for UMLclass in ASGroot.nodeTypes:
          for obj in ASGroot.listNodes[UMLclass]:
            if obj.keyword_:  # Added 7 April 2003 by JL
              file.write('def createNew'+obj.keyword_.toString()
                         +'(self, wherex, wherey, screenCoordinates = 1):\n')
              file.write('   self.fromClass = None\n')
              file.write('   self.toClass = None\n')
              file.write('   # try the global constraints...\n')
              file.write('   res = self.ASGroot.preCondition(ASG.CREATE)\n')
              file.write('   if res:\n')
              file.write('      self.constraintViolation(res)\n')
              file.write('      self.mode=self.IDLEMODE\n')
              file.write('      return\n\n')
              file.write('   new_semantic_obj = '+obj.keyword_.toString()+'(self)\n')
              file.write('   res = new_semantic_obj.preCondition ( ASGNode.CREATE )\n')
              file.write('   if res: return self.constraintViolation(res)\n')
              file.write('   new_semantic_obj.preAction ( ASGNode.CREATE ) \n\n')
              file.write('   ne = len(self.ASGroot.listNodes["'+obj.keyword_.toString()+'"])\n')
              file.write('   if new_semantic_obj.keyword_:\n')
              file.write('      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))\n')
              file.write('   if screenCoordinates:\n')
              file.write('      new_obj = graph_'+obj.keyword_.toString()+'(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)\n')
              file.write('   else: # already in canvas coordinates\n')
              file.write('      new_obj = graph_'+obj.keyword_.toString()+'(wherex, wherey, new_semantic_obj)\n')            
              file.write('   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)\n')
              file.write('   self.UMLmodel.addtag_withtag("'+obj.keyword_.toString()+'", new_obj.tag)\n')
              file.write('   new_semantic_obj.graphObject_ = new_obj\n')
              file.write('   self.ASGroot.addNode(new_semantic_obj)\n')
              file.write('   res = self.ASGroot.postCondition(ASG.CREATE)\n')
              file.write('   if res:\n')
              file.write('      self.constraintViolation(res)\n')
              file.write('      self.mode=self.IDLEMODE\n')
              file.write('      return\n\n')
              file.write('   res = new_semantic_obj.postCondition(ASGNode.CREATE)\n')
              file.write('   if res:\n')
              file.write('      self.constraintViolation(res)\n')
              file.write('      self.mode=self.IDLEMODE\n')
              file.write('      return\n')
              file.write('   new_semantic_obj.postAction(ASGNode.CREATE)\n\n')
              file.write('   self.mode=self.IDLEMODE\n')
              file.write('   if self.editGGLabel :\n')
              file.write('      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)\n')
              file.write('   else:\n')
              file.write('      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)\n')
              file.write('   return new_semantic_obj\n')

       # generate also the function "createNewModel" to allow hierarchical Modelling
       file.write('def createNew_Model(self, wherex, wherey, screenCoordinates = 1):\n')
       file.write('   self.toClass = None\n')
       file.write('   self.fromClass = None\n')
       file.write('   new_semantic_obj = ASG_'+ASGroot.keyword_.toString()+'(self)\n')
       file.write('   ne = len(self.ASGroot.listNodes["ASG_'+ASGroot.keyword_.toString()+'"])\n')
       file.write('   if new_semantic_obj.keyword_:\n')
       file.write('      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))\n')
       file.write('   if screenCoordinates:\n')
       file.write('      new_obj = '+grFName+'(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)\n')
       file.write('   else: # already in canvas coordinates\n')
       file.write('      new_obj = '+grFName+'(wherex, wherey, new_semantic_obj)\n')       
       file.write('   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)\n')
       file.write('   self.UMLmodel.addtag_withtag("ASG_'+ASGroot.keyword_.toString()+'", new_obj.tag)\n')
       file.write('   new_semantic_obj.graphObject_ = new_obj\n')
       file.write('   self.ASGroot.addNode(new_semantic_obj)\n')
       file.write('   self.mode=self.IDLEMODE\n')
       file.write('   if self.editGGLabel :\n')
       file.write('      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)\n')
       file.write('   else:\n')
       file.write('      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)\n')
       file.write('   return new_semantic_obj\n')

       # generate fillTypesInformation function

       file.write('def fillTypesInformation(self):\n')
       file.write('    objs = []\n')
       itemList = self.typeList.getValue()						# obtain the item list
       for item in itemList:								# obtain the value (ATOM3TypeInfo) of each item
           file.write('    obj = ATOM3TypeInfo(self)\n')
           file.write('    params  = []\n')
           value = item.getValue()
           for param in value[2]:							# if we have parameters
              file.write('    param = ATOM3String("'+param.toString()+'")\n')
	      file.write('    params.append(param)\n')
           file.write('    obj.setValue(("'+value[0]+'", "'+value[1]+'", params, '+str(value[3])+' ))\n')
           file.write('    objs.append(obj)\n')
       file.write('    self.typeList.setValue(objs)\n\n')

    def genSetConnectivity(self, file):
       """
          Generates the setConnectivity function in the file.
       """
       file.write('def setConnectivity(self):\n')
       indent = '    '								# set the indentation to be used in the function
       self.__genConnectivityMap(file, indent)
       file.write(indent+'\n')
       self.__genCardinalityTable(file, indent)
       file.write(indent+'\n')
       self.__genEntitiesInMetaModel(file, indent)
       file.write(indent+'\n')

    def __reachesDirectly (self, nobj1, nobj2, listOfObjects, direc):
       """
          Added 12 Sept 2002
          Returns 1 if nobj1 can reach nobj2 directly.
          nobj1 and nobj2 are strings.
          listOfObjects is a list with the real objects
          direc is the direction of the connection: 1 is from nobj1 ro nobj2, 0 is the reverse
       """
       for obj in listOfObjects:
         if obj.keyword_.toString() == nobj1:                                   # we've found the object...
           for attr in obj.generatedAttributes.keys():				# look for ATOM3Connections...
              if obj.generatedAttributes[attr][0] == 'ATOM3List' and obj.generatedAttributes[attr][1] == 'ATOM3Connection':
                lc = obj.getAttrValue(attr).getValue()
                for conn1 in lc:
                  name, direc1, min1, max1 = conn1.getValue()			# unwrap it
                  if name == nobj2 and direc1[1] == direc: return 1
       return 0            
       
    def __genConnectivityMap(self, file, indent):
       """
          Generates code in the file to generate the 'ConnectivityMap' dictionary
       """
       entities = {}
       connections = []                    					# this will be a list with all the entities with connection possibilities...
       for UMLclass in self.ASGroot.nodeTypes:					# build the dicionary, search for 'entities'
          for obj in self.ASGroot.listNodes[UMLclass]:
            if obj.keyword_:    # Added 7 April 2003 by JL
               hasConns = 0
               for attr in obj.generatedAttributes.keys():				# look for ATOM3Connections...
                 if obj.generatedAttributes[attr][0] == 'ATOM3Connection' or (obj.generatedAttributes[attr][0] == 'ATOM3List' and obj.generatedAttributes[attr][1] == 'ATOM3Connection'):
                    hasConns = 1
                    break
               if hasConns: connections.append(obj)
               entities[obj.keyword_.toString()] = {}

       # initialize dictionary to void
       for ent1 in entities.keys():
         for ent2 in entities.keys():
           entities[ent1][ent2] = []

       for obj in connections: 							# for each element with connections...
         #if obj.keyword_:         # Added 7 April 2003 by JL
            objName = obj.keyword_.toString()					# get its name
            for attr in obj.generatedAttributes.keys():				# look for ATOM3Connections...
              if obj.generatedAttributes[attr][0] == 'ATOM3List' and obj.generatedAttributes[attr][1] == 'ATOM3Connection':
                 lc = obj.getAttrValue(attr).getValue()				# get the list of connections
                 for conn1 in lc:                                                  # for each connection...
                    name1, direc1, min1, max1 = conn1.getValue()			# unwrap it
                    lc2 = []+lc
                    lc2.remove(conn1)
                    if name1 in entities.keys():
                       for conn2 in lc2:
                          name2, direc2, min2, max2 = conn2.getValue()
                          if name2 in entities[name1].keys() and name2 in entities.keys() and direc1 != direc2 and not self.__reachesDirectly(name1, name2, connections, direc2[1]):   # last condition added 12 Sept 2002
                             ntuple = (objName, "self.createNew"+objName)
                             if direc1[1] == 1:
                                if not ntuple in entities[name1][name2]:
                                   entities[name1][name2].append(ntuple)
                             else:
                                if not ntuple in entities[name2][name1]:
                                   entities[name2][name1].append(ntuple)

       # now, write the dictionary in the file...

       for name1 in entities.keys():
          file.write(indent+"self.ConnectivityMap['"+name1+"']={")
          outcont = 0
          for name2 in entities[name1].keys():
             if outcont > 0: file.write("\n"+indent+"      ,'"+name2+"': [")
             else: file.write("\n"+indent+"       '"+name2+"': [")
             outcont = outcont + 1
             count = 0
             for element in entities[name1][name2]:
                if count > 0: file.write(", ")
                file.write("( '"+element[0]+"', "+element[1]+")")
                count = count + 1
             file.write("]")
          file.write(" }\n")

    def __genEntitiesInMetaModel(self, file, indent):
       """
          Generates code in file to write the 'entitiesInMetaModel' list
       """
       metaModelName = self.ASGroot.keyword_.toString()
       file.write(indent+"self.entitiesInMetaModel['"+metaModelName+"']=[")
       counter = 0
       for entity1 in self.ASGroot.nodeTypes:					
         for obj1 in self.ASGroot.listNodes[entity1]:
           if obj1.keyword_:  # Added 7 April 2003 by JL
              if counter > 0: file.write(", ")
              file.write ('"'+obj1.keyword_.toString()+'"')
              counter = counter + 1
       file.write("]\n\n")

    def __genCardinalityTable(self, file, indent):
       """
          Generates code in file to write the 'CardinalityTable' dictionary
       """
       cardTable = {}
       # in this function we also include the filling of the dictionary self.CardinalityTable...
       for entity1 in self.ASGroot.nodeTypes:					
         for obj1 in self.ASGroot.listNodes[entity1]:
           if obj1.keyword_: # Added 7 April 2003 by JL
              name1 = obj1.keyword_.toString()
              cardTable[name1] = {}
	      for entity2 in self.ASGroot.nodeTypes:	
                 for obj2 in self.ASGroot.listNodes[entity2]:
                   if obj2.keyword_:  # Added 7 April 2003 by JL
	             name2 = obj2.keyword_.toString()
	             cardTable[name1][name2] = []					# Initialize to None
	
       for UMLclass in self.ASGroot.nodeTypes:					# build the dicionary, search for 'entities'
          for obj in self.ASGroot.listNodes[UMLclass]:
            if obj.keyword_:    # Added 7 April 2003 by JL
               objName = obj.keyword_.toString()					# get the entity name
               for attr in obj.generatedAttributes.keys():				# look for ATOM3Connections...
                 if obj.generatedAttributes[attr][0] == 'ATOM3List' and obj.generatedAttributes[attr][1] == 'ATOM3Connection':
                    lc = obj.getAttrValue(attr).getValue()				# get the list of connections
                    for conn1 in lc:
                       name1, direc1, min1, max1 = conn1.getValue()
                       cardTable[objName][name1].append((min1, max1, direc1[0][direc1[1]]))

       for UMLclass in self.ASGroot.nodeTypes:				
          for obj in self.ASGroot.listNodes[UMLclass]:
             if obj.keyword_:  # Added 7 April 2003 by JL                
                name1 = obj.keyword_.toString()
                file.write(indent+"self.CardinalityTable['"+name1+"']={")
                count = 0
                for UMLclass1 in self.ASGroot.nodeTypes:		
                    for obj2 in self.ASGroot.listNodes[UMLclass1]:
                     if obj2.keyword_:  # Added 7 April 2003 by JL                      
                       name2 = obj2.keyword_.toString()
                       if count > 0: file.write("\n"+indent+"      ,'"+name2+"': "+ str(cardTable[name1][name2]))
                       else: file.write("\n"+indent+"      '"+name2+"': "+ str(cardTable[name1][name2]))
                       count = count + 1
                file.write(" }\n")

    def editTypes(self):
       """
          Opens a dialog to edit the types available in the session. If the user creates a new one,
          then calls the graph grammar to generate code for the type.
       """
       from TypeCodeGen         import *
       ma = ATOM3TypeDialog(self, self.typeList, ATOM3TypeDialog.OPEN )# edit types...
       # generate code for the edited type...
       newTypes     = self.typeList.getValue()          				# obtain the list of existing types
       oldTypes = []
       for name in self.types.keys():
          className = str(self.types[name][0])
          oldTypes.append(className[string.rfind(className,".")+1:])
       newTypesNames = []
       for type in newTypes:                            				# search for new defined types
          typeName = type.getValue()[1]
          newTypesNames.append(typeName)
          if not typeName in oldTypes:                                                  # This is a new Type!
             self.GraphGrammars = [ TypeCodeGen(self)]
             grs = GraphRewritingSys(self, self.GraphGrammars, type.typeModel )
             grs.evaluate(stepByStep = 0, moveEntities = 1, execute = grs.SEQ_MANUAL, graphics = 0)	# no graphics (the canvas with the model is closed!)
             self.newTypes.append((type.getValue()[0], typeName, (), 1))                     	# add the new type to the list of newly created types
       # delete the deleted types...
       elements2delete = []
       for nt in self.newTypes:
          name, name, args, flag = nt
          if not name in newTypesNames:
             elements2delete.append(nt)
       for delElem in elements2delete: self.newTypes.remove(delElem)			# delete the element
       for type in self.types.keys():							# remove all elements
          del self.types[type]
       self.fillDictionaryWithTypes()							# fill the dictionary again with the types

    def add2Types(self, ASGNodeType, oldName):
       """
          check if the object whose name was oldName is included in the list of types, and if not, include it
       """
       # create a new ATOM3TypeInfo to add it to the list
       newType = ATOM3TypeInfo(self)
       newType.setValue( (ASGNodeType.keyword_.toString(), ASGNodeType.keyword_.toString(), () ))
       # generate code for the class...
       self.genCodeFor( ASGNodeType )
       # import the class file.
       exec "from "+ASGNodeType.keyword_.toString()+" import *\n"
       self.types[ASGNodeType.keyword_.toString()] = ( eval(ASGNodeType.keyword_.toString()), (self, ))
       # see if the name has changed
       if (oldName in self.types.keys()) and (oldName != ASGNodeType.keyword_.toString()):
          del self.types[oldName]
          os.remove( oldName+".py")
       typesInList = self.typeList.getValue()					# the ATOM3TypeInfo objects in the list
       counter = 0
       for typ in typesInList:
          val = typ()  # Get the objects value
          if val[0] == oldName:								# we have found it
             typesInList[counter] = newType
             break
          counter = counter + 1

    def newModeUMLrelationship(self):
       """
          Enters in the mode NEWUMLrelationship
       """
       self.mode = NEWUMLrelationship



    def copyFromLHS(self):
       """
          Performs the copying from the LHS of one rule. It takes this information from self.GGSemanticRule
          Added 20/July/2002
       """
       clonedObjects = [] 
                                                                                       # A list with the cloned objects
       for nodeType in self.GGSemanticRule.LHS.listNodes.keys():
         for node in self.GGSemanticRule.LHS.listNodes[nodeType]:           
           newObj = node.clone()
           newObj.parent = self                                                                           # change the object's parent to myself
           newObj.editGGLabel = ASG.INRHS                                                                 # This node is in RHS
           newObj.GGset2Any = {}                                                                          # reinitialize GG info
           newObj.graphObject_ = newObj.graphClass_(node.graphObject_.x, node.graphObject_.y, newObj)     # create the graphical object
           #newObj.graphObject_.DrawObject(self.UMLmodel, self.editGGLabel)
           #self.UMLmodel.addtag_withtag(nodeType, newObj.graphObject_)
           try:
             self.ASGroot.addNode(newObj)
           except:
             tkMessageBox.showerror( 
               "Copy LHS",
               "ERROR: copy LHS failed since a formalism open in the LHS is"
               + " not currently open in the RHS\n\nPlease open it now...",
               parent=self)
             return
           node.clonedObject = newObj                                                                     # keep a pointer to the cloned object
           clonedObjects.append(newObj)
       
       # copy also the (semantic) connections
       for obj in clonedObjects:
         obj.in_connections_nw = []
         for icn in obj.in_connections_: 
           obj.in_connections_nw.append(icn.clonedObject)
         obj.in_connections_ = obj.in_connections_nw
         obj.out_connections_nw = []         
         for icn in obj.out_connections_: 
           obj.out_connections_nw.append(icn.clonedObject)
         obj.out_connections_ = obj.out_connections_nw
         del obj.in_connections_nw
         del obj.out_connections_nw
       
       # Make sure that the RHS has the appropriate starting GG label #
       maxEditLabel = 0
       for nodeType in self.GGSemanticRule.RHS.listNodes.keys():
         for node in self.GGSemanticRule.RHS.listNodes[nodeType]:
           maxEditLabel = max(maxEditLabel, node.GGLabel.getValue())
       self.GGSemanticRule.RHS.minimumGG = maxEditLabel + 1
         
       # delete the pointer to the cloned object
       for nodeType in self.GGSemanticRule.LHS.listNodes.keys():
         for node in self.GGSemanticRule.LHS.listNodes[nodeType]:
           del node.clonedObject

       # show the copied objects in the canvas    
       self.ASGroot.writeContents(self, self.genGraphics, 1, clonedObjects)    
         
    def reDrawGGLabels(self):
       """
          redraws the GGLabels of each drawn entity, if appropriate
       """
       if self.editGGLabel:
          for nt in self.ASGroot.listNodes.keys():
             for node in self.ASGroot.listNodes[nt]:
                if node.graphObject_:
                   node.graphObject_.drawGGLabel(self.UMLmodel)
                   for drawnAttribute in node.graphObject_.attr_display.keys():                       
                       if node.getAttrValue(drawnAttribute).isNone() and self.editGGLabel == ASG.INLHS :
                          node.graphObject_.ModifyAttribute(drawnAttribute, "<ANY>")
                       elif self.editGGLabel== ASG.INRHS:                             # Modified 22 July, JL
                          if node.GGset2Any.has_key(drawnAttribute):
                            if node.GGset2Any[drawnAttribute].Copy.getValue()[1]:
                              node.graphObject_.ModifyAttribute(drawnAttribute, "<COPIED>")
                            elif not node.GGset2Any[drawnAttribute].Specify.getValue()[4] in ["", "\n", None]:
                              node.graphObject_.ModifyAttribute(drawnAttribute, "<SPECIFIED>")

    def drawEntity(self, semObject, className):
       """
          draws an existing entity
       """
       graphObj = semObject.graphObject_
       if graphObj:
          #print "<DEBUG> ATOM3.drawEntity() ", graphObj
          graphObj.redrawObject(self.getCanvas(), self.editGGLabel)
          # now evaluate ONLY the graphical constraints!
          graphObj.postCondition(ASG.CREATE)
          self.UMLmodel.addtag_withtag(className, graphObj.tag)
       self.mode=self.IDLEMODE

    def genASGNodeCode(self, f, UMLobject, isGlobalModel = None):
       """ generates code for the lower meta-level of a user-defined entity.
           - isGlobalModel may contain a list with the objects with cardinality constraints"""
       self.theKeyword = None
       f.write("      self.parent = parent\n")
       # search for something that is of Attribute Type or List of Attribute
       self.hasAppearance = None									# flag that indicates if the entity has an attribute of type appearance
       													# if it has, it must have a keyword...
       self.visitorOnAttributes( f, UMLobject, self.findKeywordAndIcons)
       if self.hasAppearance and self.theKeyword == None:						# ... check that it is the case...
          tkMessageBox.showerror(
              "need a keyword!",
              "Entity "+UMLobject.keyword_.toString()+" did not define a keyword attribute",
              parent = self
          )
          return 0
       self.visitorOnAttributes( f, UMLobject, self.writeCreation)

       # fill the 'generatedAttributes' dictionary
       f.write("      self.generatedAttributes = {")
       self.visitorOnAttributes( f, UMLobject, self.writeGeneratedDictionary)
       f.write("      }\n")
       # fill the 'realOrder' list
       f.write("      self.realOrder = [")
       self.visitorOnAttributes( f, UMLobject, self.writeRealOrderList)
       f.write("]\n")
       # fill the 'directEditing' list          (Added 31 July 2002, by JL)
       f.write("      self.directEditing = [")
       self.visitorOnAttributes( f, UMLobject, self.writeDirectEditingList)
       f.write("]\n")     
       
       #
       # Generate the clone function
       #

       f.write("   def clone(self):\n")
       if isGlobalModel  != None:        # we don't clone whole models!!
          #f.write("      cloneObject = ASG_"+ UMLobject.keyword_.toString() +"( self.parent )\n")
          #f.write("      cloneObject.listNodes     = copy.copy(self.listNodes)\n")
          f.write("      return self\n")
       else:
          f.write("      cloneObject = "+ UMLobject.keyword_.toString() +"( self.parent )\n")
          f.write("      for atr in self.realOrder:\n")
          f.write("         cloneObject.setAttrValue(atr, self.getAttrValue(atr).clone() )\n")
          if self.theKeyword:
	     f.write("      cloneObject.keyword_ = cloneObject."+self.theKeyword+"\n")

       if isGlobalModel == None:
          f.write("      ASGNode.cloneActions(self, cloneObject)\n\n")
          f.write("      return cloneObject\n")                                                         # changed 16 July 2002
       
       #
       # Generate the copy function
       #
       f.write("   def copy(self, other):\n")
       f.write("      ATOM3Type.copy(self, other)\n")
       f.write("      for atr in self.realOrder:\n")
       f.write("         self.setAttrValue(atr, other.getAttrValue(atr) )\n")
       
       if self.theKeyword:
	  f.write("      self.keyword_ = self."+self.theKeyword+"\n")

       # only if the object is a descendant of ASGNode
       if isGlobalModel == None:
          f.write("      ASGNode.copy(self, other)\n\n")

       # if we are an ASG class, must override the open() method from ATOM3Type
       if isGlobalModel != None:
          f.write("   def open(self, parent, topWindowParent):\n")
	  #f.write("       ATOM3Type.show(self, parent, topWindowParent)\n")
          f.write("       from ATOM3 import *\n")
          f.write("       a = ATOM3(topWindowParent, '"+UMLobject.keyword_.toString()+"', 0, 1, self)\n")
          f.write("       #self.writeContents(a)\n")
          f.write("       return a\n")

       # Generate code for the constraints...
       f.write("   def preCondition (self, actionID, * params):\n")
       self.visitorOnConstraints ( "PREcondition", f, UMLobject, self.writeActionConstraint )
       f.write("      if self.graphObject_:\n")
       f.write("         return self.graphObject_.preCondition(actionID, params)\n")
       f.write("      else: return None\n")
       f.write("   def postCondition (self, actionID, * params):\n")
       self.visitorOnConstraints ( "POSTcondition", f, UMLobject, self.writeActionConstraint )
       f.write("      if self.graphObject_:\n")
       f.write("         return self.graphObject_.postCondition(actionID, params)\n")
       f.write("      else: return None\n")
       self.visitorOnConstraints (  "", f, UMLobject, self.writeConstraintCode )
       
       # Local methods to generate the actions code...
       def writeActionCode ( file, value, unUsed):
          """ Writes out the action code  """
          tempCode = value[4]
          if(tempCode == None):
            return
          tempCode = tempCode.replace( '\n', '')
          tempCode = tempCode.replace( ' ', '')
          tempCode = tempCode.replace( '\t', '')
          tempCode = tempCode.replace( '\r', '')
          if(tempCode != ''):
            file.write ("   def "+value[0]+"(self, params):\n")
            file.write ("      "+string.replace(value[4],'\n', '\n      '))
            file.write ("\n\n")
       def visitorOnActions ( which, file, UMLobject, function ):
          """ Generates code for actions, in a 'visitor' pattern way  """     
          for attr in UMLobject.generatedAttributes.keys():
            type = UMLobject.generatedAttributes[attr]	# A tuple with the types...
            if( type[0] == 'ATOM3Action' ):            
              value = UMLobject.getAttrValue(attr).getValue()                                # obtain the value
              function(file, value, which)
            elif( type[0] == 'ATOM3List' and type[1] == 'ATOM3Action' ):
              items = UMLobject.getAttrValue(attr).getValue()
              for item in items:
                value = item.getValue()
                function(file, value, which)
       def writeAction ( file, value, which):
        """ Writes part of the function to evaluate local actions """
        listAct, selAct = value[3]
        listKnd, selKnd = value[2]
        
        # Abort if there's no code...
        tempCode = value[4]
        if(tempCode == None):
          return
        tempCode = tempCode.replace( '\n', '')
        tempCode = tempCode.replace( ' ', '')
        tempCode = tempCode.replace( '\t', '')
        tempCode = tempCode.replace( '\r', '')
        if(len(tempCode) == 0):
          return
        
        # Filter to make sure at least one actionID is selected
        if( listKnd[selKnd] == which 
             and filter( lambda item: item == True, selAct ) ):
            # iterate on the specified event... 
            file.write("      if actionID == ")
            conta = 0
            writed = 0
            for event in selAct:
                if event == 1:
                  if not writed:
                      file.write("self."+listAct[conta])
                  else:
                      file.write(" or actionID == self."+listAct[conta])
                  writed = 1
                conta = conta + 1
            file.write(":\n")
            file.write("         self."+value[0]+"(params)\n")
    
       # Generate code for the actions... (added by Denis Feb 26,2005)
       f.write("   def preAction (self, actionID, * params):\n")
       visitorOnActions ( "PREaction", f, UMLobject, writeAction )
       f.write("      if self.graphObject_:\n")
       f.write("         return self.graphObject_.preAction(actionID, params)\n")
       f.write("      else: return None\n")
       f.write("   def postAction (self, actionID, * params):\n")
       visitorOnActions ( "POSTaction", f, UMLobject, writeAction )
       f.write("      if self.graphObject_:\n")
       f.write("         return self.graphObject_.postAction(actionID, params)\n")
       f.write("      else: return None\n")
       visitorOnActions ( "", f, UMLobject, writeActionCode )
       
       
    def moveBox (self, x, y):
      """
         method to move a graphical node in the canvas, called by the mouseMove method.
      """
      sel = self.UMLmodel.find_withtag("selected")		# find the selected 'box'
      tag = self.UMLmodel.gettags(sel[0])[0]
      if sel and tag and VisualObj.Tag2ObjMap.has_key(tag):
         # 1st. try the global constraints...
         # modified 07-march-03: added x, y, initDragX, initDragY parameters
	 res = self.ASGroot.preCondition(ASG.MOVE, x, y, self.initDragX, self.initDragY)	# evaluate global pre-conditions
	 if res: return self.undodrag(res)
         obj = VisualObj.Tag2ObjMap[tag]
         # modified 07-march-03: added x, y, initDragX, initDragY parameters
         res = obj.semanticObject.preCondition(ASG.MOVE, x, y, self.initDragX, self.initDragY)	# evaluate global pre-conditions
	 if res: return self.undodrag(res)	
         # modified 07-march-03: added x, y, initDragX, initDragY parameters
	 self.ASGroot.preAction(ASG.MOVE, x, y, self.initDragX, self.initDragY)			# execute global pre-actions
	 obj.semanticObject.preAction(ASG.MOVE, x, y, self.initDragX, self.initDragY)		# execute local pre-actions
	
         dx = x-self.initDragX					# calculate the displacement in x and y
         dy = y-self.initDragY

         obj.Move(dx, dy)					# Move object (We do not care wether it is a link or an entity)

         # modified 07-march-03: added x, y, initDragX, initDragY parameters
       	 res = self.ASGroot.postCondition(ASG.MOVE, x, y, self.initDragX, self.initDragY)		# evaluate global pre-conditions
	 if res: return self.undomovebox(res,dx,dy,sel,obj, tag)
         # modified 07-march-03: added x, y, initDragX, initDragY parameters	 
         res = obj.semanticObject.postCondition(ASG.MOVE, x, y, self.initDragX, self.initDragY)	# evaluate global pre-conditions
	 if res: return self.undomovebox(res,dx,dy,sel,obj, tag)	

         # modified 07-march-03: added x, y, initDragX, initDragY parameters
       	 self.ASGroot.postAction(ASG.MOVE, x, y, self.initDragX, self.initDragY)          # execute global post-actions
	 obj.semanticObject.postAction(ASG.MOVE, x, y, self.initDragX, self.initDragY)	  # execute local post-actions
                                        # 
    def undomovebox(self, res, dx, dy, sel, obj, tag):
      """
         undoes an entity movement, due to a constraint failure...
      """
      obj.Move(-dx, -dy)
      return self.undodrag(res)

  
if __name__ == '__main__':
    """ WARNING: This code isn't executed if the atom3.py bootup script is used! """

    TkRoot = Tk()
    TkRoot.configure(cursor='watch')
    
    if len(sys.argv) == 1:
        ATOM3(TkRoot, None , 1, 1) #.mainloop()
    else:
        ATOM3(TkRoot, sys.argv[1] , 1, 1) #.mainloop()
    print "\nClosing AToM3 - A Tool for Multi-formalism and Meta-Modelling\n"

    
