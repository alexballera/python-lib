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

#%% https://matplotlib.org/stable/users/explain/colors/index.html
X = [1,2,3,4,5,6,7,8]
Y = [3,4,5,3,2,4,5,7]
Z = [1,3,2,5,5,7,4,6]

fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.plot(X, Y, color='b', zorder=1)
ax.plot(X, Z, color='g', zorder=2)

plt.show()

#%%
X = ['A', 'B', 'C', 'D', 'E']
Y = [14, 7 ,18, 9, 10]

fig, ax = plt.subplots(figsize=figsize, layout=layout)
ax.bar(X, Y, color='b', edgecolor='r')

plt.show()
#%% Colormap
# https://matplotlib.org/stable/gallery/color/colormap_reference.html#sphx-glr-gallery-color-colormap-reference-py
arr1 = np.arange(3, 9)
X = []
for i in range(6):
    X.append(arr1)
X = np.array(X)
#%% Imshow
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.imshow.html#matplotlib.pyplot.imshow
fig, ax = plt.subplots(figsize=figsize, layout=layout)

ax.imshow(X, cmap='winter', interpolation='bilinear', extent=(1,10,1,10))
plt.show()
#%%
X = np.array([
    [2,3,4,5,6,9],
    [2,3,4,5,6,7],
    [2,3,11,5,6,7],
    [2,3,4,5,6,7],
    [2,3,4,5,6,7],
    [10,3,4,5,6,7]
])

fig, ax = plt.subplots(figsize=figsize, layout=layout)
# Variar los valores de la matriz y observar
# Variar los parámetros, interpolation, extent, cmap
ax.imshow(X, cmap='winter', interpolation='bilinear', extent=(1,10,1,10))
plt.show()
#%% Diagrama de puntos (polar). Angulo, Radio

r = np.linspace(0, 2, 20)
beta = np.pi*r
beta = np.pi*2*np.random.rand(20)
colors = beta

fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
sc = ax.scatter(beta, r, c=colors, s=100, cmap='hsv')

plt.colorbar(mappable=sc, location='left') # plt o fig es igual

plt.show()