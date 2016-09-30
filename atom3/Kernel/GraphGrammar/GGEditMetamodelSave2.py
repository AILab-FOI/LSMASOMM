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

def GGEditMetamodelSave2(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj0 =[]
    rootNode.attributes.setValue(lcobj0)
    rootNode.name.setValue('GGEditMetaModel2')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj0 =[]
    rootNode.constraints.setValue(lcobj0)
    rootNode.graphClass_= graph_ASG_UMLmetaMetaModel

    obj3=UMLclass(self)

    obj3.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj0 =[]
    obj3.constraints.setValue(lcobj0)
    obj3.name.setValue('GraphGrammarEdit')
    obj3.appearance.setValue(('GraphGrammarEdit',))
    obj3.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj0 =[]
    cobj0=ATOM3Attribute(self.types)
    cobj0.setValue(('Name', 'String', None, 1, 1))
    cobj0.initialValue=ATOM3String('')
    lcobj0.append(cobj0)
    cobj0=ATOM3Attribute(self.types)
    cobj0.setValue(('Rules', 'List', None, 0, 1))
    cobj0.initialValue=ATOM3List([ 1, 1, 1, self.types],ATOM3Attribute,self.types )
    lcobj1=[]
    cobj0.initialValue.setValue(lcobj1)
    lcobj0.append(cobj0)
    cobj0=ATOM3Attribute(self.types)
    cobj0.setValue(('InitialAction', 'Constraint', None, 0, 0))
    cobj0.initialValue=ATOM3Constraint()
    cobj0.initialValue.setValue(('constraint', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), None))
    lcobj0.append(cobj0)
    cobj0=ATOM3Attribute(self.types)
    cobj0.setValue(('FinalAction', 'Constraint', None, 0, 0))
    cobj0.initialValue=ATOM3Constraint()
    cobj0.initialValue.setValue(('const', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), 'hola caracola\nque\npasa\n\n\n\n'))
    lcobj0.append(cobj0)
    obj3.attributes.setValue(lcobj0)
    obj3.graphClass_= graph_UMLclass
    new_obj = graph_UMLclass(60,99,obj3)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("UMLclass", new_obj.tag)
    obj3.graphObject_ = new_obj
    rootNode.addNode(obj3)
def mainGGEditMetamodelSave2(self):
    self.ASGroot = ASG_UMLmetaMetaModel(self)
    self.GGEditMetamodelSave2(self, self.ASGroot)

newfunction = mainGGEditMetamodelSave2

