#!/usr/bin/python
# -*- coding: utf-8 -*-
# hubs em9NZf))r(D*I#af

from ASGNode import *
from Role import *
from CustomCodeDB import *


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
            [inheritActions.append(a) for a in mR.roleActions.getValue()]

        for a in inheritActions:
            self.roleActions.newItem(item=a)

        # self.roleActions.setValue([self.roleActions.getValue().append(a) for a in inheritActions])

        return inheritActions


def RoleInheritanceAllRoles(self):
    Root = self.ASGroot.getASGbyName('LSMASOMM_META')

    nodeList = Root.listNodes['Role']

    for role in nodeList:
        if role.isMetaRole.toString() is 'False':
            print role
            RoleInheritance(role)
            role.updateAppearanceAttributes()
            # role.graphObject_.ModifyAttribute('roleActions', role.roleActions.toString())


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


def saveToFile(filename, content):
    """Write content into a filename."""
    file = open(filename, 'w')
    file.write(str(content))
    file.close()


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


def printSpecificNodeClassNames(self, className):
    """Work with nodes of a specific class specified by className."""
    # get the current model
    Root = self.ASGroot.getASGbyName('LSMASOMM_META')

    nodeList = Root.listNodes[className]

# aux elements
    # store elements for code generating
    elements = {}

    # beginning of generated code
    code = 'import spade \n'

    # templates for agents ang behaviours
    agent = ["""
class {0}(spade.Agent.Agent):
    '''Bear skeleton for agent type {0}'''
""", """
    def _setup(self):
        print '{0}: running'
"""]

    behaviour = """
    class {0}(spade.Behaviour.OneShotBehaviour):
        '''Bare skeleton for behaviour {0}'''
        def _process(self):
            print '{0}: behaving'
"""

    # OrgUnits
    if className is 'OrgUnit':
        for node in nodeList:
            # save name of the node
            if node.UnitSize.getValue() is 'Individual':
                nodeName = node.name.getValue()
            elif node.UnitSize.getValue() is 'Group':
                nodeName = "OrgUnit{}".format(node.name.getValue())

            elements[nodeName] = {}
            elements[nodeName]['behavs'] = []
            # add declaration of the agent
            elements[nodeName]['code'] = [agent[0].format(nodeName)]

            # work with the behaviours of the agent/role
            for behav in node.UnitActions.getValue():
                elements[nodeName]['behavs'].append(
                    behav.getValue())
                elements[nodeName]['code'].append(
                    behaviour.format(behav.getValue()))

            # add the default method of an agent (_setup)
            elements[nodeName]['code'].append(agent[1].format(nodeName))

        print elements

        for el in elements.keys():
            print elements[el]['code']
            code = code + ''.join(elements[el]['code'])
        saveToFile('./OrgUnit.txt', code)

    # Roles
    if className is 'Role':
        for node in nodeList:
            nodeName = "Role{}".format(node.name.getValue())
            if node.isMetaRole.toString() is 'False':
                elements[nodeName] = {}
                elements[nodeName]['behavs'] = []
                elements[nodeName]['code'] = [agent[0].format(nodeName)]

                for behav in node.roleActions.getValue():
                    elements[nodeName]['behavs'].append(behav.getValue())
                    elements[nodeName]['code'].append(
                        behaviour.format(behav.getValue()))

                elements[nodeName]['code'].append(agent[1].format(nodeName))

        print elements

        for el in elements.keys():
            print elements[el]['code']
            code = code + ''.join(elements[el]['code'])
        saveToFile('./Roles.txt', code)


def SaveAll(self):
    import ZODB, ZODB.FileStorage
    import transaction
    import BTrees.OOBTree

    # open DB connection to file mydata.fs; check if conn is open already
    storage = ZODB.FileStorage.FileStorage('mydata.fs')
    db = ZODB.DB(storage)
    conn = db.open()

    Root = self.ASGroot.getASGbyName('LSMASOMM_META')
    nodeTypeList = Root.listNodes.keys()

    # go through all the nodes
    for nodeType in nodeTypeList:
        nodeList = Root.listNodes[nodeType]
        for node in nodeList:
            # save node to DB
            SaveNode(node, conn)

    db.close()


def SaveNode(node, conn):
    import ZODB, ZODB.FileStorage
    import transaction
    import BTrees.OOBTree

    # create placeholder object of the node, and fill it with attribute values
    nodeNew = savedNode(node.copyCoreAttributes())
    nodeNew.saveAttributes(
        node.realOrder,
        node.getValue()
        )

    # if Node Class is not yet saved, create it in DB
    try:
        nodeClass = conn.root()[node.getClass()]
    except Exception:
        conn.root()[node.getClass()] = {}
        nodeClass = conn.root()[node.getClass()]

    # finally save the node
    nodeClass[nodeNew.objectNumber] = nodeNew
    transaction.commit()
