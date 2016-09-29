"""
__graph_genericAssociation_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_______________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_genericAssociation_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 88, 22
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
        h = drawing.create_oval(self.translate([-34.0, 1.0, -34.0, 1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([-44.0, -11.0, -22.0, 11.0]), tags = self.tag, stipple = '', width = 1, outline = '', fill = 'purple1')
        self.gf152 = GraphicalForm(drawing, h, "gf152")
        self.graphForms.append(self.gf152)

        if self.semanticObject: drawText = self.semanticObject.Name.toString()
        else: drawText = "<Name>"
        font = tkFont.Font( family='Helvetica', size=10, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([-16.0, -1.0, -16.0, -232.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["Name"] = h
        self.gf159 = GraphicalForm(drawing, h, 'gf159', fontObject=font)
        self.graphForms.append(self.gf159)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_genericAssociation_Center
