import numpy as np
import matplotlib.pyplot as pyl
import math as m
import matplotlib as mpl
import time

from utils import limit_boundaries, get_palette

b_type = 'j1'

start = time.time()

x = np.linspace(-2, 2, 800)
y = np.linspace(-1.5, 1.5, 600)
re = 1.0
im = 0.0

xx, yy = np.meshgrid(x, y, indexing='ij')

z = xx + 1j * yy

# if b_type in ['j1', 'j2', 'j3']:
#	z = xx + 1j*yy
# elif b_type in ['m1', 'm2', 'm3']:
#	a = 1.0
#	b = 0.0
#	z = (xx + a) + (1j * (yy + b))

if b_type == 'j1' or b_type == 'j2':
    c = complex(0.6, 1.1)
elif b_type == 'j3':
    c = complex(0.1, 0.36)
elif b_type in ['m1', 'm2', 'm3']:
    c = z.copy()

if b_type in ['m1', 'm2', 'm3']:
    z += complex(re, im)

img = np.zeros(z.shape)

iters = 150

for i in range(1, iters):
    zt = z.copy()

    if b_type == 'j1':
        cond = np.real(z) >= 0

        zt[cond] = (zt[cond] - 1) * c
        zt[~cond] = (zt[~cond] + 1) * c

    elif b_type == 'j2':
        cond = np.real(z) * np.imag(c) + np.real(c) * np.imag(z) >= 0

        zt[cond] = (zt[cond] - 1) * c
        zt[~cond] = (zt[~cond] + 1) * c

    elif b_type == 'j3':
        cond = np.real(z) >= 0

        zt[cond] = (np.real(zt[cond]) ** 2 - np.imag(zt[cond]) ** 2 - 1) + 1j * (
                    2 * np.real(zt[cond]) * np.imag(zt[cond]))
        zt[~cond] = (np.real(zt[~cond]) ** 2 - np.imag(zt[~cond]) ** 2 - 1 + np.real(c) * np.real(zt[~cond])) + 1j * (
                    2 * np.real(zt[~cond]) * np.imag(zt[~cond]) + np.imag(c) * np.real(zt[~cond]))

    elif b_type == 'm1':
        cond = np.real(z) >= 0

        zt[cond] = (zt[cond] - 1) * c[cond]
        zt[~cond] = (zt[~cond] + 1) * c[~cond]

    elif b_type == 'm2':
        cond = np.real(z) * np.imag(c) + np.real(c) * np.imag(z) >= 0

        zt[cond] = (zt[cond] - 1) * c[cond]
        zt[~cond] = (zt[~cond] + 1) * c[~cond]

    elif b_type == 'm3':
        cond = np.real(z) >= 0

        zt[cond] = (np.real(zt[cond]) ** 2 - np.imag(zt[cond]) ** 2 - 1) + 1j * (
                    2 * np.real(zt[cond]) * np.imag(zt[cond]))
        zt[~cond] = (np.real(zt[~cond]) ** 2 - np.imag(zt[~cond]) ** 2 - 1 + np.real(c[~cond]) * np.real(
            zt[~cond])) + 1j * (2 * np.real(zt[~cond]) * np.imag(zt[~cond]) + np.imag(c[~cond]) * np.real(zt[~cond]))

    z = limit_boundaries(zt, -1e10, 1e10, -1e10, 1e10)
    img[(abs(z) > 2) & (img == 0)] = i

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
