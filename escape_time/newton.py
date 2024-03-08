import numpy as np
import pylab as pyl
import math as m
import matplotlib as mpl
import time

from utils import limit_boundaries, get_palette

start = time.time()

x = np.linspace(-2, 2, 800)
y = np.linspace(-1.5, 1.5, 600)
# x = np.linspace(-0.03026725, -0.03024936, 800)
# y = np.linspace(-0.00000713, 0.00000627, 600)

xx, yy = np.meshgrid(x, y, indexing='ij')

z = xx + complex(0.0, 1.0) * yy
p = complex(3, 0)
r = complex(1, 0)

img = np.zeros(z.shape)

iters = 150

for i in range(iters):
    # z = limit_boundaries(((p-1)*z**p+1)/(p*z**(p-1)), -1e10, 1e10, -1e10, 1e10)
    z = limit_boundaries(((p - 1) * z ** p + r) / (p * z ** (p - 1)), -1e6, 1e6, -1e6, 1e6)
    img[(abs(z ** p - r) < 0.05) & (img == 0)] = i

end = time.time()

print('Calculation time:', (end - start))

map_f = get_palette()
cmap = mpl.colors.ListedColormap(map_f, name='mymap')
n = mpl.colors.Normalize(vmin=1, vmax=256)
# n = mpl.colors.Normalize()
m = mpl.cm.ScalarMappable(norm=n, cmap=cmap)

# img = imshow(I.T, origin='lower left', aspect=1)
pyl.imshow(m.to_rgba(img.T), origin='lower', aspect=1)

pyl.show()
