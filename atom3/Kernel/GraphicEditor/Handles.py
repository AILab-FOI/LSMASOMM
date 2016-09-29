# Handles.py
# Francois Plamondon
# Summer 2003


import Tkinter
# class HandleSet:
# A handle set is made of 8 handles which are placed around a box given as argument. The
# box can be set with the "set" method. A handle in a handle set is named according to its relative
# position in the set:
#
#    "x0y0"......"x01y0"......."x1y0"
#       .                        .
#       .                        . 
#    "x0y01"                   "x1y01"
#       .                        .
#       .                        .
#    "x0y1"......"x01y1"......."x1y1"

class HandleSet:
    def __init__(self, x0, y0, x1, y1, isActive, canvas, eventHandler): 
        # x0,y0,x1,y1: box
        # isActive: boolean
        # canvas: Tkinter Canvas
        # eventHandler: The eventHandler must implement the following methods:
        #     onHandleSetButton(self, handleName, event)
        #     onHandleSetButtonMotion(self, handleName, event)
        #     onHandleSetShiftButtonMotion(self, handleName, event)
        #     onHandleSetButtonRelease(self, handleName, event)
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.space = 0  # distance from box
        self.canvas = canvas
        self.eventHandler = eventHandler
        self.handles = []
        self.handles.append(Handle(self.x0 - self.space, self.y0 - self.space, "x0y0", isActive, self.canvas, self))
        self.handles.append(Handle(self.x1 + self.space, self.y0 - self.space, "x1y0", isActive, self.canvas, self))
        self.handles.append(Handle(self.x0 - self.space, self.y1 + self.space, "x0y1", isActive, self.canvas, self))
        self.handles.append(Handle(self.x1 + self.space, self.y1 + self.space, "x1y1", isActive, self.canvas, self))
        self.handles.append(Handle((self.x0 + self.x1)/2, self.y0 - self.space, "x01y0", isActive, self.canvas, self))
        self.handles.append(Handle((self.x0 + self.x1)/2, self.y1 + self.space, "x01y1", isActive, self.canvas, self))
        self.handles.append(Handle(self.x1 + self.space, (self.y0 + self.y1)/2, "x1y01", isActive, self.canvas, self))
        self.handles.append(Handle(self.x0 - self.space, (self.y0 + self.y1)/2, "x0y01", isActive, self.canvas, self))

    def set(self, x0, y0, x1, y1):
        """place the handle set around a new box"""
        self.x0 = x0
        self.y0 = y0
        self.x1 = x1
        self.y1 = y1
        self.update()

#    def setRelative(self, dx0, dy0, dx1, dy1):
#        self.x0 += dx0
#        self.y0 += dy0
#        self.x1 += dx1
#        self.y1 += dy1
#        self.update()

    def update(self):
        """update the position of the handles around the box (self.x0, self.y0, self.x1, self.y1)"""
        self.handles[0].set(self.x0 - self.space, self.y0 - self.space)
        self.handles[1].set(self.x1 + self.space, self.y0 - self.space)
        self.handles[2].set(self.x0 - self.space, self.y1 + self.space)
        self.handles[3].set(self.x1 + self.space, self.y1 + self.space)
        self.handles[4].set((self.x0 + self.x1)/2, self.y0 - self.space)
        self.handles[5].set((self.x0 + self.x1)/2, self.y1 + self.space)
        self.handles[6].set(self.x1 + self.space, (self.y0 + self.y1)/2)
        self.handles[7].set(self.x0 - self.space, (self.y0 + self.y1)/2)

    def activate(self):
        """activate the handles"""
        for h in self.handles:
            h.activate()

    def deactivate(self):
        """deactivate the handles"""
        for h in self.handles:
            h.deactivate()

    def onHandleButton(self, handleName, event):
        """handle button event"""
        self.eventHandler.onHandleSetButton(self, handleName, event)

    def onHandleButtonMotion(self, handleName, event):
        """handle button motion event"""
        self.eventHandler.onHandleSetButtonMotion(self, handleName, event)

    def onHandleShiftButtonMotion(self, handleName, event):
        """handle button motion event while holding the shift key"""
        self.eventHandler.onHandleSetShiftButtonMotion(self, handleName, event)

    def onHandleButtonRelease(self, handleName, event):
        """handle button release"""
        self.eventHandler.onHandleSetButtonRelease(self, handleName, event)

    def bringToTop(self):
        """bring handle set on top of the other items on the canvas"""
        for h in self.handles:
            h.bringToTop()

    def pushToBottom(self):
        """push the handle set under the other items on the canvas"""
        for h in self.handles:
            h.pushToBottom()


# class Handle. Handles can be used as a GUI tool.
# For example, the user can grab a handle and scale objects or move points.
class Handle:
    def __init__(self, x, y, name, isActive, canvas, eventHandler):
        # x, y: position on the canvas
        # isActive: boolean
        # canvas: Tkinter Canvas
        # eventHandler: The event handler must implement the following methods:
        #    onHandleButton(self.name, event)
        #    onHandleButtonMotion(self.name, event)
        #    onHandleShiftButtonMotion(self.name, event)
        #    onHandleButtonRelease(self.name, event)
        self.size = 6
        self.fill = "white"
        self.outline = "black"
        self.name = name
        self.canvas = canvas
        self.eventHandler = eventHandler
        self.x = x
        self.y = y
        self.isActive = 0
        if isActive == 1:
            self.activate()

    def activate(self):
        """create a square on the canvas representing the handle"""
        if self.isActive == 1:
            return
        s = self.size / 2
        coords = [self.x - s, self.y - s, 
                  self.x + s, self.y + s] 
        self.item = self.canvas.create_rectangle(coords, fill=self.fill, outline=self.outline, width=1)
        self.bindEvents()
        self.isActive = 1

    def bindEvents(self):
        """bind item events to the corresponding methods""" 
        self.canvas.tag_bind(self.item, "<Button-1>", self.onButton)
        self.canvas.tag_bind(self.item, "<Button-2>", self.onButton)
        self.canvas.tag_bind(self.item, "<Button-3>", self.onButton)
        self.canvas.tag_bind(self.item, "<B1-Motion>", self.onButtonMotion)
        self.canvas.tag_bind(self.item, "<B2-Motion>", self.onButtonMotion)
        self.canvas.tag_bind(self.item, "<B3-Motion>", self.onButtonMotion)
        self.canvas.tag_bind(self.item, "<Shift-B1-Motion>", self.onShiftButtonMotion)
        self.canvas.tag_bind(self.item, "<Shift-B2-Motion>", self.onShiftButtonMotion)
        self.canvas.tag_bind(self.item, "<Shift-B3-Motion>", self.onShiftButtonMotion)
        self.canvas.tag_bind(self.item, "<ButtonRelease-1>", self.onButtonRelease)
        self.canvas.tag_bind(self.item, "<ButtonRelease-2>", self.onButtonRelease)
        self.canvas.tag_bind(self.item, "<ButtonRelease-3>", self.onButtonRelease)
        
    def onButton(self, event):
        """button pressed event"""
        self.eventHandler.onHandleButton(self.name, event)

    def onButtonMotion(self, event):
        """button motion event"""
        self.eventHandler.onHandleButtonMotion(self.name, event)

    def onShiftButtonMotion(self, event):
        """button motion event while holding the shift key"""
        self.eventHandler.onHandleShiftButtonMotion(self.name, event)

    def onButtonRelease(self, event):
        """button release event"""
        self.eventHandler.onHandleButtonRelease(self.name, event)

    def deactivate(self):
        """delete the handle's item"""
        if self.isActive == 0:
            return
        self.canvas.delete(self.item)
        self.isActive = 0

    def setVisible(self, isVisible):
        """When speed is needed, instead of being deactivated, a handle can be made invisible.
        Warning: an invisible handle is still on the canvas and will therefore continue
        to recognize events."""
        if isVisible:
            self.canvas.itemconfig(self.item, fill=self.fill, outline=self.outline)
        else:
            self.canvas.itemconfig(self.item, fill = "", outline="")

    def set(self, x, y):
        """set the position of the handle on the canvas"""
        self.x = x
        self.y = y
        #update item if active
        if self.isActive == 1:
            self.canvas.coords(self.item, x - self.size/2, y - self.size/2, x + self.size/2, y + self.size/2)

    def translate(self, dx, dy):
        """translate the handle by (dx,dy)"""
        self.x += dx
        self.y += dy
        #update item if active
        if self.isActive == 1: 
            self.canvas.coords(self.item, self.x - self.size/2, self.y - self.size/2, self.x + self.size/2, self.y + self.size/2)

    def bringToTop(self):
        """bring handle's item on top of the other items on the canvas (if active)"""
        if self.isActive == 1:
            self.canvas.lift(self.item)

    def pushToBottom(self):
        """push the handle's item under the other items on the canvas (if active)"""
        if self.isActive == 1:
            self.canvas.lower(self.item)

