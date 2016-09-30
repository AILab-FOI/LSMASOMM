"""
OptionDialog.py

My best tkSimpleDialog derivitive to date. I keep trying to find ways to
improve it. This is pretty simple to use, yet quite expressive and expandible.

Last modified June 24, 2004 by Denis Dube
"""


import os, string, tkMessageBox
from Tkinter        import *
from tkFileDialog   import askopenfilename
from tkColorChooser import askcolor

class OptionDialog(Toplevel):
    """ A re-usable dialog box derived from tkSimpleDialog """
    
    # General option format:
    # [ InitialValue, optionList, promptString, helpString(optional) ]
    
    # optionList values:
    BOOLEAN_ENTRY = [0]
    INT_ENTRY     = [1]
    FLOAT_ENTRY   = [2]
    STRING_ENTRY  = [3]
    FILE_ENTRY    = 4       # optionList = [ FILE_ENTRY, "Button Label", 
                            # File Type Mask, FileType, initialDir ]
    COLOR_ENTRY   = 5       # optionList = [ COLOR_ENTRY, "Button Label" ]
    NO_ENTRY      = [6]     # An option with this code presents no dialog
    BOOL_BUTTON_ENTRY  = 7  # optionList = [ BUTTON_ENTRY, "Button Label" ]
    ENUM_ENTRY    = 8       # optionList = [ ENUM_ENTRY, enumeration1,enumeration2, ... ]
    LABEL         = 9       # optionList = [ LABEL, font,color,justification ]
    LIST_FILE_ENTRY = 10    # optionList = [ LIST_FILE_ENTRY, *args ]
    SEPERATOR     = [11]    # Just draws a line
    LIST_INT_ENTRY = [12]   # optionList = [ LIST_INT_ENTRY, *args ]
    MULTI_LIST_ENTRY = 13   # optionList = [ MULTI_LIST_ENTRY, option1,value1,option2,value2, ... ]
    SINGLE_LIST_ENTRY = 14  # optionList = [ SINGLE_LIST_ENTRY, option1,value1,option2,value2, ... ]
    ENUM_ENTRY_HORIZ  = 15  # optionList = [ ENUM_ENTRY_HORIZ, enumeration1,enumeration2, ... ]
    
    # FileType values:
    FILEPATH = 0
    FILENAME_ONLY = 1
    RELATIVE_DIRNAME = 2    
    
    def __init__(self, parent, title, optionDatabase,optionOrder,position=(0,0), grab = True ):

        Toplevel.__init__(self, parent)
        self.transient(parent)

        if title:     
            self.title(title)
            self.titleString = title
        
        self.CancelPressed = 0
        self.optionDatabase = optionDatabase
        self.optionOrder = optionOrder

        self.parent = parent
        self.position = position

        self.result = None

        body = Frame(self)
        #self.initial_focus = self.body(body)
        self.body(body)
        body.pack(padx=5, pady=5)

        self.initial_focus = self.buttonbox()

        if( grab ):
          self.grab_set()

        if not self.initial_focus:
            self.initial_focus = self

        self.protocol("WM_DELETE_WINDOW", self.cancel)

        if self.parent is not None:
            x, y = position
            if( x > 0 and y > 0 ):
                x = x / 2 
                y = y / 2 
            self.geometry("+%d+%d" % (x, y))

        self.initial_focus.focus_force() # Ok button gets focus
        #self.initial_focus.focus_set()
        parent.update()

        self.wait_window(self)
        
    def destroy(self):
        """ Destroy the window """
        self.initial_focus = None
        Toplevel.destroy(self)
        
    def buttonbox(self):
        """ Buttons!"""

        box = Frame(self)
        boxTop = Frame(box)
        boxBottom = Frame(box)

        wx = Button(boxBottom , text="OK", width=10, command=self.ok, 
                   default=ACTIVE)
        wx.pack(side=LEFT, padx=5, pady=5)
        w = Button(boxBottom , text="Cancel", width=10, command=self.okCancel)
        w.pack(side=LEFT, padx=5, pady=5)

        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        
        box.pack()
        boxTop.pack(side = TOP)
        boxBottom.pack(side = BOTTOM)
        return wx

        
    def ok(self, event=None):

        if not self.validate():
            print "Invalid selection, try again."
            self.initial_focus.focus_set() # put focus back
            return

        self.withdraw()
        self.update_idletasks()

        self.apply()

        self.cancel()
        
    def okCancel(self, event=None):

        self.CancelPressed = 1
        
        # put focus back to the parent window
        if self.parent is not None:
            self.parent.focus_set()
        self.destroy()

    def cancel(self, event=None):

        
        # put focus back to the parent window
        if self.parent is not None:
            self.parent.focus_set()
        self.destroy()
        
    #----------------------------  WIDGET BLOCKS -------------------------------
        
    def addEntry(self,master,initialValue,i):
      """ Creates an entry widget that can capture strings or numbers """
      widget = Entry(master)
      widget.insert( 0,str( initialValue ))
      widget.grid(row=i+1, column=1, sticky=EW) 
      return widget
    
    def addBoolean(self,master,initialValue,i):
      """ Creates a checkbutton that can be toggled on/off """
      variable = IntVar()
      variable.set( bool( initialValue )  )
      widget = Checkbutton(master, variable=variable)   
      widget.grid(row=i+1, column=1,sticky=W)  
      return [widget,variable]
          
    def addHelp(self,master,helpString,i):
      """ Creates a help button that can be triggered for extra information """
      if( helpString != "" ):
        helpButton = Button(master, text="Info",
                            command=lambda s=self,t=helpString: s.helpMe(t) )
        helpButton.grid(row=i+1,column=3,stick=E) 
        
    def addFile(self,master,option,optionList,widget,i):
      """ Creates a file button that can be triggered to show a file choosing dialog """
      #"Choose Filename"
      label = optionList[1]
      button = Button(master, text=label, 
          command=lambda s=self,o=option,w=widget,l=optionList: s.fileNameOpener(o,l,w) )
      button.grid(row=i+1, column=2,stick=EW) 
        
        
    def addSingleList(self, master, option, optionList, initialValue, i ):
      """ Creates a button that lets you access another dialog, store res in list """
      itemList  = Listbox(master, exportselection=0)	
      for item in initialValue:
        itemList.insert(END, str(item) )
      itemList.selection_set(END)
      self.widgetDict[option] = itemList
      
      button = Button(master, text='Edit',width=10,
                  command=lambda s=self,o=option,l=optionList: s.MultiListEdit(o,l) )
      button.grid(row=i+1, column=1,stick=EW)
      
        
    def addMultiList(self, master,option, optionList,initialValue,i ):
      #todo: addMultiList
      listFrame = Frame( master )
      
      # a scrollbar for the listbox
      scrollbar      = Scrollbar(listFrame, orient=VERTICAL)			
      
      # Create a ListBox
      height = max( len( initialValue ), 5 )
      itemList  = Listbox(listFrame, height=height,
                          exportselection=0, yscrollcommand=scrollbar.set)	
      
      scrollbar.config(command=itemList.yview)
      scrollbar.pack(side=RIGHT, fill=Y)
      
      # show the items in the list, if any
      for item in initialValue:
        itemList.insert(END, str(item) )
             
      itemList.pack(side=BOTTOM, fill=BOTH, expand=1)
      
      listFrame.grid(row=i+1, column=1, stick=EW )
      
      # Edit buttons
      buttonFrame = Frame( master )
      
      width = 10
      buttonNew = Button(buttonFrame, text='New',width=width,
                  command=lambda s=self,o=option,l=optionList: s.MultiListNew(o,l) )
      buttonEdit = Button(buttonFrame, text='Edit',width=width,
                  command=lambda s=self,o=option,l=optionList: s.MultiListEdit(o,l) )
      buttonDel = Button(buttonFrame, text='Delete',width=width,
                  command=lambda s=self,o=option: s.listDel(o) )
      ## buttonUp = Button(buttonFrame, text='Move Up',width=width,
                  ## command=lambda s=self,o=option: s.listUp(o) )
      ## buttonDown = Button(buttonFrame, text='Move Down',width=width,
                  ## command=lambda s=self,o=option: s.listDown(o) )
            
      buttonNew.pack( side=TOP, fill=X )
      buttonEdit.pack( side=TOP, fill=X )
      buttonDel.pack( side=TOP, fill=X )      
      ## buttonUp.pack( side=TOP, fill=X )
      ## buttonDown.pack( side=TOP, fill=X )
      
      buttonFrame.grid(row=i+1, column=2, stick=EW )
      
      self.widgetDict[option] = itemList
      
              
    def addList(self, master,option, optionList,initialValue,i, mode=0 ):
      listFrame = Frame( master )
      
      # a scrollbar for the listbox
      scrollbar      = Scrollbar(listFrame, orient=VERTICAL)			
      
      # Create a ListBox
      height = max( len( initialValue ), 5 )
      itemList  = Listbox(listFrame, height=height,
                          exportselection=0, yscrollcommand=scrollbar.set)	
      
      scrollbar.config(command=itemList.yview)
      scrollbar.pack(side=RIGHT, fill=Y)
      
      # show the items in the list, if any
      for item in initialValue:
        itemList.insert(END, str(item) )
             
      itemList.pack(side=BOTTOM, fill=BOTH, expand=1)
      
      listFrame.grid(row=i+1, column=1, stick=EW )
      
      # Edit buttons
      buttonFrame = Frame( master )
      
      width = 10
      if( mode == self.LIST_INT_ENTRY[0] ):        
        buttonNew = Button(buttonFrame, text='New',width=width,
                  command=lambda s=self, o=option: s.listNewInteger(o) )
      else:
        buttonNew = Button(buttonFrame, text='New',width=width,
                  command=lambda s=self,o=option,l=optionList: s.listNew(o,l) )
      buttonDel = Button(buttonFrame, text='Delete',width=width,
                  command=lambda s=self,o=option: s.listDel(o) )
      buttonUp = Button(buttonFrame, text='Move Up',width=width,
                  command=lambda s=self,o=option: s.listUp(o) )
      buttonDown = Button(buttonFrame, text='Move Down',width=width,
                  command=lambda s=self,o=option: s.listDown(o) )
            
      buttonNew.pack( side=TOP, fill=X )
      buttonDel.pack( side=TOP, fill=X )      
      buttonUp.pack( side=TOP, fill=X )
      buttonDown.pack( side=TOP, fill=X )
      
      buttonFrame.grid(row=i+1, column=2, stick=EW )
      
      self.widgetDict[option] = itemList
      
    def addLabel(self,master,promptString,i):
      """ Creates a label with the given text """
      Label(master, text=promptString,font="Times 12").grid(row=i+1,sticky=W)
      
    def addColor(self,master,option,label,widget,i):
      """ Creates a button that can be triggered to show a color choosing dialog """
      button = Button(master, text=label, 
          command=lambda s=self,o=option,w=widget: s.colorChooser(o,w) )
      button.grid(row=i+1, column=2,stick=EW) 
      
    def addButton(self,master, option,label,i ):
      button = Button(master, text=label, 
          command=lambda s=self,o=option,l=label: s.buttonCallback(o,l) )
      button.grid(row=i+1, column=2,stick=EW)
      
    def addEnumHoriz( self, master,option, enumList,initialValue,i):
      var = StringVar()
      var.set( str(initialValue) )
      self.widgetDict[option] = var
      
      radioButtonFrame = Frame(master, bg='blue')
      for stringValue in enumList:
        Radiobutton(radioButtonFrame, variable=var, value=stringValue,
                    indicatoron=False, text=stringValue).pack(side=LEFT, 
                                                     fill=BOTH, expand=1)
      radioButtonFrame.grid(row=i+1, column=1,sticky=EW)
      return i
      
    def addEnum( self, master,option, enumList,initialValue,i):
      var = StringVar()
      var.set( str(initialValue) )
      self.widgetDict[option] = var
            
      # Create radio buttons to choose from the enumerated values
      i += 1
      for stringValue in enumList:
        widget = Radiobutton(master, variable=var, value=stringValue,
                             indicatoron=False, text=stringValue )   
        widget.grid(row=i, column=1,sticky=EW) 
        i += 1
      return i - 1
    
    def addSpecialLabel( self, master, optionList,text,i):
      """ Label that takes a full line """
      font, color, justification = optionList
      if( justification == "left" ):
        sticky = W
      elif( justification == "right" ):
        sticky = E
      else:
        sticky = EW
      l = Label(master, text=text,font=font, fg=color)
      l.grid(row=i+1,sticky=sticky, columnspan = 10)
   
                    
    #----------------------------  WIDGET BLOCKS -------------------------------
    
    def body(self, realMaster):
      """ The body of the dialog, widgets are assembled here """

      self.addSpecialLabel( realMaster, ["times 16","black","center"],self.titleString,0 )
      master = Frame( realMaster, relief='groove', borderwidth=2 )      
      # Special internal dictionary for tracking widget changes (buttons, entries, etc.)
      self.widgetDict = dict()
      i = 0

      for option in self.optionOrder:
        
        initialValue, optionList, promptString,helpString = self.optionDatabase[option]
        i += 1

        typeCode = optionList[0]
                
        # String - Integer - Float Entries
        if( typeCode == self.FLOAT_ENTRY[0] or typeCode == self.INT_ENTRY[0] 
            or typeCode == self.STRING_ENTRY[0] ):
          self.addLabel(master,promptString,i)
          self.widgetDict[option] = self.addEntry(master,initialValue,i)
          self.addHelp(master,helpString,i)
    
        # Boolean Entry
        elif( typeCode == self.BOOLEAN_ENTRY[0] ):
          self.addLabel(master,promptString,i)
          self.widgetDict[option] = self.addBoolean(master,initialValue,i)
          self.addHelp(master,helpString,i)       
                                  
        # File Name Entry
        elif( typeCode == self.FILE_ENTRY ):
          self.addLabel(master,promptString,i)
          widget = self.addEntry(master,initialValue,i)  
          if( len( optionList ) == 3 ): 
            optionList.append( OptionDialog.FILEPATH )
            optionList.append( '' )
          if( len( optionList ) == 4 ): 
            optionList.append( '' )
          self.addFile(master,option,optionList,widget,i)
          self.addHelp(master,helpString,i) 
          self.widgetDict[option] = widget
        
        # Color Entry
        elif( typeCode == self.COLOR_ENTRY ):
          self.addLabel(master,promptString,i)
          widget = self.addEntry(master,initialValue,i)            
          self.addColor(master,option,optionList[1],widget,i)
          self.addHelp(master,helpString,i) 
          self.widgetDict[option] = widget
          
        # Boolean Button Entry
        elif( typeCode == self.BOOL_BUTTON_ENTRY ):
          self.addLabel( master,promptString,i)
          self.addButton(master,option,optionList[1],i)
          self.addHelp(master,helpString,i)           
        
        # No dialog representation
        elif( typeCode == OptionDialog.NO_ENTRY[0] ):
          pass

        # Enumeration Entry (Vertical)
        elif( typeCode == self.ENUM_ENTRY ):
          self.addLabel( master,promptString,i)          
          self.addHelp(master,helpString,i) 
          i = self.addEnum(master,option,optionList[1:],initialValue,i)
           
        # Horizontal Enumeration Entry
        elif( typeCode == self.ENUM_ENTRY_HORIZ ):
          self.addLabel( master,promptString,i)          
          self.addHelp(master,helpString,i) 
          i = self.addEnumHoriz(master,option,optionList[1:],initialValue,i)   
              
        # Label
        elif( typeCode == self.LABEL ):
          self.addSpecialLabel( master,optionList[1:],promptString,i) 
          
        # List file entry
        elif( typeCode == self.LIST_FILE_ENTRY ):     
          self.addLabel( master,promptString,i)          
          self.addHelp(master,helpString,i)           
          self.addList(master,option,optionList[1:],initialValue,i)
              
        # List integer entry
        elif( typeCode == self.LIST_INT_ENTRY[0] ):
          self.addLabel( master,promptString,i)          
          self.addHelp(master,helpString,i)           
          self.addList(master,option,None,initialValue,i, mode=self.LIST_INT_ENTRY[0])
          
        # Line Seperator
        elif( typeCode == self.SEPERATOR[0] ):
          frame = Frame( master,relief='raised',borderwidth=2,
                         height=4 )
          frame.grid(row=i+1,sticky=EW, columnspan = 10, pady=5)
          
        # Multi-List Entry
        elif( typeCode == self.MULTI_LIST_ENTRY ):
          self.addLabel( master,promptString,i)          
          self.addHelp(master,helpString,i)           
          self.addMultiList(master,option,optionList[1:],initialValue,i)
        
        # SINGLE_LIST_ENTRY Entry
        elif( typeCode == self.SINGLE_LIST_ENTRY ):
          self.addLabel( master,promptString,i)          
          self.addHelp(master,helpString,i)           
          self.addSingleList(master,option,optionList[1:],initialValue,i)      
          
              
      master.grid( row=2)
      return None # initial focus
        

    def apply(self):
      """ Retrieves information from the widgets """
   
      for option in self.optionDatabase.keys():          

        initialValue, optionList, promptString,helpString = self.optionDatabase[option]
        
        typeCode = optionList[0]
        
        # Floating Point Entry
        if( typeCode == self.FLOAT_ENTRY[0] ):
          self.optionDatabase[option] = [float(self.widgetDict[option].get()),
                                        optionList,promptString,helpString]
        # Boolean Entry
        elif( typeCode == self.BOOLEAN_ENTRY[0] ): 
      
          self.optionDatabase[option] = [bool(float(self.widgetDict[option][1].get())),
                                        optionList,promptString,helpString] 
        
        # Integer Entry
        elif( typeCode == self.INT_ENTRY[0] ): 
          try:
            self.optionDatabase[option] = [int(float(self.widgetDict[option].get())),
                                        optionList,promptString,helpString] 
          except:
            print "ERROR: Option not set! Invalid value"
                                        
        # No dialog representation
        elif( typeCode == self.NO_ENTRY[0] or 
              typeCode == self.BOOL_BUTTON_ENTRY or
              typeCode == self.LABEL or
              typeCode == self.SEPERATOR[0] ):
          pass
        
        # List File Entry
        elif( typeCode == self.LIST_FILE_ENTRY ):
          self.optionDatabase[option] = [self.widgetDict[option].get(0,END),
                                        optionList,promptString,helpString]
                                        
        # List Integer Entry
        elif( typeCode == self.LIST_INT_ENTRY[0] ):
          itemList = self.widgetDict[option].get(0,END)
          intList = []
          for item in itemList:
            intList.append( int( item ) )
          self.optionDatabase[option] = [ intList,optionList,promptString,helpString]
        
        # Mutli-List Entry
        elif( typeCode == self.MULTI_LIST_ENTRY or typeCode == self.SINGLE_LIST_ENTRY):
          itemList = self.widgetDict[option].get(0,END)
          listItemsList = []
          for item in itemList:
            try:
              listItemsList.append( eval( item ) )
            except:
              print 'Error while evaluating items in MULTI_LIST_ENTRY', __file__
              continue
          self.optionDatabase[option] = [ listItemsList,optionList,promptString,helpString]
                                       
        # String/Filename/Dirname/Color Entry/Enumeration Entry
        else:
          self.optionDatabase[option] = [self.widgetDict[option].get(),
                                        optionList,promptString,helpString]
                                        
            
    def validate(self):
        """ Validate the data """
        return True
          
    def getOptionsDatabase(self):
      return self.optionDatabase
    
    def isCanceled(self):
      return self.CancelPressed
    
    
    #---------------------  Callbacks -------------------------------
    
    def buttonCallback(self, option, buttonLabel):
      """ When special button is pushed, immediately okays the dialog, toggles button value """
      if( self.optionDatabase[option][0] ):   self.optionDatabase[option][0] = False
      else:                               self.optionDatabase[option][0] = True
      self.ok()
    
    def helpMe(self, helpString):      
      tkMessageBox.showinfo("Info", helpString)
    
    def listNew(self,option,optionList):      
      label = optionList[0]    
      fileType = optionList[1]    
      fileDialogType = optionList[2]
      initialDir = optionList[3]
      path = askopenfilename(filetypes=fileType, title=label,
                              initialdir=initialDir )
      if( path == '' ): return
      name = self.processPath( path, fileDialogType )
      
      itemList = self.widgetDict[option]
      itemList.insert(END, name )
      
      itemList.selection_clear(0,END)
      itemList.selection_set(END)
      
    def listNewInteger(self, option):      
      from tkSimpleDialog import askinteger
      result = askinteger("New Integer", "Value", initialvalue=0)
      if( not result ): return
      
      itemList = self.widgetDict[option]
      itemList.insert(END, str(result) )
      
      itemList.selection_clear(0,END)
      itemList.selection_set(END)
      
    def MultiListEdit( self, option, optionList):
      #todo: MultiListEdit
      itemList = self.widgetDict[option]
      
      currentSelectionIndex = itemList.curselection()

      if( not currentSelectionIndex ): return
      currentSelectionIndex = currentSelectionIndex[0]
      stringItem = itemList.get( currentSelectionIndex )
      
      # Extract the data from the string: should be a list of values
      try:
        valueList = eval( stringItem )
      except:
        print 'ERROR: unable to extract data from item list string',__file__
        return
      
      # Build an options dialog for the options
      j = 0
      optsDB = simpleOptionWrapper()
      for i in range(0, len(optionList) - 1, 4 ):   
        name = optionList[i] 
        optsDB.add( name, [ valueList[j],optionList[i+2], 
                           name, optionList[i+3]] )
        j += 1
        
      # Show the options and get teh result
      result = optsDB(root=self.parent, pos=self.position,title=option )
      if( result.isCanceled() ):
        ##print "Dialog aborted by user cancel"
        return
      else:
        resultDict = result.getOptionsDatabase()
        multiList = []
        for option in optsDB.getOrderedOptionsKeys():
          ##print 'Option', option, '=', resultDict[option][0]
          multiList.append( resultDict[option][0] )
        
      # Modify the list box to reflect the edited data
      index = int( currentSelectionIndex )
      itemList.delete(index)
      itemList.selection_clear(0,END)
      
      itemList.insert(currentSelectionIndex, str(multiList) )
      itemList.selection_set(currentSelectionIndex)
      
      ## itemList.insert(END, str(multiList) )
      ## itemList.selection_clear(0,END)
      ## itemList.selection_set(END)
      
      
    def MultiListNew( self, option, optionList):
      #todo: MultiListNew
      itemList = self.widgetDict[option]

      optsDB = simpleOptionWrapper()
      for i in range(0, len(optionList) - 1, 4 ):   
        name = optionList[i] 
        optsDB.add( name, [ optionList[i+1],optionList[i+2], 
                           name, optionList[i+3]] )
        
      result = optsDB(root=self.parent, pos=self.position,title=option )
      if( result.isCanceled() ):
        ##print "Dialog aborted by user cancel"
        return
      else:
        resultDict = result.getOptionsDatabase()
        multiList = []
        for option in optsDB.getOrderedOptionsKeys():
          ##print 'Option', option, '=', resultDict[option][0]
          multiList.append( resultDict[option][0] )
        
      itemList.insert(END, str(multiList) )
      itemList.selection_clear(0,END)
      itemList.selection_set(END)
      
    def listDown(self, option):     
        itemList = self.widgetDict[option]
      
        if( not itemList.curselection() ): return
        index = int( itemList.curselection()[0] )
        if( index >= itemList.index(END)-1 ): return
        
        selected = itemList.get( index )        
        itemList.delete(index)
        newIndex = index + 1   
        itemList.insert( newIndex, selected )
        
        itemList.selection_clear(0,END)
        itemList.selection_set(newIndex)
    
    def listUp(self, option):     
        itemList = self.widgetDict[option]
        
        #index = self.itemList.index(ANCHOR)
        if( not itemList.curselection() ): return
        index = int( itemList.curselection()[0] )
        if( index == 0 ): return
        selected = itemList.get( index )
        itemList.delete(index)
        newIndex = index - 1 
        itemList.insert( newIndex, selected )
        
        itemList.selection_clear(0,END)
        itemList.selection_set(newIndex)
      
    def listDel(self, option):    
        itemList = self.widgetDict[option]
        
        #items = self.itemList.curselection()
        if( not itemList.curselection() ): return
        index = int( itemList.curselection()[0] )
        itemList.delete(index)
        itemList.selection_clear(0,END)
    
    def processPath( self, path, fileDialogType ):
      # Return full filepath
      if( fileDialogType == OptionDialog.FILEPATH ): 
        name = path
        
      # This will get the relative dir instead of the filename
      elif( fileDialogType == OptionDialog.RELATIVE_DIRNAME ):
        path = os.path.split( path )[0]     # Get rid of the filename
        name = os.path.split( path )[1]     # Just keep the relative pathname
        
      # This gets the filename, but no path and no extension
      elif( fileDialogType == OptionDialog.FILENAME_ONLY ):
        name = os.path.split( path )[1]     # Get rid of the pathname
        name = string.split( name, '.' )[0] # Lose the extension
        
      else: 
        name = ''
      return name
    
    def fileNameOpener(self,option,optionList,widget):
      """ Gets the name of the opened file and shows it in the widget """
      label = optionList[1]    
      fileType = optionList[2]    
      fileDialogType = optionList[3]
      initialDir = optionList[4]
      path = askopenfilename(filetypes=fileType, title=label,
                              initialdir=initialDir )
      if( path == '' ): return
      name = self.processPath( path, fileDialogType )
      widget.delete(0,len( widget.get() ) )
      widget.insert(0, name )
      self.widgetDict[option] = widget
                
    
    def colorChooser(self,option,widget):
      """ Gets the name of the color from the color dialog """
      color = askcolor()
      if( color and len(color) > 1 and color[0] != None ):
        widget.delete(0,len( widget.get() ) )
        widget.insert(0, str(color[1]) )
        self.widgetDict[option] = widget      
    
    #---------------------  END Callbacks -------------------------------
          

class simpleOptionWrapper:
  """
  This is only intended for testing this module
  Use OptionDatabase.py for serious applications since it provides load/save to
  file support for free.
  """
  
  def __init__(self):
    self.optionDatabase = dict()
    self.optionOrder = []
    
  def add( self, option, value ):
    self.optionDatabase[ option ] = value
    self.optionOrder.append( option )
    
  def getOrderedOptionsKeys(self):
    return self.optionOrder
    
  def __call__( self, root=None, title=None, pos=None, grab=True ):
    if( not root ):   root = Tk()
    if( not title ):  title = "The Dialog Without A Title"
    if( not pos ):    pos = [50,50] 
    return OptionDialog(root, title, self.optionDatabase,self.optionOrder,pos, grab)


# --------------------------- UNIT TEST -------------------------------------
if __name__ == "__main__":

  if( 1 ):
    # This version looks much nicer with the wrapper...
    optsDB = simpleOptionWrapper()
    
    optsDB.add( 'Integer Test', [2,OptionDialog.INT_ENTRY,
                        "How many pies can you eat in a day?",
                        "You don't get any extra points for eating a dozen :p"] )
                        
    optsDB.add( 'Float Test', [3.14,OptionDialog.FLOAT_ENTRY,"What is Pi?",""] )
    optsDB.add( 'Boolean Test', [1,OptionDialog.BOOLEAN_ENTRY,"Do you like Pie?",""] )
    optsDB.add( 'String Test', ['Strawberry Shortcake',
                            OptionDialog.STRING_ENTRY,"What is better than pie?",
                            "St Huberts has some really good shortcake :D"] )
    
    optionList = [OptionDialog.FILE_ENTRY,"Choose File",[("Desert File","*.*")], 
                  OptionDialog.FILEPATH]
    optsDB.add( 'Filename Test', ['Desserts',optionList,"File that contains pies?",""] )
    
    optionList = [OptionDialog.FILE_ENTRY,"Choose Directory",
                   [("Choose any file in directory","*")], 
                   OptionDialog.RELATIVE_DIRNAME]
    optsDB.add( 'Dirname Test',  ['Recipes',optionList,"Directory that contains pies?",""] )
    
    optionList = [OptionDialog.COLOR_ENTRY,"Choose Color"]
    optsDB.add( 'Color Test', ['Red',optionList,"Color of your favorite pie?",""] )
    
    optsDB.add( 'No Entry Test', ['Hidden',OptionDialog.NO_ENTRY,'',''] )
    
    optionList = [OptionDialog.BOOL_BUTTON_ENTRY,"Add"]
    optsDB.add( 'Button Test', [False,optionList,'Would you like to add pies to your cart?','Free delivery!'] )
    
    optionList = [OptionDialog.ENUM_ENTRY, "Strawberry Shortcake", "Sugar Pie", "Apple Pie" ]
    optsDB.add( 'Enumeration Test', ["Strawberry Shortcake",optionList,'Choose one pie','Free delivery!'] )
    
    optionList = [OptionDialog.ENUM_ENTRY_HORIZ, "Duck Hunt", "Metroid", "Contra" ]
    optsDB.add( 'Horizontal Enumeration Test', ["Duck Hunt",optionList,'Choose best NES game','Nostalgia moment?'] )
    
    
    optionList = [OptionDialog.LABEL,"Times 12","blue", "left" ]
    optsDB.add( 'Label Test', [None,optionList,'Attention: pie stolen! Repeat pie stolen!', ''] )
    
    optionList = [OptionDialog.LIST_FILE_ENTRY, 'Choose File',[("Any File","*")]
                   ,OptionDialog.FILENAME_ONLY,'']
    optsDB.add( 'List File Test', [["Strawberry Shortcake","Phat Angel Cake"],optionList,
                                 'List it','No help for you!'] )
    
    optsDB.add( 'List Int Test', [[2,4,8],OptionDialog.LIST_INT_ENTRY,
                                 'List int','No help for you!'] )
                                 
    optionList = [OptionDialog.MULTI_LIST_ENTRY, 
                  'Radius',8, OptionDialog.INT_ENTRY, '',
                  'Threshold',100, OptionDialog.INT_ENTRY,'',
                  'MinStroke',4, OptionDialog.INT_ENTRY,'',
                  'MaxStroke',16, OptionDialog.FLOAT_ENTRY,'',
                   ]
    optsDB.add( 'Multi List Test', [ [ [8,100,1,16], [4,30,4,16],[2,10,8,16] ],optionList,
                                 'Muli List it','No help for you!'] )
    
    optsDB.add( 'Seperator Test', ['Ignored',OptionDialog.SEPERATOR,"Ignored?","Ignored!"] )

    optionList = [OptionDialog.SINGLE_LIST_ENTRY, 
                  'Radius',8, OptionDialog.INT_ENTRY, '',
                  'Threshold',100, OptionDialog.INT_ENTRY,'',
                  'MinStroke',4, OptionDialog.INT_ENTRY,'',
                  'MaxStroke',16, OptionDialog.FLOAT_ENTRY,'',
                   ]
    optsDB.add( 'Single List Test', [[[ 8,100,1,16 ]],optionList,
                                 'Single List it','No help for you!'] )
    

    # Call optsDB to show the Options Dialog to the user
    result = optsDB()
    if( result.isCanceled() ):
      print "Dialog aborted by user cancel"
    else:
      resultDict = result.getOptionsDatabase()
      for option in optsDB.getOrderedOptionsKeys():
        print 'Option', option, '=', resultDict[option][0]
  
