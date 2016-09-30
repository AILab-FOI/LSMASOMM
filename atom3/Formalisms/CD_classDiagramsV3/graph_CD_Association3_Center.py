"""
__graph_CD_Association3_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_CD_Association3_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 154, 114
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
        h = drawing.create_oval(self.translate([-3.0, 5.0, -3.0, 5.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([-74.0, -34.0, 74.0, 57.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'black')
        self.gf12 = GraphicalForm(drawing, h, "gf12")
        self.graphForms.append(self.gf12)

        h = drawing.create_rectangle(self.translate([-75.0, -39.0, 75.0, 57.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'white')
        self.gf10 = GraphicalForm(drawing, h, "gf10")
        self.graphForms.append(self.gf10)

        h = drawing.create_polygon(self.translate([-75.0, -49.75, -75.0, -39.25, 0.0, -34.0, 75.0, -39.25, 75.0, -49.75, 0.0, -55.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'yellow', smooth = 'False', splinesteps =  '12')
        self.gf9 = GraphicalForm(drawing, h, "gf9")
        self.graphForms.append(self.gf9)

        h = drawing.create_oval(self.translate([-2.0, 5.0, -2.0, 5.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='times', size=12, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([0.0, -45.0, 0.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf3 = GraphicalForm(drawing, h, 'gf3', fontObject=font)
        self.graphForms.append(self.gf3)

        if self.semanticObject: drawText = self.semanticObject.display.toString()
        else: drawText = "<display>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([-74.0, 12.0, -74.0, 12.0])[:2], tags = self.tag, font=font, fill = 'blue1', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["display"] = h
        self.gf11 = GraphicalForm(drawing, h, 'gf11', fontObject=font)
        self.graphForms.append(self.gf11)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_CD_Association3_Center
