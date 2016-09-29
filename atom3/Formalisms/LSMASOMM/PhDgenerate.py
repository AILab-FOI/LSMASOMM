def generateCode(atom3i):

    # Get the ASGroot for this formalism

    # Where QuickTut_META.py is the generated buttons model, it is in your
    # formalism directory
    ASGroot = atom3i.ASGroot.getASGbyName('QuickTut_META')

    # NOTE: you can use atom3i.ASGroot instead of ASGroot for multi-formalism
    # traversals

    # Traverse all nodes in the graph of this formalism only

    nodeTypeList = ASGroot.listNodes.keys()

    for nodeType in noedTypeList:

        nodeList = ASGroot.listNodes[nodeType]

        for node in nodeList:

            # Access the name attribute and get its value
            print node.name.getValue()

    # Traverse only the instances of the class QuickTurialClass

    for node in ASGroot.listNodes['QuickTutClass']:

        newValue = hash(node.name.getValue())  # Hash the string name

        node.number.setValue(newValue)  # Example of setting an integer value

        node.graphObject_.ModifyAttribute('number', newValue)  # Update the
        # visual icon

        # Access the number attribute and get its value
        print node.number.getValue()