"""
GreedyCycleRemoval.py

By Denis Dube, Sept. 2005
"""
  

def GreedyCycleRemoval(wrappedNodeList):
  """
  Uses topological sort then reverses backward edges to eliminate cycles
  Returns nodes in topological sort order
  """    
  topSort = __getTopologicalSort(wrappedNodeList)
  
  # Debug
#  print 'Topological sorting'
#  for wrappedNode in topSort:
#    print '   ', str(wrappedNode)
  
  # Reverse backward arcs to eliminate cycles 
  for nodeIndex in range(0, len(topSort)):
    wrappedNode = topSort[nodeIndex]         
    wrappedChildrenNodes = wrappedNode.children.keys()
    
    for wrappedChildrenNode in wrappedChildrenNodes:
      # If the child has a smaller index than the current node it is left
      # of the current node. That means it forms a cycle!
      if(nodeIndex > topSort.index(wrappedChildrenNode)):
        
        # Get the link (or maybe more than one link) between parent
        # wrappedNode and child wrappedChildrenNode
        linkFlagList = wrappedNode.children[wrappedChildrenNode][:]
        
        # Remove it to break the cycle! We'll put it back, but in reverse...
        del wrappedNode.children[wrappedChildrenNode]
        del wrappedChildrenNode.parents[wrappedNode]
        
        # Reverse it
        tempList = []
        for linkFlag in linkFlagList:
          tempList.append([linkFlag[0], True]) # Reverse flag set to True
        wrappedChildrenNode.children[wrappedNode] = tempList[:]
        wrappedNode.parents[wrappedChildrenNode] = tempList[:]
      
      # Self-loop situation (handled elswhere, this should not be triggered)
      elif(nodeIndex == topSort.index(wrappedChildrenNode)):
        print 'SELFLOOP', str(wrappedChildrenNode)
        
  return topSort
    

    
    
    
def __getTopologicalSort(wrappedNodeList):
  """
  Returns the node list as topologically sorted with forward arcs running 
  from left to right (if cycles exist, there will be backward arcs too)
  
  WARNING: Result is non-deterministic since node.children.keys() has no order
           This was an unintentional implementation error, although unless you
           desperately wanted a deterministic algorithm it shouldn't bother you
           much...
  """
  def DFSlookup(node, sortedNodeList):
    """ Sub-method for topological sort, does depth first search """
    for childNode in node.children.keys(): #node.getChildrenWrappers():
      if(not childNode.isVisited()):
        childNode.setVisited()
        DFSlookup(childNode, sortedNodeList)
    sortedNodeList.append(node)
  
  # Go through each non-visited node and set it to visited then DFS it
  sortedNodeList = []
  for node in wrappedNodeList:
    if(not node.isVisited()):    
      node.setVisited()    
      DFSlookup(node, sortedNodeList)
      
  sortedNodeList.reverse()
  return sortedNodeList
  
  
  
#    TODO: implement this idea
#    From: A Technique for Drawing Directed Graphs
#    Emden R. Gansner, Eleftherios Koutsofios, Stephen C. North, Kiem-Phong Vo
#    AT&T Bell Laboratories Murray Hill, New Jersey 07974
#It seems reasonable to try to reverse a smaller or even minimal set of edges. 
#One difficulty is that finding a minimal set (the feedback arc set problem) 
#is NP-complete [EMW] [GJ]. More important, this would probably not improve the 
#drawings. We implemented a heuristic to reverse edges that participate in many 
#cycles. The heuristic takes one non-trivial strongly connected component at a 
#time, in an arbitrary order. Within each component, it counts the number of 
#times each edge forms a cycle in a depth-first traversal. An edge with a 
#maximal count is reversed. This is repeated until there are no more 
#non-trivial strongly connected components.
  