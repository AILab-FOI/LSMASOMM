# __ File: apperanceDialog.py __________________________________________________________________________________________________
#  Implements  : class apperanceEditor
#  Author      : Juan de Lara
#  Description : An editor to edit graphical appearance.
#  Modified    : 23 Oct 2001
#  Changes :
#   - 26 Oct 2001 : Fixed bug, if parameter 'attribute' of constructor is None then we must initialize
#                   self.attributes to an empty list
#   - 14  Nov 2001 : Fixed bug, when being in SELECT mode (POINT_TOOL), and then move a rectangle, and then
#                   go to LINE_TOOL, an exception was raised, because self.transient_handle was not None,
#                   and attempted to manipulate a rectangle with a wrong number of coordinates (as if it were
#                   a line). Corrected it by inserting and extra condition when releasing the mouse, in drag_mode
#                   and in POINT_TOOL, then makes setlf.transient_handler = None. (method end_drag)
#		    This fix has been copied from ATOM3's previous version.
#   - 14  Jan 2002: If semObject is None in constructor, the constructr fails (self.ATOM3instance = semObject.parent). Fixed
#   - 14  Jan 2002: If semObject is None in constructor, body() fails. Fixed
#   - 11  July 2002: Added a checkbox to specify if the graphical object can change at run-time
#   - 24  July 2002: Added a names to connectors.
# ____________________________________________________________________________________________________

import tkFont
import tkFileDialog
import EZDialog
import string
import sys
import os
import tkMessageBox

from Tkinter 			    import *
from MyDialog         import *
from ATOM3Type			  import *
from ATOM3List			  import *
from ATOM3Constraint	import *
from ATOM3TypeDialog	import *
from GraphicalForm		import *

# Now import a number of objects generated with ATOM3. 
# They will be used to present/request graphical objects properties

from line                       import *
from oval                       import *
from rectangle                  import *
from polygon                    import *
from text                       import *
from connector                  import *

from GraphicEditor import Editor

class appearanceEditor(MyDialog):

   # Some useful constants

   POINT_TOOL        = 0
   LINE_TOOL         = 1
   POLYGON_TOOL      = 2
   OVAL_TOOL         = 3
   RECTANGLE_TOOL    = 4
   TEXT_TOOL         = 5
   ATTR_TOOL         = 6
   CONNECTOR_TOOL    = 7
   DELETE_TOOL       = 8
   SET_CONSTRAINT    = 9
   PROPERTIES_TOOL   = 10
   GRAPHIC_EDITOR    = 11

   PORT_STRING = "[** PORT **]"                          # String to be added to the ATOM3Port variable names

   def __init__(self, parent, title, className, attributes, semObject = None ):
      self.className  = className           		# store the class name
      #print "in appearanceEditor.ClassName="+self.className
      if not attributes:                                # attributes is None, put an empty list as the attributes
         self.attributes = []
      else:
         self.attributes = attributes                      # List of ATOM3Attributes
      self.drawnAttributes = {}		    		# Dictionary of drawn attributes, the value is the attribute graphical handle
      self.connectors = []                  		# the set of the connector's handles
      self.namedConnectors = {}                         # a dictionary with the named connectors
      self.result_ok = 0		    		# for the moment, suposse that Cancel will be pressed

      # Some necessary attributes
      self.drag_mode = 0
      self.transient_handle = None
      self.oldx = 0
      self.oldy = 0
      self.pop_x = 0
      self.pop_y = 0

      self.handles = []
      self.false_coupling = []
      self.center = (-1, -1)
      self.new_class = None

      self.gfwrappers_handle = {}					# dictionary of graphical forms, indexed by handlers
      self.numGraphForms = 0						# number of graphical forms created so far.
      self.graphFormsNames = []						# a list of graphical forms names
      # put the semantic attributes also in the list...
      for atr in self.attributes:
         atrName = atr.getValue()[0]
         self.graphFormsNames.append('semanticObject.'+atrName)

      self.constraintList = ATOM3List([1,1,1,0], ATOM3Constraint, self.graphFormsNames)	# a list of the specified graphical constraints
      if semObject:							# if we have information about the associated semantic object (modified 14-Jan-2002)
         self.ATOM3instance = semObject.parent
      else:
         self.ATOM3instance = None
         
      tkMessageBox.showinfo(  "Deprecated Appearence Dialog",
                            "The Icon-Editor supersedes this appearence dialog, please use it instead.\n\n"+
                            "WARNING: although this dialog can import Icon-Editor models it does\n"+
                            "*NOT* properly export them again.\n\n"+
                            "Note: the Icon-Editor CAN import & export all models",
                            parent = parent)  
   
         
      MyDialog.__init__(self, parent, title)

   def CancelOld():
      if self.transient_handle:
        self.drawing.delete(self.transient_handle)
      self.drag_mode = 0
      self.transient_handle = None

   def enlarge_font(self, widget, new_size):
      "sets widget font size to new_size"
      f = tkFont.Font(font = widget["font"])
      f.configure(size = new_size)
      widget.configure(font = f)

   def body(self, master):

      # ---- drawing area ----

      draw_area = Frame(master)

      bar = Label(draw_area, text = "Appearance", relief = GROOVE)
      self.enlarge_font(bar, 14)
      bar.pack(side = TOP, fill = X, ipady = 5)

      toolbar2 = Frame(draw_area)

      self.current_tool = IntVar()
      self.current_tool.set(self.POINT_TOOL)

      b = Radiobutton(toolbar2, text="Select", selectcolor = "lightblue", indicatoron = 0, value = self.POINT_TOOL, variable = self.current_tool, command= lambda x=self: x.CancelOld)
      b.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)

      b = Radiobutton(toolbar2, text="Delete", selectcolor = "lightblue", indicatoron = 0, value = self.DELETE_TOOL, variable = self.current_tool, command=lambda x=self: x.CancelOld)
      b.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)

      b = Radiobutton(toolbar2, text="Line", selectcolor = "lightblue", indicatoron = 0, value = self.LINE_TOOL, variable = self.current_tool, command=lambda x=self: x.CancelOld)
      b.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)

      b = Radiobutton(toolbar2, text="Polygon", selectcolor = "lightblue", indicatoron = 0, value = self.POLYGON_TOOL, variable = self.current_tool, command=lambda x=self: x.CancelOld)
      b.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)

      b = Radiobutton(toolbar2, text="Oval", selectcolor = "lightblue", indicatoron = 0, value = self.OVAL_TOOL, variable = self.current_tool, command=lambda x=self: x.CancelOld)
      b.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)

      b = Radiobutton(toolbar2, text="Rectangle", selectcolor = "lightblue", indicatoron = 0, value = self.RECTANGLE_TOOL, variable = self.current_tool, command=lambda x=self: x.CancelOld)
      b.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)

      b = Radiobutton(toolbar2, text="Text", selectcolor = "lightblue", indicatoron = 0, value = self.TEXT_TOOL, variable = self.current_tool, command=lambda x=self: x.CancelOld)
      b.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)

      b = Radiobutton(toolbar2, text="Attribute", selectcolor = "lightblue", indicatoron = 0, value = self.ATTR_TOOL, variable = self.current_tool, command=lambda x=self: x.CancelOld)
      b.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)

      b = Radiobutton(toolbar2, text="Connector", selectcolor = "lightblue", indicatoron = 0, value = self.CONNECTOR_TOOL, variable = self.current_tool, command=lambda x=self: x.CancelOld)
      b.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)

      b = Radiobutton(toolbar2, text="Properties", selectcolor = "lightblue", indicatoron = 0, value = self.PROPERTIES_TOOL, variable = self.current_tool, command=lambda x=self: x.CancelOld)
      b.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)

      b = Radiobutton(toolbar2, text="Set Constraint", selectcolor = "lightblue", indicatoron = 0, value = self.SET_CONSTRAINT, variable = self.current_tool, command=self.setConstraint)
      b.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)
      
      self.dynamic_change = IntVar()                                                         # changed 12-July-2002
      cbDyn = Checkbutton(toolbar2, text="Changes at run-time", variable=self.dynamic_change)    # changed 12-July-2002
      cbDyn.pack(side = TOP, fill = X, padx=2, pady=2, ipadx = 7, ipady = 5)                     # changed 12-July-2002

      toolbar2.pack(side = RIGHT, fill = Y)

      self.drawing = Canvas(draw_area, relief = SUNKEN, borderwidth = 2, width = 300, height = 300, bg = "white")
      self.drawing.pack(fill = BOTH, expand = 1)
      self.drawing.bind("<Button-1>", self.left_click)
      self.drawing.bind("<B1-Motion>", self.drag)
      self.drawing.bind("<Button-3>", self.right_click)
      self.drawing.bind("<ButtonRelease-1>", self.end_drag)
      self.drawing.bind("<Motion>", self.mouse_move)

      # ---- Attributes area -----

      attrbar = Frame(master)
      f = Frame(attrbar)
      f.pack(side = BOTTOM, fill = X)

      b = Label(attrbar, text = "Attributes", relief = GROOVE)
      self.enlarge_font(b, 14)
      b.pack(side = TOP, fill = X, ipady = 5)

      scrollbar1 = Scrollbar(attrbar, orient=VERTICAL)
      scrollbar2 = Scrollbar(attrbar, orient=HORIZONTAL)
      self.attrbox = Listbox(attrbar, yscrollcommand=scrollbar1.set, xscrollcommand=scrollbar2.set)
      
      if self.attributes:
         for atr in self.attributes:
            value = atr.getValue()                                      # Modified by JL, 24 July 2002
            if value[1] == 'Port':
              self.attrbox.insert(END, atr.getValue()[0]+self.PORT_STRING)  
            else:
              self.attrbox.insert(END, atr.getValue()[0])

      scrollbar1.config(command=self.attrbox.yview)
      scrollbar1.pack(side=RIGHT, fill=Y)
      scrollbar2.config(command=self.attrbox.xview)
      scrollbar2.pack(side=BOTTOM, fill=X)
      self.attrbox.pack(fill=BOTH, expand=1)

      # -------------------

      attrbar.pack(side = LEFT, fill = Y)
      draw_area.pack(fill = BOTH, expand = 1)

      # try to compose and load the graphical file associated with the class

      nameClass = "graph_"+self.className
      nameFile  = "graph_"+self.className+".py"

      if nameClass in sys.modules.keys():       # file has already been loaded
         #print "file already loaded..."
         del sys.modules[nameClass]

      # check if file exists
      #print "Trying to open "+nameFile

      try:
         exec "import graph_"+self.className+"\n" # in self.__dict__, self.__dict__
      except SyntaxError:							# class Name not valid (modified 14-Jan-2002)
         print "Could not open graphical file"
      except IOError:                                                           # could not open file (?)
         print "Could not open graphical file"
      except ImportError:                                                       # could not open file...
         print "Could not open graphical file"
      else:      								# We have susccessful loaded an existing graphical class
        
         separator = os.sep
        
         # compare module path and model path...
         moduleRef = str(eval('graph_'+self.className))							# obtain "<module 'xxx' from 'path/xxx.py'>"
         modulePathAndFile  = moduleRef[string.find(moduleRef, "' from '")+8:len(moduleRef)-2]		# obtain the path from the previous expression
         absOrRelModulePath, file = os.path.split(modulePathAndFile)              # eliminate file from the previous string
         modulePath = os.path.abspath(absOrRelModulePath)                               # make it absolute path
       
         # obtain model path (if self.ATOM3instance is not None)
         if self.ATOM3instance:    						# modified (14-Jan-2002)
            statusbar = self.ATOM3instance.statusbar
            modelPathAndFile = statusbar.getState(statusbar.MODEL)[1][0]
            modelPath, file = os.path.split(modelPathAndFile)            
            if modelPath == '':							# model is not saved...
               if not self.equalPaths(absOrRelModulePath, self.ATOM3instance.codeGenDir ):
                  if tkMessageBox.askyesno(
                    "A graphical appearance has been found...",
                    "Would you like to use the graphical appearance in directory"+absOrRelModulePath+"?",
                    parent = self
                  ) == 0:
                    return
            # now see if sys.path[0]+modulePath is equal to modelPath...
            elif not self.equalPaths(modelPath, modulePath):
               return
         else:                                                                  # modified (14-Jan-2002)
            return
         className = eval('graph_'+self.className+'.graph_'+self.className)     # obtain the class object
         new_obj = className(10, 10)                                            # create an instance of the new class
         new_obj.DrawObject(self.drawing)					# draw the object
         if new_obj.ChangesAtRunTime:                                           # set the check-box if the object changes at run-time (added 12-July-2002)
            self.dynamic_change.set(1)                                          # (added 12-July-2002) 
         else:                                                                  # (added 12-July-2002) 
            self.dynamic_change.set(0)                                          # (added 12-July-2002)  
         a = self.drawing.find_withtag(new_obj.tag)                             # list with the handles of all the shapes drawn
         for handle in a:							# iterate...
            if not handle in self.handles: self.handles.append(handle)		# add to the local list of handles
         # store the connectors in self.connectors
         for handle in new_obj.connectors:
             self.connectors.append(handle)                                     # add the connectors to the local list
             x0, y0, x1, y1 = self.drawing.coords(handle)
             print "Importing Connector( ", handle, " ) = ", x0,y0,x1,y1
             self.drawing.coords(handle,x0-2, y0-2, x0+2, y0+2)                 # convert it into a big dot
         # store the named connectors in self.namedConnectors                     (Added by JL, 24 July 2002)
         for handle in new_obj.namedConnectors.keys():                          # (Added by JL, 24 July 2002)
            self.namedConnectors[handle] = new_obj.namedConnectors[handle]       # (Added by JL, 24 July 2002)
         # store the drawn attributes...
         for dr_att in new_obj.attr_display.keys():				# iterate over all the semantic attributes to be drawn
             self.drawnAttributes[dr_att] = new_obj.attr_display[dr_att]	# add to the local dictionary
         # constraints!
         self.constraintList.setValue(new_obj.constraintList)
         # store the GraphicalForm objects
         for gf in new_obj.graphForms:						# iterate on the list of graphical forms...
             self.gfwrappers_handle[gf.handler] = gf				# add entry to the dictionaty of gf's
             print "Importing GF( ", gf.handler, " ) = ", self.drawing.coords(gf.handler)
             self.numGraphForms = self.numGraphForms+1
             if not gf.name in self.graphFormsNames:
                self.graphFormsNames.append(gf.name)          			# add name to the list of gf names (if not there)...
             self.drawing.tag_bind(gf.handler, "<Enter>", gf.showName)		# add bind to the callback to show the name
         # set the correct attributes for each constraint of the new object...
         for const in new_obj.constraintList:
             const.classAttribs = self.graphFormsNames
                

   def equalPaths(self, p1, p2):
      "returns if p1 and p2 are the same path"
      np2 = os.path.normpath(p2)                                           # first normalize...
      np1 = os.path.normpath(p1)
      return string.upper(np1) == string.upper(np2)                         # then compare

   def coord2handle(self, x, y):
      handles = self.drawing.find_overlapping(x - 1, y - 1, x + 1, y + 1)
      if len(handles):
         return handles[0]

   def getSize(self):
      "get the x and y size of all the drawings"
      bound = self.drawing.bbox(ALL)                    # if we dornt have anything, maybe this is None
      if bound:
         return (bound[2]-bound[0], bound[3]-bound[1])
      else:
         return (0, 0)

   def mouse_move(self, event):
      "callback function for moving the mouse..."
      if self.current_tool.get() in [self.POLYGON_TOOL, self.LINE_TOOL] and self.drag_mode:	# check if we are drawing a line or a rectangle
         coord = self.drawing.coords(self.transient_handle)
         count = len(coord)
         coord[count - 2] = event.x
         coord[count - 1] = event.y
         apply(self.drawing.coords, tuple([self.transient_handle] + coord))

   def right_click(self, event):
      if self.current_tool.get() in [self.POLYGON_TOOL, self.LINE_TOOL] and self.drag_mode:
        if self.current_tool.get() == self.POLYGON_TOOL:
            coord = self.drawing.coords(self.transient_handle)
            self.drawing.delete(self.transient_handle)
            handle = self.drawing.create_polygon(tuple(coord), fill = "", outline = "black")
            self.handles.append(handle)
            self.createNewGraphicalForm(handle)
        else:
            self.handles.append(self.transient_handle)
            self.createNewGraphicalForm(self.transient_handle)
        self.transient_handle = None
        self.drag_mode = 0

   def left_click(self, event):
      "Handles left clicks"

      if self.current_tool.get() in [self.POLYGON_TOOL, self.LINE_TOOL]:				# we are drawing a line or a polygon
        if self.transient_handle:
            coord = self.drawing.coords(self.transient_handle)
            coord.append(event.x)
            coord.append(event.y)
            apply(self.drawing.coords, tuple([self.transient_handle] + coord))
        else:
            self.drag_mode = 1
            self.transient_handle = self.drawing.create_line(event.x, event.y, event.x, event.y)
      elif self.current_tool.get() == self.POINT_TOOL:
        self.transient_handle = self.coord2handle(event.x, event.y)
        if self.transient_handle != None and 'center' not in self.drawing.gettags(self.transient_handle):
            self.drag_mode = 1
            self.oldx = event.x
            self.oldy = event.y
      elif self.current_tool.get() in [self.RECTANGLE_TOOL, self.OVAL_TOOL]:				# Drawing Rectangles or Ovals
        self.drag_mode = 1
        if self.current_tool.get() == self.RECTANGLE_TOOL:
            self.transient_handle = self.drawing.create_rectangle(event.x, event.y, event.x, event.y)
        else:
            self.transient_handle = self.drawing.create_oval(event.x, event.y, event.x, event.y)
      elif self.current_tool.get() == self.TEXT_TOOL:
        new_text = EZDialog.askstring("New Text", "Enter a text string:")
        if new_text == None:
             return
        handle = self.drawing.create_text(event.x, event.y, text = new_text)
        self.createNewGraphicalForm(handle)
        self.handles.append(handle)
      elif self.current_tool.get() == self.ATTR_TOOL:
        idx = self.attrbox_get_sel_idx()
        if idx == None:
           return
        self.drawAttribute(idx, event.x, event.y)
      elif self.current_tool.get() == self.CONNECTOR_TOOL:
        connHandle = self.drawing.create_oval(event.x, event.y, event.x+4, event.y+4, fill="red" )
        self.handles.append( connHandle )
        self.connectors.append( connHandle )
      elif self.current_tool.get() == self.DELETE_TOOL:
        self.deleteClosest(event)
      elif self.current_tool.get() == self.SET_CONSTRAINT:
        self.setConstraint(event)
      elif self.current_tool.get() == self.PROPERTIES_TOOL:
        self.showItemProperties(self.coord2handle(event.x, event.y))

   def drawAttribute ( self, idx, px, py ):
       """
          Plot the attribute "idx" in the canvas in the position (px, py).
          If the attribute is a PORT, the draws it as a (blue) connector.
          Created 24 July 2002 by JL.
       """
       # See if it is a port (the string finishes with self.PORT_STRING)
       pos = string.find(idx, self.PORT_STRING)
       if pos > -1:                # it is a port
          connHandle = self.drawing.create_oval(px, py, px+4, py+4, fill="blue" )
          self.handles.append( connHandle )
          self.connectors.append( connHandle )
          self.namedConnectors[ connHandle ] = idx[:pos]
       else:                                                      # it is a regular attribute
          self.drawnAttributes[idx] = self.drawing.create_text(px, py, text = '<' + idx + '>', fill = "blue")
          self.createNewGraphicalForm(self.drawnAttributes[idx])

   def showItemProperties(self, handler):
       """
          Shows the properties of the given handler (which can be None).
       """
       if not handler: return                                        # if no handler, then nothing to do
       if self.namedConnectors.has_key(handler):                     # A named Connector (Modified 24 July 2002, JL)
          itemObject = connector()                                   # create an object to show its properties
          itemObject.setValue((self.namedConnectors[handler], ))     # initialize it
          ATOM3TypeDialog(self, itemObject)
       else:
          itemType   = self.drawing.type(handler)                    # get the type of the graphical object
          itemObject = eval(itemType)()                              # create an object to show its properties
          for attr in itemObject.generatedAttributes.keys():         # walk through all the properties and get the value
             value = self.drawing.itemcget(handler, attr)         # get the value...
             # set the attribute value depending on its type...
             if itemObject.generatedAttributes[attr][0] == "ATOM3Integer":
                itemObject.getAttrValue(attr).setValue(int(float(value)))   # convert previously to float for cases such as "3.0"
             else:                                                # A STring, so nothing special to do
                itemObject.getAttrValue(attr).setValue(value)        # set the value in the object
          # Open a dialog window so that the user can change those values
          ma_ok = ATOM3TypeDialog(self, itemObject)
          if ma_ok.result_ok:                                     # if the user said 'ok', then set the attributes in the graphical object
             attr_dict = {}                                       # A dictionary with the new values
             for attr in itemObject.generatedAttributes.keys():   # walk through all the properties and get the value
                attr_dict[attr] = itemObject.getAttrValue(attr).getValue()
             self.drawing.itemconfig(handler, attr_dict)

   def setConstraint(self):
       "Sets a graphical constraints"
       vcm = ATOM3TypeDialog(self, self.constraintList)

   def deleteClosest(self, event):
       "delete the nearest thing"
       ct = self.drawing.find_closest(event.x, event.y)
       self.drawing.delete(ct[0])
       if ct[0] in self.handles: self.handles.remove(ct[0])
       if ct[0] in self.connectors: self.connectors.remove(ct[0])
       # see if ct[0] is in self.drawnAttributes...
       for atr in self.drawnAttributes.keys():
          if self.drawnAttributes[atr] == ct[0]:
             del self.drawnAttributes[atr]

   def drag(self, event):
       "Handles drag operations"
       if self.drag_mode:
           if self.current_tool.get() in [self.RECTANGLE_TOOL, self.OVAL_TOOL]:
               temp = self.drawing.coords(self.transient_handle)
               temp[2] = event.x
               temp[3] = event.y
               self.drawing.coords(self.transient_handle, temp[0], temp[1], temp[2], temp[3])
           elif self.current_tool.get() == self.POINT_TOOL:
               self.drawing.move(self.transient_handle, event.x - self.oldx, event.y - self.oldy)
               self.oldx = event.x
               self.oldy = event.y

   def createNewGraphicalForm(self, handle):
       name = "gf"+str(self.numGraphForms)
       self.graphFormsNames.append(name)
       self.numGraphForms = self.numGraphForms+1
       gf = GraphicalForm(self.drawing, handle, name )
       self.drawing.tag_bind(handle, "<Enter>", gf.showName )
       self.gfwrappers_handle[handle]=gf

   def end_drag(self, event):
       "Handles drop operations"
       if self.current_tool.get() not in [self.POLYGON_TOOL, self.LINE_TOOL]:
           self.drag_mode = 0
           if self.current_tool.get() in [self.RECTANGLE_TOOL, self.OVAL_TOOL]:
              self.handles.append(self.transient_handle)
              self.createNewGraphicalForm(self.transient_handle)
              self.transient_handle = None
           else: self.transient_handle = None

   def attrbox_get_sel_idx(self):
       cs = self.attrbox.curselection()
       if cs != ():
         return self.attrbox.get(cs[0])
       else:
         return None

   def back_translate(self, cur_coord):
       bound = self.drawing.bbox(ALL)
       for i in range(len(cur_coord)):
           if i % 2 == 0:
               cur_coord[i] = cur_coord[i] - bound[0]
           else:
               cur_coord[i] = cur_coord[i] - bound[1]
       return cur_coord

   def writeGraphicalAttributes( self, file, handler, isSemantic):
       """
          Prints in file the attributes of the handler. isSemantic is a flag that indicates if the attribute is the text
          of a semantic attribute.
       """
       objectType = self.drawing.type(handler)                     # get the objects type
       propObject = eval(objectType)()                             # create an object
       for attr in propObject.generatedAttributes.keys():
          if isSemantic and attr == "text":                         # this case is done outside this function!
             pass
          else:
             attrValue = self.drawing.itemcget(handler, attr)
             if attr == "smooth":                                    # uhm! handle it separatelly, a strange case...
                if attrValue != "0" and attrValue != "":
                   file.write(", "+attr+"= 1")
                else: file.write(", "+attr+"= 0")
             elif type(attrValue) == StringType:
                file.write(", "+attr+"= '"+attrValue+"'")
             else:
                file.write(", "+attr+"= "+str(attrValue))       

   def apply(self):
       #todo: apply / generate code
       name = "graph_"+self.className       
       showDialog = True
       
       if( self.ATOM3instance):    	
            statusbar = self.ATOM3instance.statusbar         
            modelPathAndFile = statusbar.getState(statusbar.MODEL)[1][0]
            modelPath = os.path.split(modelPathAndFile)[0]
            if( modelPath != '' ):
              fileName = os.path.join( modelPath, name + '.py' )
              showDialog = False
              
       if( showDialog ):
            fileName = tkFileDialog.asksaveasfilename(filetypes=[("Appearence file", "*.py")], 
                                                     initialfile=name+'.py',
                                                     title='Generating graphical appearence file' )
                                                     
             
       if( fileName[-3:] != '.py'  ): return
       f = open( fileName, "w+t" )
             
       if f == None:
    	  return
       sx, sy = self.getSize()
       if sx == 0 and sy == 0:                          # ey, we don't have any drawing!
          f.close()
          try:
            os.remove(fileName)
            os.remove(fileName+'c')     # can fail!
          except OSError:
            pass
          return 
 
       f.write('from graphEntity          import *\n')
       f.write('from GraphicalForm   import *\n')
       f.write('from ATOM3Constraint import *\n\n')
       f.write('class ' + name + '(graphEntity):\n\n    def __init__(self, x, y, semObject = None):\n')
       f.write('        self.semanticObject = semObject\n')
       
       f.write('        self.sizeX, self.sizeY = '+str(sx)+', '+str(sy)+'\n')
       f.write('        graphEntity.__init__(self, x, y)\n')
       if self.dynamic_change.get():                           # changed 11-July-2002
          f.write('        self.ChangesAtRunTime = 1\n')       # changed 11-July-2002
       else:                                                   # changed 11-July-2002
          f.write('        self.ChangesAtRunTime = 0\n')       # changed 11-July-2002d

       #print "self.center = ", self.center
       if -1 not in self.center:
           f.write('        self.center = self.translate(' + str(self.back_translate(list(center))) + ')\n')
       # write the list of constraints...
       f.write('        self.constraintList = []\n')
       f.write('        if self.semanticObject: atribs = self.semanticObject.attributesToDraw()\n')
       f.write('        else: atribs = None\n')
       for obj in self.constraintList.getValue():                                          # for each constraint
           cvalue = obj.getValue()
           f.write('        constObj = ATOM3Constraint(atribs,"'+cvalue[0]+'","self.semanticObject.", [], [])\n') # write constraint creation
           f.write('        constObj.setValue('+str(cvalue)+')\n')
           f.write('        self.constraintList.append(constObj)\n\n')
       f.write('        self.graphForms = []\n')		# A list of GraphicalForms


       f.write('\n    def DrawObject(self, drawing, showGG = 0):\n')
       f.write('        self.dc = drawing\n')
       f.write('        if showGG and self.semanticObject: self.drawGGLabel(drawing)\n')

       # create a list (attrHandles) with the drawn semantic attributes handles
       attrHandles = []
       for attr in self.drawnAttributes.keys():
          attrHandles.append(self.drawnAttributes[attr])
       for i in self.handles:
          if not i in attrHandles:  # if it is NOT a drawn attribute handler
             objectType = self.drawing.type(i)                     # get the objects type
             f.write('        h = drawing.create_' + objectType + '(self.translate(')
             if i in self.connectors:                              # if the handle is a connector, compress it into an invisible dot
                x0, y0, x1, y1 = self.drawing.coords(i)
                coordins = [x0+2, y0+2, x0+2, y0+2]
             else:
                coordins = self.drawing.coords(i)
             if i in self.connectors:                              # if the handle is a connector, add a special tag
                print "Exporting Connector( ", i ," ) = ", self.back_translate(coordins)
                f.write(str(self.back_translate(coordins)) + '), tags = (self.tag, "connector")')
             else:
                print "Exporting GF( ", i ," ) = ", self.back_translate(coordins)
                f.write(str(self.back_translate(coordins)) + '), tags = self.tag')
             self.writeGraphicalAttributes( f, i, 0)
             f.write(")\n")
                
             if i in self.connectors:                              # if the handle is a connector, add to the list
                f.write('        self.connectors.append(h)\n')
                if self.namedConnectors.has_key(i):                # if it is also a named connector (modified 24 July 2002 by JL)
                   f.write('        self.namedConnectors[h] = "'+self.namedConnectors[i]+'"\n')
             else:
                gf = self.gfwrappers_handle[i]                
                f.write('        self.'+gf.name+' = GraphicalForm(drawing, h, "'+gf.name+'")\n')
                f.write('        self.graphForms.append(self.'+gf.name+')\n')
       # now draw the semantic attributes
       for i in self.drawnAttributes.keys():
          f.write('        if self.semanticObject: drawText = self.semanticObject.'+ i+'.toString(25,5)\n')
          f.write('        else: drawText = "<'+i+'>"\n')
          f.write('        h = drawing.create_text(self.translate(')
          attrHandle = self.drawnAttributes[i]
          f.write(str(self.back_translate(self.drawing.coords(attrHandle))) + '), tags = self.tag, text = drawText')
          self.writeGraphicalAttributes( f, attrHandle, 1)
          f.write(')\n')
          f.write('        self.attr_display[\"' + i + '\"] = h\n')
          gf = self.gfwrappers_handle[attrHandle]
          f.write('        self.'+gf.name+' = GraphicalForm(drawing, h, "'+gf.name+'")\n')
          f.write('        self.graphForms.append(self.'+gf.name+')\n')

       # generate the constraint functions...
       for const in self.constraintList.getValue():
           cvalue = const.getValue()                                                  # a tuple
           cname  = cvalue[0]                                                  # compose the function name

           # Change added by Spencer Borland (sborla@cs.mcgill.ca)
           # added 'params' parameter to GRAPHICAL constraint functions so that
           # params is accessible here as well as in the semantic constraint functions
           f.write('\n    def '+cname+'(self,params):\n')    # 1st. value is the name

           f.write('       '+string.replace(cvalue[4],'\n', '\n       '))             # 4th. value is the code
       # generate the constrains handlers...
       f.write("\n\n")
       f.write("    def postCondition (self, actionID, * params):\n")
       self.writeCondition( 1, f)               # 1 = POSTcondition
       f.write("       return None\n\n")
       f.write("    def preCondition (self, actionID, * params):\n")
       self.writeCondition( 0, f)               # 0 = PREcondition
       f.write("       return None\n\n")
       f.write('\nnew_class = ' + name + '\n')
       f.close()

   def writeCondition(self, which, file):
       "Writes the constraint invokation in the file"
       for condition in self.constraintList.getValue():
          name, language, kind, actions, code = condition.getValue()
          if which == kind[1]:                          # same kind...
             listAct, selAct = actions
             file.write("       if actionID == ")
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
             file.write("         res = self."+name+"(params)\n")
             file.write("         if res: return res\n")


