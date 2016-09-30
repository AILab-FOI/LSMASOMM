from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('CD_to_ER')
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('inheritance_semantics')
   cobj0.Order=ATOM3Integer(1)

   from AtomClass import *
   from AtomInheritance import *
   from ASG_ClassDiagramB import *
   from AtomAssociation import *

   cobj0.LHS = ASG_ClassDiagramB(self)

   self.obj26=AtomClass(self)

   self.obj26.ClassName.setValue('')
   self.obj26.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj1 =[]
   self.obj26.ClassCardinality.setValue(lcobj1)
   self.obj26.ClassCardinality.setNone()
   self.obj26.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj26.ClassConstraints.setValue(lcobj1)
   self.obj26.ClassConstraints.setNone()
   self.obj26.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj26.ClassAttributes.setValue(lcobj1)
   self.obj26.ClassAttributes.setNone()
   self.obj26.ClassAppearance.setValue( ('MyClass', self.obj26))
   self.obj26.ClassAppearance.setNone()
   self.obj26.GGLabel.setValue(1)
   self.obj26.graphClass_= graph_AtomClass
   if self.genGraphics:
      from graph_AtomClass import *
      new_obj = graph_AtomClass(90.0,43.0,self.obj26)
   else: new_obj = None
   self.obj26.graphObject_ = new_obj
   cobj0.LHS.addNode(self.obj26)

   self.obj27=AtomClass(self)

   self.obj27.ClassName.setValue('')
   self.obj27.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj1 =[]
   self.obj27.ClassCardinality.setValue(lcobj1)
   self.obj27.ClassCardinality.setNone()
   self.obj27.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj27.ClassConstraints.setValue(lcobj1)
   self.obj27.ClassConstraints.setNone()
   self.obj27.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj27.ClassAttributes.setValue(lcobj1)
   self.obj27.ClassAttributes.setNone()
   self.obj27.ClassAppearance.setValue( ('MyClass', self.obj27))
   self.obj27.ClassAppearance.setNone()
   self.obj27.GGLabel.setValue(2)
   self.obj27.graphClass_= graph_AtomClass
   if self.genGraphics:
      from graph_AtomClass import *
      new_obj = graph_AtomClass(84.0,245.0,self.obj27)
   else: new_obj = None
   self.obj27.graphObject_ = new_obj
   cobj0.LHS.addNode(self.obj27)

   self.obj28=AtomInheritance(self)

   self.obj28.GGLabel.setValue(0)
   self.obj28.graphClass_= graph_AtomInheritance
   if self.genGraphics:
      from graph_AtomInheritance import *
      new_obj = graph_AtomInheritance(162.0,212.0,self.obj28)
   else: new_obj = None
   self.obj28.graphObject_ = new_obj
   cobj0.LHS.addNode(self.obj28)
   self.obj27.out_connections_.append(self.obj28)
   self.obj28.in_connections_.append(self.obj27)
   self.obj28.out_connections_.append(self.obj26)
   self.obj26.in_connections_.append(self.obj28)
   cobj0.RHS = ASG_ClassDiagramB(self)

   self.obj30=AtomClass(self)

   self.obj30.ClassName.setValue('MyClass0')
   self.obj30.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj1 =[]
   self.obj30.ClassCardinality.setValue(lcobj1)
   self.obj30.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj30.ClassConstraints.setValue(lcobj1)
   self.obj30.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj30.ClassAttributes.setValue(lcobj1)
   self.obj30.ClassAppearance.setValue( ('MyClass0', self.obj30))
   self.obj30.GGLabel.setValue(1)
   self.obj30.graphClass_= graph_AtomClass
   if self.genGraphics:
      from graph_AtomClass import *
      new_obj = graph_AtomClass(88.0,44.0,self.obj30)
   else: new_obj = None
   self.obj30.graphObject_ = new_obj
   self.obj300= AttrCalc()
   self.obj300.Copy=ATOM3Boolean()
   self.obj300.Copy.setValue(('Copy from LHS', 1))
   self.obj300.Copy.config = 0
   self.obj300.Specify=ATOM3Constraint()
   self.obj300.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj30.GGset2Any['ClassName']= self.obj300
   self.obj301= AttrCalc()
   self.obj301.Copy=ATOM3Boolean()
   self.obj301.Copy.setValue(('Copy from LHS', 1))
   self.obj301.Copy.config = 0
   self.obj301.Specify=ATOM3Constraint()
   self.obj301.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj30.GGset2Any['ClassCardinality']= self.obj301
   self.obj302= AttrCalc()
   self.obj302.Copy=ATOM3Boolean()
   self.obj302.Copy.setValue(('Copy from LHS', 1))
   self.obj302.Copy.config = 0
   self.obj302.Specify=ATOM3Constraint()
   self.obj302.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj30.GGset2Any['ClassAttributes']= self.obj302
   self.obj303= AttrCalc()
   self.obj303.Copy=ATOM3Boolean()
   self.obj303.Copy.setValue(('Copy from LHS', 1))
   self.obj303.Copy.config = 0
   self.obj303.Specify=ATOM3Constraint()
   self.obj303.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj30.GGset2Any['ClassConstraints']= self.obj303
   self.obj304= AttrCalc()
   self.obj304.Copy=ATOM3Boolean()
   self.obj304.Copy.setValue(('Copy from LHS', 1))
   self.obj304.Copy.config = 0
   self.obj304.Specify=ATOM3Constraint()
   self.obj304.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj30.GGset2Any['ClassAppearance']= self.obj304
   cobj0.RHS.addNode(self.obj30)

   self.obj31=AtomClass(self)

   self.obj31.ClassName.setValue('MyClass1')
   self.obj31.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj1 =[]
   self.obj31.ClassCardinality.setValue(lcobj1)
   self.obj31.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj31.ClassConstraints.setValue(lcobj1)
   self.obj31.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj31.ClassAttributes.setValue(lcobj1)
   self.obj31.ClassAppearance.setValue( ('MyClass1', self.obj31))
   self.obj31.GGLabel.setValue(2)
   self.obj31.graphClass_= graph_AtomClass
   if self.genGraphics:
      from graph_AtomClass import *
      new_obj = graph_AtomClass(80.0,245.0,self.obj31)
   else: new_obj = None
   self.obj31.graphObject_ = new_obj
   self.obj310= AttrCalc()
   self.obj310.Copy=ATOM3Boolean()
   self.obj310.Copy.setValue(('Copy from LHS', 1))
   self.obj310.Copy.config = 0
   self.obj310.Specify=ATOM3Constraint()
   self.obj310.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj31.GGset2Any['ClassName']= self.obj310
   self.obj311= AttrCalc()
   self.obj311.Copy=ATOM3Boolean()
   self.obj311.Copy.setValue(('Copy from LHS', 1))
   self.obj311.Copy.config = 0
   self.obj311.Specify=ATOM3Constraint()
   self.obj311.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj31.GGset2Any['ClassCardinality']= self.obj311
   self.obj312= AttrCalc()
   self.obj312.Copy=ATOM3Boolean()
   self.obj312.Copy.setValue(('Copy from LHS', 1))
   self.obj312.Copy.config = 0
   self.obj312.Specify=ATOM3Constraint()
   self.obj312.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj31.GGset2Any['ClassAttributes']= self.obj312
   self.obj313= AttrCalc()
   self.obj313.Copy=ATOM3Boolean()
   self.obj313.Copy.setValue(('Copy from LHS', 1))
   self.obj313.Copy.config = 0
   self.obj313.Specify=ATOM3Constraint()
   self.obj313.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj31.GGset2Any['ClassConstraints']= self.obj313
   self.obj314= AttrCalc()
   self.obj314.Copy=ATOM3Boolean()
   self.obj314.Copy.setValue(('Copy from LHS', 1))
   self.obj314.Copy.config = 0
   self.obj314.Specify=ATOM3Constraint()
   self.obj314.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj31.GGset2Any['ClassAppearance']= self.obj314
   cobj0.RHS.addNode(self.obj31)
   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 1\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'atom = self.graphRewritingSystem.parent   #atom root\n\nParent = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nChild = self.getMatched(graphID, self.LHS.nodeWithLabel(2))\n\nParentAttrib = Parent.ClassAttributes\nChildAttrib = Child.ClassAttributes\n\nParent_in = Parent.in_connections_\nParent_out =  Parent.out_connections_\n\n#print dir(Parent.in_connections_[0])\n#print dir(Parent.out_connections_[0])\n#print Parent.out_connections_[0].out_connections_\n#print Parent.out_connections_[0].in_connections_\n#A = Parent.out_connections_[0].out_connections_[0]\n#B = Parent.out_connections_[0].in_connections_[0]\n\nfor a in ParentAttrib.getValue():\n	ChildAttrib.newItem(a)\n\nfor a in Parent_in:\n	atom.drawConnections((a,Child))\nfor a in Parent_out:\n	atom.drawConnections((Child,a))\n\n#Conn = atom.createNewAtomAssociation(atom,500,500,1)\n#atom.drawConnections((A,Conn), (Conn,B))\n\n'))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))


