#!/usr/bin/python
# -*- coding: utf-8 -*-
# hubs em9NZf))r(D*I#af

from ASGNode import *
from Role import *
from CustomCodeDB import *
import ZODB
import ZODB.FileStorage
import transaction
import os
# from os import mkdir, getcwd, isdir

from ASG_LSMASOMM import *
from graph_ASG_ERmetaMetaModel import *
from Tkinter import *
from ATOM3TypeInfo import *
from ATOM3String import *
from StatusBar import *
from ATOM3TypeDialog import *

from Role import *


def setNodeID(self):
    ID = "{}{}".format(self.getClass(), self.objectNumber)
    self.ID.setValue(ID)
    return ID


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


def openDB():
    # open DB connection to file mydata.fs; check if conn is open already
    storage = ZODB.FileStorage.FileStorage('mydata.fs')
    db = ZODB.DB(storage)
    return db


def generateNodeCode(self):
    # print os.getcwd()
    db = openDB()
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


# dasdasdsadasd
def SaveAll(self):
    """Traverse all the nodes of the graph, and save each to the DB."""
    db = openDB()
    conn = db.open()

    Root = self.ASGroot.getASGbyName('LSMASOMM_META')
    nodeTypeList = Root.listNodes.keys()

    # go through all the nodes
    for nodeType in nodeTypeList:
        conn.root()[nodeType] = {}
        nodeList = Root.listNodes[nodeType]
        for node in nodeList:
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

def SaveNode(node, conn):
    """Save one particular Node [node] to the already open DB [conn]."""
    # create placeholder object of the node, and fill it with attribute values
    nodeNew = savedNode(node.copyCoreAttributes())
    nodeNew.saveAttributes(
        node.realOrder,
        node.getValue(),
    )

    conn.root()[node.getClass()].update(
        {nodeNew.objectNumber: nodeNew})

#
#
# GRAPHICS / LOADING CONCEPTS
#
#


class ClassSelectionWindow:
    """docstring for ClassSelectionWindow"""
    def __init__(self, parent, wherex, wherey):
        self.wherex = wherex
        self.wherey = wherey

        db = openDB()
        self.conn = db.open()
        self.nodeTypeList = self.conn.root().keys()
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
            self.concList.insert(END, x)

        self.concList.pack(
            side=TOP,
            fill=BOTH,
            expand=YES)

        self.concList.activate(0)

        # Button
        self.btn = Button(
            self.win,
            command=self.PrintSelection,
            text="Continue",
            background="green",
            height=1)

        self.btn.pack(
            side=TOP,
            fill=X,
            expand=NO)

    def PrintSelection(self):
        selection = None
        try:
            selection = self.concList.curselection()
        except Exception as e:
            tkMessageBox.showinfo(
                "Error",
                "No concept selected!\n{}".format(e))

        if selection is not None:
            # print self.wherex, self.wherey
            selectConcept = ConceptSelectWindow(self.concList.get(selection), self.parent, self.wherex, self.wherey)


class ConceptSelectWindow:
    """docstring for ConceptSelectWindow"""
    def __init__(self, concType, parent, wherex=100, wherey=100):
        self.concType = concType
        db = openDB()

        self.wherex = wherex
        self.wherey = wherey
        self.parent = parent
        # print self.wherex, self.wherey, self.parent

        self.conn = db.open()
        self.concepts = self.conn.root()[concType].items()

        self.win = Toplevel()
        self.win.geometry("200x320")
        self.win.title(
            'Select {} Concept'.format(concType))

        # Lable
        self.winlabel = Label(
            self.win,
            text='Select {} concept:'.format(concType),
            relief=RIDGE,
            height=1)
        self.winlabel.pack(
            side=TOP,
            fill=X,
            expand=NO)

        # List of Concepts
        self.concList = Listbox(
            self.win)

        for k, v in sorted(self.concepts):
            self.concList.insert(END, v.attrs[v.realOrder.index('name')])

        db.close()

        self.concList.pack(
            side=TOP,
            fill=BOTH,
            expand=YES)

        self.concList.activate(0)

        # Button
        self.btn = Button(
            self.win,
            command=self.CreateElement,
            text="Select",
            background="green",
            height=1)

        self.btn.pack(
            side=TOP,
            fill=X,
            expand=NO)

        # print concType

    def CreateElement(self):
        db = openDB()

        root = self.parent

        # dynamic creation function calling, depending on the class
        funcCalls = {
            'Role': root.createNewRole,
            'OrgUnit': root.createNewOrgUnit
        }

        newElement = funcCalls[self.concType](root, 100, 100)

        print "####{}\n{}\n{}\n{}\n{}".format(
            newElement.__class__.__name__,
            newElement,
            newElement.graphClass_,
            newElement.objectNumber,
            newElement.getValue())

        # newRole = Role(root)
        # newRole.doPrint()

        # retrieve the selected concept
        selectConcept = self.concList.get(self.concList.curselection())

        # identify the selected concept in the database
        for k, v in sorted(self.concepts):
            if v.attrs[v.realOrder.index('name')] == selectConcept:
                savedElement = v
                nr = k

        try:
            newElement.keyword_.setValue(
                savedElement.keyword_.getValue())
        except:
            print "No keyword_ set."

        print "###{}\n{}\n{}\n{}\n{}".format(
            savedElement.__class__.__name__,
            savedElement,
            savedElement.keyword_,
            savedElement.graphClass_,
            savedElement.objectNumber
            )

        newElement.keyword_ = savedElement.keyword_
        # newElement.editGGLabel = savedElement.editGGLabel
        # newElement.GGset2Any = savedElement.GGset2Any
        newElement.GGLabel.setValue(savedElement.GGLabel)
        newElement.objectNumber = savedElement.objectNumber

        # copy attribute values to the new node from the saved node
        newElement.setValue(savedElement.attrs)

        for attr in newElement.realOrder:
            if newElement.getAttrValue(attr).__class__.__name__ == 'ATOM3List':
                newElement.graphObject_.ModifyAttribute(attr, newElement.getAttrValue(attr).toString())
            else:
                newElement.graphObject_.ModifyAttribute(attr, newElement.getAttrValue(attr).getValue())

        # newElement.graphObject_.ModifyAttribute('name', newElement.name.getValue())
        # newElement.graphObject_.ModifyAttribute('ID', newElement.ID.getValue())
        # newElement.graphObject_.ModifyAttribute('UnitSize', newElement.UnitSize.getValue())
        # newElement.graphObject_.ModifyAttribute('hasActions', newElement.hasActions.toString())

        print "##\n{}\n{}".format(
            newElement.copyCoreAttributes(),
            newElement.getValue())

        # atom3i = self.parent
        # Root = atom3i.ASGroot.getASGbyName('LSMASOMM_META')
        # # self.parent.ASGroot.getASGbyName('LSMASOMM_META')

        # new_semantic_obj = Role(Root)


        # for k, v in sorted(self.concepts):
        #     if v.attrs[v.realOrder.index('name')] == selectConcept:
        #         nr = k

        db.close()

        # new_obj = graph_Role(self.wherex, self.wherey, new_semantic_obj)
        # new_obj.DrawObject(Root.UMLmodel, Root.editGGLabel)
        # Root.UMLmodel.addtag_withtag("Role", new_obj.tag)
        # new_semantic_obj.graphObject_ = new_obj
        # Root.ASGroot.addNode(new_semantic_obj)

        # Root.mode = Root.IDLEMODE
        # if Root.editGGLabel:
        #     Root.statusbar.event(StatusBar.TRANSFORMATION, StatusBar.CREATE)
        # else:
        #     Root.statusbar.event(StatusBar.MODEL, StatusBar.CREATE)
        # return new_semantic_obj
