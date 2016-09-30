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

def GraphicalObjects_ER_mdl(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.attributes.setValue(lcobj1)
    rootNode.name.setValue('ATOM3GraphicalObjects')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.constraints.setValue(lcobj1)
    rootNode.graphClass_= graph_ASG_ERmetaMetaModel

    self.globalPrecondition( rootNode )

    self.obj21=ERentity(self)

    self.obj21.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('width', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('fill', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('stipple', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('arrow', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('arrowshape', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('capstyle', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('joinstyle', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('smooth', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('splinesteps', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    lcobj2.append(cobj2)
    self.obj21.attributes.setValue(lcobj2)
    self.obj21.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj21.cardinality.setValue(lcobj2)
    self.obj21.appearance.setValue( ('line', self.obj21))
    self.obj21.name.setValue('line')
    self.obj21.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj21.constraints.setValue(lcobj2)
    self.obj21.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(285.75,20.7166666667,self.obj21)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.2400000000000002]
    else: new_obj = None
    self.obj21.graphObject_ = new_obj
    rootNode.addNode(self.obj21)
    self.globalAndLocalPostcondition(self.obj21, rootNode)

    self.globalPrecondition( rootNode )

    self.obj22=ERentity(self)

    self.obj22.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('fill', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('stipple', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('outline', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('width', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    lcobj2.append(cobj2)
    self.obj22.attributes.setValue(lcobj2)
    self.obj22.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj22.cardinality.setValue(lcobj2)
    self.obj22.appearance.setValue( ('oval', self.obj22))
    self.obj22.name.setValue('oval')
    self.obj22.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj22.constraints.setValue(lcobj2)
    self.obj22.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(505.75,180.716666667,self.obj22)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.2400000000000002]
    else: new_obj = None
    self.obj22.graphObject_ = new_obj
    rootNode.addNode(self.obj22)
    self.globalAndLocalPostcondition(self.obj22, rootNode)

    self.globalPrecondition( rootNode )

    self.obj23=ERentity(self)

    self.obj23.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('fill', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('stipple', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('outline', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('width', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('smooth', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('splinesteps', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    lcobj2.append(cobj2)
    self.obj23.attributes.setValue(lcobj2)
    self.obj23.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj23.cardinality.setValue(lcobj2)
    self.obj23.appearance.setValue( ('polygon', self.obj23))
    self.obj23.name.setValue('polygon')
    self.obj23.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj23.constraints.setValue(lcobj2)
    self.obj23.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(505.75,20.7166666667,self.obj23)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.2400000000000002]
    else: new_obj = None
    self.obj23.graphObject_ = new_obj
    rootNode.addNode(self.obj23)
    self.globalAndLocalPostcondition(self.obj23, rootNode)

    self.globalPrecondition( rootNode )

    self.obj24=ERentity(self)

    self.obj24.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('fill', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('outline', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('stipple', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('width', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    lcobj2.append(cobj2)
    self.obj24.attributes.setValue(lcobj2)
    self.obj24.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj24.cardinality.setValue(lcobj2)
    self.obj24.appearance.setValue( ('rectangle', self.obj24))
    self.obj24.name.setValue('rectangle')
    self.obj24.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj24.constraints.setValue(lcobj2)
    self.obj24.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(285.75,180.716666667,self.obj24)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.2400000000000002]
    else: new_obj = None
    self.obj24.graphObject_ = new_obj
    rootNode.addNode(self.obj24)
    self.globalAndLocalPostcondition(self.obj24, rootNode)

    self.globalPrecondition( rootNode )

    self.obj25=ERentity(self)

    self.obj25.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('anchor', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('fill', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('font', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('justify', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('stipple', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('text', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('')
    lcobj2.append(cobj2)
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('width', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3Integer(0)
    lcobj2.append(cobj2)
    self.obj25.attributes.setValue(lcobj2)
    self.obj25.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj25.cardinality.setValue(lcobj2)
    self.obj25.appearance.setValue( ('text', self.obj25))
    self.obj25.name.setValue('text')
    self.obj25.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj25.constraints.setValue(lcobj2)
    self.obj25.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(285.75,340.716666667,self.obj25)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.2400000000000002]
    else: new_obj = None
    self.obj25.graphObject_ = new_obj
    rootNode.addNode(self.obj25)
    self.globalAndLocalPostcondition(self.obj25, rootNode)

    self.globalPrecondition( rootNode )

    self.obj26=ERentity(self)

    self.obj26.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('c')
    lcobj2.append(cobj2)
    self.obj26.attributes.setValue(lcobj2)
    self.obj26.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj26.cardinality.setValue(lcobj2)
    self.obj26.appearance.setValue( ('connector', self.obj26))
    self.obj26.name.setValue('connector')
    self.obj26.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj26.constraints.setValue(lcobj2)
    self.obj26.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(65.75,20.7166666667,self.obj26)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.2400000000000002]
    else: new_obj = None
    self.obj26.graphObject_ = new_obj
    rootNode.addNode(self.obj26)
    self.globalAndLocalPostcondition(self.obj26, rootNode)

    self.globalPrecondition( rootNode )

    self.obj27=ERentity(self)

    self.obj27.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    cobj2=ATOM3Attribute(self.types)
    cobj2.setValue(('name', 'String', None, ('Key', 1), ('Direct Editing', 1)))
    cobj2.initialValue=ATOM3String('i')
    lcobj2.append(cobj2)
    self.obj27.attributes.setValue(lcobj2)
    self.obj27.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj2 =[]
    self.obj27.cardinality.setValue(lcobj2)
    self.obj27.appearance.setValue( ('image', self.obj27))
    self.obj27.name.setValue('image')
    self.obj27.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj2 =[]
    self.obj27.constraints.setValue(lcobj2)
    self.obj27.graphClass_= graph_ERentity
    if self.genGraphics:
       new_obj = graph_ERentity(65.75,180.716666667,self.obj27)
       new_obj.DrawObject(self.UMLmodel)
       self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
       new_obj.layConstraints = dict() # Graphical Layout Constraints 
       new_obj.layConstraints['scale'] = [1.0, 1.2400000000000002]
    else: new_obj = None
    self.obj27.graphObject_ = new_obj
    rootNode.addNode(self.obj27)
    self.globalAndLocalPostcondition(self.obj27, rootNode)
    self.drawConnections( )

newfunction = GraphicalObjects_ER_mdl

loadedMMName = 'EntityRelationship'
