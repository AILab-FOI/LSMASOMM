from graphEntity          import *
from GraphicalForm   import *
from ATOM3Constraint import *

class graph_AtomAssociation_Center(graphEntity):

    def __init__(self, x, y, semObject = None):
        self.semanticObject = semObject
        self.sizeX, self.sizeY = 130, 116
        graphEntity.__init__(self, x, y)
        self.ChangesAtRunTime = 0
        self.constraintList = []
        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()
        else: atribs = None
        constObj = ATOM3Constraint(atribs,"Hide","self.semanticObject.", [], [])
        constObj.setValue(('Hide', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0]), 'if self.semanticObject.AssociationAttributes.getValue() == []:\012   self.gf0.setVisible(0)\012   self.gf1.setVisible(0)\012   self.gf6.setVisible(0)\012   self.gf3.setVisible(0)\012   self.gf4.setVisible(0)\012   self.gf5.setVisible(1)\012else:\012   self.gf0.setVisible(1)\012   self.gf1.setVisible(1)\012   self.gf6.setVisible(1)\012   self.gf3.setVisible(1)\012   self.gf4.setVisible(1)\012   self.gf5.setVisible(0)\012\012\012\012\012'))
        self.constraintList.append(constObj)

        self.graphForms = []

    def DrawObject(self, drawing, showGG = 0):
        self.dc = drawing
        if showGG and self.semanticObject: self.drawGGLabel(drawing)
        h = drawing.create_rectangle(self.translate([1.0, 33.0, 129.0, 53.0]), tags = self.tag, fill= 'yellow', outline= 'black', width= '1.0', stipple= '')
        self.gf0 = GraphicalForm(drawing, h, "gf0")
        self.graphForms.append(self.gf0)
        h = drawing.create_rectangle(self.translate([1.0, 52.0, 129.0, 115.0]), tags = self.tag, fill= 'lightyellow', outline= 'black', width= '1.0', stipple= '')
        self.gf1 = GraphicalForm(drawing, h, "gf1")
        self.graphForms.append(self.gf1)
        h = drawing.create_line(self.translate([61.0, 32.0, 61.0, 17.0]), tags = self.tag, fill= 'black', joinstyle= 'round', smooth= 0, capstyle= 'butt', arrow= 'none', arrowshape= '8 10 3', splinesteps= '12', width= '1.0', stipple= '')
        self.gf4 = GraphicalForm(drawing, h, "gf4")
        self.graphForms.append(self.gf4)
        h = drawing.create_oval(self.translate([61.0, 16.0, 61.0, 16.0]), tags = (self.tag, "connector"), fill= 'red', outline= 'black', width= '1.0', stipple= '')
        self.connectors.append(h)

        if self.semanticObject: drawText = self.semanticObject.AssociationName.toString(25,5)
        else: drawText = "<AssociationName>"
        h = drawing.create_text(self.translate([66.0, 8.0]), tags = self.tag, text = drawText, fill= 'black', anchor= 'center', font= '{Helvetica} 10', justify= 'left', width= '0', stipple= '')
        self.attr_display["AssociationName"] = h
        self.gf5 = GraphicalForm(drawing, h, "gf6")
        self.graphForms.append(self.gf5)
       
        #h = drawing.create_text(self.translate([66.0, 8.0]), tags = self.tag, fill= 'black', anchor= 'center', font= '{Helvetica} 10', text= '<AssociationName>', justify= 'left', width= '0', stipple= '')
        #self.gf5 = GraphicalForm(drawing, h, "gf5")
        #self.graphForms.append(self.gf5)
        if self.semanticObject: drawText = self.semanticObject.AssociationName.toString(25,5)
        else: drawText = "<AssociationName>"
        h = drawing.create_text(self.translate([66.0, 42.0]), tags = self.tag, text = drawText, fill= 'black', anchor= 'center', font= '{Helvetica} 10', justify= 'left', width= '0', stipple= '')
        self.attr_display["AssociationName"] = h
        self.gf6 = GraphicalForm(drawing, h, "gf6")
        self.graphForms.append(self.gf6)
        if self.semanticObject: drawText = self.semanticObject.AssociationAttributes.toString(25,5)
        else: drawText = "<AssociationAttributes>"
        h = drawing.create_text(self.translate([5.0, 54.0]), tags = self.tag, text = drawText, fill= 'blue', anchor= 'nw', font= '{MS Sans Serif} 8', justify= 'left', width= '0', stipple= '')
        self.attr_display["AssociationAttributes"] = h
        self.gf3 = GraphicalForm(drawing, h, "gf3")
        self.graphForms.append(self.gf3)

    def Hide(self,params):
       if self.semanticObject.AssociationAttributes.getValue() == []:
          self.gf0.setVisible(0)
          self.gf1.setVisible(0)
          self.gf6.setVisible(0)
          self.gf3.setVisible(0)
          self.gf4.setVisible(0)
          self.gf5.setVisible(1)
       else:
          self.gf0.setVisible(1)
          self.gf1.setVisible(1)
          self.gf6.setVisible(1)
          self.gf3.setVisible(1)
          self.gf4.setVisible(1)
          self.gf5.setVisible(0)
       
       
       
       
       

    def postCondition (self, actionID, * params):
       if actionID ==  self.EDIT or actionID == self.CREATE:
         res = self.Hide(params)
         if res: return res
       return None

    def preCondition (self, actionID, * params):
       return None


new_class = graph_AtomAssociation_Center
