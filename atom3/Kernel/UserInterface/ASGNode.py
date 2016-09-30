# __ File: ASGNode.py ________________________________________________________________________________________________
#  Implements  : class ASGNode
#  Author      : Juan de Lara
#  Description : Base (Abstract) class for Nodes in a ASG
#  Modified    : 16 July 2002
#  Changes :
#   - 23 Oct 2001 : added method "hasGenerativeAttributes"
#   - 3 Nov  2001 : in methods copy and cloneActions, added statement to copy and clone the rootNode and objectNumber field
#   - 23 Nov 2001 : added method "updateAppearanceAttributes". Copied from old version of ATOM3
#   - 23 Nov 2001 : The method "attributesToDraw" is filled (it was as pass, and then implemented in entities
#                   and relationships of the ERMetaModel. Now this is not necessary. Copied from old version of ATOM3
#   - 30 Nov 2001 : AttributesToDraw was fixed, because sometimes the dictionary self.generatedAttributes does not give the complete information
#		    about which type the components of a list have.
#   - 16 July 2002: Added a list called realOrder which stores the string names of the attributes in the order they've
#                   been created.
#   - 06 August 2002: Added method isSubType.
# _____________________________________________________________________________________________________________________
from types import *
import string
from ATOM3Integer import *
from ATOM3Boolean import *
from AttrCalc     import *
from ATOM3Type import isSubTypeOfByDenis

from ModelSpecificCode        import isConnectionLink
from HierarchicalASGNode import HierarchicalASGNode


class ASGNode(HierarchicalASGNode):
  # static variable to count the number of objects created so far
  numObjects = 0
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
  # Values that editGGLabel can take...
  INLHS      = 1		# This means that the node is being edited in a Graph Grammar Rule, on the LHS (shows a 'setAny' widget)
  INRHS      = 2    # This means that the node is being edited in a Graph Grammar Rule, on the LHS (shows a 'copy values' widget)
  INMODEL    = 0		# This means that the node is not being edited in a Graph Grammar

  def __init__(self):
     self.processed    = 0 				# flag if we are using the visitor pattern...
     self.objectNumber = ASGNode.numObjects		# get a unique object number
     ASGNode.numObjects= ASGNode.numObjects+1		# increase the total number of object of this class

     self.graphClass_    = None				# <graphClass_> class of the graphical object, may be None
     self.graphObject_   = None				# <graphObject_> graphical object, may be None
     
     self.in_connections_  = []				# incoming connections, may be empty
     self.out_connections_ = []				# outgoing connections, may be empty
     self.keyword_       = None       # Pointer to the attribute that is the keyword...
     self.containerFrame = None				# Frame that will be used to edit the class

     self.generatedAttributes = {}			# dicitionary that will contain all the generated attributes
     self.realOrder = []                                # list with the real order in which the attributes have been specified (changed 16 July 2002)
     self.directEditing = []                            # list with the directEditing flag...

     self.GGLabel  = ATOM3Integer()                     # Label for Graph Grammar stuff (positive integer)
     self.GGLabel.setValue(-1)				# initialize it to invalid value

     self.GGset2Any= {}					# Dictionary that will contain an ATOM3Boolean object for each widget. They will indicate if they must be set to None
     self.editGGLabel = 0				# Flag that indicates if the Graph Grammar Label must be edited
     self.rootNode = None				# this is the parent node
     
     self.parent = None # Instance of ATOM3. The value is set elsewhere.
     
     # Built-in hierarchy tracking by Denis Dube, Sept 2005
     HierarchicalASGNode.__init__(self)
       
          
  def getLastObjectNumber(self):
    """
       Returns the object number of the last created object
    """
    return ASGNode.numObjects-1

  def editGGLabel(self, frame, topWindowParent, showRow):
     "if the flag 'editGGLabel' is on, presents a widget to edit the Graph Grammar Label"
     if self.editGGLabel:				# if editGGLabel's value is INLHS or INRHS
        if self.GGLabel == None: self.GGLabel = ATOM3Integer()
        Label(frame, text="GGLabel").grid(row=showRow, column=0, sticky=W)  	
        self.GGLabel.show(frame, topWindowParent).grid(row=showRow, column=1, sticky=W)   # constraints

  def setGGAnyWidget (self, frame, topWindowParent, name, showRow, showCol):
     "if the flag 'editGGLabel' is on, presents a widget that allows to set the corresponding element to None"
     # if we're in the LHS of a Graph Grammar Rule...
     if self.editGGLabel == self.INLHS:					
        # Show the 'Set to any' widget...
        if (not name in self.GGset2Any.keys()) or (not self.GGset2Any[name]):
          print 'self.GGset2Any', self.GGset2Any, name
          self.GGset2Any[name] = ATOM3Boolean('Set to any', 0)            
          # set it to any if the corrsponding attribute is None...
          atr = self.getAttrValue(name)
 
          if atr.isNone(): 
            self.GGset2Any[name] = ATOM3Boolean('Set to any', 1)
            #self.GGset2Any[name].setValue((None,1))
        self.GGset2Any[name].show(frame, topWindowParent).grid(
                                        row=showRow, column=showCol, sticky=W)
     # If we're on the RHS of a Graph Grammar Rule...
     elif self.editGGLabel == self.INRHS:				
        if (not name in self.GGset2Any.keys()) or (not self.GGset2Any[name]):
           self.GGset2Any[name] = AttrCalc()				# watch out! we use the same dictionary!
        self.GGset2Any[name].show(frame, topWindowParent).grid(
                                      row=showRow, column=showCol, sticky=W)

  def GGcheckSetNone(self):
     "if the flag 'editGGLabel' is on, sets to none the attributes, conforming to the ATOM3Boolean objects in self.GGset2Any"
     if self.GGLabel:							# if we are using the GGLabel...
        self.GGLabel.destroy()						# then destroy it!
     if self.editGGLabel == self.INLHS:                                 # --- We have Labels ---
        for name in self.GGset2Any.keys():         			# Look over all the attribute names...
           atr = self.getAttrValue(name)				# get the attribute value...
           if self.GGset2Any[name].getValue()[1] == 1:			# see if we should set it to none...
              atr.setNone()						# set it to None
           else:
              atr.unSetNone()						# unset none (this is done because in some cases isNone is implemented as a flag)
     elif self.editGGLabel == self.INRHS:				# --- We have AttrCalc's ---
        for name in self.GGset2Any.keys():     				# Look over all the attribute names...
            self.GGset2Any[name].destroy()				# destroy it!

  def resetProcessed(self):
     "resets the processed flag"
     self.processed = 0

  def getAttributes(self):
     "Returns a list with the generated attributes"
     return self.generatedAttributes.keys()

  def getAttrValue(self, attribute):
     "returns the value associated with that attribute"
     return self.__dict__[attribute]

  def setAttrValue(self, attribute, value):
     "sets to 'value' the attribute specified"
     self.__dict__[attribute] = value

  def getClass(self):
     "Method that returns a string with the class name"
     return self.__class__.__name__

  def writeConstraint2File(self, file, indent, object, constraintType, constraint):
     "Writes the handling of the constraint to file"
     file.write('\n'+indent+'res=  '+object+'.'+constraintType+'('+constraint+')')
     file.write(indent+'if res:\n')
     file.write(indent+'   self.constraintViolation(res)\n')
     file.write(indent+'   self.mode=self.IDLEMODE\n')
     file.write(indent+'   return\n')
   
  def isSubclass( self, node, which):
      "returns != 0 if node is a subclass of which (which is the string name of the class)"
      bases = node.__class__.__bases__						# obtain the list of all the node's base classes
      for base in bases:							# iterate over all the base classes
         if base.__name__ == which: return 1					# ey! we have found a coincidence
      return 0									# if we have reached this point, then it is not a subclass



  def genConnectionsCode(self, file, genGraphicalInfo = 1, isRootNode = 0, 
                         indent='    ', genSelf = 0, writeComma = 0, 
                         nodesToGenList=[] ):
      """Generates code for the relations. 
      Returns 1 if something has been writed in the file,0 otherwise"""
      writed = 0    # Flag that will indicate if something has been writed
      if genSelf:       									# check if we should add "self."
         myName = 'self.obj'+str(self.objectNumber)
      else:
         myName = 'obj'+str(self.objectNumber)	# Compose file name
         

      # For each object in the input connections
      for obj in self.out_connections_:		 
          
          # Skip objects not in the selection (if any)
          if( nodesToGenList and obj not in nodesToGenList ):    
            continue
            
          
          # looping over the output connections is sufficient
          if genSelf:
             # Compose other object's name
             otherName = 'self.obj'+str(obj.objectNumber)					
          else:
             # Compose other object's name
             otherName = 'obj'+str(obj.objectNumber)
             						
          # now generate code to draw the connection
          if isRootNode:
             if (writeComma and isRootNode) or writed: 
               file.write(',\n')
             # Store information about graphical objects if graphical info 
             #   has to be generated...
             if genGraphicalInfo:								
                # see if both nodes are in the same sub-model...
                smoothCoord = 0
                
                #FIXME: at seeming random, returns bad coordinates!?!
                # Can't duplicate the problem at all :(
                try:
                  connCoords, num1st, smooth = \
                                  self.graphObject_.getConnectionCoordinates( 
                                                      "OUT", obj.graphObject_)
                except:
                  print "ERROR: getConnectionCoordinates returned none, " \
                          + "ASGNode.py in genConnectionsCode()"
                  print "    You will need automatic layout to fix this!"
                  connCoords = [10.0, 10.0, 20.0, 20.0] 
                  num1st = 2 
                  smooth = 1
                
                
                # if origin is a graphLink then must invert the points...
                if self.graphObject_.isSubclass("graphLink"):
                  connCoords = self.graphObject_.reverseList2by2(connCoords)
                      
                smoothCoord = self.graphObject_.itemcget(
                            self.graphObject_.getConnectionHandler(
                            "OUT", obj.graphObject_), "smooth")
                            
                if self.rootNode != obj.rootNode:    # ey! different models!
                   if genSelf:   # compose the root's name
                      rootName = 'self.obj'+str(obj.rootNode.objectNumber)
                   else:
                      rootName = 'obj'+str(obj.rootNode.objectNumber)
                   if smoothCoord and smoothCoord != "0": 
                     file.write('('+myName+'.graphObject_.tag, '+rootName
                           +'.graphObject_.tag, '+myName+','+otherName+','
                           +str(connCoords)+', "'+smoothCoord+'", '
                           +str(num1st)+')')
                   else: 
                     file.write('('+myName+'.graphObject_.tag, '+rootName
                     +'.graphObject_.tag, '+myName+','+otherName+','
                     +str(connCoords)+', 0, '+str(num1st)+')')
                else:
                   if smoothCoord and smoothCoord != "0": 
                     file.write('('+myName+','+otherName+','+str(connCoords)
                     +',"'+smoothCoord+'", '+str(num1st)+')')
                   else: 
                     file.write('('+myName+','+otherName+','+str(connCoords)
                     +', 0, '+str(num1st)+')')
             else: 
               file.write('('+myName+','+otherName+', None, 0)')
             writed = 1   # set flag to 1, because we have written something!
          elif( self.rootNode == obj.rootNode 
                  or (self.level() > 1 and self.level() < obj.level())):
             file.write(indent+myName+'.out_connections_.append('
                         +otherName+')\n')
             file.write(indent+otherName+'.in_connections_.append('
                         +myName+')\n')
	     info_tuple = self.graphObject_.getConnectionCoordinates( 
                   "OUT", obj.graphObject_)	# coords, len, (optional) smooth
	     if info_tuple:
	        file.write(indent+myName+'.graphObject_.pendingConnections.append((')
	        file.write(myName+'.graphObject_.tag, '+otherName
            +'.graphObject_.tag, '+str(info_tuple[0])+', '+str(info_tuple[1])
            +', '+str(info_tuple[2])+'))\n')                
             else:
                print "from:", myName, "(", self, ") to ", otherName, \
                      "info_tuple is None"
             writed = 1   # set flag to 1, because we have written something!
      # if connections come from other model, they are not still drawn!!!
      
      # For each object in the input connections
      for obj in self.in_connections_: 
          # Compose other object's name
          if genSelf:
             otherName = 'self.obj'+str(obj.objectNumber)	
          else:
             otherName = 'obj'+str(obj.objectNumber)						
          # now generate code to draw the connection
          if self.rootNode != obj.rootNode:       # ey! different models!
             if isRootNode:   # see if both nodes are in the same sub-model...
                if (writeComma and isRootNode) or writed: 
                  file.write(', ')
                # Store information about graphical objects if graphical 
                #  info has to be generated...
                if genGraphicalInfo:              
                   if genSelf:       # compose the root's name
                      rootName = 'self.obj'+str(obj.rootNode.objectNumber)
                   else:
                      rootName = 'obj'+str(obj.rootNode.objectNumber)
                   file.write('('+rootName+'.graphObject_.tag, '+myName
                   +'.graphObject_.tag, '+otherName+', '+myName+')')
                else: 
                  file.write('('+otherName+', '+myName+')')
                writed = 1 # set flag to 1, because we have written something!
             # we are not in the rootModel
             elif( self.rootNode == obj.rootNode 
                 or (self.level() > 1 and self.level() < obj.level())):                              			
                file.write(indent+myName+'.in_connections_.append('
                  +otherName+')\n')
                file.write(indent+otherName+'.out_connections_.append('
                  +myName+')\n')
                writed = 1 # set flag to 1, because we have written something!
      return writed

  def genCode(self, fileName, allowedTypes, genGraph = 1, isRootNode = 0):
      "generates code for creating this graph"
      return 0                      # must be overriden in ASG and ignored in ASGNode

  def attributesToDraw(self):
      """
         return a (Python) list of all the ATOM3Attribute attributes of this object.
      """
      listOfAttributes = []
      for attr in self.generatedAttributes.keys():
        infoTuple = self.generatedAttributes[attr]
        if infoTuple[0] == 'ATOM3Attribute':
          listOfAttributes.append(self.getAttrValue(attr))
        elif infoTuple[0] == 'ATOM3List' and self.getAttrValue(attr).itemType.__name__ == 'ATOM3Attribute':
          listOfAttributes = listOfAttributes+self.getAttrValue(attr).getValue()
      return listOfAttributes

  def setGGLabel(self, intValue):
      "sets the value for the GGLabel field"
      if not self.GGLabel:                      # Label does not exist yet
         self.GGLabel = ATOM3Integer()          # Label is an integer
      self.GGLabel.setValue(intValue)

  def showGGLabel(self, parent):
      "Returns a widget to edit the GGLabel field"
      if not self.GGLabel:                      # Label does not exist yet
         self.GGLabel = ATOM3Integer()          # Label is an integer
      return self.GGLabel.show(parent, None)

  def removeNode (self ):
      "removes specified node (removes itself from neighbors connections)"
      # walk through input connections and remove 'node' from each element
      for element in self.in_connections_:
         #todo: Existance check added by Denis, Aug 30 2005, was having problems in some GG rule
         if(self in element.out_connections_):
           element.out_connections_.remove(self)
         # now try and see if this object is in the other's named connector... (Added Oct 15, 2002)
         self.__removeFromNeighbourNamedConnectors(element)
      # walk through output connections and remove 'node' from each element
      for element in self.out_connections_:
         #todo: Existance check added by Denis, Aug 30 2005, was having problems in some GG rule
         if(self in element.in_connections_):
           element.in_connections_.remove(self)
         # now try and see if this object is in the other's named connector... (Added Oct 15, 2002)
         self.__removeFromNeighbourNamedConnectors(element)
         
      try:
        self.rootNode.listNodes[self.getClass()].remove(self)		# now remove itself from the list of nodes of the graph
      except:
        print "WARNING in ASGNode.removeNode():", self, "already removed from", self.rootNode.listNodes[self.getClass()]

           
      
  def __removeFromNeighbourNamedConnectors(self, element):
      """
         Method added: Oct 15 2002.
         Removes all the pointers to this objects from the named connectors of the objects "element"
      """
      for nh in element.graphObject_.namedConnectors.keys():         # walk through all the connectors
           nc = element.graphObject_.namedConnectors[nh]             # retrieve the connector name
           print "nc = ", nc, " element = ", element
           if nc in element.__dict__.keys():
             connections = element.getAttrValue(nc)                    # get the objects in that connector
           while self in connections:                                # while there are pointers to myself in the list...
             connections.remove(self)                          

  def doPrint(self):
      print "Type= ", self.getClass(), "(", self, ")"
      print "Value= ",
      for attr in self.generatedAttributes.keys():
          print self.getAttrValue(attr).toString(), " ",
      print " "
      # print connections...
      print "out connections= ",
      for con in self.out_connections_:
          print con, " , ",         
      print " "

  def doPrintM(self):
      self.doPrint()
      print "Matched=", self._matched

  def level(self ):
      " returns the hierarchy level in which node is"
      level = 0                     # the lowest level is the 0 (only ownd by the main root node)
      r = self.rootNode
      while r != None:              # go up trough the hierarchy
        r = r.rootNode
        level = level + 1
      return level         
         
  def hasGenerativeAttributes(self):
      "returns 1 if the entity has generative attributes, 0 otherwise"
      generativeAttributes = ["ATOM3Attribute", "ATOM3Appearance", "ATOM3Constraint", "ATOM3Cardinality"]
      for attribs in self.generatedAttributes.keys():               # for each attribute the node has...
          attr = self.generatedAttributes[attribs]                  # get its value
          if attr[0] in generativeAttributes: return 1              # it is a generative attribute    
          elif attr[0] == "ATOM3List":                              # this list may have geneartive attributes inside...
             # go until the basic type...
             btype = self.getAttrValue(attribs).itemType.__name__
             if btype in generativeAttributes: return 1             # found it!
      return 0

  def updateAppearanceAttributes(self):
      """
         If the entity has a keyword, calls the setValue method on all the attributes of type ATOM3Appearance.
         This method is called when the keyword of the entity is changed in it creation. The method updates all the
         ATOM3Appearance attributes.
      """
      if self.keyword_:
        for attr in self.generatedAttributes.keys():
          if self.generatedAttributes[attr][0] == 'ATOM3Appearance':
            attrib = self.getAttrValue(attr)
            attrib.setValue((self.keyword_.toString(), self))

#.......................................................................................
# The following functions are used in the children classes which are generated by AToM3
#.......................................................................................
  def show(self, parent, parentWindowInfo):
      """
         Shows the widget associated with each attribute of the object
      """
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      self.leftContainerFrame = Frame(self.containerFrame)
      self.rightContainerFrame = Frame(self.containerFrame)
      
      showCanvas = Canvas(self.leftContainerFrame, name = "editcanvas", 
                              borderwidth=0, 
                              relief=FLAT)
      
      showCanvasFrame = Frame(showCanvas)  
      canvasFrameHandler = showCanvas.create_window(0,0, 
                                              window=showCanvasFrame, anchor=NW)
    
      rowCount = 0
      for atr in self.realOrder:
         Label(showCanvasFrame, text=atr).grid(row=rowCount,column=0,sticky=W)
         if len(self.directEditing) >= rowCount+1 and self.directEditing[rowCount] == 0:    # Modified 13 Sept 2002
            #print "DIrect Editing == 0"
            exec 'Button( showCanvasFrame, text = "edit", command = lambda x=self : ' \
             + 'ATOM3TypeDialog(x.containerFrame, x.'+atr+') )' \
             + '.grid(row=rowCount,column=1,sticky=W)\n' 
         else: 
            #print "DIrect Editing == 1", self.directEditing, rowCount           
            self.getAttrValue(atr).show(showCanvasFrame, 
                        parentWindowInfo).grid(row=rowCount,column=1,sticky=W)
         ASGNode.setGGAnyWidget (self, showCanvasFrame, parentWindowInfo, atr, rowCount, 2)
         rowCount = rowCount + 1
      if not self.isSubclass( self, "ASG"):   # only show this widget if we are not a subclass of ASG
         ASGNode.editGGLabel(self, showCanvasFrame, parentWindowInfo, rowCount)
         
      showCanvas.scrollY = Scrollbar(self.rightContainerFrame, orient=VERTICAL)
      showCanvas['yscrollcommand'] = showCanvas.scrollY.set
      showCanvas.scrollY['command'] = showCanvas.yview
      
      showCanvas.scrollX = Scrollbar(self.leftContainerFrame, orient=HORIZONTAL)
      showCanvas['xscrollcommand'] = showCanvas.scrollX.set
      showCanvas.scrollX['command'] = showCanvas.xview
      
      showCanvas.pack(side="top", fill=BOTH, expand=1)
      showCanvas.scrollX.pack(side="top", fill=X, expand=1)
      showCanvas.scrollY.pack(side="left", fill=Y, expand=1)
      self.leftContainerFrame.pack(side="left", fill=BOTH, expand=1)
      self.rightContainerFrame.pack(side="left", fill=Y, expand=1)
      
      # This is the width, height that the canvas is using 'virtually'
      parent.update()
      vx = showCanvasFrame.winfo_width()
      vy = showCanvasFrame.winfo_height()
            
      if(vx > 800):
        showCanvas.configure(width = 800)
      else:
        showCanvas.configure(width = vx)
      if(vy > 440):
        showCanvas.configure(height = 440)
      else:
        showCanvas.configure(height = vy)        
        
      showCanvas.configure(scrollregion = (0, 0, vx, vy))
      self.__resizeInfo = [showCanvas, showCanvasFrame, parent]
      self.__resizeState = 0
      showCanvas.bind('<Configure>', self.resizeEvent)
            
      return self.containerFrame
      '''
      ATOM3Type.show(self, parent, parentWindowInfo)
      self.containerFrame = Frame(parent)
      rowCount = 0
      for atr in self.realOrder:
         Label(self.containerFrame, text=atr).grid(row=rowCount,column=0,sticky=W)
         if len(self.directEditing) >= rowCount+1 and self.directEditing[rowCount] == 0:    # Modified 13 Sept 2002
            #print "DIrect Editing == 0"
            exec "Button( self.containerFrame, text = 'edit', command = lambda x=self : ATOM3TypeDialog(x.containerFrame, x."+atr+") ).grid(row=rowCount,column=1,sticky=W)\n" 
         else: 
            #print "DIrect Editing == 1", self.directEditing, rowCount           
            self.getAttrValue(atr).show(self.containerFrame, parentWindowInfo).grid(row=rowCount,column=1,sticky=W)
         ASGNode.setGGAnyWidget (self, self.containerFrame, parentWindowInfo, atr, rowCount, 2)
         rowCount = rowCount + 1
      if not self.isSubclass( self, "ASG"):                                   # only show this widget if we are not a subclass of ASG
         ASGNode.editGGLabel(self, self.containerFrame, parentWindowInfo, rowCount)
      return self.containerFrame
    '''   
  def resizeEvent(self, event):
      """
      This is a very bad resize callback! I'm not proud of it, but it works 
      better than what it replaces... - Denis
      """
      if(self.__resizeState == 0):
         self.__resizeState += 1
         return
      elif(self.__resizeState == 1):
        self.__resizeState += 1
        return
      else:
         self.__resizeState = 0
      showCanvas, showCanvasFrame, parent = self.__resizeInfo
      parent.update()
      
      scrollbarSizeGuestimate = 50 # pixels
      vx = self.containerFrame.winfo_width() - scrollbarSizeGuestimate
      vy = self.containerFrame.winfo_height() - scrollbarSizeGuestimate
      showCanvas.configure(width = vx)
      showCanvas.configure(height = vy)
  
        

  def toString(self, maxWide = None, maxLines = None ):
      """
         Method returns a string with the object's value. If maxWide is specified and the string is greater
         than maxWide, then it is cutted to this value, adding a "..."
      """
    
      rs = "" 
      for atr in self.realOrder:
        rs = rs + self.getAttrValue(atr).toString()
        if atr != self.realOrder[len(self.realOrder)-1]: rs = rs+" "
      if maxWide and len(rs) > maxWide : return rs[0:maxWide-3]+'...'
      else: return rs

  def getValue(self):
      """
         Method gets the value of the object. Returns a tuple containing the value of each
         attribute of the object.
      """
     
      atrList = []
      for atr in self.realOrder:
         print 'atr is', atr, type(atr)
         atrList.append(self.getAttrValue(atr).getValue())
      return tuple(atrList)

  def setValue(self, value):
      """
         Method sets the value of the object. It receives a tuple containing the value of each
         attribute of the object.
      """
     
      count = 0
      for atr in self.realOrder:
         self.getAttrValue(atr).setValue(value[count])
         count = count + 1

  def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      """
         Method that writes into a file the constructor and the value of the object.
      """
      for atr in self.realOrder:
         self.getAttrValue(atr).writeConstructor2File(file, indent, objName+"."+atr, depth, generatingCode)

  def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):
      """
         Method that writes into a file the the value of the object.
      """
      for atr in self.realOrder:
         self.getAttrValue(atr).writeValue2File(file, indent, objName+"."+atr, depth, generatingCode)

  def invalid(self):
      """
         Returns 1 if the node has some invalid attribute, 0 otherwise
      """
      self.GGcheckSetNone()
      for atr in self.realOrder:
         if self.getAttrValue(atr).invalid(): return 1  
      return 0 

  def destroy(self):
      """
         Destroys the node, calling destroy on all its generated attributes...
      """
      self.GGcheckSetNone()
      for atr in self.realOrder:
         self.getAttrValue(atr).destroy()
      # Added 30 July 2002 by JL
      if self.isSubclass(self, "ASG"):			# call also destroy graphical things...
	self.destroyNodes()
      self.containerFrame = None

  def cloneActions(self, cloneObject):
      "clones the common attributes into cloneObject"
      cloneObject.graphClass_   = self.graphClass_
      cloneObject.graphObject_  = self.graphObject_
      cloneObject.rootNode      = self.rootNode
      cloneObject.objectNumber  = self.objectNumber
      import copy
      cloneObject.in_connections_  = copy.copy(self.in_connections_)
      cloneObject.out_connections_  = copy.copy(self.out_connections_)
      if self.GGLabel: cloneObject.GGLabel = self.GGLabel.clone()
      cloneObject.GGset2Any = self.GGset2Any
      cloneObject.editGGLabel = self.editGGLabel
      cloneObject.containerFrame= self.containerFrame

  def copy(self, other):
      "copies the common attributes from other into self"
      self.graphClass_      = other.graphClass_
      self.graphObject_     = other.graphObject_
      self.in_connections_  = other.in_connections_
      self.out_connections_ = other.out_connections_
      self.containerFrame   = other.containerFrame
      self.keyword_         = other.keyword_
      self.editGGLabel      = other.editGGLabel
      self.GGset2Any        = other.GGset2Any
      self.GGLabel          = other.GGLabel
      self.rootNode         = other.rootNode
      self.objectNumber     = other.objectNumber

  def preAction(self, actionID, * params):
      pass

  def postAction(self, actionID, * params):
      pass

  def preCondition(self, actionID, * params):
      pass

  def postCondition(self, actionID, * params):
      pass

  def isSubType(self, node):
      """
      Decides if self is a subtype of "node". That is, if it has at least the 
      same attributes as node and these attributes have same type (or are a 
      subtype), and may be more.
      
      Modified by Denis Dube, Aug 2006
      """

      for attr in node.generatedAttributes.keys():
        
        # Check if we at least have the same attribute names
        if( not self.generatedAttributes.has_key(attr)): 
          return 0
        
        # Check if attribute1 string is a subtype of attribute2 string
        # Example: myTypeInfo = ('ATOM3String', )
        myTypeInfo = self.generatedAttributes[attr]
        hisTypeInfo= node.generatedAttributes[attr]
        if(isSubTypeOfByDenis(myTypeInfo[0], hisTypeInfo[0]) == 0): 
          return 0 
        
        # Recursive attribute check, when myTypeInfo[0] == 'ATOM3List'
        # Example: myTypeInfo = ('ATOM3List', 'ATOM3Attribute')
        if(myTypeInfo[0] in ATOM3Type.recursiveTypes):
          # self must have at least those attributes that node has so...
          if(len(myTypeInfo) < len(hisTypeInfo)):
             return 0
          for i in range(1, len(hisTypeInfo)): # Already checked i == 0
            if(isSubTypeOfByDenis(myTypeInfo[i], hisTypeInfo[i]) == 0): 
              return 0 
            
      # Now check that if they have a keyword, it is the same...
      if(self.keyword_):
         if(node.keyword_):            # must be the same type and name
           # Only checking that type...this should be extended to check also the Name
           return isSubTypeOfByDenis(self.keyword_.getClass(), node.keyword_.getClass())  
         else: 
           return 1               # ok, we extend the node type with a keyword...
      elif(node.keyword_): 
        return 0    # we have "lost" the keyword, which is not allowed    
      return 1

    
# -------------- MODIFIED/CREATED by Denis Dube, Summer 2004 -----------------

  
  def genLayoutConstraintsCode( self,file, myName, indent):
    """ Generates code related to graphical layout constraints """
    
      
    file.write(indent+myName+'.layConstraints = dict() # Graphical Layout Constraints \n')
    
    lcDict = self.graphObject_.layConstraints
    
    # Links will have their layout constraints tucked away in the center object...
    if( isConnectionLink( self.graphObject_ ) ):      
      if( self.graphObject_.centerObject ):
        centerConstraints = self.graphObject_.centerObject.layConstraints

        # Add in the center object constraints 
        for key in centerConstraints:
          if( not lcDict.has_key( key ) ):
            lcDict[ key ] = centerConstraints[ key ]
          
          # Scaling of the arrow width doesn't exist, so we must want the center object scale
          elif( key == 'scale' ):
            lcDict[ key ] = centerConstraints[ key ]
            
          # Uh oh, conflict... just use one of them...
          else:            
            ## print "WARNING: Constraint conflict, see ASGNode.py in genLayoutConstraintsCode() if this is a problem."
            ## print lcDict, "<-- Object constraints"
            ## print centerConstraints, "<-- Center object constraints"
            ## print centerConstraints[ key ], "<-- Saved constraint (other one dropped)"
            lcDict[ key ] = centerConstraints[ key ]
      
    # Write down all the constraints...
    for key in lcDict.keys():
      file.write(indent+myName+'.layConstraints[\''+str(key)+'\'] = '+str(lcDict[key])+'\n' )

    
    
  def genAttributesCode(self, file, genGraphicalInfo = 1, objName = None, 
                        isMainModel = 1, rootNodeName = "rootNode", 
                        indent = '    ', genConstraints = 0, genSelf = 0, 
                        genGGcode = 0, parentName="self", genImport = 0, 
                        theDepth = 1, cautiousGenAttr = False ):
    """
    Generates code for the constructor and the attributes value
    """
    # generate the constructor call if the last argument is None
    if not objName:                                                                           # compose a name if not given
      if genSelf:
          myName = 'self.obj'+str(self.objectNumber)
      else:
          myName = 'obj'+str(self.objectNumber)
      # write code for the global preCondition evaluation, if genConstraints is set...
      if genConstraints and isMainModel :
          if( rootNodeName ):
            file.write( '\n'+indent+'self.globalPrecondition( '+rootNodeName+' )\n')
          #self.writeConstraint2File(file, indent, 'self.ASGroot', 'preCondition', 'ASG.CREATE')
      if genImport:                                                                          # Added 17 Sept 2002
        file.write( '\n'+indent+'from '+self.getClass()+' import '+self.getClass()+'\n')     # Added 17 Sept 2002
       # write constructor...
      file.write( '\n'+indent+myName+'='+self.getClass()+'('+parentName+')\n') 
      # Following two lines added by Denis, 2005 
      if( rootNodeName ):
        file.write( indent+myName+'.preAction( '+rootNodeName+'.CREATE )\n' )                
      self._generateHierarchicalFlagCode(file, indent, myName) # See HierarchicalASGNode.py
    else: myName = objName

    for attr in self.generatedAttributes.keys():  # for each generated attribute
        #print attr, self.getAttrValue(attr)
        file.write( '\n'+indent+'# '+attr+'\n' )
        if( cautiousGenAttr ):  
          file.write( indent+'try:\n' )
          indent += '    '
        # write its value to file
        self.getAttrValue(attr).writeValue2File ( file = file, indent = indent, 
              objName = myName+'.'+attr, depth = theDepth, generatingCode = 0) 
        if( cautiousGenAttr ):
          indent = indent[:-4]  
          file.write( indent+'except:\n' )                                          
          file.write( indent
                     +'    print "Root model attribute '+attr+' could not be '
                     +'loaded (most likely cause: the formalism it needs is '
                     + 'not open).\\n"\n' )                                          
      
    file.write( '\n' )
    
    # ey!, write GGLabel value (if appropriate)
    if self.GGLabel and (genGGcode == self.INLHS or genGGcode == self.INRHS):                 # if we are using the fields (we're defining a graph grammar rule)
      self.GGLabel.writeValue2File(file, indent, myName+'.GGLabel', 1)
    drawObject = 0

    if genGraphicalInfo:
      if self.graphClass_:                                                                   # check if the graphical class attribute has value
        if genImport:
          file.write( '\n'+indent+'from graph_'+self.getClass()+' import graph_'+self.getClass()+'\n')       # Added 17 Sept 2002    
        rootNodeName = str( rootNodeName )        
        # We probably didn't intend to ask for the rootNodes graphclass
        if( myName == rootNodeName ):
          file.write(indent+'# This is the rootNode, I really dont think we want to load a graphClass fort it...\n')
          file.write(indent+'try: '+myName+'.graphClass_= graph_'+self.getClass()+'\n')
          file.write(indent+'except: pass\n')
        else:
          file.write(indent+myName+'.graphClass_= graph_'+self.getClass()+'\n')
      if self.graphObject_:                                                                  # check if the graphical object attribute has value
        graphicalFile = 'graph_'+self.getClass()                                           # see if the graphical file exists...
        try:                                                                               # see if we have associated a graphical attribute
          fgd = open( graphicalFile+".py", "r+t")                                          # try to open the file with the graphical class
        except IOError:
          exists = 0
        else:
          fgd.close()
          exists = 1
        file.write(indent+'if '+parentName+'.genGraphics:\n')
        if not exists and self.isSubclass(self, 'ASG'):
            file.write(indent+'   new_obj = graph_ASG_ERmetaMetaModel('+str(self.graphObject_.x)+','+str(self.graphObject_.y)+','+myName+')\n')
        else: 
          self.graphObject_.writeConstructor2File (file, 'new_obj', indent+"   ", myName)
        if isMainModel:
            file.write(indent+'   new_obj.DrawObject(self.UMLmodel)\n')
            file.write(indent+'   self.UMLmodel.addtag_withtag("'+self.getClass()+'", new_obj.tag)\n')
            if self.graphObject_.ChangesAtRunTime:                                          # if the object changes at run-time, save its properties (Added 11-7-2002)
              self.graphObject_.write2File(file, indent+'   ')
        self.genLayoutConstraintsCode( file, 'new_obj', indent + '   ') # Added July 17,2004 by Denis Dube
        file.write(indent+'else: new_obj = None\n')
        file.write(indent+myName+'.graphObject_ = new_obj\n')

    # if genGGcode == 1, then we must generate code for the self.GGset2Any...
    if genGGcode == self.INRHS:
      ggcounter = 0
      for name in self.GGset2Any.keys():                                                     # iterate on all the attributes...
          nobjName = myName+str(ggcounter)
          file.write(indent+nobjName+"= AttrCalc()\n")
          self.GGset2Any[name].writeConstructor2File(file, indent, nobjName, 0, 0)             # write AttrCalc value or "set to Any"
          file.write(indent+myName+".GGset2Any['"+name+"']= "+nobjName+"\n")
          ggcounter = ggcounter + 1

    if not objName:
      if( not rootNodeName or rootNodeName == 'None' ): 
        rootNodeName = "rootNode"
      file.write('\n'+indent+'# Add node to the root: ' +rootNodeName + '\n' )
      file.write(indent+rootNodeName+'.addNode('+myName+')\n')
    if genConstraints and isMainModel:
      file.write(indent+'self.globalAndLocalPostcondition('+myName+', rootNode)\n')
      #self.writeConstraint2File(file, indent, 'self.ASGroot', 'postCondition', 'ASG.CREATE')
      #self.writeConstraint2File(file, indent, myName, 'postCondition', 'ASG.CREATE')

    # Following two lines added by Denis, 2006 
    # *** WARNING: Could adversely affect some formalisms ***
    if( rootNodeName ):
      file.write( indent+myName+'.postAction( '+rootNodeName+'.CREATE )\n' ) 

  
  def setGenValue(self, attribute, value ):
    """ 
    This will set the generated attribute value both semantically and graphically
    """
    # Valid attribute check
    if( not self.generatedAttributes.has_key( attribute ) ): 
      import Dialog
      myText = "Attribute "+str(attribute)+" not found in " \
               +str(self.generatedAttributes.keys())
      dialog = Dialog.Dialog(None, {'title': "ASGNode.setGenValue(attribute,value)",
                  'text': myText,
                  'bitmap': 'error',
                  'default': 0,
                  'strings': ('Print to console','Close')})
      if( dialog.num == 0 ): 
        # A traceback will make debuggin easier
        raise Exception, myText
      else:
        return
      
    # Update semantics
    attr = self.getAttrValue(attribute)
    attr.setValue( value )
    self.setAttrValue( attribute, attr )
    
    # Update graphics
    if( not self.graphObject_ ): return
    self.graphObject_.ModifyAttribute( attribute, value )
    
    

    
