import Graphics
import Tkinter
import Handles
import AbstractHandler as EventHandler 
import GFVisitors
import os

from Utilities import snapIt
from FilePaths import GRAPHIC_EDITOR_DATA

#zoom handler class
class ZoomHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        # the event handler must implement onZoomHandlerStopped
        self.eventHandler = eventHandler

#canvas events
    def onCanvasButton(self, event):
        """Canvas button event:
        button 1: multiply zoom by 2
        button 3: divide zoom by 2
        button 2: quit zoom"""
        zoom = self.editor.getZoom()
        if event.num == 1 and zoom < 16.0:
            zoom = zoom * 2
            self.editor.setZoom(zoom, event.x, event.y)
        elif event.num == 3 and zoom > .25:
            zoom = zoom / 2
            self.editor.setZoom(zoom, event.x, event.y)
        elif event.num == 2:
            self.eventHandler.onZoomHandlerStopped()

    def onCanvasDoubleButton(self, event):
        self.onCanvasButton(event)

#
#
#  USUAL TRANSFORMATION HANDLER
#
class SelectHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = self.editor.getCanvas()
        self.eventHandler = eventHandler
        self.handleSet = Handles.HandleSet(200, 100, 20, 20, 0, self.canvas, self)
        self.gfList = [] # list of selected GFs
        self.translationHandler = TranslationHandler(self.editor, self)
        self.rotationHandler = RotationHandler(self.editor, self)
        self.scalingHandler = ScalingHandler(self.editor, self)
        self.boxHandler = BoxHandler(self.editor, self)
        self.shiftHandler = ShiftHandler(self.editor, self)
        self.compositionVisitor = GFVisitors.CompositionVisitor(self.editor)

    def start(self, gfList):
        """start the handler with or without selected GFs"""
        self.currentHandler = None
        self.zoom = self.editor.getZoom()
        self.gfList = gfList
        self.select()
        self.gfMenuOn = 0


    def stop(self):
        """stop the handler and return the GF that was selected, if any"""
        self.deselect()
        self.editor.statusBar.setGF("")
        return self.gfList
    

# Internal handleset events
    def onHandleSetButton(self, handleSet, handleName, event):
        """if no current handler, start scaling handler"""
        if self.currentHandler != None:
            self.currentHandler.onHandleSetButton(handleSet, handleName, event)
        elif event.num == 1:
            self.currentHandler = self.scalingHandler
            self.currentHandler.start(self.gfList, self.handleSet, event)

    def onHandleSetButtonMotion(self, handleSet, handleName, event):
        if self.currentHandler != None:
            self.currentHandler.onHandleSetButtonMotion(handleSet, handleName, event)


    def onHandleSetShiftButtonMotion(self, handleSet, handleName, event):
        if self.currentHandler != None:
            self.currentHandler.onHandleSetShiftButtonMotion(handleSet, handleName, event)


    def onHandleSetButtonRelease(self, handleSet, handleName, event):
        if self.currentHandler != None:
            self.currentHandler.onHandleSetButtonRelease(handleSet, handleName, event)

    # GF events
    def onGFEnter(self, gf):
        """update status bar (GF's name)"""
        self.editor.statusBar.setGF("gf" + str(gf.getObjectNumber()))

    def onGFLeave(self, gf):
        """update status bar (empty string)"""
        self.editor.statusBar.setGF("")

    def onGFButton(self, gf, event):
        """if no current handler:
        button 1: start translation handler
        button 2: start rotation handler
        button 3: launch popup menu"""
        if self.currentHandler != None:
            self.currentHandler.onGFButton(gf, event)
        elif event.num == 1:
            self.deselect()
            self.currentHandler = self.translationHandler
            if not (gf in self.gfList):
                self.gfList = [gf]
            self.currentHandler.start(self.gfList, event)
        elif event.num == 2:
            self.deselect()
            self.currentHandler = self.rotationHandler
            if not (gf in self.gfList):
                self.gfList = [gf]
            self.currentHandler.start(self.gfList, event)
        elif event.num == 3:
            if gf not in self.gfList:
                self.gfList = [gf]
                self.select()
            self.launchPopup(event)
            self.gfMenuOn = 1

    def onGFShiftButton(self, gf, event):
        """if no current handler:
        button 1: start shift handler (add to selection)"""
        if self.currentHandler != None:
            self.currentHandler.onGFShiftButton(gf, event)
        elif event.num == 1:
            self.deselect()
            self.currentHandler = self.shiftHandler
            self.currentHandler.start(gf, self.gfList, event)

    def onGFShiftDoubleButton(self, gf, event):
        self.onGFShiftButton(gf, event)

    def onGFDoubleButton(self, gf, event):
        if gf != None: #Tkinter sends a double button event even
            # when the item is deleted after the first click.
            self.onGFButton(gf, event)


    def onGFButtonMotion(self, gf, event):
        if self.currentHandler != None:
            self.currentHandler.onGFButtonMotion(gf, event)


    def onGFButtonRelease(self, gf, event):
        if self.currentHandler != None:
            self.currentHandler.onGFButtonRelease(gf, event)


#canvas events
    def onCanvasButton(self, event):
        if self.currentHandler != None:
            self.currentHandler.onCanvasButton(event)
        elif event.num == 1:
            self.deselect()
            self.currentHandler = self.boxHandler
            self.currentHandler.start(event)
        elif event.num == 3:
            if self.gfMenuOn == 0: 
                self.gfList = []
                self.deselect()
                self.launchPopup(event)
            else:
                self.gfMenuOn = 0

    def onCanvasDoubleButton(self, event):
        self.onCanvasButton(event)

    def onCanvasButtonMotion(self, event):
        if self.currentHandler != None:
            self.currentHandler.onCanvasButtonMotion(event)
    
    def onCanvasButtonRelease(self, event):
        if self.currentHandler != None:
            self.currentHandler.onCanvasButtonRelease(event)

    #Keyboard events
    def onKey(self, event):
        if self.currentHandler == None:
            if event.keysym == "Delete":
                self.onDelete()
        
        # Quick translation events, per pixel baby, yah!
        if( event.keysym == "Up"):
          for g in self.gfList:
              g.translate(0, -1 / self.editor.getZoom() )
        elif( event.keysym == "Down"):
          for g in self.gfList:
              g.translate(0,  1 / self.editor.getZoom() )
        elif( event.keysym == "Right"):
          for g in self.gfList:
              g.translate(1 / self.editor.getZoom() , 0)
        elif( event.keysym == "Left"):
          for g in self.gfList:
              g.translate(-1 / self.editor.getZoom() , 0)
        

    def onControlKey(self, event):
        if self.currentHandler == None:
            if event.keysym == "z": # undo
                if not self.editor.isUndoStackEmpty():
                    self.onUndo()
            elif event.keysym == "x": # cut selection
                self.onCut()
            elif event.keysym == "c": # copy selection
                self.onCopy()
            elif event.keysym == "v": # paste
                if not self.editor.isClipboardEmpty():
                    self.onPaste()
            elif event.keysym == "t": # bring to top
                if len(self.gfList) > 0:
                    self.onBringToTop()
            elif event.keysym == "b": # push to bottom
                if len(self.gfList) > 0:
                    self.onPushToBottom()
            elif event.keysym == "g": # group
                if  len(self.gfList) > 1:
                    self.onGroup()
            elif event.keysym == "f": # ungroup
                if  self.hasComposites():
                    self.onUngroup()
                
#color events
    def onFillColor(self, color):
        self.editor.setFillColor(self.gfList, color)


    def onOutlineColor(self, color):
        self.editor.setOutlineColor(self.gfList, color)

    # line width event
    def onLineWidth(self, lineWidth):
        self.editor.setLineWidth(self.gfList, lineWidth)
        self.select() #update selection in case the bounding box changes


#outline-fill option event
    def onOutlineFillOption(self, option):
        self.editor.setOutlineFillOption(self.gfList, option)
        self.select()

    # a list of gfs
    def select(self):
        if len(self.gfList) > 0:
            bBox = self.editor.getBoundingBox(self.gfList)
            self.handleSet.activate()
            apply(self.handleSet.set, bBox)
        else:
            self.deselect()

    # deselect a list of gfs
    def deselect(self):
        self.handleSet.deactivate()


#edit events
    def onEditMenu(self, editMenu):
        if not self.editor.isUndoStackEmpty():
            editMenu.entryconfigure(0, state=Tkinter.NORMAL) #undo
        if len(self.gfList) > 0:
            editMenu.entryconfigure(2, state=Tkinter.NORMAL) #cut
            editMenu.entryconfigure(3, state=Tkinter.NORMAL) #copy
        if not self.editor.isClipboardEmpty():
            editMenu.entryconfigure(4, state=Tkinter.NORMAL) #paste
        if len(self.gfList) > 0:
            editMenu.entryconfigure(5, state=Tkinter.NORMAL) #delete
            editMenu.entryconfigure(7, state=Tkinter.NORMAL) #to top
            editMenu.entryconfigure(8, state=Tkinter.NORMAL) #to bottom
        if len(self.gfList) > 1:
            editMenu.entryconfigure(10, state=Tkinter.NORMAL) #group
        if  self.hasComposites():
            editMenu.entryconfigure(11, state=Tkinter.NORMAL) #ungroup
        if len(self.gfList) > 0:
            editMenu.entryconfigure(13, state=Tkinter.NORMAL) #Rotate
            editMenu.entryconfigure(14, state=Tkinter.NORMAL) #Up
            editMenu.entryconfigure(15, state=Tkinter.NORMAL) #Down
            editMenu.entryconfigure(16, state=Tkinter.NORMAL) #Right
            editMenu.entryconfigure(17, state=Tkinter.NORMAL) #Left
        if len(self.gfList) == 1:
            editMenu.entryconfigure(19, state=Tkinter.NORMAL) #properties


    def onUndo(self):
        self.deselect()
        self.gfList = []
        self.editor.undo()

    def onCut(self):
        self.deselect()
        self.editor.cut(self.gfList)
        self.gfList = []
        
    def onCopy(self):
        self.editor.copy(self.gfList)

    def onPaste(self):
        self.deselect()
        self.gfList = self.editor.paste()
        self.select()

    def onBringToTop(self):
        self.deselect()
        self.editor.bringToTop(self.gfList)
        self.select()

    def onPushToBottom(self):
        self.editor.pushToBottom(self.gfList)

    def onGroup(self):
        self.deselect()
        self.gfList = self.editor.compose(self.gfList)
        self.select()

    def onUngroup(self):
        self.editor.decompose(self.gfList)
        self.gfList = []
        self.deselect()

    def onDelete(self):
        self.editor.delete(self.gfList)
        self.gfList = []
        self.deselect()

    def onProperties(self):
        pass

    def hasComposites(self):
        for gf in self.gfList:
            if self.compositionVisitor.isComposite(gf):
                return 1
        return 0


    def launchPopup(self, event):
        self.popup = Tkinter.Menu(self.canvas, tearoff=0)
        if not self.editor.isUndoStackEmpty():
            self.popup.add_command(label="Undo", accelerator="Ctrl+Z", command=self.onUndo, state=Tkinter.NORMAL)
        else:
            self.popup.add_command(label="Undo", accelerator="Ctrl+Z", command=self.onUndo, state=Tkinter.DISABLED)
        self.popup.add_separator()
        if len(self.gfList) > 0:
            self.popup.add_command(label="Cut", accelerator="Ctrl+X", command=self.onCut, state=Tkinter.NORMAL)
            self.popup.add_command(label="Copy", accelerator="Ctrl+C", command=self.onCopy, state=Tkinter.NORMAL)
        else:
            self.popup.add_command(label="Cut", accelerator="Ctrl+X", command=self.onCut, state=Tkinter.DISABLED)
            self.popup.add_command(label="Copy", accelerator="Ctrl+C", command=self.onCopy, state=Tkinter.DISABLED)
        if not self.editor.isClipboardEmpty():
            self.popup.add_command(label="Paste", accelerator="Ctrl+V", command=self.onPaste, state=Tkinter.NORMAL)
        else:
            self.popup.add_command(label="Paste", accelerator="Ctrl+V", command=self.onPaste, state=Tkinter.DISABLED)
        if len(self.gfList) > 0:
            self.popup.add_command(label="Delete", accelerator="Delete", command=self.onDelete, state=Tkinter.NORMAL)
        else:
            self.popup.add_command(label="Delete", accelerator="Delete", command=self.onDelete, state=Tkinter.DISABLED)
        self.popup.add_separator()
        if len(self.gfList) > 0:
            self.popup.add_command(label="to Top", accelerator="Ctrl+T", command=self.onBringToTop, state=Tkinter.NORMAL)
            self.popup.add_command(label="to Bottom", accelerator="Ctrl+B", command=self.onPushToBottom, state=Tkinter.NORMAL)
        else:
            self.popup.add_command(label="to Top", accelerator="Ctrl+T", command=self.onBringToTop, state=Tkinter.DISABLED)
            self.popup.add_command(label="to Bottom", accelerator="Ctrl+B", command=self.onPushToBottom, state=Tkinter.DISABLED)
        self.popup.add_separator()
        if  len(self.gfList) > 1:
            self.popup.add_command(label="Group", accelerator="Ctrl+G", command=self.onGroup, state=Tkinter.NORMAL)
        else:
            self.popup.add_command(label="Group", accelerator="Ctrl+G", command=self.onGroup, state=Tkinter.DISABLED)
        if  self.hasComposites():
            self.popup.add_command(label="Ungroup", accelerator="Ctrl+F", command=self.onUngroup, state=Tkinter.NORMAL)
        else:
            self.popup.add_command(label="Ungroup", accelerator="Ctrl+F", command=self.onUngroup, state=Tkinter.DISABLED)
        self.popup.tk_popup(event.x_root, event.y_root)


# sub-handler events
    def onTranslationHandlerStopped(self, dxdy):
        self.currentHandler = None
        self.select()
        
    def onRotationHandlerStopped(self):
        self.currentHandler = None
        self.select()

    def onScalingHandlerStopped(self):
        self.currentHandler = None
        self.select()
        
    def onBoxHandlerStopped(self, gfList):
        self.currentHandler = None
        self.gfList = gfList
        self.select()

    def onShiftHandlerStopped(self):
        self.currentHandler = None
        self.select()

    
#assumes that "start" is called on a "onGFButton 1" event (button 1 is still down) and takes this event as argument.
#Also, it assumes that the gf of the onGFButton event is one of the GFs in the list when the start method is called.
#This is reasonable since the handler executes only one translation and calls "onTranslationHandlerStopped"
#when button 1 is released.
class TranslationHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = self.editor.getCanvas()
        # the event handler must implement onTranslationHandlerStopped
        self.eventHandler = eventHandler


    # start the handler
    def start(self, gfList, event):
        """start the handler"""
        self.gfList = gfList #selected GFs
        self.totalTranslationX = 0
        self.totalTranslationY = 0
        self.zoom = self.editor.getZoom()
        self.previousX = event.x / self.zoom
        self.previousY = event.y / self.zoom        

    def onGFButtonMotion(self, gf, event):
        """translate the selected GFs and keep track of the total translation since the handler started"""
   
        # Using the snap grid
        if( self.editor.snapGridInfoTuple and len( self.gfList ) > 0 ):
          gridSize = self.editor.snapGridInfoTuple[0] / self.zoom
          x0 = self.previousX
          y0 = self.previousY
          ex = event.x / self.zoom
          ey = event.y / self.zoom
          
          # Snapping to the top left corner of the first object encountered
          x,y = self.gfList[0].getCoords()[:2] 
          x1 = snapIt( x + ex - x0, ex, gridSize)
          y1 = snapIt( y + ey - y0, ey, gridSize)     
          self.previousX = x1
          self.previousY = y1        
          dx = x1 - x0
          dy = y1 - y0 
          self.totalTranslationX += dx
          self.totalTranslationY += dy
          
          for g in self.gfList:
              g.translate(dx, dy)
          
              
        # No snap grid
        else:          
          ex = event.x / self.zoom 
          ey = event.y / self.zoom 
          dx = ex - self.previousX
          dy = ey - self.previousY
          for g in self.gfList:
              g.translate(dx, dy)
          self.totalTranslationX += dx
          self.totalTranslationY += dy
          self.previousX = ex
          self.previousY = ey
          

    def onGFButtonRelease(self, gf, event):
        """stop on button 1 release. translate back to initial position if the mouse cursor is outside the canvas."""
        if event.num == 1:
            if (event.x >= self.editor.getCanvasWidth()) or (event.x <= 0) or (event.y >= self.editor.getCanvasHeight()) or (event.y <= 0):
                for g in self.gfList:
                    g.translate(-self.totalTranslationX, -self.totalTranslationY)
                    self.eventHandler.onTranslationHandlerStopped((0, 0))
            else:
                self.editor.addUndoTranslate(self.gfList, self.totalTranslationX, self.totalTranslationY)
                self.eventHandler.onTranslationHandlerStopped((self.totalTranslationX, self.totalTranslationY))

#assumes that "start" is called on a "onGFButton 2" event (button 2 is still down) and takes this event as argument.
class RotationHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        # the event handler must implement onRotationHandlerStopped()
        self.eventHandler = eventHandler

    # start the handler
    def start(self, gfList, event):
        """start the handler"""
        self.gfList = gfList
        zoom = self.editor.getZoom()
        box = self.editor.getBoundingBox(gfList)
        self.centerX = (box[0] + box[2])/(zoom * 2)
        self.centerY = (box[1] + box[3])/(zoom * 2)
        self.angle = 90
        for gf in gfList:
            gf.rotate(self.centerX, self.centerY, self.angle)

    def onCanvasButtonRelease(self, event):
        """stop on button 2 release"""
        if event.num == 2:
            self.stopHandler()
      
    def stopHandler( self ):
        """ Stop the handler """
        self.editor.addUndoRotate(self.gfList, self.centerX, self.centerY, self.angle)
        self.eventHandler.onRotationHandlerStopped()


#assumes that "start" is called on a "onHandleSetButton 1" event (button 1 is still down) and takes this event as argument.
class ScalingHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        # the event handler must implement onScalingHandlerStopped()
        self.eventHandler = eventHandler


    def start(self, gfList, handleSet, event):
        """start the handler"""
        self.zoom = self.editor.getZoom()
        self.composite = Graphics.Composite(gfList, canvas=self.editor.getCanvas(), zoom=self.zoom, eventHandler=self)
        self.handleSet = handleSet
        self.previousX = event.x
        self.previousY = event.y
        self.relX = 0
        self.relY = 0
        self.reverseX = 0
        self.reverseY = 0
        self.totalScaleFactorX = 1.
        self.totalScaleFactorY = 1.
        
     
    def onHandleSetButton(self, handleSet, handleName, event):
        pass

    def onHandleSetButtonMotion(self, handleSet, handleName, event):
        """ 
        Scale the selected GFs
        The scaling center and scaling factors depend on the handle that is 
        grabbed, resulting in 8 different cases, and thus a lengthy method
        """ 
        
        self.relX += event.x - self.previousX
        self.relY += event.y - self.previousY
        self.previousX = event.x
        self.previousY = event.y
        self.cBox = self.composite.getCoreBox()
        width = self.cBox[2] - self.cBox[0]
        if self.reverseX == 1:
            width = -width
        height = self.cBox[3] - self.cBox[1]
        if self.reverseY == 1:
            height = -height
        if width == 0 and handleName !=  "x01y0" and handleName != "x01y1":
            return
        if height == 0 and handleName != "x0y01" and handleName != "x1y01":
            return
        print self.cBox
        # names of the handles:
        #         x0y0......x01y0.......x1y0
        #          .                     .
        #          .                     .
        #         x0y01                 x1y01
        #          .                     .
        #          .                     .
        #         x0y1......x01y1.......x1y1
        #
        # define the meaning of moving each handle
        if handleName == "x01y0": #north
            centerX = 0.
            if not self.reverseY:
                centerY = self.cBox[3]
            else:
                centerY = self.cBox[1]
            scaleFactorX = 1.
            scaleFactorY = float(height - self.relY)/height
        elif handleName == "x01y1": #south
            centerX = 0.
            if not self.reverseY:
                centerY = self.cBox[1]
            else:
                centerY = self.cBox[3]
            scaleFactorX = 1.
            scaleFactorY = float(height + self.relY)/height
        elif handleName == "x0y01": #west
            if not self.reverseX:
                centerX = self.cBox[2]
            else:
                centerX = self.cBox[0]
            centerY = 0.
            scaleFactorX = float(width - self.relX)/width
            scaleFactorY = 1.
        elif handleName == "x1y01": #east
            if not self.reverseX:
                centerX = self.cBox[0]
            else:
                centerX = self.cBox[2]
            centerY = 0.
            scaleFactorX = float(width + self.relX)/width
            scaleFactorY = 1.
        elif handleName == "x0y0": #northwest
            if not self.reverseX:
                centerX = self.cBox[2]
            else:
                centerX = self.cBox[0]
            if not self.reverseY:
                centerY = self.cBox[3]
            else:
                centerY = self.cBox[1]
            scaleFactorX = float(width - self.relX)/width
            scaleFactorY = float(height - self.relY)/height
        elif handleName == "x1y0": #southwest
            if not self.reverseX:
                centerX = self.cBox[0]
            else:
                centerX = self.cBox[2]
            if not self.reverseY:
                centerY = self.cBox[3]
            else:
                centerY = self.cBox[1]
            scaleFactorX = float(width + self.relX)/width
            scaleFactorY = float(height - self.relY)/height
        elif handleName == "x0y1": #northeast
            if not self.reverseX:
                centerX = self.cBox[2]
            else:
                centerX = self.cBox[0]
            if not self.reverseY:
                centerY = self.cBox[1]
            else:
                centerY = self.cBox[3]
            scaleFactorX = float(width - self.relX)/width
            scaleFactorY = float(height + self.relY)/height
        elif handleName == "x1y1": #southeast
            if not self.reverseX:
                centerX = self.cBox[0]
            else:
                centerX = self.cBox[2]
            if not self.reverseY:
                centerY = self.cBox[1]
            else:
                centerY = self.cBox[3]
            scaleFactorX = float(width + self.relX)/width
            scaleFactorY = float(height + self.relY)/height
            
        # Prevent scaling to (near) zero in width and height
        # The two middle (top/bottom) handles can't affect width, so ignore  
        if( (handleName != "x01y0") and (handleName != "x01y1") ):
            if abs(width*scaleFactorX) < 1: 
                return
        # The two middle (left/right) handles can't affect height, so ignore
        if( (handleName != "x0y01") or (handleName != "x1y01") ):
            if abs(height*scaleFactorY) < 1:
                return
  
        self.totalScaleFactorX *= scaleFactorX
        self.totalScaleFactorY *= scaleFactorY
        self.centerX = centerX/self.zoom
        self.centerY = centerY/self.zoom
  
        self.composite.scale(self.centerX, self.centerY, scaleFactorX, scaleFactorY)
        self.bBoxSelectedGF = self.composite.getApproxBoundingBox()
        apply(self.handleSet.set, self.bBoxSelectedGF)  #adjust to the new bounding box
        if scaleFactorX < 0:
            self.reverseX = not self.reverseX
        if scaleFactorY < 0:
            self.reverseY = not self.reverseY
        self.relX = 0
        self.relY = 0



    def onHandleSetShiftButtonMotion(self, handleSet, handleName, event):
        """scale while keeping the same proportions for the bounding box."""
        self.relX += event.x - self.previousX
        self.relY += event.y - self.previousY
        self.previousX = event.x
        self.previousY = event.y
        self.cBox = self.composite.getCoreBox()
        width = self.cBox[2] - self.cBox[0]
        if self.reverseX == 1:
            width = -width
        height = self.cBox[3] - self.cBox[1]
        if self.reverseY == 1:
            height = -height
        if width == 0 or height == 0:  # for unscalable objects, do nothing
            return
        # define the meaning of moving each handle
        if handleName == "x01y0": # north
            centerX = (self.cBox[2] + self.cBox[0])/2
            if not self.reverseY:
                centerY = self.cBox[3]
            else:
                centerY = self.cBox[1]
            scaleFactor = float(height - self.relY)/height
        elif handleName == "x01y1": #south
            centerX = (self.cBox[2] + self.cBox[0])/2
            if not self.reverseY:
                centerY = self.cBox[1]
            else:
                centerY = self.cBox[3]
            scaleFactor = float(height + self.relY)/height
        elif handleName == "x0y01": #west
            if not self.reverseX:
                centerX = self.cBox[2]
            else:
                centerX = self.cBox[0]
            centerY = (self.cBox[3] + self.cBox[1])/2
            scaleFactor = float(width - self.relX)/width
        elif handleName == "x1y01": #east
            if not self.reverseX:
                centerX = self.cBox[0]
            else:
                centerX = self.cBox[2]
            centerY = (self.cBox[3] + self.cBox[1])/2
            scaleFactor = float(width + self.relX)/width
        elif handleName == "x0y0": #northwest
            if not self.reverseX:
                centerX = self.cBox[2]
            else:
                centerX = self.cBox[0]
            if not self.reverseY:
                centerY = self.cBox[3]
            else:
                centerY = self.cBox[1]
            scaleFactor = float(height - self.relY)/height
        elif handleName == "x1y0": #northeast
            if not self.reverseX:
                centerX = self.cBox[0]
            else:
                centerX = self.cBox[2]
            if not self.reverseY:
                centerY = self.cBox[3]
            else:
                centerY = self.cBox[1]
            scaleFactor = float(height - self.relY)/height
        elif handleName == "x0y1": #southwest
            if not self.reverseX:
                centerX = self.cBox[2]
            else:
                centerX = self.cBox[0]
            if not self.reverseY:
                centerY = self.cBox[1]
            else:
                centerY = self.cBox[3]
            scaleFactor = float(height + self.relY)/height
        elif handleName == "x1y1": #southeast
            if not self.reverseX:
                centerX = self.cBox[0]
            else:
                centerX = self.cBox[2]
            if not self.reverseY:
                centerY = self.cBox[1]
            else:
                centerY = self.cBox[3]
            scaleFactor = float(height + self.relY)/height
        #scale if possible
        if abs(width*scaleFactor) > 1 and abs(height*scaleFactor) > 1: #prevent scaling to zero
            self.totalScaleFactorX *= scaleFactor
            self.totalScaleFactorY *= scaleFactor
            self.centerX = centerX/self.zoom
            self.centerY = centerY/self.zoom
            self.composite.scale(self.centerX, self.centerY, scaleFactor, scaleFactor)
            self.bBoxSelectedGF = self.composite.getApproxBoundingBox()
            apply(self.handleSet.set, self.bBoxSelectedGF)           #adjust to the new bounding box
            if scaleFactor < 0:
                self.reverseX = not self.reverseX
                self.reverseY = not self.reverseY
            self.relX = 0
            self.relY = 0
        

    def onHandleSetButtonRelease(self, handleSet, handleName, event):
        """stop on button 1 release"""
        if event.num == 1:
            gfList = self.composite.getComponents()
            for gf in gfList:
                gf.setEventHandler(self.editor.mainHandler)
            if self.totalScaleFactorX != 1. or self.totalScaleFactorY != 1.:
                self.editor.addUndoScale(gfList, self.centerX, self.centerY, self.totalScaleFactorX, self.totalScaleFactorY)

            self.eventHandler.onScalingHandlerStopped()


#assumes that "start" is called on a "onCanvasButton 1" event (button 1 is still down) and takes this event as argument.
class BoxHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = self.editor.getCanvas()
        # the event handler must implement onBoxHandlerStopped()
        self.eventHandler = eventHandler


    # start the handler
    def start(self, event):
        """create a box"""
        self.xy = [event.x,event.y,event.x,event.y]
        stipplexbm = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'stipple.xbm' ) )
        self.box = self.canvas.create_rectangle(self.xy, outline="black", fill="blue", width=1, stipple=stipplexbm)

    #canvas events
    def onCanvasButtonMotion(self, event):
        """resize the box to fit xy[2] and xy[3] to the new mouse position"""
        self.xy[2] = event.x
        self.xy[3] = event.y
        args = [self.box]
        args.extend(self.xy)
        apply(self.canvas.coords, args)


    def onCanvasButtonRelease(self, event):
        """stop and return selection on button 1 release"""
        if event.num == 1:
            self.canvas.delete(self.box)
            self.eventHandler.onBoxHandlerStopped(self.getSelection())

    def getSelection(self):
        """find out what GFs are in the box"""
        if self.xy[0] > self.xy[2]:
            self.xy[0], self.xy[2] = self.xy[2], self.xy[0]
        if self.xy[1] > self.xy[3]:
            self.xy[1], self.xy[3] = self.xy[3], self.xy[1]
        gfList = []
        GFs = self.editor.getGFs()
        for gf in GFs:
            if gf.getCanvas() != None:
                gfBox = gf.getApproxBoundingBox()
                # if gf is in box
                if gfBox[0] > self.xy[0] and gfBox[1] > self.xy[1] and gfBox[2] < self.xy[2] and gfBox[3] < self.xy[3]:
                    gfList.append(gf)
        return gfList

     

#assumes that "start" is called on a "onGFShiftButton 1" event (button 1 is still down) and takes this event as argument.
# ShiftHandler adds the gf th
class ShiftHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        #the event handler must implement onShiftHandlerStopped()
        self.eventHandler = eventHandler
       
    def start(self, gf, gfList, event):
        "start the handler"
        if gf in gfList:
            gfList.remove(gf)
        else:
            gfList.append(gf)

    def onCanvasButtonRelease(self, event):
        "stop on button 1 release"
        if event.num == 1:
            self.eventHandler.onShiftHandlerStopped()
    
