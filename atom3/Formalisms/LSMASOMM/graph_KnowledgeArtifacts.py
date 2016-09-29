"""
__graph_KnowledgeArtifacts.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_KnowledgeArtifacts(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 31, 71
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
        h = drawing.create_polygon(self.translate([2.0, 2.0, 2.0, 2.0, 2.0, 69.0, 11.969230769230819, 46.66666666666691, 26.923076923077048, 59.07407407407419, 15.707692307692241, 36.740740740740705, 29.0, 19.990740740740762, 8.64615384615388, 29.29629629629636]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'moccasin', smooth = '0', splinesteps =  '12')
        self.gf29 = GraphicalForm(drawing, h, "gf29")
        self.graphForms.append(self.gf29)

        h = drawing.create_oval(self.translate([10.0, 39.0, 10.0, 39.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_KnowledgeArtifacts
