# __ File: VisualObj.py __________________________________________________________________________________________________
#  Implements  : class VisualObj
#  Author      : Juan de Lara
#  Description : This is the base class for all graphical Objects
#  Modified    : 24 July 2002
#     - 24 July 2002, by JL: Added methods hasNamedPortInConnector and hasNamedPortInConnector for Named Ports handling
# ____________________________________________________________________________________________________________________

import math
from types import *


class VisualObj:
    """
      Class Attributes:
        - EntityList           : List of Entity descendents
        - LinkList  	       : List of graphLink  descendents
        - Tag2ObjMap           : Dictionary for Public-tag to object mapping
        - TabOrder	       : (integer) counter used to create unique tags
        - ChangesAtRunTime     : (integer) which indicates if the object changes at run-time
      _______________________________________________________________________________________________________________________________________

      Attributes (supossed to be private):
        - self.dc              : canvas where the object is to be drawn.
        - self.x, self.y       : coordinates of the object in the canvas.
        - self.connections     : set of tuples (handler, #order) where #order is 0 o 1 depending on the connection order
        - self.shapeAttrConstr : dictionary for constraints on shape
        - self.attr_display    : dictionary that has the semantic attributes to be displayed
        - self.list            : pointer to EntityList or to LinkList depending on the type of the current object
        - self.out_connections_Points	: dictionary indexed by handlers of tuples (myTag, hisTag, (points), smooth) describing the output segments
       					  Both attributes are updated calling the destroy method.
	- self.isDestroyed : Flag that indicates if this object's been destroyed (that is, its method destroy's been called). If this
	  is the case, the canvas (self.dc) in which this object's been drawn is no longer valid. Added 30 July 2002, JL
	- self.pendingConnections: List with tuples (myTag, hisTag, (points), smooth), of connections which must be drawn when the
	  object gets drawn in some canvas. The reason is that the object was saved, with information about multi-point connections,
	  then retrieved, and it is still not drawn (so we cannot have this information in self.out_connections_Points, because
	  we still don't have the connection handlers)
      _______________________________________________________________________________________________________________________________________

      Private Methods:
        - add2List(self, baseClasses):
              Adds the object to the list EntityList if one of the classes of 'baseClasses' is 'Entity', otherwise adds it to LinkList
      _______________________________________________________________________________________________________________________________________

      Public Methods:
        - toString(self):
              Prints information about the object
        - ModifyAttribute(self, name, new_value):
              Modifies the visible value of an attribute that is being displayed. As it is being displayed,
              it should be in the dictionary attr_display
        - removeFromList(self):
              Removes itself from one of the lists of current objects
        - Draw(self, dc):
              Draws object in canvas 'dc'
        - DrawObject(self):
              Abstract method to draw the object in canvas, called by method 'Draw'.
        - Move(self, delta_x, delta_y):
              Abstract method to move the object in the canvas
        - getMinDistance_Connectors2Fixed (self, graphObject, fx, fy):
              Returns the connector (cx, cy) of graphObject which make minimum the distance to (fx, fy)
        - getMinDistance_Connectors2Connectors (self, objFrom, objTo):
              Returns the pair of connectors (cx0, cy0, cx1, cy1) which are nearer and are free
        - moveGGLabel (self, dx, dy ):
              Moves the Graph Grammar Label by (dx, dy)
        - drawGGLabel (self, drawing):
              Draws the Graph Grammar label that the semantic object has
        - Destroy(self):
              Destroys graphical object:
              - erases it from the canvas.
              - removes it from its list
              - removes the entry in the dictironary
        - isSubclass( self, which):
              returns != 0 if i'm a subclass of which (which is the string name of the class)
        - changeTag (self, newTag):
              changes its tag for a new one
        - preAction(self, actionID, * params):
              Abstract method to evaluate graphical pre-actions.
        - postAction(self, actionID, * params):
              Abstract method to evaluate graphical post-actions.
        - preCondition(self, actionID, * params):
              Abstract method to evaluate graphical pre-conditions.
        - postCondition(self, actionID, * params):
              Abstract method to evaluate graphical post-conditions.
        - writeConstructor2File (self, file, objectName, indent, semObjectName):
              Prints a constructor of itself in the given file (the variable name is objectName)
        - select (self, tag, handler, x, y):
              Selects the object corresponding to tag. Adds the tag 'selected' to the tags
        - connectActions (self, htuple):
              Abstract method to make some actions when we are the destination of a connection.
        - smooth (self, handler):
              Abstract method (to be filled by graphLinks) to smooth a connection segment
        - getConnectionCoordinates( self, direction, obj, number = 1):
              Gets the coordinates of the connection that joins this object and 'obj', the connection has the direction
              given by 'direction' which is the string 'IN' or 'OUT'. number is the connection number. It is possible to
              have several connections between the same objects.
        - getConnectionHandler( self, direction, obj, number = 1):
              Abstract method. Gets the handler of the connection that joins this object and 'obj', the connection has the direction
              given by 'direction' which is the string 'IN' or 'OUT'. number is the connection number. It is possible to
              have several connections between the same objects.
        - itemcget( self, handler, parameter ):
              wraps the method itemcget on the local canvas dc.
        - deletePointFromConnection (self, tag, handler, x, y):
              Abstract method. To be filled by graphLinks.
        - changeConnector (self, hconnection, hnewConnector):
              Abstract method. Changes a connection (the given by the handler hconnection) to a new connector (the given by handler hnewConnector)
        - erase (self):
              Erases the object. Abstract method
        - removeConnectionFromList(self, handler):
              Removes the connection whose handler is handler from the list self.connections. Returns the deleted tuple or None if
              no tuple was removed.
        - removeConnection(self, atom3i, handler):
              Removes the (input or output) connection whose handler is 'handler'. If this is a 1:1 connection, then removes the whole
              connection (and not just the incoming or outgoing segment).
              - Should return Returns:
                -1 if handler is not a connection.
                0  if handler corresponds to an output segment
                1  if handler corresponds to an input  segment
               2  if the whole connection has been removed
        - hasConnectHandler(self, ch):
              checks if the object has a connection with handler 'ch'
        - translate(self, pts):
              adds object coordinates to the points in the list pts
        - reverseList2by2 (self, list):
             Reverses the list, taking its element 2 by 2 (they are pair of points...)

    """

    # events...
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
    MOVE       = 10         # changed 13/03/03

    # class attribute to handle objects (links and entities) and tags

    EntityList   = []	    	# List of Entity descendents
    LinkList  = []	    	# list of graphLink  descendents
    Tag2ObjMap = {}         	# Public-tag to object mapping
    TabOrder = 0		# counter used to create unique tags

    def __init__(self):
        """ Initializes object:
            - creates a unique tag.
            - adds it to the dictionary Tag2ObjMap, to be able to retrieve it by tag.
            - adds it to the list of entities or links, depending on its type.
        """
        self.x, self.y = 0, 0
        self.backupCoords = None                                # Hack to fix coord corruption
        self.tag = 'Obj' + str(VisualObj.TabOrder)
        self.ID = VisualObj.TabOrder
        VisualObj.Tag2ObjMap[self.tag] = self			# puts object in dictionary
        VisualObj.TabOrder = VisualObj.TabOrder + 1		# increments the counter
        self.__add2List( )		                        # add object to correspoinding class list
        self.dc = None                                  	# canvas to draw object into
        self.connections= []					# set of tuples (handler, #order) where #order is 0 o 1 depending on the connection order
        self.shapeAttrConstr = {}				# dictionary for constraints on shape
        self.attr_display = {}					# dictionary that has the semantic attributes to be displayed
        self.out_connections_Points= {}				# dictionary with tuples that describe the outgoing connections (points, smoothing and so on...)
        self.ChangesAtRunTime = 0# flag that indicates if the object changes at run time
        self.pendingConnections = []				# Added 30 July 2002
        self.isDestroyed = 0					# Added 30 July 2002, flag that indicates if destroy() method's been called
        self.namedConnectors = {} # Dictionary for named connectors. IT'LL ONLY GET SOME VALUE IN graphEntity instance. Added 4 Nov 2002 by Juan de Lara
                
        # Graphical Layout Contraints Dictionary, Added 17 July 2004, Denis Dube
        self.layConstraints = dict()
        # QOCA linear constraints --> list of associated variables
        self.qocaVariables = []   # These need to be killed if this entity dies
        self.qocaConstraints = [] # These need to be killed if this entity dies        
        #todo: qoca vars
             
    # ______________________________________________________________________________________________________________________
    #				PRIVATE METHODS
    # ______________________________________________________________________________________________________________________

    def __add2List(self):
        """
           Adds the object to the list EntityList if I'm a sub-class of graphEntity, otherwise adds it to LinkList
        """      
        #todo: changed from "from graphEntity import *"
        from graphEntity import graphEntity
        if issubclass(self.__class__, graphEntity):
           self.list = VisualObj.EntityList
        else:
           self.list = VisualObj.LinkList
	self.list.append(self)

    # ______________________________________________________________________________________________________________________
    #				PUBLIC METHODS
    # ______________________________________________________________________________________________________________________

    def update_connection_points ( self, handler, dx, dy , idx1, idx2):
        """
           Updates the out_connections_Points dictionary, because the handler has been moved. idx1 and idx2
           indicates which extreme should be moved.
           Added 23/12/2002 by JL
        """
        if handler in self.out_connections_Points.keys():
           coordinates = self.out_connections_Points[handler][2]
           coordinates[idx1] = coordinates[idx1]+dx
           coordinates[idx2] = coordinates[idx2]+dy

    def distance ( self, p1x, p1y, p2x, p2y ):
        """
           Calculates the distance between the two points given by (p1x, p1y) (p2x, p2y)
        """
        return math.sqrt((p1x-p2x)*(p1x-p2x)+(p1y-p2y)*(p1y-p2y))


    def toString(self):
        """
           returns a string with information about the object
        """
        return self.tag + ' = ' + self.__class__.__name__ + '(' + str(self.x) + ', ' + str(self.y) + ')'

	
    def ModifyAttribute(self, name, new_value):
        """
           Modifies the visible value of an attribute that is being displayed. As it is being displayed,
           it should be in the dictionary attr_display
        """
        if self.attr_display.has_key(name) and self.dc:
            self.dc.itemconfig(self.attr_display[name], text = str(new_value))

    def removeFromList(self):
        """
           Removes itself from one of the lists of current objects
        """
        self.list.remove(self)

    def Draw(self, dc):
        """
           Draws object in canvas 'dc'
        """

        self.dc = dc
        self.DrawObject()

    def DrawObject(self):
        """
           Abstract method to draw the object in canvas
        """

        pass	# not implemeneted here, to be overriden

    def Move(self, delta_x, delta_y):
        """
           Abstract method to move the object in the canvas
        """
        pass	# not implemeneted here, to be overriden

    def getNearestConnectorHandler (self, px, py):
        """
           Gets the handler of the nearest connector
        """
        pass
      
          

    def getMinDistance_Connectors2Connectors (self, objFrom, objTo):
        """
           Returns the pair of connectors (cx0, cy0, cx1, cy1) which are nearer and are free
        """
        maxDistance, maxFreeDistance = 20000, 20000				# flag with the minimum distance so far...
        mdx0, mdy0, mdx1, mdy1 = 0,0,0,0
        for i in objFrom.connectors:
          for j in objTo.connectors:
            x0, y0, x1, y1 = objFrom.getCoords(i)
            x2, y2, x3, y3 = objTo.getCoords(j)
            xc1, yc1, xc2, yc2 = (x0+x1)/2, (y0+y1)/2, (x2+x3)/2, (y2+y3)/2
            actDistance = self.distance(xc1, yc1, xc2, yc2)
            if actDistance < maxDistance:
               maxDistance = actDistance
               mdx0, mdy0, mdx1, mdy1 = xc1, yc1, xc2, yc2
               if (actDistance < maxFreeDistance) and (objFrom.isFree(xc1, yc1, xc2, yc2) or objTo.isFree(xc1, yc1, xc2, yc2)):
                  maxFreeDistance = actDistance
                  mfdx0, mfdy0, mfdx1, mfdy1 = xc1, yc1, xc2, yc2
        if maxFreeDistance < 20000: return( mfdx0, mfdy0, mfdx1, mfdy1)
        else: return ( mdx0, mdy0, mdx1, mdy1)

    def removeConnectionFromList(self, handler, position = 0):
        """
            Removes the connection whose handler is handler from the list self.connections. Returns the deleted tuple
            or None if no tuple was removed
        """
        for htuple in self.connections:
            if htuple[position] == handler:
                self.connections.remove(htuple)
                return htuple
        return None

    def Destroy(self):
        """
            Destroys graphical object:
            - erases it from the canvas.
            - removes it from its list
            - removes the entry in the dictironary
        """
        try:
          self.dc.delete(self.tag)
        except:
          print "WARNING: tag ", str(self.tag), " not found & not removed by Destroy of VisualObj.py (Severity = LOW)"
        if self in self.list:
           self.list.remove(self)
        # We delete tags like this, because we may have done changes to the tags that are not reflected in this dictionary...
        for node in VisualObj.Tag2ObjMap.keys():                             # This may happen if we are the center of a link...
            if VisualObj.Tag2ObjMap[node] == self:
                del VisualObj.Tag2ObjMap[node]

    def isSubclass( self, which):
        """
           returns != 0 if i'm a subclass of which (which is the string name of the class)
        """
        bases = self.__class__.__bases__					# obtain the list of all the node's base classes
        for base in bases:							# iterate over all the base classes
           if base.__name__ == which: return 1					# ey! we have found a coincidence
        return 0								# if we have reached this point, then it is not a subclass

    def changeTag (self, newTag):
        """
           changes its tag for a new one
        """
        # EY! WE SHOULD CHANGE THE TAG2OBJMAP, BUT WHAT IF WE HAVE REPEATED TAGS??
        # Indeed! Why would you need to change the tag?
        self.tag = newTag

    def preAction(self, actionID, * params):
        pass

    def postAction(self, actionID, * params):
        pass

    def preCondition(self, actionID, * params):
        pass

    def postCondition(self, actionID, * params):
        pass

    def writeConstructor2File (self, file, objectName, indent, semObjectName):
      """
         Prints a constructor of itself in the given file (the variable name is objectName)
      """
      myName = self.__class__.__name__
      #file.write(indent+"from "+myName+" import *\n")
      file.write(indent+objectName+' = '+myName+'('+str(self.x)+','+str(self.y)+','+semObjectName+')\n')

    def select (self, tag, handler, x, y):
      """
         Selects the object corresponding to tag. Basically adds the tag 'selected' to the tags
      """
      self.dc.addtag_withtag( "selected", tag )    # add them the "selected" tag

    def connectActions (self, htuple):
      """ 
         Abstract method to make some actions when we are the destination of a connection. 
      """
      pass

    def smooth (self, handler):
      """
         Abstract method (to be filled by graphLinks) to smooth a connection segment
      """
      pass

    def getConnectionHandler( self, direction, obj, number = 1):
      """
         gets the handler of the connection that joins this object and 'obj', the connection has the direction
         given by 'direction' which is the string 'IN' or 'OUT'. number is the connection number. It is possible to
         have several connections between the same objects.
      """
      if direction == "IN":
           connDirection = 1                                                      # connection direction
           otherObjDir   = 0
      else:
           connDirection  = 0
           otherObjDir   = 1

      numFound = 0                                                                # num of connections found -> 0
      for htuple in self.connections:
          tcon = obj.hasConnectHandler(htuple[0])
          if tcon and tcon[1] == otherObjDir:
            numFound = numFound + 1
            if numFound == number:                                                # see if the connection order is the appropriate
               return htuple[0]
      return None


    def itemcget( self, handler, parameter ):
      """
         wraps the method itemcget on the local canvas dc.
      """
      try:
        return self.dc.itemcget(handler, parameter)
      except:
        if(parameter == 'smooth'):
          return False
        else:
          raise

    def deletePointFromConnection (self, tag, handler, x, y):
      """
          Abstract method. To be filled by graphLinks.
      """
      pass

    def changeConnector (self, hconnection, hnewConnector):
      """
          Abstract method. Changes a connection (the given by the handler hconnection) to a new connector (the given by handler hnewConnector)
      """
      pass

    def erase (self, atom3i, entityOnly):
      """
         Abstract method. It is used to delete the graphical Object.
         entityOnly flag used to delete only the entity and not the 
         connections that also depend on it.
      """
      pass

    def removeConnection(self, atom3i, handler):
      """
         Abstract Method. Removes the (input or output) connection whose handler is 'handler'. If this is a 1:1 connection, then removes the whole
         connection (and not just the incoming or outgoing segment).
         - Should return Returns:
             -1 if handler is not a connection.
             0  if handler corresponds to an output segment
             1  if handler corresponds to an input  segment
             2  if the whole connection has been removed
      """
      pass

    def hasConnectHandler(self, ch, pos = 0):
        """
           checks if the object has a connection with handler 'ch' in the pos 'pos'
           Changed 6 Aug by JL
        """
        for conn in self.connections:
           if conn[pos] == ch: return conn
        return 0

    def getConnectionCoordinates( self, direction, obj, number = 1):
      """
         gets the coordinates of the connection that joins this object and 'obj', the connection has the direction
         given by 'direction' which is the string 'IN' or 'OUT'. number is the connection number. It is possible to
         have several connections between the same objects.
         Changed 31 July 2002 to return a 3-element tuple with the last element being the smooth flag.
      """
      if direction == "IN":
           connDirection = 1                                                      # connection direction
           otherObjDir   = 0
      else:
           connDirection  = 0
           otherObjDir   = 1

      numFound = 0                                                                # num of connections found -> 0
      for htuple in self.connections:
          tcon = obj.hasConnectHandler(htuple[0])
          if tcon and tcon[1] == otherObjDir:
            numFound = numFound + 1
            if numFound == number:                                                # see if the connection order is the appropriate
               # Quick hack by Denis Feb 11, 2005 (this bug nuked my whole GG!)
               try:
                   self.dc.coords(htuple[0])
               except:
                   self.isDestroyed = True
               if not self.isDestroyed:
                   #print "not isDestroyed"
                   coordinates = self.dc.coords(htuple[0])
                   ssmooth = self.dc.itemcget(htuple[0], "smooth")                 # Added 31 July 2002-
                   if ssmooth: smooth = 1
                   else: smooth = 0
               elif self.out_connections_Points.has_key(htuple[0]):               # Added 30 July 2002
                  #print "connections_Points" 
                  # This means the canvas is closed, and we have to look in self.out_connections_Points, as
                  # we store here information about the connection points when the canvas closes...               
                  myTag, hisTag, coords, smooth, lencoords = self.out_connections_Points[htuple[0]]
                  return ( coords, lencoords, smooth )
                          
               return ( coordinates, len(coordinates)/2, smooth)
      # Look in the Pending connections list...
      if direction == 'OUT':
         first  = self.tag
         second = obj.tag
      else:
         first = obj.tag
         second = self.tag
      #print "pendingConnections = ", self.pendingConnections, " f = ", first, " s = ", second
      for element in self.pendingConnections:
          if element[0] == first and element[1] == second:
             return ( element[2], element[3], element[4] )

      return None

    
    

    def moveGGLabel (self, dx, dy ):
      """
         Moves the Graph Grammar Label by (dx, dy)
      """
      if "GGLabel" in self.attr_display.keys():						# 1st check if the Graph Grammar Label has been drawn
         self.dc.move(self.attr_display["GGLabel"], dx, dy)

    def drawGGLabel (self, drawing):
      """
         Draws the Graph Grammar label that the semantic object has. If it has been already drawn, the it modifies it.
      """
      if self.attr_display.has_key("GGLabel"):			# Added 30 July 2002, by JL
         drawing.itemconfig(self.attr_display["GGLabel"], text = self.semanticObject.GGLabel.toString() )
      else:
         import tkFont
         helv12 = tkFont.Font ( family="Helvetica", size=12, weight="bold" )
         h = drawing.create_text(self.translate([-3, -3]), font=helv12,
                              tags = (self.tag, self.semanticObject.getClass()), 
                              fill = "black", 
                              text=self.semanticObject.GGLabel.toString())
#         h = drawing.create_text(self.translate([-3, -3]), 
#                              tags = (self.tag, self.semanticObject.getClass()), 
#                              fill = "dark gray", 
#                              text=self.semanticObject.GGLabel.toString())
       
         self.attr_display["GGLabel"] = h
      #self.gf0 = GraphicalForm(drawing, h, "gf0")
      #self.graphForms.append(self.gf0)

    def destroy(self):
      """
      	 The graphical appearance of the object is going to be destroyed, so we must store its description. Particularly, we will store the
      	 description of input and output segments
      """
      if not self.isDestroyed:
         self.isDestroyed = 1								      # Set the destroyed flag
         for handler in self.out_connections_Points.keys():                                   # only output connections will be stored
            htuple = self.out_connections_Points[handler]				      # get the stored information
      	    newCoords = self.dc.coords(handler)                                               # get the actual coordinates      	    
            currentSmooth = self.dc.itemcget( handler, "smooth")                              # get current smooth status
            if currentSmooth == "0": doSmooth = 0
            else: doSmooth = 1
	    # Just trying...
	    if len(newCoords) > 6:
	    	nc = self.reverseList2by2(newCoords[2:len(newCoords)-2])
	    	newCoords[2:len(newCoords)-2] = nc
            self.out_connections_Points[handler] = (htuple[0], htuple[1], newCoords, doSmooth, len(newCoords)/2)     # create and store the new tuple

    def getInfoTuple(self, fromObj, toObj, index, whichDictionary ):
      """
         look in dictionary out_connections_Points for a tuple whose two first elements are fromObj and toObj.
         If the tuple is found, it returns a tuple (<tuple-found>, handler)
         Returns None if the tuple is not found.
      """
      numConn = 0
      for handler in whichDictionary.keys():
         htuple = whichDictionary[handler]
         if htuple[0:2] == ( fromObj, toObj ):
            numConn = numConn + 1
            if numConn == index:
               return (htuple, handler)
      return None
                 
    def reverseList2by2 (self, list):
      """
         Reverses the list, taking its element 2 by 2 (they are pair of points...)
      """
      reversed = []
      counter = len(list)-1
      while counter > 0:
          px, py = list[counter-1], list[counter]
          reversed.append(px)
          reversed.append(py)
          counter = counter - 2
      return reversed

    def hasGraphicalConnection(self, node):
      """
         checks if there are a connection between this object and node.
         Check this method. It WILL NOT WORK WITH THE NEW VERSION OF ATOM3
      """
      for connec in self.connections:
            if node.hasConnectHandler(connec[0]): return connec
      return -1

    def deleteGraphicalConnectionsList(self):
      """
         Deletes the graphical connections. Ey! this function is overwrited in graphLink's
      """
      while len(self.connections) > 0: self.connections.pop()      

    def deleteGraphicalConnections(self):
      """
         Deletes the graphical connections
      """
      for c in self.connections: 
        self.dc.delete(c[0])      
      self.deleteGraphicalConnectionsList()

    def write2File(self, file, indent):
      """
         Writes its properties into a file (Abstract method).
      """
      pass

    def getConnectedObjectByHandler (self, handler):
      """
         Returns the object connected to self by the connection handler, if any (Abstract method).
         Created 24 July 2002 by JL                  
      """
      pass

    def hasNamedPortInConnector (self, handler):
      """
         Looks to see if in the connector 'handler' there is a named Port. If it does, return the name.
         Abstract method
         Created 24 July 2002 by JL
      """
      pass

    def getPendingConnection( self, dest_tag, index = 1 ):
      """
	Gets the tuple in the pendingConnections list which has "dest_tag" as "destination object tag" (index = 1) or
	origin object tag (index == 0). Returns None if it does not exists.
        Created 30 July 2002 by JL
      """
      for tuple in self.pendingConnections:
        if tuple[index] == dest_tag: return tuple
      return None

    def removePendingConnection( self, tuple ):
      """
	Removes tuple from pendingConnections
	Created 30 July 2002 by JL
      """
      if tuple in self.pendingConnections: self.pendingConnections.remove(tuple)

    def getSize(self):
      """
         Abstract (Virtual pure) method that should returns the a tuple with the object's dimensions
         to be implemented in children classes
      """
      pass
      
    #----------------------------- Modified by Denis Dube, Summer 2004 --------------------------------
      
      
    def getMinDistance_Connectors2Fixed (self, graphObject, fx, fy, unamedOnly = False ):
        """
           Returns the connector (cx, cy) of graphObject which makes minimum the distance to (fx, fy)
        """

        if( unamedOnly ):
          connectorList = graphObject.connectors[:] # <-- make copy of connectors
          # Remove the named connectors from the list
          for handler in graphObject.namedConnectors.keys():
            connectorList.remove( handler )
        else:
          connectorList = graphObject.connectors
          
        maxDistance = 2000							# flag with the minimum distance so far...
        mdx0, mdy0  = 0,0
        for j in connectorList:
           x0, y0, x1, y1 = graphObject.getCoords(j)				# get coordinates of connector # j
           xc1, yc1 = (x0+x1)/2, (y0+y1)/2					# calculate the middle point
           actDistance = self.distance(xc1, yc1, fx, fy)			# calculate distance from (fx, fy) to connector j middle point
           if actDistance < maxDistance:					# if this is less than the minimum distance found so far
              maxDistance = actDistance						# write it down
              mdx0, mdy0 = xc1, yc1
        return (mdx0, mdy0)
 
    def findImagePath( self, fileName ):
        """ 
        Finds the full absolute pathname of a an image file, ie: fileName = 'image.gif' 
        The key assumption is that the file resides in one of the sys.path directories
        Also assumed to be only 1 image with that name in sys.path
        
        This method is currently unused, since image embedding is more 'fun'.
        However, if we had some truly large GIF's, we might want to use this
        instead to load the GIF image. 
        """
        import sys, os
        for path in sys.path:
            if( not os.path.isdir( path ) ): continue
            for file in os.listdir( path ):
                if( file == fileName ):
                    return os.path.join( path, fileName )
        return None  
    
    def getGraphClassName( self ):
        """ Returns the graphical appearence name, ie: graph_SuperIcon """
        return self.__class__.__name__
    
    
    def getCanvas(self):
        """ Returns the canvas this entity is drawn on (may be none)"""
        return self.dc
    
    def saveBackupCoords(self ):
        """
        This is called by ASG.py addNode() when adding nodes to the model
        Purpose: backup coords are a quick fix for mysterious coord corruption
        with the visual GraphGrammar models
        Called by ASG.py addNode()
        """
        self.backupCoords = [self.x,self.y]
        #print "Backup coords", self , self.backupCoords
        
    def checkCoords(self):
        """
        Checks the current self.x and self.y coordinates for corruption
        Uses backup coords as a quick fix for mysterious coord corruption
        with the visual GraphGrammar models
        This is called by graphEntity.py redrawObject()
        
        NOTE: Better fix might be to just restore backup right away since
        the GraphGrammar entities seem to always be screwed up...
        """        
        if( self.backupCoords == None ): return 
        
        minX = self.dc.winfo_x()
        minY = self.dc.winfo_y()
        maxX = self.dc.winfo_width()
        maxY = self.dc.winfo_height()
                
        if( self.x < minX or self.y < minY or self.x > maxX or self.y > maxY ):
            # This hack seems to totally fix the problem, however it's not
            # very statisfying... so I'll leave this message here for now...
            print "WARNING: VisualObj.py checkCoords() had to fix corrupted coords (Severity = LOW)"
            if( self.x < minX ):
                self.x = self.backupCoords[0]
            elif( self.y < minY ):
                self.y = self.backupCoords[1]
            elif( self.x > maxX ):
                self.x = self.backupCoords[0]
            elif( self.y > maxY ):
                self.y = self.backupCoords[1]
        
    def translate(self, pts):
      """
      Adds object coordinates to the points in the list pts
      """      
      for i in range(0,len(pts),2):
        pts[i] = pts[i] + self.x
        pts[i+1] = pts[i+1] + self.y
      return tuple(pts)
    
    
    def qocaCleanup(self, atom3i):
      """ Remove QOCA variables/constraints from solver on obj delete """
      #todo: qoca cleanup 
      
#      print 'Cleanup', self.tag 
#      print 'before'
#      for var in atom3i.qocaSolver.activeVariables:
#        print var
#      for var in atom3i.qocaSolver.activeConstraints:
#        print var
      atom3i.qocaSolver.delVariables(self.qocaVariables)
      atom3i.qocaSolver.delConstraints(self.qocaConstraints)
      self.qocaVariables = []
      self.qocaConstraints = []
#      print 'after'
#      for var in atom3i.qocaSolver.activeVariables:
#        print var
#      for var in atom3i.qocaSolver.activeConstraints:
#        print var
   
      
   