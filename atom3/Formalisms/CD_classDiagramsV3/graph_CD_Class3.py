"""
__graph_CD_Class3.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_CD_Class3(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 192, 142
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None

        constObj = ATOM3Constraint(atribs,"abstractVisibility","self.semanticObject.", [], [])
        constObj.setValue(('abstractVisibility', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'if self.semanticObject.Abstract.toString() == "True":\n   self.gf46.setVisible(1)\nelse:\n   self.gf46.setVisible(0)\n\n'))
        self.constraintList.append(constObj)
        self.graphForms = []
        self.imageDict = self.getImageDict()

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([36.0, 141.0, 36.0, 141.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([76.0, 141.0, 76.0, 141.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([116.0, 141.0, 116.0, 141.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([156.0, 141.0, 156.0, 141.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([1.0, 69.0, 1.0, 69.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([1.0, 41.0, 1.0, 41.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([1.0, 96.0, 1.0, 96.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([1.0, 121.0, 1.0, 121.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([191.0, 69.0, 191.0, 69.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([191.0, 41.0, 191.0, 41.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([191.0, 96.0, 191.0, 96.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([191.0, 121.0, 191.0, 121.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([156.0, 1.0, 156.0, 1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([116.0, 1.0, 116.0, 1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([76.0, 1.0, 76.0, 1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([36.0, 1.0, 36.0, 1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([1.0, 1.0, 191.0, 21.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'yellow')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)

        h = drawing.create_rectangle(self.translate([1.0, 21.0, 191.0, 141.0]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = '#f8f8f8')
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)

        if self.semanticObject: drawText = self.semanticObject.display.toString()
        else: drawText = "<display>"
        font = tkFont.Font( family='Helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([2.0, 24.0, 2.0, 12.0])[:2], tags = self.tag, font=font, fill = 'blue1', anchor = 'nw', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["display"] = h
        self.gf4 = GraphicalForm(drawing, h, 'gf4', fontObject=font)
        self.graphForms.append(self.gf4)

        font = tkFont.Font( family='Helvetica', size=9, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([188.0, 5.0, 188.0, 9.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'ne', text = '<<Abstract>>', width = '0', justify= 'left', stipple='' )
        self.gf46 = GraphicalForm(drawing, h, 'gf46', fontObject=font)
        self.graphForms.append(self.gf46)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([5.0, 2.0, 5.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'nw', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf63 = GraphicalForm(drawing, h, 'gf63', fontObject=font)
        self.graphForms.append(self.gf63)


    def abstractVisibility(self,params):
        if self.semanticObject.Abstract.toString() == "True":
           self.gf46.setVisible(1)
        else:
           self.gf46.setVisible(0)
        
        

    def postCondition( self, actionID, * params):
        if actionID ==  self.EDIT or actionID == self.CREATE:
             res = self.abstractVisibility(params)
             if res: return res
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_CD_Class3
