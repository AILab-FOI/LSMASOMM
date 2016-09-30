"""
atom3.py

This script bootstraps AToM3 and displays a splash screen
while the AToM3 files are imported.

NOTE: ATOM3.py must reside in the 'Kernel' path, and __init__.py must be in 
the same directory as this script file.

Created August 11, 2004 by Denis Dube
Modified January 26, 2005 by Denis: Added minimum time delay & MSDL image
Modified Feb 16, 2005 by Denis: Added uncaught exception handling
Modified Jan 25, 2006 by Denis: Added command-line help and model load support
"""

import os, sys, Tkinter, time
timeElapsed = time.time()

if(len(sys.argv) > 1 and sys.argv[1] == '-h'):
  print '\nAToM3 command-line help:\n'
  print 'Pattern 1: No command-line options,',
  print 'loads meta-models defined in AToM3 option dialog'
  print ''
  print 'Pattern 2: Loading a specific meta-model'
  print '    ', sys.argv[0], '[meta-model name, extension _META.py]'
  print '     NOTE: Discard the _META.py, so GPSSMetaModel_META.py is just',
  print 'GPSSMetaModel'
  print '     Example:', sys.argv[0], 'GPSSMetaModel'
  print ''
  print 'Pattern 3: Loading a specific model (auto-loads meta-model/s)'
  print '    ', sys.argv[0], '[path to model, extension _MDL.py]'
  print '     NOTE: You must use the ABSOLUTE path (spaces permitted) to the',
  print '*_MDL.py model file'
  print '     Example:', sys.argv[0], \
        str(os.path.split(sys.argv[0])[0]) + \
        '\Models\GPSS\supermarket_1_GPSS_mdl.py'
  sys.exit()
  

# Get the path to the Kernel and stick in the sys.path for import goodness
from __init__ import BASE_PATH
kernelPath = os.path.normpath( os.path.join( BASE_PATH, 'Kernel' ) )
sys.path.append( kernelPath )

# Catch otherwise uncaught exceptions
import Kernel.ErrorHandlers.loadErrorHandlers # Import does all the work
from Kernel.ErrorHandlers.exceptionHookFriendlyTk import exceptionHookFriendlyTk
TkRoot = exceptionHookFriendlyTk()
TkRoot.configure( cursor='watch' )

# Make sure that Tk's double-click and next/previous word
# operations use our definition of a word (i.e. an identifier)
try:
  tk = TkRoot.tk
  tk.call('tcl_wordBreakAfter', 'a b', 0) # make sure word.tcl is loaded
  tk.call('set', 'tcl_wordchars', '[a-zA-Z0-9_]')
  tk.call('set', 'tcl_nonwordchars', '[^a-zA-Z0-9_]')
except:
  print 'ERROR: Unable to set custom double-click behaviour for text-widgets'

# People with slower computers may now stare at the splash screen :p
try:
  from __init__ import getSplashLogo           
  splashLogo = getSplashLogo()   
  TkRoot.geometry( '815x479+0+0' )
  frame = Tkinter.Frame( TkRoot, relief='raised', bg='white' )
  splashLabel = Tkinter.Label(frame, image=splashLogo, bg="white", fg="white") 
  splashLabel.pack()
  frame.pack()
except:
  TkRoot.destroy()
  print "This message should only appear if it is the first time you use AToM3"
  raise

"""
spashBackgroundColor = 'white'
splashFrame = Tkinter.Frame( TkRoot, relief='raised', bg=spashBackgroundColor )
splashLabel1 = Tkinter.Label( splashFrame, text='A T o M', 
                             fg='dark green', bg=spashBackgroundColor, 
                             font='helvetica 72' )
splashLabel2 = Tkinter.Label( splashFrame, text='A Tool for Multi-formalism and Meta-Modelling', 
                             fg='navy blue', bg=spashBackgroundColor, 
                              font='Times 28' )
splashLabel3 = Tkinter.Label( splashFrame, text='Loading ...', 
                              fg='red', bg=spashBackgroundColor, 
                              font='times 18' )
splashLabel4 = Tkinter.Label( splashFrame, text='3', 
                             fg='dark green', bg=spashBackgroundColor, 
                             font='helvetica 72' )
splashLabel5 = Tkinter.Label( splashFrame, text='http://msdl.cs.mcgill.ca/', 
                             fg='#CC0033', bg=spashBackgroundColor, 
                             font='helvetica 24' )
            
try:
  from __init__ import getImageMSDL           
  MSDL_image = getImageMSDL()   
  splashImage2 = Tkinter.Label(splashFrame, image=MSDL_image, 
                  bg="white",fg="white" )  
  splashImage2.place( relx=0.15, rely=0.05) 
except:
  TkRoot.destroy()
  print "This message should only appear if it is the first time you use AToM3"
  sys.exit()

 
splashLabel5.place( relx=0.45, rely=0.05)                                   
splashLabel1.place( relx=0.28, rely=0.3 )
splashLabel4.place( relx=0.74, rely=0.24 )
splashLabel2.place( relx=0.05, rely=0.6 )
splashLabel3.place( relx=0.45, rely=0.8 )
splashFrame.pack(side='top', fill='both', expand=1)
"""

# No, you may not kill the TkRoot prematurely :p
def handler(): 
  pass
TkRoot.protocol("WM_DELETE_WINDOW", handler )

#TkRoot.geometry( '800x600+0+0' )
TkRoot.title("Loading AToM3")
TkRoot.update() # Draw on the screen

print '\nStarting AToM3, for command-line option help:'
print sys.argv[0], '-h\n\n'

import ATOM3 # Import the juggernaught known as ATOM3

try:
  import UserPathScript # Will work only if AToM3 is installed (configured)
except:
  print 'Please restart AToM3: Installation complete'
  TkRoot.destroy()
  sys.exit()


minDelay = 2 # Display splash screen for at least this many seconds
delayTime = timeElapsed - time.time() + minDelay
if( delayTime > 0 ):
  time.sleep( delayTime )

# if(True) then splash shows and app terminates
if( False ):
  TkRoot.destroy()
  sys.exit()


# Kill the splashed entities on the canvas
splashLabel.destroy()
frame.destroy()


# Start ATOM3 Kernel
if(len(sys.argv) == 1 or sys.argv[1] == '-h'):
    ATOM3.ATOM3(TkRoot, None , 1, 1).mainloop()

else:
    # Suppose we got a full path with spaces in it...
    # Sample input:
    # D:\EclipseWorkspace\atom3>atom3NoSplash.py D:\ResearchSummer2005\atom3 user area\User Models\DChart_Tests\saveLoadTest_MDL.py
    # argv[0] = 'D:\EclipseWorkspace\atom3>atom3NoSplash.py'
    # argv[1] = 'D:\ResearchSummer2005\atom3'
    # argv[2] = 'user'
    # argv[3] = 'area\User'
    # argv[4] = 'Models\DChart_Tests\saveLoadTest_MDL.py'
    argumentString = ''
    for i in range(1, len(sys.argv) - 1):
      argumentString += sys.argv[i] + ' '
    argumentString += sys.argv[-1] # The last item
      
    ATOM3.ATOM3(TkRoot, argumentString, 1, 1).mainloop()
print "\nClosing AToM3 - A Tool for Multi-formalism and Meta-Modelling\n"


  
    
