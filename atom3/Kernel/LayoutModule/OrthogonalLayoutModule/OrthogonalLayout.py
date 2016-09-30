"""
OrthogonalLayout.py
  
By Denis Dube, Oct. 2005
"""

import math
import sys
from random               import randint

from OrthogonalOptionsKeys import PROMOTE_EDGE_TO_NODE


def doOrthogonalLayout(abstractGraph, optionsDict):
  """ Applies the orthogonal layout algorithm """

  # Promote directed edges to hyperedges, useful if the edge has a large drawing
  # then that drawing becomes a node, and two new directed edges are created.
  if(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Always'):
    abstractGraph.promoteDirectedEdge(True)
  elif(optionsDict[PROMOTE_EDGE_TO_NODE] == 'Smart'):
    abstractGraph.promoteDirectedEdge(False)

  nodeList = abstractGraph.getAbstractNodeList()
  
  #todo...
           