import numpy as np

from vispy import app, scene

from dynamic.lorenz import Lorenz


class MyWidget:
    def __init__(self, sim, p0, t_max):
        canvas = scene.SceneCanvas(keys='interactive', show=True)
        grid = canvas.central_widget.add_grid(spacing=0)

        view = grid.add_view(row=0, col=1, camera='panzoom')
        view.camera = 'turntable'

        self.sim = sim
        self.t_max = t_max
        self.iters = int(self.t_max / sim.dt)
        self.pos = np.zeros((self.iters, 3)) + p0
        self.i = 1

        self.scatter = scene.visuals.Markers()
        self.scatter.set_data(self.pos, edge_width=0, face_color=(1.0, 0.0, 0.0, 0.5), size=1)

        view.add(self.scatter)

        timer = app.Timer()
        timer.connect(self.step)
        timer.start()

        app.run()

    def step(self, ev):
        if self.i < self.iters:
            self.pos[self.i] = self.sim.next_state(self.pos[self.i - 1])
            self.i += 1
            self.scatter.set_data(pos=self.pos)


# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    MyWidget(Lorenz(), [1, 1, 1], 200)
