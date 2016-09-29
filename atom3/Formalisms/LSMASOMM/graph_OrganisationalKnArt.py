"""
__graph_OrganisationalKnArt.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_OrganisationalKnArt(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 349, 176
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
        h = drawing.create_rectangle(self.translate([-298.0, -478.0, -254.7839195979902, -435.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'skyblue3')
        self.gf84 = GraphicalForm(drawing, h, "gf84")
        self.graphForms.append(self.gf84)

        h = drawing.create_oval(self.translate([-285.25, -464.75, -267.4673366834169, -446.96733668341636]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'white')
        self.gf86 = GraphicalForm(drawing, h, "gf86")
        self.graphForms.append(self.gf86)

        h = drawing.create_oval(self.translate([-276.0, -455.5, -276.0, -455.5]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        if self.semanticObject: drawText = self.semanticObject.ID.toString()
        else: drawText = "<ID>"
        font = tkFont.Font( family='Helvetica', size=10, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([-248.0, -458.0, -248.0, -637.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["ID"] = h
        self.gf89 = GraphicalForm(drawing, h, 'gf89', fontObject=font)
        self.graphForms.append(self.gf89)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_OrganisationalKnArt
