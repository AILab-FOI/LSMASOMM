"""
Cursors.py

Sets the cursor for the occasion.

Different platforms have different graphics for each icon! Worse: it is not
possible to set an explicit icon file for the cursor graphic that is multi-
platform compatible. This means that icon files must be chosen/created for
each supported platform. *BAD*


Sample Usage:
from Cursors              import setCursor, setDefaultCursor
setCursor( atom3i.parent, 'Drag Label Motion' )
setDefaultCursor( atom3i.parent )

Created August 11, 2004 by Denis Dube
"""

import sys

CURSOR_DICT = dict()

if( sys.platform == 'win32' ):
    CURSOR_DICT[ 'Default']             = 'arrow'
    CURSOR_DICT[ 'Drag Label']          = 'draft_large'
    CURSOR_DICT[ 'Drag Label Motion']   = 'xterm'
    CURSOR_DICT[ 'Postscript']          = 'iron_cross'
    CURSOR_DICT[ 'Sizing']              = 'sizing'
    CURSOR_DICT[ 'Drag']                = 'hand1'
    CURSOR_DICT[ 'Selection']           = 'fleur'
    CURSOR_DICT[ 'Arrow Editor Idle']   = 'dot'
    CURSOR_DICT[ 'Arrow Editor Active'] = 'crosshair'
    CURSOR_DICT[ 'New Arrow']           = 'tcross'
    CURSOR_DICT[ 'New Arrow No Snap']   = 'crosshair'
    CURSOR_DICT[ 'Busy']                = 'watch'
    
else:
    CURSOR_DICT[ 'Default']             = 'arrow'
    CURSOR_DICT[ 'Drag Label']          = 'plus'
    CURSOR_DICT[ 'Drag Label Motion']   = 'xterm'
    CURSOR_DICT[ 'Postscript']          = 'iron_cross'
    CURSOR_DICT[ 'Sizing']              = 'top_left_corner'
    CURSOR_DICT[ 'Drag']                = 'hand1'
    CURSOR_DICT[ 'Selection']           = 'fleur'
    CURSOR_DICT[ 'Arrow Editor Idle']   = 'dot'
    CURSOR_DICT[ 'Arrow Editor Active'] = 'crosshair'
    CURSOR_DICT[ 'New Arrow']           = 'diamond_cross'
    CURSOR_DICT[ 'New Arrow No Snap']   = 'crosshair'
    CURSOR_DICT[ 'Busy']                = 'watch'
    

def setCursor( root, contextString ):
  """ Sets the cursor by mapping a context string to an actual cursor """
  root.configure( cursor=CURSOR_DICT[ contextString ] )

def setDefaultCursor( root ):
  """ Convenience method to set default cursor, could also use setCursor """
  root.configure( cursor=CURSOR_DICT[ 'Default' ] ) 
