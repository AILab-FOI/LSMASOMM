# _ File: graphLink.py ___________________________________________________________________________________________
#  Implements  : class graphLink
#  Author      : Juan de Lara
#  Description : Base class for the drawings of links
#  Modified    : 20 Jul 2002
#  - Changes: corrected bug in redrawObject method
#     - 24 July 2002, by JL: Added methods getNamedPort, hasNamedPortInConnector and hasNamedPortInConnector for
#       Named Ports handling
# ________________________________________________________________________________________________________________

import cmath

from VisualObj import *

class graphLink(VisualObj):
  """
    WARNING: The following list does NOT include all contents of this file - Denis
      
    Attributes (these all should be private):
       - self.centerObject: A pointer to the central object or None if it does no exists.
       - self.in_connections_: List of tuples of three elements (handler, tag, segmentObject, linkObject),
         where handler is the handler of the incoming segment line, tag is its tag, segmentObject is a pointer
         to the segment drawing and linkObject (or None) is a pointer to the link drawing (or None).
       - self.out_connections_: The same but for outgoing connections.
       - self.has1stLink       : 1 or 0 depending if the incoming links have a drawing
       - self.x1l, self.y1l    : Coordinates of the last drawn incoming link drawing
       - self.firstLinkName    : The first link drawing name
       - self.has2ndLink       : 1 or 0 depending if the outgoing links have a drawing
       - self.x2l, self.y2l    : Coordinates of the last drawn outgoing link drawing
       - self.secondLinkName   : The second link drawing name
       - self.has1stSegment    : 1 or 0 depending if the incoming segments have a drawing
       - self.x1s, self.y1s    : Coordinates of the last drawn incoing segment drawing
       - self.firstSegmentName : The first segment drawing name
       - self.has2ndSegment    : 1 or 0 depending if the outgoing segments have a drawing
       - self.x2s, self.y2s    : Coordinates of the last drawn outgoing segment drawing
       - self.firstSegmentName : The segment segment drawing name
       - self.unconnected      : list of unconnected segments. Tuples (handler, tag, segmentObject, linkObject)
       - self.selectedHandler  : Handler of the selected part of the link. If its value is -1, then nothing is selected.
       - self.aFirstLink       : temporary object for incoming link drawings.
       - self.aSecondLink      : temporary object for outgoing link drawings.
       - self.aFirstSegment    : temporary object for incoming segment drawings.
       - self.aSecondSegment   : temporary object for outgoing segment drawings.
       - self.drawings         : A list with all the drawings of the link
       - self.linkInfo         : A structure of type linkEditor with all the information about the structure of the link
       - self.selectedHandler  : Handler of the selected connection, or NOTHING_SELECTED or CENTER_SELECTED
       - self.selectedPoint    : Point that is selected if the selected thing is a connection
       - self.oldColor         : tuple with the old colors of the selected connections

   __________________________________________________________________________________________________________________________________________________
    Private methods:
       - __drawConnection(self, canvas, linkObject, segmentObject, linkx, linky, linkInfo_Link, linkInfo_Segment, list2include):
             Draws an incoming or outgoing link in the canvas, given the extreme object drawing (may be None), the segment object drawing (may be None)
             and the coordinates of the extreme. linkInfo_Link should be one of self.linkInfo.FirstLink or SecondLink. linkInfo_Segment should be
             one of self.linkInfo.FirstSegment or SecondSegment. list2include should be self.in_connections_ or self.out_connections_.
             It also adds the connection into list2include. The function returns the handler of the drawed line.
       - __drawSegment( self, drawing, x0, y0, x1, y1, arrowObject, segmentObject, tag):
	     Draws a line from (x0, y0) to (x1, y1) using the formatting information of arrowObject and segmentObject. This information is
             from the linkEditor information. It provides the link the tag 'tag'. The order of coordinate is from link to center. It does not actually draw
             the objects!. Returns the handler.
       - __handlerInList( self, handler, list ):
             Returns the tuple of handler if handler is in list, which is a list of tuples (handler, tag, objLink, objSegement). Returns None if it does not
             belong to the list.
       - __get_MinDistance_Point2List (self, x, y, coords):
             returns the index of the point from coords that makes minimum the distance to point (x, y).
       - __have2removeAll(self, atom3i):
             Called by removeConnection. Looks in the cardinalities (Attribute CardinalityTable of atom3i) table, to see if we should erase the whole link
             (i.e. it is a 1 to 1 link, not a hyperlink)
       - __removeSegment(self, handler):
             Removes the (input or output) segment whose handler is 'handler'.
             - Returns:
                -1 if handler is not a connection.
                0  if handler corresponds to an output segment
                1  if handler corresponds to an input  segment
______________________________________________________________________________________________________________________________________________
    Public methods:
       - DrawObject(self, canvas, showGG = 0):
             Redefines this method to draw the link properly.
       - connect(self, obj, intermediatePoints = []):
             Connects this object to Object obj which must be a child of VisualObj, where obj must be a child of VisualObject. intermediatePoints
             is a list of intermediate points between origin and destination. The function returns the handler of the connection.
       - connectActions (self, htuple):
             Actions performed if this object is the destination of a connection.
             Removes the tuple from the list of unconnected segments
       - getSegment(self, whichDirection):
             returns an unconnected input or output segment or creates a new one if there's no unconnected.
             - whichDirection is a string with values "IN" or "OUT"
             - The function returns a tuple (handler, tag, segmentObject, linkObject).
       - removeConnection(self, handler):
             Removes the (input or output) connection whose handler is 'handler'.
             - Returns:
                -1 if handler is not a connection.
                0  if handler corresponds to an output segment
                1  if handler corresponds to an input  segment
       - select (self, tag, handler, x, y):
             Selects the point of the link (if it is a multi-point link) or center part corresponding to tag. Extends the method of VisualObj
       - getDrawing(self, name, cx, cy) :
             Given the class name and the coordinates, tries to create an object of that class, this may not exists, but if
             it does, it is a subclass of graphEntity.
       - getHandlerOfConnection( self, direction, obj, number = 1):
             gets the handler of the connection that joins this object and 'obj', the connection has the direction
             given by 'direction' which is the string 'IN' or 'OUT'. number is the connection number. It is possible to
             have several connections between the same objects.
       - deletePointFromConnection (self, tag, handler, x, y):
             Selects the point of the link (if it is a multi-point link) nearest to x, y and deletes it
       - changeConnector (self, tag, hconnection, hnewConnector):
             Changes a connection (the given by the handler hconnection) to a new connector (the given by handler hnewConnector)
       - erase (self, atom3i):
             Deletes the graphical Object.
       - getConnectionCoordinates( self, direction, obj, number = 1):
             Specializes the method defined in VisualObj for the case of two graphLinks.
  """

  # Constants to define what is actually selected

  NOTHING_SELECTED = -1
  CENTER_SELECTED  = -2
  ALL_SELECTED     = -3

  def __init__(self, xc, yc, linkInfo, semObject  ):
     """Creates a link, receives information about where the each link must be created, and also the center.
        Details about how to draw each part (links, segments and center) are stored in linkInfo, which is an
        object of type linkEditor. semObject is the associated semantic entity. """
     VisualObj.__init__(self)							# put itself in appropriate lists
     self.selectedHandler  = self.NOTHING_SELECTED                              # handler of the "selected" object
     self.selectedPoint    = -1							# number of the selected point (if the selected thing is a connection)
     self.in_connections_  = []							# handlers of incomming segments (1st segments)
     self.out_connections_ = []							# handlers of outgoing segments (2nd segments)
     self.unconnected      = []							# unconnected segments (in OR out)
     self.drawings	   = []							# drawings (of type graphEntity) that this link has
     self.has1stLink       = 0							# initialize flags...
     self.has2ndLink       = 0
     self.has1stSegment    = 0
     self.has2ndSegment    = 0

     self.semanticObject = semObject

     # get the drawing of the center...
     centerObjectName = 'graph_'+linkInfo.Center.getValue()[0]
     self.centerObject = self.getDrawing(centerObjectName, xc, yc)
     if self.centerObject:
        self.centerObject.removeFromList()					# remove from the global list of entities, 'cause we are a link
        self.centerObject.changeTag(self.tag)					# change the part's tag
        csx, csy = self.centerObject.sizeX, self.centerObject.sizeY
        # Added 8 April 2003 by JL
        #self.centerObject.Move(-self.centerObject.sizeX/2, 0)
        self.drawings.append(self.centerObject)
     else: csx, csy = 0, 0
      
     self.x, self.y = xc, yc
     self.x1l, self.y1l = self.x-20, self.y+csy/2                                      # choose a position from the 1st segment
     self.x2l, self.y2l = self.x+csx+20, self.y+csy/2                                  # choose a position from the 1st segment 

     # get the drawing of the 1st link...
     self.firstLinkName = 'graph_'+linkInfo.FirstLink.decoration.getValue()[0]		# name of the first link drawing
     self.aFirstLink = self.getDrawing(self.firstLinkName, self.x1l, self.y1l) 	        # try to instanciate an object with that name
     if self.aFirstLink:                                                             	# if we've done it
     	self.aFirstLink.removeFromList()                       				# remove from the global list of entities, 'cause we are a link
     	self.aFirstLink.changeTag(self.tag)                                     	# Change whichever tag it has to current graphLink tag
     	self.has1stLink = 1								# annotate that we have 1st links drawings
     	self.drawings.append(self.aFirstLink)
     	# copy the displayed attributes of the object in the local dictionary
     	
     # get the drawing of the 2nd link...
     self.secondLinkName = 'graph_'+linkInfo.SecondLink.decoration.getValue()[0]		# name of the first link drawing
     self.aSecondLink = self.getDrawing(self.secondLinkName, self.x2l, self.y2l)		# try to instanciate an object with that name
     if self.aSecondLink:                                                       	# if we've done it
        self.aSecondLink.removeFromList()                         			# remove from the global list of entities, 'cause we are a link
        self.aSecondLink.changeTag(self.tag)                                    	# Change whichever tag it has to current graphLink tag
        self.has2ndLink = 1			                                	# annotate that we have 1st links drawings
        self.drawings.append(self.aSecondLink)					
        # copy the displayed attributes of the object in the local dictionary

     # get the drawing of the 1st segment...
     self.firstSegmentName = 'graph_'+linkInfo.FirstSegment.decoration.getValue()[0]  # Name of the first segment drawing
     self.x1s, self.y1s = (xc+self.x1l)/2, (yc+self.y1l)/2				# Store coordinates of 1st segment drawing
     
     if linkInfo.FirstSegment.decoration_Position and linkInfo.FirstSegment.decoration_Position.toString() != "No decoration":        
        self.aFirstSegment = self.getDrawing(self.firstSegmentName, self.x1s, self.y1s)	# try to create an object of the first segment drawing...
        if self.aFirstSegment:
           self.aFirstSegment.removeFromList()                         			# remove from the global list of entities, 'cause we are a link
           self.aFirstSegment.changeTag(self.tag)                                    	# Change whichever tag it has to current graphLink tag
     	   self.has1stSegment = 1							# Annotate that we have 1st links drawings
           self.drawings.append(self.aFirstSegment)
     else:
        self.aFirstSegment = None

     # get the drawing of the 2nd segment...
     self.secondSegmentName= 'graph_'+linkInfo.SecondSegment.decoration.getValue()[0]# Name of the second segment drawing
     self.x2s, self.y2s = (xc+self.x2l)/2, (yc+self.y2l)/2				# Store coordinates of 2nd segment drawing
     if linkInfo.SecondSegment.decoration_Position and linkInfo.SecondSegment.decoration_Position.toString() != "No decoration":       
        self.aSecondSegment= self.getDrawing(self.secondSegmentName, self.x2s, self.y2s)# Try to create an object of the second segment drawing...
        if self.aSecondSegment:
           self.aSecondSegment.removeFromList()                         		# remove from the global list of entities, 'cause we are a link
           self.aSecondSegment.changeTag(self.tag)                                    	# Change whichever tag it has to current graphLink tag
     	   self.has2ndSegment = 1							# Annotate that we have 1st links drawings
     	   self.drawings.append(self.aSecondSegment)
     else:
       self.aSecondSegment = None

     self.linkInfo = linkInfo
     
     self.linkColor = "#000000"         # Default color if all goes wrong
     self.linkColorInitilized = False   # Default color not yet set
     
     self.lastAngle = [math.pi / 2, math.pi / 2]
     
     #todo: auto creation of qoca vars
     from Qoca.constraints.QocaSolverAbstract import getSolver
     solver = getSolver()
     if(solver == None): 
       return
     ID = str(self.ID)
     self.qcX = solver.makeVar('x'+ID, self.x, 8, 512, 
                            callback=lambda x, self=self: self.moveTo(x=x))
     self.qcY = solver.makeVar('y'+ID, self.y, 8, 512, 
                              callback=lambda y, self=self: self.moveTo(y=y))
     self.qcW = solver.makeFixedVar('w'+ID, 0, fixedWeight=65536)
     self.qcH = solver.makeFixedVar('h'+ID, 0, fixedWeight=65536)
     map(self.qocaVariables.append, [self.qcX, self.qcY, self.qcW, self.qcH])
 
  # ________________________________________________________________________________________________________________________________________________
  #						PRIVATE METHODS
  # ________________________________________________________________________________________________________________________________________________

  def __tupleInList (self, key, list, pos = 0):
    """
       Traverses the list, and determines if the list has a tuple whose component number 'pos' is 'key' (returns the tuple in that case, otherwise
       it returns None.
    """
    for htuple in list:
       if htuple[pos] == key: return htuple
    return None

   
  def __drawConnection(self, canvas, linkObject, segmentObject, linkx, linky, linkInfo_Link, linkInfo_Segment, list2include, tag):
     """
         Draws an incoming or outgoing link in the canvas, given the extreme object drawing (may be None), the segment object drawing (may be None)
         and the coordinates of the extreme. linkInfo_Link should be one of self.linkInfo.FirstLink or SecondLink. linkInfo_Segment should be
         one of self.linkInfo.FirstSegment or SecondSegment. list2include should be self.in_connections_ or self.out_connections_.
         It also adds the connection into list2include. The function returns the handler of the drawed line.
     """

     lx, ly = linkx, linky										# coordinates of the extreme

     if linkObject: linkx, linky = linkObject.x, linkObject.y						# update coordinates of extreme if there's a drawing...
     if self.centerObject: self.x, self.y = self.centerObject.x, self.centerObject.y			# update coordinates of the center if there's a center drawing

     VisualObj.Tag2ObjMap[tag] = self                                   				# puts object in dictionary
     if (not self.centerObject) or (not self.centerObject.connectors):					# no drawing in the middle or no connectors in drawing...
        if (not linkObject) or (not linkObject.connectors):						# no drawing in the first link...
           h = self.__drawSegment(canvas, lx, ly, self.x, self.y, linkInfo_Link, linkInfo_Segment, tag, segmentObject)
        else:						
           linkOnex, linkOney = self.getMinDistance_Connectors2Fixed (linkObject, self.x, self.y)	# get nearest connection
           h = self.__drawSegment(canvas, linkOnex, linkOney, self.x, self.y, linkInfo_Link, linkInfo_Segment, tag, segmentObject)
     else:
        if (not linkObject) or (not linkObject.connectors):						# not drawing for 1st link or no conenctors
           centerx, centery = self.getMinDistance_Connectors2Fixed (self.centerObject, lx, ly)    	# get nearest connection
           h = self.__drawSegment(canvas, lx, ly, centerx, centery, linkInfo_Link, linkInfo_Segment, tag, segmentObject)
	else:
           lx, ly, cx, cy,  = self.getMinDistance_Connectors2Connectors (linkObject, self.centerObject )  # get nearest connections
           h = self.__drawSegment(canvas, lx, ly, cx, cy, linkInfo_Link, linkInfo_Segment, tag, segmentObject)
     infoTuple = (h, tag, segmentObject, linkObject)							# create a tuple with the necessary information
     list2include.append(infoTuple)									# add it to the list
     self.unconnected.append(infoTuple)									# for the moment it is unconnected
     return (h, tag)

  def __drawSegment( self, drawing, x0, y0, x1, y1, arrowObject, segmentObject, tag, segmentDrawing):
    """
        Draws a line from (x0, y0) to (x1, y1) using the formatting information of arrowObject and segmentObject. This information is
        from the linkEditor information. It provides the link the tag 'tag'. The order of coordinate is from link to center.
        It does not actually draw the objects!.Returns the handler.
    """
    # draws a line according to self.linkInfo
    hasArrow   = arrowObject.arrow.getValue()[1]			# check if an arrow has to be displayed...
    arrowShape = (arrowObject.arrowShape1.getValue(),arrowObject.arrowShape2.getValue(),arrowObject.arrowShape3.getValue())	# get arrow shape (if any)
    theWidth   = segmentObject.width.getValue()				# get segment width
    doFill     = segmentObject.fill.getValue()                          # get segment color    
    if segmentObject.stipple:                                           # get segment stipple (added 17-10-2002)
       doStipple  = segmentObject.stipple.getValue()                    # get segment stipple (added 17-10-2002)
    else: doStipple = ""                                                # get segment stipple (added 17-10-2002)
    if segmentObject.arrow:                                             # get the segment arrow (if any)
      segArrow = segmentObject.arrow.getValue()[1]
      if segmentObject.arrowShape1 and segmentObject.arrowShape2 and segmentObject.arrowShape3:
         segArrowShape = (segmentObject.arrowShape1.getValue(),segmentObject.arrowShape2.getValue(),segmentObject.arrowShape3.getValue())	# get arrow shape (if any)
      else: segArrowShape = (8, 10, 3)
    else: segArrow = 0  
    # now draw the line!
    if hasArrow:          # draw (at least the 1st arrow)
       if not segArrow:   # draw only one arrow
          handle = drawing.create_line (x0, y0, x1, y1, width=theWidth, fill=doFill, stipple = doStipple, arrow="first", arrowshape = arrowShape, tags = tag)
       else:
          handle = drawing.create_line (x0, y0, x1, y1, width=theWidth, fill=doFill, stipple = doStipple, arrow="both", arrowshape = arrowShape, tags = tag)
    elif segArrow:        # draw 2nd arrow. Modified 17-10-2002
       handle = drawing.create_line (x0, y0, x1, y1, width=theWidth, fill=doFill, stipple = doStipple, arrow="last", arrowshape = segArrowShape, tags = tag)
    else:                 # no arrows...
       handle = drawing.create_line (x0, y0, x1, y1, width=theWidth, fill=doFill, stipple = doStipple, tags = tag)
    # if we have a segment drawing, then move it to the appropriate position!!
    if segmentDrawing: self.drawSegmentIcon(handle, segmentDrawing)
    return handle

  def __handlerInList( self, handler, list ):
    """
       Returns the tuple of handler if handler is in list, which is a list of tuples (handler, tag, objLink, objSegement). Returns None if it does not belong to the list.
    """
    for htuple in list:
       if handler == htuple[0]: return htuple
    return None

  def __distance_Point2Rect( self, x, y, x0, y0, x1, y1 ):
    """
       returns the distance of the point (x, y) to the segment (x0, y0) (x1, y1)
    """
    # calculate the intersection of the rect with a perpendicular passing through (x,y)
    a = x1-x0 
    b = y0-y1
    c = x-x1
    if b == 0:yc = y1                                                                        # rect parallel to x axis
    else:     yc = - ( a*c-y1*a*a/b-y*b )/( a*a/b+b )
    if b!= 0: xc = - ( yc*a-x1*b-y1*a )/b
    else:     xc = - ( yc*b+x*a+y*b )/(x0-x1 )
    return self.distance(x, y, xc, yc)                                                    #return distance to this point

  def __get_MinDistance_Point2List (self, x, y, coords):
    """
       returns the index of the point from coords that makes minimum the distance to point (x, y).
    """
    minDistance = 10000
    minCoord    = -1
    counter     = 0
    while counter < len(coords):							# we do not want to evaluate the initial nor the final points
       cx, cy = coords[counter], coords[counter+1]
       distance = self.distance( x, y, cx, cy )				        # calculate distance
       if distance < minDistance:
           minCoord = counter
           minDistance = distance
       counter = counter + 2
    return minCoord

  def __have2removeAll(self, atom3i):
    """
       Called by removeConnection. Looks in the cardinalities (Attribute CardinalityTable of atom3i) table, to see if we should erase the whole link
    """
    # if we don't have a center and the number of connections is two or less, delete it also.
    if self.centerObject == None and len(self.semanticObject.in_connections_)+len(self.semanticObject.out_connections_) <=2:
       return 1
    myName = self.semanticObject.__class__.__name__
    # look for possible output connections from this link
    if( not atom3i.CardinalityTable.has_key( myName ) ): return 1
    outputs = atom3i.CardinalityTable[myName]
    numOuts = 0
    numInputs = 0
    for out in outputs.keys():
       for card in outputs[out]:
          cardValue = (card[0], card[1])
          if cardValue != ('1', '1') and cardValue != ('0', '1'): return 0
          elif cardValue == ('1', '1') and card[2] == 'Source': numOuts = numOuts + 1
          elif cardValue == ('1', '1') and card[2] == 'Destination': numInputs = numInputs + 1
          if numOuts > 1: return 0
          if numInputs > 1: return 0
    return 1

  def __removeSegment(self, atom3i, handler):
    """
       Removes the (input or output) segment whose handler is 'handler'.
       - Returns:
          None if handler is not a connection.
          returns the 3-element tuple with the information about the connection that has been removed.
    """
    h2remove = handler                                                                          # handler of the connection 2 be removed
    removed = self.removeConnectionFromList(handler)    
    if not removed:                                                                             # connection not found!
      # may be it is the other end what we are trying to delete
      removed = self.removeConnectionFromList(handler, 2)
      if not removed: return
      else: h2remove = removed[0]
    try:
      tags = self.dc.gettags(h2remove)
    except:
      print "WARNING: tag ", h2remove, " not found & not removed by __removeSegment of graphLink.py  (Severity = LOW)"
      return -1
    if len(tags) > 0 :
       del VisualObj.Tag2ObjMap[tags[0]]    							# remove the tag of the connection from the table of mappings
    ic = self.__handlerInList(h2remove, self.in_connections_)
    if ic :
         self.dc.delete(h2remove)
         self.in_connections_.remove(ic)							# remove the tuple
         if ic[2]: ic[2].Destroy()                                                              # Destroy the segment drawing object, if any
         if ic[3]: ic[3].Destroy()                                                              # Destroy the link drawing object, if any
         if self.centerObject:									# if a center object exists, then may be the handler is also there
	       self.centerObject.removeConnection(atom3i, h2remove)
         return removed
    oc = self.__handlerInList(h2remove, self.out_connections_)
    if oc :
         self.dc.delete(h2remove)
         self.out_connections_.remove(oc)							# remove the tuple
         if oc[2]: oc[2].Destroy()                                                              # Destroy the segment drawing object, if any
         if oc[3]: oc[3].Destroy()                                                              # Destroy the link drawing object, if any         
         if self.centerObject:									# if a center object exists, then may be the handler is also there
	    self.centerObject.removeConnection(atom3i, h2remove)
         return removed
    return -1

  def __connect2Entity(self, obj, segmentTuple, intermediatePoints = [], px0 = None, py0 = None, px1 = None, py1 = None, smoothConn = 0, numPoints1stConn = 2):
    """
      Connects the link to an entity.
    """
    segmentHandler  = segmentTuple[0]
    ctuple = self.dc.coords(segmentHandler)						# get initial and final coordinates of the segment
    if len(ctuple) != 4:
      x0, y0, x1, y1 = 0, 0, 0, 0
    else:
      x0, y0, x1, y1 = ctuple
    if intermediatePoints == []:
      connx, conny   = self.getMinDistance_Connectors2Fixed (obj, x0, y0)                     # find to which connector we have to move
    else:
      connx, conny   = self.getMinDistance_Connectors2Fixed (obj, intermediatePoints[0], intermediatePoints[1])           # find to which connector we have to move
    if px0 != None and py0 != None and px1 != None and py1 != None:
      connx, conny = px1, py1
      x1, y1 = px0, py0
    pointList = [connx, conny] + intermediatePoints + [x1, y1]                        		# make list with intermediate points
    #    self.dc.coords(segmentHandler, tuple(pointList))                                       	# move line to desired position
    # HV
    apply(self.dc.coords, tuple([segmentHandler] + pointList))                                       	# move line to desired position
    if smoothConn:        									# smooth connection if necessary
      self.dc.itemconfig(segmentHandler, smooth = 1)
    
    # now see if we have to move the link drawing also...
    if segmentTuple[3]:
      dx, dy = connx-x0, conny-y0								# calculate displacement of the connection
      segmentTuple[3].Move(dx, dy, 0)                                                           # Apply it to the drawing
    # now see if we have to move the segment drawing also...
    if segmentTuple[2]:
      # see if the connection is of a  1stSegment or of a 2nd Segment
      self.drawSegmentIcon(segmentHandler ,segmentTuple[2])
    
    obj.connectActions(segmentTuple, self)                                                       	# add segmentHandler to obj.connections

  def __connect2Link(self, obj, segmentTuple, intermediatePoints = [], px0 = None, py0 = None, px1 = None, py1 = None, smoothConn = 0, numPoints1stConn = 2):
    """
       Connects the link to another link
    """
    segmentHandler  = segmentTuple[0]
    x0, y0, x1, y1 = self.dc.coords(segmentHandler)						# get initial and final coordinates of the segment
    objSegmentTuple = obj.getSegment("IN")
    lx, ly, cx, cy = self.dc.coords(objSegmentTuple[0])                                    # get handler coordinates
    # calculate how many points of the connection should be given to the IN and OUT connections
    numINpoints  = (numPoints1stConn - 2)
    numOUTpoints = len(intermediatePoints)/2 - numINpoints
    # move connectors to the middle
    pmx, pmy = (lx+x0)/2, (ly+y0)/2
    if px1 != None and py1 != None:							# IN connection must begin here if these points are given						
      if len(intermediatePoints) > 0:
         pointList = intermediatePoints[2*numINpoints:] + [px1, py1]
      else:
         pointList = [pmx, pmy, px1, py1]
    else:
      if len(intermediatePoints) > 0:
         pointList = intermediatePoints[2*numINpoints:] + [cx, cy]
      else:
         pointList = [pmx, pmy, cx, cy]
    apply(self.dc.coords, tuple([objSegmentTuple[0]] + pointList))                                   # move line to desired position
    if smoothConn:        									# smooth connection if necessary
       self.dc.itemconfig(objSegmentTuple[0], smooth = 1)
    # also change the coordinates of segmentHandler if appropriate...
    if px0 != None and py0 != None:
       if len(intermediatePoints) > 0:
          invCoords = self.reverseList2by2(intermediatePoints[:2*numINpoints+2])+[px0, py0]
          apply(self.dc.coords, tuple([segmentHandler] + invCoords))
       else:
          apply(self.dc.coords, (segmentHandler, pmx, pmy, px0, py0))
    else:
       if len(intermediatePoints) > 0:
         invCoords = self.reverseList2by2(intermediatePoints[:2*numINpoints+2])+[x1, y1]
         apply(self.dc.coords, tuple([segmentHandler] + invCoords))
       else:
         apply(self.dc.coords, (segmentHandler, pmx, pmy, x1, y1))
    if smoothConn:        									# smooth connection if necessary
       self.dc.itemconfig(segmentHandler, smooth = 1)
    obj.connectActions(objSegmentTuple, segmentHandler, self)
    return objSegmentTuple[0]
  # ________________________________________________________________________________________________________________________________________________
  #						PUBLIC METHODS
  # ________________________________________________________________________________________________________________________________________________

      
  def drawSegmentIcon( self, handler, segmentDrawing ):
    """
       Given the handler of the segment ( from (x0, y0) to (x1, y1)), places the drawing segmentDrawing appropiatelly
    """
    coords = self.dc.coords(handler)
    
    # ---------------- Modified by Denis Dube, summer 2004 -------------------
    # Segment icon should now *always* appear on the arrow, even if it has a 
    # lot of control points or devilish curves :D
    coordLength = len(coords) 
    coordPointNumber = coordLength / 2
    
    # Get middle, 2 point segment, so use those :D
    if( coordPointNumber == 2 ):
      x0, y0, x1, y1 = coords[0], coords[1], coords[2], coords[3]
      
    # Get middle of even numbered segment, use middle two points
    elif( coordPointNumber % 2 == 0 ):    
      indexA = coordPointNumber - 2
      indexB = coordPointNumber
      x0, y0, x1, y1 = coords[indexA], coords[indexA+1], coords[indexB], coords[indexB+1]
      
    # Get middle of odd numbered segment, bias a bit away from the arrow center
    else:    
      indexA = coordPointNumber - 3
      indexB = coordPointNumber - 1
      x0, y0, x1, y1 = coords[indexA], coords[indexA+1], coords[indexB], coords[indexB+1]
    # ---------------------- End of modification ----------------------------
      
    tags = self.dc.gettags(handler)
    tag = tags[0]
    if tag.find(self.tag+"1stSeg")==0 :                                 # find out whether this is a first or a second segment
      segmentObject = self.linkInfo.FirstSegment
    else:
      segmentObject = self.linkInfo.SecondSegment
    obj_bbox = segmentDrawing.getbbox()                                         # gets bounding box of object
    sizex, sizey = obj_bbox[2]-obj_bbox[0], obj_bbox[3]-obj_bbox[1]             # calculates its size
    if segmentObject.decoration_Position.toString() == "Up":			# put in ABOVE the segment line
      absx, absy   = (x1+x0)/2-sizex/2, (y1+y0)/2-sizey-5				# calculates the absoulte point to move to
    elif segmentObject.decoration_Position.toString() == "Down":		# put in BELOW the segment line
      absx, absy   = (x1+x0)/2-sizex/2, (y1+y0)/2+5				# calculates the absoulte point to move to
    elif segmentObject.decoration_Position.toString() == "Middle":		# put in BELOW the segment line
      absx, absy   = (x1+x0)/2-sizex/2, (y1+y0)/2-sizey/2			# calculates the absoulte point to move to
    elif segmentObject.decoration_Position.toString() == "No decoration":	# put in BELOW the segment line
      return
    dx, dy = absx-segmentDrawing.x, absy-segmentDrawing.y			# calculates relative displacement
    segmentDrawing.Move(dx, dy, 0)    
    
  def DrawObject(self, canvas, showGG = 0):
     """
        Draws the link in the canvas 'canvas'
     """
     self.dc = canvas
     for draw in self.drawings:                                                 		# draw each part...
         draw.DrawObject(canvas)								# but not draw the GGLabel, it will be drawn separatelly
         for attr in draw.attr_display.keys():
            self.attr_display[attr] = draw.attr_display[attr]
     
     htuple1 = self.__drawConnection(canvas, self.aFirstLink,
                                     self.aFirstSegment,
                                     self.x1l, self.y1l,
                                     self.linkInfo.FirstLink, self.linkInfo.FirstSegment,
                                     self.in_connections_,
                                     self.tag+"1stSeg"+str(len(self.in_connections_)))		# Draw the 1st segment stored in self.aFirstSegment and self.aFirstLink
     htuple2 = self.__drawConnection(canvas, self.aSecondLink,
                                     self.aSecondSegment,
                                     self.x2l, self.y2l,
                                     self.linkInfo.SecondLink, self.linkInfo.SecondSegment,
                                     self.out_connections_,
                                     self.tag+"2ndSeg"+str(len(self.out_connections_)))		# Draw the 2nd segment stored in self.aSecondSegment and self.aSecondLink
     if showGG:											# check if we should show the graph grammar label
        self.drawGGLabel(canvas)
     if self.centerObject:
        self.centerObject.connections.append((htuple1[0], 1))
        self.centerObject.connections.append((htuple2[0], 0))
        # Added August 14, 2004 by Denis Dube
        self.dc.tag_raise( self.centerObject.tag )
        
     self.connections.append((htuple1[0], 1, None))                                             # add the handlers to connections (because they were not obtained with getSegment)
     self.connections.append((htuple2[0], 0, None))

  def Move(self, delta_x, delta_y, what = ALL_SELECTED, moveCenter=True):
     """
         Move the link:
         - Moves central part if present...
         - Moves links if they are unconnected
     """     
     if what != None: self.selectedHandler = what
     if self.selectedHandler in [self.CENTER_SELECTED, self.NOTHING_SELECTED, self.ALL_SELECTED]:
        if self.centerObject and moveCenter: 
          self.centerObject.Move(delta_x, delta_y, 0)				# move central object.
        self.x, self.y = self.x+delta_x, self.y+delta_y
        self.moveGGLabel( delta_x, delta_y)
        allconn = self.in_connections_+self.out_connections_
        for handlerTuple in allconn:								# go through all the connections
           if handlerTuple in self.unconnected:
              if handlerTuple[3] != None:							# No drawing in the link...
                 handlerTuple[3].Move(delta_x, delta_y)             				# move the drawing
              if handlerTuple[2] != None:							# No drawing in the link...
                 handlerTuple[2].Move(delta_x, delta_y)             				# move the drawing

              self.dc.move(handlerTuple[0], delta_x, delta_y)             			# move the connection
           else:
              points = self.dc.coords(handlerTuple[0])						# move only the center coordinate (the last one in the list)...
              cxf, cyf = points[len(points)-2], points[len(points)-1]                           # get the center coordinates
              points[len(points)-2], points[len(points)-1] = cxf+delta_x, cyf+delta_y		# update them
              apply(self.dc.coords, tuple([handlerTuple[0]] + points))
              if handlerTuple[2] != None:			# No drawing in the link...
                 self.drawSegmentIcon(handlerTuple[0] ,handlerTuple[2])
           # update objects of incoming segments
           for in_obj in self.semanticObject.in_connections_:     # added 24/12/2002 by JL
              in_obj.graphObject_.update_connection_points (handlerTuple[0], delta_x, delta_y, 2, 3)
     if self.selectedHandler == self.CENTER_SELECTED: return
     allconn = self.in_connections_+self.out_connections_
     if self.selectedHandler in [self.NOTHING_SELECTED, self.ALL_SELECTED]:
        # move all the intermediate points...
        for conn in allconn:
          coords = self.dc.coords( conn[0] )
          if len (coords) > 4:                                                                  # if we have more than a couple of points
            idx = 2
            newCoords = coords[0:2]                                                             # copy the first coordinate
            while idx < len(coords)-2:                                                          # iterate through the intermediate coordinates 2 by 2
              newCoords.append(coords[idx]+delta_x)
              newCoords.append(coords[idx+1]+delta_y)
              idx = idx + 2
            newCoords = newCoords+coords[len(coords)-2:len(coords)]                             # add the two last components  
            apply(self.dc.coords, tuple([conn[0]] + newCoords))                                          # Update the coordinates              
     else: # Move only the selected point of the selected connection
        for idx in range(len(self.selectedHandler)): 
           points = self.dc.coords(self.selectedHandler[idx])        
           cx, cy = points[self.selectedPoint], points[self.selectedPoint+1]
           points[self.selectedPoint], points[self.selectedPoint+1] = cx+delta_x, cy+delta_y
           apply(self.dc.coords, tuple([self.selectedHandler[idx]] + points))
           handlerTuple = self.__handlerInList( self.selectedHandler[idx], allconn )
           if handlerTuple and handlerTuple[2] != None:							# No drawing in the link...
              self.drawSegmentIcon(handlerTuple[0] ,handlerTuple[2])
      
        
  def HighLight(self, flag):
      """
         Highlights (flag = 1) or LowLights (flag = 0) all the selected elements
         self.selectedHandler stores a tuple with the handlers of the selected in/out segments, or CENTER_SELECTED or ALL_SELECTED
      """
      
      if not self.selectedHandler or self.selectedHandler == self.NOTHING_SELECTED: self.selectedHandler = self.ALL_SELECTED
      if self.selectedHandler in [self.CENTER_SELECTED, self.ALL_SELECTED]:
         # for each graphical form in graphObject, HighLight it...
         for drawing in self.drawings:
            drawing.HighLight(flag)                       					# 1 = HighLight
      if self.selectedHandler == self.ALL_SELECTED or type(self.selectedHandler) == TupleType:    # a segment selected
         
         # Activate Highlight color
         if flag == 1:                                                                        	# 1 = HighLight
            if self.selectedHandler == self.ALL_SELECTED:						# convert it to a list with all the segment handlers
               theHandlers = []
          
               for htupl in self.in_connections_+self.out_connections_:
                  theHandlers.append(htupl[0])
            else: theHandlers = self.selectedHandler
            
            # Assumption: the link has the same color on all handlers
            # This part of the code will only be executed ONCE
            if( not self.linkColorInitilized and theHandlers ):
              self.linkColor = self.dc.itemcget(theHandlers[0], "fill")
              self.linkColorInitilized = True   
              
            # Apply highlighting
            for index in range(len(theHandlers)):
              try:
                self.dc.itemconfigure( theHandlers[index], fill='green')
              except:
                print '(ERROR) Green highlight failed in', self.tag
         
         # De-Activate Highlighting
         else:
            if self.selectedHandler == self.ALL_SELECTED:						# convert it to a list with all the segment handlers
               theHandlers = []
               for htupl in self.in_connections_+self.out_connections_:
                  theHandlers.append(htupl[0])
            else: theHandlers = self.selectedHandler
          
            # Re-Apply the link color (but only if needed)
            if( self.linkColorInitilized ):
              for index in range(len(theHandlers)): 
                self.dc.itemconfigure( theHandlers[index], fill=self.linkColor )


  def connect(self, obj, intermediatePoints = [], px0 = None, py0 = None, px1 = None, py1 = None, smoothConn = 0, numPoints1stConn = 2):
      """
         Connects this object to 'obj', where obj must be a child of VisualObject. intermediatePoints is a list of intermediate points
         between origin and destination. The function returns the handler of the connection.
         Parameters:
         - obj        : the object to connect to.
         - px0, py0   : If present, point where the first connection (IN) should begin.
         - px1, py1   : If present, point where the first connection should end (if obj is of type graphEntity) or where the OUT connection
           must begin if obj is of type graphLink.
         - smoothConn : Flag that indicates if the connection should be smoothed
         - numPoints1stConn : Number of points of the 1st connection (only useful if obj is of type graphLink). It should be grater or equal than 2.
      """
      # print "in graphLink:: connect, ip = ", intermediatePoints
      segmentTuple   = self.getSegment("OUT")                                                   # Find a free output segment or create a new one
      segmentHandler, segmentTag, segmObj, linkObj = segmentTuple

      destHandler = None									# handler of the other link connection (if the obj is a link)
      pl = self.reverseList2by2(intermediatePoints)						# reverse the list of intermediate points, because we'll draw the line from the entity to the link...

      if obj.isSubclass("graphEntity"):                                                         # if it is a subclass of graphEntity
         self.__connect2Entity(obj, segmentTuple, pl, px0, py0, px1, py1, smoothConn, numPoints1stConn)
      else:                                                                                     # subclass of link...
         destHandler = self.__connect2Link(obj, segmentTuple, intermediatePoints, px0, py0, px1, py1, smoothConn, numPoints1stConn)

      if segmentTuple in self.unconnected:
         self.unconnected.remove(segmentTuple)                                                   # remove segmentTuple from unconnected if appropriate

      # add to connectors of centerObject if this exists
      if self.centerObject:
        if not (segmentHandler, 0) in self.centerObject.connections:
           self.centerObject.connections.append((segmentHandler, 0))		 		# add segmentHandler to obj.connections
           
      coordinates = self.dc.coords(segmentHandler)
      if len(coordinates) > 6:
        #print "in connect:: reversing" 
        aux = self.reverseList2by2(coordinates[2:len(coordinates)-2])        
        coordinates = coordinates[0:2]+aux+coordinates[len(coordinates)-2:]
      self.out_connections_Points[segmentHandler] = (self.tag, obj.tag, coordinates, smoothConn, numPoints1stConn)

      oldConn = self.hasConnectHandler(segmentHandler)
      if oldConn: self.connections.remove(oldConn)                                               # remove from connections (the 3rd component may have changed)
      self.connections.append((segmentHandler, 0, destHandler))                                  # add segmentHandler to obj.connections
      return segmentHandler

  def connectActions (self, htuple, htupleDest = None, objDest = None):
      """
         Actions performed if this object is the destination of a connection.
         Removes the tuple from the list of unconnected segments
      """
      segmentHandler, tag, sObj, lObj = htuple                                                    # Unwrap the tuple
      hcoords = self.dc.coords(segmentHandler)						        # get the new segment coordinates

      if self.centerObject:
        if not (segmentHandler, 1) in self.centerObject.connections:
           self.centerObject.connections.append((segmentHandler, 1))

      if sObj:
         # see if the connection is of a  1stSegment or of a 2nd Segment
         self.drawSegmentIcon(segmentHandler ,sObj)
      oldConn = self.hasConnectHandler(segmentHandler)
      if oldConn: self.connections.remove(oldConn)                                               # remove from connections (the 3rd component may have changed)      
      self.connections.append((segmentHandler, 1, htupleDest))                                   # add segmentHandler to obj.connections
      self.unconnected.remove (htuple)

  def getSegment(self, whichDirection):
      """
         returns an unconnected input or output segment or creates a new one if there's no unconnected.
         - whichDirection is a string with values "IN" or "OUT"
         - The function returns a tuple (handler, tag, segmentObject, linkObject).
      """
      if whichDirection == "IN":           							# set the appropriate list to search in
         list2search = self.in_connections_
         link        = self.aFirstLink
         linkName    = self.firstLinkName
         segment     = self.aFirstSegment
         segmentName = self.firstSegmentName
      else:
         list2search = self.out_connections_
         link        = self.aSecondLink
         linkName    = self.secondLinkName
         segment     = self.aSecondSegment
         segmentName = self.secondSegmentName

      segmentTuple = None
      segmentHandler, segmentTag, segmObj, linkObj  = None, None, None, None
      for segm in self.unconnected:
         segmentHandler, segmentTag, segmObj, linkObj  = segm					# unwrap the tuple
         if self.__handlerInList(segmentHandler, list2search): 					# it's the one we are looking for !
            segmentTuple  = segm                                    				# store the found tuple in segmentTuple
            break

      if segmentTuple == None:									# produce a new segment if no one has been found
         # see if we have drawings for links or segments
         linkObj, segmObj = None, None
         if link   :
            link    = self.getDrawing(linkName, self.x-10, self.y-10)
            link.removeFromList()                         					# remove from the global list of entities, 'cause we are a link
            link.changeTag(self.tag)          	                          			# Change whichever tag it has to current graphLink tag
            if whichDirection == "IN": self.x1l, self.y1l = link.x, link.y			# Storage for the 1st link coordinates
            else: self.x2l, self.y2l = link.x, link.y						# Storage for the 2nd link coordinates
            linkObj = link

         if segment :
            segment = self.getDrawing(segmentName, self.x-5, self.y-5)
            segment.removeFromList()               		          			# remove from the global list of entities, 'cause we are a link
            segment.changeTag(self.tag)                         	           		# Change whichever tag it has to current graphLink tag
            if whichDirection == "IN": self.x1s, self.y1s = segment.x, segment.y		# Storage for the 1st segment coordinates
            else: self.x1s, self.y1s = segment.x, segment.y					# Storage for the 2nd segment coordinates
            segmObj = segment

         if whichDirection == "IN":
            tag = self.tag+"1stSeg"+str(len(self.in_connections_))                              # Produce a new tag for the segment
            segmentHandler, segmentTag = self.__drawConnection(self.dc, linkObj, segmObj, self.x1l, self.y1l,
                                                         self.linkInfo.FirstLink, self.linkInfo.FirstSegment, list2search, tag)
            self.connections.append((segmentHandler, 0, None))
         else:
            tag = self.tag+"2ndSeg"+str(len(self.out_connections_))                              # Produce a new tag for the segment
            segmentHandler, segmentTag = self.__drawConnection(self.dc, linkObj, segmObj, self.x2l, self.y2l,
                                                         self.linkInfo.SecondLink, self.linkInfo.SecondSegment, list2search, tag)
            self.connections.append((segmentHandler, 1, None))
         VisualObj.Tag2ObjMap[tag] = self                                   			# puts object in dictionary

      return (segmentHandler, segmentTag, segmObj, linkObj)

  def removeConnection(self, atom3i, handler):
      """
         Removes the (input or output) connection whose handler is 'handler'. If this is a 1:1 connection, then removes the whole
         connection (and not just the incoming or outgoing segment).
         - Returns:
            -1 if handler is not a connection.
            0  if handler corresponds to an output segment
            1  if handler corresponds to an input  segment
            2  if the whole connection has been removed
      """            
      if self.hasConnectHandler(handler):
         if self.__have2removeAll(atom3i):
            self.erase(atom3i)         
            return 2
         else:
            removedTuple1 = self.__removeSegment(atom3i, handler)
            # see if we have two ends to remove (a graphLink connected to itself...)
            if removedTuple1:
               if removedTuple1[2] != None: 
                 removedTuple2 = self.__removeSegment(atom3i, removedTuple1[2])
                 return removedTuple1[0]
            return -1
      return -1
      
                 
  def select (self, tag, handler, x, y):
      """
          Selects the point of the link (if it is a multi-point link) or center part corresponding to tag
      """
      VisualObj.select(self, tag, handler, x, y)               					# call super's action
      if tag == self.tag:					                                # it is the center object or one of the drawings that is being selected...
           self.selectedHandler = self.CENTER_SELECTED						# WE SHOULD LOOK IF IT IS REALLY THE CENTER
      elif string.find(tag, self.tag+"1stSeg")==0 or string.find(tag, self.tag+"2ndSeg") == 0:	# it is one of the incoming segments...
           htuple = self.hasConnectHandler(handler)                                             # get the tuple with the info connection
           coords = self.dc.coords ( handler )							# see how many points do we have
           if len (coords) == 4 and htuple[2] == None:  					# only two points, so we cannot move it...
              self.selectedHandler = self.CENTER_SELECTED					# ... so select the center
           elif htuple[2] != None:             
              self.selectedPoint   = self.__get_MinDistance_Point2List (x, y, coords[:len(coords)-2])
              if self.selectedPoint == 0: self.selectedHandler = (handler, htuple[2])           # store the two handlers to be moved...
              else: self.selectedHandler = (handler, )
           else:										# select the nearest point!
              self.selectedHandler = (handler, )                                               # only one handler has to be moved...
              self.selectedPoint   = self.__get_MinDistance_Point2List (x, y, coords[2:len(coords)-2])+2

  def getDrawing(self, name, cx, cy):
     """
         Given the class name ('name') and the coordinates (cx, cy), tries to create an object of that class,
         this may not exist, but if it does, it is a subclass of graphEntity.
     """
     try:									# it is possible that it does not exist
        exec "from "+name+" import *\n"
     except IOError:								# File does not exist
        return None
        print "Could not open graphical file"
     except ImportError:	                                                # File does not exist
        return None						
        print "Could not open graphical file"
     else: return eval(name)(cx, cy, self.semanticObject)
  
  def smooth (self, handler):
      """
         Abstract method (to be filled by graphLinks) to smooth a connection segment
      """
      if self.__handlerInList( handler, self.in_connections_+self.out_connections_):  # check that it is really a connection segment
         currentSmooth = self.dc.itemcget( handler, "smooth")                         # get current smooth status
         if currentSmooth == "0": nextStatus = "1"
         else: nextStatus = "0"
         self.dc.itemconfig( handler, smooth = nextStatus)                    # invert this status

  def deletePointFromConnection (self, tag, handler, x, y):
      """
          Selects the point of the link (if it is a multi-point link) nearest to x, y and deletes it
      """
      #print handler, tag
      if tag == self.tag:					                                # it is the center object or one of the drawings that is being selected...
           return
      elif string.find(tag, self.tag+"1stSeg")==0 or string.find(tag, self.tag+"2ndSeg") == 0:	# it is one of the incoming segments...
           coords = self.dc.coords ( handler )							# see how many points do we have
           if len (coords) == 4:								# only two points, so we cannot delete them...
              return
           else:										# select the nearest point!
              point2delete = self.__get_MinDistance_Point2List (x, y, coords[2:len(coords)-2])+2
              del coords[point2delete]
              del coords[point2delete]
#              self.dc.coords(handler, tuple(coords))
# HV
              apply(self.dc.coords, tuple([handler] +coords))

  def insertIntermediatePoint(self, tag, handler, x, y):
      """
          Inserts the point x,y in the connection given by handler 
      """
      if tag == self.tag:					                                # it is the center object or one of the drawings that is being selected...
           return
      elif string.find(tag, self.tag+"1stSeg")==0 or string.find(tag, self.tag+"2ndSeg") == 0:	# it is one of the incoming segments...
           coords = self.dc.coords ( handler )							# see how many points do we have
           if len (coords) == 4:								# only two points, so we cannot delete them...            
              coords.insert(2, x)
              coords.insert(3, y)                                                               # insert the point
           else:										# select the nearest segment!
              counter = 0
              mindistance = 10000
              minindex = 0
              while counter < len(coords)-2:
                  x0, y0, x1, y1 = coords[counter:counter+4]
                  distance = self.__distance_Point2Rect( x, y, x0, y0, x1, y1 )
                  if distance < mindistance:
                      mindistance = distance
                      minindex = counter
                  counter = counter + 2
              coords.insert(minindex+2, x)
              coords.insert(minindex+3, y)
           if handler in self.out_connections_Points.keys():
              myTag, objTag, oldcoords, smooth, numP = self.out_connections_Points[handler]
              self.out_connections_Points[handler] = (myTag, objTag, coords, smooth, numP)
#           self.dc.coords ( handler, tuple(coords))
# HV
           apply(self.dc.coords, tuple([handler] + coords))

  def changeConnector (self, hconnection, hnewConnector):
      """
          Changes a connection (the given by the handler hconnection) to a new connector (the given by handler hnewConnector)
          Returns 1 if the connector is in other object, 0 otherwise.
      """
      coords    = self.dc.coords(hconnection)
      newCoords = self.dc.coords(hnewConnector)
      fromOtherObject = 1									# see if the new handler is from a center connector or is of another object
      if self.centerObject and hnewConnector in self.centerObject.connectors: fromOtherObject = 0
      if fromOtherObject == 1:                                                    		# change the appropriate coordinate depending on where the new connector is
         dx, dy = newCoords[0]-coords[0], newCoords[1]-coords[1]
         coords[0], coords[1] = newCoords[0], newCoords[1]
      else:
         dx, dy = newCoords[0]-coords[len(coords)-2], newCoords[1]-coords[len(coords)-1]
         coords[len(coords)-2], coords[len(coords)-1] = newCoords[0], newCoords[1]
#      self.dc.coords(hconnection, tuple(coords))
# HV
      apply(self.dc.coords, tuple([hconnection] + coords))
      # see if we have to move the associated link drawing
      inTuple = self.__tupleInList (hconnection, self.in_connections_)
      if inTuple:
         if inTuple[3]:
            inTuple[3].Move(dx, dy, 0)
      outTuple = self.__tupleInList (hconnection, self.out_connections_)
      if outTuple:
         if outTuple[3]:
            outTuple[3].Move(dx, dy, 0)

      return fromOtherObject      


  def erase (self, atom3i, deleteConnections = 1, entityOnly=False):
      """
         It is used to delete the graphical Object. atom3i is an instance of ATOM3.
      """
      #todo: qocaCleanup   
      self.qocaCleanup(atom3i)
      
      if deleteConnections:
         conn2delete = self.in_connections_+self.out_connections_				# get all the connections that we have to delete
         while len(conn2delete) > 0:
            self.__removeSegment(atom3i, conn2delete[0][0])
            # delete the connection from the lists of other connected objects...
            objs = self.EntityList + self.LinkList						# get all the objects
            for obj in objs:								# remove the link from all the objects (if they have it)
               if obj != self:
                 obj.removeConnection(atom3i, conn2delete[0][0])
            conn2delete.remove(conn2delete[0])
      if self.centerObject:
         self.centerObject.erase(atom3i, deleteConnections)
      self.Destroy()
      

  def getConnectionCoordinates( self, direction, obj, number = 1):
      """
         Specializes the method defined in VisualObj for the case of two graphLinks.
      """
      if issubclass(obj.__class__, graphLink):
         if direction == "IN":
           connDirection = 1                                                      # connection direction
           otherObjDir   = 0
         else:
           connDirection  = 0
           otherObjDir   = 1

         numFound = 0                                                                # num of connections found -> 0
         for htuple in self.connections:
            if htuple[2] != None:
               tcon = obj.hasConnectHandler(htuple[2])
               if tcon and tcon[1] == otherObjDir:
                  numFound = numFound + 1
                  if numFound == number:                                             # see if the connection order is the appropriate
                    if not self.isDestroyed:                                         # if graphic is visible... (MODIFIED 20 Sept 2002) 
                       coords1st = self.dc.coords(htuple[0])                     
                       coords2nd = self.dc.coords(htuple[2])
                       coords2nd = self.reverseList2by2(coords2nd)
                       ssmooth = self.dc.itemcget(htuple[0], "smooth")
                       if ssmooth: smooth = 1
                       else: smooth = 0
                       return (coords2nd+coords1st[2:], len(coords1st)/2, smooth)
                    else:
                       if self.out_connections_Points.has_key(htuple[0]):
			   myTag, hisTag, coords, smooth, lencoords = self.out_connections_Points[htuple[0]]			   
			   return ( coords, lencoords, smooth )                       
         return None

      else:
         return VisualObj.getConnectionCoordinates(self, direction, obj, number)

  def getConnectionHandler( self, direction, obj, number = 1):
      """
         Specializes the method defined in VisualObj for the case of two graphLinks
      """
      if issubclass(obj.__class__, graphLink):      
         if direction == "IN":
              connDirection = 1                                                      # connection direction
              otherObjDir   = 0
         else:
              connDirection  = 0
              otherObjDir   = 1

         numFound = 0                                                                # num of connections found -> 0
         for htuple in self.connections:
           if htuple[2] != None:
              tcon = obj.hasConnectHandler(htuple[2])
              if tcon and tcon[1] == otherObjDir:
                numFound = numFound + 1
                if numFound == number:                                                # see if the connection order is the appropriate
                   return htuple[0]
         return None

      else:
         return VisualObj.getConnectionHandler(self, direction, obj, number)

  def deleteGraphicalConnectionsList(self):
      """
         Deletes the graphical connections
      """
      while len(self.in_connections_) > 0: self.in_connections_.pop()
      while len(self.out_connections_) > 0: self.out_connections_.pop()			# remove in place handles of outgoing segments (2nd segments)
      while len(self.unconnected) > 0: self.unconnected.pop()				# unconnected segments (in OR out)
      while len(self.connections) > 0: self.connections.pop()
      self.destroy()        # Added 24/12/2003 by JL
      self.isDestroyed = 0  # Added 24/12/2003 by JL

  def redrawObject(self, canvas, showGG = 0):
      """
      	 The canvas in which this object was drawn before was closed, and now it is requested to this object to draw itself again...
      """
      self.dc = canvas
      while len(self.in_connections_) > 0: self.in_connections_.pop()
      while len(self.out_connections_) > 0: self.out_connections_.pop()			# remove in place handles of outgoing segments (2nd segments)
      while len(self.unconnected) > 0: self.unconnected.pop()				# unconnected segments (in OR out)
      while len(self.connections) > 0: self.connections.pop()      
      self.attr_display = {}
      if showGG: self.drawGGLabel (canvas)                                              # corrected 20-July-2002
      for icon in self.drawings:
         icon.redrawObject(canvas )
         for attr in icon.attr_display.keys():
            self.attr_display[attr] = icon.attr_display[attr]


  def postCondition (self, actionID, * params):
      for draw in self.drawings:
        ret = draw.postCondition (actionID, params)
        if ret: return ret
      return None

  def preCondition (self, actionID, * params):
      for draw in self.drawings:
        ret = draw.preCondition (actionID, params)
        if ret: return ret
      return None

  def write2File(self, file, indent):
      """
         Writes its properties into a file .
      """
      for draw in self.drawings:                 # draw each object into a file
        draw.write2File(file, indent)
      
  def getNamedPort(self, handler_connection ):
      """
         Returns the name of the named connector which is connected to the connection whose handler is
         'handler_connection'. None if it can not be found.
      """
      return None
    
  def hasNamedPortInConnector (self, handler):
      """
         Looks to see if in the connector 'handler' there is a named Port. If it does, return the name
         Created 24 July 2002 by JL         
      """
      return None

  def getConnectedObjectByHandler (self, handler):
      """
         Returns the object connected to self by the connection handler, if any.
         Created 24 July 2002 by JL                  
      """
      for conn_tuple in self.connections:
          hndler, dir, other_obj = conn_tuple
          # print "in graphLink::getConnectedObjectByHandler::conn_tuple = ", conn_tuple, " handler = ", handler
          if handler == hndler:         # This connection exists... Look for all the possible objects...
             if dir == 0:               # source
                list2look = self.semanticObject.out_connections_
             else:                      # destination
                list2look = self.semanticObject.in_connections_
             # print "list2look = ", list2look             
             for sem_obj in list2look:                
                if sem_obj.graphObject_.hasConnectHandler(handler): return sem_obj.graphObject_     # We've found it! (changed 6 Aug 2002 by JL)
                if sem_obj.graphObject_.hasConnectHandler(handler, 2): return sem_obj.graphObject_     # We've found it! (changed 6 Aug 2002 by JL)
      return None

  def getSize(self):
      """
         Method that returns the (SizeX, SizeY) tuple with the center object's dimensions. If we do not have
         a center object, it returns (0, 0)
         Added 05 Nov 2002 by Juan de Lara
      """
      if self.centerObject: return (self.centerObject.sizeX, self.centerObject.sizeY)
      else: return (0, 0)
      
  #---------------------------------------------------------------------------
  # Added by Denis Dube over the summer of 2004
      
  def hasConnectors(self):
      """ Clearly, an edge has no connector """
      return False
  
  def hasCenterObjectConnector( self ):
      """ The edge may have a CenterObject with a connector though """
      if( self.centerObject ):
          return self.centerObject.hasConnectors()
      return False
  
  def getSemanticObject(self):
    return self.semanticObject
  
  def getCenterCoord(self):
    return [self.x,self.y]
      
  def setCenterSelect(self):
    self.selectedHandler = self.CENTER_SELECTED
    
  def setSelectAll(self):
    self.selectedHandler = self.ALL_SELECTED
    
  def getCenterObject(self):
    if( self.centerObject ):
        return self.centerObject
    else:
        return None
      
  def updateDrawingsTo( self, x, y, segmentHandle, segmentNumber=1 ):
    """ 
    Moves link & segment drawings to the given location 
    segmentHandle = the item handler for the 1stSeg or 2ndSeg part of the arrow
    """
    
    # First link & segment
    if( segmentNumber == 1 ):
      
      # Move the link drawing if it exists
      if( self.has1stLink ):
        self.aFirstLink.moveTo( x,y )
        
      # Move the 1st segment drawing if it exists
      if( self.has1stSegment ):
        self.drawSegmentIcon( segmentHandle, self.aFirstSegment )
      
    # Second link & segment
    else:
      
      # Move the link drawing if it exists
      if( self.has2ndLink ):
        self.aSecondLink.moveTo( x,y )
          
      # Move the 1st segment drawing if it exists
      if( self.has2ndSegment ):
        self.drawSegmentIcon( segmentHandle, self.aSecondSegment )
          
  def getAnyItemHandler( self ):
    """ Returns the first item handler belonging to this visual entity """
    connList = self.in_connections_ + self.out_connections_ +  self.unconnected
    for tupleList in connList:
      #for tuple in tupleList:
      return tupleList[0]
    return None
  
  def raiseItem( self ):
    """ Raises this link above anything else """
    tupleList = self.in_connections_ + self.out_connections_ 
    canvas = self.dc
    if( canvas ):
      for htuple in tupleList:
          canvas.tag_raise( htuple[0] )
    if( self.centerObject ):
      self.centerObject.raiseItem()
    if( self.has1stLink ):
      self.aFirstLink.raiseItem()
    if( self.has2ndLink ):
      self.aSecondLink.raiseItem()
    if( self.has1stSegment ):
      self.aFirstSegment.raiseItem()
    if( self.has2ndSegment ):
      self.aSecondSegment.raiseItem()
        
  def setVisibility(self, isVisible):
    """
    Sets the visibility of this edge and all its dependents
    Parameter:
      isVisible, boolean True or False with obvious meaning
    """
    if(isVisible):
      stateString = 'normal' 
    else:
      stateString = 'hidden'
    tupleList = self.in_connections_ + self.out_connections_ 
    canvas = self.dc
    if( canvas ):
      for htuple in tupleList:
        canvas.itemconfigure(htuple[0], state=stateString)
    if( self.centerObject ):
      self.centerObject.setVisibility(isVisible)
    if( self.has1stLink ):
      self.aFirstLink.setVisibility(isVisible)
    if( self.has2ndLink ):
      self.aSecondLink.setVisibility(isVisible)
    if( self.has1stSegment ):
      self.aFirstSegment.setVisibility(isVisible)
    if( self.has2ndSegment ):
      self.aSecondSegment.setVisibility(isVisible)
        
 
  def getArrowEndpoint(self, direction):
    """ 
    Returns the coordinates of the end point of the arrow [Xn,Yn]
    On failure, returns [0, 0]
    """
    if(direction is None): 
      if(len(self.out_connections_) == 0):
        return None
      tuple = self.out_connections_[-1]
    else: 
      if(len(self.in_connections_) == 0):
        return None
      tuple = self.in_connections_[-1]
    if( not tuple ): return None
    handler = tuple[0]
    coordList = self.dc.coords( handler )
    ##if( len( coordList ) < 4 ): raise "hell"
    # NOTE: 2nd segement coords are in reverse order
    return coordList[:2]
    ##return [ coordList[:2], coordList[2:4] ]  

  
  def getArrowEndangle(self, direction):
    """ Returns the angle in degrees of the last segment of the arrow """
    if(direction is None): tuple = self.out_connections_[-1]
    else: tuple = self.in_connections_[-1]
    if( not tuple ): return None
    handler = tuple[0]
    coordList = self.dc.coords( handler )
    x1,y1,x0,y0 = coordList[:4] # BEWARE: 2nd seg coords in reverse order

    angle = math.atan2( float(y0 - y1) , float(x1 - x0) )
    if( angle < 0 ): angle += math.pi + math.pi
    return angle ##/ math.pi * 180
  
  
  def rotate2D( self, angle, rotationBase, x, y, direction ):
      """ Rotates a point (x,y) around rotationBase (x0,y0) with given angle """
        
      # From the previous angle, figure out how much rotation needed
      if(direction is None):
        cAngle = self.lastAngle[0] - angle 
        self.lastAngle[0] = angle     
      else:
        cAngle = self.lastAngle[1] - angle 
        self.lastAngle[1] = angle 
               
      cAngle = cmath.exp(cAngle*1j) # angle in radians
        
      # Point around which rotation occurs
      rotationBase = complex( *rotationBase )

      # Apply rotation directly to the canvas coordinates          
      v = cAngle * (complex(x, y) - rotationBase) + rotationBase     
      return (v.real, v.imag)
  
  
  def rotateMoveArrowEnd( self, direction=None ):
      """ 
      For polygon and line drawings, moves and rotates them with arrow end 
      If the direction parameter is not supplied, the 'end' of the arrow is used
      Otherwise, the 'start' of the arrrow is used
      """
          
      # Does the end of the arrow have a art deco?
      if(direction is None and self.has2ndLink): 
        obj = self.aSecondLink
      elif(self.has1stLink): 
        obj = self.aFirstLink
      else:         
        return # Something screwed up, bail out
           
      ##x,y = self.getArrowEndpoint(direction)
      ##obj.dc.create_oval( x-2,y-2,x+2,y+2, fill='red' )
      
      # Where does the arrow end or connect with something else
      res = self.getArrowEndpoint(direction)
      if(res == None):
        return None # Something screwed up, bail out
      ax,ay = res
      
      # Do the rotation around the arrows end point
      angle = self.getArrowEndangle(direction)
            
      for gf in obj.graphForms:
        if( gf.elementType == 'polygon' ):
          gf.rotate2D( angle, (ax, ay) )
                  
      def dist(  x0, y0, x1, y1 ):
        """ Distance between two points """
        return math.sqrt(abs((x0-x1)*(x0-x1)+(y0-y1)*(y0-y1)))
                     
        
      # Which point in the arrow endpoint decoration is closest to the endpoint?
      # METHOD 1: Use a connector to choose the point
      if( obj.connectors ):
        handler = obj.connectors[0]
        coordList = self.dc.coords( handler )
        minX, minY = coordList[:2]
        minX, minY = self.rotate2D( angle, (ax, ay), minX, minY, direction )[:2]
        self.dc.coords( handler, minX, minY, minX, minY )
        
        
        
      # METHOD 2: Use some rather random distance choosing method
      else:                
        minDist = 100000
        minX = 0
        minY = 0
        for gf in obj.graphForms:
          if( gf.elementType == 'polygon' ):
            xy = gf.getXY()      
            for x,y in xy:
              distance = dist( ax, ay, x, y )
              if( distance < minDist ):
                minX = x
                minY = y
                minDist = distance
              
      # Move the decoration so it touches the arrows end point
      dx, dy = [ ax-minX, ay-minY ]
      obj.Move( dx, dy, moveConn=False )
            
      # Make sure we can see the damn thing!
      obj.raiseItem()
      
  def moveTo(self, x=None, y=None, what=None, moveCenter=True):
    """ Convenience method: Moves this entity to the new location """      
    #todo: expand this so decorations 1,2,3,4,5 can be independently targeted?
    #todo: expand this so start/end points can be targeted?
    if(x is not None):
      dx = x - self.x
    else:
      dx = 0
    if(y is not None):
      dy = y - self.y   
    else:
      dy = 0
    ## print 'moveTo', self.tag, x, y
    if(not what):
      what = self.CENTER_SELECTED
    self.Move(dx, dy, what, moveCenter)
    
    
  def getbbox(self):
    """ 
    Returns the bounding box of the center object if it exists: [x0, y0, x1, y1]
            if no center object: [0, 0, 0, 0]
    """
    if(self.centerObject):
      return self.centerObject.getbbox()
    return [0, 0, 0, 0]
      
  #---------------------------------------------------------------------------
  
  
      
