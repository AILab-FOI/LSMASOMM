from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_AtomInheritance_2ndLink(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 28, 30
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        constObj = ATOM3Constraint(atribs,"lift","self.semanticObject.", [], [])
        constObj.setValue(('lift', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]), 'self.gf0.lift()\012\012\012'))
        self.constraintList.append(constObj)

        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_polygon(self.translate([9.0, 2.0, 2.0, 22.0, 19.0, 22.0, 19.0, 22.0]), tags = self.tag, fill= 'lightyellow', outline= 'black', smooth= 0, splinesteps= '12', width= '1.0', stipple= '')
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)
        h = drawing.create_oval(self.translate([11.0, 15.0, 11.0, 15.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)

    def lift(self,params):
       self.gf0.lift()
       
       
       

    def postCondition (self, actionID, * params):
       if actionID ==  self.CREATE or actionID == self.CONNECT:
         res = self.lift(params)
         if res: return res
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_AtomInheritance_2ndLink
