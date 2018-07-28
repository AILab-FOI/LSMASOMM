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
      self.exactMatch = 0
      self.LHS = ASG_LSMASOMM(parent)

      self.obj122=OrgUnit(parent)
      self.obj122.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_OrgUnit(68.0,41.0,self.obj122)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj122.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj122)
      self.obj122.postAction( self.LHS.CREATE )

      self.obj123=Role(parent)
      self.obj123.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_Role(161.0,41.0,self.obj123)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj123.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj123)
      self.obj123.postAction( self.LHS.CREATE )

      self.obj124=canHaveRole(parent)
      self.obj124.preAction( self.LHS.CREATE )
      self.obj124.isGraphObjectVisual = True

      if(hasattr(self.obj124, '_setHierarchicalLink')):
        self.obj124._setHierarchicalLink(True)

      # ID
      self.obj124.ID.setValue('OUR|0')

      self.obj124.GGLabel.setValue(3)
      self.obj124.graphClass_= graph_canHaveRole
      if parent.genGraphics:
         new_obj = graph_canHaveRole(150.775714032,90.5328543483,self.obj124)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj124.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj124)
      self.obj124.postAction( self.LHS.CREATE )

      self.obj122.out_connections_.append(self.obj124)
      self.obj124.in_connections_.append(self.obj122)
      self.obj122.graphObject_.pendingConnections.append((self.obj122.graphObject_.tag, self.obj124.graphObject_.tag, [388.0, 424.0, 150.77571403127953, 90.5328543484751], 0, True))
      self.obj124.out_connections_.append(self.obj123)
      self.obj123.in_connections_.append(self.obj124)
      self.obj124.graphObject_.pendingConnections.append((self.obj124.graphObject_.tag, self.obj123.graphObject_.tag, [386.0, 59.0, 248.5, 202.5], 0, True))

      self.RHS = ASG_LSMASOMM(parent)

      self.obj126=OrgUnit(parent)
      self.obj126.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj126)
      self.obj126.postAction( self.RHS.CREATE )

      self.obj127=OrgUnit(parent)
      self.obj127.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj127)
      self.obj127.postAction( self.RHS.CREATE )

      self.obj128=Role(parent)
      self.obj128.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj128)
      self.obj128.postAction( self.RHS.CREATE )

      self.obj129=isPartOfOrgUnit(parent)
      self.obj129.preAction( self.RHS.CREATE )
      self.obj129.isGraphObjectVisual = True

      if(hasattr(self.obj129, '_setHierarchicalLink')):
        self.obj129._setHierarchicalLink(True)

      # ID
      self.obj129.ID.setValue('pOU|0')

      self.obj129.GGLabel.setValue(6)
      self.obj129.graphClass_= graph_isPartOfOrgUnit
      if parent.genGraphics:
         new_obj = graph_isPartOfOrgUnit(170.95,135.5,self.obj129)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj129.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj129)
      self.obj129.postAction( self.RHS.CREATE )

      self.obj130=canHaveRole(parent)
      self.obj130.preAction( self.RHS.CREATE )
      self.obj130.isGraphObjectVisual = True

      if(hasattr(self.obj130, '_setHierarchicalLink')):
        self.obj130._setHierarchicalLink(True)

      # ID
      self.obj130.ID.setValue('OUR|0')

      self.obj130.GGLabel.setValue(3)
      self.obj130.graphClass_= graph_canHaveRole
      if parent.genGraphics:
         new_obj = graph_canHaveRole(96.0835477534,103.612551906,self.obj130)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj130.graphObject_ = new_obj

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj130)
      self.obj130.postAction( self.RHS.CREATE )

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

   def condition(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the ACTION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName25 is not guaranteed to be unique (so change it, be safe!)
      
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      
      for eOut in node.out_connections_:
          if eOut.getClass() == 'canHaveRole':
              roles = eOut.out_connections_
              print(roles)
              for r in roles:
                  if r.name.getValue() == 'PartyFounder':
                      return 1
      return 0
      
      

   def action(self, graphID, isograph, atom3i):
      pass

