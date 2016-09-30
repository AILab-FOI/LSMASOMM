"""
KeyBinds.py

This module recieves direct calls from the AToM3 kernel mouse&key bindings.
It interprets each mouse & key press as an action/s and sends that action to the 
UI statechart that then decides what behaviour will occur, depending on what
previous actions were taken, and where the mouse is, etc...
 
Created June 15, 2004 by Denis Dube
"""

import Tkinter

from AToM3LayoutInterface import doHierarchicalLayout
from AToM3LayoutInterface import doSpringLayout
from AToM3LayoutInterface import doForceTransfer
from AToM3LayoutInterface import doTreeLikeLayout
from AToM3LayoutInterface import doCircleLayout


def createBindings(self, canvas, tkRoot):
  """ Binds up the cavnas and the tkRoot window """
  
  #------------------------- Mouse 1, Left Button  ---------------------------
 
#  def handler(event):
#    self.UI_Statechart.event("Fresh Selection", event)  
#    self.UI_Statechart.event("Select Point", event)
#    self.UI_Statechart.event("Drop Point", event)
#    self.UI_Statechart.event("Start Drag", event)     
#    self.popupMenuCreator.popupRemover()
#  canvas.bind("<ButtonPress-1>", handler)

  def buttonPress1Handler(self, event):
    self.UI_scope('<ButtonPress-1>', event)
    self.popupMenuCreator.popupRemover()
  canvas.bind("<ButtonPress-1>", lambda event, s=self: 
                                     buttonPress1Handler(s, event))                                           

#  def handler(event):      
#    self.UI_Statechart.event("Finish Selection", event)
#    self.UI_Statechart.event("Finish Drag", event)
#    self.UI_Statechart.event("Finish Scale", event) 
#  canvas.bind("<Any-ButtonRelease-1>", handler)  

  canvas.bind("<Any-ButtonRelease-1>", lambda event, zone=self.UI_scope: 
                                        zone('<Any-ButtonRelease-1>', event))  
  
  #todo: WARNING: Drop point will not work with control modifier now
#  def handler(event):
#    self.UI_Statechart.event("Drop Point", event)
#    self.UI_Statechart.event("Create New Arrow", event)    
#  canvas.bind("<Control-ButtonPress-1>", handler)  
  canvas.bind("<Control-ButtonPress-1>", lambda event, zone=self.UI_scope: 
                                       zone('<Control-ButtonPress-1>', event)) 

#  canvas.bind("<Shift-ButtonPress-1>", lambda event, s=self: \
#                            s.UI_Statechart.event("Additive Selection", event)) 
  
  canvas.bind("<Shift-ButtonPress-1>", lambda event, zone=self.UI_scope: 
                                       zone('<Shift-ButtonPress-1>', event))   
                            
#  def handler(event):    
#    self.UI_Statechart.event("Edit Arrow", event)    
#  canvas.bind("<Double-ButtonPress-1>", handler)  
  
  canvas.bind("<Double-ButtonPress-1>", lambda event, zone=self.UI_scope: 
                                       zone('<Double-ButtonPress-1>', event))
                            
  #**** WARNING: Already bound on Linux desktop ( Window movement )
#  canvas.bind("<Alt-ButtonPress-1>", lambda event, s=self: \
#                            s.UI_Statechart.event("Negative Selection", event)) 
  canvas.bind("<Alt-ButtonPress-1>", lambda event, zone=self.UI_scope: 
                                       zone('<Alt-ButtonPress-1>', event))
  #**** 
  
  
  #------------------------ Mouse 2, Middle Button ---------------------------
  
  #todo: WARNING: Middle mouse will not start negative selection anymore
  #****  WARNING: Already bound on Windows desktop ( Scrollbar navigation )
#  canvas.bind("<ButtonPress-2>", lambda event, s=self: \
#                           s.UI_Statechart.event("Negative Selection", event))
#  canvas.bind("<Any-ButtonRelease-2>", lambda event, s=self: \
#                           s.UI_Statechart.event("Finish Selection", event)) 
  canvas.bind("<ButtonPress-2>", lambda event, zone=self.UI_scope: 
                                       zone('<ButtonPress-2>', event))
  canvas.bind("<Any-ButtonRelease-2>", lambda event, zone=self.UI_scope: 
                                       zone('<Any-ButtonRelease-2>', event))
  #**** 


  #------------------------ Mouse 3, Right Button ----------------------------
  
#  def handler(event):    
#    self.UI_Statechart.event("Popup Menu", event)
#    self.UI_Statechart.event("Done", event)
#    self.UI_Statechart.event("Rollback", event)
#    self.UI_Statechart.event("Reset Scale", event)
#  canvas.bind("<ButtonPress-3>", handler)  

  canvas.bind("<ButtonPress-3>", lambda event, zone=self.UI_scope: 
                                       zone('<ButtonPress-3>', event))
  
#  def handler(event):
#    self.UI_Statechart.event("Model Action", event)
#    self.popupMenuCreator.popupRemover()
#  canvas.bind("<Control-ButtonPress-3>", handler)  

  def buttonPress3Handler(self, event):
    self.UI_scope('<Control-ButtonPress-3>', event)
    self.popupMenuCreator.popupRemover()
  canvas.bind("<Control-ButtonPress-3>", lambda event, s=self: 
                                     buttonPress3Handler(s, event))       

  
#  def handler(event):
#    self.UI_Statechart.event("Edit Arrow", event)
#    self.popupMenuCreator.popupRemover()
#  canvas.bind("<Shift-ButtonPress-3>", handler)  

  def shiftButtonPress3Handler(self, event):
    self.UI_scope('<Shift-ButtonPress-3>', event)
    self.popupMenuCreator.popupRemover()
  canvas.bind("<Shift-ButtonPress-3>", lambda event, s=self: 
                                     shiftButtonPress3Handler(s, event))
  
  #-------------------------------- Mouse Motion -----------------------------
  
#  canvas.bind("<Any-Motion>", lambda event, s=self: \
#                                        s.UI_Statechart.event("Motion", event))

  canvas.bind("<Any-Motion>", lambda event, zone=self.UI_scope: 
                                       zone('<Any-Motion>', event))
    
  #------------------------------ Keyboard Binds -----------------------------
  
  # Since the canvas widget steadfastly refuses to be binded with mere keystrokes
  # the keys are binded to the Tk root window. Unfortunately, this means that
  # there is a position offset to the Canvas widget. The convert utility handles
  # this.
  conv = self.cb.convertRootToCanvasEvent  
    
  #--------------------------- Precise Movement ------------------------------
  
#  tkRoot.bind("<KeyPress-Up>", lambda event, s=self: \
#                              s.UI_Statechart.event("Move Up", conv(event)))
#  tkRoot.bind("<KeyPress-Down>", lambda event, s=self: \
#                             s.UI_Statechart.event("Move Down", conv(event)))
#  tkRoot.bind("<KeyPress-Left>", lambda event, s=self: \
#                             s.UI_Statechart.event("Move Left", conv(event)))
#  tkRoot.bind("<KeyPress-Right>", lambda event, s=self: \
#                            s.UI_Statechart.event("Move Right", conv(event)))

  tkRoot.bind("<KeyPress-Up>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-Up>', conv(event)))
  tkRoot.bind("<KeyPress-Down>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-Down>', conv(event)))
  tkRoot.bind("<KeyPress-Left>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-Left>', conv(event)))
  tkRoot.bind("<KeyPress-Right>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-Right>', conv(event)))
                                                    
  #------------------------------- Editing -----------------------------------

#  tkRoot.bind("<Control-KeyPress-a>", lambda event, s=self: \
#                           s.UI_Statechart.event("Select All", conv(event)))
#  tkRoot.bind("<Control-KeyPress-d>", lambda event, s=self: \
#                           s.UI_Statechart.event("Deselect All", conv(event)))
#
#  tkRoot.bind("<KeyPress-Delete>", lambda event, s=self: \
#                           s.UI_Statechart.event("Delete", conv(event)))
#  tkRoot.bind("<Shift-KeyPress-Delete>", lambda event, s=self: \
#                           s.UI_Statechart.event("EntityDelete", conv(event)))  
             
  tkRoot.bind("<Control-KeyPress-a>", lambda event, zone=self.UI_scope: 
                                       zone('<Control-KeyPress-a>', conv(event)))
  tkRoot.bind("<Control-KeyPress-d>", lambda event, zone=self.UI_scope: 
                                       zone('<Control-KeyPress-d>', conv(event)))
  tkRoot.bind("<KeyPress-Delete>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-Delete>', conv(event)))
  tkRoot.bind("<Shift-KeyPress-Delete>", lambda event, zone=self.UI_scope: 
                                  zone('<Shift-KeyPress-Delete>', conv(event)))
  
  #todo: WARNING: key i no longer inserts points
#  tkRoot.bind("<KeyPress-Insert>", lambda event, s=self: \
#                           s.UI_Statechart.event("Insert Point", conv(event)))
#  tkRoot.bind("<KeyPress-i>", lambda event, s=self: \
#                           s.UI_Statechart.event("Insert Point", conv(event)))
#  
#  tkRoot.bind("<Control-KeyPress-Delete>", lambda event, s=self: \
#                          s.UI_Statechart.event("Clear Canvas", conv(event)))
#
#  tkRoot.bind("<KeyPress-s>", lambda event, s=self: \
#                          s.UI_Statechart.event("Smooth", conv(event)))

  tkRoot.bind("<KeyPress-Insert>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-Insert>', conv(event)))
  tkRoot.bind("<KeyPress-i>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-i>', conv(event)))
  tkRoot.bind("<Control-KeyPress-Delete>", lambda event, zone=self.UI_scope: 
                               zone('<Control-KeyPress-Delete>', conv(event)))
  tkRoot.bind("<KeyPress-s>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-s>', conv(event)))
              
#  tkRoot.bind("<KeyPress-e>", lambda event, s=self: \
#                          s.UI_Statechart.event("Edit Overlap", conv(event)))
#       
#  tkRoot.bind("<KeyPress-r>", lambda event, s=self: \
#                          s.UI_Statechart.event("Scale Selection", conv(event)))
#                              
#    
#  tkRoot.bind("<KeyPress-d>", lambda event, s=self: \
#                          s.UI_Statechart.event("Drag Overlap", conv(event)))
    
  tkRoot.bind("<KeyPress-e>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-e>', conv(event)))
  tkRoot.bind("<KeyPress-r>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-r>', conv(event)))
  tkRoot.bind("<KeyPress-d>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-d>', conv(event)))

  #todo: WARNING: Return/Enter key no longer signals "DONE"
#  def handler(event):
#    self.UI_Statechart.event("Toggle Snap", conv(event))
#    self.UI_Statechart.event("Toggle Label Drag")
#    self.UI_Statechart.event("Move Label Toggle", conv(event))
#  tkRoot.bind("<KeyPress-space>", handler)  
#           
#  def handler(event):
#    self.UI_Statechart.event("Done")   
#  tkRoot.bind("<KeyPress-Return>", handler)      
  
  tkRoot.bind("<KeyPress-space>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-space>', conv(event)))
  tkRoot.bind("<KeyPress-Return>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-Return>', conv(event)))
  
  #--------------------------------- Menus -----------------------------------

#  tkRoot.bind("<KeyPress-l>", lambda event, s=self: \
#                              s.UI_Statechart.event("Layout Menu", conv(event)))
#  tkRoot.bind("<KeyPress-t>", lambda event, s=self: \
#                              s.UI_Statechart.event("Trans. Menu", conv(event)))
#  tkRoot.bind("<KeyPress-m>", lambda event, s=self: \
#                              s.UI_Statechart.event("Model Menu", conv(event)))
#  tkRoot.bind("<KeyPress-f>", lambda event, s=self: \
#                              s.UI_Statechart.event("File Menu", conv(event)))

  tkRoot.bind("<KeyPress-l>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-l>', conv(event)))
  tkRoot.bind("<KeyPress-t>", self.editTrans)
  #tkRoot.bind("<KeyPress-t>", lambda event, zone=self.UI_scope: 
  #                                     zone('<KeyPress-t>', conv(event)))
  tkRoot.bind("<KeyPress-m>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-m>', conv(event)))
  tkRoot.bind("<KeyPress-f>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-f>', conv(event)))
                 
  #--------------------------------- File Ops --------------------------------
  
#  tkRoot.bind('<Alt-X>', lambda event, s=self: \
#                        s.UI_Statechart.event("Exit"))
#  tkRoot.bind('<Alt-x>', lambda event, s=self: \
#                        s.UI_Statechart.event("Exit")) 

  tkRoot.bind("<Alt-x>", lambda event, zone=self.UI_scope: 
                                       zone('<Alt-x>', conv(event)))
  
#  tkRoot.bind("<Control-KeyPress-o>", lambda event, s=self: \
#                                s.UI_Statechart.event("Open", conv(event)))
#  tkRoot.bind("<Control-KeyPress-s>", lambda event, s=self: \
#                                s.UI_Statechart.event("Save", conv(event)))
#  tkRoot.bind("<Alt-KeyPress-s>", lambda event, s=self: \
#                                s.UI_Statechart.event("Save As", conv(event)))

  tkRoot.bind("<Control-KeyPress-o>", lambda event, zone=self.UI_scope: 
                                       zone('<Control-KeyPress-o>', conv(event)))
  tkRoot.bind("<Control-KeyPress-s>", lambda event, zone=self.UI_scope: 
                                       zone('<Control-KeyPress-s>', conv(event)))
  tkRoot.bind("<Alt-KeyPress-s>", lambda event, zone=self.UI_scope: 
                                       zone('<Alt-KeyPress-s>', conv(event)))
   
                           
#  tkRoot.bind("<KeyPress-F1>", lambda event, s=self: \
#                     s.UI_Statechart.event("Options", conv(event)))
#  tkRoot.bind("<KeyPress-F2>", lambda event, s=self: \
#                     s.UI_Statechart.event("Show Console", conv(event))) 
#  tkRoot.bind("<KeyPress-F3>", lambda event, s=self: \
#                     s.UI_Statechart.event("Open Metamodel", conv(event)))
#  tkRoot.bind("<KeyPress-F4>", lambda event, s=self: \
#                     s.UI_Statechart.event("Close Metamodel", conv(event)))
#  tkRoot.bind("<KeyPress-F5>", lambda event, s=self: \
#                     s.UI_Statechart.event("Postscript", conv(event)))
#  tkRoot.bind("<KeyPress-F6>", lambda event, s=self: \
#                     s.UI_Statechart.event("Recent Model", conv(event)))
#  tkRoot.bind("<KeyPress-F7>", lambda event, s=self: \
#                     s.UI_Statechart.event("Recent Metamodel", conv(event)))
#  tkRoot.bind("<KeyPress-F8>", lambda event, s=self: \
#                     s.UI_Statechart.event("Source Paths", conv(event))) 
                     
  tkRoot.bind("<KeyPress-F1>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F1>', conv(event)))
  tkRoot.bind("<KeyPress-F2>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F2>', conv(event)))
  tkRoot.bind("<KeyPress-F3>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F3>', conv(event)))
  tkRoot.bind("<KeyPress-F4>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F4>', conv(event)))
  tkRoot.bind("<KeyPress-F5>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F5>', conv(event)))
  tkRoot.bind("<KeyPress-F6>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F6>', conv(event)))
  tkRoot.bind("<KeyPress-F7>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F7>', conv(event)))
  tkRoot.bind("<KeyPress-F8>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F8>', conv(event)))
                                         
  # -------------------------- Graphics / Layout -----------------------------
  
#  tkRoot.bind("<KeyPress-F9>", lambda event, s=self: \
#                        s.UI_Statechart.event("Smooth Default", conv(event))) 
#  tkRoot.bind("<KeyPress-F10>", lambda event, s=self: \
#                        s.UI_Statechart.event("Snap Grid Toggle", conv(event))) 
#  tkRoot.bind("<KeyPress-F11>", lambda event, s=self: \
#                        s.UI_Statechart.event("Spring Layout", conv(event)))
#  tkRoot.bind("<KeyPress-F12>", lambda event, s=self: \
#                        s.UI_Statechart.event("Arrow Optimizer", conv(event)))
#  tkRoot.bind("<Control-KeyPress-f>", lambda event, s=self: \
#                        s.UI_Statechart.event("Force Layout", conv(event)))
#  tkRoot.bind("<KeyPress-z>", lambda event, s=self: \
#                        s.UI_Statechart.event("Zoom Layout", conv(event)))

  tkRoot.bind("<KeyPress-F9>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F9>', conv(event)))
  tkRoot.bind("<KeyPress-F10>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F10>', conv(event)))
  tkRoot.bind("<KeyPress-F11>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F11>', conv(event)))
  tkRoot.bind("<KeyPress-F12>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-F12>', conv(event)))
  tkRoot.bind("<Control-KeyPress-f>", lambda event, zone=self.UI_scope: 
                                       zone('<Control-KeyPress-f>', conv(event)))
  tkRoot.bind("<KeyPress-z>", lambda event, zone=self.UI_scope: 
                                       zone('<KeyPress-z>', conv(event)))
                                                       
  # --------------------------- Copy & Paste ---------------------------------
  
#  tkRoot.bind("<Control-KeyPress-x>", lambda event, s=self: \
#                       s.UI_Statechart.event("Cut", conv(event)))
#  tkRoot.bind("<Control-KeyPress-c>", lambda event, s=self: \
#                       s.UI_Statechart.event("Copy", conv(event)))
#  tkRoot.bind("<Control-KeyPress-v>", lambda event, s=self: \
#                       s.UI_Statechart.event("Paste", conv(event)))
#  tkRoot.bind("<Alt-KeyPress-c>", lambda event, s=self: \
#                       s.UI_Statechart.event("Copy Attributes", conv(event)))
#  tkRoot.bind("<Alt-KeyPress-v>", lambda event, s=self: \
#                       s.UI_Statechart.event("Paste Attributes", conv(event)))
  
  tkRoot.bind("<Control-KeyPress-x>", lambda event, zone=self.UI_scope: 
                                   zone('<Control-KeyPress-x>', conv(event)))
  tkRoot.bind("<Control-KeyPress-c>", lambda event, zone=self.UI_scope: 
                                   zone('<Control-KeyPress-c>', conv(event)))
  tkRoot.bind("<Control-KeyPress-v>", lambda event, zone=self.UI_scope: 
                                   zone('<Control-KeyPress-v>', conv(event)))
  tkRoot.bind("<Alt-KeyPress-c>", lambda event, zone=self.UI_scope: 
                                      zone('<Alt-KeyPress-c>', conv(event)))
  tkRoot.bind("<Alt-KeyPress-v>", lambda event, zone=self.UI_scope: 
                                       zone('<Alt-KeyPress-v>', conv(event)))
  
  # ---------------------------- Undo & Redo ---------------------------------
  
#  tkRoot.bind("<Control-KeyPress-z>", lambda event, s=self: \
#                              s.UI_Statechart.event("Undo", conv(event)))
#  tkRoot.bind("<Control-KeyPress-y>", lambda event, s=self: \
#                              s.UI_Statechart.event("Redo", conv(event)))

  tkRoot.bind("<Control-KeyPress-z>", lambda event, zone=self.UI_scope: 
                                    zone('<Control-KeyPress-z>', conv(event)))
  tkRoot.bind("<Control-KeyPress-y>", lambda event, zone=self.UI_scope: 
                                    zone('<Control-KeyPress-y>', conv(event)))
  
  
  
  def rClicker(e):
    """ 
    Right click context menu for all Tk Entry widgets 
    Author: eltronic at juno.com
    Link: http://mail.python.org/pipermail/python-list/2004-March/214834.html
    """
  
    def rClick_Copy(e):
        e.widget.event_generate('<Control-c>')

    def rClick_Cut(e):
        e.widget.event_generate('<Control-x>')

    def rClick_Paste(e): 
        e.widget.event_generate('<Control-v>')

    e.widget.focus()
    nclst = [
        ('      ', None), 
        (' Cut', lambda e=e: rClick_Cut(e)), 
        (' Copy', lambda e=e: rClick_Copy(e)), 
        (' Paste', lambda e=e: rClick_Paste(e)), 
        ]
    
    rmenu = Tkinter.Menu(None, tearoff=0, takefocus=0)  
    for (txt, cmd) in nclst:
        if txt == ' ------ ':
            rmenu.add_separator()
        else:
            rmenu.add_command(label=txt, command=cmd)

    rmenu.entryconfigure(0, state = 'disabled')  
    rmenu.tk_popup(e.x_root-3, e.y_root+3, entry="0")
    
    return "break"
  
  for b in [ 'Entry', 'Listbox']:   
    self.parent.bind_class(b, sequence='<Button-3>', func=rClicker, add='')
    
  #-------------------------------- LAYOUT  ------------------------------ 
  
  tkRoot.bind("<Control-KeyPress-1>", lambda event, s=self: 
                  doHierarchicalLayout(s, s.cb.buildSelectionObjectSet()))
  tkRoot.bind("<Control-KeyPress-2>", lambda event, s=self: 
                  doSpringLayout(s, s.cb.buildSelectionObjectSet()))
  tkRoot.bind("<Control-KeyPress-3>", lambda event, s=self: 
                  doForceTransfer(s, s.cb.buildSelectionObjectSet()))
  tkRoot.bind("<Control-KeyPress-4>", lambda event, s=self: 
                  doTreeLikeLayout(s, s.cb.buildSelectionObjectSet()))
  tkRoot.bind("<Control-KeyPress-5>", lambda event, s=self: 
                  doCircleLayout(s, s.cb.buildSelectionObjectSet()))
                  
  #--------------------------------- OTHER --------------------------------   
                
  tkRoot.bind("<Control-KeyPress-6>", lambda event, 
              s=self: makeAllConnectionsVisible(s))
   
  # Toggle control for enabling/disabling the toolbar
  class Toggle:
    isToggled = False            
  def handler(self):
    #print 'Toggle.isToggled', Toggle.isToggled
    if(Toggle.isToggled):
      #print "PUT IT BACK"
      self.canvasPanel.pack_forget()
      self.statusbar.pack_forget()
      self.toolBarFrame.pack( side='top', fill='x', expand=0)
      self.canvasPanel.pack(side='top', fill='both', expand=1)
      self.statusbar.pack(side = 'top', fill = 'x', expand = 0)
      Toggle.isToggled = False
    else:
      self.toolBarFrame.pack_forget()
      Toggle.isToggled = True
  tkRoot.bind("<KeyPress-Scroll_Lock>", lambda event, s=self: handler(s))
  
  #------------------------------- DEBUGGING  ------------------------------  
#  tkRoot.bind("<Control-KeyPress-7>", lambda event, s=self: onDebugKey7(s))
  tkRoot.bind("<KeyPress-Home>", lambda event, s=self: onDebugLayout(s))
  


def makeAllConnectionsVisible(self):
  """ """
  color = 'orange'
  
  print '\nVisual modification activated'
  print 'All invisible links have been re-colored to the color', color
  print 'NOTE:'
  print '    Effect is purely visual.'
  print '    Re-load model to restore invisibility of affected links.'
  print '    The', color, 'color is hard-coded in', __file__,
  print 'method makeAllConnectionsVisible\n'  
  
  from ModelSpecificCode import isConnectionLink
  dc = self.cb.getCanvas()
  
  for nodeList in self.ASGroot.listNodes.values():
    for node in nodeList:
      obj = node.graphObject_
      if isConnectionLink(obj):
        for connectionList in [obj.in_connections_ + obj.out_connections_]:
          for conInfoTuple in connectionList:
            itemHandler = conInfoTuple[0]
            #print 'itemHandler', itemHandler
            if(not self.cb.isItemVisible(itemHandler)):
              #print 'invisible'
              itemtype = dc.type(itemHandler)
              #print 'itemtype', itemtype
              if itemtype in ['line', 'text']:
                dc.itemconfigure(itemHandler, fill=color)
              else:
                dc.itemconfigure(itemHandler, outline=color)

      
#def sysPathHacker(fileName):
#  """
#  Makes sure the given filename, if it is in User Formalisms or User Models
#  is in the sys.path so that it can be imported
#  Assumes fileName does not include the .py extension
#  """
#  import sys, os
#  from FilePaths           import USER_MMODEL_PATH, USER_MODEL_PATH
#  
#  newPath = None
#  
#  allFormalismDirs = os.listdir(USER_MMODEL_PATH)
#  for formalismDir in allFormalismDirs:
#    fullFormalismDir = os.path.join(USER_MMODEL_PATH, formalismDir)
#    try:
#      allFormalismFiles = os.listdir(fullFormalismDir)
#    except:
#      pass
#    for file in allFormalismFiles:
#      if(file[:-3] == fileName):
#        sys.path.append(fullFormalismDir)
#        newPath = fullFormalismDir
#        
#  allModelDirs = os.listdir(USER_MODEL_PATH)
#  for modelDir in allModelDirs:
#    fullModelDir = os.path.join(USER_MODEL_PATH, modelDir)
#    try:
#      allModelFiles = os.listdir(fullModelDir)
#    except:
#      pass
#    for file in allModelFiles:
#      if(file[:-3] == fileName):
#        sys.path.append(fullModelDir)
#        newPath = fullModelDir
#  
#  return os.path.join(newPath, fileName) + '.py'


      
def onDebugKey1(self):
  print 'onDebugKey1'
  
#  # Uncomment these to load the corresponding meta-model
#  #self.openMetaModel(GUIModel='BondGraph_META')
#  #self.openMetaModel(GUIModel='CausalBlockDiagram_META')
#  self.openMetaModel(GUIModel='RWM_META')
#  self.openMetaModel(GUIModel='IPM_META')
#  
#  # Just enter the name of the model, nothing else, sysPathHacker will find it
#  # if it is in User Models or User Formalisms (as long as it is one dir deep)
#  modelFileName = 'Hositing_Device_RWM_MDL'
#  graphGrammarFileName = 'RWM_2_IPM_GG_exec' # don't put the .py
#  
#  modelFileName = sysPathHacker(modelFileName)
#  self.open(fileName=modelFileName)
#  #self.open(fileName='D:\\ResearchSummer2005\\atom3 user area\\User Models\\Sagar\\Hositing_Device_RWM_MDL.py')
#
#  # Copy and paste this code to run more grammars... 
#  # But change graphGrammarFileName of course
#  from GraphRewritingSys import GraphRewritingSys
#  sysPathHacker(graphGrammarFileName)
#  exec "from "+graphGrammarFileName+" import " + graphGrammarFileName  
#  
#  # get the graph grammar to execute from the options...          
#  self.GraphGrammars = [ eval(graphGrammarFileName+"(self)") ]                  
#  # get the graph grammar to execute from the options... 
#  self.grs = GraphRewritingSys(self, self.GraphGrammars, self.ASGroot )
#  self.grs.evaluate(stepByStep = 0, moveEntities = 0, 
#                   execute = self.grs.SEQ_RANDOM, graphics = 0)  


  
def onDebugLayout(self):
  print 'onDebugLayout(self)'
  from AToM3LayoutInterface import doChosenLayout
  doChosenLayout(self, self.cb.buildSelectionObjectSet())
  

      
      
  