class Lorenz:
    def __init__(self, a=5, b=15, c=1, dt=0.02):
        self.a = a
        self.b = b
        self.c = c
        self.dt = dt

    def next_state(self, pos):
        x, y, z = pos

        xn = x + (-self.a * x * self.dt) + (self.a * y * self.dt)
        yn = y + (self.b * x * self.dt) - (y * self.dt) - (z * x * self.dt)
        zn = z + (-self.c * z * self.dt) + (x * y * self.dt)

        return xn, yn, zn
