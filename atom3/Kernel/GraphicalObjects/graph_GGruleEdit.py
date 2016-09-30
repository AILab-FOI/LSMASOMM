from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_GGruleEdit(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        graphEntity.__init__(self, x, y)
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing):
        self.dc = drawing
        h = drawing.create_oval(self.translate([19.0, 4.0, 107.0, 94.0]), tags = self.tag, fill = "", outline = "black")
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)
        h = drawing.create_rectangle(self.translate([1.0, 1.0, 118.0, 98.0]), tags = self.tag, fill = "", outline = "black")
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_GGruleEdit
