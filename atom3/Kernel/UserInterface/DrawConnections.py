"""
DrawConnections.py

Moved connection drawing code out of atom3.py into a seperate module
Modified it to create more flexible & aesthetic looking links
self = instance of ATOM3
  June 16, 2004 by Denis Dube
"""

from ATOM3TypeInfo       import *
from VisualObj import VisualObj

from tkMessageBox import showerror, askyesno
       


def drawConnections(self, * listOfConnections ):
  """Same as drawConnection but a tuple of tuples is given...
      tuples can be :
      - Size 4 and then it means (fromClass, toClass, sem_objFrom, sem_objTo)
      - Size 2 and then it means (sem_objFrom, sem_objTo) and connecting respective icons...
- TO DO (sem_objFrom, "named_port1", sem_objTo, "named_port2")
  """
  for connection in listOfConnections:
      num1st      = 2
      smoothConn  = 0
      interPoints = []
      lconn = len(connection)
      
      # A 'Visual connection'
      if issubclass(connection[0].__class__, VisualObj):		
        # then we must have something like (fromClass, toClass, sem_objFrom, sem_objTo, [inter-points], smooth, num-points-of-1st-connection)
        # the three last parameters are optional.
        self.fromClass   = connection[0]
        self.toClass     = connection[1]
        self.sem_objFrom = connection[2]
        self.sem_objTo   = connection[3]
        if lconn >= 5: interPoints = connection[4]
        if lconn >= 6: smoothConn  = connection[5]
        if lconn >= 7: num1st      = connection[6]
           
      # A 'non-visual' connection (i.e. loading model from file)
      else:							
        # then we must have something like (sem_objFrom, sem_objTo, [inter-points], smooth, num-points-of-1st-connection)
        # the three last parameters are optional.
        self.sem_objFrom  = connection[0]
        self.sem_objTo    = connection[1]
        if lconn >= 3: interPoints = connection[2]
        if lconn >= 4: smoothConn  = connection[3]
        if lconn >= 5: num1st      = connection[4]
        
        if self.sem_objFrom.graphObject_:				# check if we have graphics...
            self.fromClass = self.sem_objFrom.graphObject_.tag
            self.toClass   = self.sem_objTo.graphObject_.tag
        else:
            self.fromClass = None
            self.toClass   = None
            tkMessageBox.showinfo(
            "Connecting non-graphical entities",
            "From '"+self.sem_objFrom.toString()+"' to '"+self.sem_objTo.toString()+"'",
            parent = self
        )
      if len(interPoints) > 4: self.inter_connect_points = []+interPoints[2:len(interPoints)-2]
      else: self.inter_connect_points = []
      if len (interPoints) > 1:
        drawConnection(self,smoothConn, interPoints[0], interPoints[1], 
                    interPoints[len(interPoints)-2],
                    interPoints[len(interPoints)-1], num1st)
      else:
        drawConnection(self,smoothConn, None, None, None, None, num1st)       
  self.fromClass = None
  self.toClass   = None
  self.sem_objFrom = None
  self.sem_objTo = None
  
  
  
  
  
def simpleConnection( self, sem_objFrom, sem_objTo, filterLinkTypeList=None ):
    """
    The easy way of getting a connection, just supply the semantic objects
    you want connected, and this will handle the rest...
    Parameters:
      sem_objFrom, subclass of ASGNode.py it is the source object for the arrow
      sem_objTo, subclass of ASGNode.py it is the target object for the arrow
      filterLinkTypeList, list of the class-names of relations to be ignored
    """
    self.sem_objFrom = sem_objFrom
    self.sem_objTo = sem_objTo
    if( sem_objFrom.graphObject_ ): self.fromClass = sem_objFrom.graphObject_
    if( sem_objTo.graphObject_ ): self.toClass = sem_objTo.graphObject_
    drawConnection( self, filterLinkTypeList=filterLinkTypeList )
  
  
def drawConnection(self, smoothConnection=0, x0=None, y0=None, x1=None, 
                 y1=None, num1st=2, simpleConnect=True, 
                 filterLinkTypeList=None):
  """
  Connects two entities of the model, whether they are given as graphical 
  entities (self.fromClass and self.toClass must have a value then) or just 
  semantically, (self.sem_objFrom and self.sem_objTo must have a value then).
  """
  if self.fromClass and self.toClass:			# if we have graphical information...
      connTuple = showConnection(self,self.fromClass, self.toClass, 
                        smoothConnection, x0, y0, x1, y1, num1st,
                        simpleConnect, filterLinkTypeList)
      if(connTuple == None):
        return
      
      connHandler, objFrom, objTo, auxHandler, newObj = connTuple
      self.newCreatedObject = newObj                         # added 17/Mar/2003       
      if not connHandler and not objFrom and not objTo:      # something went wrong in showConnection
        return
      
      # Make sure centerObjects of arrows are properly visible
      for objToRaise in [objFrom, objTo]:
        if(objToRaise.__dict__.has_key('centerObject') and
            objToRaise.centerObject != None):
          objToRaise.centerObject.raiseItem()      

      
      #
      # This is for named port handling (Added 24 July 2002, JL)
      #

      if not newObj:                                                # nothing created in between
        namedConnector_From = objFrom.getNamedPort( connHandler )  # Get Named ports of source and destination objects
        namedConnector_To   = objTo.getNamedPort( connHandler )
      else:                                                         # A newly created object
        namedConnector_From = objFrom.getNamedPort( connHandler )  # Get Named ports of source and destination objects, as well as newly created object
        namedConnector_Aux1 = newObj.graphObject_.getNamedPort( connHandler )
        namedConnector_Aux2 = newObj.graphObject_.getNamedPort( auxHandler )
        namedConnector_To   = objTo.getNamedPort( auxHandler )

      #
      # End named Ports handling
      #

      # now set the sematic objects to be connected if we don't have them yet...

      if not self.sem_objFrom:
          self.sem_objFrom = objFrom.semanticObject

      if not self.sem_objTo:
          self.sem_objTo   = objTo.semanticObject

  # try the global constraints (if not drawing a rule)...
  if not self.editGGLabel:
      res = self.ASGroot.preCondition(ASG.CONNECT)
      if res:                                        # global constraint do not hold!
        if newObj:
          undoConnection(self,res, objFrom, newObj.graphObject_, connHandler)
          undoConnection(self,res, newObj.graphObject_, objTo, auxHandler)
          # remove newObj   	
          newObj.graphObject_.erase(self)
          newObj.removeNode()   	                         
        else: 
          undoConnection(self,res, objFrom, objTo, connHandler)
        return                                                                 

      res = self.sem_objFrom.preCondition(ASGNode.CONNECT, "SOURCE")  # local constraint do not hold!
      if res:
        if newObj:
          undoConnection(self, res, objFrom, newObj.graphObject_, connHandler)
          undoConnection(self, res, newObj.graphObject_, objTo, auxHandler)
          # remove newObj   	
          newObj.graphObject_.erase(self)
          newObj.removeNode()   	                         
        else: 
          undoConnection(self, res, objFrom, objTo, connHandler)
        return                                                                 

      res = self.sem_objTo.preCondition(ASGNode.CONNECT, "DESTINATION")                # local constraint do not hold!
      if res:
        if newObj:
          undoConnection(self, res, objFrom, newObj.graphObject_, connHandler)
          undoConnection(self, res, newObj.graphObject_, objTo, auxHandler)
          # remove newObj   	
          newObj.graphObject_.erase(self)
          newObj.removeNode()   	                         
        else: 
          undoConnection(self, res, objFrom, objTo, connHandler)
        return

      # ey! also in the newly created entity (if any has been created)
      if newObj:
        res = newObj.preCondition(ASGNode.CONNECT, "DESTINATION")                # local constraint do not hold!
        if res:
          undoConnection(self, res, objFrom, newObj.graphObject_, connHandler)
          # remove newObj   	
          newObj.graphObject_.erase(self)
          newObj.removeNode()   	                        
          return

        res = newObj.preCondition(ASGNode.CONNECT, "SOURCE")                # local constraint do not hold!
        if res:
          undoConnection(self,res, newObj.graphObject_, objTo, auxHandler)
          # remove newObj   	
          newObj.graphObject_.erase(self)
          newObj.removeNode()   	                        
          return              
    
  self.sem_objFrom.preAction(ASGNode.CONNECT, "SOURCE")
  self.sem_objTo.preAction(ASGNode.CONNECT, "DESTINATION")
  if newObj:
      newObj.preAction(ASGNode.CONNECT, "SOURCE")
      newObj.preAction(ASGNode.CONNECT, "DESTINATION")
  
  if newObj == None:                                              			  	# No new objects created
      self.sem_objFrom.out_connections_.append(self.sem_objTo)
      self.sem_objTo.in_connections_.append(self.sem_objFrom)
      # see if we also have to add the connections in the named ports... (Added 24 July 2002, by JL)
      if namedConnector_From:                                                       # (Added 24 July 2002, by JL)
        self.sem_objFrom.getAttrValue(namedConnector_From).append(self.sem_objTo)   # (Added 24 July 2002, by JL)
      if namedConnector_To:                                                         # (Added 24 July 2002, by JL)
        self.sem_objTo.getAttrValue(namedConnector_To).append(self.sem_objFrom)     # (Added 24 July 2002, by JL)
  else:    									 # A new object had to be created in between
      self.sem_objFrom.out_connections_.append(newObj)
      newObj.in_connections_.append(self.sem_objFrom)
      newObj.out_connections_.append(self.sem_objTo)
      self.sem_objTo.in_connections_.append(newObj)
      
      if namedConnector_From:                                                      # (Added 24 July 2002, by JL)
        self.sem_objFrom.getAttrValue(namedConnector_From).append(newObj)          # (Added 24 July 2002, by JL)
      if namedConnector_To:                                                        # (Added 24 July 2002, by JL)
        self.sem_objTo.getAttrValue(namedConnector_To).append(newObj)              # (Added 24 July 2002, by JL)
      if namedConnector_Aux1:                                                      # (Added 24 July 2002, by JL)
        newObj.getAttrValue(namedConnector_Aux1).append(self.sem_objFrom)          # (Added 24 July 2002, by JL)
      if namedConnector_Aux2:                                                      # (Added 24 July 2002, by JL)
        newObj.getAttrValue(namedConnector_Aux2).append(self.sem_objTo)            # (Added 24 July 2002, by JL)                 
      # shouldn't we test constraints in the newly created object??
  
  # Check the cardinalities if we are not editing a Graph Grammar...(we have them in cardinalityTable)...
  if not self.editGGLabel:
      if newObj == None:								# 1st check that no object has been created in between
        res = self.checkCardinalities (self.sem_objFrom, self.sem_objTo)		# if it returns !=0, then the connection is illegal...
        if res:
            undoConnection(self,res, objFrom, objTo, connHandler)
            return
      else:                             						# check the cardinalities with the object in between
        res = self.checkCardinalities (self.sem_objFrom, newObj)                      # if it returns 0, then the connection is illegal...
        if res:
            undoConnection(self,res, objFrom, newObj.graphObject_, connHandler)
            # remove newObj   	
            newObj.graphObject_.erase(self)
            newObj.removeNode()
            return   	

        res = self.checkCardinalities (newObj, self.sem_objTo) 		        # if it returns 0, then the connection is illegal...
        if res:
            undoConnection(self,res, newObj.graphObject_, objTo, auxHandler)
            # remove newObj   	
            newObj.graphObject_.erase(self)
            newObj.removeNode()   	        
            return	
  
  # try the global constraints...
  if not self.editGGLabel:

      res = self.ASGroot.postCondition(ASG.CONNECT)
      if res:                 
        if newObj:
          undoConnection(self,res, objFrom, newObj.graphObject_, connHandler)
          undoConnection(self,res, newObj.graphObject_, objTo, auxHandler, 0)
        else: 
          undoConnection(self,res, objFrom, objTo, connHandler)
        return      
      res = self.sem_objFrom.postCondition(ASGNode.CONNECT, "SOURCE")   # try the local post-conditions (1st object)

      if res:
        if newObj:
          undoConnection(self,res, objFrom, newObj.graphObject_, connHandler)
          undoConnection(self,res, newObj.graphObject_, objTo, auxHandler, 0)
          # remove newObj   	
          newObj.graphObject_.erase(self)
          newObj.removeNode()
          newObj = None
        else: 
          undoConnection(self,res, objFrom, objTo, connHandler)
        return
      
      res = self.sem_objTo.postCondition(ASGNode.CONNECT, "DESTINATION")               # try the local post-conditions (2nd object)
      if res:
        if newObj:
          undoConnection(self,res, objFrom, newObj.graphObject_, connHandler)
          undoConnection(self,res, newObj.graphObject_, objTo, auxHandler, 0)
          # remove newObj   	
          newObj.graphObject_.erase(self)
          newObj.removeNode()
        else: 
          undoConnection(self,res, objFrom, objTo, connHandler)
        return
      if newObj:
        res = newObj.postCondition(ASGNode.CONNECT, "DESTINATION")                  # try the local post-conditions (1st object)
        if res:
            undoConnection(self,res, objFrom, newObj.graphObject_, connHandler)
            # remove newObj   	
            newObj.graphObject_.erase(self)
            newObj.removeNode()
            return
        res = newObj.postCondition(ASGNode.CONNECT, "SOURCE")               # try the local post-conditions (2nd object)
        if res:
            undoConnection(self,res, newObj.graphObject_, objTo, auxHandler)
            # remove newObj   	
            newObj.graphObject_.erase(self)
            newObj.removeNode()
            return
  
  if newObj:      
      # QOCA, gotta update this after the fact, since connect info comes late
      # See ASG.processLoadedLinkNodes() for more info
      atom3i = newObj.parent
      if(atom3i):
        isLoadingModel = atom3i.isLoadingModel
      else:
        isLoadingModel = False
      self.ASGroot.processLoadedLinkNodes(isLoadingModel)
      
      #=====================================================
      #  Hierarchical structure maintenance (See HierarchicalASGNode.py)
      #  NOTE: This uses processLoadedLinkNodes() to handle saved models too
      #=====================================================
      if(newObj.isHierarchicalLink()):
        self.sem_objTo._setHierParent(self.sem_objFrom)
        self.sem_objFrom._addHierChild(self.sem_objTo)
  
        
  ##print "Connecting (source-->dest)", self.sem_objFrom, self.sem_objTo
  self.ASGroot.postAction(ASGNode.CONNECT, "SOURCE")
  self.ASGroot.postAction(ASGNode.CONNECT, "DESTINATION")
  self.sem_objFrom.postAction(ASGNode.CONNECT, "SOURCE")
  self.sem_objTo.postAction(ASGNode.CONNECT, "DESTINATION")
  
  
  if newObj:
      """ Okay this may screw up some code, hope not, but... it's efficient.."""
      newObj.postAction(ASGNode.CONNECT, "SOURCE&DESTINATION")
      #newObj.postAction(ASGNode.CONNECT, "SOURCE")
      # Do we really need to do this for DESTINATION too???? - Denis
      #newObj.postAction(ASGNode.CONNECT, "DESTINATION")  
      
  

def undoConnection(self, res, objFrom, objTo, connHandler, showMessage = 1):
  """
      Undoes a connection due to constraint fail. res is the resulting message
  """
  if showMessage: self.constraintViolation(res)
  if self.sem_objTo in self.sem_objFrom.out_connections_: self.sem_objFrom.out_connections_.remove(self.sem_objTo)
  if self.sem_objFrom in self.sem_objTo.in_connections_: self.sem_objTo.in_connections_.remove(self.sem_objFrom)

  if self.fromClass and self.toClass:						# if we have graphical information...

    self.UMLmodel.delete(connHandler)
    # UNDO THE PREACTIONS!!!!!
    result1 = objFrom.removeConnection(self, connHandler)
    result2 = objTo.removeConnection(self, connHandler)
    if result1 == 2 and objFrom.isSubclass("graphLink"):
        objFrom.semanticObject.removeNode()
    if result2 == 2 and objTo.isSubclass("graphLink"):
        objTo.semanticObject.removeNode()
  
  return


def showConnection(self, fromClass, toClass, smoothConn=0, x0=None, y0=None, 
        x1=None, y1=None, num1st=2, simpleConnect=True, filterLinkTypeList=None):
  """
  Connects graphically two entities of the model. Checks if graphical 
  objects have connectors and if an intermediate object has to be created.
  """
  #print fromClass,toClass, x0,y0,x1,y1, self.inter_connect_points
  if fromClass  : self.fromClass   = fromClass
  if toClass    : self.toClass     = toClass
  maxDistance, maxFreeDistance = 10000, 10000
  actDistance = 0
  xc0, yc0, xc1, yc1 = 0, 0, 0, 0

  # Obtain the graphical object associated with the semantic object
  if type(self.fromClass) == StringType: 
    objFrom = VisualObj.Tag2ObjMap[self.fromClass]  
  else: 
    objFrom = self.fromClass                      
  if type(self.toClass) == StringType: 
    objTo   = VisualObj.Tag2ObjMap[self.toClass]  
  else: 
    objTo = self.toClass                          
    
  # Make sure that if we are connecting two entities, that they have ports
  if objFrom.isSubclass("graphEntity") and not objFrom.connectors:
      tkMessageBox.showwarning(
            "Dont know how to connect objects!      ",
            "First object does not have connectors",
            parent = self
      )
      return (None, None, None, None, None)
  if objTo.isSubclass("graphEntity") and not objTo.connectors:
      tkMessageBox.showwarning(
            "Dont know how to connect objects!       ",
            "Second object does not have connectors",
            parent = self
      )
      return (None, None, None, None, None)

  def relaxCardinalityConstraints( class1Name, class2Name = None):
    """ 
    Allow entities of different formalisms to connect by fooling them into
    thinking that they know GenericGraphEdge.
    This hack is very useful as a 'glue' in graph grammar transformations...
    """    
    self.CardinalityTable['GenericGraphEdge'][class1Name] = \
                    [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
    self.CardinalityTable[class1Name]['GenericGraphEdge'] = \
                    [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
    if( not class2Name ): return
    self.CardinalityTable['GenericGraphEdge'][class2Name] = \
                    [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
    self.CardinalityTable[class2Name]['GenericGraphEdge'] = \
                    [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
    
  class1Name = objFrom.semanticObject.getClass()
  class2Name = objTo.semanticObject.getClass()
  
  # Not sure when/if this situation ever occurs - Denis
  if( not class1Name in self.ConnectivityMap.keys() or
      not class2Name in self.ConnectivityMap.keys()):
            
    connHandler = objFrom.connect(objTo, self.inter_connect_points, 
                                  x0, y0, x1, y1, smoothConn, num1st)
    self.inter_connect_points = []
    #print "When does this happen?", objFrom, objTo, class1Name, class2Name
    return (connHandler, objFrom, objTo, -1, None)  
  
    
  # Does class1 have connection capability with class2?
  # Typically this means that the entities belong to the same meta-model
  if( class2Name in self.ConnectivityMap[class1Name].keys() ):  
    # Check if we can connect the objects directly (they are Entity and Link), 
    # or we must put something in between (but this may be a list)
    betweenClasses = self.ConnectivityMap[class1Name][class2Name]				
  
  # However using the multi-formalism connection hack with GenericGraphEdge's
  # We must also allow the GenericGraphEdge here to pass uncontested!
  # The following two cases occur when LOADING a model
  elif( class2Name == 'GenericGraphEdge' ):
    betweenClasses = []
    relaxCardinalityConstraints( class1Name )    
  elif( class1Name == 'GenericGraphEdge' ):
    betweenClasses = []
    relaxCardinalityConstraints( class2Name )
                    
  # No mapping exists between class1 and class2
  # We are typically trying to 'glue' two different formalisms
  # For the purpose of graph grammars
  else:    
    from GenericGraph_MM import createNewGenericGraphEdge
    btClass = ('GenericGraphEdge',createNewGenericGraphEdge)
    
    # Make sure that the Generic node formalism is loaded
    if( not self.ASGroot.listNodes.has_key('GenericGraphEdge') ):
      self.openMetaModel( GUIModel='GenericGraph' )
    relaxCardinalityConstraints( class1Name, class2Name )

    return intermediateObjectConnection(self,objFrom,objTo,btClass,
                                        smoothConn,simpleConnect )
  
  # Multiple link types possible between the source and target node
  if( len(betweenClasses) > 1):								        
      # Denis Dube, 2005, added filter link types for automatic creation 
      # of certain connections, specifically, hierarchical contain relations.
      # filterLinkTypeList is simply a list of class names of relations that
      #   you do NOT want to be created
      if(filterLinkTypeList == None):
        # No filtering: manually choose a link type
        btClass = self.chooseLinkType(betweenClasses)  
        
      else:
        # Apply the filter to the possible betweenClasses      
        betweenClassesCopy = betweenClasses[:]
        if(filterLinkTypeList):
          for linkTypeFunction in betweenClassesCopy:
            if(linkTypeFunction[0] in filterLinkTypeList):
              betweenClassesCopy.remove(linkTypeFunction)
              
        # Oops, filtered everything out, no good, restore full choice
        if(len(betweenClassesCopy) == 0):
          betweenClassesNames = []
          for linkTypeFunction in betweenClasses:
            betweenClassesNames.append(linkTypeFunction[0])
          showerror('Relations filtered',
                    'Cannot create any relation: ' + betweenClassesNames 
                    + ' are all being filtered out')
          return None
      
        # Filter worked, only 1 possible link type left
        elif(len(betweenClassesCopy) == 1):
          btClass = betweenClassesCopy[0]  
        
        # Filter didn't filter enough! Must still choose between link types
        else:
          btClass = self.chooseLinkType(betweenClassesCopy)
        
  # Only one link type possible between the source and target node
  elif len(betweenClasses)==1:                                                                  
      btClass = betweenClasses[0]		
      if(filterLinkTypeList != None and btClass[0] in filterLinkTypeList):        
        showerror('Relation filtered',
        'Cannot create the relation: ' + btClass[0] + ' is being filtered out')
        return None
  else:												
      # No possibilities -> objects cannot be connected
      if objFrom.isSubclass("graphEntity") and objTo.isSubclass("graphEntity"):
        tkMessageBox.showwarning(
          "Dont know how to connect objects!         ",
          "None of them is a link!",
          parent = self
        )
        return (None, None, None, None, None)   
      # This occurs with hyperedges 
      if( simpleConnect ):
        connHandler = objFrom.connect(objTo, self.inter_connect_points, 
                                      x0, y0, x1, y1, smoothConn, num1st)
        self.inter_connect_points = []
      else:              
        x0,y0 = self.inter_connect_points[:2]
        x1,y1 = self.inter_connect_points[-2:] 
        self.inter_connect_points = self.inter_connect_points[2:-2]
        num1st = len( self.inter_connect_points )
        connHandler = objFrom.connect(objTo, self.inter_connect_points, 
                                      x0, y0, x1, y1, smoothConn, num1st)
        self.inter_connect_points = []
  
      # This typically connects an EDGE to a NODE or vice versa...
      return (connHandler, objFrom, objTo, -1, None)

  # btClass is a tuple (class, method-to-create-a-class-instance), 
  # Creates an object in the middle of both selected objects...
  # Both source and destiation objects are of type
  return intermediateObjectConnection(self,objFrom,objTo,btClass, 
                                    smoothConn,simpleConnect )

  

def intermediateObjectConnection( self, objFrom,objTo,btClass,smoothConn, simpleConnect  ):
  """ 
  Creates an intermediate object to link two entities in:
  Method 1: The old & simple & generally un-aesthetic way
  Method 2: The new & improved way :D
  
  Created June 16, 2004 by Denis Dube 
  """
  #print 'intermediateObjectConnection'
  # Automatically draw the connection, ignoring intermediate points
  # Thus you get 2 segments between your entities and an intermediate node
  if( simpleConnect ):
    
    # Get object dimensions
    fromSX, fromSY = objFrom.getSize()
    toSX, toSY = objTo.getSize()

    # Create new object at midpoint between them
    newObjX, newObjY = (objFrom.x+fromSX/2+objTo.x+toSX/2)/2, (objFrom.y+fromSY/2+objTo.y+toSY/2)/2
    newSemObj = btClass[1](self, newObjX, newObjY, 0)
    
    
    # Evaluate the pre and post conditions in a stupid way...
    res = newSemObj.preCondition(ASG.CREATE)
    if res:  self.constraintViolation(res)
    newSemObj.preAction(ASG.CREATE)    
    res = newSemObj.postCondition(ASG.CREATE)
    if res:  self.constraintViolation(res)
    newSemObj.postAction(ASG.CREATE)

    
    # Now connect objects with the newly created one...
    #todo: we should evaluate pre and post conditions!! Yes we should, Denis, 2005
    connHandle1 = objFrom.connect(newSemObj.graphObject_)
    connHandle2 = newSemObj.graphObject_.connect(objTo)
    return (connHandle1, objFrom, objTo, connHandle2, newSemObj)
  
  # Use the intermediate points to place the intermediate node and extra points
  # These points come from the interactive pilot arrow
  else:
    coords = self.inter_connect_points
    num = len( coords ) / 2
    
    # Odd number of points
    if( (num % 2) == 1 ):
        
      # Straight forward method: newObj is at the center control point
      if( not smoothConn ):
        newObjCoords = coords[ num - 1 : num + 1 ]
        newSemObj = btClass[1](self, newObjCoords[0],newObjCoords[1], 0)
      
        seg1Coords = coords[ : num + 1 ]
        seg2Coords = coords[ num - 1 : ]
        
      # Sneaky method: add new control points in the middle of the two innermost segments
      # Add the newObj in the center of these two new control points
      else:
        virtualCenterPoint = coords[ num - 1 : num + 1 ]
        
        leftCenterPoint = [ (virtualCenterPoint[0] + coords[ num - 3 ]) / 2 , 
                            (virtualCenterPoint[1] + coords[ num - 2 ]) / 2 ]
                            
        rightCenterPoint = [ (virtualCenterPoint[0] + coords[ num + 1 ]) / 2 , 
                             (virtualCenterPoint[1] + coords[ num + 2 ]) / 2 ]
                             
        newObjCoords = [ (leftCenterPoint[0] + rightCenterPoint[0]) / 2,
                        (leftCenterPoint[1] + rightCenterPoint[1]) / 2 ]
        newSemObj = btClass[1](self, newObjCoords[0], newObjCoords[1], 0)
            
        seg1Coords = coords[ : num - 1  ] + leftCenterPoint + newObjCoords
        seg2Coords = newObjCoords + rightCenterPoint + coords[ num + 1 : ] 
                 
      
    # Even number of points, Place newObj in middle of 2 points ( NEW POINT )
    elif( smoothConn ):
      newObjCoords = [ (coords[num-2]+coords[num])/2, (coords[num-1]+coords[num+1])/2  ]
      newSemObj = btClass[1](self, newObjCoords[0],newObjCoords[1], 0)
      seg1Coords = coords[ : num ] + newObjCoords
      seg2Coords = newObjCoords + coords[ num : ] 
      
    # Even number of points, no extra point trickery required (no smooth)
    else:
      newObjCoords = coords[ num - 2 : num  ]
      newSemObj = btClass[1](self, newObjCoords[0],newObjCoords[1], 0)
      
      seg1Coords = coords[ : num  ]
      seg2Coords = coords[ num - 2 : ]
      
    # Evaluate the pre and post conditions in a stupid way...
    res = newSemObj.preCondition(ASG.CREATE)
    if res:  self.constraintViolation(res)
    newSemObj.preAction(ASG.CREATE)    
    res = newSemObj.postCondition(ASG.CREATE)
    if res:  self.constraintViolation(res)
    newSemObj.postAction(ASG.CREATE)
    
      
    # Connection From starting object to intermediate object
    x0, y0 = seg1Coords[:2]
    x1, y1 = seg1Coords[-2:] 
    self.inter_connect_points = seg1Coords[2:-2]
    num1st = len( self.inter_connect_points )
    #print x0,y0,x1,y1,self.inter_connect_points, "<-- seg 1"
    connHandle1 = objFrom.connect(newSemObj.graphObject_, 
                  self.inter_connect_points, x0, y0, x1, y1, smoothConn, num1st)
    
    # Connection from intermediate object to finishing object
    x0, y0 = seg2Coords[:2]
    x1, y1 = seg2Coords[-2:] 
    self.inter_connect_points = seg2Coords[2:-2] 
    num1st = len( self.inter_connect_points )
    #print x0,y0,x1,y1,self.inter_connect_points, "<-- seg 2"
    connHandle2 = newSemObj.graphObject_.connect(objTo,
                  self.inter_connect_points, x0, y0, x1, y1, smoothConn, num1st)
               
    self.inter_connect_points = []
    return (connHandle1, objFrom, objTo, connHandle2, newSemObj)
    
    

def allowGenericLinks(self):
  """
  This method makes constructing graph grammars easier by forcing AToM3 to 
  accept generic links between any entity and any other entity. 
  This is called by pressing a button created in addCopyFromLHSButton() in 
  ATOM3.py (note: button is created for LHS and RHS of GG).
  The modification appears to be completely local to the rule it is applied to.
  """
  result = askyesno( "Allow Generic Links",
            "Are you sure you want to enable generic links between any two"
            + " entities?\n\n"
            + "NOTE: Applies only to this rule. If you close AToM3 and edit"
            + " this rule again\nyou may get errors if you do not enable"
            + " generic links again.",
            parent = self ) 
  if(not result): 
    return
 
  classNameList = self.ASGroot.listNodes.keys()
  classNameList = [className for className in classNameList if 
                   className[:4] != 'ASG_']
  
  # Make sure that the Generic node formalism is loaded
  if( not self.ASGroot.listNodes.has_key('GenericGraphEdge') ):
    self.openMetaModel( GUIModel='GenericGraph' )
  
  # Fix the cardinality table so that generic links are allowed to and from
  # any class we could possibly have.
  for class1Name in classNameList:
    self.CardinalityTable['GenericGraphEdge'][class1Name] = \
                    [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
    self.CardinalityTable[class1Name]['GenericGraphEdge'] = \
                    [('0', 'N', 'Destination'), ('0', 'N', 'Source')]
  
  from GenericGraph_MM import createNewGenericGraphEdge
  btClass = ('GenericGraphEdge', createNewGenericGraphEdge)
  
  # Now fix it so that "connectivity" is possible between any class and any
  # other class using a generic edge.
  for class1Name in classNameList:
    for class2Name in classNameList:
      classList = self.ConnectivityMap[class1Name][class2Name] 
      genericExists = False
      for classFuncTuple in classList:
        if(classFuncTuple[0] == 'GenericGraphEdge'):
          genericExists = True
      if(not genericExists):
        self.ConnectivityMap[class1Name][class2Name].append(btClass)    