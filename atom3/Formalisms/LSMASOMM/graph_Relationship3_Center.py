"""
__graph_Relationship3_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
__________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Relationship3_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 260.0, 104.5
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
        h = drawing.create_oval(self.translate([-129.0, -51.5, -129.0, -51.5]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([-130.0, -52.5, -130.0, -52.5]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([73.0, -13.067039106145181, 128.81751824817525, 51.499999999999886]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'yellow')
        self.gf35 = GraphicalForm(drawing, h, "gf35")
        self.graphForms.append(self.gf35)

        h = drawing.create_rectangle(self.translate([75.08133118891482, -10.634078212290568, 126.92539898552468, 49.44134078212282]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'white')
        self.gf36 = GraphicalForm(drawing, h, "gf36")
        self.graphForms.append(self.gf36)

        h = drawing.create_rectangle(self.translate([84.35271557589985, -15.5, 116.70795496721587, -8.57541899441329]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'gray')
        self.gf37 = GraphicalForm(drawing, h, "gf37")
        self.graphForms.append(self.gf37)

        h = drawing.create_rectangle(self.translate([95.32700729926978, -14.751396648044683, 107.62578250649534, -6.89106145251376]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'black')
        self.gf38 = GraphicalForm(drawing, h, "gf38")
        self.graphForms.append(self.gf38)

        h = drawing.create_line(self.translate([80.1900531980703, 3.963687150837984, 121.81667697636982, 3.963687150837984]), tags = self.tag, stipple = '', width = 2, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf40 = GraphicalForm(drawing, h, "gf40")
        self.graphForms.append(self.gf40)

        h = drawing.create_line(self.translate([80.1900531980703, 15.192737430167398, 121.81667697636982, 15.192737430167398]), tags = self.tag, stipple = '', width = 2, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf42 = GraphicalForm(drawing, h, "gf42")
        self.graphForms.append(self.gf42)

        h = drawing.create_line(self.translate([80.1900531980703, 26.42178770949687, 121.81667697636982, 26.42178770949687]), tags = self.tag, stipple = '', width = 2, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf43 = GraphicalForm(drawing, h, "gf43")
        self.graphForms.append(self.gf43)

        h = drawing.create_line(self.translate([80.1900531980703, 37.650837988826254, 121.81667697636982, 37.650837988826254]), tags = self.tag, stipple = '', width = 2, fill = 'black', smooth = '0', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf44 = GraphicalForm(drawing, h, "gf44")
        self.graphForms.append(self.gf44)

        h = drawing.create_oval(self.translate([101.0, -13.5, 101.0, -13.5]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([76.0, 19.5, 76.0, 19.5]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([101.0, 50.5, 101.0, 50.5]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([126.0, 17.5, 126.0, 17.5]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Relationship3_Center
