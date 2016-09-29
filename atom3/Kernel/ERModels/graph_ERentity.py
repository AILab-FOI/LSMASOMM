import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_ERentity(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 179, 119
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
        h = drawing.create_oval(self.translate([9.0, 49.0, 9.0, 49.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([9.0, 69.0, 9.0, 69.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([9.0, 89.0, 9.0, 89.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([169.0, 29.0, 169.0, 29.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([29.0, 109.0, 29.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([49.0, 109.0, 49.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([69.0, 109.0, 69.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([89.0, 109.0, 89.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([109.0, 109.0, 109.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([129.0, 109.0, 129.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([149.0, 109.0, 149.0, 109.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([169.0, 49.0, 169.0, 49.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([169.0, 69.0, 169.0, 69.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([169.0, 89.0, 169.0, 89.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([29.0, 9.0000000000000284, 29.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([49.0, 9.0000000000000284, 49.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([69.0, 9.0000000000000284, 69.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([89.0, 9.0000000000000284, 89.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([109.0, 9.0000000000000284, 109.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([129.0, 9.0000000000000284, 129.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_oval(self.translate([149.0, 9.0000000000000284, 149.0, 9.0000000000000284]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_rectangle(self.translate([9.0, 9.0, 169.50000000000011, 108.5]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'lightyellow')
        self.gf12 = GraphicalForm(drawing, h, "gf12")
        self.graphForms.append(self.gf12)

        h = drawing.create_rectangle(self.translate([8.9999999999999432, 8.9999999999999716, 169.99999999999989, 30.000000000000028]), tags = self.tag, stipple = '', width = 1, outline = 'black', fill = 'orange')
        self.gf8 = GraphicalForm(drawing, h, "gf8")
        self.graphForms.append(self.gf8)

        if self.semanticObject: drawText = self.semanticObject.attributes.toString(80,10)
        else: drawText = "<attributes>"
        font = tkFont.Font( family='helvetica', size=12, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([11.0, 32.0]), tags = self.tag, font=font, fill = 'blue1', anchor = 'nw', text = drawText, justify= 'left', width='0', stipple='' )
        self.attr_display["attributes"] = h
        self.gf3 = GraphicalForm(drawing, h, 'gf3', fontObject=font)
        self.graphForms.append(self.gf3)

        if self.semanticObject: drawText = self.semanticObject.name.toString(25,5)
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([12.0, 12.0]), tags = self.tag, font=font, fill = 'black', anchor = 'nw', text = drawText, justify= 'left', width='0', stipple='' )
        self.attr_display["name"] = h
        self.gf9 = GraphicalForm(drawing, h, 'gf9', fontObject=font)
        self.graphForms.append(self.gf9)

        h = drawing.create_oval(self.translate([9.0, 29.0, 9.0, 29.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        return imageDict

new_class = graph_ERentity
