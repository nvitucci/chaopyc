import numpy as np
import pylab as pyl
import math as m
import matplotlib as mpl
import time

from utils import limit_boundaries, get_palette


def fnzz():
    x = np.linspace(-4., 4., 800)
    y = np.linspace(-3., 3., 600)
    # x = np.linspace(0.0816, 1.1696, 1024)
    # y = np.linspace(-0.9321, -0.1161, 768)

    xx, yy = np.meshgrid(x, y, indexing='ij')

    z = np.cdouble(xx + complex(0.0, 1.0) * yy)
    print(z.dtype)

    img = np.zeros(z.shape)

    iters = 150

    for i in range(iters):
        img[(abs(z) * abs(z) >= 4) & (img == 0)] = i
        # z = limit_boundaries(np.exp(z*z, dtype=np.cdouble), -1e10, 1e10, -1e10, 1e10)

        MINVAL = -1e3
        MAXVAL = 1e3
        z = limit_boundaries(z, MINVAL, MAXVAL, MINVAL, MAXVAL)
        # z1 = limit_boundaries(np.exp(z), MINVAL, MAXVAL, MINVAL, MAXVAL)
        # z2 = limit_boundaries(z * z, MINVAL, MAXVAL, MINVAL, MAXVAL)
        # z = z1 * z2
        z = np.cos(z * z)

    return img


if __name__ == '__main__':
    start = time.time()

    img = fnzz()

    print('Calculation time:', (time.time() - start))

    map_f = get_palette()
    cmap = mpl.colors.ListedColormap(map_f, name='mymap')
    n = mpl.colors.Normalize(vmin=1, vmax=256)
    # n = mpl.colors.Normalize()
    m = mpl.cm.ScalarMappable(norm=n, cmap=cmap)

    # img = imshow(I.T, origin='lower left', aspect=1)
    pyl.imshow(m.to_rgba(img.T), origin='lower', aspect=1)

    pyl.show()
