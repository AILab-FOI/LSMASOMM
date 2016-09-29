import Graphics

class GFVisitor:
  def __init__(self):
    raise NotImplementedError, "GFVisitor is an abstract class"
  
  def visitRectangle(self, rectangle):
      pass
  
  def visitOval(self, oval):
      pass
      
  def visitPolygon(self, polygon):
      pass
  
  def visitLine(self, polyline):
      pass
  
  def visitText(self, text):
      pass

  def visitImage(self, image):
      pass
  
  def visitConnector(self, connector):
      pass
  
  def visitComposite(self, composite):
      pass
    
  def visitAttribute( self, attribute):
      pass
    
  def visitNamedConnector( self, namedConnector):
      pass


# The colorVisitor methods changeFillColor or changeOutlineColor
# take as argument a GF object and the new color.
class ColorVisitor(GFVisitor):
    def __init__(self):
      pass
  
    def setFillColor(self, gfList, color):
      self.toChange = "fill"
      self.color = color
      self.undoList = []
      for gf in gfList:
        gf.accept(self)
      return self.undoList

    def setOutlineColor(self, gfList, color):
      self.toChange = "outline"
      self.color = color
      self.undoList = []
      for gf in gfList:
        gf.accept(self)
      return self.undoList

    def visitRectangle(self, gf):
      if self.toChange == "fill":
        self.visitFilledGF(gf)
      else:
        self.visitOutlinedGF(gf)
          
    def visitOval(self, gf):
      if self.toChange == "fill":
        self.visitFilledGF(gf)
      else:
        self.visitOutlinedGF(gf)
        
    def visitPolygon(self, gf):
      if self.toChange == "fill":
        self.visitFilledGF(gf)
      else:
        self.visitOutlinedGF(gf)

    def visitLine(self, gf):
      if self.toChange == "fill":
        self.visitFilledGF(gf) 

    def visitText(self, gf):
      if self.toChange == "fill":
        self.visitFilledGF(gf)
        
    def visitAttribute(self, gf):
      if self.toChange == "fill":
        self.visitFilledGF(gf)
        
    def visitComposite(self, gf):
      list = gf.getComponents()
      for gf in list:
        gf.accept(self)

    def visitFilledGF(self, gf):
        gfColor = gf.getFillColor()
        if gfColor != self.color:
          self.undoList.append((gf, gfColor))
          gf.setFillColor(self.color)

    def visitOutlinedGF(self, gf):
        gfColor = gf.getOutlineColor()
        if gfColor != self.color:
          self.undoList.append((gf, gfColor))
          gf.setOutlineColor(self.color)
      

# visitor to change the line width of a GF object. Takes different meaning
# depending on the specific type. setWidth takes as argument a GF object and the new color.
class WidthVisitor(GFVisitor):
  def __init__(self):
      pass

  def setWidth(self, gfList, width):
      self.width = width
      self.undoList = []
      for gf in gfList:
        gf.accept(self)
      return self.undoList

  def visitRectangle(self, gf):
    self.visitLinedGF(gf)
    
  def visitOval(self, gf):
    self.visitLinedGF(gf)

  def visitPolygon(self, gf):
    self.visitLinedGF(gf)

  def visitLine(self, gf):
    self.visitLinedGF(gf)

  def visitLinedGF(self, gf):
      gfWidth = gf.getWidth()
      if gfWidth != self.width:
        self.undoList.append((gf, gfWidth))
        gf.setWidth(self.width)

    
  def visitComposite(self, gf):
      componentList = gf.getComponents()
      for component in componentList:
          component.accept(self)


# visitor to change the outline/fill option on a GF object.
# change option takes as arguments the gf object and the new outline/fill option.
class OptionVisitor(GFVisitor):
  def __init__(self, editor):
      self.editor = editor

  def changeOption(self, gfList, option):
      self.outlineOption, self.fillOption = option
      # self.undoList is a list of pairs (gf, option)
      self.undoList = []
      for gf in gfList:
        gf.accept(self)
      return self.undoList

  def visitRectangle(self, gf):
      self.visitOutlinedGF(gf)

  def visitOval(self, gf):
      self.visitOutlinedGF(gf)
      
  def visitPolygon(self, gf):
      self.visitOutlinedGF(gf)
        
  def visitComposite(self, gf):
      componentList = gf.getComponents()
      for component in componentList:
          component.accept(self)

  def visitOutlinedGF(self, gf):
    gfOutlineOption = gf.getOutlineOption()
    gfFillOption = gf.getFillOption()
    if gfOutlineOption != self.outlineOption or gfFillOption != self.fillOption:
      self.undoList.append((gf, (gfOutlineOption, gfFillOption)))
      gf.setOutlineOption(self.outlineOption)
      gf.setFillOption(self.fillOption)


class EditHandlerVisitor(GFVisitor):
  def __init__(self, mainHandler):
      self.mainHandler = mainHandler

  def getEditHandler(self, gf):
      self.editHandler = None
      gf.accept(self)
      return self.editHandler

  def visitPolygon(self, polygonGF):
      self.editHandler = self.mainHandler.getPolygonEditHandler()

  def visitLine(self, polylineGF):
      self.editHandler = self.mainHandler.getLineEditHandler()
  
  def visitText(self, textGF):
      self.editHandler = self.mainHandler.getTextEditHandler()

  def visitImage(self, imageGF):
      self.editHandler = self.mainHandler.getImageEditHandler()
      
  def visitNamedConnector( self, namedConnectorGF ):
      self.editHandler = self.mainHandler.getNamedConnectorEditHandler()
   
  def visitAttribute( self, attributeGF ):
      self.editHandler = self.mainHandler.getAttributeEditHandler()
      

class CompositionVisitor(GFVisitor):
    def __init__(self, editor):
        self.editor = editor
        self.eventHandler = self.editor.getEventHandler()
   
    def decompose(self, gf):
        self.request = "decompose"
        self.componentList = []
        gf.accept(self)
        return self.componentList

    def isComposite(self, gf):
        self.request = "isComposite"
        self.composite = 0
        gf.accept(self)
        return self.composite

    def visitComposite(self, compositeGF):
        if self.request == "decompose":
            self.componentList = compositeGF.getComponents()
            componentListCopy = self.componentList[:]
            index = self.editor.removeGF(compositeGF)
            componentListCopy.reverse() # reverse the list to insert the components in order
            for component in componentListCopy:
                component.setEventHandler(self.eventHandler)
                self.editor.insertGF(index, component)

        elif self.request == "isComposite":
            self.composite = 1
            
