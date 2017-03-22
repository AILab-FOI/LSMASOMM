"""
__graph_canAccessKnArt_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
___________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_canAccessKnArt_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 20, 20
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
        self.image_gf188 = PhotoImage(format='gif',data=self.imageDict['canAccessKnArtNew.gif' ])
        h = drawing.create_image(self.translate([0.0, 0.0]), tags = self.tag, image = self.image_gf188)
        self.gf188 = GraphicalForm(drawing, h, 'gf188', 'canAccessKnArtNew.gif')
        self.graphForms.append(self.gf188)

        h = drawing.create_oval(self.translate([0.0, -1.0, 0.0, -1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'canAccessKnArtNew.gif' ] = ''+\
'R0lGODlhFAAUAPEAAAAAAP/MAICz/wAAACH5BAEAAAMALAAAAAAUABQAAAI8lH8zwN0IlZsQyfmquRjo'+\
'vXTex2GfUFJk2J2po8Ty28y2CAT6vtMMD/TlgD0WhljEIXXCZaC5hCKlRGEBADs='        

        return imageDict

new_class = graph_canAccessKnArt_Center
