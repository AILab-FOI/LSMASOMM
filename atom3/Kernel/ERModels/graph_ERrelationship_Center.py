import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_ERrelationship_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 99, 99
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
        h = drawing.create_oval(self.translate([-2.0, 0.0, -2.0, 0.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_polygon(self.translate([-47.999999999999993, 0.0, 0.0, -47.999999999999993, 47.999999999999993, 0.0, 0.0, 47.999999999999993]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'lightyellow', smooth = 'False', splinesteps =  '12')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)

        if self.semanticObject: drawText = self.semanticObject.name.toString(25,5)
        else: drawText = "<name>"
        font = tkFont.Font( family='times', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([1.0, 0.0]), tags = self.tag, font=font, fill = 'blue1', anchor = 'center', text = drawText, justify= 'left', width='0', stipple='' )
        self.attr_display["name"] = h
        self.gf3 = GraphicalForm(drawing, h, 'gf3', fontObject=font)
        self.graphForms.append(self.gf3)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_ERrelationship_Center
