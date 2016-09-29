"""
GraphicEditor.py

Icon-Editor for AToM3. Imports old graphical appearence files or creates new
ones. The quickest & easiest way to make AToM3 graphical appearence files :D

Created by Francois Plamondon, Summer 2003
Modified by Denis Dube, Summer 2004
"""

import Tkinter, pickle, tkFileDialog, os, tkMessageBox, sys, re, Dialog

import Graphics
import Colors
import Tools
import MainHandler
import GFVisitors
import SaveGFVisitor
from Workspace        import Workspace

from Scripting        import Scripting
from FilePaths        import GRAPHIC_EDITOR_DATA
from IconPositioner   import IconPositioner
import SnapGrid



class Editor:
  
    # Canvas size is used by the snap grid to determine how far to draw the grid
    # Actually, should be called the canvas bounding box :p
    # BTW: Using negative values, or values that are too small, doesn't work well :p
    CANVAS_SIZE_TUPLE = [0, 0, 2000, 2000]
  
    def __init__(self, semObject, className, modelPath=None):
        
        # Use the AToM3 Tkinter root window
        self.className = className
        root = self.rootInitilization(semObject, modelPath)
        if( not root ): return
  
        self.root = root
        self.mainHandler = MainHandler.MainHandler(self)
        root.bind("<Key>", self.mainHandler.onKey)
        root.bind("<Shift-Key>", self.mainHandler.onShiftKey)
        root.bind("<Control-Key>", self.mainHandler.onControlKey)
        zoom = 1.0
        self.menuBar = Tools.MenuBar(root, self, self.mainHandler) #goes to top by itself
        self.statusBar = Tools.StatusBar(root, "", zoom, 0, 0) #goes to bottom by itself

        self.colorSelector = Colors.ColorSelector(root, self.mainHandler) #goes to bottom by itself
        
        self.toolFrame = Tkinter.Frame(root, relief=Tkinter.RAISED, bd=1)
        self.toolSelector = Tools.ToolSelector(self.toolFrame, self.mainHandler, Tkinter.TOP)
        self.outlineFillOptionSelector = Tools.OutlineFillOptionSelector(self.toolFrame, self.mainHandler, Tkinter.TOP)
        self.lineWidthSelector = Tools.LineWidthSelector(self.toolFrame, self.mainHandler, Tkinter.TOP)
        self.toolFrame.pack(side=Tkinter.LEFT)
        self.workspace = Workspace(self, 
                                   self.CANVAS_SIZE_TUPLE[2], self.CANVAS_SIZE_TUPLE[3], 
                                   self.CANVAS_SIZE_TUPLE[2], self.CANVAS_SIZE_TUPLE[3], 
                                   self.mainHandler, zoom) #goes to the right by itself
        self.workspace.setZoom(zoom, 0, 0)
        self.canvas = self.workspace.getCanvas()
        
        self.scripting = Scripting()
        ## self.GFs = self.open() 
        self.GFs = []
        self.extendedInitilization( semObject )
        
        self.clipboardList = []
        self.undoStack = []
        self.mainHandler.start()
        self.compositionVisitor = GFVisitors.CompositionVisitor(self)
        self.colorVisitor = GFVisitors.ColorVisitor()
        self.widthVisitor = GFVisitors.WidthVisitor()
        self.optionVisitor = GFVisitors.OptionVisitor(self)
        
        # Carefully try to load the GF model (may fail for random reasons)
        try:    self.GFs = self.open()
        except: raise
                        
    def rootInitilization(self, semObject, modelPathAndFile):
      """
      Extension to the old initilization routine 
      This directly sets up the editor for generating icons for AToM3 
      """
            
      # Do we have everything we need? Check the minimum requirements:
      try:
        atom3i = semObject.parent
        TkRoot = atom3i.parent 
        statusbar = atom3i.statusbar
      except:
        print "ERROR: Unable to start editor, lacking information (atom3i,TkRoot, or statusbar)"
        return None
      self.atom3i = atom3i
      
      # Do we have the fileName we'll be using to save the graphicalAppearence?       
      if(not modelPathAndFile):
        modelPathAndFile = statusbar.getState(statusbar.MODEL)[1][0]      
      self.modelPath = os.path.split(modelPathAndFile)[0]
      if( self.modelPath == '' ):
        tkMessageBox.showerror( 
               "Icon-Editor model path error",
               "Please save your ER model before modifying graphical appearences.",
               parent=TkRoot)
        return None
    
      
      # Setup a new toplevel window for the editor      
      root = Tkinter.Toplevel( TkRoot )
      root.title("Icon Editor - AToM3")
      root.geometry("%dx%d%+d%+d" % (800, 600, 100, 0))
      root.transient( TkRoot )
      root.grab_set() 
      
      return root 
      
    def extendedInitilization( self, semObject ):
      
      # SnapGrid: since this is a singleton, must first disable old stuff
      self.snapGridInfoTuple = None 
      self.snapGridInfoBackup = None           
      SnapGrid.applyLayout( self, disableForPrinting = True )
      SnapGrid.applyLayout( self )
      
      # Useful binds
      self.root.bind("<Alt-x>", lambda event: self.mainHandler.onExit() )
      self.root.bind("<F1>", lambda event: self.mainHandler.onSnapSetting() )
      self.root.bind("<Control-e>", lambda event: self.mainHandler.onExport() )      
      self.root.protocol("WM_DELETE_WINDOW", self.mainHandler.onExit )
      
      # AToM3 graphical appearence exporter
      self.exportVisitor = SaveGFVisitor.ATOM3_Export_Visitor(semObject, self)
      
      # Extra info: includes text attributes that change dynamically & named ports      
      self.attributes = semObject.attributesToDraw()
      
      # Icon Positioning System (not quite GPS)
      self.iconPositioner = IconPositioner( self )
      self.root.bind("<F2>", lambda event: self.iconPositioner.createDialog() )
      

    def iconPlacer(self, anchor = 'nw' ):
        """ 
        Places the graphical icon at a position determined by 'anchor'
        If anchor is 'nw', then the icon will be moved so that when the user
          creates an item with this icon, the top-left edge of the icon appears
          at the position the user clicked.
        If anchor is 'origin', then the icon appears exactly centered on origin.
        If anchor is of type 'float', then use the float value directly.
        """
        x0,y0,x1,y1 = self.getBoundingBox( self.getGFs() )
        
        # Top-Left positioning
        if( anchor == 'nw' ):
          dx = -x0
          dy = -y0 
          
        # Center positioning
        elif( anchor == 'origin' ):
          dx = -x0 - ( x1 - x0 ) / 2
          dy = -y0 - ( y1 - y0 ) / 2
        
        # Manual offset
        elif( type( anchor ) == type( float() ) ):
          dx = dy = anchor
          
        # Invalid use
        else:
          raise Exception, "Wake up and smell the API you lopsided kitten burger! j/k"

        for gf in self.getGFs():
          gf.translate( dx,dy )
        self.addUndoTranslate( self.getGFs(), dx, dy )

      
    def getAttributes( self ):
      return self.attributes
    
    def exit( self, event=None ): 
      """ Exit point for the Icon-Editor """
      # Clean up the snap grid
      SnapGrid.applyLayout( self, disableForPrinting = True )
      # Did AToM3 want its snap grid back? :D
      self.atom3i.toggleSnapGrid()    
      # Make this window go boom    
      self.root.destroy()     

    def getRoot(self):
        """get a reference to the root window of the editor"""
        return self.root

    def save(self, event=None):
        """ 
        1) Exports a graphical appearence file readable by AToM3
        2) Saves everything in a pickled file (not cross-platform compatible)
        """
        
        # Make sure that Text is at the end of the list
        gfListSorted = SaveGFVisitor.TextSortVisitor().sortGraphicalForms( self.getGFs() ) 
               
        # Uber-cool save dialog :D
        if( 1 ):
          text = 'The following AToM3 file will be generated:\n\n'+\
                  os.path.normpath( os.path.join( self.modelPath, 'graph_' + self.className + '.py' )  ) +\
                 '\n\nIf you have not already done so, you should position the icon '+\
                 'so that it appears where you expect it to in your models.'
          
          saveDialog = Dialog.Dialog(None, {'title': 'Saving graphical appearence file...',
                    'text': text,'bitmap': '', 'default': 0,
                    'strings': ('Position icon','Save','Save & Exit','Cancel')})
          
          # Position icon
          if( saveDialog.num == 0 ):
            self.iconPositioner.createDialog()            
            return self.save()
          
          # Save
          if( saveDialog.num == 1 ):
            self.exportVisitor.AToM3_export( gfListSorted )
            return self.root.focus_force() 
                    
          # Save & Exit
          if( saveDialog.num == 2 ):
            self.exportVisitor.AToM3_export( gfListSorted )
            return self.exit()
            
          # Cancel
          elif( saveDialog.num == 3 ):
            return self.root.focus_force() 
            
          
              
        # Lousy Dialog save, m'kay
        elif( 0 ):
          
          self.exportVisitor.AToM3_export( gfListSorted )
          
          tkMessageBox.showinfo( 
               "Saving Graphical Appearence",
               "The following AToM3 file has been generated:\n\n" + 
               os.path.normpath( os.path.join( self.modelPath, 'graph_' + self.className + '.py' )  ),             
               parent=self.root)
        
        # Pickle save.... EWWWWWWWWWWWWW!
        elif( 0 ):
          gfList = self.getGFs()
          gfListCopy = []
          for gf in gfList:
            gfListCopy.append(gf.copy())
          for gf in gfListCopy:
            gf.setEventHandler(None)
            gf.setCanvas(None)
            gf.setZoom(1.0)
            
          # Store extra scripting info
          gfListCopy = [ self.scripting ] + gfListCopy
            
          fileName = os.path.normpath( os.path.join( self.modelPath, 'graph_' + self.className + '.gf1' )  )          
          file=open( fileName, "w")
          pickle.dump(gfListCopy, file)
          file.close()

          tkMessageBox.showinfo( 
               "Saving Graphical Appearence",
               "The following icon-editor file has been generated:\n\n"+         
               fileName,
               parent=self.root)

    def export(self):
        filename = tkFileDialog.asksaveasfilename(title="Export",filetypes=[("Postscript","*.ps")])
        if filename != "":
            self.canvas.postscript(file=filename)

    def debug(self):
        """ Many things can go wrong when openning a graphical file
        this gives the user more flexibility in figuring out wtf went wrong """
        print "Error occured in importer", __file__
        from tkMessageBox import askokcancel
        res = askokcancel("Import Error",
                 "The existing graphical file could not be imported\n" \
                 "Press Ok to proceed normally, Cancel to dump error to console")
                 
        # Raise the 'caught' error
        if(res == False): raise

            
    def open( self ):
      """ Tries to open an existing graphical form in the AToM3 format and to reproduce it on canvas """
      
      fileName = os.path.normpath( os.path.join( self.modelPath, 'graph_' + self.className + '.py' )  )
      if( not os.path.exists( fileName ) ):  return []

      nameClass = "graph_"+self.className
      dc = Tkinter.Canvas(self.root)   
      
      # File is already loaded
      if nameClass in sys.modules.keys():   
        del sys.modules[nameClass]
        
      # Make sure we can reach the path and import from it
      sys.path.append( self.modelPath )
            
      # Load it in memory
      try:
        exec "import graph_"+self.className+"\n"
        sys.path = sys.path[:-1]
      except SyntaxError:	  #  class Name not valid 
        sys.path = sys.path[:-1]
        print "Syntax Error, Could not open graphical file", self.className 
        self.debug()
        return []
      except IOError:    # could not open file (?)
        sys.path = sys.path[:-1]   
        print "IO Error, Could not open graphical file", self.className 
        self.debug()
        return []
      except ImportError:   # could not open file...
        print "Import Error, Could not open graphical file", self.className 
        self.debug()
        sys.path = sys.path[:-1]
        return []   
      
      try:          
        # obtain the class object
        className = eval('graph_'+self.className+'.graph_'+self.className)     
      except:
        print 'WARNING:', 'graph_'+self.className+'.graph_'+self.className, \
              'not found' 
        return []
      new_obj = className(0, 0)                                            # create an instance of the new class
      new_obj.DrawObject(dc)					# draw the object
      
      # Get the constraints
      constraintList = []        
      for constraint in new_obj.constraintList:
        constraintList.append( constraint.getValue() )
      self.scripting.setConstraintList( constraintList ) 
      self.scripting.setRunTimeChange( new_obj.ChangesAtRunTime )
      
      GFlist = []
      
      # List with the handles of all the shapes drawn     
      handleList = []
      for handle in dc.find_withtag(new_obj.tag):							
        if( not handle in handleList): 
          handleList.append(handle)		
        
          
      # Get the connectors in self.connectors      
      for handle in new_obj.connectors:
        x0, y0, x1, y1 = dc.coords(handle)
        if( new_obj.namedConnectors.has_key( handle) ):
          name = new_obj.namedConnectors[ handle ]
          gf = Graphics.NamedConnector(x0, y0, canvas=self.canvas, eventHandler=self.mainHandler, name=name)
        else:
          gf = Graphics.Connector(x0, y0, canvas=self.canvas, eventHandler=self.mainHandler)
        GFlist.append( gf )
           
      
      # Get the drawn semantic attributes...
      handleAttributeDict = dict()
      for attribute in new_obj.attr_display.keys():	
        handleAttributeDict[ new_obj.attr_display[ attribute ] ] = attribute
    
      # Get the image dict, if any
      if( hasattr( new_obj, 'imageDict' ) ):
        Graphics.Image.IMAGE_DICT = new_obj.imageDict
            
      # Get the GraphicalForm objects 
      objectNumberPattern = re.compile( '\Agf(\d*)\Z' )
      for graphicalForm in new_obj.graphForms:	
      
        handle = graphicalForm.getHandler()  
        objectNumber = int( objectNumberPattern.search( graphicalForm.getName() ).group(1) )        
        coords = dc.coords( handle )
        objectType = dc.type(handle)	
         
        # Attribute  --- Special Text
        if( handleAttributeDict.has_key( handle ) ):
          attribute = handleAttributeDict[ handle ]
          
          fontObject = graphicalForm.getFont() 
          if( fontObject ):
            if( fontObject.cget( 'weight' ) == 'bold' ): bold = True
            else:                                        bold = False
            if( fontObject.cget( 'slant' ) == 'bold' ):  italic = True
            else:                                        italic = False
            GFlist.append( Graphics.Attribute(coords[0],coords[1], canvas=self.canvas, eventHandler=self.mainHandler,
                           fill=dc.itemcget(handle, "fill"),text=attribute,
                           anchor=dc.itemcget(handle, "anchor"), family=fontObject.cget( 'family' ),
                           size=int(float(fontObject.cget( 'size' ))),bold=bold,savedNumber=objectNumber,
                           width=int(float(dc.itemcget(handle, "width"))),
                           italic=italic,underline=int(float(fontObject.cget( 'underline' )))) )
          
          # Backward compatibility with graphical appearences that don't have
          # a font object. NOTE: Font type & size info is neccessarily lost.
          else:
            GFlist.append( Graphics.Attribute(coords[0],coords[1], canvas=self.canvas, eventHandler=self.mainHandler,
                           fill=dc.itemcget(handle, "fill"),text=attribute,
                           width=int(float(dc.itemcget(handle, "width"))),
                           anchor=dc.itemcget(handle, "anchor"), savedNumber=objectNumber ) )
                                
             
             
        elif( objectType == 'text' ):  
          
          fontObject = graphicalForm.getFont() 
          if( fontObject ):
            if( fontObject.cget( 'weight' ) == 'bold' ): bold = True
            else:                                        bold = False
            if( fontObject.cget( 'slant' ) == 'bold' ):  italic = True
            else:                                        italic = False
            GFlist.append( Graphics.Text(coords[0],coords[1], canvas=self.canvas, eventHandler=self.mainHandler,
                           fill=dc.itemcget(handle, "fill"),text=dc.itemcget(handle, "text"),
                           anchor=dc.itemcget(handle, "anchor"), family=fontObject.cget( 'family' ),
                           size=int(float(fontObject.cget( 'size' ))),bold=bold,savedNumber=objectNumber,
                           width=int(float(dc.itemcget(handle, "width"))),
                           italic=italic,underline=int(float(fontObject.cget( 'underline' )))) )
          
          # Backward compatibility with graphical appearences that don't have
          # a font object. NOTE: Font type & size info is neccessarily lost.
          else:
            GFlist.append( Graphics.Text(coords[0],coords[1], canvas=self.canvas, eventHandler=self.mainHandler,
                           fill=dc.itemcget(handle, "fill"),text=dc.itemcget(handle, "text"),
                           width=int(float(dc.itemcget(handle, "width"))),
                           anchor=dc.itemcget(handle, "anchor"), savedNumber=objectNumber ) )
                                 
             
                
        elif( objectType == 'line' ):
          
           if( dc.itemcget(handle, "smooth") == 'bezier' ): smooth = True
           else:                                            smooth = False
           GFlist.append( Graphics.Line( coords, canvas=self.canvas, eventHandler=self.mainHandler,
                         fill=dc.itemcget(handle, "fill"), stipple=dc.itemcget(handle, "stipple"),
                         arrow=dc.itemcget(handle, "arrow"),capstyle=dc.itemcget(handle, "capstyle"),
                         joinstyle=dc.itemcget(handle, "joinstyle"),smooth=smooth,savedNumber=objectNumber,
                         width=int(float(dc.itemcget(handle, "width"))) ) )
                         
        elif( objectType == 'polygon' ):  

           if( dc.itemcget(handle, "smooth") == 'bezier' ): smooth = True
           else:                                            smooth = False
           GFlist.append( Graphics.Polygon( coords, canvas=self.canvas, eventHandler=self.mainHandler,
                         fill=dc.itemcget(handle, "fill"), stipple=dc.itemcget(handle, "stipple"),
                         smooth=smooth,outline=dc.itemcget(handle, "outline"),savedNumber=objectNumber,
                         width=int(float(dc.itemcget(handle, "width"))) ) )         
                         
        elif( objectType == 'oval' ):  
          x0,y0,x1,y1 = coords
          GFlist.append( Graphics.Oval( x0,y0,x1,y1, canvas=self.canvas, eventHandler=self.mainHandler,
                         fill=dc.itemcget(handle, "fill"),outline=dc.itemcget(handle, "outline"),
                         width=int(float(dc.itemcget(handle, "width" ))), savedNumber=objectNumber,
                         stipple=dc.itemcget(handle, "stipple") ) )
          
          
        elif( objectType == 'rectangle' ):  
          
          x0,y0,x1,y1 = coords
          GFlist.append( Graphics.Rectangle( x0,y0,x1,y1, canvas=self.canvas, eventHandler=self.mainHandler,
                         fill=dc.itemcget(handle, "fill"),outline=dc.itemcget(handle, "outline"),
                         width=int(float(dc.itemcget(handle, "width" ))), 
                         savedNumber=objectNumber, stipple=dc.itemcget(handle, "stipple") ) )
       
        elif( objectType == 'image' ):  

          fileName = graphicalForm.getImageFilename()
          if( not Graphics.Image.IMAGE_DICT.has_key( fileName ) ):
            print "ERROR: could not load image " + fileName + "... SKIPPED"
            continue            
            
          '''
          pathName = ''
          for path in sys.path:
            if( not os.path.isdir( path ) ): continue
            if( pathName ): break
            for file in os.listdir( path ):
              if( file == fileName ):
                pathName = os.path.join( path, fileName )
                break
      
          if( not fileName ): 
            print "ERROR: could not load image " + fileName + "... SKIPPED"
            continue
          '''
          GFlist.append( Graphics.Image( coords[0], coords[1], canvas=self.canvas, eventHandler=self.mainHandler,
                         savedNumber=objectNumber, filename=fileName )  )       
        
        else:
          print "WARNING: Attempted to load unsupported objectType: " + str( objectType)
          
      #print GFlist
      dc.destroy()
      return GFlist
      



            
            
    def openOLD(self):
        if( 0 ):
          return  []
        
        elif( 1 ):
          fileName = os.path.join( self.modelPath, 'graph_' + self.className + '.gf1' )  
          if( os.path.exists( fileName ) ):                                      
            f = open( fileName, 'r' )
          else:
            return []
         
          try:
            gfList = pickle.load(f)
          except ImportError:
            print "Failed to load pickled graphic data"
            return []
            
          # Get the scripting stuff out of the way...
          self.scripting = gfList[0]
          if( self.scripting.getRunTimeChange() ):
            self.menuBar.getModelMenu().entryconfigure( 0, label = "Changes at run-time ENABLED" )
          else:
            self.menuBar.getModelMenu().entryconfigure( 0, label = "Changes at run-time DISABLED" )
           
           
          for gf in gfList[1:]:
              gf.setCanvas(self.canvas)
              gf.setEventHandler(self.mainHandler)
          return gfList[1:]
      
        elif( 0 ):
          return [Graphics.Rectangle(50, 50, 90, 90, canvas=self.canvas, outline="black", fill="blue", width=2, eventHandler=self.mainHandler),
                      Graphics.Oval(50, 50, 90, 90, canvas=self.canvas, outline="black", fill="green", eventHandler=self.mainHandler),
                      Graphics.Text(70, 90, canvas=self.canvas, zoom=1.00, eventHandler=self.mainHandler, text="text", fill="red"),
                      Graphics.Connector(100, 100, canvas=self.canvas, zoom=1.00, eventHandler=self.mainHandler),
                      Graphics.Polygon([50, 50, 90, 90, 32, 2], canvas=self.canvas,  outline="green", fill="purple", width=2, eventHandler=self.mainHandler),
                      Graphics.Line([50, 10, 50, 50, 132, 50], canvas=self.canvas, fill="black", eventHandler=self.mainHandler),
                      Graphics.Composite([Graphics.Rectangle(50, 20, 140, 100, canvas=self.canvas, outline="black", fill="yellow", width=2, eventHandler=self.mainHandler),
                                            Graphics.Rectangle(50, 50, 100, 120, canvas=self.canvas, outline="black", fill="purple", width=2, eventHandler=self.mainHandler),
                                            Graphics.Oval(70, 20, 40, 90, canvas=self.canvas, outline="black", fill="green", width=2, eventHandler=self.mainHandler),
                                            Graphics.Oval(50, 50, 40, 20, canvas=self.canvas, outline="black", fill="gray", width=2, eventHandler=self.mainHandler)], canvas=self.canvas, zoom=100, eventHandler=self.mainHandler)]


    def cut(self, gfList):
        if len(gfList) > 0:
            previousClipboard = self.clipboardList
            self.clipboardList = gfList
            indexList = []
            for gf in gfList:
                gf.setCanvas(None)
                indexList.append(self.removeGF(gf))
            pairList = map(None, gfList, indexList)
            self.undoStack.append((self.undo_cut, [previousClipboard, pairList]))


    def copy(self, gfList):
        if len(gfList) > 0:
            previousClipboard = self.clipboardList
            self.clipboardList = []
            for gf in gfList:
                cgf = gf.copy()
                self.clipboardList.append(cgf)
                cgf.setCanvas(None)


    def paste(self):
        clipboardCopy = []
        for gf in self.clipboardList:
            c = gf.copy()
            c.setZoom(self.getZoom())
            clipboardCopy.append(c)
        for gf in clipboardCopy:
            gf.translate(10, 10)
            gf.setCanvas(self.canvas)
            self.appendGF(gf)
        self.undoStack.append((self.undo_paste, [clipboardCopy]))
        return clipboardCopy

    #The GFs in gfList are not necessarily in the order in which they are drawn.
    #Since we want the relative order of the selection to be preserved, we first bring
    #to top the GF which is drawn first.
    def bringToTop(self, gfList):
        allGFs = self.getGFs()
        pairList = []
        for gf in allGFs:
            if gf in gfList:
                pairList.append((gf, self.bringToTopGF(gf)))
        if len(pairList) > 0:
            self.undoStack.append((self.undo_bringPush, [pairList]))

    #(see bringToTop) Here we need to reverse the list to push the GFs in the right order.
    def pushToBottom(self, gfList):
        allGFs = self.getGFs()
        allGFs.reverse()
        pairList = []
        for gf in allGFs:
            if gf in gfList:
                pairList.append((gf, self.pushToBottomGF(gf)))
        if len(pairList) > 0:
            self.undoStack.append((self.undo_bringPush, [pairList]))

    def compose(self, gfList):
        if len(gfList) > 1: # create a composite only if it's worth it
            allGFs = self.getGFs()
            sortedList = []
            for gf in allGFs:
                if gf in gfList:
                    sortedList.append(gf)
            indexList = []
            for gf in sortedList:
                indexList.append(self.removeGF(gf))
            composite = Graphics.Composite(sortedList, canvas=self.canvas, zoom=self.getZoom(), eventHandler=self.mainHandler)
            self.insertGF(indexList[len(indexList)-1], composite)
            self.undoStack.append((self.undo_compose, [composite, indexList]))
            return [composite]
        else:
            return gfList

    def decompose(self, gfList):
        compositeList = []
        for gf in gfList:
            componentList = self.compositionVisitor.decompose(gf)
            if len(componentList) > 0: #if gf was decomposed
                compositeList.append(gf) #add the composite to the list of composites
        self.undoStack.append((self.undo_decompose, [compositeList]))

    def delete(self, gfList):
        indexList = []
        for gf in gfList:
            gf.setCanvas(None)
            indexList.append(self.removeGF(gf))
        pairList = map(None, gfList, indexList)
        self.undoStack.append((self.undo_delete, [pairList]))

    def getBoundingBox(self, gfList):
        boxes = []
        for gf in gfList:
            if gf.getCanvas() != None:
                boxes.append(gf.getApproxBoundingBox())
        if len(boxes) == 0:
            raise TypeError, "gfList contains no active GF"
        xMin = boxes[0][0]
        yMin = boxes[0][1]
        xMax = boxes[0][2]
        yMax = boxes[0][3]
        for box in boxes:
            if box[0] < xMin:
                xMin = box[0]
            if box[1] < yMin:
                yMin = box[1]
            if box[2] > xMax:
                xMax = box[2]
            if box[3] > yMax:
                yMax = box[3]
        return [xMin, yMin, xMax, yMax]

    def setFillColor(self, gfList, color):
        undoList = self.colorVisitor.setFillColor(gfList, color)
        if len(undoList) > 0:
            self.undoStack.append((self.undo_setFillColor, [undoList]))

    def setOutlineColor(self, gfList, color):
        undoList = self.colorVisitor.setOutlineColor(gfList, color)
        if len(undoList) > 0:
            self.undoStack.append((self.undo_setOutlineColor, [undoList]))

    def setLineWidth(self, gfList, lineWidth):
        undoList = self.widthVisitor.setWidth(gfList, lineWidth)
        if len(undoList) > 0:
            self.undoStack.append((self.undo_setLineWidth, [undoList]))

    def setOutlineFillOption(self, gfList, option):
        undoList = self.optionVisitor.changeOption(gfList, option)
        if len(undoList) > 0:
            self.undoStack.append((self.undo_setOutlineFillOption, [undoList]))

    def createRectangle(self, xy):
        gf = Graphics.Rectangle(xy[0], xy[1], xy[2], xy[3], canvas=self.canvas, outline=self.getOutlineColor(), outlineOption=self.hasOutline(), fill=self.getFillColor(), fillOption=self.hasFill(), width=self.getLineWidth(), zoom=self.getZoom(), eventHandler=self.mainHandler)
        self.appendGF(gf)
        self.undoStack.append((self.undo_create, [[gf]]))
        return gf

    def createOval(self, xy):
        gf = Graphics.Oval(xy[0], xy[1], xy[2], xy[3], canvas=self.canvas, outline=self.getOutlineColor(), outlineOption=self.hasOutline(), fill=self.getFillColor(), fillOption=self.hasFill(), width=self.getLineWidth(), zoom=self.getZoom(), eventHandler=self.mainHandler)
        self.appendGF(gf)
        self.undoStack.append((self.undo_create, [[gf]]))
        return gf

    def createLine(self, xy, smooth=0):
        gf = Graphics.Line(xy, canvas=self.canvas, fill=self.getFillColor(), width=self.getLineWidth(), zoom=self.getZoom(), eventHandler=self.mainHandler, smooth = smooth)
        self.appendGF(gf)
        self.undoStack.append((self.undo_create, [[gf]]))
        return gf

    def createPolygon(self, xy, smooth=0):
        gf = Graphics.Polygon(xy, canvas=self.canvas, outline=self.getOutlineColor(), outlineOption=self.hasOutline(), fill=self.getFillColor(), fillOption=self.hasFill(), width=self.getLineWidth(), zoom=self.getZoom(), eventHandler=self.mainHandler, smooth = smooth)
        self.appendGF(gf)
        self.undoStack.append((self.undo_create, [[gf]]))
        return gf

    def createConnector(self, xy):
        gf = Graphics.Connector(xy[0], xy[1], canvas=self.canvas, zoom=self.getZoom(), eventHandler=self.mainHandler)
        self.appendGF(gf)
        self.undoStack.append((self.undo_create, [[gf]]))
        return gf

    def createImage(self, xy, filename):
        gf = Graphics.Image(xy[0], xy[1], filename, canvas=self.canvas, zoom=self.getZoom(), eventHandler=self.mainHandler)
        self.appendGF(gf)
        self.undoStack.append((self.undo_create, [[gf]]))
        return gf

    def createText(self, xy, text):
        gf = Graphics.Text(xy[0], xy[1], canvas=self.canvas, zoom=self.getZoom(), eventHandler=self.mainHandler, text=text, fill=self.getFillColor())
        self.appendGF(gf)
        self.undoStack.append((self.undo_create, [[gf]]))
        return gf
      
    def createNamedConnector(self, xy):
        gf = Graphics.NamedConnector(xy[0], xy[1], canvas=self.canvas, zoom=self.getZoom(), eventHandler=self.mainHandler)
        self.appendGF(gf)
        self.undoStack.append((self.undo_create, [[gf]]))
        return gf

    def createAttribute(self, xy, text ):
        gf = Graphics.Attribute(xy[0], xy[1], canvas=self.canvas, zoom=self.getZoom(), eventHandler=self.mainHandler, text=text )
        self.appendGF(gf)
        self.undoStack.append((self.undo_create, [[gf]]))
        return gf

    def isUndoStackEmpty(self):
        if len(self.undoStack) == 0:
            return 1
        else:
            return 0

    def isClipboardEmpty(self):
        if len(self.clipboardList) == 0:
            return 1
        else:
            return 0


    def translate(self, gfList, dx, dy):
        for gf in gfList:
            gf.translate(dx, dy)
        self.undoStack.append((self.undo_translate, [gfList, -dx,-dy]))

    def rotate(self, gfList, centerX, centerY, angle):
        for gf in gfList:
            gf.rotate(centerX, centerY, angle)
        self.undoStack.append((self.undo_rotate, [gfList, centerX, centerY, -angle]))

    def scale(self, gfList, centerX, centerY, factorX, factorY):
        for gf in gfList:
            gf.scale(centerX, centerY, factorX, factorY)
        self.undoStack.append((self.undo_scale, [gfList, centerX, centerY, 1/factorX, 1/factorY]))

# the following method is used by the translation handler to add an undo command.
# Instead of creating an undo for each small translation (by using the normal translate method of the editor),
# the handler calls the "add undo translation" method of the editor when the translation is complete.
    def addUndoTranslate(self, gfList, dx, dy):
        if( not (dx == 0 and dy == 0) ):
            self.undoStack.append((self.undo_translate, [gfList, -dx,-dy]))

# see addUndoTranslate
    def addUndoRotate(self, gfList, centerX, centerY, angle):
        self.undoStack.append((self.undo_rotate, [gfList, centerX, centerY, -angle]))

# see addUndoTranslate
    def addUndoScale(self, gfList, centerX, centerY, factorX, factorY):
        self.undoStack.append((self.undo_scale, [gfList, centerX, centerY, 1/factorX, 1/factorY]))

    def addUndoSetCoords(self, gf, oldCoords):
        self.undoStack.append((self.undo_setCoords, [gf, oldCoords]))

    def undo(self):
        method, args = self.undoStack.pop()
        apply(method, args)


#######################
# undo commands
    def undo_create(self, gfList):
        for gf in gfList:
            gf.setCanvas(None)
            self.removeGF(gf)


    def undo_delete(self, pairList):
        # pairList is a list of pairs, where each
        # pair contains an inactive GF and its position in the canvas.
        # pairList must be reversed because the index is valid
        # for the editor's list after the other gfs are deleted.
        pairList.reverse()
        for gf, index in pairList:
            gf.setCanvas(self.canvas)
            self.insertGF(index, gf)

    def undo_cut(self, previousClipboard, pairList):
        # pairList is a list of pairs, where each
        # pair contains an inactive GF and its position in the canvas.
        # pairList must be reversed because the index is valid
        # for the editor's list after the other gfs are deleted.
        pairList.reverse()
        for gf, index in pairList:
            gf.setCanvas(self.canvas)
            self.insertGF(index, gf)
        self.clipboardList = previousClipboard

    def undo_copy(self, previousClipboard):
        self.clipboardList = previousClipboard
       
    def undo_paste(self, pastedList):
        for gf in pastedList:
            gf.setCanvas(None)
            self.removeGF(gf)

    def undo_bringPush(self, pairList):
        pairList.reverse()
        for gf, index in pairList:
            self.removeGF(gf)
            self.insertGF(index, gf)

    def undo_compose(self, compositeGF, indexList):
        gfList = compositeGF.getComponents()
        self.removeGF(compositeGF)
        pairList = map(None, gfList, indexList)
        pairList.reverse()
        for gf, index in pairList:
            gf.setEventHandler(self.mainHandler)
            self.insertGF(index, gf)

    def undo_decompose(self, compositeList):
        for composite in compositeList:
            gfList = composite.getComponents()
            for gf in gfList:
                index = self.removeGF(gf)
                gf.setEventHandler(composite)
            self.insertGF(index, composite)

    def undo_translate(self, gfList, dx, dy):
        for gf in gfList:
            gf.translate(dx, dy)

    def undo_rotate(self, gfList, centerX, centerY, angle):
        for gf in gfList:
            gf.rotate(centerX, centerY, angle)

    def undo_scale(self, gfList, centerX, centerY, factorX, factorY):
        for gf in gfList:
            gf.scale(centerX, centerY, factorX, factorY)

    def undo_setCoords(self, gf, oldCoords):
        gf.setCoords(oldCoords)

    def undo_setFillColor(self, undoList):
        for gf, color in undoList:
            gf.setFillColor(color)

    def undo_setOutlineColor(self, undoList):
        for gf, color in undoList:
            gf.setOutlineColor(color)

    def undo_setLineWidth(self, undoList):
        for gf, width in undoList:
            gf.setWidth(width)

    def undo_setOutlineFillOption(self, undoList):
        for gf, (outlineOption, fillOption) in undoList:
            gf.setOutlineOption(outlineOption)
            gf.setFillOption(fillOption)

######################
    def appendGF(self, gf):
        self.GFs.append(gf)

    def insertGF(self, index, gf):
        self.GFs.insert(index, gf)
        for gf in self.GFs:
            gf.bringToTop()

    def getIndex(self, gf):
        return self.GFs.index(gf)

    def removeGF(self, gf):
        index = self.GFs.index(gf)
        self.GFs.remove(gf)
        return index #return the index the gf had in the list (which was also its relative position on the canvas)

    # convention: the first gfs in the list are drawn first.
    # The order in which the GFs are drawn is useful when we want to save.
    def bringToTopGF(self, gf):
        gf.bringToTop()
        index = self.removeGF(gf)
        self.GFs.append(gf)
        return index

    def pushToBottomGF(self, gf):
        gf.pushToBottom()
        index = self.removeGF(gf)
        self.GFs.insert(0, gf)
        return index


    def getGFs(self):
        return self.GFs[:]
      
    def setGFs(self, gfList ):
        self.GFs = gfList

    def getEventHandler(self):
        return self.mainHandler

    def getCanvasWidth(self):
        return self.workspace.getCanvasWidth()

    def getCanvasHeight(self):
        return self.workspace.getCanvasHeight()

    def getCanvas(self):
        return self.workspace.getCanvas()

    def getZoom(self):
        return self.workspace.getZoom()

    def setZoom(self, zoom, x, y):
        self.workspace.setZoom(zoom, x, y)
        # update statusBar and GFs to the new zoom (whether it changed or not)
        newZoom = self.workspace.getZoom()
        self.statusBar.setZoom(newZoom)
        for gf in self.GFs:
            gf.setZoom(newZoom)
    
    def setToolSelector(self, tool):
        self.toolSelector.set(tool)

    def getLineWidth(self):
        return self.lineWidthSelector.get()

    def getOutlineColor(self):
        return self.colorSelector.getOutlineColor()

    def getFillColor(self):
        return self.colorSelector.getFillColor()

    def hasOutline(self):
        option = self.outlineFillOptionSelector.get()
        return option[0]

    def hasFill(self):
        option = self.outlineFillOptionSelector.get()
        return option[1]


  