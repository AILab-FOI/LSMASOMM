"""
Exporter.py

Provides a means of exporting the graphics of an AToM3 model to one of three
graph languages. At least three free editors exist that can read these graph
languages and provide considerable automated layout support. 

WARNING: Hyper-edges are not supported at the moment

Created Summer 2004 by Denis Dube
"""

import os, string, tkFileDialog, Dialog, Tkinter, tkColorChooser
from random             import randint

from ASG                import *
from ModelSpecificCode  import isConnectionLink

class Exporter:
  
  GML_LABELED = 0 # Edges are labeled, Graph Modeling Language
  GML_CLASSIC = 1 # "Fake nodes" provide edge labeling, Graph Modeling Language
  GXL_LABELED = 2 # Edges are labeled, Graph Exchange Language
  GXL_CLASSIC = 3 # "Fake nodes" provide edge labeling, Graph Exchange Language
  DOT_LABELED = 4 # Edges are labeled, GraphViz language
  
  # Dictionary Format: { exportFormat : ( fileType, labelingMode, useShape, useColor, useLabels ) }
  FORMAT_DICT = dict()
  FORMAT_DICT[ GML_LABELED ]  = ( 'gml', False, True,  True,  True )
  FORMAT_DICT[ GML_CLASSIC ]  = ( 'gml', True,  True,  True,  True )
  FORMAT_DICT[ GXL_LABELED ]  = ( 'gxl', False, False, False, True )
  FORMAT_DICT[ GXL_CLASSIC ]  = ( 'gxl', True,  False, False, True  )
  FORMAT_DICT[ DOT_LABELED ]  = ( 'dot', False, False, False, True  )
  
  # Automatically assigned colors... defaults
  COLORS = [ '#0000FF', '#006400', '#FF8C00', '#00BFFF', '#3CB371', '#A0522D', 
            '#D2B48C', '#808000', '#000080', '#FF0000', '#32CD32', '#FF00FF', 
            '#778899', '#FFD700', '#FF7F50' ]
  
  # All GML shapes that happen to be recognized by yED :D
  GML_SHAPE_LIST = [ 'rectangle', 'ellipse', 'roundrectangle', 'rectangle3d',
                     'triangle','hexagon', 'octagon','trapezoid','trapezoid2',
                     'parallelogram', 'diamond' ]
  
  # Dictionary Format: { nodeType :  [ shape, color, attributeList ] }
  EXPORT_GRAPHIC_DICT = dict()
  EXPORT_SHAPE = 0
  EXPORT_COLOR = 1
  EXPORT_ATTR  = 2
     
  
  def __init__(self, atom3i ):
    self.atom3i     = atom3i
    self.Tkroot     = atom3i.parent
    
  def initilizeGraphicsDict( self, nodeTypeList ):
    """ Provides default values for exporting graphics """
    usedColors = []
    unInitilized = []
    
    # Node types that have already been initilized
    for nodeType in nodeTypeList:
      if( self.EXPORT_GRAPHIC_DICT.has_key( nodeType ) ):
        usedColors.append( self.EXPORT_GRAPHIC_DICT[ nodeType ][ self.EXPORT_COLOR ] )
      else:
        unInitilized.append( nodeType )
    
    # Node types for which we have no information yet... just make it up :D
    for nodeType in unInitilized:
      for i in range( 0, len( self.COLORS ) ):
        if( self.COLORS[i] not in usedColors ):
          usedColors.append( self.COLORS[i] )
          break
          
      # Pick the first node, get the keys, and that's the attributes we display
      node = self.atom3i.ASGroot.listNodes[ nodeType ][ 0 ]
      attrList = node.generatedAttributes.keys()
      if( 'name' in attrList ): attrList = ['name']       
      elif( 'Name' in attrList ): attrList = ['Name']       
      elif( 'label' in attrList ): attrList = ['label']       
      elif( 'Label' in attrList ): attrList = ['Label']       
      self.EXPORT_GRAPHIC_DICT[ nodeType ] = [ 'rectangle3d', usedColors[-1], attrList ]
                 
  def assembleExportMenu( self, menu ):
    """ Builds a menu system that gives access to the exporter """
    
    self.exportMode = IntVar()     
                
    menu.add_radiobutton(label='GML export', \
                            command=lambda x=self: x.createPropertiesWindow(), \
                            indicatoron=False, \
                            variable=self.exportMode, value = self.GML_LABELED)
                            
    menu.add_radiobutton(label='GML export, with edges as nodes', \
                            command=lambda x=self: x.createPropertiesWindow(), \
                            indicatoron=False, \
                            variable=self.exportMode, value = self.GML_CLASSIC)
               
    menu.add_separator()

                            
    menu.add_radiobutton(label='GXL export', \
                            command=lambda x=self: x.createPropertiesWindow(), \
                            indicatoron=False, \
                            variable=self.exportMode, value = self.GXL_LABELED)
                            
    menu.add_radiobutton(label='GXL export, with edges as nodes', \
                            command=lambda x=self: x.createPropertiesWindow(), \
                            indicatoron=False, \
                            variable=self.exportMode, value = self.GXL_CLASSIC)
                            
    menu.add_separator()
                            
    menu.add_radiobutton(label='DOT export', \
                            command=lambda x=self: x.createPropertiesWindow(), \
                            indicatoron=False, \
                            variable=self.exportMode, value = self.DOT_LABELED)
                                
  def createPropertiesWindow(self ):
    """ 
    Creates a master window that allows for the configuration of the export...
    provided the export format is GML. Otherwise, the GXL and DOT format don't
    need much configuration since they have no mechanisms for storing graphical info.
    """
        
    # If nothing on the canvas, don't bother
    exportableNodeTypes = self.getDisplayableNodeTypes()
    if( len( exportableNodeTypes ) == 0 ): return
            
    # Assigns arbitrary shapes/colors/attributes graphics to each node type
    self.initilizeGraphicsDict( exportableNodeTypes )
        
    # New toplevel window
    self.propertiesWindow = Tkinter.Toplevel(self.Tkroot)
    self.propertiesWindow.geometry("+%d+%d" % (150,150))
    self.propertiesWindow.title("AToM3 Exporter: " + self.getExportTypeTuple()[0].upper() + " format" )
    self.propertiesWindow.transient(self.Tkroot)        
    try:    self.propertiesWindow.grab_set() 
    except: pass
    self.propertiesWindow.focus_set()  
    
    # Create a Frame, Scrollbar, and Listbox
    self.windowFrame = Tkinter.Frame(self.propertiesWindow) 
    self.listboxFrame = Tkinter.Frame(self.windowFrame) 
    self.listbox, self.scrollbar = self.createListBox( self.listboxFrame,
                                                      exportableNodeTypes,
                                                      releaseCallback = self.edit )
                                                          
    # Action buttons
    self.buttonFrame = Tkinter.Frame(self.windowFrame)
    self.infob = Tkinter.Button(self.buttonFrame, text="Info", command=self.info, height=2 )
    self.okayb = Tkinter.Button(self.buttonFrame, text="Ok", command=self.okay, height=3  )
    self.cancelb = Tkinter.Button(self.buttonFrame, text="Cancel", command=self.cancel,height=2 )
    
    self.label = Tkinter.Label(self.windowFrame, height=2, font = 'Times 14',
                               text="Exported graphics configuration", 
                               relief=Tkinter.GROOVE, bg='white' )
                               
    # Help information about the export format
    self.assembleInfoFrame()
    
    # Widget Packaging 
    self.listbox.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)    
    self.scrollbar.pack(side=Tkinter.LEFT, fill=Tkinter.Y)
    
    self.infob.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
    self.okayb.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
    self.cancelb.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
    
    for label in self.info_labelList:
      label.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
    
    self.label.pack(side=Tkinter.TOP, fill=Tkinter.X, expand=1) 
    self.listboxFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
    self.buttonFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
    
    self.windowFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
    
  def assembleInfoFrame( self ):
    """ Provides export format specific info """

    self.infoFrame = Tkinter.Frame(self.windowFrame )   
    self.infoFrameEnabled = False
    self.info_labelList = []
    fileType = self.getExportTypeTuple()[0]
    
    def labelMaker( text ):
      self.info_labelList.append( Tkinter.Label(self.infoFrame, height=2, 
                                                font = 'Times 12',anchor=Tkinter.W ,
                                                text=text, bg='#fffae8' ) )
    
    if( fileType == 'gml' ):
      labelMaker( 'The GML format is compatible with the free Java based yED editor (among others)' )
      labelMaker( 'Caveat: to export to this format, AToM3 graphics will be lost' )
      labelMaker( 'Therefore you must specify the appearence of each node type (or use defaults)' )
    
    elif( fileType == 'gxl' ):
      labelMaker( 'The GXL format is compatible with the free Java based JGraphpad editor (among others)' )
      labelMaker( 'Caveat: to export to this format, AToM3 graphics will be lost' )
      labelMaker( 'However, you can specify which attributes will be exported in the node/edge labels' )
        
    elif( fileType == 'dot' ):
      labelMaker( 'The DOT format is compatible with the GraphViz editor' )
      labelMaker( 'Caveat: to export to this format, AToM3 graphics will be lost' )
      labelMaker( 'However, you can specify which attributes will be exported in the node/edge labels' )
    
    else:
      raise Exception, 'Unkown fileType ' , fileType

  def info( self, event=None ):
    """ Toggles the information frame on/off """
    if( self.infoFrameEnabled ):
      self.infoFrameEnabled = False
      self.infoFrame.pack_forget()
    else:
      self.infoFrameEnabled = True
      self.infoFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
      
  def createListBox( self, frame, items, releaseCallback = None, doubleclickCallback = None ):
    """ Quick listbox with scroll and callback maker """
    
    scrollbar = Tkinter.Scrollbar(frame, orient=Tkinter.VERTICAL)
    listbox = Tkinter.Listbox(frame, yscrollcommand=scrollbar.set, exportselection=0,
                                              selectmode=Tkinter.BROWSE, height = 7)
    
    # Configure the Scrollbar & Listbox
    scrollbar.config(command=listbox.yview)       
    for item in items:
      listbox.insert(Tkinter.END, str( item ) ) 
    
    # Callback method when button is realease in the list box
    if( releaseCallback ):
      listbox.bind("<ButtonRelease>",releaseCallback )
    if( doubleclickCallback ):
      listbox.bind("<Double-ButtonPress>", doubleclickCallback )
    
    return ( listbox, scrollbar )
      
  def okay( self, event=None ):
    self.propertiesWindow.destroy()
    self.export()
    
  def cancel( self, event=None ):
    self.propertiesWindow.destroy()    
    

  def edit( self, event=None ):
    """ Edit window for setting up the graphical appearence of a given node type """
    
    nodeType = self.listbox.get(self.listbox.curselection()[0])
    shape, color, attrList = self.EXPORT_GRAPHIC_DICT[ nodeType ]
    node = self.atom3i.ASGroot.listNodes[ nodeType ][ 0 ]
    allAttrList = node.generatedAttributes.keys()
    useShape, useColor, useLabels = self.getExportTypeTuple( getExportableAttributes = True )
      
    # New toplevel window
    self.editWindow = Tkinter.Toplevel(self.Tkroot)
    self.editWindow.geometry("+%d+%d" % (150,150))
    self.editWindow.title("Export Appearence: " + nodeType  )
    self.editWindow.transient(self.Tkroot)        
    try:    self.editWindow.grab_set() 
    except: pass
    self.editWindow.focus_set()  
    self.editWindow.tk_focusFollowsMouse()
    
    # Frame Creation Area
    self.superEditFrame = Tkinter.Frame(self.editWindow) 
    self.editFrame = Tkinter.Frame(self.superEditFrame) 
    
    self.shapeColorFrame = Tkinter.Frame(self.editFrame)
    self.labelFrame = Tkinter.Frame(self.shapeColorFrame)   
    self.shapeFrame = Tkinter.Frame(self.shapeColorFrame)   
    self.colorFrame = Tkinter.Frame(self.shapeColorFrame)   
       
    self.activeFrame = Tkinter.Frame(self.editFrame)
    self.av_labelFrame = Tkinter.Frame(self.activeFrame)
    self.av_listFrame = Tkinter.Frame(self.activeFrame)
    self.av_remFrame = Tkinter.Frame(self.activeFrame)
          
    self.allAttributesFrame = Tkinter.Frame(self.editFrame) 
    self.all_labelFrame = Tkinter.Frame(self.allAttributesFrame) 
    self.all_listFrame = Tkinter.Frame(self.allAttributesFrame) 
    self.all_addFrame = Tkinter.Frame(self.allAttributesFrame) 
    
    
    # Shape & Color Panel 
    self.shapeColorl = Tkinter.Label(self.labelFrame, height=2, text='Shape & Color',                               
                                relief=Tkinter.GROOVE, bg='white' )
    self.shapeListBox = self.createListBox( self.shapeFrame, self.GML_SHAPE_LIST ) 
    
    # Set the active shape
    for i in range( 0, len( self.GML_SHAPE_LIST ) ):
      if( shape == self.GML_SHAPE_LIST[ i ] ):
        self.shapeListBox[0].selection_set( i )
        
    self.colorb = Tkinter.Button(self.colorFrame, text="Choose Color",
                                 command=self.chooseColor )
    self.colorl = Tkinter.Label(self.colorFrame, height=2,                               
                                relief=Tkinter.RIDGE, bg=color )                                        
        
    self.shapeColorl.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1 ) 
    self.shapeListBox[0].pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1) 
    self.shapeListBox[1].pack(side=Tkinter.LEFT, fill=Tkinter.Y)
    self.colorb.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH ) 
    self.colorl.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1 ) 
    
    # Active Attributes Panel
    self.av_activel = Tkinter.Label(self.av_labelFrame, height=2, text='Export Attributes',                               
                                    relief=Tkinter.GROOVE, bg='white' )
    self.av_activeListbox = self.createListBox( self.av_listFrame, attrList, 
                                               doubleclickCallback = self.removeActiveAttribute  ) 
    self.av_orderb = Tkinter.Button(self.av_remFrame, text="Remove Attribute",
                                 command=self.removeActiveAttribute ) 
                                                                        
    self.av_activel.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1 ) 
    self.av_activeListbox[0].pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1) 
    self.av_activeListbox[1].pack(side=Tkinter.LEFT, fill=Tkinter.Y)
    self.av_orderb.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1 ) 
    
    # All Attributes Panel
    self.all_activel = Tkinter.Label(self.all_labelFrame, height=2, text='All Attributes',                               
                                    relief=Tkinter.GROOVE, bg='white' )
    self.all_attributesListbox = self.createListBox( self.all_listFrame, allAttrList,
                                                    doubleclickCallback = self.addAttribute) 
    self.all_orderb = Tkinter.Button(self.all_addFrame, text="Add Attribute",
                                 command=self.addAttribute ) 
                                                                        
    self.all_activel.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1 ) 
    self.all_attributesListbox[0].pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1) 
    self.all_attributesListbox[1].pack(side=Tkinter.LEFT, fill=Tkinter.Y)
    self.all_orderb.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1 ) 
    
    # Done & Ready Panel 
    self.editDoneb = Tkinter.Button(self.superEditFrame, text="Done",
                                 command=self.editDone )
    self.editDoneb.pack(side=Tkinter.BOTTOM, fill=Tkinter.BOTH, expand=1 )     
        
    # Frame Packaging Area
    if( not isConnectionLink( node.graphObject_ ) and (useShape or useColor) ):
      self.labelFrame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
      if( useShape ):
        self.shapeFrame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
      if( useColor ):
        self.colorFrame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
      self.shapeColorFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
    
    if( useLabels ):
      self.av_labelFrame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
      self.av_listFrame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
      self.av_remFrame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
      self.activeFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
              
      self.all_labelFrame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
      self.all_listFrame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
      self.all_addFrame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
      self.allAttributesFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
    
    self.superEditFrame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
    self.editFrame.pack(side=Tkinter.TOP, fill=Tkinter.BOTH, expand=1)
    
  def addAttribute( self, event=None ):
    """ 
    Adds the attribute in the all attributes listbox to the active attributes
    listbox... provided it isn't already there :D
    """
    listBox = self.all_attributesListbox[0]
    if( listBox.curselection() ):
      attribute = listBox.get( listBox.curselection()[0] )
      activeListbox = self.av_activeListbox[0]
      activeList = activeListbox.get( 0, activeListbox.size() )
      if( not activeList or attribute not in activeList ):
        activeListbox.insert( Tkinter.END, str( attribute ) )
           
  def removeActiveAttribute( self, event=None ):
    """ Removes an attribute from the active attributes list box """
    listBox = self.av_activeListbox[0]
    if( listBox.curselection() ):
      listBox.delete( listBox.curselection()[0] )
      
  def editDone( self, event=None ):
    """ Done editing a nodeTypes graphical export appearence """
    
    nodeType = self.listbox.get(self.listbox.curselection()[0])
    
    # Active Attributes
    activeListbox = self.av_activeListbox[0]
    activeList = activeListbox.get( 0, activeListbox.size() )
    if( activeList ):
      self.EXPORT_GRAPHIC_DICT[ nodeType ][ self.EXPORT_ATTR ] = activeList
    else:
      self.EXPORT_GRAPHIC_DICT[ nodeType ][ self.EXPORT_ATTR ] = []
    
    # Shape Attribute
    shapeListbox = self.shapeListBox[0]
    shape = shapeListbox.get( shapeListbox.curselection()[0] )
    if( shape ):
      self.EXPORT_GRAPHIC_DICT[ nodeType ][ self.EXPORT_SHAPE ] = shape
    else:
      self.EXPORT_GRAPHIC_DICT[ nodeType ][ self.EXPORT_SHAPE ] = self.GML_SHAPE_LIST[0]
    
    # Color was already set in a callback, so lets ditch this window
    self.editWindow.destroy()
    
  def chooseColor( self, event=None ):
    color = tkColorChooser.askcolor()
    if( color != None and color[1] != None ):
      self.colorl.configure( bg = color[1]  )
      nodeType = self.listbox.get(self.listbox.curselection()[0])
      self.EXPORT_GRAPHIC_DICT[ nodeType ][ self.EXPORT_COLOR ] = color[1]
      
  def getDisplayableNodeTypes( self ):
    """ Nodes which will need a graphical appearence when exported """
    nodeList = []
    
    # All the nodeTypes that could possibly be on the canvas
    for item in self.atom3i.ASGroot.nodeTypes: 
            
      # Does this nodeType actually occur on the canvas?
      if( self.atom3i.ASGroot.listNodes[item] ):
        nodeList.append( item )
      
    return nodeList
  
  def getExportTypeTuple( self, getExportableAttributes = False ):    
    """ Export type information from radio button """
    exportFormat = self.exportMode.get()
    if( self.FORMAT_DICT.has_key( exportFormat ) ):
      # Get the useShape, useColor, and useLabels
      if( getExportableAttributes ):
        return self.FORMAT_DICT[ exportFormat ][ 2 : ]
      # Get the fileType and labelingMode
      else:
        return self.FORMAT_DICT[ exportFormat ][ : 2 ]
    raise Exception, "Invalid export format code " + exportFormat
  
  def export( self ):
    """ 
    Exports the model to a human readable file, which can also be read by 
    tools such as yED for automatic layout processing 
    """
    
    fileType, labelingMode = self.getExportTypeTuple()
        
    # Get the fileName & check for cancel
    fileName = tkFileDialog.asksaveasfilename(filetypes=[("Export", "*."+fileType)])	
    if( fileName == '' ):  return    
      
    # Make sure the user is using the right extension (and add it if not)
    if( fileName[-4:] != ("."+fileType) ): fileName += "."+fileType
    
    # Check if the file exists already
    if( os.access(fileName, os.F_OK) ):        
        # Check if back already exists, if so delete it
        if( os.access(fileName+".back", os.F_OK) ):        
          os.remove(fileName+".back")               
        os.rename(fileName, fileName+".back")
  
    # Go go go!
    writeExportCode(self.atom3i.ASGroot, fileName, self.exportMode.get(), 
                    self.EXPORT_GRAPHIC_DICT, labelingMode )
    
    # Update status bar information...
    self.atom3i.statusbar.event( self.atom3i.statusbar.MODEL,  self.atom3i.statusbar.SAVE, fileName)
    if self.atom3i.console: self.atom3i.console.appendText('Exporting model as '+fileType+' in file '+fileName)


  

# ----------------------- CODE GENERATING METHODS ----------------------------

def getShapeColorLabel( node, nodetype, graphicDict ):
  label = ''
  if( graphicDict.has_key( nodetype ) ):
    shape, color, attrList = graphicDict[ nodetype ]            
    for attr in attrList: 
      label += str( node.getAttrValue(attr).getValue() ) + '\n'
  
  # No graphic dictionary? Just dump stuff...
  else:
    color = '#0000FF'
    shape = 'rectangle'
    for attr in node.generatedAttributes.keys(): 
      label += str( node.getAttrValue(attr).getValue() ) + '\n'
  
  return ( shape, color, label )


def writeExportCode(self, fileName,exportFormat, graphicDict, labelingMode = False ):
    """
    Generates GML code for creating this graph. 
    self = ASGroot
    """
        
    file = open(fileName, "w+t" )
    dir, fil   = os.path.split(fileName)
    funcName   = string.split (fil, ".")	# Compose class name

    # Header code
    if( exportFormat == Exporter.GML_LABELED or exportFormat == Exporter.GML_CLASSIC ):
      # GML 
      file.write('Creator	\"Atom3 GML Exporter\"\n')
      file.write('Version	\"0.2.2\"\n')
      file.write('graph\n')
      file.write('[\n')
      file.write('  hierarchic	1\n')
      file.write('  label	\"' + funcName[0] + '\"\n')
      file.write('  directed	1\n')
    elif( exportFormat == Exporter.GXL_LABELED or exportFormat == Exporter.GXL_CLASSIC ):
      # GXL
      file.write('<gxl><graph>\n')
    elif(exportFormat == Exporter.DOT_LABELED ):
      # DOT
      file.write('digraph g {\n')         
    else:
      raise Exception
      
    # Body Code, Version 1: generates a graph with nodes in between nodes (as labels)
    if( labelingMode ):  
      
      for nodetype in self.nodeTypes:		# Iterate on all the node types...
        for node in self.listNodes[nodetype]:	# Iterate on all the nodes of each type                
          if( isConnectionLink( node.graphObject_ ) ):  whiteLabel = True
          else:                                         whiteLabel = False
          
          shape, color, label = getShapeColorLabel( node, nodetype, graphicDict )
          position = [node.graphObject_.x, node.graphObject_.y]
   
          # Label with no border
          if( whiteLabel and exportFormat == Exporter.GML_CLASSIC ):            
            file.write(  genGMLNodeCode(node.objectNumber,label,position, \
                                            fill="#FFFFFF", outline= "#FFFFFF" ) )
          else:
            if( exportFormat == Exporter.GML_CLASSIC ):               
              file.write(  genGMLNodeCode(node.objectNumber,label,position, 
                                          fill = color, type = shape ) )
            elif( exportFormat == Exporter.GXL_CLASSIC ): 
              file.write(  genGXLNodeCode(node.objectNumber,label ) )
              
      # Generate code for the connections...
      edgeID = 0
      for nodetype in self.nodeTypes:
        for node in self.listNodes[nodetype]:
          # Looping over the output connections is sufficient
          for obj in node.out_connections_:
            if( exportFormat == Exporter.GML_CLASSIC ):             
              file.write( genGMLConnectionCode(node.objectNumber,obj.objectNumber)) 
            elif( exportFormat == Exporter.GXL_CLASSIC ): 
              file.write( genGXLConnectionCode(node.objectNumber,obj.objectNumber,edgeID)) 
              edgeID += 1
    
    
    # Body Code, Version 2: no intermediate nodes, labels directly on the edges
    else:      
      
      for nodetype in self.nodeTypes:		# Iterate on all the node types...
        for node in self.listNodes[nodetype]:	# Iterate on all the nodes of each type               
          if( isConnectionLink( node.graphObject_ ) ):  continue
              
          shape, color, label = getShapeColorLabel( node, nodetype, graphicDict )
          position = [ node.graphObject_.x, node.graphObject_.y]
        
          # Generate code for the nodes...
          if( exportFormat == Exporter.GML_LABELED ):
            file.write(  genGMLNodeCode(node.objectNumber,label,position, fill=color, type=shape) )
          elif( exportFormat == Exporter.GXL_LABELED ):
            file.write(  genGXLNodeCode(node.objectNumber,label) )
          elif(exportFormat == Exporter.DOT_LABELED ):
            file.write(  genDOTNodeCode(node.objectNumber,label) )
      
      # Generate code for the connections...
      edgeID = 0
      for nodetype in self.nodeTypes:
        for node in self.listNodes[nodetype]:
          if( not isConnectionLink( node.graphObject_ ) ):  continue
      
          label = getShapeColorLabel( node, nodetype, graphicDict )[ 2 ]
                  
          target = node.out_connections_[0].objectNumber
          source = node.in_connections_[0].objectNumber     
          if( exportFormat == Exporter.GML_LABELED ):                                                
            file.write( genGMLConnectionCode(source,target,label)  )
          elif( exportFormat == Exporter.GXL_LABELED ):
            file.write( genGXLConnectionCode(source,target,edgeID,label)  )
            edgeID += 1
          elif(exportFormat == Exporter.DOT_LABELED ):
            file.write( genDOTConnectionCode(source,target,label)  )
          
    # Footer code
    if( exportFormat == Exporter.GML_LABELED or exportFormat == Exporter.GML_CLASSIC ):
      # GML
      file.write(']\n')
    elif( exportFormat == Exporter.GXL_LABELED or exportFormat == Exporter.GXL_CLASSIC ):
      # GXL
      file.write('</graph></gxl>\n')
    elif(exportFormat == Exporter.DOT_LABELED ):
      #DOT
      file.write('}\n')
    else:
      raise Exception
  
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

  
def genGXLNodeCode( objectID, label):
  """ Generates GML code for a node """

  code = ''  
  code += '  <node id=\"'+str(objectID)+'\">\n'
  code += '  	<attr name="Label">\n'
  code += '  		<string>' + label + '</string>\n'
  code += '  	</attr>\n'
  code += '  </node>\n' 
  return code


def genGXLConnectionCode(sourceID, targetID, edgeID, label="" ):
  """ Generates GXL code for a connection between two objects """                        
      
  code = ''  
  code += '  <edge id=\"edge'+str(edgeID)+'\" from=\"' + str(sourceID) + '\" to=\"' + str(targetID) + '\">\n'
  code += '  	<attr name="Label">\n'
  code += '  		<string>' + label + '</string>\n'
  code += '  	</attr>\n'
  code += '  </edge>\n'  
  return code


def genDOTNodeCode( objectID, label):
  code = ''  
  code += '\"'+str(objectID)+'\" [ label = \"'+label+'\" ];\n'
  return code

def genDOTConnectionCode(sourceID, targetID, label="" ):
  code = ''  
  code += '\"'+str(sourceID)+'\" -> \"'+str(targetID)+'\" [ label = \"'+label+'\" ];\n'
  return code
