#!/usr/bin/python
# -*- coding: utf-8 -*-
# hubs em9NZf))r(D*I#af

from ASGNode import *
from Role import *
from CustomCodeDB import *
import ZODB
import ZODB.FileStorage
import transaction
from persistent.mapping import PersistentMapping
import os
import DrawConnections
# from os import mkdir, getcwd, isdir

from ASG_LSMASOMM import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter import *
from ATOM3TypeInfo import *
from ATOM3String import *
from StatusBar import *
from ATOM3TypeDialog import *

from Role import *


def checkUniqueID(self):
    """Check if node ID values specified in the model are unique.
    If two identical values are found in the current model, error occurs.
    If some of the node ID values are in the DB already, user is informed. """
    try:
        Root = self
        db = openDB(Root.name.getValue())
        conn = db.open()

        # Nodes and ID values of all the nodes present in the model
        MDnodes = sum(Root.listNodes.values(), [])
        MDnodesID = [n.ID.getValue() for n in MDnodes]
        # ID values of all the nodes present in the DB file
        DBnodesID = sum([n.keys() for n in conn.root().values()], [])

        db.close()

        print "\nNodes in model: {}".format(MDnodesID)
        print "Nodes in DB: {}".format(DBnodesID)

        # if there are duplicate ID values in the model
        if len(MDnodesID) != len(set(MDnodesID)):
            nodeID = [n for n in set(MDnodesID) if MDnodesID.count(n) > 1][0]
            # return True to AToM3 to raise error
            return (MDnodes[MDnodesID.index(nodeID)].graphObject_, nodeID)

        # check for every node in the model
        existID = []
        for node in MDnodes:
            nodeID = node.ID.getValue()
            print "check.ID: {}".format(nodeID)

            # check if the node ID values exists in the DB already
            if nodeID in DBnodesID:
                # inform the user that the ID is a duplicate
                existID.append(nodeID)
        if existID:
            tkMessageBox.showinfo(
                "Duplicate ID(s)",
                "The following ID(s) already exist in the DB: {}".format(str(existID).strip('[]'))
            )

        return False
    except Exception as e:
        print e
        return False

def canAccessKnArtCheckConnections(self):
    '''
    Check input and output connections of a canAccessKnArt instance.

    Return value depencs on the set of constraints:
        - either a Role or an OrgUnit can be input connection;
        - Rule instance can access OrgKnArt only;
        - OrgUnit instance can access IndivKnArt only;

    and is described in the model as follows:

res = canAccessKnArtCheckConnections(self)
if res is "eitherRoleOrUnit":
    return ("Either Role of OrgUnit can access knowledge.", self.graphObject_)
elif res is "onlyOneInput":
    return ("Only one Role or OrgUnit can access one knowledge medium.", self.graphObject_)
elif res is "RoleWithOrgOnly":
    return ("Role can access OrganisationalKnArt only!", self.graphObject_)
elif res is "OrgUnitWithIndivOnly":
    return ("OrgUnit can access IndividualKnArt only!", self.graphObject_)
else:
    return
    '''
    eIns = NodeOutputsInputs(self, 'in', 'count')
    if 'Role' in eIns and 'OrgUnit' in eIns:
        return 'eitherRoleOrUnit'
    # removed since two OrgUnits or two Roles can have access to the same set of KnArts
    # if 'Role' in eIn and eIn['Role'] > 1 or 'OrgUnit' in eIn and eIn['OrgUnit'] > 1:
    #     return 'onlyOneInput'

    eOuts = NodeOutputsInputs(self, 'out', 'count')
    if 'Role' in eIns and 'IndividualKnArt' in eOuts:
        return 'RoleWithOrgOnly'
    if 'OrgUnit' in eIns and 'OrganisationalKnArt' in eOuts:
        return 'OrgUnitWithIndivOnly'
    return


def OrgUnitCheckOutputs(self):
    '''
    Check output connections of an OrgUnit instance.

    Return value depends on the set constraints:
        - can have only one canAccessKnArt;

    and is described in the model as follows:

res = OrgUnitCheckOutputs(self)
if res is "manyKnArts":
    return ("OrgUnit can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)
else:
    return
    '''
    eOuts = NodeOutputsInputs(self, 'out', 'count')

    # cannot have more than 1 connection towards canAccessKnArt
    if 'canAccessKnArt' in eOuts:
        if eOuts['canAccessKnArt'] > 1:
            return "manyKnArts"

    return


def OrgUnitDetermineSize(self):
    """Determine whether OrgUnit is an Individual or a Group."""
    eIns = NodeOutputsInputs(self, 'in', 'count')

    if 'isPartOfOrgUnit' in eIns:
        # self.Individual = False
        return 'Group'
    elif 'isPartOfOrgUnit' not in eIns:
        # self.Individual = True
        return 'Individual'

    return


def RoleHierarchy(self):
    """Check if a Role is a MetaRole, i.e. it has some subRoles."""
    eIns = NodeOutputsInputs(self, 'in', 'count')

    if 'isPartOfRole' in eIns:
        print eIns
        return 1
    else:
        return 0


def RoleInheritance(self):
    """Make Role nodes inherit Actions from their superior Roles."""
    eOuts = NodeOutputsInputs(self, 'out', 'nodes')

    metaRoles = []
    inheritActions = []

    if 'isPartOfRole' in eOuts:
        for link in eOuts['isPartOfRole']:
            # print link.out_connections_
            eOutsLink = NodeOutputsInputs(link, 'out', 'nodes')
            if 'Role' in eOutsLink:
                for mR in eOutsLink['Role']:
                    metaRoles.append(mR)

        for mR in metaRoles:
            [inheritActions.append(a) for a in mR.hasActions.getValue()]

        for a in inheritActions:
            self.hasActions.newItem(item=a)

        # self.hasActions.setValue([self.hasActions.getValue().append(a) for a in inheritActions])

        return inheritActions


def RoleInheritanceAllRoles(self):
    Root = self.ASGroot.getASGbyName('LSMASOMM_META')

    nodeList = Root.listNodes['Role']

    for role in nodeList:
        if role.isMetaRole.toString() is 'False':
            print role
            RoleInheritance(role)
            role.updateAppearanceAttributes()
            # role.graphObject_.ModifyAttribute('hasActions', role.hasActions.toString())


def RoleCheckOutputs(self):
    '''
    Check output connections of a Role instance.

    Return value depends on the set constraints:
        - can have only one canAccessKnArt;

    and is described in the model as follows:

res = RoleCheckOutputs(self)
if res is "manyKnArts":
    return ("Role can have only one accessway to knowledge artifacts (KnArt)!", self.graphObject_)
else:
    return
    '''
    eOuts = NodeOutputsInputs(self, 'out', 'count')

    # cannot have more than 1 connection towards canAccessKnArt
    if 'canAccessKnArt' in eOuts:
        if eOuts['canAccessKnArt'] > 1:
            return "manyKnArts"

    return


def NodeOutputsInputs(self, inOutBoth, countNodes):
    """Iterate through inputs and/or outputs of a node.
Returns a dictionary with
'ClassName':numberOfInstances
OR
'ClassName':[instances] dictionary

inOutBoth -- in / out / both -- iterates through input / output / both nodes
countNodes -- count / nodes -- returns count of nodes or nodes
"""
    eOuts = {}

    if inOutBoth is 'in':
        nodes = self.in_connections_
    elif inOutBoth is 'out':
        nodes = self.out_connections_
    elif inOutBoth is 'both':
        nodes = self.in_connections_
        nodes.append(self.out_connections_)

    if countNodes is 'count':
        for eOut in nodes:
            if eOut.getClass() in eOuts:
                eOuts[eOut.getClass()] += 1
            else:
                eOuts[eOut.getClass()] = 1

    elif countNodes is 'nodes':
        for eOut in nodes:
            if eOut.getClass() in eOuts:
                eOuts[eOut.getClass()].append(eOut)
            else:
                eOuts[eOut.getClass()] = [eOut]

    return eOuts


def printAllNodeNames(self):
    '''
    '''
    # get the current model
    Root = self.ASGroot.getASGbyName('LSMASOMM_META')

    # traverse all nodes of the graph
    nodeTypeList = Root.listNodes.keys()
    for nodeType in nodeTypeList:
        print "#### {} ####".format(nodeType)
        nodeList = Root.listNodes[nodeType]
        for node in nodeList:
            for attr in node.realOrder:
                try:
                    print "{} -- {}".format(attr, node.getAttrValue(attr).getValue())
                except Exception as e:
                    print e


def saveToFile(filename, content):
    """Write content into a filename."""
    file = open(filename, 'w')
    file.write(str(content))
    file.close()

#
#
# SAVING CONCEPTS
#
#


def openDB(DBname='LSMASOMM'):
    # open DB connection to file mydata.fs; check if conn is open already
    storage = ZODB.FileStorage.FileStorage("./DB/{}.fs".format(DBname))
    db = ZODB.DB(storage)
    return db


# saving process - creating DB and saving individual nodes
def SaveAll(self):
    """Traverse all the nodes of the graph, and save each to the DB."""
    Root = self.ASGroot.getASGbyName('LSMASOMM_META')

    db = openDB(Root.name.getValue())
    conn = db.open()

    # go through all the node types
    for nodeType in Root.listNodes.keys():
        try:
            dbRoot = conn.root()[nodeType]
        except Exception as e:
            print e
            # conn.root()[nodeType] = {}
            conn.root()[nodeType] = PersistentMapping()
            dbRoot = conn.root()[nodeType]

        # go through all the nodes of a specific type
        for node in Root.listNodes[nodeType]:
            if node.ID.getValue() in dbRoot.keys():
                # update already existing node
                SaveNode(node, conn, True)
            else:
                # save node to DB
                SaveNode(node, conn)

    transaction.commit()

    KB = {}
    rules = []

    for process in Root.listNodes['Process']:
        # if 'RoleProcessGoals' not in KB.keys():
        #     KB['RoleProcessGoals'] = []

        for prevLink in process.in_connections_:
            for prevNode in prevLink.in_connections_:
                for postLink in process.out_connections_:
                    for postNode in postLink.out_connections_:
                        rules.append((prevNode.name.getValue(), 'canReachGoal', postNode.name.getValue()))

    KB['RoleProcessGoal'] = rules

    print rules

    transaction.commit()
    rules = []

    for role in Root.listNodes['Role']:
        for b in role.getValue()[role.realOrder.index('hasActions')]:
            rules.append((role.name.getValue(), 'hasAction', b.getValue()))

    KB['RoleActions'] = rules
    # conn.root()['KB'].update({"RoleActions":rules})
    print rules

    conn.root()['KB'] = KB

    transaction.commit()

    db.close()


def SaveNode(node, conn, update=False):
    """Save one particular Node [node] to the already open DB [conn]."""
    if update:
        DBnode = conn.root()[node.__class__.__name__][node.ID.getValue()]
        DBnode.updateAttributes(
            node.getValue(),
            node.copyCoreAttributes()[2:4])

    else:
        # create placeholder object of the node,
        # and fill it with attribute values
        DBnode = savedNode(node.copyCoreAttributes())
        DBnode.saveAttributes(
            node.realOrder,
            node.getValue())

        conn.root()[node.getClass()].update(
            {DBnode.ID: DBnode})


def addConnectionToDB(self):
    if os.path.isfile("./DB/{}.fs".format(self.name.getValue())):

        try:
            db = openDB(self.name.getValue())
            conn = db.open()
        except Exception:
            # exception usually raised by Loading a node from DB, because reasons...
            print "Called from another function (probably when loading concepts)"
            return

        for nodeType in self.listNodes.keys():
            for node in self.listNodes[nodeType]:
                if node.objectNumber in conn.root()[nodeType].keys():
                    # IN connecctions
                    if len(node.in_connections_):
                        print "{} in nodes: {}".format(
                            node.objectNumber,
                            [x.objectNumber for x in node.in_connections_])
                        inNode = node.in_connections_[-1]
                        DBnode = conn.root()[nodeType][node.objectNumber]
                        # if INnode class is not present, add it
                        if inNode.__class__.__name__ not in DBnode.in_connections_:
                            DBnode.in_connections_[inNode.__class__.__name__] = []
                        # if INnode class is present, add the node to DB
                        if inNode.objectNumber not in DBnode.in_connections_[inNode.__class__.__name__]:
                            SaveNode(node, conn, True)
                            DBnode.in_connections_._p_changed = 1
                            transaction.commit()
                    # OUT connections
                    if len(node.out_connections_):
                        print "{} out nodes: {}".format(
                            node.objectNumber,
                            [x.objectNumber for x in node.out_connections_])
                        outNode = node.out_connections_[-1]
                        DBnode = conn.root()[nodeType][node.objectNumber]
                        # if OUTnode class is not present, add it
                        if outNode.__class__.__name__ not in DBnode.out_connections_:
                            DBnode.out_connections_[outNode.__class__.__name__] = []
                        # if OUTnode class is present, add the node to DB
                        if outNode.objectNumber not in DBnode.out_connections_[outNode.__class__.__name__]:
                            SaveNode(node, conn, True)
                            DBnode.out_connections_._p_changed = 1
                            transaction.commit()
                else:
                    SaveNode(node, conn)
                    transaction.commit()

        print conn.root()['canStartProcess']
        db.close()


def generateNodeCode(self):
    Root = self.ASGroot.getASGbyName('LSMASOMM_META')
    db = openDB(Root.name.getValue())
    conn = db.open()

    if not os.path.isdir("./Code"):
        os.mkdir("./Code")

    # writing start of the role behaviour file
    filename = './Code/RoleBehaviours.py'
    if os.path.isfile(filename):
        os.rename(filename, '{}.old'.format(filename))

    file = open(filename, 'w')
    file.write("""import spade
class ChangeRole(spade.Behaviour.OneShotBehaviour):
    '''Basic Behaviour for changing Roles.'''
    def _process(self):
        print 'I would like to change...'
""")
    file.close()

    agents = []

    # generate Director Role
    DirectorAgent = GenerateAgentSPADE(
        'DirectorAgent',
        behavs=[
            'ReceiveRequest',
            'FindSuitableRole',
            'AnswerRequest'],
        KB=conn.root()['KB']['RoleProcessGoal'])
    agents.append(DirectorAgent.generateCode())

    # generate Teacher Agent
    TeacherAgent = GenerateAgentSPADE(
        'TeacherAgent',
        behavs=[
            'ReceiveRequest',
            'FindSuitableBehaviours',
            'AnswerRequest'],
        KB=conn.root()['KB']['RoleActions'])
    agents.append(TeacherAgent.generateCode())

    # generate code for OrgUnits
    for k, v in conn.root()['OrgUnit'].items():
        agents.append(v.generateCodeSPADE())

    # generate code for Roles
    for k, v in conn.root()['Role'].items():
        v.generateCodeSPADE()

    db.close()

    # writing the agent system file
    filename = './Code/TheSystem.py'

    if os.path.isfile(filename):
        os.rename(filename, '{}.old'.format(filename))

    file = open(filename, 'w')
    file.write("import spade\nfrom RoleBehaviours import *\n")
    for agT in agents:
        file.write("from {} import *\n".format(agT))

    file.write('\nif __name__ == "__main__":\n')

    for x in range(0, len(agents)):
        file.write("""
    agent{0} = {1}("{1}{0}@127.0.0.1", "secret")
    agent{0}.start()
""".format(x, agents[x]))

    file.close()

#
#
# LOADING CONCEPTS
#
#


class ClassSelectionWindow:
    """docstring for ClassSelectionWindow"""
    def __init__(self, parent):
        Root = parent.ASGroot.getASGbyName('LSMASOMM_META')
        db = openDB(Root.name.getValue())

        self.conn = db.open()
        self.nodeTypeList = [(k, len(v)) for k, v in self.conn.root().items()]
        db.close()

        self.parent = parent
        # print self.parent

        self.win = Toplevel()
        self.win.geometry("200x320")
        self.win.title('Select Concept Type')

        # Lable
        self.winlabel = Label(
            self.win,
            text='Select concept type:',
            relief=RIDGE,
            height=1)
        self.winlabel.pack(
            side=TOP,
            fill=X,
            expand=NO)

        # List of Concepts
        self.concList = Listbox(
            self.win)

        for x in sorted(self.nodeTypeList):
            if x[1]:
                self.concList.insert(END, "{x[0]} ({x[1]})".format(x=x))

        self.concList.pack(
            side=TOP,
            fill=BOTH,
            expand=YES)

        self.concList.activate(0)

        # Button
        self.btn = Button(
            self.win,
            command=self.SelectValue,
            text="Continue",
            background="green",
            height=1)

        self.btn.pack(
            side=TOP,
            fill=X,
            expand=NO)

    def SelectValue(self):
        selection = None
        try:
            selection = self.concList.curselection()
        except Exception as e:
            tkMessageBox.showinfo(
                "Error",
                "No concept selected!\n{}".format(e))

        if selection is not None:
            # print self.wherex, self.wherey
            selectConcept = ConceptSelectWindow(self.concList.get(selection).split(' (',1)[0], self.parent)


class ConceptSelectWindow:
    """docstring for ConceptSelectWindow"""
    def __init__(self, concType, parent):
        self.concType = concType
        self.Root = parent.ASGroot.getASGbyName('LSMASOMM_META')
        db = openDB(self.Root.name.getValue())

        self.parent = parent

        self.conn = db.open()
        # nodes of concepts stored in DB
        self.DBconcepts = self.conn.root()[concType].items()


        print "DBconcepts: {}".format(self.DBconcepts)

        for k, v in self.DBconcepts:
            print "Koncepti:{} - {}, {}".format(k, v.in_connections_, v.out_connections_)

        self.win = Toplevel()
        self.win.geometry("200x320")
        self.win.title(
            'Select a {} Concept'.format(concType))

        # Lable
        self.winlabel = Label(
            self.win,
            text='Select a {} concept:'.format(concType),
            relief=RIDGE,
            height=1)
        self.winlabel.pack(
            side=TOP,
            fill=X,
            expand=NO)

        # List of Concepts
        self.concList = Listbox(
            self.win)

        MDnodes = self.Root.listNodes[concType]
        MDnodesID = [x.ID.getValue() for x in MDnodes]

        try:
            for k, v in sorted(self.DBconcepts):
                if k not in MDnodesID: #v.objectNumber not in [x.objectNumber for x in MDnodes] and v.attrs[v.realOrder.index('name')] not in [x.name.getValue() for x in MDnodes]:
                    self.concList.insert(END, "{:9} // {}".format(k, v.attrs[v.realOrder.index('name')]))
        except Exception:
            for k, v in sorted(self.DBconcepts):
                if k not in MDnodesID:
                    self.concList.insert(END, "{:9} // no name".format(k))

        db.close()

        self.concList.pack(
            side=TOP,
            fill=BOTH,
            expand=YES)

        self.concList.activate(0)

        # Button
        self.btn = Button(
            self.win,
            command=self.ConceptSelectFeedback,
            text="Load",
            background="green",
            height=1)

        self.btn.pack(
            side=TOP,
            fill=X,
            expand=NO)

    def ConceptSelectFeedback(self):
        # retrieve the selected concept
        selectConcept = self.concList.get(self.concList.curselection())

        # check if node exists in the model already
        self.CreateElement(selectConcept.split(' //', 1)[0].strip(), self.concType)

        self.win.destroy()
        # self.CreateElement(selectConcept, self.concType)

    # def CheckNodeExist(self, nodeID, nodeClass):
    #     modelNodes = self.Root.listNodes[nodeClass]
    #     print "New node: {} vs. {}".format(nodeID, [x.objectNumber for x in modelNodes])

    #     if nodeID in [x.objectNumber for x in modelNodes] and nodeID in [x.name.getValue() for x in modelNodes]:
    #         return
    #     else:
    #         self.CreateElement(nodeID, nodeClass)
    #     # modelNodes = sum(self.Root.listNodes.values(), [])

    #     # if nodeNumber in [x.objectNumber for x in modelNodes]:


    def CreateElement(self, nodeID, nodeClass, conn=None):
        if not conn:
            db = openDB(self.Root.name.getValue())
            conn = db.open()

        concepts = conn.root()[nodeClass].items()

        root = self.parent

        # dynamic creation function calling, depending on the class
        funcCalls = {
            'Role': root.createNewRole,
            'OrgUnit': root.createNewOrgUnit,
            'Objective': root.createNewObjective,
            'Process': root.createNewProcess,
            'IndividualKnArt': root.createNewIndividualKnArt,
            'OrganisationalKnArt': root.createNewOrganisationalKnArt,
            'canAccessKnArt': root.createNewcanAccessKnArt,
            'canHaveRole': root.createNewcanHaveRole,
            'isPartOfRole': root.createNewisPartOfRole,
            'isPartOfOrgUnit': root.createNewisPartOfOrgUnit,
            'isPartOfObjective': root.createNewisPartOfObjective,
            'answersToOrgUnit': root.createNewanswersToOrgUnit,
            'canStartProcess': root.createNewcanStartProcess,
            'hasObjective': root.createNewhasObjective,
            'genericAssociation': root.createNewgenericAssociation,
            'answersToRole': root.createNewanswersToRole
        }

        newElement = funcCalls[nodeClass](root, 100, 100)

        print "\n####{}\n{}\n{}\n{}\n{}".format(
            newElement.__class__.__name__,
            newElement,
            newElement.graphClass_,
            newElement.ID.getValue(),
            newElement.getValue())

        # identify the selected concept in the database
        for k, v in sorted(self.DBconcepts):
            try:
                if k == nodeID:
                    savedElement = v
                    # nr = k
            except Exception as e:
                print e
                # if v.objectNumber == int(nodeID):
                #     savedElement = v
                    # nr = k

        try:
            newElement.keyword_.setValue(
                savedElement.keyword_.getValue())
        except:
            print "No keyword_ set."

        print "###{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
            savedElement.__class__.__name__,
            savedElement,
            savedElement.ID,
            savedElement.keyword_,
            savedElement.graphClass_,
            savedElement.in_connections_,
            savedElement.out_connections_
            )

        newElement.keyword_ = savedElement.keyword_
        # newElement.editGGLabel = savedElement.editGGLabel
        # newElement.GGset2Any = savedElement.GGset2Any
        newElement.GGLabel.setValue(savedElement.GGLabel)
        newElement.objectNumber = savedElement.objectNumber
        # newElement.in_connections_ = savedElement.in_connections_ # won't work because only objectNumber is given
        # newElement.out_connections_ = savedElement.out_connections_

        # copy attribute values to the new node from the saved node
        newElement.setValue(savedElement.attrs)

        for attr in newElement.realOrder:
            if newElement.getAttrValue(attr).__class__.__name__ == 'ATOM3List':
                newElement.graphObject_.ModifyAttribute(attr, newElement.getAttrValue(attr).toString())
            else:
                newElement.graphObject_.ModifyAttribute(attr, newElement.getAttrValue(attr).getValue())

        print "##\n{}\n{}".format(
            newElement.copyCoreAttributes(),
            newElement.getValue())

        modelNodes = sum(self.Root.listNodes.values(), [])
        print "Nodes in model: {}".format(modelNodes)

        if savedElement.in_connections_:
            # check for all connection nodes by class name
            for conSet in savedElement.in_connections_.items():
                print "Connection set: {}".format(conSet)
                for conNode in conSet[1]:
                    # if connection node exists on canvas already
                    if conNode in [x.ID.getValue() for x in modelNodes]:
                        for x in modelNodes:
                            print "{} vs. {}".format(conNode, x.ID.getValue())
                            if conNode == x.ID.getValue():
                            # create connection
                                print "Bingo!"
                                DrawConnections.simpleConnection(self.parent, x, newElement)

                    # if it does not exist
                    else:
                        # get all objectNumbers of INnodes of the connection node
                        farNodes = sum(conn.root()[conSet[0]][conNode].in_connections_.values(), [])
                        print "Far nodes: {}".format(farNodes)
                        for farNode in farNodes:
                            # if an INnode of connection node exists in the model
                            if farNode in [x.ID.getValue() for x in modelNodes]:
                                # create connection node
                                self.CreateElement(conNode, conSet[0], conn=conn)
                                # create connection
                                print "Bingo2!"

        if savedElement.out_connections_:
            # check for all connection nodes by class name
            for conSet in savedElement.out_connections_.items():
                print "Connection set: {}".format(conSet)
                for conNode in conSet[1]:
                    # if connection node exists on canvas already
                    if conNode in [x.ID.getValue() for x in modelNodes]:
                        for x in modelNodes:
                            print "{} vs. {}".format(conNode, x.ID.getValue())
                            if conNode == x.ID.getValue():
                            # create connection
                                print "Bingo!"
                                DrawConnections.simpleConnection(self.parent, newElement, x)

                    # if it does not exist
                    else:
                        # get all objectNumbers of INnodes of the connection node
                        farNodes = sum(conn.root()[conSet[0]][conNode].out_connections_.values(), [])
                        print "Far nodes: {}".format(farNodes)
                        for farNode in farNodes:
                            # if an INnode of connection node exists in the model
                            if farNode in [x.ID.getValue() for x in modelNodes]:
                                # create connection node
                                self.CreateElement(conNode, conSet[0], conn=conn)
                                # create connection
                                print "Bingo2!"

        try:
            db.close()
        except Exception:
            pass
