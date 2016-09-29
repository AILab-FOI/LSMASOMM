#Colors.py
#Francois Plamondon
#Summer 2003
import Tkinter
import Colors
import os
try:
  import textwrap
except:
  print 'Minor error: textwrap not found (most likely cause: old version of Python)'


from FilePaths import GRAPHIC_EDITOR_DATA

#ToolSelector is instantiated by the editor
class ToolSelector:
    def __init__(self, masterFrame, eventHandler, where):
        toolSelectionFrame = Tkinter.Frame(masterFrame)
        self.frame = Tkinter.Frame(toolSelectionFrame)
        self.eventHandler = eventHandler
        
        select          = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'select.xbm' ) )
        zoom            = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'zoom.xbm' ) )
        rectangle       = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'rectangle.xbm' ) )
        oval            = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'oval.xbm' ) )
        line            = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'line.xbm' ) )
        text            = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'text.xbm' ) )
        polyline        = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'polyline.xbm' ) )
        smoothpolyline  = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'smoothpolyline.xbm' ) )
        polygon         = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'polygon.xbm' ) )
        smoothpolygon   = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'smoothpolygon.xbm' ) )
        image           = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'image.xbm' ) )
        connector       = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'connector.xbm' ) )
        attribute       = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'attribute.xbm' ) )
        namedconnector  = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'namedconnector.xbm' ) )
        
        
        
        
        self.toolDict = {"select":ToolButton("select", select, self.frame, self, 0, 0),
                         "zoom":ToolButton("zoom", zoom, self.frame, self, 0, 1),
#                         "group":ToolButton("group", "@group.xbm", self.frame, self, 2, 0),
#                         "ungroup":ToolButton("ungroup", "@ungroup.xbm", self.frame, self, 2, 1),
#                         "bring":ToolButton("bring", "@bring.xbm", self.frame, self, 3, 0),
#                         "push":ToolButton("push", "@push.xbm", self.frame, self, 3, 1),
                         "rectangle":ToolButton("rectangle", rectangle, self.frame, self, 1, 0),
                         "oval":ToolButton("oval", oval, self.frame, self, 1, 1),
                         "line":ToolButton("line", line, self.frame, self, 2, 0),
                         "text":ToolButton("text", text, self.frame, self, 2, 1),
                         "polyline":ToolButton("polyline", polyline, self.frame, self, 3, 0),
                         "smoothpolyline":ToolButton("smoothpolyline", smoothpolyline, self.frame, self, 3, 1),
                         "polygon":ToolButton("polygon", polygon, self.frame, self, 4, 0),
                         "smoothpolygon":ToolButton("smoothpolygon", smoothpolygon, self.frame, self, 4, 1),
                         "image":ToolButton("image", image, self.frame, self, 5, 0),
                         "connector":ToolButton("connector", connector, self.frame, self, 5, 1),
                         "attribute":ToolButton("attribute", attribute, self.frame, self, 6, 0),
                         "namedPort":ToolButton("namedPort", namedconnector, self.frame, self, 6, 1)}
        
        self.isResetingLabel = False
        self.labelFrame = Tkinter.Frame(toolSelectionFrame)
        self.labelTextVar = Tkinter.StringVar()
        self.labelTextVar.set('SELECT')
        self.label = Tkinter.Label(self.labelFrame, width=10, height=3,
                                    textvariable=self.labelTextVar,
                                   background='white', relief='groove')
        self.label.pack(side='top')
        self.labelFrame.pack(side='top')
        self.frame.pack(side='bottom')
        
        toolSelectionFrame.pack(side=where)
        
        self.currentTool = self.toolDict["select"]
        self.currentTool.sinkButton()
        

    def onToolButton(self, tool, button):
        if button == 1:
            self.currentTool.raiseButton()
            self.currentTool = tool
            self.currentTool.sinkButton()
            self.eventHandler.onToolSelection(tool.getName())


    def set(self, toolName):
        if self.toolDict.has_key(toolName):
            self.currentTool.raiseButton()
            self.currentTool = self.toolDict[toolName]
            self.currentTool.sinkButton()
            self.setOnHoverTool(toolName)
        else:
            raise TypeError, "given string is not a tool name"


    def get(self):
        return self.currentTool.getName()


    def setOnHoverTool(self, name):
        finalText = ''
        try:
          for textLine in textwrap.wrap(name.upper(),7):
            if(textLine):
              finalText += textLine + '-\n'
          self.labelTextVar.set(finalText[:-2])
        except:
          pass
        if(not self.isResetingLabel):
          self.isResetingLabel = True
          self.frame.after(3000, self.resetToolLabel)         
        
    def resetToolLabel(self, *args):
        self.isResetingLabel = False
        self.setOnHoverTool(self.currentTool.getName())


#instantiated by ToolSelector
class ToolButton:
    def __init__(self, name, icon, masterFrame, eventHandler, row, column):
        self.name = name
        self.eventHandler = eventHandler
        self.button = Tkinter.Button(masterFrame, width = 25, height = 25, bitmap=icon)
        self.button.bind("<Button-1>", self.onButton)
        self.button.grid(row=row, column=column)
        
        self.button.bind("<Motion>", self.onHover)
        
    def sinkButton(self):
        self.button.config(relief= Tkinter.SUNKEN)

    def raiseButton(self):
        self.button.config(relief= Tkinter.RAISED)

    def onButton(self, event):
        self.eventHandler.onToolButton(self, event.num)

    def getName(self):
        return self.name
        
    def onHover(self, event):
        self.eventHandler.setOnHoverTool(self.name)


#OutlineFillOptionSelector is instantiated by the editor
# the current option is represented as a pair, where the first element is true iff outline is true, and the
# second element is true iff fill is true. At least one is true.
class OutlineFillOptionSelector:
    def __init__(self, masterFrame, eventHandler, where):
        self.frame = Tkinter.Frame(masterFrame, relief=Tkinter.RAISED, bd=1)
        self.defaultColor = self.frame.cget("bg")
        self.bWidth = 56 #button width
        self.bHeight = 35 #button height
        self.eventHandler = eventHandler
        
        outlinefill   = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'outlinefill.xbm' ) )
        outline       = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'outline.xbm' ) )
        fill          = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'fill.xbm' ) )
        
        self.outlineFillButton = Tkinter.Button(self.frame, width = self.bWidth, 
                  height = self.bHeight, bitmap=outlinefill, 
                  relief=Tkinter.SUNKEN, bd=0, bg="blue", activebackground="blue")
        self.outlineFillButton.bind("<Button-1>", self.onOutlineFillButton)
        self.outlineFillButton.pack(side=Tkinter.TOP)

        self.outlineButton = Tkinter.Button(self.frame, width = self.bWidth, 
                          height = self.bHeight, bitmap=outline, 
                          relief=Tkinter.SUNKEN, bd=0, activebackground=self.defaultColor)
        self.outlineButton.bind("<Button-1>", self.onOutlineButton)
        self.outlineButton.pack(side=Tkinter.TOP)

        self.fillButton = Tkinter.Button(self.frame, width = self.bWidth, 
                          height = self.bHeight, bitmap=fill, 
                          relief=Tkinter.SUNKEN, bd=0, activebackground=self.defaultColor)
        self.fillButton.bind("<Button-1>", self.onFillButton)
        self.fillButton.pack(side=where)
        self.currentOption = (1,1) # default to outline + fill
#        self.frame.grid(row=row, column=column)
        self.frame.pack(side=Tkinter.TOP)

    def onOutlineFillButton(self, event):
        self.outlineFillButton.config(bg="blue", activebackground="blue")
        if self.currentOption == (1,0):
            self.outlineButton.config(bg=self.defaultColor, activebackground=self.defaultColor)
        elif self.currentOption == (0,1):
            self.fillButton.config(bg=self.defaultColor, activebackground=self.defaultColor)
        self.currentOption = (1,1)
        self.eventHandler.onOutlineFillOption(self.currentOption)
 
    def onOutlineButton(self, event):
        self.outlineButton.config(bg="blue", activebackground="blue")
        if self.currentOption == (1,1):
            self.outlineFillButton.config(bg=self.defaultColor, activebackground=self.defaultColor)
        elif self.currentOption == (0,1):
            self.fillButton.config(bg=self.defaultColor, activebackground=self.defaultColor)
        self.currentOption = (1,0)
        self.eventHandler.onOutlineFillOption(self.currentOption)

    def onFillButton(self, event):
        self.fillButton.config(bg="blue", activebackground="blue")
        if self.currentOption == (1,1):
            self.outlineFillButton.config(bg=self.defaultColor, activebackground=self.defaultColor)
        elif self.currentOption == (1,0):
            self.outlineButton.config(bg=self.defaultColor, activebackground=self.defaultColor)
        self.currentOption = (0,1)
        self.eventHandler.onOutlineFillOption(self.currentOption)

    def get(self):
        return self.currentOption

#        self.eventHandler.onFillOutlineOption()

#LineWidthSelector is instantiated by the editor
class LineWidthSelector:
    def __init__(self, masterFrame, eventHandler, where):
        self.eventHandler = eventHandler
        self.width = 60 #width of a "line width button"
        self.lineWidthList = [1,2,3,4,5,6,8,10,12]
        self.canvas = Tkinter.Canvas(masterFrame, width=self.width, height=110, relief=Tkinter.RAISED,bd=1)
        self.lineWidthButtonList = []
        self.currentLineWidth=1 # current line width of the line width selector
        pad = 5
        y = 0
        for lw in self.lineWidthList:
            self.lineWidthButtonList.append(LineWidthButton(self.canvas, self, lw, self.width, y))
            y = y + lw + 6
#        self.canvas.grid(row=row, column=column)
        self.canvas.pack(side=where)
        self.currentLineWidthButton = self.lineWidthButtonList[0]
        self.currentLineWidthButton.select()

    def onLineWidthButton(self, lineWidthButton):
        self.currentLineWidthButton.deselect()
        self.currentLineWidth = lineWidthButton.getLineWidth()
        self.currentLineWidthButton = lineWidthButton
        self.currentLineWidthButton.select()
        self.eventHandler.onLineWidth(self.currentLineWidth)

    def get(self):
        return self.currentLineWidth


#instantiated by LineWidthSelector
class LineWidthButton:
    def __init__(self, canvas, eventHandler, lineWidth, width, y):
        self.canvas = canvas
        self.eventHandler = eventHandler
        self.lineWidth = lineWidth
        pad = 5
        self.rectangle = self.canvas.create_rectangle(0, y+1, width, y+self.lineWidth+2*pad-1, width=0)
        self.defaultColor = self.canvas.itemcget(self.rectangle, "fill")
        self.line = self.canvas.create_line(pad, y+pad+self.lineWidth/2, width-pad, y+pad+self.lineWidth/2, width=self.lineWidth, fill="black")
        self.canvas.tag_bind(self.line, "<Button-1>", self.onButton)
        self.canvas.tag_bind(self.rectangle, "<Button-1>", self.onButton)

    def onButton(self, event):
        self.eventHandler.onLineWidthButton(self)

    def select(self):
        self.canvas.itemconfig(self.rectangle, fill="blue")

    def deselect(self):
        self.canvas.itemconfig(self.rectangle, fill=self.defaultColor)

    def getLineWidth(self):
        return self.lineWidth



class MenuBar:
    def __init__(self, root, editor, mainHandler): #goes to top by itself
        self.menu = Tkinter.Menu(root)
        self.mainHandler = mainHandler
        # create file menu
        self.fileMenu = Tkinter.Menu(self.menu, tearoff=0)
        
        self.fileMenu.add_command(label="Snap grid settings", accelerator="F1", 
                                  command=self.mainHandler.onSnapSetting )
        self.fileMenu.add_command(label="Icon Positioner", accelerator="F2", 
                                  command=self.mainHandler.onIconPositioner )
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Save", accelerator="Ctrl+S", 
                                  command=self.mainHandler.onSave)
        self.fileMenu.add_command(label="Postscript Export", accelerator="Ctrl+E", 
                                  command=self.mainHandler.onExport)
        self.fileMenu.add_separator()
        self.fileMenu.add_command(label="Exit", accelerator="Alt+X",
                                  command=self.mainHandler.onExit)
      

        self.menu.add_cascade(label="File", menu=self.fileMenu)

        # create edit menu
        self.editMenu = Tkinter.Menu(self.menu, tearoff=0, postcommand=self.editPostCommand)

        self.editMenu.add_command(label="Undo", accelerator="Ctrl+Z", command=mainHandler.onUndo)
        self.editMenu.add_separator()
        self.editMenu.add_command(label="Cut", accelerator="Ctrl+X", command=mainHandler.onCut)
        self.editMenu.add_command(label="Copy", accelerator="Ctrl+C", command=mainHandler.onCopy)
        self.editMenu.add_command(label="Paste", accelerator="Ctrl+V", command=mainHandler.onPaste)
        self.editMenu.add_command(label="Delete", accelerator="Delete", command=mainHandler.onDelete)
        self.editMenu.add_separator()
        self.editMenu.add_command(label="to Top", accelerator="Ctrl+T", command=mainHandler.onBringToTop)
        self.editMenu.add_command(label="to Bottom", accelerator="Ctrl+B", command=mainHandler.onPushToBottom)
        self.editMenu.add_separator()
        self.editMenu.add_command(label="Group", accelerator="Ctrl+G", command=mainHandler.onGroup)
        self.editMenu.add_command(label="Ungroup", accelerator="Ctrl+F", command=mainHandler.onUngroup)
        self.editMenu.add_separator()
        
        def rotateHandler():
            """ Quick hack to get rotation into the menu-system """
            # Check if we have a select handler (necessary condition)   
            selectHandler = mainHandler.currentHandler
            if( selectHandler != mainHandler.selectHandler ):  return
        
            selectHandler.deselect()
            selectHandler.currentHandler = selectHandler.rotationHandler
            selectHandler.currentHandler.start( selectHandler.gfList, None )
            selectHandler.currentHandler.stopHandler()
            
        self.editMenu.add_command(label="Rotate", accelerator="MB 2", command=rotateHandler )
        
        def moveHandler(direction):
            """ Quick hack to get pixel movement into men-system """
            selectHandler = mainHandler.currentHandler
            if( selectHandler != mainHandler.selectHandler ):  return
            
            if( direction == 'Up' ):
                for g in selectHandler.gfList:
                    g.translate(0, -1 / editor.getZoom() )
            elif( direction == 'Down' ):
                for g in selectHandler.gfList:
                    g.translate(0, 1 / editor.getZoom() )
            elif( direction == 'Right' ):
                for g in selectHandler.gfList:
                    g.translate(1, 0 / editor.getZoom() )
            elif( direction == 'Left' ):
                for g in selectHandler.gfList:
                    g.translate(-1, 0 / editor.getZoom() ) 
                    
        self.editMenu.add_command(label="Move Up", accelerator="Up", 
                                  command=lambda d='Up': moveHandler(d) )
        self.editMenu.add_command(label="Move Down", accelerator="Down", 
                                  command=lambda d='Down': moveHandler(d) )
        self.editMenu.add_command(label="Move Left", accelerator="Left", 
                                  command=lambda d='Left': moveHandler(d) )
        self.editMenu.add_command(label="Move Right", accelerator="Right", 
                                  command=lambda d='Right': moveHandler(d) )
                                  
        self.editMenu.add_separator()
        self.editMenu.add_command(label="Properties...", command=mainHandler.onProperties)

        self.menu.add_cascade(label="Edit", menu=self.editMenu)
        
        # create model menu
        self.modelMenu = Tkinter.Menu(self.menu, tearoff=0 )
  
        self.modelMenu.add_command( label = "Changes at run-time DISABLED", 
                                   command=lambda mH = mainHandler, mM = self.modelMenu:
                                   mH.onRunTimeChange( mM )  )        
        self.modelMenu.add_command(label="Set graphical constraints", 
                                         command=mainHandler.onSetConstraints )
        self.modelMenu.add_command(label="Help", 
                                         command=mainHandler.onConstraintHelp )
                      
        self.menu.add_cascade(label="Scripting", menu=self.modelMenu)

        root.config(menu = self.menu)
        
    def getModelMenu( self ):
        return self.modelMenu

    def editPostCommand(self):
        self.editMenu.entryconfigure(0, state=Tkinter.DISABLED) #undo
        self.editMenu.entryconfigure(2, state=Tkinter.DISABLED) #cut
        self.editMenu.entryconfigure(3, state=Tkinter.DISABLED) #copy
        self.editMenu.entryconfigure(4, state=Tkinter.DISABLED) #paste
        self.editMenu.entryconfigure(5, state=Tkinter.DISABLED) #delete
        self.editMenu.entryconfigure(7, state=Tkinter.DISABLED) #to top
        self.editMenu.entryconfigure(8, state=Tkinter.DISABLED) #to bottom
        self.editMenu.entryconfigure(10, state=Tkinter.DISABLED) #group
        self.editMenu.entryconfigure(11, state=Tkinter.DISABLED) #ungroup
        self.editMenu.entryconfigure(13, state=Tkinter.DISABLED) # Rotate
        self.editMenu.entryconfigure(14, state=Tkinter.DISABLED) # Up
        self.editMenu.entryconfigure(15, state=Tkinter.DISABLED) # Down
        self.editMenu.entryconfigure(16, state=Tkinter.DISABLED) # Right
        self.editMenu.entryconfigure(17, state=Tkinter.DISABLED) # Left
        self.editMenu.entryconfigure(19, state=Tkinter.DISABLED) #properties
        self.mainHandler.onEditMenu(self.editMenu)

    def printFunction(self):
        print "print command"


class StatusBar(Tkinter.Frame):
    def __init__(self, masterFrame, gf, zoom, x, y):
        Tkinter.Frame.__init__(self, masterFrame)
        self.label = Tkinter.Label(self, bd=1, relief=Tkinter.SUNKEN, anchor=Tkinter.W)
        self.label.pack(fill=Tkinter.X)
        self.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
        self.gf = gf
        self.zoom = zoom
        self.x = x
        self.y = y
        self.update()

    def setGF(self, gf):
        self.gf = gf
        self.update()

    def setZoom(self, zoom):
        self.zoom = zoom
        self.update()

    def setXY(self, x, y):
        self.x = x
        self.y = y
        self.update()

    def update(self):
        string = self.gf + "\t\tZoom: " + str(int(self.zoom * 100)) + "%" + \
                "\t\t" + "%.2f" % self.x + "\t" + "%.2f" % self.y
        self.label.config(text=string)
        self.label.update_idletasks()
        

