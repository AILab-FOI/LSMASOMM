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
    print "(MININ) constr=", constr, assoc, assoc.AssociationConstraints
    #assoc.AssociationConstraints.setValue(constr)

def addConstraintMinOut (assoc):
    constr = assoc.AssociationConstraints.getValue()    
    for con in constr:
        if con.getValue()[0] == "minCardinality_Out_INH": return
    const = ATOM3Constraint()
    const.setValue(("minCardinality_Out_INH", 1, (None, 1), (None, [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]), "    if len(self.out_connections_)>1: return ('Too much target objects', self)\n"))
    constr.append(const)
    print "(MINOUT) constr=", constr, assoc, assoc.AssociationConstraints
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

