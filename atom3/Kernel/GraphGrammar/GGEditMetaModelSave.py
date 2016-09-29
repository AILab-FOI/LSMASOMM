from ASG_UMLmetaMetaModel import *
from UMLclass import *
from graph_UMLclass import *
from UMLrelationship import *
from graph_UMLrelationship import *
from ASG_UMLmetaMetaModel import *
from graph_ASG_UMLmetaMetaModel import *
from ATOM3Enum import *
from ATOM3List import *
from ATOM3Float import *
from ATOM3Integer import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *
from ATOM3Appearance import *

def GGEditMetaModelSave(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj0 =[]
    rootNode.attributes.setValue(lcobj0)
    rootNode.name.setValue('GGEditMetaModel')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj0 =[]
    rootNode.constraints.setValue(lcobj0)
    rootNode.graphClass_= graph_ASG_UMLmetaMetaModel

    obj2=UMLclass(self)

    obj2.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj0 =[]
    obj2.constraints.setValue(lcobj0)
    obj2.name.setValue('GGruleEdit')
    obj2.appearance.setValue(('GGruleEdit',))
    obj2.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj0 =[]
    cobj0=ATOM3Attribute(self.types)
    cobj0.setValue(('Name', 'String', None, 1, 1))
    cobj0.initialValue=ATOM3String('rule')
    lcobj0.append(cobj0)
    cobj0=ATOM3Attribute(self.types)
    cobj0.setValue(('Order', 'Integer', None, 0, 1))
    cobj0.initialValue=ATOM3Integer(1)
    lcobj0.append(cobj0)
    cobj0=ATOM3Attribute(self.types)
    cobj0.setValue(('LHS', 'String', None, 0, 0))
    cobj0.initialValue=ATOM3String('')
    lcobj0.append(cobj0)
    cobj0=ATOM3Attribute(self.types)
    cobj0.setValue(('RHS', 'String', None, 0, 0))
    cobj0.initialValue=ATOM3String('')
    lcobj0.append(cobj0)
    cobj0=ATOM3Attribute(self.types)
    cobj0.setValue(('Condition', 'Constraint', None, 0, 0))
    cobj0.initialValue=ATOM3Constraint()
    cobj0.initialValue.setValue('a : ')
    lcobj0.append(cobj0)
    cobj0=ATOM3Attribute(self.types)
    cobj0.setValue(('Action', 'Constraint', None, 0, 0))
    cobj0.initialValue=ATOM3Constraint()
    cobj0.initialValue.setValue('b : ')
    lcobj0.append(cobj0)
    obj2.attributes.setValue(lcobj0)
    obj2.graphClass_= graph_UMLclass
    new_obj = graph_UMLclass(51,125,obj2)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("UMLclass", new_obj.tag)
    obj2.graphObject_ = new_obj
    rootNode.addNode(obj2)
def mainGGEditMetaModelSave(self):
    self.ASGroot = ASG_UMLmetaMetaModel(self)
    self.GGEditMetaModelSave(self, self.ASGroot)

newfunction = mainGGEditMetaModelSave

