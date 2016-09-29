"""
__graph_answersToOrgUnit_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_____________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_answersToOrgUnit_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 62, 106
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
        h = drawing.create_oval(self.translate([-5.391608391608486, 50.511363636362375, -5.391608391608486, 50.511363636362375]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([-1.4108391608411353, -51.1791958041959, -1.4108391608411353, -51.1791958041959]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([-21.314685314685505, -9.923951048951892, 11.255244755246736, 51.597027972028]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'grey45')
        self.gf116 = GraphicalForm(drawing, h, "gf116")
        self.graphForms.append(self.gf116)

        h = drawing.create_oval(self.translate([-30.0, -51.902972027972, 28.625874125872997, 6.722902097901056]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'orange')
        self.gf117 = GraphicalForm(drawing, h, "gf117")
        self.graphForms.append(self.gf117)

        h = drawing.create_oval(self.translate([3.293706293706805, -28.01835664335698, 12.702797202797171, -18.609265734264852]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'white')
        self.gf118 = GraphicalForm(drawing, h, "gf118")
        self.graphForms.append(self.gf118)

        h = drawing.create_oval(self.translate([20.664335664334317, -30.189685314684823, 30.073426573425422, -20.780594405595593]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'white')
        self.gf120 = GraphicalForm(drawing, h, "gf120")
        self.graphForms.append(self.gf120)

        h = drawing.create_line(self.translate([-5.753496503495967, 15.046328671329377, -5.753496503495967, 15.046328671329377]), tags = self.tag, stipple = '', width = 1, fill = 'white', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf121 = GraphicalForm(drawing, h, "gf121")
        self.graphForms.append(self.gf121)

        h = drawing.create_line(self.translate([-5.753496503495967, 16.49388111888294, 2.20804195804385, 30.245629370628706]), tags = self.tag, stipple = '', width = 5, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf122 = GraphicalForm(drawing, h, "gf122")
        self.graphForms.append(self.gf122)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_answersToOrgUnit_Center
