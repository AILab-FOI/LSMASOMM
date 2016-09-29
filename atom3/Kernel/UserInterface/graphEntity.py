# __ File: graphEntity.py __________________________________________________________________________________________________
#  Implements  : class graphEntity, child of VisualObj
#  Author      : Juan de Lara
#  Description : This is the base class for all graphical graphEntity Objects
#  Modified    : 24 July 2002
#     - 24 July 2002, by JL: Added methods getNamedPort, hasNamedPortInConnector and hasNamedPortInConnector for
#       Named Ports handling
# ____________________________________________________________________________________________________________________

import string, Dialog, sys
from time import sleep

from VisualObj import *

        

class graphEntity(VisualObj):
    """
      Attributes (these should be private):
         - self.center                : tuple with the center of the object.
         - self.connectors            : list of connectors elements.
         - self.delta_x, self.delta_y : last increment applied in Scaling.
         - self.graphForms            : list of graphical forms.
         - self.namedConnectors       : Dictionary for named connectors. It is indexed by habdler, and the value is a
                                        string with the connector name.
      __________________________________________________________________________________________________________________________________________________
      Private methods:
        - __moveConnection(self, conHandle, coordList, dx, dy, which):
               method to displace a connection. coordList is a list with the coordinates of conHandle. (dx, dy) is
               the displacement to apply.
      __________________________________________________________________________________________________________________________________________________
      Public  methods:
         - Move(self, delta_x, delta_y):
               Modifies object position by delta_x, delta_y
         - isFree (self, x0, y0, x1, y1 ):
               decides if this object has a connector whose average coordinates are either (x0, y0) or (x1, y1)
         - getCoordsVertex(self):
               returns the coordinate of the upper-left connector
         - getCoords(self, handle):
               returns the coordinates of a given handler
         - Scale(self, x_inc, y_inc):
               Scales the object in a factor of x_inc in x and y_inc in y
         - hasGraphicalConnection(self, node):
               checks if there are a connection between this object and node.
               Check this method. It WILL NOT WORK WITH THE NEW VERSION OF ATOM3
         - deleteGraphicalConnection(self, handler):
               Deletes connection with handler 'handler' from actual node and from the other node end.
               Should check this, it will not work in the new version of ATOM3
         - HighLight(self, flag):
               Highlights (flag = 1) or LowLights (flag = 0) all the VISIBLE elements with the 'selected' tag
         - connect(self, obj, intermediatePoints = []):
               Connects this object with another object of type 'graphLink'. The connection may have intermediate points, stored in the list
               intermediatePoints.               
         - connectActions (self, htuple):
               Actions performed if this object is the destination of a connection.
               Adds the handler (1st component of htuple) to the list of connections
         - hasConnectHandler(self, ch):
               checks if the object has a connection with handler 'ch'. Returns a tuple ( handler, <order>) where order is 0 o 1 depending if
               it is the origing or destination
         - removeConnection(self, atom3i, handler):
               Removes the (input or output) connection whose handler is 'handler'.
               - Returns:
                  -1 if handler is not a connection.
                  0  if handler corresponds to an output segment
                  1  if handler corresponds to an input  segment
         - def erase (self, atom3i):
               Deletes the graphical Object.
        
    """

    def __init__(self, x, y, stayEditListTuple=None):
        """
           Initializes object
        """
        VisualObj.__init__(self)
        self.x, self.y = x, y
        self.center = (-1, -1)
        self.connectors = []				# set of connector handlers
        self.delta_x = 0
        self.delta_y = 0
        self.graphForms = []                            # List with the graphical forms
                
        # Size is usually set by subclasses of graphEntity before this init 
        # method is called. Older code does not do this. 
        # The size will thus be hard-coded... yielding poor results possibly
        if(not self.__dict__.has_key('sizeX')):
          self.sizeX = 100
        if(not self.__dict__.has_key('sizeY')):
          self.sizeY = 100
                
        # Force existence of scale layout constraint, added by Denis Dube, summer 2004
        if( not self.layConstraints.has_key( 'scale' ) ):
            self.layConstraints['scale'] = [1.00,1.00]
            
        #todo: auto creation of qoca vars
        from Qoca.constraints.QocaSolverAbstract import getSolver
        solver = getSolver()
        if(solver == None): 
          return
        ID = str(self.ID)
        if(stayEditListTuple): # stayEditListTuple = (stayWeightList, editWeightList)
          sx, sy, sw, sh = stayEditListTuple[0]
          ex, ey, ew, eh = stayEditListTuple[1]
        else:
          # Denis: These defaults seem fairly good. Making entities with different
          #        weight values doesn't seem to do anything worthwhile though :(
          sx, sy, sw, sh = (8, 8, 512, 512)
          ex, ey, ew, eh = (1024, 1024, 1024, 1024)
          
        self.qcX = solver.makeVar('x'+ID, self.x, sx, ex, 
                              callback=lambda x, self=self: self.moveTo(x=x))
        self.qcY = solver.makeVar('y'+ID, self.y, sy, ey, 
                                callback=lambda y, self=self: self.moveTo(y=y))
        self.qcW = solver.makeVar('w'+ID, self.sizeX, sw, ew, 
                                callback=lambda w, self=self: self.scaleX(w))
        self.qcH = solver.makeVar('h'+ID, self.sizeY, sh, eh, 
                                callback=lambda h, self=self: self.scaleY(h))
        map(self.qocaVariables.append, [self.qcX, self.qcY, self.qcW, self.qcH])
        

    # ________________________________________________________________________________________________________________
    #                                       PRIVATE METHODS
    # ________________________________________________________________________________________________________________

# SB: added the following 2 private methods mainly for 
# the Scale operation so that links are properly pointed at their
# respective connectors
# Denis Dube: discovered that these two methods don't work reliably 
# for scaling, and thus are not being used.
    def __associate_links_with_connectors(g):
        canvas = g.dc
        associated = []
        from graphLink import graphLink
        for l in g.connections:
            con, order, sobj, lobj, obj = l
            if isinstance(obj, graphLink):
                for out_con in obj.out_connections_:
                    out_con_handle = out_con[0]
                    out_coords = canvas.coords(out_con_handle)
                    for connector_handle in g.connectors:
                        connector_coords = canvas.coords(connector_handle)
                        if connector_coords[0] == out_coords[0] and connector_coords[1] == out_coords[1]:
                            associated.append((out_con_handle, connector_handle))
                for in_con in obj.in_connections_:
                    in_con_handle = in_con[0]
                    in_coords = canvas.coords(in_con_handle)
                    for connector_handle in g.connectors:
                        connector_coords = canvas.coords(connector_handle)
                        if connector_coords[0] == in_coords[0] and connector_coords[1] == in_coords[1]:
                            associated.append((in_con_handle, connector_handle))
        return associated

    def __move_links_to_connectors(g, to_move):
        canvas = g.dc
        for con in to_move:
            connection_handle, connector_handle = con
            connector_coords = canvas.coords(connector_handle)
            connection_coords = canvas.coords(connection_handle)
            apply(canvas.coords, (connection_handle, connector_coords[0], connector_coords[1], connection_coords[2], connection_coords[3]))

    def __moveConnection(self, conHandle, dx, dy, sobj, lobj, graphLinkObj):
        """
           method to displace (dx, dy) units a connection, whose handler is conHandle. 
           The link may also have a drawing (lobj) and the segment may also have a link 
           (sobj)
        """

        coordList = self.dc.coords(conHandle)
        try:
          cx, cy = coordList[0], coordList[1]      					# obtain coordinates to move. 
        except:
          print '\nBad coordinates in graphEntity.py in __moveConnection()'
          print conHandle
          print coordList
          print self.connections
          return
                    #We always select the two firsts, as connection are drawn from entities to links
        coordList[0], coordList[1] = cx+dx, cy+dy					# move coordinates
#        self.dc.coords(conHandle, tuple(coordList))
# HV replaced by following for backward compatibility
        apply(self.dc.coords, tuple([conHandle] + coordList))

        if lobj != None:								# if we have a link object, then move it also...
           lobj.Move(dx, dy, 0)
        if sobj != None:
            graphLinkObj.drawSegmentIcon( conHandle, sobj )

        if conHandle in self.out_connections_Points.keys(): # Modified 23/12/2002 by JL
            coordinates = self.out_connections_Points[conHandle][2]
            coordinates[0] = coordinates[0] + dx
            coordinates[1] = coordinates[1] + dy

        # tell graphLinkObj to update its handler... this is an update of outgoing connections.

        # Added 23/12/2002 by JL
        graphLinkObj.update_connection_points ( conHandle, dx, dy, 0, 1 ) 
        
    # ________________________________________________________________________________________________________________
    #                                       PUBLIC METHODS
    # ________________________________________________________________________________________________________________

    def Move(self, delta_x, delta_y, moveConn = 1):
        """
           Modifies object position by delta_x, delta_y
        """
        for gf in self.graphForms:				        # move each graphical form...
           self.dc.move(gf.handler, delta_x, delta_y)
        for con in self.connectors:					# move each connector
           self.dc.move(con,  delta_x, delta_y)
        self.moveGGLabel( delta_x, delta_y)
        self.x = self.x + delta_x
        self.y = self.y + delta_y
        if -1 not in self.center:
            self.center = (self.center[0] + delta_x, self.center[1] + delta_y)

        # now move connections
        if moveConn:
            for con_order in self.connections:		
                con, order, sobj, lobj, obj = con_order
                self.__moveConnection(con, delta_x, delta_y, sobj, lobj, obj)
        
    
    def MoveConnections(self, delta_x, delta_y):
        for con_order in self.connections:
            con, order, sobj, lobj, obj = con_order
            self.__moveConnection(con, delta_x, delta_y, sobj, lobj, obj)
 		
    def isFree (self, x0, y0, x1, y1 ):
        """
           decides if this object has a connector whose average coordinates are either (x0, y0) or (x1, y1)
        """
        for conn in self.connections:
            cl = self.dc.coords(conn[0])
            limit = len(cl)/2
            for i in range(limit):
              x, y = cl[i*2:i*2+2]
              if ((x, y) == (x0, y0)) or ((x, y) == (x1, y1)):
                 return 0
        return 1

    def getCoordsVertex(self):
        """
           returns the coordinate of the upper-left connector
        """
        xmin, ymin = 10000, 10000
        for h in self.connectors:
           x0, y0, x1, y1 = self.dc.coords(h)
           x, y = (x0+x1)/2, (y0+y1)/2
           if x<xmin: xmin = x
           if y<ymin: ymin = y
        return (xmin, ymin)

    def getCoords(self, handle):
        """
           returns the coordinates of a given handler
        """
        return self.dc.coords(handle)

    def ScaleOld(self, x_inc, y_inc):
        """
           Scales the object in a factor of x_inc in x and y_inc in y
        """
        box = self.dc.bbox(self.tag)
        x_factor = 1 + float(x_inc) / (box[2] - box[0])
        y_factor = 1 + float(y_inc) / (box[3] - box[1])
        #extra = self.dc.create_text(self.GetInputLinkCoord(), text = "Processing...", fill = "blue", tags = self.tag)
        self.dc.scale(self.tag, 0, 0, x_inc, y_inc)
        #self.center = tuple(self.dc.coords(extra))
        #self.dc.delete(extra)
        self.delta_x = self.delta_x + x_inc
        self.delta_y = self.delta_y + y_inc

    def Scale(self, xscale, yscale, moveLinks = True ):
        """
           Scales the object in a factor of x_inc in x and y_inc in y
        """
        # don't allow scaling by a factor of 0
        if xscale == 0:
          xscale = 1
        if yscale == 0:
          yscale = 1
        
        objCoords = self.getCoords(self.tag)
        if(not objCoords):
          return

        if( moveLinks ):     
          to_move = self.__associate_links_with_connectors()        
          self.dc.scale(self.tag, objCoords[0], objCoords[1], xscale, yscale)    
          self.__move_links_to_connectors(to_move)
        else:    
          self.dc.scale(self.tag, objCoords[0], objCoords[1], xscale, yscale) 
             
        
    def deleteGraphicalConnection(self, handler):
        """
           Deletes connection with handler 'handler' from actual node and from the other node end.
        """
        for conn in self.connections:
           if conn[0] == handler: 			# we have found it!
              self.connections.remove(conn)
              break
        for tag in VisualObj.Tag2ObjMap.keys():		# run on all the graphical objects
           obj = VisualObj.Tag2ObjMap[tag]
           if obj != self:
              for conn in obj.connections:
                 if conn[0] == handler: 		# we have found it!
                    obj.connections.remove(conn)
                    return
        self.destroy()          # Added 24/12/2003 by JL
        self.isDestroyed = 0    # Added 24/12/2003 by JL

    def HighLight(self, flag):
      """
         Highlights (flag = 1) or LowLights (flag = 0) all the VISIBLE elements with the 'selected' tag
      """
      # for each graphical form in graphObject, HighLight it...
      for grf in self.graphForms:
         grf.HighLight(flag)                       				# 1 = HighLight

    def connect(self, obj, intermediatePoints = [], x0 = None, y0 = None, x1 = None, y1 = None, smoothConn = 0, num1st = 2):
      """
         Connects this object with another object of type 'graphLink'. The connection may have intermediate points, stored in the list
         intermediatePoints
      """
      handlerTuple = obj.getSegment("IN")					        # get the new segment
      handler, tag, segmObj, linkObj = handlerTuple				        # unwrap the tuple
      hcoords = self.dc.coords(handler)						        # get the new segment coordinates
      if intermediatePoints == [] :
         mx, my = self.getMinDistance_Connectors2Fixed(self, hcoords[2], hcoords[3])    # get the connector whose distance to the center is minimum
      else:
         px, py = intermediatePoints[0], intermediatePoints[1]
         mx, my = self.getMinDistance_Connectors2Fixed(self, px, py)		        # get the connector whose distance to the center is minimum
      # set the correct initial and final coordinates if any...
      cx, cy = hcoords[len(hcoords)-2], hcoords[len(hcoords)-1]
      if x0 != None and y0 != None and x1 != None and y1 != None:
         cx, cy = x1, y1
         mx, my = x0, y0
      pointList = [mx, my] + intermediatePoints + [cx, cy]			        # create a list with the intermediate points
# HV
#      self.dc.coords(handler, tuple(pointList))                                                # move the connection!
      apply(self.dc.coords, tuple([handler] + pointList))                       
      if smoothConn:
      	self.dc.itemconfig(handler, smooth = 1)
      self.connections.append((handler, 0, segmObj, linkObj, obj ))		        # add segmentHandler to obj.connections
      if linkObj:
         dx, dy = mx-hcoords[0], my-hcoords[1]
         linkObj.Move(dx, dy, 0)

      coordinates = self.dc.coords(handler)
      if len(coordinates) > 6:
        aux = self.reverseList2by2(coordinates[2:len(coordinates)-2])        
        coordinates = coordinates[0:2]+aux+coordinates[len(coordinates)-2:]

      self.out_connections_Points[handler] = (self.tag, obj.tag, coordinates, smoothConn, num1st)
      obj.connectActions (handlerTuple)                                                 # call the other object to make the appropriate actions

      return handler

    def connectActions (self, htuple, obj):
      """
         Actions performed if this object is the destination of a connection.
         Adds the handler (1st component of htuple) to the list of connections
      """
      segmentHandler, tag, sObj, lObj = htuple                                  	# Unwrap the tuple
      self.connections.append((segmentHandler, 1, sObj, lObj, obj))                     # add segmentHandler to obj.connections

    def removeConnection(self, atom3i, handler):
      """
         Removes the (input or output) connection whose handler is 'handler'.
          - Returns:
            -1 if handler is not a connection.
            0  if handler corresponds to an output segment
            1  if handler corresponds to an input  segment
      """
      deleted = self.removeConnectionFromList(handler)
      
      if deleted: return deleted[1]
      else: return -1

    def erase (self, atom3i, deleteConnections=True, entityOnly=False):
      """
         It is used to delete the graphical Object. atom3i is an instance of ATOM3.
      """
      #todo: qocaCleanup
      self.qocaCleanup(atom3i)
      
      
      if deleteConnections:
         while self.connections != []:                                               	# clear all the connections...
            c    = self.connections[0]
            try:
              tags = self.dc.gettags(c[0])
            except:
              print "WARNING: tag ", c[0], " not found & not removed by erase of graphEntity.py (Severity = LOW)"
              return -1
            if(entityOnly == False and len(c) > 0 and len(tags) > 0):  # Modified 4-Jul-2002     
               atom3i.deleteConnection(c[0], tags[0])   # delete connection! (calling pre and post conditions)
            if c in self.connections:						        # Modified 18-Jan-2002
               self.connections.remove(c)
      cts = self.dc.find_withtag(self.tag)
      for c in cts: 
        self.dc.delete(c)
      self.Destroy()    


    def redrawObject(self, canvas, showGG = 0):
      """
      	 The canvas in which this object was drawn has been closed, and now it is requested to this object to draw itself again...
      """
      while len(self.connections)>0: self.connections.pop()			# remove connectors 'in place'
      while len(self.connectors)>0: self.connectors.pop()			# remove connectors 'in place'
      while len(self.graphForms)>0: self.graphForms.pop()			# remove graphForms 'in place'
      self.attr_display = {}
      
      # Ensure self.x and self.y are okay (GraphGrammar fix/hack)
      self.dc = canvas
      self.checkCoords()  
      
      self.DrawObject(canvas, showGG)

    def getbbox(self):
      """
         gets the bounding box of this object
      """
      minx, miny, maxx, maxy = 100000, 100000, -100000, -100000
      # 1st collect all the handlers...
      for grform in self.graphForms:
         bbx = self.dc.bbox(grform.handler)
         if bbx:	# the thing can be invisble and not have bounding box!!!
            if bbx[0] < minx: minx = bbx[0]
            if bbx[1] < miny: miny = bbx[1]
            if bbx[2] > maxx: maxx = bbx[2]
            if bbx[3] > maxy: maxy = bbx[3]

      return (minx, miny, maxx, maxy)

    def write2File(self, file, indent):
      """
         Writes its properties into a file .
      """
      for gf in self.graphForms:
        gf.write2File(file, indent)

    def getNamedPort(self, handler_connection ):
      """
         Returns the name of the named connector which is connected to the connection whose handler is
         'handler_connection'. None if it can not be found.
         Created 24 July 2002 by JL
      """
      coords_connection = self.dc.coords(handler_connection)
      cx1, cy1 = coords_connection[0], coords_connection[1]
      cx2, cy2 = coords_connection[len(coords_connection)-2], coords_connection[len(coords_connection)-1]
      for nc in self.namedConnectors.keys():                    # get the handlers of the named connectors
          ncc = self.dc.coords(nc)
          #print cx1 >= ncc[0], cy1 >= ncc[1], cx1 <= ncc[2], cy1 <= ncc[3]
          if cx1 >= ncc[0] and cy1 >= ncc[1] and cx1 <= ncc[2] and cy1 <= ncc[3]:
              return self.namedConnectors[nc]
          if cx2 >= ncc[0] and cy2 >= ncc[1] and cx2 <= ncc[2] and cy2 <= ncc[3]:
              return self.namedConnectors[nc]  
      return None

    def hasNamedPortInConnector (self, handler):
      """
         Looks to see if in the connector 'handler' there is a named Port. If it does, return the name
         Created 24 July 2002 by JL         
      """
      if self.namedConnectors.has_key(handler): return self.namedConnectors[handler]
    
    def getConnectedObjectByHandler (self, handler):
      """
         Returns the object connected to self by the connection handler, if any.
         Created 24 July 2002 by JL                  
      """
      for conn_tuple in self.connections:
          hndler, dir, sobj, lobj, other_obj = conn_tuple
          if handler == hndler: return other_obj
      return 0
    
    def getSizeOld(self):
      """
         Method that returns the (SizeX, SizeY) tuple
         Added 05 Nov 2002 by Juan de Lara
      """
      return (self.sizeX, self.sizeY)
    
    #--------------------------- ADDED Summer 2004 by Denis --------------------
    
    def hasNamedPorts(self):
      """ Returns True if the entity has at least one named port """
      if( self.namedConnectors ):
        return True
      return False
    
    def getSize( self ):
      """ This new getSize() method takes scaling into account """
      sx, sy = self.layConstraints['scale']
      return ( sx * self.sizeX, sy * self.sizeY)
      
    def getCenterCoord(self):
      """
      Returns the center of the object, whereby the center is defined to be
      the center of all the connection ports
      Added June 10, 2004 by Denis Dube
      """
      x = y = 0
      for h in self.connectors:
        x0, y0, x1, y1 = self.dc.coords(h)
        x += (x0+x1)/2
        y += (y0+y1)/2
      
      size = len( self.connectors )
      if( size == 0 ):
        return (self.x,self.y)
      return ( x/size, y/size )
    
    def getNearestConnectors( self, other ):
      """ 
      Returns the connectors that are nearest each other of two entities 
      Added July 22, 2004 by Denis Dube
      """
      from MathUtilities import fastDistanceApproximation
      nearestDist = 900000
      nearPoints = None
      for sHandler in self.connectors:
        if(other.hasConnectors):          
          for oHandler in other.connectors:
            x0, y0, z, z = self.dc.coords(sHandler)
            x1, y1, z, z = self.dc.coords(oHandler)
            d = fastDistanceApproximation( x0-x1,y0-y1 )
            if( d < nearestDist ):
              nearestDist = d
              nearPoints = ( [x0,y0], [x1,y1] )
        else:
          x0, y0, z, z = self.dc.coords(sHandler)
          x1, y1 = other.getCenterCoord()
          d = fastDistanceApproximation( x0-x1,y0-y1 )
          if( d < nearestDist ):
            nearestDist = d
            nearPoints = ( [x0,y0], [x1,y1] )
          
      if( nearPoints == None ): 
        raise Exception, "No near points found! Are you sure both nodes are on a canvas?"
      return nearPoints
      

    
    def getConnectorBoundaryBox(self):
      
      minX = minY = 100000
      maxX = maxY = -1
      for h in self.connectors:
        x0, y0, x1, y1 = self.dc.coords(h)
        if( x0 > maxX ):
          maxX = x0
        if( x0 < minX ):
          minX = x0
        if( y0 > maxY ):
          maxY = y0
        if( y0 < minY ):
          minY = y0

      #self.dc.create_rectangle( minX,minY,maxX,maxY )
      return [minX,minY,maxX,maxY ]
        
        
    def setSelectAll(self):
      """ Dummy method, cheaper to activate than figuring out if link or node. Added June 22, 2004 by Denis Dube """
      pass
    
    def hasConnectors(self):
      """ Does the entity have anything to connect to??? Added June 22, 2004 by Denis Dube """
      if( self.connectors or self.namedConnectors ): return True
      return False
  
  
    def ScaleText( self, scale ):
        """ Scales all text attributes, if any, added August 12, 2004 by Denis Dube """
        for gf in self.graphForms:
            if( gf.getFont() ):
              fontObject = gf.getFont()              
              fontObject.config( size=int( scale * gf.getFontSize() ) )
              gf.refreshFont()  
  
    
    def scaleHack(self,sx, sy ):
      """ 
      This ugly hack is needed because DCharts scales objects automatically
      when you save/load a model... but woops, it doesn't save the scaling on
      the connectors. Grrrr.
      Thus this method will scale & move the connectors so they match with
      the graphical object.
      Added July 21, 2004 by Denis Dube
      """
      
      def getCentralObjectBoundaryBox():
        for gf in self.graphForms:
          c = self.dc.coords( gf.handler )
          if( len(c) == 4 ):
            return c
      
      c = self.getCenterCoord()
      x0,y0,x1,y1 = getCentralObjectBoundaryBox()
      cTarget = [ (x0+x1)/2, (y0+y1)/2 ]
      dx,dy = [ cTarget[0] - c[0], cTarget[1] - c[1] ]
      #print c, cTarget, dy
            
      for con in self.connectors:					# move each connector
        self.dc.scale(con, c[0],c[1], sx, sy)
        self.dc.move( con, dx, dy)

      #self.dc.create_rectangle( x0,y0,x1,y1,fill="red", stipple='gray25' )
      
    def moveTo(self, x=None, y=None):
      """ Convenience method: Moves this entity to the new location """      
      self.x, self.y = self.getbbox()[:2]      
      if(x is not None):
        dx = x - self.x
      else:
        dx = 0
      if(y is not None):
        dy = y - self.y   
      else:
        dy = 0
      self.Move(dx, dy, moveConn=False )
      
    def invisibleMoveTo(self, coords2DTuple):
      """
      Intention in context:
        Moves an "invisible" icon containing just a connection port to the 
        coordinates given by the parameter coord2DTuple
        DO NOT USE WITH NORMAL ICONS
      Assumption: 
        The connectors are Tkinter canvas oval shapes, defined by 4 coords.
      """
      self.x, self.y = coords2DTuple
      for itemHandler in self.connectors:
        self.dc.coords(itemHandler, (self.x, self.y, self.x + 1, self.y + 1))
      
      
    def animatedMoveTo(self, coord2DTuple, timeSecInt=1, acceleration=0):     
      """ 
      Moves the entity to the coordinates (x, y) in timeSecInt seconds
      
      Alternatively, use an acceleration value to move your entity to the 
      desired coordinate. Accleration does not allow you to choose the time 
      duration, although a high acceleration such as 400 pixels/sec will not 
      require much more than a second or two... 
      
      WARNING: This method is very rough and un-polished!
      """
      dc = self.dc
      framesPerSecond = 15 # If this was a video game... 60 FPS, but it isn't
      frequency = 1.0 / float(framesPerSecond)
      self.x, self.y = self.getbbox()[:2] 
      
      x, y = coord2DTuple
      if(x is not None):
        dx = x - self.x
      else:
        dx = 0
      if(y is not None):
        dy = y - self.y   
      else:
        dy = 0
      
      # Linear animation speed (no acceleration)
      if(acceleration == 0):
        keyFrames = float(framesPerSecond * timeSecInt)
        dxPerFrame = float(dx) / keyFrames
        dyPerFrame = float(dy) / keyFrames
        i = 0
        while(i < keyFrames):
          self.Move(dxPerFrame, dyPerFrame, moveConn=False )
          dc.update()
          sleep(frequency)
          i += 1
      
      # Quadratic animation speed (motion accelerates)
      # This is a messy new method, seems to work though :)
      # Should probably change it so that the time to impact is computed
      # as the maximum of dx and dy. If dy is very small, dx will move like
      # a rocket...
      else:
        if(dy == 0):
          dy = 0.001
        if(dx == 0):
          dx = 0.001
        oldPos = [self.x, self.y]
        from math import sqrt
        
        aY = float(acceleration)  # Gravity like acceleration
        if(dy < 0):
          aY = -aY
        totalTimeToImpact = sqrt(abs(2 * dy / aY))
        #print 'totalTimeToImpact', totalTimeToImpact
        aX = 2 * dx / (totalTimeToImpact * totalTimeToImpact)
        keyFrames = float(framesPerSecond * totalTimeToImpact)
        for i in range(1, int(keyFrames) + 1):
          t = float(i) * frequency
          newX = oldPos[0] + 0.5 * aX * t * t
          newY = oldPos[1] + 0.5 * aY * t * t
          #print 't', t, 'pos', newX, newY          
          self.Move(newX - self.x, newY - self.y, moveConn=False )
          dc.update()
          sleep(frequency)  
        
        # The acceleration is a simulation, doesn't give the exact answer...
        # So nudge it to the final position
        self.Move(x - self.x, y - self.y, moveConn=False )
      
            
    def fitNodeToText2( self, textGFtupleList ):
        """ 
        Scales an object such that text will fit 
        Input: 
          List of tuples
        Tuple: 
          string text (can be many lines)
          graphicalForm of the text attribute(graphicalForm = gf in icon editor)
          graphicalForm that has the text encapsulated (should be tight)
          float multiplier to inc/dec X size of text container, default 1.00
          float multiplier to inc/dec Y size of text container, default 1.00
        """
        
        self.resetScale()       
        sx = sy = 0.00
        for textGFtuple in textGFtupleList:
          text, gfText, gfContainer = textGFtuple[0:3]
          
          # Fudge arguments because the text metrics are innaccurate in Tcl/Tk
          if( len( textGFtuple[3:] ) == 2 ):
            fudgeX = textGFtuple[3]
            fudgeY = textGFtuple[4]
          elif( len( textGFtuple[3:] ) == 1 ):
            fudgeX = textGFtuple[3]
            fudgeY = 1
          else:
            fudgeX = fudgeY = 1  
      
          # Strip trailing newlines, then get a list of lines
          text = string.rstrip( text, '\n' )
          text += '\n' # <-- removed one too many...
          lines = string.split( text , '\n' )
          if( lines[-1] == '' ): lines = lines[:-1]
          #print 'lines: ', lines
          
          w = 1.00
          for line in lines:
            w = max( w, gfText.getFontMeasure( line ) )
          w *= fudgeX # <--- font measure is unreliable!!!
          h = gfText.getFontMetric() * fudgeY
          h = h * len( lines )
          
          x0,y0,x1,y1 = gfContainer.getBbox()
          wc = x1-x0
          hc = y1-y0
          
          #print 'text :', w,h
          #print 'container :', wc,hc
          
          if( w > wc ): sx = max( sx, float(w) / wc )
          if( h > hc ): sy = max( sy, float(h) / hc )
          #print 'Current sx is', sx
          #print 'GFinfo', gfText.fontObject.actual() 
          
        #print 'Scale by: ', sx,sy
          
        # Increase X and Y size to fit longest line
        if( sx and sy ): 
          self.Scale( sx, sy, moveLinks = False )       
          self.layConstraints['scale'] = [sx, sy]
                    
        # Increase X size to fit longest line
        elif( sx ): 
          self.Scale( sx, 1.00, moveLinks = False )       
          self.layConstraints['scale'] = [sx, 1.00]   

        # Increase Y size to fit lines
        elif( sy ): 
          self.Scale( 1.00, sy, moveLinks = False )    
          self.layConstraints['scale'] = [1.00, sy]     
      
        
      
    def fitNodeToText( self, text, charHeight=18.0, charWidth=7.5 ):
        """ 
        Scales an object such that text will fit 
        NOTE: Char height & width will vary from font to font!
        If the font were a tkFont object, you might use the measure() method...
        But even that turns out to be undependable! Bah! Bah I say...
        """
      
        # Strip trailing newlines, then get a list of lines
        text = string.rstrip( text, '\n' )
        text += '\n' # <-- removed one too many...
        lines = string.split( text , '\n' )
        
        # Approximate the pixel size of character width & height
        desiredHeight = len( lines ) * charHeight
        desiredWidth = 0
        for line in lines:
            if( len( line ) > desiredWidth ):
                desiredWidth = len( line )
        desiredWidth *= charWidth
        
        # Reset the scaling factor on the object back to 1.00
        sx,sy = self.layConstraints['scale']         
        self.Scale( 1.00 / sx, 1.00 / sy, moveLinks = False ) 
        self.layConstraints['scale'] = [ 1.00, 1.00 ]
        
        # Get the size of our object
        w, h = self.getSize()

        # Increase X size to fit longest line
        if( desiredWidth > w + 2 ):  

            sx = desiredWidth / w      
            self.Scale( sx, 1.00, moveLinks = False )          
            self.layConstraints['scale'] = [sx, sy ]
                      
          
        # Increase Y size to fit lines
        if( desiredHeight > self.sizeY + 2 ):
                                  
            sy = desiredHeight / h 
            self.Scale( 1.00, sy, moveLinks = False )         
            self.layConstraints['scale'] = [sx, sy]
 
      
          
          
    def isConnectedByNamedPort( self, semanticEdgeObject ):
      """
      Determines if the semantic object of this graphical entity is connected
      by named port to the given semantic edge object.
      NOTE: Requires graphical attributes to figure out, so method belongs here! 
      """
      for namedPortHandler in self.namedConnectors.keys():
        namedPort = self.namedConnectors[ namedPortHandler ]
        namedPortEdgeObjects = getattr( self.semanticObject, namedPort )
        for namedPortEdgeObject in namedPortEdgeObjects:          
          if( namedPortEdgeObject == semanticEdgeObject ): 
            return True
      return False
      
      
    def getConnectedByNamedPortHandler( self, semanticEdgeObject ):
      """
      Determines if the semantic object of this graphical entity is connected
      by named port to the given semantic edge object.
      NOTE: Requires graphical attributes to figure out, so method belongs here! 
      Returns the handler so you can get the coords of this port
      """
      for namedPortHandler in self.namedConnectors.keys():
        namedPort = self.namedConnectors[ namedPortHandler ]
        namedPortEdgeObjects = getattr( self.semanticObject, namedPort )
        for namedPortEdgeObject in namedPortEdgeObjects:          
          if( namedPortEdgeObject == semanticEdgeObject ): 
            return namedPortHandler

          
    def getAnyItemHandler( self ):
      """ Returns the first item handler belonging to this visual entity """
      for gf in self.graphForms:
        if( gf.handler ): 
          return gf.handler
      if(self.connectors):
        return self.connectors[0] # Desperation move, return port itemhandler
      return None
    
    def raiseItem( self ):
      """ Lifts the item to the foreground of the canvas """
      for gf in self.graphForms:
        gf.lift()
        
    
    def scaleX(self, w):
      """ Quick 1 dimensional scaling along X """
      sx,sy = self.layConstraints['scale']         
      self.Scale( 1.00 / sx, 1.00, moveLinks = False ) # Reset scale X   
      sx = 0.1 # Minimum of 10 percent of original size
      sx = max(sx, float(w) / float(self.sizeX))   
      
      #self.qocaScale(box[:2], sx, 1.00)
      self.Scale( sx, 1.00, moveLinks = False )       
      self.layConstraints['scale'] = [sx, sy]
      
      box = self.getbbox()
#      print 'scale factor', sx
#      print 'scaled x (w desired, box)', w, box[2] - box[0], box
      
    def scaleY(self, h):
      """ Quick 1 dimensional scaling along Y """
      oldY = self.getbbox()[1]
#      print 'oldY', oldY, self.getbbox()[1]
      
      sx,sy = self.layConstraints['scale']         
      self.Scale( 1.00, 1.00 / sy, moveLinks = False )  # Reset scale Y     
      sy = 0.1 # Minimum of 10 percent of original size
      
      
      sy = max(sy, float(h) / float(self.sizeY))      
      self.Scale( 1.00, sy, moveLinks = False )
      self.layConstraints['scale'] = [sx, sy]
      
      dy = oldY - self.getbbox()[1]
      self.Move(0, dy, moveConn=False )
#      print 'new Y', self.y, self.getbbox()[1]
      self.y = self.getbbox()[1]
      box = self.getbbox()
#      print 'scaled y (h desired, actual)', h, box[3] - box[1]

    def resetScale( self ):
      """ 
      Reset the scaling factor on the object back to 1.00
      This can make subsequent scaling much easier :D
      """
      sx,sy = self.layConstraints['scale']         
      self.Scale( 1.00 / sx, 1.00 / sy, moveLinks = False ) 
      self.layConstraints['scale'] = [ 1.00, 1.00 ]
         
      
    def easyScale( self, dWidth, dHeight ):
      """
      Parameters:
        desired Width & Height
      Output:
        Scales entity to be just large enough to have the desired Width & Height
      """
      
      self.resetScale()
      sx = sy = 0.1 # Minimum size, 10 percent of default size
      
      # Get the actual Width & Height of this entity
      ## bbx = self.getbbox()
      ## aWidth =  bbx[2]-bbx[0] 
      ## aHeight = bbx[3]-bbx[1] 
      aWidth = self.sizeX
      aHeight = self.sizeY

      if(aWidth == 0): 
        sx = 1.0
      else:
        sx = max( sx, float(dWidth) / float(aWidth) )
      if(aHeight == 0): 
        sy = 1.0
      else:
        sy = max( sy, float(dHeight) / float(aHeight) )
      
      self.Scale( sx, sy, moveLinks = False )       
      self.layConstraints['scale'] = [sx, sy]
      
      #print 'Desired vs Actual widths:', dWidth, 'vs', aWidth, 'scale',sx
      #print 'Desired vs Actual heights:', dHeight, 'vs', aHeight, 'scale',sy
      
      ## # Increase X and Y size to fit longest line
      ## if( sx and sy ): 
        ## self.Scale( sx, sy, moveLinks = False )       
        ## self.layConstraints['scale'] = [sx, sy]
                  
      ## # Increase X size to fit longest line
      ## elif( sx ): 
        ## self.Scale( sx, 1.00, moveLinks = False )       
        ## self.layConstraints['scale'] = [sx, 1.00]   

      ## # Increase Y size to fit lines
      ## elif( sy ): 
        ## self.Scale( 1.00, sy, moveLinks = False )    
        ## self.layConstraints['scale'] = [1.00, sy] 
        
        
    def hierarchicalDisconnect(self, semanticParent, extendSearchBox = 0 ):
        """
        When to use: 
          Call this method when dropping an entity to automatically remove it
          from it's containing entity if it is no longer near it
        Parameters:
          semanticParent: semantic object that is this objects parent in the 
            hiearchy.
          extendSearchBox: For small entities, you may want to extend their 
            'search' radius for container objects. Value is in pixels.
        Return Values:
          None: could not proceed, needed references not found
          False: no disconnect occured
          True: disconnect occured
        Created March 2005, Denis Dube
        """
  
        # Get some useful references (and be super cautious about it)
        semObj = self.semanticObject
        if( not semObj ): return
        atom3i = semObj.parent
        if( not atom3i ): return
        canvas = atom3i.getCanvas()
        if(not canvas): return
        
        # Search region: Bounding box plus some extension
        bbox = self.getbbox()
        bbox = [ bbox[0] - extendSearchBox, bbox[1] - extendSearchBox,
                 bbox[2] + extendSearchBox, bbox[3] + extendSearchBox ]
                 
        TAG2OBJ = VisualObj.Tag2ObjMap # Maps tags to their objects        
        tagsProcessed = ['current', self.tag ] 
        objCandidates = []
       
        # Find all items under our newly created self object
        itemList = canvas.find_overlapping( *bbox ) 
        for item in itemList:
            tags = canvas.gettags( item ) 
            # Go through the tags, ignore those we've already seen
            for tag in tags:
                if( tag not in tagsProcessed ):
                    tagsProcessed.append( tag )
                    # Get the object from the tag
                    if( TAG2OBJ.has_key( tag ) ):
                        overObj = TAG2OBJ[tag]            
                        overSemObj = overObj.semanticObject
                        # Note: this may not even be a valid container
                        if( overSemObj ): objCandidates.append( overSemObj )

        # Is our parent nearby to the location we occupy? If so, no disconnect
        if( semanticParent in objCandidates ): return False
  
        # Okay, lets disconnect if the user agrees... so show dialog
        text = 'Disconnect '+semObj.name.toString() + ' from '
        text += semanticParent.name.toString() + ' ?'
        stringList = ( 'Disconnect', 'Cancel')
        response = self.showDialog( 'Hierarchical disconnect', text, stringList )
    
        # Read dialog response, apply connection unless cancelled
        if( response != 0 ): return False 
        
        # Alrighty then, now we must find the connection and kill it
        for INconnection in semObj.in_connections_:
            for OUTconnection in semanticParent.out_connections_:
                if( INconnection == OUTconnection and INconnection.graphObject_):
                    obj = INconnection.graphObject_
                    
                    atom3i.deleteConnection(obj.getAnyItemHandler(), obj.tag)
                    #atom3i.deleteRealEntity( None, INconnection.graphObject_ )
        return True
        
        
    def hierarchicalConnect(self, ERcontainerNames, extendSearchBox=0,
                                   ignoreSelected=True, filterLinkTypeList=None ):
        """
        When to use: 
          Call this method when creating/dropping an entity to add it to
          automatically add it to a hierarchical container entity
        Parameters:
          ERcontainerNames: The actual class name of all possible containers for
            this object. 
            IE: This is just the name you gave the entity in the ER model or
                class diagram model
          extendSearchBox: For small entities, you may want to extend their 
            'search' radius for container objects. Value is in pixels.
        Return Values:
          False: no connect occured
          True: connect occured
        What it does: 
          Checks to see if we have overlapped an existing entity and
          then tries to connect the two together, hopefully this will be an 
          insideness relation, since the alternative might look wierd...
        Created March 2005, Denis Dube
        """
              
        # Get some useful references (and be super cautious about it)
        semObj = self.semanticObject
        if( not semObj ): 
          return False
        atom3i = semObj.parent
        if( not atom3i ): 
          return False
        canvas = atom3i.getCanvas()
        if(not canvas): 
          return False
        
        # Assuming that children will be selected, we find them this way
        # Selected = {tag : [itemHandler, Object] }
        cb = atom3i.cb
        if( not cb and ignoreSelected ): 
          return False
        if( ignoreSelected ): 
          selected = cb.getSelectionDict()
        else: 
          selected = dict()
        
        # Search region: Bounding box plus some extension
        bbox = self.getbbox()
        bbox = [ bbox[0] - extendSearchBox, bbox[1] - extendSearchBox,
                 bbox[2] + extendSearchBox, bbox[3] + extendSearchBox ]
        
        TAG2OBJ = VisualObj.Tag2ObjMap # Maps tags to their objects        
        tagsProcessed = ['current', self.tag ] 
        objCandidates = []
        
        # Find all items under our newly created self object
        itemList = canvas.find_overlapping( *bbox ) 
        for item in itemList:
            tags = canvas.gettags( item ) 
            # Go through the tags, ignore those we've already seen
            for tag in tags:
                # Ignore tags of selected children and tags already seen
                if( not selected.has_key(tag) and tag not in tagsProcessed ):
                    tagsProcessed.append( tag )
                    # Get the object from the tag
                    if( TAG2OBJ.has_key( tag ) ):
                        overObj = TAG2OBJ[tag]            
                        overSemObj = overObj.semanticObject
                        if( overSemObj ):
                            # Only ERcontainerNames can contain us!
                            if( overSemObj.__class__.__name__ in ERcontainerNames ):
                                objCandidates.append( overSemObj )
        
        
            
        
        # We have possible containers for this object
        if( objCandidates ):
             
            # SIMPLE Hierarchical add: just add it to the top level thing
            oldCandidates = objCandidates[:]
            for obj in oldCandidates:
              for containedObjLink in obj.out_connections_:
                for containedObj in containedObjLink.out_connections_:
                  if(containedObj in objCandidates):
                    objCandidates.remove(obj)
                    break
            if(len(objCandidates) == 1):
              from DrawConnections import simpleConnection     
              simpleConnection( atom3i, objCandidates[0], semObj, 
                                          filterLinkTypeList=filterLinkTypeList)
              return True
              
            
            # MORE COMPLEX METHOD:                      
            # Put together a meaninful selection of choices (actual object names)
            objCandidates = oldCandidates
            stringList = []
            for container in objCandidates:
                stringList.append( container.name.toString()  )
            if( ignoreSelected ): stringList.append( 'Help' )
            stringList.append( 'Cancel' )
        
            # Show dialog
            text = 'Add '+semObj.name.toString()+' to...'    
            response = self.showDialog( 'Hierarchical add', text, stringList )
        
            # Read dialog response, apply connection unless cancelled
            if( ignoreSelected and response == len(stringList) -2 ): 
                text = 'Why can I not add to item X? I dragged over it!'
                text += '\n\nMake sure item X is not selected, selected items'
                text += ' are ignored (cycle prevention mechanism)'
                self.showDialog( 'Hierarchical add', text, ['Okay'] )
                return self.hierarchicalConnect( ERcontainerNames,
                                              extendSearchBox, ignoreSelected )
                     
            if( response >= len(stringList) -1 ): 
              return False      
            from DrawConnections import simpleConnection     
            simpleConnection( atom3i, objCandidates[response], semObj, 
                                          filterLinkTypeList=filterLinkTypeList)
            return True
        return False
                
                
    def showDialog( self, title, text, stringList, default = 0 ):
      """ Simple dialog --> Useful for the hierarchical add/del methods """      
      if( self.semanticObject and self.semanticObject.parent ):  
          root = self.semanticObject.parent.parent
      else:
          root = None      
      d = Dialog.Dialog(root, {'title': title, 'text': text, 'bitmap': '',
                      'default': default, 'strings': stringList})
      return d.num
      
      
    def getClosestConnector2Point(self, graphObject, fx, fy):
        """
         Returns the connector (cx, cy) of graphObject which makes minimum 
         the distance to (fx, fy)
         NOTE: Only considers un-named connectors because you would never use
         this method if a named connector was involved
        """                  
        maxDistance = 2000              # flag with the minimum distance so far...
        mdx0, mdy0  = 0,0
        for j in self.connectors:
           # Ignore named ports
           if(self.namedConnectors.has_key(j)):
             continue
           x0, y0, x1, y1 = graphObject.getCoords(j)        # get coordinates of connector # j
           xc1, yc1 = (x0+x1)/2, (y0+y1)/2          # calculate the middle point
           actDistance = self.distance(xc1, yc1, fx, fy)      # calculate distance from (fx, fy) to connector j middle point
           if actDistance < maxDistance:          # if this is less than the minimum distance found so far
              maxDistance = actDistance            # write it down
              mdx0, mdy0 = xc1, yc1
        return (mdx0, mdy0)
               
    def guesstimateNamedConnAtPoint(self, x, y):
       """ 
       Guess/estimates the name of the named connector near x, y 
       Denis: I'm probably being overly pessimistic here...
       """
       bestGuessValue = sys.maxint
       bestGuessHandler = None
       for connHandler in self.namedConnectors.keys():
         cnX, cnY = self.dc.coords(connHandler)[:2]
         diffSum = abs(x - cnX) + abs(y - cnY)
         if(diffSum < bestGuessValue):
           bestGuessValue = diffSum 
           bestGuessHandler = connHandler
       if(bestGuessHandler and bestGuessValue < 10):
         return self.namedConnectors[bestGuessHandler]
       return None
         
    def setVisibility(self, isVisible):
      """
      Sets the visibility of this graphObject_ and all its dependents
      Parameter:
        isVisible, boolean True or False with obvious meaning
      """
      for gf in self.graphForms:
        gf.setVisibleSimple(isVisible)
     
         
