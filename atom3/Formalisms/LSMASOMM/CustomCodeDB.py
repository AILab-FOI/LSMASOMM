import persistent


class savedNode(persistent.Persistent):
    """This is a class containing all the data specifying a Node in a specific ASG"""

    def __init__(self, coreAttrs):
        """Initialise the savedNode object with values for all the default attributes."""
        for attr in coreAttrs:
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

    def saveAttributes(self, attrs, values):
        """Save custom attributes of the Node."""
        self.realOrder = attrs
        self.attrVals = values

    def generateCode(self):
        """Generate code for the Node."""
        if self.isClass in ['Role', 'OrgUnit']:
            # store elements for code generating
            elements = {}

            # beginning of generated code
            code = 'import spade \n'

            # templates for agents ang behaviours
            agent = [
"""
class {0}(spade.Agent.Agent):
    '''Bear skeleton for agent type {0}'''
""",
"""
    def _setup(self):
        print '{0}: running'
"""]

            behaviour = """
    class {0}(spade.Behaviour.OneShotBehaviour):
        '''Bare skeleton for behaviour {0}'''
        def _process(self):
            print '{0}: behaving'
"""
            nodeName = "{}{}".format(self.isClass, self.objectNumber)
            fileName = "./Code/{}{}.txt".format(nodeName)
            # fileName = "./Code/{}{}{}.txt".format(self.isClass, self.objectNumber, self.attrVals[self.realOrder.index('name')])
            file = open(fileName, 'w')

            nodeName = "{}{}".format(
                self.isClass, self.attrVals[self.realOrder.index('name')])
            code = code + agent[0].format(nodeName)

            for attr in self.attrVals[self.realOrder.index('actions')]:
                pass
            file.close()
