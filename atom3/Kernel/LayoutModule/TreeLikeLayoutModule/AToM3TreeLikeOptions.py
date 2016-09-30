"""
AToM3TreeLikeOptions.py

By Denis Dube, Sept 2005
"""

from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog

from TreeLikeOptionsKeys import MIN_HORIZONTAL_DISTANCE
from TreeLikeOptionsKeys import MIN_VERTICAL_DISTANCE
from TreeLikeOptionsKeys import MANUAL_CYCLE_BREAKING
from TreeLikeOptionsKeys import FORCE_TOPLEFT_TO_ORIGIN
from TreeLikeOptionsKeys import USE_SPLINES
from TreeLikeOptionsKeys import ARROW_CURVATURE
from TreeLikeOptionsKeys import PROMOTE_EDGE_TO_NODE
from TreeLikeOptionsKeys import TIP_OVER_STYLE



class AToM3TreeLikeOptions:
  """ Trivial class to store an option database instance """
  OptionDatabase = None
  

#===============================================================================
#Public method
#===============================================================================
  
def showTreeLikeOptions(atom3i):
  """ 
  Use:
    Change the option via a dialog system 
  Precondition:
    loadOptions was used so that AToM3TreeLikeOptions.OptionDatabase class
    variable points to an instance of an OptionDatabase.
  Returns:
    A dictionary of optionStrings to optionValues
  """
  if(not AToM3TreeLikeOptions.OptionDatabase):
    __loadOptions(atom3i)
    
  if(AToM3TreeLikeOptions.OptionDatabase.showOptionsDatabase()):    
    return AToM3TreeLikeOptions.OptionDatabase.getOptionValueMap()
  return None 
    
    
def dumpOptions2Console(atom3i):
  """ Quick way to get all options neccessary to use this layout """
  if(not AToM3TreeLikeOptions.OptionDatabase):
    __loadOptions(atom3i)
  optionDB = AToM3TreeLikeOptions.OptionDatabase.cloneDatabase()

  print '# Tree-like Layout Options'
  print 'optionsDict = dict()'
  for optionString, valueList in optionDB.items():
    initialValue, optionTuple, promptString, helpString = valueList
    extraText = ''
    
    if(optionTuple[0] == OptionDialog.LABEL 
                                      or optionTuple == OptionDialog.SEPERATOR):
      continue
    elif(optionTuple[0] == OptionDialog.ENUM_ENTRY 
                            or optionTuple[0] == OptionDialog.ENUM_ENTRY_HORIZ):
      extraText = ' # ' + str(optionTuple[1:])
      
    print '"""\n' + helpString + '\n"""'
    if(type(initialValue) == type(str())):
      print "optionsDict['" + str(optionString) + "'] = '" + str(initialValue) \
              + "'" + extraText
    else:
      print "optionsDict['" + str(optionString) + "'] = " + str(initialValue) \
            + extraText

#===============================================================================
#Private method
#===============================================================================

def __loadOptions(atom3i):
  """
  Use:
    Sets default option values for Hierarchical layout, unless a save option 
    file is found, in which case the value in the file is used.
  Parameter:
    atom3i is an instance of ATOM3
  """
  
  # Instantiate the Option Database module
  AToM3TreeLikeOptions.OptionDatabase = OptionDatabase( atom3i.parent,
                  'Options_TreeLikeLayout.py', 'TreeLikeLayout Configuration')
  
  # Local methods/variables with short names to make things more readable :D
  newOp = AToM3TreeLikeOptions.OptionDatabase.createNewOption
  IE = OptionDialog.INT_ENTRY
  BE = OptionDialog.BOOLEAN_ENTRY
  EE = OptionDialog.ENUM_ENTRY
    

  # Create New Options
  # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
  
  optionList = [OptionDialog.LABEL, "Times 12", "blue", "center" ]
  newOp( 'label0000', None, optionList, 'Complexity: O(n)', '' )
  newOp('sep0003', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!")
    
  optionList = [OptionDialog.LABEL, "Times 12", "blue", "left" ]
  
  newOp( 'label0001', None, optionList, 'Node spacing', '' )
  newOp( MIN_HORIZONTAL_DISTANCE, 20, IE, "Minimum X Distance", 
      "Minimum horizontal distance between any 2 tree nodes (Default 20)" )   
  newOp( MIN_VERTICAL_DISTANCE, 70, IE, "Minimum Y Distance", 
      "Minimum vertical distance between any 2 tree nodes (Default 70)" )  
  
  newOp('sep0000', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  newOp( 'label0002', None, optionList, 'Miscellaneous options', '' )
  
  newOp( TIP_OVER_STYLE, True, BE, "Tip over style", 
        "If true, using a more space efficient tip over style drawing technique." 
        + "If false, uses a traditional top to bottom drawing technique.")
  newOp( FORCE_TOPLEFT_TO_ORIGIN, False, BE, "Start tree at origin?", 
      "If false, the current position of the selected nodes is used" )        
  newOp( MANUAL_CYCLE_BREAKING, False, BE, "Manual Cycle Breaking", 
      "Forces the user to break cycles by manually clicking on nodes" )
      
  enumOptions = [EE, 'Never', 'Smart', 'Always']
  newOp(PROMOTE_EDGE_TO_NODE, 'Never', enumOptions, 
        "Promote edge centers to nodes?", 
      "For directed edges with large center drawings, promoting the center to "\
      + "a node can lead to a much superiour layout\n\n"
      + "Example: One directed edge becomes one node and 2 directed edges\n\n"
      + "The 'smart' option will promote only if a center drawing is present" )     
      
  
  newOp('sep0001', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  newOp('label0003', None, optionList, 'Arrow post-processing options', '')
      
  newOp( USE_SPLINES , True, BE, "Spline optimization", 
      "Sets the arrow to smooth mode and adds 2 extra control points" )
  newOp( ARROW_CURVATURE, 10, IE, "Arrow curvature", 
      "Adds a curve of magnitude X to the arrows, "
      +"set to 0 for a straight arrow." )    

     
  # Load the options from the file, on failure the defaults above are used.
  AToM3TreeLikeOptions.OptionDatabase.loadOptionsDatabase()
    


    