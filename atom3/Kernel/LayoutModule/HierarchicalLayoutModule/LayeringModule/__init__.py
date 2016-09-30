"""
LayeringModule

This module is responsible for creating a proper layering of an arbitrary
directed graph. The optimal solution (minmal height and width layering) is an
NP-complete problem.

Responsibilities:
  1) Eliminate cycles
  2) Assign each node to a layer
  3) Assign dummy nodes to layers wherever edges traverse multipler layers
  
Known layering algorithms:
  1) Longest-path heuristic, minimizes height
  2) Coffman-Graham heuristic, minimizes width given an upperbound on the width
  3) Gansner et al. ILP, minimizes dummy edges
  4) Healy et al. ILP, minimizes width and dummy edges, given upperbound on
                      both the width and the height
  5) Tarassov et al. heuristic, minimizes width and width of dummy edges
  
By Denis Dube, Sept. 2005
"""