"""
Simple script to remove PYC files. Can make Python distributions 
smaller and have less files improving de/compression speed.

The script works automatically, starting at the directory from 
which it is called, and recursing into all the subfolders.
"""


import os

def PythonByteCodeCleaner(  dir, isInitialCall=True, showActivity=False ):
    """ Kills PYC files without mercy """
    
    # Sneak attack by a non-directory!
    if( isInitialCall ):
      if( not os.path.exists( dir ) ):
        return
      elif( os.path.isfile( dir ) and os.path.splitext(dir)[1].lower() == '.pyc' ):
        if( showActivity ): print 'Deleting file: ', dir
        return os.path.remove( dir )  
    
    for f in os.listdir(dir):
      pathname = os.path.join( dir, f )

      # It's a directory, recurse into it
      if( os.path.isdir( pathname ) ):            
        PythonByteCodeCleaner(pathname, isInitialCall = False)
          
      # It's a file, kick it in the nutz
      elif( os.path.isfile( pathname ) and os.path.splitext(pathname)[1].lower() == '.pyc' ):            
        if( showActivity ): 
          print 'Deleting file: ', pathname
        os.remove( pathname )
          
       
if __name__ == '__main__':
        PythonByteCodeCleaner( os.getcwd() )