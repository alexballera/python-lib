#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Visualización con Matplotlib
@author: Alex Ballera
"""
#%%
# Celda 1: Configuración
# %matplotlib widget
import matplotlib.pyplot as plt
import numpy as np
#%% Variables
layout = 'constrained'
figsize = (10,6)
# Datos de ejemplo
X = [1, 2, 3, 4, 5, 6, 7, 8]
Y = [3, 4, 5, 3, 2, 4, 5, 7]

#%%
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.text.html#matplotlib.axes.Axes.text

fig, ax = plt.subplots(figsize=figsize, layout=layout)

fontdict = dict(
            c = 'yellow', # color
            family = 'monospace', # {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
            size = 'xx-large', # float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
            style = 'italic', # 	{'normal', 'italic', 'oblique'}
            stretch = 'expanded', # {a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}
            variant = 'small-caps', # {'normal', 'small-caps'}
            weight = 700, # {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}
            )

bbox=dict(
        fc='blue', # facecolor o backgroundColor
        ec='red', # edgecolor o borde
        alpha=0.8,
        joinstyle='round',
        ls='--', # linestyle {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
        lw= 3.0, # linewidth
        fill=True, # por default True, pero False sin relleno
        boxstyle='round',
        )

ax.plot(X, Y)
ax.text(x=5,
        y=5,
        s='Hola Mundo',
        fontdict=fontdict,
        rotation='vertical',
        alpha=0.8, # transparencia
        bbox=bbox
        )

plt.show()
#%%
fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.plot(X, Y)
ax.text(x=5,
        y=5,
        s='Hola Mundo', # string o texto
        c = 'yellow', # color
        family = 'monospace', # {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
        size = 'xx-large', # float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
        style = 'italic', # 	{'normal', 'italic', 'oblique'}
        stretch = 'expanded', # {a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}
        variant = 'small-caps', # {'normal', 'small-caps'}
        weight = 1000, # {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}
        bbox=bbox
        )

plt.show()