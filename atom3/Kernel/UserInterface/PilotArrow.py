"""
PilotArrow.py

Keeps track of the interactively drawn temporary arrow while a connection
is being forged by the user.
The only concern here is the graphical representation of this imaginary arrow,
as it has no impact on the model itself.

Created by Denis Dube on June 16, 2004
"""


class PilotArrow:
  
  def __init__(self,canvas):
      
    self.dc = canvas
    
    self.arrow = None      # itemHandler                             
    self.objFrom = None    # Entity being connected from, graphical object reference
    self.tagFrom = None    # Entity being connected from, canvas tag
    
    self.namedPortSnapLock = False  # Prevent auto-snap on named ports
    
    self.smooth = False    # Should new arrows be smooth?
                  
    self.pilotArrowDone = False
                  
  def enteringArrowMode(self, atom3i ):
    """ Hack to break out of the arrow mode in the statechart """
    if( self.pilotArrowDone ):
#      atom3i.UI_scope.event("Reset")
      atom3i.UI_scope("Reset", None)
      self.pilotArrowDone = False        
                                                        
  def getArrow(self, create=True):
    if(self.arrow):
      return self.arrow
    elif(create):
      self.arrow = self.dc.create_line(0,0,0,0, arrow="last" ,
                                        width = 2,fill="orange",smooth=self.smooth,
                                        arrowshape = (15,15,3) )
      #UPDATE: Lowering it would place it under the snap grid...
      # Make it an under cover arrow... (below all other canvas items)
      #self.dc.tag_lower( self.arrow )
      return self.arrow         
    return None                           
  
  def removeArrow(self, arrowDoneFlag=True):
    """ Goodbye arrow... """
    self.dc.delete( self.arrow )
    self.arrow = None
    self.namedPortSnapLock = False
    self.pilotArrowDone = arrowDoneFlag   
    
        
  def setFromObject(self,obj):
    self.objFrom = obj
  def setFromTag(self,tag):
    self.tagFrom = tag
    
  def getFromObject(self):
    return self.objFrom
  def getFromTag(self):
    return self.tagFrom
  
  def getSnapLock(self):
    return self.namedPortSnapLock
  def setSnapLock(self, lockFlag ):
    """ True if not allowing auto-snap on the first object """
    self.namedPortSnapLock = lockFlag

  def toggleCreateSmooth(self):
    if( self.smooth ): self.smooth = False
    else: self.smooth = True  
    
  def getSmoothness(self):
    return self.smooth
  
  def rollbackArrow(self,eventPos):
    """ 
    Remove last point from the arrow or destroy the arrow completely
    Returns True if arrow has been destroyed 
    """
    coords = self.dc.coords(self.arrow)
    num = len( coords )
    
    if( num == 4 ):
      self.removeArrow()
      return True
    else:
      self.dc.coords( * [self.arrow ] + coords[:-4] + eventPos ) 
      return False
