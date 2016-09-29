"""
__graph_IndividualKnArt.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_____________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_IndividualKnArt(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 89, 46
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
        h = drawing.create_oval(self.translate([21.5, 23.75, 21.5, 23.75]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([21.0, 24.0, 21.0, 24.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([1.0, 1.0, 44.75, 44.75]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'sienna3')
        self.gf101 = GraphicalForm(drawing, h, "gf101")
        self.graphForms.append(self.gf101)

        h = drawing.create_rectangle(self.translate([14.5, 14.0, 31.25000000000003, 30.75]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'white')
        self.gf102 = GraphicalForm(drawing, h, "gf102")
        self.graphForms.append(self.gf102)

        if self.semanticObject: drawText = self.semanticObject.ID.toString()
        else: drawText = "<ID>"
        font = tkFont.Font( family='Helvetica', size=10, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([50.0, 22.0, 50.0, 33.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["ID"] = h
        self.gf26 = GraphicalForm(drawing, h, 'gf26', fontObject=font)
        self.graphForms.append(self.gf26)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_IndividualKnArt
