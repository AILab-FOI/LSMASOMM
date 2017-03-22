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
        self.image_gf175 = PhotoImage(format='gif',data=self.imageDict['answersToRoleNew.gif' ])
        h = drawing.create_image(self.translate([0.0, 0.0]), tags = self.tag, image = self.image_gf175)
        self.gf175 = GraphicalForm(drawing, h, 'gf175', 'answersToRoleNew.gif')
        self.graphForms.append(self.gf175)

        h = drawing.create_oval(self.translate([0.0, 0.0, 0.0, 0.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'answersToRoleNew.gif' ] = ''+\
'R0lGODlhFAAUAPAAAICz/wAAACH5BAEAAAEALAAAAAAUABQAAAIghI+py+0Po5y02hay3rz7v2GBlZFj'+\
'VaInlbLr1MJvUgAAOw=='        

        return imageDict

new_class = graph_answersToRole_Center
