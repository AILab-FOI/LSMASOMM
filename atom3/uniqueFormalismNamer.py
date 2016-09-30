"""
uniqueFormalismNamer.py

Use:
  AToM3 file names must be globally unique due to super-ugly importation scheme.
  This will assist you in ensuring unique names.

By Denis Dube, Oct. 2005
"""

import os
import re
import string


def reName(sourceString, stringID, doPrepend):
  if(doPrepend):
    # Get rid of existing prefix, example: UI_ClassDiagrams --> ClassDiagrams
    underScoreComponentList = sourceString.split('_')
    if(len(underScoreComponentList) > 1):
      # Assume that prefixes have length <= 4
      # So if we have ClassDiagrams_CD_MDL then keep the 'ClassDiagrams'
      if(len(underScoreComponentList[0]) > 4):
        #sourceString = string.join(underScoreComponentList, '_')
        pass
      # If we have Foo_ClassDiagrams_CD_MDL then drop the Foo 
      else:
        sourceString = string.join(underScoreComponentList[1:], '_')
        
    # Return prefixed string
    return stringID + '_' +  sourceString
  else:
    return sourceString + stringID
    


def uniqueFormalismNamer(sourceDir, stringID, prependId):
  
  # Target directory is re-named source directory
  path, fileName = os.path.split(sourceDir)
  fileName = reName(fileName, stringID, prependId)
  targetDir = os.path.join(path, fileName)
  
  if(not os.path.exists(targetDir)):
    os.mkdir(targetDir)
  
  sourceFileList = []
  oldName2NewNameDict = dict()
  
  # Re-name the graphical icon files
  for fileName in os.listdir(sourceDir):
    if(fileName[:6] == 'graph_' and fileName[-3:] == '.py'):
      renameGraphFile(fileName, sourceDir, targetDir, stringID, prependId)
    elif(fileName[-3:] == '.py'):
      sourceFileList.append(fileName)
      oldName = fileName[:-3] # Source file name without the '.py'
      oldName2NewNameDict[oldName] = reName(oldName, stringID, prependId)
      
  # Re-name the source files
  formalismNamePattern = re.compile("RootNode.name.setValue\('\w*'\)")
  for fileName in sourceFileList: 
    renameSourceFile(fileName, sourceDir, targetDir, stringID, prependId, 
                     oldName2NewNameDict, formalismNamePattern)
      
      
      
      
def renameSourceFile(fileName, sourceDir, targetDir, stringID, prependId,
                      oldName2NewNameDict, formalismNamePattern):
  #print '\nfileName, sourceDir, targetDir, stringID, prependId'
  #print fileName, sourceDir, targetDir, stringID, prependId
  
  oldName = fileName[:-3] # Get rid of  '.py'
  newName = reName(oldName, stringID, prependId)  
  newFormalismName = string.join(newName.split('_')[:2], '_')
  
  if(newName[-3:] != '.py'):    
    newName += '.py'
   
  fileIn = open(os.path.join(sourceDir, fileName), 'r')
  fileOut = open(os.path.join(targetDir, newName), 'w')
  
  
  for line in fileIn:
    for oldName, newName in oldName2NewNameDict.items():
      line = line.replace(oldName, newName)
      
      # The generator model (i.e.: class diagrams) has a formalism name that
      # must be changed too
      matchObject = formalismNamePattern.search(line)
      if(matchObject):
        index = matchObject.start() + len("RootNode.name.setValue('")
        line = line[:index] + newFormalismName + "')"
        
      
    fileOut.write(line)

  fileIn.close()
  fileOut.close()
  
  
    
def renameGraphFile(fileName, sourceDir, targetDir, stringID, prependId):
  
  oldName = fileName[6:-3] # Get rid of 'graph_' and '.py'
  newName = reName(oldName, stringID, prependId)

  newName = 'graph_' + newName
  if(newName[-3:] != '.py'):    
    newName += '.py'
  #print 'Re-naming ' + fileName + ' to: ' + newName

  fileIn = open(os.path.join(sourceDir, fileName), 'r')
  fileOut = open(os.path.join(targetDir, newName), 'w')
  
  oldGraphName = fileName.split('.')[0] # Get rid of .py
  oldGraphName = oldGraphName.split('_', 1)[1]  # Get rid of graph_
  newGraphName = newName.split('.')[0] # Get rid of .py
  newGraphName = newGraphName.split('_', 1)[1]  # Get rid of graph_

  #print '\nReplacing all instances of', oldGraphName, 'with', newGraphName
  for line in fileIn:
    #print line
    #print line.replace(oldGraphName, newGraphName)
    fileOut.write(line.replace(oldGraphName, newGraphName))

  fileIn.close()
  fileOut.close()
  
  
  
  
  
if __name__ == '__main__':
  
  # I don't want to see an ugly Tk box, so I'll make a big, black, ugly Tk box
  from Tkinter import Tk
  root = Tk()
  root.wm_title('Unique Formalism Re-name')
  root.geometry("%dx%d+0+0"%(1600,1200))
  from Tkinter import Frame
  frame = Frame(bg='black')
  frame.pack(fill='both', expand=1)
  root.update()
  
  # Inform the user
  from tkMessageBox import showinfo
  text = 'For legacy reasons, the scope of almost every file in AToM3 is global'
  text += ' as far as the import mechanism is concerned.'
  text += '\n\nThe consquence of this is that every new formalism you generate '
  text += 'using AToM3 must have unique names!'
  text += '\nThis includes unique names for each generated Entity, Relationship'
  text += ', graphical icon, etc.'
  text += '\nIn other words: Every Python source file must be unique!'
  text += '\n\nThis is where this script comes handy, it lets you re-name your'
  text += ' entire formalism in one go.'
  text += '\n\nHow it works: you specify the formalism directory, and the '
  text += 'script automatically generates a renamed directory'
  text += '\n\nWARNING: This is not guaranteed to work all the time!'
  text += '\n\nBy Denis Dube'
  showinfo('Unique Formalism Re-name', text)
  
  # Get the formalism directory
  import tkFileDialog
  try:          
    dir = tkFileDialog.askdirectory(title="Formalism directory to rename")  
  except:
    dir = tkFileDialog.askopenfilename(title="A file in the formalism to rename",
                    filetypes=[("Choose any file in formalism directory", "*")])        
    if(dir):  
      dir = os.path.split(dir)[0] 
  if(dir == '' or dir == None): 
    print 'ERROR: No directory specified', dir
    import sys
    sys.exit(1) # Cancel
    
  # Ask for string to prepend
  from tkSimpleDialog import askstring
  stringID = askstring('New formalism name prefix', 
 'Example: Given prefix UI, CD_ClassDiagram (or ClassDiagram) becomes UI_ClassDiagream\n' 
 + '\ASSUMPTIONS: The prefix has 4 chars are less and the formalism name has 5 or more chars\n'
 + 'If the assumptions are violated, the result will not be quite right') 
                       #initialvalue=os.path.split(dir)[1]) # Old formalism name
  if(stringID == '' or stringID == None):
    print 'ERROR: No string specified', stringID
    import sys
    sys.exit(1) # Cancel
      
  uniqueFormalismNamer(dir, stringID, True)
  
  
  text = 'Before you use the re-named formalism:\n\n'
  text += '1) Identify the generative model (i.e.: class diagram)\n'
  text += '2) Identify any code files (i.e.: codeGenerator.py)\n'
  text += '3) Identify all the graph_*.py visual icons\n'
  text += '4) Delete all the files of the re-named formalism that are not one of the above\n'
  text += '5) Open the generative model and re-generate the re-named formalism\n'
  text += '\nNote: the contents of this dialog are printed in the console as well'
  print text
  showinfo('Re-name complete!', text)
  
  
#  basePath = os.getcwd()
#  addID = 'XXX_'
#  uniqueFormalismNamer(os.path.join(basePath, 'classDiagramsV3'), addID, True)