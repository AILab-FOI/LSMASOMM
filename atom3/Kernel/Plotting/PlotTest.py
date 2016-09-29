## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##
# PlotTest.py --- Simple example using Plot.py
#
# Jean-Sébastien  BOLDUC
# Hans Vangheluwe (turned thread into an object, 
#                  allow multiple generator threads)
# last modified: 09/15/02
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

from Plotter import *
from Tkinter import *
from threading import *
from time import sleep  # only to slow down the output
from math import sin, cos, pi

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

class Generator:
  """ This class generates data.

  In our example, each generated data-item is a tuple with three elements.
  """
  def __init__(self, dataSet):
    """ dataSet: DataSet
    """
    self.running = 0         # generate data iff true
    self.dataSet = dataSet   # DataSet object to which data-items are added

  def addDataItems(self):
    self.running = 1

    # Generate 100 data items:
    for i in range(100):
      t = i/25.
      x = cos(2*pi*t)/5
      y = sin(2*pi*t)/5

      # add the data-item to dataSet
      # (this will trigger updating the appropriate trajectory plots in the GUI)
      self.dataSet.append( [t, x, y] )

      sleep(0.1)  # pause to make it look as if some real calculation is
                  # happening (to emulate a real simulator at work)

      # running will be set to 0 by stop() called from another thread
      if not self.running:
        break

  def stop(self):
    self.running = 0

## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

class GeneratorThread(Thread):

  def __init__(self, generatorObject):
    """ generatorObject is a Generator instance. """

    self.theThread = None
    self.generatorObject = generatorObject

  def start(self):
    """ Start generating data-items. """
  
    # if (has been stopped) or (is finished)...
    if self.theThread == None or not(self.theThread.isAlive()):
      # Empty the DataSet
      self.generatorObject.dataSet.clear()  
      # Create the thread
      self.theThread = Thread(target=self.generatorObject.addDataItems)
      # Start the thread 
      self.theThread.start()           
  
  def stop(self):
    """ Stop data-items from being generated. """
  
    self.generatorObject.stop()  # stop the generator
    if self.theThread != None:
      self.theThread.join()  # wait until the thread terminates
      self.theThread = None
  
## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ## ##

if __name__ == "__main__":

  def quit():
    generatorThread1.stop()
    generatorThread2.stop()
    root.quit()
    print "Bye!"

  root = Tk()
  
  # Create a "DataSet" object (contains data):
  # "source" is the name given to the data source
  # "titles" is a tuple containing the names of the available variables.
  RTdata1 = DataSet(source = 'generator1', titles = ('time','x', 'y'))
  RTdata2 = DataSet(source = 'generator2', titles = ('time','z', 'v'))
  
  generator1 = Generator(RTdata1)  # "Generator" object
  generatorThread1 = GeneratorThread(generator1) # generator thread
  generator2 = Generator(RTdata2)  # "Generator" object
  generatorThread2 = GeneratorThread(generator2) # generator thread

  # Create a "GraphFrame" object, passing it the "DataSet"
  # object, and pack it:
  GFrame1 = GraphFrame(root, [RTdata1])
  GFrame1.pack(fill=BOTH, expand=1)
  GFrame2 = GraphFrame(root, [RTdata2])
  GFrame2.pack(fill=BOTH, expand=1)
  
  # Optional: create default trajectories.
  # Parameters are
  #   dataset -- the "DataSet" object
  #   xcol    -- index of the data for the X-axis
  #   ycol    -- index of the data for the Y-axis
  #   style   -- the line style
  #   color   -- the line color
  # See heading of "Plot.py" for the latter parameters.
  GFrame1.graph.addTrajectory(RTdata1, 0, 1, 'lines', 'blue')
  GFrame1.graph.addTrajectory(RTdata1, 0, 2, 'circles', 'red')
  
  # Update textual representation of trajectories:
  GFrame1.update_list()
  
  # Extra buttons:
  Button(root, text='Start1', command=generatorThread1.start).pack(side=LEFT)
  Button(root, text='Stop1', command=generatorThread1.stop).pack(side=LEFT)
  Button(root, text='Start2', command=generatorThread2.start).pack(side=LEFT)
  Button(root, text='Stop2', command=generatorThread2.stop).pack(side=LEFT)
  Button(root, text='Quit', fg="red", command=quit).pack(side=RIGHT)
  
  root.mainloop()


#  if len(argv) > 1:
#    data.readFromFile(argv[-1])
