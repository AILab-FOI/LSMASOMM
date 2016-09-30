"""
UI_Scoping.py

Assumes we are using the built-in hierarchical system. If not, then the scoping
mechanism will always send events directly to the default UI statechart.
If we are using the hierarchical system, then events will be sent to the 
hierarchical node at the deepest level that bounds the event coordinates, and
if the event is not excplicitly handled, it will propagate upwards until the
default statechart handles it.

WARNING: This is a great deal of power. It is possible to get inconsistent
states if it is not used responsibly! (ie: If you have a default statechart
that can go to a dragging mode, and you have a lower level statechart that
"handles" the event that exits dragging mode, you will have a very unhappy
system...)

WARNING 2: Tkinter events are MULTI-THREADED. 
This means that if two events Ea and Eb come in, then x lines of code handling
Ea may get executed and then Eb will get handled and only then will Ea finish
it's remaining handler code. You were warned.

Denis Dube, Sept 2005
"""

from Tkinter import Event, TclError
import sys

from HierarchicalASGNode import HierarchicalASGNode


class UI_Scoping:

  def __init__(self, canvas, defaultStatechart):
    self.__dc = canvas
    self.__defaultChart = defaultStatechart
    
    self.__preChartList = []
    self.__postChartList = []
       
    self.__lockedStatechart = None
    
#===============================================================================
#  Public methods
#===============================================================================
  

    
    
  def addPostChart(self, postChart):
    """
    Use:
      Adds a global scope level statechart that can handle events after the 
      global default UI statechart is done with them.
      Why? So you at least know what has been done...
    """
    if(postChart not in self.__postChartList):
      self.__postChartList.append(postChart)
    else:
      print 'WARNING: attempted to add the same postChart twice', __file__
  
  
  
  def delPostChart(self, postChart):
    """
    Use:
      Deletes a global scope level post-statechart
    """
    if(postChart in self.__postChartList):
      self.__postChartList.remove(postChart)
    else:
      print 'WARNING: attempted to del a non-existing postChart', __file__
  


  def addPreChart(self, preChart):
    """
    Use:
      Adds a global scope level statechart that can handle events before the 
      global default UI statechart is done with them.
    """
    if(preChart not in self.__preChartList):
      self.__preChartList.append(preChart)
    else:
      print 'WARNING: attempted to add the same preChart twice', __file__
  
  
  
  def delPreChart(self, preChart):
    """
    Use:
      Deletes a global scope level pre-statechart
    """
    if(preChart in self.__preChartList):
      self.__preChartList.remove(preChart)
    else:
      print 'WARNING: attempted to del a non-existing preChart', __file__
      
      
      
      
  def releaseLock(self):
    """
    Use:
      Immediately releases the statechart lock (if any)
    """
    self.__lockedStatechart = None
    
    
      
#===============================================================================
#  Private methods  
#===============================================================================
    
  def __call__(self, keyName, event):
    """ 
    Use:
      Uses the coordinates the event occured to find a hierarchical node that
      bounds the location. If such a hierarchical node exists, it recursively
      walks the children to find more nodes. When done, UI statecharts are 
      extracted from each node, and starting from the deepest level node, we
      send the given keyName and event. If the statechart handles the event,
      then we stop. 
      
      If no statecharts handle the event, then global level statecharts are 
      tried. First, a list of filtering statecharts might be defined (these are 
      sent the event one by one). If none of these handle the event, it is 
      finally sent to the global default UI statechart.
    Parameters:
      keyName is the name of the user-input key, a string
      event is an object with lots of info, including coordinates,  generated
        by Tkinter when a keybind is triggered by the user
    Note: for those unfamiliar with __call__()
      self.ui_scope = UI_Scoping()  # Instantiate this class
      self.ui_scope(keyName, event) # <-- This calls this method
    """   
    #if(keyName != '<Any-Motion>'): print 'keyName:', keyName

    
    # The locked in statechart gets all events until it alters the event to
    # WARNING: An event *CAN* slip through here before the lock becomes active
    # This is a multi-threaded environment curtesy of Tkinter
    if(self.__lockedStatechart):
      event = self.__augmentEvent(event)
      self.__lockedStatechart.event(keyName, event)
      return # NOTE: Lock is released via releaseLock() method call
     
      
    # If it's a Tkinter event we need to convert x, y into canvas coords
    if( issubclass(event.__class__, Event)):        
      x = self.__dc.canvasx(event.x)
      y = self.__dc.canvasy(event.y)    
      
    # No event at all! The coordinates are not important then...
    elif(event == None):
      x = 0
      y = 0
      
    # Not a Tkinter event: expected to have x, y attributes in canvas coords
    else:
      x = event.x
      y = event.y 
      
    event = self.__augmentEvent(event)
      
    # Get the UI statecharts that will handle the event at the given coordinates
    scopedNodeQueue = []                                    
    for node in HierarchicalASGNode.hierarchicalTopLayer:
      obj = node.graphObject_
      if(obj):
        try:
          x0, y0, x1, y1 = obj.getbbox()
        except TclError: # Canvas not open (i.e. in closed a GG rule)
          continue
        if(x >= x0 and x <= x1 and y >= y0 and y <= y1):
          # This node completely bounds the event!
          scopedNodeQueue = \
                    self.__recursiveScopeWalker(x, y, node, scopedNodeQueue)
          break
          
    # Go through UI statecharts from deepest level to root
    scopedNodeQueue.reverse()
    for node in scopedNodeQueue:
      
      # Assumes the UI statechart attribute is exactly "UI_Statechart"
      if(node.__dict__.has_key('UI_Statechart')):        
        
        # Give the statechart a trigger 'keyName', as well as:
        # The actual event, with coordinates and a method that can be called 
        # back to tell us if the event was handled
#        if(keyName != '<Any-Motion>'):
#          print 'Event sent to node:', keyName
        node.UI_Statechart.event(keyName, event)  
                
        # Check if the statechart wants to take some special actions with regard
        # to the event. The statechart directly modifies the event attributes.
        
        # Lock all succeeding events to the current statechart.
        if(event._setStatechartLock):
          self.__lockedStatechart = node.UI_Statechart
          
        # Event handled by statechart hierarchy! Stop propagating event.
        if(event._isHandled):            
          return
    
    #if(keyName != '<Any-Motion>'): print 'Event sent to default statechart:', keyName
    
    # Send event to the pre-statecharts: these may observe the action that is
    # going to be taken by the default statechart and inform other statecharts 
    # of what will occur, or prepare them for it.
    for statechart in self.__preChartList:
      statechart.event(keyName, event)
    
    # Event not handled: send it to the global default statechart
    self.__defaultChart.event(keyName, event)  
    
    # Send event to the post-statecharts: these may observe the action taken by
    # the default statechart and inform other statecharts of what occured.
    for statechart in self.__postChartList:
      statechart.event(keyName, event)


  def __augmentEvent(self, event):
    """ 
    Augments the given event with some handy attributes 
    _isHandled --> Indicates that the last statechart to recieve this event has
                   dealt with it and that we can toss this event to dev/null now
    _setStatechartLock --> Indicates that the last statechart should recieve all
                           events from now on.
    """
    class NoneEvent:
      """ Default event when none exists... """        
      def __init__(self):
        self.x = 0
        self.y = 0
        self._isHandled = False 
        self._setStatechartLock = False
          
    # Create a new event
    if(event == None):
      return NoneEvent()
         
    # Modify existing event
    else:
      event._isHandled = False 
      event._setStatechartLock = False
      return event


  def __recursiveScopeWalker(self, x, y, node, scopedNodeQueue):
    """
    Use:
      If the given node has a child that bounds the x, y coordinates, then
      its UI_Statechart is added to stateChartScopeQueue, and if this child
      also has a child... recursion...
    Return:
      List of UI_Statecharts, in order of root level to deepest leaf
    Paramters:
      x, y coordinates (integer/float)
      node instance (ASGNode)
      stateChartScopeQueue, list of UI statecharts
    """
    scopedNodeQueue.append(node)    
    
    children = node.getHierChildren()
    if(children):
      for child in children:
        obj = child.graphObject_
        if(obj):
          x0, y0, x1, y1 = obj.getbbox()
          if(x >= x0 and x <= x1 and y >= y0 and y <= y1):
            # This node completely bounds the event!
            return self.__recursiveScopeWalker(x, y, child, scopedNodeQueue)
    
    return scopedNodeQueue
    
    