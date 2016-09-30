from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_TypeName(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 80, 37
        graphEntity.__init__(self, x, y)
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_rectangle(self.translate([2.0, 3.0, 76.0, 34.0]), tags = self.tag, fill= 'pink', outline= 'black', width= '1.0', stipple= '')
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)
        h = drawing.create_oval(self.translate([39.0, 3.0, 39.0, 3.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([39.0, 34.0, 39.0, 34.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([77.0, 18.0, 77.0, 18.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([3.0, 18.0, 3.0, 18.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        if self.semanticObject: drawText = self.semanticObject.Name.toString(25,5)
        else: drawText = "<Name>"
        h = drawing.create_text(self.translate([39.0, 19.0]), tags = self.tag, text = drawText, fill= 'blue', anchor= 'center', font= 'Helvetica -12', justify= 'left', width= '0', stipple= '')
        self.attr_display["Name"] = h
        self.gf2 = GraphicalForm(drawing, h, "gf2")
        self.graphForms.append(self.gf2)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_TypeName
