# _ buttonFromEntity.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from ASG_ERmetaMetaModel import *
from ERrelationship import *
from ERentity import *
class buttonFromEntity (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.LHS = ASG_ERmetaMetaModel(parent)

      self.obj35=ERentity(parent)

      self.obj35.constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj1 =[]
      self.obj35.constraints.setValue(lcobj1)
      self.obj35.constraints.setNone()
      self.obj35.name.setValue('')
      self.obj35.appearance.setValue( ('entity', self.obj35))
      self.obj35.appearance.setNone()
      self.obj35.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj1 =[]
      self.obj35.cardinality.setValue(lcobj1)
      self.obj35.cardinality.setNone()
      self.obj35.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj1 =[]
      self.obj35.attributes.setValue(lcobj1)
      self.obj35.attributes.setNone()
      self.obj35.GGLabel.setValue(1)
      self.obj35.graphClass_= graph_ERentity
      if parent.genGraphics:
         from graph_ERentity import *
         new_obj = graph_ERentity(210.0,276.0,self.obj35)
      else: new_obj = None
      self.obj35.graphObject_ = new_obj
      self.LHS.addNode(self.obj35)
      self.RHS = ASG_ERmetaMetaModel(parent)

      self.obj37=ERentity(parent)

      self.obj37.constraints.setActionFlags([ 1, 1, 1, 0])
      lcobj1 =[]
      self.obj37.constraints.setValue(lcobj1)
      self.obj37.name.setValue('entity0')
      self.obj37.appearance.setValue( ('entity0', self.obj37))
      self.obj37.cardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj1 =[]
      self.obj37.cardinality.setValue(lcobj1)
      self.obj37.cardinality.setNone()
      self.obj37.attributes.setActionFlags([ 1, 1, 1, 0])
      lcobj1 =[]
      self.obj37.attributes.setValue(lcobj1)
      self.obj37.GGLabel.setValue(1)
      self.obj37.graphClass_= graph_ERentity
      if parent.genGraphics:
         from graph_ERentity import *
         new_obj = graph_ERentity(140.0,224.0,self.obj37)
      else: new_obj = None
      self.obj37.graphObject_ = new_obj
      self.obj370= AttrCalc()
      self.obj370.Copy=ATOM3Boolean()
      self.obj370.Copy.setValue(('Copy from LHS', 1))
      self.obj370.Copy.config = 0
      self.obj370.Specify=ATOM3Constraint()
      self.obj370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj37.GGset2Any['constraints']= self.obj370
      self.obj371= AttrCalc()
      self.obj371.Copy=ATOM3Boolean()
      self.obj371.Copy.setValue(('Copy from LHS', 1))
      self.obj371.Copy.config = 0
      self.obj371.Specify=ATOM3Constraint()
      self.obj371.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj37.GGset2Any['name']= self.obj371
      self.obj372= AttrCalc()
      self.obj372.Copy=ATOM3Boolean()
      self.obj372.Copy.setValue(('Copy from LHS', 1))
      self.obj372.Copy.config = 0
      self.obj372.Specify=ATOM3Constraint()
      self.obj372.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj37.GGset2Any['appearance']= self.obj372
      self.obj373= AttrCalc()
      self.obj373.Copy=ATOM3Boolean()
      self.obj373.Copy.setValue(('Copy from LHS', 1))
      self.obj373.Copy.config = 0
      self.obj373.Specify=ATOM3Constraint()
      self.obj373.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj37.GGset2Any['attributes']= self.obj373
      self.RHS.addNode(self.obj37)
   def condition(self, graphID, isograph, atom3i):
      entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return entity.visited == 0
      
      

   def action(self, graphID, isograph, atom3i):
      entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      entity.visited = 1
      posx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)
      self.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1
      ename = entity.name.toString()
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
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      

