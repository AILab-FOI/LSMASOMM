"""
SelectionBox.py

Interactive drawn selection box, has no meaning in terms of models.
Just a graphical helper.
This keeps track of its data.

Created by Denis Dube on June 16, 2004
"""

class SelectionBox:

  
  def __init__(self,canvas):
    
    self.dc = canvas
    self.selectionBox = None
    
    
  def setSelectionBox(self, color ):
    self.selectionBox = self.dc.create_rectangle(0, 0, 10, 10, 
                                    fill=color,
                                    stipple="gray12", width=1) 
  def getSelectionBox(self ):          
    return self.selectionBox     
  
  def removeSelectionBox(self):
    self.dc.delete( self.selectionBox )
    self.selectionBox = None
  
  