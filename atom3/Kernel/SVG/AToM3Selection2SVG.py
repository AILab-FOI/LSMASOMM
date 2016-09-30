"""
AToM3Selection2SVG.py

Denis Dube, 2006
"""
"""
ATTENTION: 
  Firefox specific issue with text
  Any font size (Helvetica family) less than 12pt is forced to 12pt size. 
  Bug does not occur in Inkscape.
"""

from Tk2SVG import getPolygonSVG, getPolylineSVG, getRectangleSVG, getOvalSVG
from Tk2SVG import getTextSVG, getTextSVG_NoFontObject, getImageSVG


def AToM3Selection2SVG(selectionList):
  """
  Intention in context:
    Export the selected graph objects to SVG
  Parameter:
    selectionList = AToM3 selection list of graph objects
  Return:
    SVG textual description 
  """
  # HEADER
  SVGtext = '<?xml version="1.0"?>\n'
  SVGtext += '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"'
  SVGtext += ' "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">\n'
  SVGtext += '<svg xmlns="http://www.w3.org/2000/svg"\n'
  SVGtext += '  xmlns:xlink="http://www.w3.org/1999/xlink"\n'
  SVGtext += '  id="top_"'
  SVGtext += ' xml:lang="en"'
  SVGtext += ' version="1.1"'
  SVGtext += ' baseProfile="full"'
  SVGtext += '>\n\n' 
  SVGtext += "<desc>AToM3 model exported to SVG by Denis' AToM3Selection2SVG.py"
  SVGtext += "</desc>\n"
  SVGtext += '''
<defs>
  <marker id="TriangleArrowhead"
    viewBox="0 0 10 10" refX="10" refY="5" 
    markerUnits="strokeWidth"
    markerWidth="6" markerHeight="6"
    orient="auto">
    <path d="M 0 0 L 10 5 L 0 10 z" />
  </marker>
</defs>\n\n'''
  # marker-end="url(#TriangleArrowhead)"
  
  # BODY
  for graphObj in selectionList:
    SVGtext += convertObj2SVG(graphObj)
    
  # FOOTER
  return SVGtext + '\n</svg>\n'


def convertObj2SVG(graphObj, appendIDString=''):
  """
  Intention in context:
    Convert a single AToM3 graphical object to a SVG textual description
  Parameters:
    graphObj = AToM3 grapical object
    appendIDString = String to add to the ID (used with graphLink.py objects)
  Returns:
    SVG textual description
  """
  groupID = graphObj.tag + appendIDString
  SVGtext = '<g id="' + groupID + '">\n'
  
  # All graphEntity.py subclasses will have this attribute gauranteed
  if(graphObj.__dict__.has_key('graphForms')):
    isArrow = False
    gfList = graphObj.graphForms
    
  # Only other "graphObject" is a graphLink.py which does not have graphForms
  else:
    isArrow = True
    gfList = []
    
    startMarker = graphObj.linkInfo.FirstLink.arrow.getValueBoolean()
    endMarker = graphObj.linkInfo.SecondLink.arrow.getValueBoolean()
    
    for connTuple in graphObj.in_connections_:
      handler = connTuple[0]
      name = connTuple[1]
      SVGtext += getPolylineSVG(graphObj.dc, handler, name, endMarker=startMarker) + '\n'
    for connTuple in graphObj.out_connections_:
      handler = connTuple[0]
      name = connTuple[1]
      SVGtext += getPolylineSVG(graphObj.dc, handler, name, endMarker=endMarker) + '\n'
      
    # Some arrows will have centerObject's and other decorations
    # These are really just graphObject's in their own rights
    if(graphObj.centerObject ):
      SVGtext += convertObj2SVG(graphObj.centerObject, appendIDString='_Center')
    if(graphObj.has1stLink ):
      SVGtext += convertObj2SVG(graphObj.aFirstLink, appendIDString='_1stLink')
    if(graphObj.has2ndLink ):
      SVGtext += convertObj2SVG(graphObj.aSecondLink, appendIDString='_2ndLink')
    if(graphObj.has1stSegment ):
      SVGtext += convertObj2SVG(graphObj.aFirstSegment, appendIDString='_1stSegment')
    if(graphObj.has2ndSegment ):
      SVGtext += convertObj2SVG(graphObj.aSecondSegment, appendIDString='_2ndSegment')

  # Generate SVG for each graphical form (primitive) of the graphical object
  groupID += '.'
  for gf in gfList:
    handler = gf.getHandler()
    dc = gf.canvas
    type = dc.type(handler)
    if(type == 'polygon'):
      SVGtext += getPolygonSVG(dc, handler, groupID + gf.name) + '\n'
    elif(type == 'line'):
      SVGtext += getPolylineSVG(dc, handler, groupID + gf.name) + '\n'
    elif(type == 'rectangle'):
      SVGtext += getRectangleSVG(dc, handler, groupID + gf.name) + '\n'
    elif(type == 'oval'):
      SVGtext += getOvalSVG(dc, handler, groupID + gf.name) + '\n'
    elif(type == 'text'):
      if(gf.fontObject):
        SVGtext += getTextSVG(dc, handler, groupID + gf.name, gf.fontObject, isArrow) + '\n'
      else:
        SVGtext += getTextSVG_NoFontObject(dc, handler, groupID + gf.name) + '\n'
    elif(type == 'image'):
      encodedImageString = graphObj.getImageDict()[gf.imageFilename]
      SVGtext += getImageSVG(dc, handler, groupID + gf.name, encodedImageString)
    else:
      print 'Type not handled', type
      
  SVGtext += '</g>\n'
  return SVGtext
  
