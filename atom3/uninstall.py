"""
Simple uninstall script for AToM3 options and temporary files.
By Denis Dube, Aug 2005
"""

import os
import sys
import Tkinter
from Dialog import Dialog
from tkMessageBox import showinfo, showerror


def uninstall(useDialogs=True):

  text = """Are you sure you want to "uninstall" AToM3?
  
  If you proceed all options and temporary files will be deleted.
  
  NOTE: Neither the central AToM3 installation or the user area will be affected
  """
  
  if(useDialogs):
    res = Dialog(None, {'title': "Uninstall AToM3",
                        'text': text,
                        'bitmap': 'warning',
                        'default': 1,
                        'strings': ('Uninstall','Cancel')})
                     
    if(res.num == 1): 
      sys.exit(1)
    
   
  # Platform specific USER_NAME & USER_PATH
  from __init__ import BASE_PATH
  if( sys.platform.lower().find( 'win' ) != -1 ):
    if( os.environ.has_key( 'HOMEDRIVE' ) and os.environ.has_key( 'HOMEPATH' ) ):
      USER_PATH         = os.path.join( os.environ[ 'HOMEDRIVE' ], os.environ[ 'HOMEPATH' ] )
      USER_PATH         = os.path.normpath( os.path.join( USER_PATH, 'AToM3' ) )
    else:
      USER_PATH         = os.path.normpath( os.path.join( BASE_PATH, 'User' ) )
  else:
    if( os.environ.has_key( 'HOME' ) ):
      USER_PATH         = os.path.normpath( os.path.join( os.environ['HOME'] , '.AToM3' ) )
    else:
      USER_PATH         = os.path.normpath( os.path.join( BASE_PATH, 'User' ) )
  
  
  print 'Uninstalling ', USER_PATH
  
  def DirectoryDeleter(dir, isInitialCall=True, showActivity=False):
    """ Kills a directory & everything in it & show no mercy """
    
    # Sneak attack by a non-directory!
    if(isInitialCall):
      if(not os.path.exists(dir)):
        return
      elif(not os.path.isdir(dir)):
        return os.path.remove(dir)  
    
    for f in os.listdir(dir):
      pathname = os.path.join(dir, f)
  
      # It's a directory, recurse into it
      if(os.path.isdir(pathname)):            
        DirectoryDeleter(pathname, isInitialCall = False)
        if(showActivity): print 'Deleting dir: ', pathname
        os.rmdir(pathname)
          
      # It's a file, kick it in the nutz
      elif(os.path.isfile(pathname)):            
        if(showActivity): print 'Deleting file: ', pathname
        os.remove(pathname)
          
      # It's a symbolic link, break it
      elif(os.path.islink(pathname)):            
        if(showActivity): print 'Deleting symbolic link: ', pathname
        os.remove(pathname)
          
      # Unknown file type, print a message
      else:            
        if(showActivity): print 'Skipping %s' % pathname
            
    if(isInitialCall):
      if(showActivity): print 'Deleting root dir: ', dir
      os.rmdir(dir)
  
  try:
    DirectoryDeleter(USER_PATH)
    if(useDialogs):
      showinfo("Uninstall complete", 
            "Uninstall successful\n\n"
         + "NOTE: The central and user areas of AToM3 must be manually removed")    
  except:
    showerror("Uninstall failed", 
            "Make sure no program is using a file in the option directory\n"
            + USER_PATH + "\n\n"
            + "See console for the ugly details")    
    raise


  
if __name__ == '__main__':
  tkRoot = Tkinter.Tk()
  tkRoot.withdraw()
  uninstall()
