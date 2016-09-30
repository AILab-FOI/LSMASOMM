"""
AToM3OrthogonalOptions.py

By Denis Dube, Sept 2005
"""

from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog


from OrthogonalOptionsKeys import PROMOTE_EDGE_TO_NODE



class AToM3OrthogonalOptions:
  """ Trivial class to store an option database instance """
  OptionDatabase = None
  

#===============================================================================
#Public method
#===============================================================================
  
def showOrthogonalOptions(atom3i):
  """ 
  Use:
    Change the option via a dialog system 
  Precondition:
    loadOptions was used so that AToM3OrthogonalOptions.OptionDatabase class
    variable points to an instance of an OptionDatabase.
  Returns:
    A dictionary of optionStrings to optionValues
    None if user canceled the 'show' dialog
  """
  if(not AToM3OrthogonalOptions.OptionDatabase):
    __loadOptions(atom3i)
    
  if(AToM3OrthogonalOptions.OptionDatabase.showOptionsDatabase()):    
    return AToM3OrthogonalOptions.OptionDatabase.getOptionValueMap()
  else:
    return None
    
    
    
def dumpOptions2Console(atom3i):
  """
  Use:
    Dumps all the option key/value pairs into the console
  """
  if(not AToM3OrthogonalOptions.OptionDatabase):
    __loadOptions(atom3i)
  optionMap = AToM3OrthogonalOptions.OptionDatabase.getOptionValueMap()
  print '\nDumping option database entries to console\n\n'
  for optionString, optionValue in optionMap.items():
    print '"' + str(optionString) + '"\n', optionValue
  print '\n'


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
  AToM3OrthogonalOptions.OptionDatabase = OptionDatabase(atom3i.parent, 
        'Options_Orthogonal.py', 'Orthogonal Layout Configuration')
  
  # Local methods/variables with short names to make things more readable :D
  newOp = AToM3OrthogonalOptions.OptionDatabase.createNewOption
#  IE = OptionDialog.INT_ENTRY
#  FE = OptionDialog.FLOAT_ENTRY
#  BE = OptionDialog.BOOLEAN_ENTRY
  LA  = OptionDialog.LABEL
  EE = OptionDialog.ENUM_ENTRY
  
  # Create New Options
  # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
  
  newOp('label0001', None, [LA, "Times 12", "blue", "center" ], 
        "Complexity: O(n)", "")    
  newOp('sep0000', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  
#  newOp(RANDOM_AMOUNT, 0.0, FE, "Initial randomization", 
#      "Randomizes the initial position of linked nodes as a percentage of " + 
#      "spring length.")    
#      
#  newOp(MAXIMUM_ITERATIONS, 100, IE, "Maximum Iterations", 
#    'Duration of the spring simulation, tradeof between layout running-time '+
#    'and the quality of the layout')
                 
  enumOptions = [EE, 'Never', 'Smart', 'Always']
  newOp(PROMOTE_EDGE_TO_NODE, 'Never', enumOptions, 
        "Promote edge centers to nodes?", 
      "For directed edges with large center drawings, promoting the center to "\
      + "a node can lead to a much superiour layout\n\n"
      + "Example: One directed edge becomes one node and 2 directed edges\n\n"
      + "The 'smart' option will promote only if a center drawing is present" )
      
                 
#  newOp('sep0002', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
#  newOp('label0005', None, [OptionDialog.LABEL, "Times 12", "blue", "center" ], 
#                            'Physical simulation parameters', '')
#                                 
#  newOp(SPRING_CONSTANT, 0.1, FE, "Spring Constant (Do not change)", 
#      'The restoring force of the spring, larger values make the spring ' +
#      '"stiffer"\nIn other words: a larger value makes it attracts/repulses ' +
#      'connected nodes much more violently '+
#      '\nWARNING: Do not change, 0.1 works quite well.')
#  newOp(SPRING_LENGTH, 100, IE, "Spring rest length", 
#      'The ideal distance between any two connected nodes' +
#      '\nBecause of other forces, this distance may never be achieved' +      
#      '\nDefault: 100' +
#      '\nNote: negative spring lengths are possible, and have the effect of ' +
#      'pulling connected nodes closer together.' +
#      '\n       The physics of this are rather dubious however.')
#      
#  newOp(CHARGE_STRENGTH, 10.00, FE, "Electric charge strength", 
#      'A multiplier on the repulsive force between each and every node.' +
#      '\nIf set to 0.0, no repulsive forces are calculated' +
#      '\nDefault: 10.0')
#  newOp(CHARGE_THRESHOLD, 300, IE, "Charge treshold distance", 
#      'The effect of electric charges diminishes with the square of the ' +
#      '\ndistance until this threshold distance is reached... at which point' +
#      '\nelectric charge has no effect at all.' +
#      '\nWhy a charge distance threshold?' +
#      '\n  1) Slight improvement to running time' +
#      '\n  2) Allows you to set higher charge strength without pushing ' +
#      '\n     distant objects obscenely far away...' +
#      '\n  3) Improves convergence?' +
#      '\nDefault: 300')    
#  newOp(GRAVITY_STRENGTH, 10, IE, "Gravitional force strength", 
#      'A coarse simulation of gravity, all nodes are drawn to the center of ' +
#      'the graph.' +
#      '\nThe gravity strength integer is multiplied with the unit vector each '+
#      'node makes with the graph center.'
#      '\nDefault value: 10')
  
              
#  newOp('sep0001', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
#  newOp('label0004', None, [OptionDialog.LABEL, "Times 12", "blue", "center" ], 
#                            'Post-processing options', '')
       
#  newOp(FORCE_TOPLEFT_TO_ORIGIN, True, BE, "Force topleft to origin", 
#      "If False, some nodes may move outside the viewable canvas area" ) 

     
  # Load the options from the file, on failure the defaults above are used.
  AToM3OrthogonalOptions.OptionDatabase.loadOptionsDatabase()
    


    