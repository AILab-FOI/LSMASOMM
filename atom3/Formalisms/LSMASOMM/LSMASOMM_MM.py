"""
__LSMASOMM_MM.py______________________________________________________

Automatically generated AToM3 MetaModel (DO NOT MODIFY DIRECTLY)
Author: bogdan
Modified: Sat Oct 21 18:15:30 2017
______________________________________________________________________
"""
from ASG_LSMASOMM import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter         import *
from ATOM3TypeInfo   import *
from ATOM3String     import *
from StatusBar       import *
from ATOM3TypeDialog import *

from OrgUnit       import *
from Role       import *
from Action       import *
from KnowledgeArtifacts       import *
from OrganisationalKnArt       import *
from IndividualKnArt       import *
from Strategy       import *
from Objective       import *
from Process       import *
from isPartOfOrgUnit       import *
from canHaveRole       import *
from hasActions       import *
from canAccessKnArt       import *
from isPartOfObjective       import *
from hasObjective       import *
from genericAssociation       import *
from answersToRole       import *
from canStartProcess       import *
from answersToOrgUnit       import *
from isPartOfRole       import *
from isPartOfProcess       import *
def createNewASGroot(self):
   return ASG_LSMASOMM(self, None)

def createModelMenu(self, modelMenu):
    "Creates a customized Model Menu for the actual formalism"
    modelMenu.add_command(label="New OrgUnit", command=lambda x=self: x.createNewOrgUnit(x, 100, 100) )
    modelMenu.add_command(label="New Role", command=lambda x=self: x.createNewRole(x, 100, 100) )
    modelMenu.add_command(label="New Action", command=lambda x=self: x.createNewAction(x, 100, 100) )
    modelMenu.add_command(label="New KnowledgeArtifacts", command=lambda x=self: x.createNewKnowledgeArtifacts(x, 100, 100) )
    modelMenu.add_command(label="New OrganisationalKnArt", command=lambda x=self: x.createNewOrganisationalKnArt(x, 100, 100) )
    modelMenu.add_command(label="New IndividualKnArt", command=lambda x=self: x.createNewIndividualKnArt(x, 100, 100) )
    modelMenu.add_command(label="New Strategy", command=lambda x=self: x.createNewStrategy(x, 100, 100) )
    modelMenu.add_command(label="New Objective", command=lambda x=self: x.createNewObjective(x, 100, 100) )
    modelMenu.add_command(label="New Process", command=lambda x=self: x.createNewProcess(x, 100, 100) )
    modelMenu.add_command(label="New isPartOfOrgUnit", command=lambda x=self: x.createNewisPartOfOrgUnit(x, 100, 100) )
    modelMenu.add_command(label="New canHaveRole", command=lambda x=self: x.createNewcanHaveRole(x, 100, 100) )
    modelMenu.add_command(label="New hasActions", command=lambda x=self: x.createNewhasActions(x, 100, 100) )
    modelMenu.add_command(label="New canAccessKnArt", command=lambda x=self: x.createNewcanAccessKnArt(x, 100, 100) )
    modelMenu.add_command(label="New isPartOfObjective", command=lambda x=self: x.createNewisPartOfObjective(x, 100, 100) )
    modelMenu.add_command(label="New hasObjective", command=lambda x=self: x.createNewhasObjective(x, 100, 100) )
    modelMenu.add_command(label="New genericAssociation", command=lambda x=self: x.createNewgenericAssociation(x, 100, 100) )
    modelMenu.add_command(label="New answersToRole", command=lambda x=self: x.createNewanswersToRole(x, 100, 100) )
    modelMenu.add_command(label="New canStartProcess", command=lambda x=self: x.createNewcanStartProcess(x, 100, 100) )
    modelMenu.add_command(label="New answersToOrgUnit", command=lambda x=self: x.createNewanswersToOrgUnit(x, 100, 100) )
    modelMenu.add_command(label="New isPartOfRole", command=lambda x=self: x.createNewisPartOfRole(x, 100, 100) )
    modelMenu.add_command(label="New isPartOfProcess", command=lambda x=self: x.createNewisPartOfProcess(x, 100, 100) )
def setConnectivity(self):
    self.ConnectivityMap['isPartOfProcess']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': [( 'Process', self.createNewProcess)]
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['OrganisationalKnArt']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['hasActions']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': [( 'Action', self.createNewAction)]
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['hasObjective']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': [( 'Objective', self.createNewObjective)]
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['Process']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': [( 'hasObjective', self.createNewhasObjective)]
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['Strategy']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['canHaveRole']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': [( 'Role', self.createNewRole)]
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': [( 'Role', self.createNewRole)]
          ,'isPartOfRole': [( 'Role', self.createNewRole)]
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': [( 'Role', self.createNewRole)]
          ,'Role': []
          ,'genericAssociation': [( 'Role', self.createNewRole)]
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': [( 'Role', self.createNewRole)]
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [( 'Role', self.createNewRole)] }
    self.ConnectivityMap['isPartOfRole']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': [( 'Role', self.createNewRole)]
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': [( 'Role', self.createNewRole)]
          ,'isPartOfRole': [( 'Role', self.createNewRole)]
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': [( 'Role', self.createNewRole)]
          ,'Role': []
          ,'genericAssociation': [( 'Role', self.createNewRole)]
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': [( 'Role', self.createNewRole)]
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [( 'Role', self.createNewRole)] }
    self.ConnectivityMap['IndividualKnArt']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['answersToOrgUnit']={
           'isPartOfOrgUnit': [( 'OrgUnit', self.createNewOrgUnit)]
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': [( 'OrgUnit', self.createNewOrgUnit)]
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': [( 'OrgUnit', self.createNewOrgUnit)]
          ,'Objective': []
          ,'canAccessKnArt': [( 'OrgUnit', self.createNewOrgUnit)]
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['KnowledgeArtifacts']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['isPartOfObjective']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': [( 'Objective', self.createNewObjective)]
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['Objective']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': [( 'isPartOfObjective', self.createNewisPartOfObjective)]
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['canStartProcess']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': [( 'Process', self.createNewProcess)]
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['Role']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': [( 'canAccessKnArt', self.createNewcanAccessKnArt)]
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': [( 'canStartProcess', self.createNewcanStartProcess)]
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': [( 'canAccessKnArt', self.createNewcanAccessKnArt)]
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': [( 'hasActions', self.createNewhasActions)]
          ,'canStartProcess': []
          ,'Role': [( 'genericAssociation', self.createNewgenericAssociation), ( 'answersToRole', self.createNewanswersToRole), ( 'isPartOfRole', self.createNewisPartOfRole)]
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': [( 'hasObjective', self.createNewhasObjective)]
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['isPartOfOrgUnit']={
           'isPartOfOrgUnit': [( 'OrgUnit', self.createNewOrgUnit)]
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': [( 'OrgUnit', self.createNewOrgUnit)]
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': [( 'OrgUnit', self.createNewOrgUnit)]
          ,'Objective': []
          ,'canAccessKnArt': [( 'OrgUnit', self.createNewOrgUnit)]
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['Action']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': [( 'isPartOfProcess', self.createNewisPartOfProcess)]
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['canAccessKnArt']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': []
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': []
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['OrgUnit']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': [( 'canAccessKnArt', self.createNewcanAccessKnArt)]
          ,'hasObjective': []
          ,'OrgUnit': [( 'isPartOfOrgUnit', self.createNewisPartOfOrgUnit), ( 'answersToOrgUnit', self.createNewanswersToOrgUnit)]
          ,'Process': []
          ,'hasActions': []
          ,'isPartOfRole': []
          ,'IndividualKnArt': [( 'canAccessKnArt', self.createNewcanAccessKnArt)]
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': []
          ,'Role': [( 'canHaveRole', self.createNewcanHaveRole)]
          ,'genericAssociation': []
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': []
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [] }
    self.ConnectivityMap['answersToRole']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': [( 'Role', self.createNewRole)]
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': [( 'Role', self.createNewRole)]
          ,'isPartOfRole': [( 'Role', self.createNewRole)]
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': [( 'Role', self.createNewRole)]
          ,'Role': []
          ,'genericAssociation': [( 'Role', self.createNewRole)]
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': [( 'Role', self.createNewRole)]
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [( 'Role', self.createNewRole)] }
    self.ConnectivityMap['genericAssociation']={
           'isPartOfOrgUnit': []
          ,'isPartOfObjective': []
          ,'OrganisationalKnArt': []
          ,'hasObjective': [( 'Role', self.createNewRole)]
          ,'OrgUnit': []
          ,'Process': []
          ,'hasActions': [( 'Role', self.createNewRole)]
          ,'isPartOfRole': [( 'Role', self.createNewRole)]
          ,'IndividualKnArt': []
          ,'answersToOrgUnit': []
          ,'Strategy': []
          ,'isPartOfProcess': []
          ,'Action': []
          ,'canStartProcess': [( 'Role', self.createNewRole)]
          ,'Role': []
          ,'genericAssociation': [( 'Role', self.createNewRole)]
          ,'canHaveRole': []
          ,'Objective': []
          ,'canAccessKnArt': [( 'Role', self.createNewRole)]
          ,'KnowledgeArtifacts': []
          ,'answersToRole': [( 'Role', self.createNewRole)] }
    
    self.CardinalityTable['OrgUnit']={
          'OrgUnit': []
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'canHaveRole': [('0', 'N', 'Source')]
          ,'hasActions': []
          ,'canAccessKnArt': [('0', 'N', 'Source')]
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['Role']={
          'OrgUnit': []
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': [('0', 'N', 'Destination')]
          ,'hasActions': [('0', 'N', 'Source')]
          ,'canAccessKnArt': [('0', 'N', 'Source')]
          ,'isPartOfObjective': []
          ,'hasObjective': [('0', 'N', 'Source')]
          ,'genericAssociation': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'answersToRole': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'canStartProcess': [('0', 'N', 'Source')]
          ,'answersToOrgUnit': []
          ,'isPartOfRole': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'isPartOfProcess': [] }
    self.CardinalityTable['Action']={
          'OrgUnit': []
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': [('0', 'N', 'Destination')]
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [('0', 'N', 'Source')] }
    self.CardinalityTable['KnowledgeArtifacts']={
          'OrgUnit': []
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['OrganisationalKnArt']={
          'OrgUnit': []
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': [('0', 'N', 'Destination')]
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['IndividualKnArt']={
          'OrgUnit': []
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': [('0', 'N', 'Destination')]
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['Strategy']={
          'OrgUnit': []
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['Objective']={
          'OrgUnit': []
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': [('0', 'N', 'Source'), ('0', 'N', 'Destination')]
          ,'hasObjective': [('0', 'N', 'Destination')]
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['Process']={
          'OrgUnit': []
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': [('0', 'N', 'Source')]
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': [('0', 'N', 'Destination')]
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [('0', 'N', 'Destination')] }
    self.CardinalityTable['isPartOfOrgUnit']={
          'OrgUnit': [('1', 'N', 'Destination'), ('1', 'N', 'Source')]
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['canHaveRole']={
          'OrgUnit': [('0', 'N', 'Destination')]
          ,'Role': [('0', 'N', 'Source')]
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['hasActions']={
          'OrgUnit': []
          ,'Role': [('1', '1', 'Destination')]
          ,'Action': [('1', 'N', 'Source')]
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['canAccessKnArt']={
          'OrgUnit': [('0', 'N', 'Destination')]
          ,'Role': [('0', 'N', 'Destination')]
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': [('0', 'N', 'Source')]
          ,'IndividualKnArt': [('0', 'N', 'Source')]
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['isPartOfObjective']={
          'OrgUnit': []
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['hasObjective']={
          'OrgUnit': []
          ,'Role': [('0', 'N', 'Destination')]
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': [('1', 'N', 'Source')]
          ,'Process': [('0', 'N', 'Destination')]
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['genericAssociation']={
          'OrgUnit': []
          ,'Role': [('1', 'N', 'Source'), ('1', 'N', 'Destination')]
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['answersToRole']={
          'OrgUnit': []
          ,'Role': [('1', 'N', 'Destination'), ('1', 'N', 'Source')]
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['canStartProcess']={
          'OrgUnit': []
          ,'Role': [('0', 'N', 'Destination')]
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': [('0', 'N', 'Source')]
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['answersToOrgUnit']={
          'OrgUnit': [('1', 'N', 'Source'), ('1', 'N', 'Destination')]
          ,'Role': []
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['isPartOfRole']={
          'OrgUnit': []
          ,'Role': [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
          ,'Action': []
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': []
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    self.CardinalityTable['isPartOfProcess']={
          'OrgUnit': []
          ,'Role': []
          ,'Action': [('0', 'N', 'Destination')]
          ,'KnowledgeArtifacts': []
          ,'OrganisationalKnArt': []
          ,'IndividualKnArt': []
          ,'Strategy': []
          ,'Objective': []
          ,'Process': [('0', 'N', 'Source')]
          ,'isPartOfOrgUnit': []
          ,'canHaveRole': []
          ,'hasActions': []
          ,'canAccessKnArt': []
          ,'isPartOfObjective': []
          ,'hasObjective': []
          ,'genericAssociation': []
          ,'answersToRole': []
          ,'canStartProcess': []
          ,'answersToOrgUnit': []
          ,'isPartOfRole': []
          ,'isPartOfProcess': [] }
    
    self.entitiesInMetaModel['LSMASOMM']=["OrgUnit", "Role", "Action", "KnowledgeArtifacts", "OrganisationalKnArt", "IndividualKnArt", "Strategy", "Objective", "Process", "isPartOfOrgUnit", "canHaveRole", "hasActions", "canAccessKnArt", "isPartOfObjective", "hasObjective", "genericAssociation", "answersToRole", "canStartProcess", "answersToOrgUnit", "isPartOfRole", "isPartOfProcess"]

    
def createNewOrgUnit(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = OrgUnit(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["OrgUnit"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_OrgUnit(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_OrgUnit(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("OrgUnit", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewRole(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Role(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Role"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Role(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Role(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Role", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewAction(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Action(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Action"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Action(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Action(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Action", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewKnowledgeArtifacts(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = KnowledgeArtifacts(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["KnowledgeArtifacts"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_KnowledgeArtifacts(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_KnowledgeArtifacts(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("KnowledgeArtifacts", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewOrganisationalKnArt(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = OrganisationalKnArt(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["OrganisationalKnArt"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_OrganisationalKnArt(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_OrganisationalKnArt(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("OrganisationalKnArt", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewIndividualKnArt(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = IndividualKnArt(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["IndividualKnArt"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_IndividualKnArt(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_IndividualKnArt(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("IndividualKnArt", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewStrategy(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Strategy(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Strategy"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Strategy(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Strategy(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Strategy", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewObjective(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Objective(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Objective"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Objective(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Objective(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Objective", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewProcess(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = Process(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["Process"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_Process(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_Process(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("Process", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewisPartOfOrgUnit(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = isPartOfOrgUnit(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["isPartOfOrgUnit"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_isPartOfOrgUnit(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_isPartOfOrgUnit(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("isPartOfOrgUnit", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewcanHaveRole(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = canHaveRole(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["canHaveRole"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_canHaveRole(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_canHaveRole(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("canHaveRole", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewhasActions(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = hasActions(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["hasActions"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_hasActions(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_hasActions(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("hasActions", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewcanAccessKnArt(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = canAccessKnArt(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["canAccessKnArt"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_canAccessKnArt(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_canAccessKnArt(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("canAccessKnArt", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewisPartOfObjective(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = isPartOfObjective(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["isPartOfObjective"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_isPartOfObjective(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_isPartOfObjective(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("isPartOfObjective", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewhasObjective(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = hasObjective(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["hasObjective"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_hasObjective(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_hasObjective(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("hasObjective", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewgenericAssociation(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = genericAssociation(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["genericAssociation"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_genericAssociation(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_genericAssociation(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("genericAssociation", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewanswersToRole(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = answersToRole(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["answersToRole"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_answersToRole(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_answersToRole(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("answersToRole", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewcanStartProcess(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = canStartProcess(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["canStartProcess"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_canStartProcess(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_canStartProcess(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("canStartProcess", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewanswersToOrgUnit(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = answersToOrgUnit(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["answersToOrgUnit"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_answersToOrgUnit(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_answersToOrgUnit(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("answersToOrgUnit", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewisPartOfRole(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = isPartOfRole(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["isPartOfRole"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_isPartOfRole(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_isPartOfRole(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("isPartOfRole", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNewisPartOfProcess(self, wherex, wherey, screenCoordinates = 1):
   self.fromClass = None
   self.toClass = None
   # try the global constraints...
   res = self.ASGroot.preCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   new_semantic_obj = isPartOfProcess(self)
   res = new_semantic_obj.preCondition ( ASGNode.CREATE )
   if res: return self.constraintViolation(res)
   new_semantic_obj.preAction ( ASGNode.CREATE ) 

   ne = len(self.ASGroot.listNodes["isPartOfProcess"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_isPartOfProcess(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_isPartOfProcess(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("isPartOfProcess", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   res = self.ASGroot.postCondition(ASG.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return

   res = new_semantic_obj.postCondition(ASGNode.CREATE)
   if res:
      self.constraintViolation(res)
      self.mode=self.IDLEMODE
      return
   new_semantic_obj.postAction(ASGNode.CREATE)

   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def createNew_Model(self, wherex, wherey, screenCoordinates = 1):
   self.toClass = None
   self.fromClass = None
   new_semantic_obj = ASG_LSMASOMM(self)
   ne = len(self.ASGroot.listNodes["ASG_LSMASOMM"])
   if new_semantic_obj.keyword_:
      new_semantic_obj.keyword_.setValue(new_semantic_obj.keyword_.toString()+str(ne))
   if screenCoordinates:
      new_obj = graph_ASG_ERmetaMetaModel(self.UMLmodel.canvasx(wherex), self.UMLmodel.canvasy(wherey), new_semantic_obj)
   else: # already in canvas coordinates
      new_obj = graph_ASG_ERmetaMetaModel(wherex, wherey, new_semantic_obj)
   new_obj.DrawObject(self.UMLmodel, self.editGGLabel)
   self.UMLmodel.addtag_withtag("ASG_LSMASOMM", new_obj.tag)
   new_semantic_obj.graphObject_ = new_obj
   self.ASGroot.addNode(new_semantic_obj)
   self.mode=self.IDLEMODE
   if self.editGGLabel :
      self.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
   else:
      self.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
   return new_semantic_obj
def fillTypesInformation(self):
    objs = []
    self.typeList.setValue(objs)

