# __ File: GraphicalForm.py __________________________________________________________________________________________________
#  Implements  : class GraphicalForm
#  Author      : Juan de Lara
#  Description : A wrapper to Canvas objects. It is used when posing graphical constraints
#  Modified    : 23 Oct 2001
#  Changes :
#   - 14  Nov 2001 : Added methods setFill() and setSmooth() (copied from the old version of ATOM3)
#   - 24  July 2002: Corrected bug in setVisible()
#   - 30  July 2002: (Ernesto) Corrected bug in setVisible(), only make something invisible if it is not invisible yet.
#   - 08  April 2003: (Juan) Added methods lift and lower
# ____________________________________________________________________________________________________________________________

from Tkinter import *
import cmath, math

from line                       import *
from oval                       import *
from rectangle                  import *
from polygon                    import *
from text                       import *
from image                      import *

class GraphicalForm:
    # a useful constant set
    fillForms = ['line', 'text'] 	# These forms use fill instead outline
    anchorForms = [ 'text', 'image' ]
    rotationForms = ['line', 'polygon']
    validAnchors = [ 'nw', 'ne', 'sw', 'se', 'n', 'w', 'e', 's', 'center' ]

    def __init__(self, canvas, handler, name, imageFilename = None, fontObject = None ):
        "Constructor, takes a canvas and the handler to be wrapped as well as the name assigned to the object"
        self.handler        = handler                                          	# The handler of the associated drawing
        self.canvas         = canvas						# The canvas in which the element is being drawn
        self.name           = name						# its name
        self.drawingHandler = None						# The handler of the text
        self.elementType    = self.canvas.type(self.handler)			# store the element type
        self.hidden         = 0                                                 # flag that indicates if the element is hidden
        
        self.isImage        = False
        self.imageFilename  = imageFilename
        
        self.fontObject     = fontObject
        if( fontObject ):
          self.fontSize     = fontObject.cget( 'size' )
        else:
          self.fontSize     = None
                    
        if self.elementType in self.fillForms:                          	# store the element color
           self.Color = self.canvas.itemcget(self.handler, "fill")
           self.bgColor = None
        elif self.elementType == 'image':
           self.bgColor = 'black'
           self.Color = 'black'
           self.isImage = True
           if( self.imageFilename == None ):
               raise Exception, "Image graphical form is missing the imageFilename attribute"
        else:
           self.bgColor = self.canvas.itemcget(self.handler, "fill") 
           self.Color = self.canvas.itemcget(self.handler, "outline")
        self.antColor = self.Color    # Remember last color for HighLighting
                                
        # Polygons & lines rotation initial angle: assumed to be 90 degrees
        self.lastAngle = math.pi / 2 # Radians


    def getImageFilename( self ):
        return self.imageFilename
    
    def getFontSize( self ):
        return self.fontSize
           
    def getFontMetric( self ):
        if( not self.fontObject ): return
        return self.fontObject.metrics("linespace")
      
    def getBbox( self ):
        return self.canvas.bbox( self.handler )
      
    def getFontMeasure( self, text ):
        """ 
        Get size of font given a line of text and the font type 
        Unfortunately, the font measure method is not precise, so you need to 
        multiply by a fudge factor, which I've determined to be 1.15 - Denis
        """
        #x,y,w,h = self.canvas.bbox( self.handler )
        #print 'BBOX', x,y, w-x,  h-y
        #print 'COORDS',  self.canvas.coords( self.handler )
        #print 'Metric',  self.fontObject.metrics("linespace")
        #print 'Actual',  self.fontObject.actual() 
        #self.canvas.create_rectangle( x,y,x+(w-x), y-(h-y) )
        
        if( self.fontObject ):
          # The following lines let you debug the fudge factor
          #x,y = self.canvas.bbox( self.handler )[:2]
          #w = self.fontObject.measure( text ) * 1.15
          #self.canvas.create_rectangle( x,y,x+w,y-28 ) 
          return self.fontObject.measure( text )
    
    def getFont( self ):
        return self.fontObject
      
    def refreshFont( self ):
        if( self.fontObject ):
            self.canvas.itemconfig(self.handler, font=self.fontObject)
            
    def setAnchor( self , anchorString = 'center' ):
        """ Allows anchor to be set at run-time, with valid Tkinter anchor string """
        if( self.elementType in self.anchorForms ):
            if( anchorString in self.validAnchors ):
                self.canvas.itemconfigure( self.handler, anchor=anchorString )
            
    def getHandler( self ):
        return self.handler
    
    def getName( self ):
        return self.name
     
    def lift(self):
        "Moves the item to the top of the canvas stack"
        #self.canvas.lift(self.handler)
        # Canvas lift is deprecated...
        self.canvas.tag_raise(self.handler)
        

    def lower(self):
        "Moves the item to the bottom of the canvas stack"
        #self.canvas.lower(self.handler)        
        # Canvas lower is deprecated...
        self.canvas.tag_lower(self.handler)        

    def setCoords(self, coords):
        "sets the coordinates of the handler"
        arg = [self.handler]                    # Put all arguments in a list
        for c in coords: arg.append(c)
        apply(self.canvas.coords, arg)          # apply the function

    def getCoords(self):
        "gets the coordinates of the handler"
        return self.canvas.coords(self.handler)

    def setFill(self, color, stealth=False):
        "sets the color of the shape (color is a string)"
        if( self.isImage ): return 
        self.canvas.itemconfigure( self.handler, fill=color)
        if(not stealth):
          self.Color = color

    def setOutline(self, color):
        "sets the colour of the outline shape (color is a string)"
        if( self.isImage ): return 
        self.canvas.itemconfigure( self.handler, outline=color)   
        
    def setStipple(self, stippleString, outline=False):
      """ Sets the stippling of the shape """
      if( self.isImage ): return 
      if(outline):
        self.canvas.itemconfigure( self.handler, outlinestipple=stippleString)  
      else:
        self.canvas.itemconfigure( self.handler, stipple=stippleString)  

    def setWidth(self, width):
      if( self.isImage ): return 
      self.canvas.itemconfigure( self.handler, width=width)  

    def setSmooth(self, flag):
        "sets the color of the shape (color is a string)"
        if( self.isImage ): return 
        self.canvas.itemconfigure( self.handler, smooth=flag)

    def setColor(self, color):
        "sets the color of the shape (color is a string)"
        if( self.isImage ): return 
        if self.elementType in self.fillForms:
            self.canvas.itemconfigure( self.handler, fill=color)
        else:
            self.canvas.itemconfigure( self.handler, outline=color)
        self.Color = color

    def HighLight(self, flag = 1):
        "Highlights (flag = 1) or LowLights (flag = 0) the element if it is not hidden"
        if( self.isImage ): return 
        if not self.hidden:                     # Change color only if item is visible
           if flag:                             # Highlights element (draws it with green color)
              if( self.Color != 'green' ):
                self.antColor = self.Color        # Store current color
              self.setColor('green')            # set new color to green
           else:                                # Lowlights the element (back to previous color)
              self.setColor(self.antColor)

    def showName(self, event):
        "prints the name in the drawing. This is a callback function invoked when <ENTER>"
        if self.drawingHandler:
           self.canvas.delete(self.drawingHandler)
           self.drawingHandler = None
        else:
           self.drawingHandler = self.canvas.create_text(event.x, event.y, text = self.name, fill = 'Magenta')

    def setVisibleSimple(self, switch):
      """
      A much simpler visibility method that doesn't mess around with colors
      Parameter: 
        switch = True: then form is made invisible (if not already so)
        switch = False: then form is made visible (if not already so)
      """
      # STATE = NORMAL, DISABLED, or HIDDEN
      if(switch):
        if(self.hidden):
          self.canvas.itemconfig(self.handler, state="normal") 
          self.hidden = 0
      elif(not self.hidden):
          self.canvas.itemconfig(self.handler, state="hidden") 
          self.hidden = 1
    
    def setVisible(self, switch):
        "if switch is different from None, it makes the form visible, otherwise, it makes it invisible"
        if( self.isImage ): return 
        if( not switch):
          if( not self.hidden):
            if self.elementType in self.fillForms:
              self.Color = self.canvas.itemcget(self.handler, "fill") 
              self.canvas.itemconfig(self.handler, fill = "") 
            else:
              self.Color = self.canvas.itemcget(self.handler, "outline")
              self.bgColor = self.canvas.itemcget(self.handler, "fill")                
              self.canvas.itemconfig(self.handler, fill = "")  
              self.canvas.itemconfig(self.handler, outline = "")
            self.hidden = 1
        else:
          if self.hidden:
            if self.elementType in self.fillForms: 
              self.canvas.itemconfig(self.handler, fill = self.Color)
            else:
              self.canvas.itemconfig(self.handler, fill = self.bgColor) 
              self.canvas.itemconfig(self.handler, outline = self.Color)
            self.hidden = 0


    def write2File(self, file, indent="    "):
      """
      Writes the properties of this object to a file. Added 10-July-2002
      """
      itemType = self.canvas.type(self.handler)               # get my type
      # set the coordinates
      coords = self.canvas.coords(self.handler)               # get the coordinates
      file.write(indent+"self.UMLmodel.coords(new_obj."+self.name+".handler")
      for c in coords:
        file.write (","+str(c))
      file.write(")\n")
      itemObject = eval(itemType)()                           # create an object to show its properties
      for attr in itemObject.generatedAttributes.keys():      # walk through all the properties and get the value
        value = self.canvas.itemcget(self.handler, attr)      # get the value...
        # replace possible '\n' : corrected 11 March 2003
        replacedStr = str(value)                                       # Added 11/March/2003 by JL
        replacedStr = replace( replacedStr, '\\', '\\'+'\\')                 # Added 11/March/2003 by JL
        replacedStr = replace( replacedStr, "'", "\\'")                      # Added 11/March/2003 by JL   
        replacedStr = replace( replacedStr, '\n', '\\n')                     # Added 11/March/2003 by JL
        file.write(indent+"self.UMLmodel.itemconfig(new_obj."+self.name+".handler, "+attr+"='"+replacedStr+"')\n")


    def getXY( self ):
        """ Get the coordinates of the polygon/line as [ (x1,y1), ..., (xn,yn) ] """
        coordList = self.canvas.coords( self.handler )
        xy = []
        for i in range( 0, len(coordList), 2):
          xy.append( (coordList[i], coordList[i+1] ) )
        return xy

    def getRotationBase( self, direction='NW'):
        """ 
        Choose the coord in one of cardinal directions that the object will
        rotate on
        """
        if( direction == 'center' ):
          x0,y0,x1,y1 = self.cavans.bbox( self.handler )
          return complex( (x0-x1)/2, (y0-y1)/2 )
        
        xy = self.getXY()        
        minVal = 100000
        minX = 100000
        minY = 100000
        if( direction == 'NW' ):
          for x,y in xy:
            if( x + y < minVal ):
              minVal = x+y
              minX = x
              minY = y
        elif( direction == 'NE' ):
          for x,y in xy:
            if( -x + y < minVal ):
              minVal = -x+y
              minX = x
              minY = y
        elif( direction == 'SW' ):
          for x,y in xy:
            if( x - y < minVal ):
              minVal = x-y
              minX = x
              minY = y
        elif( direction == 'SE' ):
          for x,y in xy:
            if( -x - y < minVal ):
              minVal = -x-y
              minX = x
              minY = y
        else:
          print 'WARNING: Possible incorrect usage of GraphicalForm.getOffset()'
          return complex( 0,0 )
        ##print 'rotation base is ', minX, minY
        return complex( minX,minY )


    def rotate2D( self, angle, rotationBase=(0,0) ):
        """ Rotates a polygon or line in 2D """
        
        # From the previous angle, figure out how much rotation needed
        cAngle = self.lastAngle - angle 
        self.lastAngle = angle
              
        ##cAngle = float(cAngle) / 180.0 * math.pi
        cAngle = cmath.exp(cAngle*1j) # angle in radians
          
        # Point around which rotation occurs
        rotationBase = complex( *rotationBase )

        # Apply rotation directly to the canvas coordinates
        xy = self.getXY()           
        newxy = []
        for x, y in xy:
            v = cAngle * (complex(x, y) - rotationBase) + rotationBase  
            newxy.append(v.real)
            newxy.append(v.imag)
        self.canvas.coords( self.handler, *newxy)
                
        
        