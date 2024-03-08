import numpy as np
import pyqtgraph as pg
import pyqtgraph.opengl as gl

from pyqtgraph.Qt import QtCore

from dynamic.lorenz import Lorenz


class MyWidget(gl.GLViewWidget):
    def __init__(self, sim, p0, t_max):
        super(MyWidget, self).__init__()
        self.show()
        self.setCameraPosition(distance=80)

        g = gl.GLGridItem()
        self.addItem(g)

        self.sim = sim
        self.t_max = t_max
        self.iters = int(self.t_max / sim.dt)
        self.pos = np.zeros((self.iters, 3)) + p0
        self.i = 1

        self.sp = gl.GLScatterPlotItem(pos=self.pos, size=0.25, color=(1.0, 0.0, 0.0, 0.5), pxMode=False)
        self.addItem(self.sp)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.step)
        self.timer.start(1)

    # Do not name it "update", because it conflicts with the class method
    def step(self):
        if self.i < self.iters:
            self.pos[self.i] = self.sim.next_state(self.pos[self.i - 1])
            self.i += 1

            self.sp.setData(pos=self.pos)
            self.orbit(0.1, 0)


# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    app = pg.mkQApp("PyQtGraph example")
    mywidget = MyWidget(Lorenz(), [1, 1, 1], 200)
    app.exec_()
