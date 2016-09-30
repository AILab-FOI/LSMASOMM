from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_image(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 42, 44
        graphEntity.__init__(self, x, y)
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        try:
          self.image_gf0 = PhotoImage(file='genOOCSMP.gif')
          h = drawing.create_image(self.translate([1.0, 1.0]), tags = self.tag, image=self.image_gf0 )
          self.gf0 = GraphicalForm(drawing, h, "gf0")
          self.graphForms.append(self.gf0)
        except:
          pass


    def postCondition (self, actionID, * params):
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_image
