"""
Have a directory full of graph_* files that you want to re-use in another formalism?
Then this script is for YOU.
Just place this script in said directory and run it. 
You will be prompted to enter new names for each graph file, and not only is the file
re-named, but also all internal references to the name.

NOTE: Does not destroy original graph_* files 

By Denis Dube, Summer 2005
"""
import os
#import re

basePath = os.getcwd()
print "AToM3 graph file re-namer has been set loose on " + basePath
print "Press return without typing anything if you don't want to rename a file"

for fileName in os.listdir(basePath):
  if(fileName[:6] != 'graph_'):
    continue

  filePath = os.path.join(basePath, fileName)
  newName = raw_input("\nPlease enter a new name for " + fileName + ": graph_")

  if(newName):
    newName = 'graph_' + newName
    if(newName[-3:] != '.py'):    
      newName += '.py'
    print 'Re-naming ' + fileName + ' to: ' + newName

    fileIn = open(filePath, 'r')
    fileOut = open(os.path.join(basePath, newName), 'w')
    
    oldGraphName = fileName.split('.')[0] # Get rid of .py
    oldGraphName = oldGraphName.split('_', 1)[1]  # Get rid of graph_
    newGraphName = newName.split('.')[0] # Get rid of .py
    newGraphName = newGraphName.split('_', 1)[1]  # Get rid of graph_

    print '\nReplacing all instances of', oldGraphName, 'with', newGraphName
    for line in fileIn:
      #print line
      #print line.replace(oldGraphName, newGraphName)
      fileOut.write(line.replace(oldGraphName, newGraphName))

    fileIn.close()
    fileOut.close()

