# Graphics.py
# Francois Plamondon
# Summer 2003

# Graphical object classes

import Tkinter
import Geometry
import tkFont
import os
import binascii

from FilePaths import GRAPHIC_EDITOR_DATA

# GF abstract class. Provides an interface to manipulate a general graphical object.
class GF:
    def __init__(self):
        raise NotImplementedError, 'GF is an abstract class'

    def accept(self, visitor):
        """accept visitor method"""
        pass


    def getApproxBoundingBox(self): #  return 4-tuple
        """get the approximate bounding box of the GF"""
        pass


    def getCoreBox(self): # return 4-tuple
        """get the minimum box containing all the points of the GF"""
        pass
    

    def translate(self, dx,dy):
        """translate the GF by (dx, dy)"""
        pass


    def rotate(self, centerX, centerY, angle):
        """rotate the GF by angle degrees using (centerX, centerY) as the center of rotation.
        angle must be a multiple of 90 degrees."""
        pass

    
    def scale(self, centerX, centerY, scaleFactorX, scaleFactorY):
        """scale the GF by a factor of scaleFactor using (centerX, centerY) as the center."""
        pass

    
    def setZoom(self, zoom):
        """set the zoom and update the item(s)"""
        pass


    def setLock(self, isLocked):
        """set lock to isLocked. If true, any operation has no effect"""
        pass


    def getLock(self): #boolean 
        """get lock. return true iff the GF is in a locked state"""
        pass


    def copy(self): #GF
        """copy the GF and return it"""
        pass


    def pushToBottom(self):
        """push the GF under all the other GFs on the canvas"""
        pass


    def bringToTop(self):
        """bring the GF above all the other GFs on the canvas"""
        pass


    def getEventHandler(self):
        """get the event handler"""
        return self.eventHandler


    def setEventHandler(self, eventHandler):
        """set the event handler"""
        self.eventHandler = eventHandler


    def getCanvas(self):
        """get the canvas"""
        return self.canvas



# LeafGF abstract class. Implements the methods that are similar among the leaf classes.
class LeafGF(GF):
    
    OBJECT_NUMBER = 0
    
    def __init__(self):
        raise NotImplementedError, 'LeafGF is an abstract class'

    def getNewObjectNumber( self, savedNumber = None ):
        """ Unique number identifier that is preserved accross saving/loading """
        if( savedNumber ):
            self.objectNumber = savedNumber
            if( savedNumber >= LeafGF.OBJECT_NUMBER ):
                LeafGF.OBJECT_NUMBER = savedNumber + 1
        else:
            self.objectNumber = LeafGF.OBJECT_NUMBER
            LeafGF.OBJECT_NUMBER += 1
                
    def getObjectNumber( self ):
        """ Returns the objects unique identifier """
        return self.objectNumber
    
    def getApproxBoundingBox(self): #  return 4-tuple (int)  
        """get the approximate bounding box of the GF"""
        return self.canvas.bbox(self.item)


    def getCoreBox(self): # return 4-tuple
        """get the minimum box containing all the points of the GF"""
        xMin = self.xy[0]
        yMin = self.xy[1]
        xMax = self.xy[0]
        yMax = self.xy[1]
        i = 0
        for xy in self.xy:
            if i % 2 == 0:
                if xy < xMin:
                    xMin = xy
                elif xy > xMax:
                    xMax = xy
            else:
                if xy < yMin:
                    yMin = xy
                elif xy > yMax:
                    yMax = xy
            i = i + 1
        return (xMin*self.zoom, yMin*self.zoom, xMax*self.zoom, yMax*self.zoom)
        

    def operateGeom(self, operation, args):
        """general geometric operation"""
        if self.isLocked == 1:
            return
          
        # Wow, this is fantastically ugly
        """
        newXY = []
        i = 0        
        for xy in self.xy:
            if i % 2 == 0:
                allArgs = [xy]
            else:
                allArgs.append(xy)
                allArgs.extend(args)
                newX, newY = apply(operation, allArgs) 
                newXY.append(newX)
                newXY.append(newY)
            i = i + 1
        self.xy = newXY
        """
        
        # This is understandable IMHO - Denis 
        newXY = []
        for i in range(0, len(self.xy), 2):
          xyPair = self.xy[i:i+2]
          newXY.extend( apply(operation, xyPair + args ) )
        self.xy = newXY

        if self.canvas != None:
            self.updateView()

        
    def translate(self, dx, dy):# return None
        """translate the GF by distance d (d is a pair)"""
        self.operateGeom(Geometry.translate, [dx, dy])


    def rotate(self, centerX, centerY, angle):#  return None
        """rotate the GF by angle degrees using (centerX, centerY) as the center of rotation. angle must be a multiple of 90 degrees"""
        self.operateGeom(Geometry.rotate, [centerX, centerY, angle])
        
    
    def scale(self, centerX, centerY, scaleFactorX, scaleFactorY):#  return None 
        """scale the GF by a factor of scaleFactor using (centerX, centerY) as the center"""
        self.operateGeom(Geometry.scale, [centerX, centerY, scaleFactorX, scaleFactorY])

    
    def getZoom(self):
        """get zoom"""
        return self.zoom

    def setZoom(self, zoom):
        """set zoom and update item"""
        self.zoom = float(zoom)
        if self.canvas != None:
            self.updateView()

    def initZoom(self, zoom):
        """set the zoom without updating the item (used during the initialization of a LeafGF)"""
        self.zoom = float(zoom)

            
    def updateView(self):
        """update the position and look (change width of outline to simulate zoom) of the item on the screen"""
        pass

    def setLock(self, isLocked):
        """set lock to isLocked. If true, any operation has no effect."""
        self.isLocked = isLocked


    def getLock(self): #boolean 
        """get lock. return true iff the GF is in a locked state."""
        return self.isLocked


    def pushToBottom(self): 
        """push the GF under all the other GFs on the canvas"""
        if self.canvas != None:
            self.canvas.lower(self.item)


    def bringToTop(self):
        """bring the GF above all the other GFs on the canvas"""
        if self.canvas != None:
            self.canvas.lift(self.item)

    def getCoords(self):
        """get the coordinates"""
        return self.xy[:]
                  
    def setCoords(self, xy): 
        """set the coordinates"""
        self.xy = xy[:]
        if self.canvas != None:
            args = [self.item]
            args.extend(map(self.multiplyByZoom, self.xy))
            apply(self.canvas.coords, args)


    def multiplyByZoom(self, x_or_y):
        """multiply by the current zoom. Useful for mapping to screen coordinates in PolylineGF and PolygonGF."""
        return x_or_y * self.zoom

    def bindEvents(self):
        """bind events to item"""
        self.canvas.tag_bind(self.item, "<Enter>", self.onEnter)
        self.canvas.tag_bind(self.item, "<Leave>", self.onLeave)
        self.canvas.tag_bind(self.item, "<Button-1>", self.onButton)
        self.canvas.tag_bind(self.item, "<Button-2>", self.onButton)
        self.canvas.tag_bind(self.item, "<Button-3>", self.onButton)
        self.canvas.tag_bind(self.item, "<Shift-Button-1>", self.onShiftButton)
        self.canvas.tag_bind(self.item, "<Shift-Button-2>", self.onShiftButton)
        self.canvas.tag_bind(self.item, "<Shift-Button-3>", self.onShiftButton)
        self.canvas.tag_bind(self.item, "<Shift-Double-Button-1>", self.onShiftButton)
        self.canvas.tag_bind(self.item, "<Shift-Double-Button-2>", self.onShiftButton)
        self.canvas.tag_bind(self.item, "<Shift-Double-Button-3>", self.onShiftButton)
        self.canvas.tag_bind(self.item, "<Double-Button-1>", self.onDoubleButton)
        self.canvas.tag_bind(self.item, "<Double-Button-2>", self.onDoubleButton)
        self.canvas.tag_bind(self.item, "<Double-Button-3>", self.onDoubleButton)
        self.canvas.tag_bind(self.item, "<B1-Motion>", self.onButtonMotion)
        self.canvas.tag_bind(self.item, "<B2-Motion>", self.onButtonMotion)
        self.canvas.tag_bind(self.item, "<B3-Motion>", self.onButtonMotion)
        self.canvas.tag_bind(self.item, "<ButtonRelease-1>", self.onButtonRelease)
        self.canvas.tag_bind(self.item, "<ButtonRelease-2>", self.onButtonRelease)
        self.canvas.tag_bind(self.item, "<ButtonRelease-3>", self.onButtonRelease)

    def onEnter(self, event):
        """mouse cursor enters item"""
        handler = self.getEventHandler()
        if handler != None:
            handler.onGFEnter(self)

    def onLeave(self, event):
        """mouse cursor leaves item"""
        handler = self.getEventHandler()
        if handler != None:
            handler.onGFLeave(self)

    def onButton(self, event): 
        """button event"""
        handler = self.getEventHandler()
        if handler != None:
            handler.onGFButton(self, event)

    def onShiftButton(self, event):
        """button event while holding the Shift key"""
        handler = self.getEventHandler()
        if handler != None:
            handler.onGFShiftButton(self, event)

    def onDoubleButton(self, event):
        """double button event"""
        handler = self.getEventHandler()
        if handler != None:
            handler.onGFDoubleButton(self, event)

    def onShiftDoubleButton(self, event):
        """double button event while holding the Shift key"""
        handler = self.getEventHandler()
        if handler != None:
            handler.onGFShiftDoubleButton(self, event)

    def onButtonMotion(self, event):
        """mouse motion event while button is being pressed"""
        handler = self.getEventHandler()
        if handler != None:
            handler.onGFButtonMotion(self, event)

    def onButtonRelease(self, event):
        """button release event"""
        handler = self.getEventHandler()
        if handler != None:
            handler.onGFButtonRelease(self, event)

    

# leaf class RectangleGF
class Rectangle(LeafGF):
    def __init__(self, x0, y0, x1, y1, canvas=None, outline="black", outlineOption=1, 
                 fill="white", fillOption=1, width=1, stipple="", zoom=1.0, 
                 eventHandler=None, locked=0, savedNumber=None):
        self.xy = [float(x0), float(y0), float(x1), float(y1)]
        self.outline = outline
        self.fill = fill
        self.outlineOption = outlineOption
        self.fillOption = fillOption
        self.width = width
        self.stipple = stipple
        self.isLocked = locked
        self.initZoom(zoom)
        self.canvas = None
        self.setCanvas(canvas)
        self.setEventHandler(eventHandler)
        self.getNewObjectNumber( savedNumber )


    def accept(self, visitor):
        """accept visitor method"""
        visitor.visitRectangle(self)


    def getFillColor(self):#  return color
        """get the fill color of the GF"""
        return self.fill


    def setFillColor(self, color):#  return None
        """set the fill color of the GF"""
        self.fill = color
        if self.canvas != None and self.fillOption:
            self.canvas.itemconfig(self.item, fill=self.fill)

    def getOutlineColor(self):#  return color
        """get the outline color of the GF"""
        return self.outline


    def setOutlineColor(self, color):
        """set the outline color of the GF"""
        self.outline = color
        if self.canvas != None and self.outlineOption:
            self.canvas.itemconfig(self.item, outline=self.outline)


    def getFillOption(self):
        """return 1 iff gf has fill"""
        return self.fillOption


    def getOutlineOption(self):
        """return 1 iff gf has outline"""
        return self.outlineOption


    def setFillOption(self, option):
        """set the fill option of the GF. If option is true, the fill color is used.
        Otherwise, the GF is not filled."""
        self.fillOption = option
        if option:
            itemFill = self.fill
        else:
            itemFill = ""
        if self.canvas != None:
            self.canvas.itemconfig(self.item, fill=itemFill)

        
    def setOutlineOption(self, option):
        """set the outline option of the GF. If option is true, the outline color is used.
        Otherwise, the GF doesn't have an outline."""
        self.outlineOption = option
        if option:
            itemOutline = self.outline
            itemWidth = self.width * self.getZoom()
        else:
            itemOutline = ""
            itemWidth = 0
        if self.canvas != None:
            self.canvas.itemconfig(self.item, outline=itemOutline, width=itemWidth)

    def getWidth(self):
        """get outline width"""
        return self.width

    def setWidth(self, width):
        """set outline width"""
        self.width = width
        if self.canvas != None:
            self.canvas.itemconfig(self.item, width=self.width*self.zoom)

    def getStipple(self):
        return self.stipple

    def setStipple(self, stipple):
        """set the stipple bitmap"""
        self.stipple = stipple
        if self.canvas != None:
            self.canvas.itemconfig(self.item, stipple=self.stipple)


    def setCanvas(self, canvas):
        """set the canvas"""
        if canvas is self.canvas:
            return
        if self.canvas != None:
            self.deleteItem()
            self.canvas = None
        if canvas == None:
            return
        self.canvas = canvas
        self.createItem()

    def createItem(self):
        zoom = self.getZoom()
        if self.fillOption:
            itemFill = self.fill
        else:
            itemFill = ""
        if self.outlineOption:
            itemOutline = self.outline
            itemWidth = self.width * zoom
        else:
            itemOutline = ""
            itemWidth = 0
        self.item = self.canvas.create_rectangle(self.xy[0] * zoom, self.xy[1] * zoom, self.xy[2] * zoom, self.xy[3] * zoom, outline=itemOutline, fill=itemFill, width=itemWidth, stipple=self.stipple)
        self.bindEvents()

    def deleteItem(self):
        self.canvas.delete(self.item)


    def copy(self):
        """return a copy of self"""
        return Rectangle(self.xy[0], self.xy[1], self.xy[2], self.xy[3], canvas=self.canvas, outline=self.outline, outlineOption=self.outlineOption, fill=self.fill, fillOption=self.fillOption, width=self.width, stipple=self.stipple, locked=self.isLocked, zoom=self.getZoom(), eventHandler=self.getEventHandler())

    def updateView(self):
        """update the position of the item on the screen"""
        zoom = self.getZoom()
        self.canvas.coords(self.item, self.xy[0] * zoom, self.xy[1] * zoom, self.xy[2] * zoom, self.xy[3] * zoom)
        if self.outlineOption:
            itemWidth = self.width * zoom
        else:
            itemWidth = 0
        self.canvas.itemconfig(self.item, width=itemWidth)







#leaf class Oval:
class Oval(LeafGF):
    def __init__(self, x0, y0, x1, y1, canvas=None, outline="black", outlineOption=1, 
                 fill="white", fillOption=1, width=1, start=0.0, extent=360.0, 
                 stipple="", zoom=1.0, eventHandler=None, locked=0, savedNumber=None):
        self.xy = [float(x0), float(y0), float(x1), float(y1)]
        self.outline = outline
        self.fill = fill
        self.outlineOption = outlineOption
        self.fillOption = fillOption
        self.width = width
        self.start = start
        self.extent = extent
        self.stipple = stipple
        self.isLocked = locked
        self.initZoom(zoom)
        self.canvas = None
        self.setCanvas(canvas)
        self.setEventHandler(eventHandler)
        self.getNewObjectNumber( savedNumber )


    def accept(self, visitor):
        """accept visitor method"""
        visitor.visitOval(self)


    def getFillColor(self):
        """get the fill color of the GF"""
        return self.fill


    def setFillColor(self, color):
        """set the fill color of the GF"""
        self.fill = color
        if self.canvas != None and self.fillOption:
            self.canvas.itemconfig(self.item, fill=self.fill)


    def getOutlineColor(self):
        """get the outline color of the GF"""
        return self.outline


    def setOutlineColor(self, color):
        """set the outline color of the GF"""
        self.outline = color
        if self.canvas != None and self.outlineOption:
            self.canvas.itemconfig(self.item, outline=self.outline)


    def getFillOption(self):
        """return 1 iff gf has fill"""
        return self.fillOption


    def getOutlineOption(self):
        """return 1 iff gf has outline"""
        return self.outlineOption


    def setFillOption(self, option):
        """set the fill option of the GF. If option is true, the fill color is used.
        Otherwise, the GF is not filled."""
        self.fillOption = option
        if option:
            itemFill = self.fill
        else:
            itemFill = ""
        if self.canvas != None:
            self.canvas.itemconfig(self.item, fill=itemFill)


    def setOutlineOption(self, option):
        """set the outline option of the GF. If option is true, the outline color is used.
        Otherwise, the GF doesn't have an outline."""
        self.outlineOption = option
        if option:
            itemOutline = self.outline
            itemWidth = self.width * self.getZoom()
        else:
            itemOutline = ""
            itemWidth = 0
        if self.canvas != None:
            self.canvas.itemconfig(self.item, outline=itemOutline, width=itemWidth)

        
    def getWidth(self):
        return self.width

    def setWidth(self, width):
        """set the outline width of the GF"""
        self.width = width
        if self.canvas != None:
            self.canvas.itemconfig(self.item, width=self.width*self.zoom)

    def getStipple(self):
        return self.stipple

    def setStipple(self, stipple):
        """set the stipple bitmap"""
        self.stipple = stipple
        if self.canvas != None:
            self.canvas.itemconfig(self.item, stipple=self.stipple)

    def setCanvas(self, canvas):
        """set the canvas"""
        if canvas is self.canvas:
            return
        if self.canvas != None:
            self.deleteItem()
            self.canvas = None
        if canvas == None:
            return
        self.canvas = canvas
        self.createItem()

    def createItem(self):
        zoom = self.getZoom()
        if self.fillOption:
            itemFill = self.fill
        else:
            itemFill = ""
        if self.outlineOption:
            itemOutline = self.outline
            itemWidth = self.width * zoom
        else:
            itemOutline = ""
            itemWidth = 0
        if self.extent % 360 == 0:
            self.item = self.canvas.create_oval(self.xy[0] * zoom, self.xy[1] * zoom, self.xy[2] * zoom, self.xy[3] * zoom, outline=itemOutline, fill=itemFill, width=itemWidth, stipple=self.stipple)
        else:
            self.item = self.canvas.create_arc(self.xy[0] * zoom, self.xy[1] * zoom, self.xy[2] * zoom, self.xy[3] * zoom, outline=itemOutline, fill=itemFill, width=itemWidth, stipple=self.stipple, start=self.start, extent=self.extent)
        self.bindEvents()

    def deleteItem(self):
        self.canvas.delete(self.item)

   
    # set visibility to isVisible and update the item
#    def setVisible(self, isVisible): #None 
#        self.isVisible = isVisible
#        if self.isVisible == 1:
#            self.canvas.itemconfig(self.item, outline=self.outline, fill=self.fill)
#        else:
#            self.canvas.itemconfig(self.item, outline="", fill="")


    def copy(self): 
        """return a copy of self"""
        return Oval(self.xy[0], self.xy[1], self.xy[2], self.xy[3], canvas=self.canvas, outline=self.outline, outlineOption=self.outlineOption, fill=self.fill, fillOption=self.fillOption, width=self.width, stipple=self.stipple, locked=self.isLocked, zoom=self.getZoom(), eventHandler=self.getEventHandler())


    def updateView(self): 
        """update the position of the item on the screen"""
        zoom = self.getZoom()
        self.canvas.coords(self.item, self.xy[0] * zoom, self.xy[1] * zoom, self.xy[2] * zoom, self.xy[3] * zoom)
        if self.outlineOption:
            itemWidth = self.width * zoom
        else:
            itemWidth = 0
        self.canvas.itemconfig(self.item, width=itemWidth)


#class Line
class Line(LeafGF):
    def __init__(self, xy, canvas=None, zoom=1.0, eventHandler=None, locked=0, fill="black", 
                 width=1, stipple="", arrow="none", capstyle="butt", joinstyle="round", 
                 smooth=0, savedNumber=None):
        self.xy = []
        for coord in xy:
            self.xy.append(float(coord))
        self.isLocked = locked
        self.fill = fill
        self.width = width
        self.stipple=stipple
        self.arrow=arrow
        self.capstyle=capstyle
        self.joinstyle=joinstyle
        self.smooth=smooth
        self.initZoom(zoom)
        self.canvas = None
        self.setCanvas(canvas)
        self.setEventHandler(eventHandler)
        self.getNewObjectNumber( savedNumber )


    def accept(self, visitor):
        """accept visitor method"""
        visitor.visitLine(self)


    def getFillColor(self):#  return color 
        """get the fill color of the GF"""
        return self.fill


    def getWidth(self):
        return self.width

    def getStipple(self):
        return self.stipple

    def getArrow(self):
        return self.arrow

    def getCapstyle(self):
        return self.capstyle

    def getJoinstyle(self):
        return self.joinstyle

    def getSmooth(self):
        return self.smooth

    
    def setFillColor(self, color):
        """set the fill color of the GF"""
        self.fill = color
        if self.canvas != None:
            self.canvas.itemconfig(self.item, fill=self.fill)


    def setWidth(self, width):
        """set the line width of the GF"""
        self.width = width
        if self.canvas != None:
            self.canvas.itemconfig(self.item, width=self.width*self.zoom)

    def setStipple(self, stipple):
        """set the stipple bitmap"""
        self.stipple = stipple
        if self.canvas != None:
            self.canvas.itemconfig(self.item, stipple=self.stipple)

    def setArrow(self, arrow):
        """set the arrow option"""
        self.arrow = arrow
        if self.canvas != None:
            self.canvas.itemconfig(self.item, arrow=self.arrow)

    def setCapstyle(self, capstyle):
        """set the cap style"""
        self.capstyle = capstyle
        if self.canvas != None:
            self.canvas.itemconfig(self.item, capstyle=self.capstyle)

    def setJoinstyle(self, joinstyle):
        """set the join style"""
        self.joinstyle = joinstyle
        if self.canvas != None:
            self.canvas.itemconfig(self.item, joinstyle=self.joinstyle)

    def setSmooth(self, smooth):
        """set the boolean smooth"""
        self.smooth = smooth
        if self.canvas != None:
            self.canvas.itemconfig(self.item, smooth=self.smooth)


    def setCanvas(self, canvas):
        """set the canvas"""
        if canvas is self.canvas:
            return
        if self.canvas != None:
            self.deleteItem()
            self.canvas = None
        if canvas == None:
            return
        self.canvas = canvas
        self.createItem()


    def createItem(self):
        zoom = self.getZoom()
        self.item = self.canvas.create_line(map(self.multiplyByZoom, self.xy), fill=self.fill, width=self.width*zoom, stipple=self.stipple, arrow=self.arrow, capstyle=self.capstyle, joinstyle=self.joinstyle, smooth=self.smooth)
        self.bindEvents()


    def deleteItem(self):
        self.canvas.delete(self.item)


    def copy(self): 
        """return a copy of self"""
        return Line(self.xy, canvas=self.canvas, fill=self.fill, width=self.width, locked=self.isLocked, zoom=self.getZoom(), eventHandler=self.getEventHandler(), stipple=self.stipple, arrow=self.arrow, capstyle=self.capstyle, joinstyle=self.joinstyle, smooth=self.smooth)


    def updateView(self):
        """update the position of the item on the screen"""
        zoom = self.getZoom()
        args = [self.item]
        args.extend(map(self.multiplyByZoom, self.xy))
        apply(self.canvas.coords, args)
        self.canvas.itemconfig(self.item, width=self.width*zoom)



#leaf class Polygon
class Polygon(LeafGF):
    def __init__(self, xy, canvas=None, outline="black", outlineOption=1, fill="white", 
                 fillOption=1, width=1, smooth=0, stipple="", zoom=1.0, 
                 eventHandler=None, locked=0, savedNumber=None):
        self.xy = []
        for coord in xy:
            self.xy.append(float(coord))
        self.outline = outline
        self.fill = fill
        self.outlineOption = outlineOption
        self.fillOption = fillOption
        self.width = width
        self.smooth = smooth
        self.stipple = stipple
        self.isLocked = locked
        self.initZoom(zoom)
        self.canvas = None
        self.setCanvas(canvas)
        self.setEventHandler(eventHandler)
        self.getNewObjectNumber( savedNumber )


    def accept(self, visitor): 
        """accept visitor method"""
        visitor.visitPolygon(self)

    def getStipple(self):
        return self.stipple
        
    def getSmooth(self):
        return self.smooth
 
    def getFillColor(self):#  return color
        """get the fill color of the GF"""
        return self.fill


    def getOutlineColor(self):#  return color
        """get the outline color of the GF"""
        return self.outline


    def getFillOption(self):
        """return 1 iff gf has fill"""
        return self.fillOption


    def getOutlineOption(self):
        """return 1 iff gf has outline"""
        return self.outlineOption


    def setStipple(self, stipple):
        """set the stipple bitmap"""
        self.stipple = stipple
        if self.canvas != None:
            self.canvas.itemconfig(self.item, stipple=self.stipple)
    
    def setSmooth(self, smooth):
        self.smooth =smooth


    def setFillColor(self, color):
        """set the fill color of the GF"""
        self.fill = color
        if self.canvas != None and self.fillOption:
            self.canvas.itemconfig(self.item, fill=self.fill)


    def setOutlineColor(self, color):
        """set the outline color of the GF"""
        self.outline = color
        if self.canvas != None and self.outlineOption:
            self.canvas.itemconfig(self.item, outline=self.outline)

    def setFillOption(self, option):
        """set the fill option of the GF. If option is true, the fill color is used.
        Otherwise, the GF is not filled."""
        self.fillOption = option
        if option:
            itemFill = self.fill
        else:
            itemFill = ""
        if self.canvas != None:
            self.canvas.itemconfig(self.item, fill=itemFill)


    def setOutlineOption(self, option):
        """set the outline option of the GF. If option is true, the outline color is used.
        Otherwise, the GF doesn't have an outline."""
        self.outlineOption = option
        if option:
            itemOutline = self.outline
            itemWidth = self.width * self.getZoom()
        else:
            itemOutline = ""
            itemWidth = 0
        if self.canvas != None:
            self.canvas.itemconfig(self.item, outline=itemOutline, width=itemWidth)


    def setWidth(self, width): 
        """set the outline width of the GF"""
        self.width = width
        if self.canvas != None:
            self.canvas.itemconfig(self.item, width=self.width*self.zoom)

    def getWidth(self):
        return self.width

    def setCanvas(self, canvas):
        """set the canvas"""
        if canvas is self.canvas:
            return
        if self.canvas != None:
            self.deleteItem()
            self.canvas = None
        if canvas == None:
            return
        self.canvas = canvas
        self.createItem()

    def createItem(self):
        zoom = self.getZoom()
        if self.fillOption:
            itemFill = self.fill
        else:
            itemFill = ""
        if self.outlineOption:
            itemOutline = self.outline
            itemWidth = self.width * zoom
        else:
            itemOutline = ""
            itemWidth = 0
        self.item = self.canvas.create_polygon(map(self.multiplyByZoom, self.xy), outline=itemOutline, fill=itemFill, width=itemWidth, stipple=self.stipple, smooth=self.smooth)
        self.bindEvents()

    def deleteItem(self):
        self.canvas.delete(self.item)


    def copy(self):
        """return a copy of self"""
        return Polygon(self.xy, canvas=self.canvas, outline=self.outline, outlineOption=self.outlineOption, fill=self.fill, fillOption=self.fillOption, width=self.width, smooth=self.smooth, stipple=self.stipple, locked=self.isLocked, zoom=self.getZoom(), eventHandler=self.getEventHandler())

    def updateView(self):
        """update the position of the item on the screen"""
        zoom = self.getZoom()
        args = [self.item]
        args.extend(map(self.multiplyByZoom, self.xy))
        apply(self.canvas.coords, args)
        if self.outlineOption:
            itemWidth = self.width * zoom
        else:
            itemWidth = 0
        self.canvas.itemconfig(self.item, width=itemWidth)



#leaf class Text.
class Text(LeafGF):
    def __init__(self, x, y, canvas=None, eventHandler=None, zoom=1.0, locked=0, 
                 text="", width=0, fill="black", family="Arial", 
                 size=12, bold=0, italic=0, underline=0, anchor="CENTER", 
                 savedNumber=None):
        self.xy = [float(x), float(y),float(x), float(size)]
        self.isLocked = locked
        self.textCopy = text
        self.fill = fill
        self.family = family
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.anchor = anchor
        self.width = width
        self.initZoom(zoom)
        self.previousZoom = self.getZoom()
        self.canvas = None
        self.setCanvas(canvas)
        self.setEventHandler(eventHandler)
        self.getNewObjectNumber( savedNumber )
        

    def accept(self, visitor):
        """accept visitor method"""
        visitor.visitText(self)
        
    def getFamily(self):
        return self.family

    def getSize(self):
        return self.size

    def getBold(self):
        return self.bold

    def getItalic(self):
        return self.italic

    def getUnderline(self):
        return self.underline

    def getAnchor(self):
        return self.anchor

    def getFillColor(self):#  return color
        """get the fill color of the GF"""
        return self.fill

    def setFamily(self, family):
        self.family = family
        if self.canvas != None:
            self.updateFont()

    def setSize(self, size):
        self.size = size
        if self.canvas != None:
            self.updateFont()

    def setBold(self, bold):
        self.bold = bold
        if self.canvas != None:
            self.updateFont()

    def setItalic(self, italic):
        self.italic = italic
        if self.canvas != None:
            self.updateFont()

    def setUnderline(self, underline):
        self.underline = underline
        if self.canvas != None:
            self.updateFont()


    def setAnchor(self, anchor):
        self.anchor = anchor
        if self.canvas != None:
            self.canvas.itemconfig(self.item, anchor=self.getTkAnchor())


    def updateFont(self):
        
        if self.bold:
            b = "bold"
        else:
            b = "normal"
        if self.italic:
            i = "italic"
        else:
            i = "roman"
        self.font = tkFont.Font(family=self.family, size=int(self.size * self.zoom),
                                 weight=b, slant=i, underline=self.underline)
        self.canvas.itemconfig(self.item, font=self.font)
        
        #self.xy[2] = self.xy[0] + self.font.measure( self.getText() )
        #self.xy[3] = self.xy[1] + self.size * self.zoom 
        #print "Update font", self.xy

    def setFillColor(self, color):
        """set the fill color of the GF"""
        self.fill = color
        if self.canvas != None:
            self.canvas.itemconfig(self.item, fill=self.fill)


    def setCanvas(self, canvas):
        """set the canvas"""
        
        if canvas is self.canvas:
            return
        if self.canvas != None:
            self.deleteItem()
            self.canvas = None
        if canvas == None:
            return
        self.canvas = canvas
        self.createItem()

    def createItem(self):
        zoom = self.getZoom()
        self.item = self.canvas.create_text(self.xy[0] * zoom, self.xy[1] * zoom, width=self.width, text=self.textCopy, fill=self.fill, anchor=self.getTkAnchor())
        self.updateFont()
        self.bindEvents()

    def deleteItem(self):
        self.canvas.delete(self.item)
        self.font = None

    def copy(self):
        """return a copy of self"""
        return Text(self.xy[0], self.xy[1], canvas=self.canvas, eventHandler=self.getEventHandler(), zoom=self.getZoom(), locked=self.isLocked, text=self.getText(), fill=self.fill, family=self.family, size=self.size, bold=self.bold, underline=self.underline, anchor=self.anchor)


    def updateView(self):
        """update the position of the item on the screen"""
        # if zoom has changed, update font. The only reason why updateFont() is not always called is that it takes very long to execute.
        zoom = self.getZoom()
        if self.previousZoom != zoom:
            self.updateFont()
            self.previousZoom = zoom
        self.canvas.coords(self.item, self.xy[0] * zoom, self.xy[1] * zoom)

    def getText(self):
        """ Get text string, may be modified on canvas or by setText """
        if self.canvas != None:
            return self.canvas.itemcget(self.item, "text")
        else:
            return self.textCopy

    def setText(self, text):
        """set text string"""
        self.canvas.itemconfig(self.item, text=text)
        self.textCopy = text 
        #self.xy[2] = self.xy[0] + self.font.measure( text )
        #self.xy[3] = self.xy[1] + self.size * self.zoom 
  

    #todo: really annoying to scale text :p
    def scale(self, centerX, centerY, scaleFactorX, scaleFactorY):
        pass
        #xS = (self.xy[0] - centerX)*scaleFactorX + centerX
        #yS = (self.xy[1] - centerY)*scaleFactorY + centerY
        #print "scale?", xS, yS
        
    def getTkAnchor(self):
        if self.anchor.lower() == "n":
            return Tkinter.N
        elif self.anchor.lower()  == "s":
            return Tkinter.S
        elif self.anchor.lower()  == "e":
            return Tkinter.E
        elif self.anchor.lower()  == "w":
            return Tkinter.W
        elif self.anchor.lower()  == "nw":
            return Tkinter.NW
        elif self.anchor.lower()  == "ne":
            return Tkinter.NE
        elif self.anchor.lower()  == "sw":
            return Tkinter.SW
        elif self.anchor.lower()  == "se":
            return Tkinter.SE
        else:
            return Tkinter.CENTER
          
    def rotate(self, centerX, centerY, angle):
        """ Rotation method override """
        # Set to Horizontal text
        if( self.width ):
            self.width = 0
            self.canvas.itemconfig(self.item, width=0)
        # Set to Vertical text
        else:
            self.width = 1
            self.canvas.itemconfig(self.item, width=1)
            
    def getWidth(self):
        return self.width
        

#leaf class Image.
class Image(LeafGF):
    
    IMAGE_DICT = dict()
  
    def __init__(self, x, y, filename, canvas=None, zoom=1.0, eventHandler=None, 
                 locked=0, anchor="CENTER", savedNumber=None):     
                      
        self.filename = os.path.split( filename )[1] # Drop the path info (if any)
        if( not self.IMAGE_DICT.has_key( self.filename ) ):
          self.IMAGE_DICT[ self.filename ] = self.base64string( filename )
        
        self.xy = [float(x), float(y)]
        self.isLocked = locked
        self.anchor = anchor
        self.initZoom(zoom)
        self.canvas = None
        self.setCanvas(canvas)
        self.setEventHandler(eventHandler)
        self.getNewObjectNumber( savedNumber )
        
    def accept(self, visitor):
        """accept visitor method"""
        visitor.visitImage(self)
              
    def base64string(self, inFile):
        """ Converts a file to base64 string, lifted from img2pytk.py """
        B2AMAXREAD = 45                       #longest line b2a_base64 will take
        f = open(inFile,'rb')
        s = ''
        while 1:
            b = f.read(B2AMAXREAD)
            if not b:
                break
            s += binascii.b2a_base64(b)[0:-1]   #-1 to remove new-line char
        f.close()
        return s
 
    def getFilename( self ):
        return self.filename

    def getAnchor(self):
        return self.anchor

    def setAnchor(self, anchor):
        self.anchor = anchor
        if self.canvas != None:
            self.canvas.itemconfig(self.item, anchor=self.getTkAnchor())

    def setCanvas(self, canvas):
        """set the canvas"""
        if canvas is self.canvas:
            return
        if self.canvas != None:
            self.deleteItem()
            self.canvas = None
        if canvas == None:
            return
        self.canvas = canvas
        self.createItem()

    def createItem(self):
        zoom = self.getZoom()
        #self.photoImage = Tkinter.PhotoImage(file=self.filename)
        self.photoImage = Tkinter.PhotoImage(format='gif', 
                                      data=self.IMAGE_DICT[ self.filename ] )
        self.item = self.canvas.create_image(self.xy[0] * zoom, self.xy[1] * zoom, image=self.photoImage, anchor=self.getTkAnchor())
        self.bindEvents()

    def deleteItem(self):
        self.canvas.delete(self.item)
        self.photoImage = None

    def copy(self):
        """return a copy of self"""
        return Image(self.xy[0], self.xy[1], self.filename, locked=self.isLocked, canvas=self.canvas, zoom=self.getZoom(), eventHandler=self.getEventHandler(), anchor=self.anchor)

    def updateView(self):
        """update the position of the item on the screen"""
        zoom = self.getZoom()
        self.canvas.coords(self.item, self.xy[0] * zoom, self.xy[1] * zoom)

    def getTkAnchor(self):
        if self.anchor == "N":
            return Tkinter.N
        elif self.anchor == "S":
            return Tkinter.S
        elif self.anchor == "E":
            return Tkinter.E
        elif self.anchor == "W":
            return Tkinter.W
        elif self.anchor == "NW":
            return Tkinter.NW
        elif self.anchor == "NE":
            return Tkinter.NE
        elif self.anchor == "SW":
            return Tkinter.SW
        elif self.anchor == "SE":
            return Tkinter.SE
        else:
            return Tkinter.CENTER
          
    def rotate(self, centerX, centerY, angle):
        """ Sorry, please get PIL if you want to do this to images """
        pass

#leaf class Connector:
class Connector(LeafGF):
    def __init__(self, x, y, canvas=None, zoom=1.0, eventHandler=None, locked=0, savedNumber=None):
        self.xy = [float(x), float(y)]
        self.bitmap = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'connector.xbm' ) )
        self.isLocked = locked
        self.initZoom(zoom)
        self.canvas = None
        self.setCanvas(canvas)
        self.setEventHandler(eventHandler)
        self.getNewObjectNumber( savedNumber )

    def accept(self, visitor):
        """accept visitor method"""
        visitor.visitConnector(self)
        
    def setCanvas(self, canvas):
        """set the canvas"""
        if canvas is self.canvas:
            return
        if self.canvas != None:
            self.deleteItem()
            self.canvas = None
        if canvas == None:
            return
        self.canvas = canvas
        self.createItem()

    def createItem(self):
        zoom = self.getZoom()
        self.item = self.canvas.create_bitmap(self.xy[0] * zoom, self.xy[1] * zoom, 
                                              bitmap=self.bitmap )
        self.bindEvents()

    def deleteItem(self):
        self.canvas.delete(self.item)

    def copy(self): #GF
        """return a copy of self"""
        return Connector(self.xy[0], self.xy[1], canvas=self.canvas, zoom=self.getZoom(),
                        eventHandler=self.getEventHandler(), locked=self.isLocked)

    def updateView(self): 
        """update the position of the item on the screen"""
        zoom = self.getZoom()
        self.canvas.coords(self.item, self.xy[0] * zoom, self.xy[1] * zoom)

    def getApproxBoundingBox(self): #  return 4-tuple (int)  
        """get the approximate bounding box of the GF <-- Point object"""
        x, y = self.xy
        zoom = self.getZoom()
        x *= zoom
        y *= zoom        
        return [x,y,x,y]
      
    def rotate(self, centerX, centerY, angle):
        """ Meaningless... """
        pass


#composite class Composite:
class Composite(GF):
    def __init__(self, GFs, canvas=None, locked=0, zoom=1., eventHandler=None):
        self.GFs = GFs #Convention: the first gf in the list is drawn first
        self.zoom = float(zoom)
        self.isLocked = locked

        self.componentsLocked = 0
        for gf in self.GFs:
            if (self.componentsLocked == 1) or (gf.getLock() == 1):
                self.componentsLocked == 1
        if self.componentsLocked == 1:
            self.isLocked = 1
        else:
            self.isLocked = locked
        self.setCanvas(canvas)
        self.setEventHandler(eventHandler)
        for gf in self.GFs:
            gf.setEventHandler(self)
            

    def accept(self, visitor): 
        """accept visitor method"""
        visitor.visitComposite(self)


    def getComponents(self):
        """the method getComponents is mostly useful for visitors"""
        return self.GFs
      
    def getCoords(self):
        """ Hack added by Denis --> Makes life easy for snap grid routine """
        return self.getCoreBox()
      
    def getObjectNumber(self):
        """ Hack added by Denis --> Makes life easy for status update """
        return " group"

    def getApproxBoundingBox(self): #  return 4-tuple (int)
        """get the approximate bounding box of the GF"""
        boxes = []
        for gf in self.GFs:
            if gf.getCanvas() != None:
                boxes.append(gf.getApproxBoundingBox())
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
        return (xMin, yMin, xMax, yMax)


    def getCoreBox(self): #  return 4-tuple
        """get the minimum containing all the points of the GF"""
        boxes = []
        for gf in self.GFs:
            boxes.append(gf.getCoreBox())
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
        return (xMin, yMin, xMax, yMax)


    def translate(self, dx,dy): 
        """translate the GF by (dx, dy)"""
        if self.isLocked == 1:
            return
        for gf in self.GFs:
            gf.translate(dx,dy)


    def rotate(self, centerX, centerY, angle): 
        """rotate the GF by angle degrees using (centerX, centerY) as the center of rotation.
        angle must be a multiple of 90 degrees."""
        if self.isLocked == 1:
            return
        for gf in self.GFs:
            gf.rotate(centerX, centerY, angle)
            
    
    def scale(self, centerX, centerY, scaleFactorX, scaleFactorY):  
        """scale the GF by a factor of scaleFactor using (centerX, centerY) as the center."""
        if self.isLocked == 1:
            return
        for gf in self.GFs:
            gf.scale(centerX, centerY, scaleFactorX, scaleFactorY)
    

    def setZoom(self, zoom):
        """set the zoom and update the item(s)"""
        for gf in self.GFs:
            gf.setZoom(zoom)

    def setCanvas(self, canvas):
        """set the canvas"""
        self.canvas = canvas
        for gf in self.GFs:
            gf.setCanvas(canvas)


    def setLock(self, isLocked):
        """set lock to isLocked. If true, any operation has no effect."""
        if self.componentsLocked == 1:
            return
        self.isLocked = isLocked


    def getLock(self): #boolean 
        """get lock. return true iff the GF is in a locked state."""
        return self.isLocked


    def copy(self):
        """return a copy of self"""
        GFs = []
        for gf in self.GFs:
            GFs.append(gf.copy())
        return Composite(GFs, canvas=self.canvas, locked=self.isLocked, zoom=self.zoom, eventHandler=self.getEventHandler())


    def pushToBottom(self):
        """push the GF under all the other GFs on the canvas. Convention: the first gf in the list is drawn first"""
        self.GFs.reverse()
        for gf in self.GFs:
            gf.pushToBottom()
        self.GFs.reverse()


    def bringToTop(self):
        """bring the GF above all the other GFs on the canvas. Convention: the first gf in the list is drawn first"""
        for gf in self.GFs:
            gf.bringToTop()


    def onGFEnter(self, gf): #called by the components
        """mouse cursor enters component"""
        if self.eventHandler != None:
            self.eventHandler.onGFEnter(self) #call my own event handler


    def onGFLeave(self, gf): #called by the components
        """mouse cursor leaves component"""
        if self.eventHandler != None:
            self.eventHandler.onGFLeave(self) #call my own event handler


    def onGFButton(self, gf, event): #called by the components
        """button event"""
        if self.eventHandler != None:
            self.eventHandler.onGFButton(self, event) #call my own event handler


    def onGFShiftButton(self, gf, event): #called by the components
        """button event while holding the Shift key"""
        if self.eventHandler != None:
            self.eventHandler.onGFShiftButton(self, event) #call my own event handler


    def onGFDoubleButton(self, gf, event): #called by the components
        """double button event"""
        if self.eventHandler != None:
            self.eventHandler.onGFDoubleButton(self, event) #call my own event handler


    def onGFShiftDoubleButton(self, gf, event): #called by the components
        """double button event while holding the Shift key"""
        if self.eventHandler != None:
            self.eventHandler.onGFShiftDoubleButton(self, event) #call my own event handler


    def onGFButtonMotion(self, gf, event): #called by the components
        """mouse motion event while button is being pressed"""
        if self.eventHandler != None:
            self.eventHandler.onGFButtonMotion(self, event) #call my own event handler


    def onGFButtonRelease(self, gf, event): #called by the components
        """button release event"""
        if self.eventHandler != None:
            self.eventHandler.onGFButtonRelease(self, event) #call my own event handler



#leaf class NamedConnector:
class NamedConnector(LeafGF):
    def __init__(self, x, y, canvas=None, zoom=1.0, eventHandler=None, locked=0, name="", savedNumber=None):
        self.xy = [float(x), float(y)]
        self.bitmap = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'namedconnector.xbm' ) )
        self.isLocked = locked
        self.initZoom(zoom)
        self.canvas = None
        self.setCanvas(canvas)
        self.setEventHandler(eventHandler)
        self.name = name
        self.getNewObjectNumber( savedNumber )

    def accept(self, visitor):
        """accept visitor method"""
        visitor.visitNamedConnector(self)
        
    def getName( self ):
        return self.name
    
    def setName( self, name ):
        self.name = name
        
    def setCanvas(self, canvas):
        """set the canvas"""
        if canvas is self.canvas:
            return
        if self.canvas != None:
            self.deleteItem()
            self.canvas = None
        if canvas == None:
            return
        self.canvas = canvas
        self.createItem()

    def createItem(self):
        zoom = self.getZoom()
        self.item = self.canvas.create_bitmap(self.xy[0] * zoom, self.xy[1] * zoom, 
                                              bitmap=self.bitmap )
        self.bindEvents()

    def deleteItem(self):
        self.canvas.delete(self.item)

    def copy(self): #GF
        """return a copy of self"""
        return NamedConnector(self.xy[0], self.xy[1], canvas=self.canvas, zoom=self.getZoom(),
                        eventHandler=self.getEventHandler(), locked=self.isLocked, name =self.name)

    def updateView(self): 
        """update the position of the item on the screen"""
        zoom = self.getZoom()
        self.canvas.coords(self.item, self.xy[0] * zoom, self.xy[1] * zoom)

    def getApproxBoundingBox(self): #  return 4-tuple (int)  
        """get the approximate bounding box of the GF <-- Point object"""
        return self.xy + self.xy
    
    def rotate(self, centerX, centerY, angle):
        """ Meaningless... """
        pass

#leaf class Attribute.
class Attribute(Text):
    def __init__(self, x, y, canvas=None, eventHandler=None, zoom=1.0, locked=0, 
                 text="attribute", fill="black", family="Helvetica", size=12, width=0,
                 bold=0, italic=0, underline=0, anchor="CENTER", savedNumber=None ):
         
        Text.__init__( self, x, y, canvas=canvas, eventHandler=eventHandler, 
                      zoom=zoom, locked=locked, text=text, fill=fill, width=width,
                      family=family, size=size, bold=bold, italic=italic, 
                      underline=underline, anchor=anchor, savedNumber=savedNumber )
    
    def accept(self, visitor):
        """accept visitor method"""
        visitor.visitAttribute(self)

    def createItem(self):
        zoom = self.getZoom()
        self.item = self.canvas.create_text(self.xy[0] * zoom, self.xy[1] * zoom, text='< '+self.textCopy+' >',
                                            fill=self.fill, anchor=self.getTkAnchor(), width=self.width  )
        self.updateFont()
        self.bindEvents()

    def getText(self):
        """ Get text string, this string is modified only by setText """
        return self.textCopy
  
    def setText(self, text):
        """set text string"""
        self.canvas.itemconfig(self.item, text='< '+text+' >')
        self.textCopy = text 


