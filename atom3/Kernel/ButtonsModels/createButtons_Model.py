from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('createButtons')
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('buttonFromEntity')
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)

   from ASG_ERmetaMetaModel import *
   from ERrelationship import *
   from ERentity import *

   cobj0.LHS = ASG_ERmetaMetaModel(self)

   self.obj35=ERentity(self)

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
   if self.genGraphics:
      from graph_ERentity import *
      new_obj = graph_ERentity(210.0,276.0,self.obj35)
   else: new_obj = None
   self.obj35.graphObject_ = new_obj
   cobj0.LHS.addNode(self.obj35)
   cobj0.RHS = ASG_ERmetaMetaModel(self)

   self.obj37=ERentity(self)

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
   if self.genGraphics:
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
   cobj0.RHS.addNode(self.obj37)
   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn entity.visited == 0\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nentity.visited = 1\nposx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)\nself.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1\nename = entity.name.toString()\nfile = self.graphRewritingSystem.file\nfile.write("   self.globalPrecondition(rootNode)\\n\\n")\nfile.write("   self.obj"+ename+"=ButtonConfig(self)\\n")\nfile.write("   self.obj"+ename+".Contents.Text.setValue(\'New "+ename+"\')\\n")\nfile.write("   self.obj"+ename+".Contents.Image.setValue(\'\')\\n")\nfile.write("   self.obj"+ename+".Contents.lastSelected= \'Text\'\\n")\nfile.write("   self.obj"+ename+".Drawing_Mode.setValue(1)\\n")\nfile.write("   self.obj"+ename+".Action.setValue((\'ActionButton1\', ([\'Python\', \'OCL\'], 1), ")\nfile.write("([\'PREcondition\', \'POSTcondition\'], 1),")\nfile.write("([\'EDIT\', \'SAVE\', \'CREATE\', \'CONNECT\', \'DELETE\', \'DISCONNECT\', \'TRANSFORM\', \'SELECT\', \'DRAG\', \'DROP\', \'MOVE OBJECT\'], ")\nfile.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")\nfile.write("\'# This method has as parameters:\\\\n")\nfile.write("#   - wherex : X Position in window coordinates where the user clicked.\\\\n")\nfile.write("#   - wherey : Y Position in window coordinates where the user clicked.\\\\n")\nfile.write("newPlace = self.createNew"+ename+" (self, wherex, wherey)\\\\n\'))\\n")\nfile.write("   self.obj"+ename+".graphClass_= graph_ButtonConfig\\n")\nfile.write("   if self.genGraphics:\\n")\nfile.write("      from graph_ButtonConfig import *\\n")\nfile.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+ename+")\\n")\nfile.write("      new_obj.DrawObject(self.UMLmodel)\\n")\nfile.write("      self.UMLmodel.addtag_withtag(\'ButtonConfig\', new_obj.tag)\\n")\nfile.write("   else: new_obj = None\\n")\nfile.write("   self.obj"+ename+".graphObject_ = new_obj\\n")\nfile.write("   rootNode.addNode(self.obj"+ename+")\\n")\nfile.write("   self.globalAndLocalPostcondition(self.obj"+ename+", rootNode)\\n")\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('buttonFromRelationship')
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)

   from ASG_ERmetaMetaModel import *
   from ERrelationship import *
   from ERentity import *

   cobj0.LHS = ASG_ERmetaMetaModel(self)

   self.obj42=ERrelationship(self)

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
   if self.genGraphics:
      from graph_ERrelationship import *
      new_obj = graph_ERrelationship(163.0,272.0,self.obj42)
   else: new_obj = None
   self.obj42.graphObject_ = new_obj
   cobj0.LHS.addNode(self.obj42)
   cobj0.RHS = ASG_ERmetaMetaModel(self)

   self.obj44=ERrelationship(self)

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
   if self.genGraphics:
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
   cobj0.RHS.addNode(self.obj44)
   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nreturn entity.visited == 0\n\n\n\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'entity = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\nentity.visited = 1\nename = entity.name.toString()\nposx, posy = 10+125*(self.graphRewritingSystem.NButtons%3), 10+70*(self.graphRewritingSystem.NButtons/3)\nself.graphRewritingSystem.NButtons = self.graphRewritingSystem.NButtons + 1\nfile = self.graphRewritingSystem.file\nfile.write("   self.globalPrecondition(rootNode)\\n\\n")\nfile.write("   self.obj"+ename+"=ButtonConfig(self)\\n")\nfile.write("   self.obj"+ename+".Contents.Text.setValue(\'New "+ename+"\')\\n")\nfile.write("   self.obj"+ename+".Contents.Image.setValue(\'\')\\n")\nfile.write("   self.obj"+ename+".Contents.lastSelected= \'Text\'\\n")\nfile.write("   self.obj"+ename+".Drawing_Mode.setValue(1)\\n")\nfile.write("   self.obj"+ename+".Action.setValue((\'ActionButton1\', ([\'Python\', \'OCL\'], 1), ")\nfile.write("([\'PREcondition\', \'POSTcondition\'], 1),")\nfile.write("([\'EDIT\', \'SAVE\', \'CREATE\', \'CONNECT\', \'DELETE\', \'DISCONNECT\', \'TRANSFORM\', \'SELECT\', \'DRAG\', \'DROP\', \'MOVE OBJECT\'], ")\nfile.write("[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), ")\nfile.write("\'# This method has as parameters:\\\\n")\nfile.write("#   - wherex : X Position in window coordinates where the user clicked.\\\\n")\nfile.write("#   - wherey : Y Position in window coordinates where the user clicked.\\\\n")\nfile.write("newPlace = self.createNew"+ename+" (self, wherex, wherey)\\\\n\'))\\n")\nfile.write("   self.obj"+ename+".graphClass_= graph_ButtonConfig\\n")\nfile.write("   if self.genGraphics:\\n")\nfile.write("      from graph_ButtonConfig import *\\n")\nfile.write("      new_obj = graph_ButtonConfig("+str(posx)+", "+str(posy)+",self.obj"+ename+")\\n")\nfile.write("      new_obj.DrawObject(self.UMLmodel)\\n")\nfile.write("      self.UMLmodel.addtag_withtag(\'ButtonConfig\', new_obj.tag)\\n")\nfile.write("   else: new_obj = None\\n")\nfile.write("   self.obj"+ename+".graphObject_ = new_obj\\n")\nfile.write("   rootNode.addNode(self.obj"+ename+")\\n")\nfile.write("   self.globalAndLocalPostcondition(self.obj"+ename+", rootNode)\\n")\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.rewritingSystem.name = self.rewritingSystem.parent.ASGroot.keyword_.toString()\nself.rewritingSystem.NButtons = 0\nfileName = self.rewritingSystem.name+".py"\ncgd = self.rewritingSystem.parent.codeGenDir\nself.rewritingSystem.file = open(cgd+"/"+fileName,"w+t")\nfile = self.rewritingSystem.file\nfile.write("from ASG_Buttons import *\\n")\nfile.write("from ButtonConfig import *\\n")\nfile.write("from ATOM3Enum import *\\n")\nfile.write("from ATOM3List import *\\n")\nfile.write("from ATOM3Float import *\\n")\nfile.write("from ATOM3Integer import *\\n")\nfile.write("from ATOM3Attribute import *\\n")\nfile.write("from ATOM3Constraint import *\\n")\nfile.write("from ATOM3String import *\\n")\nfile.write("from ATOM3BottomType import *\\n")\nfile.write("from ATOM3Boolean import *\\n")\nfile.write("from ATOM3Appearance import *\\n")\nfile.write("from ATOM3Link import *\\n")\nfile.write("def "+self.rewritingSystem.name+"(self, rootNode):\\n")\nfile.write("   rootNode.Formalism_Name.setValue(\'"+self.rewritingSystem.name+"\')\\n")\nfile.write("   rootNode.RowSize.setValue(4)\\n")\nfile.write("   rootNode.Formalism_File.setValue(\'"+cgd+"/"+self.rewritingSystem.name+"_MM.py\')\\n")\nfor nt in graph.listNodes.keys():\n   for node in graph.listNodes[nt]:\n      node.visited = 0      \n\n\n\n\n'))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'file = self.rewritingSystem.file\n\nfile.write("newfunction = "+self.rewritingSystem.name+"\\n")\nfile.write("loadedMMName = \'Buttons\'\\n")\n\nfor nt in graph.listNodes.keys():\n   for node in graph.listNodes[nt]:\n      del node.visited     \n   \ndel self.rewritingSystem.file\ndel self.rewritingSystem.NButtons\n\n\n'))


