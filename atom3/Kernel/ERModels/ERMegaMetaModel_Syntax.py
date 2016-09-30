from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_ERmetaMetaModel import *
from ERentity import *
from ERrelationship import *
from ASG_ERmetaMetaModel import *
from ATOM3Enum import *
from ATOM3List import *
from ATOM3Float import *
from ATOM3Integer import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Link import *

def ERMegaMetaModel_Syntax(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.attributes.setValue(lcobj1)
    rootNode.name.setValue('ERModel')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.constraints.setValue(lcobj1)
    rootNode.graphClass_= graph_ASG_ERmetaMetaModel

    self.globalPrecondition( rootNode )

    self.obj21=ERentity(self)

    self.obj21.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    self.obj21.constraints.setValue(lcobj1)
    self.obj21.name.setValue('ERentity')
    self.obj21.appearance.setValue( ('ERentity', self.obj21))
    self.obj21.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj1 =[]
    cobj1=ATOM3Connection()
    cobj1.setValue(('ERrelationship', (('Source', 'Destination'), 0), '1', '1'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('ERrelationship', (('Source', 'Destination'), 1), '1', '1'))
    lcobj1.append(cobj1)
    self.obj21.cardinality.setValue(lcobj1)
    self.obj21.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('attributes', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
    lcobj2=[]
    cobj1.initialValue.setValue(lcobj2)
    lcobj1.append(cobj1)
    self.obj21.attributes.setValue(lcobj1)
    self.obj21.graphClass_= graph_ERentity
    if self.genGraphics:
       from graph_ERentity import *
       new_obj = graph_ERentity(107.0,273.0,self.obj21)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    else: new_obj = None
    self.obj21.graphObject_ = new_obj
    rootNode.addNode(self.obj21)
    self.globalAndLocalPostcondition(self.obj21, rootNode)

    self.globalPrecondition( rootNode )

    self.obj22=ERrelationship(self)

    self.obj22.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    self.obj22.constraints.setValue(lcobj1)
    self.obj22.name.setValue('ERrelationship')
    self.obj22.appearance.setValue( ('ERrelationship', self.obj22))
    self.obj22.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj1 =[]
    cobj1=ATOM3Connection()
    cobj1.setValue(('ERentity', (('Source', 'Destination'), 1), '1', '1'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Connection()
    cobj1.setValue(('ERentity', (('Source', 'Destination'), 0), '1', '1'))
    lcobj1.append(cobj1)
    self.obj22.cardinality.setValue(lcobj1)
    self.obj22.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    self.obj22.attributes.setValue(lcobj1)
    self.obj22.graphClass_= graph_ERrelationship
    if self.genGraphics:
       from graph_ERrelationship import *
       new_obj = graph_ERrelationship(275.0,141.0,self.obj22)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
    else: new_obj = None
    self.obj22.graphObject_ = new_obj
    rootNode.addNode(self.obj22)
    self.globalAndLocalPostcondition(self.obj22, rootNode)
    self.drawConnections((self.obj21,self.obj22,[257.0, 322.0, 278.0, 189.0], 0, 2), (self.obj22,self.obj21,[368.0, 189.0, 257.0, 322.0], 0, 2) )

newfunction = ERMegaMetaModel_Syntax

loadedMMName = 'EntityRelationship'
