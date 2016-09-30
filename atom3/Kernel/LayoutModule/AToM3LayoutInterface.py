"""
AToM3LayoutInterface.py

This file just gives an example of how to use the layout algoirthms in the 
layout module.  
   
Options Dictionary:
  Each layout algorithm uses an option dictionary to control parameters.
  AToM3 uses OptionDatabase.py and OptionDialog.py to show/save/load these 
    options. They can easily be used in other applications where Tkinter is 
    being used as a GUI, get them from atom3/kernel/UserInterface)
  Otherwise, you will need to implement an option dictionary with all the keys
  specified in the *OptionsKeys.py file of each layout package. 
  
By Denis Dube
Sept. 2005
"""


import Dialog


from HierarchicalLayoutModule.HierarchicalLayout import doHierarchicalLayout \
  as hierarchicalLayoutMethod
from HierarchicalLayoutModule.AToM3HierarchicalOptions \
  import showHierarchicalOptions
  
from CircleLayoutModule.CircleLayout import doCircleLayout \
  as circleLayoutMethod
from CircleLayoutModule.AToM3CircleOptions \
  import showCircleOptions
  
from TreeLikeLayoutModule.TreeLikeLayout import doTreeLikeLayout \
  as treeLikeLayoutMethod
from TreeLikeLayoutModule.AToM3TreeLikeOptions \
  import showTreeLikeOptions
  
from ForceTransferModule.ForceTransfer import doForceTransfer \
  as forceTransferMethod
from ForceTransferModule.AToM3FTAOptions \
  import showFTAOptions

from SpringLayoutModule.SpringLayout import doSpringLayout \
  as springElectricalMethod
from SpringLayoutModule.AToM3SpringOptions \
  import showSpringOptions 
  
from OrthogonalLayoutModule.OrthogonalLayout import doOrthogonalLayout \
  as orthogonalLayoutMethod
from OrthogonalLayoutModule.AToM3OrthogonalOptions \
  import showOrthogonalOptions 

  

from AToM3LayoutInterfaceModule.AbstractGraph import AbstractGraph
  
  
def getParent(selectionList):
  """
  Finds the hierarchical parent within a selectionList of graphical objects
  """
  parentDict = dict()
  for obj in selectionList:
    parentDict[obj.semanticObject.getHierParent()] = obj
  for obj in selectionList:
    if(parentDict.has_key(obj.semanticObject)):
      del parentDict[obj.semanticObject]
  if(parentDict.has_key(None)):
    del parentDict[None]
    
  if(len(parentDict) == 0):
    topLayerList = selectionList[0].semanticObject.getHierTopLayer()
    for obj in selectionList:
      if(obj.semanticObject in topLayerList):
        return obj
    return None
  return parentDict.values()[0]
  
  

def hierarchicalFilter(selectionList):
  """
  Prunes the selection list to include only the top level graphical objects
  within a hierarchical selection. This means the internal nodes of a 
  hierarchical object will NOT be selected, however these nodes will get
  moved if the hierarchical object is moved by the layout engine. 
  """
  if(len(selectionList) == 0):
    return []
  
  parentObj = getParent(selectionList)
  if(not parentObj):
    return selectionList
    
  newSelection = []
  for semObj in parentObj.semanticObject.getHierChildren():
    newSelection.append(semObj.graphObject_)
    for outLink in semObj.out_connections_:
      if(outLink.isGraphObjectVisual):
        newSelection.append(outLink.graphObject_)
  return newSelection



def doChosenLayout(atom3i, selectionList, optionsDict=None):
  """
  Shows a menu of all the layout algorithms
  """
  selectionList = hierarchicalFilter(selectionList)
 

#  stringList = ['Hierarchical', 'Circle', 'Tree-like', 'FTA', 'Spring', 
#                'Orthogonal', 'Cancel']
  stringList = ['Hierarchical', 'Circle', 'Tree-like', 'FTA', 'Spring', 
                'Dump options to console', 'Circle C++', 'Spring C++', 
                'FTA C++', 'Tree C++', 'Cancel']
  d = Dialog.Dialog(atom3i.parent, {'title': 'Automatic Layout', 
                           'text': 'Choose layout algorithm', 
                           'bitmap': '',
                           'default': 0, 
                           'strings': stringList})
  if(d.num == 0):
    doHierarchicalLayout(atom3i, selectionList, optionsDict)
  elif(d.num == 1):
    doCircleLayout(atom3i, selectionList, optionsDict)
  elif(d.num == 2):
    doTreeLikeLayout(atom3i, selectionList, optionsDict) 
  elif(d.num == 3):
    doForceTransfer(atom3i, selectionList, optionsDict) 
  elif(d.num == 4):
    doSpringLayout(atom3i, selectionList, optionsDict) 
  elif(d.num == 5):
    print '\n\n'
    from HierarchicalLayoutModule import AToM3HierarchicalOptions 
    AToM3HierarchicalOptions.dumpOptions2Console(atom3i)
    print '\n'
    from CircleLayoutModule import AToM3CircleOptions 
    AToM3CircleOptions.dumpOptions2Console(atom3i)
    print '\n'
    from SpringLayoutModule import AToM3SpringOptions 
    AToM3SpringOptions.dumpOptions2Console(atom3i)
    print '\n'
    from TreeLikeLayoutModule import AToM3TreeLikeOptions 
    AToM3TreeLikeOptions.dumpOptions2Console(atom3i)
    print '\n'
    from ForceTransferModule import AToM3FTAOptions 
    AToM3FTAOptions.dumpOptions2Console(atom3i)
  elif(d.num == 6):
    from LayoutViaServer.LayoutViaServer import LayoutType, layoutViaServer
    layoutType = LayoutType([LayoutType.CIRCLE], True, 10)
    layoutViaServer(atom3i, selectionList, layoutType)
  elif(d.num == 7):
    from LayoutViaServer.LayoutViaServer import LayoutType, layoutViaServer
    layoutType = LayoutType([LayoutType.SPRING], True, 10)
    layoutViaServer(atom3i, selectionList, layoutType)
  elif(d.num == 8):
    from LayoutViaServer.LayoutViaServer import LayoutType, layoutViaServer
    layoutType = LayoutType([LayoutType.FTA], True, 10)
    layoutViaServer(atom3i, selectionList, layoutType)
  elif(d.num == 9):
    from LayoutViaServer.LayoutViaServer import LayoutType, layoutViaServer
    layoutType = LayoutType([LayoutType.TREE], True, 10)
    layoutViaServer(atom3i, selectionList, layoutType)
  #doOrthogonalLayout(atom3i, selectionList, optionsDict)
    
    

def doHierarchicalLayout(atom3i, selectionList, optionsDict=None):
  """
  Apply the hierarchical layout algorithm, treats graph as a layered drawing
  """
  if(optionsDict == None):
    optionsDict = showHierarchicalOptions(atom3i)
    # User-canceled the show dialog
    if(optionsDict == None):
      return 
      
  abstractGraph = AbstractGraph(atom3i, selectionList) 
  hierarchicalLayoutMethod(abstractGraph, optionsDict)
  
  abstractGraph.updateAToM3()
  
  
  
def doCircleLayout(atom3i, selectionList, optionsDict=None):
  """
  Simple circle layout, looks like a spoked wheel
  """
  if(optionsDict == None):
    optionsDict = showCircleOptions(atom3i)
    # User-canceled the show dialog
    if(optionsDict == None):
      return 
      
  abstractGraph = AbstractGraph(atom3i, selectionList) 
  circleLayoutMethod(abstractGraph, optionsDict)
  
  abstractGraph.updateAToM3()
  
  
  
def doTreeLikeLayout(atom3i, selectionList, optionsDict=None):
  """
  Simple tree-like layout, works best on actual trees
  """
  if(optionsDict == None):
    optionsDict = showTreeLikeOptions(atom3i)
    # User-canceled the show dialog
    if(optionsDict == None):
      return 

  abstractGraph = AbstractGraph(atom3i, selectionList) 
  treeLikeLayoutMethod(abstractGraph, optionsDict)
  
  abstractGraph.updateAToM3()


  
def doForceTransfer(atom3i, selectionList, optionsDict=None):
  """
  Simple tree-like layout, works best on actual trees
  """
  if(optionsDict == None):
    optionsDict = showFTAOptions(atom3i)
    # User-canceled the show dialog
    if(optionsDict == None):
      return 
  
  abstractGraph = AbstractGraph(atom3i, selectionList) 
  forceTransferMethod(abstractGraph, optionsDict)
  
  abstractGraph.updateAToM3()



def doSpringLayout(atom3i, selectionList, optionsDict=None):
  """
  Spring-electrical layout
  """
  if(optionsDict == None):
    optionsDict = showSpringOptions(atom3i)
    # User-canceled the show dialog
    if(optionsDict == None):
      return 
  
  abstractGraph = AbstractGraph(atom3i, selectionList) 
  springElectricalMethod(abstractGraph, optionsDict)
  
  abstractGraph.updateAToM3()
  
  
  
def doOrthogonalLayout(atom3i, selectionList, optionsDict=None):
  """
  Orthogonal layout
  """
  if(optionsDict == None):
    optionsDict = showOrthogonalOptions(atom3i)
    # User-canceled the show dialog
    if(optionsDict == None):
      return 
  
  abstractGraph = AbstractGraph(atom3i, selectionList) 
  orthogonalLayoutMethod(abstractGraph, optionsDict)
  
  abstractGraph.updateAToM3()
  
  
  
  
def customTraceback():
  """
  Intention in context:
    Use this for debugging to find out exactly how you got into a certain line
    of code. It will print out the sequence of prior method calls.
  
  WARNING: This method does **NOT** belong here. Denis just found the basis for 
           it on the internet by chance and didn't want to lose it...
  """
  import inspect
  print 'Custom traceback'
  frames = inspect.getouterframes(inspect.currentframe())
  for i in range(len(frames) - 1, 0, -1):
    frame = frames[i]
    print 'File:', frame[1], 'Method:', frame[3]
    print 'Line ' + str(frame[2]) + ':' + frame[4][0]  

