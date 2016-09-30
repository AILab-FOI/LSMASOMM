"""
popupMenuElements.py

Provides the basic building blocks for creating a dynamic menu

Created June 17, 2004 by Denis Dube
"""

import os
from Tkinter import Menu

from CallbackHandlers    import *
from StaticMenus         import assembleLayoutMenu,assembleTransformationMenu
from StaticMenus         import assembleModelMenu,assembleFileMenu
from StaticMenus         import assembleExporterMenu

STATE_MAP = ["normal","disabled"]


def addSeperator( self ):
  self.popupMenu.add_separator()
  
def addLogo( self ):
  self.popupMenu.add_command(activebackground = "white",
                             image=self.popupLogoPhotoimage,
                             command=lambda x=self.popupMenu: x.unpost() )
  
# ---------------------------------  DRAWING ---------------------------------
  
def addDrawArrow( self ):
  self.popupMenu.add_command(label="Create Arrow", 
                             accelerator="Ctrl-Left-Click", 
                             command=lambda x=self.atom3i, e=self.event: 
                         x.UI_Statechart.event("<Control-ButtonPress-1>", e))  
#                              x.UI_Statechart.event("Create New Arrow",e))  
  
def addModelAction(self):
  mode = self.atom3i.mode
  if(type(mode) != type(str())): mode = "Unknown"
  elif(mode[:7] == "NEWMODE"):     mode = mode[7:]
  label = "Action (" + str(mode) + ")"
  self.popupMenu.add_command(label=label, 
                  state= STATE_MAP[self.cb.isATOM3idle(self.atom3i.mode)], 
                  accelerator= "Ctrl-Right-Click", 
                  command=lambda x=self.atom3i, e=self.event: \
                          x.UI_Statechart.event("<Control-ButtonPress-3>", e))  
#                              x.UI_Statechart.event("Model Action",e))  

# ---------------------------------  EDITING ---------------------------------
                  
def addEditEntity(self):
  self.popupMenu.add_command(label="Edit Nearest Entity", 
                             accelerator="Left-Double-Click", 
                             command=lambda x=self.atom3i, e=self.event: \
                              x.UI_Statechart.event("Edit Properties", e)) 
  self.popupMenu.add_command(label="Edit Overlapping", accelerator="E", 
                             command=lambda x=self.atom3i, e=self.event: \
                              x.UI_Statechart.event("<KeyPress-e>", e)) 
#                              x.UI_Statechart.event("Edit Overlap",e)) 
                              
def addDragOverlap(self):
  self.popupMenu.add_command(label="Drag Overlapping", accelerator="D", 
                             command=lambda x=self.atom3i, e=self.event: \
                              x.UI_Statechart.event("<KeyPress-d>", e)) 
#                             x.UI_Statechart.event("Drag Overlap",e)) 
                                                
def addSelectAll(self):
  self.popupMenu.add_command(label="Select All", accelerator= "Ctrl-A", 
                        command=lambda x=self.atom3i, e=self.event: \
                             x.UI_Statechart.event("<Control-KeyPress-a>", e)) 
#                            x.UI_Statechart.event("Select All",e)) 
                        
def addDeselectAll(self):
  self.popupMenu.add_command(label="Deselect All", accelerator= "Ctrl-D", 
                        command=lambda x=self.atom3i, e=self.event: \
                            x.UI_Statechart.event("<Control-KeyPress-d>", e)) 
  
  
def addClear(self):
  self.popupMenu.add_command(label="Clear Selected", accelerator= "Delete", 
                          command=lambda x=self.atom3i, e=self.event: \
                              x.UI_Statechart.event("<KeyPress-Delete>", e)) 
#                              x.UI_Statechart.event("Delete",e)) 
                              
def addInsertPoint(self):
  self.popupMenu.add_command(label="Insert Control Knob", accelerator= "Insert", 
                             command=lambda x=self.atom3i, e=self.event: \
                              x.UI_Statechart.event("<KeyPress-Insert>", e)) 
#                              x.UI_Statechart.event("Insert Point",e)) 
def addDeletePoint(self):
  self.popupMenu.add_command(label="Delete Active Control Knob", 
                             accelerator= "Delete", 
                             command=lambda x=self.atom3i, e=self.event: \
                       x.UI_Statechart.event("<Control-KeyPress-Delete>", e)) 
#                              x.UI_Statechart.event("Delete",e)) 
def addSmoothSelected( self ):
  self.popupMenu.add_command(label="Toggle Selection Smoothness",accelerator= "S",
                             command=lambda x=self.atom3i,e=self.event: \
                              x.UI_Statechart.event("<KeyPress-s>",e))  
#                              x.UI_Statechart.event("Smooth",e))  
def addToggleSmoothMode( self ):
  if( self.optionsDatabase.get(self.atom3i.SMOOTH_ARROWS) ):
    label = "Spline arrows by default"
  else:
    label = "Straight arrows by default"
  self.popupMenu.add_command(label=label,accelerator="F9",
                             command=lambda x=self.atom3i,e=self.event: \
                              x.UI_Statechart.event("<KeyPress-F9>",e)) 
#                              x.UI_Statechart.event("Smooth Default",e)) 
      
     
def addCut( self ):
  self.popupMenu.add_command(label="Cut", accelerator="Ctrl-X",
                             command=lambda x=self.atom3i,e=self.event: \
                              x.UI_Statechart.event("<Control-KeyPress-x>",e)) 
#                              x.UI_Statechart.event("Cut",e)) 
def addCopy( self ):
  self.popupMenu.add_command(label="Copy", accelerator="Ctrl-C",
                             command=lambda x=self.atom3i,e=self.event: \
                              x.UI_Statechart.event("<Control-KeyPress-c>",e)) 
#                              x.UI_Statechart.event("Copy",e)) 
def addPaste( self ):
  if( self.cb.isCopyBufferInitilized() ):   state = "normal"
  else:                                     state = "disabled"  
  self.popupMenu.add_command(label="Paste", accelerator="Ctrl-V",state=state,
                             command=lambda x=self.atom3i,e=self.event: \
                              x.UI_Statechart.event("<Control-KeyPress-v>",e)) 
#                              x.UI_Statechart.event("Paste",e)) 
         
                              
def addCopyAttributes( self ):
  self.popupMenu.add_command(label="Copy Attributes", accelerator="Alt-C",
                             command=lambda x=self.atom3i,e=self.event: \
                              x.UI_Statechart.event("<Alt-KeyPress-c>",e)) 
#                              x.UI_Statechart.event("Copy Attributes",e)) 
def addPasteAttributes( self ):  
  if( self.cb.isAttributesBufferInitilized() ):   state = "normal"
  else:                                           state = "disabled" 
  self.popupMenu.add_command(label="Paste Attributes", accelerator="Alt-V",
                             state=state,
                             command=lambda x=self.atom3i,e=self.event: \
                              x.UI_Statechart.event("<Alt-KeyPress-v>",e)) 
#                              x.UI_Statechart.event("Paste Attributes",e)) 
                    
                              
def addUndo( self ):  
  if( self.atom3i.undoer.isUndoable() ):  state = "normal"
  else:                                   state = "disabled"    
  self.popupMenu.add_command(label="Undo", accelerator="Ctrl-Z",state=state,
                             command=lambda x=self.atom3i,e=self.event: \
                              x.UI_Statechart.event("<Control-KeyPress-z>",e)) 
#                              x.UI_Statechart.event("Undo",e)) 
def addRedo( self ):  
  if( self.atom3i.undoer.isRedoable() ):  state = "normal"
  else:                                   state = "disabled"  
  self.popupMenu.add_command(label="Redo", accelerator="Ctrl-Y",state=state,
                             command=lambda x=self.atom3i,e=self.event: \
                              x.UI_Statechart.event("<Control-KeyPress-y>",e)) 
#                              x.UI_Statechart.event("Redo",e)) 
                              
          
                          
# --------------------------------  SUB-MENUS --------------------------------
  
def addLayoutMenu(self):
    menu = Menu(self.popupMenu, tearoff = 0, bg = "white")  
    assembleLayoutMenu(self.atom3i, menu)
    self.popupMenu.add_cascade(label="Layout Menu", underline=0, 
                               accelerator= "L", menu=menu)
                               
def addExportMenu(self):
    menu = Menu(self.popupMenu, tearoff = 0, bg = "white")  
    assembleExporterMenu(self.atom3i, menu)
    self.popupMenu.add_cascade(label="Export Menu", underline=0, menu=menu)

def addModelMenu(self):
    #menu = Menu(self.popupMenu, tearoff = 0, bg = "white")  
    menu = self.atom3i.modelMenu
    #assembleModelMenu( self.atom3i, menu )
    self.popupMenu.add_cascade(label="Model Menu", underline=0, 
                               accelerator= "M", menu=menu)
  
def addTransformationMenu(self):
    menu = Menu(self.popupMenu, tearoff = 0, bg = "white")  
    assembleTransformationMenu(self.atom3i, menu)
    self.popupMenu.add_cascade(label="Transformation Menu", underline=0, 
                               accelerator= "T", menu=menu)
    
def addFileMenu(self):    
    menu = Menu(self.popupMenu, tearoff = 0, bg = "white")  
    assembleFileMenu(self.atom3i, menu)
    self.popupMenu.add_cascade(label="File Menu", underline=0, 
                               accelerator= "F", menu=menu) 

def addExit(self):  
  self.popupMenu.add_command(label="Exit AToM3", 
                        command=lambda x=self.atom3i, e=self.event: \
                        x.UI_Statechart.event("<Alt-x>", e), 
#                        x.UI_Statechart.event("Exit", e), 
                        underline = 1, accelerator="Alt-X")
        
#--------------------------------- EDITORS -----------------------------------
                       
def addArrowEditor( self ):
  self.popupMenu.add_command(label="Arrow Editor", 
                             accelerator="Shift-Right-Click",
                             command=lambda x=self.atom3i,e=self.event: \
                            x.UI_Statechart.event("<Shift-ButtonPress-3>",e)) 
#                              x.UI_Statechart.event("Edit Arrow",e)) 
  
def addArrowEditorExit( self ):
  self.popupMenu.add_command(label="Exit Arrow Editor", 
                             accelerator="Left-Click",
                             command=lambda x=self.atom3i,e=self.event: \
                              x.UI_Statechart.event("<ButtonPress-1>",e)) 
#                              x.UI_Statechart.event("Edit Arrow",e)) 
                              
def addResizeEntity(self):
  
  self.popupMenu.add_command(label="Resize Selected",accelerator="R",
                              command=lambda x=self.atom3i,event=self.event: \
                              x.UI_Statechart.event("<KeyPress-r>",event) )
#                              x.UI_Statechart.event("Scale Selection",event) )
      
      
def addNodeLabelMoveToggle(self):
  """ For use with the arrow editor & an intermediate object control point """
  
  editor = self.atom3i.arrowEditor
  if(editor.isMoveLabelDrawingMode()):
    label = "Disable label movement mode"
  else:
    label = "Enable label movement mode" 
      
  self.popupMenu.add_command(label=label, accelerator="Spacebar", 
    command=lambda e=self.event, x=self.atom3i.UI_Statechart: 
      x.event("<KeyPress-space>", e))
#      x.event("Move Label Toggle", e))
           
def addNodeLabelDragToggle(self):
  """ For use with the main dragging method """
  
  if(self.cb.isLabelDragMode()):
    label = "Disable label dragging"
  else:
    label = "Enable label dragging" 
    
  self.popupMenu.add_command(label=label, accelerator="Spacebar", 
    command=lambda x=self.atom3i.UI_Statechart: x.event("<KeyPress-space>"))
#    command=lambda x=self.atom3i.UI_Statechart: x.event("Toggle Label Drag"))
                                 
#-------------------------------- UTILITIES ----------------------------------
  
def addOpenLastModel(self):  

  menu = Menu(self.popupMenu, tearoff = 0, bg = "white")    
  addOpenLastModelSubroutine(self, menu)      
  self.popupMenu.add_cascade(label="Open Recent Model", accelerator = "F6", 
                               menu=menu) 
                               
def addOpenLastModelSubroutine(self, menu):
  fileNameList = self.optionsDatabase.get(self.atom3i.LASTOPEN_MODEL)
  
  # Cleanup the list
  cleanList = []
  for fileName in fileNameList:
    if(os.path.exists(fileName)):
        cleanList.append(fileName)
  self.optionsDatabase.set(self.atom3i.LASTOPEN_MODEL, cleanList)
    
  menu.add_command(label="Recent Models Menu", accelerator = "F6", 
                   command=lambda e=self.event: self.LastModelPopup(e)) 
  menu.add_separator()
  if(len(cleanList) < 1):
      menu.add_command(label="--- EMPTY ---") 
      
  for fileName in cleanList:
    menu.add_command(label=str(fileName), 
                     command=lambda x=self.atom3i, y=fileName: x.open(y))

def addOpenLastMetaModel(self):  
  menu = Menu(self.popupMenu, tearoff = 0, bg = "white")    
  addOpenLastMetaModelSubroutine(self, menu)
  self.popupMenu.add_cascade(label="Open Recent Meta-Model", 
                             accelerator = "F7", menu=menu) 

def addOpenLastMetaModelSubroutine(self, menu):
  fileNameList = self.optionsDatabase.get(self.atom3i.LASTOPEN_MMODEL)
  # Cleanup the list
  cleanList = []
  for fileName in fileNameList:
    if(os.path.exists(fileName)):
        cleanList.append(fileName)
  self.optionsDatabase.set(self.atom3i.LASTOPEN_MMODEL, cleanList)
        
  menu.add_command(label="Recent Meta-Model Models Menu", accelerator = "F7", 
                   command=lambda e=self.event: self.LastMetaModelPopup(e)) 
  menu.add_separator() 
  if(len(cleanList) < 1):
      menu.add_command(label="--- EMPTY ---") 
                            
  for fileName in cleanList:
    menu.add_command(label=str(fileName), 
                     command=lambda x=self.atom3i, y=fileName: 
                       x.openMetaModel(fileName=y))
                               
                               
def addSourcePath(self):
  
  menu = Menu(self.popupMenu, tearoff = 0, bg = "white")    
  addSourcePathSubroutine(self, menu) 
  self.popupMenu.add_cascade(label="Source Paths", menu=menu, 
                             accelerator = "F8")       
    
def addSourcePathSubroutine(self, menu):
    
  menu.add_command(label="Source Path Menu", accelerator = "F8", 
                   command=lambda e=self.event: self.SourcePathPopup(e))   
  menu.add_separator()
    
  menu.add_command(label="Add Source Path", 
                   command=lambda x=self.atom3i: x.sourcePathManager(0))
  menu.add_command(label="Remove Source Path", 
                   command=lambda x=self.atom3i: x.sourcePathManager(1))
  menu.add_command(label="Source Path Conflict Finder", 
                   command=lambda x=self.atom3i: x.sourcePathManager(2))                  
  menu.add_command(label="Source Path Help", 
                   command=lambda x=self.atom3i: x.sourcePathManager(3))    
   

         


      
 