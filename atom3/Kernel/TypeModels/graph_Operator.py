# _ File: graph_Operator.py__________________________________________________________________________________
#  Graphical LINK for entity Operator, generated by ATOM3
# ______________________________________________________________________________________________________
from graphLink import *
from stickylink import *
from widthXfillXdecoration import *
class graph_Operator(graphLink):

   def __init__(self, xc, yc, semObject = None ):
      self.semObject = semObject
      self.semanticObject = semObject
      from linkEditor import *
      self.le=linkEditor(self,self.semObject, "Operator")
      self.le.FirstLink= stickylink()
      self.le.FirstLink.arrow=ATOM3Boolean()
      self.le.FirstLink.arrow.setValue((' ', 0))
      self.le.FirstLink.arrow.config = 0
      self.le.FirstLink.arrowShape1=ATOM3Integer(0)
      self.le.FirstLink.arrowShape2=ATOM3Integer(0)
      self.le.FirstLink.arrowShape3=ATOM3Integer(0)
      self.le.FirstLink.decoration=ATOM3Appearance()
      self.le.FirstLink.decoration.setValue( ('Operator_1stLink', self.le.FirstLink))
      self.le.FirstSegment= widthXfillXdecoration()
      self.le.FirstSegment.width=ATOM3Integer(1)
      self.le.FirstSegment.fill=ATOM3String('darkgray')
      self.le.FirstSegment.decoration=ATOM3Appearance()
      self.le.FirstSegment.decoration.setValue( ('Operator_1stSegment', self.le.FirstSegment))
      self.le.FirstSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.le.Center=ATOM3Appearance()
      self.le.Center.setValue( ('Operator_Center', self.le))
      self.le.SecondSegment= widthXfillXdecoration()
      self.le.SecondSegment.width=ATOM3Integer(1)
      self.le.SecondSegment.fill=ATOM3String('darkgray')
      self.le.SecondSegment.decoration=ATOM3Appearance()
      self.le.SecondSegment.decoration.setValue( ('Operator_2ndSegment', self.le.SecondSegment))
      self.le.SecondSegment.decoration_Position=ATOM3Enum(['Up', 'Down', 'Middle', 'No decoration'],3,0)
      self.le.SecondLink= stickylink()
      self.le.SecondLink.arrow=ATOM3Boolean()
      self.le.SecondLink.arrow.setValue((' ', 1))
      self.le.SecondLink.arrow.config = 0
      self.le.SecondLink.arrowShape1=ATOM3Integer(6)
      self.le.SecondLink.arrowShape2=ATOM3Integer(10)
      self.le.SecondLink.arrowShape3=ATOM3Integer(6)
      self.le.SecondLink.decoration=ATOM3Appearance()
      self.le.SecondLink.decoration.setValue( ('Operator_2ndLink', self.le.SecondLink))
      self.le.FirstLink.decoration.semObject=self.semObject
      self.le.FirstSegment.decoration.semObject=self.semObject
      self.le.Center.semObject=self.semObject
      self.le.SecondSegment.decoration.semObject=self.semObject
      self.le.SecondLink.decoration.semObject=self.semObject
      graphLink.__init__(self, xc, yc, self.le,semObject)
