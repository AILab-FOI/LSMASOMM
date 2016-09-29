"""
__graph_OrgGoal.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_OrgGoal(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 195, 56
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
        h = drawing.create_oval(self.translate([90.0, 10.0, 131.00000000000014, 51.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'olivedrab4')
        self.gf24 = GraphicalForm(drawing, h, "gf24")
        self.graphForms.append(self.gf24)

        h = drawing.create_oval(self.translate([91.0, 30.0, 91.0, 30.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([112.0, 51.0, 112.0, 51.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([110.0, 11.0, 110.0, 11.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Courier 10 Pitch', size=10, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([130.0, 40.0, 130.0, -26.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'nw', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf29 = GraphicalForm(drawing, h, 'gf29', fontObject=font)
        self.graphForms.append(self.gf29)

        font = tkFont.Font( family='Arial', size=8, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([47.0, 6.0, 47.0, 8.0])[:2], tags = self.tag, font=font, fill = 'gray', anchor = 'center', text = 'Organizational Goal', width = '0', justify= 'left', stipple='' )
        self.gf30 = GraphicalForm(drawing, h, 'gf30', fontObject=font)
        self.graphForms.append(self.gf30)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_OrgGoal
