import numpy as np
import pylab as pyl
import matplotlib as mpl
import time

from utils import limit_boundaries, get_palette


def mandel():
    resolution = (800, 600)

    x = np.linspace(-2.5, 1.5, resolution[0])
    y = np.linspace(-1.5, 1.5, resolution[1])

    xx, yy = np.meshgrid(x, y, indexing='ij')

    # z = xx + complex(0.0, 1.0) * yy
    z = complex(0, 0)
    c = xx + complex(0.0, 1.0) * yy
    perturbation = complex(0, 0)

    img = np.zeros(resolution)

    iters = 150

    # First iteration with perturbation
    z = z * z + c + perturbation

    for i in range(1, iters):
        z = limit_boundaries(z * z + c, -1e10, 1e10, -1e10, 1e10)
        img[(abs(z) >= 2) & (img == 0)] = i

    print(np.max(img))

    return img


if __name__ == '__main__':
    start = time.time()

    img = mandel()

    print('Calculation time:', (time.time() - start))

    map_f = get_palette()
    cmap = mpl.colors.ListedColormap(map_f, name='mymap')
    n = mpl.colors.Normalize(vmin=1, vmax=255)
    # n = mpl.colors.Normalize()
    m = mpl.cm.ScalarMappable(norm=n, cmap=cmap)

    # img = imshow(I.T, origin='lower left', aspect=1)
    pyl.imshow(m.to_rgba(img.T), origin='lower', aspect=1)

    pyl.show()
