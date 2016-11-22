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
        self.sizeX, self.sizeY = 136, 51
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
        h = drawing.create_oval(self.translate([24.0, 23.0, 24.0, 23.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        self.image_gf25 = PhotoImage(format='gif',data=self.imageDict['Role.gif' ])
        h = drawing.create_image(self.translate([30.0, 25.0]), tags = self.tag, image = self.image_gf25)
        self.gf25 = GraphicalForm(drawing, h, 'gf25', 'Role.gif')
        self.graphForms.append(self.gf25)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([55.0, 10.0, 55.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf23 = GraphicalForm(drawing, h, 'gf23', fontObject=font)
        self.graphForms.append(self.gf23)

        if self.semanticObject: drawText = self.semanticObject.hasActions.toString()
        else: drawText = "<hasActions>"
        font = tkFont.Font( family='Helvetica', size=10, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([60.0, 18.0, 60.0, 10.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'nw', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["hasActions"] = h
        self.gf24 = GraphicalForm(drawing, h, 'gf24', fontObject=font)
        self.graphForms.append(self.gf24)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'Role.gif' ] = ''+\
'R0lGODlhIQAxAPezAEg+N0k/OEpEPE5FPFBFPFBGPVFHPlNJP0tGQkxHQ0xIQ01LR09MR1RJQFBRTVFU'+\
'UFJUUVRaWFVbWVZfXmBVSFdhX29kVHNoV3VrWXhuW1hjY1hjZVlkZFlmZFpmZlpnZ1poZltpaVlqaFpq'+\
'altra1xqalxqa11sblxtbl1tbl1vcF5xcV1wcmF3emF3e2J3emN5e2N7fGJ6fWN7f56Td6abfamef2N8'+\
'gGN+gWR9gGR/gWR+gmV+gmV/g2aBhWaDh2eDh2eFiGeFiWiGi2iHjWiIjmmJj2qKjmmLkWqLkGuMkWuM'+\
'k2uOk2yNk2uOlGyQl26VnXCWnnGbo3KcpHKcpnKeqHSirHWjrnWmr3amsHansXirt3mst3mtt36uuH+0'+\
'v3+1wn+4xX+4x368yaqegLClhIWlrIunrYGor4morY6prpOmqZyqq56qrYSpsIapsYattYmqsY+sspCq'+\
'sJSusZevsoSwu4CyvIKyvIS0v56ytaWvsaevsaS1uLK6urS6utLHntbKodbLodnNo+jbrujcroK3w4G5'+\
'xYK5xoC9yoC9y4O+y4S8yYS+y4C9zIHAzYHAzoHBz4HA0ILB0YHC0YLC0YTD04TE04TF1YTG1oTG14XH'+\
'14XJ2obJ2oXK24bL3IfL3IbM3IbM3YfN3rzCwszQ0NDS0tva2tnc2tzd3eDg3+Lh4Obn5+np6Ozr6/n4'+\
'+Pv6+v39/f7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'ACH5BAEAALQALAAAAAAhADEAAAj+AGkJHEhQIIgYQYgsORJkBoiCECMS5MFllMWLFjltuSGxIy0elTCK'+\
'xAjJh0eCHyqOXHlxi4iTJUKynDmq0omOJTDR3InpJcQPYnYKhfQBYhahSLUUnIG06QyCY5oiTTTwhtSm'+\
'PARiuToSVBw9dBJZtELrAyeuIte8mjWLVKNRnTS04Brmy9lRd1qxZUvHIgwgUhuxOaWKT55RaPay7WPx'+\
'x5Gmodoo/mPpECrFcyweSdIUjCrFsNCMUsOKLR+Zm5t6caV4lhmLduS8yXRxSZGmmf4oLnVoJhEeUuGU'+\
'YpvqDM0bLK4aOqMGz04WtGSinQlJoJPpNJ0IFAEKO0voAqXEeB9JhaCEu+NHcfIpMMDc9KOAFAyAAEr6'+\
'8gUBAGAgHvuViPoFsMB1aEUhkX76CXCCdEJVAkNHCCL4ABCa8JTEBh5FGKEDJzwRFUaJOKFCBSfRouGJ'+\
'CkAgwQQRPJAAAAGUaGKEFGCgYQAnAiCjhmUUQoYBOUa4Y4QD0EDIIBnAGOSQGloAiI8DLFlikAbYQIgg'+\
'F+TIZI4YCFJIDUAKOWWQ+lU5yAEabklmAyeqSWabY74p5UlykulmnfrdiaeedfIp50kBAQA7'        

        return imageDict

new_class = graph_Role
