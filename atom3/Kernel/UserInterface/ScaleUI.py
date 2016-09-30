"""
ScaleUI.py

Constructs an interactive UI for scaling entities

Interactions with AToM3:
  CallbackState activates ScaleUI when the highlighter method is called
  Acquires UI_Statechart and CallbackState from a graphObject_ instance in the 
  selection dictionary.
  SelectBox.scaleHandler() and SelectBox.textScaleHandler() call UI_Statechart
  SelectBox.textScaleHandler() calls the CallbackState instance

By Denis Dube, April 3 2006
"""

from Tkinter import Button
import sys



class ScaleUI:
  
  UPDATE_INTERVAL = 300 # milliseconds
  
  def __init__(self, canvas):
    self.__selectionDict = []
    self.__dc = canvas
    self.__selectBox = None
    self.__wasActive = False
    
    
  def updateScaleUI(self, isActive, selectionDict):
    """
    Activates/De-Activates the scale UI widget
    Parameters:
      isActive: Boolean flag to activate/disable
      selectionDict: Dictionary of selected objects
    """
    self.__selectionDict = selectionDict
    # Remove selection box
    if(not isActive):
      self.__wasActive = False
      if(self.__selectBox != None):
        self.__selectBox.destroy()
      return
    elif(self.__wasActive and self.__selectBox):
      self.__selectBox.destroy()
  
    # Build the selection box
    if(len(selectionDict) > 0):
      self.__wasActive = True
      self.__selectBox = SelectBox(self.__dc, selectionDict)
      self.__autoUpdate()
    
      
  def __autoUpdate(self):
    """
    While the scale UI widget exists, continuously updates it at the specified
    time interval. 
    """
    if(self.__wasActive and self.__selectBox != None):
      self.__selectBox.update()
      self.__dc.after(ScaleUI.UPDATE_INTERVAL, self.__autoUpdate)
        
        
         
#===============================================================================
# Private class
#===============================================================================
         
class SelectBox:
  """
  SelectBox class should be considered "private" and is used entirely by 
  the ScaleUI class. It is responsible for the raw mechanics of actually
  drawing a box on the selected entities and dealing with user-input on the
  control points.
  """
  MIN_WIDTH = 30
  MIN_HEIGHT = 30
  
  def __init__(self, dc, selectionDict):
    self.__dc = dc
    self.__selectionDict = selectionDict
    self.__selectedEntityBoxDict = dict()
    

    for tag in selectionDict:            
      obj = selectionDict[tag][1]
      atom3i = obj.semanticObject.parent
      self.__UI_Statechart = atom3i.UI_Statechart
      self.__callbackState = atom3i.cb
      break
          
    bbox = getBoundingBox(selectionDict)
    minx, miny, maxx, maxy = bbox     
    
    # Put a box around the selection
    self.__selectionBoxHandler = self.__dc.create_rectangle(bbox, width=4, 
                                                    outline='green', dash=(4,4))
    
    # Define re-size entity buttons
    self.NW_button = Button(self.__dc, bg='SpringGreen')
    self.NE_button = Button(self.__dc, bg='SpringGreen')
    self.SW_button = Button(self.__dc, bg='SpringGreen')
    self.SE_button = Button(self.__dc, bg='SpringGreen')
    self.NW_button.pack()     
    self.NE_button.pack()     
    self.SW_button.pack()     
    self.SE_button.pack()    
    self.NW_button.bind('<Button-1>', self.scaleHandler)
    self.NE_button.bind('<Button-1>', self.scaleHandler)
    self.SW_button.bind('<Button-1>', self.scaleHandler)
    self.SE_button.bind('<Button-1>', self.scaleHandler)
    
    # Define re-size text buttons
    self.N_button = Button(self.__dc, font=("Times", 8, "bold"), text='T', bg='SpringGreen')
    self.E_button = Button(self.__dc, font=("Times", 8, "bold"), text='T', bg='SpringGreen')
    self.S_button = Button(self.__dc, font=("Times", 8, "bold"), text='T', bg='SpringGreen')
    self.W_button = Button(self.__dc, font=("Times", 8, "bold"), text='T', bg='SpringGreen')
    self.N_button.pack()     
    self.E_button.pack()     
    self.S_button.pack()     
    self.W_button.pack()    
    self.N_button.bind('<Button-1>', self.textScaleHandler)
    self.E_button.bind('<Button-1>', self.textScaleHandler)
    self.S_button.bind('<Button-1>', self.textScaleHandler)
    self.W_button.bind('<Button-1>', self.textScaleHandler)
     
    # Place the buttons on the canvas
    size = 10
    self.NW_window = self.__dc.create_window(minx, miny, width=size, height=size,
                                              window=self.NW_button)   
    self.NE_window = self.__dc.create_window(maxx, miny, width=size, height=size,
                                              window=self.NE_button)          
    self.SW_window = self.__dc.create_window(minx, maxy, width=size, height=size,
                                              window=self.SW_button)          
    self.SE_window = self.__dc.create_window(maxx, maxy, width=size, height=size,
                                              window=self.SE_button) 
     
    # Text re-size buttons
    widthOver2 = float(maxx - minx) / 2.0
    heightOver2 = float(maxy - miny) / 2.0
    self.N_window = self.__dc.create_window(minx + widthOver2, miny, 
                                            width=size, height=size,
                                            window=self.N_button)   
    self.E_window = self.__dc.create_window(maxx, miny + heightOver2, 
                                            width=size, height=size,
                                            window=self.E_button)          
    self.S_window = self.__dc.create_window(minx + widthOver2, maxy, 
                                            width=size, height=size,
                                            window=self.S_button)          
    self.W_window = self.__dc.create_window(minx, miny + heightOver2, 
                                            width=size, height=size,
                                            window=self.W_button)                                          
                                                       

    # Make individual elements of the selection obvious
    if(len(selectionDict) > 1):
      self.individualPackaging()




  def individualPackaging(self):
    """
    Give each element of the selection its own mini-box
    """
    for tag in self.__selectionDict:            
      obj = self.__selectionDict[tag][1]
      self.__selectedEntityBoxDict[tag] = self.__dc.create_rectangle(
                                                      obj.getbbox(), width=3, 
                                                   outline='green', dash=(2,2))
           
           
           
                                                    
  def destroy(self):
    self.__dc.delete(self.__selectionBoxHandler)
    self.__dc.delete(self.NW_window)
    self.__dc.delete(self.NE_window)
    self.__dc.delete(self.SW_window)
    self.__dc.delete(self.SE_window)
    
    self.__dc.delete(self.N_window)
    self.__dc.delete(self.E_window)
    self.__dc.delete(self.S_window)
    self.__dc.delete(self.W_window)
    
    for itemHandler in self.__selectedEntityBoxDict.values():
      self.__dc.delete(itemHandler)
    self.__individuallyPackagedList = dict()
    
    
    
    
  def scaleHandler(self, event=None):
    """ Activate the UI_Statechart to handle the reactive behaviour """
    self.__UI_Statechart.event('<KeyPress-r>', self)
    
    
    
  def textScaleHandler(self, event=None):
    """ Activate the UI_Statechart to handle the reactive behaviour """
    if(not self.__callbackState.isLabelDragMode()):
      self.__callbackState.toggleLabelDragMode()
      self.__UI_Statechart.event('<KeyPress-r>', self)
      self.__callbackState.toggleLabelDragMode()
    else:
      self.__UI_Statechart.event('<KeyPress-r>', self)
    
    
    
  def update(self):
    """
    After scaling, make sure the boxes & buttons are scaled too!
    """
    minx, miny, maxx, maxy = getBoundingBox(self.__selectionDict)
    
    self.__dc.coords(self.__selectionBoxHandler, (minx, miny, maxx, maxy))
    self.__dc.coords(self.NW_window, (minx, miny))
    self.__dc.coords(self.NE_window, (maxx, miny))
    self.__dc.coords(self.SW_window, (minx, maxy))
    self.__dc.coords(self.SE_window, (maxx, maxy))
    
    widthOver2 = float(maxx - minx) / 2.0
    heightOver2 = float(maxy - miny) / 2.0
    self.__dc.coords(self.N_window, (minx + widthOver2, miny))
    self.__dc.coords(self.E_window, (maxx, miny + heightOver2))
    self.__dc.coords(self.S_window, (minx + widthOver2, maxy))
    self.__dc.coords(self.W_window, (minx, miny + heightOver2))
    
    for tag in self.__selectedEntityBoxDict:            
      obj = self.__selectionDict[tag][1]
      try:
        self.__dc.coords(self.__selectedEntityBoxDict[tag], obj.getbbox())
      except:
        pass
  

#===============================================================================
# Non-class methods
#===============================================================================
      
def getBoundingBox(selectionDict):
  """
  Return the bounding box of the entities in a selectionDict
  The box is forced to be larger than a minumum width and height
  """
  minx, miny = sys.maxint, sys.maxint
  maxx, maxy = -(sys.maxint - 1), -(sys.maxint - 1)
  
  for tag in selectionDict:            
    obj = selectionDict[tag][1]
    box = obj.getbbox()
    
    if(minx > box[0]):
      minx = box[0]
    if(miny > box[1]):
      miny = box[1]
    if(maxx < box[2]):
      maxx = box[2]
    if(maxy < box[3]):
      maxy = box[3]
      
  # Force minimum width/height of the bbox
  width = maxx - minx
  if(width < SelectBox.MIN_WIDTH):
    temp = (SelectBox.MIN_WIDTH - width) / 2
    minx -= temp
    maxx += temp
  height = maxy - miny
  if(height < SelectBox.MIN_HEIGHT):
    temp = (SelectBox.MIN_HEIGHT - height) / 2
    miny -= temp
    maxy += temp
      
  return [minx, miny, maxx, maxy]