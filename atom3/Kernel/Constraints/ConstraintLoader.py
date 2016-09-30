"""
ConstraintLoader.py

Processes graphical layout constraints of a saved model.

Created July 17,2004 by Denis Dube
"""

from ModelSpecificCode import isObject_Self_Label_Offseting
from ModelSpecificCode import isObject_Scaling_Neutral
from ModelSpecificCode import isObject_Partially_Self_Scaling
from ModelSpecificCode import isEntityNode

def ConstraintLoader( node ):
  
  lcDict = node.graphObject_.layConstraints

  for key in lcDict.keys():
    
    if( key == 'scale' ):
      scaleConstraint( node.graphObject_, lcDict[key]  )
      
    elif( key == 'Text Scale' ):
      textScaleConstraint( node.graphObject_, lcDict[key]  )  
      
    elif( key == 'Label Offset' ):
      labelOffsetConstraint( node.graphObject_, lcDict[key]  )
      
      
def textScaleConstraint( graphObject, scale ):
  """ Scales a graphical entity's text """ 
  
  # Normal objects that we must scale
  if( isObject_Scaling_Neutral( graphObject ) ):
    
    # Entity node
    if( isEntityNode( graphObject ) ): 
      graphObject.ScaleText( scale )
      
    # Link with a center object
    elif( graphObject.centerObject ):
      graphObject.centerObject.layConstraints[ 'Text Scale' ] = scale
      graphObject.centerObject.ScaleText( scale )

    
      
def scaleConstraint( graphObject, scaleSize ):
  """ Scales a graphical entity """ 
  
  # Normal objects that we must scale
  if( isObject_Scaling_Neutral( graphObject ) ):
    
    # Entity node
    if( isEntityNode( graphObject ) ): 
      graphObject.Scale( scaleSize[0], scaleSize[1], moveLinks = False )
      # Make sure scale didn't screw up the the top-left (not supposed to...)
      graphObject.moveTo(graphObject.x, graphObject.y)
      
    # Link with a center object
    elif( graphObject.centerObject ):
      #x, y = graphObject.centerObject.getbbox()[:2] 
      graphObject.centerObject.layConstraints[ 'scale' ] = scaleSize
      graphObject.centerObject.Scale( scaleSize[0], scaleSize[1], 
                                                            moveLinks = False )
      # Make sure scale didn't screw up the the top-left (not supposed to...)
      #graphObject.centerObject.moveTo(x, y)
      
  # Some formalisms can *almost* scale themselves without any help...
  elif( isObject_Partially_Self_Scaling( graphObject ) ):
    graphObject.scaleHack( scaleSize[0], scaleSize[1] )

    
    
def labelOffsetConstraint( graphObject, labelOffset ):
  """ Offset to the label of link or entity """
    
  if( isObject_Self_Label_Offseting (graphObject ) ):
    return
    
  # Entity Label
  if( isEntityNode( graphObject ) ): 
    # Associated graphical forms
    for gf in graphObject.graphForms:	
      
      # Text label
      if( gf.elementType == 'text' ):
        graphObject.dc.move( gf.handler, labelOffset[0], labelOffset[1] )
          
  # Link Label
  elif( graphObject.centerObject ):
    graphObject.centerObject.Move( labelOffset[0], labelOffset[1], 0 )
    