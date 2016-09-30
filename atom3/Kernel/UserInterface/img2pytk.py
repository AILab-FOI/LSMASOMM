#!/usr/bin/python

#img2pytk.py - imageEmbedder 1.0 - 26 Feb 01
#A cross-platform script to to create embedded base-64 Tkinter
#  PhotoImages from GIF files.
#Update at http://www.3dartist.com/WP/python/pynotes.htm#img2pytk
#Created by Bill Allen <dempy@3dartist.com>

#HOW TO USE:
#This script converts a GIF image into a base-64 text version
#  that is written out as a workbench, or test, Python script.
#The newly created script allows you to test view the Tkinter
#  PhotoImage object, and to copy/paste that object into your
#  own Python scripts.
#To embed an icon in your Python script, first create a tiny
#  GIF image in an image editor (Photoshop, etc.), then run
#  that GIF through imageEmbedder. Now you can copy the ready-
#  to-use PhotoImage code from the resulting test script
#  ("icon.gif" converts to "icon_gif.py" in the same folder).
#This program works most practically with (and has been tested
#  with only) small images, well under 1K (e.g., under 200 bytes).
#Presently Tkinter only supports GIF for base64 embedding, but
#  update the imageAllowed constant if others become available.
#The imageEmbedder img2pytk.py script is discussed at
#  http://www.3dartist.com/WP/python/pynotes.htm#img2pytk
#For more about Tkinter scripting, visit
#  http://www.3dartist.com/WP/python/pynotes.htm#tkint

#INSTALLATION:
#Place this script anywhere you like on a machine with Python
#  already installed, then either click on the script like any
#  regular program, or launch it from the OS or Python command line,
#  or from within an IDE/IDLE interactive programming environment.
#This is not a self-executing program but rather a Python script. 
#  You don't have to be a programmer to use it, but you must have
#  the Python 2.x language interpreter installed on your system.
#  Python is a free download from http://www.python.org for many
#  different platforms (Mac, Win95+, etc.), and comes with Linux
#  (Linux users may need to upgrade to 2.x).

#PLATFORM: This code should run on any machine that has Python
#  2.x installed, but has been tested only with 2.0 on Windows ME.

#HISTORY:
#2001-02-26: v1.0 - First posted.

#LICENSE: This code is free software provided as is and without
#  warranty for fitness for any purpose. Use it at your own risk.
#  This code and derivations may be used anywhere, including for
#  commercial application. If used publicly, acknowledgment
#  and a link back would be appreciated.

#WARNING about making revisions: Because this script writes out a
#new Python script, you will find below that the appearance of
#commands both inside and outside of 'quoting' can be more than
#a little disorienting in trying to keep separate which are
#active commands and which are just text for output.

### BEGIN PROGRAM ###

#--- user inits ---

imageFormat = 'gif'     #force to gif on systems not using file extensions

### touch nothing below here except to intentionally rewrite the program ###

#--- modules & constants ---

from string import lower
import Tkinter as tk
import binascii, os, tkFileDialog, tkMessageBox

__version__ = '1.0'
B2AMAXREAD = 45                        #longest line b2a_base64 will take
imageAllowed = '*.gif'                 #put spaces between formats
imageFormat = lower(imageFormat)       #  like: '*.gif *.mno *.xyz'

#--- functions ---

def base64string(inFile):
    f = open(inFile,'rb')
    s = []
    while 1:
        b = f.read(B2AMAXREAD)
        if not b:
            break
        s.append(binascii.b2a_base64(b)[0:-1])   #-1 to remove new-line char
    f.close()
    return s
    #end def base64string

def makeButton(inFile,txtList):
    cr = '\n'
    dot = inFile.find('.')
    fmt = ''
    tb = '            '                     #12 spaces = 3 Python tabs
    if dot == -1:	                    #file extension not used
        fmt = imageFormat                   #  so force
        outFile = inFile + '_' + pyf
    else:
        fmt = lower(inFile[dot+1:dot+4])    #get the file extension/format
        if imageAllowed.find(fmt) == -1:    #extension not recognized, bail out
            tkMessageBox.showerror('You probably know...',
                                   'A file of invalid or unknown\n'
                                   +'format was selected.')
            return
        outFile = inFile[0:dot] + '_'   \
                + inFile[dot+1:len(inFile)] + pyf
    f = open(outFile,'w')
    f.write('#Embedded image created from '+inFile+cr
            +'#Done with imageEmbedder 1.0 utility img2pytk.py from'+cr
            +'#  http://www.3dartist.com/WP/python/pycode.htm#img2pytk'+cr+cr)
    f.write('import Tkinter as tk'+cr+'root = tk.Tk()'+cr+cr
            +'img00 = tk.PhotoImage(')
    if fmt != '':
        f.write('format=\''+fmt+'\',')
    f.write('data='+cr+tb+' \''+txtList[0]+'\''+cr)
    for i in range(1,len(txtList)-1):
        f.write(tb+'+\''+txtList[i]+'\''+cr)
    f.write(tb+'+\''+txtList[len(txtList)-1]+'\')'+cr+cr)
    f.write('newButton = tk.Button(root,image=img00)'+cr
            +'t = str(img00.width()) + \' wide x \' + str(img00.height())'
            +' + \' high\''+cr)
    f.write('newButton.pack()'+cr
            +'tk.Label(root,text=\'The image is\\n\'+t).pack()'+cr
            +'root.mainloop()    #comment this out to run from IDLE'+cr)
    f.flush()
    f.close()
    if os.name == 'nt':
        tkMessageBox.showinfo('All done!',
                              'Click OK to finish.\n\n'
                              +'The test script at\n'+outFile
                              +'\nwill now execute.')
        try:
            os.startfile(outFile)
        except:
            pass
    else:
        tkMessageBox.showinfo('All done!','Click OK to finish,\n'
                              +'then find the PhotoImage\n'
                              +'code in the test script at\n'+outFile)
    #end def makeButton

def openFile():
    n = tkFileDialog.askopenfilename(master=root,
                   title='Select IMAGE to EMBED',
                   filetypes=[('Tk valid images',imageAllowed),
                              ('All Files','*.*')])  #a courtesy to users
    if n:
        folder, file = os.path.split(n)
        return file,folder
    else:
        return None, ''
    #end def openFile

#--- do some work ---

if os.name == 'nt':
    pyf = '.pyw'        #if in Windows, suppress MS-DOS for output script
else:
    pyf = '.py'
root = tk.Tk()
root.withdraw()
tkMessageBox.showinfo('imageEmbedder '+__version__,
                      'Click OK when ready\n'
                      +'to select a GIF image\n'
                      +'to turn into a Tkinter\n'
                      +'embedded PhotoImage.')
f,d = openFile()
if f:
    inFileNm = d + '/' + f
    tList = base64string(inFileNm)
    makeButton(inFileNm,tList)

#[end]
