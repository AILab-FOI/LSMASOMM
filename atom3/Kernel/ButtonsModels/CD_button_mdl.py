from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('CD_buttons')
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('buttonFromAtomClass')
   cobj0.Order=ATOM3Integer(1)

   from AtomClass import *
   from AtomInheritance import *
   from ASG_ClassDiagramB import *
   from AtomAssociation import *

   cobj0.LHS = ASG_ClassDiagramB(self)

   self.obj28=AtomClass(self)

   self.obj28.ClassName.setValue('')
   self.obj28.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj1 =[]
   self.obj28.ClassCardinality.setValue(lcobj1)
   self.obj28.ClassCardinality.setNone()
   self.obj28.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj28.ClassConstraints.setValue(lcobj1)
   self.obj28.ClassConstraints.setNone()
   self.obj28.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj28.ClassAttributes.setValue(lcobj1)
   self.obj28.ClassAttributes.setNone()
   self.obj28.ClassAppearance.setValue( ('MyClass', self.obj28))
   self.obj28.ClassAppearance.setNone()
   self.obj28.GGLabel.setValue(1)
   self.obj28.graphClass_= graph_AtomClass
   if self.genGraphics:
      from graph_AtomClass import *
      new_obj = graph_AtomClass(51.0,24.0,self.obj28)
   else: new_obj = None
   self.obj28.graphObject_ = new_obj
   cobj0.LHS.addNode(self.obj28)
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
      new_obj = graph_AtomClass(54.0,52.0,self.obj30)
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
   self.obj30.GGset2Any['ClassConstraints']= self.obj302
   self.obj303= AttrCalc()
   self.obj303.Copy=ATOM3Boolean()
   self.obj303.Copy.setValue(('Copy from LHS', 1))
   self.obj303.Copy.config = 0
   self.obj303.Specify=ATOM3Constraint()
   self.obj303.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj30.GGset2Any['ClassAttributes']= self.obj303
   self.obj304= AttrCalc()
   self.obj304.Copy=ATOM3Boolean()
   self.obj304.Copy.setValue(('Copy from LHS', 1))
   self.obj304.Copy.config = 0
   self.obj304.Specify=ATOM3Constraint()
   self.obj304.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj30.GGset2Any['ClassAppearance']= self.obj304
   cobj0.RHS.addNode(self.obj30)
   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'myclass = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn myclass.visited == 0\n\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'myclass = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nmyclass.visited = 1\nposx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)\nself.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1\ncname = myclass.ClassName.toString()\nfile = self.graphRewritingSystem.file\nfile.write("   self.globalPrecondition(rootNode)\\n\\n")\nfile.write("   self.obj"+cname+"=ButtonConfig(self)\\n")\nfile.write("   self.obj"+cname+".Contents.Text.setValue(\'New "+cname+"\')\\n")\nfile.write("   self.obj"+cname+".Contents.Image.setValue(\'\')\\n")\nfile.write("   self.obj"+cname+".Contents.lastSelected= \'Text\'\\n")\nfile.write("   self.obj"+cname+".Drawing_Mode.setValue(1)\\n")\nfile.write("   self.obj"+cname+".Action.setValue((\'ActionButton1\', ([\'Python\', \'OCL\'], 1), ")\nfile.write("([\'PREcondition\', \'POSTcondition\'], 1),")\nfile.write("([\'EDIT\', \'SAVE\', \'CREATE\', \'CONNECT\', \'DELETE\', \'DISCONNECT\', \'TRANSFORM\', \'SELECT\', \'DRAG\', \'DROP\', \'MOVE OBJECT\'], ")\nfile.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")\nfile.write("\'# This method has as parameters:\\\\n")\nfile.write("#   - wherex : X Position in window coordinates where the user clicked.\\\\n")\nfile.write("#   - wherey : Y Position in window coordinates where the user clicked.\\\\n")\nfile.write("newPlace = self.createNew"+cname+" (self, wherex, wherey)\\\\n\'))\\n")\nfile.write("   self.obj"+cname+".graphClass_= graph_ButtonConfig\\n")\nfile.write("   if self.genGraphics:\\n")\nfile.write("      from graph_ButtonConfig import *\\n")\nfile.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+cname+")\\n")\nfile.write("      new_obj.DrawObject(self.UMLmodel)\\n")\nfile.write("      self.UMLmodel.addtag_withtag(\'ButtonConfig\', new_obj.tag)\\n")\nfile.write("   else: new_obj = None\\n")\nfile.write("   self.obj"+cname+".graphObject_ = new_obj\\n")\nfile.write("   rootNode.addNode(self.obj"+cname+")\\n")\nfile.write("   self.globalAndLocalPostcondition(self.obj"+cname+", rootNode)\\n")\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('buttonFromAtomAssociation')
   cobj0.Order=ATOM3Integer(1)

   from AtomClass import *
   from AtomInheritance import *
   from ASG_ClassDiagramB import *
   from AtomAssociation import *

   cobj0.LHS = ASG_ClassDiagramB(self)

   self.obj159=AtomAssociation(self)

   self.obj159.AssociationConstraints.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj159.AssociationConstraints.setValue(lcobj1)
   self.obj159.AssociationConstraints.setNone()
   self.obj159.AssociationAppearance.setValue( ('None', self.obj159))
   self.obj159.AssociationAppearance.linkInfo=linkEditor(self,self.obj159.AssociationAppearance.semObject, "Class_information_not_available")
   self.obj159.AssociationAppearance.linkInfo.FirstLink= stickylink()
   self.obj159.AssociationAppearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
   self.obj159.AssociationAppearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
   self.obj159.AssociationAppearance.linkInfo.FirstLink.arrow.config = 0
   self.obj159.AssociationAppearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
   self.obj159.AssociationAppearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
   self.obj159.AssociationAppearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
   self.obj159.AssociationAppearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
   self.obj159.AssociationAppearance.linkInfo.FirstLink.decoration.setValue( ('Class_information_not_available_1stLink', self.obj159.AssociationAppearance.linkInfo.FirstLink))
   self.obj159.AssociationAppearance.linkInfo.FirstSegment= widthXfillXdecoration()
   self.obj159.AssociationAppearance.linkInfo.FirstSegment.width=ATOM3Integer(0)
   self.obj159.AssociationAppearance.linkInfo.FirstSegment.fill=ATOM3String('black')
   self.obj159.AssociationAppearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
   self.obj159.AssociationAppearance.linkInfo.FirstSegment.decoration.setValue( ('Class_information_not_available_1stSegment', self.obj159.AssociationAppearance.linkInfo.FirstSegment))
   self.obj159.AssociationAppearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj159.AssociationAppearance.linkInfo.Center=ATOM3Appearance()
   self.obj159.AssociationAppearance.linkInfo.Center.setValue( ('Class_information_not_available_Center', self.obj159.AssociationAppearance.linkInfo))
   self.obj159.AssociationAppearance.linkInfo.SecondSegment= widthXfillXdecoration()
   self.obj159.AssociationAppearance.linkInfo.SecondSegment.width=ATOM3Integer(0)
   self.obj159.AssociationAppearance.linkInfo.SecondSegment.fill=ATOM3String('black')
   self.obj159.AssociationAppearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
   self.obj159.AssociationAppearance.linkInfo.SecondSegment.decoration.setValue( ('Class_information_not_available_2ndSegment', self.obj159.AssociationAppearance.linkInfo.SecondSegment))
   self.obj159.AssociationAppearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj159.AssociationAppearance.linkInfo.SecondLink= stickylink()
   self.obj159.AssociationAppearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
   self.obj159.AssociationAppearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
   self.obj159.AssociationAppearance.linkInfo.SecondLink.arrow.config = 0
   self.obj159.AssociationAppearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
   self.obj159.AssociationAppearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
   self.obj159.AssociationAppearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
   self.obj159.AssociationAppearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
   self.obj159.AssociationAppearance.linkInfo.SecondLink.decoration.setValue( ('Class_information_not_available_2ndLink', self.obj159.AssociationAppearance.linkInfo.SecondLink))
   self.obj159.AssociationAppearance.linkInfo.FirstLink.decoration.semObject=self.obj159.AssociationAppearance.semObject
   self.obj159.AssociationAppearance.linkInfo.FirstSegment.decoration.semObject=self.obj159.AssociationAppearance.semObject
   self.obj159.AssociationAppearance.linkInfo.Center.semObject=self.obj159.AssociationAppearance.semObject
   self.obj159.AssociationAppearance.linkInfo.SecondSegment.decoration.semObject=self.obj159.AssociationAppearance.semObject
   self.obj159.AssociationAppearance.linkInfo.SecondLink.decoration.semObject=self.obj159.AssociationAppearance.semObject
   self.obj159.AssociationName.setValue('')
   self.obj159.AssociationCardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj1 =[]
   self.obj159.AssociationCardinality.setValue(lcobj1)
   self.obj159.AssociationCardinality.setNone()
   self.obj159.GGLabel.setValue(1)
   self.obj159.graphClass_= graph_AtomAssociation
   if self.genGraphics:
      from graph_AtomAssociation import *
      new_obj = graph_AtomAssociation(86.0,86.0,self.obj159)
   else: new_obj = None
   self.obj159.graphObject_ = new_obj
   cobj0.LHS.addNode(self.obj159)
   cobj0.RHS = ASG_ClassDiagramB(self)

   self.obj37=AtomAssociation(self)

   self.obj37.AssociationConstraints.setActionFlags([ 1, 1, 1, 0])
   lcobj1 =[]
   self.obj37.AssociationConstraints.setValue(lcobj1)
   self.obj37.AssociationAppearance.setValue( ('None', self.obj37))
   self.obj37.AssociationAppearance.linkInfo=linkEditor(self,self.obj37.AssociationAppearance.semObject, "Class_information_not_available")
   self.obj37.AssociationAppearance.linkInfo.FirstLink= stickylink()
   self.obj37.AssociationAppearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
   self.obj37.AssociationAppearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
   self.obj37.AssociationAppearance.linkInfo.FirstLink.arrow.config = 0
   self.obj37.AssociationAppearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
   self.obj37.AssociationAppearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
   self.obj37.AssociationAppearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
   self.obj37.AssociationAppearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
   self.obj37.AssociationAppearance.linkInfo.FirstLink.decoration.setValue( ('Class_information_not_available_1stLink', self.obj37.AssociationAppearance.linkInfo.FirstLink))
   self.obj37.AssociationAppearance.linkInfo.FirstSegment= widthXfillXdecoration()
   self.obj37.AssociationAppearance.linkInfo.FirstSegment.width=ATOM3Integer(0)
   self.obj37.AssociationAppearance.linkInfo.FirstSegment.fill=ATOM3String('black')
   self.obj37.AssociationAppearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
   self.obj37.AssociationAppearance.linkInfo.FirstSegment.decoration.setValue( ('Class_information_not_available_1stSegment', self.obj37.AssociationAppearance.linkInfo.FirstSegment))
   self.obj37.AssociationAppearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj37.AssociationAppearance.linkInfo.Center=ATOM3Appearance()
   self.obj37.AssociationAppearance.linkInfo.Center.setValue( ('Class_information_not_available_Center', self.obj37.AssociationAppearance.linkInfo))
   self.obj37.AssociationAppearance.linkInfo.SecondSegment= widthXfillXdecoration()
   self.obj37.AssociationAppearance.linkInfo.SecondSegment.width=ATOM3Integer(0)
   self.obj37.AssociationAppearance.linkInfo.SecondSegment.fill=ATOM3String('black')
   self.obj37.AssociationAppearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
   self.obj37.AssociationAppearance.linkInfo.SecondSegment.decoration.setValue( ('Class_information_not_available_2ndSegment', self.obj37.AssociationAppearance.linkInfo.SecondSegment))
   self.obj37.AssociationAppearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
   self.obj37.AssociationAppearance.linkInfo.SecondLink= stickylink()
   self.obj37.AssociationAppearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
   self.obj37.AssociationAppearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
   self.obj37.AssociationAppearance.linkInfo.SecondLink.arrow.config = 0
   self.obj37.AssociationAppearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
   self.obj37.AssociationAppearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
   self.obj37.AssociationAppearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
   self.obj37.AssociationAppearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
   self.obj37.AssociationAppearance.linkInfo.SecondLink.decoration.setValue( ('Class_information_not_available_2ndLink', self.obj37.AssociationAppearance.linkInfo.SecondLink))
   self.obj37.AssociationAppearance.linkInfo.FirstLink.decoration.semObject=self.obj37.AssociationAppearance.semObject
   self.obj37.AssociationAppearance.linkInfo.FirstSegment.decoration.semObject=self.obj37.AssociationAppearance.semObject
   self.obj37.AssociationAppearance.linkInfo.Center.semObject=self.obj37.AssociationAppearance.semObject
   self.obj37.AssociationAppearance.linkInfo.SecondSegment.decoration.semObject=self.obj37.AssociationAppearance.semObject
   self.obj37.AssociationAppearance.linkInfo.SecondLink.decoration.semObject=self.obj37.AssociationAppearance.semObject
   self.obj37.AssociationName.setValue('0')
   self.obj37.AssociationCardinality.setActionFlags([ 0, 1, 0, 0])
   lcobj1 =[]
   self.obj37.AssociationCardinality.setValue(lcobj1)
   self.obj37.GGLabel.setValue(1)
   self.obj37.graphClass_= graph_AtomAssociation
   if self.genGraphics:
      from graph_AtomAssociation import *
      new_obj = graph_AtomAssociation(116.0,48.0,self.obj37)
   else: new_obj = None
   self.obj37.graphObject_ = new_obj
   self.obj370= AttrCalc()
   self.obj370.Copy=ATOM3Boolean()
   self.obj370.Copy.setValue(('Copy from LHS', 1))
   self.obj370.Copy.config = 0
   self.obj370.Specify=ATOM3Constraint()
   self.obj370.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj37.GGset2Any['AssociationConstraints']= self.obj370
   self.obj371= AttrCalc()
   self.obj371.Copy=ATOM3Boolean()
   self.obj371.Copy.setValue(('Copy from LHS', 1))
   self.obj371.Copy.config = 0
   self.obj371.Specify=ATOM3Constraint()
   self.obj371.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj37.GGset2Any['AssociationAppearance']= self.obj371
   self.obj372= AttrCalc()
   self.obj372.Copy=ATOM3Boolean()
   self.obj372.Copy.setValue(('Copy from LHS', 1))
   self.obj372.Copy.config = 0
   self.obj372.Specify=ATOM3Constraint()
   self.obj372.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj37.GGset2Any['AssociationName']= self.obj372
   self.obj373= AttrCalc()
   self.obj373.Copy=ATOM3Boolean()
   self.obj373.Copy.setValue(('Copy from LHS', 1))
   self.obj373.Copy.config = 0
   self.obj373.Specify=ATOM3Constraint()
   self.obj373.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
   self.obj37.GGset2Any['AssociationCardinality']= self.obj373
   cobj0.RHS.addNode(self.obj37)
   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'assoc = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn assoc.visited == 0\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'assoc = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nassoc.visited = 1\nename = assoc.AssociationName.toString()\nposx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)\nself.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1\nfile = self.graphRewritingSystem.file\nfile.write("   self.globalPrecondition(rootNode)\\n\\n")\nfile.write("   self.obj"+ename+"=ButtonConfig(self)\\n")\nfile.write("   self.obj"+ename+".Contents.Text.setValue(\'New "+ename+"\')\\n")\nfile.write("   self.obj"+ename+".Contents.Image.setValue(\'\')\\n")\nfile.write("   self.obj"+ename+".Contents.lastSelected= \'Text\'\\n")\nfile.write("   self.obj"+ename+".Drawing_Mode.setValue(1)\\n")\nfile.write("   self.obj"+ename+".Action.setValue((\'ActionButton1\', ([\'Python\', \'OCL\'], 1), ")\nfile.write("([\'PREcondition\', \'POSTcondition\'], 1),")\nfile.write("([\'EDIT\', \'SAVE\', \'CREATE\', \'CONNECT\', \'DELETE\', \'DISCONNECT\', \'TRANSFORM\', \'SELECT\', \'DRAG\', \'DROP\', \'MOVE OBJECT\'], ")\nfile.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")\nfile.write("\'# This method has as parameters:\\\\n")\nfile.write("#   - wherex : X Position in window coordinates where the user clicked.\\\\n")\nfile.write("#   - wherey : Y Position in window coordinates where the user clicked.\\\\n")\nfile.write("newPlace = self.createNew"+ename+" (self, wherex, wherey)\\\\n\'))\\n")\nfile.write("   self.obj"+ename+".graphClass_= graph_ButtonConfig\\n")\nfile.write("   if self.genGraphics:\\n")\nfile.write("      from graph_ButtonConfig import *\\n")\nfile.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+ename+")\\n")\nfile.write("      new_obj.DrawObject(self.UMLmodel)\\n")\nfile.write("      self.UMLmodel.addtag_withtag(\'ButtonConfig\', new_obj.tag)\\n")\nfile.write("   else: new_obj = None\\n")\nfile.write("   self.obj"+ename+".graphObject_ = new_obj\\n")\nfile.write("   rootNode.addNode(self.obj"+ename+")\\n")\nfile.write("   self.globalAndLocalPostcondition(self.obj"+ename+", rootNode)\\n")\n'))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.rewritingSystem.name = self.rewritingSystem.parent.ASGroot.keyword_.toString()\nself.rewritingSystem.NButtons = 0\nfileName = self.rewritingSystem.name+".py"\ncgd = self.rewritingSystem.parent.codeGenDir\nself.rewritingSystem.file = open(cgd+"/"+fileName,"w+t")\nfile = self.rewritingSystem.file\nfile.write("from ASG_Buttons import *\\n")\nfile.write("from ButtonConfig import *\\n")\nfile.write("from ATOM3Enum import *\\n")\nfile.write("from ATOM3List import *\\n")\nfile.write("from ATOM3Float import *\\n")\nfile.write("from ATOM3Integer import *\\n")\nfile.write("from ATOM3Attribute import *\\n")\nfile.write("from ATOM3Constraint import *\\n")\nfile.write("from ATOM3String import *\\n")\nfile.write("from ATOM3BottomType import *\\n")\nfile.write("from ATOM3Boolean import *\\n")\nfile.write("from ATOM3Appearance import *\\n")\nfile.write("from ATOM3Link import *\\n")\nfile.write("def "+self.rewritingSystem.name+"(self, rootNode):\\n")\nfile.write("   rootNode.Formalism_Name.setValue(\'"+self.rewritingSystem.name+"\')\\n")\nfile.write("   rootNode.RowSize.setValue(4)\\n")\nfile.write("   rootNode.Formalism_File.setValue(\'"+cgd+"/"+self.rewritingSystem.name+"_MM.py\')\\n")\nfor nt in graph.listNodes.keys():\n   for node in graph.listNodes[nt]:\n      node.visited = 0 \n\n\n\n\n'))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'file = self.rewritingSystem.file\n\nfile.write("newfunction = "+self.rewritingSystem.name+"\\n")\nfile.write("loadedMMName = \'Buttons\'\\n")\n\nfor nt in graph.listNodes.keys():\n   for node in graph.listNodes[nt]:\n      del node.visited     \n   \ndel self.rewritingSystem.file\ndel self.rewritingSystem.NButtons\n\n\n'))


