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
   self.obj51.GGset2Any['Individual']= self.obj510
   self.obj511= AttrCalc()
   self.obj511.Copy=ATOM3Boolean()
   self.obj511.Copy.setValue(('Copy from LHS', 1))
   self.obj511.Copy.config = 0
   self.obj511.Specify=ATOM3Constraint()
   self.obj511.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj51.GGset2Any['hasActions']= self.obj511
   self.obj512= AttrCalc()
   self.obj512.Copy=ATOM3Boolean()
   self.obj512.Copy.setValue(('Copy from LHS', 1))
   self.obj512.Copy.config = 0
   self.obj512.Specify=ATOM3Constraint()
   self.obj512.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj51.GGset2Any['ID']= self.obj512
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
   self.obj51.GGset2Any['UnitSize']= self.obj514

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

   self.obj59=OrgUnit(self)
   self.obj59.preAction( cobj0.LHS.CREATE )
   self.obj59.isGraphObjectVisual = True

   if(hasattr(self.obj59, '_setHierarchicalLink')):
     self.obj59._setHierarchicalLink(False)

   # Individual
   self.obj59.Individual.setNone()
   self.obj59.Individual.config = 0

   # hasActions
   self.obj59.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj59.hasActions.setValue(lcobj2)
   self.obj59.hasActions.setNone()

   # ID
   self.obj59.ID.setValue('')
   self.obj59.ID.setNone()

   # name
   self.obj59.name.setValue('')
   self.obj59.name.setNone()

   # UnitSize
   self.obj59.UnitSize.setValue('Individual')

   self.obj59.GGLabel.setValue(1)
   self.obj59.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(0,0,self.obj59)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj59.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj59)
   self.obj59.postAction( cobj0.LHS.CREATE )

   self.obj60=Role(self)
   self.obj60.preAction( cobj0.LHS.CREATE )
   self.obj60.isGraphObjectVisual = True

   if(hasattr(self.obj60, '_setHierarchicalLink')):
     self.obj60._setHierarchicalLink(False)

   # isMetaRole
   self.obj60.isMetaRole.setNone()
   self.obj60.isMetaRole.config = 0

   # hasActions
   self.obj60.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj60.hasActions.setValue(lcobj2)
   self.obj60.hasActions.setNone()

   # ID
   self.obj60.ID.setValue('')
   self.obj60.ID.setNone()

   # name
   self.obj60.name.setValue('PartyFounder')

   self.obj60.GGLabel.setValue(2)
   self.obj60.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(93,0,self.obj60)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj60.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj60)
   self.obj60.postAction( cobj0.LHS.CREATE )

   self.obj61=canHaveRole(self)
   self.obj61.preAction( cobj0.LHS.CREATE )
   self.obj61.isGraphObjectVisual = True

   if(hasattr(self.obj61, '_setHierarchicalLink')):
     self.obj61._setHierarchicalLink(True)

   # ID
   self.obj61.ID.setValue('OUR|0')

   self.obj61.GGLabel.setValue(3)
   self.obj61.graphClass_= graph_canHaveRole
   if self.genGraphics:
      new_obj = graph_canHaveRole(82.7757140317,49.5328543483,self.obj61)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj61.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj61)
   self.obj61.postAction( cobj0.LHS.CREATE )

   self.obj59.out_connections_.append(self.obj61)
   self.obj61.in_connections_.append(self.obj59)
   self.obj59.graphObject_.pendingConnections.append((self.obj59.graphObject_.tag, self.obj61.graphObject_.tag, [320.0, 383.0, 82.77571403127953, 49.532854348475105], 0, True))
   self.obj61.out_connections_.append(self.obj60)
   self.obj60.in_connections_.append(self.obj61)
   self.obj61.graphObject_.pendingConnections.append((self.obj61.graphObject_.tag, self.obj60.graphObject_.tag, [318.0, 18.0, 248.5, 202.5], 0, True))

   cobj0.RHS = ASG_LSMASOMM(self)

   self.obj63=OrgUnit(self)
   self.obj63.preAction( cobj0.RHS.CREATE )
   self.obj63.isGraphObjectVisual = True

   if(hasattr(self.obj63, '_setHierarchicalLink')):
     self.obj63._setHierarchicalLink(False)

   # Individual
   self.obj63.Individual.setNone()
   self.obj63.Individual.config = 0

   # hasActions
   self.obj63.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj63.hasActions.setValue(lcobj2)
   self.obj63.hasActions.setNone()

   # ID
   self.obj63.ID.setValue('')
   self.obj63.ID.setNone()

   # name
   self.obj63.name.setValue('')
   self.obj63.name.setNone()

   # UnitSize
   self.obj63.UnitSize.setValue('Individual')

   self.obj63.GGLabel.setValue(1)
   self.obj63.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(0,104,self.obj63)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj63.graphObject_ = new_obj
   self.obj630= AttrCalc()
   self.obj630.Copy=ATOM3Boolean()
   self.obj630.Copy.setValue(('Copy from LHS', 1))
   self.obj630.Copy.config = 0
   self.obj630.Specify=ATOM3Constraint()
   self.obj630.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj63.GGset2Any['ID']= self.obj630
   self.obj631= AttrCalc()
   self.obj631.Copy=ATOM3Boolean()
   self.obj631.Copy.setValue(('Copy from LHS', 1))
   self.obj631.Copy.config = 0
   self.obj631.Specify=ATOM3Constraint()
   self.obj631.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj63.GGset2Any['Individual']= self.obj631
   self.obj632= AttrCalc()
   self.obj632.Copy=ATOM3Boolean()
   self.obj632.Copy.setValue(('Copy from LHS', 1))
   self.obj632.Copy.config = 0
   self.obj632.Specify=ATOM3Constraint()
   self.obj632.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj63.GGset2Any['hasActions']= self.obj632
   self.obj633= AttrCalc()
   self.obj633.Copy=ATOM3Boolean()
   self.obj633.Copy.setValue(('Copy from LHS', 1))
   self.obj633.Copy.config = 0
   self.obj633.Specify=ATOM3Constraint()
   self.obj633.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj63.GGset2Any['UnitSize']= self.obj633
   self.obj634= AttrCalc()
   self.obj634.Copy=ATOM3Boolean()
   self.obj634.Copy.setValue(('Copy from LHS', 1))
   self.obj634.Copy.config = 0
   self.obj634.Specify=ATOM3Constraint()
   self.obj634.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj63.GGset2Any['name']= self.obj634

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj63)
   self.obj63.postAction( cobj0.RHS.CREATE )

   self.obj64=OrgUnit(self)
   self.obj64.preAction( cobj0.RHS.CREATE )
   self.obj64.isGraphObjectVisual = True

   if(hasattr(self.obj64, '_setHierarchicalLink')):
     self.obj64._setHierarchicalLink(False)

   # Individual
   self.obj64.Individual.setValue(('1', 0))
   self.obj64.Individual.config = 0

   # hasActions
   self.obj64.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj64.hasActions.setValue(lcobj2)

   # ID
   self.obj64.ID.setValue('OU|99')

   # name
   self.obj64.name.setValue('Party')

   # UnitSize
   self.obj64.UnitSize.setValue('Group')

   self.obj64.GGLabel.setValue(5)
   self.obj64.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(124,0,self.obj64)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj64.graphObject_ = new_obj
   self.obj640= AttrCalc()
   self.obj640.Copy=ATOM3Boolean()
   self.obj640.Copy.setValue(('Copy from LHS', 0))
   self.obj640.Copy.config = 0
   self.obj640.Specify=ATOM3Constraint()
   self.obj640.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj64.GGset2Any['ID']= self.obj640
   self.obj641= AttrCalc()
   self.obj641.Copy=ATOM3Boolean()
   self.obj641.Copy.setValue(('Copy from LHS', 0))
   self.obj641.Copy.config = 0
   self.obj641.Specify=ATOM3Constraint()
   self.obj641.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj64.GGset2Any['Individual']= self.obj641
   self.obj642= AttrCalc()
   self.obj642.Copy=ATOM3Boolean()
   self.obj642.Copy.setValue(('Copy from LHS', 0))
   self.obj642.Copy.config = 0
   self.obj642.Specify=ATOM3Constraint()
   self.obj642.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj64.GGset2Any['hasActions']= self.obj642
   self.obj643= AttrCalc()
   self.obj643.Copy=ATOM3Boolean()
   self.obj643.Copy.setValue(('Copy from LHS', 0))
   self.obj643.Copy.config = 0
   self.obj643.Specify=ATOM3Constraint()
   self.obj643.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj64.GGset2Any['UnitSize']= self.obj643
   self.obj644= AttrCalc()
   self.obj644.Copy=ATOM3Boolean()
   self.obj644.Copy.setValue(('Copy from LHS', 0))
   self.obj644.Copy.config = 0
   self.obj644.Specify=ATOM3Constraint()
   self.obj644.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj64.GGset2Any['name']= self.obj644

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj64)
   self.obj64.postAction( cobj0.RHS.CREATE )

   self.obj65=Role(self)
   self.obj65.preAction( cobj0.RHS.CREATE )
   self.obj65.isGraphObjectVisual = True

   if(hasattr(self.obj65, '_setHierarchicalLink')):
     self.obj65._setHierarchicalLink(False)

   # isMetaRole
   self.obj65.isMetaRole.setNone()
   self.obj65.isMetaRole.config = 0

   # hasActions
   self.obj65.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj65.hasActions.setValue(lcobj2)
   self.obj65.hasActions.setNone()

   # ID
   self.obj65.ID.setValue('')
   self.obj65.ID.setNone()

   # name
   self.obj65.name.setValue('PartyFounder')

   self.obj65.GGLabel.setValue(2)
   self.obj65.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(206,104,self.obj65)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj65.graphObject_ = new_obj
   self.obj650= AttrCalc()
   self.obj650.Copy=ATOM3Boolean()
   self.obj650.Copy.setValue(('Copy from LHS', 1))
   self.obj650.Copy.config = 0
   self.obj650.Specify=ATOM3Constraint()
   self.obj650.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj65.GGset2Any['isMetaRole']= self.obj650
   self.obj651= AttrCalc()
   self.obj651.Copy=ATOM3Boolean()
   self.obj651.Copy.setValue(('Copy from LHS', 1))
   self.obj651.Copy.config = 0
   self.obj651.Specify=ATOM3Constraint()
   self.obj651.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj65.GGset2Any['hasActions']= self.obj651
   self.obj652= AttrCalc()
   self.obj652.Copy=ATOM3Boolean()
   self.obj652.Copy.setValue(('Copy from LHS', 1))
   self.obj652.Copy.config = 0
   self.obj652.Specify=ATOM3Constraint()
   self.obj652.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj65.GGset2Any['ID']= self.obj652
   self.obj653= AttrCalc()
   self.obj653.Copy=ATOM3Boolean()
   self.obj653.Copy.setValue(('Copy from LHS', 1))
   self.obj653.Copy.config = 0
   self.obj653.Specify=ATOM3Constraint()
   self.obj653.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj65.GGset2Any['name']= self.obj653

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj65)
   self.obj65.postAction( cobj0.RHS.CREATE )

   self.obj66=isPartOfOrgUnit(self)
   self.obj66.preAction( cobj0.RHS.CREATE )
   self.obj66.isGraphObjectVisual = True

   if(hasattr(self.obj66, '_setHierarchicalLink')):
     self.obj66._setHierarchicalLink(True)

   # ID
   self.obj66.ID.setValue('pOU|0')

   self.obj66.GGLabel.setValue(6)
   self.obj66.graphClass_= graph_isPartOfOrgUnit
   if self.genGraphics:
      new_obj = graph_isPartOfOrgUnit(84.8158842791,109.370539238,self.obj66)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj66.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj66)
   self.obj66.postAction( cobj0.RHS.CREATE )

   self.obj67=canHaveRole(self)
   self.obj67.preAction( cobj0.RHS.CREATE )
   self.obj67.isGraphObjectVisual = True

   if(hasattr(self.obj67, '_setHierarchicalLink')):
     self.obj67._setHierarchicalLink(True)

   # ID
   self.obj67.ID.setValue('OUR|0')

   self.obj67.GGLabel.setValue(3)
   self.obj67.graphClass_= graph_canHaveRole
   if self.genGraphics:
      new_obj = graph_canHaveRole(148.95,152.35,self.obj67)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj67.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj67)
   self.obj67.postAction( cobj0.RHS.CREATE )

   self.obj63.out_connections_.append(self.obj67)
   self.obj67.in_connections_.append(self.obj63)
   self.obj63.graphObject_.pendingConnections.append((self.obj63.graphObject_.tag, self.obj67.graphObject_.tag, [172.0, 262.0, 148.57342374154044, 141.9178391958854], 2, 0))
   self.obj63.out_connections_.append(self.obj66)
   self.obj66.in_connections_.append(self.obj63)
   self.obj63.graphObject_.pendingConnections.append((self.obj63.graphObject_.tag, self.obj66.graphObject_.tag, [172.0, 262.0, 84.81588427919901, 109.37053923790864], 0, True))
   self.obj66.out_connections_.append(self.obj64)
   self.obj64.in_connections_.append(self.obj66)
   self.obj66.graphObject_.pendingConnections.append((self.obj66.graphObject_.tag, self.obj64.graphObject_.tag, [138.0, 54.0, 146.5, 173.5], 0, True))
   self.obj67.out_connections_.append(self.obj65)
   self.obj65.in_connections_.append(self.obj67)
   self.obj67.graphObject_.pendingConnections.append((self.obj67.graphObject_.tag, self.obj65.graphObject_.tag, [271.0, 251.0, 211.39913777316735, 113.1006935442384], 2, 0))

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


