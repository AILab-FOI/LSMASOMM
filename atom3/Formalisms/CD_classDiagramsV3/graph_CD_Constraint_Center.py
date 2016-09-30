"""
__graph_CD_Constraint_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_______________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_CD_Constraint_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 67, 58
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
        h = drawing.create_line(self.translate([-13.0, 1.0, -14.0, -23.0, 15.0, -22.0, 12.0, 1.0]), tags = self.tag, stipple = '', width = 5, fill = 'yellow', smooth = '1', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf14 = GraphicalForm(drawing, h, "gf14")
        self.graphForms.append(self.gf14)

        h = drawing.create_rectangle(self.translate([-17.0, -1.0, 18.399999999999636, 18.200000000000216]), tags = self.tag, stipple = '', width = 1, outline = '', fill = 'red1')
        self.gf6 = GraphicalForm(drawing, h, "gf6")
        self.graphForms.append(self.gf6)

        h = drawing.create_polygon(self.translate([-17.0, 17.000000000000171, 19.0, 17.000000000000171, 7.0000000000001705, 29.0, -5.0000000000002274, 29.0]), tags = self.tag, stipple = '', width = 1, outline = '', fill = 'red1', smooth = 'False', splinesteps =  '12')
        self.gf10 = GraphicalForm(drawing, h, "gf10")
        self.graphForms.append(self.gf10)

        font = tkFont.Font( family='Helvetica', size=18, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([0.0, 11.0, 0.0, 24.0])[:2], tags = self.tag, font=font, fill = 'white', anchor = 'center', text = 'VC', width = '0', justify= 'left', stipple='' )
        self.gf7 = GraphicalForm(drawing, h, 'gf7', fontObject=font)
        self.graphForms.append(self.gf7)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([0.0, 1.0, 0.0, 18.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 's', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf12 = GraphicalForm(drawing, h, 'gf12', fontObject=font)
        self.graphForms.append(self.gf12)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_CD_Constraint_Center
