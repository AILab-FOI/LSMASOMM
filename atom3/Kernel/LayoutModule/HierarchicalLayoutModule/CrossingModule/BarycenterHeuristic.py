"""
BarycenterHeuristic.py

By Denis Dube, 2005
"""

from random import shuffle
import sys

from Utilities import updateOrder
from Utilities import isSorted
from Utilities import copyDict
from CrossingCounter import countAllCrossings

# OPTIONAL - DEBUG
#from Utilities import prettyPrintList
from HierarchicalLayoutModule.Debug import debugLevelDict

def BarycenterHeuristic(levelDictionary, maxNoProgressRounds, maxTotalRounds,
                                                           useRandomRestarts):
  """
  Use:
    Reduces crossings between each pair of layers in a k-layer graph by sweeping
    down/up the layers. This is done by re-ordering the nodes.
  Parameters:
    levelDictionary, dictionary where keys are levels, values are node lists
    maxTotalRounds, hard maximum on number of crossing reduction rounds
    maxNoProgressRounds, maximum number of consecutive rounds with no crossing
                         reduction
    useRandomRestarts, enables random restarting when no progress is being made
  Returns:
    levelDictionary, modified with a reduced crossing ordering.
  """
    
  # Init variables
  totalLevelsInt = len(levelDictionary.keys())
  currentRound = 0
  currentNoProgressRound = 0
  if(useRandomRestarts):
    roundsUntilTryRandom = 0
  else:
    roundsUntilTryRandom = sys.maxint # In other words: NEVER!
  
  # Initilize layer orderings 
  for level in levelDictionary.values():
    updateOrder(level)
    
  bestGlobalCrossingsInt = countAllCrossings(levelDictionary)
  bestOrderingDict = copyDict(levelDictionary)
  
  print 'Edge crossings before barycenter crossing reduction:', 
  print bestGlobalCrossingsInt, '\n'
  
  # Global-graph crossing reduction loop: runs infintely long because
  # the down and up sweeps will undo each other's work at some point.
  # Therefore, must halt after maxTotalRounds iterations, or check for 
  # convergence in the number of global crossings.
  while(currentRound < maxTotalRounds):
    currentRound += 1
    
#===============================================================================
#    Down Barycenter layer sweeper
#    The main down-sweep loop will run at most |levelDictionary| times
#===============================================================================
    isMakingProgress = True
    while(isMakingProgress):
      isMakingProgress = False
      
      # Iterate over all the levels in the level dictionary
      # If totalLevelsInt = 3, then this range yields [0, 1]
      for j in range(0, totalLevelsInt - 1):
        ## Down-Barycenter (Parent to child)
        for node in levelDictionary[j]:
          node.computeBarycenter(True)
        # Sort the list in place according to barycenter values
        if(not isSorted(levelDictionary[j])):
          levelDictionary[j].sort(lambda a, b: cmp(a.getBarycenter(),
                                                 b.getBarycenter()))
          # Save the node's sorted position in it's internal parameter
          updateOrder(levelDictionary[j])   
          isMakingProgress = True
          
#===============================================================================
#    Up Barycenter layer sweeper
#    The main up-sweep loop will run at most |levelDictionary| times
#===============================================================================
    isMakingProgress = True
    while(isMakingProgress):
      isMakingProgress = False
              
      # Iterate over all the levels in the level dictionary
      # If totalLevelsInt = 3, then this range yields [2, 1, 0]
      for j in range(totalLevelsInt - 1, -1, -1):
        
        ## Up-Barycenter (Child to parent)
        for node in levelDictionary[j]:
          node.computeBarycenter(False)
          
        # Sort the list in place according to barycenter values
        if(not isSorted(levelDictionary[j])):
          levelDictionary[j].sort(lambda a, b: cmp(a.getBarycenter(),
                                                     b.getBarycenter()))
          # Save the node's sorted position in it's internal parameter
          updateOrder(levelDictionary[j])
          isMakingProgress = True
      
#===============================================================================
#    Convergence Test: Check if crossings are still reducing
#===============================================================================
  
    currentCrossings = countAllCrossings(levelDictionary)
    print 'Current round:', currentRound, 'of', maxTotalRounds
    print '    Current crossings:', currentCrossings, '(Best so far:',
    print str(bestGlobalCrossingsInt) + ')'
        
    # No crossings: HALT
    if(currentCrossings == 0):
      print '\nCrossing minimization yielded 0 crossings in', currentRound, 
      print 'rounds!\n'
      return levelDictionary
    
    # Better crossings than ever seen before, save it!
    elif(currentCrossings < bestGlobalCrossingsInt):
      bestGlobalCrossingsInt = currentCrossings
      bestOrderingDict = copyDict(levelDictionary)
      currentNoProgressRound = 0
      
    # No crossing reduction... *cries*
    else:
      currentNoProgressRound += 1      
      print '<< No progress round:', currentNoProgressRound, 'of', 
      print maxNoProgressRounds, '>>'
      
      # No progress: HALT
      if(currentNoProgressRound >= maxNoProgressRounds):
        print '\nCrossing minimization terminated early, max rounds without', \
              'crossing reduction reached at round', currentRound
        print 'Edge crossings after barycenter crossing reduction:', 
        print bestGlobalCrossingsInt, '\n'  
        return bestOrderingDict
      
      # Randomization: roundsUntilTryRandom is sys.maxint if disabled
      elif(roundsUntilTryRandom <= 0):
        # Reset roundsUntilTryRandom, proportional to number of levels
        # Why? Because more levels need more time to propagate changes...
        roundsUntilTryRandom = max(1, int(totalLevelsInt / 10))
        for layer in levelDictionary.values():
          shuffle(layer)
          updateOrder(layer)
        print '|| Vertex ordering randomized ||'
          
      else:
        roundsUntilTryRandom -= 1
    
    
  print '\nCrossing minimization reached max rounds', currentRound
  print 'Edge crossings after barycenter crossing reduction:', 
  print bestGlobalCrossingsInt, '\n'  
  return bestOrderingDict
  
