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

def ERex11(self, rootNode):

    res = self.ASGroot.preCondition(ASG.CREATE)
    if res:
       self.constraintViolation(res)
       self.mode=self.IDLEMODE
       return

    obj5=UMLrelationship(self)

    obj5.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj0 =[]
    obj5.constraints.setValue(lcobj0)
    obj5.name.setValue('relationship0')
    obj5.appearance.setValue(('relationship0',))
    obj5.cardinality.setActionFlags([ 0, 1, 0, 0])
    lcobj0 =[]
    cobj0=ATOM3Connection()
    cobj0.setValue(('entity0', (('FROM entity TO relationship', 'FROM relationship TO entity'), 0), '1', '1'))
    lcobj0.append(cobj0)
    obj5.cardinality.setValue(lcobj0)
    obj5.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj0 =[]
    obj5.attributes.setValue(lcobj0)
    obj5.graphClass_= graph_UMLrelationship
    new_obj = graph_UMLrelationship(200,239,obj5)
    obj5.graphObject_ = new_obj
    rootNode.addNode(obj5)

    res = self.ASGroot.postCondition(ASG.CREATE)
    if res:
       self.constraintViolation(res)
       self.mode=self.IDLEMODE
       return

    res = obj5.postCondition(ASG.CREATE)
    if res:
       self.constraintViolation(res)
       self.mode=self.IDLEMODE
       return
