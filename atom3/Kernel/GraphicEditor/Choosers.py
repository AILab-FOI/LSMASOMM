import Tkinter
import tkFont
import os

from FilePaths import GRAPHIC_EDITOR_DATA


#class StippleChooser:
#    def __init__(self, master, eventHandler, stipple):
#        self.eventHandler = eventHandler
#        self.stippleFrame = Tkinter.Frame(master)



class AnchorChooser:
    def __init__(self, master, eventHandler, anchor):
        self.eventHandler = eventHandler
        h = 1
        w = 1
        self.anchorFrame = Tkinter.Frame(master)

        self.label = Tkinter.Label(self.anchorFrame, text="anchor:")
        self.label.grid(row=1,column=0)

        self.NW = Tkinter.Button(self.anchorFrame, text="NW", width=w, height=h, command = self.onAnchorNW, font=("Helvetica", 8))
        self.N = Tkinter.Button(self.anchorFrame, text="N", height = h, width = w, command = self.onAnchorN, font=("Helvetica", 8))
        self.NE = Tkinter.Button(self.anchorFrame, text="NE", height = h, width = w, command = self.onAnchorNE, font=("Helvetica", 8))
        self.W = Tkinter.Button(self.anchorFrame, text="W", height = h, width = w, command = self.onAnchorW, font=("Helvetica", 8))
        self.CENTER = Tkinter.Button(self.anchorFrame, text="+", height = h, width = w, command = self.onAnchorCENTER, font=("Helvetica", 8))
        self.E = Tkinter.Button(self.anchorFrame, text="E", height = h, width = w, command = self.onAnchorE, font=("Helvetica", 8))
        self.SW = Tkinter.Button(self.anchorFrame, text="SW", height = h, width = w, command = self.onAnchorSW, font=("Helvetica", 8))
        self.S = Tkinter.Button(self.anchorFrame, text="S", height = h, width = w, command = self.onAnchorS, font=("Helvetica", 8))
        self.SE = Tkinter.Button(self.anchorFrame, text="SE", height = h, width = w, command = self.onAnchorSE, font=("Helvetica", 8))

        self.anchorFrame.pack(side=Tkinter.BOTTOM)
        self.NW.grid(row=0,column=1)
        self.N.grid(row=0,column=2)
        self.NE.grid(row=0,column=3)
        self.W.grid(row=1,column=1)
        self.CENTER.grid(row=1,column=2)
        self.E.grid(row=1,column=3)
        self.SW.grid(row=2,column=1)
        self.S.grid(row=2,column=2)
        self.SE.grid(row=2,column=3)

        self.previousAnchor = self.getAnchorButton(anchor)
        self.previousAnchor.config(relief = Tkinter.SUNKEN)


    def getAnchorButton(self, anchor):
        if anchor == "n":
            return self.N
        elif anchor == "s":
            return self.S
        elif anchor == "e":
            return self.E
        elif anchor == "w":
            return self.W
        elif anchor == "nw":
            return self.NW
        elif anchor == "ne":
            return self.NE
        elif anchor == "sw":
            return self.SW
        elif anchor == "se":
            return self.SE
        else:
            return self.CENTER

    def onAnchorN(self):
        self.previousAnchor.config(relief = Tkinter.RAISED)
        self.N.config(relief = Tkinter.SUNKEN)
        self.previousAnchor = self.N
        self.eventHandler.onAnchor("n")

    def onAnchorS(self):
        self.previousAnchor.config(relief = Tkinter.RAISED)
        self.S.config(relief = Tkinter.SUNKEN)
        self.previousAnchor = self.S
        self.eventHandler.onAnchor("s")

    def onAnchorE(self):
        self.previousAnchor.config(relief = Tkinter.RAISED)
        self.E.config(relief = Tkinter.SUNKEN)
        self.previousAnchor = self.E
        self.eventHandler.onAnchor("e")

    def onAnchorW(self):
        self.previousAnchor.config(relief = Tkinter.RAISED)
        self.W.config(relief = Tkinter.SUNKEN)
        self.previousAnchor = self.W
        self.eventHandler.onAnchor("w")

    def onAnchorNE(self):
        self.previousAnchor.config(relief = Tkinter.RAISED)
        self.NE.config(relief = Tkinter.SUNKEN)
        self.previousAnchor = self.NE
        self.eventHandler.onAnchor("ne")

    def onAnchorNW(self):
        self.previousAnchor.config(relief = Tkinter.RAISED)
        self.NW.config(relief = Tkinter.SUNKEN)
        self.previousAnchor = self.NW
        self.eventHandler.onAnchor("nw")

    def onAnchorSE(self):
        self.previousAnchor.config(relief = Tkinter.RAISED)
        self.SE.config(relief = Tkinter.SUNKEN)
        self.previousAnchor = self.SE
        self.eventHandler.onAnchor("se")

    def onAnchorSW(self):
        self.previousAnchor.config(relief = Tkinter.RAISED)
        self.SW.config(relief = Tkinter.SUNKEN)
        self.previousAnchor = self.SW
        self.eventHandler.onAnchor("sw")

    def onAnchorCENTER(self):
        self.previousAnchor.config(relief = Tkinter.RAISED)
        self.CENTER.config(relief = Tkinter.SUNKEN)
        self.previousAnchor = self.CENTER
        self.eventHandler.onAnchor("center")


class ImageProperties:
    def __init__(self, root, anchor, eventHandler):
        self.root = root
        self.anchor = anchor
        self.eventHandler = eventHandler

        self.anchorChooser = AnchorChooser(self.root, self, self.anchor)

    def onAnchor(self, anchor):
        if self.anchor != anchor:
            self.anchor = anchor
            self.eventHandler.onAnchor(self.anchor)
            
            


class TextProperties:
    def __init__(self, root, family, size, bold, italic, underline, anchor, eventHandler):
        self.root = root
        self.family = family
        self.size = size
        self.bold = bold
        self.italic = italic
        self.underline = underline
        self.anchor = anchor
        self.eventHandler = eventHandler

        self.familyScrollbar = Tkinter.Scrollbar(root, orient=Tkinter.VERTICAL)
        self.familyListbox = Tkinter.Listbox(root, yscrollcommand=self.familyScrollbar.set, selectmode=Tkinter.BROWSE, exportselection=0, height = 7)
        allFontsList = list(tkFont.families())
        allFontsList.sort()
        for font in allFontsList:
            self.familyListbox.insert(Tkinter.END, font)
        self.familyScrollbar.config(command=self.familyListbox.yview)

        self.familyListbox.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
        self.familyListbox.bind("<ButtonRelease>",self.checkFamilyChange)
        self.familyScrollbar.pack(side=Tkinter.LEFT, fill=Tkinter.Y)

        self.sizeScrollbar = Tkinter.Scrollbar(root, orient=Tkinter.VERTICAL)
        self.sizeListbox = Tkinter.Listbox(root, yscrollcommand=self.sizeScrollbar.set, selectmode=Tkinter.BROWSE, width = 5, exportselection=0, height = 7)
        for size in [6,8,9,10,12,14,16,18,20,22,24,26,28,36,48,72]:
            self.sizeListbox.insert(Tkinter.END, size)
        self.sizeListbox.see(4)
        self.sizeScrollbar.config(command=self.sizeListbox.yview)

        self.sizeListbox.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
        self.sizeListbox.bind("<ButtonRelease>",self.checkSizeChange)
        self.sizeScrollbar.pack(side=Tkinter.LEFT, fill=Tkinter.Y)

        self.optionFrame = Tkinter.Frame(root)
        h = 40
        w = 40
        
        boldxbm      = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'bold.xbm' ) )
        italicxbm    = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'italic.xbm' ) )
        underlinexbm = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'underline.xbm' ) )
        
        self.boldButton = Tkinter.Button(self.optionFrame, bitmap=boldxbm, height = h, width = w, command = self.onBold)
        self.italicButton = Tkinter.Button(self.optionFrame, bitmap=italicxbm, height = h, width = w, command = self.onItalic)
        self.underlineButton = Tkinter.Button(self.optionFrame, bitmap=underlinexbm, height = h, width = w, command = self.onUnderline)
        if self.bold:
            self.boldButton.config(relief=Tkinter.SUNKEN)
        if self.italic:
            self.italicButton.config(relief=Tkinter.SUNKEN)
        if self.underline:
            self.underlineButton.config(relief=Tkinter.SUNKEN)

        self.boldButton.pack(side=Tkinter.LEFT)
        self.italicButton.pack(side=Tkinter.LEFT)
        self.underlineButton.pack(side=Tkinter.LEFT)

        self.anchorChooser = AnchorChooser(root, self, self.anchor)

        self.optionFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)


    def checkFamilyChange(self, event):
        family = self.familyListbox.get(self.familyListbox.curselection()[0])
        if family != self.family:
            self.family = family
            self.eventHandler.onFamily(self.family)

    def checkSizeChange(self, event):
        if( not self.sizeListbox.curselection() ): return
        size = self.sizeListbox.get(self.sizeListbox.curselection()[0])
        if int(size) != self.size:
            self.size = int(size)
            self.eventHandler.onSize(self.size)

    def onBold(self):
        if self.bold:
            self.bold = 0
            self.boldButton.config(relief=Tkinter.RAISED)
        else:
            self.bold = 1
            self.boldButton.config(relief=Tkinter.SUNKEN)
        self.eventHandler.onBold(self.bold)

    def onItalic(self):
        if self.italic:
            self.italic = 0
            self.italicButton.config(relief=Tkinter.RAISED)
        else:
            self.italic = 1
            self.italicButton.config(relief=Tkinter.SUNKEN)
        self.eventHandler.onItalic(self.italic)

    def onUnderline(self):
        if self.underline:
            self.underline = 0
            self.underlineButton.config(relief=Tkinter.RAISED)
        else:
            self.underline = 1
            self.underlineButton.config(relief=Tkinter.SUNKEN)
        self.eventHandler.onUnderline(self.underline)


    def onAnchor(self, anchor):
        if self.anchor != anchor:
            self.anchor = anchor
            self.eventHandler.onAnchor(self.anchor)


class RectangleProperties:
    def __init__(self, bitmap, eventHandler):
        self.bitmap = bitmap

class OvalProperties:
    def __init__(self, bitmap, eventHandler):
        self.bitmap = bitmap

class PolygonProperties:
    def __init__(self, bitmap, eventHandler):
        self.bitmap = bitmap


class LineProperties:
    def __init__(self, root, bitmap, arrow, capstyle, joinstyle, eventHandler):
        self.bitmap = bitmap
        self.arrow = Tkinter.StringVar()
        self.arrow.set(arrow)
        self.capstyle = Tkinter.StringVar()
        self.capstyle.set(capstyle)
        self.joinstyle = Tkinter.StringVar()
        self.joinstyle.set(joinstyle)
        self.eventHandler = eventHandler

        self.arrowFrame = Tkinter.Frame(root, borderwidth=2, relief=Tkinter.GROOVE)
        self.arrowLabel = Tkinter.Label(self.arrowFrame, text="Arrow:")
        self.arrowLabel.pack(anchor=Tkinter.W)
        self.arrowRadiobuttons = []
        for text, mode in [("None", "none"), ("First", "first"), ("Last", "last"), ("Both", "both")]:
            self.arrowRadiobuttons.append(Tkinter.Radiobutton(self.arrowFrame, text=text, variable=self.arrow, value=mode, command=self.onArrow))
        for button in self.arrowRadiobuttons:
            button.pack(anchor=Tkinter.W)
        self.arrowFrame.pack(side=Tkinter.TOP, fill=Tkinter.X)

        self.capstyleFrame = Tkinter.Frame(root, borderwidth=2, relief=Tkinter.GROOVE)
        self.capstyleLabel = Tkinter.Label(self.capstyleFrame, text="Cap Style:")
        self.capstyleLabel.pack(anchor=Tkinter.W)
        self.capstyleRadiobuttons = []
        for text, mode in [("Butt", "butt"), ("Projecting", "projecting"), ("Round", "round")]:
            self.capstyleRadiobuttons.append(Tkinter.Radiobutton(self.capstyleFrame, text=text, variable=self.capstyle, value=mode, command=self.onCapstyle))
        for button in self.capstyleRadiobuttons:
            button.pack(anchor=Tkinter.W)
        self.capstyleFrame.pack(side=Tkinter.TOP, fill=Tkinter.X)

        self.joinstyleFrame = Tkinter.Frame(root, borderwidth=2, relief=Tkinter.GROOVE)
        self.joinstyleLabel = Tkinter.Label(self.joinstyleFrame, text="Join Style:")
        self.joinstyleLabel.pack(anchor=Tkinter.W)
        self.joinstyleRadiobuttons = []
        for text, mode in [("Bevel", "bevel"), ("Miter", "miter"), ("Round", "round")]:
            self.joinstyleRadiobuttons.append(Tkinter.Radiobutton(self.joinstyleFrame, text=text, variable=self.joinstyle, value=mode, command=self.onJoinstyle))
        for button in self.joinstyleRadiobuttons:
            button.pack(anchor=Tkinter.W)
        self.joinstyleFrame.pack(side=Tkinter.TOP, fill=Tkinter.X)


    def onArrow(self):
        self.eventHandler.onArrow(self.arrow.get())

    def onCapstyle(self):
        self.eventHandler.onCapstyle(self.capstyle.get())

    def onJoinstyle(self):
        self.eventHandler.onJoinstyle(self.joinstyle.get())

    def onStipple(self):
        self.eventHandler.onStipple(self.stipple)



class NamedPortProperties:
    def __init__(self, root, name, eventHandler):
        self.root = root
        self.port = name
        self.eventHandler = eventHandler
        self.originalPort = name
        
        portList = []
        for attr in self.eventHandler.editor.getAttributes():
            if( attr.getValue()[1] == 'Port' ):
                portList.append( attr.getValue()[0] )
        
        self.namedPortFrame = Tkinter.Frame(self.root)
        
        if( len( portList ) == 0 ):
            
            self.label = Tkinter.Label(self.namedPortFrame, text="ERROR: No named ports defined")
            self.label.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
            self.label = Tkinter.Label(self.namedPortFrame, text="Please give your entity some 'Port' Attributes in AToM3 first")
            self.label.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
            
            self.eventHandler.editor.delete( [eventHandler.getCurrent() ] )
            
            self.okayb = Tkinter.Button(self.namedPortFrame, text="Ok", command=self.okay )
            self.okayb.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
        
        else:
            
            self.portScrollbar = Tkinter.Scrollbar(self.namedPortFrame, orient=Tkinter.VERTICAL)
            self.portListbox = Tkinter.Listbox(self.namedPortFrame, yscrollcommand=self.portScrollbar.set, 
                                                       selectmode=Tkinter.BROWSE, exportselection=0, height = 7)
            i = 0
            for port in portList:
                self.portListbox.insert(Tkinter.END, port )
                if( port == name ):
                    self.portListbox.selection_set( i )
                i+=1
            self.portScrollbar.config(command=self.portListbox.yview)
    
            self.portListbox.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
            self.portListbox.bind("<ButtonRelease>",self.checkPortChange)
            self.portScrollbar.pack(side=Tkinter.LEFT, fill=Tkinter.Y)
            
            self.okayb = Tkinter.Button(self.namedPortFrame, text="Ok", command=self.okay )
            self.okayb.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
            
            self.cancelb = Tkinter.Button(self.namedPortFrame, text="Cancel", command=self.cancel )
            self.cancelb.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
            
        self.namedPortFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)

    def checkPortChange( self, event):
        port = self.portListbox.get(self.portListbox.curselection()[0])
        if( port != self.port ):
            self.port = port
            self.eventHandler.onSetName(self.port)
        
    def okay(self):
        self.root.destroy()
             
    def cancel(self):
        if( self.port != self.originalPort ):
            self.eventHandler.onSetName( self.originalPort )
        elif( self.port == '' ):
            self.eventHandler.editor.delete( [self.eventHandler.getCurrent() ] )
        self.root.destroy()
        
class AttributeProperties:
    def __init__(self, root, attribute, eventHandler):
        self.root = root
        self.attribute = attribute
        self.eventHandler = eventHandler
        self.originalAttribute = attribute
  
        
        attrList = []
        for attr in self.eventHandler.editor.getAttributes():
            if( attr.getValue()[1] != 'Port' ):
                attrList.append( attr.getValue()[0] )
        
        self.attributeFrame = Tkinter.Frame(self.root)
        
        if( len( attrList ) == 0 ):
            
            self.label = Tkinter.Label(self.attributeFrame, text="ERROR: No attributes defined")
            self.label.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
            self.label = Tkinter.Label(self.attributeFrame, text="Please give your entity some attributes in AToM3 first")
            self.label.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
            
            self.eventHandler.editor.delete( [eventHandler.getCurrent() ] )
            
            self.okayb = Tkinter.Button(self.attributeFrame, text="Ok", command=self.okay )
            self.okayb.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
                    
        else:
            
            self.attrScrollbar = Tkinter.Scrollbar(self.attributeFrame, 
                                                   orient=Tkinter.VERTICAL)
            self.attrListbox = Tkinter.Listbox(self.attributeFrame, 
                                          yscrollcommand=self.attrScrollbar.set, 
                                          selectmode=Tkinter.BROWSE, exportselection=0, height = 7)
            i = 0
            for attr in attrList:
                self.attrListbox.insert(Tkinter.END, attr )
                if( attr == attribute ):
                    self.attrListbox.selection_set( i )
                i+=1
            self.attrScrollbar.config(command=self.attrListbox.yview)
    
            self.attrListbox.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)
            self.attrListbox.bind("<ButtonRelease>",self.checkAttrChange)
            self.attrScrollbar.pack(side=Tkinter.LEFT, fill=Tkinter.Y)
            
            self.okayb = Tkinter.Button(self.attributeFrame, text="Ok", command=self.okay )
            self.okayb.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
            
            self.cancelb = Tkinter.Button(self.attributeFrame, text="Cancel", command=self.cancel )
            self.cancelb.pack( side=Tkinter.TOP, fill=Tkinter.BOTH )
            
        self.attributeFrame.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH, expand=1)

    def checkAttrChange( self, event):
        attribute = self.attrListbox.get(self.attrListbox.curselection()[0])
        if( attribute != self.attribute ):
            self.attribute = attribute
            self.eventHandler.onSetAttribute(self.attribute)
        
    def okay(self):
        self.eventHandler.stop()
        self.eventHandler.eventHandler.onEditHandlerStopped([])
        #self.root.destroy()
             
    def cancel(self):
        if( self.attribute != self.originalAttribute ):
            self.eventHandler.onSetAttribute( self.originalAttribute )
        elif( self.attribute == 'attribute' ):
            self.eventHandler.editor.delete( [self.eventHandler.getCurrent() ] )
        #self.root.destroy()
        self.okay()

if __name__ == "__main__":
    root = Tkinter.Tk()
    root.title("Font - AToM3")
    polylineChooser = LineProperties(root, "gray50", "both", "butt", "round", 0, None)
    root.mainloop()
    


