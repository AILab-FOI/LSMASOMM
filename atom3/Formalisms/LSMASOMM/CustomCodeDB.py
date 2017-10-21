import persistent
import os


class savedNode(persistent.Persistent):
    """This is a class containing all the data specifying a Node in a specific ASG"""

    def __init__(self, coreAttrs):
        """Initialise the savedNode object with values for all the default attributes."""
        self.graphClass_ = coreAttrs[0]
        self.isClass = coreAttrs[1]
        self.in_connections_ = coreAttrs[2]
        self.out_connections_ = coreAttrs[3]
        self.containerFrame = coreAttrs[4]
        self.keyword_ = coreAttrs[5]
        self.editGGLabel = coreAttrs[6]
        self.GGset2Any = coreAttrs[7]
        self.GGLabel = coreAttrs[8]
        # self.rootNode = coreAttrs[9]
        self.objectNumber = coreAttrs[10]
        self.ID = coreAttrs[11]

    def saveAttributes(self, order, attrValues):
        """Save custom attributes of the Node."""
        self.realOrder = order
        self.attrs = attrValues

        print self.attrs

    def updateAttributes(self, attrValues, connections):
        """Update custom attributes of the Node."""
        self.attrs = attrValues

        print connections

        modelInCs = connections[0]
        modelOutCs = connections[1]

        for nodeType in modelInCs.keys():
            newConn = [
                x for x in modelInCs[nodeType]
                if x not in self.in_connections_[nodeType]]
            if len(newConn):
                self.in_connections_[nodeType].append(newConn[0])
                # print '{} added to {}'.format(newConn, self.attrs[self.realOrder.index('name')])

        for nodeType in modelOutCs.keys():
            newConn = [
                x for x in modelOutCs[nodeType]
                if x not in self.out_connections_[nodeType]]
            if len(newConn):
                self.out_connections_[nodeType].append(newConn[0])
                # print '{} added to {}'.format(newConn, self.attrs[self.realOrder.index('name')])

        print self.attrs

    def getAttribute(self, attrName):
        if hasattr(self, attrName):
            return self.attrs[self.realOrder.index(attrName)]

    def generateCodeSPADE(self, KB=None):
        """Generate code for the Node."""

        print "Generating stuff...", self.isClass

        # templates for agents ang behaviours
        agent = [
"""
class {0}(spade.Agent.Agent):
    '''Bear skeleton for agent type {0}'''
""",
"""
    def _setup(self):
        print '{0}: running'
        self.addBehaviour(self.ChangeRole(), None)

"""]
        behaviour = """
    class {0}(spade.Behaviour.OneShotBehaviour):
        '''Behaviour {0} of {2} {1}'''
        def _process(self):
            print '{1}: behaving {0}'
"""

        if hasattr(self, 'isClass') and self.isClass in ['OrgUnit']:
            # beginning of generated code
            code = "import spade\nfrom RoleBehaviours import *\n"

            nodeName = "OU{}{}".format(
                self.ID,
                self.attrs[self.realOrder.index('name')])

            file = open("./Code/{}.py".format(nodeName), 'w')

            # nodeName = "{}{}".format(
            #     self.isClass,
            #     self.attrs[self.realOrder.index('name')])

            code = code + agent[0].format(nodeName)

            print self.attrs[self.realOrder.index('hasActions')]

            for behav in self.attrs[self.realOrder.index('hasActions')].split("\n")[:-1]:
                # code = code + "\n{}\n".format(behav.getValue())
                code = code + behaviour.format(
                    behav,
                    self.attrs[self.realOrder.index('name')],
                    self.isClass)

            code = code + agent[1].format(nodeName)


            if KB:
                code = code + """
        self.configureKB('SWI', None, 'swipl')"""
                for x in KB:
                    code = code + """
        self.addBelieve('{0[1]}({0[0]},{0[2]})')""".format(x)

            file.write(code)
            file.close()

            print nodeName

            return nodeName
