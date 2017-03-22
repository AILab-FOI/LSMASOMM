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

        # if len(modelInCs) == len(self.in_connections_) and len(modelOutCs) == len(self.out_connections_):
        #     return

        # # if the model has more connections than DB node
        # # add the missing connection to DB node
        # # since it was added only now, it is [-1]
        # if len(modelInCs) > self.in_connections_:
        #     self.in_connections_.append(modelInCs[-1])
        # elif len(modelOutCs) > self.out_connections_:
        #     self.out_connections_.append(modelOutCs[-1])

        # # if the model has less connections than DB node
        # # remove the extra connection from DB node
        # elif len(modelInCs) < self.in_connections_:
        #     self.in_connections_.remove(
        #         [x for x in self.in_connections_ if x not in modelInCs][0])
        # elif len(modelOutCs) < self.out_connections_:
        #     self.out_connections_.remove(
        #         [x for x in self.out_connections_ if x not in modelOutCs][0])

        print self.attrs

    def getAttribute(self, attrName):
        if hasattr(self, attrName):
            return self.attrs[self.realOrder.index(attrName)]

    def generateCodeSPADE(self):
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

            nodeName = "{}{}{}".format(
                self.isClass,
                self.objectNumber,
                self.attrs[self.realOrder.index('name')])

            file = open("./Code/{}.py".format(nodeName), 'w')

            # nodeName = "{}{}".format(
            #     self.isClass,
            #     self.attrs[self.realOrder.index('name')])

            code = code + agent[0].format(nodeName)

            print self.attrs[self.realOrder.index('hasActions')]

            for behav in self.attrs[self.realOrder.index('hasActions')]:
                # code = code + "\n{}\n".format(behav.getValue())
                code = code + behaviour.format(
                    behav.getValue(),
                    self.attrs[self.realOrder.index('name')],
                    self.isClass)

            code = code + agent[1].format(nodeName)

            file.write(code)
            file.close()

            print nodeName

            return nodeName

        # generate a file with all the Role behaviours
        if hasattr(self, 'isClass') and self.isClass in ['Role']:
            behaviour = """
class {0}(spade.Behaviour.OneShotBehaviour):
    '''Behaviour {0} of {2} {1}'''
    def _process(self):
        print '{1}: behaving {0}'
"""
            file = open('./Code/RoleBehaviours.py', 'a')

            for behav in self.attrs[self.realOrder.index('hasActions')]:
                file.write(behaviour.format(
                    behav.getValue(),
                    self.attrs[self.realOrder.index('name')],
                    self.isClass))

            file.close()


class GenerateAgentSPADE():
    """Class used for generating SPADE agent code"""
    def __init__(self, name, behavs=None, KB=None):
        self.name = name
        self.behavs = behavs
        self.KB = KB

        # templates for agents and behaviours
        self.agent = [
"""
class {0}(spade.Agent.Agent):
'''Bare skeleton for agent type {0}'''""",
"""
    def _setup(self):
        print '{0}: running'"""]
        self.behaviour = """
    class {0}(spade.Behaviour.OneShotBehaviour):
        '''Behaviour {0} of {2} {1}'''
        def _process(self):
            print '{1}: behaving {0}'"""

    def generateCode(self):
        # beginning of generated code
        code = ["import spade\nfrom RoleBehaviours import *\n"]

        # generate agent initialisation
        code.append(self.agent[0].format(self.name))

        if self.behavs:
            # generate agent behaviours
            for b in self.behavs:
                code.append(self.behaviour.format(b, self.name, "Agent"))

        code.append(self.agent[1].format(self.name))

        if self.behavs:
            for b in self.behavs:
                code.append("""
        self.addBehaviour(self.{}(), None)""".format(b))

        code.append("""
        self.configureKB('SWI', None, 'swipl')""")

        if self.KB:
            for x in self.KB:
                code.append("""
        self.addBelieve('{0[1]}({0[0]},{0[2]})')""".format(x))

        filename = "./Code/{}.py".format(self.name)

        if os.path.isfile(filename):
            os.rename(filename, '{}.old'.format(filename))

        file = open(filename, 'w')

        file.write("\n".join(code))
        file.close()

        return self.name
