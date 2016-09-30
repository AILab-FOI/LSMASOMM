# Workspace.py
# Francois Plamondon
# Summer 2003


import Tkinter

class Workspace:
    def __init__(self, editor, width, height, canvasWidth, canvasHeight, 
                 eventHandler, zoom):
        masterFrame = editor.root
        self.editor = editor
                  
        #frame containing the canvas and the scrollbars
        self.frame = Tkinter.Frame(masterFrame)
        #width of the total workspace
        self.width = width
        #height of the total workspace
        self.height = height
        #current width of the canvas
        self.canvasWidth = canvasWidth
        #current height of the canvas
        self.canvasHeight = canvasHeight
        #event handler to send events to. This is a reference to the main event handler.
        self.eventHandler = eventHandler
        #initial zoom
        self.zoom = float(zoom)
        #horizontal scrollbar
        self.xScrollbar = Tkinter.Scrollbar(self.frame, orient=Tkinter.HORIZONTAL)
        self.xScrollbar.pack(side=Tkinter.BOTTOM, fill=Tkinter.X)
        #vertical scrollbar
        self.yScrollbar = Tkinter.Scrollbar(self.frame, orient=Tkinter.VERTICAL)
        self.yScrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)
        #canvas
        self.bd = 2 # borderwidth
        self.canvas = Tkinter.Canvas(self.frame, height=self.canvasHeight, 
                                     width=self.canvasWidth, bg="white", 
                                     borderwidth=self.bd, relief=Tkinter.SUNKEN, 
                                     yscrollcommand=self.setYScrollbar, 
                                     xscrollcommand=self.setXScrollbar, 
                                     scrollregion=( editor.CANVAS_SIZE_TUPLE[0]*self.zoom,
                                                   editor.CANVAS_SIZE_TUPLE[1]*self.zoom, 
                                                   width*self.zoom, 
                                                   height*self.zoom))
        #bind canvas events
        self.canvas.bind("<Button-1>", self.onButton)
        self.canvas.bind("<Button-2>", self.onButton)
        self.canvas.bind("<Button-3>", self.onButton)
        self.canvas.bind("<Double-Button-1>", self.onDoubleButton)
        self.canvas.bind("<Double-Button-2>", self.onDoubleButton)
        self.canvas.bind("<Double-Button-3>", self.onDoubleButton)
        self.canvas.bind("<Motion>", self.onMotion)
        self.canvas.bind("<Shift-Motion>", self.onShiftMotion)
        self.canvas.bind("<B1-Motion>", self.onButtonMotion)
        self.canvas.bind("<B2-Motion>", self.onButtonMotion)
        self.canvas.bind("<B3-Motion>", self.onButtonMotion)
        self.canvas.bind("<Shift-B1-Motion>", self.onShiftButtonMotion)
        self.canvas.bind("<Shift-B2-Motion>", self.onShiftButtonMotion)
        self.canvas.bind("<Shift-B3-Motion>", self.onShiftButtonMotion)
        self.canvas.bind("<ButtonRelease-1>", self.onButtonRelease)
        self.canvas.bind("<ButtonRelease-2>", self.onButtonRelease)
        self.canvas.bind("<ButtonRelease-3>", self.onButtonRelease)
        #make the canvas resizable
        self.canvas.pack(side=Tkinter.RIGHT, fill=Tkinter.BOTH, expand=1)
        self.canvas.focus_set() # focus on canvas
        self.yScrollbar.config(command=self.canvas.yview)
        self.xScrollbar.config(command=self.canvas.xview)
        self.x0 = 0
        self.y0 = 0
        #make the workspace resizable
        self.frame.pack(side=Tkinter.RIGHT, fill=Tkinter.BOTH, expand=1)

    # set the scrollbar and update y0 at the same time so that it doesn't need to
    # be updated each time an event occurs.
    def setXScrollbar(self, *args):
        apply(self.xScrollbar.set, args)
        low, hi = self.xScrollbar.get()
        #Because of the borderwidth, need to adjust the position to reflect the
        # real position of the cursor for both x0 and y0.
        self.x0 = low * self.width * self.zoom - self.bd - 1
        self.canvasWidth = (hi - low) * self.width * self.zoom

    # set the scrollbar and update y0
    def setYScrollbar(self, *args):
        apply(self.yScrollbar.set, args)
        low, hi = self.yScrollbar.get()
        self.y0 = low * self.height * self.zoom  - self.bd - 1
        self.canvasHeight = (hi - low) * self.height * self.zoom

    def getCanvas(self):
        return self.canvas

    def getCanvasWidth(self):
        return self.canvasWidth

    def getCanvasHeight(self):
        return self.canvasHeight

    def getZoom(self):
        return self.zoom

    def setZoom(self, zoom, x, y):
        offsetX = x/(self.width * self.zoom) #offsetX = relative position of cursor on workspace
        offsetY = y/(self.height * self.zoom)
        self.zoom = float(zoom)
        # change zoom, i.e. the size of the workspace
        self.canvas.config(scrollregion=(self.editor.CANVAS_SIZE_TUPLE[0]*self.zoom, 
                                         self.editor.CANVAS_SIZE_TUPLE[1]*self.zoom, 
                                         self.width * self.zoom, self.height * self.zoom))
        # calculate the percentage of the workspace occupied by half of the canvas
        halfCanvasX = (self.canvasWidth/(self.width * self.zoom))/2
        halfCanvasY = (self.canvasHeight/(self.height * self.zoom))/2
        #the offset for the upper left corner is the offset of the center minus halfCanvas
        offsetX = offsetX - halfCanvasX
        offsetY = offsetY - halfCanvasY
        self.canvas.xview(Tkinter.MOVETO, offsetX)
        self.canvas.yview(Tkinter.MOVETO, offsetY)


    def onButton(self, event):
        event.x += self.x0
        event.y += self.y0
        self.eventHandler.onCanvasButton(event)


    def onDoubleButton(self, event):
        event.x += self.x0
        event.y += self.y0
        self.eventHandler.onCanvasDoubleButton(event)


    def onMotion(self, event):
        event.x += self.x0
        event.y += self.y0
        self.eventHandler.onCanvasMotion(event)


    def onShiftMotion(self, event):
        event.x += self.x0
        event.y += self.y0
        self.eventHandler.onCanvasShiftMotion(event)


    def onButtonMotion(self, event):
        event.x += self.x0
        event.y += self.y0
        self.eventHandler.onCanvasButtonMotion(event)


    def onShiftButtonMotion(self, event):
        event.x += self.x0
        event.y += self.y0
        self.eventHandler.onCanvasShiftButtonMotion(event)


    def onButtonRelease(self, event):
        event.x += self.x0
        event.y += self.y0
        self.eventHandler.onCanvasButtonRelease(event)
        