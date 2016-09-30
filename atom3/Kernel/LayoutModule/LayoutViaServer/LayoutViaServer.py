"""
LayoutViaServer.py

Denis Dube, 2006
"""

from AToM3LayoutInterfaceModule.AbstractGraph import AbstractGraph
from LayoutClient.PipeClient import PipeClient



class LayoutType:
  """
  Allows only valid layout methods accepted by the LayoutServer
  Example usage:
    1) layoutType = LayoutType(LayoutType.CIRCLE, LayoutType.SPRING)
    2) # Export graph information to the LayoutServer
    3) layoutType.performLayout(writingMethod)
    4) # Read output from the LayoutServer
    5) # Close the LayoutServer or start again at 2 or 3
  """
  RANDOM = 'r\n' # Command for layout server to do random layout
  CIRCLE = 'c\n'
  SPRING = 's\n'
  FTA =    'f\n'
  TREE =   't 20\n'
  VALID_LAYOUT_LIST = [RANDOM, CIRCLE, SPRING, FTA, TREE]
  
  def __init__(self, layouts=list(), fixArrows=False, fixArrowsCurve=0):
    self.__layoutList = []
    if(type(layouts) != type([])):
      raise TypeError, "Invalid layout type, should be a list of types"
    for layout in layouts:
      if(layout not in self.VALID_LAYOUT_LIST):
        raise TypeError, "Invalid layout type: " + str(layout) 
      self.__layoutList.append(layout)
    
    self.fixArrows = fixArrows
    self.fixArrowsCurve = fixArrowsCurve
    
  def performLayout(self, writingMethod, edgeList=list()):
    """
    Intention in context:
      Does each layout method specified.
    Parameter:
      writingMethod: a file.write() type thing that takes a string input
      edgeList: List of abstract edges so AToM3 can fix up the edges
    """
    for layoutCmd in self.__layoutList:
      writingMethod(layoutCmd)
      
    if(self.fixArrows):
      if(self.fixArrowsCurve):
        useSplines = True
      else:
        useSplines = False
      for arrow in edgeList:
        arrow.setLinkOptimization(useSplines, self.fixArrowsCurve)
      



def layoutViaServer(atom3i, selectionList, layoutType):
  """
  Intention in context:
    Provide a simple interface for doing layout via a C++ external layout server
  Parameters:
    atom3i: ATOM3 instance
    selectionList: List of vertices/edges to do layout on (if empty, all canvas)
    layoutType: a LayoutType object, with the layout operations to perform
  """
  if(not isinstance(layoutType, LayoutType)):
    raise TypeError, "Invalid layoutType parameter, must be instance of LayoutType"
  
  p = PipeClient()
  p.connect(verbose=False)
  
  abstractGraph = AbstractGraph(atom3i, selectionList) 
  nodeList = abstractGraph.getAbstractNodeList()
  edgeList = abstractGraph.getAbstractEdgeList()

  for node in nodeList:
    x, y = node.getPos()
    w, h = node.getSize()
    #cmd = 'v ' + node.getDistinctiveName() + ' ' + str(x) + ' ' + str(y)
    cmd = 'v ' + repr(node)[-11:-1] + ' ' + str(x) + ' ' + str(y)
    cmd += ' ' + str(w) + ' ' + str(h)
    p.write(cmd + '\n')
    #print cmd
  for edge in edgeList:
    source, target = edge.getSourceTargetNodeTuple()
    #cmd = 'e ' + source.getDistinctiveName() + ' ' + target.getDistinctiveName()
    cmd = 'e ' + repr(source)[-11:-1] + ' ' + repr(target)[-11:-1]
    p.write(cmd + '\n')
    #print cmd
  
  # Do whatever layouts need doing... 
  layoutType.performLayout(p.write, edgeList)
  
  p.write('o\n')
  finalCoords = p.read()
  #print 'finalCoords', finalCoords
  
  i = 0
  coordList = finalCoords.split(';')
  for coordTuple in coordList[:-1]:  # Skip the last one, it's an empty
    name, x, y = coordTuple.split(' ')
    nodeList[i].setNewCoords((float(x), float(y)))
    #print name, x, y, nodeList[i].getDistinctiveName()
    i += 1
    
  abstractGraph.updateAToM3() # Redraw the canvas
  p.write('q\n') # Quit the layout server
  p.disconnect() # Kill the pipe
  
