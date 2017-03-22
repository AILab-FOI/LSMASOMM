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
        self.image_gf168 = PhotoImage(format='gif',data=self.imageDict['answersToOrgUnitNew.gif' ])
        h = drawing.create_image(self.translate([0.0, 0.0]), tags = self.tag, image = self.image_gf168)
        self.gf168 = GraphicalForm(drawing, h, 'gf168', 'answersToOrgUnitNew.gif')
        self.graphForms.append(self.gf168)

        h = drawing.create_oval(self.translate([0.0, 0.0, 0.0, 0.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'answersToOrgUnitNew.gif' ] = ''+\
'R0lGODlhFAAUAPAAAP/MAAAAACH5BAEAAAEALAAAAAAUABQAAAIghI+py+0Po5y02hay3rz7v2GBlZFj'+\
'VaInlbLr1MJvUgAAOw=='        

        return imageDict

new_class = graph_answersToOrgUnit_Center
