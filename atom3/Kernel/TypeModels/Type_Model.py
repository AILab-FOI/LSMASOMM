from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_ERmetaMetaModel import *
from ERentity import *
from ERrelationship import *
from ASG_ERmetaMetaModel import *
from ATOM3BottomType import *
from ATOM3String import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Enum import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Link import *
from ATOM3Integer import *
from ATOM3List import *
from ATOM3Port import *

def Type_Model(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Author', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Comments', 'String', None, ('Key', 0), ('Direct Editing', 0)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    rootNode.attributes.setValue(lcobj1)
    rootNode.name.setValue('TypesMetaModel')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.constraints.setValue(lcobj1)
    rootNode.graphClass_= graph_ASG_ERmetaMetaModel

    self.globalPrecondition( rootNode )

    self.obj20=ERentity(self)

    self.obj20.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('typename')
    lcobj1.append(cobj1)
    self.obj20.attributes.setValue(lcobj1)
    self.obj20.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj1 =[]
    cobj1=ATOM3Connection()
    cobj1.setValue(('Operator', (('Source', 'Destination'), 0), '1', '1'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('Operator', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj1.append(cobj1)
    self.obj20.cardinality.setValue(lcobj1)
    self.obj20.appearance.setValue( ('TypeName', self.obj20))
    self.obj20.name.setValue('TypeName')
    self.obj20.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Constraint()
    cobj1.setValue(('validName', (['Python', 'OCL'], 0), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'import string\nvname = self.Name.getValue()\n# check if we have a name\nif (not vname) or (vname == ""):                 # the name is mandatory\n   return "Entity name must be specified", ""\n# now check that the name is valid (a variable name)\nif string.count(vname, " ") > 0:\n   return "Invalid entity name, no white spaces allowed",""\n# check first character\nif (vname[0] >= \'0\') and (vname[0] <= \'9\'):              # a number\n   return "Invalid variable name, first character must be a letter or \'_\'",""\nif vname[0] != \'_\' and (vname[0]<\'A\' or vname[0]>\'z\'):\n   return "Invalid entity name, first character must be a letter or \'_\'",""\n# now check for the rest of not allowed characters...\nfor c in range(len(vname)-1):\n if vname[c+1] < \'A\' or vname[c+1] > \'z\':              # not a letter\n  if vname[c+1] < \'0\' or vname[c+1] > \'9\':           # not a number\n   if vname[c+1] != \'_\':                                # not underscore\n    return "Invalid entity name, character \'"+vname[c+1]+"\' is not allowed",""\n\n\n\n'))
    lcobj1.append(cobj1)
    self.obj20.constraints.setValue(lcobj1)
    self.obj20.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(112.0,61.0,self.obj20)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj20.graphObject_ = new_obj
    rootNode.addNode(self.obj20)
    self.globalAndLocalPostcondition(self.obj20, rootNode)

    self.globalPrecondition( rootNode )

    self.obj21=ERentity(self)

    self.obj21.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Type', 'Attribute', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3Attribute(self.types)
    cobj1.initialValue.setValue(('ltypename', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('TypeConstraint', 'Constraint', None, ('Key', 0), ('Direct Editing', 0)))
    cobj1.initialValue=ATOM3Constraint()
    cobj1.initialValue.setValue(('typeConst', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n\n'))
    lcobj1.append(cobj1)
    self.obj21.attributes.setValue(lcobj1)
    self.obj21.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj1 =[]
    cobj1=ATOM3Connection()
    cobj1.setValue(('Operator', (('Source', 'Destination'), 1), '1', '1'))
    lcobj1.append(cobj1)
    self.obj21.cardinality.setValue(lcobj1)
    self.obj21.appearance.setValue( ('LeafType', self.obj21))
    self.obj21.name.setValue('LeafType')
    self.obj21.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    self.obj21.constraints.setValue(lcobj1)
    self.obj21.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(53.0,363.0,self.obj21)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj21.graphObject_ = new_obj
    rootNode.addNode(self.obj21)
    self.globalAndLocalPostcondition(self.obj21, rootNode)

    self.globalPrecondition( rootNode )

    self.obj22=ERentity(self)

    self.obj22.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('MetaModelName', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    self.obj22.attributes.setValue(lcobj1)
    self.obj22.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj1 =[]
    cobj1=ATOM3Connection()
    cobj1.setValue(('Operator', (('Source', 'Destination'), 1), '1', '1'))
    lcobj1.append(cobj1)
    self.obj22.cardinality.setValue(lcobj1)
    self.obj22.appearance.setValue( ('ModelType', self.obj22))
    self.obj22.name.setValue('ModelType')
    self.obj22.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    self.obj22.constraints.setValue(lcobj1)
    self.obj22.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(287.0,362.0,self.obj22)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj22.graphObject_ = new_obj
    rootNode.addNode(self.obj22)
    self.globalAndLocalPostcondition(self.obj22, rootNode)

    self.globalPrecondition( rootNode )

    self.obj23=ERrelationship(self)

    self.obj23.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('type', 'Enum', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3Enum(['X', 'U', '->'],0,1)
    cobj1.initialValue.configItems.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3String('X')
    lcobj2.append(cobj2)
    cobj2=ATOM3String('U')
    lcobj2.append(cobj2)
    cobj2=ATOM3String('->')
    lcobj2.append(cobj2)
    cobj1.initialValue.configItems.setValue(lcobj2)
    lcobj1.append(cobj1)
    self.obj23.attributes.setValue(lcobj1)
    self.obj23.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj1 =[]
    cobj1=ATOM3Connection()
    cobj1.setValue(('TypeName', (('Source', 'Destination'), 1), '0', '1'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('LeafType', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('TypeName', (('Source', 'Destination'), 0), '0', '1'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('Operator', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('Operator', (('Source', 'Destination'), 1), '0', 'N'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('ModelType', (('Source', 'Destination'), 0), '0', 'N'))
    lcobj1.append(cobj1)
    self.obj23.cardinality.setValue(lcobj1)
    self.obj23.appearance.setValue( ('Operator', self.obj23))
    self.obj23.appearance.linkInfo=linkEditor(self,self.obj23.appearance.semObject, "Operator")
    self.obj23.appearance.linkInfo.FirstLink= stickylink()
    self.obj23.appearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj23.appearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj23.appearance.linkInfo.FirstLink.arrow.config = 0
    self.obj23.appearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj23.appearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj23.appearance.linkInfo.FirstLink.decoration.setValue( ('Operator_1stLink', self.obj23.appearance.linkInfo.FirstLink))
    self.obj23.appearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj23.appearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj23.appearance.linkInfo.FirstSegment.fill=ATOM3String('darkgray')
    self.obj23.appearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj23.appearance.linkInfo.FirstSegment.decoration.setValue( ('Operator_1stSegment', self.obj23.appearance.linkInfo.FirstSegment))
    self.obj23.appearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj23.appearance.linkInfo.Center=ATOM3Appearance()
    self.obj23.appearance.linkInfo.Center.setValue( ('Operator_Center', self.obj23.appearance.linkInfo))
    self.obj23.appearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj23.appearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj23.appearance.linkInfo.SecondSegment.fill=ATOM3String('darkgray')
    self.obj23.appearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj23.appearance.linkInfo.SecondSegment.decoration.setValue( ('Operator_2ndSegment', self.obj23.appearance.linkInfo.SecondSegment))
    self.obj23.appearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj23.appearance.linkInfo.SecondLink= stickylink()
    self.obj23.appearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj23.appearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj23.appearance.linkInfo.SecondLink.arrow.config = 0
    self.obj23.appearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(6)
    self.obj23.appearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(10)
    self.obj23.appearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(6)
    self.obj23.appearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj23.appearance.linkInfo.SecondLink.decoration.setValue( ('Operator_2ndLink', self.obj23.appearance.linkInfo.SecondLink))
    self.obj23.appearance.linkInfo.FirstLink.decoration.semObject=self.obj23.appearance.semObject
    self.obj23.appearance.linkInfo.FirstSegment.decoration.semObject=self.obj23.appearance.semObject
    self.obj23.appearance.linkInfo.Center.semObject=self.obj23.appearance.semObject
    self.obj23.appearance.linkInfo.SecondSegment.decoration.semObject=self.obj23.appearance.semObject
    self.obj23.appearance.linkInfo.SecondLink.decoration.semObject=self.obj23.appearance.semObject
    self.obj23.name.setValue('Operator')
    self.obj23.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    self.obj23.constraints.setValue(lcobj1)
    self.obj23.graphClass_= graph_ERrelationship
    if self.genGraphics:
       from graph_ERrelationship import *
       new_obj = graph_ERrelationship(136.0,201.0,self.obj23)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    else: new_obj = None
    self.obj23.graphObject_ = new_obj
    rootNode.addNode(self.obj23)
    self.globalAndLocalPostcondition(self.obj23, rootNode)
    self.drawConnections((self.obj20,self.obj23,[184.0, 153.0, 184.0, 204.0], 0, 2), (self.obj23,self.obj21,[182.0, 289.0, 123.0, 364.0], 0, 2), (self.obj23,self.obj20,[139.0, 249.0, 39.0, 248.0, 40.0, 36.0, 183.0, 36.0, 182.0, 62.0], 0, 5), (self.obj23,self.obj23,[229.0, 249.0, 260.0, 226.0, 235.0, 193.0, 212.0, 178.0, 184.0, 204.0],"bezier", 3), (self.obj23,self.obj22,[229.0, 249.0, 309.0, 365.0], 0, 2) )

newfunction = Type_Model

loadedMMName = 'EntityRelationship'
