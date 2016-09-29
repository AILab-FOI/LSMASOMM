"""
EditHandlers.py

Francois Plamondon
Summer 2003
"""

import Tkinter
import Graphics
import Handles
import AbstractHandler as EventHandler 
import TransformHandlers
import Choosers

from Utilities import snapIt

#Handler to edit text
# Tkinter provides text editing capabilities that are used
# directly on the text item of the TextGF object.
# The handler assumes that button 1 is being pressed on the textGF when it is started.
class TextEditHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        # eventHandler must implement onEditHandlerStopped()
        self.eventHandler = eventHandler
        self.currentText = None
        self.clipboard = ""
        self.firstSelectedIndex = 0 # index of the tail of the current selection
        self.textSelectionHandler = TextSelectionHandler(editor, self)

    #starts the handler.
    def start(self, currentText, showProperties = True):
        self.currentText = currentText
        self.root = self.editor.getRoot()
        if( showProperties ):
          self.createPropertiesWindow()
        else:
          self.started = 1
          class noWindow:
            def destroy(self): pass
          self.propertiesWindow = noWindow()
        self.setFocusOnText()
        self.canvas.select_from(self.currentText.item, 0)
        self.canvas.select_to(self.currentText.item, Tkinter.END)
        self.currentHandler = None

    def createPropertiesWindow(self):
        # start a font chooser in a new window
        self.propertiesWindow = Tkinter.Toplevel()
        x,y = self.currentText.getCoords()[:2]
        y+= 60          
        self.propertiesWindow.geometry("+%d+%d" % (x,y))
        
        #self.propertiesWindow.geometry("+%d+%d" % (self.root.winfo_rootx()+self.root.winfo_width()-400, self.root.winfo_rooty()))
        self.propertiesWindow.title("Text - AToM3")
        self.propertiesWindow.transient(self.root) 
        self.propertiesWindow.bind("<Key>", self.onKey)
        self.propertiesWindow.bind("<Shift-Key>", self.onShiftKey)
        self.propertiesWindow.bind("<Control-Key>", self.onControlKey)
        self.properties = Choosers.TextProperties(self.propertiesWindow, self.currentText.getFamily(), self.currentText.getSize(), self.currentText.getBold(), self.currentText.getItalic(), self.currentText.getUnderline(), self.currentText.getAnchor(), self)
        self.started = 0 # while we wait for visibility of the new window,
        #the callback method of other events can be called.
        #We use the boolean self.started so that the event methods ignore the calls until self.started == 1
        #self.propertiesWindow.wait_visibility()
        self.started = 1        
        try:    self.propertiesWindow.grab_set() 
        except: pass 
        self.propertiesWindow.focus_force()  
        self.setFocusOnText()

    def setFocusOnText(self):
        #set focus to the text item
        self.root.focus_set()
        self.canvas.focus_set() # focus on canvas
        self.canvas.focus(self.currentText.item) #focus on text
        

    # stops the handler
    def stop(self):
        self.canvas.select_clear()
        self.canvas.focus("") # remove focus from self.currentText.item
        self.propertiesWindow.destroy() # destroy text properties window
        return self.currentText


    # internal FontChooser events
    def onFamily(self, family):
        self.currentText.setFamily(family)

    def onSize(self, size):
        self.currentText.setSize(size)

    def onBold(self, bold):
        self.currentText.setBold(bold)

    def onItalic(self, italic):
        self.currentText.setItalic(italic)

    def onUnderline(self, underline):
        self.currentText.setUnderline(underline)

    def onAnchor(self, anchor):
        self.currentText.setAnchor(anchor)

    #GF events
    def onGFButton(self, gf, event):
        if not self.started: return
        if event.num == 1:
            if gf == self.currentText:
                self.currentHandler = self.textSelectionHandler
                self.currentHandler.start(gf, event)

    def onGFDoubleButton(self, gf, event):
        self.onGFButton(gf, event)

    def onGFButtonMotion(self, gf, event):
        if not self.started: return
        if( self.currentText != None and self.currentHandler != None):
            self.currentHandler.onGFButtonMotion(gf, event)

    def onGFButtonRelease(self, gf, event):
        if not self.started: return
        if self.currentHandler != None:
            self.currentHandler.onGFButtonRelease(gf, event)

#canvas events
    def onCanvasButton(self, event):
        if not self.started: return
        box = self.currentText.getApproxBoundingBox()
        if box[0] > event.x or box[1] > event.y or box[2] < event.x or box[3] < event.y:
            self.stop()
            self.eventHandler.onEditHandlerStopped([])

    def onCanvasDoubleButton(self, event):
        if not self.started: return
        self.onCanvasButton(event)

    def onCanvasButtonRelease(self, event):
        if not self.started: return
        if self.currentHandler != None:
            self.currentHandler.onCanvasButtonRelease(event)
            
            
# Keyboard events
    def onKey(self, event):
        if not self.started: return
        #set focus to the main window
        self.editor.getRoot().focus_set()
        self.canvas.focus_set() # focus on canvas
        self.canvas.focus(self.currentText.item) #focus on text

        insertIndex = self.canvas.index(self.currentText.item, Tkinter.INSERT)
        isSelected = self.canvas.tk.call(self.canvas._w, 'select', 'item')
        if isSelected:
            firstSelected = self.canvas.index(self.currentText.item, Tkinter.SEL_FIRST)
            lastSelected = self.canvas.index(self.currentText.item, Tkinter.SEL_LAST) - 1
        if event.keysym == "BackSpace":
            if isSelected:
                self.canvas.dchars(self.currentText.item, firstSelected, lastSelected)
                self.canvas.select_clear()
            elif insertIndex > 0:
                self.canvas.dchars(self.currentText.item, insertIndex - 1)
        elif event.keysym == "Delete":
            if isSelected:
                self.onDelete()
            else:
                self.canvas.dchars(self.currentText.item, insertIndex)
            self.canvas.select_clear()
        elif event.keysym == "Home":
            self.canvas.icursor(self.currentText.item, 0)
            self.canvas.select_clear()
        elif event.keysym == "End":
            self.canvas.icursor(self.currentText.item, Tkinter.END)
            self.canvas.select_clear()
        elif event.keysym == "Right":
            self.canvas.icursor(self.currentText.item, insertIndex + 1)
            self.canvas.select_clear()
        elif event.keysym == "Left":
            self.canvas.icursor(self.currentText.item, insertIndex - 1)
            self.canvas.select_clear()
        elif event.keysym == "Return":
            if isSelected:
                self.canvas.dchars(self.currentText.item, firstSelected, lastSelected)
                self.canvas.select_clear()
            self.canvas.insert(self.currentText.item, "insert", "\n")
        elif event.char >= " ":# usual character
            if isSelected:
                self.canvas.dchars(self.currentText.item, firstSelected, lastSelected)
                self.canvas.select_clear()
            self.canvas.insert(self.currentText.item, "insert", event.char)
        else:
            pass


    def onShiftKey(self, event):
            if not self.started: return
            insertIndex = self.canvas.index(self.currentText.item, Tkinter.INSERT)
            isSelected = self.canvas.tk.call(self.canvas._w, 'select', 'item')
            if event.keysym == "Right":
                self.canvas.icursor(self.currentText.item, insertIndex + 1)
                if not isSelected:
                    self.firstSelectedIndex = insertIndex
                self.canvas.select_from(self.currentText.item, min(insertIndex + 1, self.firstSelectedIndex))
                self.canvas.select_to(self.currentText.item, max(insertIndex + 1, self.firstSelectedIndex))

            elif event.keysym == "Left":
                self.canvas.icursor(self.currentText.item, insertIndex - 1)
                if not isSelected:
                    self.firstSelectedIndex = insertIndex
                self.canvas.select_from(self.currentText.item, min(insertIndex - 1, self.firstSelectedIndex))
                self.canvas.select_to(self.currentText.item, max(insertIndex - 1, self.firstSelectedIndex))
            else:
                self.onKey(event)


    def onControlKey(self, event):
        if not self.started: return
        isSelected = self.canvas.tk.call(self.canvas._w, "select", "item")
        if event.keysym == "x": # cut selection
            if isSelected:
                self.onCut()
        elif event.keysym == "c": # copy selection
            if isSelected:
                self.onCopy()
        elif event.keysym == "v": # paste
            self.onPaste()


    #fill color event
    def onFillColor(self, color):
        self.currentText.setFillColor(color)


    def onTextSelectionHandlerStopped():
        self.currentHandler = None


    def onEditMenu(self, editMenu):
        isSelected = self.canvas.tk.call(self.canvas._w, "select", "item")
        if isSelected:
            editMenu.entryconfigure(2, state=Tkinter.NORMAL) #cut
            editMenu.entryconfigure(3, state=Tkinter.NORMAL) #copy
            editMenu.entryconfigure(5, state=Tkinter.NORMAL) #delete
        editMenu.entryconfigure(4, state=Tkinter.NORMAL) #paste
            
            
    def onCut(self): #assumes that there is a selection
        ctext = self.canvas.itemcget(self.currentText.item, "text")
        firstSelected = self.canvas.index(self.currentText.item, Tkinter.SEL_FIRST)
        lastSelected = self.canvas.index(self.currentText.item, Tkinter.SEL_LAST)
        self.clipboard = ctext[firstSelected:lastSelected]
        self.canvas.dchars(self.currentText.item, firstSelected, lastSelected - 1)
        self.canvas.select_clear()


    def onCopy(self): #assumes that there is a selection
        ctext = self.canvas.itemcget(self.currentText.item, "text")
        firstSelected = self.canvas.index(self.currentText.item, Tkinter.SEL_FIRST)
        lastSelected = self.canvas.index(self.currentText.item, Tkinter.SEL_LAST)
        self.clipboard = ctext[firstSelected:lastSelected]


    def onPaste(self):
        isSelected = self.canvas.tk.call(self.canvas._w, "select", "item")
        if isSelected:
            self.canvas.select_clear()
        self.canvas.insert(self.currentText.item, "insert", self.clipboard)

        
    def onDelete(self): #assumes that there is a selection
        firstSelected = self.canvas.index(self.currentText.item, Tkinter.SEL_FIRST)
        lastSelected = self.canvas.index(self.currentText.item, Tkinter.SEL_LAST) - 1
        self.canvas.dchars(self.currentText.item, firstSelected, lastSelected)
        self.canvas.select_clear()


    def onTextSelectHandlerStopped(self):
        pass
        
    
# helper class for TextEditHandler
# Selects text
class TextSelectionHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler

#assumes that the handler is started on a GFButton1 event and takes this event as argument.
    def start(self, gf, event ):
        self.currentText = gf
        # translate to canvas coordinates
        cx = self.canvas.canvasx(event.x + 3)
        cy = self.canvas.canvasy(event.y)
        self.firstSelectedIndex = self.canvas.index(self.currentText.item, "@%d,%d" % (cx, cy))
        # move cursor
        self.canvas.icursor(self.currentText.item, self.firstSelectedIndex)
        self.canvas.select_clear()

    def onGFButtonMotion(self, gf, event):
        isSelected = self.canvas.tk.call(self.canvas._w, 'select', 'item')
        cx = self.canvas.canvasx(event.x + 3)
        cy = self.canvas.canvasy(event.y)
        pointerIndex = self.canvas.index(self.currentText.item, "@%d,%d" % (cx, cy))
        # move cursor
        # self.canvas.select_adjust(self.currentText.item, pointerIndex) #doesn't work
        self.canvas.icursor(self.currentText.item, pointerIndex)
        self.canvas.select_from(self.currentText.item, min(pointerIndex, self.firstSelectedIndex))
        self.canvas.select_to(self.currentText.item, max(pointerIndex, self.firstSelectedIndex))


    def onCanvasButtonRelease(self, event):
        if event.num == 1:
            self.eventHandler.onTextSelectHandlerStopped()


class ImageEditHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.root = self.editor.getRoot()
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler
        self.translationHandler = TransformHandlers.TranslationHandler(self.editor, self)
        self.currentHandler = None

    #starts the handler.
    def start(self, current, showProperties = True):
        self.zoom = self.editor.getZoom()
        self.current = current
        if( showProperties ):
          self.createPropertiesWindow()
        else:
          self.started = 1
          class noWindow:
            def destroy(self): pass
          self.propertiesWindow = noWindow()


    def createPropertiesWindow(self):
        # start an anchor chooser in a new window
        self.propertiesWindow = Tkinter.Toplevel()
        x,y = self.current.getCoords()[:2]
        self.propertiesWindow.geometry("+%d+%d" % (x,y))
        #self.propertiesWindow.geometry("+%d+%d" % (self.root.winfo_rootx()+self.root.winfo_width()-150, self.root.winfo_rooty()))
        self.propertiesWindow.title("Image - AToM3")
        self.propertiesWindow.transient(self.root)        
        self.properties = Choosers.ImageProperties(self.propertiesWindow, self.current.getAnchor(), self)
        try:    self.propertiesWindow.grab_set() 
        except: pass  
        self.propertiesWindow.focus_set()  

    # stops the handler.
    def stop(self):
        self.propertiesWindow.destroy()
        return self.current

#internal anchor event
    def onAnchor(self, anchor):
        self.current.setAnchor(anchor)

#GF events
    def onGFButton(self, gf, event):
        if self.currentHandler != None:
            self.currentHandler.onGFButton(gf, event)
        elif event.num == 1:
            if gf is self.current:
                self.currentHandler = self.translationHandler
                self.currentHandler.start([self.current], event)


    def onGFDoubleButton(self, gf, event):
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
            self.stop()
            self.eventHandler.onEditHandlerStopped([])

#Keyboard events
    def onKey(self, event):
        if event.keysym == "Delete":
            self.editor.delete([self.current])
            self.stop()
            self.eventHandler.onEditHandlerStopped([])

#sub-handler events
    def onTranslationHandlerStopped(self, dxdy):
        self.currentHandler = None



class PolyEditHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        raise NotImplementedError, "PolyEditHandler is an abstract class"

    def initPolyEditHandler(self, editor, eventHandler):
        self.editor = editor
        self.root = self.editor.getRoot()
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler
        self.translationHandler = TransformHandlers.TranslationHandler(self.editor, self)
        self.movePointHandler = MovePointHandler(self.editor, self)
        self.currentHandler = None

    #starts the handler.
    def start(self, currentPoly, showProperties=True):
        self.zoom = self.editor.getZoom()
        self.gfsClicked = [] #gfs clicked when leaving
        self.currentPoly = currentPoly
        self.handles = []
        i = 0
        coords = self.currentPoly.getCoords()
        for xy in coords:
            if i % 2 == 0:
                x = xy
            else:
                y = xy
                self.handles.append(Handles.Handle(x*self.zoom, y*self.zoom, (i - 1)/2, 1, self.canvas, self))
            i = i + 1
        self.startPolyEditHandler(showProperties)


    def startPolyEditHandler( *args ):
        pass

    # stops the handler.
    def stop(self):
        for h in self.handles:
            h.deactivate()
        self.stopPolyEditHandler()
        return self.currentPoly


    def stopPolyEditHandler(self):
        pass
    
    
# internal handle events
    def onHandleButton(self, handleNumber, event):
        if self.currentHandler != None:
            self.currentHandler.onHandleButton(handleNumber, event)
        elif event.num == 1:
            self.currentHandler = self.movePointHandler
            self.currentHandler.start(self.currentPoly, handleNumber, self.handles, event)

    def onHandleButtonMotion(self, handleNumber, event):
        if self.currentHandler != None:
            self.currentHandler.onHandleButtonMotion(handleNumber, event)

    def onHandleShiftButtonMotion(self, handleName, event):
            pass

    def onHandleButtonRelease(self, handleNumber, event):
        if self.currentHandler != None:
            self.currentHandler.onHandleButtonRelease(handleNumber, event)

#GF events
    def onGFButton(self, gf, event):
        if self.currentHandler != None:
            self.currentHandler.onGFButton(gf, event)
        elif event.num == 1:
            if gf is self.currentPoly:
                for h in self.handles:
                    h.setVisible(0)
                self.currentHandler = self.translationHandler
                self.currentHandler.start([self.currentPoly], event)
            else:
                self.gfsClicked = [gf]


    def onGFDoubleButton(self, gf, event):
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
            self.stop()
            self.eventHandler.onEditHandlerStopped([])

#Keyboard events
    def onKey(self, event):
        if event.keysym == "Delete":
            for h in self.handles:
                h.deactivate()
            self.editor.delete([self.currentPoly])
            self.eventHandler.onEditHandlerStopped([])

#color event
    def onFillColor(self, color):
        self.currentPoly.setFillColor(color)

#line width event
    def onLineWidth(self, lineWidth):
        self.currentPoly.setWidth(lineWidth)



#sub-handler events
    def onTranslationHandlerStopped(self, dxdy):
        self.currentHandler = None
        zoom = self.editor.getZoom()
        for h in self.handles:
            h.translate(dxdy[0] * zoom, dxdy[1] * zoom)
        for h in self.handles:
            h.setVisible(1)
        #self.activateHandles()

    def onMovePointHandlerStopped(self):
        self.currentHandler = None
        


class PolygonEditHandler(PolyEditHandler):
    def __init__(self, editor, eventHandler):
        self.initPolyEditHandler(editor, eventHandler)

    def onOutlineColor(self, color):
        self.currentPoly.setOutlineColor(color)

    def onOutlineFillOption(self, option):
        self.currentPoly.setOutlineOption(option[0])
        self.currentPoly.setFillOption(option[1])

class LineEditHandler(PolyEditHandler):
    def __init__(self, editor, eventHandler):
        self.initPolyEditHandler(editor, eventHandler)


    def startPolyEditHandler(self, showProperties = True ):
      
        if( showProperties ):
          self.createPropertiesWindow()
        else:
          self.started = 1
          class noWindow:
            def destroy(self): pass
          self.propertiesWindow = noWindow()
   
    def stopPolyEditHandler(self):
        self.propertiesWindow.destroy()


    def createPropertiesWindow(self):
        # start an anchor chooser in a new window
        self.propertiesWindow = Tkinter.Toplevel()
        x,y = self.currentPoly.getCoords()[:2]
        self.propertiesWindow.geometry("%dx%d+%d+%d" % (160, 295, x,y))
        self.propertiesWindow.title("Line - AToM3")
        self.propertiesWindow.transient(self.root) 
        self.properties = Choosers.LineProperties(self.propertiesWindow, self.currentPoly.getStipple(), self.currentPoly.getArrow(), self.currentPoly.getCapstyle(), self.currentPoly.getJoinstyle(), self)
        try:    self.propertiesWindow.grab_set() 
        except: pass 
        self.propertiesWindow.focus_set()  
        
#line properties events
    def onArrow(self, arrow):
        self.currentPoly.setArrow(arrow)

    def onCapstyle(self, capstyle):
        self.currentPoly.setCapstyle(capstyle)

    def onJoinstyle(self, joinstyle):
        self.currentPoly.setJoinstyle(joinstyle)

    def onStipple(self, stipple):
        self.currentPoly.setStipple(stipple)




# assumes that start is called on a "onHandleButton 1" event (button 1 is still down) and the
# event is given as argument.
class MovePointHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.eventHandler = eventHandler


    def start(self, poly, handleNumber, handles, event, showProperties=None):
        self.previousHX = event.x
        self.previousHY = event.y
        self.poly = poly
        self.oldCoords = self.poly.getCoords()
        self.handles = handles
        self.zoom = self.editor.getZoom()

    def onHandleButton(self, handleNumber, event):
        pass

    def onHandleButtonMotion(self, handleNumber, event):
        newXY = self.poly.getCoords()
        
        
        # Using the snap grid
        if( self.editor.snapGridInfoTuple ):
          gridSize = self.editor.snapGridInfoTuple[0]
          x0 = self.previousHX
          y0 = self.previousHY
                    
          # Snapping to the top left corner of the first object encountered
          x = newXY[handleNumber * 2]
          y = newXY[handleNumber * 2 + 1] 
          x1 = snapIt( x + event.x - x0,event.x,gridSize)
          y1 = snapIt( y + event.y - y0,event.y,gridSize)  
                            
          dx = x1 - x0
          dy = y1 - y0
          
          newXY[handleNumber * 2] += dx/self.zoom
          newXY[handleNumber * 2 + 1] += dy/self.zoom
          self.poly.setCoords(newXY)
          self.handles[handleNumber].translate(dx, dy)
          
          self.previousHX = x1
          self.previousHY = y1
          
        # No snaps
        else:
          dx = (event.x - self.previousHX)
          dy = (event.y - self.previousHY)
          newXY[handleNumber * 2] += dx/self.zoom
          newXY[handleNumber * 2 + 1] += dy/self.zoom
          self.poly.setCoords(newXY)
          self.handles[handleNumber].translate(dx, dy)
          self.previousHX = event.x
          self.previousHY = event.y

    def onHandleButtonRelease(self, handleNumber, event):
        if event.num == 1:
            newCoords = self.poly.getCoords()
            if newCoords != self.oldCoords:
                self.editor.addUndoSetCoords(self.poly, self.oldCoords)
            self.eventHandler.onMovePointHandlerStopped()



class NamedPortEditHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.root = self.editor.getRoot()
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler
        self.translationHandler = TransformHandlers.TranslationHandler(self.editor, self)
        self.currentHandler = None

    #starts the handler.
    def start(self, current, showProperties = True):
        self.current = current
        self.createPropertiesWindow()
        
    def createPropertiesWindow(self):
        # start an anchor chooser in a new window
        self.propertiesWindow = Tkinter.Toplevel()
        x,y = self.current.getCoords()[:2]
        self.propertiesWindow.geometry("+%d+%d" % (x,y))
        self.propertiesWindow.title("Named Connector - AToM3")
        self.propertiesWindow.transient(self.root)        
        self.properties = Choosers.NamedPortProperties(self.propertiesWindow, self.current.getName(), self)
        try:    self.propertiesWindow.grab_set() 
        except: pass
        self.propertiesWindow.focus_set()  
        
    # Returns the current graphical object from Graphics.py
    def getCurrent( self ):
        return self.current

    # stops the handler.
    def stop(self):
        self.propertiesWindow.destroy()
        return self.current

    #internal anchor event
    def onSetName(self, name ):
        self.current.setName( name )

    #GF events
    def onGFButton(self, gf, event):
        if self.currentHandler != None:
            self.currentHandler.onGFButton(gf, event)
        elif event.num == 1:
            if gf is self.current:
                self.currentHandler = self.translationHandler
                self.currentHandler.start([self.current], event)


    def onGFDoubleButton(self, gf, event):
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
            self.stop()
            self.eventHandler.onEditHandlerStopped([])

    #Keyboard events
    def onKey(self, event):
        if event.keysym == "Delete":
            self.editor.delete([self.current])
            self.stop()
            self.eventHandler.onEditHandlerStopped([])

    #sub-handler events
    def onTranslationHandlerStopped(self, dxdy):
        self.currentHandler = None



'''
class AttributeEditHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.root = self.editor.getRoot()
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler
        self.translationHandler = TransformHandlers.TranslationHandler(self.editor, self)
        self.currentHandler = None

    #starts the handler.
    def start(self, current, showProperties = True):
        self.current = current
        self.createPropertiesWindow()
        
    def createPropertiesWindow(self):
        # start an anchor chooser in a new window
        self.propertiesWindow = Tkinter.Toplevel()
        x,y = self.current.getCoords()[:2]
        self.propertiesWindow.geometry("+%d+%d" % (x,y))
        self.propertiesWindow.title("Attributes - AToM3")
        self.propertiesWindow.transient(self.root)        
        self.properties = Choosers.AttributeProperties(self.propertiesWindow, self.current.getText(), self)
        try:    self.propertiesWindow.grab_set() 
        except: pass
        self.propertiesWindow.focus_set()  
        
        
    # Returns the current graphical object from Graphics.py
    def getCurrent( self ):
        return self.current

    # stops the handler.
    def stop(self):
        self.propertiesWindow.destroy()
        return self.current

    #internal anchor event
    def onSetAttribute(self, attr ):
        print "Setting attr to ", attr
        self.current.setText( attr )

    #GF events
    def onGFButton(self, gf, event):
        if self.currentHandler != None:
            self.currentHandler.onGFButton(gf, event)
        elif event.num == 1:
            if gf is self.current:
                self.currentHandler = self.translationHandler
                self.currentHandler.start([self.current], event)


    def onGFDoubleButton(self, gf, event):
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
            self.stop()
            self.eventHandler.onEditHandlerStopped([])

    #Keyboard events
    def onKey(self, event):
        if event.keysym == "Delete":
            self.editor.delete([self.current])
            self.stop()
            self.eventHandler.onEditHandlerStopped([])

    #sub-handler events
    def onTranslationHandlerStopped(self, dxdy):
        self.currentHandler = None
 '''

class AttributeEditHandler(TextEditHandler):
    def __init__(self, editor, eventHandler):
        TextEditHandler.__init__(self, editor, eventHandler)

  
    # Returns the current graphical object from Graphics.py
    def getCurrent( self ):
        return self.currentText
      
    def onSetAttribute(self, attr ):
        self.currentText.setText( attr )
      
    def specialAttributeProperties( self ):
        # start an anchor chooser in a new window
        self.propertiesWindow = Tkinter.Toplevel()
        x,y = self.currentText.getCoords()[:2]
        self.propertiesWindow.geometry("+%d+%d" % (x,y))
        self.propertiesWindow.title("Attributes - AToM3")
        self.propertiesWindow.transient(self.root)        
        self.properties = Choosers.AttributeProperties(self.propertiesWindow, self.currentText.getText(), self)
        try:    self.propertiesWindow.grab_set() 
        except: pass
        self.propertiesWindow.focus_set()  
  
    #------------------------ Overriden Methods -----------------------------
    
    #starts the handler.
    def start(self, currentText, showProperties = True):
        self.currentText = currentText
        self.root = self.editor.getRoot()
        if( showProperties ):
          self.createPropertiesWindow()
        else:
          self.started = 1
          self.specialAttributeProperties()
          self.currentHandler = None
          return
        self.setFocusOnText()
        self.canvas.select_from(self.currentText.item, 0)
        self.canvas.select_to(self.currentText.item, Tkinter.END)
        self.currentHandler = None
    
    def onKey(self, event):
        self.specialAttributeProperties()
                    
    def onShiftKey(self, event):
        pass
    def onControlKey(self, event):
        pass   
    def onEditMenu(self, editMenu):
        pass            
    def onCut(self): #assumes that there is a selection
        pass
    def onPaste(self):
        pass
    def onDelete(self): #assumes that there is a selection
        pass
      
      