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
        self.sizeX, self.sizeY = 58, 86
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
        h = drawing.create_oval(self.translate([29.0, 40.0, 29.0, 40.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([9.0, 20.0, 48.000000000000114, 59.000000000000114]), tags = self.tag, stipple = '', width = 2, outline = '#000000', fill = 'white')
        self.gf207 = GraphicalForm(drawing, h, "gf207")
        self.graphForms.append(self.gf207)

        h = drawing.create_line(self.translate([28.746835443038208, 39.253164556961906, 28.746835443038208, 59.0]), tags = self.tag, stipple = '', width = 2, fill = 'red4', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf204 = GraphicalForm(drawing, h, "gf204")
        self.graphForms.append(self.gf204)

        h = drawing.create_oval(self.translate([25.291139240506197, 35.79746835443031, 32.20253164556982, 42.708860759493874]), tags = self.tag, stipple = '', width = 2, outline = '', fill = 'red4')
        self.gf210 = GraphicalForm(drawing, h, "gf210")
        self.graphForms.append(self.gf210)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=10, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([29.0, 5.0, 29.0, 10.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf30 = GraphicalForm(drawing, h, 'gf30', fontObject=font)
        self.graphForms.append(self.gf30)

        if self.semanticObject: drawText = self.semanticObject.ID.toString()
        else: drawText = "<ID>"
        font = tkFont.Font( family='Helvetica', size=9, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([30.0, 72.0, 30.0, 9.0])[:2], tags = self.tag, font=font, fill = 'gray', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["ID"] = h
        self.gf31 = GraphicalForm(drawing, h, 'gf31', fontObject=font)
        self.graphForms.append(self.gf31)



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

new_class = graph_Objective
