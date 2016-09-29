"""
__graph_answersToRole_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
__________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_answersToRole_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 35, 62
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
        h = drawing.create_rectangle(self.translate([-14.795158628277818, -8.289473684210435, 3.2774619475516147, 30.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'grey45')
        self.gf146 = GraphicalForm(drawing, h, "gf146")
        self.graphForms.append(self.gf146)

        h = drawing.create_oval(self.translate([-16.0, -30.0, 16.932330827067517, 2.3684210526317884]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'skyblue1')
        self.gf147 = GraphicalForm(drawing, h, "gf147")
        self.graphForms.append(self.gf147)

        h = drawing.create_oval(self.translate([0.46616541353392904, -15.0, 6.088758481570153, -9.473684210526187]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'white')
        self.gf148 = GraphicalForm(drawing, h, "gf148")
        self.graphForms.append(self.gf148)

        h = drawing.create_oval(self.translate([11.309737759031464, -17.763157894736764, 15.727489455345676, -13.421052631579045]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'white')
        self.gf149 = GraphicalForm(drawing, h, "gf149")
        self.graphForms.append(self.gf149)

        h = drawing.create_line(self.translate([-9.17256556024222, 8.684210526316008, -0.7386759581879687, 13.026315789473756]), tags = self.tag, stipple = '', width = 4, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf150 = GraphicalForm(drawing, h, "gf150")
        self.graphForms.append(self.gf150)

        h = drawing.create_oval(self.translate([-5.0, 12.0, -5.0, 12.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_answersToRole_Center
