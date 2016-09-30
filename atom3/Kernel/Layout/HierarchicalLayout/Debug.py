"""
Debug.py

By Denis Dube, 2005
"""

from CrossingModule import countCrossings

def debugLevelDict(levelDictionary, level=None):
  if(level != None):
    levelNames = []
    for node in level:
      levelNames.append([node.getName(), node.getOrder()])
    print 'LEVEL', levelNames
    return      
  for levelInt in levelDictionary.keys():
    levelNames = []
    for node in levelDictionary[levelInt]:
      #levelNames.append([node.getName(), node.getOrder()])
      levelNames.append([node.getName(), node.getGridPosition()])
    print 'LEVEL', levelInt, levelNames
  
  
  
def debugCrossing(levelDictionary):
  def updateOrder(orderedLayer):
    i = 0
    for node in orderedLayer:
      node.setOrder(i)
      i += 1
  for i in range(0, len(levelDictionary) ):
    updateOrder(levelDictionary[i])
  
  total = 0
  for i in range(0, len(levelDictionary) - 1):      
    temp = countCrossings(levelDictionary[i], levelDictionary[i + 1])
    total += temp
    print '   Crossings between levels', i, i + 1, '=', temp
  print 'Total crossings', total  