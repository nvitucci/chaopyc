import time, sys
import numpy as np
import pylab as pyl
# import matplotlib as pyl
import math as m

from utils import limit_boundaries


l_limit = -1e50
l_fill = -np.inf
r_limit = 1e50
r_fill = np.inf

colors = ['r', 'g', 'b', 'c', 'm', 'y']

f_cycles = 1000
seed = 0.66
beta = 5

n_values = 500
iters = 200

bif_types = ['bif', 'biflambda', 'bif=sinpi', 'bif+sinpi', 'bifstewart', 'bifmay']

bif_type = 'bif'

if bif_type == 'bif':
	r = np.linspace(1.9, 3.9, n_values)
elif bif_type == 'biflambda':
	r = np.linspace(-2, 4, n_values)
elif bif_type == 'bif=sinpi':
	r = np.linspace(-2.5, 2.5, n_values)
elif bif_type == 'bif+sinpi':
	r = np.linspace(0, 2, n_values)
elif bif_type == 'bifstewart':
	r = np.linspace(0.5, 2, n_values)
elif bif_type == 'bifmay':
	r = np.linspace(-3.5, -0.9, n_values)

y = []

yp = seed * np.ones(n_values)

if bif_type == 'bif':
	for c in range(f_cycles):
		# yp = np.ma.masked_less(yp, n_limit).filled(n_fill)
		# yp = np.ma.masked_greater(yp, p_limit).filled(p_fill)
		yp = limit_boundaries(yp, l_limit, r_limit, l_fill, r_fill)
		yp = yp + r * yp * (1.0 - yp)
elif bif_type == 'biflambda':
	for c in range(f_cycles):
		yp = r * yp * (1 - yp)
elif bif_type == 'bif=sinpi':
	for c in range(f_cycles):
		yp = r * np.sin(np.pi * yp)
elif bif_type == 'bif+sinpi':
	for c in range(f_cycles):
		yp = yp + r * np.sin(np.pi * yp)
elif bif_type == 'bifstewart':
	for c in range(f_cycles):
		yp = r * yp * yp - 1
elif bif_type == 'bifmay':
	for c in range(f_cycles):
		yp = r * yp / ((1 + yp)**beta)

y.append(yp)

if bif_type == 'bif':
	for i in range(iters):
		# yy = y[-1]

		# yy = np.ma.masked_less(yy, n_limit).filled(n_fill)
		# yy = np.ma.masked_greater(yy, p_limit).filled(p_fill)

		yy = limit_boundaries(y[-1], l_limit, r_limit, l_fill, r_fill)
		y.append(yy + r * yy * (1 - yy))
elif bif_type == 'biflambda':
	for i in range(iters):
		y.append(r * y[-1] * (1 - y[-1]))
elif bif_type == 'bif=sinpi':
	for i in range(iters):
		y.append(r * np.sin(np.pi * y[-1]))
elif bif_type == 'bif+sinpi':
	for i in range(iters):
		y.append(y[-1] + r * np.sin(np.pi * y[-1]))
elif bif_type == 'bifstewart':
	for i in range(iters):
		y.append(r * y[-1] * y[-1] - 1)
elif bif_type == 'bifmay':
	for i in range(iters):
		y.append(r * y[-1] / ((1 + y[-1])**beta))

for i, yy in enumerate(y):
	pyl.scatter(r, yy, color=colors[i % len(colors)], s=0.1, marker='.')

if bif_type == 'bif+sinpi':
	pyl.xlim([0, 2])
	pyl.ylim([0, 2])

pyl.show()
