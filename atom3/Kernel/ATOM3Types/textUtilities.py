"""
textUtilities.py

Adds coloring to a text widget, and better tab support for python code
Needs multi-line indentation, undo/redo, and find/search capabilities now

Created March 13, 2005 by Denis Dube
"""

from ATOM3Integer import ATOM3Integer
from string import split, rstrip
import os
from Tkinter import Button, Frame, TOP,X,Y,LEFT, END, INSERT
import Tkinter
import tkSimpleDialog, tkMessageBox, tkFileDialog

from Percolator     import Percolator
from ColorDelegator import ColorDelegator
from UndoDelegator  import UndoDelegator
import SearchDialog  
import ReplaceDialog  

BASEDIR = os.path.split( __file__ )[ 0 ] # <-- Exactly which dir this file is in
BASEDIR = os.path.join( BASEDIR, 'bitmaps' ) # <-- Where the bitmaps are
STIPPLE8 = '@' + str( os.path.join( BASEDIR, 'thindotline8.xbm' ) )
STIPPLE16= '@' + str( os.path.join( BASEDIR, 'dotline16.xbm' ) )
STIPPLE32= '@' + str( os.path.join( BASEDIR, 'thindotline32.xbm' ) )

KEY_DICT =       {'<<replace>>': ['<Control-KeyPress-r>','<Alt-KeyPress-r>'],
                  '<<undo>>' : ['<Control-KeyPress-z>','<Alt-KeyPress-z>'],
                  '<<redo>>' : ['<Control-KeyPress-y>','<Alt-KeyPress-y>'],
                  '<<find>>' : ['<Control-KeyPress-f>','<Alt-KeyPress-f>'],
                  '<<goto-line>>' : ['<Control-KeyPress-g>','<Alt-KeyPress-g>'],
                  '<<add-indent>>' : ['<Control-KeyPress-bracketright>',
                                      '<Control-KeyPress-period>'],
                  '<<del-indent>>' : ['<Control-KeyPress-bracketleft>',
                                      '<Control-KeyPress-comma>'],
                  '<<add-comment>>' : ['<Control-KeyPress-3>',
                                       '<Alt-KeyPress-3>'],
                  '<<del-comment>>' : ['<Control-KeyPress-2>',
                                       '<Alt-KeyPress-2>'],
                  '<<select-all>>' : ['<Control-KeyPress-a>',
                                       '<Alt-KeyPress-a>'],
                  '<<deselect-all>>' : ['<Control-KeyPress-d>',
                                        '<Alt-KeyPress-d>'],
                  '<<paste>>' : ['<Control-KeyPress-v>'],
                  '<<cut>>' : ['<Control-KeyPress-x>'],
                  '<<copy>>' : ['<Control-KeyPress-c>'],
                  '<<popup-menu>>' : ['<Button-3>','<Button-2>'],
                  '<<open>>' : ['<Control-KeyPress-o>'],
                  '<<save>>' : ['<Control-KeyPress-s>'],
                  '<<select>>' : ['<Double-Button-1>'],
                 }


def addFiltersFromIDLE(self):
  """
  Adds syntax colors, undo, replace, find, goto, indent, commment 
  functionality from IDLE to the text widget
  """
  textWidget = self.textWidget
  
  p = Percolator( textWidget )
  p.insertfilter( ColorDelegator() )  # Python syntax coloring
  undo = UndoDelegator() 
  p.insertfilter( undo )              # Undo/Redo feature
  
  # This is used to undo stuff done with replace, indent, comment, etc.
  textWidget.undo_block_start = undo.undo_block_start
  textWidget.undo_block_stop = undo.undo_block_stop
    
  
  #----------------- Bind virtual events to the text widget ------------------
  textWidget.bind("<<replace>>", lambda e=None,self=self:
                                 ReplaceDialog.replace(self.textWidget) )
  textWidget.bind("<<find>>", lambda e=None,self=self:
                              SearchDialog.find(self.textWidget) )
  textWidget.bind("<<goto-line>>", lambda e=None,self=self:
                              goto_line_event(self) )
  textWidget.bind("<<add-indent>>", lambda e=None,self=self:
                                    indent_region_event(self) )
  textWidget.bind("<<del-indent>>", lambda e=None,self=self:
                                    dedent_region_event(self) )
  textWidget.bind("<<add-comment>>", lambda e=None,self=self:
                                     comment_region_event(self) )
  textWidget.bind("<<del-comment>>", lambda e=None,self=self:
                                     uncomment_region_event(self) )
  textWidget.bind("<<select-all>>", lambda e=None,self=self:
                                    select_all(self) )
  textWidget.bind("<<deselect-all>>", lambda e=None,self=self:
                                      deselect_all(self) )
  textWidget.bind("<<paste>>", lambda e=None,self=self:
                               paste(self) )
  textWidget.bind("<<copy>>", lambda e=None,self=self:
                              copy(self) )
  textWidget.bind("<<cut>>", lambda e=None,self=self:
                             cut(self) )
  textWidget.bind("<<popup-menu>>", lambda e=None,self=self:
                                    popupMenu(self, e) )
  textWidget.bind("<<open>>", lambda e=None,self=self:
                              Open(self) )
  textWidget.bind("<<save>>", lambda e=None,self=self:
                              SaveAs(self) )
                                      
  #---------------- Give virtual events a concrete keybinding ----------------
  for key,value in KEY_DICT.iteritems(): 
    textWidget.event_add( key, *value )
    

  
def Open(self):
  """ Open Python files """
  FileName=tkFileDialog.askopenfilename(filetypes=
                                    [("Python files", "*.py"),
                                    ("All files", "*")])
  if (FileName==None or FileName==""):
      return
  try:
      File=open(FileName,"r")
      NewText=File.read()
      File.close()     
  except IOError:
      tkMessageBox.showerror("Read error...",
          "Could not read from '%s'"%FileName) 
      return
  self.textWidget.delete("1.0",END) 
  self.textWidget.insert(END,NewText)
        
def SaveAs(self):
  FileName=tkFileDialog.asksaveasfilename(filetypes=[("Python files", "*.py"),
                                                      ("All files", "*")])
  if (FileName==None or FileName==""):
      return        
  try:
      File=open(FileName,"w")
      NewText=self.textWidget.get("1.0",Tkinter.END)
      File.write(NewText)
      File.close()
  except IOError:
      tkMessageBox.showerror("Save error...",
          "Could not save to '%s'"%FileName) 
      return 
  
def popupMenu(self, e):
  """ 
  Right click context menu for all Tk Text widget
  Automatically generated from the KEY_DICT
  """  
  rmenu = Tkinter.Menu(self.textWidget, tearoff=0, takefocus=0)  
  rmenu.add_separator()
  sortedKeys = KEY_DICT.keys()
  sortedKeys.sort()
  for vEvent in sortedKeys:
    keyList = KEY_DICT[vEvent]    
    accelerator = ''
    numKeys = len(keyList)
    for i in range( 0, numKeys ):
      accelerator += keyList[i]
      if( i+1 < numKeys ): accelerator += ' or '
      
    rmenu.add_command(label=vEvent[2:-2] , accelerator=accelerator,
                      command=lambda e=None,self=self,vEvent=vEvent:
                              self.textWidget.event_generate(vEvent)  )

  rmenu.tk_popup(e.x_root-3, e.y_root+3)
  return "break"
  
def copy(self,event=None):
  """ Handle copy event manually (stays in memory after AToM3 closes!) """
  # Get the selected text
  head, tail = get_selection_indices(self)
  if( not head or not tail ): return 'break'
  clipText = self.textWidget.get( head, tail )
  
  # Add it to clipboard
  self.textWidget.clipboard_clear()
  self.textWidget.clipboard_append( clipText.rstrip('\n') )
  return 'break'

def cut(self,event=None):
  """ Handle copy event manually (stays in memory after AToM3 closes!) """
  # Get the selected text
  head, tail = get_selection_indices(self)
  if( not head or not tail ): return 'break'
  clipText = self.textWidget.get( head, tail )
  
  # Add it to clipboard
  self.textWidget.clipboard_clear()
  self.textWidget.clipboard_append( clipText.rstrip('\n') )
  
  # Remove cut text
  self.textWidget.undo_block_start()
  self.textWidget.delete( head,tail) 
  self.textWidget.undo_block_stop()
  return 'break'
       
def paste(self,event=None):
  """ Handle paste manually (automatic tab coloring) """
  try:
    clipboard = self.textWidget.selection_get(selection="CLIPBOARD")
  except:
    return
  ## pasteIndex = self.textWidget.index( INSERT )
  self.textWidget.undo_block_start()
  
  # Delete current selection
  head, tail = get_selection_indices(self)
  if( head and tail ): self.textWidget.delete( head,tail)
  
  # Paste & Colorize tabs
  self.textWidget.insert( INSERT, clipboard  )
  ## newIndex = self.textWidget.index( INSERT )
  ## colorizeTabs(self) #<-- messes up index but colorizes :D

  # Fix the insert index
  ## self.textWidget.mark_set("insert", newIndex)
  ## self.textWidget.see(pasteIndex)
  self.textWidget.undo_block_stop()
  return 'break'


  
  
# If a selection is defined in the text widget, return (start,
# end) as Tkinter text indices, otherwise return (None, None)
def get_selection_indices(self):
    try:
        first = self.textWidget.index("sel.first")
        last = self.textWidget.index("sel.last")
        return first, last
    except TclError:
        return None, None
          
def get_region(self):
    text = self.textWidget
    first, last = get_selection_indices(self)
    if first and last:
        head = text.index(first + " linestart")
        tail = text.index(last + "-1c lineend +1c")
    else:
        head = text.index("insert linestart")
        tail = text.index("insert lineend +1c")
    chars = text.get(head, tail)
    lines = chars.split("\n")
    return head, tail, chars, lines 

def set_region(self, head, tail, chars, lines):
    text = self.textWidget
    newchars = "\n".join(lines)
    if newchars == chars:
        text.bell()
        return
    text.tag_remove("sel", "1.0", "end")
    text.mark_set("insert", head)
    text.undo_block_start()
    text.delete(head, tail)
    text.insert(head, newchars)
    text.undo_block_stop()
    #text.tag_add("sel", head, "insert")
  
# Look at the leading whitespace in s.
# Return pair (# of leading ws characters,
#              effective # of leading blanks after expanding
#              tabs to width tabwidth)
def classifyws(s, tabwidth):
    raw = effective = 0
    for ch in s:
        if ch == ' ':
            raw = raw + 1
            effective = effective + 1
        elif ch == '\t':
            raw = raw + 1
            effective = (effective // tabwidth + 1) * tabwidth
        else:
            break
    return raw, effective
  
def indent_region_event(self, event=None):
  head, tail, chars, lines = get_region(self)
  for pos in range(len(lines)):
      line = lines[pos]
      if line:
          raw, effective = classifyws(line, self.tabSpacing)
          effective = effective + self.tabSpacing
          lines[pos] = ' ' * effective + line[raw:]
  set_region(self, head, tail, chars, lines)
  colorizeTabs(self)
  
  self.textWidget.tag_add("sel", head,  tail)
  self.textWidget.mark_set("insert", head )
  self.textWidget.see("insert")
  return "break"

def dedent_region_event(self, event=None):
  head, tail, chars, lines = get_region(self)
  for pos in range(len(lines)):
      line = lines[pos]
      if line:
          raw, effective = classifyws(line, self.tabSpacing)
          effective = max(effective - self.tabSpacing, 0)
          lines[pos] = ' ' * effective + line[raw:]
  set_region(self, head, tail, chars, lines)
  
  self.textWidget.tag_add("sel", head,  tail)
  self.textWidget.mark_set("insert", head )
  self.textWidget.see("insert")
  return "break"

def comment_region_event(self, event=None):
  head, tail, chars, lines = get_region(self)
  for pos in range(len(lines) - 1):
      line = lines[pos]
      lines[pos] = '##' + line
  set_region(self, head, tail, chars, lines)
  

def uncomment_region_event(self, event=None):
  head, tail, chars, lines = get_region(self)
  for pos in range(len(lines)):
      line = lines[pos]
      if not line:
          continue
      if line[:2] == '##':
          line = line[2:]
      elif line[:1] == '#':
          line = line[1:]
      lines[pos] = line
  set_region(self, head, tail, chars, lines)
  
def select_all(self, event=None):
    self.textWidget.tag_add("sel", "1.0", "end-1c")
    self.textWidget.mark_set("insert", "1.0")
    self.textWidget.see("insert")
    return "break"

def deselect_all(self, event=None):
    self.textWidget.tag_remove("sel", "1.0", "end")
    self.textWidget.see("insert")
    return "break"
  

def goto_line_event(self, event=None):
    text = self.textWidget
    lineno = tkSimpleDialog.askinteger("Goto",
            "Go to line number:",parent=text)
    if lineno is None:
        return "break"
    if lineno <= 0:
        text.bell()
        return "break"
    text.mark_set("insert", "%d.0" % lineno)
    text.see("insert")

def setTabs( self, event=None ):
    """ Updates the 'Spaces per tab' value, and redraws all tabs """
    self.tabSpacing = self.ATOM3tab.getValue()
    self.tabSpace = " " * self.tabSpacing

    if(  self.tabSpacing <= 1 ):
      self.textWidget.tag_config( 'tab', background='white',bgstipple='' )
      return
    elif( self.tabSpacing < 2 or (self.tabSpacing % 2) == 1 ):  
      stipple = STIPPLE8
    elif( self.tabSpacing == 2 or (self.tabSpacing % 4) != 0 ):
      stipple = STIPPLE16
    else:
      stipple = STIPPLE32
    
    # Try: because somehow it might be hard to find the stipple
    try:
      self.textWidget.tag_config( 'tab', background='black',
                                    bgstipple=stipple )
    except:
      self.textWidget.tag_config( 'tab', background='light grey' )
    colorizeTabs(self)
    
def createTabPanel(self, frame, frameSide='left' ):
    """ Create a small panel to configure the tabbing """      
    tabFrame = Frame( frame )

#===============================================================================
#    Set the number of spaces each tab press represents
#===============================================================================
    spacePerTabButton = Button(tabFrame, text='Set Spaces Per Tab', 
                         command=lambda s=self:setTabs(s) )
    spacePerTabButton.pack(side=LEFT,fill=Y)
  
    self.ATOM3tab = ATOM3Integer( 4 )
    widget = self.ATOM3tab.show( tabFrame )
    widget.pack(side=LEFT,fill=Y)
    self.tabSpacing = self.ATOM3tab.getValue()
    self.tabSpace = " " * self.tabSpacing
    
#===============================================================================
#    Set the height in text lines that the box occupies
#===============================================================================
    def handler(self=self):
      self.setHeight(None)
    setHeightButton = Button(tabFrame, text='Set Text Box Height', 
                         command=handler )
    setHeightButton.pack(side=LEFT,fill=Y)    
    heightWidget = self.heightATOM3Integer.show( tabFrame )
    heightWidget.pack(side=LEFT,fill=Y)
    
#===============================================================================
#    Generic menu button
#===============================================================================
    popupButton = Button(tabFrame, text='Text Editor Menu', 
                         command=lambda self=self, vEvent='<<popup-menu>>':
                         self.textWidget.event_generate(vEvent) )
    popupButton.pack(side=LEFT,fill=Y)     
     
    tabFrame.pack(side=frameSide)
    
    
def helpText( *args ):
    try:
      path = __file__ # ../Kernel/ATOM3Types/textUtilities.py
      path = os.path.split( os.path.split( path )[0] )[0] # ../Kernel/
      path = os.path.join( path, 'HelpDocuments' ) # ../Kernel/HelpDocuments
      path = os.path.join( path, 'constraintsActions.txt' )
      f = open( path, 'r' )
      text = f.read()
      f.close()
    except:
      text = 'constraintsActions.txt not found... sorry'
    ATOM3TypeDialog( None , ATOM3Text( text ) )
  
def colorizeTabs( self, event=None ):
    """ Processes the entire text and adds colored tabs where applicable """
    textTuple = self.textWidget.get(1.0, END).split( '\n' )
    self.textWidget.delete( 1.0, END )
          
    # Cleanup spurious newlines at the end
    maxIndex = len(textTuple)
    for i in range( len(textTuple)-1,0,-1):
      if( textTuple[i] != '' ): 
        maxIndex = i+1
        break
    textTuple = textTuple[:maxIndex]
    
    for line in textTuple:            
      # Convert spaces to tabs
      lineIndex = 0
      spaceCount = 0
      lineTerminated = False
      for char in line:       
        if( char == ' ' ): spaceCount += 1
        else:
          while( spaceCount > 0 ):
            if( spaceCount >= self.tabSpacing ):            
              self.textWidget.insert( INSERT, self.tabSpace, ('tab',) )            
              spaceCount -= self.tabSpacing
            else:
              self.textWidget.insert( INSERT, ' ' )
              spaceCount -= 1
          self.textWidget.insert( INSERT,line[lineIndex:]+'\n' )
          lineTerminated = True
          break
        lineIndex += 1
      if( not lineTerminated ): self.textWidget.insert( INSERT, '\n' ) 
      

        
  
def tagIndex2Number( tagIndex ):
    """ Converts line.char strings into integer tuples [line,char] """
    return map( int, tagIndex.split( '.' ) )
  
def isIndexInRange( startIndex, testIndex, endIndex ):
    """ Determines if startIndex <= testIndex <= endIndex """
    ls,cs = tagIndex2Number( startIndex )
    lt,ct = tagIndex2Number( testIndex )
    le,ce = tagIndex2Number( endIndex )
    if( ls == lt and lt == le and cs <= ct and ct <= ce ): return True
    return False
  
def processBackspace(self,event=None):
    """ Special handling for tab removals (since they are really spaces) """
    currentIndex = self.textWidget.index( INSERT )
    tabRanges = self.textWidget.tag_ranges('tab')
    for i in range(0,len(tabRanges),2):
      if( isIndexInRange( tabRanges[i], currentIndex, tabRanges[i+1] ) ):
        line,char = tagIndex2Number( currentIndex )
        if( char == tagIndex2Number( tabRanges[i] )[1] ): break
        if( char % self.tabSpacing == 0 ): char = char - self.tabSpacing
        else: char = char - (char % self.tabSpacing)        
        self.textWidget.delete( "%d.%d" % (line,char),
                                    "%d.%d" % (line,char+self.tabSpacing) )
        return "break"
def processDelete(self,event=None):
    """ Special handling for tab removals (since they are really spaces) """
    currentIndex = self.textWidget.index( INSERT )
    tabRanges = self.textWidget.tag_ranges('tab')
    for i in range(0,len(tabRanges),2):
      if( isIndexInRange( tabRanges[i], currentIndex, tabRanges[i+1] ) ):
        line,char = tagIndex2Number( currentIndex )
        if( char == tagIndex2Number( tabRanges[i+1] )[1] ): break
        if( char % self.tabSpacing != 0 ):  char -= (char % self.tabSpacing)        
        self.textWidget.delete( "%d.%d" % (line,char),
                                    "%d.%d" % (line,char+self.tabSpacing) )
        return "break"
  
def processTab(self,event=None):
    """ Convert tab to space and colorize it """
    
    # Multiple lines selected? Indent them all...
    text = self.textWidget
    first, last = get_selection_indices(self)
    chars = text.get(first, last)
    lines = chars.split("\n")
    if( len( lines ) > 1 ): 
      return indent_region_event(self)
          
    # Adds a colored tab if at line start
    currentIndex = self.textWidget.index( INSERT )
    line,char = tagIndex2Number( currentIndex )
    
    # Line start (colored tab)
    if( char == 0 ):
      self.textWidget.insert( INSERT, self.tabSpace, tags='tab')
      return "break"
      
    # Between the line start and text start (colored tab)
    tabRanges = self.textWidget.tag_ranges('tab')
    for i in range(0,len(tabRanges),2):
      if( isIndexInRange( tabRanges[i], currentIndex, tabRanges[i+1] ) ):
        if( char % self.tabSpacing != 0 ):  
          # In the middle of a tab, remove it, then add 2 tabs to make up
          processBackspace(self)
          self.textWidget.insert( INSERT, self.tabSpace, tags='tab')
        self.textWidget.insert( INSERT, self.tabSpace, tags='tab')
        return "break"
      
    # After text start (regular no-color tab)
    self.textWidget.insert( INSERT, self.tabSpace )
    return "break"

def processReturn(self, event=None):
    "Adds a return to the text..."
    spaces = 0
    
    # If we are pressing enter inside a tab, kill that tab
    currentIndex = self.textWidget.index( INSERT )
    line,char = tagIndex2Number( currentIndex )
    tabRanges = self.textWidget.tag_ranges('tab')
    for i in range(0,len(tabRanges),2):
      if( isIndexInRange( tabRanges[i], currentIndex, tabRanges[i+1] ) ):
        if( char % self.tabSpacing != 0 ):  
          processBackspace(self)
          spaces = self.tabSpacing
        
    # Get the current line
    currentIndex = self.textWidget.index( INSERT )
    line,char = tagIndex2Number( currentIndex )   
    line = self.textWidget.get( "%d.0" % (line),"%d.%d" % (line,char) )
    
    # Terminate the current line
    lineEnd = self.textWidget.search( '\n', INSERT )
    putBackText = self.textWidget.get( INSERT, lineEnd )
    self.textWidget.delete( INSERT, lineEnd  )
    self.textWidget.insert( INSERT, "\n")
    
    # Add extra tabs to the new line so it has same tab as old line
    for char in line:
      if( char == ' ' ): spaces += 1
      else: break
    for tab in range(0,spaces,self.tabSpacing):
      self.textWidget.insert( INSERT, self.tabSpace, tags='tab')
    self.textWidget.insert( INSERT, putBackText )
    return "break"
