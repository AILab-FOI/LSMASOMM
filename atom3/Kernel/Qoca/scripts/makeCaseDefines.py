'''
Silly script to generate integer definitions for both Java and Python
'''

s = """
SOLVER_SOLVE
SOLVER_RESOLVE
SOLVER_GET_CHANGED
EDIT_BEGIN
EDIT_END
EDIT_ADDVAR
EDIT_SUGGEST
FLOAT_FIXED_ADD
FLOAT_ADD
FLOAT_REMOVE
CONSTRAINT_ADD
CONSTRAINT_REMOVE
CONSTRAINT_CHANGE
SOLVER_CASS
SOLVER_EQ
SOLVER_INEQ
SOLVER_RESTART
SOLVER_GET_ALL
"""
s = s.strip()
slist = s.splitlines()
i = 0
spacing = 20
# Print out the java defines
print "    // Parsing integer to method code definitions"
for item in slist:
  print "    public final static int " + item + " "*(spacing-len(item)) + \
        " =" + " "*(3-len(str(i)))+ str(i) + ";"
  i += 1
print '\n'
 

s2 = """
EQ
LE
GE
"""
s2 = s2.strip()
list2 = s2.splitlines()
i = 0
spacing2 = 1
# Print out java defines for the term operators
print "    // Term operators definitions"
for item in list2:
  print "    public final static int " + item + " "*(spacing2-len(item)) + \
        " =" + " "*(3-len(str(i)))+ str(i) + ";"
print '\n'
        
        
# Print out the python defines
i = 0
print "    # Parsing integer to method code definitions"
for item in list:
  print "    " + item + " "*(spacing-len(item)) + \
        " =" + " "*(3-len(str(i)))+ '"' + str(i) + '"'
  i += 1

# Print out python defines for the term operators
i = 0
print "    # Parsing integer to method code definitions"
for item in list2:
  print "    " + item + " "*(spacing2-len(item)) + \
        " =" + " "*(3-len(str(i)))+ '"' + str(i) + '"'
  i += 1
print '\n'