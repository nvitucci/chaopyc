import numpy as np


def limit_boundaries(v, l_limit, r_limit, l_fill, r_fill):
    vv = np.ma.masked_less(v, l_limit).filled(l_fill)
    vv = np.ma.masked_greater(vv, r_limit).filled(r_fill)

    return vv


def get_palette():
    palette_f = open('../colormaps/default.map', 'r')
    palette = palette_f.readlines()
    palette_f.close()
    map_s = [p.strip().split() for p in palette[1:-1]]
    return [[float(x[0]) / 255., float(x[1]) / 255., float(x[2]) / 255.] for x in map_s]
