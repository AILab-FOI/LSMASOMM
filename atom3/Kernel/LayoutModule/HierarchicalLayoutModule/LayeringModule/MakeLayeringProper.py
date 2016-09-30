"""
MakeLayeringProper.py

Adds dummy vertices wherever a long edge traverses more than a single layer.

By Denis Dube, Sept. 2005
"""

from HierarchicalLayoutModule.NodeWrapper import NodeWrapper

"""
Larger layer node: E3
Parents: E2 False
Children: E4 False
Children: E23 False
Children: E25 True (E3 has child E25 via reversal)
"""
"""
Larger layer node: E3
Parents: E2 False
Parents: L36 True (E3 has child L36 through reversal) # Should not exist
Children: E4 False
Children: L60 False
Children: E25 True (E3 has child L36 through reversal, L36 leads to E25)
"""

def MakeLayeringProper(levelDictionary):
  """
  If an edge crosses more than 1 layer, a dummy node is added so the edge
  can be bent around other nodes (thus avoiding overlap, min crossing)
  """
  multiEdgeAlreadyVisitedList = []
  
  uniqueID = 0  
  # Add dummy nodes if an edge traverses > 1 layer
  for currentLevelInt in levelDictionary.keys():
    for node in levelDictionary[currentLevelInt]:  
      
      debug = str(node) == 'E21'
      
    
      # Go through each node connected to this node
      # sourceNode --> Source2TargetListMap --> edge to target and the targetNode
      # WARNING: This list is not reversed as is node.children(), node.parent()
      #          Reversals are done in GreedyCycleRemoval.py to break cycles!
      for targetNode, directedEdge in NodeWrapper.Source2TargetListMap[node]:
                
        # Is the connected node more than 1 layer distant?
        # If yes, insert a dummy node here! One for each layer crossed
        targetNodeLayer = targetNode.getLayer()
        if(abs(targetNodeLayer - currentLevelInt) > 1):
          
          
          # This is the n-th edge in a series of
          # edges having the same source and target nodes... 
          if(directedEdge in multiEdgeAlreadyVisitedList):
            multiEdgeAlreadyVisitedList.remove(directedEdge)
            continue
          

          # We do not have the child we expected! What happened you ask?
          # Well, this edge was "deleted" to break a cycle, but 
          # NodeWrapper.Source2TargetListMap remembered it! 
          if(not node.children.has_key(targetNode)):
            uniqueID += 1
            multiEdgeAlreadyVisitedList = reversedArrowPatch(node, targetNode, 
                  directedEdge, levelDictionary, multiEdgeAlreadyVisitedList,
                  targetNodeLayer, currentLevelInt, uniqueID)
            continue
            
          else:
            linkFlagList = node.children[targetNode][:]
            
            # The linkFlagList potentially contains a number of edges each with
            # same source and target nodes! Make sure we handle it once only!
            for multiEdgeFlag in linkFlagList:
              if(directedEdge != multiEdgeFlag[0]):
                multiEdgeAlreadyVisitedList.append(multiEdgeFlag[0])
            
            # Child of node is now a dummy node (or chain of them),
            # with the last dummy node having the child targetNode
            del node.children[targetNode] 
            
          uniqueID += 1
          
          # The start/stop of the range depends on whether we go up or down
          if(targetNodeLayer > currentLevelInt):
            startLevel = currentLevelInt + 1
            stopLevel = targetNodeLayer
          else:            
            startLevel = targetNodeLayer + 1
            stopLevel = currentLevelInt 
            
          dummyParent = node     #node = E21, targetNode = E19
            
          for i in range(startLevel, stopLevel):
            # Create the dummy node, add it to level dict
            dummyNode = NodeWrapper((uniqueID, linkFlagList), 
                                     NodeWrapper.MULTI_LAYER_EDGE, i)
            levelDictionary[i].append(dummyNode)
            

            # I need to be able to trace links back and forth
            # Including the dummy nodes...
            dummyParent.children[dummyNode] = linkFlagList              
            dummyNode.parents[dummyParent] = linkFlagList
            dummyParent = dummyNode
            

            
          # The parent of the targetNode is now a dummy
          # This key will not exist if we are dealing with a reversed edge
          if(targetNode.parents.has_key(node)):
            del targetNode.parents[node]

          # The last dummy points to the targetNode, and the targetNode to the
          # last dummy.
          dummyNode.children[targetNode] = linkFlagList
          targetNode.parents[dummyNode] = linkFlagList
          
  return levelDictionary # Really not necessary...
  
  
def reversedArrowPatch(node, targetNode, directedEdge, levelDictionary,
      multiEdgeAlreadyVisitedList, targetNodeLayer, currentLevelInt, uniqueID):
  """
  Ugly quicky patch to fix the reversed arrow situation
  Basically just like the main version but reversed...
  """
  linkFlagList = node.parents[targetNode][:]

  # The linkFlagList potentially contains a number of edges each with
  # same source and target nodes! Make sure we handle it once only!
  for multiEdgeFlag in linkFlagList:
    if(directedEdge != multiEdgeFlag[0]):
      multiEdgeAlreadyVisitedList.append(multiEdgeFlag[0])
  
  # The start/stop of the range depends on whether we go up or down
  if(targetNodeLayer > currentLevelInt):
    startLevel = currentLevelInt + 1
    stopLevel = targetNodeLayer
  else:            
    startLevel = targetNodeLayer + 1
    stopLevel = currentLevelInt 
    
  
  dummyParent = targetNode     
  for i in range(startLevel, stopLevel):
    # Create the dummy node, add it to level dict
    dummyNode = NodeWrapper((uniqueID, linkFlagList), 
                             NodeWrapper.MULTI_LAYER_EDGE, i)
    levelDictionary[i].append(dummyNode)

    # I need to be able to trace links back and forth
    # Including the dummy nodes...
    dummyNode.parents[dummyParent] = linkFlagList
    dummyParent.children[dummyNode] = linkFlagList              
    dummyParent = dummyNode
    
  del targetNode.children[node]
  del node.parents[targetNode] 

  dummyNode.children[node] = linkFlagList
  node.parents[dummyNode] = linkFlagList
  
  
  return multiEdgeAlreadyVisitedList
  
