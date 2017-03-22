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
        self.sizeX, self.sizeY = 83, 22
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
        h = drawing.create_oval(self.translate([-31.0, 1.0, -31.0, 1.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        self.image_gf173 = PhotoImage(format='gif',data=self.imageDict['genericAssociationNew.gif' ])
        h = drawing.create_image(self.translate([-31.0, 1.0]), tags = self.tag, image = self.image_gf173)
        self.gf173 = GraphicalForm(drawing, h, 'gf173', 'genericAssociationNew.gif')
        self.graphForms.append(self.gf173)

        if self.semanticObject: drawText = self.semanticObject.Name.toString()
        else: drawText = "<Name>"
        font = tkFont.Font( family='Helvetica', size=10, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([-18.0, -1.0, -18.0, 10.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["Name"] = h
        self.gf159 = GraphicalForm(drawing, h, 'gf159', fontObject=font)
        self.graphForms.append(self.gf159)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'genericAssociationNew.gif' ] = ''+\
'R0lGODlhFAAUAPIEAAAAAHFxcampqaqqqv///wAAAAAAAAAAACH5BAAAAAAALAAAAAAUABQAAAM9CLrc'+\
'/jBKGIa4I+scnCBgKIKCN55E2XyoqDJsS5ryvNY2jKd0/S4x2U8RbA0BRdQxeToGLoKNtDOpWq/VBAA7'        

        return imageDict

new_class = graph_genericAssociation_Center
