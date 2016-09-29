"""
__graph_Class_.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Class_(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 127, 73
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
        h = drawing.create_oval(self.translate([20.0, 39.0, 20.0, 39.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([122.0, 36.0, 122.0, 36.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_polygon(self.translate([1.0, 1.0, 19.151925389624807, 2.68850147380644, 29.725649615093346, 4.862848169136981, 46.49980922866325, 36.461447279649065, 28.929798335197887, 70.4668945921735, 1.900085141598197, 72.44125533896431, 19.69718746218615, 36.46386278579985]), tags = self.tag, stipple = '', width = 1, outline = '', fill = '#fbee64', smooth = 'False', splinesteps =  '12')
        self.gf57 = GraphicalForm(drawing, h, "gf57")
        self.graphForms.append(self.gf57)

        h = drawing.create_polygon(self.translate([41.0, 1.0, 59.15192538962481, 2.68850147380644, 69.72564961509335, 4.862848169136981, 86.49980922866325, 36.461447279649065, 68.92979833519789, 70.4668945921735, 41.9000851415982, 72.44125533896431, 59.69718746218615, 36.46386278579985]), tags = self.tag, stipple = '', width = 1, outline = '', fill = '#fbee64', smooth = 'False', splinesteps =  '12')
        self.gf59 = GraphicalForm(drawing, h, "gf59")
        self.graphForms.append(self.gf59)

        h = drawing.create_polygon(self.translate([81.0, 1.0, 99.15192538962481, 2.68850147380644, 109.72564961509335, 4.862848169136981, 126.49980922866325, 36.461447279649065, 108.92979833519792, 70.4668945921735, 81.9000851415982, 72.44125533896431, 99.69718746218615, 36.46386278579985]), tags = self.tag, stipple = '', width = 1, outline = '', fill = '#fbee64', smooth = 'False', splinesteps =  '12')
        self.gf60 = GraphicalForm(drawing, h, "gf60")
        self.graphForms.append(self.gf60)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Class_
