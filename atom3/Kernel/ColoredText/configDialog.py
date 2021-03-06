"""IDLE Configuration Dialog: support user customization of IDLE by GUI

Customize font faces, sizes, and colorization attributes.  Set indentation
defaults.  Customize keybindings.  Colorization and keybindings can be
saved as user defined sets.  Select startup options including shell/editor
and default window size.  Define additional help sources.

Note that tab width in IDLE is currently fixed at eight due to Tk issues.
Refer to comment in EditorWindow autoindent code for details.

"""
from Tkinter import *
import tkMessageBox, tkColorChooser, tkFont
import string, copy

from configHandler import idleConf
from dynOptionMenuWidget import DynOptionMenu
from tabpage import TabPageSet
from keybindingDialog import GetKeysDialog
from configSectionNameDialog import GetCfgSectionNameDialog
from configHelpSourceEdit import GetHelpSourceDialog

class ConfigDialog(Toplevel):
    """
    configuration dialog for idle
    """
    def __init__(self,parent,title):
        Toplevel.__init__(self, parent)
        self.configure(borderwidth=5)
        self.geometry("+%d+%d" % (parent.winfo_rootx()+20,
                parent.winfo_rooty()+30))
        #Theme Elements. Each theme element key is it's display name.
        #The first value of the tuple is the sample area tag name.
        #The second value is the display name list sort index.
        self.themeElements={'Normal Text':('normal','00'),
            'Python Keywords':('keyword','01'),
            'Python Definitions':('definition','02'),
            'Python Comments':('comment','03'),
            'Python Strings':('string','04'),
            'Selected Text':('hilite','05'),
            'Found Text':('hit','06'),
            'Cursor':('cursor','07'),
            'Error Text':('error','08'),
            'Shell Normal Text':('console','09'),
            'Shell Stdout Text':('stdout','10'),
            'Shell Stderr Text':('stderr','11')}
        self.ResetChangedItems() #load initial values in changed items dict
        self.CreateWidgets()
        self.resizable(height=FALSE,width=FALSE)
        self.transient(parent)
        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.Cancel)
        self.parent = parent
        self.tabPages.focus_set()
        #key bindings for this dialog
        #self.bind('<Escape>',self.Cancel) #dismiss dialog, no save
        #self.bind('<Alt-a>',self.Apply) #apply changes, save
        #self.bind('<F1>',self.Help) #context help
        self.LoadConfigs()
        self.AttachVarCallbacks() #avoid callbacks during LoadConfigs
        self.wait_window()

    def CreateWidgets(self):
        self.tabPages = TabPageSet(self,
                pageNames=['Fonts/Tabs','Highlighting','Keys','General'])
        self.tabPages.ChangePage()#activates default (first) page
        frameActionButtons = Frame(self)
        #action buttons
        self.buttonHelp = Button(frameActionButtons,text='Help',
                command=self.Help,takefocus=FALSE)
        self.buttonOk = Button(frameActionButtons,text='Ok',
                command=self.Ok,takefocus=FALSE)
        self.buttonApply = Button(frameActionButtons,text='Apply',
                command=self.Apply,takefocus=FALSE)
        self.buttonCancel = Button(frameActionButtons,text='Cancel',
                command=self.Cancel,takefocus=FALSE)
        self.CreatePageFontTab()
        self.CreatePageHighlight()
        self.CreatePageKeys()
        self.CreatePageGeneral()
        self.buttonHelp.pack(side=RIGHT,padx=5,pady=5)
        self.buttonOk.pack(side=LEFT,padx=5,pady=5)
        self.buttonApply.pack(side=LEFT,padx=5,pady=5)
        self.buttonCancel.pack(side=LEFT,padx=5,pady=5)
        frameActionButtons.pack(side=BOTTOM)
        self.tabPages.pack(side=TOP,expand=TRUE,fill=BOTH)

    def CreatePageFontTab(self):
        #tkVars
        self.fontSize=StringVar(self)
        self.fontBold=BooleanVar(self)
        self.fontName=StringVar(self)
        self.spaceNum=IntVar(self)
        #self.tabCols=IntVar(self)
        self.indentBySpaces=BooleanVar(self)
        self.editFont=tkFont.Font(self,('courier',10,'normal'))
        ##widget creation
        #body frame
        frame=self.tabPages.pages['Fonts/Tabs']['page']
        #body section frames
        frameFont=Frame(frame,borderwidth=2,relief=GROOVE)
        frameIndent=Frame(frame,borderwidth=2,relief=GROOVE)
        #frameFont
        labelFontTitle=Label(frameFont,text='Set Base Editor Font')
        frameFontName=Frame(frameFont)
        frameFontParam=Frame(frameFont)
        labelFontNameTitle=Label(frameFontName,justify=LEFT,
                text='Font :')
        self.listFontName=Listbox(frameFontName,height=5,takefocus=FALSE,
                exportselection=FALSE)
        self.listFontName.bind('<ButtonRelease-1>',self.OnListFontButtonRelease)
        scrollFont=Scrollbar(frameFontName)
        scrollFont.config(command=self.listFontName.yview)
        self.listFontName.config(yscrollcommand=scrollFont.set)
        labelFontSizeTitle=Label(frameFontParam,text='Size :')
        self.optMenuFontSize=DynOptionMenu(frameFontParam,self.fontSize,None,
            command=self.SetFontSample)
        checkFontBold=Checkbutton(frameFontParam,variable=self.fontBold,
            onvalue=1,offvalue=0,text='Bold',command=self.SetFontSample)
        frameFontSample=Frame(frameFont,relief=SOLID,borderwidth=1)
        self.labelFontSample=Label(frameFontSample,
                text='AaBbCcDdEe\nFfGgHhIiJjK\n1234567890\n#:+=(){}[]',
                justify=LEFT,font=self.editFont)
        #frameIndent
        labelIndentTitle=Label(frameIndent,text='Set Indentation Defaults')
        frameIndentType=Frame(frameIndent)
        frameIndentSize=Frame(frameIndent)
        labelIndentTypeTitle=Label(frameIndentType,
                text='Choose indentation type :')
        radioUseSpaces=Radiobutton(frameIndentType,variable=self.indentBySpaces,
            value=1,text='Tab key inserts spaces')
        radioUseTabs=Radiobutton(frameIndentType,variable=self.indentBySpaces,
            value=0,text='Tab key inserts tabs')
        labelIndentSizeTitle=Label(frameIndentSize,
                text='Choose indentation size :')
        labelSpaceNumTitle=Label(frameIndentSize,justify=LEFT,
                text='indent width')
        self.scaleSpaceNum=Scale(frameIndentSize,variable=self.spaceNum,
                orient='horizontal',tickinterval=2,from_=2,to=16)
        #labeltabColsTitle=Label(frameIndentSize,justify=LEFT,
        #        text='when tab key inserts tabs,\ncolumns per tab')
        #self.scaleTabCols=Scale(frameIndentSize,variable=self.tabCols,
        #        orient='horizontal',tickinterval=2,from_=2,to=8)
        #widget packing
        #body
        frameFont.pack(side=LEFT,padx=5,pady=10,expand=TRUE,fill=BOTH)
        frameIndent.pack(side=LEFT,padx=5,pady=10,fill=Y)
        #frameFont
        labelFontTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        frameFontName.pack(side=TOP,padx=5,pady=5,fill=X)
        frameFontParam.pack(side=TOP,padx=5,pady=5,fill=X)
        labelFontNameTitle.pack(side=TOP,anchor=W)
        self.listFontName.pack(side=LEFT,expand=TRUE,fill=X)
        scrollFont.pack(side=LEFT,fill=Y)
        labelFontSizeTitle.pack(side=LEFT,anchor=W)
        self.optMenuFontSize.pack(side=LEFT,anchor=W)
        checkFontBold.pack(side=LEFT,anchor=W,padx=20)
        frameFontSample.pack(side=TOP,padx=5,pady=5,expand=TRUE,fill=BOTH)
        self.labelFontSample.pack(expand=TRUE,fill=BOTH)
        #frameIndent
        labelIndentTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        frameIndentType.pack(side=TOP,padx=5,fill=X)
        frameIndentSize.pack(side=TOP,padx=5,pady=5,fill=BOTH)
        labelIndentTypeTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        radioUseSpaces.pack(side=TOP,anchor=W,padx=5)
        radioUseTabs.pack(side=TOP,anchor=W,padx=5)
        labelIndentSizeTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        labelSpaceNumTitle.pack(side=TOP,anchor=W,padx=5)
        self.scaleSpaceNum.pack(side=TOP,padx=5,fill=X)
        #labeltabColsTitle.pack(side=TOP,anchor=W,padx=5)
        #self.scaleTabCols.pack(side=TOP,padx=5,fill=X)
        return frame

    def CreatePageHighlight(self):
        self.builtinTheme=StringVar(self)
        self.customTheme=StringVar(self)
        self.fgHilite=BooleanVar(self)
        self.colour=StringVar(self)
        self.fontName=StringVar(self)
        self.themeIsBuiltin=BooleanVar(self)
        self.highlightTarget=StringVar(self)
        ##widget creation
        #body frame
        frame=self.tabPages.pages['Highlighting']['page']
        #body section frames
        frameCustom=Frame(frame,borderwidth=2,relief=GROOVE)
        frameTheme=Frame(frame,borderwidth=2,relief=GROOVE)
        #frameCustom
        self.textHighlightSample=Text(frameCustom,relief=SOLID,borderwidth=1,
            font=('courier',12,''),cursor='hand2',width=21,height=10,
            takefocus=FALSE,highlightthickness=0,wrap=NONE)
        text=self.textHighlightSample
        text.bind('<Double-Button-1>',lambda e: 'break')
        text.bind('<B1-Motion>',lambda e: 'break')
        textAndTags=(('#you can click here','comment'),('\n','normal'),
            ('#to choose items','comment'),('\n','normal'),('def','keyword'),
            (' ','normal'),('func','definition'),('(param):','normal'),
            ('\n  ','normal'),('"""string"""','string'),('\n  var0 = ','normal'),
            ("'string'",'string'),('\n  var1 = ','normal'),("'selected'",'hilite'),
            ('\n  var2 = ','normal'),("'found'",'hit'),('\n\n','normal'),
            (' error ','error'),(' ','normal'),('cursor |','cursor'),
            ('\n ','normal'),('shell','console'),(' ','normal'),('stdout','stdout'),
            (' ','normal'),('stderr','stderr'),('\n','normal'))
        for txTa in textAndTags:
            text.insert(END,txTa[0],txTa[1])
        for element in self.themeElements.keys():
            text.tag_bind(self.themeElements[element][0],'<ButtonPress-1>',
                lambda event,elem=element: event.widget.winfo_toplevel()
                .highlightTarget.set(elem))
        text.config(state=DISABLED)
        self.frameColourSet=Frame(frameCustom,relief=SOLID,borderwidth=1)
        frameFgBg=Frame(frameCustom)
        labelCustomTitle=Label(frameCustom,text='Set Custom Highlighting')
        buttonSetColour=Button(self.frameColourSet,text='Choose Colour for :',
            command=self.GetColour,highlightthickness=0)
        self.optMenuHighlightTarget=DynOptionMenu(self.frameColourSet,
            self.highlightTarget,None,highlightthickness=0)#,command=self.SetHighlightTargetBinding
        self.radioFg=Radiobutton(frameFgBg,variable=self.fgHilite,
            value=1,text='Foreground',command=self.SetColourSampleBinding)
        self.radioBg=Radiobutton(frameFgBg,variable=self.fgHilite,
            value=0,text='Background',command=self.SetColourSampleBinding)
        self.fgHilite.set(1)
        buttonSaveCustomTheme=Button(frameCustom,
            text='Save as New Custom Theme',command=self.SaveAsNewTheme)
        #frameTheme
        labelThemeTitle=Label(frameTheme,text='Select a Highlighting Theme')
        labelTypeTitle=Label(frameTheme,text='Select : ')
        self.radioThemeBuiltin=Radiobutton(frameTheme,variable=self.themeIsBuiltin,
            value=1,command=self.SetThemeType,text='a Built-in Theme')
        self.radioThemeCustom=Radiobutton(frameTheme,variable=self.themeIsBuiltin,
            value=0,command=self.SetThemeType,text='a Custom Theme')
        self.optMenuThemeBuiltin=DynOptionMenu(frameTheme,
            self.builtinTheme,None,command=None)
        self.optMenuThemeCustom=DynOptionMenu(frameTheme,
            self.customTheme,None,command=None)
        self.buttonDeleteCustomTheme=Button(frameTheme,text='Delete Custom Theme',
                command=self.DeleteCustomTheme)
        ##widget packing
        #body
        frameCustom.pack(side=LEFT,padx=5,pady=10,expand=TRUE,fill=BOTH)
        frameTheme.pack(side=LEFT,padx=5,pady=10,fill=Y)
        #frameCustom
        labelCustomTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        self.frameColourSet.pack(side=TOP,padx=5,pady=5,expand=TRUE,fill=X)
        frameFgBg.pack(side=TOP,padx=5,pady=0)
        self.textHighlightSample.pack(side=TOP,padx=5,pady=5,expand=TRUE,
            fill=BOTH)
        buttonSetColour.pack(side=TOP,expand=TRUE,fill=X,padx=8,pady=4)
        self.optMenuHighlightTarget.pack(side=TOP,expand=TRUE,fill=X,padx=8,pady=3)
        self.radioFg.pack(side=LEFT,anchor=E)
        self.radioBg.pack(side=RIGHT,anchor=W)
        buttonSaveCustomTheme.pack(side=BOTTOM,fill=X,padx=5,pady=5)
        #frameTheme
        labelThemeTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        labelTypeTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        self.radioThemeBuiltin.pack(side=TOP,anchor=W,padx=5)
        self.radioThemeCustom.pack(side=TOP,anchor=W,padx=5,pady=2)
        self.optMenuThemeBuiltin.pack(side=TOP,fill=X,padx=5,pady=5)
        self.optMenuThemeCustom.pack(side=TOP,fill=X,anchor=W,padx=5,pady=5)
        self.buttonDeleteCustomTheme.pack(side=TOP,fill=X,padx=5,pady=5)
        return frame

    def CreatePageKeys(self):
        #tkVars
        self.bindingTarget=StringVar(self)
        self.builtinKeys=StringVar(self)
        self.customKeys=StringVar(self)
        self.keysAreBuiltin=BooleanVar(self)
        self.keyBinding=StringVar(self)
        ##widget creation
        #body frame
        frame=self.tabPages.pages['Keys']['page']
        #body section frames
        frameCustom=Frame(frame,borderwidth=2,relief=GROOVE)
        frameKeySets=Frame(frame,borderwidth=2,relief=GROOVE)
        #frameCustom
        frameTarget=Frame(frameCustom)
        labelCustomTitle=Label(frameCustom,text='Set Custom Key Bindings')
        labelTargetTitle=Label(frameTarget,text='Action - Key(s)')
        scrollTargetY=Scrollbar(frameTarget)
        scrollTargetX=Scrollbar(frameTarget,orient=HORIZONTAL)
        self.listBindings=Listbox(frameTarget,takefocus=FALSE,
                exportselection=FALSE)
        self.listBindings.bind('<ButtonRelease-1>',self.KeyBindingSelected)
        scrollTargetY.config(command=self.listBindings.yview)
        scrollTargetX.config(command=self.listBindings.xview)
        self.listBindings.config(yscrollcommand=scrollTargetY.set)
        self.listBindings.config(xscrollcommand=scrollTargetX.set)
        self.buttonNewKeys=Button(frameCustom,text='Get New Keys for Selection',
            command=self.GetNewKeys,state=DISABLED)
        buttonSaveCustomKeys=Button(frameCustom,
                text='Save as New Custom Key Set',command=self.SaveAsNewKeySet)
        #frameKeySets
        labelKeysTitle=Label(frameKeySets,text='Select a Key Set')
        labelTypeTitle=Label(frameKeySets,text='Select : ')
        self.radioKeysBuiltin=Radiobutton(frameKeySets,variable=self.keysAreBuiltin,
            value=1,command=self.SetKeysType,text='a Built-in Key Set')
        self.radioKeysCustom=Radiobutton(frameKeySets,variable=self.keysAreBuiltin,
            value=0,command=self.SetKeysType,text='a Custom Key Set')
        self.optMenuKeysBuiltin=DynOptionMenu(frameKeySets,
            self.builtinKeys,None,command=None)
        self.optMenuKeysCustom=DynOptionMenu(frameKeySets,
            self.customKeys,None,command=None)
        self.buttonDeleteCustomKeys=Button(frameKeySets,text='Delete Custom Key Set',
                command=self.DeleteCustomKeys)
        ##widget packing
        #body
        frameCustom.pack(side=LEFT,padx=5,pady=5,expand=TRUE,fill=BOTH)
        frameKeySets.pack(side=LEFT,padx=5,pady=5,fill=Y)
        #frameCustom
        labelCustomTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        buttonSaveCustomKeys.pack(side=BOTTOM,fill=X,padx=5,pady=5)
        self.buttonNewKeys.pack(side=BOTTOM,fill=X,padx=5,pady=5)
        frameTarget.pack(side=LEFT,padx=5,pady=5,expand=TRUE,fill=BOTH)
        #frame target
        frameTarget.columnconfigure(0,weight=1)
        frameTarget.rowconfigure(1,weight=1)
        labelTargetTitle.grid(row=0,column=0,columnspan=2,sticky=W)
        self.listBindings.grid(row=1,column=0,sticky=NSEW)
        scrollTargetY.grid(row=1,column=1,sticky=NS)
        scrollTargetX.grid(row=2,column=0,sticky=EW)
        #frameKeySets
        labelKeysTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        labelTypeTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        self.radioKeysBuiltin.pack(side=TOP,anchor=W,padx=5)
        self.radioKeysCustom.pack(side=TOP,anchor=W,padx=5,pady=2)
        self.optMenuKeysBuiltin.pack(side=TOP,fill=X,padx=5,pady=5)
        self.optMenuKeysCustom.pack(side=TOP,fill=X,anchor=W,padx=5,pady=5)
        self.buttonDeleteCustomKeys.pack(side=TOP,fill=X,padx=5,pady=5)
        return frame

    def CreatePageGeneral(self):
        #tkVars
        self.winWidth=StringVar(self)
        self.winHeight=StringVar(self)
        self.startupEdit=IntVar(self)
        self.autoSave=IntVar(self)
        self.encoding=StringVar(self)
        self.userHelpBrowser=BooleanVar(self)
        self.helpBrowser=StringVar(self)
        #widget creation
        #body
        frame=self.tabPages.pages['General']['page']
        #body section frames
        frameRun=Frame(frame,borderwidth=2,relief=GROOVE)
        frameSave=Frame(frame,borderwidth=2,relief=GROOVE)
        frameWinSize=Frame(frame,borderwidth=2,relief=GROOVE)
        frameEncoding=Frame(frame,borderwidth=2,relief=GROOVE)
        frameHelp=Frame(frame,borderwidth=2,relief=GROOVE)
        #frameRun
        labelRunTitle=Label(frameRun,text='Startup Preferences')
        labelRunChoiceTitle=Label(frameRun,text='At Startup')
        radioStartupEdit=Radiobutton(frameRun,variable=self.startupEdit,
            value=1,command=self.SetKeysType,text="Open Edit Window")
        radioStartupShell=Radiobutton(frameRun,variable=self.startupEdit,
            value=0,command=self.SetKeysType,text='Open Shell Window')
        #frameSave
        labelSaveTitle=Label(frameSave,text='Autosave Preference')
        labelRunSaveTitle=Label(frameSave,text='At Start of Run (F5)  ')
        radioSaveAsk=Radiobutton(frameSave,variable=self.autoSave,
            value=0,command=self.SetKeysType,text="Prompt to Save")
        radioSaveAuto=Radiobutton(frameSave,variable=self.autoSave,
            value=1,command=self.SetKeysType,text='No Prompt')
        #frameWinSize
        labelWinSizeTitle=Label(frameWinSize,text='Initial Window Size'+
                '  (in characters)')
        labelWinWidthTitle=Label(frameWinSize,text='Width')
        entryWinWidth=Entry(frameWinSize,textvariable=self.winWidth,
                width=3)
        labelWinHeightTitle=Label(frameWinSize,text='Height')
        entryWinHeight=Entry(frameWinSize,textvariable=self.winHeight,
                width=3)
        #frameEncoding
        labelEncodingTitle=Label(frameEncoding,text="Default Source Encoding")
        radioEncLocale=Radiobutton(frameEncoding,variable=self.encoding,
            value="locale",text="Locale-defined")
        radioEncUTF8=Radiobutton(frameEncoding,variable=self.encoding,
            value="utf-8",text="UTF-8")
        radioEncNone=Radiobutton(frameEncoding,variable=self.encoding,
            value="none",text="None")
        #frameHelp
        ##labelHelpTitle=Label(frameHelp,text='Help Options')
        frameHelpList=Frame(frameHelp)
        frameHelpListButtons=Frame(frameHelpList)
        labelHelpListTitle=Label(frameHelpList,text='Additional Help Sources:')
        scrollHelpList=Scrollbar(frameHelpList)
        self.listHelp=Listbox(frameHelpList,height=5,takefocus=FALSE,
                exportselection=FALSE)
        scrollHelpList.config(command=self.listHelp.yview)
        self.listHelp.config(yscrollcommand=scrollHelpList.set)
        self.listHelp.bind('<ButtonRelease-1>',self.HelpSourceSelected)
        self.buttonHelpListEdit=Button(frameHelpListButtons,text='Edit',
                state=DISABLED,width=8,command=self.HelpListItemEdit)
        self.buttonHelpListAdd=Button(frameHelpListButtons,text='Add',
                width=8,command=self.HelpListItemAdd)
        self.buttonHelpListRemove=Button(frameHelpListButtons,text='Remove',
                state=DISABLED,width=8,command=self.HelpListItemRemove)
        # the following is better handled by the BROWSER environment
        # variable under unix/linux
        #checkHelpBrowser=Checkbutton(frameHelp,variable=self.userHelpBrowser,
        #    onvalue=1,offvalue=0,text='user specified (html) help browser:',
        #    command=self.OnCheckUserHelpBrowser)
        #self.entryHelpBrowser=Entry(frameHelp,textvariable=self.helpBrowser,
        #        width=40)
        #widget packing
        #body
        frameRun.pack(side=TOP,padx=5,pady=5,fill=X)
        frameSave.pack(side=TOP,padx=5,pady=5,fill=X)
        frameWinSize.pack(side=TOP,padx=5,pady=5,fill=X)
        frameEncoding.pack(side=TOP,padx=5,pady=5,fill=X)
        frameHelp.pack(side=TOP,padx=5,pady=5,expand=TRUE,fill=BOTH)
        #frameRun
        labelRunTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        labelRunChoiceTitle.pack(side=LEFT,anchor=W,padx=5,pady=5)
        radioStartupShell.pack(side=RIGHT,anchor=W,padx=5,pady=5)
        radioStartupEdit.pack(side=RIGHT,anchor=W,padx=5,pady=5)
        #frameSave
        labelSaveTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        labelRunSaveTitle.pack(side=LEFT,anchor=W,padx=5,pady=5)
        radioSaveAuto.pack(side=RIGHT,anchor=W,padx=5,pady=5)
        radioSaveAsk.pack(side=RIGHT,anchor=W,padx=5,pady=5)
        #frameWinSize
        labelWinSizeTitle.pack(side=LEFT,anchor=W,padx=5,pady=5)
        entryWinHeight.pack(side=RIGHT,anchor=E,padx=10,pady=5)
        labelWinHeightTitle.pack(side=RIGHT,anchor=E,pady=5)
        entryWinWidth.pack(side=RIGHT,anchor=E,padx=10,pady=5)
        labelWinWidthTitle.pack(side=RIGHT,anchor=E,pady=5)
        #frameEncoding
        labelEncodingTitle.pack(side=LEFT,anchor=W,padx=5,pady=5)
        radioEncNone.pack(side=RIGHT,anchor=E,pady=5)
        radioEncUTF8.pack(side=RIGHT,anchor=E,pady=5)
        radioEncLocale.pack(side=RIGHT,anchor=E,pady=5)
        #frameHelp
        ##labelHelpTitle.pack(side=TOP,anchor=W,padx=5,pady=5)
        frameHelpListButtons.pack(side=RIGHT,padx=5,pady=5,fill=Y)
        frameHelpList.pack(side=TOP,padx=5,pady=5,expand=TRUE,fill=BOTH)
        labelHelpListTitle.pack(side=TOP,anchor=W)
        scrollHelpList.pack(side=RIGHT,anchor=W,fill=Y)
        self.listHelp.pack(side=LEFT,anchor=E,expand=TRUE,fill=BOTH)
        self.buttonHelpListEdit.pack(side=TOP,anchor=W,pady=5)
        self.buttonHelpListAdd.pack(side=TOP,anchor=W)
        self.buttonHelpListRemove.pack(side=TOP,anchor=W,pady=5)
        #checkHelpBrowser.pack(side=TOP,anchor=W,padx=5)
        #self.entryHelpBrowser.pack(side=TOP,anchor=W,padx=5,pady=5)
        return frame

    def AttachVarCallbacks(self):
        self.fontSize.trace_variable('w',self.VarChanged_fontSize)
        self.fontName.trace_variable('w',self.VarChanged_fontName)
        self.fontBold.trace_variable('w',self.VarChanged_fontBold)
        self.spaceNum.trace_variable('w',self.VarChanged_spaceNum)
        #self.tabCols.trace_variable('w',self.VarChanged_tabCols)
        self.indentBySpaces.trace_variable('w',self.VarChanged_indentBySpaces)
        self.colour.trace_variable('w',self.VarChanged_colour)
        self.builtinTheme.trace_variable('w',self.VarChanged_builtinTheme)
        self.customTheme.trace_variable('w',self.VarChanged_customTheme)
        self.themeIsBuiltin.trace_variable('w',self.VarChanged_themeIsBuiltin)
        self.highlightTarget.trace_variable('w',self.VarChanged_highlightTarget)
        self.keyBinding.trace_variable('w',self.VarChanged_keyBinding)
        self.builtinKeys.trace_variable('w',self.VarChanged_builtinKeys)
        self.customKeys.trace_variable('w',self.VarChanged_customKeys)
        self.keysAreBuiltin.trace_variable('w',self.VarChanged_keysAreBuiltin)
        self.winWidth.trace_variable('w',self.VarChanged_winWidth)
        self.winHeight.trace_variable('w',self.VarChanged_winHeight)
        self.startupEdit.trace_variable('w',self.VarChanged_startupEdit)
        self.autoSave.trace_variable('w',self.VarChanged_autoSave)
        self.encoding.trace_variable('w',self.VarChanged_encoding)

    def VarChanged_fontSize(self,*params):
        value=self.fontSize.get()
        self.AddChangedItem('main','EditorWindow','font-size',value)

    def VarChanged_fontName(self,*params):
        value=self.fontName.get()
        self.AddChangedItem('main','EditorWindow','font',value)

    def VarChanged_fontBold(self,*params):
        value=self.fontBold.get()
        self.AddChangedItem('main','EditorWindow','font-bold',value)

    def VarChanged_indentBySpaces(self,*params):
        value=self.indentBySpaces.get()
        self.AddChangedItem('main','Indent','use-spaces',value)

    def VarChanged_spaceNum(self,*params):
        value=self.spaceNum.get()
        self.AddChangedItem('main','Indent','num-spaces',value)

    #def VarChanged_tabCols(self,*params):
    #    value=self.tabCols.get()
    #    self.AddChangedItem('main','Indent','tab-cols',value)

    def VarChanged_colour(self,*params):
        self.OnNewColourSet()

    def VarChanged_builtinTheme(self,*params):
        value=self.builtinTheme.get()
        self.AddChangedItem('main','Theme','name',value)
        self.PaintThemeSample()

    def VarChanged_customTheme(self,*params):
        value=self.customTheme.get()
        if value != '- no custom themes -':
            self.AddChangedItem('main','Theme','name',value)
            self.PaintThemeSample()

    def VarChanged_themeIsBuiltin(self,*params):
        value=self.themeIsBuiltin.get()
        self.AddChangedItem('main','Theme','default',value)
        if value:
            self.VarChanged_builtinTheme()
        else:
            self.VarChanged_customTheme()

    def VarChanged_highlightTarget(self,*params):
        self.SetHighlightTarget()

    def VarChanged_keyBinding(self,*params):
        value=self.keyBinding.get()
        keySet=self.customKeys.get()
        event=self.listBindings.get(ANCHOR).split()[0]
        if idleConf.IsCoreBinding(event):
            #this is a core keybinding
            self.AddChangedItem('keys',keySet,event,value)
        else: #this is an extension key binding
            extName=idleConf.GetExtnNameForEvent(event)
            extKeybindSection=extName+'_cfgBindings'
            self.AddChangedItem('extensions',extKeybindSection,event,value)

    def VarChanged_builtinKeys(self,*params):
        value=self.builtinKeys.get()
        self.AddChangedItem('main','Keys','name',value)
        self.LoadKeysList(value)

    def VarChanged_customKeys(self,*params):
        value=self.customKeys.get()
        if value != '- no custom keys -':
            self.AddChangedItem('main','Keys','name',value)
            self.LoadKeysList(value)

    def VarChanged_keysAreBuiltin(self,*params):
        value=self.keysAreBuiltin.get()
        self.AddChangedItem('main','Keys','default',value)
        if value:
            self.VarChanged_builtinKeys()
        else:
            self.VarChanged_customKeys()

    def VarChanged_winWidth(self,*params):
        value=self.winWidth.get()
        self.AddChangedItem('main','EditorWindow','width',value)

    def VarChanged_winHeight(self,*params):
        value=self.winHeight.get()
        self.AddChangedItem('main','EditorWindow','height',value)

    def VarChanged_startupEdit(self,*params):
        value=self.startupEdit.get()
        self.AddChangedItem('main','General','editor-on-startup',value)

    def VarChanged_autoSave(self,*params):
        value=self.autoSave.get()
        self.AddChangedItem('main','General','autosave',value)

    def VarChanged_encoding(self,*params):
        value=self.encoding.get()
        self.AddChangedItem('main','EditorWindow','encoding',value)

    def ResetChangedItems(self):
        #When any config item is changed in this dialog, an entry
        #should be made in the relevant section (config type) of this
        #dictionary. The key should be the config file section name and the
        #value a dictionary, whose key:value pairs are item=value pairs for
        #that config file section.
        self.changedItems={'main':{},'highlight':{},'keys':{},'extensions':{}}

    def AddChangedItem(self,type,section,item,value):
        value=str(value) #make sure we use a string
        if not self.changedItems[type].has_key(section):
            self.changedItems[type][section]={}
        self.changedItems[type][section][item]=value

    def GetDefaultItems(self):
        dItems={'main':{},'highlight':{},'keys':{},'extensions':{}}
        for configType in dItems.keys():
            sections=idleConf.GetSectionList('default',configType)
            for section in sections:
                dItems[configType][section]={}
                options=idleConf.defaultCfg[configType].GetOptionList(section)
                for option in options:
                    dItems[configType][section][option]=(
                            idleConf.defaultCfg[configType].Get(section,option))
        return dItems

    def SetThemeType(self):
        if self.themeIsBuiltin.get():
            self.optMenuThemeBuiltin.config(state=NORMAL)
            self.optMenuThemeCustom.config(state=DISABLED)
            self.buttonDeleteCustomTheme.config(state=DISABLED)
        else:
            self.optMenuThemeBuiltin.config(state=DISABLED)
            self.radioThemeCustom.config(state=NORMAL)
            self.optMenuThemeCustom.config(state=NORMAL)
            self.buttonDeleteCustomTheme.config(state=NORMAL)

    def SetKeysType(self):
        if self.keysAreBuiltin.get():
            self.optMenuKeysBuiltin.config(state=NORMAL)
            self.optMenuKeysCustom.config(state=DISABLED)
            self.buttonDeleteCustomKeys.config(state=DISABLED)
        else:
            self.optMenuKeysBuiltin.config(state=DISABLED)
            self.radioKeysCustom.config(state=NORMAL)
            self.optMenuKeysCustom.config(state=NORMAL)
            self.buttonDeleteCustomKeys.config(state=NORMAL)

    def GetNewKeys(self):
        listIndex=self.listBindings.index(ANCHOR)
        binding=self.listBindings.get(listIndex)
        bindName=binding.split()[0] #first part, up to first space
        if self.keysAreBuiltin.get():
            currentKeySetName=self.builtinKeys.get()
        else:
            currentKeySetName=self.customKeys.get()
        currentBindings=idleConf.GetCurrentKeySet()
        if currentKeySetName in self.changedItems['keys'].keys(): #unsaved changes
            keySetChanges=self.changedItems['keys'][currentKeySetName]
            for event in keySetChanges.keys():
                currentBindings[event]=keySetChanges[event].split()
        currentKeySequences=currentBindings.values()
        newKeys=GetKeysDialog(self,'Get New Keys',bindName,
                currentKeySequences).result
        if newKeys: #new keys were specified
            if self.keysAreBuiltin.get(): #current key set is a built-in
                message=('Your changes will be saved as a new Custom Key Set. '+
                        'Enter a name for your new Custom Key Set below.')
                newKeySet=self.GetNewKeysName(message)
                if not newKeySet: #user cancelled custom key set creation
                    self.listBindings.select_set(listIndex)
                    self.listBindings.select_anchor(listIndex)
                    return
                else: #create new custom key set based on previously active key set
                    self.CreateNewKeySet(newKeySet)
            self.listBindings.delete(listIndex)
            self.listBindings.insert(listIndex,bindName+' - '+newKeys)
            self.listBindings.select_set(listIndex)
            self.listBindings.select_anchor(listIndex)
            self.keyBinding.set(newKeys)
        else:
            self.listBindings.select_set(listIndex)
            self.listBindings.select_anchor(listIndex)

    def GetNewKeysName(self,message):
        usedNames=(idleConf.GetSectionList('user','keys')+
                idleConf.GetSectionList('default','keys'))
        newKeySet=GetCfgSectionNameDialog(self,'New Custom Key Set',
                message,usedNames).result
        return newKeySet

    def SaveAsNewKeySet(self):
        newKeysName=self.GetNewKeysName('New Key Set Name:')
        if newKeysName:
            self.CreateNewKeySet(newKeysName)

    def KeyBindingSelected(self,event):
        self.buttonNewKeys.config(state=NORMAL)

    def CreateNewKeySet(self,newKeySetName):
        #creates new custom key set based on the previously active key set,
        #and makes the new key set active
        if self.keysAreBuiltin.get():
            prevKeySetName=self.builtinKeys.get()
        else:
            prevKeySetName=self.customKeys.get()
        prevKeys=idleConf.GetCoreKeys(prevKeySetName)
        newKeys={}
        for event in prevKeys.keys(): #add key set to changed items
            eventName=event[2:-2] #trim off the angle brackets
            binding=string.join(prevKeys[event])
            newKeys[eventName]=binding
        #handle any unsaved changes to prev key set
        if prevKeySetName in self.changedItems['keys'].keys():
            keySetChanges=self.changedItems['keys'][prevKeySetName]
            for event in keySetChanges.keys():
                newKeys[event]=keySetChanges[event]
        #save the new theme
        self.SaveNewKeySet(newKeySetName,newKeys)
        #change gui over to the new key set
        customKeyList=idleConf.GetSectionList('user','keys')
        customKeyList.sort()
        self.optMenuKeysCustom.SetMenu(customKeyList,newKeySetName)
        self.keysAreBuiltin.set(0)
        self.SetKeysType()

    def LoadKeysList(self,keySetName):
        reselect=0
        newKeySet=0
        if self.listBindings.curselection():
            reselect=1
            listIndex=self.listBindings.index(ANCHOR)
        keySet=idleConf.GetKeySet(keySetName)
        bindNames=keySet.keys()
        bindNames.sort()
        self.listBindings.delete(0,END)
        for bindName in bindNames:
            key=string.join(keySet[bindName]) #make key(s) into a string
            bindName=bindName[2:-2] #trim off the angle brackets
            if keySetName in self.changedItems['keys'].keys():
                #handle any unsaved changes to this key set
                if bindName in self.changedItems['keys'][keySetName].keys():
                    key=self.changedItems['keys'][keySetName][bindName]
            self.listBindings.insert(END, bindName+' - '+key)
        if reselect:
            self.listBindings.see(listIndex)
            self.listBindings.select_set(listIndex)
            self.listBindings.select_anchor(listIndex)

    def DeleteCustomKeys(self):
        keySetName=self.customKeys.get()
        if not tkMessageBox.askyesno('Delete Key Set','Are you sure you wish '+
                                     'to delete the key set '+`keySetName`+' ?',
                                     parent=self):
            return
        #remove key set from config
        idleConf.userCfg['keys'].remove_section(keySetName)
        if self.changedItems['keys'].has_key(keySetName):
            del(self.changedItems['keys'][keySetName])
        #write changes
        idleConf.userCfg['keys'].Save()
        #reload user key set list
        itemList=idleConf.GetSectionList('user','keys')
        itemList.sort()
        if not itemList:
            self.radioKeysCustom.config(state=DISABLED)
            self.optMenuKeysCustom.SetMenu(itemList,'- no custom keys -')
        else:
            self.optMenuKeysCustom.SetMenu(itemList,itemList[0])
        #revert to default key set
        self.keysAreBuiltin.set(idleConf.defaultCfg['main'].Get('Keys','default'))
        self.builtinKeys.set(idleConf.defaultCfg['main'].Get('Keys','name'))
        #user can't back out of these changes, they must be applied now
        self.Apply()
        self.SetKeysType()

    def DeleteCustomTheme(self):
        themeName=self.customTheme.get()
        if not tkMessageBox.askyesno('Delete Theme','Are you sure you wish '+
                                     'to delete the theme '+`themeName`+' ?',
                                     parent=self):
            return
        #remove theme from config
        idleConf.userCfg['highlight'].remove_section(themeName)
        if self.changedItems['highlight'].has_key(themeName):
            del(self.changedItems['highlight'][themeName])
        #write changes
        idleConf.userCfg['highlight'].Save()
        #reload user theme list
        itemList=idleConf.GetSectionList('user','highlight')
        itemList.sort()
        if not itemList:
            self.radioThemeCustom.config(state=DISABLED)
            self.optMenuThemeCustom.SetMenu(itemList,'- no custom themes -')
        else:
            self.optMenuThemeCustom.SetMenu(itemList,itemList[0])
        #revert to default theme
        self.themeIsBuiltin.set(idleConf.defaultCfg['main'].Get('Theme','default'))
        self.builtinTheme.set(idleConf.defaultCfg['main'].Get('Theme','name'))
        #user can't back out of these changes, they must be applied now
        self.Apply()
        self.SetThemeType()

    def GetColour(self):
        target=self.highlightTarget.get()
        prevColour=self.frameColourSet.cget('bg')
        rgbTuplet, colourString = tkColorChooser.askcolor(parent=self,
            title='Pick new colour for : '+target,initialcolor=prevColour)
        if colourString and (colourString!=prevColour):
            #user didn't cancel, and they chose a new colour
            if self.themeIsBuiltin.get(): #current theme is a built-in
                message=('Your changes will be saved as a new Custom Theme. '+
                        'Enter a name for your new Custom Theme below.')
                newTheme=self.GetNewThemeName(message)
                if not newTheme: #user cancelled custom theme creation
                    return
                else: #create new custom theme based on previously active theme
                    self.CreateNewTheme(newTheme)
                    self.colour.set(colourString)
            else: #current theme is user defined
                self.colour.set(colourString)

    def OnNewColourSet(self):
        newColour=self.colour.get()
        self.frameColourSet.config(bg=newColour)#set sample
        if self.fgHilite.get(): plane='foreground'
        else: plane='background'
        sampleElement=self.themeElements[self.highlightTarget.get()][0]
        self.textHighlightSample.tag_config(sampleElement, **{plane:newColour})
        theme=self.customTheme.get()
        themeElement=sampleElement+'-'+plane
        self.AddChangedItem('highlight',theme,themeElement,newColour)

    def GetNewThemeName(self,message):
        usedNames=(idleConf.GetSectionList('user','highlight')+
                idleConf.GetSectionList('default','highlight'))
        newTheme=GetCfgSectionNameDialog(self,'New Custom Theme',
                message,usedNames).result
        return newTheme

    def SaveAsNewTheme(self):
        newThemeName=self.GetNewThemeName('New Theme Name:')
        if newThemeName:
            self.CreateNewTheme(newThemeName)

    def CreateNewTheme(self,newThemeName):
        #creates new custom theme based on the previously active theme,
        #and makes the new theme active
        if self.themeIsBuiltin.get():
            themeType='default'
            themeName=self.builtinTheme.get()
        else:
            themeType='user'
            themeName=self.customTheme.get()
        newTheme=idleConf.GetThemeDict(themeType,themeName)
        #apply any of the old theme's unsaved changes to the new theme
        if themeName in self.changedItems['highlight'].keys():
            themeChanges=self.changedItems['highlight'][themeName]
            for element in themeChanges.keys():
                newTheme[element]=themeChanges[element]
        #save the new theme
        self.SaveNewTheme(newThemeName,newTheme)
        #change gui over to the new theme
        customThemeList=idleConf.GetSectionList('user','highlight')
        customThemeList.sort()
        self.optMenuThemeCustom.SetMenu(customThemeList,newThemeName)
        self.themeIsBuiltin.set(0)
        self.SetThemeType()

    def OnListFontButtonRelease(self,event):
        font = self.listFontName.get(ANCHOR)
        self.fontName.set(font.lower())
        self.SetFontSample()

    def SetFontSample(self,event=None):
        fontName=self.fontName.get()
        if self.fontBold.get():
            fontWeight=tkFont.BOLD
        else:
            fontWeight=tkFont.NORMAL
        self.editFont.config(size=self.fontSize.get(),
                weight=fontWeight,family=fontName)

    def SetHighlightTarget(self):
        if self.highlightTarget.get()=='Cursor': #bg not possible
            self.radioFg.config(state=DISABLED)
            self.radioBg.config(state=DISABLED)
            self.fgHilite.set(1)
        else: #both fg and bg can be set
            self.radioFg.config(state=NORMAL)
            self.radioBg.config(state=NORMAL)
            self.fgHilite.set(1)
        self.SetColourSample()

    def SetColourSampleBinding(self,*args):
        self.SetColourSample()

    def SetColourSample(self):
        #set the colour smaple area
        tag=self.themeElements[self.highlightTarget.get()][0]
        if self.fgHilite.get(): plane='foreground'
        else: plane='background'
        colour=self.textHighlightSample.tag_cget(tag,plane)
        self.frameColourSet.config(bg=colour)

    def PaintThemeSample(self):
        if self.themeIsBuiltin.get(): #a default theme
            theme=self.builtinTheme.get()
        else: #a user theme
            theme=self.customTheme.get()
        for elementTitle in self.themeElements.keys():
            element=self.themeElements[elementTitle][0]
            colours=idleConf.GetHighlight(theme,element)
            if element=='cursor': #cursor sample needs special painting
                colours['background']=idleConf.GetHighlight(theme,
                        'normal', fgBg='bg')
            #handle any unsaved changes to this theme
            if theme in self.changedItems['highlight'].keys():
                themeDict=self.changedItems['highlight'][theme]
                if themeDict.has_key(element+'-foreground'):
                    colours['foreground']=themeDict[element+'-foreground']
                if themeDict.has_key(element+'-background'):
                    colours['background']=themeDict[element+'-background']
            self.textHighlightSample.tag_config(element, **colours)
        self.SetColourSample()

##     def OnCheckUserHelpBrowser(self):
##         if self.userHelpBrowser.get():
##             self.entryHelpBrowser.config(state=NORMAL)
##         else:
##             self.entryHelpBrowser.config(state=DISABLED)

    def HelpSourceSelected(self,event):
        self.SetHelpListButtonStates()

    def SetHelpListButtonStates(self):
        if self.listHelp.size()<1: #no entries in list
            self.buttonHelpListEdit.config(state=DISABLED)
            self.buttonHelpListRemove.config(state=DISABLED)
        else: #there are some entries
            if self.listHelp.curselection(): #there currently is a selection
                self.buttonHelpListEdit.config(state=NORMAL)
                self.buttonHelpListRemove.config(state=NORMAL)
            else:  #there currently is not a selection
                self.buttonHelpListEdit.config(state=DISABLED)
                self.buttonHelpListRemove.config(state=DISABLED)

    def HelpListItemAdd(self):
        helpSource=GetHelpSourceDialog(self,'New Help Source').result
        if helpSource:
            self.userHelpList.append( (helpSource[0],helpSource[1]) )
            self.listHelp.insert(END,helpSource[0])
            self.UpdateUserHelpChangedItems()
        self.SetHelpListButtonStates()

    def HelpListItemEdit(self):
        itemIndex=self.listHelp.index(ANCHOR)
        helpSource=self.userHelpList[itemIndex]
        newHelpSource=GetHelpSourceDialog(self,'Edit Help Source',
                menuItem=helpSource[0],filePath=helpSource[1]).result
        if (not newHelpSource) or (newHelpSource==helpSource):
            return #no changes
        self.userHelpList[itemIndex]=newHelpSource
        self.listHelp.delete(itemIndex)
        self.listHelp.insert(itemIndex,newHelpSource[0])
        self.UpdateUserHelpChangedItems()
        self.SetHelpListButtonStates()

    def HelpListItemRemove(self):
        itemIndex=self.listHelp.index(ANCHOR)
        del(self.userHelpList[itemIndex])
        self.listHelp.delete(itemIndex)
        self.UpdateUserHelpChangedItems()
        self.SetHelpListButtonStates()

    def UpdateUserHelpChangedItems(self):
        "Clear and rebuild the HelpFiles section in self.changedItems"
        self.changedItems['main']['HelpFiles'] = {}
        for num in range(1,len(self.userHelpList)+1):
            self.AddChangedItem('main','HelpFiles',str(num),
                    string.join(self.userHelpList[num-1][:2],';'))

    def LoadFontCfg(self):
        ##base editor font selection list
        fonts=list(tkFont.families(self))
        fonts.sort()
        for font in fonts:
            self.listFontName.insert(END,font)
        configuredFont=idleConf.GetOption('main','EditorWindow','font',
                default='courier')
        lc_configuredFont = configuredFont.lower()
        self.fontName.set(lc_configuredFont)
        lc_fonts = [s.lower() for s in fonts]
        if lc_configuredFont in lc_fonts:
            currentFontIndex = lc_fonts.index(lc_configuredFont)
            self.listFontName.see(currentFontIndex)
            self.listFontName.select_set(currentFontIndex)
            self.listFontName.select_anchor(currentFontIndex)
        ##font size dropdown
        fontSize=idleConf.GetOption('main','EditorWindow','font-size',
                default='10')
        self.optMenuFontSize.SetMenu(('7','8','9','10','11','12','13','14',
                '16','18','20','22'),fontSize )
        ##fontWeight
        self.fontBold.set(idleConf.GetOption('main','EditorWindow',
                'font-bold',default=0,type='bool'))
        ##font sample
        self.SetFontSample()

    def LoadTabCfg(self):
        ##indent type radiobuttons
        spaceIndent=idleConf.GetOption('main','Indent','use-spaces',
                default=1,type='bool')
        self.indentBySpaces.set(spaceIndent)
        ##indent sizes
        spaceNum=idleConf.GetOption('main','Indent','num-spaces',
                default=4,type='int')
        #tabCols=idleConf.GetOption('main','Indent','tab-cols',
        #        default=4,type='int')
        self.spaceNum.set(spaceNum)
        #self.tabCols.set(tabCols)

    def LoadThemeCfg(self):
        ##current theme type radiobutton
        self.themeIsBuiltin.set(idleConf.GetOption('main','Theme','default',
            type='bool',default=1))
        ##currently set theme
        currentOption=idleConf.CurrentTheme()
        ##load available theme option menus
        if self.themeIsBuiltin.get(): #default theme selected
            itemList=idleConf.GetSectionList('default','highlight')
            itemList.sort()
            self.optMenuThemeBuiltin.SetMenu(itemList,currentOption)
            itemList=idleConf.GetSectionList('user','highlight')
            itemList.sort()
            if not itemList:
                self.radioThemeCustom.config(state=DISABLED)
                self.customTheme.set('- no custom themes -')
            else:
                self.optMenuThemeCustom.SetMenu(itemList,itemList[0])
        else: #user theme selected
            itemList=idleConf.GetSectionList('user','highlight')
            itemList.sort()
            self.optMenuThemeCustom.SetMenu(itemList,currentOption)
            itemList=idleConf.GetSectionList('default','highlight')
            itemList.sort()
            self.optMenuThemeBuiltin.SetMenu(itemList,itemList[0])
        self.SetThemeType()
        ##load theme element option menu
        themeNames=self.themeElements.keys()
        themeNames.sort(self.__ThemeNameIndexCompare)
        self.optMenuHighlightTarget.SetMenu(themeNames,themeNames[0])
        self.PaintThemeSample()
        self.SetHighlightTarget()

    def __ThemeNameIndexCompare(self,a,b):
        if self.themeElements[a][1]<self.themeElements[b][1]: return -1
        elif self.themeElements[a][1]==self.themeElements[b][1]: return 0
        else: return 1

    def LoadKeyCfg(self):
        ##current keys type radiobutton
        self.keysAreBuiltin.set(idleConf.GetOption('main','Keys','default',
            type='bool',default=1))
        ##currently set keys
        currentOption=idleConf.CurrentKeys()
        ##load available keyset option menus
        if self.keysAreBuiltin.get(): #default theme selected
            itemList=idleConf.GetSectionList('default','keys')
            itemList.sort()
            self.optMenuKeysBuiltin.SetMenu(itemList,currentOption)
            itemList=idleConf.GetSectionList('user','keys')
            itemList.sort()
            if not itemList:
                self.radioKeysCustom.config(state=DISABLED)
                self.customKeys.set('- no custom keys -')
            else:
                self.optMenuKeysCustom.SetMenu(itemList,itemList[0])
        else: #user key set selected
            itemList=idleConf.GetSectionList('user','keys')
            itemList.sort()
            self.optMenuKeysCustom.SetMenu(itemList,currentOption)
            itemList=idleConf.GetSectionList('default','keys')
            itemList.sort()
            self.optMenuKeysBuiltin.SetMenu(itemList,itemList[0])
        self.SetKeysType()
        ##load keyset element list
        keySetName=idleConf.CurrentKeys()
        self.LoadKeysList(keySetName)

    def LoadGeneralCfg(self):
        #startup state
        self.startupEdit.set(idleConf.GetOption('main','General',
                'editor-on-startup',default=1,type='bool'))
        #autosave state
        self.autoSave.set(idleConf.GetOption('main', 'General', 'autosave',
                                             default=0, type='bool'))
        #initial window size
        self.winWidth.set(idleConf.GetOption('main','EditorWindow','width'))
        self.winHeight.set(idleConf.GetOption('main','EditorWindow','height'))
        # default source encoding
        self.encoding.set(idleConf.GetOption('main', 'EditorWindow',
                                             'encoding', default='none'))
        # additional help sources
        self.userHelpList = idleConf.GetAllExtraHelpSourcesList()
        for helpItem in self.userHelpList:
            self.listHelp.insert(END,helpItem[0])
        self.SetHelpListButtonStates()
        #self.userHelpBrowser.set(idleConf.GetOption('main','General',
        #        'user-help-browser',default=0,type='bool'))
        #self.helpBrowser.set(idleConf.GetOption('main','General',
        #        'user-help-browser-command',default=''))
        #self.OnCheckUserHelpBrowser()

    def LoadConfigs(self):
        """
        load configuration from default and user config files and populate
        the widgets on the config dialog pages.
        """
        ### fonts / tabs page
        self.LoadFontCfg()
        self.LoadTabCfg()
        ### highlighting page
        self.LoadThemeCfg()
        ### keys page
        self.LoadKeyCfg()
        ### general page
        self.LoadGeneralCfg()

    def SaveNewKeySet(self,keySetName,keySet):
        """
        save a newly created core key set.
        keySetName - string, the name of the new key set
        keySet - dictionary containing the new key set
        """
        if not idleConf.userCfg['keys'].has_section(keySetName):
            idleConf.userCfg['keys'].add_section(keySetName)
        for event in keySet.keys():
            value=keySet[event]
            idleConf.userCfg['keys'].SetOption(keySetName,event,value)

    def SaveNewTheme(self,themeName,theme):
        """
        save a newly created theme.
        themeName - string, the name of the new theme
        theme - dictionary containing the new theme
        """
        if not idleConf.userCfg['highlight'].has_section(themeName):
            idleConf.userCfg['highlight'].add_section(themeName)
        for element in theme.keys():
            value=theme[element]
            idleConf.userCfg['highlight'].SetOption(themeName,element,value)

    def SetUserValue(self,configType,section,item,value):
        if idleConf.defaultCfg[configType].has_option(section,item):
            if idleConf.defaultCfg[configType].Get(section,item)==value:
                #the setting equals a default setting, remove it from user cfg
                return idleConf.userCfg[configType].RemoveOption(section,item)
        #if we got here set the option
        return idleConf.userCfg[configType].SetOption(section,item,value)

    def SaveAllChangedConfigs(self):
        "Save configuration changes to the user config file."
        idleConf.userCfg['main'].Save()
        for configType in self.changedItems.keys():
            cfgTypeHasChanges = False
            for section in self.changedItems[configType].keys():
                if section == 'HelpFiles':
                    #this section gets completely replaced
                    idleConf.userCfg['main'].remove_section('HelpFiles')
                    cfgTypeHasChanges = True
                for item in self.changedItems[configType][section].keys():
                    value = self.changedItems[configType][section][item]
                    if self.SetUserValue(configType,section,item,value):
                        cfgTypeHasChanges = True
            if cfgTypeHasChanges:
                idleConf.userCfg[configType].Save()
        self.ResetChangedItems() #clear the changed items dict

    def ActivateConfigChanges(self):
        #things that need to be done to make
        #applied config changes dynamic:
        #update editor/shell font and repaint
        #dynamically update indentation setttings
        #update theme and repaint
        #update keybindings and re-bind
        #update user help sources menu
        winInstances=self.parent.instanceDict.keys()
        for instance in winInstances:
            instance.ResetColorizer()
            instance.ResetFont()
            instance.ResetKeybindings()
            instance.reset_help_menu_entries()

    def Cancel(self):
        self.destroy()

    def Ok(self):
        self.Apply()
        self.destroy()

    def Apply(self):
        self.SaveAllChangedConfigs()
        self.ActivateConfigChanges()

    def Help(self):
        pass

if __name__ == '__main__':
    #test the dialog
    root=Tk()
    Button(root,text='Dialog',
            command=lambda:ConfigDialog(root,'Settings')).pack()
    root.instanceDict={}
    root.mainloop()
