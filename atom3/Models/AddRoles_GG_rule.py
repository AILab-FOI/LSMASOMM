# _ AddRoles_GG_rule.py ____________________________________________________________________________
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
class AddRoles_GG_rule (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_LSMASOMM(parent)

      self.obj112=OrgUnit(parent)
      self.obj112.preAction( self.LHS.CREATE )
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
      if parent.genGraphics:
         new_obj = graph_OrgUnit(60.0,120.0,self.obj112)
         new_obj.layConstraints = dict() # Graphical Layout Constraints 
         new_obj.layConstraints['scale'] = [1.0, 1.0]
      else: new_obj = None
      self.obj112.graphObject_ = new_obj

      # Add node to the root: self.LHS
      self.LHS.addNode(self.obj112)
      self.obj112.postAction( self.LHS.CREATE )


      self.RHS = ASG_LSMASOMM(parent)

      self.obj114=OrgUnit(parent)
      self.obj114.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj114)
      self.obj114.postAction( self.RHS.CREATE )

      self.obj115=Role(parent)
      self.obj115.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj115)
      self.obj115.postAction( self.RHS.CREATE )

      self.obj116=Role(parent)
      self.obj116.preAction( self.RHS.CREATE )
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
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj116)
      self.obj116.postAction( self.RHS.CREATE )

      self.obj117=canHaveRole(parent)
      self.obj117.preAction( self.RHS.CREATE )
      self.obj117.isGraphObjectVisual = True

      if(hasattr(self.obj117, '_setHierarchicalLink')):
        self.obj117._setHierarchicalLink(True)

      # ID
      self.obj117.ID.setValue('OUR|90')

      self.obj117.GGLabel.setValue(4)
      self.obj117.graphClass_= graph_canHaveRole
      if parent.genGraphics:
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

      # Add node to the root: self.RHS
      self.RHS.addNode(self.obj117)
      self.obj117.postAction( self.RHS.CREATE )

      self.obj114.out_connections_.append(self.obj117)
      self.obj117.in_connections_.append(self.obj114)
      self.obj114.graphObject_.pendingConnections.append((self.obj114.graphObject_.tag, self.obj117.graphObject_.tag, [71.0, 203.0, 178.5, 145.5], 0, True))
      self.obj117.out_connections_.append(self.obj115)
      self.obj115.in_connections_.append(self.obj117)
      self.obj117.graphObject_.pendingConnections.append((self.obj117.graphObject_.tag, self.obj115.graphObject_.tag, [286.0, 102.0, 178.5, 152.5], 0, True))
      self.obj117.out_connections_.append(self.obj116)
      self.obj116.in_connections_.append(self.obj117)
      self.obj117.graphObject_.pendingConnections.append((self.obj117.graphObject_.tag, self.obj116.graphObject_.tag, [306.0, 222.0, 178.5, 152.5], 0, True))

   def condition(self, graphID, isograph, atom3i):
      # If you want to apply this rule at most once on asingle host graph node, 
      # then uncomment the next two lines. Change the default GG label (1) if needed.
      
      # Make sure to enable the ACTION code as well
      # And to use the same label & unique name in the ACTION
      # WARNING: _uniqueName13 is not guaranteed to be unique (so change it, be safe!)
      
      #from CustomCode import NodeOutputsInputs
      
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      
      for eOut in node.out_connections_:
          if eOut.getClass() == 'canHaveRole':
              roles = eOut.out_connections_
              for r in roles:
                  if r.name.getValue() == 'PartyFounder':
                      return 0
      print(eOut)
      return 1
      
      

   def action(self, graphID, isograph, atom3i):
      pass

