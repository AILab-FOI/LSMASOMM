# _ buttonFromRelationship.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from ASG_ERmetaMetaModel import *
from ERrelationship import *
from ERentity import *
class buttonFromRelationship (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.LHS = ASG_ERmetaMetaModel(parent)

      self.obj42=ERrelationship(parent)

      self.obj42.constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj1 =[]
      self.obj42.constraints.setValue(lcobj1)
      self.obj42.constraints.setNone()
      self.obj42.name.setValue('')
      self.obj42.appearance.setNone()
      self.obj42.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj1 =[]
      self.obj42.cardinality.setValue(lcobj1)
      self.obj42.cardinality.setNone()
      self.obj42.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj1 =[]
      self.obj42.attributes.setValue(lcobj1)
      self.obj42.attributes.setNone()
      self.obj42.GGLabel.setValue(1)
      self.obj42.graphClass_= graph_ERrelationship
      if parent.genGraphics:
         from graph_ERrelationship import *
         new_obj = graph_ERrelationship(163.0,272.0,self.obj42)
      else: new_obj = None
      self.obj42.graphObject_ = new_obj
      self.LHS.addNode(self.obj42)
      self.RHS = ASG_ERmetaMetaModel(parent)

      self.obj44=ERrelationship(parent)

      self.obj44.constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj1 =[]
      self.obj44.constraints.setValue(lcobj1)
      self.obj44.name.setValue('relationship0')
      self.obj44.appearance.setValue( ('relationship0', self.obj44))
      self.obj44.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj1 =[]
      self.obj44.cardinality.setValue(lcobj1)
      self.obj44.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj1 =[]
      self.obj44.attributes.setValue(lcobj1)
      self.obj44.GGLabel.setValue(1)
      self.obj44.graphClass_= graph_ERrelationship
      if parent.genGraphics:
         from graph_ERrelationship import *
         new_obj = graph_ERrelationship(185.0,190.0,self.obj44)
      else: new_obj = None
      self.obj44.graphObject_ = new_obj
      self.obj440= AttrCalc()
      self.obj440.Copy=ATOM3Boolean()
      self.obj440.Copy.setValue(('Copy from LHS', 1))
      self.obj440.Copy.config = 0
      self.obj440.Specify=ATOM3Constraint()
      self.obj440.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['constraints']= self.obj440
      self.obj441= AttrCalc()
      self.obj441.Copy=ATOM3Boolean()
      self.obj441.Copy.setValue(('Copy from LHS', 1))
      self.obj441.Copy.config = 0
      self.obj441.Specify=ATOM3Constraint()
      self.obj441.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['name']= self.obj441
      self.obj442= AttrCalc()
      self.obj442.Copy=ATOM3Boolean()
      self.obj442.Copy.setValue(('Copy from LHS', 1))
      self.obj442.Copy.config = 0
      self.obj442.Specify=ATOM3Constraint()
      self.obj442.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['appearance']= self.obj442
      self.obj443= AttrCalc()
      self.obj443.Copy=ATOM3Boolean()
      self.obj443.Copy.setValue(('Copy from LHS', 1))
      self.obj443.Copy.config = 0
      self.obj443.Specify=ATOM3Constraint()
      self.obj443.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['cardinality']= self.obj443
      self.obj444= AttrCalc()
      self.obj444.Copy=ATOM3Boolean()
      self.obj444.Copy.setValue(('Copy from LHS', 1))
      self.obj444.Copy.config = 0
      self.obj444.Specify=ATOM3Constraint()
      self.obj444.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj44.GGset2Any['attributes']= self.obj444
      self.RHS.addNode(self.obj44)
   def condition(self, graphID, isograph, atom3i):
      entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return entity.visited == 0
      
      
      
      
      

   def action(self, graphID, isograph, atom3i):
      entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      entity.visited = 1
      ename = entity.name.toString()
      posx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)
      self.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1
      file = self.graphRewritingSystem.file
      file.write("   self.globalPrecondition(rootNode)\n\n")
      file.write("   self.obj"+ename+"=ButtonConfig(self)\n")
      file.write("   self.obj"+ename+".Contents.Text.setValue('New "+ename+"')\n")
      file.write("   self.obj"+ename+".Contents.Image.setValue('')\n")
      file.write("   self.obj"+ename+".Contents.lastSelected= 'Text'\n")
      file.write("   self.obj"+ename+".Drawing_Mode.setValue(1)\n")
      file.write("   self.obj"+ename+".Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), ")
      file.write("(['PREcondition', 'POSTcondition'], 1),")
      file.write("(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], ")
      file.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")
      file.write("'# This method has as parameters:\\n")
      file.write("#   - wherex : X Position in window coordinates where the user clicked.\\n")
      file.write("#   - wherey : Y Position in window coordinates where the user clicked.\\n")
      file.write("newPlace = self.createNew"+ename+" (self, wherex, wherey)\\n'))\n")
      file.write("   self.obj"+ename+".graphClass_= graph_ButtonConfig\n")
      file.write("   if self.genGraphics:\n")
      file.write("      from graph_ButtonConfig import *\n")
      file.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+ename+")\n")
      file.write("      new_obj.DrawObject(self.UMLmodel)\n")
      file.write("      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)\n")
      file.write("   else: new_obj = None\n")
      file.write("   self.obj"+ename+".graphObject_ = new_obj\n")
      file.write("   rootNode.addNode(self.obj"+ename+")\n")
      file.write("   self.globalAndLocalPostcondition(self.obj"+ename+", rootNode)\n")
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      

