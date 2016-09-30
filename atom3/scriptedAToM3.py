"""
scriptedAToM3.py

Template that shows how you can control AToM3 from a script and make it load
models, run graph grammars, etc. 
You have full power over the entire API (see ATOM3.py in Kernel for API)
Great for doing automatic batch runs! 

NOTE: The good stuff is at the bottom of the file!

Denis Dube, 2006
"""
import os, sys, Tkinter, time
timeElapsed = time.time()


# Get the path to the Kernel and stick in the sys.path for import goodness
from __init__ import BASE_PATH
kernelPath = os.path.normpath( os.path.join( BASE_PATH, 'Kernel' ) )
sys.path.append( kernelPath )

# Catch otherwise uncaught exceptions
import Kernel.ErrorHandlers.loadErrorHandlers
from Kernel.ErrorHandlers.exceptionHookFriendlyTk import exceptionHookFriendlyTk
TkRoot = exceptionHookFriendlyTk()
TkRoot.configure( cursor='watch' )

# Make sure that Tk's double-click and next/previous word
# operations use our definition of a word (i.e. an identifier)
try:
  tk = TkRoot.tk
  tk.call('tcl_wordBreakAfter', 'a b', 0) # make sure word.tcl is loaded
  tk.call('set', 'tcl_wordchars', '[a-zA-Z0-9_]')
  tk.call('set', 'tcl_nonwordchars', '[^a-zA-Z0-9_]')
except:
  print 'ERROR: Unable to set custom double-click behaviour for text-widgets'

# No, you may not kill the TkRoot prematurely :p
def handler(): pass
TkRoot.protocol("WM_DELETE_WINDOW", handler )

TkRoot.geometry( '800x600+0+0' )
TkRoot.title("Loading AToM3")
TkRoot.update() # Draw on the screen


print '\nStarting AToM3, for command-line option help:'
print sys.argv[0], '-h\n\n'
  
try:
  import ATOM3 # Import the juggernaught known as ATOM3
except:
  print "This message should only appear if you are using AToM3 for the first time"
  TkRoot.destroy()
  raise
  

def sysPathHacker(fileName):
  """
  Makes sure the given filename, if it is in User Formalisms or User Models
  is in the sys.path so that it can be imported
  Assumes fileName does not include the .py extension
  """
  import sys, os
  from FilePaths           import USER_MMODEL_PATH, USER_MODEL_PATH
  
  newPath = None
  
  allFormalismDirs = os.listdir(USER_MMODEL_PATH)
  for formalismDir in allFormalismDirs:
    fullFormalismDir = os.path.join(USER_MMODEL_PATH, formalismDir)
    try:
      allFormalismFiles = os.listdir(fullFormalismDir)
    except:
      pass
    for file in allFormalismFiles:
      if(file[:-3] == fileName):
        sys.path.append(fullFormalismDir)
        newPath = fullFormalismDir
        
  allModelDirs = os.listdir(USER_MODEL_PATH)
  for modelDir in allModelDirs:
    fullModelDir = os.path.join(USER_MODEL_PATH, modelDir)
    try:
      allModelFiles = os.listdir(fullModelDir)
    except:
      pass
    for file in allModelFiles:
      if(file[:-3] == fileName):
        sys.path.append(fullModelDir)
        newPath = fullModelDir
  
  return os.path.join(newPath, fileName) + '.py'


# Start ATOM3 Kernel, atom3i is an AToM3 instance
atom3i = ATOM3.ATOM3(TkRoot, None , 1, 1)


#===============================================================================
#                              Template starts here
#===============================================================================

#===============================================================================
#  Open a formalism by name. 
#  Formalism must be in either Central or User formalism directories! 
#  Older formalisms may have file names like GenericGraph.py, so you enter
#     the formalism name as GenericGraph. Newer formalisms, will be named like
#     ClassDiagramsV3_META.py and you enter ClassDiagramsV3_META.
#===============================================================================
if(False):
  #atom3i.openMetaModel(GUIModel='BondGraph_META')
  #atom3i.openMetaModel(GUIModel='CausalBlockDiagram_META')
  atom3i.openMetaModel(GUIModel='RWM_META')
  atom3i.openMetaModel(GUIModel='IPM_META')

#===============================================================================
#  Open a model name. Must be in User Models or User Formalisms. Will not work
#  properly if more than model by that name exists! For more flexibility, either
#  give an absolute path to the model or modify sysPathHacker()
#===============================================================================
if(False):
  modelFileName = 'Hositing_Device_RWM_MDL'
  modelFileName = sysPathHacker(modelFileName)
  atom3i.open(fileName=modelFileName)
  #atom3i.open(fileName='D:\\ResearchSummer2005\\atom3 user area\\User Models\\Sagar\\Hositing_Device_RWM_MDL.py')

#===============================================================================
#  Execute a graph grammar. It *MUST* be in User Models or User Formalisms.
#  Alternatively, you can change the sysPathHacker() to find it elsewhere.
#===============================================================================
if(False):
  graphGrammarFileName = 'RWM_2_IPM_GG_exec' # don't put the .py
  
  from GraphRewritingSys import GraphRewritingSys
  sysPathHacker(graphGrammarFileName)
  exec "from "+graphGrammarFileName+" import " + graphGrammarFileName  
  
  # get the graph grammar to execute from the options...          
  atom3i.GraphGrammars = [ eval(graphGrammarFileName+"(atom3i)") ]                  
  # get the graph grammar to execute from the options... 
  atom3i.grs = GraphRewritingSys(atom3i, atom3i.GraphGrammars, atom3i.ASGroot )
  atom3i.grs.evaluate(stepByStep = 0, moveEntities = 0, 
                   execute = atom3i.grs.SEQ_RANDOM, graphics = 0)  
           
#===============================================================================
# Generate postscript automatically
#===============================================================================
if(False):
  print 'modelFileName', os.path.splitext(modelFileName)[0] + '.ps'
  postscriptFilePath = os.path.splitext(modelFileName)[0] + '.ps'
  atom3i.postscriptBox.generatePostscript(autoSaveToFileName=postscriptFilePath)      
          
#===============================================================================
#  Save model
#===============================================================================
if(False):
  modelFileName = os.path.splitext(modelFileName)[0] + '_addedByScript'
  atom3i.save(fileName=modelFileName)
          
#===============================================================================
#  Quit AToM3 (or not, you may want to keep working...)
#===============================================================================
exitAToM3Now = False
          
#===============================================================================
#                                Template ends here
#===============================================================================


  
#===============================================================================
#  Script example: Converting reachability graph to genericV2
#  This just goes to show you that Graph Grammars ARE easier for this stuff :)
#===============================================================================
if(False):
  modelFileName = '' # Full path to a model in formalism ReachGraph
  atom3i.open(fileName=modelFileName)
  atom3i.openMetaModel(GUIModel='genericV2_META')
  #print atom3i.ASGroot.listNodes.keys()
  
  # Create a generic entity for each ReachGraph entity
  # The createNewgenericEntityV2() method is found in genericV2_MM.py
  reach2genericMap = dict()
  for rNode in atom3i.ASGroot.listNodes['RGnode']:
    obj = rNode.graphObject_
    reach2genericMap[rNode] = \
                    atom3i.createNewgenericEntityV2(atom3i, obj.x, obj.y, False)
    
  # Create a generic arrow for each ReachGraph arrow between generic entities
  from DrawConnections import simpleConnection
  for rGtrans in atom3i.ASGroot.listNodes['RGtrans']:
    simpleConnection(atom3i, reach2genericMap[rGtrans.in_connections_[0]],
                             reach2genericMap[rGtrans.out_connections_[0]])
    
  # Delete all the ReachGraph entities/arrows.
  # Since the delete mechanism seems to have difficulty, loop until it works...
  while(len(atom3i.ASGroot.listNodes['RGnode']) > 1):
    for rNode in atom3i.ASGroot.listNodes['RGnode']:
      atom3i.deleteRealEntity(rNode.graphObject_.tag, rNode.graphObject_)
  while(len(atom3i.ASGroot.listNodes['RGtrans']) > 1):
    for rGtrans in atom3i.ASGroot.listNodes['RGtrans']:
      atom3i.deleteRealEntity(rGtrans.graphObject_.tag, rGtrans.graphObject_)
#===============================================================================
#  End script example
#===============================================================================


#===============================================================================
#  Random graph (model) generation example
#===============================================================================
def applyHierachical(atom3i, abstractGraph):
  # Hierarchical Layout Options
  optionsDict = dict()
  optionsDict['Origin'] = True
  optionsDict['EdgePromotion'] = 'Never' # ['Never', 'Smart', 'Always']
  optionsDict['randomRestartsWith'] = 'None' # ['None', 'Barycenter', 'Transpose', 'Both']
  optionsDict['maxNoProgressRounds'] = 10
  optionsDict['yOffset'] = -28
  optionsDict['LayoutDirection'] = 'East' # ['North', 'East', 'South', 'West']
  optionsDict['baryPlaceMax'] = 100
  optionsDict['Spline optimization'] = True
  optionsDict['crossAlgChoice'] = 'Barycenter' # ['None', 'Barycenter', 'Transpose', 'Both']
  optionsDict['layerAlg'] = 'BFS' # ['BFS', 'Longest-path', 'Minimum-width']
  optionsDict['Arrow curvature'] = 10
  optionsDict['xOffset'] = 20
  optionsDict['maxTotalRounds'] = 3
      
  from HierarchicalLayoutModule.HierarchicalLayout import doHierarchicalLayout
  
  timeElapsed = time.time()
  doHierarchicalLayout(abstractGraph, optionsDict)    
  #abstractGraph.updateAToM3()
  timeElapsed = time.time() - timeElapsed
  return timeElapsed
    
def applySpring(atom3i, abstractGraph):
  # Spring Layout Options
  optionsDict = dict()
  optionsDict['Origin'] = True
  optionsDict['Random amount'] = 0
  optionsDict['Maximum iterations'] = 100
  optionsDict['Forgiveness rounds'] = 2
  optionsDict['Minimum force'] = 10.0
  optionsDict['Arrow curvature'] = 10
  optionsDict['Spring rest length'] = 100
  optionsDict['EdgePromotion'] = 'Never' # ['Never', 'Smart', 'Always']
  optionsDict['Gravity strength'] = 10
  optionsDict['Charge strength'] = 10.0
  optionsDict['Charge threshold'] = 300
  optionsDict['Spring constant'] = 0.1
  optionsDict['Spline optimization'] = True
    
  from SpringLayoutModule.SpringLayout import doSpringLayout
  
  timeElapsed = time.time()
  doSpringLayout(abstractGraph, optionsDict)    
  #abstractGraph.updateAToM3()
  timeElapsed = time.time() - timeElapsed
  return timeElapsed
  

def applyTreeLike(atom3i, abstractGraph):
  # Tree-like Layout Options
  optionsDict = dict()
  optionsDict['Origin'] = True
  optionsDict['Manual Cycles'] = False
  optionsDict['yOffset'] = 70
  optionsDict['Spline optimization'] = True
  optionsDict['EdgePromotion'] = 'Never' # ['Never', 'Smart', 'Always']
  optionsDict['Arrow curvature'] = 10
  optionsDict['xOffset'] = 20
    
  from TreeLikeLayoutModule.TreeLikeLayout import doTreeLikeLayout
  
  timeElapsed = time.time()
  doTreeLikeLayout(abstractGraph, optionsDict)    
  #abstractGraph.updateAToM3()
  timeElapsed = time.time() - timeElapsed
  return timeElapsed
  
def applyFTA(atom3i, abstractGraph):
  # Force-Transfer Layout Options
  optionsDict = dict()
  optionsDict['EdgePromotion'] = 'Never' # ['Never', 'Smart', 'Always']
  optionsDict['Minimum link distance'] = 0
  optionsDict['Minimum node distance'] = 1
  optionsDict['Max Total Iterations'] = 100
  optionsDict['Seperation Force'] = 0.2
  optionsDict['Arrow curvature'] = 10
  optionsDict['Border Distance'] = 0
  optionsDict['Spline optimization'] = True
    
  from ForceTransferModule.ForceTransfer import doForceTransfer
  
  timeElapsed = time.time()
  doForceTransfer(abstractGraph, optionsDict)    
  #abstractGraph.updateAToM3()
  timeElapsed = time.time() - timeElapsed
  return timeElapsed
  
  
def applyCircle(atom3i, abstractGraph):
  # Circle Layout Options
  optionsDict = dict()
  optionsDict['Origin'] = True
  optionsDict['Spline optimization'] = True
  optionsDict['Offset'] = -20
  optionsDict['EdgePromotion'] = 'Never' # ['Never', 'Smart', 'Always']
  optionsDict['Arrow curvature'] = 10
    
  from CircleLayoutModule.CircleLayout import doCircleLayout
  
  timeElapsed = time.time()
  doCircleLayout(abstractGraph, optionsDict)    
  #abstractGraph.updateAToM3()
  timeElapsed = time.time() - timeElapsed
  return timeElapsed


def randomGraphGenerator(atom3i, verticesInt, edgesInt):
  """
  Creates a random graph with verticesInt vertices, and edgesInt edges.
  If edgesInt > verticesInt, the first verticesInt - 1 edges are used to make
  the graph connected. All other edges are added completely randomly, and the 
  source and target of an edge may be the same. 
  """
  # Clean the canvas first
  atom3i.clearModel(showDialog=False)
  
  # Create verticesInt vertices in a line... \
  vertexList = []
  j = 0
  for i in range(0, verticesInt):
    j += i + 5
    vertexList.append(atom3i.createNewgenericEntityV2(atom3i, j, j, False))
  
  # Create edges now... but make sure its a connected graph (if possible)
  if(edgesInt > verticesInt):
    edgesInt -= verticesInt - 1
    for i in range(0, verticesInt - 1):
      simpleConnection(atom3i, vertexList[i], vertexList[i+1])
      
  # Add in remaining edges randomly
  for i in range(0, edgesInt):
    simpleConnection(atom3i, choice(vertexList), choice(vertexList))
  
  # Build an abstract graph representation and return it  
  objList = []
  for entity in atom3i.ASGroot.listNodes['genericEntityV2']:
    objList.append(entity.graphObject_)
  for entity in atom3i.ASGroot.listNodes['genericLinkV2']:
    objList.append(entity.graphObject_)
  return AbstractGraph(atom3i, objList) 
  
    
if(False):
  atom3i.openMetaModel(GUIModel='genericV2_META')
  from AToM3LayoutInterfaceModule.AbstractGraph import AbstractGraph
  from random import choice
  from DrawConnections import simpleConnection
  
  maxTrials = 1
  #graphSizeList = [50, 100, 150, 200, 250, 300, 350, 400, 450, 500]
  graphSizeList = [50, 100, 150, 200, 250, 300, 350, 400]
  #graphSizeList = [300]
  # 
  # 
  #layoutNameMethodList = [('Hierarchical', applyHierachical)]
  #layoutNameMethodList = [('Force-Transfer', applyFTA),
  #  ('Circle', applyCircle), ('Spring', applySpring),
  #  ('Tree-like', applyTreeLike), ('Hierarchical', applyHierachical)  ]
  layoutNameMethodList = [('Force-Transfer', applyFTA)]
  
  # Force a time-limit, if alg takes longer just cut-it off
  maxTimeInSec = 600
  name2isOkayDict = dict()
  for layName, layMethod in layoutNameMethodList:
    name2isOkayDict[layName] = True
  
  size2resultsDict = dict()
  for graphSize in graphSizeList:
    size2resultsDict[graphSize] = dict()
    
    for trialNumber in range(0, maxTrials):
      size2resultsDict[graphSize][trialNumber] = dict()
      abstractGraph = randomGraphGenerator(atom3i, graphSize, int(graphSize * 1.5))
      print 'Random graph generated of size: ', graphSize
      
      for layName, layMethod in layoutNameMethodList:
        # This algorithm is exceeding the time limit, continue...
        if(not name2isOkayDict[layName]):
          size2resultsDict[graphSize][trialNumber][layName] = maxTimeInSec
          continue
          
        elapsedTime = layMethod(atom3i, abstractGraph)
        
        # Took too long! Assume it just gets worse...
        if(elapsedTime > maxTimeInSec):
          name2isOkayDict[layName] = False
          size2resultsDict[graphSize][trialNumber][layName] = maxTimeInSec
        
        # Store the actual elapsed time
        size2resultsDict[graphSize][trialNumber][layName] = elapsedTime
        
    
  # Printout Results
  name2sizeTimeTupleDict = dict()  
  for layName, layMethod in layoutNameMethodList:
      name2sizeTimeTupleDict[layName] = []
  
  for graphSize in graphSizeList:
    print '\nGraph size:', graphSize, '(|V|=' + str(graphSize) + ', |E|=' \
          + str(int(graphSize * 1.5)) + ')'
    
    # Init a mapping from layout name to a list of times in each trial
    layName2timeListDict = dict()
    for layName, layMethod in layoutNameMethodList:
      layName2timeListDict[layName] = []
        
    for trialNumber in range(0, maxTrials):
      print '    ', 'Trial:', trialNumber
      
      for layName, layMethod in layoutNameMethodList:
        timeTaken = size2resultsDict[graphSize][trialNumber][layName]
        print '        ', layName, ':',  timeTaken
        layName2timeListDict[layName].append(timeTaken)
        
    # Show median time for each layout method at that graph size
    for layName in layName2timeListDict.keys():
      timeList = layName2timeListDict[layName]
      timeList.sort()
      
      medianTime = timeList[len(timeList) / 2] 
      name2sizeTimeTupleDict[layName].append((graphSize, medianTime))
      print '    ', 'Median time for', layName, 'is:', medianTime

  # Write result to file
  fileOut = open('layoutTimeMarathon.txt', 'w')
  for layName in name2sizeTimeTupleDict.keys():
    print '***', layName, '***'
    print 'Graph size:'
    fileOut.write('\n\n*** ' + layName + ' ***\n')
    fileOut.write('Graph size:\n')
    for graphSize, medianTime in name2sizeTimeTupleDict[layName]:
       print graphSize
       fileOut.write(str(graphSize) + '\n')
    print 'Median time:'
    fileOut.write('Median time:\n')
    for graphSize, medianTime in name2sizeTimeTupleDict[layName]:
       print medianTime
       fileOut.write(str(medianTime) + '\n')
  fileOut.close()
  exitAToM3Now = True
  
#===============================================================================
#  END: Random graph (model) generation example
#===============================================================================


if(exitAToM3Now):
  atom3i.exitFromATOM3(noDialog=True)
else:
  atom3i.mainloop() 
print "\nClosing AToM3 - A Tool for Multi-formalism and Meta-Modelling\n"
print 'AToM3 ran for', time.time() - timeElapsed, 'seconds'






"""
if(True):
  file = 'D:\\ResearchSummer2005\\atom3 user area\\User Models\\DigitalWatch\\problem\\FINALmerge_MDL.py'
  atom3i.open(fileName=file)
  atom3i.openMetaModel(GUIModel='DChartsV3_META')
  from DrawConnections import simpleConnection
  
#===============================================================================
#  Create/copy nodes
#===============================================================================
  DC_DChart = atom3i.createNewDC_DChart(atom3i, 0, 0, False)
  
  old2newMap = dict()
  for node in atom3i.ASGroot.listNodes['Composite']:
    obj = node.graphObject_
    old2newMap[node] = \
                    atom3i.createNewDC_Composite(atom3i, obj.x, obj.y, False)
    
  for node in atom3i.ASGroot.listNodes['Basic']:
    obj = node.graphObject_
    old2newMap[node] = \
                    atom3i.createNewDC_Basic(atom3i, obj.x, obj.y, False)
  
  for node in atom3i.ASGroot.listNodes['Orthogonal']:
    obj = node.graphObject_
    old2newMap[node] = \
                    atom3i.createNewDC_Orthogonal(atom3i, obj.x, obj.y, False)
  
#===============================================================================
#  Copy edges
#===============================================================================
  print 'orthogonality'
  for relation in atom3i.ASGroot.listNodes['orthogonality']:
    simpleConnection(atom3i, old2newMap[relation.in_connections_[0]],
                             old2newMap[relation.out_connections_[0]],
      filterLinkTypeList=['DC_Hyperedge', 'DC_DChartContains', 'DC_Contains'])
      
  print 'contains'
  for relation in atom3i.ASGroot.listNodes['contains']:
    simpleConnection(atom3i, old2newMap[relation.in_connections_[0]],
                             old2newMap[relation.out_connections_[0]],
    filterLinkTypeList=['DC_Hyperedge', 'DC_DChartContains', 'DC_Orthogonality'])                 
    
  print 'Hyperedge'
  for relation in atom3i.ASGroot.listNodes['Hyperedge']:
    simpleConnection(atom3i, old2newMap[relation.in_connections_[0]],
                             old2newMap[relation.out_connections_[0]],
    filterLinkTypeList=['DC_Contains', 'DC_DChartContains', 'DC_Orthogonality'])                 
    
  print 'DC_DChart'
#===============================================================================
#  Link up the DC_DChart
#===============================================================================
  containmentList = ['DC_Contains', 'DC_DChartContains', 'DC_Orthogonality']
  nodeList = atom3i.ASGroot.listNodes['DC_Composite'] \
    + atom3i.ASGroot.listNodes['DC_Basic'] #\
    #+ atom3i.ASGroot.listNodes['DC_Orthogonal']
    
  for node in nodeList:
    needsParent = True
    for relation in node.in_connections_:
      if(relation.__class__.__name__ in containmentList):
        needsParent = False
        break
    if(needsParent):      
      print 'Connecting', DC_DChart.name.toString(), 'to', node.name.toString()
      simpleConnection(atom3i, DC_DChart, node,
        filterLinkTypeList=['DC_Hyperedge', 'DC_Contains', 'DC_Orthogonality'])                 

#===============================================================================
#  Clean-up
#===============================================================================
  def cleaner(atom3i, className):
    while(len(atom3i.ASGroot.listNodes[className]) > 1):
      for node in atom3i.ASGroot.listNodes[className]:
        atom3i.deleteRealEntity(node.graphObject_.tag, node.graphObject_)
        
  cleaner(atom3i, 'visual_settings')
  cleaner(atom3i, 'Hyperedge')
  cleaner(atom3i, 'orthogonality')
  cleaner(atom3i, 'contains')
  cleaner(atom3i, 'Basic')
  cleaner(atom3i, 'Orthogonal')
  cleaner(atom3i, 'Composite')
  """
