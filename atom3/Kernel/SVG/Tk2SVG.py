"""
Tk2SVG.py

WARNING:
    The 'stipple' attribute of Tk cannot be exported

Denis Dube, 2006
"""
                
from TkColor2SVG import TkColor2SVG      
from Text2XML import Text2XML
        
#===============================================================================
# Public Functions
#===============================================================================
  
def getPolygonSVG(dc, handler, idString):
  """
  Converts a Tkinter canvas (dc) closed polygon object referenced by handler
  and with the tag idString into a SVG string description (return value)
  
  Parameters:
    dc = Tkinter Canvas
    handler = Tkinter polygon ID handler
    idString = Name of a AToM3 graphical form (i.e., "gf43") or any string :)
  
  Returns:
    SVG textual description
  """
  smooth = dc.itemcget(handler, "smooth")
  if(smooth == 'bezier' or smooth == True):
    SVGtext = '  <path'
  else:
    SVGtext = '  <polygon'
    
  if(idString):
    SVGtext += ' id="' + idString + '"'
  SVGtext += ' fill="' + TkColor2SVG(dc.itemcget(handler, "fill")) + '"'
  SVGtext += ' stroke="' + TkColor2SVG(dc.itemcget(handler, "outline")) + '"'
  SVGtext += ' stroke-width="' + str(dc.itemcget(handler, "width")) + '"'
  
  dash = dc.itemcget(handler, "dash")
  if(dash):
    SVGtext += ' dasharray="' + str(dash)[1:-1] + '"'
   
  pointList = dc.coords(handler) 
  if(smooth == 'bezier' or smooth == True):
    SVGtext += '\n  d="' + __TkSmooth2SVGQuadraticPolygon(pointList) + '" />\n'
  else:
    pointsText = ''
    for i in range(0, len(pointList), 2):
      pointsText += str(pointList[i]) + ',' + str(pointList[i+1]) + ' '
    pointsText = pointsText[:-1]  
    SVGtext += '\n  points="' + pointsText + '" />\n'
  
  return SVGtext     
       
          
          
def getPolylineSVG(dc, handler, idString, endMarker=False):
  """  
  Parameters:
    dc = Tkinter Canvas
    handler = Tkinter poly-line ID handler
    idString = Name of a AToM3 graphical form (i.e., "gf43") or any string :)
  
  Returns:
    SVG textual description
  """
  SVGtext = '  <path'
  if(idString):
    SVGtext += ' id="' + idString + '"'
  SVGtext += ' fill="none"'
  SVGtext += ' stroke="' + TkColor2SVG(dc.itemcget(handler, "fill")) + '"'
  SVGtext += ' stroke-width="' + str(dc.itemcget(handler, "width")) + '"'
  
  dash = dc.itemcget(handler, "dash")
  if(dash):
    SVGtext += ' dasharray="' + str(dash)[1:-1] + '"'
    
  pointList = dc.coords(handler) 
  if(endMarker):
    SVGtext += ' marker-end="url(#TriangleArrowhead)"'
    
    # Must now reverse the coordinates so that the marker appears properly
    oldList = pointList[:]
    pointList = []
    for i in range(len(oldList)-1, 0, -2):
      pointList += [oldList[i-1], oldList[i]]
      
  smooth = dc.itemcget(handler, "smooth")
  if(smooth == 'bezier' or smooth == True):
    SVGtext += '\n  d="' + __TkSmooth2SVGQuadraticPolyline(pointList) + '" />\n'
  else:
    pointsText = ''
    for i in range(0, len(pointList), 2):
      if(i == 0):
        pointsText += 'M'
      elif(i == 2):
        pointsText += 'L'
      pointsText += str(pointList[i]) + ',' + str(pointList[i+1]) + ' '
    pointsText = pointsText[:-1]  
    SVGtext += '\n  d="' + pointsText + '" />\n'

  return SVGtext
        
          
                
def getRectangleSVG(dc, handler, idString):
  """  
  Parameters:
    dc = Tkinter Canvas
    handler = Tkinter rectangle ID handler
    idString = Name of a AToM3 graphical form (i.e., "gf43") or any string :)
  
  Returns:
    SVG textual description
  """
  SVGtext = '  <rect'
  if(idString):
    SVGtext += ' id="' + idString + '"'
  SVGtext += ' fill="' + TkColor2SVG(dc.itemcget(handler, "fill")) + '"'
  SVGtext += ' stroke="' + TkColor2SVG(dc.itemcget(handler, "outline")) + '"'
  SVGtext += ' stroke-width="' + str(dc.itemcget(handler, "width")) + '"'
  
  dash = dc.itemcget(handler, "dash")
  if(dash):
    SVGtext += ' dasharray="' + str(dash)[1:-1] + '"'
   
  x, y, w, h = dc.coords(handler) 
  w = w - x
  h = h - y
  SVGtext += '\n  x="%s" y="%s" width="%s" height="%s" />\n' % (x, y, w, h)
  return SVGtext
  
  

def getOvalSVG(dc, handler, idString):
  """  
  Parameters:
    dc = Tkinter Canvas
    handler = Tkinter rectangle ID handler
    idString = Name of a AToM3 graphical form (i.e., "gf43") or any string :)
  
  Returns:
    SVG textual description
  """
  SVGtext = '  <ellipse'
  if(idString):
    SVGtext += ' id="' + idString + '"'
  SVGtext += ' fill="' + TkColor2SVG(dc.itemcget(handler, "fill")) + '"'
  SVGtext += ' stroke="' + TkColor2SVG(dc.itemcget(handler, "outline")) + '"'
  SVGtext += ' stroke-width="' + str(dc.itemcget(handler, "width")) + '"'
  
  dash = dc.itemcget(handler, "dash")
  if(dash):
    SVGtext += ' dasharray="' + str(dash)[1:-1] + '"'
   
  x0, y0, x1, y1 = dc.coords(handler) 
  cx = (x0 + x1) / 2.0
  cy = (y0 + y1) / 2.0
  rx = (x1 - x0) / 2.0
  ry = (y1 - y0) / 2.0
  SVGtext += '\n  cx="%s" cy="%s" rx="%s" ry="%s" />\n' % (cx, cy, rx, ry)
  return SVGtext
  
  
  
def getTextSVG(dc, handler, idString, fontObject, isArrow):
  """  
  Parameters:
    dc = Tkinter Canvas
    handler = Tkinter rectangle ID handler
    idString = Name of a AToM3 graphical form (i.e., "gf43") or any string :)
  Returns:
    SVG textual description
    
  NOTE:
    Different coordinates are used depending on whether the text is multi-line
    or not (i.e.: 'this\ntext is multi-line'). 
    dc.coords(handler) != dc.bbox(handler)
    This choice impacts the anchor alignment offsets.
  """
  text = dc.itemcget(handler, "text") 
  newLinePos = text.find('\n')
  if(newLinePos < 0 or newLinePos - 1 == len(text)):
    multiLine = False
  else:
    textList = __getXMLEscapedTextList(text)
    multiLine = True
  
  if(multiLine):
    SVGtext = '  <g'
  else:
    SVGtext = '  <text'
    
  if(idString):
    SVGtext += ' id="' + idString + '"'
    
#===============================================================================
#  Vertical anchor offset
#===============================================================================
  ascent = fontObject.metrics("ascent")
  descent = fontObject.metrics("descent")
  anchor = dc.itemcget(handler, "anchor") 
  dy = ascent
  
  if(not multiLine):  
    if(anchor[0] == 'n'): # NORTH alignment
      dy = ascent
      #print 'ascent', ascent, 'descent', descent
    elif(anchor[0] == 's'): # SOUTH alignment
      dy = -descent 
    else: # CENTER alignment
      dy = -descent + (ascent + descent) / 2.0 + 1.0 # Don't ask how I got this
      
#===============================================================================
#  Horizontal anchor offset
#===============================================================================
  # Default anchorSVG is 'start' (optimization: remove the 'start'?)
  anchorSVG = "start"
  dx = 0
  if(not multiLine):
    if(anchor in ('center', 's', 'n')): # Center alignment
      dx -= fontObject.measure(text) / 2.0
      
    elif(anchor[-1] == 'e'): # East alignment
      dx -= fontObject.measure(text)

#===============================================================================
#  Text style
#===============================================================================
  SVGtext += '\n    style="'
  
  fontSize = fontObject.cget( 'size' )
  SVGtext += 'font-size:' + str(fontSize) + 'pt'

  SVGtext += ';font-family:' + fontObject.cget( 'family' )
  SVGtext += ';fill:' + TkColor2SVG(dc.itemcget(handler, "fill")) 

  # Default weight is 'normal'
  if(fontObject.cget( 'weight' ) == 'bold'):
    SVGtext += ';font-weight:bold'
  
  # Default style is 'normal'
  if(fontObject.cget( 'slant' ) == 'italic'):
    SVGtext += ';font-style:italic' 

  SVGtext += ';text-anchor:' + anchorSVG + '"'
  
#===============================================================================
#  Final output
#===============================================================================
  if(multiLine):
    coords = dc.bbox( handler )
    lineSpacing = fontObject.metrics("linespace")
    SVGtext += '  >'
    
    x = coords[0] + dx
    y = coords[1] + dy
    if(isArrow):
      y += lineSpacing / 2  # <-- I have no explanation for this fudge factor
    
    for line in textList:
      dx = __getWhitespaceOffset(line, fontObject)
      SVGtext += '\n    <text x="%s" y="%s">%s</text>' % (x + dx, y, line)
      y += lineSpacing
    SVGtext += '    </g>'
      
    
  else:   
    coords = dc.coords(handler)    
    dx += __getWhitespaceOffset(text, fontObject)
    SVGtext += '\n    x="%s" y="%s"' % (coords[0] + dx, coords[1] + dy)
    SVGtext += '>\n    '+ Text2XML(text)
    SVGtext += '  </text>'
  return SVGtext
  

  
def getTextSVG_NoFontObject(dc, handler, idString=None):
  """  
  Parameters:
    dc = Tkinter Canvas
    handler = Tkinter rectangle ID handler
    idString = Name of a AToM3 graphical form (i.e., "gf43") or any string :)
    forceArial = Allows forcing font-family to Arial, since Firefox uses Arial
                 regardless of what you want :(
  Returns:
    SVG textual description
    
  WARNING: Cannot handle multi-line text at present
  WARNING: Uses default font family, size, italics, bold, anchor
  """
  print "WARNING: No fontObject, export quality comprimised"
  SVGtext = '  <text'
  if(idString):
    SVGtext += ' id="' + idString + '"'
  coords = dc.coords(handler) 
  SVGtext += ' x="%s" y="%s"' % (coords[0], coords[1])
  SVGtext += ' fill="' + TkColor2SVG(dc.itemcget(handler, "fill")) + '"'
  SVGtext += '>\n    '+ dc.itemcget(handler, "text") 
  SVGtext += '  </text>'
  return SVGtext
  
  

def getImageSVG(dc, handler, idString, encodedImageString):
  """
  Intention in context:
    Embed an image inside an SVG file. AToM3 stores images in a base64 encoded
    string form, making it trivial to export. If the image were not already
    encoded, the following method could be used: __imageEmbedder(filePath)
  Parameters:
    dc = Tkinter Canvas
    handler = Tkinter polygon ID handler
    idString = Name of a AToM3 graphical form (i.e., "gf43") or any string :)
    encodedImageString = Image encoded in base64
  Returns:
    SVG textual description
  """
  SVGtext = '  <image'
  if(idString):
    SVGtext += ' id="' + idString + '"'
  
  x0, y0, x1, y1 = dc.bbox(handler)
  SVGtext += ' x="' + str(x0) + '"'
  SVGtext += ' y="' + str(y0) + '"'
  SVGtext += ' width="' + str(x1 - x0) + '"'
  SVGtext += ' height="' + str(y1 - y0) + '"'
  
  # Embed the image data
  SVGtext += ' xlink:href="data:;base64,\n' + encodedImageString
  
  return SVGtext + '"/>\n\n'
  

#===============================================================================
# Subroutines  
#===============================================================================


  
def __TkSmooth2SVGQuadraticPolyline(l):
  """
  Smooth polyline coordinate conversion subroutine
  NOTE: Quadratic curves are formed of a sequence of control point, 'real' point
        Where the 'real' point is a point the curve actually goes through.
  """
  length = len(l)
  if(length <= 4):
    SVGtext = 'M%s, %s ' % (l[0], l[1])
    SVGtext += 'L%s, %s' % (l[2], l[3])
  elif(length <= 6):
    SVGtext = 'M%s, %s ' % (l[0], l[1])
    SVGtext += 'Q%s, %s ' % (l[2], l[3])
    SVGtext += '%s, %s' % (l[4], l[5])
  else: 
    SVGtext = 'M%s, %s\n' % (l[0], l[1])
    SVGtext += '    Q%s, %s ' % (l[2], l[3])
    internalPointList = l[2:-2]
    
    for i in range(0, len(internalPointList), 2):
      if(i + 2 >= len(internalPointList)):
        break
      px1 = internalPointList[i]
      py1 = internalPointList[i + 1]
      px2 = internalPointList[i + 2]
      py2 = internalPointList[i + 3]
      midx = (px1 + px2) / 2.0
      midy = (py1 + py2) / 2.0
      SVGtext += '%s, %s\n' % (midx, midy)
      SVGtext += '    %s, %s ' % (px2, py2)
    SVGtext += '%s, %s' % (l[-2], l[-1])
    
  return SVGtext
  
  
  
def __getWhitespaceOffset(singleLineText, fontObject):
  """
  Returns the size (for the given font) that the whitespace at the start of a 
  line would have occupied if SVG would actually render those spaces.
  """
  i = 0
  while(singleLineText[i] == ' '):
    i += 1
  return fontObject.measure(singleLineText[:i])
  
  
  
def __getLengthOfLongestLine(text, fontObject):
  """
  Intention in context:
    Horizontal anchoring offsets in Tk are computed according to the length of
    the longest line in a string with newline characters.
    Example: 'this text\noccupies two lines!' -> len('occupies two lines!') used
  Parameters:
    textLine = A string representing a single line of text
    fontObject = A Tk font object that can measure the length of X whitespace
  Returns:
    Length of the longest line in a multi-line string
  """
  maxLength = 0
  maxLine = ''
  for line in text.split('\n'):
    if(len(line) > maxLength):
      maxLength = len(line)
      maxLine = line
  return fontObject.measure(maxLine)
  
  
  
def __getXMLEscapedTextList(text):
  """
  IntentionInContext:
    1) Escape XML reserved chars
    2) Split the text at newlines into a list of strings
  Parameter:
    text = string
  Returns:
    XML excaped text in a list of strings
  """
  text = Text2XML(text) # Escape reserved XML characters
  if(text == '\n'):
    return ''
  textList = text.split('\n')
  if(textList[-1] == ''):
    textList = textList[:-1]
  return textList
  
  

def __imageEmbedder(path2gifImage):
  """
  Parameter:
    path2gifImage = Path to a GIF image
  Return:
    List of strings representing the encoded image
    
  WARNING: This method is not currently being used  
  """
  import binascii
  
  f = open(path2gifImage,'rb')
  s = []
  while(True):
      b = f.read(80) # f.read parameter is the # of chars to read at one time
      if(not b):
        break
      s.append(binascii.b2a_base64(b)[0:-1])   #-1 to remove new-line char
  f.close()
  return s



  
