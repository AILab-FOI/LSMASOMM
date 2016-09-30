"""
Utilities.py

Simple but useful methods...

By Denis Dube, 2005
""" 


def isSorted(nodeList):
  """ 
  Use:
    Returns True if the node list is already sorted by barycenter value
  Parameter:
    nodeList, a list of nodes with a getBarycenter() method
  Pre-condition:
    nodeList is a non-empty list, nodes have computed barycenters
  """
  A = nodeList[0].getBarycenter()
  for i in range(1, len(nodeList)):
    B = nodeList[i].getBarycenter()
    if(A <= B):
      A = B
      continue
    else:
      return False
  return True
  
  
  
def updateOrder(orderedLayer):
  """ 
  The ordering is implicit in the node sequence in the list
  However to do a node sort, it's handy to have each node know its order
  This order is used only within __barycentricOrdering() except for debug
  """
  i = 0
  for node in orderedLayer:
    node.setOrder(i)
    i += 1
    
    
    
def copyDict(levelDictionary):
  """ 
  Makes a true copy of the levelDictionary 
  Useful for back-tracking to a previous levelDictionary
  """
  newDict = dict()
  for i in levelDictionary.keys():
    newDict[i] = levelDictionary[i][:]
  return newDict
  
  

def prettyPrintList(someList):
  """ Debug method to pretty print a list """
  text = '['
  if(len(someList) == 0):
    return '[]'
  else:
    text += str(someList[0])
    someList = someList[1:]
  for someItem in someList:
    text += ', ' + str(someItem)
  return text + ']'
  
  
#  def initialOrdering(levelDictionary):
#  """ 
#  Gives the nodes an initial order to reduce cross reduction workload 
#  Assumed: getOrder() returns -1 for all nodes at this point
#  PROBLEM: the nodes are already implicitly ordered in their layer list position
#  according to DFS... so this method is doing nothing! 
#  """
#
#  def DFS(node, levelInt, orderTracker):
#    for child in node.children.keys():
#        if(child.getOrder() == -1):
#          child.setOrder(orderTracker[levelInt])
#          DFS(child, levelInt, orderTracker)
#      
#  orderTracker = dict()
#  for i in range(0, len(levelDictionary)):
#    orderTracker[i] = 0
#      
#  for levelInt in range(0, len(levelDictionary)):
#    level = levelDictionary[levelInt]
#    for node in level:
#      node.setOrder(orderTracker[levelInt])
#      orderTracker[levelInt] += 1
#      DFS(node, levelInt, orderTracker)
#      
#  
#  for level in levelDictionary.values():
#    level.sort(lambda a, b: cmp(a.getOrder(), b.getOrder()))
#
#  return levelDictionary
  