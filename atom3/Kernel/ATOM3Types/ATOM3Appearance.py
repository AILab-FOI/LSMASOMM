# __ ATOM3Appearance.py __________________________________________________________________________________________________
#  Implements  : class ATOM3Appearance
#  Author      : Juan de Lara
#  Description : class that implements an appearance attribute. The widget is just a button that enables to open an appearanceDialog
#  Modified    : 23 Nov 2001
#  Changes :
#   - 23 Nov 2001 : Fixed bug, function writeConstructor2File does not pass all the parameters to writeValue2File. This last function
# 		    has also been modified in the case of the flag generatingCode == 1. COpied from old version of ATOM3
#   - 14 Jan 2002 : If semObject is None the method showAppDialog fails. Fixed
#   - 14 Jan 2002: If a variable of this type is the initial value of an ATOM3Attribute, then if we save it, it won't work. Fixed
#		  bug in writeValue2File
#   - 15 Jan 2002: If a variable of this type is writen inside an icon, it fails because toString() did not have the appropriate parameters. Fixed
# ____________________________________________________________________________________________________________________

from Tkinter          import *
from ATOM3Type        import *
#from appearanceDialog import *
#from GraphicEditor import Editor
from GraphicEditor.GraphicEditor import Editor


class ATOM3Appearance(ATOM3Type):
    def __init__(self, className = None, semObject = None ):
       " className is the class name, attrList is an ATOM3List(ATOM3Attribute)"
       self.appDialog = None				# at first, the dialog is hidden
       self.className = className			# we should have a class name, in order to store all the information in a file...
       self.semObject = semObject 			# List of ATOM3Attributes
       self.editButton= None				# the button to edit is also hidden
       self.pWindow   = None
       self._isNone   = 0
       ATOM3Type.__init__(self)				# call ancestor

    def show(self, parent, topWindowParent = None ):
       "method to show the button to edit the appearance"
       ATOM3Type.show(self, parent, topWindowParent )
       self.editButton = Button ( parent, text="edit", command = lambda x = (self, parent): x[0].showAppDialog(x[1]) )
       return self.editButton

    def showAppDialog(self, parent):
       "shows the appearandeDialog"
       if( self.className == None ):  self.className = ""
       if( not self.semObject ):
         import tkMessageBox
         tkMessageBox.showerror( "Icon Editor Error",
                            "Could not open the graphical appearance editor "
                            +"because no semantic object was provided!"+
                            "\n\nPlease inform Denis at d3n14@yahoo.com if and "+
                            "how this error occured." )
         return
       Editor( self.semObject, self.className)#self.semObject.name.getValue() )
       
       return
      
       """
       if self.semObject:				# if we have information about the associated semantic object (modified 14 Jan 2002)
          self.appDialog = appearanceEditor ( parent, "Editing appearance of class "+self.className, self.className, self.semObject.attributesToDraw(), self.semObject )
       else:						# semObject is None, so pass an empty list of attributes (modified 14 Jan 2002)
          self.appDialog = appearanceEditor ( parent, "Editing appearance of class "+self.className, self.className, [], self.semObject )
       """
       
    def destroy (self):
       "updates attributes and destroys the graphical widget"
       pass						# actually do nothing

    def setValue(self, value):
       "sets the class name"
       if value:
         if value[0]: self.className = value[0]
         if len(value) == 2 and value[1]:
            self.semObject = value[1]

    def isNone(self):
       "checks if the value is equivalent to None"
       return self._isNone == 1

    def setNone (self):
       "sets the type value equivalent to None"
       self._isNone = 1
       return 1

    def unSetNone (self):
       "calls unSetNone on all its attributes"
       self._isNone = 0
       return 1

    def getValue(self):
       "returns the class name"
       return (self.className, self.semObject)

    def toString(self, maxWide = None, maxLines = None ):       # modified 15-Jan-2002
       "returns the file name"
       result = "graph_"+self.className+".py"
       if maxWide: return result[:maxWide]    			# modified 15-Jan-2002
       return result

    def clone(self):
       "makes an exact copy of itself"
       cloneObject = ATOM3Appearance(self.className, self.semObject)
       cloneObject.appDialog     = self.appDialog
       cloneObject.className     = self.className
       cloneObject.semObject     = self.semObject
       cloneObject.editButton    = self.editButton
       cloneObject.parent        = self.parent
       cloneObject.mode          = self.mode
       cloneObject._isNone       = self._isNone
       return cloneObject

    def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.appDialog = other.appDialog
       self.className = other.className
       self.editButton= other.editButton
       self.semObject = other.semObject
       self._isNone   = other._isNone

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+"=ATOM3Appearance()\n")
       self.writeValue2File(file, indent, objName, depth, generatingCode)

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       if generatingCode:
          file.write(indent+objName+".setValue( (self.keyword_.toString(), self))\n")
       else:
          if "." in objName:
             # check if actually we are in an ATOM3Attribute...
             secondPart = objName[string.rfind( objName, "." ):]
             if secondPart == ".initialValue":				# that means we are the initial value of an ATOM3Attribute, and we do
             								# not have an associated semantic object (modified 14-Jan-2002)
                objectName = "None"
             else:
                objectName = objName[:string.rfind( objName, "." )]	
          else:
             objectName = objName
          file.write(indent+objName+".setValue( ('"+str(self.getValue()[0])+"', "+objectName+"))\n")
       if self.isNone():
          file.write(indent+objName+".setNone()\n")


    def updateGraphicalFile(self, newClassName):
       "change the file name if the className has changed..."
       if self.className == newClassName: return                 # no change...
       if not "dirAct" in self.__dict__.keys() or not self.dirAct:
          self.dirAct = self.semObject.parent.codeGenDir
          direcs = [self.semObject.parent.codeGenDir ]
          #objs = self.semObject.parent.option.PathDirectories.getValue()
          #for dir in objs: direcs.append(dir.toString())

          # search the directory that contains graph_<oldName>
          for dir in direcs:
            if os.path.isfile(dir+"/graph_"+self.className+".py"):
               break
          else:
             self.className = newClassName
             return
          self.dirAct = dir
       oldName = "graph_"+self.className
       newName = "graph_"+newClassName
       try:
          fOld = open(self.dirAct+"/"+oldName+".py", "r+t")
       except IOError:
          self.className = newClassName
          return
       fNew = open(self.dirAct+"/"+newName+".py", "w+t")
       fNew.write(string.replace(fOld.read(), oldName, newName))
       fOld.close()
       fNew.close()
       os.remove( self.dirAct+"/"+oldName+".py")
       self.className = newClassName



       




