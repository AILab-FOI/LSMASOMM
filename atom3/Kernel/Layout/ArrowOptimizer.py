"""
ArrowOptimizer.py

Optimizes selected arrows by making them perfectly straight with their
intermediate node at the center. It can also set the arrow to smooth 
mode and add 2 extra control points to ensure that the arrow doesn't
'break' when moved. Furthermore, it can move the intermediate node
and the extra control points by a certain offset to add a curvature
effect to the arrow, giving the arrow an organic look. Although the
magnitude of the curvature can be set, the direction of the curvature
is randomized to keep with the organic look.

Created July 26, 2004
"""

from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog
from Utilities            import optimizeLinks

def applyLayout( atom3i = None, settings = False, selection = None ):
  
   # Instantiate the layout algorithm, if not already done  
  if( ArrowOptimizer.instance == None ):
    if( atom3i == None ):   
      raise Exception, "You forgot to initilize "+__name__+" before using it!"
    ArrowOptimizer.instance = ArrowOptimizer(atom3i)    
  
  if( atom3i ):
    ArrowOptimizer.instance.updateATOM3instance( atom3i )
  
  if( settings ):
    ArrowOptimizer.instance.settings( selection ) 
  else:    
    ArrowOptimizer.instance.main( selection )     

    
class ArrowOptimizer:
  
  instance = None
  
  # Option keys
  USE_SPLINE_OPTIMIZATION      = 'Spline optimization' 
  ARROW_CURVATURE              = 'Arrow curvature'

  
  def __init__(self, atom3i ):
     
    self.cb = atom3i.cb

    # Instantiate the Option Database module
    self.__optionsDatabase = OptionDatabase( atom3i.parent,
                    'Options_ArrowOptimizer.py', 'Arrow Optimizer Configuration')
    
    # Local methods/variables with short names to make things more readable :D
    newOp = self.__optionsDatabase.createNewOption
    IE = OptionDialog.INT_ENTRY
    BE = OptionDialog.BOOLEAN_ENTRY
      
    # Create New Options
    # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
    
    newOp( self.USE_SPLINE_OPTIMIZATION, True, BE, "Spline optimization", 
        "Sets the arrow to smooth mode and adds 2 extra control points" )
    newOp( self.ARROW_CURVATURE, 10, IE, "Arrow curvature", 
        "Adds a curve of magnitude X to the arrows, set to 0 for a straight arrow." )    
        
     
    # Load the options from the file, on failure the defaults above are used.
    self.__optionsDatabase.loadOptionsDatabase()
  
  def updateATOM3instance( self, atom3i ):
    """ Possible to have multiple instances of atom3 """
    self.cb = atom3i.cb    
   
  def settings( self, selection ):
    """
    Dialog to interactively change the spring's behavior
    Automatically applies layout if not canceled
    """
    if( self.__optionsDatabase.showOptionsDatabase() ):
      self.main( selection )
    
  def main( self, selection ): 
    
    setSmooth    = self.__optionsDatabase.get(self.USE_SPLINE_OPTIMIZATION)   
    setCurvature = self.__optionsDatabase.get(self.ARROW_CURVATURE) 
    
    if( selection ):
      optimizeLinks( self.cb, setSmooth, setCurvature, selectedLinks=selection )
    else: 
      optimizeLinks( self.cb, setSmooth, setCurvature  )
      
      
      