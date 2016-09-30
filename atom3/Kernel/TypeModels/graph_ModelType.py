from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_ModelType(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 111, 57
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_rectangle(self.translate([3.0, 14.0, 86.0, 54.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'lightgreen', fill= 'lightgreen')
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)
        h = drawing.create_rectangle(self.translate([7.0, 9.0, 90.0, 49.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'lightblue', fill= 'lightblue')
        self.gf4 = GraphicalForm(drawing, h, "gf4")
        self.graphForms.append(self.gf4)
        h = drawing.create_rectangle(self.translate([14.0, 2.0, 94.0, 40.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'blue', fill= 'blue')
        self.gf5 = GraphicalForm(drawing, h, "gf5")
        self.graphForms.append(self.gf5)
        h = drawing.create_oval(self.translate([3.0, 23.0, 3.0, 23.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([45.0, 54.0, 45.0, 54.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([95.0, 21.0, 95.0, 21.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([47.0, 3.0, 47.0, 3.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)
        if self.semanticObject: drawText = self.semanticObject.Name.toString(25,5)
        else: drawText = "<Name>"
        h = drawing.create_text(self.translate([19.0, 6.0]), tags = self.tag, text = drawText, stipple= '', width= '0', fill= 'lightgreen', font= '{MS Sans Serif} 9', anchor= 'nw', justify= 'left')
        self.attr_display["Name"] = h
        self.gf9 = GraphicalForm(drawing, h, "gf9")
        self.graphForms.append(self.gf9)
        if self.semanticObject: drawText = self.semanticObject.MetaModelName.toString(25,5)
        else: drawText = "<MetaModelName>"
        h = drawing.create_text(self.translate([17.0, 19.0]), tags = self.tag, text = drawText, stipple= '', width= '0', fill= 'lightblue', font= '{MS Sans Serif} 9', anchor= 'nw', justify= 'left')
        self.attr_display["MetaModelName"] = h
        self.gf8 = GraphicalForm(drawing, h, "gf8")
        self.graphForms.append(self.gf8)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_ModelType
