# InsertHandlers.py
# Francois Plamondon
# Summer 2003
import Tkinter
import tkFileDialog
import tkMessageBox
import Graphics
import AbstractHandler as EventHandler 


#the insert() method is implemented by the RectangleInsertHandler and OvalInsertHandler classes.
class GeneralBoxInsertHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        raise NotImplementedError, "GeneralBoxInsertHandler is an abstract class"

    def start(self):
        """start the handler"""
        self.current = None

    def stop(self):
        """stop the handler"""
        return self.current


#canvas events
    def onCanvasButton(self, event):
        """on button 1: insert a new box object (rectangle or oval)
        on button 3: cancel current insertion"""
        if event.num == 1:
            self.zoom = self.editor.getZoom()
            x = event.x/self.zoom
            y = event.y/self.zoom
            self.xy = []
            self.xy.append(x)
            self.xy.append(y)
            self.xy.append(x+1)
            self.xy.append(y+1)
            self.current = self.insert()
        elif event.num == 3:
            if self.current != None:
                self.editor.delete([self.current])
                self.current = None

    def onCanvasButtonMotion(self, event):
        """set xy[2], xy[3] to the new position of the mouse"""
        if self.current != None:
            newXY2 =event.x/self.zoom
            newXY3 = event.y/self.zoom
            if abs(newXY2 - self.xy[0]) >= 1 and abs(newXY3 - self.xy[1]) >= 1: #avoid zero width or height
                self.xy[2] = newXY2
                self.xy[3] = newXY3
                self.current.setCoords(self.xy)


    def onCanvasShiftButtonMotion(self, event):
        """set xy[2], xy[3] to make a square box"""
        if self.current != None:
            x = event.x/self.zoom
            y = event.y/self.zoom
            side = max(abs(x - self.xy[0]), abs(y - self.xy[1]))
            if x > self.xy[0]:
                self.xy[2] = self.xy[0] + side
            else:
                self.xy[2] = self.xy[0] - side
            if y > self.xy[1]:
                self.xy[3] = self.xy[1] + side
            else:
                self.xy[3] = self.xy[1] - side
            self.current.setCoords(self.xy)


    
    def onCanvasButtonRelease(self, event):
        """stop on button 1 release if insertion was not canceled"""
        if event.num == 1 and self.current != None:
            current = self.stop()
            self.eventHandler.onInsertHandlerStopped(current)


# Rectangle Insertion handler
class RectangleInsertHandler(GeneralBoxInsertHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler

    def insert(self):
        """insert a rectangle"""
        return self.editor.createRectangle(self.xy)


# Oval Insertion handler
class OvalInsertHandler(GeneralBoxInsertHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler

    def insert(self):
        """insert an oval"""
        return self.editor.createOval(self.xy)


# Line Insertion handler
class LineInsertHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler

    def start(self):
        """start the handler"""
        self.current = None
        
    def stop(self):
        """stop the handler"""
        return self.current


#canvas events
    def onCanvasButton(self, event):
        """on button 1: insert new line
        on button 3: cancel current insertion"""
        if event.num == 1:
            self.zoom = self.editor.getZoom()
            x = event.x/self.zoom
            y = event.y/self.zoom
            self.xy = []
            self.xy.append(x)
            self.xy.append(y)
            self.xy.append(x)
            self.xy.append(y)
            self.current = self.editor.createLine(self.xy)
        elif event.num == 3:
            if self.current != None:
                self.editor.delete([self.current])
                self.current = None
            

    def onCanvasButtonMotion(self, event):
        """set xy[2], xy[3] to the new position of the cursor"""
        if self.current != None:
            self.xy[2] =  event.x/self.zoom
            self.xy[3] =  event.y/self.zoom
            self.current.setCoords(self.xy)


    def onCanvasShiftButtonMotion(self, event):
        """set xy[2], xy[3] to make a perfectly horizontal or vertical line, depending which one is closer"""
        if self.current != None:
            x = event.x/self.zoom
            y = event.y/self.zoom
            if abs(x - self.xy[0]) > abs(y - self.xy[1]):
                self.xy[2] = x
                self.xy[3] = self.xy[1]
            else:
                self.xy[2] = self.xy[0]
                self.xy[3] = y
            self.current.setCoords(self.xy)
            
    
    def onCanvasButtonRelease(self, event):
        """stop on button 1 release if insertion was not canceled."""
        if event.num == 1 and self.current != None:
            current = self.stop()
            self.eventHandler.onInsertHandlerStopped(current)



# Base class for Polyline and Polygon Insertion
class PolyInsertHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        raise NotImplementedError, "PolyInsertHandler is an abstract class"

    def start(self, smooth=0):
        """start the handler"""
        self.current = None
        self.smooth = smooth # smooth option
        self.inserting = 0

    def stop(self):
        """stop the handler. if there are less than 2 points, cancel insertion"""
        if self.current != None:
            if len(self.xy) < self.minimumCoords:
                self.editor.delete([self.current])
                self.current = None
            return self.current

    def create(self):
        pass

#canvas events
    def onCanvasButton(self, event):
        if event.num == 1:
            self.inserting = 1
            self.zoom = self.editor.getZoom()
            x = event.x/self.zoom
            y = event.y/self.zoom
            if self.current == None:
                self.xy = []
                self.xy.append(x)
                self.xy.append(y)
                self.xy.append(x)
                self.xy.append(y)
                self.current = self.create()
            else:
                self.xy.append(x)
                self.xy.append(y)
                self.current.setCoords(self.xy)
        elif event.num == 3:
            if self.inserting: #if button 1 also being pressed, cancel insertion
                self.editor.delete([self.current])
                self.current = None
                self.inserting = 0
            else:
                self.stop()
                self.eventHandler.onInsertHandlerStopped(self.current)


    def onCanvasDoubleButton(self, event):
        self.onCanvasButton(event)


    def onCanvasButtonMotion(self, event):
        if self.current != None and self.inserting:
            x = event.x/self.zoom
            y = event.y/self.zoom
            self.xy[len(self.xy) - 2] = x
            self.xy[len(self.xy) - 1] = y
            self.current.setCoords(self.xy)


    def onCanvasShiftButtonMotion(self, event):
        if self.current != None and self.inserting:
            x = event.x/self.zoom
            y = event.y/self.zoom
            if abs(x - self.xy[len(self.xy) - 4]) > abs(y - self.xy[len(self.xy) - 3]):
                self.xy[len(self.xy) - 2] = x
                self.xy[len(self.xy) - 1] = self.xy[len(self.xy) - 3]
            else:
                self.xy[len(self.xy) - 2] = self.xy[len(self.xy) - 4]
                self.xy[len(self.xy) - 1] = y
            self.current.setCoords(self.xy)

    
    def onCanvasButtonRelease(self, event):
        if event.num == 1:
            self.inserting = 0

#fill color event
    def onFillColor(self, color):
        if self.current != None:
            self.current.setFillColor(color)

#line width event
    def onLineWidth(self, lineWidth):
        if self.current != None:
            self.current.setWidth(lineWidth)


class PolylineInsertHandler(PolyInsertHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler
        self.minimumCoords = 4 # minimum number of coordinates to make a polyline

    def create(self):
        return self.editor.createLine(self.xy, smooth=self.smooth)


class PolygonInsertHandler(PolyInsertHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler
        self.minimumCoords = 6 #minimum number of coordinates to make a polygon

    def create(self):
        return self.editor.createPolygon(self.xy, smooth=self.smooth)

    def onOutlineColor(self, color):
        if self.current != None:
            self.current.setOutlineColor(color)

    def onOutlineFillOption(self, option):
        if self.current != None:
            self.current.setOutlineOption(option[0])
            self.current.setFillOption(option[1])


# Connector Insertion handler
class ConnectorInsertHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler

    #starts the handler.
    def start(self):
        self.current = None

    # stops the handler.
    def stop(self):
        return self.current



#canvas events
    def onCanvasButton(self, event):
        if event.num == 1:
            self.zoom = self.editor.getZoom()
            x = event.x/self.zoom
            y = event.y/self.zoom
            self.current = self.editor.createConnector([x,y])
            self.eventHandler.onInsertHandlerStopped(self.current)


#Image Insertion Handler
class ImageInsertHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler

    #starts the handler.
    def start(self):
        self.current = None

    # stops the handler.
    def stop(self):
        return self.current


#canvas events
    def onCanvasButton(self, event):
        if event.num == 1:
            self.zoom = self.editor.getZoom()
            x = event.x/self.zoom
            y = event.y/self.zoom
            filename = tkFileDialog.askopenfilename(title="Open Image File",
                        filetypes=[("GIF files", "*.gif"),("All files", "*")] )
            self.editor.root.focus_force()
            if( filename != "" and filename[-4:].upper() == '.GIF' ):
                if( 1):#try:
                    self.current = self.editor.createImage([x,y], filename)
                else:#except:
                    tkMessageBox.showerror("Open Image File","Cannot open file:\nFormat not recognized")
                    self.eventHandler.onInsertHandlerStopped(None)
                    return
                self.eventHandler.onInsertHandlerStopped(self.current)
                return
            else:
                self.eventHandler.onInsertHandlerStopped(None)
                return
            

# Text Insertion Handler
# The encapsulation of TextGF is broken here. Tkinter provides text editing
# capabilities that are used directly on the text item of the TextGF object.
class TextInsertHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler

    #starts the handler.
    def start(self):
        self.current = None

    # stops the handler.
    def stop(self):
        return self.current

        
    #canvas events
    def onCanvasButton(self, event):
        if event.num == 1:
            self.zoom = self.editor.getZoom()
            x = event.x/self.zoom
            y = event.y/self.zoom
            self.current = self.editor.createText([x,y], "")
            self.eventHandler.onInsertHandlerStopped(self.current)



# Named Connector Insertion handler
class NamedConnectorInsertHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler

    #starts the handler.
    def start(self):
        self.current = None

    # stops the handler.
    def stop(self):
        return self.current

    #canvas events
    def onCanvasButton(self, event):
        if event.num == 1:
            self.zoom = self.editor.getZoom()
            x = event.x/self.zoom
            y = event.y/self.zoom
            self.current = self.editor.createNamedConnector([x,y])
            self.eventHandler.onInsertHandlerStopped(self.current)

# Attribute Insertion handler
class AttributeInsertHandler(EventHandler.EventHandler):
    def __init__(self, editor, eventHandler):
        self.editor = editor
        self.canvas = editor.getCanvas()
        self.eventHandler = eventHandler

    #starts the handler.
    def start(self):
        self.current = None

    # stops the handler.
    def stop(self):
        return self.current

    #canvas events
    def onCanvasButton(self, event):
        if event.num == 1:
            self.zoom = self.editor.getZoom()
            x = event.x/self.zoom
            y = event.y/self.zoom
            self.current = self.editor.createAttribute([x,y], "attribute")
            self.eventHandler.onInsertHandlerStopped(self.current)

