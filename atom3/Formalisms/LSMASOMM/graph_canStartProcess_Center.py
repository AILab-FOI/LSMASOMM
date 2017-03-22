"""
__graph_canStartProcess_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_canStartProcess_Center(graphEntity):

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
        h = drawing.create_oval(self.translate([0.0, -1.0, 0.0, -1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        self.image_gf196 = PhotoImage(format='gif',data=self.imageDict['canStartProcessNew.gif' ])
        h = drawing.create_image(self.translate([0.0, 0.0]), tags = self.tag, image = self.image_gf196)
        self.gf196 = GraphicalForm(drawing, h, 'gf196', 'canStartProcessNew.gif')
        self.graphForms.append(self.gf196)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'IndKnArtNew.gif' ] = ''+\
'R0lGODlhKAAoAPEAAAAAAP/MAAAAAAAAACH5BAEAAAIALAAAAAAoACgAAAKRhI8mEu3fVpp0LoiDrNyy'+\
'/GzdCFygI5KceWqCOrJnCntt9NaVDNL6wcv4fqVPa/gLYpA6JYRZc4ZyRIQURa0qjLOs9orTWrk9bxXs'+\
'EgPJQjMRDYXB3Un2kt60P/FR/VS9dZMGuFBoeBingrhYCFhEkgjJt+WYGBkz+UiYedlhmSkZuimq9lnJ'+\
'CYpJKmY6qjpSAAA7'        

        imageDict[ 'canStartProcessNew.gif' ] = ''+\
'R0lGODlhFAAUAPEAAABVAICz/wAAAAAAACH5BAEAAAIALAAAAAAUABQAAAI0jH8iwN0IlZsQyfmquRjo'+\
'vXTex2FfUFJk2J2p4yryLMT0HIuj9mY8a1rpciJiS1hEHn+6AgA7'        

        return imageDict

new_class = graph_canStartProcess_Center
