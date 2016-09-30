"""
CallbackState.py

Keeps track of useful data related to the graphical manipulation of objects
Provides methods to access and set this data
Provides some utility methods to act on the data

All data declared in the init statement should be considered private
Only methods inside this class have my blessings to directly manipulate this data

Created by Denis Dube on June 15, 2004
"""

import re, os, sys
from copy import copy as cloningMachine

from ModelSpecificCode    import isConnectionLink, isEntityNode
from FilePaths            import COPY_DIRECTORY 
from Cursors              import setCursor, setDefaultCursor
from ASGNode import ASGNode

from ATOM3Attribute import ATOM3Attribute        
from ATOM3Constraint import ATOM3Constraint     
from ATOM3Action import ATOM3Action    
from tkMessageBox import askyesno   

from ScaleUI import ScaleUI


class CallbackState:
  
 
  IDLEMODE         = "IDLEMODE"
  COPY_BUFFER_NAME = "copyBuffer.py"
  COPY_BUFFER_PATH = os.path.join(COPY_DIRECTORY, COPY_BUFFER_NAME) 
    
  def __init__(self, canvas, tag2ObjMap, windowRoot):
    
    self.windowRoot = windowRoot  # Tkinter root window instance
    self.dc = canvas              # Tkinter canvas widget instance
    self.tag2ObjMap = tag2ObjMap  # Mapping of tags to graphical objects
                                           
    self.selectionDict = dict()     # {tag : [itemHandler, Object] }
    self.selectionObjectSet = ()    # (obj, obj, ... )
    self.selectTuple = ()           # tuple of item handlers  (1,4,5,)
   
    self.lastClickCoord = [0, 0] # Co-ordinates of the last mouse click

    # Regular Expression Pattern: Obtains object number,segment type & number
    self.tagInfoPattern = re.compile('\AObj(\d+)(1|2)(?:st|nd)Seg(\d+)\Z')
      
    self.attributeCopy = None
    self.copyBufferInit = False
    
    self.dragLabelMode = False

    self.lastATOM3action = self.IDLEMODE
    
    self.__askAttributes = True
    
    self.__editStateTuple = (None, None) # Last object edited, and it's old state
           
    self.__scaleUI = ScaleUI(canvas)
           
  #------------------------ AToM3 Idle Mode Override ------------------------

  def setATOM3action(self, actionMode):
    self.lastATOM3action = actionMode 
  def getAction(self, action):
    if(action != self.IDLEMODE):
      self.lastATOM3action = action
    return self.lastATOM3action
  def isATOM3idle(self, mode):
    if(self.lastATOM3action == self.IDLEMODE and mode == self.IDLEMODE):
      return True
    elif(self.lastATOM3action == self.IDLEMODE):
      self.lastATOM3action = mode
      return False
    else:
      return False
    
  #-----------------------  Node VS Label drag modes -------------------------
    
  def isLabelDragMode(self):
    return self.dragLabelMode
  
  def toggleLabelDragMode(self):
    if(self.dragLabelMode): 
      self.dragLabelMode = False      
    else:                     
      self.dragLabelMode = True
    self.setLabelDragModeCursor() 
    
          
  def setLabelDragModeCursor(self):
    if(self.dragLabelMode): 
      setCursor(self.windowRoot, 'Drag Label')     
    # For some reason, this tends to bug out when exiting the Icon-Editor
    else:       
      try:
        setDefaultCursor(self.windowRoot)
      except:
        pass

  #------------------------------  Re-Size -----------------------------------
  
  def initReSizer(self):
    self.buildSelectionObjectSet()    
    # Re-Size is only valid if done on entities, so need at least 1 entity
    for obj in self.selectionObjectSet:
      if(isEntityNode(obj) or obj.getCenterObject()):
        self.reSizeAbort = False
        return
    self.reSizeAbort = True
  def enteringReSizer(self, atom3i):
    if(self.reSizeAbort):
      atom3i.UI_Statechart.event("Reset")

  #-----------------------  Regular Copy/Paste -------------------------------
  
  def initilizeCopyBuffer(self):
    self.copyBufferInit = True
  def isCopyBufferInitilized(self):
    return self.copyBufferInit

  #---------------------  Attributes Copy/Paste ------------------------------
  
  def isAttributesBufferInitilized(self):
    return self.attributeCopy != None
  
  def copyAttributes(self, node, unused):
    """ Stores the attributes of a node, nodetype is deprecated """
    
    # Name is usually a keyword, cardinality must not be copied in ER or CD
    doNotCopyList = ['cardinality', 'name']
                
    def getValueDict(self, doNotCopyList):     
      """ Obtain the node attributes in a dictionary """
      atrDict = dict()
      typeDict = dict()
      attributes = filter(lambda x: x not in doNotCopyList, self.realOrder)
      for atr in attributes:
        atrDict[atr] = self.getAttrValue(atr).getValue()
        typeDict[atr] = self.getAttrValue(atr).__class__.__name__
      return (atrDict, typeDict)
    
    def dict2String(self, atrDict, doNotCopyList):
      """ Display the dictionary in a nicely formatted fashion """
      s = ''
      attributes = filter(lambda x: x not in doNotCopyList, self.realOrder)
      for atr in attributes:
        value = str(atrDict[atr])
        if(len(value) > 70): 
          value = value[:67] + '...'
        s += str(atr) + ' : ' + value + '\n'
      return s
    
    self.attributeCopy = getValueDict(node, doNotCopyList)
    
#    import tkMessageBox
#    tkMessageBox.showinfo('Copying ' + node.getClass() , 
#                           'Copied attributes: \n' 
#                    + dict2String(node, self.attributeCopy[0], doNotCopyList))

    if(self.__askAttributes):
      self.__askAttributes = askyesno('Show Copy/Paste Dialogs?         ', 
                'Copying ' + node.getClass() + '\n\n' +
                'Copied attributes: \n\n' 
                + dict2String(node, self.attributeCopy[0], doNotCopyList))
           
    
  
  def pasteCompatibleAttributes(self, node, unused):
    """ Pastes stored attributes to a new node of the same type, 
    nodetype deperecated """
    if(not self.attributeCopy):            
      return 
      
    copiedAttributeDict = self.attributeCopy[0]
    copiedTypeDict = self.attributeCopy[1]
    notCopied = copiedAttributeDict.keys()
              
    # Dialog mode: badgers the user for exactly what it is they want to paste
    if(self.__askAttributes): 
      optDict = {'default':'no'}
      
      # Set the pasted attributes
      for atr in node.realOrder:
        if(copiedAttributeDict.has_key(atr)):
#          print 'copiedAttributeDict[atr]', copiedAttributeDict[atr]
          if(type(copiedAttributeDict[atr]) == type(list())):
            copyList = []
            for item in copiedAttributeDict[atr]:
              if(isinstance(item, ATOM3Attribute)):
                if(askyesno('Copy ATOM3Attribute?', 
                            item.getValue()[0], **optDict)):
                  copyList.append(item)
              elif(isinstance(item, ATOM3Constraint)):
                if(askyesno('Copy ATOM3Constraint?', 
                            item.getValue()[0], **optDict)):
                  copyList.append(item)
              elif(isinstance(item, ATOM3Action)):
                if(askyesno('Copy ATOM3Action?', item.getValue()[0], **optDict)):
                  copyList.append(item)
            node.getAttrValue(atr).setValue(copyList)
          
          else:
            if(askyesno('Copy AToM3 attribute?', str(atr), **optDict)):
              node.getAttrValue(atr).setValue(copiedAttributeDict[atr])
          notCopied.remove(atr)
          
    # No dialog mode: automatically pastes all compatible attributes
    else:
      for atr in node.realOrder:
        if(copiedAttributeDict.has_key(atr)):
          node.getAttrValue(atr).setValue(copiedAttributeDict[atr])
          notCopied.remove(atr)
        
    # Allow user to force copying of uncopied items...
    # Force is only permitted for attributes of the same type
    # However no checking is done for subtypes, so list actions == list text
    import Dialog     
    for atr in notCopied:
      forceChoiceStringList = ['-- Do Not Force --']
      sourceType = copiedTypeDict[atr]
      for nodeAtr in node.realOrder:        
        targetType = node.getAttrValue(nodeAtr).__class__.__name__
        if(sourceType == targetType):
          forceChoiceStringList.append(nodeAtr)

      dialog = Dialog.Dialog(self.windowRoot, {'title': 'Attribute mismatch', 
                          'text': 'Would you like to force copied attribute "'
                                  + atr + '" into:', 
                          'bitmap': '', 
                          'default': 0, 
                          'strings': forceChoiceStringList})
      # Set new name...
      if(dialog.num == 0):
        continue
      else:
        forcedAttribute = forceChoiceStringList[dialog.num]
        node.getAttrValue(forcedAttribute).setValue(copiedAttributeDict[atr])

          
    node.updateAppearanceAttributes()
    
    # Make sure the visual appearence is updated
    obj = node.graphObject_
    node.parent.editclass(0, 0, self.dc.find_withtag(obj.tag)[0])
#    for visualAttr in obj.attr_display.keys():       
#        obj.ModifyAttribute(visualAttr, 
#                            node.__dict__[visualAttr].toString(25, 5))
  
   
  
  # ----------------------------  Canvas Stuff -------------------------------
    
  # Tkinter canvas widget
  def getCanvas(self):
    return self.dc  
  # Canvas Coordinate converter
  def getCanvasCoords(self, event):
    self.lastClickCoord = [self.dc.canvasx(event.x), self.dc.canvasy(event.y)]
    return self.lastClickCoord
  def convertRootToCanvasEvent(self, event):
    """ Necessary offsets for binds made to the root window instead 
    of the canvas """
    # Commented out an older and less reliable method
    #event.x -= (self.dc.winfo_rootx() - self.windowRoot.winfo_rootx() )
    #event.y -= (self.dc.winfo_rooty() - self.windowRoot.winfo_rooty() )     
    event.x = event.x_root - self.dc.winfo_rootx()
    event.y = event.y_root - self.dc.winfo_rooty()
    return event      
  # Mouse click tracker
  def getLastClickCoord(self):
    return self.lastClickCoord
  def setLastClickCoords(self, pos):
    self.lastClickCoord = pos
  def getLastClickCoordInRootCoords(self):
    x, y = self.lastClickCoord
    x += (self.dc.winfo_rootx() - self.windowRoot.winfo_rootx())
    y += (self.dc.winfo_rooty() - self.windowRoot.winfo_rooty()) 
    return [x, y]
    
  # --------------------------- Selection Dictionary --------------------------
  
  # Tags to object mapping
  def getTag2ObjMap(self):
    return self.tag2ObjMap
  
  # Selection Dictionary Method. selectionDict() = {tag : [itemHandler, Object] }
  def clearSelectionDict(self):
    self.highlighter(0)
    self.selectionDict = dict() 
  def getSelectionDict(self):
    return self.selectionDict
  def isLastSelectionEmpty(self):
    return len(self.selectionDict) == 0
    
  def buildSelectionObjectSet(self):
    """ Builds a non-duplicating set of objects from the selection dictionary """
    self.selectionObjectSet = ()
    for tag in self.selectionDict:
      obj = self.selectionDict[tag][1]
      if(obj not in self.selectionObjectSet):
        self.selectionObjectSet += (obj,)
    return self.selectionObjectSet
  def getSelectionObjectSet(self):
    return self.selectionObjectSet      
      
  #---------------------- Temporary Selection -------------------------------
  
  # Selection Tuple Methods 
  def clearSelectionTuple(self):
    self.selectTuple = () 
  def appendSelectionTuple(self, itemHandlers):
    if(type(itemHandlers) == type(tuple())):
      self.selectTuple += itemHandlers
    else:
      self.selectTuple += (itemHandlers,)
  def getSelectionTuple(self):
    return self.selectTuple
  
  # Just to be 100% safe, with this you can use the temporary selection mechanism
  # and have no worries :D
  def backupSelectionTuple(self):
    self.backupSelTuple = cloningMachine(self.selectTuple)
  def restoreSelectionTuple(self):
    self.selectTuple = self.backupSelTuple

  # ------------------------- Utility Methods --------------------------------
  
  def highlighter(self, flag):
    """ Highlights all objects in the selectionDict with the flag """
    self.__scaleUI.updateScaleUI(flag, self.selectionDict)
#    for tag in self.selectionDict:            
#      obj = self.selectionDict[tag][1]
#      obj.setSelectAll()  
#      obj.HighLight(flag)
#      
  
  def isObjectInSelectionDict(self, obj):
      return self.selectionDict.has_key(obj.tag)
  
  def updateSelectionDict(self, selected, ignoreConditionsActions=False):
    """ Add itemHandlers in selected to the selectionDict """
    
    for itemHandler in selected:
      tags = self.dc.gettags(itemHandler)
      if(tags and not self.selectionDict.has_key(tags[0])):
        # Add dictionary entry: {tag : [itemHandler, Object] }
        if(self.tag2ObjMap.has_key(tags[0])):
          obj = self.tag2ObjMap[tags[0]]
          self.selectionDict.update({tags[0]: [itemHandler, obj] })
                    
          # postconditions and postactions      
          semanticObj = obj.semanticObject  
          if(not semanticObj): 
            continue            
          if(ignoreConditionsActions): 
            continue
          
          res = semanticObj.postCondition (ASGNode.SELECT)
          if res:
            self.constraintViolation(res)
            continue            
          semanticObj.postAction (ASGNode.SELECT)
      
      
  def deleteFromSelectionDict(self, selected):
    """ Removes the selected items from the selectionDict and 
    un-highlights them """
    
    dc = self.getCanvas()
    fullSelection = self.selectionDict.copy()  
    
    # Find all the objects to be deleted given a list of itemHandlers
    objDeletionList = []
    for tag in fullSelection:
      for itemHandler in selected:
        sTag = dc.gettags(itemHandler)
        if(sTag and tag == sTag[0]):
          objDeletionList.append(fullSelection[tag][1])
          break
          
    # Find all entries in the selectionDict that have this obj 
    # (could be multiple entries)
    for tag in fullSelection:
      for obj in objDeletionList:
        if(fullSelection[tag][1] == obj):        
          obj.setSelectAll()        
          obj.HighLight(0)  
          if(self.selectionDict.has_key(tag)):
            del self.selectionDict[tag]  # Remove from selection dict
          break
          
          
  def getItemUnderCursor(self, atom3i, event, ignore = None, allTags = False):
    """ Returns an itemHandler,tag,obj tuple if there is an item at the event """
    
    x, y = self.getCanvasCoords(event)   # Event coordinates
    itemHandler = atom3i.find_visible_closest(x, y, self.dc, limit=20, 
                                              ignore=ignore)	
    
    if(itemHandler and itemHandler[0] != -1):
      tags = self.dc.gettags(itemHandler[0])  
      if(tags):
        if(self.tag2ObjMap.has_key(tags[0])):
          obj = self.tag2ObjMap[ tags[0] ]  
          if(allTags): 
            return (itemHandler[0], tags, obj)
          return (itemHandler[0], tags[0], obj)
    return ()
    
    
  '''
  On mouse button 1, fresh selection is triggered with this action code:
    
  event = eventhandler.get_event_params()
  
  cb.clearSelectionTuple()
  startNewSelectionBox(atom3i,event , "yellow")
  
  cb.highlighter( 0 ) 
  cb.clearSelectionDict()     
  
  # Item under cursor, make sure it's in the selection
  cb.appendSelectionTuple( cb.getItemUnderCursor( atom3i, event)[0]  )
  
  setCursor( atom3i.parent, 'Selection' )
  '''

  
  def isItemUnderCursorSelected(self, atom3i, event):
    """ 
    Returns true if there is an item under the cursor that is already in
    the selection dictionary
    """   
    x, y = self.getCanvasCoords(event)   # Event coordinates
    itemHandler = atom3i.find_visible_closest(x, y, self.dc, limit=20, 
                                              ignore=None)	
    if(itemHandler and itemHandler[0] != -1):
      tags = self.dc.gettags(itemHandler[0])  
      if(tags):
        if(self.selectionDict.has_key(tags[0])):
          return True
    return False
  
  def isItemUnderCursorUnselected(self, atom3i, event, whoami='N/A'):
    """ 
    Returns true if there is an item under the cursor that is not already in
    the selection dictionary
    """
    x, y = self.getCanvasCoords(event)   # Event coordinates
    itemHandler = atom3i.find_visible_closest(x, y, self.dc, limit=20, 
                                                ignore=None)	
    if(itemHandler and itemHandler[0] != -1):
      tags = self.dc.gettags(itemHandler[0])  
      if(tags):
        if(self.tag2ObjMap.has_key(tags[0])  and not
            self.selectionDict.has_key(tags[0])):
          return True
    return False
  
  def isNoItemUnderCursor(self, atom3i, event):
    """ Returns true if no item under the cursor """
    x, y = self.getCanvasCoords(event)   # Event coordinates
    itemHandler = atom3i.find_visible_closest(x, y, self.dc, limit=20, 
                                              ignore=None)	
    if(itemHandler and itemHandler[0] != -1):
      tags = self.dc.gettags(itemHandler[0])  
      if(tags):
        if(self.tag2ObjMap.has_key(tags[0])):
          return False
    return True
        
  def isItemVisible(self, itemHandler):
    """ Returns true if the item can be visibily seen on the canvas """
    dc = self.dc
    itemtype = dc.type(itemHandler)
    
    # Images
    if(itemtype == 'image'): 
      return True
      
    # Line/Text uses the fill attribute to be visible
    elif(itemtype in ['line', 'text']):
      if(dc.itemcget(itemHandler, "fill") in ["", None]):
        return False
      return True
      
    # Windows (widgets)
    elif(itemtype == 'window'):
      return False
    
    # Anything else: polygon, etc. 
    else:
      if(dc.itemcget(itemHandler, "outline") in ["", None] 
        and dc.itemcget(itemHandler, "fill") in ["", None]): 
        return False
    return True
        
    
  def smoothSelected(self):
    """ Toggle smooths all links in the selection, toggles via majority vote """
    
    howManySmoothOnes = 0
    itemHandlers = []
    smoothFlag = True
    
    # Gather Statistics on what's smooth and what's not :D
    for tag in self.selectionDict:
      obj = self.selectionDict[tag][1]
      if(isConnectionLink(obj)):  
        for connObjTuple in obj.in_connections_ + obj.out_connections_:
          itemHandler = connObjTuple[0]
          itemHandlers.append(itemHandler)
          if(self.dc.itemcget(itemHandler, "smooth") != "0"):
            howManySmoothOnes += 1

    # Most of them are already smooth, so un-smooth them
    if(howManySmoothOnes != 0 
        and float(len(itemHandlers)) / float(howManySmoothOnes) > 0.5):
      smoothFlag = False
      
    # Apply the smoothness to the items...
    for itemHandler in itemHandlers:
      self.dc.itemconfigure(itemHandler, smooth = smoothFlag)
        
  def getSegmentTagInfoTuple(self, tag):
    """ 
    Given a segment tag such as: "Obj331stSeg10" or "Obj42ndSeg0" 
    Get the obj number: 33, 4 
    Get the type: 1st, 2nd 
    Get the segment number: 10, 0 <-- It will be 0 unless its a hyperedge
    """
    
    # Do a regular expression search on the tag
    match = self.tagInfoPattern.search(tag)    
    if(not match): 
      return None
    
    # Convert the matched object to integers...
    objNumber = int(match.group(1))
    segmentType = int(match.group(2))
    segmentNum = int(match.group(3))
    
    return (objNumber, segmentType, segmentNum)

  def findItemHandlerWithTag(self, tag):
    """ 
    Returns the itemHandler associated with the tag & 
    checks if the tag is mapped to an object 
    """
    itemHandler = self.dc.find_withtag(tag) 
    if(not itemHandler):
      raise Exception, "Itemhandler for tag "  + str(tag) + " not found!"
    elif(not self.tag2ObjMap.has_key(tag)):    
      raise Exception, "Tag not found for itemHandler " + str(itemHandler) 
    return itemHandler[0]
  
  
  def getOverlappedItemUnderCursor(self, atom3i, event, 
                                              title = 'Select Object To Drag'):
    """ 
    Allows precise selection of objects when they are overlapping and initiates
    a drag operation to allow the user to seperate the mess apart 
    """
    
    canvas = self.getCanvas()
    cb = self  # Callback state
    x, y = self.getCanvasCoords(event)   # Event coordinates
    
    # Find the overlapping entities
    limit = 30
    itemsTuple = canvas.find_overlapping(x-limit, y-limit, x+limit, y+limit) 
    if(not itemsTuple or itemsTuple[0] == -1): 
      return
    itemDict = dict()
    for itemHandle in itemsTuple:
      tags = canvas.gettags(itemHandle) 
      # Check if one of the tags is 'current', if so short-circuit
      if('current' in tags):
        cb.clearSelectionDict()
        cb.updateSelectionDict([itemHandle, ])
        cb.highlighter(True)
        return True 
      
      # Create a dict entry with Key: Obj, Value: [item#, tags] 
      if(tags and cb.tag2ObjMap.has_key(tags[0])):
        obj = cb.tag2ObjMap[ tags[0] ]
        itemDict[obj] = [ itemHandle, tags  ] 
    
    # Prepare a list of Entities for the user to choose
    stringList = []
    stringIndexToObjMap = []
    namelessTuple = []
    from ATOM3String import ATOM3String
    for obj in itemDict.keys():
      itemHandle, tags = itemDict[obj]
      if(not self.isItemVisible(itemHandle)):  # is it visible? Do we care?
        continue
            
      # Go through all the attributes to find something distintive
      item = ''
      for attr in obj.semanticObject.getAttributes():
        attrValue = obj.semanticObject.getAttrValue(attr)  
        # String attribute... excellent      
        if(attrValue.__class__.__name__ == ATOM3String.__name__):
          valueString = attrValue.getValue().strip('\n')
          if(valueString == ''):
            continue
          else:
            item = valueString
            # Oooh, it's a name/Name attribute, very distinctive
            if(attr.upper() == 'NAME'):
              break
      if(item):
        stringList.append(item)
        #stringList.append( canvas.itemcget( item, 'text' ) )     
        stringIndexToObjMap.append(obj)
      
      # Couldn't find a distintive attribute... just use the obj tag :(
      else: 
        superTag = ''
        for tag in tags:
          superTag += tag + '_'
        namelessTuple.append([obj, superTag[:-1] ])
      
    # Put the 'nameless' ones at the top
    for obj, string  in namelessTuple:
      stringList = [string] + stringList
      stringIndexToObjMap = [ obj ] + stringIndexToObjMap

    # Display the choices
    if(len(stringList) == 0): 
      index = 0
    elif(len(stringList) == 1): 
      index = 1
    else:
      index = atom3i.popupMenuCreator.listChoicePopup(title, stringList)
    
    # Apply the choice
    if(index == 0): 
      return False
  
    obj = stringIndexToObjMap[index-1] 
    itemHandle, tags = itemDict[obj]
    cb.clearSelectionDict()
    cb.updateSelectionDict([itemHandle, ])
    cb.highlighter(True)
    return True
  
  
  def initMatchChoice(self, value, matchList):
    self.matchChoiceIs = value
    self.matchListIs = matchList
    
  def getMatchChoice(self):
    return self.matchChoiceIs
  
  def setMatchChoice(self, atom3i, event):          
    itemTuple = self.getItemUnderCursor(atom3i, event)
    if(itemTuple):
      itemHandle, tag, obj = itemTuple
      if(obj.semanticObject):
        semanticObject = obj.semanticObject
        
        matchIndex = 0
        for match in self.matchListIs:
          num, objList = match    
          for obj in objList:
            if(obj == semanticObject):
              self.matchChoiceIs = matchIndex
              return 
          matchIndex += 1
    self.matchChoiceIs = None


    
  def setEditState(self, semObj, oldSemObj):
    """ This is set by ATOM3.editclass() """
    self.__editStateTuple = (semObj, oldSemObj)
  
  def getEditState(self):
    """ This is called by formalisms after an edit occured """
    return self.__editStateTuple
    