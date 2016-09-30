# _ UnionGen.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from ASG_TypesMetaModel import *
from ModelType import *
from Operator import *
from TypeName import *
from LeafType import *
class UnionGen (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_TypesMetaModel(parent)

      self.obj32=Operator(parent)

      self.obj32.type.setValue( (['X', 'U', '->'], 1) )
      self.obj32.type.config = 0
      self.obj32.GGLabel.setValue(1)
      self.obj32.graphClass_= graph_Operator
      if parent.genGraphics:
         from graph_Operator import *
         new_obj = graph_Operator(215.0,300.0,self.obj32)
      else: new_obj = None
      self.obj32.graphObject_ = new_obj
      self.LHS.addNode(self.obj32)
      self.RHS = ASG_TypesMetaModel(parent)

      self.obj34=Operator(parent)

      self.obj34.type.setValue( (['X', 'U', '->'], 1) )
      self.obj34.type.config = 0
      self.obj34.GGLabel.setValue(1)
      self.obj34.graphClass_= graph_Operator
      if parent.genGraphics:
         from graph_Operator import *
         new_obj = graph_Operator(226.0,344.0,self.obj34)
      else: new_obj = None
      self.obj34.graphObject_ = new_obj
      self.obj340= AttrCalc()
      self.obj340.Copy=ATOM3Boolean()
      self.obj340.Copy.setValue(('Copy from LHS', 1))
      self.obj340.Copy.config = 0
      self.obj340.Specify=ATOM3Constraint()
      self.obj340.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj34.GGset2Any['type']= self.obj340
      self.RHS.addNode(self.obj34)
   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      if node.FILE_: 						# This node has been processed yet!
         return 0
      
      self.generatedChilds = []
      for child in node.out_connections_:			# All childs must have the FILE_ slot filled...
         if child.FILE_:					# if this is the case, add to list
            self.generatedChilds.append(child)
         else:
            return 0						# otherwise, the condition does not hold...
      return 1	
      
      

   def action(self, graphID, isograph, atom3i):
      "action performed when the rule is applied "
      
      def getElementFromName (list, name):
         for element in list:
            if element.getClass() == "LeafType":
               if element.Type.getValue()[0] == name: return element
            elif name == element.getClass() == "ModelType":
               if element.MetaModelName.toString() == name: return element
         return None
      
      nnode = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      AT3Types = ['Enum', 'String', 'Integer', 'Float', 'List', 'Attribute', 'Boolean', 'Connection', 'Port', 'Constraint', 'Appearance', 'BottomType', 'File', 'Link']
      # compose the class name
      className = ""
      counter = 0
      attributesInfo = []
      for node in self.generatedChilds:					# for each child that has been found...
         if counter > 0: className = className+"U"
         if node.getClass() == 'LeafType':
            className = className + node.Type.getValue()[0]			# append the name of the element
            val = node.Type.getValue()
            if val[1] in AT3Types: attributesInfo.append((val[0], 'ATOM3'+val[1], val[2], node))
            else: attributesInfo.append((val[0], val[1], val[2], node))
         elif node.getClass() == 'ModelType':					# A "Model" node...
            className += node.MetaModelName.toString()			# add the MetaModel name to the class...
            attributesInfo.append(( node.Name.toString(), "ASG_"+node.MetaModelName.toString(), None, node))	# add info. to the attributesInfo list
         else:
            className = className + node.FILE_
            attributesInfo.append((node.FILE_, node.FILE_, None, node))
         counter = counter + 1
      print "performing action! className = ", className
      ind = "     "
      nnode.FILE_=className
      fileName = className+".py"
      file = open(atom3i.codeGenDir+"/"+fileName, "w+t")			
      file.write("from Tkinter import *\n")					
      file.write("from ATOM3Type import *\n")
      # generate imports...
      imports = []
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         		# unpack element components
         if not type in imports: imports.append(type)
         if type == "ATOM3List":					# should look for the initialValue
              element = getElementFromName ( self.generatedChilds, name )
              if element.getClass() == "LeafType" and element.Type.initialValue:
                 initialItems = element.Type.initialValue.getValue()				# get a list of items...
                 for item in initialItems:
                   if not item.getTypeName() in imports: imports.append(item.getTypeName())
                 if element.Type.initialValue.itemType:
                    if not element.Type.initialValue.itemType.__name__ in imports: imports.append(element.Type.initialValue.itemType.__name__)
      for type in imports:
         file.write("from "+type+" import "+type+"\n")
      file.write("class "+className+" (ATOM3Type):\n")
      file.write("   def __init__(self):\n")
      # .........................................................
      # Generate the __init__ method
      # .........................................................
      file.write(ind+"ATOM3Type.__init__(self)\n")
      file.write(ind+"self.optMenu = None\n")
      file.write(ind+"self.selected= None\n")
      file.write(ind+"self.lastSelected= None\n")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+"self."+name+"= None\n")			# for the moment, initialize to None...
      file.write("\n")
      # .........................................................
      # Generate the createComponents method
      # .........................................................
      file.write("   def createComponents(self):\n")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+"if not self."+name+":\n")
         if node.getClass() == 'LeafType': # we are dealing with a simple type...
            node.Type.initialValue.writeConstructor2File(file,ind+"   ", "self."+name, 0, 1)
         elif node.getClass() == 'ModelType':			# a model
            file.write(ind+"   from "+type+" import "+type+"\n")	# import the class...
            file.write(ind+"   self."+name+"="+type+"()\n")      
         else:
            file.write(ind+"   from "+name+" import *\n")		# import the class...
            file.write(ind+"   self."+name+"="+type+"()\n")
      file.write("\n")
      # .........................................................
      # Generate the show method
      # .........................................................
      file.write("   def show(self, parent, parentWindowInfo=None):\n")
      file.write(ind+"ATOM3Type.show(self, parent, parentWindowInfo)\n")
      file.write(ind+"self.createComponents()\n")
      file.write(ind+"self.showParent = parent\n")
      file.write(ind+"self.parentWindowInfo = parentWindowInfo\n")
      file.write(ind+"self.selected = StringVar()\n")
      file.write(ind+"if not self.lastSelected:\n")
      # make 1st element selected...
      name, type, valInitial, node = attributesInfo[0]
      file.write(ind+"   self.selected.set('"+name+"')\n")
      file.write(ind+"else:\n")
      file.write(ind+"   self.selected.set(self.lastSelected)\n")
      
      file.write(ind+"self.label = None\n")
      file.write(ind+"self.widget = None\n")
      file.write(ind+"self.containerFrame = Frame(parent)\n")
      file.write(ind+"Label(self.containerFrame, text='Select Attribute').grid(row=0,column=0,sticky=W)\n")
      file.write(ind+"self.optMenu = OptionMenu(self.containerFrame, self.selected")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(",'"+name+"'")
      file.write(")\n")
      file.write(ind+"self.selected.trace_variable( 'w', self.valueChanged)\n")
      file.write(ind+"self.optMenu.grid(row=0,column=1,sticky=W)\n")
      counter = 0
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         if counter == 0:
            file.write(ind+"if self.lastSelected == '"+name+"':\n")
         else:
            file.write(ind+"elif self.lastSelected == '"+name+"':\n")
         file.write(ind+"      self.destroyAllBut(self."+name+")\n")
         file.write(ind+"      self.show"+name+"(self.showParent, self.parentWindowInfo)\n")
      file.write(ind+"return self.containerFrame\n\n")
      # .........................................................
      # Generate the valueChanged method
      # .........................................................
      file.write("   def valueChanged(self, param1, param2, param3):\n")
      counter = 0
      file.write(ind+"value = self.selected.get()\n")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         if counter == 0:
            file.write(ind+"if value == '"+name+"':\n")
         else:
            file.write(ind+"elif value == '"+name+"':\n")
         file.write(ind+"   if self.lastSelected != '"+name+"':\n")
         file.write(ind+"      self.destroyAllBut(self."+name+")\n")
         file.write(ind+"      self.show"+name+"(self.showParent, self.parentWindowInfo)\n")
      # .........................................................
      # Generate the destroyAllBut method
      # .........................................................
      file.write("   def destroyAllBut(self, survivor):\n")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+"if survivor != self."+name+":\n")
         file.write(ind+"   self."+name+".destroy()\n")
      file.write("\n")
      # .........................................................
      # Generate the show<name> method
      # .........................................................
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write("   def show"+name+"(self, parent, parentWindow = None):\n")
         file.write(ind+"if self.label and self.widget:\n")
         file.write(ind+"   self.label.grid_forget()\n")
         file.write(ind+"   self.widget.grid_forget()\n")
      
         if node.getClass() == "LeafType":				# Check if we should create an intermediate button or not
            directEditing = node.Type.getValue()[4][1]
         elif node.getClass() == "ModelType":				# Always create an intermediat button te edit models
            directEditing = 0
         else:							# direct editing for other composite types
            directEditing = 1
      
         file.write(ind+"self.label = Label(self.containerFrame, text='"+name+"')\n")
         file.write(ind+"self.label.grid(row=1,column=0,sticky=W)\n")
      
         if directEditing:
            file.write(ind+"self.widget = self."+name+".show(self.containerFrame, self.parentWindowInfo)\n")
            file.write(ind+"self.widget.grid(row=1,column=1,sticky=W)\n")
         else:
            file.write(ind+"Button( self.containerFrame, text = 'edit', ")
            if node.getClass() == "ModelType":
               file.write("command =  lambda x=self : ATOM3TypeDialog(x.containerFrame, x."+name+", ATOM3TypeDialog.OPEN))")
            else:
               file.write("command =  lambda x=self : ATOM3TypeDialog(x.containerFrame, x."+name+"))")
            file.write(".grid(row=1,column=1,sticky=W)\n")
          
         file.write(ind+"self.lastSelected = '"+name+"'\n")
         file.write("\n")
      # .........................................................
      # Generate the toString method
      # .........................................................
      file.write("   def toString(self, fils = 25, cols = 5):\n")
      file.write(ind+"self.createComponents()\n")
      file.write(ind+"if self.selected:\n")
      file.write(ind+"   value = self.selected.get()\n")
      file.write(ind+"elif self.lastSelected:\n")
      file.write(ind+"   value = self.lastSelected\n")   
      file.write(ind+"else:\n")
      file.write(ind+"   value = None\n")
      counter = 0
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         if counter==0: file.write(ind+"if value == '"+name+"':\n")
         else:file.write(ind+"elif value == '"+name+"':\n")
         file.write(ind+"   return self."+name+".toString(fils, cols)\n")
         counter = counter + 1
      file.write(ind+"return ''\n")
      file.write("\n")
      # .........................................................
      # Generate the getValue method
      # .........................................................
      file.write("   def getValue(self):\n")
      file.write(ind+"self.createComponents()\n")
      file.write(ind+"return (")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write("self."+name+".getValue(),")
      file.write(")\n\n")
      # .........................................................
      # Generate the setValue method
      # .........................................................
      file.write("   def setValue(self, value):\n")
      file.write(ind+"self.createComponents()\n")
      file.write(ind+"if value == None:\n")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+"   self."+name+".setNone()\n")
      file.write(ind+"else:\n")
      counter = 0
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+"   self."+name+".setValue(value["+str(counter)+"])\n")
         counter = counter + 1
      file.write("\n")
      # .........................................................
      # Generate the writeConstructor2File method
      # .........................................................
      file.write('   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):\n')
      file.write(ind+"self.createComponents()\n")
      file.write(ind+"file.write(indent+objName+'= "+className+"()\\n')\n")
      file.write(ind+"if self.lastSelected:\n")
      file.write(ind+"   file.write(indent+objName+'.lastSelected= "+'"'+"'+self.lastSelected+'"+'"'+"\\n')\n")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+"   if self.lastSelected == '"+name+"' :\n") 
         file.write(ind+"      file.write(indent+'from "+type+" import "+type+"\\n')\n")    
         file.write(ind+"      file.write(indent+objName+'."+name+" = "+type+"()\\n')\n")    
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+"self."+name+".writeConstructor2File(file, indent, objName+'."+name+"', depth, generatingCode)\n")
      file.write("\n")
      # .........................................................
      # Generate the writeValue2File method
      # .........................................................
      file.write('   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):\n')
      file.write(ind+"self.createComponents()\n")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+"if self.lastSelected == '"+name+"' :\n") 
         file.write(ind+"   file.write(indent+'from "+type+" import "+type+"\\n')\n")    
         file.write(ind+"   file.write(indent+objName+'."+name+" = "+type+"()\\n')\n")    
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+"self."+name+".writeValue2File(file, indent, objName+'."+name+"', depth, generatingCode)\n")
      file.write(ind+"if self.lastSelected:\n")
      file.write(ind+"   file.write(indent+objName+'.lastSelected= "+'"'+"'+self.lastSelected+'"+'"'+"\\n')\n")
      file.write("\n")
      # .........................................................
      # Generate the clone method
      # .........................................................
      file.write('   def clone(self):\n')
      file.write(ind+'"Makes an exact copy of itself"\n')
      file.write(ind+'cloneObject = '+className+'()\n')
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+'if self.'+name+': cloneObject.'+name+' = self.'+name+'.clone()\n')
      file.write(ind+'cloneObject.lastSelected = self.lastSelected\n')
      file.write(ind+'return cloneObject\n')
      # .........................................................
      # Generate the copy method
      # ........................................................
      file.write('   def copy(self, other):\n')
      file.write(ind+'"Copies the content of other into itself"\n')
      file.write(ind+'ATOM3Type.copy(self, other)\n')
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+'self.'+name+' = other.'+name+'\n')
      file.write(ind+'ASGNode.copy(self,other)\n')
      # .........................................................
      # Generate the destroy method
      # .........................................................
      file.write('   def destroy(self):\n')
      file.write(ind+'"Destroys (i.e. updates) each field"\n')
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element # unpack element components
         file.write(ind+'if self.'+name+': self.'+name+'.destroy()\n')
      file.write('\n\n')
      # .........................................................
      # Generate the invalid method
      # .........................................................
      file.write('   def invalid(self):\n')
      file.write('     "checks whether the entity is valid or not"\n')
      file.write('     inval = 0\n')
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         # unpack element components
         file.write('     if self.'+name+': inval = inval or self.'+name+'.invalid()\n')
      file.write('     return inval\n\n')
      file.close()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      

