from graphEntity     import *
from ATOM3Constraint import *
from GraphicalForm   import *

class graph_ExternalConnection(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        graphEntity.__init__(self, x, y)
        self.graphForms = []

    def DrawObject(self, drawing):
        self.dc = drawing
        h = drawing.create_line(self.translate([2.0, 3.0, 2.0, 70.0, 106.0, 70.0, 106.0, 13.0, 106.0, 13.0]), tags = self.tag, fill = "black")
        self.gf0 = GraphicalForm( drawing, h, "gf0")
        self.graphForms.append(self.gf0)

        h = drawing.create_line(self.translate([2.0, 3.0, 94.0, 3.0, 106.0, 14.0, 88.0, 20.0, 94.0, 3.0]), tags = self.tag, fill = "black")
        self.gf1 = GraphicalForm( drawing, h, "gf1")
        self.graphForms.append(self.gf1)

        h = drawing.create_oval(self.translate([15.0, 21.0, 33.0, 43.0]), tags = self.tag, fill = "", outline = "black")
        self.gf2 = GraphicalForm( drawing, h, "gf2")
        self.graphForms.append(self.gf2)

        h = drawing.create_oval(self.translate([53.0, 36.0, 70.0, 58.0]), tags = self.tag, fill = "", outline = "black")
        self.gf3 = GraphicalForm( drawing, h, "gf3")
        self.graphForms.append(self.gf3)

        h = drawing.create_oval(self.translate([46.0, 11.0, 62.0, 30.0]), tags = self.tag, fill = "", outline = "black")
        self.gf4 = GraphicalForm( drawing, h, "gf4")
        self.graphForms.append(self.gf4)

        h = drawing.create_line(self.translate([32.0, 25.0, 46.0, 22.0]), tags = self.tag, fill = "black")
        self.gf5 = GraphicalForm( drawing, h, "gf5")
        self.graphForms.append(self.gf5)

        h = drawing.create_line(self.translate([56.0, 29.0, 59.0, 35.0]), tags = self.tag, fill = "black")
        self.gf6 = GraphicalForm( drawing, h, "gf6")
        self.graphForms.append(self.gf6)

        h = drawing.create_line(self.translate([32.0, 38.0, 54.0, 44.0]), tags = self.tag, fill = "black")
        self.gf7 = GraphicalForm( drawing, h, "gf7")
        self.graphForms.append(self.gf7)

        h = drawing.create_line(self.translate([75.0, 26.0, 98.0, 26.0]), tags = self.tag, fill = "black")
        self.gf8 = GraphicalForm( drawing, h, "gf8")
        self.graphForms.append(self.gf8)

        h = drawing.create_line(self.translate([74.0, 34.0, 98.0, 34.0]), tags = self.tag, fill = "black")
        self.gf9 = GraphicalForm( drawing, h, "gf9")
        self.graphForms.append(self.gf9)

        h = drawing.create_line(self.translate([74.0, 41.0, 97.0, 41.0]), tags = self.tag, fill = "black")
        self.gf10 = GraphicalForm( drawing, h, "gf10")
        self.graphForms.append(self.gf10)

        h = drawing.create_text(self.translate([55.0, 64.0]), tags = self.tag, text = "Ext. connection", fill = "black")
        self.gf11 = GraphicalForm( drawing, h, "gf11")
        self.graphForms.append(self.gf11)

        h = drawing.create_oval(self.translate([52.0, 72.0, 52.0, 72.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([3.0, 37.0, 3.0, 37.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([51.0, 3.0, 51.0, 3.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([107.0, 40.0, 107.0, 40.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([3.0, 71.0, 3.0, 71.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([3.0, 5.0, 3.0, 5.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([96.0, 5.0, 96.0, 5.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([107.0, 15.0, 107.0, 15.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([107.0, 71.0, 107.0, 71.0]), tags = self.tag, fill = "red", outline = "black")
        self.connectors.append(h)

new_class = graph_ExternalConnection
