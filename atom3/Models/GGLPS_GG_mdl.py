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

   self.obj112=OrgUnit(self)
   self.obj112.preAction( cobj0.LHS.CREATE )
   self.obj112.isGraphObjectVisual = True

   if(hasattr(self.obj112, '_setHierarchicalLink')):
     self.obj112._setHierarchicalLink(False)

   # Individual
   self.obj112.Individual.setValue(('1', 0))
   self.obj112.Individual.config = 0

   # hasActions
   self.obj112.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj112.hasActions.setValue(lcobj2)
   self.obj112.hasActions.setNone()

   # ID
   self.obj112.ID.setValue('')
   self.obj112.ID.setNone()

   # name
   self.obj112.name.setValue('')
   self.obj112.name.setNone()

   # UnitSize
   self.obj112.UnitSize.setValue('Individual')

   self.obj112.GGLabel.setValue(1)
   self.obj112.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(60.0,120.0,self.obj112)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj112.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj112)
   self.obj112.postAction( cobj0.LHS.CREATE )


   cobj0.RHS = ASG_LSMASOMM(self)

   self.obj114=OrgUnit(self)
   self.obj114.preAction( cobj0.RHS.CREATE )
   self.obj114.isGraphObjectVisual = True

   if(hasattr(self.obj114, '_setHierarchicalLink')):
     self.obj114._setHierarchicalLink(False)

   # Individual
   self.obj114.Individual.setValue(('1', 0))
   self.obj114.Individual.config = 0

   # hasActions
   self.obj114.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj114.hasActions.setValue(lcobj2)

   # ID
   self.obj114.ID.setValue('OU|0')

   # name
   self.obj114.name.setValue('OUname')

   # UnitSize
   self.obj114.UnitSize.setValue('Individual')

   self.obj114.GGLabel.setValue(1)
   self.obj114.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(40.0,140.0,self.obj114)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj114.graphObject_ = new_obj
   self.obj1140= AttrCalc()
   self.obj1140.Copy=ATOM3Boolean()
   self.obj1140.Copy.setValue(('Copy from LHS', 1))
   self.obj1140.Copy.config = 0
   self.obj1140.Specify=ATOM3Constraint()
   self.obj1140.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj114.GGset2Any['UnitSize']= self.obj1140
   self.obj1141= AttrCalc()
   self.obj1141.Copy=ATOM3Boolean()
   self.obj1141.Copy.setValue(('Copy from LHS', 1))
   self.obj1141.Copy.config = 0
   self.obj1141.Specify=ATOM3Constraint()
   self.obj1141.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj114.GGset2Any['Individual']= self.obj1141
   self.obj1142= AttrCalc()
   self.obj1142.Copy=ATOM3Boolean()
   self.obj1142.Copy.setValue(('Copy from LHS', 1))
   self.obj1142.Copy.config = 0
   self.obj1142.Specify=ATOM3Constraint()
   self.obj1142.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj114.GGset2Any['hasActions']= self.obj1142
   self.obj1143= AttrCalc()
   self.obj1143.Copy=ATOM3Boolean()
   self.obj1143.Copy.setValue(('Copy from LHS', 1))
   self.obj1143.Copy.config = 0
   self.obj1143.Specify=ATOM3Constraint()
   self.obj1143.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj114.GGset2Any['name']= self.obj1143
   self.obj1144= AttrCalc()
   self.obj1144.Copy=ATOM3Boolean()
   self.obj1144.Copy.setValue(('Copy from LHS', 1))
   self.obj1144.Copy.config = 0
   self.obj1144.Specify=ATOM3Constraint()
   self.obj1144.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj114.GGset2Any['ID']= self.obj1144

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj114)
   self.obj114.postAction( cobj0.RHS.CREATE )

   self.obj115=Role(self)
   self.obj115.preAction( cobj0.RHS.CREATE )
   self.obj115.isGraphObjectVisual = True

   if(hasattr(self.obj115, '_setHierarchicalLink')):
     self.obj115._setHierarchicalLink(False)

   # isMetaRole
   self.obj115.isMetaRole.setValue((None, 0))
   self.obj115.isMetaRole.config = 0

   # hasActions
   self.obj115.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj115.hasActions.setValue(lcobj2)

   # ID
   self.obj115.ID.setValue('R|90')

   # name
   self.obj115.name.setValue('PartyFounder')

   self.obj115.GGLabel.setValue(2)
   self.obj115.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(250.0,50.0,self.obj115)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj115.graphObject_ = new_obj
   self.obj1150= AttrCalc()
   self.obj1150.Copy=ATOM3Boolean()
   self.obj1150.Copy.setValue(('Copy from LHS', 0))
   self.obj1150.Copy.config = 0
   self.obj1150.Specify=ATOM3Constraint()
   self.obj1150.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj115.GGset2Any['isMetaRole']= self.obj1150
   self.obj1151= AttrCalc()
   self.obj1151.Copy=ATOM3Boolean()
   self.obj1151.Copy.setValue(('Copy from LHS', 0))
   self.obj1151.Copy.config = 0
   self.obj1151.Specify=ATOM3Constraint()
   self.obj1151.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj115.GGset2Any['hasActions']= self.obj1151
   self.obj1152= AttrCalc()
   self.obj1152.Copy=ATOM3Boolean()
   self.obj1152.Copy.setValue(('Copy from LHS', 0))
   self.obj1152.Copy.config = 0
   self.obj1152.Specify=ATOM3Constraint()
   self.obj1152.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj115.GGset2Any['ID']= self.obj1152
   self.obj1153= AttrCalc()
   self.obj1153.Copy=ATOM3Boolean()
   self.obj1153.Copy.setValue(('Copy from LHS', 0))
   self.obj1153.Copy.config = 0
   self.obj1153.Specify=ATOM3Constraint()
   self.obj1153.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj115.GGset2Any['name']= self.obj1153

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj115)
   self.obj115.postAction( cobj0.RHS.CREATE )

   self.obj116=Role(self)
   self.obj116.preAction( cobj0.RHS.CREATE )
   self.obj116.isGraphObjectVisual = True

   if(hasattr(self.obj116, '_setHierarchicalLink')):
     self.obj116._setHierarchicalLink(False)

   # isMetaRole
   self.obj116.isMetaRole.setValue((None, 0))
   self.obj116.isMetaRole.config = 0

   # hasActions
   self.obj116.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj116.hasActions.setValue(lcobj2)

   # ID
   self.obj116.ID.setValue('R|91')

   # name
   self.obj116.name.setValue('PartyMember')

   self.obj116.GGLabel.setValue(3)
   self.obj116.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(270.0,170.0,self.obj116)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj116.graphObject_ = new_obj
   self.obj1160= AttrCalc()
   self.obj1160.Copy=ATOM3Boolean()
   self.obj1160.Copy.setValue(('Copy from LHS', 0))
   self.obj1160.Copy.config = 0
   self.obj1160.Specify=ATOM3Constraint()
   self.obj1160.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj116.GGset2Any['isMetaRole']= self.obj1160
   self.obj1161= AttrCalc()
   self.obj1161.Copy=ATOM3Boolean()
   self.obj1161.Copy.setValue(('Copy from LHS', 0))
   self.obj1161.Copy.config = 0
   self.obj1161.Specify=ATOM3Constraint()
   self.obj1161.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj116.GGset2Any['hasActions']= self.obj1161
   self.obj1162= AttrCalc()
   self.obj1162.Copy=ATOM3Boolean()
   self.obj1162.Copy.setValue(('Copy from LHS', 0))
   self.obj1162.Copy.config = 0
   self.obj1162.Specify=ATOM3Constraint()
   self.obj1162.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj116.GGset2Any['ID']= self.obj1162
   self.obj1163= AttrCalc()
   self.obj1163.Copy=ATOM3Boolean()
   self.obj1163.Copy.setValue(('Copy from LHS', 0))
   self.obj1163.Copy.config = 0
   self.obj1163.Specify=ATOM3Constraint()
   self.obj1163.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj116.GGset2Any['name']= self.obj1163

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj116)
   self.obj116.postAction( cobj0.RHS.CREATE )

   self.obj117=canHaveRole(self)
   self.obj117.preAction( cobj0.RHS.CREATE )
   self.obj117.isGraphObjectVisual = True

   if(hasattr(self.obj117, '_setHierarchicalLink')):
     self.obj117._setHierarchicalLink(True)

   # ID
   self.obj117.ID.setValue('OUR|90')

   self.obj117.GGLabel.setValue(4)
   self.obj117.graphClass_= graph_canHaveRole
   if self.genGraphics:
      new_obj = graph_canHaveRole(178.5,145.5,self.obj117)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj117.graphObject_ = new_obj
   self.obj1170= AttrCalc()
   self.obj1170.Copy=ATOM3Boolean()
   self.obj1170.Copy.setValue(('Copy from LHS', 0))
   self.obj1170.Copy.config = 0
   self.obj1170.Specify=ATOM3Constraint()
   self.obj1170.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj117.GGset2Any['ID']= self.obj1170

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj117)
   self.obj117.postAction( cobj0.RHS.CREATE )

   self.obj114.out_connections_.append(self.obj117)
   self.obj117.in_connections_.append(self.obj114)
   self.obj114.graphObject_.pendingConnections.append((self.obj114.graphObject_.tag, self.obj117.graphObject_.tag, [71.0, 203.0, 178.5, 145.5], 0, True))
   self.obj117.out_connections_.append(self.obj115)
   self.obj115.in_connections_.append(self.obj117)
   self.obj117.graphObject_.pendingConnections.append((self.obj117.graphObject_.tag, self.obj115.graphObject_.tag, [286.0, 102.0, 178.5, 152.5], 0, True))
   self.obj117.out_connections_.append(self.obj116)
   self.obj116.in_connections_.append(self.obj117)
   self.obj117.graphObject_.pendingConnections.append((self.obj117.graphObject_.tag, self.obj116.graphObject_.tag, [306.0, 222.0, 178.5, 152.5], 0, True))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the ACTION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName13 is not guaranteed to be unique (so change it, be safe!)\n\n#from CustomCode import NodeOutputsInputs\n\nnode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n\nfor eOut in node.out_connections_:\n    if eOut.getClass() == \'canHaveRole\':\n        roles = eOut.out_connections_\n        for r in roles:\n            if r.name.getValue() == \'PartyFounder\':\n                return 0\nprint(eOut)\nreturn 1\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   cobj0= GGruleEdit(None, self)
   cobj0.Name=ATOM3String('CreateParty', 20)
   cobj0.Order=ATOM3Integer(1)
   cobj0.TimeDelay=ATOM3Integer(2)
   cobj0.SubtypesMatching=ATOM3Boolean()
   cobj0.SubtypesMatching.setValue((None, 1))
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

   self.obj122=OrgUnit(self)
   self.obj122.preAction( cobj0.LHS.CREATE )
   self.obj122.isGraphObjectVisual = True

   if(hasattr(self.obj122, '_setHierarchicalLink')):
     self.obj122._setHierarchicalLink(False)

   # Individual
   self.obj122.Individual.setNone()
   self.obj122.Individual.config = 0

   # hasActions
   self.obj122.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj122.hasActions.setValue(lcobj2)
   self.obj122.hasActions.setNone()

   # ID
   self.obj122.ID.setValue('')
   self.obj122.ID.setNone()

   # name
   self.obj122.name.setValue('')
   self.obj122.name.setNone()

   # UnitSize
   self.obj122.UnitSize.setValue('Individual')

   self.obj122.GGLabel.setValue(1)
   self.obj122.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(68.0,41.0,self.obj122)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj122.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj122)
   self.obj122.postAction( cobj0.LHS.CREATE )

   self.obj123=Role(self)
   self.obj123.preAction( cobj0.LHS.CREATE )
   self.obj123.isGraphObjectVisual = True

   if(hasattr(self.obj123, '_setHierarchicalLink')):
     self.obj123._setHierarchicalLink(False)

   # isMetaRole
   self.obj123.isMetaRole.setNone()
   self.obj123.isMetaRole.config = 0

   # hasActions
   self.obj123.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj123.hasActions.setValue(lcobj2)
   self.obj123.hasActions.setNone()

   # ID
   self.obj123.ID.setValue('')
   self.obj123.ID.setNone()

   # name
   self.obj123.name.setValue('PartyFounder')

   self.obj123.GGLabel.setValue(2)
   self.obj123.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(161.0,41.0,self.obj123)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj123.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj123)
   self.obj123.postAction( cobj0.LHS.CREATE )

   self.obj124=canHaveRole(self)
   self.obj124.preAction( cobj0.LHS.CREATE )
   self.obj124.isGraphObjectVisual = True

   if(hasattr(self.obj124, '_setHierarchicalLink')):
     self.obj124._setHierarchicalLink(True)

   # ID
   self.obj124.ID.setValue('OUR|0')

   self.obj124.GGLabel.setValue(3)
   self.obj124.graphClass_= graph_canHaveRole
   if self.genGraphics:
      new_obj = graph_canHaveRole(150.775714032,90.5328543483,self.obj124)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj124.graphObject_ = new_obj

   # Add node to the root: cobj0.LHS
   cobj0.LHS.addNode(self.obj124)
   self.obj124.postAction( cobj0.LHS.CREATE )

   self.obj122.out_connections_.append(self.obj124)
   self.obj124.in_connections_.append(self.obj122)
   self.obj122.graphObject_.pendingConnections.append((self.obj122.graphObject_.tag, self.obj124.graphObject_.tag, [388.0, 424.0, 150.77571403127953, 90.5328543484751], 0, True))
   self.obj124.out_connections_.append(self.obj123)
   self.obj123.in_connections_.append(self.obj124)
   self.obj124.graphObject_.pendingConnections.append((self.obj124.graphObject_.tag, self.obj123.graphObject_.tag, [386.0, 59.0, 248.5, 202.5], 0, True))

   cobj0.RHS = ASG_LSMASOMM(self)

   self.obj126=OrgUnit(self)
   self.obj126.preAction( cobj0.RHS.CREATE )
   self.obj126.isGraphObjectVisual = True

   if(hasattr(self.obj126, '_setHierarchicalLink')):
     self.obj126._setHierarchicalLink(False)

   # Individual
   self.obj126.Individual.setNone()
   self.obj126.Individual.config = 0

   # hasActions
   self.obj126.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj126.hasActions.setValue(lcobj2)
   self.obj126.hasActions.setNone()

   # ID
   self.obj126.ID.setValue('')
   self.obj126.ID.setNone()

   # name
   self.obj126.name.setValue('')
   self.obj126.name.setNone()

   # UnitSize
   self.obj126.UnitSize.setValue('Individual')

   self.obj126.GGLabel.setValue(1)
   self.obj126.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(0,104,self.obj126)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj126.graphObject_ = new_obj
   self.obj1260= AttrCalc()
   self.obj1260.Copy=ATOM3Boolean()
   self.obj1260.Copy.setValue(('Copy from LHS', 1))
   self.obj1260.Copy.config = 0
   self.obj1260.Specify=ATOM3Constraint()
   self.obj1260.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj126.GGset2Any['Individual']= self.obj1260
   self.obj1261= AttrCalc()
   self.obj1261.Copy=ATOM3Boolean()
   self.obj1261.Copy.setValue(('Copy from LHS', 1))
   self.obj1261.Copy.config = 0
   self.obj1261.Specify=ATOM3Constraint()
   self.obj1261.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj126.GGset2Any['hasActions']= self.obj1261
   self.obj1262= AttrCalc()
   self.obj1262.Copy=ATOM3Boolean()
   self.obj1262.Copy.setValue(('Copy from LHS', 1))
   self.obj1262.Copy.config = 0
   self.obj1262.Specify=ATOM3Constraint()
   self.obj1262.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj126.GGset2Any['ID']= self.obj1262
   self.obj1263= AttrCalc()
   self.obj1263.Copy=ATOM3Boolean()
   self.obj1263.Copy.setValue(('Copy from LHS', 1))
   self.obj1263.Copy.config = 0
   self.obj1263.Specify=ATOM3Constraint()
   self.obj1263.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj126.GGset2Any['name']= self.obj1263
   self.obj1264= AttrCalc()
   self.obj1264.Copy=ATOM3Boolean()
   self.obj1264.Copy.setValue(('Copy from LHS', 1))
   self.obj1264.Copy.config = 0
   self.obj1264.Specify=ATOM3Constraint()
   self.obj1264.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj126.GGset2Any['UnitSize']= self.obj1264

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj126)
   self.obj126.postAction( cobj0.RHS.CREATE )

   self.obj127=OrgUnit(self)
   self.obj127.preAction( cobj0.RHS.CREATE )
   self.obj127.isGraphObjectVisual = True

   if(hasattr(self.obj127, '_setHierarchicalLink')):
     self.obj127._setHierarchicalLink(False)

   # Individual
   self.obj127.Individual.setValue(('1', 0))
   self.obj127.Individual.config = 0

   # hasActions
   self.obj127.hasActions.setActionFlags([ 1, 1, 1, 0])
   lcobj2 =[]
   cobj2=ATOM3String('ChangeRole', 20)
   lcobj2.append(cobj2)
   self.obj127.hasActions.setValue(lcobj2)

   # ID
   self.obj127.ID.setValue('OU|99')

   # name
   self.obj127.name.setValue('Party')

   # UnitSize
   self.obj127.UnitSize.setValue('Group')

   self.obj127.GGLabel.setValue(5)
   self.obj127.graphClass_= graph_OrgUnit
   if self.genGraphics:
      new_obj = graph_OrgUnit(248,104,self.obj127)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj127.graphObject_ = new_obj
   self.obj1270= AttrCalc()
   self.obj1270.Copy=ATOM3Boolean()
   self.obj1270.Copy.setValue(('Copy from LHS', 0))
   self.obj1270.Copy.config = 0
   self.obj1270.Specify=ATOM3Constraint()
   self.obj1270.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj127.GGset2Any['Individual']= self.obj1270
   self.obj1271= AttrCalc()
   self.obj1271.Copy=ATOM3Boolean()
   self.obj1271.Copy.setValue(('Copy from LHS', 0))
   self.obj1271.Copy.config = 0
   self.obj1271.Specify=ATOM3Constraint()
   self.obj1271.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj127.GGset2Any['hasActions']= self.obj1271
   self.obj1272= AttrCalc()
   self.obj1272.Copy=ATOM3Boolean()
   self.obj1272.Copy.setValue(('Copy from LHS', 0))
   self.obj1272.Copy.config = 0
   self.obj1272.Specify=ATOM3Constraint()
   self.obj1272.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj127.GGset2Any['ID']= self.obj1272
   self.obj1273= AttrCalc()
   self.obj1273.Copy=ATOM3Boolean()
   self.obj1273.Copy.setValue(('Copy from LHS', 0))
   self.obj1273.Copy.config = 0
   self.obj1273.Specify=ATOM3Constraint()
   self.obj1273.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj127.GGset2Any['name']= self.obj1273
   self.obj1274= AttrCalc()
   self.obj1274.Copy=ATOM3Boolean()
   self.obj1274.Copy.setValue(('Copy from LHS', 0))
   self.obj1274.Copy.config = 0
   self.obj1274.Specify=ATOM3Constraint()
   self.obj1274.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj127.GGset2Any['UnitSize']= self.obj1274

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj127)
   self.obj127.postAction( cobj0.RHS.CREATE )

   self.obj128=Role(self)
   self.obj128.preAction( cobj0.RHS.CREATE )
   self.obj128.isGraphObjectVisual = True

   if(hasattr(self.obj128, '_setHierarchicalLink')):
     self.obj128._setHierarchicalLink(False)

   # isMetaRole
   self.obj128.isMetaRole.setNone()
   self.obj128.isMetaRole.config = 0

   # hasActions
   self.obj128.hasActions.setActionFlags([ 0, 0, 1, 0])
   lcobj2 =[]
   self.obj128.hasActions.setValue(lcobj2)
   self.obj128.hasActions.setNone()

   # ID
   self.obj128.ID.setValue('')
   self.obj128.ID.setNone()

   # name
   self.obj128.name.setValue('PartyFounder')

   self.obj128.GGLabel.setValue(2)
   self.obj128.graphClass_= graph_Role
   if self.genGraphics:
      new_obj = graph_Role(124,0,self.obj128)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj128.graphObject_ = new_obj
   self.obj1280= AttrCalc()
   self.obj1280.Copy=ATOM3Boolean()
   self.obj1280.Copy.setValue(('Copy from LHS', 1))
   self.obj1280.Copy.config = 0
   self.obj1280.Specify=ATOM3Constraint()
   self.obj1280.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj128.GGset2Any['isMetaRole']= self.obj1280
   self.obj1281= AttrCalc()
   self.obj1281.Copy=ATOM3Boolean()
   self.obj1281.Copy.setValue(('Copy from LHS', 1))
   self.obj1281.Copy.config = 0
   self.obj1281.Specify=ATOM3Constraint()
   self.obj1281.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj128.GGset2Any['hasActions']= self.obj1281
   self.obj1282= AttrCalc()
   self.obj1282.Copy=ATOM3Boolean()
   self.obj1282.Copy.setValue(('Copy from LHS', 1))
   self.obj1282.Copy.config = 0
   self.obj1282.Specify=ATOM3Constraint()
   self.obj1282.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj128.GGset2Any['ID']= self.obj1282
   self.obj1283= AttrCalc()
   self.obj1283.Copy=ATOM3Boolean()
   self.obj1283.Copy.setValue(('Copy from LHS', 1))
   self.obj1283.Copy.config = 0
   self.obj1283.Specify=ATOM3Constraint()
   self.obj1283.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.obj128.GGset2Any['name']= self.obj1283

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj128)
   self.obj128.postAction( cobj0.RHS.CREATE )

   self.obj129=isPartOfOrgUnit(self)
   self.obj129.preAction( cobj0.RHS.CREATE )
   self.obj129.isGraphObjectVisual = True

   if(hasattr(self.obj129, '_setHierarchicalLink')):
     self.obj129._setHierarchicalLink(True)

   # ID
   self.obj129.ID.setValue('pOU|0')

   self.obj129.GGLabel.setValue(6)
   self.obj129.graphClass_= graph_isPartOfOrgUnit
   if self.genGraphics:
      new_obj = graph_isPartOfOrgUnit(170.95,135.5,self.obj129)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj129.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj129)
   self.obj129.postAction( cobj0.RHS.CREATE )

   self.obj130=canHaveRole(self)
   self.obj130.preAction( cobj0.RHS.CREATE )
   self.obj130.isGraphObjectVisual = True

   if(hasattr(self.obj130, '_setHierarchicalLink')):
     self.obj130._setHierarchicalLink(True)

   # ID
   self.obj130.ID.setValue('OUR|0')

   self.obj130.GGLabel.setValue(3)
   self.obj130.graphClass_= graph_canHaveRole
   if self.genGraphics:
      new_obj = graph_canHaveRole(96.0835477534,103.612551906,self.obj130)
      new_obj.layConstraints = dict() # Graphical Layout Constraints 
      new_obj.layConstraints['scale'] = [1.0, 1.0]
   else: new_obj = None
   self.obj130.graphObject_ = new_obj

   # Add node to the root: cobj0.RHS
   cobj0.RHS.addNode(self.obj130)
   self.obj130.postAction( cobj0.RHS.CREATE )

   self.obj126.out_connections_.append(self.obj130)
   self.obj130.in_connections_.append(self.obj126)
   self.obj126.graphObject_.pendingConnections.append((self.obj126.graphObject_.tag, self.obj130.graphObject_.tag, [172.0, 262.0, 95.70697149497339, 93.18039110179075], 2, 0))
   self.obj126.out_connections_.append(self.obj129)
   self.obj129.in_connections_.append(self.obj126)
   self.obj126.graphObject_.pendingConnections.append((self.obj126.graphObject_.tag, self.obj129.graphObject_.tag, [172.0, 262.0, 170.9500000000995, 135.49999999995433], 0, True))
   self.obj129.out_connections_.append(self.obj127)
   self.obj127.in_connections_.append(self.obj129)
   self.obj129.graphObject_.pendingConnections.append((self.obj129.graphObject_.tag, self.obj127.graphObject_.tag, [138.0, 54.0, 146.5, 173.5], 0, True))
   self.obj130.out_connections_.append(self.obj128)
   self.obj128.in_connections_.append(self.obj130)
   self.obj130.graphObject_.pendingConnections.append((self.obj130.graphObject_.tag, self.obj128.graphObject_.tag, [271.0, 251.0, 211.39913777316735, 113.1006935442384], 2, 0))

   cobj0.Condition=ATOM3Constraint()
   cobj0.Condition.setValue(('condition', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# If you want to apply this rule at most once on asingle host graph node, \n# then uncomment the next two lines. Change the default GG label (1) if needed.\n\n# Make sure to enable the ACTION code as well\n# And to use the same label & unique name in the ACTION\n# WARNING: _uniqueName25 is not guaranteed to be unique (so change it, be safe!)\n\nnode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))\n\nfor eOut in node.out_connections_:\n    if eOut.getClass() == \'canHaveRole\':\n        roles = eOut.out_connections_\n        print(roles)\n        for r in roles:\n            if r.name.getValue() == \'PartyFounder\':\n                return 1\nreturn 0\n\n'))
   cobj0.Action=ATOM3Constraint()
   cobj0.Action.setValue(('action', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   lcobj0.append(cobj0)
   self.EditingGraphGrammar.Rules.setValue(lcobj0)
   self.EditingGraphGrammar.InitialAction=ATOM3Constraint()
   self.EditingGraphGrammar.InitialAction.setValue(('constraint', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
   self.EditingGraphGrammar.FinalAction=ATOM3Constraint()
   self.EditingGraphGrammar.FinalAction.setValue(('const', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))


