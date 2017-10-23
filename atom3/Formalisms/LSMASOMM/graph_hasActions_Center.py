"""
__graph_hasActions_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_______________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_hasActions_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 27, 29
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        self.graphForms = []
        self.imageDict = self.getImageDict()

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([-10.777777777777374, -10.66666666666714, 11.333333333331666, 11.444444444444116]), tags = self.tag, stipple = '', width = 2, outline = 'black', fill = 'gray')
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)

        h = drawing.create_oval(self.translate([-4.111111111110404, -14.0, 4.888888888888459, -5.000000000000568]), tags = self.tag, stipple = '', width = 1, outline = '', fill = 'grey45')
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)

        h = drawing.create_oval(self.translate([-13.0, -8.999999999999886, -4.0, 4.831690603168681e-13]), tags = self.tag, stipple = '', width = 1, outline = '', fill = 'grey45')
        self.gf5 = GraphicalForm(drawing, h, "gf5")
        self.graphForms.append(self.gf5)

        h = drawing.create_oval(self.translate([4.7777777777777715, 0.9999999999996021, 13.777777777777601, 9.99999999999946]), tags = self.tag, stipple = '', width = 1, outline = '', fill = 'grey45')
        self.gf6 = GraphicalForm(drawing, h, "gf6")
        self.graphForms.append(self.gf6)

        h = drawing.create_oval(self.translate([-4.111111111110404, 5.999999999999716, 4.888888888888459, 15.0]), tags = self.tag, stipple = '', width = 1, outline = '', fill = 'grey45')
        self.gf7 = GraphicalForm(drawing, h, "gf7")
        self.graphForms.append(self.gf7)

        h = drawing.create_oval(self.translate([4.7777777777777715, -8.999999999999886, 13.777777777777601, 4.831690603168681e-13]), tags = self.tag, stipple = '', width = 1, outline = '', fill = 'grey45')
        self.gf8 = GraphicalForm(drawing, h, "gf8")
        self.graphForms.append(self.gf8)

        h = drawing.create_oval(self.translate([-13.0, 0.9999999999996021, -4.0, 9.99999999999946]), tags = self.tag, stipple = '', width = 1, outline = '', fill = 'grey45')
        self.gf9 = GraphicalForm(drawing, h, "gf9")
        self.graphForms.append(self.gf9)

        h = drawing.create_oval(self.translate([8.611111111110858, 8.722222222222058, -8.000000000000227, -7.888888888888744]), tags = self.tag, stipple = '', width = 1, outline = '', fill = 'white')
        self.gf11 = GraphicalForm(drawing, h, "gf11")
        self.graphForms.append(self.gf11)

        h = drawing.create_oval(self.translate([0.0, 0.0, 0.0, 0.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_hasActions_Center
