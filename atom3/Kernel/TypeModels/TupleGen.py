# _ TupleGen.py ____________________________________________________________________________
# File generated automatically by ATOM3. Graph Grammar Rule
# ___________________________________________________________________________________________
from GGrule import *
from ASG_TypesMetaModel import *
from ModelType import *
from Operator import *
from TypeName import *
from LeafType import *
class TupleGen (GGrule):

   def __init__(self, parent):
      GGrule.__init__(self, 1)
      self.TimeDelay = ATOM3Integer(2)
      self.exactMatch = 1
      self.LHS = ASG_TypesMetaModel(parent)

      self.obj25=Operator(parent)

      self.obj25.type.setValue( (['X', 'U', '->'], 0) )
      self.obj25.type.config = 0
      self.obj25.GGLabel.setValue(1)
      self.obj25.graphClass_= graph_Operator
      if parent.genGraphics:
         from graph_Operator import *
         new_obj = graph_Operator(208.0,271.0,self.obj25)
      else: new_obj = None
      self.obj25.graphObject_ = new_obj
      self.LHS.addNode(self.obj25)
      self.RHS = ASG_TypesMetaModel(parent)

      self.obj27=Operator(parent)

      self.obj27.type.setValue( (['X', 'U', '->'], 0) )
      self.obj27.type.config = 0
      self.obj27.GGLabel.setValue(1)
      self.obj27.graphClass_= graph_Operator
      if parent.genGraphics:
         from graph_Operator import *
         new_obj = graph_Operator(205.0,255.0,self.obj27)
      else: new_obj = None
      self.obj27.graphObject_ = new_obj
      self.obj270= AttrCalc()
      self.obj270.Copy=ATOM3Boolean()
      self.obj270.Copy.setValue(('Copy from LHS', 1))
      self.obj270.Copy.config = 0
      self.obj270.Specify=ATOM3Constraint()
      self.obj270.Specify.setValue(('AttrSpecify', (['Python', 'OCL'], 1), (['PREcondition', 'POSTcondition'], 1), (['EDIT', 'SAVE', 'CREATE', 'CONNECT', 'DELETE', 'DISCONNECT', 'TRANSFORM', 'SELECT', 'DRAG', 'DROP', 'MOVE'], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), '\n'))
      self.obj27.GGset2Any['type']= self.obj270
      self.RHS.addNode(self.obj27)
   def condition(self, graphID, isograph, atom3i):
      node = self.getMatched(graphID, self.LHS.nodeWithLabel(1))
      if node.FILE_: 		# This node has been processed yet!
        return 0
      self.generatedChilds = []
      for child in node.out_connections_:# childs have the FILE_ slot filled...
        if child.FILE_:	# if this is the case, add to list
           self.generatedChilds.append(child)
        else:
           return 0	        # otherwise, the condition does not hold...
      return 1		
      
      
      
      

   def action(self, graphID, isograph, atom3i):
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
      attributesInfo = []							 # list which contains tuples of the form: (name, type, valInitial, node)
      for node in self.generatedChilds:					# for each child that has been found...
         if counter > 0: className = className+"X"
         if(node.getClass() == 'LeafType'):					# A leaf type...
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
      
      # MODIFIED
      print "WARNING: Using file name generator fix by Denis Dube, 2006", __file__
      className = nnode.in_connections_[0].Name.getValue() + "Impl"
      # END MODIFIED
      
      nnode.FILE_=className
      
      fileName = className+".py"
      file = open(atom3i.codeGenDir +"/"+fileName, "w+t")			
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
      file.write("      ATOM3Type.__init__(self)\n")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         		# unpack element components
         file.write("      self."+name+"= None\n")			# for the moment, initialize to None...
      file.write("\n")
      # .........................................................
      # Generate the createComponents method
      # .........................................................
      file.write("   def createComponents(self):\n")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         		# unpack element components
         file.write("      if not self."+name+":\n")
         if node.getClass() == 'LeafType':                               		# we are dealing with a simple type...
             node.Type.initialValue.writeConstructor2File(file,"         ", "self."+name, 0, 1)
         else:
             file.write("         from "+type+" import *\n")			# import the class...
             file.write("         self."+name+"="+type+"()\n")
      file.write("\n")
      # .........................................................
      # Generate the show method
      # .........................................................
      file.write("   def show(self, parent, parentWindowInfo=None):\n")
      file.write("      self.createComponents()\n")
      file.write("      ATOM3Type.show(self, parent, parentWindowInfo)\n")
      file.write("      self.containerFrame = Frame(parent)\n")
      counter = 0
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         		# unpack element components
         if node.getClass() == "LeafType":				# Check if we should create an intermediate button or not
            directEditing = node.Type.getValue()[4][1]
         elif node.getClass() == "ModelType":				# Always create an intermediat button te edit models
            directEditing = 0
         else:							# direct editing for other composite types
            directEditing = 1
         file.write("      Label(self.containerFrame, text='"+name+"').grid(row="+str(counter)+",column=0,sticky=W)\n")
         if directEditing:
            file.write("      self."+name+".show(self.containerFrame, parentWindowInfo).grid(row="+str(counter)+",column=1,sticky=W)\n")
         else:
            file.write("      Button( self.containerFrame, text = 'edit', ")
            if node.getClass() == "ModelType":
               file.write("command =  lambda x=self : ATOM3TypeDialog(x.containerFrame, x."+name+", ATOM3TypeDialog.OPEN))")
            else:
               file.write("command =  lambda x=self : ATOM3TypeDialog(x.containerFrame, x."+name+"))")
            file.write(".grid(row="+str(counter)+",column=1,sticky=W)\n")
         counter = counter + 1
      file.write("      return self.containerFrame\n\n")
      # .........................................................
      # Generate the toString method
      # .........................................................
      file.write("   def toString(self):\n")
      file.write("      self.createComponents()\n")
      file.write("      return ")
      counter = 0
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         # unpack element components
         if counter: file.write("+' '+")
         file.write(" self."+name+".toString()")
         counter = counter + 1
      file.write("\n\n")
      # .........................................................
      # Generate the getValue method
      # .........................................................
      file.write("   def getValue(self):\n")
      file.write("      self.createComponents()\n")
      file.write("      return (")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         # unpack element components
         file.write("self."+name+".getValue(),")
      file.write(")\n\n")
      # .........................................................
      # Generate the setValue method
      # .........................................................
      file.write("   def setValue(self, value):\n")
      file.write("      self.createComponents()\n")
      file.write("      if value == None:\n")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         # unpack element components
         file.write("         self."+name+".setNone()\n")
      file.write("      else:\n")
      counter = 0
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         # unpack element components
         file.write("         self."+name+".setValue(value["+str(counter)+"])\n")
         counter = counter + 1
      file.write("\n")
      # .........................................................
      # Generate the writeConstructor2File method
      # .........................................................
      file.write('   def writeConstructor2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):\n')
      file.write("      self.createComponents()\n")
      file.write("      file.write(indent+objName+'= "+className+"()\\n')\n")
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         		# unpack element components
         if node.getClass() == "ModelType":
            file.write("      file.write(indent+objName+'."+name+"= "+type+"(self)\\n')\n")
            file.write("      self."+name+"writeGraph2File(file, 1, 0, objName+'."+name+"', indent, 0, genImports = 1)\n")
         file.write("      self."+name+".writeConstructor2File(file, indent, objName+'."+name+"', depth, generatingCode)\n")
      file.write("\n")
      # .........................................................
      # Generate the writeValue2File method
      # .........................................................
      file.write('   def writeValue2File(self, file, indent, objName="at", depth = 0, generatingCode = 0):\n')
      file.write("      self.createComponents()\n")
      for element in attributesInfo:					# for each element in attributesInfo...
        name, type, valInitial, node = element                         # unpack element components
        file.write("      self."+name+".writeValue2File(file, indent, objName+'."+name+"', depth, generatingCode)\n")
      file.write("\n")
      # .........................................................
      # Generate the clone method
      # .........................................................
      file.write('   def clone(self):\n')
      file.write('     "Makes an exact copy of itself"\n')
      file.write('     cloneObject = '+className+'()\n')
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         # unpack element components
         file.write('     if self.'+name+': cloneObject.'+name+' = self.'+name+'.clone()\n')
      file.write('     return cloneObject\n\n')
      # .........................................................
      # Generate the copy method
      # .........................................................
      file.write('   def copy(self, other):\n')
      file.write('     "copies each field of the other object into its own state"\n')
      file.write('     self.parent = other.parent\n')
      file.write('     self.mode   = other.mode\n')
      file.write('     self.createComponents()\n')
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         # unpack element components
         file.write('     self.'+name+'.copy(other.'+name+')\n')
      file.write('\n')
      # .........................................................
      # Generate the destroy method
      # .........................................................
      file.write('   def destroy(self):\n')
      file.write('     "Destroys (i.e. updates) each field"\n')
      #file.write('     cloneObject = '+className+'()\n')
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         # unpack element components
         file.write('     if self.'+name+': self.'+name+'.destroy()\n')
      file.write('\n')
      #file.write('     return cloneObject\n')
      # .........................................................
      # Generate the invalid method
      # .........................................................
      file.write('   def invalid(self):\n')
      file.write('     "checks whether the entity is valid or not"\n')
      file.write('     inval = 0\n')
      for element in attributesInfo:					# for each element in attributesInfo...
         name, type, valInitial, node = element                         		# unpack element components
         file.write('     if self.'+name+': inval = inval or self.'+name+'.invalid()\n')   
      file.write('     return inval\n\n')
      file.close()
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      

