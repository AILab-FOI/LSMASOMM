from AtomAssociation import AtomAssociation
from AtomClass import AtomClass
from ATOM3Connection import *
from ATOM3Constraint import *

def addConstraintMinIn (assoc):
    constr = assoc.AssociationConstraints.getValue()
    for con in constr:
        if con.getValue()[0] == "minCardinality_In_INH": return
    const = ATOM3Constraint()
    const.setValue(("minCardinality_In_INH", 1, (None, 1), (None, [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), "    if len(self.in_connections_)>1: return ('Too much source objects', self)\n"))
    constr.append(const)
    #assoc.AssociationConstraints.setValue(constr)

def addConstraintMinOut (assoc):
    constr = assoc.AssociationConstraints.getValue()    
    for con in constr:
        if con.getValue()[0] == "minCardinality_Out_INH": return
    const = ATOM3Constraint()
    const.setValue(("minCardinality_Out_INH", 1, (None, 1), (None, [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), "    if len(self.out_connections_)>1: return ('Too much target objects', self)\n"))
    constr.append(const)
    #assoc.AssociationConstraints.setValue(constr)    

def cloneCardinality ( assoc, parent, child, dir ):
    for elem in assoc.AssociationCardinality.getValue():
        name, dire, min, max = elem.getValue()
        if name == parent.keyword_.toString() and dir == dire[1]:
            if min == '1' and max == '1':
                elem.setValue((name, dire, '0', '1'))
                if dire == 0: addConstraintMinOut (assoc)
                else: addConstraintMinIn (assoc)
            newElem = ATOM3Connection( child, min, max )
            newElem.setValue(( child, dire, '0', max ))     # as we can have more than one child, we are not
                                                            # sure whether we should restrict to exactly one
                                                            # that is, it is ONE among all the children
            assoc.AssociationCardinality.newItem(newElem)
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
       returns true if classInstance has an attribute called attrName
    """
    for attr in classInstance.ClassAttributes.getValue():
        if attr.getValue()[0] == attrName: return 1
    return 0

def hasCardinality(classInstance, card):
    """
       returns true if classInstance has a cardinality like card
    """
    for c in classInstance.ClassCardinality.getValue():
        if c.hasEqualValue(card) : return 1
    return 0


def genCodeClassDiagram (ATOM3Instance, ASGroot=None):
    """
    Generates code for a class diagram. (added 20/01/05 by EG)
    - ASGroot: asgRoot for which buttons model is generated, by default ATOM3Instance.ASGroot 
    """
    if ASGroot==None: ASGroot=ATOM3Instance.ASGroot                  # default value for asgRoot
    
    hasGraph = 0						     # flag that indicates if we have a graphical attribute
    cardConstObjects = []
    if ASGroot.keyword_:
           if ATOM3Instance.console: ATOM3Instance.console.appendText('Generating code for model '+ASGroot.keyword_.toString())
    else:
           if ATOM3Instance.console: ATOM3Instance.console.appendText('Generating code for model.')

    inheritance_rel = ASGroot.listNodes["AtomInheritance"]
    i = 0

    for child in ASGroot.listNodes["AtomClass"]:
        child.parents = []
        child.addedAttrs = []
        child.added_in_connections_ = []
        child.added_out_connections_ = []
        child.addedCardinalities = []


    # now go for each inheritance association...
    while len(inheritance_rel)>0:
       inh = inheritance_rel[i]  				# get the ith inheritance relationship
       parent = inh.out_connections_[0]			# get parent & child of the relationship  
       child = inh.in_connections_[0]
       found = 0
       for in_proc in parent.out_connections_:		# check that the parent does not have another class up
            if in_proc in inheritance_rel: 
               found = 1
               break   
       if found == 1:
          i = i+1
          if (i>=len(inheritance_rel)-1): i = 0
       elif not parent in child.parents:
          child.parents.append(parent)
          # add the attributes of the father to the child
          #child.addedAttrs = []
          #child.added_in_connections_ = []
          #child.added_out_connections_ = []
          #child.addedCardinalities = []
          for attr in parent.ClassAttributes.getValue():
             name = attr.getValue()[0]
             if not hasAttribute (child, name): # Added 26/02/05 by JL
                child_attr = attr.clone()
                child.ClassAttributes.newItem(child_attr)
                child.addedAttrs.append(child_attr)
          for ic in parent.in_connections_:
              if not ic in child.in_connections_:
                 child.added_in_connections_.append(ic) 
                 child.in_connections_.append(ic)		## añadir tambien a ic.out_connections_
          for oc in parent.out_connections_:
              if not oc in child.out_connections_:
                 child.added_out_connections_.append(oc) 
                 child.out_connections_.append(oc)		## añadir tambien a oc.in_connections_
          # now add the Cardinalities to the list in the child...
          for card in parent.ClassCardinality.getValue():
             if not hasCardinality(child, card): 
               child_card = card.clone()
               child.ClassCardinality.newItem(child_card)
               child.addedCardinalities.append(child_card)
          # now add the Cardinalities to the list in the in and out connections...
          for ic in parent.in_connections_:
             if ic.getTypeName() == "AtomAssociation" and ic in child.in_connections_:
                cloneCardinality(ic, parent, child, 0)
          for oc in parent.out_connections_:
             if oc.getTypeName() == "AtomAssociation" and oc in child.out_connections_:
                cloneCardinality(oc, parent, child, 1)
          inheritance_rel.remove (inh)		## remove the relationship from the list
          if i>=len(inheritance_rel): i = 0
    
    for nodeType in ASGroot.nodeTypes:				# for each node type
       for UMLobject in ASGroot.listNodes[nodeType]:		# for each object of any type
           ATOM3Instance.genCodeFor (UMLobject, cardConstObjects) # Generate code for this particular entity

    # see first if we have generative attributes...
    ATOM3Instance.genASGCode(cardConstObjects)                               # generate code for the ASG node
    ATOM3Instance.genButtons()                                                # generate the file for the syntax actions
    # now generate the file with the GUI model...
    ATOM3Instance.genButtonsModel()
   
    # now delete the added attributes to the children
    for child in ASGroot.listNodes["AtomClass"]:        
       attribs = child.ClassAttributes.getValue()
       for attr in child.addedAttrs:
          attribs.remove(attr)
       child.ClassAttributes.setValue(attribs)
       # delete the added in_connections and out_connections
       for ic in child.added_in_connections_: child.in_connections_.remove(ic)
       for oc in child.added_out_connections_: child.out_connections_.remove(oc)
       cards = child.ClassCardinality.getValue()
       for card in child.addedCardinalities: cards.remove(card)
       child.ClassCardinality.setValue(cards)

    # remove the extra cardinalities from Atom3Association
    for assoc in ASGroot.listNodes["AtomAssociation"]:
       if "addedCardinalities" in assoc.__dict__.keys():
          cards = []+assoc.AssociationCardinality.getValue()
          for card in assoc.addedCardinalities: 
              if card in cards: cards.remove(card)
          assoc.AssociationCardinality.setValue(cards)
       if "added_in_connections_" in assoc.__dict__.keys():
          for ic in assoc.added_in_connections_: 
              if ic in assoc.in_connections_: assoc.in_connections_.remove(ic)
       if "added_out_connections_" in assoc.__dict__.keys():
          for oc in assoc.added_out_connections_: 
             if oc in assoc.out_connections_: assoc.out_connections_.remove(oc)
    
