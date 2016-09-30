from graph_ASG_ERmetaMetaModel import *
from stickylink import *
from widthXfillXdecoration import *
from ASG_ERmetaMetaModel import *
from ERentity import *
from ERrelationship import *
from ASG_ERmetaMetaModel import *
from ImageText import *
from ATOM3Integer import *
from ATOM3Appearance import *
from ATOM3Float import *
from ATOM3Link import *
from ATOM3Boolean import *
from ATOM3List import *
from ATOM3Enum import *
from ATOM3Attribute import *
from ATOM3Constraint import *
from ATOM3String import *
from ATOM3BottomType import *

def Buttons_Model(self, rootNode):
    rootNode.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Formalism_Name', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('RowSize', 'Integer', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3Integer(0)
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Formalism_File', 'String', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3String('')
    lcobj1.append(cobj1)
    rootNode.attributes.setValue(lcobj1)
    rootNode.name.setValue('Buttons')
    rootNode.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    rootNode.constraints.setValue(lcobj1)
    rootNode.graphClass_= graph_ASG_ERmetaMetaModel

    self.globalPrecondition()

    self.obj18=ERentity(self)

    self.obj18.constraints.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    self.obj18.constraints.setValue(lcobj1)
    self.obj18.name.setValue('ButtonConfig')
    self.obj18.appearance.setValue( ('ButtonConfig', self.obj18))
    self.obj18.attributes.setActionFlags([ 1, 1, 1, 0])
    lcobj1 =[]
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Contents', 'ImageText', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue= TextUImage()
    cobj1.initialValue.Text=ATOM3String('')
    cobj1.initialValue.Image=ATOM3String('')
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Action', 'Constraint', None, ('Key', 0), ('Direct Editing', 0)))
    cobj1.initialValue=ATOM3Constraint()
    cobj1.initialValue.setValue(('Action', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE OBJECT'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '# The parameters of this method are:\n#   - wherex\n#   - wherey\n\n'))
    lcobj1.append(cobj1)
    cobj1=ATOM3Attribute(self.types)
    cobj1.setValue(('Drawing_Mode', 'Boolean', None, ('Key', 0), ('Direct Editing', 1)))
    cobj1.initialValue=ATOM3Boolean()
    cobj1.initialValue.setValue((' ', 1))
    cobj1.initialValue.config = 1
    lcobj1.append(cobj1)
    self.obj18.attributes.setValue(lcobj1)
    self.obj18.graphClass_= graph_ERentity
    from graph_ERentity import *
    new_obj = graph_ERentity(79.0,234.0,self.obj18)
    new_obj.DrawObject(self.UMLmodel)
    self.UMLmodel.addtag_withtag("ERentity", new_obj.tag)
    self.obj18.graphObject_ = new_obj
    rootNode.addNode(self.obj18)
    self.globalAndLocalPostcondition(self.obj18)
    self.drawConnections( )

newfunction = Buttons_Model

loadedTypes = [('ImageText', 'ImageText', (), 1)]
loadedMMName = 'EntityRelationship'
