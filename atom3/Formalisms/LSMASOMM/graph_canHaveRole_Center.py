"""
__graph_canHaveRole_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_canHaveRole_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 36, 64
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
        h = drawing.create_oval(self.translate([-0.37657625849249143, -10.432160804019986, -0.37657625849249143, -10.432160804019986]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        h = drawing.create_line(self.translate([-7.115269725828995, -1.447236180904497, -7.115269725828995, -1.447236180904497, -6.45358923032785, 30.0, -4.137707496075507, 29.21381909547773]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'bevel', arrow = 'none', arrowshape = (15,15,3))
        self.gf186 = GraphicalForm(drawing, h, "gf186")
        self.graphForms.append(self.gf186)

        h = drawing.create_line(self.translate([4.464138945433547, -2.79980547900783, 4.464138945433547, -2.79980547900783, 5.12581944093489, 28.647430701896496, 7.441701175187291, 27.861249797373716]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'bevel', arrow = 'none', arrowshape = (15,15,3))
        self.gf188 = GraphicalForm(drawing, h, "gf188")
        self.graphForms.append(self.gf188)

        h = drawing.create_line(self.translate([-6.45358923032785, 26.618576754741014, -6.45358923032785, 26.618576754741014]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf189 = GraphicalForm(drawing, h, "gf189")
        self.graphForms.append(self.gf189)

        h = drawing.create_line(self.translate([-6.45358923032785, 2.610471713405502, -6.45358923032785, 2.610471713405502, -9.76199170783218, 7.034038516219425, -9.76199170783218, 16.812449343491608]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf197 = GraphicalForm(drawing, h, "gf197")
        self.graphForms.append(self.gf197)

        h = drawing.create_line(self.translate([4.794979193184815, 4.301183336035805, 4.794979193184815, 4.301183336035805, 8.765062166188429, 7.546051704136005, 8.765062166188429, 13.17049020884383]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf198 = GraphicalForm(drawing, h, "gf198")
        self.graphForms.append(self.gf198)

        h = drawing.create_polygon(self.translate([-6.355248835410862, -1.7853785054312539, -7.0370122024223605, 0.9279080985962622, -6.582503291080826, 19.31796174811052, 4.806532893361236, 19.31796174811052, 3.8712016697555782, 1.2293843879326118, 4.780219492435492, -5.7045702668024205]), tags = self.tag, stipple = '', width = 1, outline = '#000000', fill = 'yellow', smooth = 1, splinesteps =  '12')
        self.gf208 = GraphicalForm(drawing, h, "gf208")
        self.graphForms.append(self.gf208)

        h = drawing.create_line(self.translate([-4.799387991577305, 2.272329388879939, -4.799387991577305, 2.272329388879939]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf195 = GraphicalForm(drawing, h, "gf195")
        self.graphForms.append(self.gf195)

        h = drawing.create_oval(self.translate([-8.679241806104017, -11.929648241205996, 8.765062166188429, 4.977467985086847]), tags = self.tag, stipple = '', width = 1, outline = '#000000', fill = 'white')
        self.gf194 = GraphicalForm(drawing, h, "gf194")
        self.graphForms.append(self.gf194)

        h = drawing.create_oval(self.translate([-2.483506257324265, -3.1379478035334927, -0.2999606221711133, -0.7709515318523472]), tags = self.tag, stipple = '', width = 1, outline = '#000000', fill = 'black')
        self.gf200 = GraphicalForm(drawing, h, "gf200")
        self.graphForms.append(self.gf200)

        h = drawing.create_oval(self.translate([5.787499936435879, -4.828659426163554, 7.971045571588604, -2.4616631544824656]), tags = self.tag, stipple = '', width = 1, outline = '#000000', fill = 'black')
        self.gf202 = GraphicalForm(drawing, h, "gf202")
        self.graphForms.append(self.gf202)

        h = drawing.create_line(self.translate([-5.30829272270347, -11.947717791502427, -5.30829272270347, -11.947717791502427, -6.047389802879934, -8.067458120570677, -8.080545993926705, -7.580500286965389]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf221 = GraphicalForm(drawing, h, "gf221")
        self.graphForms.append(self.gf221)

        h = drawing.create_line(self.translate([3.8296929250055882, -11.931036352510148, 3.8296929250055882, -11.746262082465591, 4.5687900051820804, -8.789873761753256, 6.7860812457175825, -7.681228141487111]), tags = self.tag, stipple = '', width = 1, fill = 'black', smooth = 'False', splinesteps =  '12', capstyle = 'butt', joinstyle = 'round', arrow = 'none', arrowshape = (15,15,3))
        self.gf222 = GraphicalForm(drawing, h, "gf222")
        self.graphForms.append(self.gf222)

        h = drawing.create_polygon(self.translate([-6.3665260072361605, -13.427135678392006, -9.431287789023798, -9.141367090879257, -16.398773508799792, -4.485170246898065, 2.6183986158794426, -2.6452261306532705, 16.870272412561235, -6.4970548904649945, 7.939619962998933, -9.94031145391699, 6.2123684651253654, -13.427135678392006, 4.4153835405022335, -18.81809045226123, 2.6183986158794426, -22.412060301507353, -6.3665260072361605, -29.600000000000023, -4.569541082613171, -22.412060301507353]), tags = self.tag, stipple = '', width = 1, outline = '#000000', fill = 'royalblue', smooth = 1, splinesteps =  '12')
        self.gf217 = GraphicalForm(drawing, h, "gf217")
        self.graphForms.append(self.gf217)



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'OrgUnitRole.gif' ] = ''+\
'R0lGODlhJwA2APfyAFBRTVFTT1JUT1pZTlFUUFJVUVVVUFRWUVRWUlVYUlxbUVxeU11fV11hVmJjVGNj'+\
'VWRkVGRkVWZnV2FiWmJjW3t7X3x9X1hkY2xtYm5uYn5/YoF/b4GCYo+PZZeVZJeVZZ2ZZoeFcY6Kdo+Z'+\
'dYqXe4yYeoyafY+df4+ef5CZdZCadJCYdpWcdpiUfZKee5GffaOfZ52hcZ6hcJ+hcJ6hcaChb6Cib6Gj'+\
'b7Cta7Ksa7WvabWuarSvarWvarGtbLKtbLuuarirb7qtbLWwarexa7WxbLiwaLqzabqya7qza76waLu0'+\
'abq0ary0ab62abi0bqCicKSlcLitdLitdbqvf7ywc7+ycsC1ZcC2Zce8Z8m6ZMm6Zci5Zsm8Zcu9Zcu+'+\
'Zsy8ZM2/ZcG0asu/aMq/ac6/a8u8bMu9b8Czcc7AZNLDZdHCZ9XFZNXFZtTEZ9fIZ9fJZ9jIZ9vMZtzM'+\
'ZtzNZ9/OZ9bIaN/OaOHQZuTSZufUZ+XTaOXVaObVaOfVaOjWaOjXaOrZaOvZaezZaOzaae3baW6HhG2S'+\
'mXCZonqio3+lonyyvH2yvH21wXy0wn21wn22xH23xX+4w4eYgYeagoiagoibgo6dgIKaioOaioObioKd'+\
'joOdj4GflIGflYCfl4Gglbash7qwhrmxk7uzkr63lb+3lbqzm7u1n4GppoGusICvsYGytYG1vYG2voG3'+\
'voG2v764pMO7l8K5m8K7n8K6oMO9p8O9q8W/rcvCnczDnc7EncnFtMzHu+DWqeDVqubarendr4G3wIG5'+\
'wYC5xIG6xIK8xYG8x4K9yoC9zIG/zYLAzYHAzoLBzoPBzoLBz4HA0ILB0ILC0YXI2IXJ2IbJ2YfL3IXN'+\
'3YbM3IbM3YbN3YfN3YfM3obN3ofN3ofN34bO3ofO3ojN3YjM3tLPxdPPxdfVyuDe2ufm5Orp5+/t7O/u'+\
'7vDv7/b19fn5+fv7+/79/f7+/v///wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'+\
'ACH5BAEAAPMALAAAAAAnADYAAAj+AOcJHEiwoLeDCBEWXMiw4TxxCSNGdEhxoERv0SA5ghTtYkWGEZuB'+\
'QiFjSJY0WXbIQAGq2cSPAhO2ouQjUKGbOHECykFpWEKYCKtpYpKzqNEkmqoppIiwWIo+RqPm7JOi2LeD'+\
'DiF6awVFqtecMlotNXjQWNevaAtBOXbQ2sKD1UaknbtCqTey3jRBnYu2j6aD3wgebJWE71wiPu/GPGjJ'+\
'MF9LSw828+F4rg+Xig+CAlS5aB4qtWahuZlHEVaEKDoXDSWvtToxgwZdkijDcR0hQdjcZHOudWtaN2WE'+\
'HGLYzK138shJKaSFnW95tm4O6YiwURi+gFA9N7dGD67nom7+aomUkNEavlrSPZe3/Ayvd+xG1bm5ZlFC'+\
'R9fngkG3fnkhPGJwYdNNYTSSUCREzQXIKc+Vc14hgxylTERRGFZGLO2808toXkFhTUQvOJYHEEDMgdYL'+\
'Ch3USYSqeRUIJ1jNc1AxTrDYolFNEBPjVd6UcKNUJox1kCFp/FgUGavEuNghFRiJUyCWfKiYQNd4cwgB'+\
'IDipFmZkXbnADjaqNgQrB4nTZQABOFBYi0+kMpZFVhIgZwM1qBZFkkoKFqecAQjAARyGxUECMm/qeSWf'+\
'aELQAaBf2cGCm96EE1hDBx1KAJoHoLmABh9cMYcghQAyxxUfaJBINR9+Y6ZDlcrJ56u8lwKgwAMSPDAA'+\
'AGhG8s2uH7XqagAhhOCqqwUQUKyr0fDa656uyhIMKRQMK62cusIkI7OutgCMLyJMO6wyky5r6bAY5BJM'+\
'KRQUcKyrCJBnra/eavuLCOu6OuG72E6bwS7nNiCtu0B9M663BlyiSwLDItARvgN7SwAC0hYgTbgVwevw'+\
'xdUCle/F0rZLMVMbc8wuuAyLfDHJGjdsspzJlrzytAAvi8gFNNds8803u4TvRTzzbG2VPQMW9JQOBQQA'+\
'Ow=='        

        imageDict[ 'canHaveRoleNew.gif' ] = ''+\
'R0lGODlhFAAUAPEAAP/MAMC/f6C5v4Cz/yH5BAAAAAAALAAAAAAUABQAAAI3nI+pyyoBo5QCBYCz1sHu'+\
'n3XHBX6iQZacp65j66JwyM7nkMJ33u4z5vsFbTUd4jFJQiqNptNZAAA7'        

        return imageDict

new_class = graph_canHaveRole_Center
