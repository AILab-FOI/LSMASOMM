from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_ClassDiagramB import *
from ASG_ClassDiagramB import *
from AtomClass import *
from AtomInheritance import *
from AtomAssociation import *
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

def CD_test1(self, rootNode):
    rootNode.Author.setValue('')
    rootNode.Description.setValue('\n')
    rootNode.Constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.Constraints.setValue(lcobj1)
    rootNode.ModelName.setValue('NewCD')
    rootNode.Attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.Attributes.setValue(lcobj1)

    self.globalPrecondition( rootNode )

    self.obj26=AtomClass(self)

    self.obj26.ClassName.setValue('FooClass1')
    self.obj26.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    self.obj26.ClassAttributes.setValue(lcobj2)
    self.obj26.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj26.ClassConstraints.setValue(lcobj2)
    self.obj26.ClassAppearance.setValue( ('FooClass1', self.obj26))
    self.obj26.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('FooConnector', (['Source', 'Destination'], 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj26.ClassCardinality.setValue(lcobj2)
    self.obj26.graphClass_= graph_AtomClass
    if self.genGraphics:
       from graph_AtomClass import *
       new_obj = graph_AtomClass(39.0,63.0,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("AtomClass", new_obj.tag)
    else: new_obj = None
    self.obj26.graphObject_ = new_obj
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)

    self.globalPrecondition( rootNode )

    self.obj29=AtomClass(self)

    self.obj29.ClassName.setValue('FooClass2')
    self.obj29.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj29.ClassAttributes.setValue(lcobj2)
    self.obj29.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj29.ClassConstraints.setValue(lcobj2)
    self.obj29.ClassAppearance.setValue( ('FooClass2', self.obj29))
    self.obj29.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('FooConnector', (['Source', 'Destination'], 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj29.ClassCardinality.setValue(lcobj2)
    self.obj29.graphClass_= graph_AtomClass
    if self.genGraphics:
       from graph_AtomClass import *
       new_obj = graph_AtomClass(312.0,52.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("AtomClass", new_obj.tag)
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)

    self.globalPrecondition( rootNode )

    self.obj32=AtomAssociation(self)

    self.obj32.AssociationCardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('FooClass1', (['Source', 'Destination'], 1), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('FooClass2', (['Source', 'Destination'], 0), '1', '1'))
    lcobj2.append(cobj2)
    self.obj32.AssociationCardinality.setValue(lcobj2)
    self.obj32.AssociationName.setValue('FooConnector')
    self.obj32.AssociationAppearance.setValue( ('None', self.obj32))
    self.obj32.AssociationAppearance.linkInfo=linkEditor(self,self.obj32.AssociationAppearance.semObject, "Class_information_not_available")
    self.obj32.AssociationAppearance.linkInfo.FirstLink= stickylink()
    self.obj32.AssociationAppearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj32.AssociationAppearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj32.AssociationAppearance.linkInfo.FirstLink.arrow.config = 0
    self.obj32.AssociationAppearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj32.AssociationAppearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj32.AssociationAppearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj32.AssociationAppearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj32.AssociationAppearance.linkInfo.FirstLink.decoration.setValue( ('Class_information_not_available_1stLink', self.obj32.AssociationAppearance.linkInfo.FirstLink))
    self.obj32.AssociationAppearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.width=ATOM3Integer(1)
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.fill=ATOM3String('black')
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.decoration.setValue( ('Class_information_not_available_1stSegment', self.obj32.AssociationAppearance.linkInfo.FirstSegment))
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj32.AssociationAppearance.linkInfo.Center=ATOM3Appearance()
    self.obj32.AssociationAppearance.linkInfo.Center.setValue( ('Class_information_not_available_Center', self.obj32.AssociationAppearance.linkInfo))
    self.obj32.AssociationAppearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.width=ATOM3Integer(1)
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.fill=ATOM3String('black')
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.decoration.setValue( ('Class_information_not_available_2ndSegment', self.obj32.AssociationAppearance.linkInfo.SecondSegment))
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj32.AssociationAppearance.linkInfo.SecondLink= stickylink()
    self.obj32.AssociationAppearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj32.AssociationAppearance.linkInfo.SecondLink.arrow.setValue((' ', 1))
    self.obj32.AssociationAppearance.linkInfo.SecondLink.arrow.config = 0
    self.obj32.AssociationAppearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(3)
    self.obj32.AssociationAppearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(5)
    self.obj32.AssociationAppearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(8)
    self.obj32.AssociationAppearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj32.AssociationAppearance.linkInfo.SecondLink.decoration.setValue( ('Class_information_not_available_2ndLink', self.obj32.AssociationAppearance.linkInfo.SecondLink))
    self.obj32.AssociationAppearance.linkInfo.FirstLink.decoration.semObject=self.obj32.AssociationAppearance.semObject
    self.obj32.AssociationAppearance.linkInfo.FirstSegment.decoration.semObject=self.obj32.AssociationAppearance.semObject
    self.obj32.AssociationAppearance.linkInfo.Center.semObject=self.obj32.AssociationAppearance.semObject
    self.obj32.AssociationAppearance.linkInfo.SecondSegment.decoration.semObject=self.obj32.AssociationAppearance.semObject
    self.obj32.AssociationAppearance.linkInfo.SecondLink.decoration.semObject=self.obj32.AssociationAppearance.semObject
    self.obj32.AssociationConstraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj32.AssociationConstraints.setValue(lcobj2)
    self.obj32.graphClass_= graph_AtomAssociation
    if self.genGraphics:
       from graph_AtomAssociation import *
       new_obj = graph_AtomAssociation(227.0,125.0,self.obj32)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("AtomAssociation", new_obj.tag)
    else: new_obj = None
    self.obj32.graphObject_ = new_obj
    rootNode.addNode(self.obj32)
    self.globalAndLocalPostcondition(self.obj32, rootNode)
    self.drawConnections((self.obj26,self.obj32,[181.0, 141.0, 227.0, 125.0], 0, 2), (self.obj32,self.obj29,[227.0, 125.0, 317.0, 132.0], 0, 2) )

newfunction = CD_test1

loadedMMName = 'ClassDiagramB'
