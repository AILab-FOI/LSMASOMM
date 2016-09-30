from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_Buttons import *
from ASG_Buttons import *
from ButtonConfig import *
from ATOM3MSEnum import *
from ATOM3Port import *
from ATOM3Integer import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Link import *
from ATOM3Boolean import *
from ATOM3Connection import *
from ATOM3List import *
from ATOM3Enum import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Text import *

def ClassDiagramB(self, rootNode):
    rootNode.Formalism_Name.setValue('ClassDiagramB')
    rootNode.Formalism_File.setValue('classDiagrams_2/ClassDiagramB_MM.py')
    rootNode.RowSize.setValue(1)

    self.globalPrecondition( rootNode )

    self.obj26=ButtonConfig(self)

    self.obj26.Contents.Text.setValue('Class')
    self.obj26.Contents.Image.setValue('classDiagram/Class.gif')
    self.obj26.Contents.lastSelected= "Image"
    self.obj26.Drawing_Mode.setValue((' ', 1))
    self.obj26.Drawing_Mode.config = 0
    self.obj26.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAtomClass (self, wherex, wherey)\n'))
    self.obj26.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(10,10,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj26.graphObject_ = new_obj
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)

    self.globalPrecondition( rootNode )

    self.obj27=ButtonConfig(self)

    self.obj27.Contents.Text.setValue('Inheritance')
    self.obj27.Contents.Image.setValue('classDiagram/Inherits.gif')
    self.obj27.Contents.lastSelected= "Image"
    self.obj27.Drawing_Mode.setValue((' ', 1))
    self.obj27.Drawing_Mode.config = 0
    self.obj27.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAtomInheritance (self, wherex, wherey)\n'))
    self.obj27.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(135,10,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj27.graphObject_ = new_obj
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)

    self.globalPrecondition( rootNode )

    self.obj28=ButtonConfig(self)

    self.obj28.Contents.Text.setValue('Association')
    self.obj28.Contents.Image.setValue('classDiagram/Association.gif')
    self.obj28.Contents.lastSelected= "Image"
    self.obj28.Drawing_Mode.setValue((' ', 1))
    self.obj28.Drawing_Mode.config = 0
    self.obj28.Action.setValue(('ActionButton1', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# This method has as parameters:\n#   - wherex : X Position in window coordinates where the user clicked.\n#   - wherey : Y Position in window coordinates where the user clicked.\nnewPlace = self.createNewAtomAssociation (self, wherex, wherey)\n'))
    self.obj28.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(260,10,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)

    self.globalPrecondition( rootNode )

    self.obj29=ButtonConfig(self)

    self.obj29.Contents.Text.setValue('Generate Code')
    self.obj29.Contents.Image.setValue('classDiagram/genCode.gif')
    self.obj29.Contents.lastSelected= "Image"
    self.obj29.Drawing_Mode.setValue((' ', 0))
    self.obj29.Drawing_Mode.config = 0
    self.obj29.Action.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\nfrom CDCodeGeneratorHelper import *\nhasGraph = 0							# flag that indicates if we have a graphical attribute\ncardConstObjects = []\nif self.ASGroot.keyword_:\n       if self.console: self.console.appendText(\'Generating code for model \'+self.ASGroot.keyword_.toString())\nelse:\n       if self.console: self.console.appendText(\'Generating code for model.\')\n\ninheritance_rel = self.ASGroot.listNodes["AtomInheritance"]\ni = 0\nprint "inheritance_rel=", inheritance_rel\n\n# now go for each inheritance association...\nwhile len(inheritance_rel)>0:\n   inh = inheritance_rel[i]  				# get the ith inheritance relationship\n   print "inh=", inh\n   parent = inh.out_connections_[0]			# get parent & child of the relationship  \n   print "parent=", parent\n   child = inh.in_connections_[0]\n   print "child=", child\n   found = 0\n   for in_proc in parent.out_connections_:		# check that the parent does not have another class up\n        if in_proc in inheritance_rel: \n           found = 1\n           break   \n   if found == 1:\n      i = i+1\n      if (i>=len(inheritance_rel)-1): i = 0\n   else:\n      # add the attributes of the father to the child\n      child.addedAttrs = []\n      child.added_in_connections_ = []\n      child.added_out_connections_ = []\n      child.addedCardinalities = []\n      for attr in parent.ClassAttributes.getValue():\n         child_attr = attr.clone()\n         child.ClassAttributes.newItem(child_attr)\n         child.addedAttrs.append(child_attr)\n      child.added_in_connections_   = []+parent.in_connections_\n      child.added_out_connections_ = []+parent.out_connections_\n      for ic in child.added_in_connections_: child.in_connections_.append(ic)		## añadir tambien a ic.out_connections_\n      for oc in child.added_out_connections_: child.out_connections_.append(oc)		## añadir tambien a oc.in_connections_\n      # now add the Cardinalities to the list in the child...\n      for card in parent.ClassCardinality.getValue():\n         child_card = card.clone()\n         child.ClassCardinality.newItem(child_card)\n         child.addedCardinalities.append(child_card)\n\n      # now add the Cardinalities to the list in the in and out connections...\n      for ic in parent.in_connections_:\n         if ic.getTypeName() == "AtomAssociation":\n            cloneCardinality(ic, parent, child, 0)\n      for oc in parent.out_connections_:\n         if oc.getTypeName() == "AtomAssociation":\n            cloneCardinality(oc, parent, child, 1)\n      inheritance_rel.remove (inh)		## remove the relationship from the list\n\nfor nodeType in self.ASGroot.nodeTypes:				# for each node type\n   for UMLobject in self.ASGroot.listNodes[nodeType]:		# for each object of any type\n       self.genCodeFor (UMLobject, cardConstObjects)		# Generate code for this particular entity	              								# in cardConstObjects, we are storing the objects with cardinality constraints\n# see first if we have generative attributes...\nself.genASGCode(cardConstObjects)                                # generate code for the ASG node\nself.genButtons()                                                # generate the file for the syntax actions\n# now generate the file with the GUI model...\nself.genButtonsModel()\n\n# now delete the added attributes to the children\nfor child in self.ASGroot.listNodes["AtomClass"]:\n   if "addedAttrs" in child.__dict__.keys():\n      attribs = child.ClassAttributes.getValue()\n      print "removing from :::", attribs\n      for attr in child.addedAttrs:\n          attribs.remove(attr)\n      child.ClassAttributes.setValue(attribs)\n   # delete the added in_connections and out_connections\n   if "added_in_connections_" in child.__dict__.keys():\n      for ic in child.added_in_connections_: child.in_connections_.remove(ic)\n   if "added_out_connections_" in child.__dict__.keys():\n      for oc in child.added_out_connections_: child.out_connections_.remove(oc)\n   if "addedCardinalities" in child.__dict__.keys():\n      cards = child.ClassCardinality.getValue()\n      for card in child.addedCardinalities: cards.remove(card)\n      child.ClassCardinality.setValue(cards)\n\n# remove the extra cardinalities from Atom3Association\nfor assoc in self.ASGroot.listNodes["AtomAssociation"]:\n   if "addedCardinalities" in assoc.__dict__.keys():\n      cards = []+assoc.AssociationCardinality.getValue()\n      for card in assoc.addedCardinalities: \n          print "removing ", card.getValue()\n          cards.remove(card)\n      assoc.AssociationCardinality.setValue(cards)\n   if "added_in_connections_" in assoc.__dict__.keys():\n      for ic in assoc.added_in_connections_: assoc.in_connections_.remove(ic)\n   if "added_out_connections_" in assoc.__dict__.keys():\n      for oc in assoc.added_out_connections_: assoc.out_connections_.remove(oc)\n\n\n\n\n\n\n'))
    self.obj29.graphClass_= graph_ButtonConfig
    if self.genGraphics:
       from graph_ButtonConfig import *
       new_obj = graph_ButtonConfig(64.0,108.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ButtonConfig", new_obj.tag)
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.drawConnections( )

newfunction = ClassDiagramB

loadedMMName = 'Buttons'
