"""
SaveGFVisitor.py

Generates the AToM3 appearence code for a semantic object
in the ER formalism. These are graph_*.py files.

Fleshed out by Denis Dube, July 29, 2004
"""

import string, os, tkMessageBox

import Graphics
from GFVisitors import GFVisitor


class TextSortVisitor( GFVisitor ):
  """ 
  Sorts the graphical forms so that text is placed at the end 
  This is important as we want to be able to read the text, not have it buried
  under a heavy pile of graph forms :D
  """
  
  def __init__(self):
      pass
    
  def sortGraphicalForms( self, gfList ):    
    """ Returns the gfList with text items at the end """
    self.regularItemsList = []
    self.textItemsList = []
    
    for gf in gfList:
        gf.accept(self)
        
    return self.regularItemsList + self.textItemsList 
    
  def visitRectangle(self, gf):
      self.regularItemsList.append( gf )
        
  def visitOval(self, gf):
      self.regularItemsList.append( gf )
      
  def visitPolygon(self, gf):
      self.regularItemsList.append( gf )
  
  def visitLine(self, gf):
      self.regularItemsList.append( gf )
  
  def visitText(self, gf):
      self.textItemsList.append( gf )

  def visitImage(self, gf):
      self.regularItemsList.append( gf )
  
  def visitConnector(self, gf):
      self.regularItemsList.append( gf )
  
  def visitComposite(self, gf):
      list = gf.getComponents()
      for gf in list:
        gf.accept(self)
    
  def visitAttribute( self, gf):
      self.textItemsList.append( gf )
    
  def visitNamedConnector( self, gf ):
      self.regularItemsList.append( gf )


class ATOM3_Export_Visitor( GFVisitor ):
  
  def __init__(self, semObject, editor ):      
      self.semObject      = semObject      
      self.ATOM3instance  = semObject.parent
      self.className      = editor.className
      self.modelPath      = editor.modelPath
      self.editor         = editor
    
  def AToM3_export(self, gfList ):
       
      name = "graph_" + self.className 
      fileName = os.path.join( self.modelPath, name + '.py' )
      
      f = open( fileName, "w+t" )            
      if( f == None): return None
      
      # Check if we actually have a drawing      
      if(len(gfList) < 1):                         
          f.close()
          try:
            os.remove(fileName)
            os.remove(fileName+'c')     # can fail!
          except OSError:
            pass
          return None
          
      # Bounding box and icon size
      self.bbox = self.editor.getBoundingBox( self.editor.getGFs() )
      self.size = ( self.bbox[2] - self.bbox[0], self.bbox[3] - self.bbox[1] )
        
      # Note: you can change classIndent, but leave methodIndent alone!
      classIndent = '    '
      methodIndent = classIndent + classIndent
      self.constraintList = self.editor.scripting.getConstraintList()
      
      self.generateHeaderCode( f, name, classIndent, methodIndent )
     
      # Generate code for each graphical form
      self.f = f
      self.CI = classIndent
      self.MI = methodIndent     
                  
      self.hasConnector = False
      for gf in gfList:
        gf.accept(self)
        
      self.generateFooterCode( f, name, classIndent, methodIndent )

      if(not self.hasConnector):
        tkMessageBox.showwarning('WARNING: No connectors', 
          "You have saved a visual icon with no connectors\n\n"
          + "It will NOT be possible to connect this entity with others")

  def visitRectangle(self, gf ):
      """ Exports a rectangular object """
      self.visitRegularObject( 'rectangle', gf )
        
  def visitOval(self, gf):
      """ Exports a circle/oval object """
      self.visitRegularObject( 'oval', gf )
      
  def visitPolygon(self, gf):
      """ Exports closed polyline objects """
      self.visitRegularObject( 'polygon', gf )
  
  def visitLine(self, gf):
      """ Exports multi-point line objects """
      self.visitRegularObject( 'line', gf )
  
  def visitText(self, gf):
      """ Generates code for text objects """
    
      f = self.f
      indent = self.MI
      coordList = gf.getCoords()  
      gfName = "gf" + str( gf.getObjectNumber() )
           
      if( gf.getBold() ):     b = "bold"
      else:                   b = "normal"
      if( gf.getItalic() ):   i = "italic"
      else:                   i = "roman"
           
      f.write(indent+'font = tkFont.Font( family=\''+str( gf.getFamily() )+'\'' )
      f.write(', size='+str( gf.getSize() ) )
      f.write(', weight=\''+str( b ) + '\'' )
      f.write(', slant=\''+str( i ) + '\'' )
      f.write(', underline='+str( gf.getUnderline()  ) )
      f.write(')\n')
      
      f.write(indent+'h = drawing.create_text(self.translate(')
      f.write( str(coordList)+')[:2], tags = self.tag, font=font')
      f.write(', fill = \''   + str( gf.getFillColor()  ) + '\'' )
      f.write(', anchor = \'' + str( gf.getAnchor()     ).lower() + '\'' ) 
      text = gf.getText()
      text = string.replace(text, '\n', '\\n') # Escape newlines
      text = string.replace(text, "'", '"') # Use double quotes instead.. safe
      f.write(', text = \''   + text + '\'' )      
      f.write(', width = \''  + str( gf.getWidth()      ) + '\'' )      
      f.write(', justify= \'left\', stipple=\'\' )\n')

      f.write(indent+'self.'+gfName+' = GraphicalForm(drawing, h, \''+gfName+'\', fontObject=font)\n')
      f.write(indent+'self.graphForms.append(self.'+gfName+')\n\n')
        
  def visitAttribute( self, gf ):
      
    f = self.f
    indent = self.MI
    attribute = gf.getText()
    coordList = gf.getCoords()  
    gfName = "gf" + str( gf.getObjectNumber() )
   
    f.write(indent+'if self.semanticObject: drawText = self.semanticObject.' )
    # NOTE: the Kernel.ATOM3.modifyVisualAttribute() method must use the same 
    # text char area as the one given here in the toString() call.
    f.write(attribute +'.toString()\n')
    
    f.write(indent+'else: drawText = "<'+attribute+'>"\n')
    
    if( gf.getBold() ):     b = "bold"
    else:                   b = "normal"
    if( gf.getItalic() ):   i = "italic"
    else:                   i = "roman"
        
    f.write(indent+'font = tkFont.Font( family=\''+str( gf.getFamily() )+'\'' )
    f.write(', size='+str( gf.getSize() ) )
    f.write(', weight=\''+str( b ) + '\'' )
    f.write(', slant=\''+str( i ) + '\'' )
    f.write(', underline='+str( gf.getUnderline()  ) )
    f.write(')\n')
    
    f.write(indent+'h = drawing.create_text(self.translate(')
    f.write( str(coordList)+')[:2], tags = self.tag, font=font')
    f.write(', fill = \''   + str( gf.getFillColor()  ) + '\'' )
    f.write(', anchor = \'' + str( gf.getAnchor()     ).lower() + '\'' )  
    f.write(', text = drawText' )      
    f.write(', width = \''  + str( gf.getWidth()      ) + '\'' )     
    f.write(', justify= \'left\', stipple=\'\' )\n')
        
    f.write(indent+'self.attr_display[\"' + attribute + '\"] = h\n')
       
    f.write(indent+'self.'+gfName+' = GraphicalForm(drawing, h, \''+gfName+'\', fontObject=font)\n')
    f.write(indent+'self.graphForms.append(self.'+gfName+')\n\n')


  def visitImage(self, gf):
      
      f = self.f
      indent = self.MI
      coordList = gf.getCoords()  
      gfName = "gf" + str( gf.getObjectNumber() )
                
      f.write(indent+ 'self.image_'+gfName+' = PhotoImage(format=\'gif\',')
      f.write('data=self.imageDict[\''+gf.getFilename()+'\' ])\n')
      
      f.write(indent+'h = drawing.create_image(self.translate(')
      f.write( str(coordList)+'), tags = self.tag, image = self.image_'+gfName+')\n')
            
      f.write(indent+'self.'+gfName+' = GraphicalForm(drawing, h, \''+gfName+'\', \''+gf.getFilename()+'\')\n')
      f.write(indent+'self.graphForms.append(self.'+gfName+')\n\n')
  
  
  def visitConnector(self, gf, named = False ):
      """ Exports a connection port as an invisible graphic """
            
      f = self.f
      coordList = gf.getCoords()
      if( len( coordList ) == 2 ):
        coordList += coordList
      
      f.write(self.MI+'h = drawing.create_oval(self.translate('+str(coordList)+')')
      f.write(', tags = (self.tag, \'connector\'), outline = \'\', fill = \'\' )\n')

      f.write(self.MI+'self.connectors.append( h )\n')

      if( named ):
        f.write(self.MI+'self.namedConnectors[h] = \''+ gf.getName()+ '\' \n\n')
      else:
        f.write('\n')
        
      self.hasConnector = True
        
  def visitNamedConnector( self, gf):
      self.visitConnector( gf, named = True )

      
  def visitComposite(self, compositeGF):
      list = compositeGF.getComponents()
      for gf in list:
        gf.accept(self)
        
  def visitRegularObject( self, objectTypeString, gf ):
      """ Generates the graphical code for common objects """
    
      f = self.f
      indent = self.MI
      coordList = gf.getCoords()  
      gfName = "gf" + str( gf.getObjectNumber() )

      f.write(indent+'h = drawing.create_'+objectTypeString+'(self.translate(')
      f.write( str(coordList)+'), tags = self.tag')
      f.write(', stipple = \''  + str( gf.getStipple() ) + '\'' )
      f.write(', width = '      + str( gf.getWidth()   )        )
      
      if( objectTypeString != 'line' ):
        if( gf.getOutlineOption() ): color = gf.getOutlineColor()
        else:                        color = ''
        f.write(', outline = \''  + str( color           ) + '\'' )
      
      if( objectTypeString == 'line' or gf.getFillOption() ):    color = gf.getFillColor()
      else:                        color = '' 
      f.write(', fill = \''     + str( color         ) + '\'' )
      
      # Extra options for lines & polygons
      if( objectTypeString == 'line' or objectTypeString == 'polygon'  ):
        f.write(', smooth = \''   + str( gf.getSmooth()    ) + '\'' )
        f.write(', splinesteps =  \'12\'' )
      
      # Extra options just for lines (cause they're special)
      if( objectTypeString == 'line' ):
        f.write(', capstyle = \'' + str( gf.getCapstyle()  ) + '\'' )
        f.write(', joinstyle = \''+ str( gf.getJoinstyle() ) + '\'' )   
        if( gf.getArrow() ):
          f.write(', arrow = \''    + str( gf.getArrow()     ) + '\'' )
          f.write(', arrowshape = (15,15,3)')
        
      f.write(')\n' )

      f.write(indent+'self.'+gfName+' = GraphicalForm(drawing, h, "'+gfName+'")\n')
      f.write(indent+'self.graphForms.append(self.'+gfName+')\n\n')
        
      
 

  def generateHeaderCode(self, f, name, classIndent, methodIndent  ):
  
      f.write('"""\n')
      f.write("__"+ name +".py___________________________________________________________\n")
      f.write("\n")
      f.write("Automatically generated graphical appearance ---> MODIFY DIRECTLY WITH CAUTION\n")
      f.write("__"+ len(name+'.py')*"_" +"___________________________________________________________\n")
      f.write('"""\n')
      f.write('import tkFont\n\n')
      f.write('from graphEntity     import *\n')
      f.write('from GraphicalForm   import *\n')
      f.write('from ATOM3Constraint import *\n\n')      
      f.write('class ' + name + '(graphEntity):\n\n')
      
      f.write(classIndent+'def __init__(self, x, y, semObject = None):\n')
      
      f.write(methodIndent+'self.semanticObject = semObject\n')
      
      f.write(methodIndent+'self.sizeX, self.sizeY = '+str(self.size[0])+', '+str(self.size[1])+'\n')
      f.write(methodIndent+'graphEntity.__init__(self, x, y)\n')

      if( self.editor.scripting.getRunTimeChange() ):                       
          f.write(methodIndent+'self.ChangesAtRunTime = 1\n')     
      else:                                                  
          f.write(methodIndent+'self.ChangesAtRunTime = 0\n')       
  
      # Write the list of constraints...
      f.write(methodIndent+'self.constraintList = []\n')
      f.write(methodIndent+'if self.semanticObject: atribs = self.semanticObject.attributesToDraw()\n')
      f.write(methodIndent+'else: atribs = None\n')
           
      for cvalue in self.constraintList:                                  
          #cvalue = obj.getValue()
          f.write('\n'+methodIndent+'constObj = ATOM3Constraint(atribs,"'+cvalue[0]+'","self.semanticObject.", [], [])\n') # write constraint creation
          f.write(methodIndent+'constObj.setValue('+str(cvalue)+')\n')
          f.write(methodIndent+'self.constraintList.append(constObj)\n')
      
      
      # A list of GraphicalForms
      f.write(methodIndent+'self.graphForms = []\n')		
      
      # A dictionary of images
      f.write(methodIndent+'self.imageDict = self.getImageDict()\n\n')		
  
      # The beginning of the drawing specification
      f.write(classIndent+'def DrawObject(self, drawing, showGG = 0):\n')
      f.write(methodIndent+'self.dc = drawing\n')
      f.write(methodIndent+'if showGG and self.semanticObject: self.drawGGLabel(drawing)\n')
  
  def generateFooterCode( self, f, name, classIndent, methodIndent ):
                        
      # generate the constraint functions...
      for cvalue in self.constraintList:#.getValue():
        #cvalue = const.getValue()                                                  # a tuple
        cname  = cvalue[0]                                                  # compose the function name
        
        # Change added by Spencer Borland (sborla@cs.mcgill.ca)
        # added 'params' parameter to GRAPHICAL constraint functions so that
        # params is accessible here as well as in the semantic constraint functions
        f.write('\n'+classIndent+'def '+cname+'(self,params):\n')    # 1st. value is the name
        f.write(methodIndent+string.replace(cvalue[4],'\n', '\n'+methodIndent))             # 4th. value is the code
      
      # Generate the constraints handlers...
      f.write("\n\n")
      f.write(classIndent+"def postCondition( self, actionID, * params):\n")
      self.writeCondition( 1, f,methodIndent)               # 1 = POSTcondition
      f.write(methodIndent+"return None\n\n")
      f.write(classIndent+"def preCondition( self, actionID, * params):\n")
      self.writeCondition( 0, f,methodIndent)               # 0 = PREcondition
      f.write(methodIndent+"return None\n\n")
      
      # Generate the image data
      f.write(classIndent+"def getImageDict( self ):\n" ) 	
      f.write(methodIndent+'imageDict = dict()\n\n')		
      IMAGE_DICT = Graphics.Image.IMAGE_DICT
      for filename in IMAGE_DICT.keys():
        f.write(methodIndent+'imageDict[ \''+filename+'\' ] = \'\'' )
        for i in range(0,len( IMAGE_DICT[filename] ), 80 ):
          f.write( "+\\\n'"+IMAGE_DICT[filename][ i : i + 80 ] + "'" )
        f.write(methodIndent+'\n\n')		
      f.write(methodIndent+'return imageDict\n\n')
      
      
      f.write('new_class = ' + name + '\n')
      f.close()
      
  def writeCondition(self, which, file, methodIndent):
       """ Writes the constraint invocation in the file """
       for condition in self.constraintList: #.getValue():
          name, language, kind, actions, code = condition #.getValue()
          if which == kind[1]:                          # same kind...
             listAct, selAct = actions
             file.write(methodIndent+"if actionID == ")
             conta = 0
             writed = 0
             for event in selAct:
                 if event == 1:
                    if not writed:
                       file.write(" self."+listAct[conta])
                    else:
                       file.write(" or actionID == self."+listAct[conta])
                    writed = 1
                 conta = conta + 1
             file.write(":\n")

             # Change added by Spencer Borland (sborla@cs.mcgill.ca)
             # added 'params' parameter to GRAPHICAL constraint functions so that
             # params is accessible here as well as in the semantic constraint functions
             file.write(methodIndent+"     res = self."+name+"(params)\n")
             file.write(methodIndent+"     if res: return res\n")
      
      
