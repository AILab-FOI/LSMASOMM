"""
__graph_isPartOfObjective_Center.py___________________________________________________________

Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION
______________________________________________________________________________________________
"""
import tkFont

from graphEntity     import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_isPartOfObjective_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 50, 52
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
        self.image_gf204 = PhotoImage(format='gif',data=self.imageDict['isPartOfObjective.gif' ])
        h = drawing.create_image(self.translate([0.0, 0.0]), tags = self.tag, image = self.image_gf204)
        self.gf204 = GraphicalForm(drawing, h, 'gf204', 'isPartOfObjective.gif')
        self.graphForms.append(self.gf204)

        h = drawing.create_oval(self.translate([-5.0, 3.0, -5.0, 3.0]), tags = (self.tag, 'connector'), outline = '', fill = '' )
        self.connectors.append( h )



    def postCondition( self, actionID, * params):
        return None

    def preCondition( self, actionID, * params):
        return None

    def getImageDict( self ):
        imageDict = dict()

        imageDict[ 'isPartOfObjective.gif' ] = ''+\
'R0lGODlhMgA0AKECAP99d/9/ef///////yH5BAEKAAIALAAAAAAyADQAAAK+lI8pwawPo0SgtYmzqvbq'+\
'P3UWSEKiV6bG6agqG7juKcsdUM9j/u48SftlYJ0c8YgshpJMIqYJDUqiVFSkWn1io9pts+tNgsPHMRlm'+\
'Pkuv6vIS1baaWon4kH3eyPHkw5ofJ5IWSAdIuKdgt/D3oFanJMHRl9jC0dgGhuOnOHUo+ObJoNnZVCH5'+\
'BYp0KZaKZsgy+Pl6E+szC3lrm1s459Yqu8u76vQL3EtM6nvsmow87LwMvcnazFIRAZCdDYtRAAA7'        

        imageDict[ 'Process.gif' ] = ''+\
'R0lGODlhMgAdAIABAACAAP///yH+EUNyZWF0ZWQgd2l0aCBHSU1QACH5BAEKAAEALAAAAAAyAB0AAAKR'+\
'hG+hu3gMg0uxzaomrRpgqX2deJFlNGIpF6ote6Iv1HmwY+JuTM89b/EFdTfiz3hE5JRFpkyYWSWd080T'+\
'CIJmsVvk0BvV1prUb9n8IFsZ4yu4Zquuw9y2+9zF2+VxttQvFlj3hzaXl3ZnSId32Ac4CAm2iJjoWLgT'+\
'yUh4iakpKNnYSSm3pHhYaroZKmr5OMpQAAA7'        

        return imageDict

new_class = graph_isPartOfObjective_Center
