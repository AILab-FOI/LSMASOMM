# __ File: GGrule.py _______________________________________________________________________
# Implements : class GGrule
# Author     : Juan de Lara
# Description: Base clase for all Graph-Grammar Rules. Inherits from ASGNode.
#              This class implements the Algorithm for isomorphic graph matching proposed in
#              LNCS 922, pg. 28
# Modified   :
#   - 20 Oct 2001. Fixed bug in method addNewConnection that created an extra connection when
#                  replacing a RHS and connecting an 'old' node with a newly created node
#   - 25 July 2002. Added parameter atom3i to Specify methods.
#   - 9  Aug. 2002: Added the TimeDelay attribute
#   - 6  Sept.2002: Added exactMatch attribute and modified matches to allow subtyping also.
# ___________________________________________________________________________________________

from tkMessageBox import showerror

from ASGNode   import *
from ASG       import *
from ATOM3Type import *

class GGrule (ASGNode, ATOM3Type):
   def __init__(self, executionOrder = None):
      ASGNode.__init__(self)
      ATOM3Type.__init__(self)
      self.executionOrder = executionOrder		# The execution order, if None, the execution order is not important
      self.LHS = None					# left hand side
      self.RHS = None                                   # right hand side
      self.TimeDelay = None                             # In children, this will have the delay (in ms) until next GG evaluation (Added 9 Aug. 2002, JL)
      self.exactMatch = 1                               # 1 == Exact match when matching a LHS, 0 == allow subtyping.
      self.graphRewritingSystem = None			# reference to the Graph Rewriting System that is executing the rules...

   def matches (self, node1, node2):
      "decides if there is a matching between node1 (host graph) and node2 (L or R hand side of rule) (both of type ASGNode)"
      # ......................................................................
      # 1st : Must have the same class
      # ......................................................................

      class1 = node1.getClass()
      class2 = node2.getClass()

      if self.exactMatch:                                     # Added 6 Sept 2002
         if class1 != class2: return 0			 # no match: different classes
      else:
         if not node1.isSubType(node2): return 0         # no match: no subtyping.

      # ......................................................................
      # 2nd: compare the attributes present in dictionary generatedAttributes
      #   * if attribute in node2 has None value -> means ANY value
      #   * if attribute in node2 has a value    -> must compare values...
      # ......................................................................

      for atName in node2.generatedAttributes.keys():                   # iterate on attributes of node1...
         atValue1= node2.getAttrValue(atName).getValue()                # get attribute
         if node2.getAttrValue(atName).isNone():			# None valued...
            pass
         else:								# Must check attribute values
            atValue2= node1.getAttrValue(atName).getValue()                 # get Value of attribute in second node
            if atValue1 != atValue2 :					# They do not match...               
               return 0
            else:
               pass
      return 1

   def createEnumeration (self, obj, set):
      """
         Stores in "set" all the tuples (node1, node2) of connected nodes. This will give the order in which the
         graph will be traversed for subnode matching purposes.
      """
      if not obj.processed:
         obj.processed = 1
         for node in obj.out_connections_:
            element = (obj, node)					# create the tuple...
            if not element in set: set.append(element)			# append element to enumeration list if it is not there
            self.createEnumeration(node,set)				# create the enumeration of each child
         for node in obj.in_connections_:
            element = (node, obj)                                       # create the tuple...
            if not element in set: set.append(element)			# append element to enumeration list if it is not there
            self.createEnumeration(node,set)				# create the enumeration of each child

   def isMatched(self, nodeLHS, subGraphId):
      """
         Checks if nodeLHS has a matching in subGraph, and if this is the case, returns the matching, else returns None
      """
      for nodeTuple in nodeLHS._matched:				# This list contains all the matching for nodeLHS
         graphId, node = nodeTuple					# obtain id of graph and node
         if graphId == subGraphId:					# check if the matching is in graph 'subGraph'
           return node						        # return it
      return None							# matching not found!

   def check(self, A, edge):
      """
         Returns the elements of A (graphs) that have a morphism of edge (i.e. both ends
         of edge match two connected nodes in some graph in A)
      """
      tempSet = []                                                      # Will contain the set of all the subgraphs that have the isomorphism
      for isographTuple in A:   					# for each isomorphism found...
         c0, c1 = None, None
         id, isograph = isographTuple					# each element of A is a tuple ( <id>, subgraph )
         c0 = self.isMatched(edge[0], id)				# see if edge[0] is matched
         if c0:                                                     	# we have found the 1st. node...
            for ch in c0.out_connections_:                          	# look for a matching of the other end of edge
               if ch in isograph and self.isMatched( ch, id) == edge[1]:# we have found it!
                  c1=ch
                  break
            if c1: tempSet.append(isographTuple)
      return tempSet

   def findMatchOutsideGraph(self, edgeMapped, edge2match, graph ):
      """
          Finds a matching of either edge2match[0] or [1] (depending on the value of odgeMapped) in "graph".
          Returns a list of the matched nodes.
      """
      matched = []
      # determine which node we have to match...
      if not edgeMapped[0]:
         node2match = edge2match[0]             			# node to be matched (in LHS)
         alreadyMatched = edgeMapped[1]                                 # Node that is matched (in graph)
         conn2look = alreadyMatched.in_connections_			# where to look for new possible extensions...
      elif not edgeMapped[1]:
         node2match = edge2match[1]					# node to be matched
         alreadyMatched = edgeMapped[0]					# Node that is matched (in graph)
         conn2look = alreadyMatched.out_connections_			# where to look for new possible extensions...
      for ch in conn2look:						# look for node in the list of childs...
         if self.matches( ch, node2match ) and not ch in graph:		# see if any of them matches ''NOT CH IN GRAPH'' is it correct???
            matched.append( ch )					# return it if it does
      return matched							# else we have not found it!

   def findNodeMatchOutsideGraph(self, node2match, graph ):
      """
         Tries to find a match of a node outside 'graph' with node2match. It returns a list of ALL the matching nodes...
      """
      matchings = []
      for node in self.realGraph.listNodes[node2match.getClass()]:	# only look for nodes of same type!
         if self.matches( node, node2match ) and not node in graph:	# see if any of them matches ''NOT CH IN GRAPH'' is it correct???
            matchings.append(node)					# append node to list of matched nodes
      return matchings							# else we have not found it!

   def deleteMatched(self, node, id):
      "removes the nodes in node._matched that are part of graph and viceversa"
      for matchedNode in node._matched:				   	# for each matched node of 'node'
          if matchedNode[0] == id:					# see if the matching corresponds to the given graph...
             node._matched.remove(matchedNode)				# if it is, remove it!

   def removeMatchings (self, graphTuple):
      "removes all matchings to nodes in graph from nodes in LHS"
      id, graph = graphTuple
      for nt in self.LHS.listNodes.keys():				# iterate on LHS
         for node in self.LHS.listNodes[nt]:    			# for all nodes of type <nt>
           self.deleteMatched(node, id)					# remove matchings to subgraph <id>
      for node in graph:             					# Now iterate on all the graph's nodes
         self.deleteMatched(node, id)					# remove the subgraph <id>

   def extend(self, A, edge):
      """
         Tries to extend each subgraph in A with either match of edge[0] or edge[1]
      """
      tempSet = []						# Will contain the set of all the subgraphs that have the isomorphism
      maxId   = self.getMaxID(A)+1
      for isographTuple in A:					# for each tuple ( id, subgraph)...
         id, isograph = isographTuple
         newNode = None
         mapNode1= self.isMatched(edge[0], id)   						# find a matching in isograph of both ends...
         mapNode2= self.isMatched(edge[1], id)   						# find a matching in isograph of both ends...
         if not mapNode1 or not mapNode2:							# if some edge end is not matched in current subgraph
             newNodes = self.findMatchOutsideGraph( (mapNode1, mapNode2), edge, isograph )	# Get a list of matching nodes!\
             if len(newNodes) > 0:								# if list is not empty
                count = 0
                for newNode in newNodes:                           				# found an extension for isograph!
                   if count == len(newNodes) - 1:
                      gId = id
                      newMorphism = isograph
                   else:
                      gId = maxId
                      maxId = maxId + 1
                      newMorphism = []
                      for nod in isograph:							# we must create the node matchings for the 'new morphism'
                         match_id = self.getMatched(id, nod)					# for all nodes in morphism, the matching is the same as in subnode 'id'
                         nod._matched.append((gId, match_id))					# create a new matching of all node...
                         match_id._matched.append((gId, nod))
                         newMorphism.append(nod)
             	   newMorphism.append(newNode)							# append node to graph set
             	   if not mapNode1:								# 1st end was not matched
             	      newNode._matched.append((gId, edge[0]))					# add 1st end to _matched list of newNode
             	      edge[0]._matched.append((gId,newNode))	# add newNode to edge[0]
             	   else:
             	      newNode._matched.append((gId,edge[1]))	# add 2nd end to _matched list of newNode
                      edge[1]._matched.append((gId,newNode))	# add newNode to edge[1]
                   tempSet.append((gId, newMorphism))
                   count = count + 1
             else:
                self.removeMatchings (isographTuple)						# we have not found an extension, so clean the _matched list from the LHS and the realGraph!
         else: self.removeMatchings (isographTuple)						# we have not found an extension, so clean the _matched list from the LHS and the realGraph!
      return tempSet                                            # return only the extended isographs!

   def getMaxID(self, A):
      """ returns the max ID number of all the isomorphisms found """
      maxId = 0
      for iso in A:							# iterate through all the isomorphisms
         id, graph = iso						# unwrap tuple...
         if id > maxId: maxId = id					# get the maximum...
      return maxId

   def extendNode(self, A, node):
      "Tries to extend each subgraph in A with a match of 'node'"
      tempSet = []							# Will contain the set of all the subgraphs that have the isomorphism
      maxId   = self.getMaxID(A)+1
      for isographTuple in A:						# for each tuple ( id, subgraph)...
         id, isograph = isographTuple
         newNodes= self.findNodeMatchOutsideGraph(node, isograph)	# returns a list of the nodes that match
         if len(newNodes) > 0:						# we have found some possible nodes!
            count = 0
            for newNode in newNodes:					# iterate on all of them and create some new morphisms...
               if count == len(newNodes)-1:				# for the last one, we can use isograph, for the rest we must create new subgraphs...
                 gId = id						# set the identifier to id
                 newMorphism = isograph					# pointer to old graph...
               else:
                 gId = maxId						# The ID is the bigger one found...
                 maxId = maxId+1					
                 newMorphism = []                                       # create a new subgraph...
                 for nod in isograph:					# we must create the node matchings for the 'new morphism'
                    match_id = self.getMatched(id, nod)			# for all nodes in morphism, the matching is the same as in subnode 'id'
                    nod._matched.append((gId, match_id))		# create a new matching of all node...
                    match_id._matched.append((gId, nod))
                    newMorphism.append(nod)
               newMorphism.append(newNode)				# add to this new morphism the new node...
               node._matched.append((gId, newNode))			
               newNode._matched.append((gId, node))
               tempSet.append((gId, newMorphism))
               count = count + 1
         else:								# remove from LHS nodes the references to any node in isograph
            self.removeMatchings (isographTuple)			# we have not found an extension, so clean the _matched list from the LHS and the realGraph!
      return tempSet                                            	# return only the extended isographs!

   def createMatchedSlot(self, graph ):
      "Adds and initializes '_matched' slot to the given graph"
      for tip in graph.listNodes.keys():
         for node in graph.listNodes[tip]:
            node._matched = []

   def evaluate (self, graph):
      "tries to find a matching of the left hand side and graph (type ASG)"
      LHSRoot  = self.LHS.root			# get LHS root node
      graphRoot= graph.root			# get graph root
      self.realGraph = graph			# store the graph in which we are going to evaluate the rule...
 
      # .....................................................................
      # Add slot _matched to each node of LHS and graph
      # .....................................................................
      self.createMatchedSlot(self.LHS)
      self.createMatchedSlot(graph)
      # .......................................................................................
      # 1. INITIALIZE A:={h|exists v from graph, label(v)==label(LHSRoot) and h(LHSroot) == v }
      # .......................................................................................
      A = []
      if LHSRoot == None: return [(1,[])]                       # if an empty rule, then success...
      numSubGraphs = 0						# number of subgraphs that we are considering (== mathings found)
      if self.exactMatch:                                       # Added 6 Sept 2002
         LHSRootType = LHSRoot.getClass()		        # get type of LHSroot Node
         if not LHSRootType in graph.listNodes.keys():		# if we don't have nodes of that kind in the graph, we can return a fail...
            return []						# return a fail
         listNodes = graph.listNodes[LHSRootType]               # consider only the nodes of the same type  
      else:                                                     # we have to consider all the nodes!!         
         listNodes = []
         for nt in graph.listNodes.keys():
            listNodes += graph.listNodes[nt]     
      for node in listNodes:			                # for all nodes of the type of the LHSRoot Node
    
        if self.matches(node, LHSRoot):				# Matching of root vertex!
           A.append((numSubGraphs,[node]))   			# create new subgraph. A subGraph is a tuple (<id>, [<list of nodes>])
           LHSRoot._matched.append((numSubGraphs, node))	# add matched node to list of matching nodes... A tuple (<graph-id>, node)
           node._matched.append((numSubGraphs, LHSRoot))	# the same with the matched node in host graph. A tuple (<graph-id>, node)
           numSubGraphs = numSubGraphs+1
      # .......................................................................................
      # 2. SET W = {LHSroot},
      # .......................................................................................
      W = [LHSRoot]
      # ...........................................................................................
      # Prepare the Connected Enumeration (an ordering to cross the LHS graph). This enumeration is
      # a list of tuples (<obj1> <obj2>), where the first element is an edge going from LHSroot.
      # ...........................................................................................
      finished = 0
      while not finished:
         Enumeration = []
         self.createEnumeration(LHSRoot, Enumeration)
         self.LHS.traverse(ASGNode.resetProcessed)
         # .......................................................................................
         # 3. FOREACH EDGE ei=(s,t) IN ENUMERATION
         #   3.1. if s and t in W then A=check(A, ei)
         #   3.2. else A=extend(A,ei)
         #   3.3. W=W U {s,t}
         # .......................................................................................
         for edge in Enumeration:        
            s,t = edge							# unpack both ends of edge
            if (s in W) and (t in W): A=self.check(A,edge)              # if both ends have been processed yet, check that borh ends are in all subgraphs...
            else: A=self.extend(A,edge)					# otherwise, extend subgraphs...
            if not s in W: W.append(s)                                  # Add nodes to set of processed nodes...
            if not t in W: W.append(t)
         # .......................................................................................
         # - check that all nodes in self.LHS are matched, because it is possible to have non-connected
         # graphs in a LHS... But do this check ONLY if there's some possible isomorphism found!
         # .......................................................................................
         if len(A) > 0:							# only if we've found some morphism
            LHSRoot = None							# LHSroot will contain a node inside an unmatched subgraph in the LHS
            for nodeType in self.LHS.listNodes.keys():
               for node in self.LHS.listNodes[nodeType]:
                  if node._matched == []:
                     LHSRoot = node        				# We've found it!
                     break
               if LHSRoot: break					# get out of the outer loop if we've found it
            else: return A						# if we have not found an unconnected graph -> return the set of isomorphisms
         else: return A							# No morphisms found -> return A, which is an empty list...
         # ...................................................
         # Now, try to extend some subgraph in A with LHSNode
         # ...................................................
         A = self.extendNode(A, LHSRoot)				
         finished = len(A) == 0
      return A


   def unMatch(self, graph):
      "given an ASG, removes the attributes '_matched' if any..."
      for nt in graph.listNodes.keys():                                 # for all kind of nodes...
         for node in graph.listNodes[nt]:                               # for all nodes of type <nt>
            if "_matched" in node.__dict__.keys():			# this node is matched...
               del node._matched					# erase attribute

   def condition(self):
      "condition that must hold for the rule to be applicable (must be overriden in childs)"
      pass

   def action(self):
      "Action to be performed when the rule is applied (must be overriden in childs)"
      pass

   def setGraphRewritingSystem(self, grs):
      "Sets the reference to the GRS that is executing the rule"
      self.graphRewritingSystem = grs

   def setGraphGrammar (self, grm):
      "Sets the reference to the GG that is contains the rule"
      self.graphGrammar = grm

   def removeConnections (self, idGraph, node, collection):
     """removes connections that appear on the LHS mapped node but not in the RHS node. node is a RHS node, but has
        a mapped node in LHS"""
     LHSnode = self.getMatched(idGraph, node)			# get mapped LHS node
     # check that all the connections in LHSnode appear also in node, else, delete them
     if collection == "in":
        for el1 in LHSnode.in_connections_:
           # now check that el1._RHSlink is in collection in_connections_ of node
           if "_RHSlink" in el1.__dict__.keys() and not el1._RHSlink in node.in_connections_:
              # connection has dissapeared from RHS... so eliminate it from Host graph
              # ey! again this is not correct, must find out the index of _matched
              HGnodeFrom = self.getMatched(idGraph, LHSnode)	# obtain 1st connection node in Host graph
              HGnodeTo = self.getMatched(idGraph, el1)		# obtain 2nd connection node in Host graph
              if HGnodeTo in HGnodeFrom.in_connections_:
                 HGnodeFrom.in_connections_.remove(HGnodeTo)    # remove connection
              if HGnodeFrom in HGnodeTo.out_connections_:
                 HGnodeTo.out_connections_.remove(HGnodeFrom)      # remove connection
     else:
        for el1 in LHSnode.out_connections_:
           # now check that el1._RHSlink is in collection in_connections_ of node
           if "_RHSlink" in el1.__dict__.keys() and not el1._RHSlink in node.out_connections_:
              # connection has dissapear from RHS... so eliminate it from Host graph
              HGnodeFrom = self.getMatched(idGraph, LHSnode)	# obtain 1st connection node in Host graph
              HGnodeTo = self.getMatched(idGraph, el1)		# obtain 2nd connection node in Host graph
              #HGnodeTo.doPrint()
              if HGnodeTo in HGnodeFrom.out_connections_:
                 HGnodeFrom.out_connections_.remove(HGnodeTo)   # remove connection
              if HGnodeFrom in HGnodeTo.in_connections_:
                 HGnodeTo.in_connections_.remove(HGnodeFrom)    # remove connection

   def addNewConnections (self, idGraph, node, collection, newNodes):
      "1st. add connections appearing in RHS (node) but not in LHS (node._matched)"
      if collection == "in":
         for el1 in node.in_connections_:     
            # now search 'el1' in node._matched...
            if not self.getMatched(idGraph, el1) in self.getMatched(idGraph, node).in_connections_:
               # ey! does not appear in LHS!, add connection in host graph...
               # see if the target node is new...
               if self.getMatched(idGraph, el1) in newNodes:
                  # ey! we have to find out wich element if node._matched[0]._matched we have to look at
                  self.getMatched(idGraph, self.getMatched(idGraph, node)).in_connections_.append(self.getMatched(idGraph, el1))
                  return self.getMatched(idGraph, el1)
                  #self.getMatched(idGraph, el1).out_connections_.append(self.getMatched(idGraph, self.getMatched(idGraph, node)))
               else: # not new, so we have moved a connection, but do it only on this side, as the iteration to change connections is on all nodes!
                  self.getMatched(idGraph, self.getMatched(idGraph, node)).in_connections_.append(self.getMatched(idGraph, self.getMatched(idGraph, el1)))
                  return self.getMatched(idGraph, self.getMatched(idGraph, el1))
		  #self.getMatched(idGraph, self.getMatched(idGraph, el1)).out_connections_.append(self.getMatched(idGraph, self.getMatched(idGraph, node)))
      else:
         for el1 in node.out_connections_:     
            # now search 'el1' in node._matched...
            if not self.getMatched(idGraph, el1) in self.getMatched(idGraph, node).out_connections_:
               # ey! does not appear in LHS!, add connection in host graph...
               # see if the target node is new...
               if self.getMatched(idGraph, el1) in newNodes:
                  self.getMatched(idGraph, self.getMatched(idGraph, node)).out_connections_.append(self.getMatched(idGraph, el1))
                  return self.getMatched(idGraph, el1)
                  # self.getMatched(idGraph, el1).in_connections_.append(self.getMatched(idGraph, self.getMatched(idGraph, node)))
               else: # not new, so we have moved a connection, but do it only on this side, as the iteration to change connections is on all nodes!
                  self.getMatched(idGraph, self.getMatched(idGraph, node)).out_connections_.append(self.getMatched(idGraph, self.getMatched(idGraph, el1)))
                  return self.getMatched(idGraph, self.getMatched(idGraph, el1))
                  #self.getMatched(idGraph, self.getMatched(idGraph, el1)).in_connections_.append(self.getMatched(idGraph, self.getMatched(idGraph, node)))

   def changeAttributes(self, homGraphNode, rhsNode, lhsNode, idGraph ):
      "Replaces the attributes values of homGraphNode with the non-None attributes of rhsNode"
      for attr in rhsNode.generatedAttributes.keys():		# iterate on all the attributes of rhsNode
         atr_rhs = rhsNode.getAttrValue(attr)			# get a rhsNode attribute
         # see if we must copy the matched node value...
         if rhsNode.GGset2Any and attr in rhsNode.GGset2Any.keys():
            atrc = rhsNode.GGset2Any[attr]
            
            # Copy == 'Yes'
            if atrc and atrc.Copy.getValue()[1] == 1:		
               # print "Trying to copy ... ", attr
               # atr_homGraph = homGraphNode.getAttrValue(attr)
               # atr_lhs = lhsNode.getAttrValue(attr)			# get a rhsNode attribute
               # atr_homGraph.setValue(atr_lhs.getValue())		# Copy from LHS
               pass							# Basically, leave it as it is...
            
            # May be we have something in 'Specify'...
            elif atrc and atrc.Specify:							
               # Unwrap value...
               name, lang, kind, act, code = atrc.Specify.getValue()    
               if(code == None):
                 temp = ''
               else:
                 temp = code.replace('\n', '')
                 temp = temp.replace(' ', '')
                 temp = temp.replace('\t', '')
               
               #if code != '' and code != None and code != '\n':  # FOUND DOMETHING IN SPECIFY!!	
               if(temp != ''):
                    functionName   = attr+name                                            # compose function name
                    functionHeader = "def "+functionName+"(self, graphID, mySelf, atom3i):\n"	# compose function header
                    functionBody   = "   " +string.replace(code,'\n', '\n   ')+"\n"	# compose function body
                    try:
                      exec functionHeader+functionBody in self.__dict__, self.__dict__	# 'create' new method
                    except:
                      showerror('GGrule.changeAttributes()',
                                 'Invalid specify attribute code for attribute'
                               + ' "' + attr + '".\n'
                               + 'This occured in rule ' + self.__class__.__name__ 
                               + ' with execution order ' + str(self.executionOrder)
                               + '\nRaising the exception for further details...' )
                      raise
                     
                    method = self.__dict__[functionName]					# obtain a reference to the method
                    result = method(self, idGraph, homGraphNode, self.graphRewritingSystem.parent )  # Modified 25 July 2002, by JL
                    atr_homGraph = homGraphNode.getAttrValue(attr)      			# get the homomorphic graph attribute...
                    atr_homGraph.setValue(result)
               
               # Found nothing in specify
               else:			
                  atr_homGraph = homGraphNode.getAttrValue(attr)  # get the homomorphic graph attribute...
                  atr_homGraph.setValue(atr_rhs.getValue())				# do the replacement
            
            # No specify... so change value
            else:                                                                       
               atr_homGraph = homGraphNode.getAttrValue(attr)      			# get the homomorphic graph attribute...
               atr_homGraph.setValue(atr_rhs.getValue())				# do the replacement
         
         # check if it is not None (None means <ANY> value)
         elif not atr_rhs.isNone():							
            atr_homGraph = homGraphNode.getAttrValue(attr)      # get the homomorphic graph attribute...
            atr_homGraph.setValue(atr_rhs.getValue())		# do the replacement

   def getMatched(self, idGraph, node):
      """
         Given a (LHS) node, returns the matched node corresponding to the graph identified by <idGraph>
      """
      if(node == None):
         print 'ERROR: GGrule.getMatched() was given a "None" node as an argument!'
         print 'This occured in rule', self.__class__.__name__, \
               'with execution order', self.executionOrder, '\nReturning None'         
         showerror('GGrule.getMatched()', 'Cannot do match on a "None" node argument\n'
                   + 'This occured in rule ' + self.__class__.__name__ 
                   + ' with execution order ' + str(self.executionOrder)
                   + '\nReturning None' )
         return None
      for matchNodeTuple in node._matched:			# look over all tha matched tuples...
         idGraphMatch, matchNode = matchNodeTuple		# unwrap graph-id, and matched node
         if idGraph == idGraphMatch:				# if the matching is to the given subgraph...
            return matchNode					# returns the node (AND NOT THE TUPLE)
      return None					

   def replaceSides (self, parent, homGraphTuple, realGraph, moveEntities, graphics):
      """
         Once an homomorphic graph has been found, do the replacement (LHS by RHS)
      """
      # first check if we must add a new meta-model to the current one

      if self.RHS:
         metaModels = [self.RHS.getClass()]
         for mm in self.RHS.mergedASG:
           metaModels.append(mm.getClass())

         for mmodel in metaModels:
            if not realGraph.hasMetaModel(mmodel):		# that means we need to merge with a new meta-model
               parent.openMetaModel(mmodel[4:], 1, 0)
               #exec "from "+mmodel+" import *\n"
               #realGraph.merge(eval(mmodel)())

      else: return						# A void Right Hand Side means no replacement
      idHomGraph, homGraph = homGraphTuple			# unwrap id of graph and list of graph nodes
      # .....................................................................
      # Add slot _matched to each node of RHS
      # .....................................................................
      self.createMatchedSlot(self.RHS)
      nodes2remove = []								# keep track of nodes that must be deleted from homGraph!
      # ....................................................................
      # FOREACH NODE IN homGraph
      #   Get mapped node in LHS
      #   If it is also in RHS, then do nothing but calculate attribs values
      # ....................................................................
      for node in homGraph:                             			# for each node in graph
         mappedNode = self.getMatched(idHomGraph,node)  			# get LHS matched node
         label = mappedNode.GGLabel.getValue()          			# get Label of LHS Node
         rhsNode = self.RHS.findLabel( label)           			# try to find node
         if rhsNode:                                    			# node exists...
            rhsNode._matched.append((idHomGraph,mappedNode))   			# set link to LHS node
            mappedNode._RHSlink = rhsNode					# link from LHS to RHS...
            self.changeAttributes(node, rhsNode, mappedNode, idHomGraph) 	# change the attribute's value of node in homGraph
         else:                                          			# node does not exist (has been eliminated!)
            parent.deleteGraphicsOfSemanticEntity(node)				# delete node from graphics
            node.removeNode( )                          			# eliminate node from real graph
            nodes2remove.append(node)						# add node 2 list of nodes to remove
      # now iterate on nodes2remove to remove them from homGraph
      for nod in nodes2remove:
         homGraph.remove(nod)

      # Now walk right hand side and create new nodes
      newNodes = []
      for nt in self.RHS.listNodes.keys():              	     # for all kind of nodes...
         for node in self.RHS.listNodes[nt]:            	     # for all nodes of type <nt>
            if not node._matched:				     # Does not appear on LHS, so it is a new node...
               # Create New Node on real graph...
               newNode = node.clone()                   	     # create a new copy of node
               newNode.objectNumber = newNode.getLastObjectNumber()  # Beware! the object number must not be the same!!
               newNode.in_connections_=[]			     # empty input connections
               newNode.out_connections_=[]			     # empty output connections
               newNode._matched = []				     # create an empty list of matched nodes
               realGraph.addNode (newNode)              	     # add node to graph
               node._matched.append((idHomGraph,newNode))	     # hey! if it is a new node, _matched[0] points DIRECTLY to a node in the host graph
               newNode._matched.append((idHomGraph,node))	     # Something with the new node of Host graph...points DIRECTLY to a node in RHS (NOT LHS as the others)
               newNodes.append(newNode)				     # Put new node in set of new nodes
               homGraph.append(newNode)				     # add node to homomorphic graph (2nd component of tuple!)...
               self.changeAttributes(newNode, node, None, idHomGraph) # set attributes (LHSnode is None, because it is a new NODE)
      # Walk right hand side and set connections
      newSemanticConnections = []
      for nt in self.RHS.listNodes.keys():              	# for all kind of nodes...
         for node in self.RHS.listNodes[nt]:            	# for all nodes of type <nt>
            if self.getMatched(idHomGraph,node) in newNodes:    # it is a new node, just copy mapped connections from RHS
               for element in node.in_connections_:     	# walk through input connections
                  if self.getMatched(idHomGraph,element) in newNodes:
                     if not self.getMatched(idHomGraph,element) in self.getMatched(idHomGraph,node).in_connections_:
                        self.getMatched(idHomGraph,node).in_connections_.append(self.getMatched(idHomGraph,element))
                  else:
                     if not self.getMatched(idHomGraph, self.getMatched(idHomGraph,element)) in self.getMatched(idHomGraph,node).in_connections_:
                        self.getMatched(idHomGraph, node).in_connections_.append(self.getMatched(idHomGraph, self.getMatched(idHomGraph,element)))
               for element in node.out_connections_:    # walk through input connections
                  if self.getMatched( idHomGraph, element ) in newNodes:
                     if not self.getMatched( idHomGraph, element ) in self.getMatched( idHomGraph, node ).out_connections_:
                        self.getMatched( idHomGraph, node ).out_connections_.append(self.getMatched( idHomGraph, element ))
                  else:
                     if not self.getMatched(idHomGraph, self.getMatched(idHomGraph,element)) in self.getMatched(idHomGraph,node).out_connections_:
                        self.getMatched( idHomGraph, node ).out_connections_.append(self.getMatched(idHomGraph, self.getMatched(idHomGraph,element)))
            else:                                       # it is a replacement
               # ...........................................................................
               # 1st. add connection appearing in RHS (node) but not in LHS (node._matched)
               # a) in in_connections_
               # ...........................................................................
               c = self.addNewConnections (idHomGraph, node, "in", newNodes)
               if(c):
                 newSemanticConnections.append(c)
               # ...........................................................................
               # b) in out_connections_
               # ...........................................................................
               c = self.addNewConnections (idHomGraph, node, "out", newNodes)
               if(c):
                 newSemanticConnections.append(c)
               # ...........................................................................               
               # 2nd. eliminate connections appearing in LHS (node._matched) but not in RHS (node)
               # a) in in_connections_
               # ...........................................................................
               self.removeConnections (idHomGraph, node, "in")
               # ...........................................................................
               # b) in out_connections_
               # ...........................................................................
               self.removeConnections (idHomGraph, node, "out")
      # print " *** Host Graph"
      #realGraph.traverse(ASGNode.doPrint)
      # update graphical attributes...
      if graphics != 0:											# if working with graphics, update the attributes
        self.updateGraphicalAttributes(parent, homGraphTuple, realGraph, 
                                       newNodes, moveEntities, 
                                       newSemanticConnections)

        # Apply any relevent QOCA constraint rules
        # NOTE: normally QOCA activated by ASG.addNode(), but when we did
        # this a few dozen lines of code above, graphObject_ was not ready
        for node in newNodes:
          if(hasattr(node, 'QOCA')):
            try:
              node.QOCA(None)
            except:
              pass

   def updateGraphicalAttributes(self, parent, homGraphTuple, realGraph, 
                                 newNodes, moveEntities, 
                                 newSemanticConnections):
      """
         Updates graphical attributes once the replacement has been done.
      """
      idHomGraph, homGraph = homGraphTuple                                              # unwrap subraph id and subgraph node list
      for node in homGraph:             						# for each mapped node...
         if node in newNodes:           						# ey! new node!
            # get RHS node to obtain coordinates
            #RHSnode = self.getMatched(idHomGraph, node)
            #x, y = RHSnode.graphObject_.x, RHSnode.graphObject_.y
            x, y = self.positionNode(node, idHomGraph)
            node.graphObject_ = node.graphClass_(x, y,node)                                # create new graphical object!
            node.graphObject_.DrawObject(parent.UMLmodel)				# draw it
            parent.UMLmodel.addtag_withtag(node.getClass(), node.graphObject_.tag)	# add appropriate tags to canvas
         elif moveEntities:                                                             # Not new, but update position (if moveEntities != None)...
            LHSNode = self.getMatched( idHomGraph, node)                                # get LHS node...
            RHSNode = self.getMatched( idHomGraph, self.getMatched( idHomGraph, node))  # get RHS node...
            dx = LHSNode.graphObject_.x-RHSNode.graphObject_.x                          # begin to calculate displacement to apply
            dy = LHSNode.graphObject_.y-RHSNode.graphObject_.y
            parent.UMLmodel.addtag_withtag( "selected", node.graphObject_.tag )         # select the node we want to move...
            if (node.graphObject_.x+dx < 200) and (node.graphObject_.x+dx > 0) and (node.graphObject_.y+dy < 200) and (node.graphObject_.y+dy > 0):
               parent.initDragX = dx
               parent.initDragY = dy
               parent.moveBox(node.graphObject_.x+dx, node.graphObject_.y+dy)           # if inside canvas coords, move it!
            parent.UMLmodel.dtag(ALL, "selected")                                       # delete the selected tag from the items

 
      # grab the current position of the graphical connections
      parent.ASGroot.destroyNodes()		
      for ntype in parent.ASGroot.listNodes.keys():
         # iterate only on the homomorphic graph nodes!
         for node in parent.ASGroot.listNodes[ntype]:					
            node.graphObject_.deleteGraphicalConnections()
   
      # This will magically make the new/modified connections happen
      parent.ASGroot.writeContents(parent, 1, 0)

      # modify the graphical attributes appearance!
      for node in homGraph:						# iterate only on the homomorphic graph nodes!
         for visualAttr in node.graphObject_.attr_display.keys():
            node.graphObject_.ModifyAttribute(visualAttr, 
                                     node.__dict__[visualAttr].toString(16,5))

      # now, execute Post-Conditions on EDIT!
      for node in homGraph:						# iterate only on the homomorphic graph nodes!
        node.graphObject_.postCondition(ASG.EDIT)
        
      # Some layout...     
      if(newSemanticConnections):
        selectedLinks = []
        for newLink in newSemanticConnections:
          selectedLinks.append(newLink.graphObject_)
        from Utilities import optimizeLinks
        optimizeLinks( parent.cb, True, 9, selectedLinks  )
      
#      print parent.__class__.__name__
#      from ForceTransfer import applyLayout as FTA
#      FTA(parent)
##      print 'applied FTA'
#      from Utilities            import optimizeLinks
#      from ModelSpecificCode    import isConnectionLink
#      selectedLinks = []
#      for otype in parent.ASGroot.listNodes.keys():
#          for node in parent.ASGroot.listNodes[otype]:
#            if(node.graphObject_ and node.graphObject_ 
#                and isConnectionLink(node.graphObject_)):
#              selectedLinks.append(node.graphObject_)
#      optimizeLinks( parent.cb, True, 15, selectedLinks  )
##      print 'applied AO'

   def positionNode(self, node, idHomGraph):
    """
    Attempts to place a node created by the graph grammar near whatever this
    node is connecting to. If not connected, then it will be placed in the
    rather random fashion used before this method was added...
    Created by Denis Dube, summer 2005 
    """
    # Get the coordinates of everything this node connects too
    xCoords = []
    yCoords = []
    allConn = node.in_connections_ + node.out_connections_
    for link in allConn:
      allLinkedConn = link.in_connections_ + link.out_connections_
      for linkedNode in allLinkedConn:
        if(linkedNode != node and linkedNode.graphObject_):
          xCoords.append(linkedNode.graphObject_.x)
          yCoords.append(linkedNode.graphObject_.y)
    
    # We should have X and Y coords from connected entities...
    # If not, fall back to the old method
    if(not xCoords):
      #print 'no coords using old method to place node'
      RHSnode = self.getMatched(idHomGraph, node)
      x, y = RHSnode.graphObject_.x, RHSnode.graphObject_.y
      return (x, y)
      
    # Find the midpoint of all the gathered entities, place new node there
    xAvg = 0
    yAvg = 0
    for i in range(0, len(xCoords)):
      xAvg += xCoords[i]
      yAvg += yCoords[i]
    xAvg = float(xAvg) / float(len(xCoords))
    yAvg = float(yAvg) / float(len(yCoords))
#    print 'Placing node at', (xAvg, yAvg)
#    print 'node', node.__class__.__name__
    return (xAvg, yAvg)
    