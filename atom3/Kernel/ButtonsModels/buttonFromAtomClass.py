# _ buttonFromAtomClass.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from AtomAssociation import *
from ASG_ClassDiagramB import *
from AtomInheritance import *
from AtomClass import *
class buttonFromAtomClass (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_ClassDiagramB(parent)

      self.obj37=AtomClass(parent)

      self.obj37.ClassName.setValue('')
      self.obj37.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj37.ClassAttributes.setValue(lcobj2)
      self.obj37.ClassAttributes.setNone()
      self.obj37.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj37.ClassConstraints.setValue(lcobj2)
      self.obj37.ClassConstraints.setNone()
      self.obj37.ClassAppearance.setValue( ('MyClass', self.obj37))
      self.obj37.ClassAppearance.setNone()
      self.obj37.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj37.ClassCardinality.setValue(lcobj2)
      self.obj37.ClassCardinality.setNone()
      self.obj37.GGLabel.setValue(1)
      self.obj37.graphClass_= graph_AtomClass
      if parent.genGraphics:
         from graph_AtomClass import *
         new_obj = graph_AtomClass(51.0,24.0,self.obj37)
      else: new_obj = None
      self.obj37.graphObject_ = new_obj
      self.LHS.addNode(self.obj37)
      self.RHS = ASG_ClassDiagramB(parent)

      self.obj39=AtomClass(parent)

      self.obj39.ClassName.setValue('MyClass0')
      self.obj39.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj39.ClassAttributes.setValue(lcobj2)
      self.obj39.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj39.ClassConstraints.setValue(lcobj2)
      self.obj39.ClassAppearance.setValue( ('MyClass0', self.obj39))
      self.obj39.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj39.ClassCardinality.setValue(lcobj2)
      self.obj39.GGLabel.setValue(1)
      self.obj39.graphClass_= graph_AtomClass
      if parent.genGraphics:
         from graph_AtomClass import *
         new_obj = graph_AtomClass(54.0,52.0,self.obj39)
      else: new_obj = None
      self.obj39.graphObject_ = new_obj
      self.obj390= AttrCalc()
      self.obj390.Copy=ATOM3Boolean()
      self.obj390.Copy.setValue(('Copy from LHS', 1))
      self.obj390.Copy.config = 0
      self.obj390.Specify=ATOM3Constraint()
      self.obj390.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj39.GGset2Any['ClassName']= self.obj390
      self.obj391= AttrCalc()
      self.obj391.Copy=ATOM3Boolean()
      self.obj391.Copy.setValue(('Copy from LHS', 1))
      self.obj391.Copy.config = 0
      self.obj391.Specify=ATOM3Constraint()
      self.obj391.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj39.GGset2Any['ClassConstraints']= self.obj391
      self.obj392= AttrCalc()
      self.obj392.Copy=ATOM3Boolean()
      self.obj392.Copy.setValue(('Copy from LHS', 1))
      self.obj392.Copy.config = 0
      self.obj392.Specify=ATOM3Constraint()
      self.obj392.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj39.GGset2Any['ClassAttributes']= self.obj392
      self.obj393= AttrCalc()
      self.obj393.Copy=ATOM3Boolean()
      self.obj393.Copy.setValue(('Copy from LHS', 1))
      self.obj393.Copy.config = 0
      self.obj393.Specify=ATOM3Constraint()
      self.obj393.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj39.GGset2Any['ClassAppearance']= self.obj393
      self.obj394= AttrCalc()
      self.obj394.Copy=ATOM3Boolean()
      self.obj394.Copy.setValue(('Copy from LHS', 1))
      self.obj394.Copy.config = 0
      self.obj394.Specify=ATOM3Constraint()
      self.obj394.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj39.GGset2Any['ClassCardinality']= self.obj394
      self.RHS.addNode(self.obj39)
   def condition(self, graphID, isograph, atom3i):
      myclass = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return myclass.visited == 0
      
      
      

   def action(self, graphID, isograph, atom3i):
      myclass = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      myclass.visited = 1
      posx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)
      self.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1
      cname = myclass.ClassName.toString()
      file = self.graphRewritingSystem.file
      file.write("   self.globalPrecondition(rootNode)\n\n")
      file.write("   self.obj"+cname+"=ButtonConfig(self)\n")
      file.write("   self.obj"+cname+".Contents.Text.setValue('New "+cname+"')\n")
      file.write("   self.obj"+cname+".Contents.Image.setValue('')\n")
      file.write("   self.obj"+cname+".Contents.lastSelected= 'Text'\n")
      file.write("   self.obj"+cname+".Drawing_Mode.setValue(1)\n")
      file.write("   self.obj"+cname+".Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), ")
      file.write("(['PREcondition', 'POSTcondition'], 1),")
      file.write("(['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], ")
      file.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")
      file.write("'# This method has as parameters:\\n")
      file.write("#   - wherex : X Position in window coordinates where the user clicked.\\n")
      file.write("#   - wherey : Y Position in window coordinates where the user clicked.\\n")
      file.write("newPlace = self.createNew"+cname+" (self, wherex, wherey)\\n'))\n")
      file.write("   self.obj"+cname+".graphClass_= graph_ButtonConfig\n")
      file.write("   if self.genGraphics:\n")
      file.write("      from graph_ButtonConfig import *\n")
      file.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+cname+")\n")
      file.write("      new_obj.DrawObject(self.UMLmodel)\n")
      file.write("      self.UMLmodel.addtag_withtag('ButtonConfig', new_obj.tag)\n")
      file.write("   else: new_obj = None\n")
      file.write("   self.obj"+cname+".graphObject_ = new_obj\n")
      file.write("   rootNode.addNode(self.obj"+cname+")\n")
      file.write("   self.globalAndLocalPostcondition(self.obj"+cname+", rootNode)\n")
      
      

