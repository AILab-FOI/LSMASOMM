"""
AToM3CircleOptions.py

By Denis Dube, Sept 2005
"""

from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog


from CircleOptionsKeys import FORCE_TOPLEFT_TO_ORIGIN
from CircleOptionsKeys import MIN_NODE_SPACING
from CircleOptionsKeys import USE_SPLINES
from CircleOptionsKeys import ARROW_CURVATURE
from CircleOptionsKeys import PROMOTE_EDGE_TO_NODE



class AToM3CircleOptions:
  """ Trivial class to store an option database instance """
  OptionDatabase = None
  

#===============================================================================
#Public method
#===============================================================================
  
def showCircleOptions(atom3i):
  """ 
  Use:
    Change the option via a dialog system 
  Precondition:
    loadOptions was used so that AToM3CircleOptions.OptionDatabase class
    variable points to an instance of an OptionDatabase.
  Returns:
    A dictionary of optionStrings to optionValues
    None if user canceled the dialog
  """
  if(not AToM3CircleOptions.OptionDatabase):
    __loadOptions(atom3i)
  
  if(AToM3CircleOptions.OptionDatabase.showOptionsDatabase()):    
    return AToM3CircleOptions.OptionDatabase.getOptionValueMap()
  return None
    
    

def dumpOptions2Console(atom3i):
  """ Quick way to get all options neccessary to use this layout """
  if(not AToM3CircleOptions.OptionDatabase):
    __loadOptions(atom3i)
  optionDB = AToM3CircleOptions.OptionDatabase.cloneDatabase()

  print '# Circle Layout Options'
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
#Private method: use outside this file and I will hunt you down and hurt you
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
  AToM3CircleOptions.OptionDatabase = OptionDatabase( atom3i.parent,
        'Options_CircleLayout.py', 'Circle Layout Configuration')
  
  # Local methods/variables with short names to make things more readable :D
  newOp = AToM3CircleOptions.OptionDatabase.createNewOption
  IE = OptionDialog.INT_ENTRY
  BE = OptionDialog.BOOLEAN_ENTRY
  EE = OptionDialog.ENUM_ENTRY
    

  # Create New Options
  # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
  
  optionList = [OptionDialog.LABEL, "Times 12", "blue", "center" ]  
  newOp( 'label0000', None, optionList, 'Complexity: O(n)', '' )
  newOp('sep0003', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!")
  
  
  optionList = [OptionDialog.LABEL, "Times 12", "blue", "left" ]
  newOp( 'label0001', None, optionList, 'Node positioning', '' )
  newOp( FORCE_TOPLEFT_TO_ORIGIN, False, BE, "Start circle at origin?", 
      "If false, the current position of the selected nodes is used" )   
  newOp( MIN_NODE_SPACING, 0, IE, "Minimum node spacing", 
      "Minimum pixel distance between any 2 tree nodes." \
      + "\n\nDefault: 0" 
      + "\n\nNOTE: negative values are useful for maximizing compactness.") 
  
  enumOptions = [EE, 'Never', 'Smart', 'Always']
  newOp(PROMOTE_EDGE_TO_NODE, 'Never', enumOptions, 
        "Promote edge centers to nodes?", 
      "For directed edges with large center drawings, promoting the center to "\
      + "a node can lead to a much superiour layout\n\n"
      + "Example: One directed edge becomes one node and 2 directed edges\n\n"
      + "The 'smart' option will promote only if a center drawing is present" )     
      
  
  newOp('sep0000', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  newOp('label0003', None, optionList, 'Arrow post-processing options', '')
      
  newOp( USE_SPLINES , True, BE, "Spline optimization", 
      "Sets the arrow to smooth mode and adds 2 extra control points" )
  newOp( ARROW_CURVATURE, 10, IE, "Arrow curvature", 
      "Adds a curve of magnitude X to the arrows, "
      +"set to 0 for a straight arrow." )    

     
  # Load the options from the file, on failure the defaults above are used.
  AToM3CircleOptions.OptionDatabase.loadOptionsDatabase()
    


    