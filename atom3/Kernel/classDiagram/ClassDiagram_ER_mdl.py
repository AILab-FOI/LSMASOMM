from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_ERmetaMetaModel import *
from ERentity import *
from ERrelationship import *
from ASG_ERmetaMetaModel import *
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

def ClassDiagram_ER_mdl(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('ModelName', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('NewCD')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Description', 'Text', None, ('Key', 0), ('Direct Editing', 0)))
    cobj1.initialValue=ATOM3Text('\n', 60,15 )
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Attributes', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
    lcobj2=[]
    cobj1.initialValue.setValue(lcobj2)
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Constraints', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Constraint)
    lcobj2=[]
    cobj1.initialValue.setValue(lcobj2)
    lcobj1.append(cobj1)
    rootNode.attributes.setValue(lcobj1)
    rootNode.name.setValue('ClassDiagramB')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.constraints.setValue(lcobj1)
    rootNode.graphClass_= graph_ASG_ERmetaMetaModel

    self.globalPrecondition( rootNode )

    self.obj27=ERentity(self)

    self.obj27.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('createCardinality', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), '#constraint that generates cardinality variables for the associated classes.  \nfor a in self.in_connections_:\n	if a.getTypeName() == \'AtomAssociation\':         \n		self_source=ATOM3Connection(a, \'1\', \'1\')\n		self_source.setValue((a,(["Source", "Destination"], 1),\'0\',\'N\'))\n		if not self_source in self.ClassCardinality.getValue():\n			self.ClassCardinality.newItem(self_source)\n\nfor a in self.out_connections_:\n	if a.getTypeName() == \'AtomAssociation\':         \n		self_source=ATOM3Connection(a, \'1\', \'1\')\n		self_source.setValue((a,(["Source", "Destination"], 0),\'0\',\'N\'))\n		if not self_source in self.ClassCardinality.getValue():\n			self.ClassCardinality.newItem(self_source)\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('deleteCardinality', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]), 'myname = self.ClassName.getValue()\nin_C = self.in_connections_\nout_C = self.out_connections_\n\nfor a in in_C:\n	for b in a.in_connections_:\n		b_card = b.ClassCardinality.getValue()\n		new_b_card = b_card\n		for c in b_card:\n			if c.getValue()[0] == myname:\n				new_b_card.remove(c)\n		b.ClassCardinality.setValue(new_b_card)\n\nfor a in out_C:\n	for b in a.out_connections_:\n		b_card = b.ClassCardinality.getValue()\n		new_b_card = b_card\n		for c in b_card:\n			if c.getValue()[0] == myname:\n				new_b_card.remove(c)\n		b.ClassCardinality.setValue(new_b_card)\n\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('storeKeyword', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.oldKeyword = self.keyword_.toString()\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('updateRelationships', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'for rel in self.in_connections_:\n   if rel.getTypeName() == "AtomAssociation":\n         cards = rel.AssociationCardinality.getValue()\n         print "in updateRelationships:::", cards\n         for card in cards:\n            name, direction, min, max = card.getValue()\n            if name == self.oldKeyword and direction[1] == 0:\n               card.setValue((self, None, None, None))\n               break\nfor rel in self.out_connections_:\n   if rel.getTypeName() == "AtomAssociation":\n         cards = rel.AssociationCardinality.getValue()\n         print "in updateRelationships:::", cards\n         for card in cards:\n            name, direction, min, max = card.getValue()\n            if name == self.oldKeyword and direction[1] == 1:\n               card.setValue((self, None, None, None))\n               break\n\n\n\n\n\n'))
    lcobj2.append(cobj2)
    self.obj27.constraints.setValue(lcobj2)
    self.obj27.name.setValue('AtomClass')
    self.obj27.appearance.setValue( ('AtomClass', self.obj27))
    self.obj27.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('AtomInheritance', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('AtomInheritance', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('AtomAssociation', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('AtomAssociation', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj27.cardinality.setValue(lcobj2)
    self.obj27.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ClassName', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('MyClass')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ClassCardinality', 'List', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3List([ 0, 1, 0, self.types],ATOM3Connection)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ClassAttributes', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ClassConstraints', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Constraint)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('ClassAppearance', 'Appearance', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Appearance()
    cobj2.initialValue.setValue( ('class0', None))
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('Abstract', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    self.obj27.attributes.setValue(lcobj2)
    self.obj27.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(179.0,195.0,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj27.graphObject_ = new_obj
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)

    self.globalPrecondition( rootNode )

    self.obj28=ERrelationship(self)

    self.obj28.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj28.constraints.setValue(lcobj2)
    self.obj28.name.setValue('AtomInheritance')
    self.obj28.appearance.setValue( ('AtomInheritance', self.obj28))
    self.obj28.appearance.linkInfo=linkEditor(self,self.obj28.appearance.semObject, "AtomInheritance")
    self.obj28.appearance.linkInfo.FirstLink= stickylink()
    self.obj28.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj28.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj28.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj28.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj28.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj28.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj28.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj28.appearance.linkInfo.FirstLink.decoration.setValue( ('AtomInheritance_1stLink', self.obj28.appearance.linkInfo.FirstLink))
    self.obj28.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj28.appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj28.appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
    self.obj28.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj28.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj28.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj28.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj28.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj28.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj28.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj28.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj28.appearance.linkInfo.FirstSegment.decoration.setValue( ('AtomInheritance_1stSegment', self.obj28.appearance.linkInfo.FirstSegment))
    self.obj28.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj28.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj28.appearance.linkInfo.Center.setValue( ('AtomInheritance_Center', self.obj28.appearance.linkInfo))
    self.obj28.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj28.appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj28.appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
    self.obj28.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj28.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj28.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj28.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj28.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj28.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj28.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj28.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj28.appearance.linkInfo.SecondSegment.decoration.setValue( ('AtomInheritance_2ndSegment', self.obj28.appearance.linkInfo.SecondSegment))
    self.obj28.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj28.appearance.linkInfo.SecondLink= stickylink()
    self.obj28.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj28.appearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
    self.obj28.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj28.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(9)
    self.obj28.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(9)
    self.obj28.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(9)
    self.obj28.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj28.appearance.linkInfo.SecondLink.decoration.setValue( ('AtomInheritance_2ndLink', self.obj28.appearance.linkInfo.SecondLink))
    self.obj28.appearance.linkInfo.FirstLink.decoration.semObject=self.obj28.appearance.semObject
    self.obj28.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj28.appearance.semObject
    self.obj28.appearance.linkInfo.Center.semObject=self.obj28.appearance.semObject
    self.obj28.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj28.appearance.semObject
    self.obj28.appearance.linkInfo.SecondLink.decoration.semObject=self.obj28.appearance.semObject
    self.obj28.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('AtomClass', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('AtomClass', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    self.obj28.cardinality.setValue(lcobj2)
    self.obj28.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj28.attributes.setValue(lcobj2)
    self.obj28.graphClass_= graph_ERrelationship
    if self.genGraphics:
       from graph_ERrelationship import *
       new_obj = graph_ERrelationship(204.0,349.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)

    self.globalPrecondition( rootNode )

    self.obj29=ERrelationship(self)

    self.obj29.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Constraint()
    cobj2.setValue(('createCardinality', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 'in_C = self.in_connections_\nout_C = self.out_connections_\n\nfor a in in_C:\n	if a.getTypeName() == \'AtomClass\':\n		#self.AssociationCardinality.newItem(ATOM3Connection(a, 1, 1))\n		source=ATOM3Connection(a, 1, 1)\n		source.setValue((a,(["Source", "Destination"], 1),\'1\',\'1\'))\n		if not source in self.AssociationCardinality.getValue():\n			self.AssociationCardinality.newItem(source)\n\nfor a in out_C:\n	if a.getTypeName() == \'AtomClass\':\n		#self.AssociationCardinality.newItem(ATOM3Connection(a, 1, 1))\n		source=ATOM3Connection(a, 1, 1)\n		source.setValue((a,(["Source", "Destination"], 0),\'1\',\'1\'))\n		if not source in self.AssociationCardinality.getValue():\n			self.AssociationCardinality.newItem(source)\n\n\n\n\n\n\n\n\n\n\n\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('storeKeyword', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 0), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'self.oldKeyword = self.keyword_.toString()\n\n'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Constraint()
    cobj2.setValue(('updateRelationships', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'for rel in self.in_connections_:\n    if rel.getTypeName() == "AtomClass":\n         cards = rel.ClassCardinality.getValue()\n         for card in cards:\n            name, direction, min, max = card.getValue()\n            if name == self.oldKeyword and direction[1] == 0:\n               card.setValue((self, None, None, None))\n               break\nfor rel in self.out_connections_:\n   if rel.getTypeName() == "AtomClass":\n         cards = rel.ClassCardinality.getValue()\n         for card in cards:\n            name, direction, min, max = card.getValue()\n            if name == self.oldKeyword and direction[1] == 1:\n               card.setValue((self, None, None, None))\n               break\n\n\n'))
    lcobj2.append(cobj2)
    self.obj29.constraints.setValue(lcobj2)
    self.obj29.name.setValue('AtomAssociation')
    self.obj29.appearance.setValue( ('AtomAssociation', self.obj29))
    self.obj29.appearance.linkInfo=linkEditor(self,self.obj29.appearance.semObject, "AtomAssociation")
    self.obj29.appearance.linkInfo.FirstLink= stickylink()
    self.obj29.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj29.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj29.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj29.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj29.appearance.linkInfo.FirstLink.decoration.setValue( ('AtomAssociation_1stLink', self.obj29.appearance.linkInfo.FirstLink))
    self.obj29.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj29.appearance.linkInfo.FirstSegment.width=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.FirstSegment.fill=ATOM3String('black')
    self.obj29.appearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj29.appearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj29.appearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj29.appearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj29.appearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj29.appearance.linkInfo.FirstSegment.decoration.setValue( ('AtomAssociation_1stSegment', self.obj29.appearance.linkInfo.FirstSegment))
    self.obj29.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj29.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj29.appearance.linkInfo.Center.setValue( ('AtomAssociation_Center', self.obj29.appearance.linkInfo))
    self.obj29.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj29.appearance.linkInfo.SecondSegment.width=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.SecondSegment.fill=ATOM3String('black')
    self.obj29.appearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj29.appearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj29.appearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj29.appearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj29.appearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj29.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj29.appearance.linkInfo.SecondSegment.decoration.setValue( ('AtomAssociation_2ndSegment', self.obj29.appearance.linkInfo.SecondSegment))
    self.obj29.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj29.appearance.linkInfo.SecondLink= stickylink()
    self.obj29.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj29.appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj29.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj29.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(3)
    self.obj29.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(6)
    self.obj29.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(8)
    self.obj29.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj29.appearance.linkInfo.SecondLink.decoration.setValue( ('AtomAssociation_2ndLink', self.obj29.appearance.linkInfo.SecondLink))
    self.obj29.appearance.linkInfo.FirstLink.decoration.semObject=self.obj29.appearance.semObject
    self.obj29.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj29.appearance.semObject
    self.obj29.appearance.linkInfo.Center.semObject=self.obj29.appearance.semObject
    self.obj29.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj29.appearance.semObject
    self.obj29.appearance.linkInfo.SecondLink.decoration.semObject=self.obj29.appearance.semObject
    self.obj29.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('AtomClass', (('Source', 'Destination'), 1), '1', 'N'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('AtomClass', (('Source', 'Destination'), 0), '1', 'N'))
    lcobj2.append(cobj2)
    self.obj29.cardinality.setValue(lcobj2)
    self.obj29.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('AssociationName', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('MyAssociation')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('AssociationCardinality', 'List', None, ('Key', 0), ('Direct Editing', 0)))
    cobj2.initialValue=ATOM3List([ 0, 1, 0, self.types],ATOM3Connection)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('AssociationConstraints', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Constraint)
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('AssociationAppearance', 'Link', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Link()
    cobj2.initialValue.setValue( ('None', None))
    cobj2.initialValue.linkInfo=linkEditor(self,cobj2.initialValue.semObject, "Class_information_not_available")
    cobj2.initialValue.linkInfo.FirstLink= stickylink()
    cobj2.initialValue.linkInfo.FirstLink.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.FirstLink.arrow.setValue((' ', 0))
    cobj2.initialValue.linkInfo.FirstLink.arrow.config = 0
    cobj2.initialValue.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.FirstLink.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.FirstLink.decoration.setValue( ('Class_information_not_available_1stLink', cobj2.initialValue.linkInfo.FirstLink))
    cobj2.initialValue.linkInfo.FirstSegment= widthXfillXdecoration()
    cobj2.initialValue.linkInfo.FirstSegment.width=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.FirstSegment.fill=ATOM3String('black')
    cobj2.initialValue.linkInfo.FirstSegment.stipple=ATOM3String('')
    cobj2.initialValue.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    cobj2.initialValue.linkInfo.FirstSegment.arrow.config = 0
    cobj2.initialValue.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.FirstSegment.decoration.setValue( ('Class_information_not_available_1stSegment', cobj2.initialValue.linkInfo.FirstSegment))
    cobj2.initialValue.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    cobj2.initialValue.linkInfo.Center=ATOM3Appearance()
    cobj2.initialValue.linkInfo.Center.setValue( ('Class_information_not_available_Center', cobj2.initialValue.linkInfo))
    cobj2.initialValue.linkInfo.SecondSegment= widthXfillXdecoration()
    cobj2.initialValue.linkInfo.SecondSegment.width=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.SecondSegment.fill=ATOM3String('black')
    cobj2.initialValue.linkInfo.SecondSegment.stipple=ATOM3String('')
    cobj2.initialValue.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    cobj2.initialValue.linkInfo.SecondSegment.arrow.config = 0
    cobj2.initialValue.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.SecondSegment.decoration.setValue( ('Class_information_not_available_2ndSegment', cobj2.initialValue.linkInfo.SecondSegment))
    cobj2.initialValue.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    cobj2.initialValue.linkInfo.SecondLink= stickylink()
    cobj2.initialValue.linkInfo.SecondLink.arrow=ATOM3Boolean()
    cobj2.initialValue.linkInfo.SecondLink.arrow.setValue((' ', 0))
    cobj2.initialValue.linkInfo.SecondLink.arrow.config = 0
    cobj2.initialValue.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
    cobj2.initialValue.linkInfo.SecondLink.decoration=ATOM3Appearance()
    cobj2.initialValue.linkInfo.SecondLink.decoration.setValue( ('Class_information_not_available_2ndLink', cobj2.initialValue.linkInfo.SecondLink))
    cobj2.initialValue.linkInfo.FirstLink.decoration.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.FirstSegment.decoration.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.Center.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.SecondSegment.decoration.semObject=cobj2.initialValue.semObject
    cobj2.initialValue.linkInfo.SecondLink.decoration.semObject=cobj2.initialValue.semObject
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('AssociationAttributes', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    self.obj29.attributes.setValue(lcobj2)
    self.obj29.graphClass_= graph_ERrelationship
    if self.genGraphics:
       from graph_ERrelationship import *
       new_obj = graph_ERrelationship(201.0,43.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)
    self.drawConnections((self.obj27,self.obj28,[203.0, 289.0, 203.0, 398.0, 207.0, 397.0], 0, 3), (self.obj27,self.obj29,[201.0, 198.0, 200.0, 90.0, 204.0, 91.0], 0, 3), (self.obj28,self.obj27,[297.0, 397.0, 302.0, 396.0, 301.0, 290.0], 0, 3), (self.obj29,self.obj27,[294.0, 91.0, 296.0, 92.0, 297.0, 198.0], 0, 3) )

newfunction = ClassDiagram_ER_mdl

loadedMMName = 'EntityRelationship'
