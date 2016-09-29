"""
inheritanceCodeBase.py

By Denis Dube, Feb 2006
"""

import os
from string import replace as stringReplacer

class Magic:
  """
  Magic variables:
    If the class-diagram formalism is re-named, the following variables must 
    be changed accordingly. 
    Grouping them here should make that much less of chore :)
  """
  inheritanceClassName = 'CD_Inheritance3'
  associationClassName = 'CD_Association3'
  classClassName = 'CD_Class3'
  ASGname = 'CD_ClassDiagramsV3_META'
   
  warning = ''

  
def inheritanceCodeBase(self):
  """
  Intention in context:
    The user has just edited the class diagram in some way.
    1) Remove all attributes that were previously derived through inheritance.
    2) Propagate all attributes that can be derived through inheritance.
  Parameter:
    self, an instance of CD_Class3.py (on edit trigger) or CD_Inheritance3.py
         (on connect/disconnect trigger) subclass of ASGNode.py entity.
  Scope:
    Entire class diagram
  """
  # Avoid crazy amounts of (unnecessary) work while loading a saved model
  if(self.parent.isATOM3LoadingModel()):
    return
  
  myASG = self.rootNode.getASGbyName(Magic().ASGname)
  classEntityList = myASG.listNodes[Magic().classClassName]
  modelPath = getModelPath(self)
  
#===============================================================================
#  Remove all derived inheritance attributes
#===============================================================================
  for classEntity in classEntityList:
    localAttrOnlyList = []
    attrList = classEntity.attributes.getValue()
    while(attrList):
      attr = attrList.pop()
      if(not attr.getDerivedAttributeMarker()):
        localAttrOnlyList.append(attr)
    classEntity.attributes.setValue(localAttrOnlyList)

#===============================================================================
#  Propagate all derivable inheritance attributes
#===============================================================================
  for classEntity in classEntityList:
    # Mapping of integer depth from classEntity (superclass) to lists of
    # subclasses at that integer depth. 
    depth2subClassDict = getAllSubClasses(classEntity)
    
    # len(depth2subClassDict) == 0 if classEntity is not a superclass
    if(len(depth2subClassDict) != 0):        
      propagateAttr2Subclasses(classEntity, depth2subClassDict)
      propagateIcon2Subclasses(classEntity, modelPath)
      
#===============================================================================
#  Sort attributes alphabetically by name from A to Z
#  Update the visual text attribute of each class
#===============================================================================
  for classEntity in classEntityList:
    attrList = classEntity.attributes.getValue()
    # a.getValue()[0] = ATOM3Attribute.getValue() = (nameString, x, y, z, w)[0]
    attrList.sort(lambda a, b: cmp(a.getValue()[0], b.getValue()[0]))
    setDisplayInfo(classEntity) 
    
  if(Magic().warning):
    print '\n\n', Magic().warning, '\n\n'
    Magic().warning = ''
    
    
def propagateIcon2Subclasses(self, modelPath):
  """
  Intention in context:
    Given a class entity self, and provided that self has an icon in the 
    modelPath directory, the icon is copied and made available to each subclass.
  Limitations:
    If the user changes the superclass icon the subclass icons will not be 
    correspondingly changed. To overcome this the user should manually delete
    the graph_* files that should be regnerated.
    Furthermore, it's possible that in a long inheritance chain, multiple calls
    to the caller of this method are needed before icons reach the bottom-most 
    subclass.
  Parameters:
    self, an instance of CD_Class3.py subclass of ASGNode.py entity.
    modelPath, path to the model containing self (that saves it)
  """
  # If self (the superclass) has no icon, no propagation happens!
  selfIconPathTuple = getIconTuple(self, modelPath)
  if(not selfIconPathTuple[1]):
    return
  
  # For each immediate subclass of self...
  for conn in self.in_connections_:
    if(conn.__class__.__name__ == Magic().inheritanceClassName):
      subClass = conn.in_connections_[0]
      
      # Subclass has no icon: give it one from the superclass!
      subClassIconPathTuple = getIconTuple(subClass, modelPath)
      if(not subClassIconPathTuple[1]):
        superClassIconFile = open(selfIconPathTuple[0], 'r')
        subClassIconFile = open(subClassIconPathTuple[0], 'w')
        
        superName = "graph_" + getIconClassName(self)
        subName = "graph_" + getIconClassName(subClass)
        
        subClassIconFile.write(
                  stringReplacer(superClassIconFile.read(), superName, subName))
        
        superClassIconFile.close()
        subClassIconFile.close()
        
        
        
def getIconClassName(self):
  """
  Return:
    The class name found in the graphical appearance attribute (icon)
  """
  return self.Graphical_Appearance.className
  
  
  
def getModelPath(self):
  """
  Parameter:
    self, an instance of CD_Class3.py subclass of ASGNode.py entity.
  Returns:
    Path to the model (to which self belongs) if it exists (model is saved)
    None if model not saved or was deleted by mysterious forces
  Side effects:
    Assumes the model is saved. If not stores a warning message in Magic.
  """
  statusbar = self.parent.statusbar
  modelPathAndFile = statusbar.getState(statusbar.MODEL)[1][0] 
  if(not modelPathAndFile):
    Magic().warning = 'WARNING: Unable to propagate icons, please save model!'
    return None
  elif(not os.path.exists(modelPathAndFile)):
    Magic().warning = 'ERROR: Please save your model again!'
    return None
  
  return os.path.split(modelPathAndFile)[0]
  
  
  
def getIconTuple(self, modelPath):
  """
  Parameters:
    self, an instance of CD_Class3.py subclass of ASGNode.py entity.
    modelPath, path to the saved model containing self
  Returns:
    Tuple with: Path to the icon and a boolean that indicates if the icon exists
  Assumption:
    Icon is in the modelPath
  """
  if(not modelPath):
    return ('', False)
  
  iconFileName = "graph_" + getIconClassName(self) + '.py'
  iconFilePath = os.path.join(modelPath, iconFileName)
  if(os.path.exists(iconFilePath)):
    return (iconFilePath, True)
  return (iconFilePath, False)
  
  

def propagateAttr2Subclasses(self, depth2subClassDict):
  """
  Intention in context:
    Each attribute of self (that is not itself a derived inheritance attrbiute)
    is pushed into all the subclasses of self and marked as a derived atttriubte.
  Parameters:
    self, a superclass
    depth2subClassDict, integer subclass depth from topmost superclass mapping
                        to actual class instances
  """  
  # Filter out attributes that are derived by inheritance from superclasses
  attrList = [attr for attr in self.attributes.getValue()
              if not attr.getDerivedAttributeMarker()]
  
  # Go through all the subclasses and propagate our local attributes
  for depth in depth2subClassDict.keys():
    for subclass in depth2subClassDict[depth]:
      subAttrList = subclass.attributes.getValue()

      # Combine the attributes of super and subclass
      for attr in attrList:
        newAttr = attr.clone()
        newAttr.setDerivedAttributeMarker(True) # Indicate a derived attribute
        subAttrList.append(newAttr)
      
      # At this point I would do subclass.attributes.setValue(subAttrList)
      # So my changes would take effect. For some reason I don't need to.
      # I must be acting directly on a reference to the original list.



def getAllSubClasses(self):
  """
  Parameter:
    self is a instance of CD_Class3.py subclass of ASGNode.py entity.
  Return:
    Dictionary with integer depth from the superclass (self) mapping to a list
    of subclasses at that depth
  """
  def recursiveCrawler(semObj, subClassDict, depth=0):
    for conn in semObj.in_connections_:
      if(conn.__class__.__name__ == Magic().inheritanceClassName):
        subClass = conn.in_connections_[0]
        if(subClassDict.has_key(depth)):
          subClassDict[depth].append(subClass)
        else:
          subClassDict[depth] = [subClass]
        recursiveCrawler(subClass, subClassDict, depth + 1)
  
  depth2subClassDict = dict()
  recursiveCrawler(self, depth2subClassDict)
  return depth2subClassDict



  
def setDisplayInfo(self):
  """
  Intention in context:
    After a Edit, Connect, Disconnect event, update a handcrafted view of all 
    the contents of the entity self. 
  Parameter:
    self is a instance of CD_Class3.py subclass of ASGNode.py entity.
  """

  bullet = '  - '
  bulletPre = '  < '
  bulletPost = '  > ' 
  text = ''
  
  # Super parent: get options from the ASG
  myASG = self.rootNode.getASGbyName(Magic().ASGname)
  if( not myASG ): 
      showAttributes = False
      showConstraints = False
      showActions = False
      showCardinalities = False
  else:            
      showAttributes = myASG.showAttributes.getValue()[1]    
      showConstraints = myASG.showConditions.getValue()[1]  
      showActions = myASG.showActions.getValue()[1]  
      showCardinalities = myASG.showCardinalities.getValue()[1]  
  
  
  # Add stuff to the displayable text, depending on if it is hidden or not
  if( showAttributes and len( self.attributes.getValue() ) > 0 ):  
    text += 'Attributes:\n'
    for item in self.attributes.getValue():
      if(item.getDerivedAttributeMarker()): # Derived attribute, hide it
        continue
      val = item.getValue()
      text += bullet + val[0] + ' :: ' + val[1] + '\n'
  
  if( showConstraints and len( self.Constraints.getValue() ) > 0 ):  
    text += 'Constraints:\n'
    for item in self.Constraints.getValue():
      val = item.getValue()
      if(val[2][1] == 0): 
        text += bulletPre
      else: 
        text += bulletPost
      text += val[0] + '\n'
  
  if( showActions and len( self.Actions.getValue() ) > 0 ):    
    text += 'Actions:\n'
    for item in self.Actions.getValue():
      val = item.getValue()
      if(val[2][1] == 0): 
        text += bulletPre
      else: 
        text += bulletPost
      text += val[0]  + '\n'
  
  if( showCardinalities and len( self.cardinality.getValue() ) > 0 ):  
    text += 'Multiplicities:\n'
    for item in self.cardinality.getValue():
      val = item.getValue()
      if(val[1][1] == 0): 
        text += bullet + 'To '
      else: 
        text += bullet + 'From '
      text += val[0] + ': ' + val[2] + ' to ' + val[3] + '\n'
  
  self.display.setValue( text )
  
  if(self.graphObject_): 
    self.graphObject_.ModifyAttribute( 'display',  text )  
    fitText(self)
    

def fitText(self):
  """
  Intention in context:
    Fits (scales) self to contain it's text attributes
  Parameter:
    self, a class or association instance
  Notes:
    Input to the fitNode2Text2 method is as follows:
    String, GraphForm of the String attribute, GraphForm of the rectangle 
    container, Fudge factor
    Fudge factor is two optional parameters: scale X and scale Y
  """

  obj = self.graphObject_
  if( not obj ): 
    return
    
  if(self.__class__.__name__ == Magic().classClassName):
  

    textGFtupleList = []
    textGFtupleList.append((self.name.getValue(), obj.gf63, obj.gf1, 1.2 ))
    textGFtupleList.append((self.display.getValue(), 
                                                  obj.gf4, obj.gf3, 1.05, 1.05))
    
    obj.fitNodeToText2( textGFtupleList )
    
  
  elif(self.__class__.__name__ == Magic().associationClassName):
  
    obj = obj.centerObject
    if( not obj ): 
      return
    
    # String, GraphForm with string, Containing Rectangle GraphForm, Fudge factor
    textGFtupleList = []
    textGFtupleList.append((self.name.getValue(), obj.gf3, obj.gf9, 1.2 ) )
    textGFtupleList.append((self.display.getValue(), 
                                                obj.gf11, obj.gf12, 1.05, 1.05))
    
    obj.fitNodeToText2( textGFtupleList )
  
