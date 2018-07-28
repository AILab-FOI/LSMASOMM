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

   self.obj49=OrgUnit(self)
   self.obj49.preAction( cobj0.LHS.CREATE )
   self.obj49.isGraphObjectVisual = True

   if(hasattr(self.obj49, '_setHierarchicalLink')):
     self.obj49._setHierarchicalLink(False)

   # Individual
   self.obj49.Individual.setValue(('1', 0))
   self.obj49.Individual.config = 0

   # hasActions
   self.obj49.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj49.hasActions.setValue(lcobj2)

   # ID
   self.obj49.ID.setValue('')
   self.obj49.ID.setNone()

   # name
   self.obj49.name.setValue('')
   self.obj49.name.setNone()

   # UnitSize
   self.obj49.UnitSize.setValue('Individual')

   self.obj49.GGLabel.setValue(1)
   self.obj49.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(60.0,120.0,self.obj49)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj49.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj49)
   self.obj49.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_LSMASOMM(self)

   self.obj51=OrgUnit(self)
   self.obj51.preAction( cobj0.RHS.CREATE )
   self.obj51.isGraphObjectVisual = True

   if(hasattr(self.obj51, '_setHierarchicalLink')):
     self.obj51._setHierarchicalLink(False)

   # Individual
   self.obj51.Individual.setValue(('1', 0))
   self.obj51.Individual.config = 0

   # hasActions
   self.obj51.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj51.hasActions.setValue(lcobj2)

   # ID
   self.obj51.ID.setValue('OU|0')

   # name
   self.obj51.name.setValue('OUname')

   # UnitSize
   self.obj51.UnitSize.setValue('Individual')

   self.obj51.GGLabel.setValue(1)
   self.obj51.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(40.0,140.0,self.obj51)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj51.graphObject_ = new_obj
   self.obj510= AttrCalc()
   self.obj510.Copy=ATOM3Boolean()
   self.obj510.Copy.setValue(('Copy from LHS', 1))
   self.obj510.Copy.config = 0
   self.obj510.Specify=ATOM3Constraint()
   self.obj510.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj51.GGset2Any['UnitSize']= self.obj510
   self.obj511= AttrCalc()
   self.obj511.Copy=ATOM3Boolean()
   self.obj511.Copy.setValue(('Copy from LHS', 1))
   self.obj511.Copy.config = 0
   self.obj511.Specify=ATOM3Constraint()
   self.obj511.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj51.GGset2Any['Individual']= self.obj511
   self.obj512= AttrCalc()
   self.obj512.Copy=ATOM3Boolean()
   self.obj512.Copy.setValue(('Copy from LHS', 1))
   self.obj512.Copy.config = 0
   self.obj512.Specify=ATOM3Constraint()
   self.obj512.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj51.GGset2Any['hasActions']= self.obj512
   self.obj513= AttrCalc()
   self.obj513.Copy=ATOM3Boolean()
   self.obj513.Copy.setValue(('Copy from LHS', 1))
   self.obj513.Copy.config = 0
   self.obj513.Specify=ATOM3Constraint()
   self.obj513.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj51.GGset2Any['name']= self.obj513
   self.obj514= AttrCalc()
   self.obj514.Copy=ATOM3Boolean()
   self.obj514.Copy.setValue(('Copy from LHS', 1))
   self.obj514.Copy.config = 0
   self.obj514.Specify=ATOM3Constraint()
   self.obj514.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj51.GGset2Any['ID']= self.obj514

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj51)
   self.obj51.postAction( cobj0.RHS.CREATE )

   self.obj52=Role(self)
   self.obj52.preAction( cobj0.RHS.CREATE )
   self.obj52.isGraphObjectVisual = True

   if(hasattr(self.obj52, '_setHierarchicalLink')):
     self.obj52._setHierarchicalLink(False)

   # isMetaRole
   self.obj52.isMetaRole.setValue((None, 0))
   self.obj52.isMetaRole.config = 0

   # hasActions
   self.obj52.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj52.hasActions.setValue(lcobj2)

   # ID
   self.obj52.ID.setValue('R|90')

   # name
   self.obj52.name.setValue('PartyFounder')

   self.obj52.GGLabel.setValue(2)
   self.obj52.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(250.0,50.0,self.obj52)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj52.graphObject_ = new_obj
   self.obj520= AttrCalc()
   self.obj520.Copy=ATOM3Boolean()
   self.obj520.Copy.setValue(('Copy from LHS', 0))
   self.obj520.Copy.config = 0
   self.obj520.Specify=ATOM3Constraint()
   self.obj520.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj52.GGset2Any['isMetaRole']= self.obj520
   self.obj521= AttrCalc()
   self.obj521.Copy=ATOM3Boolean()
   self.obj521.Copy.setValue(('Copy from LHS', 0))
   self.obj521.Copy.config = 0
   self.obj521.Specify=ATOM3Constraint()
   self.obj521.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj52.GGset2Any['hasActions']= self.obj521
   self.obj522= AttrCalc()
   self.obj522.Copy=ATOM3Boolean()
   self.obj522.Copy.setValue(('Copy from LHS', 0))
   self.obj522.Copy.config = 0
   self.obj522.Specify=ATOM3Constraint()
   self.obj522.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj52.GGset2Any['ID']= self.obj522
   self.obj523= AttrCalc()
   self.obj523.Copy=ATOM3Boolean()
   self.obj523.Copy.setValue(('Copy from LHS', 0))
   self.obj523.Copy.config = 0
   self.obj523.Specify=ATOM3Constraint()
   self.obj523.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj52.GGset2Any['name']= self.obj523

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj52)
   self.obj52.postAction( cobj0.RHS.CREATE )

   self.obj53=Role(self)
   self.obj53.preAction( cobj0.RHS.CREATE )
   self.obj53.isGraphObjectVisual = True

   if(hasattr(self.obj53, '_setHierarchicalLink')):
     self.obj53._setHierarchicalLink(False)

   # isMetaRole
   self.obj53.isMetaRole.setValue((None, 0))
   self.obj53.isMetaRole.config = 0

   # hasActions
   self.obj53.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj53.hasActions.setValue(lcobj2)

   # ID
   self.obj53.ID.setValue('R|91')

   # name
   self.obj53.name.setValue('PartyMember')

   self.obj53.GGLabel.setValue(3)
   self.obj53.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(270.0,170.0,self.obj53)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj53.graphObject_ = new_obj
   self.obj530= AttrCalc()
   self.obj530.Copy=ATOM3Boolean()
   self.obj530.Copy.setValue(('Copy from LHS', 0))
   self.obj530.Copy.config = 0
   self.obj530.Specify=ATOM3Constraint()
   self.obj530.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj53.GGset2Any['isMetaRole']= self.obj530
   self.obj531= AttrCalc()
   self.obj531.Copy=ATOM3Boolean()
   self.obj531.Copy.setValue(('Copy from LHS', 0))
   self.obj531.Copy.config = 0
   self.obj531.Specify=ATOM3Constraint()
   self.obj531.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj53.GGset2Any['hasActions']= self.obj531
   self.obj532= AttrCalc()
   self.obj532.Copy=ATOM3Boolean()
   self.obj532.Copy.setValue(('Copy from LHS', 0))
   self.obj532.Copy.config = 0
   self.obj532.Specify=ATOM3Constraint()
   self.obj532.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj53.GGset2Any['ID']= self.obj532
   self.obj533= AttrCalc()
   self.obj533.Copy=ATOM3Boolean()
   self.obj533.Copy.setValue(('Copy from LHS', 0))
   self.obj533.Copy.config = 0
   self.obj533.Specify=ATOM3Constraint()
   self.obj533.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj53.GGset2Any['name']= self.obj533

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj53)
   self.obj53.postAction( cobj0.RHS.CREATE )

   self.obj54=canHaveRole(self)
   self.obj54.preAction( cobj0.RHS.CREATE )
   self.obj54.isGraphObjectVisual = True

   if(hasattr(self.obj54, '_setHierarchicalLink')):
     self.obj54._setHierarchicalLink(True)

   # ID
   self.obj54.ID.setValue('OUR|90')

   self.obj54.GGLabel.setValue(4)
   self.obj54.graphClass_= graph_canHaveRole
   if self.genGraphics:
      new_obj = graph_canHaveRole(178.5,145.5,self.obj54)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj54.graphObject_ = new_obj
   self.obj540= AttrCalc()
   self.obj540.Copy=ATOM3Boolean()
   self.obj540.Copy.setValue(('Copy from LHS', 0))
   self.obj540.Copy.config = 0
   self.obj540.Specify=ATOM3Constraint()
   self.obj540.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj54.GGset2Any['ID']= self.obj540

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj54)
   self.obj54.postAction( cobj0.RHS.CREATE )

   self.obj51.out_connections_.append(self.obj54)
   self.obj54.in_connections_.append(self.obj51)
   self.obj51.graphObject_.pendingConnections.append((self.obj51.graphObject_.tag, self.obj54.graphObject_.tag, [71.0, 203.0, 178.5, 145.5], 0, True))
   self.obj54.out_connections_.append(self.obj52)
   self.obj52.in_connections_.append(self.obj54)
   self.obj54.graphObject_.pendingConnections.append((self.obj54.graphObject_.tag, self.obj52.graphObject_.tag, [286.0, 102.0, 178.5, 152.5], 0, True))
   self.obj54.out_connections_.append(self.obj53)
   self.obj53.in_connections_.append(self.obj54)
   self.obj54.graphObject_.pendingConnections.append((self.obj54.graphObject_.tag, self.obj53.graphObject_.tag, [306.0, 222.0, 178.5, 152.5], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'return 1\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreateParty', 20)
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

   self.obj244=OrgUnit(self)
   self.obj244.preAction( cobj0.LHS.CREATE )
   self.obj244.isGraphObjectVisual = True

   if(hasattr(self.obj244, '_setHierarchicalLink')):
     self.obj244._setHierarchicalLink(False)

   # Individual
   self.obj244.Individual.setNone()
   self.obj244.Individual.config = 0

   # hasActions
   self.obj244.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj244.hasActions.setValue(lcobj2)
   self.obj244.hasActions.setNone()

   # ID
   self.obj244.ID.setValue('')
   self.obj244.ID.setNone()

   # name
   self.obj244.name.setValue('')
   self.obj244.name.setNone()

   # UnitSize
   self.obj244.UnitSize.setValue('Individual')

   self.obj244.GGLabel.setValue(1)
   self.obj244.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(60.0,56.0,self.obj244)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj244.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj244)
   self.obj244.postAction( cobj0.LHS.CREATE )

   self.obj245=Role(self)
   self.obj245.preAction( cobj0.LHS.CREATE )
   self.obj245.isGraphObjectVisual = True

   if(hasattr(self.obj245, '_setHierarchicalLink')):
     self.obj245._setHierarchicalLink(False)

   # isMetaRole
   self.obj245.isMetaRole.setNone()
   self.obj245.isMetaRole.config = 0

   # hasActions
   self.obj245.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj245.hasActions.setValue(lcobj2)
   self.obj245.hasActions.setNone()

   # ID
   self.obj245.ID.setValue('')
   self.obj245.ID.setNone()

   # name
   self.obj245.name.setValue('PartyFounder')

   self.obj245.GGLabel.setValue(2)
   self.obj245.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(153.0,56.0,self.obj245)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj245.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj245)
   self.obj245.postAction( cobj0.LHS.CREATE )

   self.obj246=canHaveRole(self)
   self.obj246.preAction( cobj0.LHS.CREATE )
   self.obj246.isGraphObjectVisual = True

   if(hasattr(self.obj246, '_setHierarchicalLink')):
     self.obj246._setHierarchicalLink(True)

   # ID
   self.obj246.ID.setValue('OUR|0')

   self.obj246.GGLabel.setValue(3)
   self.obj246.graphClass_= graph_canHaveRole
   if self.genGraphics:
      new_obj = graph_canHaveRole(142.775714032,105.532854348,self.obj246)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj246.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj246)
   self.obj246.postAction( cobj0.LHS.CREATE )

   self.obj244.out_connections_.append(self.obj246)
   self.obj246.in_connections_.append(self.obj244)
   self.obj244.graphObject_.pendingConnections.append((self.obj244.graphObject_.tag, self.obj246.graphObject_.tag, [320.0, 383.0, 142.77571403165985, 105.53285434825837], 0, True))
   self.obj246.out_connections_.append(self.obj245)
   self.obj245.in_connections_.append(self.obj246)
   self.obj246.graphObject_.pendingConnections.append((self.obj246.graphObject_.tag, self.obj245.graphObject_.tag, [318.0, 18.0, 248.5, 202.5], 0, True))

   cobj0.RHS = ASG_LSMASOMM(self)

   self.obj244=OrgUnit(self)
   self.obj244.preAction( cobj0.RHS.CREATE )
   self.obj244.isGraphObjectVisual = True

   if(hasattr(self.obj244, '_setHierarchicalLink')):
     self.obj244._setHierarchicalLink(False)

   # Individual
   self.obj244.Individual.setNone()
   self.obj244.Individual.config = 0

   # hasActions
   self.obj244.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj244.hasActions.setValue(lcobj2)
   self.obj244.hasActions.setNone()

   # ID
   self.obj244.ID.setValue('')
   self.obj244.ID.setNone()

   # name
   self.obj244.name.setValue('')
   self.obj244.name.setNone()

   # UnitSize
   self.obj244.UnitSize.setValue('Individual')

   self.obj244.GGLabel.setValue(1)
   self.obj244.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(20.0,132.0,self.obj244)
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

   self.obj258=OrgUnit(self)
   self.obj258.preAction( cobj0.RHS.CREATE )
   self.obj258.isGraphObjectVisual = True

   if(hasattr(self.obj258, '_setHierarchicalLink')):
     self.obj258._setHierarchicalLink(False)

   # Individual
   self.obj258.Individual.setValue(('1', 0))
   self.obj258.Individual.config = 0

   # hasActions
   self.obj258.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj258.hasActions.setValue(lcobj2)

   # ID
   self.obj258.ID.setValue('OU|99')

   # name
   self.obj258.name.setValue('Party')

   # UnitSize
   self.obj258.UnitSize.setValue('Group')

   self.obj258.GGLabel.setValue(5)
   self.obj258.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(144.0,28.0,self.obj258)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj258.graphObject_ = new_obj
   self.obj2580= AttrCalc()
   self.obj2580.Copy=ATOM3Boolean()
   self.obj2580.Copy.setValue(('Copy from LHS', 0))
   self.obj2580.Copy.config = 0
   self.obj2580.Specify=ATOM3Constraint()
   self.obj2580.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj258.GGset2Any['Individual']= self.obj2580
   self.obj2581= AttrCalc()
   self.obj2581.Copy=ATOM3Boolean()
   self.obj2581.Copy.setValue(('Copy from LHS', 0))
   self.obj2581.Copy.config = 0
   self.obj2581.Specify=ATOM3Constraint()
   self.obj2581.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj258.GGset2Any['hasActions']= self.obj2581
   self.obj2582= AttrCalc()
   self.obj2582.Copy=ATOM3Boolean()
   self.obj2582.Copy.setValue(('Copy from LHS', 0))
   self.obj2582.Copy.config = 0
   self.obj2582.Specify=ATOM3Constraint()
   self.obj2582.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj258.GGset2Any['ID']= self.obj2582
   self.obj2583= AttrCalc()
   self.obj2583.Copy=ATOM3Boolean()
   self.obj2583.Copy.setValue(('Copy from LHS', 0))
   self.obj2583.Copy.config = 0
   self.obj2583.Specify=ATOM3Constraint()
   self.obj2583.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj258.GGset2Any['name']= self.obj2583
   self.obj2584= AttrCalc()
   self.obj2584.Copy=ATOM3Boolean()
   self.obj2584.Copy.setValue(('Copy from LHS', 0))
   self.obj2584.Copy.config = 0
   self.obj2584.Specify=ATOM3Constraint()
   self.obj2584.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj258.GGset2Any['UnitSize']= self.obj2584

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj258)
   self.obj258.postAction( cobj0.RHS.CREATE )

   self.obj245=Role(self)
   self.obj245.preAction( cobj0.RHS.CREATE )
   self.obj245.isGraphObjectVisual = True

   if(hasattr(self.obj245, '_setHierarchicalLink')):
     self.obj245._setHierarchicalLink(False)

   # isMetaRole
   self.obj245.isMetaRole.setNone()
   self.obj245.isMetaRole.config = 0

   # hasActions
   self.obj245.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj245.hasActions.setValue(lcobj2)
   self.obj245.hasActions.setNone()

   # ID
   self.obj245.ID.setValue('')
   self.obj245.ID.setNone()

   # name
   self.obj245.name.setValue('PartyFounder')

   self.obj245.GGLabel.setValue(2)
   self.obj245.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(226.0,132.0,self.obj245)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj245.graphObject_ = new_obj
   self.obj2450= AttrCalc()
   self.obj2450.Copy=ATOM3Boolean()
   self.obj2450.Copy.setValue(('Copy from LHS', 1))
   self.obj2450.Copy.config = 0
   self.obj2450.Specify=ATOM3Constraint()
   self.obj2450.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj245.GGset2Any['isMetaRole']= self.obj2450
   self.obj2451= AttrCalc()
   self.obj2451.Copy=ATOM3Boolean()
   self.obj2451.Copy.setValue(('Copy from LHS', 1))
   self.obj2451.Copy.config = 0
   self.obj2451.Specify=ATOM3Constraint()
   self.obj2451.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj245.GGset2Any['hasActions']= self.obj2451
   self.obj2452= AttrCalc()
   self.obj2452.Copy=ATOM3Boolean()
   self.obj2452.Copy.setValue(('Copy from LHS', 1))
   self.obj2452.Copy.config = 0
   self.obj2452.Specify=ATOM3Constraint()
   self.obj2452.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj245.GGset2Any['ID']= self.obj2452
   self.obj2453= AttrCalc()
   self.obj2453.Copy=ATOM3Boolean()
   self.obj2453.Copy.setValue(('Copy from LHS', 1))
   self.obj2453.Copy.config = 0
   self.obj2453.Specify=ATOM3Constraint()
   self.obj2453.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj245.GGset2Any['name']= self.obj2453

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj245)
   self.obj245.postAction( cobj0.RHS.CREATE )

   self.obj260=isPartOfOrgUnit(self)
   self.obj260.preAction( cobj0.RHS.CREATE )
   self.obj260.isGraphObjectVisual = True

   if(hasattr(self.obj260, '_setHierarchicalLink')):
     self.obj260._setHierarchicalLink(True)

   # ID
   self.obj260.ID.setValue('pOU|0')

   self.obj260.GGLabel.setValue(6)
   self.obj260.graphClass_= graph_isPartOfOrgUnit
   if self.genGraphics:
      new_obj = graph_isPartOfOrgUnit(104.815884279,137.370539238,self.obj260)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj260.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj260)
   self.obj260.postAction( cobj0.RHS.CREATE )

   self.obj246=canHaveRole(self)
   self.obj246.preAction( cobj0.RHS.CREATE )
   self.obj246.isGraphObjectVisual = True

   if(hasattr(self.obj246, '_setHierarchicalLink')):
     self.obj246._setHierarchicalLink(True)

   # ID
   self.obj246.ID.setValue('OUR|0')

   self.obj246.GGLabel.setValue(3)
   self.obj246.graphClass_= graph_canHaveRole
   if self.genGraphics:
      new_obj = graph_canHaveRole(189.95,150.35,self.obj246)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj246.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj246)
   self.obj246.postAction( cobj0.RHS.CREATE )

   self.obj244.out_connections_.append(self.obj246)
   self.obj246.in_connections_.append(self.obj244)
   self.obj244.graphObject_.pendingConnections.append((self.obj244.graphObject_.tag, self.obj246.graphObject_.tag, [172.0, 262.0, 189.5734237415075, 139.91783919598], 2, 0))
   self.obj244.out_connections_.append(self.obj260)
   self.obj260.in_connections_.append(self.obj244)
   self.obj244.graphObject_.pendingConnections.append((self.obj244.graphObject_.tag, self.obj260.graphObject_.tag, [172.0, 262.0, 104.8158842790995, 137.37053923795432], 0, True))
   self.obj260.out_connections_.append(self.obj258)
   self.obj258.in_connections_.append(self.obj260)
   self.obj260.graphObject_.pendingConnections.append((self.obj260.graphObject_.tag, self.obj258.graphObject_.tag, [138.0, 54.0, 146.5, 173.5], 0, True))
   self.obj246.out_connections_.append(self.obj245)
   self.obj245.in_connections_.append(self.obj246)
   self.obj246.graphObject_.pendingConnections.append((self.obj246.graphObject_.tag, self.obj245.graphObject_.tag, [271.0, 251.0, 211.39913777316735, 113.1006935442384], 2, 0))

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


