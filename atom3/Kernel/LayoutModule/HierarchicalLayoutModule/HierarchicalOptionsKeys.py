"""
HierarchicalOptionsKeys.py
"""

# Integer values corresponding to a pixel offset
MIN_HORIZONTAL_DISTANCE = 'xOffset'
MIN_VERTICAL_DISTANCE   = 'yOffset'


# String, must be one of ['BFS', 'Longest-path', 'Minimum-width']
LAYERING_ALGORITHM       = 'layerAlg'      

# Crossing minimization
MAX_NO_PROGRESS_ROUNDS   = 'maxNoProgressRounds'  # Integer
MAX_TOTAL_ROUNDS         = 'maxTotalRounds'       # Integer
# String in ['None', 'Barycenter', 'Transpose', 'Both']
CROSS_ALG_CHOICE         = 'crossAlgChoice'       
# String in ['None', 'Barycenter', 'Transpose', 'Both']
USE_RANDOM_RESTARTS      = 'randomRestartsWith'    

# Horizontal coordinate assignment
MAX_BARYCENTER_ITER      = 'baryPlaceMax'       # Integer

# Boolean, force drawing to the top left of canvas
FORCE_TOPLEFT_TO_ORIGIN = 'Origin'

# Arrow post processing
USE_SPLINES             = 'Spline optimization'   # Boolean flag
ARROW_CURVATURE         = 'Arrow curvature'       # Integer, pixels of curve

# String in ['Never', 'Smart', 'Always']
PROMOTE_EDGE_TO_NODE    = 'EdgePromotion'      

# String in ['North', 'East', 'South', 'West']
LAYOUT_DIRECTION = 'LayoutDirection' 