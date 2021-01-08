from tkinter import *
import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# viewer.py constants
window_width = 1000
window_height = 500

root = Tk()

leftFrame = Frame(root, width=0.5 * window_width, height=window_height)

class Viewer(Frame):
    def __init__(self, xbnds=[-100, 100], ybnds=[-100, 100], zbnds=[-100, 100], master=None):
        Frame.__init__(self, master)
        self.master.title("matplot lib in tkinter example")
        self.pack(fill=BOTH, expand=1)
        leftFrame.pack(side=LEFT, expand=True, fill=BOTH)

        self.xMin = xbnds[0]
        self.xMax = xbnds[1]
        self.yMin = ybnds[0]
        self.yMax = ybnds[1]
        self.zMin = zbnds[0]
        self.zMax = zbnds[1]

        self.fig = Figure(figsize=(5, 5))
        self.ax = self.fig.add_subplot(111, projection='3d')
        self.ax.set_xlim3d(self.xMin, self.xMax)
        self.ax.set_ylim3d(self.yMin, self.yMax)
        self.ax.set_zlim3d(self.zMin, self.zMax)
        self.ax.set_xlabel('X', fontsize=10, rotation=0)
        self.ax.set_ylabel('Y', fontsize=10, rotation=0)
        self.ax.set_zlabel('Z', fontsize=10, rotation=0)

        self.plt1 = FigureCanvasTkAgg(self.fig, master=leftFrame)
        self.plt1.get_tk_widget().pack(side=TOP, fill=BOTH, expand=TRUE)
        self.plt1._tkcanvas.pack(side=LEFT, fill=BOTH, expand=True)
        self.plt1.mpl_connect('button_press_event', self.ax._button_press)
        self.plt1.mpl_connect('button_release_event', self.ax._button_release)
        self.plt1.mpl_connect('motion_notify_event', self.ax._on_move)
        print("Starting Window")

    def singlePoint(self, pt, col='g'):
        self.plt1.clf()
        self.ax = self.fig.add_subplot(self.subplt, projection='3d')
        self.ax.set_xlim3d(self.xMin, self.xMax)
        self.ax.set_ylim3d(self.yMin, self.yMax)
        self.ax.set_zlim3d(self.zMin, self.zMax)
        x = pt[0]
        y = pt[1]
        z = pt[2]
        print('x = ' + str(x) + '\t y =' + str(y) + '\t z =' + str(z))
        self.path = self.ax.scatter(x, y, z, color=col)
        self.plt1.draw()
        self.fig.canvas.flush_events()

    def pointsAndPath(self, pts, col):
        x = pts[0]
        y = pts[1]
        z = pts[2]
        print('x = ' + str(x) + '\t y =' + str(y) + '\t z =' + str(z))
        self.path = self.ax.plot(x, y, z, color=col)
        self.plt1.draw()
        self.fig.canvas.flush_events()

