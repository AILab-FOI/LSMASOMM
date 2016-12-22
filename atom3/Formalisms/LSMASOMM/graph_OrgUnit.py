"""
__graph_OrgUnit.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
_____________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_OrgUnit(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 105, 51
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
        h = drawing.create_oval(self.translate([17.0, 31.0, 17.0, 31.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        self.image_gf32 = PhotoImage(format='gif',data=self.imageDict['OrgUnit.gif' ])
        h = drawing.create_image(self.translate([21.0, 27.0]), tags = self.tag, image = self.image_gf32)
        self.gf32 = GraphicalForm(drawing, h, 'gf32', 'OrgUnit.gif')
        self.graphForms.append(self.gf32)

        if self.semanticObject: drawText = self.semanticObject.UnitSize.toString()
        else: drawText = "<UnitSize>"
        font = tkFont.Font( family='Helvetica', size=8, weight='normal', slant='italic', underline=0)
        h = drawing.create_text(self.translate([40.0, 44.0, 40.0, 16.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["UnitSize"] = h
        self.gf24 = GraphicalForm(drawing, h, 'gf24', fontObject=font)
        self.graphForms.append(self.gf24)

        if self.semanticObject: drawText = self.semanticObject.ID.toString()
        else: drawText = "<ID>"
        font = tkFont.Font( family='Helvetica', size=8, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([40.0, 9.0, 40.0, -103.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["ID"] = h
        self.gf33 = GraphicalForm(drawing, h, 'gf33', fontObject=font)
        self.graphForms.append(self.gf33)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='Helvetica', size=12, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([40.0, 25.0, 40.0, -149.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'w', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf34 = GraphicalForm(drawing, h, 'gf34', fontObject=font)
        self.graphForms.append(self.gf34)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'OrgUnit.gif' ] = ''+\
'R0lGODlhIgAyAPe0AEg9Nkg+N0k/OE9EN0lAOEpAOEtAOUxBOVJIOVdMOVpMOVtNOWVUPGVXPGpbPG5f'+\
'PXJjPnRkPXVlP3ZnP3hmPndoPndoP3hoPnppP3xrP1tRRlxSRmBVSGBWSWNZTGRZTGRaTHZnQX90X4Fv'+\
'QIFwQIJxQINwQYRxQIN0QYR0QIZ1QYd1QYd2Qol3Qop3Qol4Q4x5Qo17Qo17Q5J9Q5B8RJJ/RIF3YYZ7'+\
'ZYp/aJSAQ5eCRJiERJmFRJuHRJuGRZyHRKKLR6ONRaONRqSORqWPRqSPR6aQRqeQRqeRR6iRR66WR6eR'+\
'SKuUSKyUSK+XSLCYSLGZSbSbSLedSbegSZOIb5aLcbepfL6ve7iqfL6ufMKpSsOqS8SpTMmvTMyxTM+z'+\
'TdC1TdK2TtK3T9S3TdO4T9W4T9a5T9i7Tt2/T8+2XNC3Xdm+WsavY8OuZcCsZ8GtZ8iyZsaybcSydd7A'+\
'UN3BWeLEUOLEUebHUeDDV+PGV+nKUOrLUu3MUezMUu7OUu/PU+nLVenLVuHEWeLFWvHRUvHQU/HSU/TT'+\
'U/TUU/fWU/bVVPbWVPnXVPnYVP3bVf7bVP7cVf/dVbyvhresiryvib+0k7+1lr61nsa2gsK0hsK0h8Cz'+\
'jsO4k8S4lMi8lsi9lsi9l8e9n8C3oMC3pMzFs8vFtszFtM/Ju+HVqePWquTXq+bZrOXarendr9HNw+zq'+\
'6PDv7fHx7vLx7/b29f///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'ACH5BAEAALUALAAAAAAiADIAAAj+AGsJHEhwoIseRIwYIdLDRcGHEAu+mIIoksWLFg9JeRGxY60UYzCK'+\
'FCnmhMeCThyNXHnRkZKTtSqEZEnTopgKHUPMqckz0hycEMX07CkGopOhQ5kUPKESKU9HJQh+cTrUy0AW'+\
'VJE6rBUl60hHaeKoafpEoCGvGB1ZiUUrFhaVfmphRXsRzixaeGfBsXiCB1U6kkRVYmMRE97DmCz2COI0'+\
'T6nDr95EknMYrxyLQYw4vVKZ1qVIgR7jJRXIopEkTjd1duUnkqBMoTINuriEiNMsnT/TJPLDKZ5TkCXT'+\
'7CGD6hpKoywJpwmjQiO6NRtJqLUFOk0uAotbX0lDIIM620XR3iFYIjzGGQQRaDEfqUtBAQxab/dDoWCA'+\
'AA8qQkc04uH9ABCchZYh/fn3nwMzUXVGBhH9J4AACuSQCFKIAOHRfxgyoMMeNelBBAYnYfgfAQEkIAEN'+\
'T5hRRx1mOEGDBArAVIuINP43wAAiyiiiBpNoUCONOmJowyqoUEHij/cFiSEInazCCQdIBqAkhgRQsYoq'+\
'Rv44pYggfNJKJ1ACCVOUBFRB5A0A5DgmkgQI0KUNYoYYZQAP0gjAlnNieOeaedaIZ59J8gkohn8CWmif'+\
'h+Z5UkAAOw=='        

        return imageDict

new_class = graph_OrgUnit
