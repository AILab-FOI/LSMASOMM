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
        self.sizeX, self.sizeY = 70, 99
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
        h = drawing.create_line(self.translate([27.461816293522087, 46.36113701106791, 27.461816293522087, 46.36113701106791, 28.23273367645701, 83.00000000000006, 30.93094451672693, 82.08402842527678]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'bevel', arrow = 'none', arrowshape = (15,15,3))
        self.gf186 = GraphicalForm(drawing, h, "gf186")
        self.graphForms.append(self.gf186)

        h = drawing.create_line(self.translate([36.6609764525804, 59.053738460785596, 36.6609764525804, 59.053738460785596, 37.431893835515694, 82.13119823108033, 40.13010467578536, 81.5542617368227]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'bevel', arrow = 'none', arrowshape = (15,15,3))
        self.gf188 = GraphicalForm(drawing, h, "gf188")
        self.graphForms.append(self.gf188)

        h = drawing.create_line(self.translate([26.155762012341484, 79.06033731301761, 26.155762012341484, 79.06033731301761]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf189 = GraphicalForm(drawing, h, "gf189")
        self.graphForms.append(self.gf189)

        h = drawing.create_line(self.translate([26.400111619884548, 48.7674109637875, 26.400111619884548, 48.7674109637875, 22.0, 56.61024238535521, 22.545524705212365, 65.31399424911184]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf197 = GraphicalForm(drawing, h, "gf197")
        self.graphForms.append(self.gf197)

        h = drawing.create_line(self.translate([37.42873546565235, 52.20333995253773, 37.42873546565235, 52.20333995253773, 42.0542397632572, 55.983903906458075, 42.0542397632572, 62.53688142658734]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf198 = GraphicalForm(drawing, h, "gf198")
        self.graphForms.append(self.gf198)

        h = drawing.create_polygon(self.translate([26.270337431144938, 45.96717074236905, 25.4760216937903, 49.12839405505662, 26.005565518693913, 70.5544631743769, 39.274818623713976, 70.5544631743769, 38.1850734914605, 49.4796410897994, 39.244161141264954, 41.400959290711384]), tags = self.tag, stipple = '', width = 1, outline = '#000000', fill = 'yellow', smooth = 1, splinesteps =  '12')
        self.gf208 = GraphicalForm(drawing, h, "gf208")
        self.graphForms.append(self.gf208)

        h = drawing.create_line(self.translate([28.083055469675855, 50.694765966748236, 28.083055469675855, 50.694765966748236]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf195 = GraphicalForm(drawing, h, "gf195")
        self.graphForms.append(self.gf195)

        h = drawing.create_oval(self.translate([23.562676269743335, 34.14818268142405, 43.886861819829775, 53.84649611633364]), tags = self.tag, stipple = '', width = 1, outline = '#000000', fill = 'white')
        self.gf194 = GraphicalForm(drawing, h, "gf194")
        self.graphForms.append(self.gf194)

        h = drawing.create_oval(self.translate([30.78126630994656, 44.39130566757757, 33.32529367363044, 47.14906954846518]), tags = self.tag, stipple = '', width = 1, outline = '#000000', fill = 'black')
        self.gf200 = GraphicalForm(drawing, h, "gf200")
        self.graphForms.append(self.gf200)

        h = drawing.create_oval(self.translate([40.41773359662645, 42.42147432408573, 42.96176096030983, 45.17923820497319]), tags = self.tag, stipple = '', width = 1, outline = '#000000', fill = 'black')
        self.gf202 = GraphicalForm(drawing, h, "gf202")
        self.graphForms.append(self.gf202)

        h = drawing.create_oval(self.translate([32.0, 63.0, 32.0, 63.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        if self.semanticObject: drawText = self.semanticObject.UnitSize.toString()
        else: drawText = "<UnitSize>"
        font = tkFont.Font( family='FreeSans', size=9, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([35.0, 92.0, 35.0, -6.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["UnitSize"] = h
        self.gf24 = GraphicalForm(drawing, h, 'gf24', fontObject=font)
        self.graphForms.append(self.gf24)

        if self.semanticObject: drawText = self.semanticObject.ID.toString()
        else: drawText = "<ID>"
        font = tkFont.Font( family='FreeSans', size=9, weight='normal', slant='roman', underline=0)
        h = drawing.create_text(self.translate([35.0, 7.0, 35.0, 9.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["ID"] = h
        self.gf33 = GraphicalForm(drawing, h, 'gf33', fontObject=font)
        self.graphForms.append(self.gf33)

        if self.semanticObject: drawText = self.semanticObject.name.toString()
        else: drawText = "<name>"
        font = tkFont.Font( family='FreeSans', size=12, weight='bold', slant='roman', underline=0)
        h = drawing.create_text(self.translate([35.0, 23.0, 35.0, 12.0])[:2], tags = self.tag, font=font, fill = 'black', anchor = 'center', text = drawText, width = '0', justify= 'left', stipple='' )
        self.attr_display["name"] = h
        self.gf34 = GraphicalForm(drawing, h, 'gf34', fontObject=font)
        self.graphForms.append(self.gf34)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'OrgUnitNew.gif' ] = ''+\
'R0lGODlhKAAoAPAAAP/MAAAAACH5BAAAAAAALAAAAAAoACgAAAInhI+py+0Po5y02ouz3rz7D4biSJbm'+\
'iabqyrbuC8fyTNf2jef6ziMFADs='        

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
