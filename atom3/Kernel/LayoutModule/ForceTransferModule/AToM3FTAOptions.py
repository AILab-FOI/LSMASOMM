"""
AToM3FTAOptions.py

By Denis Dube, Sept 2005
"""

from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog

from FTAOptionsKeys import MIN_NODE_DISTANCE, MIN_LINK_DISTANCE
from FTAOptionsKeys import SEPERATION_FORCE, MAX_TOTAL_ITERATIONS
from FTAOptionsKeys import BORDER_DISTANCE, USE_SPLINES, ARROW_CURVATURE
from FTAOptionsKeys import PROMOTE_EDGE_TO_NODE


class AToM3FTAOptions:
  """ Trivial class to store an option database instance """
  OptionDatabase = None
  

#===============================================================================
#Public method
#===============================================================================
  
def showFTAOptions(atom3i):
  """ 
  Use:
    Change the option via a dialog system 
  Precondition:
    loadOptions was used so that AToM3FTAOptions.OptionDatabase class
    variable points to an instance of an OptionDatabase.
  Returns:
    A dictionary of optionStrings to optionValues
    None if user canceled the dialog
  """
  if(not AToM3FTAOptions.OptionDatabase):
    __loadOptions(atom3i)
    
  if(AToM3FTAOptions.OptionDatabase.showOptionsDatabase()): 
    return AToM3FTAOptions.OptionDatabase.getOptionValueMap()
  return None
    
    
    
def dumpOptions2Console(atom3i):
  """ Quick way to get all options neccessary to use this layout """
  if(not AToM3FTAOptions.OptionDatabase):
    __loadOptions(atom3i)
  optionDB = AToM3FTAOptions.OptionDatabase.cloneDatabase()

  print '# Force-Transfer Layout Options'
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
  AToM3FTAOptions.OptionDatabase = OptionDatabase( atom3i.parent,
        'Options_ForceTransfer2.py', 'Force Transfer Configuration')
  
  # Local methods/variables with short names to make things more readable :D
  newOp = AToM3FTAOptions.OptionDatabase.createNewOption
  IE = OptionDialog.INT_ENTRY
  FE = OptionDialog.FLOAT_ENTRY
  BE = OptionDialog.BOOLEAN_ENTRY
  EE = OptionDialog.ENUM_ENTRY
  LA = OptionDialog.LABEL
    
  # Create New Options
  # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
  
  newOp('label0005', None, [LA, "Times 12", "blue", "center" ], 
        "Complexity: O(iterations*n^2)", "")    
  newOp('sep0005', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  
  optionList = [ LA, "Times 12", "blue", "left" ]
  
  enumOptions = [EE, 'Never', 'Smart', 'Always']
  newOp(PROMOTE_EDGE_TO_NODE, 'Never', enumOptions, 
        "Promote edge centers to nodes?", 
      "For directed edges with large center drawings, promoting the center to "\
      + "a node can lead to a much superiour layout\n\n"
      + "Example: One directed edge becomes one node and 2 directed edges\n\n"
      + "The 'smart' option will promote only if a center drawing is present" )
      
      
  newOp( MIN_NODE_DISTANCE, 20, IE, "Minimum node seperation", 
      "Node entities will be seperated by a minimum of this many pixels")        
  newOp( MIN_LINK_DISTANCE, 20, IE, "Minimum link node seperation", 
      "Distance in pixels that link nodes should be seperated from other nodes")
  newOp( SEPERATION_FORCE, 0.2, FE, "Seperation force",
      "Magnitude of the force that will seperate overlapping nodes")
  newOp( MAX_TOTAL_ITERATIONS, 50, IE, "Max total iterations",
      "Stop iterating, even if stable configuration not reached, to prevent unreasonably long periods of non-interactivity")
  newOp( BORDER_DISTANCE, 0, IE, "Border distance",
      "If an entity is pushed off the canvas, the canvas will be re-centered plus this pixel offset to the top left")

  newOp('sep0001', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  newOp('label0003', None, optionList, 'Arrow post-processing options', '')
      
  newOp( USE_SPLINES , True, BE, "Spline optimization", 
      "Sets the arrow to smooth mode and adds 2 extra control points" )
  newOp( ARROW_CURVATURE, 10, IE, "Arrow curvature", 
      "Adds a curve of magnitude X to the arrows, "
      +"set to 0 for a straight arrow." )    

     
  # Load the options from the file, on failure the defaults above are used.
  AToM3FTAOptions.OptionDatabase.loadOptionsDatabase()
    


    