"""
HelpDialog.py

Purpose: 
  Make it really easy to add help documents to AToM3 
  The only thing better than a cool tool, is a cool tool people can actually use

Created March 28, 2005 by Denis Dube
"""

import Dialog, os, Tkinter

# NOTE: All help documents assumed to be inside HELP_PATH directory
#       or in the central/user Formalisms directories
from FilePaths        import HELP_PATH, USER_MMODEL_PATH, META_MODEL_PATH    
from ATOM3TypeDialog  import ATOM3TypeDialog
from ATOM3Text        import ATOM3Text

def show( helpFileNameList ):
  """ Shorter name for lazy typers... :D """
  return HelpDialog(helpFileNameList)

def HelpDialog( helpFileNameList ):
  """
  Convenience method (figures out what you want from the parameter)
  Parameter helpFileNameList:
    1. String which is the name of a help document (ie: 'sos.txt')
    2. List with one string that is name of help doc (ie: ['sos.txt'] )
    3. List with many strings that are names of help docs (ie: ['1.txt','2.txt'])
  If only one help file, it show it right away
  If many help files, it shows a dialog to choose one of them
  """
    
  # Did we recieve a fileName list?
  if( type( helpFileNameList ) == type( list() ) ):
    
    # Empty list? Get out!
    if( len( helpFileNameList ) == 0 ): return
    
    # Okay, just one fileName... just show the help text
    elif( len( helpFileNameList ) == 1 ): 
      showHelpText( helpFileNameList[0] )
      
    # Multiple fileNames... choice dialog
    else:
      showHelpSelectionDialog( helpFileNameList )
  
  # Did we recieve just one fileName string?
  elif( type( helpFileNameList ) == type( str() ) ): 
    showHelpText( helpFileNameList )
  
  
      
def showHelpText( helpFileNameString ):
  """
  Please call HelpDialog, not this method
  Looks in the help documents folder for the desired help document
  It then displays it using ATOM3 type widgets
  """
  
  path = pathFinder( helpFileNameString )
  if( type( path ) == type( [] ) ): error = True
  else: error = False
  
  NL = chr(10) # <-- newline
  NL2 = NL + NL
  
  # Try, because the path might not exist, we may not have permission, etc.
  if( not error ):
    try:
      f = open( path, "r" )
      text = f.read() +NL2
      f.close()    
      text += "#------------------------------------------------------"
      text += "-----------------------" + NL2
      text += "Help document loaded from:"+NL+ "    "+ path + NL2
      text += "Help document loader (by Denis Dube):"+NL+ "    "+ __file__
    except:
      error = True
      path = [path]
    
  # Give output anyway if error occured
  if( error ):  
    text = NL + "Help document not found:"+NL+"    " + helpFileNameString + NL2    
    text += "Help document loader (by Denis Dube):"+NL+"    " + __file__ + NL2
    text += "#------------------------------------------------------"
    text += "-----------------------" + NL2
    for triedPath in path:
      text += 'Tried path:'+NL +'  '+ triedPath + NL
      
  
  # Create a window, and spit out the text
  root = Tkinter.Tk()
  root.geometry( '1x1+0+0' )
  root.title( 'Help' )
  x = ATOM3TypeDialog( root , ATOM3Text( text, width=90, height = 32 ),
                   windowTitle = 'Help Document: "'+helpFileNameString+'"' )
  root.destroy()
  
def pathFinder( helpFileNameString ):
  """
  Given a help file name, looks for it in the central help doc repository
  If not found, searches the central formalisms, then user formalisms
  If still not found, returns a list of all the paths it tried
  """
  # Look in central help document repository
  path = os.path.join( HELP_PATH, helpFileNameString) 
  if( os.path.exists( path ) ): return path
  
  pathsTried = [ path ]
  
  # Look in the Central Formalisms
  for dir in os.listdir( META_MODEL_PATH ):
    path = os.path.join( META_MODEL_PATH, dir )
    if( not os.path.isdir( path ) ): continue
    path = os.path.join( path, helpFileNameString )
    if( os.path.exists( path ) ): return path
    pathsTried.append( path )
  
  # Look in all the User Formalisms
  for dir in os.listdir( USER_MMODEL_PATH ):
    path = os.path.join( USER_MMODEL_PATH, dir )
    if( not os.path.isdir( path ) ): continue
    path = os.path.join( path, helpFileNameString )
    if( os.path.exists( path ) ): return path
    pathsTried.append( path )
    
  # We really did try (though we failed), so return our efforts :D
  return pathsTried    
    
def showHelpSelectionDialog( helpFileNameList ):
  """
  Please call HelpDialog, not this method
  Multiple help documents? How do we choose? Dialog time!
  """
  root = None
  title = 'Help Dialog'
  text = 'Several help documents are available...'
  buttons = helpFileNameList + ['Cancel']
  default = 0
  bitmap = ''
  
  response = Dialog.Dialog(root, {'title': title, 'text': text,'bitmap': bitmap,
                      'default': default, 'strings': buttons}).num
  # User cancelled
  if( response == len( helpFileNameList ) ): return 
  # Display the help text
  showHelpText( helpFileNameList[ response ] )
  
  