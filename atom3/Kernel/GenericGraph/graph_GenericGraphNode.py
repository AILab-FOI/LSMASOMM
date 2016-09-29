from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_GenericGraphNode(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 22, 18
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_rectangle(self.translate([1.0, 1.0, 17.0, 15.0]), tags = self.tag, stipple= '', width= '1.0', outline= 'black', fill= 'purple')
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)
        h = drawing.create_oval(self.translate([9.0, 8.0, 9.0, 8.0]), tags = (self.tag, "connector"), stipple= '', width= '1.0', outline= 'black', fill= 'red')
        self.connectors.append(h)


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_GenericGraphNode
