"""
AToM3SpringOptions.py

By Denis Dube, Sept 2005
"""

from OptionDatabase       import OptionDatabase
from OptionDialog         import OptionDialog


from SpringOptionsKeys import MAXIMUM_ITERATIONS
from SpringOptionsKeys import SPRING_CONSTANT
from SpringOptionsKeys import SPRING_LENGTH
from SpringOptionsKeys import CHARGE_STRENGTH
from SpringOptionsKeys import CHARGE_THRESHOLD
from SpringOptionsKeys import GRAVITY_STRENGTH
from SpringOptionsKeys import RANDOM_AMOUNT
from SpringOptionsKeys import FORCE_TOPLEFT_TO_ORIGIN
from SpringOptionsKeys import USE_SPLINES
from SpringOptionsKeys import ARROW_CURVATURE
from SpringOptionsKeys import PROMOTE_EDGE_TO_NODE
from SpringOptionsKeys import MINIMUM_FORCE
from SpringOptionsKeys import FORGIVE_ROUNDS



class AToM3SpringOptions:
  """ Trivial class to store an option database instance """
  OptionDatabase = None
  

#===============================================================================
#Public method
#===============================================================================
  
def showSpringOptions(atom3i):
  """ 
  Use:
    Change the option via a dialog system 
  Precondition:
    loadOptions was used so that AToM3SpringOptions.OptionDatabase class
    variable points to an instance of an OptionDatabase.
  Returns:
    A dictionary of optionStrings to optionValues
    None if user canceled the 'show' dialog
  """
  if(not AToM3SpringOptions.OptionDatabase):
    __loadOptions(atom3i)
    
  if(AToM3SpringOptions.OptionDatabase.showOptionsDatabase()):    
    return AToM3SpringOptions.OptionDatabase.getOptionValueMap()
  else:
    return None
    
    
    
def dumpOptions2Console(atom3i):
  """ Quick way to get all options neccessary to use this layout """
  if(not AToM3SpringOptions.OptionDatabase):
    __loadOptions(atom3i)
  optionDB = AToM3SpringOptions.OptionDatabase.cloneDatabase()

  print '# Spring Layout Options'
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
  AToM3SpringOptions.OptionDatabase = OptionDatabase(atom3i.parent, 
        'Options_SpringElectrical.py', 'Spring-Electrical Configuration')
  
  # Local methods/variables with short names to make things more readable :D
  newOp = AToM3SpringOptions.OptionDatabase.createNewOption
  IE = OptionDialog.INT_ENTRY
  FE = OptionDialog.FLOAT_ENTRY
  BE = OptionDialog.BOOLEAN_ENTRY
  LA  = OptionDialog.LABEL
  EE = OptionDialog.ENUM_ENTRY
  
  # Create New Options
  # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
  
  newOp('label0001', None, [LA, "Times 12", "blue", "center" ], 
        "Complexity: O(iterations*n^2)", "")    
  newOp('sep0000', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  
  newOp(RANDOM_AMOUNT, 0, IE, "Initial randomization", 
      "Randomizes the initial position of linked nodes as a percentage of " + 
      "spring length. 0 <= RANDOM_AMOUNT <= 100")    
      
  newOp(MAXIMUM_ITERATIONS, 100, IE, "Maximum Iterations", 
    'Duration of the spring simulation, tradeof between layout running-time '+
    'and the quality of the layout')
    
  newOp(MINIMUM_FORCE, 10.0, FE, "Minimum/Convergence force", 
      "If the largest force acting on a vertex is less than the minimum force "+ 
      "the algorithm has converged and terminates.")   
 
  newOp(FORGIVE_ROUNDS, 2, IE, "Forgiveness rounds", 
      "If the convergence test is triggered the algorithm continues for "+ 
      "FORGIVE_ROUNDS.\n" +
      "If forces exceed the minimum force thereafter, the forgivness rounds " +
      "are reset.")   
                 
  enumOptions = [EE, 'Never', 'Smart', 'Always']
  newOp(PROMOTE_EDGE_TO_NODE, 'Never', enumOptions, 
        "Promote edge centers to nodes?", 
      "For directed edges with large center drawings, promoting the center to "\
      + "a node can lead to a much superiour layout\n\n"
      + "Example: One directed edge becomes one node and 2 directed edges\n\n"
      + "The 'smart' option will promote only if a center drawing is present" )     
      
                 
  newOp('sep0002', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  newOp('label0005', None, [OptionDialog.LABEL, "Times 12", "blue", "center" ], 
                            'Physical simulation parameters', '')
                                 
  newOp(SPRING_CONSTANT, 0.1, FE, "Spring Constant (Do not change)", 
      'The restoring force of the spring, larger values make the spring ' +
      '"stiffer"\nIn other words: a larger value makes it attracts/repulses ' +
      'connected nodes much more violently '+
      '\nWARNING: Do not change, 0.1 works quite well.')
  newOp(SPRING_LENGTH, 100, IE, "Spring rest length", 
      'The ideal distance between any two connected nodes' +
      '\nBecause of other forces, this distance may never be achieved' +      
      '\nDefault: 100' +
      '\nNote: negative spring lengths are possible, and have the effect of ' +
      'pulling connected nodes closer together.' +
      '\n       The physics of this are rather dubious however.')
      
  newOp(CHARGE_STRENGTH, 10.00, FE, "Electric charge strength", 
      'A multiplier on the repulsive force between each and every node.' +
      '\nIf set to 0.0, no repulsive forces are calculated' +
      '\nDefault: 10.0')
  newOp(CHARGE_THRESHOLD, 300, IE, "Charge treshold distance", 
      'The effect of electric charges diminishes with the square of the ' +
      '\ndistance until this threshold distance is reached... at which point' +
      '\nelectric charge has no effect at all.' +
      '\nWhy a charge distance threshold?' +
      '\n  1) Slight improvement to running time' +
      '\n  2) Allows you to set higher charge strength without pushing ' +
      '\n     distant objects obscenely far away...' +
      '\n  3) Improves convergence?' +
      '\nDefault: 300')    
  newOp(GRAVITY_STRENGTH, 10, IE, "Gravitional force strength", 
      'A coarse simulation of gravity, all nodes are drawn to the center of ' +
      'the graph.' +
      '\nThe gravity strength integer is multiplied with the unit vector each '+
      'node makes with the graph center.'
      '\nDefault value: 10')
  
              
  newOp('sep0001', 'Ignored', OptionDialog.SEPERATOR, "Ignored?", "Ignored!") 
  newOp('label0004', None, [OptionDialog.LABEL, "Times 12", "blue", "center" ], 
                            'Post-processing options', '')
       
  newOp(FORCE_TOPLEFT_TO_ORIGIN, True, BE, "Force topleft to origin", 
      "If False, some nodes may move outside the viewable canvas area" ) 
     
  newOp(USE_SPLINES, True, BE, "Spline arrows", 
      "Arrows are set to smooth/spline mode and given additional control " +
      "points.")         
  newOp(ARROW_CURVATURE, 10, IE, "Arrow curvature", 
      "Adds a curve of magnitude X to the arrows, set to 0 for a straight " +
      "arrow.")
  
   

     
  # Load the options from the file, on failure the defaults above are used.
  AToM3SpringOptions.OptionDatabase.loadOptionsDatabase()
    


    