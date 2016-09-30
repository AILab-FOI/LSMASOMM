"""
AToM3HierarchicalOptions.py

By Denis Dube, Sept 2005
"""

from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog


from HierarchicalOptionsKeys import LAYERING_ALGORITHM
from HierarchicalOptionsKeys import MIN_HORIZONTAL_DISTANCE
from HierarchicalOptionsKeys import MIN_VERTICAL_DISTANCE
from HierarchicalOptionsKeys import MAX_NO_PROGRESS_ROUNDS   
from HierarchicalOptionsKeys import MAX_TOTAL_ROUNDS         
from HierarchicalOptionsKeys import CROSS_ALG_CHOICE     
from HierarchicalOptionsKeys import USE_RANDOM_RESTARTS     
from HierarchicalOptionsKeys import MAX_BARYCENTER_ITER
from HierarchicalOptionsKeys import FORCE_TOPLEFT_TO_ORIGIN
from HierarchicalOptionsKeys import USE_SPLINES
from HierarchicalOptionsKeys import ARROW_CURVATURE
from HierarchicalOptionsKeys import PROMOTE_EDGE_TO_NODE
from HierarchicalOptionsKeys import LAYOUT_DIRECTION



class AToM3HierarchicalOptions:
  """ Trivial class to store an option database instance """
  OptionDatabase = None
  

#===============================================================================
#Public method
#===============================================================================
  
def showHierarchicalOptions(atom3i):
  """ 
  Use:
    Change the option via a dialog system 
  Precondition:
    loadOptions was used so that AToM3HierarchicalOptions.OptionDatabase class
    variable points to an instance of an OptionDatabase.
  Returns:
    A dictionary of optionStrings to optionValues
    None if user canceled the dialog
  """
  if(not AToM3HierarchicalOptions.OptionDatabase):
    __loadOptions(atom3i)
  
  if(AToM3HierarchicalOptions.OptionDatabase.showOptionsDatabase()):
    return AToM3HierarchicalOptions.OptionDatabase.getOptionValueMap()
  return None
    
    
    
def dumpOptions2Console(atom3i):
  """ Quick way to get all options neccessary to use this layout """
  if(not AToM3HierarchicalOptions.OptionDatabase):
    __loadOptions(atom3i)
  optionDB = AToM3HierarchicalOptions.OptionDatabase.cloneDatabase()

  print '# Hierarchical Layout Options'
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
  AToM3HierarchicalOptions.OptionDatabase = OptionDatabase( atom3i.parent,
        'Options_HiearchicalLayout2.py', 'Hieararchical Layout Configuration')
  
  # Local methods/variables with short names to make things more readable :D
  newOp = AToM3HierarchicalOptions.OptionDatabase.createNewOption
  IE = OptionDialog.INT_ENTRY
  BE = OptionDialog.BOOLEAN_ENTRY
  EE = OptionDialog.ENUM_ENTRY
  EEH = OptionDialog.ENUM_ENTRY_HORIZ
    
  # Create New Options
  # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
  
  newOp('label0005', None, [OptionDialog.LABEL, "Times 12", "blue", "center" ], 
        "Complexity: O(iterations*n^2)", "")    
  newOp('sep0005', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  
  optionList = [OptionDialog.LABEL, "Times 12", "blue", "left" ]
  
  enumOptions = [EEH, 'Never', 'Smart', 'Always']
  newOp(PROMOTE_EDGE_TO_NODE, 'Never', enumOptions, 
        "Promote edge centers to nodes?", 
      "For directed edges with large center drawings, promoting the center to "\
      + "a node can lead to a much superiour layout\n\n"
      + "Example: One directed edge becomes one node and 2 directed edges\n\n"
      + "The 'smart' option will promote only if a center drawing is present" )
  enumOptions = [EEH, 'Never', 'Smart', 'Always']

    
  enumOptions = [EEH, 'BFS', 'Longest-path', 'Minimum-width']
  newOp( LAYERING_ALGORITHM, 'BFS', enumOptions, 
        'Layering algorithm', 'The algorithm will assign each node to a row')
  
  newOp('sep0000', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  newOp( 'label0001', None, optionList, 'Crossing minimization', '' )
  
  newOp( MAX_TOTAL_ROUNDS, 30, IE, 
        "Maximum total rounds", 
      "The MAXIMUM number of outer loop crossing reduction attempts." \
      + "\n\nFeel free to use large numbers, they are unlikely to be reached!" \
      + "\nIn fact, expect the progress checker to break the loop after a" \
      + " small number of iterations." \
      + "\n\nWARNING: if random restarts are enabled, the max may be reached." \
      + "\n\nDefault: 30" )    
  newOp( MAX_NO_PROGRESS_ROUNDS, 6, IE, "Max rounds without progress", 
      "The maximum number of consecutive rounds without reducing crossings." \
      + "\nIf this number is rounds is reached the algorithm terminates early."\
      + "\n\nThis parameter can significantly reduce running time without" \
      + " affecting the quality of the resulting layout!" \
      + "\n\nDefault: 10" )  
#  newOp(USE_RANDOM_RESTARTS, True, BE, "Use random restarts?", 
#      "If true, whenever crossing reduction hits a snag, the position of each" \
#      + " vertex is randomized. Applied with the Barycenter heuristic\n\n" \
#      + "This option can easily double total running time, but almost always" \
#      + " reduces crossings.")   
  enumOptions = [EEH, 'None', 'Barycenter', 'Transpose', 'Both']
  newOp( CROSS_ALG_CHOICE, 'Barycenter', enumOptions, 'Use heuristic:', 
        'Choose the crossing reduction strategy to use.\n'
        + '\nNone: Does no crossing minimization... very fast... bad quality'
        + '\nBarycenter: O(n log n) fast heuristic'
        + '\nTranspose: O(n^2) slow heuristic.'
        + '\nBoth: Barycenter first then Transpose'
        + '\n\nNote: Transpose = Greedy Switch = Adjacent Exchange'
        + '\n\nDefault: Barycenter')
  enumOptions = [EEH, 'None', 'Barycenter', 'Transpose', 'Both']
  newOp( USE_RANDOM_RESTARTS, 'None', enumOptions, 
        'Use random restarts with:', 
        'Random restarts enable crossing minimization to make progress when it'
        + ' would otherwise get stuck.'
        + '\nNOTE: This can significantly increase running time, but almost'
        + ' always reduces crossings a bit more.'
        + '\n\nNone: never use randomization'
        + '\nBarycenter: use randomization just with barycenter'
        + '\nTranspose: use randomization just with transpose'
        + '\nBoth: use randomization with both algorithms'
        + '\n\nDefault: None')
      
  newOp('sep0001', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  newOp( 'label0002', None, optionList, 'Final node positioning', '' )
  
  newOp( FORCE_TOPLEFT_TO_ORIGIN, True, BE, "Start drawing at origin?", 
      "If false, the current position of the selected nodes is used" )       
  newOp( MIN_HORIZONTAL_DISTANCE, 30, IE, "Minimum X Distance", 
      "Minimum horizontal distance between any 2 tree nodes (negative" 
      + " values work too) (Default 30)" )   
  newOp( MIN_VERTICAL_DISTANCE, 30, IE, "Minimum Y Distance", 
      "Minimum vertical distance between any 2 tree nodes (Default 30)" )  
#  newOp( ADD_EDGEDRAWING_HEIGHT, True, BE, "Add edge object height", 
#      "Increment spacing between node layers with edge object drawing of"\
#      + " maximum height between 2 given layers" ) 
  newOp( MAX_BARYCENTER_ITER, 100, IE, "Max horizontal positioning rounds", 
      "Maximum horizontal position rounds. \nUses barycenter. " \
      + "\nConvergence testing will usually cut-off at <5 rounds." \
      + "\n\nDefault: 100" ) 
      
  enumOptions = [EEH, 'North', 'East', 'South', 'West']
  newOp( LAYOUT_DIRECTION, 'South', enumOptions, 
        'Layout direction', 'The drawing will point in the given direction.\n'
        + '\nNorth: all arrows point north'
        + '\nEast: all arrows point east'
        + '\nSouth: all arrows point south'
        + '\nWest: all arrows point west')
        
  newOp('sep0002', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  newOp('label0003', None, optionList, 'Arrow post-processing options', '')
      
  newOp( USE_SPLINES , True, BE, "Spline optimization", 
      "Sets the arrow to smooth mode and adds 2 extra control points" )
  newOp( ARROW_CURVATURE, 10, IE, "Arrow curvature", 
      "Adds a curve of magnitude X to the arrows, "
      +"set to 0 for a straight arrow." )    
      
     
  # Load the options from the file, on failure the defaults above are used.
  AToM3HierarchicalOptions.OptionDatabase.loadOptionsDatabase()
    


    