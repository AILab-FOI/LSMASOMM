from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_LeafType(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 107, 39
        graphEntity.__init__(self, x, y)
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([3.0, 3.0, 103.0, 36.0]), tags = self.tag, fill= 'lightyellow', outline= 'black', width= '1.0', stipple= '')
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)
        h = drawing.create_oval(self.translate([53.0, 3.0, 53.0, 3.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([53.0, 36.0, 53.0, 36.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([104.0, 20.0, 104.0, 20.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([3.0, 21.0, 3.0, 21.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        if self.semanticObject: drawText = self.semanticObject.Type.toString(25,5)
        else: drawText = "<Type>"
        h = drawing.create_text(self.translate([52.0, 18.0]), tags = self.tag, text = drawText, fill= 'blue', anchor= 'center', font= 'Helvetica -12', justify= 'left', width= '0', stipple= '')
        self.attr_display["Type"] = h
        self.gf2 = GraphicalForm(drawing, h, "gf2")
        self.graphForms.append(self.gf2)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_LeafType
