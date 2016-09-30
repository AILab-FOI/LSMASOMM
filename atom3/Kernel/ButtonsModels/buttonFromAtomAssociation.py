# _ buttonFromAtomAssociation.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from AtomAssociation import *
from ASG_ClassDiagramB import *
from AtomInheritance import *
from AtomClass import *
class buttonFromAtomAssociation (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_ClassDiagramB(parent)

      self.obj44=AtomAssociation(parent)

      self.obj44.AssociationCardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj44.AssociationCardinality.setValue(lcobj2)
      self.obj44.AssociationCardinality.setNone()
      self.obj44.AssociationName.setValue('')
      self.obj44.AssociationAppearance.setNone()
      self.obj44.AssociationAppearance.linkInfo=linkEditor(self,self.obj44.AssociationAppearance.semObject, "Class_information_not_available")
      self.obj44.AssociationAppearance.linkInfo.FirstLink= stickylink()
      self.obj44.AssociationAppearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
      self.obj44.AssociationAppearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
      self.obj44.AssociationAppearance.linkInfo.FirstLink.arrow.config = 0
      self.obj44.AssociationAppearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
      self.obj44.AssociationAppearance.linkInfo.FirstLink.decoration.setValue( ('Class_information_not_available_1stLink', self.obj44.AssociationAppearance.linkInfo.FirstLink))
      self.obj44.AssociationAppearance.linkInfo.FirstSegment= widthXfillXdecoration()
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.width=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.fill=ATOM3String('black')
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.stipple=ATOM3String('')
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.arrow.config = 0
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.decoration.setValue( ('Class_information_not_available_1stSegment', self.obj44.AssociationAppearance.linkInfo.FirstSegment))
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.obj44.AssociationAppearance.linkInfo.Center=ATOM3Appearance()
      self.obj44.AssociationAppearance.linkInfo.Center.setValue( ('Class_information_not_available_Center', self.obj44.AssociationAppearance.linkInfo))
      self.obj44.AssociationAppearance.linkInfo.SecondSegment= widthXfillXdecoration()
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.width=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.fill=ATOM3String('black')
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.stipple=ATOM3String('')
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.arrow.config = 0
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.decoration.setValue( ('Class_information_not_available_2ndSegment', self.obj44.AssociationAppearance.linkInfo.SecondSegment))
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.obj44.AssociationAppearance.linkInfo.SecondLink= stickylink()
      self.obj44.AssociationAppearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
      self.obj44.AssociationAppearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
      self.obj44.AssociationAppearance.linkInfo.SecondLink.arrow.config = 0
      self.obj44.AssociationAppearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
      self.obj44.AssociationAppearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
      self.obj44.AssociationAppearance.linkInfo.SecondLink.decoration.setValue( ('Class_information_not_available_2ndLink', self.obj44.AssociationAppearance.linkInfo.SecondLink))
      self.obj44.AssociationAppearance.linkInfo.FirstLink.decoration.semObject=self.obj44.AssociationAppearance.semObject
      self.obj44.AssociationAppearance.linkInfo.FirstSegment.decoration.semObject=self.obj44.AssociationAppearance.semObject
      self.obj44.AssociationAppearance.linkInfo.Center.semObject=self.obj44.AssociationAppearance.semObject
      self.obj44.AssociationAppearance.linkInfo.SecondSegment.decoration.semObject=self.obj44.AssociationAppearance.semObject
      self.obj44.AssociationAppearance.linkInfo.SecondLink.decoration.semObject=self.obj44.AssociationAppearance.semObject
      self.obj44.AssociationConstraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj44.AssociationConstraints.setValue(lcobj2)
      self.obj44.AssociationConstraints.setNone()
      self.obj44.GGLabel.setValue(1)
      self.obj44.graphClass_= graph_AtomAssociation
      if parent.genGraphics:
         from graph_AtomAssociation import *
         new_obj = graph_AtomAssociation(86.0,86.0,self.obj44)
      else: new_obj = None
      self.obj44.graphObject_ = new_obj
      self.LHS.addNode(self.obj44)
      self.RHS = ASG_ClassDiagramB(parent)

      self.obj46=AtomAssociation(parent)

      self.obj46.AssociationCardinality.setActionFlags([ 0, 1, 0, 0])
      lcobj2 =[]
      self.obj46.AssociationCardinality.setValue(lcobj2)
      self.obj46.AssociationName.setValue('0')
      self.obj46.AssociationAppearance.setValue( ('None', self.obj46))
      self.obj46.AssociationAppearance.linkInfo=linkEditor(self,self.obj46.AssociationAppearance.semObject, "Class_information_not_available")
      self.obj46.AssociationAppearance.linkInfo.FirstLink= stickylink()
      self.obj46.AssociationAppearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
      self.obj46.AssociationAppearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
      self.obj46.AssociationAppearance.linkInfo.FirstLink.arrow.config = 0
      self.obj46.AssociationAppearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
      self.obj46.AssociationAppearance.linkInfo.FirstLink.decoration.setValue( ('Class_information_not_available_1stLink', self.obj46.AssociationAppearance.linkInfo.FirstLink))
      self.obj46.AssociationAppearance.linkInfo.FirstSegment= widthXfillXdecoration()
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.width=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.fill=ATOM3String('black')
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.stipple=ATOM3String('')
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.arrow.config = 0
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.decoration.setValue( ('Class_information_not_available_1stSegment', self.obj46.AssociationAppearance.linkInfo.FirstSegment))
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.obj46.AssociationAppearance.linkInfo.Center=ATOM3Appearance()
      self.obj46.AssociationAppearance.linkInfo.Center.setValue( ('Class_information_not_available_Center', self.obj46.AssociationAppearance.linkInfo))
      self.obj46.AssociationAppearance.linkInfo.SecondSegment= widthXfillXdecoration()
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.width=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.fill=ATOM3String('black')
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.stipple=ATOM3String('')
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.arrow.config = 0
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.decoration.setValue( ('Class_information_not_available_2ndSegment', self.obj46.AssociationAppearance.linkInfo.SecondSegment))
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.obj46.AssociationAppearance.linkInfo.SecondLink= stickylink()
      self.obj46.AssociationAppearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
      self.obj46.AssociationAppearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
      self.obj46.AssociationAppearance.linkInfo.SecondLink.arrow.config = 0
      self.obj46.AssociationAppearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
      self.obj46.AssociationAppearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
      self.obj46.AssociationAppearance.linkInfo.SecondLink.decoration.setValue( ('Class_information_not_available_2ndLink', self.obj46.AssociationAppearance.linkInfo.SecondLink))
      self.obj46.AssociationAppearance.linkInfo.FirstLink.decoration.semObject=self.obj46.AssociationAppearance.semObject
      self.obj46.AssociationAppearance.linkInfo.FirstSegment.decoration.semObject=self.obj46.AssociationAppearance.semObject
      self.obj46.AssociationAppearance.linkInfo.Center.semObject=self.obj46.AssociationAppearance.semObject
      self.obj46.AssociationAppearance.linkInfo.SecondSegment.decoration.semObject=self.obj46.AssociationAppearance.semObject
      self.obj46.AssociationAppearance.linkInfo.SecondLink.decoration.semObject=self.obj46.AssociationAppearance.semObject
      self.obj46.AssociationConstraints.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      self.obj46.AssociationConstraints.setValue(lcobj2)
      self.obj46.GGLabel.setValue(1)
      self.obj46.graphClass_= graph_AtomAssociation
      if parent.genGraphics:
         from graph_AtomAssociation import *
         new_obj = graph_AtomAssociation(116.0,48.0,self.obj46)
      else: new_obj = None
      self.obj46.graphObject_ = new_obj
      self.obj460= AttrCalc()
      self.obj460.Copy=ATOM3Boolean()
      self.obj460.Copy.setValue(('Copy from LHS', 1))
      self.obj460.Copy.config = 0
      self.obj460.Specify=ATOM3Constraint()
      self.obj460.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj46.GGset2Any['AssociationCardinality']= self.obj460
      self.obj461= AttrCalc()
      self.obj461.Copy=ATOM3Boolean()
      self.obj461.Copy.setValue(('Copy from LHS', 1))
      self.obj461.Copy.config = 0
      self.obj461.Specify=ATOM3Constraint()
      self.obj461.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj46.GGset2Any['AssociationName']= self.obj461
      self.obj462= AttrCalc()
      self.obj462.Copy=ATOM3Boolean()
      self.obj462.Copy.setValue(('Copy from LHS', 1))
      self.obj462.Copy.config = 0
      self.obj462.Specify=ATOM3Constraint()
      self.obj462.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj46.GGset2Any['AssociationAppearance']= self.obj462
      self.obj463= AttrCalc()
      self.obj463.Copy=ATOM3Boolean()
      self.obj463.Copy.setValue(('Copy from LHS', 1))
      self.obj463.Copy.config = 0
      self.obj463.Specify=ATOM3Constraint()
      self.obj463.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj46.GGset2Any['AssociationConstraints']= self.obj463
      self.RHS.addNode(self.obj46)
   def condition(self, graphID, isograph, atom3i):
      assoc = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      return assoc.visited == 0
      

   def action(self, graphID, isograph, atom3i):
      assoc = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      assoc.visited = 1
      ename = assoc.AssociationName.toString()
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
      

