"""
Scripting.py

The AToM3 constraints placed on a graphical appearence file are really just
scripts :D
This file stores & retrieves the contraint list & run-time-change flag.

Created Summer 2004, Denis Dube
"""


class Scripting:
  
    def __init__(self, runTimeChange = False, constraintList = [] ):
        # Do the graphics change at run-time?
        self.runTimeChange = runTimeChange
        
        # Graphical Constraints List
        self.constraintList = constraintList	
                 
    def getRunTimeChange( self ):
        return self.runTimeChange
        
    def setRunTimeChange( self, value ):
        self.runTimeChange = value
        
    def getConstraintList( self ):
        return self.constraintList
    
    def setConstraintList( self, constraintList ):
        self.constraintList = constraintList