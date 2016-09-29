"""
__graph_Objective.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_______________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Objective(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 128, 60
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
        h = drawing.create_oval(self.translate([1.0, 8.0, 50.000000000000114, 57.00000000000034]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'white')
        self.gf25 = GraphicalForm(drawing, h, "gf25")
        self.graphForms.append(self.gf25)

        h = drawing.create_oval(self.translate([5.678391959798418, 12.678391959798887, 45.56783919598021, 52.56783919598021]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'blue1')
        self.gf26 = GraphicalForm(drawing, h, "gf26")
        self.graphForms.append(self.gf26)

        h = drawing.create_oval(self.translate([9.864321608040143, 17.603015075376675, 41.91100128742863, 48.13567839195997]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'red3')
        self.gf27 = GraphicalForm(drawing, h, "gf27")
        self.graphForms.append(self.gf27)

        h = drawing.create_oval(self.translate([15.03517587939669, 22.527638190955116, 35.964824120603396, 43.45728643216128]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'yellow')
        self.gf28 = GraphicalForm(drawing, h, "gf28")
        self.graphForms.append(self.gf28)

        h = drawing.create_oval(self.translate([25.0, 32.0, 25.0, 32.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        font = tkFont.Font( family='Arial', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([66.0, 8.0, 66.0, -125.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = 'Goal', width = '0', justify= 'left', stipple='' )
        self.gf29 = GraphicalForm(drawing, h, 'gf29', fontObject=font)
        self.graphForms.append(self.gf29)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([61.0, 48.0, 61.0, -156.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf30 = GraphicalForm(drawing, h, 'gf30', fontObject=font)
        self.graphForms.append(self.gf30)

        if self.semanticObject: drawText = self.semanticObject.ID.toString()
        else: drawText = "<ID>"
        font = tkFont.Font( family='Helvetica', size=9, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([61.0, 28.0, 61.0, -221.0])[:2], tags = self.tag, font=font, fill = 'gray', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["ID"] = h
        self.gf31 = GraphicalForm(drawing, h, 'gf31', fontObject=font)
        self.graphForms.append(self.gf31)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_Objective
