"""
NoConsole.py

Simply passes all arguments. 
The easiest way of shutting down the extra consoles that plague AToM3.
"""


class NoConsole:
    """ No more annoying window popups! """
    
    def __init__(*args):
        pass
    def clearWindow(*args):
       pass
    def closeWindow(*args):
       pass
    def appendText(*args):
       pass
    def showWindow(*args):
       return -1
    def clearAllWindows(*args):
       pass
    def executeCommand(*args):
       pass
    def destroy(self):
       pass
    def getRootTK(self):
       return self