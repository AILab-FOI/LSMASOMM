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

      self.obj252=OrgUnit(parent)
      self.obj252.preAction( self.LHS.CREATE )
      self.obj252.isGraphObjectVisual = True

      if(hasattr(self.obj252, '_setHierarchicalLink')):
        self.obj252._setHierarchicalLink(False)

      # Individual
      self.obj252.Individual.setNone()
      self.obj252.Individual.config = 0

      # hasActions
      self.obj252.hasActions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      cobj2=ATOM3String('ChangeRole', 20)
      lcobj2.append(cobj2)
      self.obj252.hasActions.setValue(lcobj2)
      self.obj252.hasActions.setNone()

      # ID
      self.obj252.ID.setValue('')
      self.obj252.ID.setNone()

      # name
      self.obj252.name.setValue('')
      self.obj252.name.setNone()

      # UnitSize
      self.obj252.UnitSize.setValue('Individual')

      self.obj252.GGLabel.setValue(1)
      self.obj252.graphClass_= graph_OrgUnit
      if parent.genGraphics:
         new_obj = graph_OrgUnit(0,0,self.obj252)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj252.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj252)
      self.obj252.postAction( self.LHS.CREATE )

      self.obj253=Role(parent)
      self.obj253.preAction( self.LHS.CREATE )
      self.obj253.isGraphObjectVisual = True

      if(hasattr(self.obj253, '_setHierarchicalLink')):
        self.obj253._setHierarchicalLink(False)

      # isMetaRole
      self.obj253.isMetaRole.setNone()
      self.obj253.isMetaRole.config = 0

      # hasActions
      self.obj253.hasActions.setActionFlags([ 0, 0, 1, 0])
      lcobj2 =[]
      self.obj253.hasActions.setValue(lcobj2)
      self.obj253.hasActions.setNone()

      # ID
      self.obj253.ID.setValue('')
      self.obj253.ID.setNone()

      # name
      self.obj253.name.setValue('PartyFounder')

      self.obj253.GGLabel.setValue(2)
      self.obj253.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(93,0,self.obj253)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj253.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj253)
      self.obj253.postAction( self.LHS.CREATE )

      self.obj254=canHaveRole(parent)
      self.obj254.preAction( self.LHS.CREATE )
      self.obj254.isGraphObjectVisual = True

      if(hasattr(self.obj254, '_setHierarchicalLink')):
        self.obj254._setHierarchicalLink(True)

      # ID
      self.obj254.ID.setValue('OUR|0')

      self.obj254.GGLabel.setValue(3)
      self.obj254.graphClass_= graph_canHaveRole
      if parent.genGraphics:
         new_obj = graph_canHaveRole(82.7757140317,49.5328543483,self.obj254)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj254.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj254)
      self.obj254.postAction( self.LHS.CREATE )

      self.obj252.out_connections_.append(self.obj254)
      self.obj254.in_connections_.append(self.obj252)
      self.obj252.graphObject_.pendingConnections.append((self.obj252.graphObject_.tag, self.obj254.graphObject_.tag, [320.0, 383.0, 82.7757140313197, 49.532854348516736], 0, True))
      self.obj254.out_connections_.append(self.obj253)
      self.obj253.in_connections_.append(self.obj254)
      self.obj254.graphObject_.pendingConnections.append((self.obj254.graphObject_.tag, self.obj253.graphObject_.tag, [318.0, 18.0, 248.5, 202.5], 0, True))

      self.RHS = ASG_LSMASOMM(parent)

      self.obj256=OrgUnit(parent)
      self.obj256.preAction( self.RHS.CREATE )
      self.obj256.isGraphObjectVisual = True

      if(hasattr(self.obj256, '_setHierarchicalLink')):
        self.obj256._setHierarchicalLink(False)

      # Individual
      self.obj256.Individual.setNone()
      self.obj256.Individual.config = 0

      # hasActions
      self.obj256.hasActions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      cobj2=ATOM3String('ChangeRole', 20)
      lcobj2.append(cobj2)
      self.obj256.hasActions.setValue(lcobj2)
      self.obj256.hasActions.setNone()

      # ID
      self.obj256.ID.setValue('')
      self.obj256.ID.setNone()

      # name
      self.obj256.name.setValue('')
      self.obj256.name.setNone()

      # UnitSize
      self.obj256.UnitSize.setValue('Individual')

      self.obj256.GGLabel.setValue(1)
      self.obj256.graphClass_= graph_OrgUnit
      if parent.genGraphics:
         new_obj = graph_OrgUnit(0,104,self.obj256)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj256.graphObject_ = new_obj
      self.obj2560= AttrCalc()
      self.obj2560.Copy=ATOM3Boolean()
      self.obj2560.Copy.setValue(('Copy from LHS', 1))
      self.obj2560.Copy.config = 0
      self.obj2560.Specify=ATOM3Constraint()
      self.obj2560.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj256.GGset2Any['ID']= self.obj2560
      self.obj2561= AttrCalc()
      self.obj2561.Copy=ATOM3Boolean()
      self.obj2561.Copy.setValue(('Copy from LHS', 1))
      self.obj2561.Copy.config = 0
      self.obj2561.Specify=ATOM3Constraint()
      self.obj2561.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj256.GGset2Any['Individual']= self.obj2561
      self.obj2562= AttrCalc()
      self.obj2562.Copy=ATOM3Boolean()
      self.obj2562.Copy.setValue(('Copy from LHS', 1))
      self.obj2562.Copy.config = 0
      self.obj2562.Specify=ATOM3Constraint()
      self.obj2562.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj256.GGset2Any['hasActions']= self.obj2562
      self.obj2563= AttrCalc()
      self.obj2563.Copy=ATOM3Boolean()
      self.obj2563.Copy.setValue(('Copy from LHS', 1))
      self.obj2563.Copy.config = 0
      self.obj2563.Specify=ATOM3Constraint()
      self.obj2563.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj256.GGset2Any['UnitSize']= self.obj2563
      self.obj2564= AttrCalc()
      self.obj2564.Copy=ATOM3Boolean()
      self.obj2564.Copy.setValue(('Copy from LHS', 1))
      self.obj2564.Copy.config = 0
      self.obj2564.Specify=ATOM3Constraint()
      self.obj2564.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj256.GGset2Any['name']= self.obj2564

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj256)
      self.obj256.postAction( self.RHS.CREATE )

      self.obj257=OrgUnit(parent)
      self.obj257.preAction( self.RHS.CREATE )
      self.obj257.isGraphObjectVisual = True

      if(hasattr(self.obj257, '_setHierarchicalLink')):
        self.obj257._setHierarchicalLink(False)

      # Individual
      self.obj257.Individual.setValue(('1', 0))
      self.obj257.Individual.config = 0

      # hasActions
      self.obj257.hasActions.setActionFlags([ 1, 1, 1, 0])
      lcobj2 =[]
      cobj2=ATOM3String('ChangeRole', 20)
      lcobj2.append(cobj2)
      self.obj257.hasActions.setValue(lcobj2)

      # ID
      self.obj257.ID.setValue('OU|99')

      # name
      self.obj257.name.setValue('Party')

      # UnitSize
      self.obj257.UnitSize.setValue('Group')

      self.obj257.GGLabel.setValue(5)
      self.obj257.graphClass_= graph_OrgUnit
      if parent.genGraphics:
         new_obj = graph_OrgUnit(248,104,self.obj257)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj257.graphObject_ = new_obj
      self.obj2570= AttrCalc()
      self.obj2570.Copy=ATOM3Boolean()
      self.obj2570.Copy.setValue(('Copy from LHS', 0))
      self.obj2570.Copy.config = 0
      self.obj2570.Specify=ATOM3Constraint()
      self.obj2570.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj257.GGset2Any['ID']= self.obj2570
      self.obj2571= AttrCalc()
      self.obj2571.Copy=ATOM3Boolean()
      self.obj2571.Copy.setValue(('Copy from LHS', 0))
      self.obj2571.Copy.config = 0
      self.obj2571.Specify=ATOM3Constraint()
      self.obj2571.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj257.GGset2Any['Individual']= self.obj2571
      self.obj2572= AttrCalc()
      self.obj2572.Copy=ATOM3Boolean()
      self.obj2572.Copy.setValue(('Copy from LHS', 0))
      self.obj2572.Copy.config = 0
      self.obj2572.Specify=ATOM3Constraint()
      self.obj2572.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj257.GGset2Any['hasActions']= self.obj2572
      self.obj2573= AttrCalc()
      self.obj2573.Copy=ATOM3Boolean()
      self.obj2573.Copy.setValue(('Copy from LHS', 0))
      self.obj2573.Copy.config = 0
      self.obj2573.Specify=ATOM3Constraint()
      self.obj2573.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj257.GGset2Any['UnitSize']= self.obj2573
      self.obj2574= AttrCalc()
      self.obj2574.Copy=ATOM3Boolean()
      self.obj2574.Copy.setValue(('Copy from LHS', 0))
      self.obj2574.Copy.config = 0
      self.obj2574.Specify=ATOM3Constraint()
      self.obj2574.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj257.GGset2Any['name']= self.obj2574

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj257)
      self.obj257.postAction( self.RHS.CREATE )

      self.obj258=Role(parent)
      self.obj258.preAction( self.RHS.CREATE )
      self.obj258.isGraphObjectVisual = True

      if(hasattr(self.obj258, '_setHierarchicalLink')):
        self.obj258._setHierarchicalLink(False)

      # isMetaRole
      self.obj258.isMetaRole.setNone()
      self.obj258.isMetaRole.config = 0

      # hasActions
      self.obj258.hasActions.setActionFlags([ 0, 0, 1, 0])
      lcobj2 =[]
      self.obj258.hasActions.setValue(lcobj2)
      self.obj258.hasActions.setNone()

      # ID
      self.obj258.ID.setValue('')
      self.obj258.ID.setNone()

      # name
      self.obj258.name.setValue('PartyFounder')

      self.obj258.GGLabel.setValue(2)
      self.obj258.graphClass_= graph_Role
      if parent.genGraphics:
         new_obj = graph_Role(124,0,self.obj258)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj258.graphObject_ = new_obj
      self.obj2580= AttrCalc()
      self.obj2580.Copy=ATOM3Boolean()
      self.obj2580.Copy.setValue(('Copy from LHS', 1))
      self.obj2580.Copy.config = 0
      self.obj2580.Specify=ATOM3Constraint()
      self.obj2580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj258.GGset2Any['isMetaRole']= self.obj2580
      self.obj2581= AttrCalc()
      self.obj2581.Copy=ATOM3Boolean()
      self.obj2581.Copy.setValue(('Copy from LHS', 1))
      self.obj2581.Copy.config = 0
      self.obj2581.Specify=ATOM3Constraint()
      self.obj2581.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj258.GGset2Any['hasActions']= self.obj2581
      self.obj2582= AttrCalc()
      self.obj2582.Copy=ATOM3Boolean()
      self.obj2582.Copy.setValue(('Copy from LHS', 1))
      self.obj2582.Copy.config = 0
      self.obj2582.Specify=ATOM3Constraint()
      self.obj2582.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj258.GGset2Any['ID']= self.obj2582
      self.obj2583= AttrCalc()
      self.obj2583.Copy=ATOM3Boolean()
      self.obj2583.Copy.setValue(('Copy from LHS', 1))
      self.obj2583.Copy.config = 0
      self.obj2583.Specify=ATOM3Constraint()
      self.obj2583.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
      self.obj258.GGset2Any['name']= self.obj2583

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj258)
      self.obj258.postAction( self.RHS.CREATE )

      self.obj259=isPartOfOrgUnit(parent)
      self.obj259.preAction( self.RHS.CREATE )
      self.obj259.isGraphObjectVisual = True

      if(hasattr(self.obj259, '_setHierarchicalLink')):
        self.obj259._setHierarchicalLink(True)

      # ID
      self.obj259.ID.setValue('pOU|0')

      self.obj259.GGLabel.setValue(6)
      self.obj259.graphClass_= graph_isPartOfOrgUnit
      if parent.genGraphics:
         new_obj = graph_isPartOfOrgUnit(170.95,135.5,self.obj259)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj259.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj259)
      self.obj259.postAction( self.RHS.CREATE )

      self.obj260=canHaveRole(parent)
      self.obj260.preAction( self.RHS.CREATE )
      self.obj260.isGraphObjectVisual = True

      if(hasattr(self.obj260, '_setHierarchicalLink')):
        self.obj260._setHierarchicalLink(True)

      # ID
      self.obj260.ID.setValue('OUR|0')

      self.obj260.GGLabel.setValue(3)
      self.obj260.graphClass_= graph_canHaveRole
      if parent.genGraphics:
         new_obj = graph_canHaveRole(96.0835477534,103.612551906,self.obj260)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj260.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj260)
      self.obj260.postAction( self.RHS.CREATE )

      self.obj256.out_connections_.append(self.obj260)
      self.obj260.in_connections_.append(self.obj256)
      self.obj256.graphObject_.pendingConnections.append((self.obj256.graphObject_.tag, self.obj260.graphObject_.tag, [172.0, 262.0, 95.70697149494045, 93.18039110188538], 2, 0))
      self.obj256.out_connections_.append(self.obj259)
      self.obj259.in_connections_.append(self.obj256)
      self.obj256.graphObject_.pendingConnections.append((self.obj256.graphObject_.tag, self.obj259.graphObject_.tag, [172.0, 262.0, 170.9500000000995, 135.49999999995433], 0, True))
      self.obj259.out_connections_.append(self.obj257)
      self.obj257.in_connections_.append(self.obj259)
      self.obj259.graphObject_.pendingConnections.append((self.obj259.graphObject_.tag, self.obj257.graphObject_.tag, [138.0, 54.0, 146.5, 173.5], 0, True))
      self.obj260.out_connections_.append(self.obj258)
      self.obj258.in_connections_.append(self.obj260)
      self.obj260.graphObject_.pendingConnections.append((self.obj260.graphObject_.tag, self.obj258.graphObject_.tag, [271.0, 251.0, 211.39913777316735, 113.1006935442384], 2, 0))

   def condition(self, graphID, isograph, atom3i):
      return 1
      

   def action(self, graphID, isograph, atom3i):
      pass

