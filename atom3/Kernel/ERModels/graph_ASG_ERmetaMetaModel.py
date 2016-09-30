from graphEntity     import *
from ATOM3Constraint import *
from GraphicalForm   import *

class graph_ASG_ERmetaMetaModel(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        graphEntity.__init__(self, x, y)
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_rectangle(self.translate([2.0, 3.0, 132.0, 92.0]), tags = self.tag, fill = "", outline = "black")
        self.gf0 = GraphicalForm( drawing, h, "gf0")
        self.graphForms.append(self.gf0)

        h = drawing.create_rectangle(self.translate([6.0, 8.0, 74.0, 29.0]), tags = self.tag, fill = "", outline = "black")
        self.gf1 = GraphicalForm( drawing, h, "gf1")
        self.graphForms.append(self.gf1)

        h = drawing.create_line(self.translate([131.0, 92.0, 164.0, 13.0, 132.0, 13.0]), tags = self.tag, fill = "black")
        self.gf2 = GraphicalForm( drawing, h, "gf2")
        self.graphForms.append(self.gf2)

        h = drawing.create_line(self.translate([132.0, 73.0, 154.0, 18.0, 132.0, 18.0]), tags = self.tag, fill = "black")
        self.gf3 = GraphicalForm( drawing, h, "gf3")
        self.graphForms.append(self.gf3)

        h = drawing.create_line(self.translate([132.0, 24.0, 139.0, 24.0, 132.0, 47.0]), tags = self.tag, fill = "black")
        self.gf4 = GraphicalForm( drawing, h, "gf4")
        self.graphForms.append(self.gf4)

        h = drawing.create_oval(self.translate([3.0, 45.0, 3.0, 45.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([65.0, 93.0, 65.0, 93.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([65.0, 3.0, 65.0, 3.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([147.0, 55.0, 147.0, 55.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([3.0, 93.0, 3.0, 93.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([132.0, 93.0, 132.0, 93.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([132.0, 3.0, 132.0, 3.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([3.0, 3.0, 3.0, 3.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([165.0, 15.0, 165.0, 15.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        if self.semanticObject.keyword_:
           if self.semanticObject: drawText = self.semanticObject.keyword_.toString(25,5)
        else: drawText = "<name>"
        h = drawing.create_text(self.translate([8.0, 12.0]), tags = self.tag, text = drawText, fill = "blue", anchor = "nw")
        self.attr_display["name"] = h
        self.gf5 = GraphicalForm( drawing, h, "gf5")
        self.graphForms.append(self.gf5)

    def evaluateGraphConstraints(self):
       pass

new_class = graph_ASG_ERmetaMetaModel

