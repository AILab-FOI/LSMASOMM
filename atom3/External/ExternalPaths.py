"""
ExternalPaths.py

1) Source code dropped into a subdirectory of the External folder will be
automatically placed in the AToM3 import search path (code is ready to use).

2) Source code in an arbitrary location can be added to the AToM3 import search
path by adding an absolute directory path string to the EXTERNAL_PATHS list.

Ex: EXTERNAL_PATHS = [ 'M:\Python23\SVM', 'J:\Utils\LP_SOLVE' ] 

Created August 13, 2004 by Denis Dube
"""

EXTERNAL_PATHS =  []