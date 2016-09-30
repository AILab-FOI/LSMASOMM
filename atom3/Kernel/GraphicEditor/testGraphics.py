import unittest
import Tkinter
import Graphics
import Geometry
# python2.2 testGraphics.py -v


def testOperationsLeafGF(tester, operations):    
  for op in operations:
    apply(op[1], op[2])
    tuples = map(None, op[0].xy, op[3])
    for tup in tuples:
      tester.failIf(tup[0] <= tup[1] - tester.e)
      tester.failIf(tup[0] >= tup[1] + tester.e)

class UselessVisitor:
  def __init__(self):
    self.visited = ""

  def visitRectangleGF(self, rectangleGF):
    self.ref = rectangleGF
    self.visited = "RectangleGF"

  def visitOvalGF(self, ovalGF):
    self.ref = ovalGF
    self.visited = "OvalGF"

  def visitPolygonGF(self, polygonGF):
    self.ref = polygonGF
    self.visited = "PolygonGF"

  def visitPolylineGF(self, polylineGF):
    self.ref = polylineGF
    self.visited = "PolylineGF"

  def visitTextGF(self, textGF):
    self.ref = textGF
    self.visited = "TextGF"

  def visitConnectorGF(self, connectorGF):
    self.ref = connectorGF
    self.visited = "ConnectorGF"

  def visitCompositeGF(self, compositeGF):
    self.ref = compositeGF
    self.visited = "CompositeGF"


#verify that GF is an abstract class and cannot be instantiated
class testGF(unittest.TestCase):
  def testNotImplementedGF(self):
    """test failure to instantiate GF"""
    self.assertRaises(NotImplementedError, Graphics.GF)


# tests depend on the internal structure of the GF classes
class testLeafGF(unittest.TestCase):
  root = Tkinter.Tk()
  canvas = Tkinter.Canvas(height = 100, width = 100)
  #epsilon. Tolerated error on operations
  e = 0.00000000001


  def testNotImplementedLeafGF(self):
    """test failure to instantiate LeafGF"""
    self.assertRaises(NotImplementedError, Graphics.LeafGF)


  def testBoundingBoxLeafGF(self):
    """test LeafGF getApproxBoundingBox"""
    #Leaf GFs
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    for gf in leafGFs:
      box = gf.getApproxBoundingBox()
      numPoints = len(gf.xy)/2
      for i in range(numPoints):
        self.failIf(box[0] > round(gf.xy[2*i]))
        self.failIf(box[2] < round(gf.xy[2*i]))
        self.failIf(box[1] > round(gf.xy[2*i+1]))
        self.failIf(box[3] < round(gf.xy[2*i+1]))


  def testSetZoomLeafGF(self):
    """test LeafGF setZoom"""
    #Leaf GFs
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    for gf in leafGFs:
      gf.setZoom(7.2)
      self.assertEqual(gf.zoom, 7.2)


  def testLockSanity(self):
    """test lock sanity LeafGF"""
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    for gf in leafGFs:
      gf.setLock(1)
      self.assertEqual(gf.getLock(), 1)
      gf.setLock(0)
      self.assertEqual(gf.getLock(), 0)


  def testLock(self):
    """test lock LeafGF"""
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    for gf in leafGFs:
      old_xy = gf.xy[:]
      gf.setLock(1)
      gf.translate(2,3)
      self.assertEqual(old_xy, gf.xy)
      gf.setLock(0)
      gf.translate(2,3)
      self.assertNotEqual(old_xy, gf.xy)


  def testSetFillColorSanity(self):
    """test fill color sanity LeafGF"""
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    for gf in leafGFs:
      gf.setFillColor("green")
      self.assertEqual(gf.getFillColor(), "green")

  def testSetOutlineColorSanity(self):
    """test outline color sanity for LeafGFs with outline"""
    leafGFs = [Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None)]
    for gf in leafGFs:
      gf.setOutlineColor("green")
      self.assertEqual(gf.getOutlineColor(), "green")



  def testTranslateLeafGF(self):
    """test LeafGF translate"""
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3, 2.3, 12], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    translations = [(leafGFs[0], leafGFs[0].translate, (3.4, 54.), (4.4, 66.0)),
                    (leafGFs[1], leafGFs[1].translate, (2.4, 4.), (12.4, 24.0)),
                    (leafGFs[2], leafGFs[2].translate, (-2., 33.), (-4.0, 36.0, -68.0, 65.3, 0.3, 45.0)),
                    (leafGFs[3], leafGFs[3].translate, (-2.1, 0.1), (-14.1, 12.33, 63.7, -32.9)),
                    (leafGFs[4], leafGFs[4].translate, (1.,1.), (2.0, 2.0, 13.0, 13.0)),
                    (leafGFs[5], leafGFs[5].translate, (4., 3.0), (6.0, 9.0, 8.8, 9.4))]
    testOperationsLeafGF(self, translations)


  def testRotateLeafGF(self):
    """test LeafGF rotate"""
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3, 2.3, 12], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    rotations = [(leafGFs[0], leafGFs[0].rotate, (0, 0, 90), (-12.0, 1.0)),
                 (leafGFs[1], leafGFs[1].rotate, (0, 0, 180), (-10.0, -20.0)),
                 (leafGFs[2], leafGFs[2].rotate, (0, 0, 0), (-2.0, 3.0, -66.0, 32.3, 2.3, 12)),
                 (leafGFs[3], leafGFs[3].rotate, (0, 0, 270), (12.23, 12.0, -33.0, -65.8)),
                 (leafGFs[4], leafGFs[4].rotate, (0, 0, -90), (1.0, -1.0, 12.0, -12.0)),
                 (leafGFs[5], leafGFs[5].rotate, (0, 0, 90), (-6.0, 2.0, -6.4, 4.8))]

    testOperationsLeafGF(self, rotations)


  def testScaleLeafGF(self):
    """test LeafGF scale"""
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3, 2.3, 12], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    scalings = [(leafGFs[0], leafGFs[0].scale, (0, 0, 0, 0), (0, 0)),
                (leafGFs[1], leafGFs[1].scale, (0, 0, 1.0, 2.0), (10.0, 40.0)),
                (leafGFs[2], leafGFs[2].scale, (0, 0, 2.0, 3.0), (-4.0, 9.0, -132.0, 96.9, 4.6, 36)),
                (leafGFs[3], leafGFs[3].scale, (0, 0, -1.0, 2.0), (12.0, 24.46, -65.8, -66.0)),
                (leafGFs[4], leafGFs[4].scale, (0, 0, 3.0, 3.0), (3.0, 3.0, 36.0, 36.0)),
                (leafGFs[5], leafGFs[5].scale, (0, 0, 0.0, 0.5), (0.0, 3.0, 0.0, 3.2))]
    testOperationsLeafGF(self, scalings)
        

#test accept visitor
  def testAcceptRectangleGF(self):
    """test accept visitor RectangleGF"""
    visitor = UselessVisitor()
    rectangleGF = Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None)
    rectangleGF.accept(visitor)
    self.assertEqual(visitor.visited, "RectangleGF")
    self.failIf(not (visitor.ref is rectangleGF))
    
    
  def testAcceptOvalGF(self):
    """test accept visitor OvalGF"""
    visitor = UselessVisitor()
    ovalGF = Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None)
    ovalGF.accept(visitor)
    self.assertEqual(visitor.visited, "OvalGF")
    self.failIf(not (visitor.ref is ovalGF))


  def testAcceptPolygonGF(self):
    """test accept visitor PolygonGF"""
    visitor = UselessVisitor()
    polygonGF = Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3, 2.3, 12], "black", "blue", 0, 1, 0, self.canvas, 1.0, None)
    polygonGF.accept(visitor)
    self.assertEqual(visitor.visited, "PolygonGF")
    self.failIf(not (visitor.ref is polygonGF))


  def testAcceptPolylineGF(self):
    """test accept visitor PolylineGF"""
    visitor = UselessVisitor()
    polylineGF = Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)
    polylineGF.accept(visitor)
    self.assertEqual(visitor.visited, "PolylineGF")
    self.failIf(not (visitor.ref is polylineGF))


  def testAcceptTextGF(self):
    """test accept visitor TextGF"""
    visitor = UselessVisitor()
    textGF = Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None)
    textGF.accept(visitor)
    self.assertEqual(visitor.visited, "TextGF")
    self.failIf(not (visitor.ref is textGF))


  def testAcceptConnectorGF(self):
    """test accept visitor ConnectorGF"""
    visitor = UselessVisitor()
    connectorGF = Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None)
    connectorGF.accept(visitor)
    self.assertEqual(visitor.visited, "ConnectorGF")
    self.failIf(not (visitor.ref is connectorGF))
               
#test copy return type
  def testCopyTypeRectangleGF(self):
    """test RectangleGF copy return type"""
    rectangleGF = Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None)
    self.failIf(not isinstance(rectangleGF.copy(), Graphics.RectangleGF))


  def testCopyTypeOvalGF(self):
    """test OvalGF copy return type"""
    ovalGF = Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None)
    self.failIf(not isinstance(ovalGF.copy(), Graphics.OvalGF))


  def testCopyTypePolygonGF(self):
    """test PolygonGF copy return type"""
    polygonGF = Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3, 2.3, 12], "black", "blue", 0, 1, 0, self.canvas, 1.0, None)
    self.failIf(not isinstance(polygonGF.copy(), Graphics.PolygonGF))


  def testCopyTypePolylineGF(self):
    """test Polyline copy return type"""
    polylineGF = Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)
    self.failIf(not isinstance(polylineGF.copy(), Graphics.PolylineGF))


  def testCopyTypeTextGF(self):
    """test TextGF copy return type"""
    textGF = Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None)
    self.failIf(not isinstance(textGF.copy(), Graphics.TextGF))


  def testCopyTypeConnectorGF(self):
    """test ConnectorGF copy return type"""
    connectorGF = Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None)
    self.failIf(not isinstance(connectorGF.copy(), Graphics.ConnectorGF))

    
#test validity of the copy 
  def testCopyRectangleGF(self):
    """test RectangleGF copy"""
    gf = Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None)
    gf2 = gf.copy()
    self.assertEqual(gf.xy, gf2.xy)
    self.assertEqual(gf.fill, gf2.fill)
    self.assertEqual(gf.outline, gf2.outline)
    self.assertEqual(gf.width, gf2.width)
    self.assertEqual(gf.isActive, gf2.isActive)
    self.assertEqual(gf.isLocked, gf2.isLocked)
    self.assertEqual(gf.zoom, gf2.zoom)

    
  def testCopyOvalGF(self):
    """test OvalGF copy"""
    gf = Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None)
    gf2 = gf.copy()
    self.assertEqual(gf.xy, gf2.xy)
    self.assertEqual(gf.fill, gf2.fill)
    self.assertEqual(gf.outline, gf2.outline)
    self.assertEqual(gf.width, gf2.width)
    self.assertEqual(gf.isActive, gf2.isActive)
    self.assertEqual(gf.isLocked, gf2.isLocked)
    self.assertEqual(gf.zoom, gf2.zoom)


  def testCopyPolygonGF(self):
    """test PolygonGF copy"""
    gf = Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3, 2.3, 32], "black", "blue", 0, 1, 0, self.canvas, 1.0, None)
    gf2 = gf.copy()
    self.assertEqual(gf.xy, gf2.xy)
    self.assertEqual(gf.fill, gf2.fill)
    self.assertEqual(gf.outline, gf2.outline)
    self.assertEqual(gf.width, gf2.width)
    self.assertEqual(gf.isActive, gf2.isActive)
    self.assertEqual(gf.isLocked, gf2.isLocked)
    self.assertEqual(gf.zoom, gf2.zoom)


  def testCopyPolylineGF(self):
    """test Polyline copy"""
    gf = Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4, 2.3, 32], "black", 0, 1, 0, self.canvas, 1.0, None)
    gf2 = gf.copy()
    self.assertEqual(gf.xy, gf2.xy)
    self.assertEqual(gf.fill, gf2.fill)
    self.assertEqual(gf.width, gf2.width)
    self.assertEqual(gf.isActive, gf2.isActive)
    self.assertEqual(gf.isLocked, gf2.isLocked)
    self.assertEqual(gf.zoom, gf2.zoom)


  def testCopyTextGF(self):
    """test TextGF copy"""
    gf = Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None)
    gf2 = gf.copy()
    self.assertEqual(gf.xy, gf2.xy)
    self.assertEqual(gf.fill, gf2.fill)
    self.assertEqual(gf.textCopy, gf2.textCopy)
    self.assertEqual(gf.isActive, gf2.isActive)
    self.assertEqual(gf.isLocked, gf2.isLocked)
    self.assertEqual(gf.zoom, gf2.zoom)

    
  def testCopyConnectorGF(self):
    """test ConnectorGF copy"""
    gf = Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None)
    gf2 = gf.copy()
    self.assertEqual(gf.xy, gf2.xy)
    self.assertEqual(gf.fill, gf2.fill)
    self.assertEqual(gf.outline, gf2.outline)
    self.assertEqual(gf.width, gf2.width)
    self.assertEqual(gf.isActive, gf2.isActive)
    self.assertEqual(gf.isLocked, gf2.isLocked)
    self.assertEqual(gf.zoom, gf2.zoom)


class testCompositeGF(unittest.TestCase):
  root = Tkinter.Tk()
  canvas = Tkinter.Canvas(height = 100, width = 100)

  #test accept visitor
  def testAcceptCompositeGF(self):
    """test accept visitor CompositeGF"""
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None)]
    visitor = UselessVisitor()
    compositeGF = Graphics.CompositeGF([leafGFs[0], leafGFs[1]], 1, 0, 1.0, None)
    compositeGF.accept(visitor)
    self.assertEqual(visitor.visited, "CompositeGF")
    self.failIf(not (visitor.ref is compositeGF))


  def testLockSanity(self):
    """test lock sanity CompositeGF"""
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    compositeGFs = [Graphics.CompositeGF([leafGFs[0], leafGFs[1]], 1, 0, 1.0, None),
                    Graphics.CompositeGF([leafGFs[1], leafGFs[3]], 1, 0, 1.0, None),
                    Graphics.CompositeGF([leafGFs[1], leafGFs[4]], 1, 0, 1.0, None),
                    Graphics.CompositeGF([leafGFs[3], leafGFs[5]], 1, 0, 1.0, None)]
    for gf in compositeGFs:
      gf.setLock(1)
      self.assertEqual(gf.getLock(), 1)
      gf.setLock(0)
      self.assertEqual(gf.getLock(), 0)


  def testLock(self):
    """test lock sanity CompositeGF"""
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    compositeGFs = [Graphics.CompositeGF([leafGFs[0], leafGFs[1]], 1, 0, 1.0, None),
                    Graphics.CompositeGF([leafGFs[1], leafGFs[3]], 1, 0, 1.0, None),
                    Graphics.CompositeGF([leafGFs[1], leafGFs[4]], 1, 0, 1.0, None),
                    Graphics.CompositeGF([leafGFs[3], leafGFs[5]], 1, 0, 1.0, None)]
    for gf in compositeGFs:
      components = gf.getComponents()
      oldCoordList = []
      for c in components:
        oldCoordList.append(c.xy[:])
      #lock
      gf.setLock(1)
      gf.translate(2,2)
      newCoordList = []
      for c in components:
        newCoordList.append(c.xy[:])
      tuples = map(None, oldCoordList, newCoordList)
      for t in tuples:
        self.assertEqual(t[0], t[1])
      #now unlock
      gf.setLock(0)
      gf.translate(2,2)
      newCoordList = []
      for c in components:
        newCoordList.append(c.xy[:])
      tuples = map(None, oldCoordList, newCoordList)
      for t in tuples:
        self.assertNotEqual(t[0], t[1])


  def testTranslateCompositeGF(self):
    """test CompositeGF translate"""
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3, 2.3, 12], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    compositeGF = Graphics.CompositeGF(leafGFs, 1, 0, 1.0, None)
    components = compositeGF.getComponents()
    oldCoordLists = []
    for c in components:
      oldCoordLists.append(c.xy[:])
    compositeGF.translate(2,2)
    newCoordLists = []
    for c in components:
        newCoordLists.append(c.xy[:])
    listPairs = map(None, oldCoordLists, newCoordLists)
    for p in listPairs:
      coordPair = map(None, p[0], p[1])
      for c in coordPair:
        self.assertEqual(c[0] + 2, c[1])


  def testRotateCompositeGF(self):
    """test CompositeGF rotate"""
    leafGFs = [Graphics.PolygonGF([-2.0, 3.0, -66.0, 32.3, 2.3, 12], "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.OvalGF(-12.0, 12.23, 65.8, -33.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    compositeGF = Graphics.CompositeGF(leafGFs, 1, 0, 1.0, None)
    components = compositeGF.getComponents()
    oldCoordLists = []
    for c in components:
      oldCoordLists.append(c.xy[:])
    compositeGF.rotate(0,0,180)
    newCoordLists = []
    for c in components:
        newCoordLists.append(c.xy[:])
    listPairs = map(None, oldCoordLists, newCoordLists)
    for p in listPairs:
      coordPair = map(None, p[0], p[1])
      for c in coordPair:
        self.assertEqual(-c[0], c[1])


  def testScaleCompositeGF(self):
    """test CompositeGF scale"""
    leafGFs = [Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    compositeGF = Graphics.CompositeGF(leafGFs, 1, 0, 1.0, None)
    components = compositeGF.getComponents()
    oldCoordLists = []
    for c in components:
      oldCoordLists.append(c.xy[:])
    compositeGF.scale(0,0,2,2)
    newCoordLists = []
    for c in components:
        newCoordLists.append(c.xy[:])
    listPairs = map(None, oldCoordLists, newCoordLists)
    for p in listPairs:
      coordPair = map(None, p[0], p[1])
      for c in coordPair:
        self.assertEqual(2*c[0], c[1])


  def testGetComponentsCompositeGF(self):
    """test CompositeGF getComponents"""
    leafGFs = [Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    compositeGF = Graphics.CompositeGF(leafGFs, 1, 0, 1.0, None)
    components = compositeGF.getComponents()
    self.failIf(not components[0] is leafGFs[0])
    self.failIf(not components[1] is leafGFs[1])


  def testBoundingBoxCompositeGF(self):
    """test CompositeGF getApproxBoundingBox"""
    #Leaf GFs
    leafGFs = [Graphics.TextGF(1.0, 12.0, "text", "blue", 1, 0, self.canvas, 1.0, None),
               Graphics.ConnectorGF(10.0, 20.0, "black", "blue", 1, 0, self.canvas, 1.0, None)]
    compositeGF = Graphics.CompositeGF(leafGFs, 1, 0, 1.0, None)
    box = compositeGF.getApproxBoundingBox()
    for gf in leafGFs:
      leafBox = gf.getApproxBoundingBox()
      self.failIf(box[0] > leafBox[0])
      self.failIf(box[2] < leafBox[2])
      self.failIf(box[1] > leafBox[1])
      self.failIf(box[3] < leafBox[3])


  #test copy return type
  def testCopyTypeCompositeGF(self):
    """test CompositeGF copy return type"""
    leafGFs = [Graphics.RectangleGF(1.0, 1.0, 12.0, 12.0, "black", "blue", 0, 1, 0, self.canvas, 1.0, None),
               Graphics.PolylineGF([2.0, 6.0, 4.8, 6.4], "black", 0, 1, 0, self.canvas, 1.0, None)]
    compositeGF = Graphics.CompositeGF(leafGFs, 1, 0, 1.0, None)
    self.failIf(not isinstance(compositeGF.copy(), Graphics.CompositeGF))



class testGeometry(unittest.TestCase):
  rotationTests = [((10.2,30,0,0,0), (10.2,30)),
                   ((10.1,30.0,0,0,90), (-30.0,10.1)),
                   ((10,30,0,0,180), (-10,-30)),
                   ((10,30,0,0,270), (30,-10)),
                   ((10.33,30,5,15,0), (10.33,30)),
                   ((10,30,5,10,90), (-15,15)),
                   ((10,30,5,10,180), (0,-10)),
                   ((10,30,5,10,270), (25,5))]
  
  translationTests = [((1.77,2,0,0), (1.77,2)),
                      ((1,2,1.8,5), (2.8,7))]
  
  scalingTests = [((1,2,0,0,0,0), (0,0)),
                  ((1,2.2,0,0,1,1), (1,2.2)),
                  ((1,2.4,0,0,2,2), (2,4.8)),
                  
                  ((1,2,1,2,0,0), (1,2)),
                  ((1,2,1,2,1,1), (1,2)),
                  ((1,2,1,2,2,2), (1,2)),
                  
                  ((1,2,2,5,0,0), (2,5)),
                  ((1,2,2,5,1,1), (1,2)),
                  ((1,2,2,5,2,2), (0,-1))]
  
  horizontalFlipTests = [((1,2,7),(13,2)),
                         ((1,2,1),(1,2))]
  
  verticalFlipTests = [((1,2,7),(1,12)),
                       ((1,2,2),(1,2))]
  
  def testRotation(self):
    """testing rotation primitive"""
    for t in self.rotationTests:
      point = Geometry.rotate(t[0][0], t[0][1], t[0][2], t[0][3], t[0][4])
      self.assertEqual(point, t[1])


  def testTranslation(self):
    """testing translation primitive"""
    for t in self.translationTests:
      point = Geometry.translate(t[0][0], t[0][1], t[0][2], t[0][3])
      self.assertEqual(point, t[1])

  def testScaling(self):
    """testing scaling primitive"""
    for t in self.scalingTests:
      point = Geometry.scale(t[0][0], t[0][1], t[0][2], t[0][3], t[0][4], t[0][5])
      self.assertEqual(point, t[1])


if __name__ == "__main__":
  unittest.main()
