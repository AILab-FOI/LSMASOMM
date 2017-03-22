"""
__graph_Role.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
__________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_Role(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 79, 85
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
        h = drawing.create_polygon(self.translate([28.0, 49.0, 22.656093037833614, 56.4729294554449, 10.507156807955965, 64.59176038045518, 43.66666666666674, 67.79999999999995, 68.51710954891229, 61.08371469229701, 52.94507517889812, 55.07984097157248, 49.93333333333291, 49.0, 46.79999999999973, 39.599999999999966, 43.66666666666674, 33.333333333333655, 28.0, 20.799999999999955, 31.133333333333155, 33.333333333333655]), tags = self.tag, stipple = '', width = 1, outline = '#000000', fill = 'royalblue', smooth = 1, splinesteps =  '12')
        self.gf217 = GraphicalForm(drawing, h, "gf217")
        self.graphForms.append(self.gf217)

        h = drawing.create_oval(self.translate([38.0, 52.0, 38.0, 52.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='FreeSans', size=12, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([40.0, 9.0, 40.0, 11.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf23 = GraphicalForm(drawing, h, 'gf23', fontObject=font)
        self.graphForms.append(self.gf23)

        if self.semanticObject: drawText = self.semanticObject.hasActions.toString()
        else: drawText = "<hasActions>"
        font = tkFont.Font( family='FreeSans', size=9, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([39.0, 71.0, 39.0, 64.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'n', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["hasActions"] = h
        self.gf24 = GraphicalForm(drawing, h, 'gf24', fontObject=font)
        self.graphForms.append(self.gf24)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'ObjectiveNew.gif' ] = ''+\
'R0lGODlhKAAoAPAAAKoAAAAAACH5BAAAAAAALAAAAAAoACgAAAInhI+py+0Po5y02ouz3rz7D4biSJbm'+\
'iabqyrbuC8fyTNf2jef6ziMFADs='        

        return imageDict

new_class = graph_Role
