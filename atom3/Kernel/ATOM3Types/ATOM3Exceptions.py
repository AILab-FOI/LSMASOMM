# _ ATOM3Exceptions.py ____________________________________________________________________________
# Some exceptions raised by the ATOM3Type childs
# _________________________________________________________________________________________________

class ATOM3Error(Exception): pass
class ATOM3BadAssignmentValue(ATOM3Error): pass
class ATOM3ElementOutOfRange(ATOM3Error): pass
