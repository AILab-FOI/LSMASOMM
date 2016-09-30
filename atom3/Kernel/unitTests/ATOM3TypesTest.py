# ----------------------------------------------------------------------
# Runs all the test on class types (Python classes named ATOM3<type>.py)
# Remember: - Add test cases with show() and show()+destroy()
#           - Test of clone() and copy()
# ----------------------------------------------------------------------

files2Test = ["testBottomType", "testConnection", "testEnum", "testInteger",
              "testBottomType", "testConstraint", "testFloat", "testString",
              "testAttribute",  "testMSEnum", "testList"]

for file in files2Test:
   print " *********************************"
   print " **** Running test "+file+" ****"
   print " *********************************"
   exec "from "+file+" import *"


