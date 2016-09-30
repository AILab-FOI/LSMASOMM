"""
ZoomFocus.py

Provides control of the canvas setup:
1. Zoom scales positions and entity sizes
2. Stretch scales positions only
3. Canvas size sets the maximum scrollable canvas region

Overhauled June 29, 2004 by Denis Dube
"""

from OptionDatabase   import OptionDatabase
from OptionDialog     import OptionDialog
from Utilities        import optimizeConnectionPorts

def applyLayout( atom3i ):
  """ 
  Applies a simple zoom & fit algorithm
  Expects the atom3 "self" as an argument
  """
  
  # Instantiate the layout algorithm, if not already done  
  if( ZoomFocus.instance == None ):
    ZoomFocus.instance = ZoomFocus( atom3i )      
  ZoomFocus.instance.main( atom3i )
  
def getZoom():  
  """ Returns the zoom factor on the current ZoomFocus instance """
  if( ZoomFocus.instance == None ):
      return 1.00
  else:
      return ZoomFocus.instance.getZoom()
  
    
class ZoomFocus:
  """
  Allows existing graphs to be scaled along both axis indepently,
  as well as fit everything on the canvas via an offset value.
  """
  
  instance = None
  
  ZOOM                = 'zoom'
  ZOOM_RESCUE         = 'zoomRescue'
  STRETCH_X           = 'strech x'
  STRETCH_Y           = 'strech y'
  CANVAS_X            = 'canvas x'
  CANVAS_Y            = 'canvas y'
  
  def __init__(self,atom3i ):
    
    self.atom3i = atom3i            # AToM3 instance
    self.dc = self.atom3i.UMLmodel  # Canvas
    
    # Last known zoom/stretch applied
    self.__lastZoom     = 100
    self.__lastStretchX = 100
    self.__lastStretchY = 100
    
    # Instantiate the Option Database module
    self.__optionsDatabase = OptionDatabase(self.atom3i.parent,
                        'Options_ZoomFocus.py', 'Zoom & Focus',autoSave=False)
    
    # Local methods/variables with short names to make things more readable :D
    newOp = self.__optionsDatabase.createNewOption
    IE  = OptionDialog.INT_ENTRY
    BE  = OptionDialog.BOOLEAN_ENTRY
    L  = OptionDialog.LABEL
    
    # Create New Options
    # Format: OptionKey, defaultValue, optionTuple, promptString, helpString
    newOp( 'WARNING', None, [L,"Times 12","red", "center" ],
          "WARNING: Zoom can cause graphical glitching (use rescue if stuck)", "" )
    text = """
If zoom causes your layout to disintegrate (particulary when save/loading) try:
  1) Control-A to select everything on the canvas
  2) R to initiate a resize
    2a) Right-click to set the default size
    2b) Left-click to accept re-size
  3) Spacebar to go to label (text) re-size mode
  4) Repeat step 2 (it will re-size text now)
  5) Save, restart AToM3, reload your model. 
"""
    newOp( self.ZOOM, 100, IE, "Zoom", text ) 
    text = """
Attempts to restore your model to normalacy after a bad experience with zoom
"""
    newOp( self.ZOOM_RESCUE, False, BE, "Zoom Rescue", text ) 
    newOp( self.STRETCH_X, 100, IE, "Stretch X", 
          "Model entities will have their positions scaled by the given amount" ) 
    newOp( self.STRETCH_Y, 100, IE, "Stretch Y", 
          "Model entities will have their positions scaled by the given amount" ) 
    newOp( self.CANVAS_X, atom3i.CANVAS_SIZE_TUPLE[2], IE, 
                  "Canvas max X", "Set the maximum scrollable canvas region" ) 
    newOp( self.CANVAS_Y, atom3i.CANVAS_SIZE_TUPLE[3], IE, 
                  "Canvas max Y", "Set the maximum scrollable canvas region" ) 
    
  
    # Load the options from the file, on failure the defaults will be returned.
    self.__optionsDatabase.loadOptionsDatabase()
    self.__processLoadedOptions()
    
  def __processLoadedOptions(self):
    """ After loading the database, have to get & store each option value """
 
    self.__zoom             = self.__optionsDatabase.get(self.ZOOM)
    self.__zoomRescue       = self.__optionsDatabase.get(self.ZOOM_RESCUE)
    self.__stretchX         = self.__optionsDatabase.get(self.STRETCH_X)
    self.__stretchY         = self.__optionsDatabase.get(self.STRETCH_Y)
    self.__canvasX          = self.__optionsDatabase.get(self.CANVAS_X)
    self.__canvasY          = self.__optionsDatabase.get(self.CANVAS_Y)
    
    
  def getZoom( self ):
      """ Return the zoom factor """
      return self.__zoom / 100.0 
  
    
  def main(self, atom3i ):
    
    # Configure it up
    if(not self.__optionsDatabase.showOptionsDatabase()):
      return # User cancelled the dialog
    self.__processLoadedOptions()
    
    # Rescue mode
    if(self.__zoomRescue == True):
      self.__optionsDatabase.set(self.ZOOM_RESCUE, False)
      for nodetype in atom3i.ASGroot.nodeTypes:  
        for node in atom3i.ASGroot.listNodes[nodetype]:
          obj = node.graphObject_
          if(obj.__dict__.has_key('centerObject')):
            obj = obj.centerObject
            
          # Just kill all layout info
          if(obj.__dict__.has_key('layConstraints')):
            for key in obj.layConstraints.keys():
              value = obj.layConstraints[key]
              if(type(value) == type(1) or type(value == type(0.1))):
                obj.layConstraints[key] = 0
              if(type(value) == type([1,2]) or type(value) == type((1,2))):
                obj.layConstraints[key] = []
                for item in value:
                  obj.layConstraints[key].append(0)                  
      return
          
    # Check if the canvas size has changed: if so apply the change
    x,y = [self.__canvasX,self.__canvasY]
    if( x != atom3i.CANVAS_SIZE_TUPLE[2] or y != atom3i.CANVAS_SIZE_TUPLE[3] ):
      if( x > 600 and y > 600 ):
        atom3i.CANVAS_SIZE_TUPLE = (0,0,x,y)
        atom3i.UMLmodel.configure( scrollregion=atom3i.CANVAS_SIZE_TUPLE )
    
    # No ASG? Halt!  
    if(not atom3i.ASGroot):
      return
      
    # Build a list of nodes
    Object.nodeList = []
    entityList = [] 
    for nodetype in atom3i.ASGroot.nodeTypes:	
      if( atom3i.ASGroot.listNodes.has_key( nodetype ) ):
        for node in atom3i.ASGroot.listNodes[nodetype]:
          if( node.isSubclass(node.graphObject_, "graphLink")):
            edgeObject( node, node.graphObject_.getCenterCoord() )          
          else:
            nodeObject( node, node.graphObject_.getCenterCoord() )
            entityList.append( node.graphObject_ )
          
    # Apply zoom factor (effect depends on previously applied zoom)
    realZoom = float(self.__zoom ) / float(self.__lastZoom)
    self.__lastZoom = self.__zoom 
    for node in Object.nodeList:
      node.zoomify( realZoom )
                        
    # Apply the stretch factor
    lsx, lsy = [ self.__lastStretchX ,self.__lastStretchY ]
    sx,sy = self.__lastStretchX, self.__lastStretchY  = [ self.__stretchX, self.__stretchY ]
    realStretch = [ float(sx ) / float(lsx), float(sy) / float(lsy) ]
    for node in Object.nodeList:
      node.scalePosition( realStretch )
                  
    # Commit zooming & stretching
    for node in Object.nodeList:
      node.commitMove()
                  
    # All that scaling & moving can mess up connections...
    optimizeConnectionPorts(atom3i, entityList)
 
class Object:
  
  nodeList = []
      
  def __init__(self, ASGnode, pos):   
    self.ASGnode = ASGnode
    self._pos = pos
    self._originalPos = pos
    nodeObject.nodeList.append( self )
    
  def getCoords(self):
    return self._pos
  
  def zoomify(self, zoom):
    """ Overide me """
    pass
  
  def scalePosition(self, scale):
    self._pos = [ self._pos[0] * scale[0], self._pos[1] * scale[1] ]

  def commitMove( self ): 
    """ Overide me """
    pass

class nodeObject(Object):
                                                      
  def __init__(self, ASGnode, pos):  
    self.graphObject = ASGnode.graphObject_
    if( not self.graphObject.layConstraints.has_key( 'scale' ) ):
      self.graphObject.layConstraints['scale'] = [1.00,1.00]
    if( not self.graphObject.layConstraints.has_key( 'Text Scale' ) ):
      self.graphObject.layConstraints['Text Scale'] = 1.00
    Object.__init__(self,ASGnode, pos)
                                                      
  def zoomify(self, zoom):
    self._pos = [ self._pos[0] * zoom, self._pos[1] * zoom ]
    #self.ASGnode.graphObject_.Scale( zoom,zoom, moveLinks=False )
    
    # Apply a Zoom to the Node Entity (preserving individual scale dimensions)
    sx, sy = self.graphObject.layConstraints['scale']
    newSx = sx * zoom
    newSy = sy * zoom
    self.graphObject.layConstraints['scale'] = [newSx,newSy]
    self.graphObject.Scale( newSx / sx, newSy / sy, moveLinks=False )
    
    # Apply a zoom to the Node Entity text
    st = self.graphObject.layConstraints['Text Scale']
    newSt = st * zoom
    self.graphObject.layConstraints['Text Scale'] = newSt
    self.graphObject.ScaleText( newSt )
    
    
  def commitMove( self ): 
    self.ASGnode.graphObject_.Move( self._pos[0] - self._originalPos[0],\
                                   self._pos[1] - self._originalPos[1]) 
    
class edgeObject(Object):
                                                      
  def __init__(self, ASGnode, pos):  
    self.graphObject = ASGnode.graphObject_.getCenterObject()
    if( self.graphObject ):
      if( not self.graphObject.layConstraints.has_key( 'scale' ) ):
        self.graphObject.layConstraints['scale'] = [1.00,1.00]
      if( not self.graphObject.layConstraints.has_key( 'Text Scale' ) ):
        self.graphObject.layConstraints['Text Scale'] = 1.00       
    Object.__init__(self,ASGnode, pos)
                                                      
  def zoomify(self, zoom):
    self._pos = [ self._pos[0] * zoom, self._pos[1] * zoom ]
    
    if( self.graphObject ):
      
      # Apply a Zoom to the Node Entity (preserving individual scale dimensions)
      sx, sy = self.graphObject.layConstraints['scale']
      newSx = sx * zoom
      newSy = sy * zoom
      self.graphObject.layConstraints['scale'] = [newSx,newSy]
      self.graphObject.Scale( newSx / sx, newSy / sy, moveLinks=False )
      
      # Apply a zoom to the Node Entity text
      st = self.graphObject.layConstraints['Text Scale']
      newSt = st * zoom
      self.graphObject.layConstraints['Text Scale'] = newSt
      self.graphObject.ScaleText( newSt )
    
  def commitMove( self ): 
    dx, dy = ( self._pos[0] - self._originalPos[0], self._pos[1] - self._originalPos[1] )
    self.ASGnode.graphObject_.setSelectAll()
    self.ASGnode.graphObject_.Move( dx,dy )
     
    