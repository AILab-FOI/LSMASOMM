
# __ File: ATOM3Link.py ______________________________________________________________________________________________
#  Implements  : class ATOM3Link
#  Author      : Juan de Lara
#  Description : This class implements a hyper-link. Links are composed of a Center, and incoming
#                and outgoing lines, with a joint at the end. Centers, joints, and segments can be
#                configured.
#  Modified    : 26 Oct 2001
#  - 14 Jan 2002: If semObject is None in the constructor (such as when added as an atribute in an entity in the ER meta-model),
#                 then it failed in method showAppDialog. Fixed.
#  - 14 Jan 2002: If className is None in the constructor (such as when added as an atribute in an entity in the ER meta-model),
#                 then it failed in method toString. Fixed.
#  - 14 Jan 2002: If a variable of this type is the initial value of an ATOM3Attribute, then if we save it, it won't work. Fixed
#		  bug in writeValue2File
#  - 14 Jan 2002: toString did not accept three parameters. so it failed when a variable of these was printed in a graphic.
#  - 14 Jan 2002: showAppDialog failed if the entity did not have a keyword.
#  - 31 July 2002: The method setNone is not present!
#  - 2 August 2002: Fixed bug with setNone(), isNone(), etc. Added attribute _isNone
# ____________________________________________________________________________________________________________________

from Tkinter         import *
from ATOM3Type       import *
from linkEditor      import *
from ATOM3TypeDialog import *

class ATOM3Link(ATOM3Type):
    def __init__(self, className = None, semObject = None ):
       " className is the class name, attrList is an ATOM3List(ATOM3Attribute)"
       self.appDialog = None				# at first, the dialog is hidden
       self.className = className			# we should have a class name, in order to store all the information in a file...
       self.semObject = semObject 			# List of ATOM3Attributes
       self.editButton= None				# the button to edit is also hidden
       self.linkInfo = None                             # info about the link graphics
       self._isNone  = 0				# for the moment it is not none (Added 3 August 2002)

       ATOM3Type.__init__(self)				# call ancestor

    def show(self, parent, topWindowParent = None ):
       "method to show the button to edit the appearance"
       ATOM3Type.show(self, parent, topWindowParent )
       self.editButton = Button ( parent, text="edit", command = lambda x=(self, parent): x[0].showAppDialog(x[1]) )
       return self.editButton

    def showAppDialog(self, parent):
       "shows the appearandeDialog"
       if not self.linkInfo:
          if self.semObject:				# check if we have the associated semantic object (changed 14-Jan-2002)
             if self.semObject.keyword_:		# check if the entity has a keyword (modified 14-Jan-2002)
                self.linkInfo = linkEditor ( self, self.semObject, self.semObject.keyword_.toString() )
             else:
                self.linkInfo = linkEditor ( self, self.semObject, "no_keyword" )
          else:                                         # we do not have semantic object (yet)
	     self.linkInfo = linkEditor ( self, self.semObject, "Class_information_not_available" )
       ma = ATOM3TypeDialog(parent, self.linkInfo)

    def isNone (self):
       "check if the type value is none"
       return self._isNone

    def setNone (self):
       "sets to None the attribute value"
       self._isNone  = 1

    def unSetNone (self):
       "sets to None the attribute value to 0"
       self._isNone = 0

    def destroy (self):
       "updates attributes and destroys the graphical widget"
       pass						# actually do nothing

    def setValue(self, value):
       "sets the class name"
       if value:
         if value[0]: self.className = value[0]
         if len(value) == 2 and value[1]:
            self.semObject = value[1]

    def getValue(self):
       "returns the class name"
       return (self.className, self.semObject)

    def toString(self, maxWide = None, maxLines = None ):
       "returns the file name"
       if self.className:				# if we have information about the className (modified 14-Jan-2002)
          result = "graph_"+self.className+".py"
       else:                    			# className is None (modified 14-Jan-2002)
          result = "graph_.py"
       if maxWide: return result[0:maxWide]
       return result

    def clone(self):
       "makes an exact copy of itself"
       cloneObject = ATOM3Link(self.className, self.semObject)
       cloneObject.appDialog     = self.appDialog
       cloneObject.className     = self.className
       cloneObject.semObject     = self.semObject
       cloneObject.editButton    = self.editButton
       cloneObject.parent        = self.parent
       cloneObject.mode          = self.mode
       cloneObject._isNone       = self._isNone
       if self.linkInfo:
          cloneObject.linkInfo = self.linkInfo.clone()
       else:
          cloneObject.linkInfo = None
       return cloneObject

    def copy(self, other):
       "copies each field of the other object into its own state"
       ATOM3Type.copy(self, other)			# call the ancestor (copies the parent field)
       self.appDialog = other.appDialog
       self.className = other.className
       self.editButton= other.editButton
       self.semObject = other.semObject
       self.linkInfo  = other.linkInfo
       self._isNone   = other._isNone

    def writeConstructor2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       file.write(indent+objName+"=ATOM3Link()\n")
       self.writeValue2File(file, indent, objName)

    def writeValue2File(self, file, indent, objName='at', depth = 0, generatingCode = 0):
       "Method that writes into a file the constructor and the value of the object. Must be overriden in children"
       if generatingCode:
          file.write(indent+objName+".setValue( ('"+str(self.getValue()[0])+"', self))\n")
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

       if not self.isNone():
          file.write(indent+objName+".setValue( ('"+str(self.getValue()[0])+"', "+objectName+"))\n")
       if self.linkInfo:
          self.linkInfo.writeConstructor2File(file, indent, objName+".linkInfo", depth, generatingCode)
       if self.isNone():
          file.write(indent+objName+".setNone()\n")
          
          
    def updateGraphicalFile(self, newClassName):
      "if class name has changed, update graphical file of each appearance..."
      if newClassName != self.className:
         self.className = newClassName
         if self.linkInfo:                      # if we have graphics information...
            self.linkInfo.updateGraphicalFile(newClassName)

    def genGraphicalFile( self, codeGenDir, tkRoot=None ):      
      "generates the graphical file, in the directory 'codeGenDir'"
      
      if( not self.linkInfo ):
        import tkMessageBox
        tkMessageBox.showwarning( "Missing Link Graphics", 
                "The following link has no visual appearence: " + 
                self.semObject.keyword_.toString() +
                "\n\nPress okay to specify the appearence in the next dialog")
        if( tkRoot ):
          self.showAppDialog( tkRoot )
          return self.genGraphicalFile( codeGenDir, tkRoot )
        else:
          return
      
      fileName = "graph_"+self.semObject.keyword_.toString()+".py"			  # Prepare file name, with the keyword
      f = open( codeGenDir+"/"+ fileName, "w+t")                                          # open file name and print header
      
      f.write('"""\n')
      f.write("__"+ fileName +"___________________________________________________________\n")
      f.write("\n")
      f.write("Automatically generated LINK for entity "+self.semObject.keyword_.toString()+"\n")
      f.write("DO NOT MODIFY DIRECTLY\n")
      f.write("__"+ len(fileName)*"_" +"___________________________________________________________\n")
      f.write('"""\n')
      
      #f.write( "# _ File: "+fileName+"__________________________________________________________________________________\n")
      #f.write( "#  Graphical LINK for entity "+self.semObject.keyword_.toString()+", generated by ATOM3\n")
      #f.write( "# ______________________________________________________________________________________________________\n")
      f.write( "from graphLink import *\n")
      f.write( "from stickylink import *\n")
      f.write( "from widthXfillXdecoration import *\n")
      f.write( "class graph_"+self.semObject.keyword_.toString()+"(graphLink):\n\n")
      f.write( "   def __init__(self, xc, yc, semObject = None ):\n")
      f.write( "      self.semObject = semObject\n")
      f.write( "      self.semanticObject = semObject\n")
      f.write( "      from linkEditor import *\n")      
      self.linkInfo.writeConstructor2File(f, "      ", "self.le")
      f.write( "      graphLink.__init__(self, xc, yc, self.le,semObject)\n")
      f.close()




