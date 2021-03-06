"""
__graph_CD_Inheritance3_2ndLink.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
__________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_CD_Inheritance3_2ndLink(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 32, 17
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
        h = drawing.create_polygon(self.translate([-14.0, 7.0, 0.0, -7.0, 14.0, 7.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'white', smooth = 'False', splinesteps =  '12')
        self.gf100 = GraphicalForm(drawing, h, "gf100")
        self.graphForms.append(self.gf100)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_CD_Inheritance3_2ndLink
