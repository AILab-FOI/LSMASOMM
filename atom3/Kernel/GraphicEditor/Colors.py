#Colors.py
#Francois Plamondon
#Summer 2003
#
# Classes related to the color selector.

import Tkinter
import tkColorChooser
import os

from FilePaths import GRAPHIC_EDITOR_DATA

# Simple color pot represented by a button. The color selector contains two rows of those.
# The event handle must recognize the following events:
#          onColorPotButton1()
#          onColorPotButton3()
#          onColorPotDoubleButton1()
#          onColorPotDoubleButton3()
class ColorPot:
    def __init__(self, masterFrame, eventHandler, color, row, column):
        blankxbm = '@' + str( os.path.join( GRAPHIC_EDITOR_DATA, 'blank.xbm' ) )
        self.button = Tkinter.Button(masterFrame, width = 15, height = 15, bitmap=blankxbm, relief= Tkinter.SUNKEN, background=color, activebackground=color, takefocus=0)
        self.button.bind("<Button-1>", self.onButton1)
        self.button.bind("<Button-3>", self.onButton3)
        self.button.bind("<Double-Button-1>", self.onDoubleButton1)
        self.button.bind("<Double-Button-3>", self.onDoubleButton3)
        if row == 0:
            self.button.grid(row=0, column=column, sticky=Tkinter.N)
        else:
            self.button.grid(row=0, column=column, sticky=Tkinter.S)  
        self.color = color
        self.eventHandler = eventHandler

        
    def setColor(self, newColor):
        self.button.config(background = newColor, activebackground = newColor)
        self.color = newColor

            
    def getColor(self):
        return self.color


    def onButton1(self, event):
        self.eventHandler.onColorPotButton1(self)

    def onButton3(self, event):
        self.eventHandler.onColorPotButton3(self)

    def onDoubleButton1(self, event):
        self.eventHandler.onColorPotDoubleButton1(self)

    def onDoubleButton3(self, event):
        self.eventHandler.onColorPotDoubleButton3(self)



#the color displayer is made of two small rectangles on a canvas. The two rectangles show the current outline and
#fill colors. When those rectangles are clicked, the color displayer will call its event handler's corresponding methods:
#            onColorDisplayerButton1Outline()
#            onColorDisplayerButton1Fill()
class ColorDisplayer:
    def __init__(self, masterFrame, eventHandler, initFillColor, initOutlineColor, row, column):
        size = 45
        rSize = 23
        posOutline = 18
        posFill = 5
        self.canvas = Tkinter.Canvas(masterFrame, width = size, height = size, background="white")
        self.canvas.grid(row=row, column=column)
        
        imagePath = os.path.join( GRAPHIC_EDITOR_DATA, "marble.ppm" )
        self.photo = Tkinter.PhotoImage(file=imagePath )
        self.background = self.canvas.create_image(0,0,image=self.photo, anchor=Tkinter.NW)
        self.currentOutline = initOutlineColor
        self.currentFill = initFillColor
        self.outlineDisplay = self.canvas.create_rectangle(posOutline, posOutline, posOutline + rSize, posOutline + rSize, fill=initOutlineColor)
        self.fillDisplay = self.canvas.create_rectangle(posFill, posFill, posFill + rSize, posFill + rSize, fill=initFillColor)
        self.canvas.tag_bind(self.fillDisplay, "<Button-1>", self.onFillDisplayButton1)
        self.canvas.tag_bind(self.outlineDisplay, "<Button-1>", self.onOutlineDisplayButton1)
        self.eventHandler = eventHandler

    def getOutlineColor(self):
        return self.currentOutline

    def getFillColor(self):
        return self.currentFill

    def setOutlineColor(self, color):
        self.currentOutline = color
        self.canvas.itemconfig(self.outlineDisplay, fill=color)

    def setFillColor(self, color):
        self.currentFill = color
        self.canvas.itemconfig(self.fillDisplay, fill=color)


    def onOutlineDisplayButton1(self, event):
        self.eventHandler.onColorDisplayerButton1Outline()


    def onFillDisplayButton1(self, event):
        self.eventHandler.onColorDisplayerButton1Fill()


#The color selector the class that is instantiated by the editor. It contains color pots and a color displayer.
# The color selector notifies its event handler (the editor) of the folowing events:
#          1)  onOutlineColor(color)
#          2)  onFillColor(color)
# which informs the editor of a change in the outline or fill color.
# The internals are quite simple. When a color pot is clicked, the color displayer is updated and a color event is sent
# to the event handler. When the color displayer is clicked, a color chooser appears. Same thing when a color pot is double-clicked,
# except that in this case, the content of the color pot is also modified.
# The left button is used to change the fill color and the right button to change the outline color.
class ColorSelector:
    def __init__(self, masterFrame, eventHandler):
        self.frame = Tkinter.Frame(masterFrame)
        self.eventHandler = eventHandler
        self.defaultTopColor = ["white", "gray","blue1","blue3","blue4", "royalblue", "cyan", "yellow", "yellow3", "yellow4", "green", "springGreen1", "springGreen2", "springGreen3", "springGreen4", "skyblue1", "skyblue3", "skyblue4", "sienna1", "sienna3"]
        self.defaultBottomColor = ["black", "grey45", "red1", "red3", "red4", "orangered1", "tomato4", "orange", "peru", "moccasin","purple1","purple3","purple4", "olivedrab1", "olivedrab3", "olivedrab4", "magenta1", "magenta3", "magenta4", "sienna4"]
        self.colorDisplayer = ColorDisplayer(self.frame, self, self.defaultBottomColor[1], self.defaultBottomColor[0], 0, 0)
        self.colorPots = []
        i = 0
        for color in self.defaultTopColor:
            self.colorPots.append(ColorPot(self.frame, self, color, 0, i + 1))
            i += 1
        i = 0
        for color in self.defaultBottomColor:
            self.colorPots.append(ColorPot(self.frame, self, color, 1, i + 1))
            i += 1
        self.frame.pack(side=Tkinter.BOTTOM)

    # getFill and getOutline are the two public methods
    def getOutlineColor(self):
        return self.colorDisplayer.getOutlineColor()

    def getFillColor(self):
        return self.colorDisplayer.getFillColor()


    #private color pot event methods
    def onColorPotButton1(self, colorPot):
        color = colorPot.getColor()
        self.colorDisplayer.setFillColor(color)
        self.eventHandler.onFillColor(color)


    def onColorPotButton3(self, colorPot):
        color = colorPot.getColor()
        self.colorDisplayer.setOutlineColor(color)
        self.eventHandler.onOutlineColor(color)


    def onColorPotDoubleButton1(self, colorPot):
        color = tkColorChooser.askcolor()
        if color[1] != None:
            colorPot.setColor(color[1])
            self.colorDisplayer.setFillColor(color[1])
            self.eventHandler.onFillColor(color[1])


    def onColorPotDoubleButton3(self, colorPot):
        color = tkColorChooser.askcolor()
        if color[1] != None:
            colorPot.setColor(color[1])
            self.colorDisplayer.setOutlineColor(color[1])
            self.eventHandler.onOutlineColor(color[1])


    def onColorDisplayerButton1Outline(self):
        color = tkColorChooser.askcolor()
        if color[1] != None:
            self.colorDisplayer.setOutlineColor(color[1])
            self.eventHandler.onOutlineColor(color[1])
            

    def onColorDisplayerButton1Fill(self):
        color = tkColorChooser.askcolor()
        if color[1] != None:
            self.colorDisplayer.setFillColor(color[1])
            self.eventHandler.onFillColor(color[1])



