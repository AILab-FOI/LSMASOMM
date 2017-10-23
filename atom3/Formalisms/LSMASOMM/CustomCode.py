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
# from ATOM3Boolean import *
from StatusBar import *
from ATOM3TypeDialog import *

DBpath = './DB'
DBname = 'LSMASOMM'

def checkUniqueID(self):
    global DBname
    """Check if node ID values specified in the model are unique.
    If two identical values are found in the current model, error occurs.
    If some of the node ID values are in the DB already, user is informed. """
    try:
        Root = self
        db = openDB(DBname)
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


# update list of Actions, to be called by a link element
def UpdateActions(self):
    eOuts = NodeOutputsInputs(self, 'out', 'nodes')
    eIns = NodeOutputsInputs(self, 'in', 'nodes')

    actions = []

    # for updating Action list of a Role (hasActions)
    if 'Action' in eOuts:
        for a in eOuts['Action']:
            actions.append(prepareAttributeValue('ATOM3String', a.name.getValue()))

    if 'Role' in eIns:
        for r in eIns['Role']:
            for a in actions:
                r.hasActions.newItem(a)
            r.graphObject_.ModifyAttribute('hasActions', r.hasActions.toString())
        return 1

    # for updating Action list of an Objective (ofActions)
    if 'Action' in eIns:
        for a in eIns['Action']:
            actions.append(prepareAttributeValue('ATOM3String', a.name.getValue()))

    if 'Objective' in eOuts:
        for o in eOuts['Objective']:
            for a in actions:
                o.ofActions.newItem(a)
        return 1

    # for updating Action list of a Process (hasActions)
    if 'Process' in eOuts:
        for p in eOuts['Process']:
            for a in actions:
                p.hasActions.newItem(a)
            p.graphObject_.ModifyAttribute('hasActions', r.hasActions.toString())
        return 1

    return 0


def ActionCodeTemplate(self):
    '''Fill in ActionCode field with a Behav template, according to the chosen implementation framework'''
    Root = self.parent.ASGroot.getASGbyName('LSMASOMM_META')

    t, s = Root.agentImplementation.getValue()

    # print "Agent implementation framework: {}".format(t[s])

    if t[s] == 'SPADE':

        codeString = u'''#action code template
class BehaviourNamePlaceholder(spade.Behaviour.OneShotBehaviour):
    """Behaviour available to agents."""
    def _process(self):
        pass
'''
    else:
        codeString = ''

    codeTemplate = prepareAttributeValue('ATOM3Text', codeString)
    # codeTemplate = ATOM3Text(codeString, 80, 15)

    return codeTemplate


def RoleHierarchy(self):
    """Check if a Role is a MetaRole, i.e. it has some subRoles."""
    eIns = NodeOutputsInputs(self, 'in', 'count')

    if 'isPartOfRole' in eIns.keys():
        print eIns

        self.isMetaRole.setValue(1)
        self.isMetaRole.config = 0

        return 1

    else:
        self.isMetaRole.setValue(0)
        self.isMetaRole.config = 0

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
            if eOut.getClass() in eOuts.keys():
                eOuts[eOut.getClass()] += 1
            else:
                eOuts[eOut.getClass()] = 1

    elif countNodes is 'nodes':
        for eOut in nodes:
            if eOut.getClass() in eOuts.keys():
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


######### #########
#
# SAVING CONCEPTS
#
######### #########


def openDB(DBnamed='LSMASOMM'):
    global DBname
    # open DB connection to file mydata.fs; check if conn is open already
    storage = ZODB.FileStorage.FileStorage("{}/{}.fs".format(DBpath,DBname))
    db = ZODB.DB(storage)
    return db


# saving process - creating DB and saving individual nodes
def SaveAll(self):
    global DBname
    """Traverse all the nodes of the graph, and save each to the DB."""
    Root = self.ASGroot.getASGbyName('LSMASOMM_META')

    db = openDB(DBname)
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

    if not 'KB' in conn.root():
        conn.root()['KB'] = {'ActionGoal': [], 'RoleAction': []}

    # rules = []

    # for action in Root.listNodes['Action']:
    #     for postLink in action.out_connections_:
    #         for goal in postLink.out_connections_:
    #             if goal.__class__.__name__ == 'Objective':
    #                 conn.root()['KB']['ActionGoal'].append((action.name.getValue(), 'canReachGoal', goal.name.getValue()))

    for goal in conn.root()['Objective'].values():
        for a in goal.attrs.split('\n'):
            conn.root()['KB']['ActionGoal'].append((a, 'canReachGoal', goal.attrs[goal.realOrder.index('name')]))


    # for process in Root.listNodes['Process']:
    #     # if 'RoleProcessGoals' not in KB.keys():
    #     #     KB['RoleProcessGoals'] = []

    #     for prevLink in process.in_connections_:
    #         for prevNode in prevLink.in_connections_:
    #             for postLink in process.out_connections_:
    #                 for postNode in postLink.out_connections_:
    #                     rules.append((prevNode.name.getValue(), 'canReachGoal', postNode.name.getValue()))

    # KB['RoleProcessGoal'] = rules

    # print rules

    transaction.commit()
    # rules = []

    # for role in Root.listNodes['Role']:
    #     for b in role.getValue()[role.realOrder.index('hasActions')]:
    #         rules.append((role.name.getValue(), 'hasAction', b.toString()))

    # KB['RoleActions'] = rules
    # # conn.root()['KB'].update({"RoleActions":rules})
    # print rules

    # conn.root()['KB'] = KB

    # transaction.commit()

    db.close()


def SaveNode(node, conn, update=False):
    """Save one particular Node [node] to the already open DB [conn]."""
    if update:
        DBnode = conn.root()[node.__class__.__name__][node.ID.getValue()]
        DBnode.updateAttributes(
            node.getStringValue(),
            node.copyCoreAttributes()[2:4])

    else:
        # create placeholder object of the node,
        # and fill it with attribute values
        DBnode = savedNode(node.copyCoreAttributes())
        DBnode.saveAttributes(
            node.realOrder,
            node.getStringValue())

        conn.root()[node.getClass()].update(
            {DBnode.ID: DBnode})


def addConnectionToDB(self):
    global DBname
    if os.path.isfile("./DB/{}.fs".format(self.name.getValue())):

        try:
            db = openDB(DBname)
            conn = db.open()
        except Exception:
            # exception usually raised by Loading a node from DB, because reasons...
            print "Called from another function (probably when loading concepts)"
            return

        for nodeType in self.listNodes.keys():
            try:
                for node in self.listNodes[nodeType]:
                    if node.ID.getValue() in conn.root()[nodeType].keys():
                        # IN connecctions
                        if len(node.in_connections_):
                            print "{} in nodes: {}".format(
                                node.ID.getValue(),
                                [x.ID.getValue() for x in node.in_connections_])
                            inNode = node.in_connections_[-1]
                            DBnode = conn.root()[nodeType][node.ID.getValue()]
                            # if INnode class is not present, add it
                            if inNode.__class__.__name__ not in DBnode.in_connections_:
                                DBnode.in_connections_[inNode.__class__.__name__] = []
                            # if INnode class is present, add the node to DB
                            if inNode.ID.getValue() not in DBnode.in_connections_[inNode.__class__.__name__]:
                                SaveNode(node, conn, True)
                                DBnode.in_connections_._p_changed = 1
                                transaction.commit()
                        # OUT connections
                        if len(node.out_connections_):
                            print "{} out nodes: {}".format(
                                node.ID.getValue(),
                                [x.ID.getValue() for x in node.out_connections_])
                            outNode = node.out_connections_[-1]
                            DBnode = conn.root()[nodeType][node.ID.getValue()]
                            # if OUTnode class is not present, add it
                            if outNode.__class__.__name__ not in DBnode.out_connections_:
                                DBnode.out_connections_[outNode.__class__.__name__] = []
                            # if OUTnode class is present, add the node to DB
                            if outNode.ID.getValue() not in DBnode.out_connections_[outNode.__class__.__name__]:
                                SaveNode(node, conn, True)
                                DBnode.out_connections_._p_changed = 1
                                transaction.commit()
                    else:
                        SaveNode(node, conn)
                        transaction.commit()
            except Exception:
                pass

        # print conn.root()['canStartProcess']
        db.close()


######### #########
#
# GENERATING CODE TEMPLATE
#
######### #########


def generateNodeCode(self):
    global DBname
    Root = self.ASGroot.getASGbyName('LSMASOMM_META')
    db = openDB(DBname)
    conn = db.open()

    if not os.path.isdir("./Code"):
        os.mkdir("./Code")

    # writing start of the role behaviour file
    filename = './Code/RoleBehaviours.py'
    if os.path.isfile(filename):
        os.rename(filename, '{}.old'.format(filename))

    file = open(filename, 'w')

    for k,v in conn.root()['Action'].items():
        file.write("\n{}".format(v.attrs[0]))
    file.close()

    agents = []


    KB = conn.root()['KB']['RoleProcessGoal'] + conn.root()['KB']['RoleActions']

    # generate code for OrgUnits
    for k, v in conn.root()['OrgUnit'].items():
        agents.append(v.generateCodeSPADE(KB))

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
        global DBname
        # Root = parent.ASGroot.getASGbyName('LSMASOMM_META')
        # self.DBname = Root.name.getValue()
        self.parent = parent
        self.DBname = StringVar()
        self.DBname.set(DBname)
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

        # List of available DBs
        self.availableDBs = Listbox(
            self.win,
            height=3)

        files = [file for file in os.listdir(DBpath)
                 if os.path.isfile(os.path.join(DBpath, file))]
        names = [e.split('.fs')[0] for e in files if e[-2:] == 'fs']

        for n in sorted(names):
            if n:
                self.availableDBs.insert(END, n)

        self.availableDBs.pack(
            side=TOP,
            fill=X,
            expand=NO)

        self.availableDBs.activate(0)

        # Refresh Button
        self.btnR = Button(
            self.win,
            command=self.RefreshList,
            text="Load Selected DB",
            background="green",
            height=1)

        self.btnR.pack(
            side=TOP,
            fill=X,
            expand=NO)

        # Lable DB
        self.winlabelDB = Label(
            self.win,
            textvariable=self.DBname,
            relief=RIDGE,
            height=1)
        self.winlabelDB.pack(
            side=TOP,
            fill=X,
            expand=NO)

        # List of Concepts
        self.concList = Listbox(
            self.win)

        self.FillList()

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

    def FillList(self):
        global DBname
        db = openDB(DBname)

        self.conn = db.open()
        self.nodeTypeList = [(k, len(v)) for k, v in self.conn.root().items()]

        for x in sorted(self.nodeTypeList):
            if x[1] and x[0] != 'KB':
                self.concList.insert(END, "{x[0]} ({x[1]})".format(x=x))

        db.close()

    def RefreshList(self):
        global DBname
        try:
            DBname = self.availableDBs.get(self.availableDBs.curselection())
            self.DBname.set(DBname)
        except Exception as e:
            tkMessageBox.showinfo(
                "Error",
                "No concept selected!\n{}".format(e))

        self.concList.delete(0, END)
        self.FillList()

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
        global DBname
        # self.name = name
        self.concType = concType
        self.Root = parent.ASGroot.getASGbyName('LSMASOMM_META')
        db = openDB(DBname)

        self.parent = parent

        self.conn = db.open()
        # nodes of concepts stored in DB
        self.DBconcepts = self.conn.root()[concType].items()


        print "DBconcepts: {}".format(self.DBconcepts)

        for k, v in self.DBconcepts:
            try:
                print "Koncepti:{} - {}, {}".format(k, v.in_connections_, v.out_connections_)
            except:
                try:
                    print "Koncepti:{} - {}, {}".format(k, None, v.out_connections_)
                except:
                    print "Koncepti:{} - {}, {}".format(k, v.in_connections_, None)

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


        self.concList.pack(
            side=TOP,
            fill=BOTH,
            expand=YES)

        db.close()

        self.concList.activate(1)

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

        # Button
        self.btn2 = Button(
            self.win,
            command=self.CreateAllElements,
            text="Load All",
            background="green",
            height=1)

        self.btn2.pack(
            side=TOP,
            fill=X,
            expand=NO)

    def ConceptSelectFeedback(self):
        # retrieve the selected concept
        selectConcept = self.concList.get(self.concList.curselection())

        self.concList.delete(self.concList.curselection())

        self.concList.activate(0)

        # create the retrieved concept in the model canvas
        CreateElement(
            self,
            selectConcept.split(' //', 1)[0].strip(),
            self.concType)

        # self.win.destroy()

    def CreateAllElements(self):
        # retrieve all the concepts

        while self.concList.size():
            selectConcept = self.concList.get(0)

            self.concList.delete(0)

            self.concList.activate(0)

            # create the retrieved concept in the model canvas
            CreateElement(
                self,
                selectConcept.split(' //', 1)[0].strip(),
                self.concType)

        self.win.destroy()


def prepareAttributeValue(attr, value):
    print 'Attribute type processed: {}; {} ({})'.format(
        attr,
        value,
        type(value))
    attribute = None

    if attr == 'ATOM3String':
        attribute = ATOM3String(value, 20)
    elif attr == 'ATOM3Text':
        attribute = ATOM3Text(value, 80, 15)
    elif attr == 'ATOM3List':
        attribute = ATOM3List([1, 1, 1, 0], ATOM3String)
        vals = []
        for v in value.split():
            vals.append(ATOM3String(v, 20))
        attribute.setValue(vals)
    elif attr == 'ATOM3Boolean':
        attribute = ATOM3Boolean()
        if value == 'True':
            attribute.setValue(1)
        elif value == 'False':
            attribute.setValue(0)
        attribute.config = 0

    return attribute


def CreateElement(self, nodeID, nodeClass, conn=None):
    """Create an element on the given canvas, where
    nodeID and nodeClass are of the node to be created,
    conn is connection to the DB."""
    global DBname
    if not conn:
        db = openDB(DBname)
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
        'Action': root.createNewAction,
        'canAccessKnArt': root.createNewcanAccessKnArt,
        'canHaveRole': root.createNewcanHaveRole,
        'isPartOfRole': root.createNewisPartOfRole,
        'isPartOfOrgUnit': root.createNewisPartOfOrgUnit,
        'isPartOfObjective': root.createNewisPartOfObjective,
        'isPartOfProcess': root.createNewisPartOfProcess,
        'answersToOrgUnit': root.createNewanswersToOrgUnit,
        'canStartProcess': root.createNewcanStartProcess,
        'hasObjective': root.createNewhasObjective,
        'hasActions': root.createNewhasActions,
        'genericAssociation': root.createNewgenericAssociation,
        'answersToRole': root.createNewanswersToRole
    }

    self.newElement = funcCalls[nodeClass](root, 100, 100)

    print "\n####{}\n{}\n{}\n{}\n{}".format(
        self.newElement.__class__.__name__,
        self.newElement,
        self.newElement.graphClass_,
        self.newElement.ID.getValue(),
        self.newElement.getValue())

    # identify the selected concept in the database
    for k, v in sorted(concepts):
        try:
            if k == nodeID:
                self.savedElement = v
                # nr = k
        except Exception as e:
            print e
            # if v.objectNumber == int(nodeID):
            #     self.savedElement = v
                # nr = k

    try:
        self.newElement.keyword_.setValue(
            self.savedElement.keyword_.getValue())
    except:
        print "No keyword_ set."

    print "###{}\n{}\n{}\n{}\n{}\n{}\n{}".format(
        self.savedElement.__class__.__name__,
        self.savedElement,
        self.savedElement.ID,
        self.savedElement.keyword_,
        self.savedElement.graphClass_,
        self.savedElement.in_connections_,
        self.savedElement.out_connections_
        )

    self.newElement.keyword_ = self.savedElement.keyword_
    # self.newElement.editGGLabel = self.savedElement.editGGLabel
    # self.newElement.GGset2Any = self.savedElement.GGset2Any
    self.newElement.GGLabel.setValue(self.savedElement.GGLabel)
    self.newElement.objectNumber = self.savedElement.objectNumber
    self.newElement.ID.setValue(self.savedElement.ID)
    # self.newElement.in_connections_ = self.savedElement.in_connections_ # won't work because only objectNumber is given
    # self.newElement.out_connections_ = self.savedElement.out_connections_

    # copy attribute values to the new node from the saved node

    # self.newElement.setValue(self.savedElement.attrs)

    # try:
    #     self.newElement.setValue(self.savedElement.attrs)
    # except:
    #     counter = 0
    #     for a in self.newElement.realOrder:
    #         self.newElement.setAttrValue(a, self.savedElement.attrs[counter])

    counter = 0
    for a in self.newElement.realOrder:
        attribute = prepareAttributeValue(self.newElement.getAttrValue(a).__class__.__name__, self.savedElement.attrs[counter])
        self.newElement.setAttrValue(a, attribute)
        counter += 1

    for attr in self.newElement.realOrder:
        print "Attribute type for {}: {}".format(attr, self.newElement.getAttrValue(attr).__class__.__name__)
        if self.newElement.getAttrValue(attr).__class__.__name__ == 'ATOM3List':
            self.newElement.graphObject_.ModifyAttribute(attr, self.newElement.getAttrValue(attr).toString())
        else:
            self.newElement.graphObject_.ModifyAttribute(attr, self.newElement.getAttrValue(attr).getValue())

    print "##\n{}\n{}".format(
        self.newElement.copyCoreAttributes(),
        self.newElement.getValue())

    modelNodes = sum(self.Root.listNodes.values(), [])
    modelNodesID = [x.ID.getValue() for x in modelNodes]
    print "Nodes in model: {}\n Node IDs: {}".format(modelNodes, modelNodesID)

    if self.savedElement.in_connections_:
        # check for all connection nodes by class name
        for conSet in self.savedElement.in_connections_.items():
            print "Connection set: {}".format(conSet)
            for conNode in conSet[1]:
                # if connection node exists on canvas already
                if conNode in modelNodesID:
                    for x in modelNodes:
                        print "{} vs. {}".format(conNode, x.ID.getValue())
                        if conNode == x.ID.getValue():
                        # create connection
                            print "Bingo!"
                            DrawConnections.simpleConnection(self.parent, x, self.newElement)

                # if it does not exist
                else:
                    # get all objectNumbers of INnodes of the connection node
                    farNodes = sum(conn.root()[conSet[0]][conNode].in_connections_.values(), [])
                    print "Far nodes: {}".format(farNodes)
                    for farNode in farNodes:
                        # if an INnode of connection node exists in the model
                        if farNode in modelNodesID:
                            # if connection node exists on canvas already
                            if conNode in [x.ID.getValue() for x in sum(self.Root.listNodes.values(), [])]:
                                continue
                            else:
                                # create connection node
                                CreateElement(self, conNode, conSet[0], conn=conn)
                                # create connection
                                print "Bingo2b!"

    if self.savedElement.out_connections_:
        # check for all connection nodes by class name
        for conSet in self.savedElement.out_connections_.items():
            print "Connection set: {}".format(conSet)
            for conNode in conSet[1]:
                print "{} -- {}".format(conNode, modelNodesID)
                # if connection node exists on canvas already
                if conNode in modelNodesID:
                    for x in modelNodes:
                        print "{} vs. {}".format(conNode, x.ID.getValue())
                        if conNode == x.ID.getValue():
                            # create connection
                            print "Bingo!"
                            DrawConnections.simpleConnection(self.parent, self.newElement, x)
                            break

                # if it does not exist
                else:
                    # get all objectNumbers of OUTnodes of the connection node
                    farNodes = sum(conn.root()[conSet[0]][conNode].out_connections_.values(), [])
                    print "Far nodes: {}".format(farNodes)
                    for farNode in farNodes:
                        # if an OUTnode of connection node exists in the model
                        if farNode in modelNodesID:
                            # if connection node exists on canvas already
                            if conNode in [x.ID.getValue() for x in sum(self.Root.listNodes.values(), [])]:
                                continue
                            else:
                                # create connection node
                                CreateElement(self, conNode, conSet[0], conn=conn)
                                # create connection
                                print "Bingo2b!"

    try:
        db.close()
    except Exception as e:
        print e
