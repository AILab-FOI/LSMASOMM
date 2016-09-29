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
        self.sizeX, self.sizeY = 39, 54
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
        h = drawing.create_oval(self.translate([0.0, 2.0, 0.0, 2.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )

        self.image_gf169 = PhotoImage(format='gif',data=self.imageDict['OrgUnitRole.gif' ])
        h = drawing.create_image(self.translate([0.0, 0.0]), tags = self.tag, image = self.image_gf169)
        self.gf169 = GraphicalForm(drawing, h, 'gf169', 'OrgUnitRole.gif')
        self.graphForms.append(self.gf169)



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

        return imageDict

new_class = graph_canHaveRole_Center
