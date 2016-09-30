from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Operator_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 40, 36
        graphEntity.__init__(self, x, y)
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_polygon(self.translate([13.0, 3.0, 28.0, 3.0, 35.0, 18.0, 28.0, 33.0, 13.0, 33.0, 6.0, 18.0]), tags = self.tag, fill= 'lightgreen', outline= 'black', smooth= 0, splinesteps= '12', width= '1.0', stipple= '')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)
        h = drawing.create_oval(self.translate([20.0, 33.0, 20.0, 33.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([20.0, 3.0, 20.0, 3.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([35.0, 18.0, 35.0, 18.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([6.0, 18.0, 6.0, 18.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        if self.semanticObject: drawText = self.semanticObject.type.toString(25,5)
        else: drawText = "<type>"
        h = drawing.create_text(self.translate([20.0, 18.0]), tags = self.tag, text = drawText, fill= 'blue', anchor= 'center', font= 'Helvetica -12', justify= 'left', width= '0', stipple= '')
        self.attr_display["type"] = h
        self.gf2 = GraphicalForm(drawing, h, "gf2")
        self.graphForms.append(self.gf2)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_Operator_Center
