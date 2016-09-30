from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_ButtonConfig(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 111, 56
        graphEntity.__init__(self, x, y)
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_rectangle(self.translate([2.0, 1.0, 103.0, 43.0]), tags = self.tag, fill= 'gray', outline= 'black', width= '1.0', stipple= 'gray75')
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)
        h = drawing.create_line(self.translate([7.0, 49.0, 109.0, 49.0, 109.0, 7.0, 104.0, 2.0]), tags = self.tag, fill= 'black', joinstyle= 'round', smooth= 0, capstyle= 'butt', arrow= 'none', arrowshape= '8 10 3', splinesteps= '12', width= '1.0', stipple= '')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)
        h = drawing.create_line(self.translate([6.0, 49.0, 2.0, 44.0]), tags = self.tag, fill= 'black', joinstyle= 'round', smooth= 0, capstyle= 'butt', arrow= 'none', arrowshape= '8 10 3', splinesteps= '12', width= '1.0', stipple= '')
        self.gf2 = GraphicalForm(drawing, h, "gf2")
        self.graphForms.append(self.gf2)
        if self.semanticObject: drawText = self.semanticObject.Contents.toString(25,5)
        else: drawText = "<Contents>"
        h = drawing.create_text(self.translate([51.0, 21.0]), tags = self.tag, text = drawText, fill= 'red', anchor= 'center', font= 'Helvetica -14', justify= 'left', width= '0', stipple= '')
        self.attr_display["Contents"] = h
        self.gf4 = GraphicalForm(drawing, h, "gf4")
        self.graphForms.append(self.gf4)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_ButtonConfig
