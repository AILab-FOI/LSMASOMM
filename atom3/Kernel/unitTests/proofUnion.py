from Tkinter   import *

import sys

sys.path.append("../ATOM3Types")
sys.path.append("../UserInterface")
sys.path.append("../GraphGrammar")

from ATOM3Boolean import *

root = Tk()

c = ATOM3Boolean(None, None, 1)
print "after creation"
d = c.show(root, root)
c.writeConstructor2File(sys.stdout, "  ")
d.pack()

root.mainloop()


