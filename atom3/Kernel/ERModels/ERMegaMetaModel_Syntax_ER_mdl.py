from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ERentity import *
from graph_ERentity import *
from ERrelationship import *
from graph_ERrelationship import *
from ASG_ERmetaMetaModel import *
from graph_ASG_ERmetaMetaModel import *
from ATOM3Enum import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Constraint import *
from ATOM3Attribute import *
from ATOM3Float import *
from ATOM3List import *
from ATOM3Link import *
from ATOM3Connection import *
from ATOM3Boolean import *
from ATOM3Appearance import *
from ATOM3Text import *
from ATOM3Integer import *
from ATOM3Port import *
from ATOM3MSEnum import *

def ERMegaMetaModel_Syntax_ER_mdl(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.attributes.setValue(lcobj1)
    rootNode.name.setValue('ERModel')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.constraints.setValue(lcobj1)
    rootNode.graphClass_= graph_ASG_ERmetaMetaModel

    self.globalPrecondition( rootNode )

    self.obj19=ERentity(self)

    self.obj19.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('attributes', 'List', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
    lcobj3=[]
    cobj2.initialValue.setValue(lcobj3)
    lcobj2.append(cobj2)
    self.obj19.attributes.setValue(lcobj2)
    self.obj19.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('ERrelationship', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('ERrelationship', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    self.obj19.cardinality.setValue(lcobj2)
    self.obj19.appearance.setValue( ('ERentity', self.obj19))
    self.obj19.name.setValue('ERentity')
    self.obj19.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj19.constraints.setValue(lcobj2)
    self.obj19.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(107.0,273.0,self.obj19)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.1400000000000001, 0.98999999999999999]
    else: new_obj = None
    self.obj19.graphObject_ = new_obj
    rootNode.addNode(self.obj19)
    self.globalAndLocalPostcondition(self.obj19, rootNode)

    self.globalPrecondition( rootNode )

    self.obj20=ERrelationship(self)

    self.obj20.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    self.obj20.attributes.setValue(lcobj2)
    self.obj20.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    cobj2=ATOM3Connection()
    cobj2.setValue(('ERentity', (('Source', 'Destination'), 1), '1', '1'))
    lcobj2.append(cobj2)
    cobj2=ATOM3Connection()
    cobj2.setValue(('ERentity', (('Source', 'Destination'), 0), '1', '1'))
    lcobj2.append(cobj2)
    self.obj20.cardinality.setValue(lcobj2)
    self.obj20.appearance.setValue( ('ERrelationship', self.obj20))
    self.obj20.name.setValue('ERrelationship')
    self.obj20.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj20.constraints.setValue(lcobj2)
    self.obj20.graphClass_= graph_ERrelationship
    if self.genGraphics:
       new_obj = graph_ERrelationship(208.0,144.0,self.obj20)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERrelationship", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
    else: new_obj = None
    self.obj20.graphObject_ = new_obj
    rootNode.addNode(self.obj20)
    self.globalAndLocalPostcondition(self.obj20, rootNode)
    self.drawConnections((self.obj19,self.obj20,[161.59999999999982, 282.39999999999998, 159.0, 144.0, 208.0, 144.0],"bezier", 3), (self.obj20,self.obj19,[208.0, 144.0, 254.0, 144.0, 252.79999999999995, 282.39999999999998],"bezier", 3) )

newfunction = ERMegaMetaModel_Syntax_ER_mdl

loadedMMName = 'EntityRelationship'
