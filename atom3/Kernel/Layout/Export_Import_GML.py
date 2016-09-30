"""
Export_Import_GML.py

This module is dedicated to exporting an AToM3 model to 'Graph Modeling Language'
and then re-importing it onto the AToM3 model. The benefit lies in the fact that
a secondary program can be used to apply sophisticated automated layout to the
GML graph and then AToM3 can mimic this layout by importing the new positions
of the elements. 
NOTE: Simply exporting is not very satisfactory, since AToM3 graphics are lost.

Created August 6, 2004
"""


import os, string, tkFileDialog, re, Tkinter
from random             import randint

from ModelSpecificCode  import isConnectionLink
from Utilities          import optimizeConnectionPorts
   
   
def exportImportDialog( self ):
        
  # New toplevel window
  propertiesWindow = Tkinter.Toplevel(self.parent)
  propertiesWindow.geometry("+%d+%d" % (150,150))
  propertiesWindow.title("AToM3" )
  propertiesWindow.transient(self.parent)        
  try:    propertiesWindow.grab_set() 
  except: pass
  propertiesWindow.focus_set()  
  
  # Create a Frame, Scrollbar, and Listbox
  windowFrame = Tkinter.Frame(propertiesWindow) 
 
  class ImportEdges:
    def __init__(self):
      self.importEdges = True
    def toggleChoice(self):
      if( self.importEdges ): self.importEdges = False
      else:                   self.importEdges = True
      return self.importEdges
    def getChoice(self):
      return self.importEdges 
  
  importEdges = ImportEdges()
 
  def importHandler(importEdges):
    importEdgesButton.pack_forget()
    exportButton.configure( text="Export", command=lambda i=importEdges: exportHandler(i) )
    importer(self, importEdges.getChoice() )   
  
  def exportHandler(importEdges):   
    if( importEdges.getChoice() ):
      importEdgesButton.configure( text="Import Edges: ENABLED" )
    else:
      importEdgesButton.configure( text="Import Edges: DISABLED" )
    closeButton.pack_forget()
    importEdgesButton.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
    closeButton.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )              
    exportButton.configure( text="Import", command=lambda i=importEdges: importHandler(i) )
    export( self )
    
  def importEdgesHandler(importEdges):
    if( importEdges.toggleChoice() ):
      importEdgesButton.configure( text="Import Edges: ENABLED" )
    else:
      importEdgesButton.configure( text="Import Edges: DISABLED" )

                                                        
  # Action buttons
  exportButton = Tkinter.Button(windowFrame, text="Export", height=2  )
  exportButton.configure( command=lambda i=importEdges: exportHandler(i) )
  
  label = Tkinter.Label(windowFrame, height=2,padx=12, font = 'Times 14',
                            text="Instant GML Exporter/Importer", 
                            relief=Tkinter.GROOVE, bg='white' )
                            
  label2 = Tkinter.Label(windowFrame, height=2,padx=12, font = 'Times 12',fg='red',
                            text="WARNING: The exported data can only be re-imported in this AToM3 session,\nand only the position information may be modified.", 
                            relief=Tkinter.GROOVE, bg='white' )
                       
  importEdgesButton = Tkinter.Button(windowFrame, height=2,
                                     command=lambda i=importEdges: importEdgesHandler(i))
                            
  closeButton = Tkinter.Button(windowFrame, text="Close", height=2, 
                               command=propertiesWindow.destroy )
  
  
  # Widget Packaging 

  label.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
  label2.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
  exportButton.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
  closeButton.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )

  windowFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)

  
   
def importer( self, importEdgesFlag = True ):
  """
  Imports GML. If the objectNumbers in the GML match the current AToM3 model,
  the position information will be applied to the AToM3 model.
  """
  
  fileName = tkFileDialog.askopenfilename( title="Import GML",
      filetypes=[("Graph Modelign Language", "*.gml"),("All files", "*")])
  if( fileName == '' ): return "User canceled"
  
  # Too cautions? Nonesense...
  if( not os.path.exists( fileName ) ): 
    return importError( self, "File does not exist: " + fileName )
  
  f = open( fileName, 'r' )
  fileString = f.read()
  f.close()
  
  nodePattern  = re.compile( 'node\s*\[\s*id[ \t]*(\d*)\s*label[ \t]*\"(\d*)\"\s*graphics\s*\[\s*x[ \t]*(-?\d*\.\d*)\s*y[ \t]*(-?\d*\.\d*)' )
  linkPattern  = re.compile( 'edge\s*\[\s*source[ \t]*(\d*)\s*target[ \t]*(\d*)\s*label[ \t]*\"(\d*)\"(?:[\w\s.\[\"\#]*Line([\w\s\[\]\.-]*edgeAnchor)|\s)' )
  pointPattern = re.compile( 'point\s*\[\s*x[ \t]*(-?\d*\.\d*)\s*y[ \t]*(-?\d*\.\d*)' )
  
  matchList = nodePattern.findall( fileString )
  if( not matchList  ): return importError( self, "Imported contents null" )
  
  objectNumberDict = dict()
  for tuple in matchList:
    id, objectNumber, x, y = tuple    
    id = int( id )
    objectNumber = int( objectNumber )
    x = float( x )
    y = float( y )
    objectNumberDict[ objectNumber ] = ( id, x, y )
         
       
  if( importEdgesFlag ):
  
    # Go through all the edges & store the points
    edgeDict = dict()
    matchList = linkPattern.findall( fileString )
    for tuple in matchList:
      sourceID, targetID, objectNumber, pointString = tuple
      sourceID = int( sourceID )
      targetID = int( targetID )
      objectNumber = int( objectNumber )
      edgeID =  objectNumberDict[ objectNumber ][0] 

      if( targetID == edgeID ):
        if( not edgeDict.has_key( objectNumber ) ):
          edgeDict[ objectNumber ] = [ [], [] ]        
        if( pointString ):
          edgeDict[ objectNumber ][0] = pointPattern.findall( pointString ) 
        
      elif( sourceID == edgeID ):
        if( not edgeDict.has_key( objectNumber ) ):
          edgeDict[ objectNumber ] = [ [], [] ] 
        if( pointString ):
          edgeDict[ objectNumber ][1] = pointPattern.findall( pointString ) 
            
      else:
        print sourceID, targetID, edgeID
        raise Exception, "Not likely..."
  
   
  if( not isImportValid( self, objectNumberDict.copy() ) ): return 
  #windowOffset = fitInWindow( objectNumberDict )
  
  # Iterate on all the node types...
  nodeTypes = self.ASGroot.nodeTypes
  listNodes = self.ASGroot.listNodes 
  dc = self.getCanvas()
  for nodetype in nodeTypes:		    
    # Iterate on all the nodes of nodetype
    for node in listNodes[nodetype]:	     
      id, x, y = objectNumberDict[ node.objectNumber ] 
      sx, sy = node.graphObject_.getSize()
      dx = x - (sx / 2.0) - node.graphObject_.x
      dy = y - node.graphObject_.y
      
      # Node, not an edge...
      if( not isConnectionLink( node.graphObject_ ) ): 
        node.graphObject_.Move( dx,dy, moveConn=False) 
      elif( not importEdgesFlag ):
        node.graphObject_.Move( dx,dy, what=node.graphObject_.ALL_SELECTED )
      
        
  # Edge, and I want to import it
  if( importEdgesFlag ):
  
    for nodetype in nodeTypes:		    
      # Iterate on all the nodes of nodetype
      for node in listNodes[nodetype]:	
          
        # Edges only!
        if( not isConnectionLink( node.graphObject_ ) ):
          continue
      
        sourceNodeSize = node.in_connections_[0].graphObject_.getSize()
        targetNodeSize = node.out_connections_[0].graphObject_.getSize()
#        offset = [(sourceNodeSize[0] + targetNodeSize[0]) / 4.0,
#                  (sourceNodeSize[1] + targetNodeSize[1]) / 4.0]
        offset = [0, (sourceNodeSize[1] + targetNodeSize[1]) / 4.0]
        
        id, x, y = objectNumberDict[ node.objectNumber ] 
        dx = x + offset[0] - node.graphObject_.x
        dy = y + offset[1] - node.graphObject_.y
        node.graphObject_.Move( dx, dy, what=node.graphObject_.ALL_SELECTED )
  
        # Edge Control Points
        if( edgeDict.has_key( node.objectNumber ) ):
          seg1coords, seg2coords = edgeDict[node.objectNumber]
          for connTuple in node.graphObject_.connections:
            itemHandler = connTuple[0]
            direction = connTuple[1]
            segCoords = dc.coords( itemHandler  ) 
            
            # Segment 2
            if( direction == 0 ):
              if( seg2coords ):
                coordList = reverseList2by2( convertTupleCoords( seg2coords ) )
                intObjCoord = addOffsetToCoordList( coordList[ -2 : ], offset )
                dx = intObjCoord[0] - node.graphObject_.x
                dy = intObjCoord[1] - node.graphObject_.y
                node.graphObject_.Move( dx,dy, what=node.graphObject_.ALL_SELECTED )
                dc.coords( * [itemHandler] + coordList[ : 2] + addOffsetToCoordList( coordList [ 2 : -2 ], offset) + intObjCoord)                 
                #dc.coords( * [itemHandler] + convertTupleCoords( seg2coords, windowOffset)[ : -2 ] + segCoords[ -2: ] ) 
              else:
                dc.coords( * [itemHandler] + segCoords[ : 2] + segCoords[ -2 : ]  )
              
            # Segment 1
            else:
              if( seg1coords ):
                coordList = convertTupleCoords( seg1coords )
                intObjCoord = addOffsetToCoordList( coordList[ -2 : ], offset)
                print 'intObjCoord', intObjCoord, node.name.toString()
                dx = intObjCoord[0] - node.graphObject_.x
                dy = intObjCoord[1] - node.graphObject_.y
                node.graphObject_.Move( dx,dy, what=node.graphObject_.ALL_SELECTED )
                dc.coords( * [itemHandler] + coordList[ : 2] + addOffsetToCoordList( coordList[ 2 : -2 ], offset) +  intObjCoord)
                #dc.coords( * [itemHandler] + convertTupleCoords( seg1coords, windowOffset)[ : -2 ] + segCoords[ -2: ]  ) 
              else:
                dc.coords( * [itemHandler] + segCoords[ : 2] + segCoords[ -2 : ]  )
                                         
  optimizeConnectionPorts(self, doAllLinks = True)

def addOffsetToCoordList( list, offset):
  """ Adds an offset to a list of coords """
  offsetedList = []
  for i in range( 0, len( list ), 2 ):
      offsetedList.append( list[i]  + offset[0] )
      offsetedList.append( list[i+1] + offset[1] )
  return offsetedList
  
def convertTupleCoords( tupleList, windowOffset = [0,0] ):
  """ 
  Takes a list of points: [ (x,y),(x,y),(x,y) ]
  Gives them an offset
  Cuts off the last point
  """
  offsetX, offsetY = windowOffset
  pureList = []
  for x,y in tupleList:
    pureList.append( float(x) + offsetX )
    pureList.append( float(y) + offsetY )
  return pureList

def reverseList2by2 ( list):
      """
         Reverses the list, taking its element 2 by 2 (they are pair of points...)
      """
      reversed = []
      counter = len(list)-1
      while counter > 0:
          px, py = list[counter-1], list[counter]
          reversed.append(px)
          reversed.append(py)
          counter = counter - 2
      return reversed

      
def fitInWindow( objectNumberDict ):
  """ Ensures a tight fit :D """
  offset = 100
  minX, minY = 10000,10000
  for key in objectNumberDict.keys():
    id,x,y = objectNumberDict[key]
    if( x < minX ):
      minX = x
    if( y < minY ):
      minY = y
  if( minX < 0 or minX > offset ):
    minX = offset - minX
  if( minY < 0 or minY > offset ):
    minY = offset - minY
  for key in objectNumberDict.keys():
    id,x,y = objectNumberDict[key]
    objectNumberDict[key] = ( id, x+minX, y+minY )
  return  (minX,minY)
   
def isImportValid( self, objectNumberDict ):
  """ Returns True if it will be possible to import """
  
  # Iterate on all the node types...
  nodeTypes = self.ASGroot.nodeTypes
  listNodes = self.ASGroot.listNodes 
  for nodetype in nodeTypes:		    
    # Iterate on all the nodes of nodetype
    for node in listNodes[nodetype]:	      
      # Tick off each node in the current AToM3 model against the imported stuff
      if( objectNumberDict.has_key( node.objectNumber ) ):
        del objectNumberDict[ node.objectNumber ]
      else:
        print node.objectNumber, objectNumberDict
        return importError( self, "Import mismatch with current model" )
      
  # The checklist should be empty...
  if( len( objectNumberDict ) != 0 ): 
    return importError( self, "Imported contents size mismatch with current model " + str(objectNumberDict.keys()) )
      
  return True
      
def importError(self, text):
  print text
  return False   
   
def export( self ):
  """ 
  Exports the model to a human readable file, which can also be read by 
  tools such as yED for automatic layout processing 
  """

  # Get the fileName & check for cancel
  fileName = tkFileDialog.asksaveasfilename(title="Export GML",
              filetypes=[("Graph Modeling Language", "*.gml"),("All files","*")])	
  if( fileName == '' ):  return    

  # Make sure the user is using the right extension (and add it if not)
  if( fileName[-4:] != (".gml") ): fileName += ".gml"
  
  # Check if the file exists already
  if( os.access(fileName, os.F_OK) ):        
      # Check if back already exists, if so delete it
      if( os.access(fileName+".back", os.F_OK) ):        
        os.remove(fileName+".back")               
      os.rename(fileName, fileName+".back")

  # Go go go!
  writeExportCode(self.ASGroot, fileName )
  
  # Update status bar information...
  self.statusbar.event( self.statusbar.MODEL,  self.statusbar.SAVE, fileName)
  if self.console: self.console.appendText('Exporting model as gml in file '+fileName)



def writeExportCode(self, fileName):
    """
    Generates GML code for creating this graph. 
    self = ASGroot
    """
        
    file = open(fileName, "w+t" )
    dir, fil   = os.path.split(fileName)
    funcName   = string.split (fil, ".")	# Compose class name

    # Header code GML 
    file.write('Creator	\"Atom3 GML Exporter\"\n')
    file.write('Version	\"0.2.2\"\n')
    file.write('graph\n')
    file.write('[\n')
    file.write('  hierarchic	1\n')
    file.write('  label	\"' + funcName[0] + '\"\n')
    file.write('  directed	1\n')
        
  
      
    for nodetype in self.nodeTypes:		# Iterate on all the node types...
      for node in self.listNodes[nodetype]:	# Iterate on all the nodes of each type                
        if( isConnectionLink( node.graphObject_ ) ):  whiteLabel = True
        else:                                         whiteLabel = False
        
        position = [node.graphObject_.x, node.graphObject_.y]

        # Label with no border
        if( whiteLabel ): 
          centerObject  = node.graphObject_.getCenterObject() 
          if( centerObject ):   
            x0,y0,x1,y1 = centerObject.getbbox()
            size = (x1-x0,y1-y0)
          else:
            size = None
          file.write(  genGMLNodeCode(node.objectNumber,str(node.objectNumber),position, \
                                          size=size, fill="#FFFFFF", outline= "#FFFFFF" ) )
        else:          
          x0,y0,x1,y1 = node.graphObject_.getbbox()  
          size = (x1-x0,y1-y0)
          file.write(  genGMLNodeCode(node.objectNumber,str(node.objectNumber),position,size=size ) )
   
            
    # Generate code for the connections...
    for nodetype in self.nodeTypes:
      # Are there any nodes of this type?
      if( self.listNodes[nodetype] ):
        # Is this a link nodeType?
        if( isConnectionLink( self.listNodes[nodetype][0].graphObject_ ) ):
          # Go over all the nodes
          for node in self.listNodes[nodetype]:
            # Go over all the outbound connections
            for obj in node.out_connections_:
              file.write( genGMLConnectionCode(node.objectNumber,
                                             obj.objectNumber,
                                             label = str(node.objectNumber))) 
            # Go over all the inbound connections
            for obj in node.in_connections_:
              file.write( genGMLConnectionCode(obj.objectNumber,
                                             node.objectNumber,
                                             label = str(node.objectNumber))) 
                               
    # Footer code GML
    file.write(']\n')
      
    file.close()
    return funcName[0] # This indicates that we've done something
  
  
def genGMLConnectionCode(sourceID, targetID, label="", fill = "#000000", \
                        targetArrow = "standard" ):
  """ 
  Generates GML code for a connection between two objects 
  """                        
      
  code = ''
  
  code += '  edge\n'
  code += '  [\n'
  code += '    source	' + str(sourceID) + '\n'
  code += '    target	' + str(targetID) + '\n'
  if( label != "" ):
    code += '    label	\"' + label + '\"\n'
  code += '    graphics\n'
  code += '    [\n'
  code += '      fill	\"' + fill + '\"\n'
  code += '      targetArrow	\"' + targetArrow + '\"\n'
  code += '    ]\n'
  if( label != "" ):
    code += '    LabelGraphics\n'
    code += '    [\n'
    code += '      text	\"' + label + '\" \n'
    code += '      fontSize	12\n'
    code += '      fontName	\"Dialog\" \n'
    code += '      model	\"six_pos\" \n'
    code += '      position	\"tail\" \n'
    code += '    ]\n'
  code += '  ]\n'

  return code
  
  
def genGMLNodeCode( objectID, label, position, size = None, \
                  type="rectangle",fill="#CCCCFF", outline = "#000000"):
  """ 
  Generates GML code for a node 
  position and size are 2-tuples, size is optional
  """

  
  # If no specified size, make it 15 pix high, and at least 15 pix wide
  # If a large label is present, give 6 pix per character
  if( size == None ):      
    size = [ max( 7*len(label), 15) , 15 + 15*label.count( '\n' )]
 
  
  code = ''
  
  code += '  node\n'
  code += '  [\n'
  code += '    id	' + str(objectID) + '\n'
  code += '    label	\"' + label + '\"\n'
  code += '    graphics\n'
  code += '    [\n'
  code += '      x	' + str(position[0]) + '\n'
  code += '      y	' + str(position[1]) + '\n'
  code += '      w	' + str(size[0]) + '\n'
  code += '      h	' + str(size[1]) + '\n'
  code += '      type	\"' + type + '\" \n'
  code += '      fill	\"' + fill + '\" \n'
  code += '      outline \"' + outline + '\" \n'
  code += '    ]\n'
  code += '    LabelGraphics\n'
  code += '    [\n'
  code += '      text	\"' + label + '\"\n'
  code += '      fontSize	12\n'
  code += '      fontName	\"Dialog\"\n'
  code += '      anchor	\"c\"\n'
  code += '    ]\n'
  code += '  ]\n'
  
  return code

  