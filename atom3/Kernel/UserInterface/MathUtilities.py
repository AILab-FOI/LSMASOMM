"""
MathUtilities.py

All this code is 'stolen' from one place or another and gathered together here
for convenience :D

Created July 21, 2004 by Denis Dube
"""

import math


def findNearestBoxPointToPoint( box, boxCenter, point ):
  """ 
  Finds the nearest point on the box to the point 
  WARNING: bugs... large man eating poisonous killer bugs!!!
  """
  
  x,y = point
  x0,y0,x1,y1 = box
  xDist = abs( x1-x0 )
  yDist = abs( y1-y0 )
  
  # Use top box line
  if(   y < y0 ): closestBoxLine = [ (x0,y0),(x0,y0+yDist) ]
  
  # Use right box line
  elif( x > x1 ): closestBoxLine = [ (x1,y0),(x1,y0+yDist) ]
    
  # Use bottom box line
  elif( y > y1 ): closestBoxLine = [ (x0,y0),(x0+xDist,y0) ]
  
  # Use left box line
  else:           closestBoxLine = [ (x0,y1),(x0+xDist,y1) ]
    
  # Find the nearest line on the box, and the line between the box and the point
  boxLine = line2dFromPoints( closestBoxLine[0],closestBoxLine[1] )
  intersectLine = line2dFromPoints( boxCenter,point )
  
  # Find the interesection point
  intersectPoint = boxLine.intersect( intersectLine )
  return intersectPoint

def getMidpoint2D( p1,p2 ):
  """ Midpoint of 2 points in 2D """ 
  return [ ( p1[0] + p2[0] ) / 2, ( p1[1] + p2[1] ) / 2 ]

def vectorLength2D( v ):
  """ Calculates the length of the 2D vector v """
  return math.sqrt( v[0] * v[0] + v[1] * v[1] ) 

def distance( x0, y0, x1, y1 ):
  """ Distance between points (x0,y0) and (x1,y1) """
  return math.sqrt(abs((x0-x1)*(x0-x1)+(y0-y1)*(y0-y1)))

def dot ( w, v):
  """ Calculates the dot product of two vectors """
  return w[0]*v[0]+w[1]*v[1]

def point2SegmentDistance( px, py, sx0, sy0, sx1, sy1):
  """
  Point = px,py
  Segment = Point 1 (sx0,sy0) and Point 2 (sx1,sy1)
  
  Calculates distance from a point to a segment. Algorithm:
  http://geometryalgorithms.com/Archive/algorithm_0102/algorithm_0102.htm
  """
    
  v = (sx1 - sx0, sy1 - sy0)    # v = s[1]-[s0]
  w = (px - sx0, py - sy0)      # w = P-s[0]
  
  c1 = dot(w,v)
  if ( c1 <= 0 ): return distance(px, py, sx0, sy0)
  #if ( c1 <= 0 ): return fastDistanceApproximation(px - sx0, py - sy0)
    
  c2 = dot(v,v)
  if ( c2 <= c1 ): return distance(px, py, sx1, sy1)
  #if ( c2 <= c1 ): return fastDistanceApproximation(px - sx1, py - sy1)
  
  b = c1 / c2
  Pb = sx0 + b * v[0], sy0 + b * v[1]
  return distance(px, py, Pb[0], Pb[1])
  #return fastDistanceApproximation(px - Pb[0], py - Pb[1])




def line2dFromPoints(P1,P2):
    """
    CODE BORROWED from Civil project, see http://civil.sourceforge.net/
    
    Does like the name says, returns a Ax+By=C type line
    """
    x1, y1 = P1
    x2, y2 = P2
    if y1 != y2:
        M = matrix([[y1]+[-1]+[x1],[y2]+[-1]+[x2]])
        b,c = M.solve()
        return line2d(1,b,c)
    else:
        M = matrix([[x1]+[-1]+[y1],[x2]+[-1]+[y2]])
        a,c = M.solve()
        return line2d(a,1,c)

def fastDistanceApproximation( dx, dy):
  """ 
  Distance = squareroot( dx^2 + dy^2 )
  This gives a close approximation to that value, but at a fraction of the
  computational cost.
  """

  if( dx < 0 ):
      dx = -dx
  if( dy < 0 ):
      dy = -dy
  
  if( dx < dy ):
      min = dx
      max = dy
  else:
      min = dy
      max = dx
      
  min = int(round(min))
  max = int(round(max))
  
  approx = ( max * 1007 ) + ( min * 441 )
  if( max < ( min << 4 )):
      approx -= ( max * 40 )
  
  # add 512 for proper rounding
  return (( approx + 512 ) >> 10 )



        
class line2d: 
    """ CODE BORROWED from Civil project, see http://civil.sourceforge.net/ """ 


    def __init__(self,a,b,c): 
        """line ax+by=c 
        normalize xco to 1, unless it's zero, then normalize yco 
        if a and b are zero, we don't handle the error."""
        
        if a == 0:
            self.xco = 0
            self.yco = 1 
            self.constant = c / b 
        else: 
            self.xco = 1 
            self.yco = b / a 
            self.constant = c / a 

    def intersect (self, them):
        """Intersection of two lines.  We could also do this with the matrix
        class, but this specialized code is already written, and probably faster anyway."""
        # are we parallel? 
        if self.yco == them.yco:
            # we are. We'll give correct answer, more or less
            if self.constant == them.constant:
                return () # same line! should return self instead? 
            else: 
                return ()   # ditto.
        # ok, not parallel .
        if self.xco != 0 and them.xco != 0:  # ok, neither is horizontal.
            Yintersect = (self.constant-them.constant)/(self.yco-them.yco)
            Xintersect = self.constant - self.yco * Yintersect
        elif self.xco == 0: # self horizontal
            Yintersect = self.constant # yco is 1, remember
            Xintersect = them.constant - them.yco*Yintersect
        elif them.xco == 0: # them horizontal
            Yintersect = them.constant
            Xintersect = self.constant - self.yco*Yintersect
        else:
            raise "Invalid lines."

        return (Xintersect, Yintersect)

    def hasPoint (self, P):
        if (self.xco*P[0] + self.yco*P[1]) == self.constant:
            return 1
        else:
            return 0

    def __repr__ (self):
        return "%dx + %dy = %d" % (self.xco, self.yco, self.constant)



class matrix:
    """
    CODE BORROWED from Civil project, see http://civil.sourceforge.net/
    
    Not really full or proper matrix implementation, just
    enough to solve systems of linear equations.

    No doubt it's full of bugs and for that matter spelling errors,
    but it does seem to work for the relevent cases.
    """

    def __init__ (self, input):
        self.m = input
        # input should be a list of lists of floats, all same length
        return

    def positivise (self):
        """make sure first column is all non-negative.
        Otherwise, sort won't do what we want."""
        for row in self.m:
            if row[0] < 0:
                for index in range(len(row)):
                    row[index] = row[index] * -1.0

    def reduceColumn (self):
        self.positivise()
        self.m.sort()
        self.m.reverse()
        if len(self.m) == 1 or self.m[0][0] == 0:
            return self.m   # degenerate case
        for row in range(1, len(self.m)):
            factor = (self.m[row][0])/((self.m[0][0])*1.0) # coerce factor to be a float
            for column in range(len(self.m[row])):
                self.m[row][column] = self.m[row][column]-(self.m[0][column]*factor)
        return 

    def subMatrix (self):
        """self without first row and first column"""
        S = []
        for row in self.m[1:]:
            S.append(row[1:])
        return matrix(S)
    
    def upperTriangular (self):
        """converts to upper triangular form"""
        self.reduceColumn()
        if len(self.m)==2:
            return self
        subMat = self.subMatrix().upperTriangular()
        for index in range(len(subMat.m)):
             self.m[index+1]= ([0] + subMat.m[index])
        return self

    def utToDiag (self):
        """converts upper triangular to diagonal"""
        if len(self.m)==1:
            return self
        for index1 in range(len(self.m)-1,0,-1):
            for index2 in range(index1-1,-1,-1):
                if self.m[index2][index1]==0 or self.m[index1][index1]==0:
                    continue
                factor = ((self.m[index2][index1])/(self.m[index1][index1]*1.0))
                for column in range(len(self.m[index1])):
                    self.m[index2][column] = self.m[index2][column]-(self.m[index1][column]*factor)
        return  # Ta da!

    def normalize (self):
        for row in range(len(self.m)):
            factor = 1.0
            for column in self.m[row]:
                if column != 0:
                    factor = column
                    break
            for column in range(len(self.m[row])):
                self.m[row][column] = self.m[row][column] / ( factor * 1.0) 
        return

    def solve (self):
        self.upperTriangular()
        self.utToDiag()
        self.normalize()
        answer = []
        for index in range(len(self.m)):
            try:
                answer.append(self.m[index][-1]/self.m[index][index]*-1.0)
            except:
                answer.append(0) # divided by 0.
        return answer
            
    def __repr__ (self):
        return `self.m`