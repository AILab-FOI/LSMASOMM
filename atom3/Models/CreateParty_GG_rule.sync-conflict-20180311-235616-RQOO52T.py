# _ CreateParty_GG_rule.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from hasObjective import *
from isPartOfOrgUnit import *
from Strategy import *
from canStartProcess import *
from Role import *
from canHaveRole import *
from Objective import *
from ASG_LSMASOMM import *
from OrganisationalKnArt import *
from hasActions import *
from isPartOfRole import *
from answersToOrgUnit import *
from isPartOfObjective import *
from IndividualKnArt import *
from answersToRole import *
from Action import *
from KnowledgeArtifacts import *
from genericAssociation import *
from Process import *
from OrgUnit import *
from isPartOfProcess import *
from canAccessKnArt import *
from precedentTo import *
class CreateParty_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_LSMASOMM(parent)

      self.obj654=OrgUnit(parent)
      self.obj654.preAction( self.LHS.CREATE )
      self.obj654.isGraphObjectVisual = True

      if(hasattr(self.obj654, '_setHierarchicalLink')):
        self.obj654._setHierarchicalLink(False)

      # Individual
      self.obj654.Individual.setNone()
      self.obj654.Individual.config = 0

      # hasActions
      self.obj654.hasActions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      cobj2=ATOM3String('ChangeRole', 20)
      lcobj2.append(cobj2)
      self.obj654.hasActions.setValue(lcobj2)
      self.obj654.hasActions.setNone()

      # ID
      self.obj654.ID.setValue('')
      self.obj654.ID.setNone()

      # name
      self.obj654.name.setValue('')
      self.obj654.name.setNone()

      # UnitSize
      self.obj654.UnitSize.setValue('Individual')

      self.obj654.GGLabel.setValue(1)
      self.obj654.graphClass_= graph_OrgUnit
      if parent.genGraphics:
         new_obj = graph_OrgUnit(0,0,self.obj654)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj654.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj654)
      self.obj654.postAction( self.LHS.CREATE )

      self.obj655=Role(parent)
      self.obj655.preAction( self.LHS.CREATE )
      self.obj655.isGraphObjectVisual = True

      if(hasattr(self.obj655, '_setHierarchicalLink')):
        self.obj655._setHierarchicalLink(False)

      # isMetaRole
      self.obj655.isMetaRole.setNone()
      self.obj655.isMetaRole.config = 0

      # hasActions
      self.obj655.hasActions.setActionFlags([ 0, 0, 1, 0])
      lcobj2 =[]
      self.obj655.hasActions.setValue(lcobj2)
      self.obj655.hasActions.setNone()

      # ID
      self.obj655.ID.setValue('')
      self.obj655.ID.setNone()

      # name
      self.obj655.name.setValue('PartyFounder')

      self.obj655.GGLabel.setValue(2)
      self.obj655.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(93,0,self.obj655)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj655.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj655)
      self.obj655.postAction( self.LHS.CREATE )

      self.obj656=canHaveRole(parent)
      self.obj656.preAction( self.LHS.CREATE )
      self.obj656.isGraphObjectVisual = True

      if(hasattr(self.obj656, '_setHierarchicalLink')):
        self.obj656._setHierarchicalLink(True)

      # ID
      self.obj656.ID.setValue('OUR|0')

      self.obj656.GGLabel.setValue(3)
      self.obj656.graphClass_= graph_canHaveRole
      if parent.genGraphics:
         new_obj = graph_canHaveRole(82.7757140317,49.5328543483,self.obj656)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj656.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj656)
      self.obj656.postAction( self.LHS.CREATE )

      self.obj654.out_connections_.append(self.obj656)
      self.obj656.in_connections_.append(self.obj654)
      self.obj654.graphObject_.pendingConnections.append((self.obj654.graphObject_.tag, self.obj656.graphObject_.tag, [320.0, 383.0, 82.77571403127953, 49.532854348475105], 0, True))
      self.obj656.out_connections_.append(self.obj655)
      self.obj655.in_connections_.append(self.obj656)
      self.obj656.graphObject_.pendingConnections.append((self.obj656.graphObject_.tag, self.obj655.graphObject_.tag, [318.0, 18.0, 248.5, 202.5], 0, True))

      self.RHS = ASG_LSMASOMM(parent)

      self.obj658=OrgUnit(parent)
      self.obj658.preAction( self.RHS.CREATE )
      self.obj658.isGraphObjectVisual = True

      if(hasattr(self.obj658, '_setHierarchicalLink')):
        self.obj658._setHierarchicalLink(False)

      # Individual
      self.obj658.Individual.setNone()
      self.obj658.Individual.config = 0

      # hasActions
      self.obj658.hasActions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      cobj2=ATOM3String('ChangeRole', 20)
      lcobj2.append(cobj2)
      self.obj658.hasActions.setValue(lcobj2)
      self.obj658.hasActions.setNone()

      # ID
      self.obj658.ID.setValue('')
      self.obj658.ID.setNone()

      # name
      self.obj658.name.setValue('')
      self.obj658.name.setNone()

      # UnitSize
      self.obj658.UnitSize.setValue('Individual')

      self.obj658.GGLabel.setValue(1)
      self.obj658.graphClass_= graph_OrgUnit
      if parent.genGraphics:
         new_obj = graph_OrgUnit(0,104,self.obj658)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj658.graphObject_ = new_obj
      self.obj6580= AttrCalc()
      self.obj6580.Copy=ATOM3Boolean()
      self.obj6580.Copy.setValue(('Copy from LHS', 1))
      self.obj6580.Copy.config = 0
      self.obj6580.Specify=ATOM3Constraint()
      self.obj6580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj658.GGset2Any['Individual']= self.obj6580
      self.obj6581= AttrCalc()
      self.obj6581.Copy=ATOM3Boolean()
      self.obj6581.Copy.setValue(('Copy from LHS', 1))
      self.obj6581.Copy.config = 0
      self.obj6581.Specify=ATOM3Constraint()
      self.obj6581.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj658.GGset2Any['hasActions']= self.obj6581
      self.obj6582= AttrCalc()
      self.obj6582.Copy=ATOM3Boolean()
      self.obj6582.Copy.setValue(('Copy from LHS', 1))
      self.obj6582.Copy.config = 0
      self.obj6582.Specify=ATOM3Constraint()
      self.obj6582.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj658.GGset2Any['ID']= self.obj6582
      self.obj6583= AttrCalc()
      self.obj6583.Copy=ATOM3Boolean()
      self.obj6583.Copy.setValue(('Copy from LHS', 1))
      self.obj6583.Copy.config = 0
      self.obj6583.Specify=ATOM3Constraint()
      self.obj6583.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj658.GGset2Any['name']= self.obj6583
      self.obj6584= AttrCalc()
      self.obj6584.Copy=ATOM3Boolean()
      self.obj6584.Copy.setValue(('Copy from LHS', 1))
      self.obj6584.Copy.config = 0
      self.obj6584.Specify=ATOM3Constraint()
      self.obj6584.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj658.GGset2Any['UnitSize']= self.obj6584

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj658)
      self.obj658.postAction( self.RHS.CREATE )

      self.obj659=OrgUnit(parent)
      self.obj659.preAction( self.RHS.CREATE )
      self.obj659.isGraphObjectVisual = True

      if(hasattr(self.obj659, '_setHierarchicalLink')):
        self.obj659._setHierarchicalLink(False)

      # Individual
      self.obj659.Individual.setValue(('1', 0))
      self.obj659.Individual.config = 0

      # hasActions
      self.obj659.hasActions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      cobj2=ATOM3String('ChangeRole', 20)
      lcobj2.append(cobj2)
      self.obj659.hasActions.setValue(lcobj2)

      # ID
      self.obj659.ID.setValue('OU|99')

      # name
      self.obj659.name.setValue('Party')

      # UnitSize
      self.obj659.UnitSize.setValue('Group')

      self.obj659.GGLabel.setValue(5)
      self.obj659.graphClass_= graph_OrgUnit
      if parent.genGraphics:
         new_obj = graph_OrgUnit(124,0,self.obj659)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj659.graphObject_ = new_obj
      self.obj6590= AttrCalc()
      self.obj6590.Copy=ATOM3Boolean()
      self.obj6590.Copy.setValue(('Copy from LHS', 0))
      self.obj6590.Copy.config = 0
      self.obj6590.Specify=ATOM3Constraint()
      self.obj6590.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj659.GGset2Any['Individual']= self.obj6590
      self.obj6591= AttrCalc()
      self.obj6591.Copy=ATOM3Boolean()
      self.obj6591.Copy.setValue(('Copy from LHS', 0))
      self.obj6591.Copy.config = 0
      self.obj6591.Specify=ATOM3Constraint()
      self.obj6591.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj659.GGset2Any['hasActions']= self.obj6591
      self.obj6592= AttrCalc()
      self.obj6592.Copy=ATOM3Boolean()
      self.obj6592.Copy.setValue(('Copy from LHS', 0))
      self.obj6592.Copy.config = 0
      self.obj6592.Specify=ATOM3Constraint()
      self.obj6592.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj659.GGset2Any['ID']= self.obj6592
      self.obj6593= AttrCalc()
      self.obj6593.Copy=ATOM3Boolean()
      self.obj6593.Copy.setValue(('Copy from LHS', 0))
      self.obj6593.Copy.config = 0
      self.obj6593.Specify=ATOM3Constraint()
      self.obj6593.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj659.GGset2Any['name']= self.obj6593
      self.obj6594= AttrCalc()
      self.obj6594.Copy=ATOM3Boolean()
      self.obj6594.Copy.setValue(('Copy from LHS', 0))
      self.obj6594.Copy.config = 0
      self.obj6594.Specify=ATOM3Constraint()
      self.obj6594.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj659.GGset2Any['UnitSize']= self.obj6594

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj659)
      self.obj659.postAction( self.RHS.CREATE )

      self.obj660=Role(parent)
      self.obj660.preAction( self.RHS.CREATE )
      self.obj660.isGraphObjectVisual = True

      if(hasattr(self.obj660, '_setHierarchicalLink')):
        self.obj660._setHierarchicalLink(False)

      # isMetaRole
      self.obj660.isMetaRole.setNone()
      self.obj660.isMetaRole.config = 0

      # hasActions
      self.obj660.hasActions.setActionFlags([ 0, 0, 1, 0])
      lcobj2 =[]
      self.obj660.hasActions.setValue(lcobj2)
      self.obj660.hasActions.setNone()

      # ID
      self.obj660.ID.setValue('')
      self.obj660.ID.setNone()

      # name
      self.obj660.name.setValue('PartyFounder')

      self.obj660.GGLabel.setValue(2)
      self.obj660.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(206,104,self.obj660)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj660.graphObject_ = new_obj
      self.obj6600= AttrCalc()
      self.obj6600.Copy=ATOM3Boolean()
      self.obj6600.Copy.setValue(('Copy from LHS', 1))
      self.obj6600.Copy.config = 0
      self.obj6600.Specify=ATOM3Constraint()
      self.obj6600.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj660.GGset2Any['isMetaRole']= self.obj6600
      self.obj6601= AttrCalc()
      self.obj6601.Copy=ATOM3Boolean()
      self.obj6601.Copy.setValue(('Copy from LHS', 1))
      self.obj6601.Copy.config = 0
      self.obj6601.Specify=ATOM3Constraint()
      self.obj6601.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj660.GGset2Any['hasActions']= self.obj6601
      self.obj6602= AttrCalc()
      self.obj6602.Copy=ATOM3Boolean()
      self.obj6602.Copy.setValue(('Copy from LHS', 1))
      self.obj6602.Copy.config = 0
      self.obj6602.Specify=ATOM3Constraint()
      self.obj6602.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj660.GGset2Any['ID']= self.obj6602
      self.obj6603= AttrCalc()
      self.obj6603.Copy=ATOM3Boolean()
      self.obj6603.Copy.setValue(('Copy from LHS', 1))
      self.obj6603.Copy.config = 0
      self.obj6603.Specify=ATOM3Constraint()
      self.obj6603.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj660.GGset2Any['name']= self.obj6603

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj660)
      self.obj660.postAction( self.RHS.CREATE )

      self.obj661=isPartOfOrgUnit(parent)
      self.obj661.preAction( self.RHS.CREATE )
      self.obj661.isGraphObjectVisual = True

      if(hasattr(self.obj661, '_setHierarchicalLink')):
        self.obj661._setHierarchicalLink(True)

      # ID
      self.obj661.ID.setValue('pOU|0')

      self.obj661.GGLabel.setValue(6)
      self.obj661.graphClass_= graph_isPartOfOrgUnit
      if parent.genGraphics:
         new_obj = graph_isPartOfOrgUnit(84.8158842791,109.370539238,self.obj661)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj661.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj661)
      self.obj661.postAction( self.RHS.CREATE )

      self.obj662=canHaveRole(parent)
      self.obj662.preAction( self.RHS.CREATE )
      self.obj662.isGraphObjectVisual = True

      if(hasattr(self.obj662, '_setHierarchicalLink')):
        self.obj662._setHierarchicalLink(True)

      # ID
      self.obj662.ID.setValue('OUR|0')

      self.obj662.GGLabel.setValue(3)
      self.obj662.graphClass_= graph_canHaveRole
      if parent.genGraphics:
         new_obj = graph_canHaveRole(148.95,152.35,self.obj662)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj662.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj662)
      self.obj662.postAction( self.RHS.CREATE )

      self.obj658.out_connections_.append(self.obj662)
      self.obj662.in_connections_.append(self.obj658)
      self.obj658.graphObject_.pendingConnections.append((self.obj658.graphObject_.tag, self.obj662.graphObject_.tag, [172.0, 262.0, 148.57342374154044, 141.9178391958854], 2, 0))
      self.obj658.out_connections_.append(self.obj661)
      self.obj661.in_connections_.append(self.obj658)
      self.obj658.graphObject_.pendingConnections.append((self.obj658.graphObject_.tag, self.obj661.graphObject_.tag, [172.0, 262.0, 84.81588427919901, 109.37053923790864], 0, True))
      self.obj661.out_connections_.append(self.obj659)
      self.obj659.in_connections_.append(self.obj661)
      self.obj661.graphObject_.pendingConnections.append((self.obj661.graphObject_.tag, self.obj659.graphObject_.tag, [138.0, 54.0, 146.5, 173.5], 0, True))
      self.obj662.out_connections_.append(self.obj660)
      self.obj660.in_connections_.append(self.obj662)
      self.obj662.graphObject_.pendingConnections.append((self.obj662.graphObject_.tag, self.obj660.graphObject_.tag, [271.0, 251.0, 211.39913777316735, 113.1006935442384], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      return 1
      

   def action(self, graphID, isograph, atom3i):
      pass

