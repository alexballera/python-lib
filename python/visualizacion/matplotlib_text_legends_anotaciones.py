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

ax.plot(X, Y)

fontdict = dict(
            c = 'purple', # color
            family = 'monospace', # {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
            size = 'xx-large', # float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
            style = 'italic', # 	{'normal', 'italic', 'oblique'}
            stretch = 'expanded', # {a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}
            variant = 'small-caps', # {'normal', 'small-caps'}
            weight = 700, # {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}
            )

bbox=dict(
        fc='coral', # facecolor o backgroundColor
        ec='blue', # edgecolor o borde
        alpha=0.8,
        ls='--', # linestyle {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
        lw= 3.0, # linewidth
        fill=True, # por default True, pero False sin relleno
        boxstyle='sawtooth', # square, circle, ellipse, larrow, rarrow, darrow, round, round4, sawtooth, roundtooth
        pad=0.7, # padding
        )


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

bbox=dict(
        fc='coral', # facecolor o backgroundColor
        ec='blue', # edgecolor o borde
        alpha=0.8,
        ls='--', # linestyle {'-', '--', '-.', ':', '', (offset, on-off-seq), ...}
        lw= 3.0, # linewidth
        fill=True, # por default True, pero False sin relleno
        boxstyle='larrow', # square, circle, ellipse, larrow, rarrow, darrow, round, round4, sawtooth, roundtooth
        pad=0.7, # padding
        )

alpha = 20
delta = 32

ax.text(x=5,
        y=5,
        s=fr'Hola Mundo $\alpha = {alpha}, delta = {delta}$', # string o texto
        c = 'purple', # color
        family = 'monospace', # {FONTNAME, 'serif', 'sans-serif', 'cursive', 'fantasy', 'monospace'}
        size = 'xx-large', # float or {'xx-small', 'x-small', 'small', 'medium', 'large', 'x-large', 'xx-large'}
        style = 'italic', # 	{'normal', 'italic', 'oblique'}
        stretch = 'expanded', # {a numeric value in range 0-1000, 'ultra-condensed', 'extra-condensed', 'condensed', 'semi-condensed', 'normal', 'semi-expanded', 'expanded', 'extra-expanded', 'ultra-expanded'}
        variant = 'small-caps', # {'normal', 'small-caps'}
        weight = 1000, # {a numeric value in range 0-1000, 'ultralight', 'light', 'normal', 'regular', 'book', 'medium', 'roman', 'semibold', 'demibold', 'demi', 'bold', 'heavy', 'extra bold', 'black'}
        bbox=bbox
        )

plt.show()

#%% ANOTACIONES
# https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.annotate.html#matplotlib.axes.Axes.annotate

fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.plot(X, Y)

arrowprops=dict(
        width=8,
        headwidth=20,
        headlength=20,
        shrink=0.05,
        facecolor='r',
        edgecolor='blue',
        lw=2,
    )

ax.annotate(
    text=fr'Hola Mundo $\alpha = {alpha}$',
    xy=(3,5),
    xytext=(6,6),
    fontsize=16,
    arrowprops=arrowprops,
)

plt.show()

#%%
fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.plot(X, Y)

arrowprops=dict(
        arrowstyle="fancy",
        facecolor='r',
        edgecolor='blue',
        lw=2,
    )

bbox['boxstyle'] = 'square'

ax.annotate(
    text=fr'Hola Mundo $\alpha = {alpha}$',
    xy=(6,4),
    xytext=(6,3),
    fontsize=16,
    arrowprops=arrowprops,
    bbox=bbox
)

plt.show()