import AbstractHandler as EventHandler 
import InsertHandlers
import EditHandlers
import TransformHandlers
import GFVisitors
import pickle

import SnapGrid
from ATOM3TypeDialog	import *
from ATOM3List	        import *
from ATOM3Constraint	import *
from ATOM3Text import ATOM3Text

class MainHandler(EventHandler.EventHandler):
    def __init__(self, editor):
        self.editor = editor

    def start(self):
        #usual selection handler
        self.selectHandler = TransformHandlers.SelectHandler(self.editor, self)
        #insertion handlers
        self.rectangleInsertHandler = InsertHandlers.RectangleInsertHandler(self.editor, self)
        self.ovalInsertHandler = InsertHandlers.OvalInsertHandler(self.editor, self)
        self.lineInsertHandler = InsertHandlers.LineInsertHandler(self.editor, self)
        self.polylineInsertHandler = InsertHandlers.PolylineInsertHandler(self.editor, self)
        self.polygonInsertHandler = InsertHandlers.PolygonInsertHandler(self.editor, self)
        self.textInsertHandler = InsertHandlers.TextInsertHandler(self.editor, self)
        self.imageInsertHandler = InsertHandlers.ImageInsertHandler(self.editor, self)
        self.connectorInsertHandler = InsertHandlers.ConnectorInsertHandler(self.editor, self)
        self.attributeInsertHandler = InsertHandlers.AttributeInsertHandler(self.editor, self)
        self.namedConnectorInsertHandler = InsertHandlers.NamedConnectorInsertHandler(self.editor, self)
        
        #edition handlers
        self.textEditHandler = EditHandlers.TextEditHandler(self.editor, self)
        self.imageEditHandler = EditHandlers.ImageEditHandler(self.editor, self)
        self.polygonEditHandler = EditHandlers.PolygonEditHandler(self.editor, self)
        self.lineEditHandler = EditHandlers.LineEditHandler(self.editor, self)
        self.namedPortEditHandler = EditHandlers.NamedPortEditHandler(self.editor, self)
        self.attributeEditHandler = EditHandlers.AttributeEditHandler(self.editor, self)
        
        
        #zoom handler
        self.zoomHandler = TransformHandlers.ZoomHandler(self.editor, self)
        #visitors
        self.editHandlerVisitor = GFVisitors.EditHandlerVisitor(self)
        # set current tool mode
        self.currentMode = "select"
        #set the current handler to the normal one.
        self.currentHandler = self.selectHandler
        self.currentHandler.start([])
    
# Most events are directly forwarded to the current handler.
# However, some event (e.g. tool selection) are treated by the
# main handler. The main handler has the power to stop
# the current handler and start another of its handlers.

### GF events
    def onGFEnter(self, gf):
        self.currentHandler.onGFEnter(gf)

    def onGFLeave(self, gf):
        self.currentHandler.onGFLeave(gf)

    def onGFButton(self, gf, event):
        self.currentHandler.onGFButton(gf, event)

    def onGFShiftButton(self, gf, event):
        self.currentHandler.onGFShiftButton(gf, event)

    def onGFDoubleButton(self, gf, event):
        """ on double button 1: if in select, go to edit mode (if there is an edit mode)"""
        if event.num == 1 and self.currentMode == "select":
            gfList = self.currentHandler.stop() # stop current handler
            if len(gfList) == 1: # if only one GF selected
                #look for an edit handler
                editHandler = self.editHandlerVisitor.getEditHandler(gfList[0])
                if editHandler != None:
                    self.currentHandler = editHandler
                    self.currentMode = "edit"
                    self.currentHandler.start(gfList[0])
                    return
            #if none, go back to select mode
            self.currentHandler.start(gfList)
            self.currentHandler.onGFDoubleButton(gf, event)
        else:
            self.currentHandler.onGFDoubleButton(gf, event)


    def onGFShiftDoubleButton(self, gf, event):
        self.currentHandler.onGFShiftDoubleButton(gf, event)

    def onGFButtonMotion(self, gf, event):
        self.currentHandler.onGFButtonMotion(gf, event)

    def onGFButtonRelease(self, gf, event):
        self.currentHandler.onGFButtonRelease(gf, event)

### canvas events
    def onCanvasButton(self, event):
        self.currentHandler.onCanvasButton(event)

    def onCanvasDoubleButton(self, event):
        self.currentHandler.onCanvasDoubleButton(event)

    def convertEvent( self, event ):
        z=self.editor.getZoom()
        return ( event.x / z  , event.y / z )

    def onCanvasMotion(self, event):
        self.editor.statusBar.setXY( * self.convertEvent(event) )
        self.currentHandler.onCanvasMotion(event)

    def onCanvasShiftMotion(self, event):
        self.editor.statusBar.setXY( * self.convertEvent(event) )
        self.currentHandler.onCanvasShiftMotion(event)

    def onCanvasButtonMotion(self, event):
        self.editor.statusBar.setXY( * self.convertEvent(event) )
        self.currentHandler.onCanvasButtonMotion(event)

    def onCanvasShiftButtonMotion(self, event):
        self.editor.statusBar.setXY( * self.convertEvent(event) )
        self.currentHandler.onCanvasShiftButtonMotion(event)
 
    def onCanvasButtonRelease(self, event):
        self.currentHandler.onCanvasButtonRelease(event)

### color events
    def onFillColor(self, color):
        self.currentHandler.onFillColor(color)


    def onOutlineColor(self, color):
        self.currentHandler.onOutlineColor(color)

### tool selection events
    def onToolSelection(self, toolName):
        """on tool selection: stop the current handler and start the appropriate handler"""
        self.currentHandler.stop()
        #update current handler
        if toolName == "select":
            self.currentHandler = self.selectHandler
            self.currentMode = "select"
            self.currentHandler.start([])
            return
        elif toolName == "zoom":
            self.currentHandler = self.zoomHandler
            self.currentMode = "zoom"
            self.currentHandler.start()
        elif toolName == "rectangle":
            self.currentHandler = self.rectangleInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start()
        elif toolName == "oval":
            self.currentHandler = self.ovalInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start()
        elif toolName == "line":
            self.currentHandler = self.lineInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start()
        elif toolName == "text":
            self.currentHandler = self.textInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start()
        elif toolName == "polyline":
            self.currentHandler = self.polylineInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start()
        elif toolName == "smoothpolyline":
            self.currentHandler = self.polylineInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start(smooth = 1)
        elif toolName == "polygon":
            self.currentHandler = self.polygonInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start()
        elif toolName == "smoothpolygon":
            self.currentHandler = self.polygonInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start(smooth = 1)
        elif toolName == "image":
            self.currentHandler = self.imageInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start()
        elif toolName == "connector":
            self.currentHandler = self.connectorInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start()
        elif toolName == "attribute":
            self.currentHandler = self.attributeInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start()
        elif toolName == "namedPort":
            self.currentHandler = self.namedConnectorInsertHandler
            self.currentMode = "insert"
            self.currentHandler.start()
            
          
### outline/fill option event
    def onOutlineFillOption(self, option):
        self.currentHandler.onOutlineFillOption(option)

### line width event
    def onLineWidth(self, lineWidth):
        self.currentHandler.onLineWidth(lineWidth)

### keyboard events
    def onKey(self, event):
        self.currentHandler.onKey(event)

    def onShiftKey(self, event):
        self.currentHandler.onShiftKey(event)

    def onControlKey(self, event):
        if event.keysym == 's': 
            self.onSave()
        else:
            self.currentHandler.onControlKey(event)


### file events
    def onSave(self):# save operation is always the same, no matter what
        self.editor.save()# the current handler is. It is handled in the main handler.

    def onExport(self):
        self.editor.export()

    def onExit(self):
        self.editor.exit()
        
    def onSnapSetting( self ):
        SnapGrid.applyLayout( self.editor, settingsMode = True )
        
    def onIconPositioner( self ):
        self.editor.iconPositioner.createDialog()
        
### model events

    def onConstraintHelp( self ):     
        try:
          from FilePaths import HELP_PATH
          path = os.path.join( HELP_PATH, 'iconEditorScripting.txt' )
          f = open( path, 'r' )
          text = f.read()
          f.close()
          text += '\n\n#------------------------------------------------------'
          text += '-----------------------'
          text += '\nHelp document loaded from:\n    ' + path
          text += '\n\nHelp document loaded by:\n    ' + __file__
        except:
          text = 'Help document not found:\n    ' + path
          text += '\n\nHelp document loaed by:\n    ' + __file__
        ATOM3TypeDialog( self.editor.root , ATOM3Text( text ) )
          
    def onSetConstraints( self ):
        
        # Python List
        constraintList = self.editor.scripting.getConstraintList()
                
        # Convert it to a ATOM3 LIST of Constraints
        tempList = [] 
        for value in constraintList:
          c = ATOM3Constraint()
          c.setValue(value )
          tempList.append( c )
       
        atom3ConstraintList = ATOM3List([1,1,1,0],ATOM3Constraint,[])
        atom3ConstraintList.setValue( tempList )

        # Dialog for user editing of constraints
        ATOM3TypeDialog(self.editor.root, atom3ConstraintList )
        
        # For each and every constraint
        constraintList = []
        for obj in atom3ConstraintList.getValue():                                       
           cvalue = obj.getValue()
           constraintList.append( cvalue )

        # Save the constraints as a normal python list again...
        self.editor.scripting.setConstraintList( constraintList )
           
    def onRunTimeChange( self, modelMenu ):
        if( self.editor.scripting.getRunTimeChange() ): 
          modelMenu.entryconfigure( 0, label = "Changes at run-time DISABLED" )
          self.editor.scripting.setRunTimeChange( False )       
        else:  
          modelMenu.entryconfigure( 0, label = "Changes at run-time ENABLED" )
          self.editor.scripting.setRunTimeChange( True )                          

### edit events
    def onEditMenu(self, editMenu):
        self.currentHandler.onEditMenu(editMenu)

    def onUndo(self):
        self.currentHandler.onUndo()

    def onCut(self):
        self.currentHandler.onCut()

    def onCopy(self):
        self.currentHandler.onCopy()

    def onPaste(self):
        self.currentHandler.onPaste()

    def onDelete(self):
        self.currentHandler.onDelete()

    def onBringToTop(self):
        self.currentHandler.onBringToTop()

    def onPushToBottom(self):
        self.currentHandler.onPushToBottom()

    def onGroup(self):
        self.currentHandler.onGroup()

    def onUngroup(self):
        self.currentHandler.onUngroup()
        
    def onProperties(self):
        self.currentHandler.onProperties()


### "sub-handler" events
 ### insert handlers events
    # called by an insertion handler that stops by itself because insertion is finished
    def onInsertHandlerStopped(self, gf):
        if( gf != None):
            editHandler = self.editHandlerVisitor.getEditHandler(gf)
            if editHandler != None:
                self.currentHandler = editHandler
                self.currentMode = "edit"
                self.currentHandler.start(gf, showProperties = False)
                return
        self.toSelect([])

    #edit handler events
    def onEditHandlerStopped(self, gfList):
        self.toSelect([])

    def onZoomHandlerStopped(self):
        self.toSelect([])

    #methods used by the visitors to get the right handlers
    def getPolygonEditHandler(self):
        return self.polygonEditHandler

    def getLineEditHandler(self):
        return self.lineEditHandler

    def getTextEditHandler(self):
        return self.textEditHandler

    def getImageEditHandler(self):
        return self.imageEditHandler
      
    def getNamedConnectorEditHandler(self):
        return self.namedPortEditHandler
      
    def getAttributeEditHandler(self):
        return self.attributeEditHandler

    #private method toSelect. 
    def toSelect(self, gfList):
        """go to select mode"""
        self.editor.setToolSelector("select")
        self.currentHandler = self.selectHandler
        self.currentMode = "select"
        self.currentHandler.start(gfList)
