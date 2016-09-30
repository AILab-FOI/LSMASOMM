"""
inheritanceGenerator.py

Generates code from the class diagram
Re-worked by Denis Dube May 16, 2005 and again Feb 2006 and again Aug 2006
Beware the mad hacks... oooops did I say the H word? :)
"""

import tkMessageBox
import os
import time

from FilePaths import USER_NAME

from ATOM3Connection import ATOM3Connection
from ATOM3Constraint import ATOM3Constraint

# Names of entities in Class Diagram formalism
from inheritanceCodeBase import Magic

  
  
def genCode(self):
  """ 
  Generates class diagram code 
  By Denis Dube
  """
    
  # Save first, so if anything goes wrong, we got a fallback position hehehe
  status = self.statusbar.getState(self.statusbar.MODEL)[0]
  if( status == self.statusbar.MODIFIED ):
    self.save()
    
#===============================================================================
#  Pathfinding initilization
#===============================================================================
    
  # Get the ASGroot for this formalism
  ASGroot = self.ASGroot.getASGbyName(Magic().ASGname)
    
  # Make sure we don't generate a formalism with no name...
  if( ASGroot and hasattr( ASGroot, 'name' ) ):
    if( ASGroot.name.getValue() == '' ): 
      modelPathAndFile = self.statusbar.getState(self.statusbar.MODEL)[1][0] 
      modelName = os.path.split(modelPathAndFile)[1].split('.')[0]
      modelName = modelName.split('_')[0]
      ASGroot.name.setValue(modelName)
      
      tkMessageBox.showerror(
               "Code Generator Error",
               "Please give your formalism a name, such as: " + modelName 
               + "\nAnd then try to generate again"
               + "\n\nNOTE: A name was automatically generated, so just"
               + " press OK in the next dialog if you like it.",
               parent = self
          )
      self.modelAttributes(ASGroot)
      return
       
  # In cardConstObjects, we are storing the objects with cardinality constraints
  cardConstObjects = []
  
  if ASGroot.keyword_:
         if self.console: 
           self.console.appendText('Generating code for model '
                         +ASGroot.keyword_.toString())
  else:
         if self.console: 
           self.console.appendText('Generating code for model.')
  

  # Use directory of class diagram for generating code
  modelPathAndFile = self.statusbar.getState(self.statusbar.MODEL)[1][0]      
  modelPath = os.path.split(modelPathAndFile)[0]
  oldCodeGenDir = self.codeGenDir
  self.codeGenDir = os.path.normpath( modelPath )
    
#===============================================================================
#  Generate code
#===============================================================================
  print 'Generating code to: ', self.codeGenDir
    
  errors = []
  
  # for each node type
  for nodeType in [Magic().associationClassName, Magic().classClassName]:        
     # for each object of any type
     for UMLobject in ASGroot.listNodes[nodeType]:    
         # Generate code for this particular entity (Graphical icon code)
         error = genCodeFor(self, UMLobject)    
         if(error):
           errors.append(error)
  if(errors):
    title = 'Entity Generation Warning'
    msg = ''
    for error in errors:
      msg += '--> ' + error + '\n'
    msg += '\nNOTE: Instantiating entities without icons will cause an exception'
    print '\n', title, '\n', msg, '\n'
    tkMessageBox.showwarning(title, msg)
  
  # see first if we have generative attributes...
  self.genASGCode(cardConstObjects, ASGroot)  # generate code for the ASG node
  
  propagateCardinalities(self) # Inherit edges
  self.genButtons(ASGroot)       # generate the file for the syntax actions
  # now generate the file with the GUI model...
  self.genButtonsModel(ASGroot)
  
#===============================================================================
#  Cleanup
#===============================================================================
  
  # Restore path
  self.codeGenDir = oldCodeGenDir
  
  # Clear the screen, and then reload the old diagram
  # WHY? Because this generator has totally messed up the diagram in order
  # to do the inheritance stuff (it's safer this way, trust Denis)
  self.clearModel( showDialog=False )
  
  #for nodeType in ASGroot.nodeTypes:
  #  print nodeType, ASGroot.listNodes[nodeType]
    
  # Re-open the model
  self.open( fileName = modelPathAndFile )
  
  tkMessageBox.showinfo(
   "Code generated",
   "Code generated in:\n    " + modelPath +
   "\n\nPlease restart AToM3 before trying to load the newly generated " +
   "formalism\n\nHINT: starting another instance of AToM3 works too"
  )
  
  
  
def propagateInheritanceItems(ASGroot):
  """
  Author?
  """
  inheritance_rel = ASGroot.listNodes[Magic().inheritanceClassName]
  i = 0
  ##print "inheritance_rel=", inheritance_rel
  
  # now go for each inheritance association...
  while len(inheritance_rel)>0:
     inh = inheritance_rel[i]          # get the ith inheritance relationship
     ##print "inh=", inh
     parent = inh.out_connections_[0]  # get parent & child of the relationship  
     ##print "parent=", parent
     child = inh.in_connections_[0]
     ##print "child=", child
     found = 0
     # check that the parent does not have another class up
     for in_proc in parent.out_connections_:  
          if in_proc in inheritance_rel: 
             found = 1
             break   
     if found == 1:
        i = i+1
        if (i>=len(inheritance_rel)-1): 
          i = 0
     else:
        # add the attributes of the father to the child
        #child.addedAttrs = []
        child.added_in_connections_ = []
        child.added_out_connections_ = []
        child.addedCardinalities = []
        #for attr in parent.attributes.getValue():
           #child_attr = attr.clone()
           #child.attributes.newItem(child_attr)
           #child.addedAttrs.append(child_attr)
        child.added_in_connections_   = []+parent.in_connections_
        child.added_out_connections_ = []+parent.out_connections_
        for ic in child.added_in_connections_: 
          child.in_connections_.append(ic)    
        for oc in child.added_out_connections_: 
          child.out_connections_.append(oc)
        # now add the Cardinalities to the list in the child...
        for card in parent.cardinality.getValue():
           child_card = card.clone()
           child.cardinality.newItem(child_card)
           child.addedCardinalities.append(child_card)
  
        # now add the Cardinalities to the list in the in and out connections...
        for ic in parent.in_connections_:
           if ic.getTypeName() == Magic().associationClassName:
              cloneCardinality(ic, parent, child, 0)
        for oc in parent.out_connections_:
           if oc.getTypeName() == Magic().associationClassName:
              cloneCardinality(oc, parent, child, 1)
        inheritance_rel.remove (inh)    ## remove the relationship from the list
  
    
  
def addConstraintMinIn (assoc):
    """
    Author?
    """
    constr = assoc.Constraints.getValue()
    for con in constr:
        if con.getValue()[0] == "minCardinality_In_INH": 
          return
    const = ATOM3Constraint()
    const.setValue(("minCardinality_In_INH", 1, (None, 1), 
                    (None, [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 
                    "    if len(self.in_connections_)>1: "
                    + "return ('Too much source objects', self)\n"))
    constr.append(const)
    #assoc.Constraints.setValue(constr)



def addConstraintMinOut (assoc):
    """
    Author?
    """
    constr = assoc.Constraints.getValue()    
    for con in constr:
        if con.getValue()[0] == "minCardinality_Out_INH": 
          return
    const = ATOM3Constraint()
    const.setValue(("minCardinality_Out_INH", 1, (None, 1), 
                    (None, [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), 
                    "    if len(self.out_connections_)>1: "
                    + "return ('Too much target objects', self)\n"))
    constr.append(const)
    #assoc.Constraints.setValue(constr)    



def cloneCardinality ( assoc, parent, child, dir ):
    """
    Author?
    """
    for elem in assoc.cardinality.getValue():
        name, dire, min, max = elem.getValue()
        if name == parent.keyword_.toString() and dir == dire[1]:
            if min == '1' and max == '1':
                elem.setValue((name, dire, '0', '1'))
                if dire == 0: 
                  addConstraintMinOut (assoc)
                else: 
                  addConstraintMinIn (assoc)
            newElem = ATOM3Connection( child, min, max )
            # as we can have more than one child, we are not
            # sure whether we should restrict to exactly one
            # that is, it is ONE among all the children
            newElem.setValue(( child, dire, '0', max ))     
                                                            
            assoc.cardinality.newItem(newElem)
            if dir == 0:
                if "added_out_connections_" in assoc.__dict__.keys():
                    assoc.added_out_connections_.append(child)
                else:
                    assoc.added_out_connections_ = [child]
            else:
                if "added_in_connections_" in assoc.__dict__.keys():
                    assoc.added_in_connections_.append(child)
                else:
                    assoc.added_in_connections_ = [child]
            if "addedCardinalities" in assoc.__dict__.keys():
                assoc.addedCardinalities.append(newElem)
            else: assoc.addedCardinalities = [newElem]
            return 



def hasAttribute (classInstance, attrName):
    """
    Author?
    Returns:
      True if classInstance has an attribute called attrName
    """
    for attr in classInstance.attributes.getValue():
        if attr.getValue()[0] == attrName: 
          return 1
    return 0



def hasCardinality(classInstance, card):
    """
    Author?
    Returns:
      True if classInstance has a cardinality like card
    """
    for c in classInstance.cardinality.getValue():
        if c.hasEqualValue(card) : 
          return 1
    return 0





def genCodeFor ( self, entity ):
   """
      Author: Juan De Lara
      Code extracted from ATOM3.py and keyword check eliminated by Denis Dube
      Generates Python code for the entity
   """
   error = None
  
   if not entity.keyword_:  
     error = 'Entity: ' + entity.name.toString() + ' has no keyword attribute defined'
     return error
     
   
   # generate code for the ATOM3Links, because a graphical file must be generated
   for attr in entity.generatedAttributes.keys():
      type = entity.generatedAttributes[attr]          # A tuple with the types...
      if type[0] == 'ATOM3Link':                      # ey! an ATOM3Link has been found...
         at3link = entity.getAttrValue(attr)
         if at3link and not at3link.isNone():         # if it has some value...
            entity.getAttrValue(attr).genGraphicalFile( self.codeGenDir, self.parent )
         else:
            error = 'Entity: ' + entity.name.toString() + ' has no graphical appearance defined'
            return error
                          
   fileName = entity.keyword_.toString()+".py"                  # Prepare file name, with the keyword
   if self.console: self.console.appendText('Generating file '+fileName+' in directory '+self.codeGenDir)
   filePath =  os.path.join( self.codeGenDir, fileName)
   f = open( filePath, "w+t")                                          # open file name and print header
   #f.write("# __"+ fileName +"_____________________________________________________\n")
   f.write('"""\n')
   f.write("__"+ fileName +"_____________________________________________________\n")
   f.write("\n")
   f.write("Automatically generated AToM3 syntactic object (DO NOT MODIFY DIRECTLY)\n")
   f.write("Author: "+USER_NAME+"\n")
   f.write("Modified: "+time.asctime()+"\n")
   f.write("__"+ len(fileName)*"_" +"_____________________________________________________\n")
   f.write('"""\n')
   
   f.write("from ASGNode import *\n\n")            # generate imports
   f.write("from ATOM3Type import *\n\n")                               # generate imports
   self.importedTypes = []                # list where the necessary types will be placed

   self.visitorOnAttributes( f, entity, self.genImport)                 # generate import for ATOM3Types

   # now write each type of the list to the file...
   for typename in self.importedTypes:
      f.write("from "+typename+" import *\n")
   
   # Open the graphical appearence file (may not exist)
   graphicName = "graph_"+entity.keyword_.toString()+".py"            
   if( os.path.exists( os.path.join( self.codeGenDir, graphicName ) ) ):
      hasGraph = True
      f.write("from graph_"+entity.keyword_.toString()+" import *\n")
   
   # Not there... doh!
   else:
      hasGraph = False
      # if we should generate graphics, then give a warning!
      if self.genGraphics:  # generate == Yes
         error = "Entity '"+entity.keyword_.toString()+"' does not have an icon"

    
   f.write("class "+entity.keyword_.toString()+"(ASGNode, ATOM3Type):\n\n")    # generate class definition
   f.write("   def __init__(self, parent = None):\n")                # declare init method
   f.write("      ASGNode.__init__(self)\n")
   f.write("      ATOM3Type.__init__(self)\n")
   if hasGraph:                             # then write down the class name
       f.write("      self.graphClass_ = graph_"+entity.keyword_.toString()+"\n")
       #f.write("      self.isGraphObjectVisual = "+str(entity.isGraphObjectVisual)+"\n")
       # See HierarchicalASGNode.py for hierarchical code...
       entity._generateHierarchicalSemanticCode(f, '      ')
   self.genASGNodeCode(f, entity)                # call method to generate the rest of the code
   f.write("\n\n")
   f.close()
   
   return error



def propagateCardinalities(self):
  """
  Enable inheritance of associations
  By Denis Dube
  """
  myASG = self.ASGroot.getASGbyName(Magic().ASGname)
  classEntityList = myASG.listNodes[Magic().classClassName]
  inheritanceClassName = Magic().inheritanceClassName  
  
  
  # Go through all the classes and get just those that are superclass but not subclass
  superClassList = []
  for classEntity in classEntityList:
    # If it's a subclass, ignore it
    isSubClass = False
    for link in classEntity.out_connections_: 
      if(link.__class__.__name__ == inheritanceClassName):
        isSubClass = True 
        break
    if(isSubClass):
      continue
    
    # It's a superclass!
    for link in classEntity.in_connections_: 
      if(link.__class__.__name__ == inheritanceClassName):
        superClassList.append(classEntity)
        break
  
  for superclass in superClassList:
    propagateEdge2Subclasses(superclass)
    
  
  
def propagateEdge2Subclasses(superclass):
  """
  Simply augments the cardinalities so that subclasses can use the edges of
  their superclasses. This method recursively calls itself.
  By Denis Dube
  """
  associationClassName = Magic().associationClassName
  associationList = []
  atom3i = superclass.parent
  
  
  # Gather all the associations of the super-class
  for link in superclass.out_connections_:
    if(link.__class__.__name__ == associationClassName):
      associationList.append(link)
  for link in superclass.in_connections_:
    if(link.__class__.__name__ == associationClassName):
      if(link not in associationList):
        associationList.append(link)
  
  # Propagate to the subclasses
  for link in superclass.in_connections_: 
    if(link.__class__.__name__ == Magic().inheritanceClassName):
      for subclass in link.in_connections_:
          
        # For each association
        for association in associationList:
          # Fix the association's cardinalities to include the subclass
          cardList = association.cardinality.getValue()
          newCardList = []
          temp = []
          for card in cardList:
            cardName = card.getValue()[0]
            if(cardName == superclass.name.getValue()):
              newCard = card.clone()
              newCard.className.setValue(subclass.name.getValue())
              newCardList.append(newCard)
              temp.append(newCard)
            newCardList.append(card.clone())
          association.cardinality.setValue(newCardList)

        # Fix the subclass cardinalites to include everything the superclass does
        newCardList = []
        cardList = superclass.cardinality.getValue() + subclass.cardinality.getValue()
        for card in cardList:
          newCardList.append(card.clone())
        subclass.cardinality.setValue(newCardList)
                    
        # Continue the propagation down the inheritance tree
        propagateEdge2Subclasses(subclass)
         