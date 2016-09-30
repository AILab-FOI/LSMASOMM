# __ File: ASG.py ____________________________________________________________
#  Implements  : class ASG
#  Author      : Juan de Lara
#  Description : Base (Abstract) class for Abstract Syntax Graphs
#  Modified    : 23 Oct 2001
#  Changes :
#   - 23 Oct 2001 : comments added
#   - 20 Jul 2002 : Added an optional parameter to method writeContents
#   - 22 Jul 2002 : Added the invalid method, which in the case that the graph 
#                   is a LHS or RHS
#     checks that labels are unique.
#   - 27 Jul 2002 : Corrected bug in unMerge.
# ____________________________________________________________________________

import os
import stat
import sys
import time
import string
import Dialog
from tkMessageBox import askokcancel
from copy import copy as cloningMachine

from ASGNode                  import *
from graph_ExternalConnection import *
from graphLink                import *
from ConstraintLoader         import ConstraintLoader  
from ModelSpecificCode        import isConnectionLink
from Utilities                import snapNewEntity
from FilePaths                import USER_NAME
from Qoca.constraints.QocaSolverAbstract import isAbstract as isNotUsingQoca

import ZoomFocus
import ForceTransfer



class ASG (ASGNode):
  # Some useful static constants
  EDIT       = 0
  SAVE       = 1
  CREATE     = 2
  CONNECT    = 3
  DELETE     = 4
  DISCONNECT = 5
  TRANSFORM  = 6
  SELECT     = 7
  DRAG       = 8
  DROP       = 9
  MOVE       = 10

  def __init__(self, metaModelName, rootASGNode, nodeTypes):   # creates a root node for the tree
      "creates a root node for the tree and a dictionary to store list of the nodes"
      ASGNode.__init__(self)
      self.metaModelName = metaModelName# the name of the MetaModel (file with the buttons)
      self.root      = rootASGNode
      self.listNodes = {}		# the dicitionary must be looked-up by the type of the node, it returns a list of all
      # the nodes of that type
      self.nodeTypes = nodeTypes
      self.constraints = {}		# dictionary of the constraints implementd, searchable by the name of the constraint
      for nt in nodeTypes:              # initialize the dictionary with the node types
          self.listNodes[nt] = []
          
      self.minimumGG = 0		# The minimum GG Label so far (Added 30 July 2002, JL)
      self.mergedASG = []		# ASGs with which this ASG is merged
      
      #--- Denis added parallel data structure for tracking ASG's, 2005 -----
      # Structure:  { modelName_META : [ ASG, nodeTypes, attributeKeys ] }
      # This is a private dictionary, no messing around with it outside this file
      self.__trackASG = dict()
      ##self.__addNewASG2Tracker( metaModelName, self )
      # Keep track of attributes that are mashed up in the merging process
      self.__collidedAttributeTracker = dict()
      # Keep track of actual attribute values (no mashing here!)
      self.__trackAttributes = dict()
      
      # List of nodes (links) added when ATOM3 is loading a model
      self.newLinkNodeQueue = []
      
      self.isInsideGraphGrammar = False     
     
     
  def trackNewASGroot( self, ASGgraph, metaModelName ):
      """
      Keeps track of various attributes in multi-formalism environment by using
      a data-structure that works in parallel to the older system which mangles
      attributes and ASG's left, right, and center!
      This is the front-end to the system, accessed when a meta-model is loaded
      Created March 2005 by Denis
      """      
      # Track the actual ASG
      self.__addNewASG2Tracker( metaModelName, ASGgraph )
      # Track the ASG's generated attributes
      self.__addNewAttr2Tracker( ASGgraph, metaModelName )
      
      # Need to fix this up... and maybe add actions?
      self.preCondition( ASG.CREATE )
      self.postCondition( ASG.CREATE )
            
  def merge(self, ASGgraph ):
      """
         Merges this ASG with another ASG
         This is very bad, should have a dictionary of ASG's and no root
         Would be highly flexible and no attribute collisions! - Denis
      """
          
      self.mergedASG.append(ASGgraph)					# add the graph to the list of merged graphs
      for nodeType in ASGgraph.listNodes.keys():
         if not nodeType in self.listNodes.keys():			# node type was not known
            self.listNodes[nodeType] = ASGgraph.listNodes[nodeType]
            self.nodeTypes.append(nodeType)
         else:                                                     	# node type existed...
            for node in ASGgraph.listNodes[nodeType]:			# add each node of merged graph to actual graph
               self.listNodes[nodeType].append(node)
      
      # copy also the model's attribute
      errors = []
      for attr in ASGgraph.generatedAttributes.keys():
        if attr in self.generatedAttributes.keys():                     # Attribute is present!
            #print "Attribute collision for ", attr, "<-- New attribute value ignored"         
            errors.append(attr)
            if( not self.__collidedAttributeTracker.has_key( attr ) ):
              self.__collidedAttributeTracker[ attr ] = 1
            else:
              self.__collidedAttributeTracker[ attr ] += 1
            continue
        self.generatedAttributes[attr] = ASGgraph.generatedAttributes[attr]
        # now create the attribute!
        self.setAttrValue(attr, ASGgraph.getAttrValue(attr).clone())
      if( errors ):
        print 'Attribute name collisions occured during load (could affect '\
              + 'old formalisms)\nThe following attributes collided: '\
              + str(errors)        
        ## print 'In fact, these messages are slated for removal, as this ' \
              ## 'attribute system is being bypassed to fix this problem'

  def unMerge(self, ASGgraph, metaModelName=None, atom3i=None ):
      """
         de-merges this ASG with the given ASG.
         returns 0 if we do not have an ASG with the same type as ASGgraph, 
         or -1 if we cannot delete the ASG because we have instances of 
        some entity defined by ASGgraph. 1 otherwise.
      """
      
      #--- Denis added parallel data structure for tracking ASG's, 2005 -----
      self.__deleteASG2Tracker( metaModelName )
           
      # 1st check if the type of ASGgraph is our own type -> 
      # so erase ourselves and return another ASG
      if self.getClass() == ASGgraph.getClass(): 
        return self.selfUnMerge( atom3i=atom3i )
      
      # 2nd check if we have this ASGgraph
      isPresent = 0
      ASGClass  = ASGgraph.getClass()
      for midx in self.mergedASG:
        if midx.getClass() == ASGClass:
           isPresent = 1
           break
      if not isPresent: return 0
      
      # now check that we do not have instances of the entities of the ASG to delete
      canDelete = 1
      for entity in midx.listNodes.keys():
        if self.listNodes[entity] != []:
          canDelete = 0
          break
        
      ##if not canDelete: return -1
#----------------- Lets delete everything anyway, Denis, 2005 ------------------      
      if( not canDelete and not askokcancel( 
            'WARNING: Deleting '+metaModelName,
            'If you press OK all things '+metaModelName 
            +' will be cleanly and utterly removed\n\n' 
            +'If you CANCEL, then the formalism will be half-kept,'+
            ' half-removed (this dialog appears to late too stop this) \n\n'
            +'CANCEL IS NOT RECOMMENDED'
            + ' (Almost 100% sure bad things will happen to you)') ):
          return -1
        
      self.mergedASG.remove(midx)
      
      # For each entity in the ASG that's going bye bye
      for entity in midx.listNodes.keys():
        # Remove from nodes list
        if( self.listNodes.has_key( entity )  ):
          # If object has an associated graphical object, kill it
          for obj in self.listNodes[ entity ]:
            if( obj.graphObject_ and atom3i): obj.graphObject_.erase(atom3i) 
          # Kill all the semantic objects of this type
          del self.listNodes[ entity ]

        # Remove from types list
        if( entity in self.nodeTypes ):
          del self.nodeTypes[ self.nodeTypes.index( entity ) ]
      
      # Remove generated attributes that aren't needed no more..
      for genattr in midx.generatedAttributes.keys():
        # If this is a collided attribute, then remove it from the tracking
        # NOTE: This will work for N model collisions of M attributes
        CAT = self.__collidedAttributeTracker
        if( CAT.has_key( genattr ) ): 
          if( CAT[ genattr ] == 1 ): del CAT[ genattr ]
          else:                          CAT[ genattr ] -= 1
        else:                         
          # Safely destroy this attribute, NO ONE, uses it now
          del self.generatedAttributes[genattr]
          
      return self
#---------------------------- Denis hack ends here -----------------------------
                
      # now proceed to erase the ASG from mergedASG, the entity types and the generatedAttributes...
      ## self.mergedASG.remove(midx)
      ## for entity in midx.listNodes.keys(): del self.listNodes[entity]
      ## for genattr in midx.generatedAttributes.keys(): del self.generatedAttributes[genattr]
      ## return self

  def selfUnMerge(self, atom3i=None ):
      """
         Same as unMerge but the current ASG is who has to be erased!.
         returns 0 if we do not have anything merged, -1 if we have instances of entities specific of
         our types and another ASG if we can be de-merged.
      """
      if (not self.mergedASG) or self.mergedASG == []: 
        return 0
      # check that we can be erased (do not have instances of entities specific of this ASG)
      exec "from "+self.getClass()+" import "+self.getClass()+"\n" \
                                     in self.__dict__, self.__dict__   
      anASG = eval(self.getClass()+"(parent)", self.__dict__, self.__dict__)   # modified 27/July/2002 by JL
      canDelete = 1
      for entity in anASG.listNodes.keys():
        if self.listNodes[entity] != []:
          canDelete = 0
          break

      ##if not canDelete: return -1
#----------------- Lets delete everything anyway, Denis, 2005 ------------------
      if( not canDelete and not askokcancel( 
            'WARNING: Deleting the root formalism',
            'If you press OK, everything in the root formalism'
            +' will be cleanly and utterly removed\n\n' 
            +'If you CANCEL, then the formalism will be half-kept,'+
            ' half-removed (this dialog appears to late too stop this) \n\n'
            +'CANCEL IS NOT RECOMMENDED'
            + ' (Almost 100% sure bad things will happen to you)' ) ):
          return -1
        
      # For each entity in the ASG that's going bye bye
      typeList = self.__getTypeListByASG( self )
      for entity in typeList:#anASG.listNodes.keys():
        # Remove from nodes list
        if( self.listNodes.has_key( entity )  ):
          # If object has an associated graphical object, kill it
          for obj in self.listNodes[ entity ]:
            if( obj.graphObject_ and atom3i): 
              obj.graphObject_.erase(atom3i) 
          # Kill all the semantic objects of this type
          del self.listNodes[ entity ]

        # Remove from types list
        if( entity in typeList): #self.nodeTypes ):
          del self.nodeTypes[ self.nodeTypes.index( entity ) ]
      
#---------------------------- Denis hack ends here -----------------------------

      # now merge the 1st merged ASG with the rest
      ASG2return = self.mergedASG[0]
      for merg in self.mergedASG[1:]: 
        ASG2return.merge(merg)
      # and copy the entities...
      for entity in ASG2return.listNodes.keys():
        ASG2return.listNodes[entity] = self.listNodes[entity]
      
      # Make sure the returned ASG knows about the new tracking mechanism
      ASG2return.__trackASG = self.__trackASG
      ASG2return.__trackAttributes = self.__trackAttributes
      return ASG2return      

  def hasMetaModel(self, metaModel):
      """
      returns 1 if metaModel (a string) is one of the meta-models that are 
      loaded
      """
      if self.getClass() == metaModel: return 1				# if the meta model is the actual class
      for mmodels in self.mergedASG:					# else check the merged meta-models
         if mmodels.getClass() == metaModel: return 1
      return 0

  def open(self):
      """
      Method to open an ATOM3 instance to edit the entities 
      (can be overwritten in children)
      """
      ATOM3Type.show(self, parent, topWindowParent)
      return ATOM3(topWindowParent, None , 0, 1, self)

  def getRoot(self):			# returns the root of the tree
      "returns the root of the tree"
      return self.root

  def setRoot(self, newRootNode):	# sets the new root node
      "sets the new root node"
      self.root = newRootNode

  def doPrint(self):			# prints each node of the tree
      "prints each node of the tree"
      self.root.clearPrint()
      self.root.doPrint()

  def traverse(self, functionToApply):
      "Traverses the tree applying the funtion 'functionToApply' to all nodes"
      for nt in self.listNodes.keys():              	# for all kind of nodes...
         for node in self.listNodes[nt]:            	# for all nodes of type <nt>
            functionToApply(node)
      
      
  def remove(self, node):
      "removes the node from the graph..."
      nl = self.listNodes[node.getClass()]
      if node in nl: nl.remove(node)

  def getValue(self, attribute):
      "returns the value associated with that attribute"
      return self.__dict__[attribute]


  #def genAttributesCode(self, file):
  #    "Generates code for the attributes value"
  #    # generate the constructor call...
  #    for attr in self.generatedAttributes.keys():				  	 # for each generated attribute
  #        self.getValue(attr).writeValue2File ( file, '    ', 'self.ASGroot.'+attr )	 # write its value to file

      
      

  def isHierarchical(self):
      "Decides if it is a Hierarchical graph..."
      for type in self.listNodes.keys():
         if type[:4] == 'ASG_':                 				# All model names begin with ASG_
            for node in self.listNodes[type]:   				# see if it is a subclass of ASG
               if node.isSubclass(node, 'ASG'): return 1                        # has node that is an ASG
      # No see if we are examining a sub-model
      if self.rootNode != None:							# that means we are not the root node!
         return 1
      return 0

  def writeImports2File(self, file, indent = "    "):
      """
         Writes the necessary imports for the entities belonging to the ASG.
         Added 10 Dec 2002.
      """
      # import each entity and its associated graphical file
      for obj in self.listNodes.keys():
         file.write(indent+"from "+obj+" import "+obj+"\n")
         if not obj[0:4] == "ASG_":
            file.write(indent+"from graph_"+obj+" import graph_"+obj+"\n")

  def writeGraph2File(self, file, genGraph=1, isRootNode=0, rootNodeName = "rootNode", \
      indent="    ", genConstraints = 0, fileName = '', genGGcode = 0, parentName="self", \
      genImports = 0, depth = 1, nodesToGenList = [] ):
      """
         Writes the graph into a file
      """

      # generate code for the nodes...
      counter =0
      if( not nodesToGenList ):
        for nodetype in self.nodeTypes:						# iterate on all the node types...
          for node in self.listNodes[nodetype]:					# Iterate on all the nodes of each type
            node.genAttributesCode(file, genGraph, None, isRootNode, rootNodeName, indent, genConstraints, 1, genGGcode, parentName, genImports, depth + 1 )
            if self.isSubclass(node, 'ASG'):					# if it is a subclass of ASG, ws should include the file generated (hierarchical modeling)
              newFile = fileName+str(counter)
              file.write(indent+'exec "from '+newFile+' import '+newFile+'\\n" in self.__dict__, self.__dict__\n')
              file.write(indent+'self.'+newFile+'(self, self.obj'+str(node.objectNumber)+') \n\n')
              counter = counter + 1
      else:
        for node in nodesToGenList:				
          node.genAttributesCode(file, genGraph, None, isRootNode, rootNodeName, indent, genConstraints, 1, genGGcode, parentName, genImports, depth + 1 )
          if self.isSubclass(node, 'ASG'):					# if it is a subclass of ASG, ws should include the file generated (hierarchical modeling)
            newFile = fileName+str(counter)
            file.write(indent+'exec "from '+newFile+' import '+newFile+'\\n" in self.__dict__, self.__dict__\n')
            file.write(indent+'self.'+newFile+'(self, self.obj'+str(node.objectNumber)+') \n\n')
            counter = counter + 1
            
            
      # if fileName has a value, we are saving a model, we must generate a function to hold the connections...
      if fileName != '':
         # if we are not dealing with a hierarchical model, an extra method is not needed..
         hierarchical = self.isHierarchical()
         if hierarchical:
            file.write('\ndef '+fileName+'_connections(self, rootNode):\n')


      #-------- Modified by Ximeng Sun / Apr 9,2005 for large conn nums --------
      file.write('\n')
      writed = 0
      # generate code for the connections...
      if( not nodesToGenList ):
        for nodetype in self.nodeTypes:
          for node in self.listNodes[nodetype]:
            if isRootNode: 
              if(node.__dict__.has_key('name')):
                debugName = ' named ' + node.name.toString() + '\n'
              else:
                debugName = ' of type ' + node.__class__.__name__ + '\n'
              file.write(indent+'# Connections for obj'+str(node.objectNumber)
                +' (graphObject_: '+node.graphObject_.tag + ')' + debugName)
              file.write(indent+'self.drawConnections(\n')
            res = node.genConnectionsCode(file, genGraph, isRootNode, 
                                          indent, 1, writed)
            if isRootNode: 
              file.write(' )\n')
      else:
        for node in nodesToGenList:
          if isRootNode: file.write(indent+'self.drawConnections(')
          res = node.genConnectionsCode(file, genGraph, isRootNode, indent, 1, 
                                        writed, nodesToGenList = nodesToGenList)
          if isRootNode: file.write(' )\n')
      file.write('\n')
      #------------ End of modification by Ximeng Sun / Apr 9,2005 -------------
                 
      
      # if rootNode and I'm generating a function (filename != '')
      # then call subModel's functions for connections...
      if isRootNode and fileName != '':                         # if main model
         counter = 0
         if( not nodesToGenList ):
           for nodetype in self.nodeTypes:                        # iterate, to search for all submodels
             for node in self.listNodes[nodetype]:
               if self.isSubclass(node, 'ASG'):                 # found a submodel
                 file.write(indent+'self.'+fileName+str(counter)+'_connections( self, self.obj'+str(node.objectNumber)+')\n')
                 writed = 1
                 counter = counter + 1
         else:
           for node in nodesToGenList:
             if self.isSubclass(node, 'ASG'):                 # found a submodel
               file.write(indent+'self.'+fileName+str(counter)+'_connections( self, self.obj'+str(node.objectNumber)+')\n')
               writed = 1
               counter = counter + 1
        
        
      if fileName != '' and (not writed) and hierarchical:        # we must write 'pass', because nothing has been writed in the function!!
         file.write(indent+'pass\n')

  def removeContents( self, atom3i, genGraphicalInfo = 1):
      "removes the contents of graph form ATOM3 drawing canvas"
      for otype in self.listNodes.keys():
         listNodes = self.listNodes[otype]					# get the list of objects...
         for obj in listNodes:                          			# for each object, delete from drawing canvas
             if obj.graphObject_:						# if object has an associated graphical object
               obj.graphObject_.erase(atom3i)                                   # erase the graphical object
      # now remove physically from memory...
      for otype in self.listNodes.keys():
         listNodes = self.listNodes[otype]					# get the list of objects...
         while len(listNodes) > 0:
            del listNodes[0]
         self.listNodes[otype] = []

  def createExternalConnection (self, atom3i, fromClass, toClass, objFrom, objTo, From = 1 ):
      "Creates an external connection between objFrom and objTo"
      # ..............................................................................................
      # create an 'externalConnection" object
      # ..............................................................................................
      # 1st.: decide the position to be created...
      xpos, ypos = 0, 0
      x, y = objFrom.graphObject_.getCoordsVertex()
      if x < 350: xpos = 110
      else: xpos = 577

      if y < 250: ypos = 85
      else: ypos = 425

      # 2nd. create the object, add the tag of peer's model

      gobj = graph_ExternalConnection(xpos, ypos)
      gobj.DrawObject(atom3i.UMLmodel)
      gobj.semanticObject = objTo.rootNode			# link to the model of peer node
      modelTag = objTo.rootNode.getClass()
      atom3i.UMLmodel.addtag_withtag(modelTag, gobj.tag)

      # 3rd. connect (only graphically) both objects

      if From == 1: atom3i.showConnection( fromClass, gobj.tag)
      else: atom3i.showConnection( gobj.tag, toClass)

  def getNumberOfDrawn(self, objDest, list):
      number = 0
      for tuple in list:
         if tuple[0] == objDest and tuple[1] != None: number = number + 1
         if tuple[1] == None: return number
      return number

  def setConnectionHandler (self, handler, obj, list):
      index = list.index((obj, None))
      list[index] = (obj, handler)

  def writeContents( self, atom3i, genGraphicalInfo = 1, rewriteObjects = 1, objects2Show = [] ):
      """
         Calls the ATOM3 API to show its contents.
         The last parameter can be a list of objects, and then only these objects are shown (added 20 July 2002, JL)
      """
      obj2show = []
      if objects2Show == []:                            # Then show all objects...
        for otype in self.listNodes.keys():             # fill objects2Show list with all the objects in the graph
          for obj in self.listNodes[otype]:
            obj2show.append(obj)
      else: obj2show = []+objects2Show

      if rewriteObjects:
        for obj in obj2show:                       	# for each object, show itself
           atom3i.drawEntity(obj, obj.getClass())
	   obj.graphObject_.isDestroyed = 0		# un set the destroy flag (Added 30 July 2002)

      if genGraphicalInfo:

         # .............................................................................
         # Repeat the iterations, this time to show the connections...
         # .............................................................................

         # 1st. : to each connection in "in_connections_" and "out_connections_" convert it in a tuple (<Obj>, handler)
         #        For the moment set the handler to None (because it has not been drawn yet). Create also in the graphical
         #	  objects a dictionary to store the new handler information
         for obj in obj2show:
              for index in range(len(obj.in_connections_)):
		obj.in_connections_[index] = ( obj.in_connections_[index], None)
	      for index in range(len(obj.out_connections_)):
		obj.out_connections_[index] = ( obj.out_connections_[index], None)
              obj.graphObject_.OLD_out_connections_Points = {}
	      for handler in obj.graphObject_.out_connections_Points.keys():
	        obj.graphObject_.OLD_out_connections_Points[handler] = obj.graphObject_.out_connections_Points[handler]
	      obj.graphObject_.out_connections_Points = {}
	      obj.graphObject_.connections = []				# delete the graphical connections

         # 2nd. : Iterate over the objects, drawing each connection, if it has not been drawn yet

         for obj in obj2show:                       					# for each object...
               fromClass = obj.graphObject_.tag                                                 # get if of the origin of the connection
               for peerTuple in obj.out_connections_:						# for each connection (<peer>, handle) of each object...
                  peer, handle = peerTuple							# unwrap tuple...
                  if type(peer.in_connections_[0]) == TupleType:
                     if handle == None:								# do not do anything if the connection's been drawn yet...
                        toClass   = peer.graphObject_.tag					# get connection destination
                        connCounter = self.getNumberOfDrawn(peer, obj.out_connections_)      	# number of connections to that object drawn so far
                        ret = obj.graphObject_.getInfoTuple(fromClass, toClass, connCounter+1, obj.graphObject_.OLD_out_connections_Points) 	# obtain connection information ....
                        if ret:
                            infoTuple, oldHandler = ret
                            interPts, smoothConn, num1st = infoTuple[2:]
                            x0, y0, x1, y1 = interPts[0], interPts[1], interPts[len(interPts)-2], interPts[len(interPts)-1]
                            if len(interPts) > 4:
                               if issubclass(obj.graphObject_.__class__, graphEntity):
                                  atom3i.inter_connect_points =  peer.graphObject_.reverseList2by2(interPts[2:len(interPts)-2])
                               else:
                                  atom3i.inter_connect_points = interPts[2:len(interPts)-2]
                            if issubclass(obj.graphObject_.__class__, graphEntity):
                               retuple = atom3i.showConnection(fromClass, toClass, smoothConn, x0, y0, x1, y1, num1st)       # call the API
                            else:
                               retuple = atom3i.showConnection(fromClass, toClass, smoothConn, x1, y1, x0, y0, num1st)       # call the API
                        else:	# Added 30 July 2002 by JL
			    # try with the pendingConnections list
			    infoTuple = obj.graphObject_.getPendingConnection( toClass )
			    #print "in pendingConnections...", infoTuple
			    if infoTuple:
				interPts, num1st, smoothConn = infoTuple[2:]
                            	x0, y0, x1, y1 = interPts[0], interPts[1], interPts[len(interPts)-2], interPts[len(interPts)-1]
                            	if len(interPts) > 4:
                                  if issubclass(obj.graphObject_.__class__, graphEntity):
                                     atom3i.inter_connect_points =  peer.graphObject_.reverseList2by2(interPts[2:len(interPts)-2])
                                  else:
                                     atom3i.inter_connect_points = interPts[2:len(interPts)-2]
                            	if issubclass(obj.graphObject_.__class__, graphEntity):
                               		retuple = atom3i.showConnection(fromClass, toClass, smoothConn, x0, y0, x1, y1, num1st)       # call the API
                            	else:
                               		retuple = atom3i.showConnection(fromClass, toClass, smoothConn, x1, y1, x0, y0, num1st)       # call the API
				obj.graphObject_.removePendingConnection(infoTuple)
			    else:
                               retuple = atom3i.showConnection(fromClass, toClass)      		# call the API
                        self.setConnectionHandler(retuple[0], peer, obj.out_connections_)	# store the new handler
                        self.setConnectionHandler(retuple[0], obj, peer.in_connections_)	# store the new handler in the peer object
                  else :
                         # umm! this means that we have a connection across hierarchies...
                         # check if we need an 'externalConnection' object or a connection
                         # to a submodel!. This last case happens when Level(TO) > Level(FROM), that is, we have
                         # a connection down.
                         from msvcrt import getch
                         getch()
                         if obj.level() > peer.level():                      				# this level > other level ! -> create external connection
				self.createExternalConnection(atom3i, fromClass, toClass, obj, peer, 1)
                         else:                                           				# this level < other level ! -> create a connection to the model icon
                                atom3i.showConnection ( fromClass, peer.rootNode.graphObject_.tag )     # it won't work with multi-level connections
               # now look for incoming connections!
               toClass = obj.graphObject_.tag							# As we are inspecting incoming connections, obj is the destination...
               for peerTuple in obj.in_connections_:						# for each connection (<peer>, handle) of each object...
                  peer, handler = peerTuple                                                     # unwrap tuple...
                  if type(peer.out_connections_[0]) == TupleType:
                     if handler == None:							# if they have not been connected yet...
                        # obtain source and destinations graphical and semantic objects...
		        fromClass   = peer.graphObject_.tag
		        connCounter = self.getNumberOfDrawn(obj, peer.out_connections_)      	# number of connections to that object drawn so far
                        ret = peer.graphObject_.getInfoTuple(fromClass, toClass, connCounter+1, peer.graphObject_.OLD_out_connections_Points)	# obtain connection information ....
                        if ret:
                           infoTuple, oldHandler = ret
                           interPts, smoothConn, num1st = infoTuple[2:]
                           if len(interPts) >= 4:
                              x0, y0, x1, y1 = interPts[0], interPts[1], interPts[len(interPts)-2], interPts[len(interPts)-1]
                           elif len(interPts) == 0:
                              x0, y0, x1, y1, num1st, smoothConn = None, None, None, None, 2, 0   # Added 19 Nov 2002
                           if len(interPts) > 4:
                              if issubclass(obj.graphObject_.__class__, graphLink):
                                 atom3i.inter_connect_points =  peer.graphObject_.reverseList2by2(interPts[2:len(interPts)-2])
                                 # atom3i.inter_connect_points = interPts[2:len(interPts)-2]
                              else:
                                 atom3i.inter_connect_points =  interPts[2:len(interPts)-2] # (Modified by JL 27 Aug 2002) 
                           if issubclass(obj.graphObject_.__class__, graphEntity):
                              retuple = atom3i.showConnection(fromClass, toClass, smoothConn, x1, y1, x0, y0, num1st)       # call the API
                           else:
                              retuple = atom3i.showConnection(fromClass, toClass, smoothConn, x0, y0, x1, y1, num1st)       # call the API
                           if len(interPts) > 6:   
                              ret = peer.graphObject_.getInfoTuple(fromClass, toClass, connCounter+1, peer.graphObject_.OLD_out_connections_Points)	# obtain connection information ....
                              infoTuple, oldHandler = ret
                              interPts, smoothConn, num1st = infoTuple[2:]
                        else:		# Added 30 July 2002, by JL
			    # try with the pendingConnections list
			    infoTuple = peer.graphObject_.getPendingConnection( toClass )
			    #print "incoming ones, infoTuple = ", infoTuple
			    if infoTuple:
				interPts, num1st, smoothConn = infoTuple[2:]
                            	x0, y0, x1, y1 = interPts[0], interPts[1], interPts[len(interPts)-2], interPts[len(interPts)-1]
                            	if len(interPts) > 4:
                                  if issubclass(obj.graphObject_.__class__, graphLink):
                                     atom3i.inter_connect_points =  peer.graphObject_.reverseList2by2(interPts[2:len(interPts)-2])
                                  else:
                                     atom3i.inter_connect_points =  interPts[2:len(interPts)-2] # (Modified by JL 27 Aug 2002) 
                            	if issubclass(obj.graphObject_.__class__, graphEntity):
                               		retuple = atom3i.showConnection(fromClass, toClass, smoothConn, x1, y1, x0, y0, num1st)       # call the API
                            	else:
                               		retuple = atom3i.showConnection(fromClass, toClass, smoothConn, x0, y0, x1, y1, num1st)       # call the API
				obj.graphObject_.removePendingConnection(infoTuple)
			    else:
                               retuple = atom3i.showConnection(fromClass, toClass)      		# call the API
                        self.setConnectionHandler(retuple[0], peer, obj.in_connections_)
                        self.setConnectionHandler(retuple[0], obj, peer.out_connections_)

                  else :										# umm! this means that we have a connection across hierarchies...
                        if obj.level() > peer.level():                  				# this level > other level ! -> create external connection
                           self.createExternalConnection(atom3i, fromClass, toClass, obj, peer, 0)
                        else:										# this level < other level ! -> create a connection to the model icon
                           atom3i.showConnection ( peer.rootNode.graphObject_.tag, toClass )       	# it won't work with multi-level connections

         # 3rd. : make the tuples in "in_connections_" and "out_connections_" single elements again

         for obj in obj2show:
              del obj.graphObject_.OLD_out_connections_Points
              for index in range(len(obj.in_connections_)):
		obj.in_connections_[index] = obj.in_connections_[index][0]
	      for index in range(len(obj.out_connections_)):
		obj.out_connections_[index] = obj.out_connections_[index][0]
		
	 # 4th, leave the state of atom3i as it was... (regarding connections...) Added 30 July 2002, by JL
	 atom3i.fromClass   = None				# empty variables
  	 atom3i.toClass     = None
         atom3i.sem_objFrom = None
         atom3i.sem_objTo   = None

  def preAction(self, actionID, * params):
      pass

  def postAction(self, actionID, * params):
      pass

  def preCondition(self, actionID, * params):
      pass

  def postCondition(self, actionID, * params):
      pass

  def findLabel(self, label):
      "Searchs graph for a node with label 'label'"
      for nt in self.listNodes.keys():              	# for all kind of nodes...
         for node in self.listNodes[nt]:            	# for all nodes of type <nt>
            if node.GGLabel.getValue() == label:        # Found it
               return node                              # Couldn't find a match
      return None

  def getAncestors(self,node):
      "returns a list of the ancestros of node"
      ancestors = []
      for nt in self.listNodes.keys():              	# for all kind of nodes...
         for nod in self.listNodes[nt]:            	# for all nodes of type <nt>
  	    nod.ancProc = 0				# create new label for ancestor calculation
      node.ancProc = 1					# make sure we don't include the node itself...
      self.getParents(node, ancestors)
      for nt in self.listNodes.keys():              	# for all kind of nodes...
         for nod in self.listNodes[nt]:            	# for all nodes of type <nt>
  	    del nod.ancProc				# delete new label for ancestor calculation
      return ancestors

  def getParents(self, node, ancestors):
      for anc in node.in_connections_:  		# iterate over input connections...
        ancestors.append(anc)
        if not anc.ancProc:				# if not processed, calculate ancestors recursively...
           self.getParents(anc, ancestors)
           anc.ancProc = 1

  def nodeWithLabel(self, label):
      """returns a node with the label 'label'"""
      for nt in self.listNodes.keys():              	# for all kind of nodes...
         for node in self.listNodes[nt]:            	# for all nodes of type <nt>
            if node.GGLabel.getValue() == label:        # check if the node's label is what we are looking for...
               return node                              # a node has been found!
      return None                                       # no appropriate node has been found 

  def evaluateLocalPreCondition(self, which, * params):
      "Traverses the tree applying the funtion 'functionToApply' to all nodes"
      for nt in self.listNodes.keys():              	# for all kind of nodes...
         for node in self.listNodes[nt]:            	# for all nodes of type <nt>
            res = apply(node.preCondition, [which]+list(params))
            if res: return res
      return None

  def evaluateLocalPostCondition(self, which, * params):
      "Traverses the tree applying the funtion 'functionToApply' to all nodes"
      for nt in self.listNodes.keys():              	# for all kind of nodes...
         for node in self.listNodes[nt]:            	# for all nodes of type <nt>
            res = apply (node.postCondition, [which]+list(params))
            if res: return res
      return None

  def isEmpty(self):
      "returns 1 if has some node inside, else return 0"
      for nt in self.listNodes.keys():
         if self.listNodes[nt] != []: return 0
      return 1

  def destroyNodes(self):
      """
         Applies the destroy method to the graphical objects of each node. This function is called when
         the canvas in which this graph is being shown is closed.
      """
      for nt in self.listNodes.keys():              	# for all kind of nodes...
         for node in self.listNodes[nt]:            	# for all nodes of type <nt>
            if node.graphObject_: node.graphObject_.destroy()

  def invalid(self):
      """
         In the case we are the LHS or RHS of a Graph Grammar, verifies that GG labels are different
         Created 21 Jul 2002 by JL
      """
      inGG = 0
      if self.root and self.root.parent: inGG = self.root.parent.editGGLabel
      for asg in self.mergedASG:
         if asg.root and asg.root.parent: inGG = inGG or asg.root.parent.editGGLabel
      if inGG:                                          # This means we are a LHS or RHS of a GG rule
        GGlabels = []                                   # A list to obtain all the GG labels...  
        for type in self.listNodes.keys():
          for node in self.listNodes[type]:
            label = node.GGLabel.getValue()             # Get the node's GG label
            if label in GGlabels:                       # it means it is repeated
              return "Graph Grammar labels are not unique."
            else: GGlabels.append(label)
      return ASGNode.invalid(self)                      # perform the checking in my parent's invalid code

# ---------------------------------- MODIFIED by Denis Dube, Summer 2004 --------------------------------
  
  
  def genCode(self, fileName, allowedTypes, genGraph = 1, isRootNode = 0, 
              metaModelName = None, export = 0, newTypes = None, 
              nodesToGenList = [], openModelStringList=[], attrGenFix=False):
      """ Generates code for creating this graph. allowedTypes is a dictionary with the allowed types..."""
      file = open(fileName, "w+t" )

      dir, fil   = os.path.split(fileName)
      funcName   = string.split (fil, ".")					# compose class name

      if export == 0:
         file.write('"""\n')
         file.write("__"+ fil +"_____________________________________________________\n")
         file.write("\n")         
         file.write("Automatically generated AToM3 Model File (Do not modify directly)\n")
         file.write("Author: "+USER_NAME+"\n")
         file.write("Modified: "+time.asctime()+"\n")       
         file.write("__"+ len(fil)*"_" +"_____________________________________________________\n")
         file.write('"""\n')
         #file.write('from graph_ASG_ERmetaMetaModel import *\n')		# just for the case!
         file.write('from stickylink import *\n')				# necessary if we describe some graphLinks...
         file.write('from widthXfillXdecoration import *\n')			# necessary if we describe some graphLinks...

         # import the subclass ...
         if( self.getClass() not in self.nodeTypes ):
           file.write('from '+self.getClass()+' import *\n')
           
         # import all the node types...
         for nodetype in self.nodeTypes:
           if( self.listNodes[nodetype] != [] ): 
             file.write('from '+nodetype+' import *\n') 
            
         # Import all the graphical appearences of the node types... that
         # are actually used! 
         # Added by Denis Dube, last modified on Sept. 9, 2004
         if( genGraph ):           
            # STEP 1: Find all graphObjects used in the model
            graph_objectDict = dict()
            for nodetype in self.listNodes.keys():
              for node in self.listNodes[nodetype]:
                if( node.graphClass_  ):
                  graph_objectDict[ node.graphObject_.getGraphClassName() ]=1
            # STEP 2: Create the import statements for each graphObject
            for graphObject in graph_objectDict.keys():
              file.write('from '+graphObject+' import *\n')
              # NOTE: I think the next two statements are caution overkill...
              #file.write('try:    from '+graphObject+' import *\n')
              #file.write('except: print "WARNING: unable to load the graphical appearence file: '+graphObject+'.py" \n')
                         
         # import the basic types...
         for typ in allowedTypes.keys():
            typeInstance, params = allowedTypes[typ]
            typeName = typeInstance.__name__
            file.write('from '+typeName+' import *\n')
            
      # Generate the ASG constructor
      if( attrGenFix ):
        self.__genASGconstructor( file, funcName )        
      else:
        # Old way
        file.write('\ndef '+funcName[0]+'(self, rootNode):\n')
      
      # Generate code for the ASGroot attributes
      if( isRootNode ):  
        # Should attrGenFix be always true? More testing required
        #todo: attrGenFix == True always?
        if( attrGenFix ): self.__genAttributesROOT( file )
        else: self.genAttributesCode(file, genGraph, "rootNode")

      self.writeGraph2File(file, genGraph, isRootNode, None, "    ", 1, funcName[0], nodesToGenList=nodesToGenList)

      # generate code for the sub-models
      counter = 0
      if( not nodesToGenList ):
          for nodetype in self.nodeTypes:
              for node in self.listNodes[nodetype]:            
                  newFile = funcName[0]+str(counter)
                  res = node.genCode(os.path.join(dir, newFile+'.py'), allowedTypes, genGraph, 0)
                  counter = counter + 1
      else:          
          for node in nodesToGenList:
              newFile = funcName[0]+str(counter)
              res = node.genCode(os.path.join(dir, newFile+'.py'), allowedTypes, genGraph, 0)
              counter = counter + 1
            

      if isRootNode:
         hierarchical = self.isHierarchical()
         if export == 0:
            if hierarchical:
               file.write('def main'+funcName[0]+'(self, ASGroot):\n')
               # file.write('    self.ASGroot = '+self.getClass()+'(self)\n')
               file.write('    self.'+funcName[0]+'(self, ASGroot)\n\n')
               file.write('    self.'+funcName[0]+'_connections(self, ASGroot)\n\n')
               file.write('newfunction = main'+funcName[0]+'\n\n')
            else:
               file.write('newfunction = '+funcName[0]+'\n\n')
            if newTypes and len(newTypes)>0:                             # generate a list of newly added types
               file.write('loadedTypes = [')
               counter = 0
               for nt in newTypes:
                  if counter > 0: file.write(',')
                  file.write(str(nt))
                  counter = counter + 1
               file.write(']\n')
         
         self.genLoadedMMName( file )
      if( attrGenFix ): file.write( '\natom3version = \'0.3\'\n' )
      file.close()
      return funcName[0]                          				# this indicates that we've done something

  

#----------------- Much modification by Denis beyond this line -----------------
      
  
  def addNode(self, node):
    "adds a node to the graph"

    nl = self.listNodes[node.getClass()]
    if( not node in nl): 
      nl.append(node)
    
    # if we don't have a root node, set the root node to it...
    if( self.root == None): 
      self.root = node
    
    # set the attribute rootNode of node to self
    node.rootNode = self
    
    # see if we have to assign a unique GGLabel... (Added 30 July, 2002, JL)
    if node.GGLabel.getValue() == -1:
      # get the maximum GGLabel in this graph...
      self.minimumGG = self.minimumGG + 1
      node.GGLabel.setValue(self.minimumGG)
      if( node.parent and node.parent.editGGLabel 
         and node.parent.genGraphics and node.graphObject_):
        node.graphObject_.drawGGLabel(node.graphObject_.dc)
    
    #=====================================================
    #  Hierarchical structure maintenance (See HierarchicalASGNode.py)
    #=====================================================   
    if(node.isHierarchicalNode()):
      node._addNodeToHierarchyTopLayer()
                
    # Non-graphical node, just stop here :D    
    if( node.graphObject_ == None ): 
      return
          
    # Graphical node, not drawn yet (happens when loading GraphGrammars)
    if( node.graphObject_.getCanvas() == None ): 
        # See VisualObj.py saveBackupCoords()
        node.graphObject_.saveBackupCoords() 
        return
        
    # Apply any QOCA linear constraints
    # For graph grammars, graphObject_ may be none, so GGrule.py will also
    # trigger QOCA in its replaceSides() method
    if(not isNotUsingQoca() and hasattr(node, 'QOCA') 
      and not node.__dict__.has_key('QOCA')):
      # Make sure that node has a method called 'QOCA', not an attribute
      node.QOCA(None)
      
    
        
    # Graphical Layout Constraints (scale, text scale, label positions... )
    if( hasattr( node.graphObject_, 'layConstraints' ) ): 
      ConstraintLoader( node ) 
          
    # Apply the global zoom-level to the newly added node 
    # (modifies the local scaling)
    self.applyZoom( node )
        
   
    # Apply additonal layout algorithms
 
    atom3i = node.parent
    if( not atom3i ): 
      return
      
    if( isConnectionLink( node.graphObject_ ) ):       
      self.newLinkNodeQueue.append(node)
      return
    else:
      obj = node.graphObject_   
    
    # Snap Grid
    if( not atom3i.isLoadingModel and atom3i.snapGridInfoTuple ):
        snapNewEntity( atom3i, obj, [obj.x, obj.y] )
        
    # Force Transfer
    if( atom3i.isAutoForceTransferEnabled ):
          ForceTransfer.applyLayout()    
        
        
  
  def processLoadedLinkNodes(self, isLoadingModel):
    """ 
    When loading a model, have to wait till model is fully loaded before
    we know in/out connections... necessary for the QOCA constraints
    So ATOM3.py is going to call us here after it's done loading a model
    """
    
    if(isLoadingModel):
      #=====================================================
      #  Hierarchical structure maintenance (See HierarchicalASGNode.py)
      #=====================================================
      for node in self.newLinkNodeQueue:
        # NOTE: node.in_connections_ could be > 1 in the metamodel since 
        # AToM3 considers meta-model relations to have hierarchy active!
        # Of course I didn't intend this, and it has no meaning, so ignore!
        if(node.isHierarchicalLink() and len(node.in_connections_) == 1):
          for child in node.out_connections_:
            child._setHierParent(node.in_connections_[0])
          node.in_connections_[0]._addHierChildrenList(node.out_connections_)    
    

    #=======================================================================
    #    QOCA Constraints
    #    Only do this if we are actually using QOCA in the first place...
    #=======================================================================
    if(isNotUsingQoca()): 
      return
    
    for node in self.newLinkNodeQueue:
      # Apply any QOCA linear constraints
      # For graph grammars, graphObject_ may be none, so GGrule.py will also
      # trigger QOCA in its replaceSides() method
      if(hasattr(node, 'QOCA') and not node.__dict__.has_key('QOCA')):
        # Make sure that node has a method called 'QOCA', not an attribute
        node.QOCA(None)
        
    # Clean out the queue
    self.newLinkNodeQueue = []
        
        
    
  def applyZoom( self, node ):
    
    zoom = ZoomFocus.getZoom()
    if( zoom == 1 ): 
      return   
      
    # Edges can only be zoomed if they have a center drawing (which is an entity)
    if( isConnectionLink( node.graphObject_ ) ):
      obj = node.graphObject_.getCenterObject()
      if( not obj ): 
        return
    else:
      obj = node.graphObject_
        
    if( not obj.layConstraints.has_key( 'scale' ) ):
      obj.layConstraints['scale'] = [1.00, 1.00]
    if( not obj.layConstraints.has_key( 'Text Scale' ) ):
      obj.layConstraints['Text Scale'] = 1.00 
        
    # Apply a Zoom to the Node Entity (preserving individual scale dimensions)
    sx, sy = obj.layConstraints['scale']
    newSx = sx * zoom
    newSy = sy * zoom
    obj.layConstraints['scale'] = [newSx, newSy]
    obj.Scale( newSx / sx, newSy / sy, moveLinks=False )
    
    # Apply a zoom to the Node Entity text
    st = obj.layConstraints['Text Scale']
    newSt = st * zoom
    obj.layConstraints['Text Scale'] = newSt
    obj.ScaleText( newSt )
    
  def getASGbyName( self, metaModelName ):
    """ Get the ASG specified by the metaModelName (PUBLIC) """
    name = self.__sanitizeMetaModelName( metaModelName )
    if( self.__trackASG.has_key( name ) ):
      return self.__trackASG[ name ][0] 
    return None
  
  def getEntireASGList( self ):
    """ Get the names of all the ASG's, Created March 28, 2005 by Denis"""
    return self.__trackASG.keys()
  
  def __genASGconstructor( self, file, funcName ):
    """
    Generate the ASG constructor the new way, 
    accepts an ASG root for each formalism...
    Created March 28, 2005 by Denis
    """
    ASGbuffer = ''
    counter = 0
        
    # Go through all actively tracked ASG's (formalisms)
    for ASGname in self.__trackASG.keys():
      # This formalism has at least one entity, we NEED IT
      if( not self.__isASGbyNameEmpty( ASGname ) ):
        ASGbuffer += ASGname + 'RootNode=None, '
        counter += 1 
    if( counter >= 1 ):
      ASGbuffer = ASGbuffer[:-2]
      file.write('\ndef '+funcName[0]+'(self, rootNode, ')
      file.write( ASGbuffer + '):\n')
    else:
      file.write('\ndef '+funcName[0]+'(self, rootNode):\n')
  
  def __getTypeListByASG( self, asg ):
      """
      Given an ASG, find the list of node types
      Created March 2005 by Denis
      """
      for (otherASG, typeList) in self.__trackASG.values():
        if( asg == otherASG ): 
          return typeList
      return []
  
  def __sanitizeMetaModelName( self, name ):
      """
      Keep it simple! All names are treated as non-'_META' tag (Backward compatiblity)
      Created March 2005 by Denis
      """
      if( name[-5:] == '_META' ): 
        return name[:-5]
      else: return name
      
  def __addNewASG2Tracker( self, metaModelName, ASGgraph ):
      """ 
      Keeps track of vital ASG information in a clean fashion
        PRIVATE DATA-STRUCTURE, no messing around with it
        Structure:  { modelName_META : [ ASG, nodeTypes ] }
        modelName_META does not have the '_META' appended to it (simplicity)
      Created March 2005 by Denis
      """ 
      self.__trackASG[ self.__sanitizeMetaModelName( metaModelName ) ] = \
                                [ASGgraph, cloningMachine(ASGgraph.nodeTypes)]
                                
  def __addNewAttr2Tracker( self, rootNode, metaModelName ):
    """
    A seperate dict for each formalism to track attributes
    Example: Formalism X has a root level attribute called 'author' which a user
            of the formalism X making a new model can set to 'Denis Dube'.
            Now we want this attribute & value to be saved in a seperate place,
            so that if Formalism Y has the exact same attribute 'author', that
            it doesn't clobber it. 
    Created March 2005 by Denis
    """
    # Just get rid of the _META extension if it's there, that way always works :D
    metaModelName = self.__sanitizeMetaModelName( metaModelName )
    
    # If not already done, create a new dict to track attributes for this model
    if( not self.__trackAttributes.has_key( metaModelName ) ):    
        self.__trackAttributes[ metaModelName ] = dict()    
    modelTracker = self.__trackAttributes[ metaModelName ]
    
    # Go through each attribute
    for attribute in rootNode.generatedAttributes.keys():
      # Access the rootNodes contents directly
      if( rootNode.__dict__.has_key( attribute ) ):
        # Make a copy of the value of this attribute
        modelTracker[attribute] = cloningMachine( rootNode.__dict__[attribute] )
                              
      else:
        print 'ERROR in ASG.py in __addNewAttr2Tracker()'
        print 'The root node: ' + rootNode + ' claims to have the' \
              ' attribute "' + attribute + '" but it actually doesn\'t!'
        print 'Generated attributes', rootNode.generatedAttributes
        print 'GUI model contents dump:', rootNode.__dict__
  
  def __deleteASG2Tracker( self, metaModelName ):
      """ 
      Keeps track of vital ASG information in a clean fashion 
      So remove ASG's your not using anymore!
      Created March 2005 by Denis
      """      
      name = self.__sanitizeMetaModelName( metaModelName )
      if( self.__trackASG.has_key( name ) ):
        del self.__trackASG[ name ]
        
  def __isASGbyNameEmpty( self, metaModelName ):
    """ 
    Return True if there is some node inside the ASG with that meta-model name
    Created March 2005 by Denis 
    """
    name = self.__sanitizeMetaModelName( metaModelName )
    if( not self.__trackASG.has_key( name ) ): 
      return False
    asg, types = self.__trackASG[ name ]
    
    # For each type of node in the ASG
    for type in types:
      # Check if any nodes of that type exist
      if( self.listNodes[type] != [] ):  
        return False
    return True
  
  def __genAttributesROOT( self, file, indent = '    ' ):
    """
    Generates attributes for the root ASG node
    Example: Whenever you edit your models global attributes, it gets saved here
    This particular generator will intelligently save only what's needed, and
    a clean copy of it at that! 
    By Denis Dube, March 28, 2005
    """
    # Go through all actively tracked ASG's (formalisms)
    for modelMetaName in self.__trackASG.keys():
      if( not self.__isASGbyNameEmpty( modelMetaName ) ):
        # This formalism has at least one entity, we NEED IT
        ASG = self.getASGbyName( modelMetaName )
   
        #todo: clean this up
        try:
          modelTracker = self.__trackAttributes[ modelMetaName ]
        except:
          print 'ERROR: see ASG.py in __genAttributesROOT(), caused by Buttons Model pointing to a Formalism with a different name'
          print 'modelMetaName', modelMetaName          
          print 'self.__trackAttributes', self.__trackAttributes
          print 'self.__trackASG', self.__trackASG
        
        file.write( '\n'+indent+'# --- Generating attributes code for ASG '
                     +modelMetaName+' ---\n' )   
        # DOH! Some formalisms may not have any attributes at all!
        if( len( modelTracker ) > 0 ):
          file.write( indent + 'if( ' + modelMetaName + 'RootNode ): ' )
          i2 =  indent + '    '
          
          #Generates code for the attributes value
          for attr in modelTracker.keys():
            #print attr, ASG.getAttrValue(attr)
            file.write( '\n'+i2+'# '+attr+'\n' )
    
            # Write its value to file
            ASG.getAttrValue(attr).writeValue2File ( file = file, indent=i2, 
                  objName = modelMetaName+'RootNode.'+attr, depth = 1,
                  generatingCode = 0)     
        else: 
          file.write( indent+'# No attributes to generate!\n' )
        file.write( indent+'# --- ASG attributes over ---\n\n' )


  def showASGattributesDialog( self, atom3i ):
    """
    A modelAttributes modifier that uses the new ASG tracking system
    By Denis Dube, March 28, 2005
    """
    
    # No ASG? Ehhhh
    if( len( self.__trackASG ) == 0 ): 
      return
    
    # One ASG, show dialog
    elif( len( self.__trackASG  ) == 1 ): 
      ASG, typeList = self.__trackASG.values()[0] #<--get the first & only value
      ATOM3TypeDialog(atom3i, ASG )
      
    # Many ASG's
    else:
      stringList = []      
      for ASGname in self.__trackASG.keys():
        stringList.append( ASGname )
      stringList.append( 'Cancel' )
      
      title = 'Meta Attributes'
      text = 'Edit attributes of meta-model...'
      default = 0
      response = Dialog.Dialog(atom3i.parent, 
                    {'title': title, 'text': text, 'bitmap': '',
                    'default': default, 'strings': stringList}).num
      if( response >= len(stringList) -1 ): 
        return
      else:
        ASGname = stringList[response]
        ATOM3TypeDialog(atom3i, self.__trackASG[ASGname][0] )
 
      
        
  def genLoadedMMName(self, file ):
    """ 
    Saves the model with an attribute that will cause AToM3 to load formalisms
    that are neccessary for the model
    Created March 2005 by Denis
    """          
    loadedMMNameList = []
      
    # Go through all actively tracked ASG's (formalisms)
    for modelMetaName in self.__trackASG.keys():
      if( not self.__isASGbyNameEmpty( modelMetaName ) ):
        # This formalism has at least one entity, we NEED IT
        loadedMMNameList.extend( self.getGUIName(modelMetaName) )
          
    # Output the loadMMName
    if( len( loadedMMNameList ) == 1 ):
      file.write("loadedMMName = '"+loadedMMNameList[0]+"'\n")   
    else:
      file.write("loadedMMName = "+str(loadedMMNameList)+"\n") 
  
  
  
  def getGUIName( self, modelName ):
      """ 
      Should just add _META to get this, but old version of AToM3 didn't 
      Created March 2005 by Denis
      """
      # For comaptibility with older AToM3 models
      try:
        exec 'import ' + modelName
        return [modelName]
      except:
        pass
      
      # This is the most common case (must do second for compatibility)
      try:
        exec 'import ' + modelName + '_META'
        return [modelName + '_META']
      except:
        pass
      
      # Ugh, crapola!
      print 'AToM3 was unable to find the buttons model (META file) for ' \
              + modelName
      return []
    
  ## def debug( self ):
      ## print '\n\n__trackAttributes\n    ',self.__trackAttributes
      ## print '\n\__trackASG\n    ',self.__trackASG
    
    
