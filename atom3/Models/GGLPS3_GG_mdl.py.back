from GraphGrammarEdit import *
from GGruleEdit import *

def savedTrans(self):
   self.EditingGraphGrammar= GraphGrammarEdit(None, self)
   self.EditingGraphGrammar.Name=ATOM3String('LSPExample', 20)
   self.EditingGraphGrammar.Rules=ATOM3List([ 1, 1, 1, 0],GGruleEdit,None, self)
   lcobj0=[]
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('AddRoles', 20)
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 0))
   cobj0.SubtypesMatching.config = 0

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

   cobj0.LHS = ASG_LSMASOMM(self)

   self.obj242=OrgUnit(self)
   self.obj242.preAction( cobj0.LHS.CREATE )
   self.obj242.isGraphObjectVisual = True

   if(hasattr(self.obj242, '_setHierarchicalLink')):
     self.obj242._setHierarchicalLink(False)

   # Individual
   self.obj242.Individual.setValue(('1', 0))
   self.obj242.Individual.config = 0

   # hasActions
   self.obj242.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj242.hasActions.setValue(lcobj2)
   self.obj242.hasActions.setNone()

   # ID
   self.obj242.ID.setValue('')
   self.obj242.ID.setNone()

   # name
   self.obj242.name.setValue('')
   self.obj242.name.setNone()

   # UnitSize
   self.obj242.UnitSize.setValue('Individual')

   self.obj242.GGLabel.setValue(1)
   self.obj242.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(60.0,120.0,self.obj242)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj242.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj242)
   self.obj242.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_LSMASOMM(self)

   self.obj244=OrgUnit(self)
   self.obj244.preAction( cobj0.RHS.CREATE )
   self.obj244.isGraphObjectVisual = True

   if(hasattr(self.obj244, '_setHierarchicalLink')):
     self.obj244._setHierarchicalLink(False)

   # Individual
   self.obj244.Individual.setValue(('1', 0))
   self.obj244.Individual.config = 0

   # hasActions
   self.obj244.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj244.hasActions.setValue(lcobj2)

   # ID
   self.obj244.ID.setValue('OU|0')

   # name
   self.obj244.name.setValue('OUname')

   # UnitSize
   self.obj244.UnitSize.setValue('Individual')

   self.obj244.GGLabel.setValue(1)
   self.obj244.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(40.0,140.0,self.obj244)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj244.graphObject_ = new_obj
   self.obj2440= AttrCalc()
   self.obj2440.Copy=ATOM3Boolean()
   self.obj2440.Copy.setValue(('Copy from LHS', 1))
   self.obj2440.Copy.config = 0
   self.obj2440.Specify=ATOM3Constraint()
   self.obj2440.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj244.GGset2Any['Individual']= self.obj2440
   self.obj2441= AttrCalc()
   self.obj2441.Copy=ATOM3Boolean()
   self.obj2441.Copy.setValue(('Copy from LHS', 1))
   self.obj2441.Copy.config = 0
   self.obj2441.Specify=ATOM3Constraint()
   self.obj2441.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj244.GGset2Any['hasActions']= self.obj2441
   self.obj2442= AttrCalc()
   self.obj2442.Copy=ATOM3Boolean()
   self.obj2442.Copy.setValue(('Copy from LHS', 1))
   self.obj2442.Copy.config = 0
   self.obj2442.Specify=ATOM3Constraint()
   self.obj2442.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj244.GGset2Any['ID']= self.obj2442
   self.obj2443= AttrCalc()
   self.obj2443.Copy=ATOM3Boolean()
   self.obj2443.Copy.setValue(('Copy from LHS', 1))
   self.obj2443.Copy.config = 0
   self.obj2443.Specify=ATOM3Constraint()
   self.obj2443.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj244.GGset2Any['name']= self.obj2443
   self.obj2444= AttrCalc()
   self.obj2444.Copy=ATOM3Boolean()
   self.obj2444.Copy.setValue(('Copy from LHS', 1))
   self.obj2444.Copy.config = 0
   self.obj2444.Specify=ATOM3Constraint()
   self.obj2444.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj244.GGset2Any['UnitSize']= self.obj2444

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj244)
   self.obj244.postAction( cobj0.RHS.CREATE )

   self.obj245=Role(self)
   self.obj245.preAction( cobj0.RHS.CREATE )
   self.obj245.isGraphObjectVisual = True

   if(hasattr(self.obj245, '_setHierarchicalLink')):
     self.obj245._setHierarchicalLink(False)

   # isMetaRole
   self.obj245.isMetaRole.setValue((None, 0))
   self.obj245.isMetaRole.config = 0

   # hasActions
   self.obj245.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj245.hasActions.setValue(lcobj2)

   # ID
   self.obj245.ID.setValue('R|90')

   # name
   self.obj245.name.setValue('PartyFounder')

   self.obj245.GGLabel.setValue(2)
   self.obj245.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(250.0,50.0,self.obj245)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj245.graphObject_ = new_obj
   self.obj2450= AttrCalc()
   self.obj2450.Copy=ATOM3Boolean()
   self.obj2450.Copy.setValue(('Copy from LHS', 0))
   self.obj2450.Copy.config = 0
   self.obj2450.Specify=ATOM3Constraint()
   self.obj2450.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj245.GGset2Any['isMetaRole']= self.obj2450
   self.obj2451= AttrCalc()
   self.obj2451.Copy=ATOM3Boolean()
   self.obj2451.Copy.setValue(('Copy from LHS', 0))
   self.obj2451.Copy.config = 0
   self.obj2451.Specify=ATOM3Constraint()
   self.obj2451.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj245.GGset2Any['hasActions']= self.obj2451
   self.obj2452= AttrCalc()
   self.obj2452.Copy=ATOM3Boolean()
   self.obj2452.Copy.setValue(('Copy from LHS', 0))
   self.obj2452.Copy.config = 0
   self.obj2452.Specify=ATOM3Constraint()
   self.obj2452.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj245.GGset2Any['ID']= self.obj2452
   self.obj2453= AttrCalc()
   self.obj2453.Copy=ATOM3Boolean()
   self.obj2453.Copy.setValue(('Copy from LHS', 0))
   self.obj2453.Copy.config = 0
   self.obj2453.Specify=ATOM3Constraint()
   self.obj2453.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj245.GGset2Any['name']= self.obj2453

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj245)
   self.obj245.postAction( cobj0.RHS.CREATE )

   self.obj246=Role(self)
   self.obj246.preAction( cobj0.RHS.CREATE )
   self.obj246.isGraphObjectVisual = True

   if(hasattr(self.obj246, '_setHierarchicalLink')):
     self.obj246._setHierarchicalLink(False)

   # isMetaRole
   self.obj246.isMetaRole.setValue((None, 0))
   self.obj246.isMetaRole.config = 0

   # hasActions
   self.obj246.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj246.hasActions.setValue(lcobj2)

   # ID
   self.obj246.ID.setValue('R|91')

   # name
   self.obj246.name.setValue('PartyMember')

   self.obj246.GGLabel.setValue(3)
   self.obj246.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(270.0,170.0,self.obj246)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj246.graphObject_ = new_obj
   self.obj2460= AttrCalc()
   self.obj2460.Copy=ATOM3Boolean()
   self.obj2460.Copy.setValue(('Copy from LHS', 0))
   self.obj2460.Copy.config = 0
   self.obj2460.Specify=ATOM3Constraint()
   self.obj2460.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj246.GGset2Any['isMetaRole']= self.obj2460
   self.obj2461= AttrCalc()
   self.obj2461.Copy=ATOM3Boolean()
   self.obj2461.Copy.setValue(('Copy from LHS', 0))
   self.obj2461.Copy.config = 0
   self.obj2461.Specify=ATOM3Constraint()
   self.obj2461.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj246.GGset2Any['hasActions']= self.obj2461
   self.obj2462= AttrCalc()
   self.obj2462.Copy=ATOM3Boolean()
   self.obj2462.Copy.setValue(('Copy from LHS', 0))
   self.obj2462.Copy.config = 0
   self.obj2462.Specify=ATOM3Constraint()
   self.obj2462.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj246.GGset2Any['ID']= self.obj2462
   self.obj2463= AttrCalc()
   self.obj2463.Copy=ATOM3Boolean()
   self.obj2463.Copy.setValue(('Copy from LHS', 0))
   self.obj2463.Copy.config = 0
   self.obj2463.Specify=ATOM3Constraint()
   self.obj2463.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj246.GGset2Any['name']= self.obj2463

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj246)
   self.obj246.postAction( cobj0.RHS.CREATE )

   self.obj247=canHaveRole(self)
   self.obj247.preAction( cobj0.RHS.CREATE )
   self.obj247.isGraphObjectVisual = True

   if(hasattr(self.obj247, '_setHierarchicalLink')):
     self.obj247._setHierarchicalLink(True)

   # ID
   self.obj247.ID.setValue('OUR|90')

   self.obj247.GGLabel.setValue(4)
   self.obj247.graphClass_= graph_canHaveRole
   if self.genGraphics:
      new_obj = graph_canHaveRole(178.5,145.5,self.obj247)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj247.graphObject_ = new_obj
   self.obj2470= AttrCalc()
   self.obj2470.Copy=ATOM3Boolean()
   self.obj2470.Copy.setValue(('Copy from LHS', 0))
   self.obj2470.Copy.config = 0
   self.obj2470.Specify=ATOM3Constraint()
   self.obj2470.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj247.GGset2Any['ID']= self.obj2470

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj247)
   self.obj247.postAction( cobj0.RHS.CREATE )

   self.obj244.out_connections_.append(self.obj247)
   self.obj247.in_connections_.append(self.obj244)
   self.obj244.graphObject_.pendingConnections.append((self.obj244.graphObject_.tag, self.obj247.graphObject_.tag, [71.0, 203.0, 178.5, 145.5], 0, True))
   self.obj247.out_connections_.append(self.obj245)
   self.obj245.in_connections_.append(self.obj247)
   self.obj247.graphObject_.pendingConnections.append((self.obj247.graphObject_.tag, self.obj245.graphObject_.tag, [286.0, 102.0, 178.5, 152.5], 0, True))
   self.obj247.out_connections_.append(self.obj246)
   self.obj246.in_connections_.append(self.obj247)
   self.obj247.graphObject_.pendingConnections.append((self.obj247.graphObject_.tag, self.obj246.graphObject_.tag, [306.0, 222.0, 178.5, 152.5], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 1\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))


