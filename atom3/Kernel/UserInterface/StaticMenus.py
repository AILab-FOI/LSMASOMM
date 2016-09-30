"""
StaticMenus.py

A convenient place to keep all the static AToM3 menus together.

Created June 26, 2004 by Denis Dube
"""

from Tkinter import Menu,IntVar
import RandomLayout  
#import ForceTransfer 

import ZoomFocus 
import SnapGrid
#import SpringLayout
import ArrowOptimizer
#import CircleLayout
#import TreeLikeLayout
#from HierarchicalLayout import HierarchicalLayout

from AToM3LayoutInterface import doHierarchicalLayout
from AToM3LayoutInterface import doSpringLayout
from AToM3LayoutInterface import doForceTransfer
from AToM3LayoutInterface import doTreeLikeLayout
from AToM3LayoutInterface import doCircleLayout
    
from Export_Import_GML import exportImportDialog
from Utilities         import modelChange, optimizeConnectionPorts

def buildAllMenus(self):
  """ Creates all the menus and stores them in AToM3 instance """
  
  # Root menu
  self.mmtoolMenu = Menu( self.parent )
  
  # File menu
  self.filemenu = Menu(self.mmtoolMenu, tearoff=0)
  assembleFileMenu( self, self.filemenu )
  
  # Model menu  
  self.modelMenu = Menu(self.mmtoolMenu, tearoff=0)
  assembleModelMenu(self, self.modelMenu )
  
  # Transformation menu
  if( self.IsMainKernel ):
    self.transMenu = Menu(self.mmtoolMenu, tearoff = 0)
    assembleTransformationMenu( self, self.transMenu )
  
  # Layout menu
  self.layoutMenu = Menu(self.mmtoolMenu, tearoff = 0)  
  assembleLayoutMenu( self, self.layoutMenu )
  
  # Export menu
  self.exportMenu = Menu(self.mmtoolMenu, tearoff = 0)  
  assembleExporterMenu( self, self.exportMenu )
  
  # Menu is initially inactive (ie: not displayed at the top of the application)
  self.mmtoooMenuActive = False
  
  # Check options database if the menu should start active
  if(self.optionsDatabase.get(self.STATIC_MENUBAR) and self.IsMainKernel):
    toggleMainToolMenu(self)
   
    
    
    
def toggleMainToolMenu(self, setState=None ):
  """ 
  Toggles the static menu bar on/off 
  If setState is True, then we want the toolmenu ACTIVE
  If setState is False, then we want the toolmenu DISABLED
  """
  
  if( self.mmtoooMenuActive and setState != True ):
    #self.parent.config(menu=None)  
    self.mmtoolMenu.delete(0,10)
    self.mmtoooMenuActive = False
  elif( setState != False ):
    self.mmtoolMenu.add_cascade(label="File Menu", menu = self.filemenu   )
    self.mmtoolMenu.add_cascade(label="Model Menu", menu = self.modelMenu   )
    if( self.IsMainKernel ):  
      self.mmtoolMenu.add_cascade(label="Transformation Menu", menu = self.transMenu )
    self.mmtoolMenu.add_cascade(label="Layout Menu", menu = self.layoutMenu   )
    self.mmtoolMenu.add_cascade(label="Export Menu", menu = self.exportMenu   )
    self.parent.config(menu=self.mmtoolMenu)
    self.mmtoooMenuActive = True
  
    
    
def assembleLayoutMenu(self, menu):
  """ Creates the layout menu """
          
  def handler():
    doHierarchicalLayout(self, self.cb.buildSelectionObjectSet())
    modelChange(self) # Model changed, update statusbar & undo
  menu.add_command(label='Hiearchical Layout', accelerator="Ctrl-1", 
                   command = handler)   
          
  def handler():
    doSpringLayout(self, self.cb.buildSelectionObjectSet())
    modelChange(self) # Model changed, update statusbar & undo
  menu.add_command(label='Spring Layout', accelerator="Ctrl-2"
                    , command=handler ) 

  def handler():
      doForceTransfer(self, self.cb.buildSelectionObjectSet())
      modelChange(self) # Model changed, update statusbar & undo
  menu.add_command(label='Force Transfer', accelerator="Ctrl-3"
                    , command=handler )  
         
  def handler():
    doTreeLikeLayout(self, self.cb.buildSelectionObjectSet())
    modelChange(self) # Model changed, update statusbar & undo
  menu.add_command(label='Tree-like Layout', accelerator="Ctrl-4", 
                   command = handler) 
         
  def handler():
    doCircleLayout(self, self.cb.buildSelectionObjectSet())
    modelChange(self) # Model changed, update statusbar & undo
  menu.add_command(label='Circle Layout', accelerator="Ctrl-5", 
                   command = handler) 
                                    
  def handler():
    RandomLayout.applyLayout(self)
    modelChange(self) # Model changed, update statusbar & undo
  menu.add_command(label='Random Layout', command=handler) 
  
  
  menu.add_separator()                         
      
  menu.add_command(label='Zoom & Fit Graph', accelerator="Z", 
               command=lambda s=self: s.UI_Statechart.event("<KeyPress-z>") ) 
      
  def handler():
      selection = self.cb.buildSelectionObjectSet()
      ArrowOptimizer.applyLayout(atom3i=self, selection=selection)
      modelChange(self) # Model changed, update statusbar & undo
  menu.add_command(label='Arrow Optimizer', accelerator="F12"
                    , command=handler )  
      
  def handler():
    ArrowOptimizer.applyLayout(self,settings=True, selection=self.cb.buildSelectionObjectSet())
    modelChange(self) # Model changed, update statusbar & undo
  menu.add_command(label='Arrow Optimizer Settings', command=handler) 
  
  menu.add_command(label='Toggle Snap Grid', accelerator="F10"
                    , command=self.toggleSnapGrid) 
                        
  menu.add_command(label='Snap Grid Settings', \
                          command=lambda x=self,settings=True: \
                          SnapGrid.applyLayout(x,settings) ) 

                                           
                          
def assembleTransformationMenu(self, menu):
  """ Creates the transformation menu """

  menu.add_command(label="Load transformation", command = self.loadTrans, underline = 0 )
  menu.add_command(label="Save transformation", command = self.saveTrans, underline = 0 )
  menu.add_command(label="Edit transformation", command = self.editTrans, underline = 0 )
  menu.add_command(label="Create transformation", command = self.createTrans, underline = 0 )  
  menu.add_separator()
  menu.add_command(label="Generate documentation", command = self.genTransDocumentation, underline = 0 )  
  menu.add_command(label="Generate code for transformation", command = self.genCode4Trans, underline = 0 )
  menu.add_command(label="Execute transformation", command = self.executeTrans, underline = 1 )
  
    
def assembleModelMenu(self, menu):
  """ Creates the model menu """
  try: 
    # This part is implemented in the meta-model (and seems rather broken!)
    self.createModelMenu(self, menu)   
  except: 
    pass #menu = Menu( self.parent )
  
  menu.add_separator()
  menu.add_command(label="Insert model", command=self.newModeModel)
  menu.add_command(label="Expand model", command=self.expandModeModel, underline = 1 )

  menu.add_separator()
  menu.add_command(label="Edit model attributes", 
                                 command=self.modelAttributes, underline = 11 )
  menu.add_command(label="Edit types", command=self.editTypes, underline = 5 )
  if self.IsMainKernel:
      menu.add_separator()
      def handler(self, event=None):
        import Dialog
        dialog = Dialog.Dialog(None, {'title': 'Code Generation Warning',
                    'text': 'Please use the GEN (generate) button in the ' 
                            + 'formalism\'s toolbar',
                    'bitmap': 'warning',
                    'default': 0,
                    'strings': ('Abort','Continue, I know what I\'m doing')})
        if(dialog.num == 0):
          return
        else:
          self.genCode()
      menu.add_command(label="Generate code", 
                       command=lambda s=self, e=None: handler(s, e))


def assembleFileMenu(self, menu):
  """ Creates the filemenu """
    
#  menu.add_command(label="Open model",accelerator="Ctrl-O", 
#                    command= lambda s=self: s.UI_Statechart.event("Open") )
#  
#  menu.add_command(label="Save model",  accelerator="Ctrl-S", 
#                    command= lambda s=self: s.UI_Statechart.event("Save") )
#            
#  menu.add_command(label="Save as...", underline = 5, accelerator="Alt-S", 
#                    command= lambda s=self: s.UI_Statechart.event("Save As") )

  menu.add_command(label="Open model", accelerator="Ctrl-O", 
                    command= lambda s=self: s.open())
  menu.add_command(label="Save model", accelerator="Ctrl-S", 
                    command= lambda s=self: 
        s.save(0, s.statusbar.getState(s.statusbar.MODEL)[1][0]))
  menu.add_command(label="Save as...", accelerator="Alt-S", 
                    command= lambda s=self: s.save(0))  
                                   
  # Does anyone even use this? All it does is generates fewer import statements
  # It is also very confusing given my export module...
  #menu.add_command(label="Export model", command= lambda x=self: x.save(1))
    
  menu.add_command(label="Generate PostScript from model", accelerator="F5", 
          command= lambda s=self: s.UI_Statechart.event("Postscript",[200,200])
          , underline = 9)
                   
  menu.add_separator()
  
  menu.add_command(label="Open meta-model", accelerator="F3",underline = 5, 
              command= lambda s=self: s.openMetaModel() )
#              command= lambda s=self: s.UI_Statechart.event("Open Metamodel") )
                   
  menu.add_command(label="Close meta-model", accelerator="F4", underline = 1, 
              command= lambda s=self: s.closeMetaModel() )
#              command= lambda s=self: s.UI_Statechart.event("Close Metamodel") )
                  
  # Only generate this if we are a main window...
  if( self.IsMainKernel ):								
      menu.add_separator()
      menu.add_command(label="Show console", accelerator="F2", underline = 1, 
              command= lambda s=self: s.showConsole() )
                       
      def handler():
        if(self.optionsDatabase.showOptionsDatabase()):
          self.loadImmediateOptions()  
      menu.add_command(label="Options", accelerator="F1", underline = 2, 
              command=handler)
#              command= lambda s=self: s.UI_Statechart.event("Options") )
         
  menu.add_separator()
  
  def handler():
    self.cb.clearSelectionDict()
    self.clearModel()
    modelChange(self) # Model changed, update statusbar & undo
  menu.add_command(label="Clear model", accelerator="Ctrl-Delete", 
                command=handler)
#            command= lambda s=self: s.UI_Statechart.event("Clear Canvas") )
              
  menu.add_command(label="Exit", underline = 1, accelerator="Alt-X",
              command= lambda s=self: s.exitFromATOM3() )
#              command= lambda s=self: s.UI_Statechart.event("Exit") )
              
              
def assembleExporterMenu(self, menu):
  """ Creates the exporter menu """
     
  self.exporter.assembleExportMenu( menu )
  menu.add_separator()
  menu.add_command( label='Instant GML Export/Import', 
                    command=lambda x=self: exportImportDialog(x) )
                    