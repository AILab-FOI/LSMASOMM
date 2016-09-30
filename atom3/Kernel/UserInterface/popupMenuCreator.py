"""
popupMenuCreator.py

This constructs context senstive menus that present only relevent information
to the user depending on the state of the canvas.
In order to make this fast & intuitive, most of the actual implementations of 
the menu elements have been pushed into another file. 

Created June 17, 2004 by Denis Dube
"""

from Tkinter import Menu, IntVar
import time

from popupMenuElements import *
from OptionDialog      import OptionDialog
from Embedded_Images   import Embedded_Images

class PopupMenuCreator:
      
  def __init__(self, atom3i ):
    self.master = atom3i.parent
    self.atom3i = atom3i
    self.cb = atom3i.cb
    self.optionsDatabase = atom3i.optionsDatabase
    self.popupLogoPhotoimage = Embedded_Images().getPopupLogo()

    self.popupMenu = None
    self.event = None
    
    
  # --------------------------- Popup Utilities -------------------------------
    
  def initilizePopupMenu( self, event ):
    """ Create a new popup menu """
    if( self.popupMenu ):
        self.popupMenu.unpost()
    self.popupMenu = Menu(self.master , tearoff=0, bg = "white")
    self.event = event
    
  def showPopupMenu( self ):
    """ Display the popup menu """
    if( self.popupMenu ):
      self.popupMenu.post(self.event.x_root, self.event.y_root)
    
  def swapMenu(self, menu ):
    """ 
    This is a fix for a problem that no longer exists :p
    It essentially takes one menu and slaps another one in its place.
    """
    raise Exception, "No one uses this method! But if you see this, maybe not so..." 
    self.popupMenu.unpost()
    self.popupMenu = menu
    self.showPopupMenu()
    
  def popupRemover(self):
    """ Goodbye popup! """
    if( self.popupMenu ):
      self.popupMenu.unpost()
      self.popupMenu = None
      
  
  # ----------------------  Context Sensitive Menus --------------------------    
    
  def NoCursorNoSelectPopup( self,event ):
    """ Popup menu to show when no items under the mouse, and no items selected """

    self.initilizePopupMenu( event )
  
    addLogo( self )
    #.........................
    addSeperator( self )
    #.........................
    addModelAction( self )
    addSelectAll( self )  
    addPaste( self )
    addUndo( self )
    addRedo( self ) 
    #.........................
    addSeperator( self )
    #.........................
    addFileMenu( self )
    addModelMenu( self )
    addTransformationMenu( self )
    addLayoutMenu( self ) 
    addExportMenu( self )
    #.........................
    addSeperator( self )
    #.........................     
    addOpenLastModel( self )
    addOpenLastMetaModel(self)
    addSourcePath( self )
    #.........................
    addSeperator( self )
    #.........................    
    addToggleSmoothMode( self )    
    #.........................
    addSeperator( self )
    #.........................
    addExit( self )
    
    self.showPopupMenu()
    
  def NoCursorMultiSelectPopup(self,event):
    """ Popup menu to show when no items under the mouse, and multiple items selected """
    
    self.initilizePopupMenu( event )
    
    addLogo( self )
    #.........................
    addSeperator( self )
    #.........................
    addLayoutMenu( self )
    addResizeEntity( self )
    addNodeLabelDragToggle( self )
    #.........................
    addSeperator( self )
    #.........................
    addSelectAll( self )
    addDeselectAll( self )
    #.........................
    addSeperator( self )
    #.........................
    addCut( self )
    addCopy( self )
    addPaste( self )
    #.........................
    addSeperator( self )
    #.........................
    addUndo( self )
    addRedo( self ) 
    #.........................
    addSeperator( self )
    #.........................
    addClear( self )
        
    self.showPopupMenu()
    
  def EntityAtCursorMultiSelectPopup(self,event):
    """ 
    A graphical entity is under the mouse cursor, along with multiple
    selected items
    """
    
    self.initilizePopupMenu( event )
    
    addLogo( self )
    #.........................
    addSeperator( self )
    #.........................
    addLayoutMenu( self )
    addEditEntity( self )
    addDragOverlap( self )
    addDrawArrow( self )  
    addResizeEntity( self )  
    addNodeLabelDragToggle( self )
    #.........................
    addSeperator( self )
    #.........................
    addSelectAll( self )
    addDeselectAll( self )
    #.........................
    addSeperator( self )
    #.........................
    addCut( self )
    addCopy( self )
    addPaste( self )
    #.........................
    addSeperator( self )
    #.........................
    addCopyAttributes( self )
    addPasteAttributes( self )
    #.........................
    addSeperator( self )
    #.........................
    addUndo( self )
    addRedo( self ) 
    #.........................
    addSeperator( self )
    #.........................
    addClear( self )
   
    
    self.showPopupMenu()

  def EntityAtCursorNoSelectPopup(self,event):
    """ A graphical entity is under the mouse cursor, but no selected items """
    
    self.initilizePopupMenu( event )
    
    addLogo( self )
    #.........................
    addSeperator( self )
    #.........................
    addEditEntity( self )
    addDragOverlap( self )
    addDrawArrow( self )
    addResizeEntity( self ) 
    #.........................
    addSeperator( self )
    #.........................
    addSelectAll( self )
    addPaste( self )
    #.........................
    addSeperator( self )
    #.........................
    addCopyAttributes( self )
    addPasteAttributes( self )
    #.........................
    addSeperator( self )
    #.........................
    addUndo( self )
    addRedo( self ) 
    
    self.showPopupMenu()
        
    
  def LinkAtCursorMultiSelectPopup(self,event):
    """ 
    A graphical link/connection is under the mouse cursor, along with multiple
    selected items
    """
    
    self.initilizePopupMenu( event )
    
    addLogo( self )
    #.........................
    addSeperator( self )
    #.........................
    addLayoutMenu( self )
    addEditEntity( self )
    addDragOverlap( self )
    addArrowEditor( self )
    addResizeEntity( self ) 
    addNodeLabelDragToggle( self )
    #.........................
    addSeperator( self )
    #.........................
    addSmoothSelected( self )
    addToggleSmoothMode( self )
    #.........................
    addSeperator( self )
    #.........................
    addSelectAll( self )
    addDeselectAll( self ) 
    #.........................
    addSeperator( self )
    #.........................
    addCut( self )
    addCopy( self )
    addPaste( self )
    #.........................
    addSeperator( self )
    #.........................
    addCopyAttributes( self )
    addPasteAttributes( self )
    #.........................
    addSeperator( self )
    #.........................
    addUndo( self )
    addRedo( self ) 
    #.........................
    addSeperator( self )
    #.........................
    addClear( self )
    
    
    self.showPopupMenu()
    
  def LinkAtCursorNoSelectPopup(self,event):
    """ 
    A graphical link/connection is under the mouse cursor, but there are no
    selected items
    """
    
    self.initilizePopupMenu( event )
    
    addLogo( self )
    #.........................
    addSeperator( self )
    #.........................
    addEditEntity( self )
    addDragOverlap( self )
    addArrowEditor( self )
    #.........................
    addSeperator( self )
    #.........................
    addSelectAll( self )
    addToggleSmoothMode( self )
    addPaste( self )
    #.........................
    addSeperator( self )
    #.........................
    addCopyAttributes( self )
    addPasteAttributes( self )
    #.........................
    addSeperator( self )
    #.........................
    addUndo( self )
    addRedo( self ) 
    
    self.showPopupMenu()
    
  def ArrowEditorPopup(self,event):
    """ Menu for the arrow editor """
    self.initilizePopupMenu( event )
    
    addLogo( self )
    #.........................
    addSeperator( self )
    #.........................
    addEditEntity( self )    
    addInsertPoint( self )
    addDeletePoint( self )
    addSmoothSelected( self )
    addNodeLabelMoveToggle( self )
    #.........................
    addSeperator( self )
    #.........................
    addArrowEditorExit( self )
    
    self.showPopupMenu()
    
  # ----------------------- Popup a specific submenu -------------------------
    
  def LayoutPopup(self,event):
    self.initilizePopupMenu( event )
    self.popupMenu = self.atom3i.layoutMenu
    self.showPopupMenu()
    
  def ExportPopup(self,event):
    self.initilizePopupMenu( event )
    self.popupMenu = self.atom3i.exportMenu
    self.showPopupMenu()
    
  def ModelPopup(self,event):
    self.initilizePopupMenu( event )
    self.popupMenu = self.atom3i.modelMenu
    self.showPopupMenu()
        
  def TransformationPopup(self,event):
    self.initilizePopupMenu( event )
    self.popupMenu = self.atom3i.transMenu
    self.showPopupMenu()
    
  def FilePopup(self,event):
    self.initilizePopupMenu( event )
    self.popupMenu = self.atom3i.filemenu
    self.showPopupMenu()
    
  def LastModelPopup(self,event):
    self.initilizePopupMenu( event )
    addOpenLastModelSubroutine( self, self.popupMenu )
    self.showPopupMenu()
     
  def LastMetaModelPopup(self,event):
    self.initilizePopupMenu( event )
    addOpenLastMetaModelSubroutine( self, self.popupMenu )
    self.showPopupMenu()
    
  def SourcePathPopup(self,event):
    self.initilizePopupMenu( event )
    addSourcePathSubroutine( self, self.popupMenu )
    self.showPopupMenu()
         
    
  # ------------------------ String List to PopupMenu ---------------------------------    
    
  def listChoicePopup(self, title, stringList, unused = None ):
    """ 
    Creates a popup menu with radiobuttons labeled from the stringList.
    Returns the index of the label that was chosen.
    NOTE: choosing outside the popup implicitly chooses index 0
    """
        
    # Remove any existing popups first
    self.popupRemover()
    
    self.popupMenu = Menu(self.master , tearoff=0)
    integerVar = IntVar()
    
    self.popupMenu.add_command( label=title, command=self.popupRemover )
    self.popupMenu.add_separator() 
    
    i = 1
    for label in stringList:
      self.popupMenu.add_radiobutton( label=label, variable=integerVar,
                                      value=i,indicatoron=False )                                               
      i += 1
      
    # This gets the last known co-ordinates of the mouse :D
    # NOTE: We get co-ordinates in terms of canvas space, convert back into
    # screenspace first before using them...
    x,y = self.atom3i.cb.getLastClickCoord()
    dc = self.atom3i.cb.getCanvas()
    x,y = [x-dc.canvasx(0),y-dc.canvasy(0)]

    # These offsets place the menu just where I like it...
    x = int(x) +40 #+ 100
    y = int(y) +40 #+ 20
        
    # Posts the menu, and blocks program execution here on win32 only
    self.popupMenu.post( x,y  )
    
    # Blocks program execution (all platforms) & waits for integerVar to be updated
    # Not ideal: If we close the popup without selecting anything this will
    # wait forever and execution will never get anywhere beyond this point!!!
    # Moreover: AToM3 will not shutdown properly!
    #self.master.wait_variable( integerVar )
    
    # THEORY: This will work whether or not the post() blocks or not
    # Practice: Works great on WinXP with Python 2.3
    #           Linux?
    while( 1 ):
      self.master.update()
      value = integerVar.get() 
 
      # Hapiness, we got the value we wanted
      if( value > 0 ):  return value
      
      # The user killed the popup! O_O
      elif( self.popupMenu == None ):  return 0
      
      # Unhapiness, the user avoided selecting anything
      elif( value == 0 ): 
        self.popupMenu.unpost()
        self.popupMenu.post( x,y  )
        self.master.update()
      
      time.sleep( 0.4 )
      
    return 0 # We won't get here, but just in case...
  
  def listChoicePopupAlternative(self, title, stringList, actionLabel ):
      """ OBSOLETE --- Delete this """
      
      raise Exception, "No one uses this method! But if you see this, maybe not so..."
          
      """
      optionList = [OptionDialog.BOOL_BUTTON_ENTRY,actionLabel]
      
      options = dict()
      optionOrder = list()
      for i in range(0,len(stringList)):
          options[i] = [False,optionList,stringList[i],'']
          optionOrder.append(i)
          i+=1
          
      dialog = OptionDialog(self.master, title, options,optionOrder, grab = False,
                            position = self.atom3i.cb.getLastClickCoordInRootCoords() )
    
      if( dialog.isCanceled() ):
        return 0
      
      options = dialog.getOptionsDatabase()
      i = 1
      for option in optionOrder:
        if( options[option][0] ):
          return i
        i += 1 
      return 0
      """
          
      
      