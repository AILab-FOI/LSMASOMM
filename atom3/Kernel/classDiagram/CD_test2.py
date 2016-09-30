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

def CD_test2(self, rootNode):
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

    self.obj27=AtomClass(self)

    self.obj27.ClassName.setValue('MyClass0')
    self.obj27.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('a', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('b', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Boolean()
    cobj2.initialValue.setValue((None, 0))
    cobj2.initialValue.config = 1
    lcobj2.append(cobj2)
    self.obj27.ClassAttributes.setValue(lcobj2)
    self.obj27.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj27.ClassConstraints.setValue(lcobj2)
    self.obj27.ClassAppearance.setValue( ('MyClass0', self.obj27))
    self.obj27.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MyAssociation0', (['Source', 'Destination'], 0), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj27.ClassCardinality.setValue(lcobj2)
    self.obj27.graphClass_= graph_AtomClass
    if self.genGraphics:
       from graph_AtomClass import *
       new_obj = graph_AtomClass(61.0,40.0,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("AtomClass", new_obj.tag)
    else: new_obj = None
    self.obj27.graphObject_ = new_obj
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)

    self.globalPrecondition( rootNode )

    self.obj28=AtomClass(self)

    self.obj28.ClassName.setValue('MyClass1')
    self.obj28.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('c', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    self.obj28.ClassAttributes.setValue(lcobj2)
    self.obj28.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj28.ClassConstraints.setValue(lcobj2)
    self.obj28.ClassAppearance.setValue( ('MyClass1', self.obj28))
    self.obj28.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj28.ClassCardinality.setValue(lcobj2)
    self.obj28.graphClass_= graph_AtomClass
    if self.genGraphics:
       from graph_AtomClass import *
       new_obj = graph_AtomClass(83.0,264.0,self.obj28)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("AtomClass", new_obj.tag)
    else: new_obj = None
    self.obj28.graphObject_ = new_obj
    rootNode.addNode(self.obj28)
    self.globalAndLocalPostcondition(self.obj28, rootNode)

    self.globalPrecondition( rootNode )

    self.obj29=AtomClass(self)

    self.obj29.ClassName.setValue('MyClass2')
    self.obj29.ClassAttributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj29.ClassAttributes.setValue(lcobj2)
    self.obj29.ClassConstraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj29.ClassConstraints.setValue(lcobj2)
    self.obj29.ClassAppearance.setValue( ('MyClass2', self.obj29))
    self.obj29.ClassCardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MyAssociation0', (['Source', 'Destination'], 1), '0', 'N'))
    lcobj2.append(cobj2)
    self.obj29.ClassCardinality.setValue(lcobj2)
    self.obj29.graphClass_= graph_AtomClass
    if self.genGraphics:
       from graph_AtomClass import *
       new_obj = graph_AtomClass(293.0,43.0,self.obj29)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("AtomClass", new_obj.tag)
    else: new_obj = None
    self.obj29.graphObject_ = new_obj
    rootNode.addNode(self.obj29)
    self.globalAndLocalPostcondition(self.obj29, rootNode)

    self.globalPrecondition( rootNode )

    self.obj30=AtomInheritance(self)

    self.obj30.graphClass_= graph_AtomInheritance
    if self.genGraphics:
       from graph_AtomInheritance import *
       new_obj = graph_AtomInheritance(165.0,234.5,self.obj30)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("AtomInheritance", new_obj.tag)
    else: new_obj = None
    self.obj30.graphObject_ = new_obj
    rootNode.addNode(self.obj30)
    self.globalAndLocalPostcondition(self.obj30, rootNode)

    self.globalPrecondition( rootNode )

    self.obj31=AtomAssociation(self)

    self.obj31.AssociationCardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('MyClass0', (['Source', 'Destination'], 1), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('MyClass2', (['Source', 'Destination'], 0), '1', '1'))
    lcobj2.append(cobj2)
    self.obj31.AssociationCardinality.setValue(lcobj2)
    self.obj31.AssociationName.setValue('MyAssociation0')
    self.obj31.AssociationAppearance.setValue( ('None', self.obj31))
    self.obj31.AssociationAppearance.linkInfo=linkEditor(self,self.obj31.AssociationAppearance.semObject, "Class_information_not_available")
    self.obj31.AssociationAppearance.linkInfo.FirstLink= stickylink()
    self.obj31.AssociationAppearance.linkInfo.FirstLink.arrow=ATOM3Boolean()
    self.obj31.AssociationAppearance.linkInfo.FirstLink.arrow.setValue((' ', 0))
    self.obj31.AssociationAppearance.linkInfo.FirstLink.arrow.config = 0
    self.obj31.AssociationAppearance.linkInfo.FirstLink.arrowShape1=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.FirstLink.arrowShape2=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.FirstLink.arrowShape3=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.FirstLink.decoration=ATOM3Appearance()
    self.obj31.AssociationAppearance.linkInfo.FirstLink.decoration.setValue( ('Class_information_not_available_1stLink', self.obj31.AssociationAppearance.linkInfo.FirstLink))
    self.obj31.AssociationAppearance.linkInfo.FirstSegment= widthXfillXdecoration()
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.width=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.fill=ATOM3String('black')
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.stipple=ATOM3String('')
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.arrow=ATOM3Boolean()
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.arrow.setValue((' ', 0))
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.arrow.config = 0
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.arrowShape1=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.arrowShape2=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.arrowShape3=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.decoration=ATOM3Appearance()
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.decoration.setValue( ('Class_information_not_available_1stSegment', self.obj31.AssociationAppearance.linkInfo.FirstSegment))
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj31.AssociationAppearance.linkInfo.Center=ATOM3Appearance()
    self.obj31.AssociationAppearance.linkInfo.Center.setValue( ('Class_information_not_available_Center', self.obj31.AssociationAppearance.linkInfo))
    self.obj31.AssociationAppearance.linkInfo.SecondSegment= widthXfillXdecoration()
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.width=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.fill=ATOM3String('black')
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.stipple=ATOM3String('')
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.arrow=ATOM3Boolean()
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.arrow.setValue((' ', 0))
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.arrow.config = 0
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.arrowShape1=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.arrowShape2=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.arrowShape3=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.decoration=ATOM3Appearance()
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.decoration.setValue( ('Class_information_not_available_2ndSegment', self.obj31.AssociationAppearance.linkInfo.SecondSegment))
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
    self.obj31.AssociationAppearance.linkInfo.SecondLink= stickylink()
    self.obj31.AssociationAppearance.linkInfo.SecondLink.arrow=ATOM3Boolean()
    self.obj31.AssociationAppearance.linkInfo.SecondLink.arrow.setValue((' ', 0))
    self.obj31.AssociationAppearance.linkInfo.SecondLink.arrow.config = 0
    self.obj31.AssociationAppearance.linkInfo.SecondLink.arrowShape1=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.SecondLink.arrowShape2=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.SecondLink.arrowShape3=ATOM3Integer(0)
    self.obj31.AssociationAppearance.linkInfo.SecondLink.decoration=ATOM3Appearance()
    self.obj31.AssociationAppearance.linkInfo.SecondLink.decoration.setValue( ('Class_information_not_available_2ndLink', self.obj31.AssociationAppearance.linkInfo.SecondLink))
    self.obj31.AssociationAppearance.linkInfo.FirstLink.decoration.semObject=self.obj31.AssociationAppearance.semObject
    self.obj31.AssociationAppearance.linkInfo.FirstSegment.decoration.semObject=self.obj31.AssociationAppearance.semObject
    self.obj31.AssociationAppearance.linkInfo.Center.semObject=self.obj31.AssociationAppearance.semObject
    self.obj31.AssociationAppearance.linkInfo.SecondSegment.decoration.semObject=self.obj31.AssociationAppearance.semObject
    self.obj31.AssociationAppearance.linkInfo.SecondLink.decoration.semObject=self.obj31.AssociationAppearance.semObject
    self.obj31.AssociationConstraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj31.AssociationConstraints.setValue(lcobj2)
    self.obj31.graphClass_= graph_AtomAssociation
    if self.genGraphics:
       from graph_AtomAssociation import *
       new_obj = graph_AtomAssociation(249.0,108.5,self.obj31)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("AtomAssociation", new_obj.tag)
    else: new_obj = None
    self.obj31.graphObject_ = new_obj
    rootNode.addNode(self.obj31)
    self.globalAndLocalPostcondition(self.obj31, rootNode)
    self.drawConnections((self.obj27,self.obj31,[203.0, 118.0, 249.0, 108.5], 0, 2), (self.obj28,self.obj30,[157.0, 267.0, 165.0, 234.5], 0, 2), (self.obj30,self.obj27,[165.0, 234.5, 179.0, 171.0], 0, 2), (self.obj31,self.obj29,[249.0, 108.5, 298.0, 123.0], 0, 2) )

newfunction = CD_test2

loadedMMName = 'ClassDiagrams'
