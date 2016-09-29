from DataSet import *
from Tkinter import *
import math
import tkFileDialog
import tkMessageBox
import tkSimpleDialog

from sys import argv

plot_colors = ['black', 'blue', 'green', 'red', 'yellow', 'brown',
               'grey', 'cyan', 'magenta']

plot_styles = ['dots', 'lines', 'circles', 'squares', 
               'triangles', 'cross', 'plus']

class Trajectory:
    def __init__(self, graph, dataset, xcol=0, ycol=1, style='lines', 
                 color='black', size=1):
        self.graph = graph
        self.dataset = dataset
        self.xcol = xcol
        self.ycol = ycol
        self.setStyle(style)
        self.color = color
        self.size = size
        self.idlist = []
        self.previous_point = None
        self.dataset.addListener(self)

    def __str__(self):
        return '[' + str(self.dataset) + '] ' + \
            self.dataset.titles[self.xcol] + ' vs ' + \
            self.dataset.titles[self.ycol] + ' in ' + self.color + ' ' + \
            self.style

    def cleanup(self):
        self.dataset.removeListener(self)

    def dataSetExtended(self, elcount=1):
        self.draw(startindex=-elcount)

    def dataSetCleared(self):
        self.clear()

    def reconfigure(self, dataset=None, xcol=None, ycol=None, style=None, 
                    color=None, size=None):
        if dataset is not None:
            self.dataset.removeListener(self)
            self.dataset = dataset
            self.dataset.addListener(self)
        if xcol is not None: self.xcol = xcol
        if ycol is not None: self.ycol = ycol
        if style is not None: self.setStyle(style)
        if color is not None: self.color = color
        if size is not None: self.size = size
        self.clear()
        self.draw()
                    
    def draw(self, startindex=0):
        points = [(d[self.xcol], d[self.ycol]) \
            for d in self.dataset.data[startindex:]]
        if self.graph.recomputeBounds(points):
            return 1
        else:
            for p in points:
                scaled_p = self.graph.scalecoords(p)
                ids = self.drawfunc(scaled_p, color=self.color, size=self.size)
                self.idlist.extend(ids)
                self.previous_point = scaled_p
            return 0

    def clear(self):
        for id in self.idlist:
            self.graph.delete(id)
        self.idlist = []
        self.previous_point = None

    def setStyle(self, style):
        self.style = style
        self.drawfunc = eval('self.draw_' + style)
        
    def draw_lines(self, p, color='black', size=1):
        p0 = self.previous_point
        if p0 is not None:
            id = self.graph.create_line(p0[0], p0[1], p[0], p[1], 
                                        fill=color, width=size)
            return [id]
        else:
            return []

    def draw_circles(self, p, color='black', size=1):
        r = size*2.5
        id = self.graph.create_oval(p[0]-r, p[1]-r, p[0]+r, p[1]+r, 
                                    fill=color, outline='black')
        return [id]

    def draw_dots(self, p, color='black', size=1):
        r = size
        id = self.graph.create_oval(p[0]-r, p[1]-r, p[0]+r, p[1]+r, 
                                    fill=color, outline=color)
        return [id]

    def draw_squares(self, p, color='black', size=1):
        r = size*2.5
        id = self.graph.create_rectangle(p[0]-r, p[1]-r, p[0]+r, p[1]+r,
                                         fill=color, outline='black')
        return [id]
    
    def draw_triangles(self, p, color='black', size=1):
        r = size*5
        id = self.graph.create_polygon(-0.5*r, 0.288675134595*r,
                                       0.5*r, 0.288675134595*r,
                                       0.0*r, -0.577350269189*r, 
                                       fill=color, outline='black')
        self.graph.move(id, p[0], p[1])
        return [id]

    def draw_cross(self, p, color='black', size=1):
        r = size*2.5
        id1 = self.graph.create_line(p[0]-r, p[1]-r, p[0]+r, p[1]+r, 
                                     fill=color)
        id2 = self.graph.create_line(p[0]-r, p[1]+r, p[0]+r, p[1]-r,
                                     fill=color)
        return [id1, id2]

    def draw_plus(self, p, color='black', size=1):
        r = size*2.5
        id1 = self.graph.create_line(p[0]-r, p[1], p[0]+r, p[1], fill=color)
        id2 = self.graph.create_line(p[0], p[1]+r, p[0], p[1]-r, fill=color)
        return [id1, id2]

class Graph(Canvas):
    def __init__(self, master, **keywords):
        Canvas.__init__(self, master, keywords)
        border_w = self.winfo_reqwidth() - int(self.cget('width'))
        border_h = self.winfo_reqheight() - int(self.cget('height'))
        self.border = (border_w, border_h)
        self.bind('<Configure>', self.config_cb)
        self.plotarea_size = [None, None]
        self._setsize()
        self.trajectories = []
        self.boundingBox = None

    def config_cb(self, event):
        new_width = event.width - self.border[0]
        new_height = event.height - self.border[1]
        if new_width == self.width and new_height == self.height: return
        self.configure(width=new_width, height=new_height)
        self._setsize()
        if self.trajectories != []:
	 doScale = 0
	 for traj in self.trajectories:
	  if traj.dataset.data != []:
	   doScale = 1
	   break
         if doScale:
           self._setscale()
        self.clear()
        self.replot()

    def addTrajectory(self, dataset, xcol=0, ycol=1, style='lines', 
                      color='black'):
        traj = Trajectory(self, dataset, 
                          xcol=xcol, ycol=ycol, style=style, color=color)
        self.trajectories.append(traj)
        traj.draw()

    def delTrajectory(self, index):
        self.trajectories[index].clear()
        self.trajectories[index].cleanup()
        del self.trajectories[index]

    def cleanup(self):
        for i in range(len(self.trajectories)):
            self.delTrajectory(i)

    def recomputeBounds(self, points):
        if not points: return 0
        if self.boundingBox is None:
            x1,y1 = points[0]
            x2,y2 = points[0]
        else:
            ((x1,y1),(x2,y2)) = self.boundingBox
        for p in points:
            if p[0] < x1: x1 = p[0]
            if p[0] > x2: x2 = p[0]
            if p[1] < y1: y1 = p[1]
            if p[1] > y2: y2 = p[1]
        if ((x1,y1),(x2,y2)) != self.boundingBox:
            self.boundingBox = ((x1,y1),(x2,y2))
            self.clear()
            self._setscale()
            self.replot()
            return 1
        else:
            return 0
        
    def scalecoords(self, p):
        return (self.scale[0] * p[0] + self.shift[0], 
                self.scale[1] * p[1] + self.shift[1])
    
    def clear(self):
        for trajectory in self.trajectories:
            trajectory.clear()
        self.delete(ALL)
    
    def replot(self):
        self._drawAxes()
        for trajectory in self.trajectories:
            if trajectory.draw(): break
                
    def reset(self):
        self.clear()
        self.boundingBox = None
        for trajectory in self.trajectories:
            if trajectory.draw(): break
            
    def _setsize(self):
        self.width = int(self.cget('width'))
        self.height = int(self.cget('height'))
        self.plotarea_size = (0.97 * self.width, 0.97 * -self.height)
        xo = 0.5 * (self.width - self.plotarea_size[0])
        yo = 0.5 * (self.height - self.plotarea_size[1])
        self.plotarea_origin = (xo, yo)

    def _setscale(self):
        ((x1, y1), (x2, y2)) = self.boundingBox
        if x1 == x2:
            x1 -= 0.5
            x2 += 0.5
        else:
            x1, x2 = self._axislimits(x1, x2)
            self.boundingBox = ((x1,self.boundingBox[0][1]),
                                (x2,self.boundingBox[1][1]))
        if y1 == y2:
            y1 -= 0.5
            y2 += 0.5
        else:
            y1, y2 = self._axislimits(y1, y2)
            self.boundingBox = ((self.boundingBox[0][0],y1),
                                (self.boundingBox[1][0],y2))
        self.xticks = self._ticks(x1, x2)
        self.yticks = self._ticks(y1, y2)

        # compute the axis borders
        text_width = [0., 0.]
        text_height = [0., 0.]
        bb = self._textBoundingBox(self.xticks[0][1])
        text_height[1] = bb[3]-bb[1]
        text_width[0] = 0.5*(bb[2]-bb[0])
        bb = self._textBoundingBox(self.xticks[-1][1])
        text_width[1] = 0.5*(bb[2]-bb[0])
        for y in self.yticks:
            bb = self._textBoundingBox(y[1])
            w = bb[2]-bb[0]
            text_width[0] = max(text_width[0], w)
        h = 0.5*(bb[3]-bb[1])
        text_height[0] = h
        text_height[1] = max(text_height[1], h)

        self.scale = ((self.plotarea_size[0]-text_width[0]-text_width[1]) / \
                      (x2 - x1),
                      (self.plotarea_size[1]+text_height[0]+text_height[1]) / \
                      (y2 - y1))
        self.shift = ((-x1*self.scale[0]) + self.plotarea_origin[0] + \
                      text_width[0],
                      (-y1*self.scale[1]) + self.plotarea_origin[1] - \
                      text_height[1])
                      
    def _axislimits(self, lower, upper):
            range = upper-lower
            if range == 0.:
                return lower-0.5, upper+0.5
            log = math.log10(range)
            power = math.floor(log)
            fraction = log-power
            if fraction <= 0.05:
                power = power-1
            grid = 10.**power
            lower = lower - lower % grid
            mod = upper % grid
            if mod != 0:
                upper = upper - mod + grid
            return lower, upper
        
    def _ticks(self, lower, upper):
        ideal = (upper-lower)/7.
        log = math.log10(ideal)
        power = math.floor(log)
        fraction = log-power
        factor = 1.
        error = fraction
        for f, lf in self._multiples:
            e = math.fabs(fraction-lf)
            if e < error:
                error = e
                factor = f
        grid = factor * 10.**power
        if power > 3 or power < -3:
            format = '%+7.0e'
        elif power >= 0:
            digits = max(1, int(power))
            format = '%' + `digits`+'.0f'
        else:
            digits = -int(power)
            format = '%'+`digits+2`+'.'+`digits`+'f'
        ticks = []
        t = -grid*math.floor(-lower/grid)
        while t <= upper and len(ticks) < 200:
            ticks.append((t, format % (t,)))
            t = t + grid
        return ticks

    _multiples = [(2., math.log10(2.)), (5., math.log10(5.))]

    def _textBoundingBox(self, text):
        bg = self.cget('background')
        item = self.create_text(0., 0., anchor=NW, text=text, fill=bg)
        bb = self.bbox(item)
        self.delete(item)
        return bb

    def _drawAxes(self):
        if self.boundingBox is None: return
        scale = self.scale
        shift = self.shift
        (x1, y1), (x2, y2) = self.boundingBox
        if x1 == x2:
            x1 -= 0.5
            x2 += 0.5
        if y1 == y2:
            y1 -= 0.5
            y2 += 0.5
        lower, upper = x1, x2
        for y, d, text in [(y1, -3, 1), (y2, 3, 0)]:
            p1 = (scale[0]*lower)+shift[0], (scale[1]*y)+shift[1]
            p2 = (scale[0]*upper)+shift[0], (scale[1]*y)+shift[1]
            self.create_line(p1[0], p1[1], p2[0], p2[1], fill='black', width=1)
            for x, label in self.xticks:
                p = (scale[0]*x)+shift[0], (scale[1]*y)+shift[1]
                self.create_line(p[0], p[1], p[0], p[1]+d, \
                                 fill='black', width=1)
                if text:
                    self.create_text(p[0], p[1], 
                                     anchor=N, fill='black', text=label)

        lower, upper = y1, y2
        for x, d, text in [(x1, -3, 1), (x2, 3, 0)]:
            p1 = (scale[0]*x)+shift[0], (scale[1]*lower)+shift[1]
            p2 = (scale[0]*x)+shift[0], (scale[1]*upper)+shift[1]
            self.create_line(p1[0], p1[1], p2[0], p2[1],
                             fill='black', width=1)
            if self.yticks:
                for y, label in self.yticks:
                    p = (scale[0]*x)+shift[0], (scale[1]*y)+shift[1]
                    self.create_line(p[0], p[1], p[0]-d, p[1],
                                     fill='black', width=1)
                    if text:
                        self.create_text(p[0]-2, p[1], 
                                         anchor=E, fill='black', text=label)

class TrajectoryDialog(tkSimpleDialog.Dialog):
    def __init__(self, parent, graph, datasets, trajectory=None):
        self.trajectory = trajectory
        self.graph = graph
        self.datasets = datasets
        tkSimpleDialog.Dialog.__init__(self, parent, "Edit trajectory")

    def body(self, master):
        Label(master, text="Source").grid(row=0, column=0, columnspan=2)
        Label(master, text="X axis").grid(row=3, column=0)
        Label(master, text="Y axis").grid(row=3, column=1)
        Label(master, text="Style").grid(row=5, column=0)
        Label(master, text="Color").grid(row=5, column=1)
        Button(master, text="Other source...", command=self.add_source).\
            grid(row=2, column=0, columnspan=2, sticky=W+E)
        self.sourcelist = Listbox(master, exportselection=0, height=5)
        self.xlist = Listbox(master, exportselection=0)
        self.ylist = Listbox(master, exportselection=0)
        self.stylelist = Listbox(master, exportselection=0)
        self.colorlist = Listbox(master, exportselection=0)
        for dataset in self.datasets:
            self.sourcelist.insert(END, str(dataset))
        if self.trajectory is not None:
            self.sourcelist.activate(
                self.datasets.index(self.trajectory.dataset))
        self.curr_source = self.sourcelist.index(ACTIVE)
        self.update_lists()
        for style in plot_styles:
            self.stylelist.insert(END, style)
        for color in plot_colors:
            self.colorlist.insert(END, color)
        self.sourcelist.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.xlist.grid(row=4, column=0)
        self.ylist.grid(row=4, column=1)
        self.stylelist.grid(row=6, column=0)
        self.colorlist.grid(row=6, column=1)
        if self.trajectory is not None:
            self.xlist.activate(self.trajectory.xcol)
            self.ylist.activate(self.trajectory.ycol)
            self.stylelist.activate(plot_styles.index(self.trajectory.style))
            self.colorlist.activate(plot_colors.index(self.trajectory.color))
        self.xlist.select_set(ACTIVE)
        self.ylist.select_set(ACTIVE)
        self.stylelist.select_set(ACTIVE)
        self.colorlist.select_set(ACTIVE)
        self.poll_sourcelist()
        return self.sourcelist

    def apply(self):
        source = self.datasets[self.sourcelist.index(ACTIVE)]
        xcol = self.xlist.index(ACTIVE)
        ycol = self.ylist.index(ACTIVE)
        style = self.stylelist.get(ACTIVE)
        color = self.colorlist.get(ACTIVE)
        if self.trajectory is None:
            self.graph.addTrajectory(source, xcol=xcol, ycol=ycol, style=style,
                                     color=color)
        else:
            self.trajectory.reconfigure(dataset=source, xcol=xcol, ycol=ycol,
                                        style=style, color=color)
        
    def update_lists(self):
        self.xlist.delete(0, END)
        self.ylist.delete(0, END)
        source = self.datasets[self.curr_source]
        for title in source.titles:
            self.xlist.insert(END, title)
            self.ylist.insert(END, title)
    
    def poll_sourcelist(self):
        now = self.sourcelist.index(ACTIVE)
        if now != self.curr_source:
            self.curr_source = now
            self.update_lists()
        self.after(250, self.poll_sourcelist)
        
    def add_source(self):
        filename = tkFileDialog.askopenfilename()
        if filename:
            dataset = DataSet()
            dataset.readFromFile(filename)
            self.datasets.append(dataset)
            self.sourcelist.insert(END, str(dataset))
        
class GraphFrame(Frame):

    def __init__(self, parent, datasets=[]):
        Frame.__init__(self, parent)
        self.datasets = datasets
        self.graph = Graph(self, background='white')
        self.graph.pack(fill=BOTH, expand=1)
        self.trajlist = Listbox(self, height=5)
        self.trajlist.pack(fill=X)
        Button(self, text="New", command=self.new_traj).pack(side=LEFT)
        Button(self, text="Edit", command=self.edit_traj).pack(side=LEFT)
        Button(self, text="Delete", command=self.delete_traj).pack(side=LEFT)
        Button(self, text="Replot", command=self.graph.reset).\
            pack(side=LEFT)
        Button(self, text="Postscript print", command=self.genPostscript).\
            pack(side=LEFT)
        self.update_list()

    def genPostscript(self):
      """ Generate a Postscript file. """
      filename = tkFileDialog.asksaveasfilename()
      if filename:
        postscript = self.graph.postscript()
        fd = open(filename, 'w')
        fd.write(postscript)
        fd.close
    
    def edit_traj(self, trajectory=None):
        active_idx = self.trajlist.index(ACTIVE)
        if not trajectory:
            trajectory = self.graph.trajectories[active_idx]
        TrajectoryDialog(self, self.graph, self.datasets, trajectory=trajectory)
        self.trajlist.delete(ACTIVE)
        self.trajlist.insert(active_idx, str(trajectory))
        self.trajlist.activate(active_idx)
        self.trajlist.select_set(ACTIVE)

    def delete_traj(self):
        if self.graph.trajectories:
            self.graph.delTrajectory(self.trajlist.index(ACTIVE))
            self.trajlist.delete(ACTIVE)

    def new_traj(self):
        TrajectoryDialog(self, self.graph, self.datasets)
        self.update_list()

    def clear(self):
        self.graph.clear()
        self.update_list()
        
    def update_list(self):
        self.trajlist.delete(0, END)
        for trajectory in self.graph.trajectories:
            self.trajlist.insert(END, str(trajectory))
            
class GraphWindow(Toplevel):
    
    def __init__(self, parent, datasets=[]):
        Toplevel.__init__(self, parent)
        self.graph_frame = GraphFrame(self, datasets)
        Button(self.graph_frame, text="Close", fg="red",
	       command=self.windowClosing).pack(side=RIGHT)
        self.graph_frame.pack(fill=BOTH, expand=1)
        self.protocol("WM_DELETE_WINDOW", self.windowClosing)

    def windowClosing(self):
        self.graph_frame.graph.cleanup()
        self.destroy()

if __name__ == '__main__':

  root = Tk()
  data = DataSet()

  GF = GraphFrame(root, [data])
  GF.pack(fill=BOTH, expand=1)

  Button(root, text='Clear', command=GF.graph.clear).pack(side=LEFT)
  Button(root, text='Redraw', command=GF.graph.replot).pack(side=LEFT)
  Button(root, text='Quit',   command=root.quit).pack(side=RIGHT)

  if len(argv) > 1:
    data.readFromFile(argv[-1])

  root.mainloop()
