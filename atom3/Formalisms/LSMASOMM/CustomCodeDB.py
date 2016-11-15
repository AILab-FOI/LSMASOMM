import persistent


class savedNode(persistent.Persistent):
    """This is a class containing all the data specifying a Node in a specific ASG"""

    def __init__(self, coreAttrs):
        for attr in coreAttrs:
            self.graphClass_ = coreAttrs[0]
            # self.graphObject_ = coreAttrs[1]
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
        self.realOrder = attrs
        self.attrVals = values
