"""
ImportSimMechanics.py

By Denis Dube, Sept 15 2005
"""

import re
import os
import tkFileDialog
from tkMessageBox import showerror

from DrawConnections import simpleConnection

class ImportSimMechanics:
  """
  AToM3 importer for SimMechanics models
  """

  def __init__(self):
    self.blockStatsDict = dict()
    self.blockType2Node = dict()
    self.blockName2Node = dict()
    self.edgeList = []
    self.fileName = None
    
    
  def loadImportedModel(self, atom3i):
    """
    Load a model we have already imported into memory
    That is, we create AToM3 nodes/edges using the datastructure we have 
    constructed from a *.mdl file.
    """
    self.__loadFormalism(atom3i)
    
    for nodeName, node in self.blockName2Node.items():      
      # Create the Node at x, y
      x, y, w, h = node.getPosSize()
      newEntity = atom3i.createNewgenericEntityV2(atom3i, x, y)
      node.setAToM3Node(newEntity)
      
      # Set size and name 
      obj = newEntity.graphObject_      
      obj.easyScale(w, h)      
      #valueStr = newEntity.__dict__['name'].toString()
      obj.ModifyAttribute('name', nodeName)  
      
    # Create the Edges
    for edge in self.edgeList:
      source, destination = edge.getAToM3SourceTarget()
      simpleConnection(atom3i, source, destination)
    
    
  def __loadFormalism(self, atom3i):
    """
    Make sure we have a formalism open...
    """
    if(not atom3i.ASGroot or not atom3i.ASGroot.getASGbyName('genericV2')):
      atom3i.openMetaModel(GUIModel='genericV2')
    
    
  def importModel(self, fileName=None):
    """
    Imports a SimMechanics model file. 
    """
    
    if(fileName == None):
      fileName = tkFileDialog.askopenfilename( title="Import MDL",
        filetypes=[("SimMechanics model", "*.MDL"),("All files", "*")])
      if( fileName == '' ): 
        return "User canceled"
    
    # Too cautions? Nonesense...
    if( not os.path.exists( fileName ) ): 
      print "File does not exist: " + fileName
      showerror('I/O Error', 'File does not exist\n' + fileName)
      return self.importModel()
    else:
      self.fileName = fileName
    
    # Open file, read file, close file ;-)
    f = open( fileName, 'r' )
    fileString = f.read()
    lineList = fileString.split('\n')
    f.close()
    
    lastBlockEncountered = False
    currentObject = None
    superLineCounter = 0
    statementLineCounter = 0
    inBlock = False
    inLine = False
    # For each line in the file
    for line in lineList:
      noSpaceLine = line.replace(' ', '')
      noSpaceLine = noSpaceLine.replace('\t', '')
#      print 'noSpaceLine', noSpaceLine
      #if(superLineCounter > 600):
      #  break
      
        
#===============================================================================
#      Not inside of a block statement, but found 'Block{'
#===============================================================================
      if(not inBlock and not inLine):
        if(noSpaceLine == 'Block{'):
          inBlock = True
          statementLineCounter = 0  
          
#===============================================================================
#       Not inside a line statement, but found a 'Line{'
#===============================================================================
        elif(noSpaceLine == 'Line{'):
          inLine = True
          statementLineCounter = 0 
          if(lastBlockEncountered == False):
            lastBlockEncountered = True
            self.__buildBlockName2NodeMap()
          
#===============================================================================
#      Inside of a line statement
#===============================================================================
      elif(inLine):
        # First line of a line statement will have the line type
        if(statementLineCounter == 1):
          if(noSpaceLine[:8] == 'LineType'):
            # Get the type string for the block, create a Block object
            lineType = noSpaceLine[8:]  
            currentObject = Edge(lineType, self.blockName2Node)           
          else:
            print 'ERROR: Unexpected deviation in model file format: "' \
                  + str(noSpaceLine[:8]) + '" on line ' + str(superLineCounter)
            inLine = False
            continue 
        
        # Second to last line of the line statement            
        else:
          if(noSpaceLine[:8] == 'SrcBlock'):
            currentObject.setSource(noSpaceLine[8:])
          elif(noSpaceLine[:8] == 'DstBlock'):
            currentObject.setDestination(noSpaceLine[8:])
          elif(noSpaceLine[:8] == '}'):
            inLine = False
            self.edgeList.append(currentObject)
            currentObject = None

        
#===============================================================================
#      Inside of a block statement
#===============================================================================
      elif(inBlock):
                
        # First line of a block statement will have the block type
        if(statementLineCounter == 1):
          if(noSpaceLine[:9] == 'BlockType'):
            # Get the type string for the block, create a Block object
            blockType = noSpaceLine[9:]   
            currentObject = Node(blockType)     
            
            # Key track of the different types of blocks we encounter (Debug)
            if(not self.blockStatsDict.has_key(blockType)):
              self.blockStatsDict[blockType] = 1
            else:
              self.blockStatsDict[blockType] += 1
              
          # Not a BlockType? Uh oh.
          else:
            print 'ERROR: Unexpected deviation in model file format: "' \
                  + str(noSpaceLine[:9]) + '" on line ' + str(superLineCounter)
            inBlock = False
            statementLineCounter = 0
            continue
            
        # Second to last line
        else:
          
          # Set the name
          if(noSpaceLine[:4] == 'Name'):
            currentObject.setName(noSpaceLine[4:])
            
          # Set the position
          elif(noSpaceLine[:8] == 'Position'):
            currentObject.setPosition(noSpaceLine[8:])
          
          # Leave the block statement
          elif(noSpaceLine == '}' or noSpaceLine[-1] == '{'):
            inBlock = False
            # Store the currentObject (which is a Block)
            if(currentObject):
              blockType = currentObject.getType()
              if(not self.blockType2Node.has_key(blockType)):
                self.blockType2Node[blockType] = [currentObject]
              else:
                self.blockType2Node[blockType].append(currentObject)
            currentObject = None
        
      statementLineCounter += 1
      superLineCounter += 1
    
          
    
  def getBlockStats(self):
    """
    Prints debug info
    """
    print '\n------------------- Imported model stats -----------------------\n'
    print 'Model path:', self.fileName, '\n'
    
    totalBlocks = 0
    validBlocks = 0
    for blockType in self.blockStatsDict.keys():
      print '    Found', self.blockStatsDict[blockType], 'blocks of type', 
      print blockType
      for block in self.blockType2Node[blockType]:        
        if(block.isValid()):
          #print '        ', block
          validBlocks += 1
      totalBlocks += self.blockStatsDict[blockType]
     
    validEdges = 0
    for edge in self.edgeList:
      if(edge.isValid()):
        validEdges += 1
     
    print '\nTotal number of blocks found:', totalBlocks
    print '\nTotal number of valid blocks found (have graphics attributes):', \
            validBlocks
    print '\nTotal number of edges found:', len(self.edgeList)
    print '\nTotal number of valid edges found (source & target node found):', \
            validEdges
  
  
  
  def __buildBlockName2NodeMap(self):
    """ 
    Takes the mapping of blockTypes to lists of nodes and converts it to a 
    new mapping of block names to single node instances.
    Assumes block names are always unique 
    """
    for blockType in self.blockType2Node.keys():
      for node in self.blockType2Node[blockType]:
        self.blockName2Node[node.getName()] = node
  
  
  
class Node:
  """
  Object that represents graphical attributes of a SimMechanics model block
  """
  
  def __init__(self, blockType):
    self.__blockType = blockType
    self.__name = 'None'
    self.__x = 0
    self.__y = 0
    self.__w = 0
    self.__h = 0
    self.__AToM3Node = None
    
  def setName(self, name):
    self.__name = name.strip('"')
    
  def setPosition(self, positionString):
    """ 
    Converts a SimMechanics position string to x, y coords and width, height
    """
    positionString = positionString.replace('[', '')
    positionString = positionString.replace(']', '')
    positionList = positionString.split(',')
    self.__x = int(positionList[0])
    self.__y = int(positionList[1])
    self.__w = int(positionList[2]) - self.__x
    self.__h = int(positionList[3]) - self.__y
    
  def setAToM3Node(self, node):
    self.__AToM3Node = node
    
  def getAToM3Node(self):
    return self.__AToM3Node

  def getType(self):
    return self.__blockType
    
  def getName(self):
    return self.__name
    
  def getPosSize(self):
    return (self.__x, self.__y, self.__w, self.__h)
  
  def isValid(self):
    return self.__name != 'None' and self.__x != 0 and self.__y != 0 \
                                and self.__w != 0 and self.__h != 0
                                
  def __str__(self):
    return self.__blockType + ': ' + self.__name + ' --> x=' + str(self.__x) \
          + ', y=' + str(self.__y) + ', w=' + str(self.__w) + ', h=' \
          + str(self.__h)
   
   
   
class Edge:
  """ 
  Object that represents an edge in the SimMechanics model 
  In particular, has a direct reference to a source and target Node object
  """
  def __init__(self, lineType, name2NodeMap):
    self.lineType = lineType
    self.name2NodeMap = name2NodeMap
    self.sourceBlock = None
    self.destinationBlock = None
  
  def setSource(self, source):
    self.sourceBlock = self.getNodeObject(source)
    
  def setDestination(self, destination):
    self.destinationBlock = self.getNodeObject(destination)
    
  def isValid(self):
    return self.sourceBlock != None and self.destinationBlock != None
   
  def getNodeObject(self, quotedString):
    return self.name2NodeMap[quotedString.strip('"')]
    
  def getAToM3SourceTarget(self):
    return (self.sourceBlock.getAToM3Node(), 
            self.destinationBlock.getAToM3Node())
   
if( __name__ == '__main__'):
    temp = ImportSimMechanics()
    temp.importModel('CarAssembly.mdl')
    temp.getBlockStats()
    
    
