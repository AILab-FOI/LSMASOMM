"""
__graph_isPartOfRole_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_isPartOfRole_Center(graphEntity):

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
        self.image_gf178 = PhotoImage(format='gif',data=self.imageDict['isPartOfRoleNew.gif' ])
        h = drawing.create_image(self.translate([0.0, 0.0]), tags = self.tag, image = self.image_gf178)
        self.gf178 = GraphicalForm(drawing, h, 'gf178', 'isPartOfRoleNew.gif')
        self.graphForms.append(self.gf178)

        h = drawing.create_oval(self.translate([1.0, 0.0, 1.0, 0.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'isPartOfRoleNew.gif' ] = ''+\
'R0lGODlhFAAUAPAAAICz/wAAACH5BAEAAAEALAAAAAAUABQAAAIohI+By9nvIFTy0coujpt3o3XBSJbm'+\
'iZJTuI3f4b5A/NKfLbIY3upGAQA7'        

        imageDict[ 'isPartOfRole.gif' ] = ''+\
'R0lGODlhMgA0AOMIACy//y2//yvA/yzA/y3A/yvB/yzB/y3B////////////////////////////////'+\
'/yH5BAEKAAgALAAAAAAyADQAAATqEMlJKwIjH8u7/5SQjQNonlZBkmhrrqwrc/A431Sd4TxW87wfMEgS'+\
'DIm2I26lvBlWgSbqoBsFAMeqdlsjvLjgrRcULuvGH7OahPas3+3Oex2nzdXfexhL1oc3fX5geYJbhIVV'+\
'hxM+iCWBdogndRONFiI7J5USQoGNOoeeTJ2hommaNQagcxUwJpeCHAQDUQgqjhVPhamdRpSNfB+5pKVu'+\
'wyu9pmUqr2WqiRZhu8mGxVzOrdM6yNVaJrLU2Z/XGZOs1uMD5TnnH4xn6JjhMOq+7HJi8PGQWvSbYfdc'+\
'+iHgEkAAIA4CEiYUByICADs='        

        return imageDict

new_class = graph_isPartOfRole_Center
