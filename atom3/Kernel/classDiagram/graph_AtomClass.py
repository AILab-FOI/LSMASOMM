from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_AtomClass(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 149, 71
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        constObj = ATOM3Constraint(atribs,"Abstract","self.semanticObject.", [], [])
        constObj.setValue(('Abstract', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'if self.semanticObject.Abstract.toString() == "True":\012   self.gf4.setVisible(1)\012else:\012   self.gf4.setVisible(0)\012\012\012'))
        self.constraintList.append(constObj)

        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_oval(self.translate([91.0, 68.0, 91.0, 68.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([146.0, 50.0, 146.0, 50.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([93.0, 3.0, 93.0, 3.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([3.0, 51.0, 3.0, 51.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([3.0, 20.0, 3.0, 20.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([21.0, 68.0, 21.0, 68.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([55.0, 68.0, 55.0, 68.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([126.0, 67.0, 126.0, 67.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([56.0, 3.0, 56.0, 3.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([146.0, 21.0, 146.0, 21.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([125.0, 3.0, 125.0, 3.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_oval(self.translate([22.0, 3.0, 22.0, 3.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)
        h = drawing.create_rectangle(self.translate([5.0, 5.0, 144.0, 22.0]), tags = self.tag, fill= 'yellow', outline= 'black', width= '1.0', stipple= '')
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)
        h = drawing.create_text(self.translate([126.0, 13.0]), tags = self.tag, fill= 'black', anchor= 'center', font= 'Helvetica -10', text= '{Abstr.}', justify= 'left', width= '0', stipple= '')
        self.gf4 = GraphicalForm(drawing, h, "gf4")
        self.graphForms.append(self.gf4)
        h = drawing.create_rectangle(self.translate([5.0, 21.0, 144.0, 65.0]), tags = self.tag, fill= 'lightyellow', outline= 'black', width= '1.0', stipple= '')
        self.gf5 = GraphicalForm(drawing, h, "gf5")
        self.graphForms.append(self.gf5)
        if self.semanticObject: drawText = self.semanticObject.ClassName.toString(25,5)
        else: drawText = "<ClassName>"
        h = drawing.create_text(self.translate([9.0, 6.0]), tags = self.tag, text = drawText, fill= 'Black', anchor= 'nw', font= 'Helvetica -11', justify= 'left', width= '0', stipple= '')
        self.attr_display["ClassName"] = h
        self.gf6 = GraphicalForm(drawing, h, "gf6")
        self.graphForms.append(self.gf6)
        if self.semanticObject: drawText = self.semanticObject.ClassAttributes.toString(25,5)
        else: drawText = "<ClassAttributes>"
        h = drawing.create_text(self.translate([9.0, 23.0]), tags = self.tag, text = drawText, fill= 'blue', anchor= 'nw', font= 'Helvetica -10', justify= 'left', width= '0', stipple= '')
        self.attr_display["ClassAttributes"] = h
        self.gf7 = GraphicalForm(drawing, h, "gf7")
        self.graphForms.append(self.gf7)

    def Abstract(self,params):
       if self.semanticObject.Abstract.toString() == "True":
          self.gf4.setVisible(1)
       else:
          self.gf4.setVisible(0)
       
       
       

    def postCondition (self, actionID, * params):
       if actionID ==  self.EDIT or actionID == self.CREATE:
         res = self.Abstract(params)
         if res: return res
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_AtomClass
