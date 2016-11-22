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

    def saveAttributes(self, order, attrValues):
        """Save custom attributes of the Node."""
        self.realOrder = order
        self.attrs = attrValues

        print self.attrs

    def generateCodeSPADE(self):
        """Generate code for the Node."""

        print "Generating stuff...", self.isClass

        # templates for agents ang behaviours
        agent = [
"""
class {0}(spade.Agent.Agent):
    '''Bear skeleton for agent type {0}'''17487
""",
"""
    def _setup(self):
        print '{0}: running'
        cR = ChangeRole() # doesn't have to be so...
        self.addBehaviour(cR, None)

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

            file = open("./Code/{}.txt".format(nodeName), 'w')

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
            file = open('./Code/RoleBehaviours.py', 'a')

            for behav in self.attrs[self.realOrder.index('hasActions')]:
                file.write(behaviour.format(
                    behav.getValue(),
                    self.attrs[self.realOrder.index('name')],
                    self.isClass))

            file.close()
